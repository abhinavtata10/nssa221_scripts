import subprocess

host = "google.com"

result = subprocess.run(["ping", "-c", "4", host])

if result.returncode == 0:
    print("Host is reachable")
else:
    print("Host is unreachable")
