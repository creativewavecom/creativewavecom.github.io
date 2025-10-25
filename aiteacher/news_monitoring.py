
import json

def get_dashboard_summary():
    # This function would fetch a summary for the dashboard.
    # For this mock, we'll return some predefined statistics.
    mock_summary = {
        "total_news_items": 1200,
        "new_today": 50,
        "duplicates_found": 15
    }
    return json.dumps(mock_summary)

def get_all_news_items(page=1, per_page=10):
    # This function would fetch a paginated list of news items.
    # For this mock, we'll return a predefined list.
    mock_items = [
        {"id": 101, "title": "News Item 1", "source": "Example News 1", "published_date": "2023-10-27"},
        {"id": 102, "title": "News Item 2", "source": "Example News 2", "published_date": "2023-10-27"}
    ]
    return json.dumps(mock_items)

def get_news_item_details(item_id):
    # This function would fetch the details of a single news item.
    # For this mock, we'll return a predefined item.
    mock_item = {
        "id": item_id,
        "title": f"News Item {item_id}",
        "content": "This is the full content of the news item.",
        "source": "Example News 1",
        "published_date": "2023-10-27",
        "is_duplicate": False,
        "linked_to": None
    }
    return json.dumps(mock_item)

def update_news_item_linkage(item_id, data):
    # This function would update the linkage of a news item (e.g., mark as duplicate).
    # For this mock, we'll return the updated data.
    updated_item = {
        "id": item_id,
        "is_duplicate": data.get("is_duplicate"),
        "linked_to": data.get("linked_to")
    }
    return json.dumps(updated_item)
