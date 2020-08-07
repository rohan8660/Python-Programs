def th(n):
    while n%4==0:
        n=n/4
    if(n%8==7):
        return False
    return True
