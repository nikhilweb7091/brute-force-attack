print("WELCOME TO BRUTE FORCE ATTACK DETECTION")
print("MADE BY NIKHIL SUTHAR")

from datetime import datetime

failed_attempt = {}
limit = 5

print("check login log..")
with open("login_log.txt", "r") as file:
    for line in file:
        line = line.strip()
        data = line.split()
        if len(data) == 2:
            ip, status = data
            if status == "failed":
                failed_attempt[ip] = failed_attempt.get(ip, 0) + 1

# report
with open("report.txt", "w") as report:
    report.write("security report\n")
    report.write("Date:" + str(datetime.now()) + "\n\n")
    report.write("Suspicious IP:\n")
    for ip in failed_attempt:
        if failed_attempt[ip] >= limit:
            print(ip, "-", failed_attempt[ip], "failed login")
            report.write(ip + " - " + str(failed_attempt[ip]) + " failed login\n")

print("\nREPORT GENERATED SUCCESSFULLY")