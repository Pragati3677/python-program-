
server_ip = ("192.168.1.1",)  

allowed_ips = ["192.168.1.10", "192.168.1.11"]


new_ip = "192.168.1.12"
allowed_ips.append(new_ip)

print("Server IP:", server_ip[0])
print("Allowed IPs:", allowed_ips)


