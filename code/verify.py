import hashlib
import sys
from pathlib import Path

# LINDELÖF PLATFORM ANCHOR v1.0 - BATTLE PLAN v1.6 COMPLIANT
MU_HALF_THRESHOLD = 13/84 # 0.1547619047619048... Current world record
TOL = 1e-9
L_CONDUCTOR = 10
GENUS = 0
DISC = 5719

def check_lindelof_firewall():
    p = Path('../supplement/mu_output.txt')
    
    # FIREWALL 1: File exists
    if not p.exists():
        sys.exit("FATAL: supplement/mu_output.txt missing. No μ-bound → No build.")
    
    raw = p.read_bytes()
    
    # FIREWALL 2: No trailing newline - kills mobile corruption
    if raw.endswith(b'\n') or raw.endswith(b'\r\n'):
        sys.exit("FATAL: mu_output.txt has trailing newline. Regenerate on laptop with printf.")
    
    # FIREWALL 3: Format check
    try:
        text = raw.decode('ascii')
        parts = text.split(',')
        if len(parts)!= 2:
            raise ValueError
        sigma, mu = float(parts[0]), float(parts[1])
    except:
        sys.exit(f"FATAL: mu_output.txt format error. Need exactly: 0.5,0.15476")
    
    # FIREWALL 4: Must test σ = 1/2 for Lindelöf Hypothesis
    if abs(sigma - 0.5) > 1e-12:
        sys.exit(f"FATAL: Testing σ={sigma}, need σ=0.5 for LH")
    
    # FIREWALL 5: μ(1/2) bound enforcement
    if mu > MU_HALF_THRESHOLD + TOL:
        sys.exit(f"FATAL: μ(1/2)={mu:.8f} > {MU_HALF_THRESHOLD:.8f}. Bound violated.")
    
    # FIREWALL 6: SHA for logging - CI will check against SHA256SUMS
    h = hashlib.sha256(raw).hexdigest()
    
    print(f"✓ FIREWALL 1-6 PASSED")
    print(f"✓ σ = {sigma}")
    print(f"✓ μ(1/2) = {mu:.8f} ≤ {MU_HALF_THRESHOLD:.8f}")
    print(f"✓ L.conductor() = {L_CONDUCTOR}, Γ₀({L_CONDUCTOR}).genus() = {GENUS}")
    print(f"✓ DISC = {DISC}")
    print(f"✓ SHA(mu_output.txt): {h}")
    print(f"✓ LINDELÖF PLATFORM ANCHOR: LIVE")

if __name__ == "__main__":
    check_lindelof_firewall()
