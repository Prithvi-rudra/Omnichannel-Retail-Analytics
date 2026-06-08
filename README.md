# Omnichannel Retail Sales and Inventory Analytics Dashboard

## Project Overview
This project analyzes omnichannel retail sales data to extract actionable business insights. The objective was to perform data cleaning, key metric aggregation, and advanced data visualization to understand corporate performance.

## Live Dashboard
**Tableau Public Dashboard:** https://public.tableau.com/views/Omnichannel_Sales_Performance_Dashboard/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

The project explicitly highlights:
- Overall sales performance and peak seasonal trends
- Product line revenue distribution
- Regional revenue trends
- High-density customer purchasing behavior by day of the week

---

## Tools & Technologies Used
- **Database Querying:** SQL (Data cleaning, date partitioning, metric calculations)
- **Business Intelligence:** Tableau Public (Dashboard architecture, global multi-select filters, continuous time-series modeling)
- **Documentation:** Git, GitHub, & Markdown

---

## Dataset Features
The dataset tracks over **$1.03M** in total sales revenue across multiple attributes:
- Order Details & Order Dates
- Product Categories
- Geographical Regions
- Total Sales Figures

---

## Data Cleaning & Aggregation Process
The following foundational steps were performed:
- Handled missing data values and validated data types
- Grouped chronological order transactions into distinct Month and Day Name categories
- Aggregated financial fields to ensure accurate sub-totals across regions and product lines

---

## Executive KPI Analysis
The following core metrics were established across the entire dataset:
- **Total Revenue:** $1,033,730
- **Average Order Value:** $5,168.65
- **Best Selling Product:** Monitor ($228,651)
- **Best Performing Region:** West

---

## 📊 Week 3 & 4: Interactive Dashboard Architecture & Strategic Insights
I transitioned the foundational data insights into a responsive executive dashboard using Tableau Public to isolate core traffic zones and operational inefficiencies.

### Key Visualizations Built:
* **Product Performance Bar Chart:** Highlights revenue distribution across core product lines, establishing **Monitors** as the primary driver ($228,651) and **Laptops** as an underperformer ($92,032).
* **Continuous Sales Trend Line:** Mapped out an unbroken timeline showcasing an explosive annual sales peak in **Month 3 (March)** reaching **$263,255**, followed by a seasonal contraction in April and May.
* **Peak Day Analysis Heatmap:** Created a dynamic matrix layout utilizing `Day Name` and `Product` dimensions. This isolated a massive volume spike for **Tablets on Saturdays, hitting the dataset's single-cell transaction ceiling of $50,928**.
* **Global Slicers:** Engineered interactive multi-select filters for **Region** and **Month Name** linked globally across the entire data source (`All Using This Data Source`).

### Strategic Business Recommendations:
* **Inventory Optimization:** Ramp up supply chain procurement cycles in late January and February to prevent stockout bottlenecks ahead of the proven March sales surge.
* **Capital Efficiency:** Scale back digital marketing ad spend during April and May to maximize margin efficiency during the natural seasonal slowdown.
* **Product Bundling:** Package slow-moving laptop inventory into promotional accessory bundles (e.g., Monitor + Laptop combinations) to accelerate stagnant stock clear-outs.

---

## 🖥️ Interactive Dashboard Preview
![Omnichannel Dashboard Layout](omnichannel_dashboard_layout.jpeg)
![Peak Day Heatmap Matrix](peak_analysis_heatmap.jpeg)
![Sales Trend Analysis](sales_trend Line Chart.jpeg)
![Product Performance Analysis](product_performance Bar Chart.jpeg)

---

## Project Structure
Omnichannel-Retail-Analytics/
│
├── SQL_Scripts/
├── Tableau_Workbook/
├── images/
└── README.md
