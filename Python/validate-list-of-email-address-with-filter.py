# Link to chall: https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
def fun(s):
    # return True if s is a valid email, else return False
    try:
        username, tmp = s.split('@')
        websitename, extension = tmp.split('.')
    except ValueError:
        return False
    if not username.replace('-', '').replace('_', '').isalnum():
        return False
    elif not websitename.isalnum():
        return False
    elif len(extension)>3:
        return False
    for ext in extension:
        if not ext.isalpha():
            return False
    return True
