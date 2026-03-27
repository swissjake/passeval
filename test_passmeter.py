from passeval import evaluate_password
import json

passwords = [
    "blitz8-concrete2-eloquence3",
    "Password1",
    "hunter2",
    "xK9#mP2$vL8@",
    "Monkey2024!",
]

for p in passwords:
    r = evaluate_password(p)
    print(f"\n--- {p!r} ---")
    print(json.dumps(r, indent=2))
