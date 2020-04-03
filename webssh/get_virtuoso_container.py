import docker
import requests
import json


#
# Get the port for the given Docker container id
#
def get_virtuoso_port(container_id: str) -> str:
    # Make a request to the container service to exchange
    # the container id for the containers port
    # payload = json.dumps({ 'machineId': container_id })
    # response = requests.post('http://localhost:5000/api/get-port', 
    #                          data=payload)

    # response_json = response.json()
    # port = response_json['HostPort']
    client = docker.from_env()

    container = client.containers.get(container_id) 
    ports = container.ports

    return ports['22/tcp'][0]['HostPort']


#
# Get the hostname for the given Docker container id
#
def get_virtuoso_hostname(container_id: str) -> str:
    client = docker.from_env()

    container = client.containers.get(container_id)
    ip_address = container.attrs['NetworkSettings']['IPAddress']

    return ip_address
