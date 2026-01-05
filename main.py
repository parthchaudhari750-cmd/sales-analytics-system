#!/usr/bin/env python3
"""
Sales Analytics System - Main Application
Analyzes e-commerce sales data with API integration
"""

import sys
from util import load_sales_data, get_unique_values
from analysis import (
    analyze_sales,
    get_top_products,
    get_region_performance,
    get_customer_analysis,
    get_daily_trends,
    get_low_performers
)
from api_integration import fetch_products, create_product_mapping, enrich_sales_data
from report_generation import generate_report

def display_menu():
    """Display main menu options"""
    print("\n" + "="*50)
    print("Sales Analytics System")
    print("="*50)
    print("\nData Filtering Options:")
    print("1. Filter by Region")
    print("2. Filter by Transaction Amount")
    print("3. No Filter (Analyze All Data)")
    print()

def get_filter_choice():
    """Get user's filter preference"""
    while True:
        try:
            choice = input("Select filtering option (1-3): ").strip()
            if choice in ['1', '2', '3']:
                return choice
            print("Invalid choice. Please enter 1, 2, or 3.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            sys.exit(0)
        except Exception as e:
            print(f"Error reading input: {e}")

def filter_by_region(data):
    """Filter data by selected region"""
    regions = get_unique_values(data, 'region')
    print("\nAvailable Regions:")
    for i, region in enumerate(regions, 1):
        print(f"{i}. {region}")
    
    while True:
        try:
            choice = int(input(f"Select region (1-{len(regions)}): "))
            if 1 <= choice <= len(regions):
                selected_region = regions[choice - 1]
                filtered = [row for row in data if row.get('region') == selected_region]
                print(f"\nFiltered {len(filtered)} records for region: {selected_region}")
                return filtered
            print(f"Invalid choice. Please enter 1-{len(regions)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"Error: {e}")

def filter_by_amount(data):
    """Filter data by transaction amount range"""
    try:
        min_amount = float(input("Enter minimum transaction amount: "))
        max_amount = float(input("Enter maximum transaction amount: "))
        
        filtered = [row for row in data 
                   if min_amount <= float(row.get('amount', 0)) <= max_amount]
        print(f"\nFiltered {len(filtered)} records between ${min_amount} and ${max_amount}")
        return filtered
    except ValueError:
        print("Invalid amount. Please enter numeric values.")
        return data
    except Exception as e:
        print(f"Error: {e}")
        return data

def main():
    """Main application workflow"""
    try:
        print("\nLoading sales data...")
        sales_data = load_sales_data()
        
        if not sales_data:
            print("Error: No sales data loaded.")
            return
        
        print(f"Successfully loaded {len(sales_data)} sales records.")
        
        # Display menu and get filter choice
        display_menu()
        filter_choice = get_filter_choice()
        
        # Apply filter
        if filter_choice == '1':
            filtered_data = filter_by_region(sales_data)
        elif filter_choice == '2':
            filtered_data = filter_by_amount(sales_data)
        else:
            filtered_data = sales_data
        
        if not filtered_data:
            print("No data matching your criteria.")
            return
        
        # Perform analysis
        print("\nPerforming analysis...")
        
        # Get all analysis results
        revenue_analysis = analyze_sales(filtered_data)
        top_products = get_top_products(filtered_data)
        region_performance = get_region_performance(filtered_data)
        customer_analysis = get_customer_analysis(filtered_data)
        daily_trends = get_daily_trends(filtered_data)
        low_performers = get_low_performers(filtered_data)
        
        # Fetch and enrich data with API
        print("\nFetching product data from API...")
        products = fetch_products()
        product_mapping = create_product_mapping(products)
        enriched_data = enrich_sales_data(filtered_data, product_mapping)
        
        # Generate report
        print("Generating comprehensive report...")
        report = generate_report(
            filtered_data,
            revenue_analysis,
            region_performance,
            top_products,
            customer_analysis,
            daily_trends,
            low_performers,
            enriched_data
        )
        
        # Display and save report
        print("\n" + report)
        
        # Save enriched data and report
        import os
        os.makedirs('output', exist_ok=True)
        
        # Save enriched data
        enriched_file = 'output/enriched_sales_data.csv'
        with open(enriched_file, 'w', encoding='utf-8') as f:
            if enriched_data:
                f.write(','.join(enriched_data[0].keys()) + '\n')
                for row in enriched_data:
                    f.write(','.join(str(v) for v in row.values()) + '\n')
        print(f"\nEnriched data saved to: {enriched_file}")
        
        # Save report
        report_file = 'output/sales_report.txt'
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Report saved to: {report_file}")
        
        print("\n" + "="*50)
        print("Analysis Complete!")
        print("="*50)
        
    except Exception as e:
        print(f"\nError in main application: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
