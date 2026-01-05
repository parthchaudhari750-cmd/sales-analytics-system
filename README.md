# Sales Analytics System

A comprehensive Python application for analyzing e-commerce sales data with API integration.

## Features
- Read and clean sales transaction data
- Regional and product performance analysis
- Customer insights and trends
- Real-time product data enrichment via DummyJSON API
- Comprehensive report generation

## Installation

1. Clone the repository:
```bash
git clone https://github.com/parthchaudhari750-cmd/sales-analytics-system.git
cd sales-analytics-system
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the main application:
```bash
python main.py
```

The application will:
1. Read and validate sales data
2. Show available filters (regions, transaction amounts)
3. Allow you to filter data
4. Perform comprehensive analysis
5. Fetch product data from API
6. Enrich sales data with API information
7. Generate a detailed report
8. Save enriched data and report to output/

## Project Structure

```
sales-analytics-system/
├── main.py                          # Main entry point
├── requirements.txt                 # Dependencies
├── README.md                        # This file
├── utils/
│   ├── __init__.py                 # Package initializer
│   ├── file_handler.py             # File I/O operations
│   ├── data_processor.py           # Data analysis functions
│   └── api_handler.py              # API integration
├── data/
│   └── sales_data.txt              # Input sales data
└── output/
    ├── sales_report.txt            # Generated report
    └── enriched_sales_data.txt     # Enriched transactions
```

## Features Implemented

### Part 1: File Handling & Preprocessing (30 points)
- Read sales data with encoding handling
- Parse and clean transactions
- Validate and filter data

### Part 2: Data Processing (25 points)
- Calculate total revenue
- Region-wise sales analysis
- Top selling products
- Customer purchase analysis
- Daily sales trends
- Peak sales day identification
- Low performing products

### Part 3: API Integration (20 points)
- Fetch products from DummyJSON API
- Create product mapping
- Enrich sales data with API information
- Save enriched data to file

### Part 4: Report Generation (15 points)
- Generate comprehensive formatted text report
- 8 sections: Header, Overall Summary, Region Performance, Top Products, Top Customers, Daily Trends, Product Analysis, API Enrichment
- Professional formatting and alignment

### Part 5: Main Application (10 points)
- Complete workflow execution
- User interaction for data filtering
- Error handling and user-friendly messages
- Console output formatting

## Total Points: 100

## Requirements
- Python 3.6+
- requests library (for API calls)

## Author
Parth Chaudhari

## License
MIT License
