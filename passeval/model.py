import os
import warnings
from functools import lru_cache
from typing import Any

import joblib

from .constants import MODEL_FILENAME


def _model_path() -> str:
    """Resolve the absolute path to the bundled model file."""
    return os.path.join(os.path.dirname(__file__), MODEL_FILENAME)


@lru_cache(maxsize=1)
def load_model() -> Any:
    """
    Load the trained Random Forest model from the bundled .pkl file.

    The model is loaded once and cached for the lifetime of the process.

    Returns
    -------
    sklearn estimator
        The fitted classifier.

    Raises
    ------
    FileNotFoundError
        If the model file is missing from the package directory.
    RuntimeError
        If the file cannot be deserialised.
    """
    path = _model_path()
    if not os.path.isfile(path):
        raise FileNotFoundError(
            f"Model file not found at '{path}'. "
            "Ensure the package was installed correctly and "
            f"'{MODEL_FILENAME}' is present inside the passmeter package directory."
        )
    try:
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore",
                message="Trying to unpickle estimator",
                category=UserWarning,
            )
            return joblib.load(path)
    except Exception as exc:
        raise RuntimeError(
            f"Failed to load model from '{path}': {exc}"
        ) from exc
