import psutil
import time


def get_network_usage():
    net_io = psutil.net_io_counters()
    sent = net_io.bytes_sent
    recv = net_io.bytes_recv
    return sent, recv


def main():
    print("Monitoring network usage. Press Ctrl+C to stop.")
    print(f"{'Time':<20} {'Bytes Sent':<20} {'Bytes Received'}")
    try:
        while True:
            sent, recv = get_network_usage()
            print(f"{time.strftime('%H:%M:%S'):<20} {sent:<20} {recv}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")


if __name__ == "__main__":
    main()
