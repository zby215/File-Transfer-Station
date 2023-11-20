def validate(num, pwd):
    if len(pwd) < 5:
        return False
    elif num < 1000 or num > 1500:
        return False
    else:
        return True
