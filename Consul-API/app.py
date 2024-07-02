from flask import Flask, jsonify
import requests

app = Flask(__name__)
CONSUL_URL = "http://127.0.0.1:8500/v1"
# get_consul_status
def get_consul_status():
    try:
        response = requests.get(f"{CONSUL_URL}/status/leader")
        response.raise_for_status()
        return {"status": 1, "message": "Consul server is running"}
    except requests.exceptions.RequestException as e:
        return {"status": 0, "message": f"Consul server is down: {e}"}

# get_consul_summary
def get_consul_summary():
    return 0



# get_consul_members
def get_consul_members():
    try:
        members = requests.get(f"{CONSUL_URL}/agent/members").json()
        node_names = [member["Name"] for member in members]
        return {"registered_nodes": node_names}
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to retrieve members: {e}"}
# get_system_info
def get_system_info():
    return 0



@app.route('/v1/api/consulCluster/status', methods=['GET'])
def status():
    return jsonify(get_consul_status())

@app.route('/v1/api/consulCluster/summary', methods=['GET'])
def summary():
    return 200

@app.route('/v1/api/consulCluster/members', methods=['GET'])
def members():
    return jsonify(get_consul_members())

@app.route('/v1/api/consulCluster/systemInfo', methods=['GET'])
def system_info():
    return 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)