TESTCCASES = [
    {
        "positional": ("string", "string",),
        "keyword": {},
        "return": True,
        "msg": "",
    },
    {
        "positional": ("same", "diffrent",),
        "keyword": {},
        "return": False,
        "msg": "",
    },
    {
        "positional": ("listen", "silent",),
        "keyword": {},
        "return": True,
        "msg": "",
    },
    {
        "positional": ("qwerty", "qwwwerty",),
        "keyword": {},
        "return": False,
        "msg": "",
    },
    {
        "positional": ("", "",),
        "keyword": {},
        "return": True,
        "msg": "empty strings",
    },
    {
        "positional": ("debit card", "bad credit",),
        "keyword": {},
        "return": True,
        "msg": "multiple words",
    },
]
