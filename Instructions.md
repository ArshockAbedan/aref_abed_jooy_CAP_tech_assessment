You are being asked to solve the practical problem of consuming, manipulating, and presenting data.
 
The json files, documented below, provides personal bank account transactions for a group of bank customers over the period of one month. The data includes both deposits and withdrawals.
 
* A deposit occurs when a customer credits (adds money to) their savings account to increase its balance.
* A withdrawal occurs when a customer debits (removes money from) their savings account to decrease its balance. A withdrawal can be one of three types: an ATM transaction (“ATM”), a bill payment (“Bill”), or a debit card purchase (“Debit Payment”).
* The bank permits its customers to overdraft their savings accounts. This means that the account balance can temporarily be less than $0.
 
You are required to build:
* A command-line tool that will query the read the files and return output to satisfy as many of the requirements below as possible.
 
Tasks:
1. Print a list of all customers who hold a savings account at this bank, and their final account balances at the end of the month (December 2017).
2. Print a list of the highest total spender in each payment category: ATM withdrawals, bill payments, and debit payments, within the month of December 2017 only. That is, the name of the person (or people) who charged the highest total over the course of the month on each payment category.
3. Print a list of all customers, who over drafted their account at any point in the month of December only. As a bonus, include the maximum overdraft balance for each customer, and the date on which it was reached.

 
### DEPOSITS
 
```
[
    {
        “customerName”: “John Smith”,
        “amount”: “100.00”,
        “time”: “2017-01-01 00:00:00”
    },
    ...
]
```
 
#### FIELDS
* customerName (string) : name of customer owning the savings account
* amount (string) : dollar amount of transaction (string to maintain precision)
* time (string) : timestamp of transaction in YYYY-MM-DD HH:MM:SS format
 
### WITHDRAWALS

```
[
    {
        “customerName”: “John Smith”,
        “amount”: “100.00”,
        “category”: “Debit Payment”,
        “time”: “2017-01-01 00:00:00”
    },
    ...
]
```
 
#### FIELDS
* customerName (string) : name of customer owning the savings account
* amount (string) : dollar amount of transaction (string to maintain precision)
* time (string) : timestamp of transaction in YYYY-MM-DD HH:MM:SS format
* category (string) : withdrawal type
    * Debit Payment
    * ATM
    * Bill
