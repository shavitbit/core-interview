from flask import Flask, jsonify
app = Flask(__name__)

# get_consul_status
# get_consul_summary
# get_consul_members
# get_system_info

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)