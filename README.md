# Core Security Operations Lab

A hands-on cybersecurity operations and defensive analysis lab aligned with **CompTIA Security+** core domains (Threats, Attacks, Vulnerabilities, and Security Operations).

## Project Overview
This project demonstrates end-to-end incident analysis:
1. **Log Simulation:** Generating realistic Linux authentication logs containing simulated SSH brute-force attacks via Python.
2. **Log Parsing & Analysis:** Writing a Python script to parse logs, aggregate failed login attempts, and extract Indicators of Compromise (IOCs).
3. **Defense & Mitigation:** Documenting incident response steps and hardening strategies.

## Lab Structure
- scripts/log_simulator.py - Generates raw authentication log samples.
- scripts/attack_analyzer.py - Parses logs and flags suspicious brute-force activity.
- logs/sample_auth_logs.txt - Raw log data output.
- eports/incident_analysis_report.md - Formal security analysis and mitigation plan.

## Security+ Concepts Covered
- **Log Review & Analysis:** Identifying unauthorized access attempts through system log interpretation.
- **Brute-Force Mitigation:** Implementing account lockout policies, rate limiting, and Fail2ban.
- **Incident Response Lifecycle:** Preparation, Detection & Analysis, Containment, Eradication, and Recovery.
