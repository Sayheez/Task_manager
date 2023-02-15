# A program to manage tasks assigned to each member in a team 
# This is an example Python program
# The program then outputs different tasks using using a variable, input, for loop, and if/else statement, reading from a file with open() functions and lower() method


#=====importing libraries===========khc
'''This is the section where you will import libraries'''
# Import sys module to use exit() method
import os

# Import datetime module to get current date
import datetime
from datetime import date

# To find the number of tasks for each user
from collections import Counter  

# Import sys module to use exit() method
from sys import exit

# function to register a user
def reg_user():
    new_user = input("Enter your user name for registration: \n").lower()
    new_pword = input("Please enter your password for registration: \n").lower()
    confirm_pword = input("Please confirm your password for registration: \n").lower()
    
    # add_user_file()
    if new_pword == confirm_pword:
        with open("user.txt", "r") as add_user:
            line = add_user.read()
            
            # The if statement checks for user name that already exist and print a message to use another name
            if new_user in line:
                print(f"The user name already exists in the database\nTry using another name")
            else:
                with open("user.txt", "a") as add_user:
                    add_user.write(f"\n{new_user}, {new_pword}")
    else:
        print(f"Your new password: {new_pword}, or confirm password: {confirm_pword} are not matching, please try again")

        
# function to add a new task
def add_task():
    task_name = input("Enter the user name of the person task is assigned to: \n")
    task_title = input("Enter the title of the task: \n")
    task_desc = input("Enter the description of the task: \n")
    task_date = date.today().strftime("%d %b %Y")
    task_due_date = input("Enter the date that task would be due, for example 10 Nov 2022:  \n")

    # add_task_file()
    with open("tasks.txt", "a") as add_user:
        add_user.write(f"{task_name}, {task_title}, {task_desc}, {task_date}, {task_due_date}, No")
        add_user.write('\n')


# function to view all tasks
def view_all():
    split_line = []                           # List for all tasks
    with open("tasks.txt", "r") as read_file:
        lines = read_file.readlines()
        for line in lines:
            split_line = line.strip().split(", ")
            print(f""" 
            ------------------------------------------------------------------------------------------------
                Task:                  {split_line[1]}
                Assigned to:           {split_line[0]}
                Task description:      {split_line[2]}
                Date assigned:         {split_line[3]}
                Due date:              {split_line[4]}
                Task Complete?:        {split_line[5]}
            ------------------------------------------------------------------------------------------------
            """)


# function to view my tasks
def view_mine():
    split_lines = []                                          # List for all tasks
    vm_list = []                                              # List for a user tasks
    with open("tasks.txt", "r") as read_file:
        for index, line in enumerate(read_file):
            split_line = line.strip().split(", ")
            split_lines.append(split_line)

            if user_login == split_line[0].lower():
                vm_list.append(line.strip().split(", "))
    
                print(f""" 
                ------------------------------------------------------------------------------------------------
                    Task:                  {split_line[1]}
                    Assigned to:           {split_line[0]}
                    Task description:      {split_line[2]}
                    Date assigned:         {split_line[3]}
                    Due date:              {split_line[4]}
                    Task Complete?:        {split_line[5]}
                ------------------------------------------------------------------------------------------------
                """)
    
    while True:
        questn = int(input("Please enter the task number you would like to edit or mark as complete? -1 to exit\n")) - 1
        if (questn + 1) == -1:
            break
        elif questn != -1:
            try:
                if vm_list[questn] in vm_list and vm_list[questn][5] == "Yes":
                    print("This task has been marked as completed and cannot be edited.")
                    break
            except:
                print(ValueError("This task number does not exist. Index out of bound"))
                break
             
            else:
                user_decision = input("""Select either of the following option below:
                                            mark - Mark the task as complete
                                            edit - Edit the task
                                        """).lower()
                
                if user_decision == "mark":
                    for i in split_lines:
                        if i == vm_list[questn]:
                            i[5] = "Yes"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                            
                    print(split_lines)
                    with open("tasks.txt", "w") as vm_file:
                        for item in split_lines:
                            # vm_file.write("%s\n" % item)
                            vm_file.write("%s\n" %  ', '.join(item))
        

                elif user_decision == "edit":                
                    completed = input("Please enter Yes if you want to mark the task as complete\n")
                    new_name = input("Please enter new name of the person you want to re-assign the task\n")
                    new_date = input("Enter the new date that task would be due, for example 10th Nov 2022:  \n")

                    vmt = f"""
                        ------------------------------------------------------------------------------------------------
                                Task:                  {vm_list[questn][1]}
                                Assigned to:           {new_name}
                                Task description:      {vm_list[questn][2]}
                                Date assigned:         {vm_list[questn][3]}
                                Due date:              {new_date}
                                Task Complete?:        {completed}
                        ------------------------------------------------------------------------------------------------
                        """

                    task_update = f"{new_name}, {vm_list[questn][1]}, {vm_list[questn][2]}, {vm_list[questn][3]}, {new_date}, {completed}"
                    
                    for index, val in enumerate(split_lines):
                        if val == vm_list[questn]:
                            position = index
                    
                    split_lines[position] = task_update                  # Add the specific updated task back into the all tasks list
                     

                    with open("tasks.txt", "w") as teks:
                        for line in split_lines:
                            if task_update == line:
                                teks.write(''.join(task_update) + '\n')
                            else:
                                teks.write(', '.join(line) + '\n')
                           

# Generate the task overview text file.
def generate_reports():
  
    with open('tasks.txt', 'r') as tasks_file_content:
        tasks_file = tasks_file_content.readlines()
        num_tasks_recorded = len(tasks_file)
        num_tasks_completed = 0
        num_tasks_uncompleted = 0
        num_tasks_uncompleted_overdue = 0
        user_assigned_list = []

        # For each line in the file, split it by comma space to create a list
        for line in tasks_file:
            line = line.strip().split(", ")
            user_assigned_list.append(line[0])
            completed = line[5]
            # If the task is complete, increase the value for completed task by 1 on each iteration
            if completed == "Yes":
                num_tasks_completed += 1

            else:
                num_tasks_uncompleted += 1
                current_date = datetime.datetime.today()
                due_date_str = line[4]
                due_date_obj = datetime.datetime.strptime(due_date_str, "%d %b %Y")
                # If the current date is bigger than the task's due date object
                # Increase the value for overdue tasks by 1 on each iteration
                if current_date > due_date_obj:
                    num_tasks_uncompleted_overdue += 1

        # Calculate the percentage of uncompleted and the percentage of overdue tasks as uncompleted tasks
        percentage_tasks_uncompleted = round(num_tasks_uncompleted / num_tasks_recorded * 100, 2)
        percentage_tasks_overdue = round(num_tasks_uncompleted_overdue / num_tasks_recorded * 100, 2)

    # Add all above results to this file
    with open("task_overview.txt", "w") as task_overview:
        task_overview.write(f'''{"Task Overview:":^50}
    Total number of tasks recorder:                       {num_tasks_recorded}
    Total number of completed tasks:                      {num_tasks_completed}
    Total number of asks that haven't been completed:     {num_tasks_uncompleted}
    Total number of tasks that haven't been completed 
    and are now overdue:                                  {num_tasks_uncompleted_overdue}
    The percentage of tasks that are incomplete:          {percentage_tasks_uncompleted}%
    The percentage of tasks that are overdue:             {percentage_tasks_overdue}%
''')

    # Get number of registered users
    with open('user.txt', 'r') as users_file_content:
        users_file = users_file_content.readlines()
        num_users_registered = len(users_file)


    # Write the information about users registered and task recorded in a user-friendly format.
    with open("user_overview.txt", "w") as user_overview:
        user_overview.write(f'''{"User Overview:":^50}
    Total number of users registered:                     {num_users_registered}
    Total number of tasks recorder:                       {num_tasks_recorded}\n
''')
    # Count how many tasks are assigned to each user with function counter. This will also create a dictionary that
    # will have the usernames as keys and the frequency of that name as the value
    num_tasks_per_user = Counter(user_assigned_list)

    # For each key and value in the dictionary created above
    # Set the username as the key, the num of tasks per user as the value
    # Calculate the percentage of tasks assigned to each user out of the total number of tasks recorded
    # Set the completed tasks and overdue tasks to 0
    for key, value in num_tasks_per_user.items():
        user_name = key
        user_num_tasks = value
        user_task_percentage = round(user_num_tasks / num_tasks_recorded * 100, 2)
        user_num_task_completed = 0
        user_num_tasks_uncompleted_overdue = 0

        # For each line in the task file, create a list by splitting the line at comma space
        for line in tasks_file:
            line = line.split(", ")

            # For each username iteration, find the task that has been assigned to that user
            if line[0].strip("\n") == user_name:
                # If the task is marked as completed (elem at index 5 in the line has the value of 'Yes')
                # Increase the number of completed tasks by 1
                if line[5].strip("\n") == "Yes":
                    user_num_task_completed += 1
                # Otherwise (if the task is not marked as completed)
                # Get the current date (today's date) and the task's due date (represented by elem at index 4 in the
                # list)
                # Create a date object from the due date string and store it in the desired format
                else:
                    current_date = datetime.datetime.today()
                    due_date_str = line[4]
                    due_date_obj = datetime.datetime.strptime(due_date_str, "%d %b %Y")

                    # If the current date is bigger than the task's due date object
                    # Increase the value for overdue tasks by 1 on each iteration
                    if current_date > due_date_obj:
                        user_num_tasks_uncompleted_overdue += 1

        # Caculate the perccentage of tasks the user has completed out of all the tasks assigned to that user
        # Find the percentage of tasks the user has not completed by subtracting the percentage of completed tasks from
        # 100%
        # # Find the percentage of tasks the user has not completed and are overdue
        user_task_percentage_completed = round(user_num_task_completed / user_num_tasks * 100, 2)
        user_task_percentage_uncompleted = 100 - user_task_percentage_completed
        user_task_percentage_overdue = round(user_num_tasks_uncompleted_overdue / user_num_tasks * 100, 2)

        # Open the user overview file in writing mode (or create and open if this does not exist yet)
        # Write all the information gathered above in a user-friendly format
        with open("user_overview.txt", "a") as user_overview:
            user_overview.write("\n")

    # Print success message
    print(f' Two reports have been successfully generated for user_overview and task_overview!')         


# Displaying only admin specific statistics to the screen.
def display_statistics():
    # If a text file is empty, run the generate_reports() function
    # Open 'task_overview.txt' and "user_overview.txt' files in reading mode

    if os.path.getsize("user_overview.txt") == 0 or os.path.getsize("task_overview.txt") == 0:
        generate_reports()

    # Read all the information from each file and display it under the "Statistics" title
    with open("task_overview.txt", "r") as task_overview_file:
        task_overview = task_overview_file.read()
    with open("user_overview.txt", "r") as user_overview_file:
        user_overview = user_overview_file.read()
    print(f'''
             ************************************************
                                       |  Statistics  |
                                       
                     {task_overview}
     
     
                     {user_overview}
             ************************************************
    ''')

  



#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''


# Define an empty dictionary variable
users_dictionary = {}

# Read from the user text file and store each name with password as a key, value pair in the dictionary
with open("user.txt", "r") as f:
    for line in f:
        (key, val) = line.strip().split(", ")
        users_dictionary[key] = val

while True: 
    # Take input from user for their login name and password
    user_login = input("Enter your login name: \n").lower()
    user_pword = input("Enter your password: \n").lower()
    
    print("Dictionary List of Users: ", users_dictionary)
    print(f"Present Login details: user_login, user_pword")

    # Check if the user input is users_dictionary, allow user to see menu section if their details entered matched or keep asking them to enter their login and password
    if user_login not in users_dictionary:
        print("The login name you entered is Invalid\n")
        continue
    elif user_pword not in users_dictionary.values():
        print("Login name is valid but the password you entered is Invalid\n")
        continue
    else: 
        print(f"\nWelcome {user_login}, and You're logged in")

        # Keep a user login until the program is exited by entering "e"
        while True:
            menu = input('''Select one of the following Options below:
                        r     - Registering a user
                        a     - Adding a task
                        va    - View all tasks
                        vm    - view my task
                        gr    - generate reports
                        ds    - display statistics
                        e     - Exit 
                    ''').lower()

            if menu == 'r' and user_login == "admin":
                # call the reg_user function
                reg_user()
            elif menu == 'a':
                # call the add_task function
                add_task()      
            elif menu == 'va':
                # call the view_all function
                view_all() 
            elif menu == 'vm':
                # call the view_mine function
                view_mine()
            elif menu == 'gr':
                # call the generate_reports function
                generate_reports()
            elif menu == 'ds' and user_login == "admin":
                # call the display_statistics function
                display_statistics()
            elif menu == 'e':
                print('Goodbye!!!')
                exit()

            else:
                print("You have made a wrong choice, Please Try again")

