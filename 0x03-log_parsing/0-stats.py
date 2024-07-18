#!/usr/bin/python3
"""
script that reads stdin line by line and compute matrics
"""
import sys
import signal


total_file_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0,
                     403: 0, 404: 0, 405: 0, 500: 0}
line_counter = 0


def print_stat():
    """
    print data of statstics
    """
    global total_file_size, status_code_count
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if status_code_count[code] > 0:
            print(f"{code}: {status_code_count[code]}")


def signal_handler(sig, frame):
    """
    Handles the keyboard interrupt signal (CTRL + C).
    """
    print_stat()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) != 9:
            continue
        ip_adress = parts[0]
        date = parts[2] + " " + parts[3]
        request = parts[4] + " " + parts[5] + " " + parts[6]
        status_code = int(parts[7])
        file_size = int(parts[8])
        if request != '"GET /projects/260 HTTP/1.1"':
            continue
        total_file_size += file_size
        if status_code in status_code_count:
            status_code_count[status_code] += 1
        line_counter += 1
        if line_counter % 10 == 0:
            print_stat()
    except (IndexError, ValueError):
        continue
print_stat()
