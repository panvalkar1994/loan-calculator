import math
import argparse
import sys

loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

# write your code here
# print(loan_principal)
# print(first_month)
# print(second_month)
# print(third_month)
# print(final_output)

# print("Enter the loan principal:")
# loan = int(input())
# print("""
# What do you want to calculate?
# type "m" - for number of monthly payments,
# type "p" - for the monthly payment:""")
# response = str(input())
# if response == 'm':
#     print("Enter the monthly payment:")
#     monthly_pay = int(input())
#     months = math.ceil(loan / monthly_pay)
#     if months == 1:
#         print(f'It will take {months} month to repay the loan')
#     else:
#         print(f'It will take {months} months to repay the loan')
# if response == 'p':
#     print("Enter the number of months:")
#     duration = int(input())
#     per_month = math.ceil(loan / duration)
#     reminder = loan - per_month * (duration-1)
#     print(f'Your monthly payment = {per_month} and the last payment = {reminder}')
#
# template = """
# What do you want to calculate?
# type "n" for number of monthly payments,
# type "a" for annuity monthly payment amount,
# type "p" for loan principal:
# """
#
#


def duration(principal, interest, payment):
    # print("Enter the loan principal:")
    # p = float(input())
    p = principal
    # print("Enter the monthly payment:")
    # m = float(input())
    m = payment
    # print("Enter the loan interest:")
    # x = float(input())
    x = interest
    i = x / (12 * 100)
    n = math.ceil(math.log((m / (m - i * p)), 1 + i))
    if n == 0 or n == 1:
        print('It will take', n,'month to repay this loan!')
    elif 1 < n < 12:
        print('It will take ', n, 'months to repay this loan!')
    elif n == 12:
        print('It will take {} year to repay this loan!'.format(n//12))
    elif 24 > n > 12:
        print('It will take {} year and {} months to repay this loan!'.format(n//12,n%12))
    elif n % 12 == 0:
        print('It will take {} years to repay this loan!'.format(n//12))
    else:
        print('It will take {} years and {} months to repay this loan!'.format(n//12,n%12))
    overpayment = math.ceil(m * n - p)
    print('Overpayment = ', overpayment)


def monthly_payment(principal, periods, interest):
    # print("I am in monthly payment")
    # print("Enter the loan principal:")
    # p = float(input())
    p = principal
    # print("Enter the number of periods:")
    # n = int(input())
    n = periods
    # print("Enter the loan interest:")
    # x = float(input())
    x = interest
    i = x / (12 * 100)
    a = math.ceil(p * ((i * (1+i)**n) / (((1 + i)**n) - 1)))
    overpayment = math.ceil(a * n-p)
    print("Your annuity payment = {}!".format(a))
    print('Overpayment = {}'.format(overpayment))


def principal_value(payment, periods, interest):
    # print("Enter the annuity payment:")
    # a = float(input())
    a = float(payment)
    # print("Enter the number of periods:")
    # n = int(input())
    n = int(periods)
    # print("Enter the loan interest:")
    # x = float(input())
    x = float(interest)
    i = x / 1200
    p = a / ((i * (1 + i)**n) / (((1 + i)**n) - 1))
    print('Your loan principal = {}!'.format(math.ceil(p)))
    overpayment = abs(a * n - p)
    print('Overpayment = {}'.format(math.ceil(overpayment)))


# principal_value(8722,120,5.6)

#
# print(template)
# response = str(input())
# if response == 'n':
#     duration()
# elif response == 'a':
#     monthly_payment()
# elif response == 'p':
#     principal()


def differentiated(principal, periods, interest):
    # print("I am in diff")
    p = principal
    n = periods
    i = interest / 1200
    total = 0
    for m in range(1, n + 1):
        d = math.ceil((p/n)+i*(p-(p*(m-1)/n)))
        total += d
        print('Month {}: payment is {}'.format(m,d))

    overpayment = math.ceil(total - principal)
    print('Overpayment = {}'.format(overpayment))


def type_check(ty):
    flag = False
    for word in sys.argv:
        if ty in word:
            flag = True
    return flag


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', type=str, choices=['annuity', 'diff'])
    parser.add_argument('--principal', type=float)
    parser.add_argument('--periods', type=int)
    parser.add_argument('--interest', type=float)
    parser.add_argument('--payment', type=float)
    args = parser.parse_args()




    # if len(sys.argv) != 4:
    #     print(f'Error: to few or to many arguments are provided')
    if type_check('diff'):
        if type_check('principal') and type_check('periods') and type_check('interest'):
            differentiated(args.principal, args.periods, args.interest)
        else:
            print('Incorrect parameters')
    elif type_check('annuity'):
        if type_check('principal') and type_check('payment') and type_check('interest'):
            duration(args.principal, args.interest, args.payment)
        elif type_check('principal') and type_check('periods') and type_check('interest'):
            monthly_payment(args.principal, args.periods, args.interest)
        elif type_check('payment') and type_check('periods') and type_check('interest'):
            principal_value(args.payment,args.periods,args.interest)
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")


if __name__ == '__main__':
    main()