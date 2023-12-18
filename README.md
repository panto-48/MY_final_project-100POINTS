# Final project for 2023's 219114/115 Programming I
## 1. A list of files in your final project repo together with a brief description describing what classes each of the files contains and what purposes do these classes serve.

### README.md
- Description to explain how my project how my code work
### Proposal.md
- Use to briefly plan how to do the Evaluate Step in very start of work(contain only the sentence not the code)
### TODO.md
- Use to plan What each Role need to do and which class , function are require
<br>*****Both TODO.md and Proposal.md are Written since the beginning of the project at the start stage so it not that accurate!!!
### database.py
- Most of relate Class work 
<br>1. Class Database : Start with change CSV file into nested list of dictionary (which CSV file and when to convent file depend on Project_manage.py)
<br>2. Class Table : Use to make Specific object depend on what are role of User (mostly make the dictionary)
### project_manage.py
- Most of relate User work
<br>1. import file and def initializing() : wait to get list that build from database.py 
<br>2. def login() : Recognize the User role to later execute specific task based on User role
<br>3. *spoiled alert this is my missing features : I don't know how to send python file related file to CSV file so I doesn't do this task
<br>  !!!BUT In order to test my project when has multiple people use continuous (multiple login) ,I modify my code to run until the Tester feel satisfied
### person.csv / login.csv
- both CSV file contained list of information that will end up in database.py to got transform to be nestedlist than contain multiple set

## 2. how to compile and run my project.
  - 1. Fork and push this repo
    2. All the work you need to do are in project_manage.py
    3. when you run the project_manage.py they will ask you Username and password
    4. Watch the Username and Password in login.csv
    5. Choose task you want my project to do
    6. if you satisfy input n(No) my project will stop working and you can execute it again whatever you want
<br> because I miss the Exit step so beware that when my project stop working your input will lost forever

## 3. A table
  - Sorry I don't know how to append the table to md file so I will add it in repo instead 

## 4. missing features and outstanding bugs
  - The Exit function to sent python file to be CSV
  - and for buck I doesn't found yet but I think It has somewhere
