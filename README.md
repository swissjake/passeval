# passeval

**Offline ML-powered password strength evaluation for Python developers.**

Built on a Random Forest classifier trained on 220,000 passwords. Runs fully locally, no API, no server.

## Installation

```bash
pip install passeval
```

## Quick Start

```python
from passeval import evaluate_password

result = evaluate_password("Monkey2024!")
print(result)
```

```json
{
  "score": 0,
  "label": "Weak",
  "confidence": 1.0,
  "features": {
    "length": 11,
    "entropy": 3.2776,
    "num_upper": 1,
    "num_digits": 4,
    "num_special": 1
  },
  "feedback": [
    "Longer passwords are significantly harder to crack",
    "Avoid predictable patterns like years or repeated digits"
  ]
}
```

## Examples

```python
from passeval import evaluate_password

evaluate_password("hunter2")["label"]                      # Weak
evaluate_password("Password1")["label"]                    # Medium
evaluate_password("blitz8-concrete2-eloquence3")["label"]  # Strong
evaluate_password("xK9#mP2$vL8@")["label"]                # Strong
```

## Key Features

- **3-class scoring** - Weak (0), Medium (1), Strong (2)
- **Confidence score** - model probability for the predicted class
- **Actionable feedback** - specific suggestions to improve weak passwords
- **Detects breach-derived patterns** - catches passwords like `Monkey2024!` that pass surface-level complexity checks
- **Fully offline** - model ships inside the package, no internet required
- **Fast after warmup** - model cached in memory, sub-millisecond from second call onward

## How It Works

`passeval` extracts 10 statistical features from each password (length, entropy, character type counts, boolean flags) then runs them through a trained Random Forest classifier. No raw characters are inspected; the model learns structural patterns, not specific passwords.

```python
from passeval import extract_features

extract_features("Monkey2024!")
# {
#   'length': 11, 'num_upper': 1, 'num_lower': 6, 'num_digits': 4,
#   'num_special': 1, 'entropy': 3.2776, 'unique_chars': 10,
#   'has_upper': 1, 'has_digit': 1, 'has_special': 1
# }
```

## vs zxcvbn

Unlike rule-based estimators like [zxcvbn](https://github.com/dwolfhub/zxcvbn-python), `passeval` detects breach-derived patterns such as `Monkey2024!` that satisfy complexity rules but remain guessable.

On realistic weak password detection:
- passeval (ML): **99.93%**
- zxcvbn (rule-based): **32.34%**

## License

MIT - see [LICENSE](LICENSE).
