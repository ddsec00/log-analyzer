import re
from collections import Counter

failed_ips = []

with open("logs/sample.log", "r") as f:
    for line in f:
        if "Failed password" in line:
            ip = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
            if ip:
                failed_ips.append(ip.group(1))

ip_counts = Counter(failed_ips)

for ip, count in ip_counts.items():
    print(f"{ip} → {count} failed attempts")