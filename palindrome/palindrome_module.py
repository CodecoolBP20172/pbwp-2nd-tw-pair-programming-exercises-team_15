def palindrome(str):
    str = str.lower()
    str = str.replace(' ', '')
    if str == str[::-1]:
        return True
    else:
        return False


def main():
    return


if __name__ == '__main__':
    main()
