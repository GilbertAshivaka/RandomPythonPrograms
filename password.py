import secrets
import string


def create_pwd(pwd_length=12):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    
    pwd = ''
    alphabet = letters+digits+special_chars
    pw_strong = False


    while not pw_strong:
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))


        if (any(char in special_chars for char in pwd) and sum(char in digits for char in pwd ) >= 2):
            pw_strong = True
        
        print(pwd)
        print(bool(pw_strong))
        
    return pwd



if __name__ == '__main__':
    create_pwd()
