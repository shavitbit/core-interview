### Vagrantfile

This Vagrantfile sets up two VMs:

1. Consul Server VM:
	- Runs a Consul server.
	- Exposes the Consul API on port 8500.
	- Performs a sanity check to ensure Consul is running correctly.
	
2. Apache VM:
	- Runs an Apache web server on port 8080.
	- Configures a health check page.
	- Runs a Consul client.

Each VM is provisioned with necessary configurations and services to function in a Consul-based service discovery setup. The Vagrantfile ensures both VMs have the required resources, network configurations, and software installations to operate correctly.


### Consulapi Python WebApp
This Python service, built with Flask, provides various endpoints to monitor a Consul cluster and gather system metrics from the host machine. The application retrieves and exposes information about the Consul cluster status, nodes, services, and system metrics such as CPU and memory usage.

### Dockerfile
This Dockerfile sets up a lightweight Python environment with the necessary dependencies to run a Flask application that monitors a Consul cluster and exposes system metrics. By following the build and run instructions, you can easily deploy this application in a Docker container.
```bash
# Build the Docker Image:
docker build -t consulapi .
# Run the Docker container:
docker run -d --name consulapi -p 5000:5000 consulapi
```
