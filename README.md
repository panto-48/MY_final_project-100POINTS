# Final project for 2023's 219114/115 Programming I
### 1. A list of files in your final project repo together with a brief description describing what classes each of the files contains and what purposes do these classes serve.
- database.py
    - Classes : Database , Table
    - purpose of these classes :
       1. Database :
                <br> processes orders and CSV files from Project_manage.py, transforming them into a nested list with each line representing an individual set.
       2. Table :
                <br> executes functions based on the user's role, each function designed to handle distinct tasks corresponding to different user roles. 
- project_manage.py
    > message :
    > "my project_manage.py doesn't has classes ,but it has some important function that use to work with classes in database.py, So I will describe about those function instead "'''
    - Function : initializing() , login() & if val[0]
    - purpose of those functions :
        1. initializing()
               <br>  Choose a file name and send that file name to database.py for import, convert, and send back to restored in project_manage.py variable (In my project the filename unable to modify outside IDE)
        2. login() & if val[0] :
               <br> handle user cyber safty and also instruct which function table class need to perform
- person.csv / login.csv
    - information that require for run the project
  
### 2. A description on how to compile and run your project.
  
  - Step to compile and run my project
<br>0. Fork and push this repo
<br>1. Compile and run the project_manage.py
<br>2. answer the Username and password (You can see in login.csv)
<br>3. Choose the choice for each tasks
<br>4. Answer the "Do_you_enough" question (y/n)
  > message : "because I missed 'the Exit function' so in order for me to test the task relate with project or request I need to use while-statement for help that why the 4-Step was created"

### 3. A table detailing each role and its actions, specifying the relevant methods and classes, and indicating the completion percentage of your code for a particular action in a given role. See an example table in the attached file.
| Role     | Action | Method     | Class | Completion Percentage |
|----------|--------|------------|-------|-----------| 
| admin     | see all the tables  | *(Regular access) with Project_list |- | 65%|
| admin     | Modify all the tables  | update_entry  |Table | 80%|
| student      | see the member request  | *(Regular access) with Member_request_list  | - | 95%|
| student | Accept or deny request | *(Regular access) with Member_request_list | Table | 90% |
| student | Build the Project | insert_operation( 'Project',... | Table | 90% |
| member | See and modify his project details | *(Regular access) with Project_list | - | 95% |
| lead | Create new project | insert_operation( 'Project',... | Table | 90% |
| lead | Send member request | insert_operation('Member_pending_request',.. | Table | 90% |
| lead | See and modify his own project details | *(Regular access) with Project_list | - | 95% |
| lead |  Send advisor request | insert_operation( 'Advisor_pending_request',... | Table | 90% |
| lead | Submit the final project report | *(Regular access) with Project_list  | - | 85% |
| faculty | See request to be a supervisor |  *(Regular access) with Advisor_request_list | - | 95% |
| faculty | Send respond | *(Regular access) with Advisor_request_list  | - | 95% |
| faculty | Evaluate projects | *(Regular access) with To_evaluate | - | 95% |
| advisor | See details of all the project |  *(Regular access) with Project_list  | - | 95% |
| advisor | Send project to Evaluate  | *(Regular access) with To_evaluate | - | 60% |
| advisor | Approved the project | *(Regular access) with Project_list | - | 50% |
  > message : "for clarify *(Regular access). I contain all the project , request(that had all information I need to perform the Action) in some list I build in project_manage.py so in reality I don't need to execute class function in order to do those Action that Method be *(Regular access)" except when I need to change User information('Role',etc.) <br> message2 : " also I build Table class to be all in one for every role , therefore for all tasks relate with role got execute in Table class"


### 4. A list of missing features and outstanding bugs, detailing actions for a particular role you have not implemented together with known bugs
  1. missing feature
      - The "Exit" function : to sent "modified python file" to be CSV.
  2.  outstanding bugs
      - None(Don't found yet)
      > message : "probably have but I doesn't found yet ,Because I doesn't test enough times" 
