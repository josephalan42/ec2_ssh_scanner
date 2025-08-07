import boto3 
from flask import Flask, request, render_template, redirect, url_for, flash

from dotenv import load_dotenv
import os

# Loading environment variables
load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
REGION = "us-east-1"

# Flask Setup
app = Flask(__name__)
app.secret_key = "secret_key_here"

# Initiating ec2 client

ec2 = boto3.client(
    "ec2",
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name = REGION
)

@app.route('/scan', methods=['GET', 'POST'])

def scan_ec2_instances():
    security_groups_with_ssh = []
    if request.method == 'GET':
        return render_template('scan.html')
    
    response = ec2.describe_security_groups()

    for groups in response.get("SecurityGroups",[]):
        for ip_permissions in groups.get("IpPermissions",[]):
            if ip_permissions.get("FromPort") == 22 or ip_permissions.get("ToPort") == 22:
                security_groups_with_ssh.append(groups.get("GroupName"))
    
    return render_template("results.html", results=security_groups_with_ssh)

if __name__ == '__main__':
    app.run(debug=True)