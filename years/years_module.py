import datetime


def years(age):
    #name = input("What is your name?: ")
    now = datetime.datetime.now()
    now_year = now.year
    estimated_time = now_year - age + 99
    print(estimated_time)

    return estimated_time

def main():
    return


if __name__ == '__main__':
    main()
