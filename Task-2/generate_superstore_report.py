import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from datetime import datetime
import os


# -------------------------------------------------
# LOAD DATA (Handle Encoding Safely)
# -------------------------------------------------
# Try reading with utf-8 first (standard), but fallback to latin1 if special characters cause errors.
# This prevents the script from crashing due to encoding issues common in older CSV files.
try:
    df = pd.read_csv("Superstore.csv", encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv("Superstore.csv", encoding="latin1")

# Clean column names by removing leading/trailing whitespace to ensure consistent access later
df.columns = df.columns.str.strip()


# -------------------------------------------------
# DATA ANALYSIS
# -------------------------------------------------
# Calculate key high-level metrics (KPIs) for the report
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique() # Count unique orders, not just line items

# Identify top performers to highlight in the executive summary
# idxmax() returns the index (category/region name) associated with the maximum value
top_category = df.groupby("Category")["Sales"].sum().idxmax()
top_region = df.groupby("Region")["Sales"].sum().idxmax()

# Prepare data for visualization: Aggregate sales by category and sort descending
sales_by_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)


# -------------------------------------------------
# CREATE CHART (Matplotlib)
# -------------------------------------------------
# Create a bar chart to visually represent sales performance by category
plt.figure(figsize=(6, 4))
sales_by_category.plot(kind="bar", color="steelblue")
plt.title("Sales by Category")
plt.ylabel("Total Sales")
plt.tight_layout() # Adjust layout to prevent labels from being cut off

# Save the chart temporarily as an image file so it can be inserted into the PDF later
chart_path = "category_chart.png"
plt.savefig(chart_path)
plt.close() # Close plot to free up memory


# -------------------------------------------------
# CREATE PDF DOCUMENT SETUP
# -------------------------------------------------
# Initialize the PDF document with A4 page size
pdf = SimpleDocTemplate(
    "Superstore_Report.pdf",
    pagesize=A4
)

# 'elements' list will hold all PDF content (paragraphs, tables, images) in sequential order
elements = []

# Load default stylesheets for standard formatting (Heading1, Normal, etc.)
styles = getSampleStyleSheet()
title_style = styles["Heading1"]
section_style = styles["Heading2"]
normal_style = styles["Normal"]


# -------------------------------------------------
# TITLE & HEADER
# -------------------------------------------------
# Add the main report title
elements.append(Paragraph("Superstore Business Performance Report", title_style))
elements.append(Spacer(1, 0.3 * inch)) # Add vertical space

# Add timestamp to show when the report was generated
elements.append(
    Paragraph(
        f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        normal_style
    )
)
elements.append(Spacer(1, 0.4 * inch))


# -------------------------------------------------
# EXECUTIVE SUMMARY SECTION
# -------------------------------------------------
elements.append(Paragraph("Executive Summary", section_style))
elements.append(Spacer(1, 0.2 * inch))

# Add bullet points for high-level metrics using f-strings for currency formatting
elements.append(Paragraph(f"• Total Sales: ${total_sales:,.2f}", normal_style))
elements.append(Paragraph(f"• Total Profit: ${total_profit:,.2f}", normal_style))
elements.append(Paragraph(f"• Total Orders: {total_orders}", normal_style))
elements.append(Paragraph(f"• Top Performing Category: {top_category}", normal_style))
elements.append(Paragraph(f"• Top Region: {top_region}", normal_style))

elements.append(Spacer(1, 0.5 * inch))


# -------------------------------------------------
# DATA TABLE SECTION
# -------------------------------------------------
elements.append(Paragraph("Sample Data (Top 5 Records)", section_style))
elements.append(Spacer(1, 0.2 * inch))

# Select specific columns to display to ensure the table fits within A4 width limits
sample_df = df[[
    "Order ID",
    "Category",
    "Sub-Category",
    "Sales",
    "Profit"
]].head()

# Convert DataFrame to a list of lists (required format for ReportLab Table)
# First row is headers, followed by data rows
table_data = [sample_df.columns.tolist()] + sample_df.values.tolist()

# Create Table object
table = Table(table_data, repeatRows=1) # repeatRows=1 ensures header repeats if table spans pages

# Apply styling to the table for better readability
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue), # Header background
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke), # Header text color
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),            # Center align all text
    ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),     # Add grid lines
    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),   # Data row background
]))

elements.append(table)
elements.append(Spacer(1, 0.6 * inch))


# -------------------------------------------------
# CHART IMAGE SECTION
# -------------------------------------------------
elements.append(Paragraph("Sales Distribution by Category", section_style))
elements.append(Spacer(1, 0.2 * inch))

# Load the chart image we saved earlier
img = Image(chart_path)

# Calculate available width on the page (Page width - margins)
# Assuming 1 inch margin on both sides (standard default)
available_width = A4[0] - 2 * inch

# Calculate aspect ratio to resize image proportionally without distortion
aspect = img.imageHeight / float(img.imageWidth)

# Set image dimensions to fit the page width perfectly
img.drawWidth = available_width
img.drawHeight = available_width * aspect

elements.append(img)


# -------------------------------------------------
# BUILD PDF
# -------------------------------------------------
# Generate the final PDF file from the list of elements
pdf.build(elements)

# Clean up: Remove the temporary chart image file to keep the directory clean
if os.path.exists(chart_path):
    os.remove(chart_path)

print("✅ Superstore_Report.pdf generated successfully!")