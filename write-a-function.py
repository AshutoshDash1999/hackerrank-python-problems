#problem-link = https://www.hackerrank.com/challenges/write-a-function/problem

# as we know the year divisible by 4 is leap year.
# some numbers are divisible by only 4 like 1992, 2016
# while some are divisible by 400


def is_leap(year):
    leap = False
    # Write your logic here
    if year % 100 == 0:
        if year % 4 == 0 and year % 400 == 0:
            return True
        else:
            return leap
    elif year % 4 == 0:
        return True
    else:
        return leap


year = int(input())
print(is_leap(year))