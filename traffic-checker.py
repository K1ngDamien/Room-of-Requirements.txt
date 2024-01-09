import psutil
import time


def network_usage():
    old_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

    while True:
        new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
        send_rate = new_value - old_value
        print(f"Current network traffic: {send_rate} bytes/sec")
        old_value = new_value
        time.sleep(1)


network_usage()
