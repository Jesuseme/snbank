import random
import string
import sys
import os


def main():
    def start_page(): 
        try:
            print('------------SN BANK-------------')
            print('Staff login ----> 1')
            print('Close App ------> 2')
            login = ''
            while login!='1'or login!='2':
                login = input('>: ')
                if login == '1':
                    login_page()
                elif login == '2':
                    print('closing application-- press 2 to confirm')
                    break                     
                elif login !=1 or login != 2:
                    print('invalid response\nTry Again')    
        except:
            print('invalid response')

    def login_page():
        global staff
        global username
        # converts txt file to dictionary
        with open('staff.txt', 'r') as document:
            staff = {}
            for line in document:
                line = line.split()
                if not line:  # empty line?
                    continue
                staff[line[0]] = line[1:]

        username = input('Username: ').upper()
        try:
            for i in staff:
                if staff[username] == staff[i]:
                    print(f'correct {staff[i]}')
                    password = input('password: ')
                    if password == staff[i][0]:
                        print('login successful')
                        fh = open('session.txt', 'a')
                        fh.write(f'{username} session begin\n')
                        fh.close() 
                        staff_access()
                    else:
                        print('Invalid password')
                        print('Try again')
                        login_page()
        except:
            print('invalid detail imputed')
            print('Try again')
            login_page()

    def staff_access():
        try:
            print('---------Staff Account---------')
            print('Create a New Account -----> 1')
            print('Check Account Details ----> 2')
            print('Logout  -----> 3')
            access = input('->: ')
            if access == '1':
                create_account()
            elif access == '2':
                check_account()
            elif access == '3':
                os.remove('session.txt')
                print('Logged out')
                start_page()
        except:
            print('invalid response')

    def create_account():
        print('-----------New Customer---------')
        global acct_name
        global acct_number
        acct_name = input('Account Name: ')
        open_bal = input('Opening Balance: ')
        acct_type = input('Account Type: ')
        acct_email = input('Account Email Address: ')
        # defining the account number
        length = 10
        random.choice(string.digits)
        random_gen = ''.join(random.choice(string.digits) for i in range(length))
        acct_number = random_gen
        # saving details to customer file
        fh = open('customer.txt', 'a')
        fh.write(f'{acct_number} {acct_name} {open_bal} {acct_type} {acct_email}\n')
        fh.close()

        print(f'Account successfully created! The account number is: {acct_number}')
        # logging user actions
        fh = open('session.txt', 'a+')
        fh.write(f'New customer account {acct_name} : {acct_number} created\n')
        fh.close()
        staff_access()

    def check_account():
        print('-----------Check Account------------')

        # changes txt file to dictionary
        with open('customer.txt', 'r') as document:
            customer = {}
            for line in document:
                line = line.split()
                if not line:  
                    continue
                customer[line[0]] = line[1:]

        check = input('Input Account number: ')
        try:
            for i in customer:
                if customer[check] == customer[i]:
                    print(f'Account Details:\n Account name: {customer[i][0]}\n Balance: {customer[i][1]}\n Account Type: {customer[i][2]}\n Email: {customer[i][3]}\n')
                    fh = open('session.txt', 'a+')
                    fh.write(f'checked account details of account: {check}\n')
                    fh.close()
                    staff_access()
        except:
            print('invalid account number')
            print('Try again ---> 1')
            print('Staff menu ----> 2')
            again = input('>: ')
            if again == '1':
                check_account()
            elif again == '2':
                staff_access()
            else:
                check_account
            

    start_page()


main()
