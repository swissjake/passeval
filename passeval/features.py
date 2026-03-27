import math
from collections import Counter
from typing import Dict, Union

from .constants import FEATURE_ORDER


def _shannon_entropy(password: str) -> float:
    """Compute Shannon entropy (bits per character) for the password."""
    if not password:
        return 0.0
    freq = Counter(password)
    length = len(password)
    return -sum(
        (count / length) * math.log2(count / length)
        for count in freq.values()
    )


def extract_features(password: str) -> Dict[str, Union[int, float]]:
    """
    Extract the 10 statistical features used by the trained model.

    Parameters
    ----------
    password : str
        The password string to analyse.

    Returns
    -------
    dict
        Feature names mapped to their computed values.
    """
    if not isinstance(password, str):
        raise TypeError(f"Password must be a str, got {type(password).__name__}")

    length = len(password)
    num_upper = sum(1 for c in password if c.isupper())
    num_lower = sum(1 for c in password if c.islower())
    num_digits = sum(1 for c in password if c.isdigit())
    num_special = sum(1 for c in password if not c.isalnum())
    entropy = _shannon_entropy(password)
    unique_chars = len(set(password))
    has_upper = int(num_upper > 0)
    has_digit = int(num_digits > 0)
    has_special = int(num_special > 0)

    return {
        "length": length,
        "num_upper": num_upper,
        "num_lower": num_lower,
        "num_digits": num_digits,
        "num_special": num_special,
        "entropy": round(entropy, 4),
        "unique_chars": unique_chars,
        "has_upper": has_upper,
        "has_digit": has_digit,
        "has_special": has_special,
    }


def features_to_vector(features: Dict[str, Union[int, float]]) -> list:
    """Return feature values in the exact order the model was trained on."""
    return [features[key] for key in FEATURE_ORDER]
