import requests
import json
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# API Details
API_URL = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
API_KEY = "579b464db66ec23bdd000001dc9498084add45397d396ea40981659f"

def fetch_market_data(limit=500):
    """
    Fetch market prices from the API.
    """
    params = {
        "api-key": API_KEY,
        "format": "json",
        "limit": limit,  # Fetch all data, then filter manually
    }

    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        records = data.get("records", [])
        print("Fetched Data (First 5 records):", json.dumps(records[:5], indent=2))  # Debugging
        return records
    return []

def market_view(request):
    """
    Render the market prices page with arrival date and full details.
    """
    search_query = request.GET.get('search_query', '').strip().lower()
    search_state = request.GET.get('search_state', '').strip().lower()
    page = request.GET.get('page', 1)

    # Fetch all data
    data = fetch_market_data()

    # 🔹 Debug: Print the first 5 results
    if not data:
        print("⚠️ No data received from API!")

    # 🔹 Filtering Logic
    if search_query:
        data = [item for item in data if search_query in item.get("Commodity", "").lower()]
    
    if search_state:
        data = [item for item in data if search_state in item.get("State", "").lower()]

    # 🔹 Debugging
    print("Filtered Data (First 5):", json.dumps(data[:5], indent=2))

    # Pagination (50 items per page)
    paginator = Paginator(data, 50)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, "myapp/market.html", {
        "market_data": page_obj,
        "search_query": search_query,
        "search_state": search_state
    })
