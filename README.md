For command-line interface (CLI) applications, 
Python packages including "Click" and "Typer" can be used. 
Due to the fact that this application is going to be used by people, 
perhaps providing them with a menu is a better approach here. 


### How to run this application?

There is a Dockerfile that can be used to run the program.

### Is the program configurable?

Yes. It is. There is a 'config.ini' file that provides different configurations.

Below are explanation of each option in config file:

```
[files_path]
deposits = Path of deposits JSON file
withdrawals = Path of withdrawals JSON file

[header]
header_text = Text printed at the top of page when program started.

[menu]
task_1_text = Title of task 1
task_2_text = Title of task 2
task_3_text = Title of task 3
exit_text = Title of exit option


[menu_accepted_options]
task_1_accepted = Accepted string if user enter it, the task 1 will be performed. 
                  It can be multiple options sepereated by ','.
task_2_accepted = Accepted string if user enter it, the task 1 will be performed. 
                  It can be multiple options sepereated by ','.
task_3_accepted = Accepted string if user enter it, the task 1 will be performed. 
                  It can be multiple options sepereated by ','.
exit_accepted = Accepted strings if user enter one of them, the task 1 will be performed. 
                  It can be multiple options sepereated by ','.

[user_input]
question_text = Title of asking user for enter the selected option.

[wrong_input]
Text of alerts that will be printed if user entered a incorrect option.
multiple alerts are acceptable.
...

[task_1]
result_title = Title of results for Task 1.
sorted = 1 provide sorted results, 0 allows to print unsorted result.
descending = if 'sorted' is 1; 
             1 here means it will be sorted in descending order. 
             0 means it will be sorted in ascending order.
customer_col_title = Title of 'Customer' column in expected output.
customer_col_size = Size of 'Customer' column in expected output.
balance_col_title = Title of 'Balance' column in expected output.
balance_col_size = Size of 'Balance' column in expected output.
adjuster = Adjuster that adjusts size of whole expected table.

[task_2]
requested_month = Number of requested month, 0 means all months.
result_title = Title of results for Task 2.
final_msg_per_category = The massege for each category in expected output.

[task_3]
requested_month = Number of requested month, 0 means all months.
result_title =T itle of results for Task 3.
final_msg_per_customer = The massege for each customer in expected output.

[are_you_done]
question_title = Title of the question of is user done or not.
user_input_title = Title of user choice getting. 
accepted_options = acceptable options to finish the program.  
```

## Assumptions

- A previous balance of zero for each customer is considered in task 1. However, all transactions are considered.
- Transactions outside of December month are ignored in task 2, 3.
