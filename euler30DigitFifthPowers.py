#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

#1634 = 14 + 64 + 34 + 44
#8208 = 84 + 24 + 04 + 84
#9474 = 94 + 44 + 74 + 44
#As 1 = 14 is not a sum it is not included.

#The sum of these numbers is 1634 + 8208 + 9474 = 19316.

#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def DigitFifthPowers(n):
    # n is the power
    start_range = 2 # 1 is excluded
    d = 0
    # max sum can be n*9^n, and this should be less than 10^(n+1)
    while d*(9**d) < 10**(n+1):
        d += 1
    final_range = (d-1)*(9**(d-1))
    list = []
    final_sum = 0
    for i in range(start_range, final_range):
        sum = 0
        number = i
        while (i > 0):
            Reminder = i % 10
            sum += Reminder**n
            i //= 10
        if sum == number:
            final_sum += number
            list.append(number)
    return final_sum, list

final = DigitFifthPowers(5)
print(final)