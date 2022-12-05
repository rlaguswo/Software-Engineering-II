def check_pwd(pwd):
    #length
    if len(pwd) < 8 or len(pwd) > 20:
        return False
    #lower case
    if not any(s.islower() for s in pwd):
        return False
    #upper case
    if not any(s.isupper() for s in pwd):
        return False
    #digits
    if not any(s.isdigit() for s in pwd):
        return False
    #symbols
    permitted = "~`!@#$%^&*()_+-="
    if not any(s in permitted for s in pwd):
        return False
    return True