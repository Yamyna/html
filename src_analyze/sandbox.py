import docker
from scapy.all import sniff

def run_in_sandbox(exe_path):
    client = docker.from_env()

    try:
        #result = client.containers.run("python:3.8", command=["python", "-c", code], remove=True)
        result = client.containers.run("scottyhardy/docker-wine", command=["wine", exe_path], remove=True)
        return result.decode("utf-8")
    except docker.errors.ContainerError as e:
        return str(e)

exe_path = "/path/to/your/file.exe"

print(run_in_sandbox(exe_path))