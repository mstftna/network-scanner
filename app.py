import os
import re
with os.popen("arp -a") as f:
    data = f.read()

# print(data)

with open("details.txt", "w") as f:
    f.truncate(0)

ips = []


for line in re.findall('([-.0-9]+)\s+([-0-9a-f]{17})\s+(\w+)',data):
    ips.append(line[0])

# print(ips)

for ip in ips:
    try:
        with os.popen(f"ping -a -n 2 {ip}") as f:
            data2 = f.read()

        with open("details.txt", "a") as f:
            f.write(f"{ip} : \n" + data2 + "\n")

        pcName = data2.split("Pinging ")[1].split(f" [{ip}] with 32 ")[0]
        if "\n" in pcName or len(pcName) >= 25:
            # print(f"{ip} : Request timed out. Logged in details.txt")
            continue
        else:
            print(f"{ip} : {pcName}")
    except Exception as e:
        print(e)

