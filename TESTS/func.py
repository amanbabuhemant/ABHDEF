TESTCASES = [
    { # test case structure
        "positional": ("arguments", "in", "tuples",),   # Positional arguments as Tuple
        "keyword": {"keyword":"arguments"},             # Keyword arguments as Dictoery
        "return": "retuen value",                       # Expected Return Value
        "msg": "sample test case",                      # Message for Testcase (optinal)
    },
    { #fus follow the same structure for every test case
        "positional": ("arguments", "in", "tuples",),
        "keyword": {"keyword":"arguments"},
        "return": "retuen value",
        "msg": "sample test case",
    },
    {
        "positional": ("some", 5, "arguments", "in", "tuples",),
        "keyword": {"keyword":"arguments"},
        "return": 5,
        "msg": "nothing just sample test case",
    },
]
