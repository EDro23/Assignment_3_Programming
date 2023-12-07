# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 09:51:44 2023

@author: ethan.drover
"""

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

def title():
    print("Monthly Sales program\n")

def menu():
    print("COMMAND MENU\n")
    print("view \t- View sales for specified month")
    print("edit \t- Edit sales for specified month")
    print("totals \t- View sales summary for year")
    print("exit \t- Exit program\n")

def read_sales():
    monthly_sales = {}
    try:
        with open('monthly_sales.txt', 'r') as rfh:
            for line in rfh:
                if line.strip():
                    month, sale = (item.strip() for item in line.split('\t'))
                    monthly_sales[month.lower()] = float(sale)
    except FileNotFoundError:
        pass
    except ValueError:
        print("Invalid data format in the file.")
        monthly_sales = {}
        
    return monthly_sales

def write_sales(file_path, sales):
    with open(file_path, 'w') as wfh:
        for month, sale in sales.items():
            wfh.write(f"{month.lower()}\t{sale:.2f}\n")

def view_sales(sales, month):
    if month.lower() in sales:
        print(f"Sales amount for {month} is {sales[month.lower()]:.2f}")
    else:
        print("Invalid three-letter month.")

def edit_sales(sales, month, amount):
    if month.lower() in sales:
        sales[month.lower()] = float(amount)
        print(f"Sales amount for {month.capitalize()} is {sales[month.lower()]:,.2f}.")
    else:
        print("Invalid three-letter month.")        

def main():
    title()
    menu()
    
    while True:
        command = input("Command: ").lower()
        sales = read_sales()
        
        if command == 'view':
            month_input = input("Three-letter Month: ")
            view_sales(sales, month_input)
        elif command == 'edit':
            month_input = input("Three-letter Month: ")
            amount_input = input("Sales Amount: ")
            edit_sales(sales, month_input, amount_input)
            write_sales('monthly_sales.txt', sales)
        elif command == 'totals':
            # Implement the logic for viewing sales summary for the year
            pass
        elif command == 'exit':
            print("Exiting program.")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == '__main__':
    main()