# a) In-Memory Storage
user_database=[]

# To create a new user record
create_new_user=lambda name, email: {"name": name, "email": email}

# To insert the user record into the list
insert_user=lambda user_record: user_database.append(user_record)

# To fetch all user records from the list
fetch_all_users=lambda: user_database

# To create a function that reads and decodes the SmartScam Code
def read_decode_smartscan(code):
    try:
        name,email=code.split(',')
        print(f"Name:{name}, Email:{email}") 
        return name,email
    except ValueError:
        print("Invalid Format! Please re-enter the values")
        return None,None

# For user registration function
def RegisterUserFromSmartScan(code):
    name,email=read_decode_smartscan(code) # using the scanning function ti extract  user data
    if name and email:
        user_record = create_new_user(name, email) # using lambda function to create record in-memeroy list
        insert_user(user_record) # using lambda function to insert the record in-memory list
                                           
        


    