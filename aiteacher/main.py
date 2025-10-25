from flask import Flask, jsonify, request, send_from_directory
from app_orchestrator import handle_request

app = Flask(__name__, static_folder='saffron_landing_page')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)

@app.route('/api/v1/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_handler(path):
    response = handle_request(
        method=request.method,
        path=f'/{path}',
        query_params=request.args,
        body=request.json
    )
    return jsonify(response['body']), response['status_code']

if __name__ == '__main__':
    app.run(debug=True)
