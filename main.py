from analyzer.parser import load_logs
from analyzer.detector import get_failed_ips, detect_bruteforce
from analyzer.report import print_report

# Load logs
logs = load_logs("logs/sample.log")

# Analyze
ip_counts = get_failed_ips(logs)
suspicious_ips = detect_bruteforce(ip_counts, threshold=3)

# Report
print_report(ip_counts, suspicious_ips)