
import json

def get_settings():
    # This function would fetch the duplicate detection settings.
    # For this mock, we'll return some predefined settings.
    mock_settings = {
        "similarity_threshold": 0.85,
        "active": True
    }
    return json.dumps(mock_settings)

def update_settings(data):
    # This function would update the duplicate detection settings.
    # For this mock, we'll just return the data that was passed in,
    # simulating that it has been updated.
    return json.dumps(data)
