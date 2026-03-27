from typing import Dict, List, Union

from .constants import FEEDBACK_RULES, SCORE_LABELS


def get_label(score: int) -> str:
    """Map a numeric score (0, 1, 2) to its human-readable label."""
    return SCORE_LABELS.get(score, "Unknown")


def get_feedback(features: Dict[str, Union[int, float]]) -> List[str]:
    """
    Generate actionable feedback based on extracted password features.

    Rules are evaluated in order; all matching rules contribute a message.

    Parameters
    ----------
    features : dict
        Output of ``extract_features()``.

    Returns
    -------
    list of str
        Zero or more feedback strings. An empty list means the password
        passed all heuristic checks.
    """
    return [
        rule["message"]
        for rule in FEEDBACK_RULES
        if rule["condition"](features)
    ]


def public_features(
    features: Dict[str, Union[int, float]]
) -> Dict[str, Union[int, float]]:
    """
    Return the subset of features exposed in the public API response.

    Only the five most interpretable features are surfaced to callers;
    the full feature dict (10 values) is used internally for prediction.
    """
    return {
        "length": features["length"],
        "entropy": features["entropy"],
        "num_upper": features["num_upper"],
        "num_digits": features["num_digits"],
        "num_special": features["num_special"],
    }
