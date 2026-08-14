from collections import Counter

def analyze_logs():
    print("[*] Analyzing authentication logs for IOCs (Indicators of Compromise)...")
    
    failed_attempts = Counter()
    
    with open("logs/sample_auth_logs.txt", "r") as f:
        for line in f:
            if "Failed password" in line or "Invalid user" in line:
                parts = line.strip().split()
                # Extract IP address (usually second to last or based on structure)
                ip = [p for p in parts if p.count('.') == 3]
                if ip:
                    failed_attempts[ip[0]] += 1
                    
    print("\n=== SECURITY ANALYSIS REPORT ===")
    print("Top Suspicious IPs with Multiple Failed Logins:")
    for ip, count in failed_attempts.most_common(3):
        print(f" [!] IP: {ip} -> {count} failed attempts (Potential Brute Force Attack)")
        
    print("\n[+] Analysis completed safely.")

if __name__ == "__main__":
    analyze_logs()
