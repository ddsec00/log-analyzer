import re
from collections import Counter

def get_failed_ips(logs):
    failed_ips = []

    for line in logs:
        if "Failed password" in line:
            match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
            if match:
                failed_ips.append(match.group(1))

    return Counter(failed_ips)


def detect_bruteforce(ip_counts, threshold=3):
    suspicious = {}

    for ip, count in ip_counts.items():
        if count >= threshold:
            suspicious[ip] = count

    return suspicious