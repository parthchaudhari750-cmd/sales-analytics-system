"""
Data Analysis Module
Provides functions for sales data analysis
"""

from collections import defaultdict
from datetime import datetime

def analyze_sales(data):
    """
    Perform basic sales analysis
    Returns: dict with total revenue, average transaction, count
    """
    if not data:
        return {'total_revenue': 0, 'avg_transaction': 0, 'count': 0}
    
    total_revenue = sum(float(row.get('amount', 0)) for row in data)
    count = len(data)
    avg_transaction = total_revenue / count if count > 0 else 0
    
    return {
        'total_revenue': round(total_revenue, 2),
        'avg_transaction': round(avg_transaction, 2),
        'count': count
    }

def get_top_products(data, limit=5):
    """
    Get top selling products by transaction count
    Returns: list of (product, count) tuples
    """
    product_count = defaultdict(int)
    for row in data:
        product = row.get('product', 'Unknown')
        product_count[product] += 1
    
    sorted_products = sorted(product_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_products[:limit]

def get_region_performance(data):
    """
    Analyze sales performance by region
    Returns: dict with region-wise revenue and count
    """
    region_stats = defaultdict(lambda: {'revenue': 0, 'count': 0})
    
    for row in data:
        region = row.get('region', 'Unknown')
        amount = float(row.get('amount', 0))
        region_stats[region]['revenue'] += amount
        region_stats[region]['count'] += 1
    
    result = {}
    for region, stats in region_stats.items():
        result[region] = {
            'revenue': round(stats['revenue'], 2),
            'count': stats['count'],
            'avg_transaction': round(stats['revenue'] / stats['count'], 2) if stats['count'] > 0 else 0
        }
    
    return result

def get_customer_analysis(data):
    """
    Analyze customer purchase patterns
    Returns: list of (customer, transaction_count, total_spent) tuples
    """
    customer_stats = defaultdict(lambda: {'count': 0, 'revenue': 0})
    
    for row in data:
        customer = row.get('customer', 'Unknown')
        amount = float(row.get('amount', 0))
        customer_stats[customer]['count'] += 1
        customer_stats[customer]['revenue'] += amount
    
    result = []
    for customer, stats in customer_stats.items():
        result.append((
            customer,
            stats['count'],
            round(stats['revenue'], 2)
        ))
    
    return sorted(result, key=lambda x: x[2], reverse=True)

def get_daily_trends(data):
    """
    Analyze daily sales trends
    Returns: dict with date-wise revenue and count
    """
    daily_stats = defaultdict(lambda: {'revenue': 0, 'count': 0})
    
    for row in data:
        date_str = row.get('date', 'Unknown')
        amount = float(row.get('amount', 0))
        daily_stats[date_str]['revenue'] += amount
        daily_stats[date_str]['count'] += 1
    
    result = {}
    for date, stats in daily_stats.items():
        result[date] = {
            'revenue': round(stats['revenue'], 2),
            'count': stats['count']
        }
    
    return result

def get_low_performers(data, threshold_percentile=25):
    """
    Identify low performing products
    Returns: list of products below threshold
    """
    product_revenue = defaultdict(float)
    product_count = defaultdict(int)
    
    for row in data:
        product = row.get('product', 'Unknown')
        amount = float(row.get('amount', 0))
        product_revenue[product] += amount
        product_count[product] += 1
    
    # Calculate average revenue per product
    if not product_revenue:
        return []
    
    avg_revenue = sum(product_revenue.values()) / len(product_revenue)
    low_threshold = avg_revenue * (threshold_percentile / 100)
    
    low_performers = []
    for product, revenue in product_revenue.items():
        if revenue < low_threshold:
            low_performers.append({
                'product': product,
                'revenue': round(revenue, 2),
                'count': product_count[product]
            })
    
    return sorted(low_performers, key=lambda x: x['revenue'])
