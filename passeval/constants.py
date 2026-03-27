SCORE_LABELS = {
    0: "Weak",
    1: "Medium",
    2: "Strong",
}

FEATURE_ORDER = [
    "length",
    "num_upper",
    "num_lower",
    "num_digits",
    "num_special",
    "entropy",
    "unique_chars",
    "has_upper",
    "has_digit",
    "has_special",
]

FEEDBACK_RULES = [
    {
        "condition": lambda f: f["length"] < 8,
        "message": "Use at least 8 characters",
    },
    {
        "condition": lambda f: f["length"] < 12,
        "message": "Longer passwords are significantly harder to crack",
    },
    {
        "condition": lambda f: not f["has_upper"],
        "message": "Add at least one uppercase letter",
    },
    {
        "condition": lambda f: not f["has_digit"],
        "message": "Include at least one number",
    },
    {
        "condition": lambda f: not f["has_special"],
        "message": "Add a special character (e.g. !, @, #, $)",
    },
    {
        "condition": lambda f: f["entropy"] < 2.5,
        "message": "Add more unique characters to increase entropy",
    },
    {
        "condition": lambda f: f["unique_chars"] < 6,
        "message": "Add more unique characters",
    },
    {
        "condition": lambda f: f["num_digits"] >= 4 and f["length"] < 14,
        "message": "Avoid predictable patterns like years or repeated digits",
    },
]

MODEL_FILENAME = "passeval_model.pkl"
