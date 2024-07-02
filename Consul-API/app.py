import datetime, platform,requests,psutil,sys,os,logging
from flask import Flask, jsonify

app = Flask(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

CONSUL_URL = os.environ['CONSUL_URL']
logging.info("Consul URL: "+CONSUL_URL)

def get_consul_status():
    try:
        response = requests.get(f"{CONSUL_URL}/status/leader")
        response.raise_for_status()
        return {"status": 1, "message": "Consul server is running"}
    except requests.exceptions.RequestException as e:
        return {"status": 0, "message": f"Consul server is down: {e}"}

def get_consul_summary():
    try:
        nodes = requests.get(f"{CONSUL_URL}/catalog/nodes").json()
        services = requests.get(f"{CONSUL_URL}/catalog/services").json()
        leader = requests.get(f"{CONSUL_URL}/status/leader").text
        protocol = requests.get(f"{CONSUL_URL}/agent/self").json()["DebugConfig"]["RaftProtocol"]

        return {
            "registered_nodes": len(nodes),
            "registered_services": len(services),
            "leader": leader.strip().replace('"', ''),
            "cluster_protocol": protocol
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to retrieve summary: {e}"}

def get_consul_members():
    try:
        members = requests.get(f"{CONSUL_URL}/agent/members").json()
        node_names = [member["Name"] for member in members]
        return {"registered_nodes": node_names}
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to retrieve members: {e}"}

def get_system_info():
    system_info = {
        "vCpus": psutil.cpu_count(),
        "MemoryGB": round(psutil.virtual_memory().total / (1024 ** 3), 2),  # Convert bytes to GB
        "DiskTotalGB": round(psutil.disk_usage('/').total / (1024 ** 3), 2),  # Convert bytes to GB
        "DiskUsedGB": round(psutil.disk_usage('/').used / (1024 ** 3), 2),  # Convert bytes to GB
        "DiskFreeGB": round(psutil.disk_usage('/').free / (1024 ** 3), 2),  # Convert bytes to GB
        "CpuUsagePercent": psutil.cpu_percent(interval=1),
        "MemoryUsagePercent": psutil.virtual_memory().percent,
        "Platform": platform.system(),
        "PlatformVersion": platform.version(),
        "Hostname": platform.node(),
        "Uptime": datetime.datetime.fromtimestamp(psutil.boot_time()),
        
    }
    return system_info

@app.route('/v1/api/consulCluster/status', methods=['GET'])
def status():
    return jsonify(get_consul_status())

@app.route('/v1/api/consulCluster/summary', methods=['GET'])
def summary():
    return jsonify(get_consul_summary())

@app.route('/v1/api/consulCluster/members', methods=['GET'])
def members():
    return jsonify(get_consul_members())

@app.route('/v1/api/consulCluster/systemInfo', methods=['GET'])
def system_info():
    return jsonify(get_system_info())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)