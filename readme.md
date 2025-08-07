# 🛡️ EC2 SSH Risk Scanner

This tool scans all EC2 security groups across your AWS account and detects any groups with port 22 (SSH) open to the internet (`0.0.0.0/0`). Built with Python, Flask, and Boto3, it enables AWS security teams to quickly identify and fix overly permissive access.

---

## 🔍 Features

* Detects SSH open to `0.0.0.0/0`
* Lists vulnerable security groups
* Recommends mitigation strategies
* Flask-based web interface

---

## ⚙️ Stack

* Python 3
* Flask
* Boto3
* AWS EC2

---

## 🚀 How to Run

```bash
git clone https://github.com/yourusername/ec2_ssh_scanner.git
cd ec2_ssh_scanner
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

---

## 📌 Security Notes

* Use IAM roles or environment variables for AWS credentials.
* Never run this tool on production EC2 groups without review.

---

## 📌 License

MIT License
