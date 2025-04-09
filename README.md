# 🛠️ CyberToolkit

**CyberToolkit** is a modular and beginner-friendly cybersecurity CLI toolkit developed in Python.  
It includes a growing collection of mini tools for everyday security tasks, including password generation, log monitoring, port scanning, and more.

---

## 📦 Features

- Modular structure: each tool is a self-contained module
- Easy to use via command line
- Custom arguments for each module
- Simple and secure scripts for real-life use or learning purposes
- Great for portfolio building and daily practice

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/CyberToolkit.git
cd CyberToolkit
```
### 2. Run a module
Use the main entrypoint to launch a module:

```bash
python main.py <module-name> [arguments]
```
Example:
```bash
python main.py password-generator --length 16 --secure --count 5 --exclude '@'
```

## 📚 Available Modules
🔐 - password-generator :

Generate strong, random passwords with customizable options.


#### Features:

Define length

Exclude specific characters

Generate multiple passwords

Option to use cryptographically secure method (--secure)

Save output to a file

## Usage:

```bash
python main.py password-generator --length 16 --secure --exclude '@$' --count 3 --save passwords.txt
```

## 📜 log-monitor
Monitor log files in real time and filter lines with keywords.

### Features:

Tail-style log reading

Keyword filtering (--filter)

Save filtered logs to a file (--save)

Add timestamps (--timestamp)

Colored output

Optional Discord/Slack webhook alerts

Usage:

```bash
python main.py log-monitor --file /var/log/syslog --filter "error" --timestamp --save alerts.log
```

### 🧩 Upcoming Modules
- port-scanner

- url-analyzer

- crypto-checker

- file-integrity

More coming soon...

## 🧑‍💻 Author
Franck CRASSAVA
Cybersecurity & Network Architecture Student
GitHub • LinkedIn

## ✅ Contributions
This project is personal but open to learning.
Feel free to fork it, suggest improvements or use it for your own training.
