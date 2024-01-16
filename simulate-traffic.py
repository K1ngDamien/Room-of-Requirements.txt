import subprocess
import threading


# Defining configuration
target_ip = "ip_here"
amount_of_pentesters = 8


def simulate_traffic(target_ip):
    command = ["nmap", "-Pn", target_ip]
    subprocess.run(command)


threads = []
for _ in range(amount_of_pentesters):
    thread = threading.Thread(target=simulate_traffic, args=(target_ip,))
    threads.append(thread)
    thread.start()


# Wait for all the threads to complete before finishing
for thread in threads:
    thread.join()

print("Simulating traffic completed.")
