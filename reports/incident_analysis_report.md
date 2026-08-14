# Incident Analysis Report: SSH Brute-Force Attack

## Incident Overview
- **Incident ID:** INC-2026-0814
- **Detection Method:** Automated Log Analysis Script (ttack_analyzer.py)
- **Target System:** Core Authentication Server (SSH)
- **Severity Level:** High
- **Attack Type:** Brute-Force / Credential Stuffing

---

## 1. Executive Summary
During a routine security log review, multiple failed authentication attempts were flagged from external IP addresses targeting the SSH service. The pattern strongly indicates an automated **Brute-Force Attack** aimed at guessing user credentials (specifically targeting administrative and common usernames like 'root', 'admin', and 'postgres').

---

## 2. Indicators of Compromise (IOCs)
The Python analysis script extracted the following malicious/suspicious source IPs:
- 45.33.32.156 (High frequency of failed passwords)
- 185.220.101.5 (Associated with automated scanning/brute-force behavior)

---

## 3. Analysis & Findings
- **Targeted Accounts:** The attacks focused heavily on default/privileged accounts (oot, dmin), which violates security hardening best practices.
- **Attack Vector:** Standard TCP port 22 (SSH) exposed to un-trusted external networks without rate-limiting controls at the initial phase.

---

## 4. Remediation & Defense Strategy (Security+ Alignment)
To mitigate and prevent future occurrences, the following controls must be implemented immediately:
1. **Disable Root SSH Login:** Modify /etc/ssh/sshd_config to set PermitRootLogin no.
2. **Key-Based Authentication:** Enforce SSH key pairs and disable password authentication entirely (PasswordAuthentication no).
3. **Intrusion Prevention (Fail2ban):** Install and configure Fail2ban to automatically ban IP addresses after 3 failed login attempts.
4. **Firewall / Network Segmentation:** Restrict SSH access using security groups or firewalls to allow administrative access only from trusted VPN IPs.
