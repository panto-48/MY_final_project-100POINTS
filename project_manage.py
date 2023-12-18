# import database module
from database import Database  
from database import Table
from datetime import datetime
# define a funcion called initializing

def initializing():
# here are things to do in this function:
    # create an object to read all csv files that will serve as a persistent state for this program
    # create all the corresponding tables for those csv files
    # see the guide how many tables are needed
    # add all these tables to the database : Sorry, I don't understand the instruction

    filename = 'persons.csv'  #Because we need to only read our prepare file so we don't need to let user decise
    persons_csv = Database(filename)
    person_list = persons_csv.open_csv_file()

    filename2 = 'login.csv'
    login_csv = Database(filename2)
    login_list = login_csv.open_csv_file()


    # from database import Table

    # persons_table = Table.insert_operation( 'Persons',person_list , login_list )
    # ### change_role = Table.insert_operation( 'Persons',person_list , login_list , Entry = input(""))
    # login_table = Table.insert_operation( 'Login',person_list , login_list)
    # project_table = Table.insert_operation( 'Project',person_list , login_list ) # THIS Entry = Username for input User
    # # project_view = Table.insert_operation( 'View_project',person_list , login_list ,Entry )
    # Advisor_request_table = Table.insert_operation( 'Advisor_pending_request',person_list , login_list)
    # Member_request_table = Table.insert_operation( 'Member_pending_request',person_list , login_list)
    return filename,filename2,persons_csv,login_csv,person_list,login_list


# define a funcion called login

def login():
# here are things to do in this function:
   # add code that performs a login task
        # ask a user for a username and password
        # returns [ID, role] if valid, otherwise returning None
    User_Username = input('Enter your username : ')
    User_password = input('Enter your password : ')
    
    Username_box = []
    Username_pass = {}
    User_ID = {}
    User_Role = {}
    login_table = Table.insert_operation( 'Login',person_list , login_list)
    for entry in login_table:
        Username_box.append(entry['Username'])
        Username_pass[entry['Username']] = entry['Password']
        User_ID[entry['Username']] = entry['ID']
        User_Role[entry['Username']] = entry['Role']

    if User_Username in Username_box and User_password == Username_pass[User_Username]:
        return User_ID[User_Username] , User_Role[User_Username]
    else :
        return('Incorrect Username or Password , please try again later.')

# define a function called exit
def exit():
    pass# sorry I don't know how to do it to be honest this is the first time I know we can modify CSV file form python IDE

# here are things to do in this function:
   # write out all the tables that have been modified to the corresponding csv files


# make calls to the initializing and login functions defined above

answer_lock = ['y','n']
project_lock = ['ProjectID', 'Title', 'Lead' , 'Member1' , 'Member2' , 'Advisor' , 'Status']
filename,filename2,persons_csv,login_csv,person_list,login_list = initializing()
persons_table = Table.insert_operation( 'Persons',person_list , login_list )
login_table = Table.insert_operation( 'Login',person_list , login_list)
Project_list = []
Advisor_request_list = []
Member_request_list = []
To_evaluate = []

Do_you_enough = 'n'
while Do_you_enough != 'y':
    val = login()
    print(val)
    # based on the return value for login, activate the code that performs activities according to the role defined for that person_id

    if val[1] == 'admin':
        #see and do admin related activities
        table_choice = ''
        admin_eye = input('Which table you need to see and modify [1/2/3/4/5] : \n1.persons_table \n2.login_table \n3.project_table \n4.Advisor_request_table \n5.Member_request_table \nYour choice : ')
        if admin_eye == "1" :
            table_choice = 'persons_table'
        elif admin_eye == '2':
            table_choice = 'login_table' 
        elif admin_eye == '3':
            table_choice = 'project_table'
        elif admin_eye == '4':
            table_choice = 'Advisor_request_table'
        elif admin_eye == '5':
            table_choice = 'Member_request_table'
        else :
            print('Incorrect Choice') 

        for n in table_choice:
            print(n)
        admin_hands_choice = input('You want to modify it or not ?[y/n] : ')
        if admin_hands_choice == 'y':
            entry_choice2 = Table.update_entry(table_choice)
        elif admin_hands_choice == 'n':
            pass
        else :
            print('Incorrect choice')

    elif val[1] == 'student':
        # see and do student related activities
        # Student Task1 : See someone want you to become member or not
        # Student Task2 : Accept or deny request
        Check_box = []
        Use_later = ''
        for to_be_member in Member_request_list :
            if to_be_member['to_be_member'] == val[0]:
                Check_box.append(to_be_member)
            else :
                pass
        n=0
        for each_things in Check_box:
            n += 1
            print(f'{n}. {each_things}')
        if Check_box != []:
            choose_one = input("Which one do you want to answer : ")
            number_of_list = int(choose_one) - 1
            request_answer = input("Will you join or not?[y,n] : ")
            while request_answer not in answer_lock:
                request_answer = input("Sorry your answer is incorrect please retry \nWill you join or not?[y,n] : ")
            if request_answer == 'y':
                for modify_member in Member_request_list :
                    if modify_member['to_be_member'] == val[0]:
                        modify_member['Response'] = 'Yes'
                        modify_member['Response_date'] = datetime.now()
                        Use_later = modify_member['to_be_member']
                        for modify_project in Project_list :
                            if Use_later == modify_project['ProjectID']:
                                if modify_project['Member1'] == None:
                                    modify_project['Member1'] = val[0]
                                else :
                                    modify_project['Member2'] = val[0]
                            else :
                                pass
                    else :
                        pass                   
                    for all_people in persons_table:
                        if all_people['ID'] == val[0]:
                            all_people['type'] = 'member'
                        else :
                            pass
                    for all_login in login_list :
                        if all_login['ID'] == val[0]:
                            all_login['Role'] = 'member'
                    else :
                        pass
            elif request_answer == 'n':
                print('thank you for your answer')
                for modify_member in Member_request_list :
                    if modify_member[2] == val[0]:
                        modify_member['Response'] = 'No'
                        modify_member['Response_date'] = datetime.now()
        else :
            print('no request')
        # Student task3 : Become the lead
            Build_da_project = input('Do you want to build the Project or not?[y/n] : ')
            while Build_da_project not in answer_lock:
                print('Invalid Answer,please try again.')
                Build_da_project = input('Do you want to build the Project or not?[y/n] : ')
            if Build_da_project == 'y':
                Check_the_status = []
                if len(Check_box) != 0:
                    for all_status in Check_box[2]:
                        Check_the_status.append(all_status)
                    for all_answer in Check_the_status:
                        if all_answer != 'n':
                            Can_be_lead = 'No'
                            print('Sorry ,You need to deny all member requests first')
                        if all_answer == n :
                            Can_be_lead = 'yes'
                    if Can_be_lead == 'yes':
                        New_project01 = Table.insert_operation( 'Project',person_list , val[0] )
                        Project_list.append(New_project01)
                        print(New_project01)
                        more_member = input('Do you need more member?[y/n] : ')
                        while more_member not in answer_lock:
                            more_member = input('Sorry your answer are invalid \nDo you need more member?[y/n] : ')
                        if more_member == 'y':
                            New_member = Table.insert_operation('Member_pending_request',person_list , login_list)
                            Member_request_list.append(New_member)
                            print(New_member)
                        else :
                            print('Thank you for your respond')
                    elif Can_be_lead == 'No':
                        pass
                else :
                    New_project01 = Table.insert_operation( 'Project',person_list , val[0] )
                    Project_list.append(New_project01)
                    print(New_project01)
                    more_member = input('Do you need more member?[y/n] : ')
                    while more_member not in answer_lock:
                        more_member = input('Sorry your answer are invalid \nDo you need more member?[y/n] : ')
                    if more_member == 'y':
                        New_member = Table.insert_operation('Member_pending_request',person_list , login_list)
                        Member_request_list.append(New_member)
                        print(New_member)
                    else :
                        print('Thank you for your respond')
                    
            elif Build_da_project == 'n':
                pass

    elif val[1] == 'member':
        #see and do member related activities
        #member task 1 : See and modify his project details
        Check_box2 = []
        for All in Project_list :
            if (All['Member1'] == val[0] or All['Member1'] == val[0]) and All['Status'] != 'Finished':
                Check_box2.append(All)
            elif All['Member1'] != val[0] and All['Member1'] != val[0]:
                pass
        if len(Check_box2) != 0 :
            Number = 0
            for eachproject2 in Check_box2 :
                Number += 1
                print(f'{Number}.{eachproject2}')
            member_choose_one_project = input('which one do you want to see ?[0:for none] : ')
            if member_choose_one_project == '0':
                pass
            elif member_choose_one_project != '0':
                project_index = int(member_choose_one_project) - 1
                print(Check_box2[project_index])
                modify_title = input('do you want to modify title or not [y/n]? : ')
                while modify_title not in answer_lock:
                    print('Sorry, you answer are invalid,please try again.')
                    modify_title = input('do you want to modify title or not [y/n]? : ')
                if modify_title == 'y':
                    for all_project in Project_list :
                        if Project_list['ProjectID'] == Check_box2[project_index]['ProjectID'] :
                            New_title = input('New title : ')
                            Project_list['Title'] = New_title
                        else :
                            pass
                elif modify_title == 'n':
                    print('Thank you for you answer.')
        else :
            pass

    elif val[1] == 'lead':
        #see and do lead related activities
        choice_lock = [0,1,2,3,4,5]
        lead_choice = input('What do you want to do? :\n0.None\n1.Create new Project\n2.Invite more members\n3.Modify your project\n4.Invite Advisor\n5.Summit final Project')
        if lead_choice not in choice_lock :
            print('Sorry your answer is invalid please try again.')
            lead_choice = input('What do you want to do? :\n0.None\n1.Create new Project\n2.Invite more members\n3.Modify your project\n4.Invite Advisor\n5.Summit final Project')
        
        if lead_choice == '0':
            pass

        #lead task 1 : Create a new project
        elif lead_choice == '1':
            New_project02 = Table.insert_operation( 'Project',person_list , val[0] )
            Project_list.append[New_project02]
            print(New_project02)
            more_member = input('Do you need more member?[y/n] : ')
            while more_member not in answer_lock:
                more_member = input('Sorry your answer are invalid \nDo you need more member?[y/n] : ')
            if more_member == 'y':
                New_member = Table.insert_operation('Member_pending_request',person_list , login_list)
                Member_request_list.append(New_member)
                print(New_member)
            else :
                print('Thank you for your respond')

        #lead task 2 : Send invitational messages to potential members & Add members to the project and form a group
        elif lead_choice == '2':
            Check_box_for_project = []
            for All in Project_list :
                if All['Lead'] == val[0] or All['Lead'] == val[0]:
                    Check_box_for_project.append(All)
                elif All['Lead'] != val[0] and All['Lead'] != val[0]:
                    pass
            if len(Check_box_for_project) != 0 :
                Number = 0
                for eachproject3 in Check_box_for_project :
                    Number += 1
                    print(f'{Number}.{eachproject3}')
                lead_choose_one_project = input('which one do you want to modify ?[0:for none] : ')
                if lead_choose_one_project == '0':
                    pass
                elif lead_choose_one_project != '0' and lead_choose_one_project <= Number and int(lead_choose_one_project)>0 :
                    project_index = int(lead_choose_one_project) - 1
                    print(Check_box_for_project[project_index])
                    if Check_box_for_project[project_index]['Member1'] != None and Check_box_for_project[project_index]['Member2'] != None :
                        pass
                    else :
                        your_project_ID = Check_box_for_project[project_index]['ProjectID']
                        More2_member = Table.insert_operation('Member_pending_request',person_list , your_project_ID)
                        Member_request_list.append(More2_member)
                else :
                    print('Your answer Invalid , please try again or contact us')
            
        #lead task 3 : See and modify his own project details
        elif lead_choice == '3':
            Check_box2 = []
            for All in Project_list :
                if (All['Lead'] == val[0] or All['Lead'] == val[0]) and All['Status'] != 'Finished':
                    Check_box2.append(All)
                elif All['Lead'] != val[0] and All['Lead'] != val[0]:
                    pass
            if len(Check_box2) != 0 :
                Number = 0
                for eachproject2 in Check_box2 :
                    Number += 1
                    print(f'{Number}.{eachproject2}')
                lead_choose_one_project = input('which one do you want to see ?[0:for none] : ')
                if lead_choose_one_project == '0':
                    pass
                elif lead_choose_one_project != '0' and lead_choose_one_project <= Number and int(lead_choose_one_project)>0 :
                    project_index = int(lead_choose_one_project) - 1
                    print(Check_box2[project_index])
                    modify_project = input('do you want to modify project or not [y/n]? : ')
                    while modify_project not in answer_lock:
                        print('Sorry, you answer are invalid,please try again.')
                        modify_project = input('do you want to modify project or not [y/n]? : ')
                    if modify_project == 'y':
                        which_project_value_to_modify = input('Which key you want to modify?[input key name] : ')
                        while which_project_value_to_modify not in project_lock:
                            print('Sorry your key not found,please try again.')
                            which_project_value_to_modify = input('Which key you want to modify?[input key name] : ')
                        for all_project in Project_list :
                            if Project_list['ProjectID'] == Check_box2[project_index]['ProjectID'] :
                                New_value = input('New value : ')
                                Project_list[which_project_value_to_modify] = New_value
                            else :
                                pass
                    elif modify_project == 'n':
                        print('Thank you for you answer.')
                else :
                    print('Your answer Invalid , please try again or contact us')
            
        # lead task 4 : Send request messages to potential advisors
        elif lead_choice == '4':
            #see all you project
            Check_box_for_project = []
            for All in Project_list :
                if All['Lead'] == val[0] or All['Lead'] == val[0]:
                    Check_box_for_project.append(All)
                elif All['Lead'] != val[0] and All['Lead'] != val[0]:
                    pass
            if len(Check_box_for_project) != 0 :
                Number = 0
                for eachproject3 in Check_box_for_project :
                    Number += 1
                    print(f'{Number}.{eachproject3}')
                lead_choose_one_project = input('which one do you want to modify ?[0:for none] : ')
                if lead_choose_one_project == '0':
                    pass
                elif lead_choose_one_project != '0' and lead_choose_one_project <= Number and int(lead_choose_one_project)>0 :
                    project_index = int(lead_choose_one_project) - 1
                    print(Check_box_for_project[project_index])
                    if Check_box_for_project[project_index]['Advisor'] == None :
                        your_project_ID = Check_box_for_project[project_index]['ProjectID']
                        Request_advisor = Table.insert_operation( 'Advisor_pending_request',person_list , your_project_ID)
                    elif Check_box_for_project[project_index]['Advisor'] != None :
                        print('This project already had advisor.')
                else :
                    print('Your answer Invalid , please try again or contact us')
            else :
                pass

        #lead tas 5 : Submit the final project report
        elif lead_choice == '5':
            Check_box_for_project = []
            for All in Project_list :
                if All['Lead'] == val[0] or All['Lead'] == val[0]:
                    Check_box_for_project.append(All)
                elif All['Lead'] != val[0] and All['Lead'] != val[0]:
                    pass
            if len(Check_box_for_project) != 0 :
                Number = 0
                for eachproject3 in Check_box_for_project :
                    Number += 1
                    print(f'{Number}.{eachproject3}')
                lead_choose_one_project = input('which one do you want to modify ?[0:for none] : ')
                if lead_choose_one_project == '0':
                    pass
                elif lead_choose_one_project != '0'and int(lead_choose_one_project) <= Number and int(lead_choose_one_project)>0  :
                    project_index = int(lead_choose_one_project) - 1
                    interested_project = Check_box_for_project[project_index]
                    print(interested_project)
                    your_project_ID = Check_box_for_project[project_index]['ProjectID']
                    if interested_project['Status'] == 'Approved':
                        print('caution!!! you will unable to modify your project after sent')
                        satisfied_yet = input("Are you ready to send your project or not? [y/n] : ")
                        while satisfied_yet not in answer_lock :
                            print('Sorry invalid answer please try again.')
                            satisfied_yet = input("Are you ready to send your project or not? [y/n] : ")
                        if satisfied_yet == 'y':
                            interested_project['Status'] = 'Finished'
                        elif satisfied_yet == 'n':
                            print('Thankyou ,If you change your mind you can always come back.')
                else :
                    print('Your answer Invalid , please try again or contact us')
            else :
                pass

    elif val[1] == 'faculty':
        #see and do faculty related activities
        Im_inadvisorver = []
        for each_advice in Advisor_request_list :
            if each_advice['to_be_advisor'] == val[0]:
                Im_inadvisorver.append(each_advice)
            else :
                pass
        # faculty task 1 : See request to be a supervisor
        Numberanswer = 0
        for all_advice_request in Im_inadvisorver :
            Numberanswer += 1
            print(f'{Numberanswer}. {all_advice_request}')
        # faculty task 2 : Send response denying to serve as an advisor
        Answer_advice_request_index = input('Which one do you need to answer?[0:for none] : ')
        if Answer_advice_request_index == '0':
            pass
        elif Answer_advice_request_index != '0' and int(Answer_advice_request_index) <= Numberanswer and int(Answer_advice_request_index)>0  :
            request_index = int(Answer_advice_request_index) - 1
            interested_request = Im_inadvisorver[request_index]
            Which_request = interested_request['ProjectID']
            for this_one_request in Advisor_request_list:
                if this_one_request['ProjectID'] == Which_request:
                    your_answer = input(" Do you agree to be this project's Advisor or not? [y/n] : ")
                    while your_answer not in answer_lock :
                        print('Sorry,Your answer is invalid,please try again.')
                        your_answer = input(" Do you agree to be this project's Advisor or not? [y/n] : ")
                        if your_answer == 'y':
                            this_one_request['Response'] = 'Yes'
                            this_one_request['Response_date'] = datetime.now() 
                            for all_people in persons_table:
                                if all_people['ID'] == val[0]:
                                    all_people['type'] = 'Advisor'
                                else :
                                    pass
                            for all_login in login_list :
                                if all_login['ID'] == val[0]:
                                    all_login['Role'] = 'Advisor'
                            Use_later2 = this_one_request['to_be_advisor']
                            for modify_project2 in Project_list :
                                if Use_later2 == modify_project2['ID']:
                                    modify_project2['Advisor'] = val[0]
                                else :
                                    pass
                        elif your_answer == 'n':
                            this_one_request['Response'] = 'No'
                            this_one_request['Response_date'] = datetime.now() 
                else :
                    pass
        else :
            print('Your answer Invalid , please try again or contact us')
        
        #faculty task 4 : Evaluate projects
            if len(To_evaluate) != 0 :
                NNN = 0
                for all_evaluate in To_evaluate:
                    NNN += 1
                    print(f'{NNN}. {all_evaluate}')
                choose_2_evaluate = input('Which one do you want to evaluate : ')
                while int(choose_2_evaluate) > len(To_evaluate) and int(choose_2_evaluate) < 0 and int(choose_2_evaluate) != 0 :
                    print('Invalid choice please try again')
                    choose_2_evaluate = input('Which one do you want to evaluate : ')
                project_index = int(choose_2_evaluate) - 1
                Your_Answer = input('Do you approve this project or not ? [y/n] : ')
                while Your_Answer not in answer_lock :
                    print('Sorry your answer is invalid,please try again.')
                    Your_Answer = input('Do you approve this project or not ? [y/n] : ')
                if Your_Answer == 'y':
                    To_evaluate.append('y')
                elif Your_Answer == 'n':
                    To_evaluate.append('n')
            else : pass

    elif val[1] == 'advisor':
        #see and do advisor related activities
        #Advisor task1 : See details of all the project
        will_choose = []
        for all_project in Project_list :
            Number_in_project = 0
            if all_project['Advisor'] == val[0]:
                Number_in_project += 1
                will_choose.append(all_project)
                print(f'{Number_in_project}. {all_project}')
            else :
                pass
        #Advisor task2 : Send project to Evaluate 
        if len(will_choose) != 1 :
            choose_which_one = input('Which one you want to modify[0 for exit] : ')
            while int(choose_which_one) > len(will_choose) and int(choose_which_one) < 0 and int(choose_which_one) != 0 :
                print('Invalid choice please try again')
                choose_which_one = input('Which one you want to modify[0 for exit] : ')
            project_index = int(choose_which_one) - 1
            Small_list = []
            Answer_list = []
            Answer_list.append('y')
            Small_list.append(will_choose[project_index])
            Small_list.append(Answer_list)
            To_evaluate.append('Small_list')
        #Advisor task3 : Approved
        All_faculty = []
        Last_Step = []
        for All_ in person_list:
            if All_['type'] == 'faculty':
                All_faculty.append(All_)
            else :
                pass
        for All_relate_project in To_evaluate :
            if All_relate_project[0]['Adviser'] == val[0]:
                for all_answer in All_relate_project[1]:
                    you_pass = 0
                    if All_relate_project[1] == 'y':
                        you_pass += 1
                    else :
                        pass
                if you_pass > int((len(All_faculty)*(80/100))):
                    Last_Step.append[All_relate_project]
                else :
                    pass
            else: 
                pass
        for All_pass_project in Last_Step :
            Using = All_pass_project['ProjectID'] 
            for All_project in Project_list :
                if All_project['ID'] == 'Using':
                    All_project['Status'] = 'Finished'
                else:
                    pass
    
    print()
    print()
    Do_you_enough = input('Do you enough yet?[y/n] : ')
    while Do_you_enough not in answer_lock:
        print('Invalid Answer,please try again')

# once everyhthing is done, make a call to the exit function
exit()


