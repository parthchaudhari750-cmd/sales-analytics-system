"""
API Integration Module
Handles integration with DummyJSON API for product data
"""

import requests
import time

API_BASE_URL = "https://dummyjson.com/products"

def fetch_products(limit=10, skip=0):
    """
    Fetch products from DummyJSON API
    Args:
        limit: Number of products to fetch
        skip: Number of products to skip
    Returns:
        List of product dictionaries
    """
    try:
        url = f"{API_BASE_URL}?limit={limit}&skip={skip}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        products = data.get('products', [])
        
        return products
    except requests.exceptions.Timeout:
        print("API request timed out")
        return []
    except requests.exceptions.ConnectionError:
        print("Failed to connect to API")
        return []
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        return []
    except Exception as e:
        print(f"Error fetching products: {e}")
        return []

def create_product_mapping(products):
    """
    Create a mapping of product IDs to product information
    Args:
        products: List of product dictionaries from API
    Returns:
        Dictionary mapping product ID to product info
    """
    mapping = {}
    for product in products:
        product_id = str(product.get('id', ''))
        mapping[product_id] = {
            'title': product.get('title', 'Unknown'),
            'category': product.get('category', 'Unknown'),
            'price': product.get('price', 0),
            'rating': product.get('rating', 0),
            'stock': product.get('stock', 0)
        }
    
    return mapping

def enrich_sales_data(sales_data, product_mapping):
    """
    Enrich sales data with product information from API
    Args:
        sales_data: List of sales transaction dictionaries
        product_mapping: Dictionary of product information
    Returns:
        List of enriched sales records with product details
    """
    enriched_data = []
    
    for transaction in sales_data:
        enriched_transaction = transaction.copy()
        
        # Try to find product information
        product_id = str(transaction.get('product_id', ''))
        
        if product_id in product_mapping:
            product_info = product_mapping[product_id]
            enriched_transaction['product_title'] = product_info.get('title', 'Unknown')
            enriched_transaction['category'] = product_info.get('category', 'Unknown')
            enriched_transaction['product_price'] = product_info.get('price', 0)
            enriched_transaction['product_rating'] = product_info.get('rating', 0)
            enriched_transaction['stock_available'] = product_info.get('stock', 0)
        else:
            enriched_transaction['product_title'] = 'Unknown'
            enriched_transaction['category'] = 'Unknown'
            enriched_transaction['product_price'] = 0
            enriched_transaction['product_rating'] = 0
            enriched_transaction['stock_available'] = 0
        
        enriched_data.append(enriched_transaction)
    
    return enriched_data

def get_product_details(product_id):
    """
    Get detailed information about a specific product
    Args:
        product_id: ID of the product
    Returns:
        Product details dictionary
    """
    try:
        url = f"{API_BASE_URL}/{product_id}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        return response.json()
    except Exception as e:
        print(f"Error fetching product {product_id}: {e}")
        return None
