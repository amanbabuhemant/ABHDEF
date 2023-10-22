def is_valid_email(email):
    parts = email.split("@")
    if len(parts) == 2:
        username, domain = parts
        if username and domain:
            if "." in domain:
                return True
    return False
