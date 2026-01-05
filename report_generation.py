"""
Report Generation Module
Generates comprehensive sales analysis reports
"""

from datetime import datetime

def generate_report(sales_data, revenue_analysis, region_performance, 
                   top_products, customer_analysis, daily_trends, 
                   low_performers, enriched_data):
    """
    Generate comprehensive sales analysis report
    Returns: Formatted report string
    """
    report = ""
    
    # Header
    report += "="*70 + "\n"
    report += "SALES ANALYTICS SYSTEM - COMPREHENSIVE REPORT".center(70) + "\n"
    report += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}".center(70) + "\n"
    report += "="*70 + "\n\n"
    
    # Executive Summary
    report += "1. EXECUTIVE SUMMARY\n"
    report += "-" * 70 + "\n"
    report += f"Total Transactions: {revenue_analysis.get('count', 0)}\n"
    report += f"Total Revenue: ${revenue_analysis.get('total_revenue', 0):,.2f}\n"
    report += f"Average Transaction Value: ${revenue_analysis.get('avg_transaction', 0):,.2f}\n"
    report += "\n"
    
    # Region Performance
    report += "2. REGION PERFORMANCE\n"
    report += "-" * 70 + "\n"
    if region_performance:
        for region, stats in sorted(region_performance.items(), 
                                   key=lambda x: x[1]['revenue'], reverse=True):
            report += f"\n{region}:\n"
            report += f"  Revenue: ${stats['revenue']:,.2f}\n"
            report += f"  Transactions: {stats['count']}\n"
            report += f"  Avg Transaction: ${stats['avg_transaction']:,.2f}\n"
    report += "\n"
    
    # Top Products
    report += "3. TOP SELLING PRODUCTS\n"
    report += "-" * 70 + "\n"
    if top_products:
        for rank, (product, count) in enumerate(top_products, 1):
            report += f"{rank}. {product}: {count} transactions\n"
    report += "\n"
    
    # Top Customers
    report += "4. TOP CUSTOMERS\n"
    report += "-" * 70 + "\n"
    if customer_analysis:
        for rank, (customer, trans_count, total_spent) in enumerate(customer_analysis[:10], 1):
            report += f"{rank}. {customer}: {trans_count} purchases, Total: ${total_spent:,.2f}\n"
    report += "\n"
    
    # Daily Trends
    report += "5. DAILY SALES TRENDS\n"
    report += "-" * 70 + "\n"
    if daily_trends:
        peak_day = max(daily_trends.items(), 
                      key=lambda x: x[1]['revenue'])
        lowest_day = min(daily_trends.items(), 
                        key=lambda x: x[1]['revenue'])
        
        report += f"Peak Sales Day: {peak_day[0]}\n"
        report += f"  Revenue: ${peak_day[1]['revenue']:,.2f}\n"
        report += f"  Transactions: {peak_day[1]['count']}\n\n"
        
        report += f"Lowest Sales Day: {lowest_day[0]}\n"
        report += f"  Revenue: ${lowest_day[1]['revenue']:,.2f}\n"
        report += f"  Transactions: {lowest_day[1]['count']}\n"
    report += "\n"
    
    # Low Performers
    report += "6. LOW PERFORMING PRODUCTS\n"
    report += "-" * 70 + "\n"
    if low_performers:
        for product in low_performers[:5]:
            report += f"\n{product['product']}:\n"
            report += f"  Total Revenue: ${product['revenue']:,.2f}\n"
            report += f"  Transaction Count: {product['count']}\n"
    else:
        report += "No low performing products identified\n"
    report += "\n"
    
    # Data Quality
    report += "7. DATA ENRICHMENT SUMMARY\n"
    report += "-" * 70 + "\n"
    if enriched_data:
        enriched_count = len(enriched_data)
        report += f"Total Enriched Records: {enriched_count}\n"
        report += f"Enrichment Rate: {(enriched_count/len(sales_data)*100):.1f}%\n"
    report += "\n"
    
    # Footer
    report += "="*70 + "\n"
    report += "END OF REPORT".center(70) + "\n"
    report += "="*70 + "\n"
    
    return report

def save_report(report, filename='sales_report.txt'):
    """
    Save report to file
    Args:
        report: Report string
        filename: Output filename
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report)
        return True
    except Exception as e:
        print(f"Error saving report: {e}")
        return False
