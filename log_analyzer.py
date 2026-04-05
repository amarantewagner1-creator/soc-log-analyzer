import re

failed_logins = {}

with open("sample.log") as file:
    logs = file.readlines()

ip_pattern = r"\d{1,3}(?:\.\d{1,3}){3}"

for line in logs:
    ip = re.search(ip_pattern, line).group()

    if "LOGIN_FAILED" in line:
        if ip not in failed_logins:
            failed_logins[ip] = 0
        failed_logins[ip] += 1

for ip, count in failed_logins.items():
    if count >= 3:
        print(f"⚠️ Brute force attack from {ip}")
print("=== Security Report ===\n")

for ip, count in failed_logins.items():
    print(f"{ip} → Failed attempts: {count}")

    if count >= 3:
        print(f"⚠️ ALERT: Brute force attack from {ip}\n")
