
import json

def get_all_rss_sources():
    # This function would fetch all RSS sources from the database.
    # For this mock, we'll return a predefined list of sources.
    mock_sources = [
        {"id": 1, "url": "http://example.com/rss1", "name": "Example News 1"},
        {"id": 2, "url": "http://example.com/rss2", "name": "Example News 2"}
    ]
    return json.dumps(mock_sources)

def add_rss_source(data):
    # This function would add a new RSS source to the database.
    # For this mock, we'll just return the data that was passed in,
    # simulating that it has been added with a new ID.
    new_source = data
    new_source["id"] = 3  # Assign a mock ID
    return json.dumps(new_source)

def update_rss_source(source_id, data):
    # This function would update an existing RSS source in the database.
    # For this mock, we'll return the updated data.
    updated_source = {"id": source_id, **data}
    return json.dumps(updated_source)

def delete_rss_source(source_id):
    # This function would delete an RSS source from the database.
    # For this mock, we'll return a success message.
    return ""
