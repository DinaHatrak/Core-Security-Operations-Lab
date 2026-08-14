import random
from datetime import datetime, timedelta

def generate_logs():
    users = ["root", "admin", "user1", "dina", "test", "postgres"]
    ips = ["192.168.1.50", "45.33.32.156", "185.220.101.5", "10.0.0.15", "203.0.113.42"]
    
    log_entries = []
    start_time = datetime.now() - timedelta(hours=1)
    
    for i in range(100):
        timestamp = (start_time + timedelta(seconds=i*35)).strftime("%b %d %H:%M:%S")
        ip = random.choice(ips)
        user = random.choice(users)
        
        # Simulate Brute force from a malicious IP
        if ip == "45.33.32.156" or ip == "185.220.101.5":
            status = "Failed password"
        else:
            status = random.choice(["Accepted password", "Failed password", "Invalid user"])
            
        log = f"{timestamp} sec-server sshd[1234]: {status} for {user} from {ip} port 523{i} ssh2"
        log_entries.append(log)
        
    with open("logs/sample_auth_logs.txt", "w") as f:
        f.write("\n".join(log_entries))
    print("[+] sample_auth_logs.txt generated successfully!")

if __name__ == "__main__":
    generate_logs()
