"""
passeval – offline ML-powered password strength evaluation.

Quick start
-----------
>>> from passeval import evaluate_password
>>> result = evaluate_password("hunter2")
>>> print(result["label"])
'Strong'
"""

from .core import evaluate_password
from .features import extract_features

__all__ = ["evaluate_password", "extract_features"]
__version__ = "0.2.0"
