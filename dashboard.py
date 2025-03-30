# dashboard.py
from flask import Flask, jsonify
from health_check import check_url_health, check_port
from resource_monitor import check_disk_usage, check_memory

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({
        "url": check_url_health("https://yourapp.com/health"),
        "port": check_port("yourhost.com", 443),
        "disk": check_disk_usage("/"),
        "memory": check_memory()
    })

if __name__ == '__main__':
    app.run(debug=True)
