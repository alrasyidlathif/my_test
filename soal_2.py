import re

def is_username_valid(username):
    
    if not (len(username) >= 5 and len(username) <= 9):
        return False

    if not re.match("^[a-zA-Z]+$", username[0]):
        return False

    if not re.match("^[a-zA-Z0-9]+$", username):
        return False

    return True

def is_password_valid(password):
    
    if not len(password) >= 8:
        return False
    
    kap, num, et = 0, 0, 0
    for pw in password:
        if re.match("^[A-Z]+$", pw):
            kap += 1
        if re.match("^[0-9]+$", pw):
            num += 1
        if re.match("^[@]+$", pw):
            et += 1
    if kap == 0 or num == 0 or et == 0:
        return False

    if re.match("^[a-zA-Z0-9@]+$", password):
        return False

    return True
        
    

if __name__ == '__main__':
    u1 = is_username_valid('@sony')
    u2 = is_username_valid('Ayu99v')
    p1 = is_password_valid('p@ssW0rd#')
    p2 = is_password_valid('C0d3YourFuture!#')
    p3 = is_password_valid('12HGF@@@@@@@@@@')
    p4 = is_password_valid('12HGF@@@@@@@@@@~')
    print(u1)
    print(u2)
    print(p1)
    print(p2)
    print(p3)
    print(p4)