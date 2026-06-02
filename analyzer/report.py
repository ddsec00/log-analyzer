def print_report(ip_counts, suspicious_ips):
    print("\n--- SECURITY REPORT ---\n")

    print("Failed login attempts per IP:")
    for ip, count in ip_counts.items():
        print(f"{ip} → {count}")

    print("\n--- ALERTS ---")
    if not suspicious_ips:
        print("No suspicious activity detected.")
    else:
        for ip, count in suspicious_ips.items():
            print(f"ALERT: {ip} → possible brute-force attack ({count} attempts)")