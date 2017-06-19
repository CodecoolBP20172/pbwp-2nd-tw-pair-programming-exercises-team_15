import random
import string
#print(dir(string))
def passwordgen():
    password = list()
    for i in range(50):
        password.append(random.choice(string.printable))
    real_password = ''.join(password)
    return real_password

def main():
    return


if __name__ == '__main__':
    main()
