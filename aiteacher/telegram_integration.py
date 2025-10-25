
import json

def get_telegram_settings():
    # This function would fetch the Telegram integration settings.
    # For this mock, we'll return some predefined settings.
    mock_settings = {
        "bot_token": "1234567890:ABC-DEF1234ghIkl-zyx57W2v1u123ew11",
        "chat_id": "@mock_channel",
        "notifications_enabled": True
    }
    return json.dumps(mock_settings)

def update_telegram_settings(data):
    # This function would update the Telegram integration settings.
    # For this mock, we'll just return the data that was passed in,
    # simulating that it has been updated.
    return json.dumps(data)

def get_telegram_history(page=1, per_page=10):
    # This function would fetch the history of messages sent to Telegram.
    # For this mock, we'll return a predefined list of messages.
    mock_history = [
        {"id": 1, "message": "News: Example 1", "sent_at": "2023-10-27 10:00:00"},
        {"id": 2, "message": "News: Example 2", "sent_at": "2023-10-27 10:05:00"}
    ]
    return json.dumps(mock_history)

def send_test_message(channel_id):
    # This function would send a test message to a Telegram channel.
    # For this mock, we'll return a success response.
    return json.dumps({"status": "success", "message": f"Test message sent to {channel_id}"})
