# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file

import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# add in code for a Database class
class Database :
    def __init__(self,name):
        self.name = name

    def open_csv_file(self):
        persons = []
        with open(os.path.join(__location__, self.name )) as f:
            rows = csv.DictReader(f)
            for r in rows:
                persons.append(dict(r))
        return persons



# add in code for a Table class
class Table :
    def __init__(self,table_name):
        self.table_name = table_name
        self.Each_table = []

# modify the code in the Table class so that it supports the insert operation where an entry can be added to a list of dictionary
    Project_list = []
    Advisor_request_list = []
    Member_request_list = []
    To_evaluate = []

    def insert_operation (table_name,CSV_list1,CSV_list2):

        real_list = []

        if table_name == 'Persons':
            #key = ['ID', 'fist', 'last', 'type']
            for each_set in CSV_list1:
                each_dict = {}
                each_dict['ID'] = each_set['ID']
                each_dict['first'] = each_set['fist']
                each_dict['last'] = each_set['last']
                each_dict['type'] = each_set['type']
                real_list.append(each_dict)
            return real_list


        elif table_name == 'Login' :
            #key = ['ID', 'Username', 'Password' , 'Role']
            for each_set2 in CSV_list2:
                each_dict2 = {}
                each_dict2['ID'] = each_set2['ID']
                each_dict2['Username'] = each_set2['username']
                each_dict2['Password'] = each_set2['password']
                each_dict2['Role'] = each_set2['role']
                real_list.append(each_dict2)
            return real_list
            

        elif table_name == 'Project':
            #key = ['ProjectID', 'Title', 'Lead' , 'Member1' , 'Member2' , 'Advisor' , 'Status']
            # Title_Project = input('Name your Project : ')
            Title_Project = input('Your Project Title : ')
            ID_project = len(Table.Project_list) + 1
            project_dict = {
                'ProjectID': ID_project,
                'Title': Title_Project,
                'Lead': CSV_list2,
                'Member1': None,
                'Member2': None,
                'Advisor': None,
                'Status': "Unfinish" }
            Table.Project_list.append(project_dict)
            return project_dict
        

        elif table_name == "View_project":
                for each_project in Table.Project_list :
                    print(each_project)


        elif table_name == 'Advisor_pending_request':
            #key = ['ProjectID','to_be_advisor','Response','Response_date']
            Your_projectID = CSV_list2
            while Your_projectID != len(Table.Project_list) and int(Your_projectID) > len(Table.Project_list) and int(Your_projectID) < 1 :
                print("Invalid Project ID please Enter your Project ID again or Enter Project ID = 0 to stop")
                Your_projectID = input('Input your ProjectID : ')
                if Your_projectID == 0 :
                    break
            Can_be_advisor = []
            for_show_advisor = []
            for role_check in CSV_list1 :
                if role_check['type'] == 'faculty':
                    for_show_set = {}
                    Can_be_advisor.append(role_check['ID'])
                    for_show_advisor[role_check['fist']] = role_check['ID']
                    for_show_advisor.append(for_show_set)
                else :
                    pass
            print(for_show_advisor)
            Input_newadvisor = input("Input ID who you want to your project advisor : ")
            if Input_newadvisor not in Can_be_advisor :
                print("Sorry this User isn't a Student")
            elif Input_newadvisor in Can_be_advisor :
                Advisor_request_dict = {
                    'ProjectID': Your_projectID,
                    'to_be_advisor': Input_newadvisor,
                    'Response': None,
                    'Response_date': None }
            Table.Advisor_request_list.append(Advisor_request_dict)
            return Advisor_request_dict


        elif table_name == 'Member_pending_request':
            #key = ['ProjectID','to_be_member','Respomse','Response_date']
            Your_projectID = input('Input your ProjectID : ')
            while Your_projectID != len(Table.Project_list) and int(Your_projectID) > len(Table.Project_list) and int(Your_projectID) < 1 :
                print("Invalid Project ID please Enter your Project ID again or Enter Project ID = 0 to stop")
                Your_projectID = input('Input your ProjectID : ')
                if Your_projectID == 0 :
                    break
            Can_be_member = []
            for_show = []
            for role_check in CSV_list1 :
                if role_check['type'] == 'student':
                    for_show_set = {}
                    Can_be_member.append(role_check['ID'])
                    for_show_set[role_check['fist']] = role_check['ID']
                    for_show.append(for_show_set)
                else :
                    pass
            print(for_show)
            Input_newmember = input("Input ID who you want to request : ")
            if Input_newmember not in Can_be_member :
                print("Sorry this User isn't a Student")
            elif Input_newmember in Can_be_member :
                Member_request_dict = {
                    'ProjectID': Your_projectID,
                    'to_be_member': Input_newmember,
                    'Response': None,
                    'Response_date': None }

            Table.Member_request_list.append(Member_request_dict)
            return Member_request_dict

        return real_list
    
# modify the code in the Table class so that it supports the update operation where an entry's value associated with a key can be updated
    def update_entry (entry_choice):
        which_one = input('ID : ')
        input_key = input('Key : ')
        input_value = input("new value : ")
        for A in entry_choice:
            if A['ID'] == which_one:
                A[input_key] = input_value
            else :
                pass

        return entry_choice
            
