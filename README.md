# 🔐 Log Analyzer (Cybersecurity Project)

A Python-based log analysis tool that detects failed SSH login attempts and identifies potential brute-force attacks using simple rule-based detection.

---

## 📌 Overview

This project simulates a basic **Security Operations Center (SOC)** tool that processes authentication logs, extracts failed login attempts, and flags suspicious IP activity.

It is designed as a learning project for:
- Cybersecurity fundamentals
- Log analysis techniques
- Python scripting for security use cases

---

## 🚀 Features

- Reads and parses SSH authentication logs
- Detects failed login attempts
- Extracts attacker IP addresses using regex
- Aggregates failed attempts per IP
- Detects brute-force behavior using threshold rules
- Generates a simple security report

---

## 🧠 How It Works

1. The tool reads a log file line by line  
2. It filters entries containing failed login attempts  
3. It extracts IP addresses from those entries  
4. It counts occurrences per IP  
5. It flags IPs exceeding a defined threshold as suspicious  

---

## 📁 Project Structure


log-analyzer/
├── analyzer/
│   ├── parser.py        # Loads and parses log files
│   ├── detector.py      # Detects failed logins and suspicious IPs
│   └── report.py        # Generates security report
│
├── logs/
│   └── sample.log       # Sample SSH log data for testing
│
├── main.py              # Entry point of the application
├── README.md
└── .gitignore


---

## ⚙️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/log-analyzer.git
cd log-analyzer
2. Run the program
python3 main.py
