An admin role
- Managing the database : can see and modify all tables include Person table , Login table , Project table , Advisor_pending_request table , Member_pending_request table

A student role
- See someone want you to become member or not
- Accept or deny request
    - update Member_pending_request table
    - update Project table
- See and modify his project details
    - Update Project table (for modify the project)
    - Update Login Table (for change the role when create the project : will be lead !!!)
    - Update Member_pending_request table (for send the request)

A lead student
- Create a project
    - Update Project table (insert new object (his project))
- Find members
    - see Person table (to find the member)
- Send invitational messages to potential members
    - Update Member_pending_request table (for send the request)
    - Update Project table (if the student agree to be member)
- See and modify his own project details
    - Update Project table (modify his project)
- Send request messages to potential advisors
    - Update Advisor_pending_request table (to find the advisor)
    - Update Project table (if got the advisor)
- Submit the final project report
    - Update Project table (update status of the project)

A member student
- See project status 
- See and modify his project detail
    - update Project table

A normal faculty who is not an advisor
- See request to be a supervisor
- Send response denying to serve as an advisor
    - Update Login table (to be advisor from faculty)
    - Update Advisor_pending_request table (for the respond)
    - Update project table ( got new advisor)
- See details of all the project
- Evaluate projects (will be update soon in proposol.md)


