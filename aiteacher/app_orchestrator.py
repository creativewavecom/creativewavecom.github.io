import rss_source_manager
import news_monitoring
import duplicate_detection_settings
import telegram_integration
import re

def handle_request(method, path, query_params=None, body=None):
    """
    Routes incoming requests to the appropriate handler based on the path and method.
    """
    # Dashboard
    if path == '/dashboard/summary':
        return {'status_code': 200, 'body': {'summary': 'Dashboard summary'}}

    # RSS Sources
    if path == '/rss-sources':
        if method == 'GET':
            return {'status_code': 200, 'body': rss_source_manager.get_all_rss_sources()}
        if method == 'POST':
            return {'status_code': 201, 'body': rss_source_manager.add_rss_source(body)}
    
    source_id_match = re.match(r'/rss-sources/(\w+)', path)
    if source_id_match:
        source_id = source_id_match.group(1)
        if method == 'PUT':
            return {'status_code': 200, 'body': rss_source_manager.update_rss_source(source_id, body)}
        if method == 'DELETE':
            return {'status_code': 204, 'body': rss_source_manager.delete_rss_source(source_id)}

    # News Items
    if path == '/news-items':
        if method == 'GET':
            return {'status_code': 200, 'body': news_monitoring.get_all_news_items(query_params)}
            
    news_id_match = re.match(r'/news-items/(\w+)', path)
    if news_id_match:
        news_id = news_id_match.group(1)
        if method == 'GET':
            return {'status_code': 200, 'body': news_monitoring.get_news_item_details(news_id)}

    # Settings
    if path == '/settings/duplicate-detection':
        if method == 'GET':
            return {'status_code': 200, 'body': duplicate_detection_settings.get_settings()}
        if method == 'PUT':
            return {'status_code': 200, 'body': duplicate_detection_settings.update_settings(body)}
            
    if path == '/settings/telegram':
        if method == 'GET':
            return {'status_code': 200, 'body': telegram_integration.get_telegram_settings()}
        if method == 'PUT':
            return {'status_code': 200, 'body': telegram_integration.update_telegram_settings(body)}

    # Telegram History
    if path == '/telegram/history':
        if method == 'GET':
            return {'status_code': 200, 'body': telegram_integration.get_telegram_history()}

    return {'status_code': 404, 'body': {'error': 'Not Found'}}

if __name__ == '__main__':
    # Example Usage
    print("--- Testing RSS Source Manager ---")
    print(handle_request('/api/v1/rss-sources', 'GET'))
    print(handle_request('/api/v1/rss-sources', 'POST', body={'url': 'http://example.com/rss'}))
    print(handle_request('/api/v1/rss-sources/src123', 'PUT', body={'url': 'http://new-example.com/rss'}))
    print(handle_request('/api/v1/rss-sources/src123', 'DELETE'))

    print("\n--- Testing News Monitoring ---")
    print(handle_request('/api/v1/news', 'GET', query_params={'limit': 10}))
    print(handle_request('/api/v1/news/news456', 'GET'))
    print(handle_request('/api/v1/news/news456', 'DELETE'))

    print("\n--- Testing Duplicate Detection Settings ---")
    print(handle_request('/api/v1/settings/duplicate-detection', 'GET'))
    print(handle_request('/api/v1/settings/duplicate-detection', 'PUT', body={'threshold': 0.9}))

    print("\n--- Testing Telegram Integration ---")
    print(handle_request('/api/v1/telegram/notify', 'POST', body={'message': 'Hello from the orchestrator!'}))
    
    print("\n--- Testing Not Found ---")
    print(handle_request('/api/v1/unknown', 'GET'))
