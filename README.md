# 🔐 Log Analyzer - Cybersecurity Project

A simple Python-based log analysis tool that detects failed login attempts and identifies potential brute-force attacks from SSH authentication logs.

---

## 📌 Features

- Parses SSH authentication logs
- Detects failed login attempts
- Extracts IP addresses from log entries
- Aggregates suspicious activity per IP
- Detects brute-force attacks using threshold rules
- Generates a simple security report

---

## 🧠 How It Works

The tool processes log files line by line, extracts failed login events, and groups them by IP address.  
If an IP exceeds a defined threshold of failed attempts, it is flagged as a potential brute-force attack.

---

## 📁 Project Structure
