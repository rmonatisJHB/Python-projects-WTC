
from user.authentication import authenticate_user
from transactions.journal import *
# from banking.reconciliation import do_reconciliation
# import banking.fvb.reconciliation as virtualbank 
# import banking.ubsa.reconciliation as unrealbank
# import banking.online.reconciliation as onlinebanking
import banking.fvb
import sys


def print_arguments():
    if  len(sys.argv) > 1:
        print(*sys.argv[1:], sep='\n')
    


if __name__ == "__main__":
    print_arguments()
    authenticate_user()
    amount = 100
    receive_income(amount)
    pay_expense(amount)
    banking.do_reconciliation()
    # virtualbank.do_reconciliation()
    # unrealbank.do_reconciliation()
    # onlinebanking.do_reconciliation()