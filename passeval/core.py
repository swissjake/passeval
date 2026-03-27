import warnings

import numpy as np

from .features import extract_features, features_to_vector
from .model import load_model
from .utils import get_feedback, get_label, public_features


def evaluate_password(password: str) -> dict:
    """
    Evaluate the strength of a password using the trained Random Forest model.

    All computation happens locally — no network calls are made.

    Parameters
    ----------
    password : str
        The password to evaluate.

    Returns
    -------
    dict with keys:
        score       int   – 0 (Weak), 1 (Medium), or 2 (Strong)
        label       str   – Human-readable strength label
        confidence  float – Probability of the predicted class (0.0–1.0)
        features    dict  – Key password statistics
        feedback    list  – Actionable improvement suggestions

    Raises
    ------
    TypeError
        If ``password`` is not a string.
    ValueError
        If ``password`` is empty.

    Examples
    --------
    >>> from passmeter import evaluate_password
    >>> result = evaluate_password("Monkey2024!")
    >>> result["label"]
    'Medium'
    """
    if not isinstance(password, str):
        raise TypeError(f"Password must be a str, got {type(password).__name__}")
    if not password:
        raise ValueError("Password must not be empty")

    features = extract_features(password)
    vector = np.array(features_to_vector(features)).reshape(1, -1)

    model = load_model()
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            message="X does not have valid feature names",
            category=UserWarning,
        )
        score = int(model.predict(vector)[0])
        probabilities = model.predict_proba(vector)[0]
    confidence = round(float(probabilities[score]), 4)

    return {
        "score": score,
        "label": get_label(score),
        "confidence": confidence,
        "features": public_features(features),
        "feedback": get_feedback(features),
    }
