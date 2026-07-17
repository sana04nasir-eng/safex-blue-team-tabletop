import time

def run_simulation():
    print("="*60)
    print(" SAFEX SOLUTIONS - INCIDENT RESPONSE TABLETOP PLAYBOOK ")
    print("="*60)
    print("\n[CRITICAL ALERT] Threat Intel: Unauthorized data exfiltration detected!")
    print("Target Footprint: dev.safexsolutions.com (Exposed Staging Subdomain)")
    
    time.sleep(1.5)
    print("\n--- PHASE 1: IDENTIFICATION ---")
    print("[+] Analysing Firewall Logs...")
    time.sleep(1)
    print("[!] Attacker is actively downloading database backups!")
    
    print("\n--- PHASE 2: CONTAINMENT (Your Action Required) ---")
    print("Select Blue Team Defensive Action:")
    print("1. Isolate server and enforce strict IP Allow-listing / VPN.")
    print("2. Do nothing and monitor.")
    
    choice = input("\nEnter choice (1 or 2): ")
    
    if choice == "1":
        print("\n--- PHASE 3: ERADICATION & RESOLUTION ---")
        print("[+] Deploying network isolation...")
        time.sleep(1.5)
        print("[+] SUCCESS: Public access revoked. dev.safexsolutions.com is now secured!")
        print("[+] Incident Status: RESOLVED.")
    else:
        print("\n[!] FAILURE: Attacker successfully bypassed and leaked data. Incident Escalated!")
        
    print("\n" + "="*60)

if __name__ == "__main__":
    run_simulation()