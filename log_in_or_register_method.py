# nested list of product and its details
nestedList=[["PRODUCT ID", "PRODUCT NAME","CATEGORY", "STOCKS", "PRICE"],
            ["S0001","WH-CH510 Wireless Headphone","Headphones","10","2,999.00"],
            ["S0002","MDR-XB55AP EXTRA BASS","Headphones","3","1,499.00"],
            ["S0003","XB550AP EXTRA BASS","Headphones","8","2,999.00"],
            ["S0004","W830 Compact Camera","Camera","10","6,999.00"],
            ["S0005","H300 Camera","Camera","7","12,999.00"],
            ["S0006","XB01 EXTRA BASS","Speaker","15","1,999.00"],
            ["S0007","GTK-PG10 Outdoor Speaker","Speaker","2","12,999.00"],
            ["S0008","XB32 EXTRA BASS","Speaker","12","6,799.00"],
            ["S0009","MDR-E9LP In-ear","Earphones","15","499.00"],
            ["S0010","MDR-XB55AP In-ear","Earphones","9","1,499.00"],
            ["S0011","WI-SP51 Wireless In-ear","Earphones","6","4,299.00"],
            ["S0012","WS410 Walkman","MP3 Player","3","4,999.00"],
            ["S0013","A50 Walkman","MP3 Player","5","9,999.00"],
            ["S0014","WS620 Walkman","MP3 Player","5","6,999.00"],
            ["S0015","WF-XB700 Truly Wireless","Headphones","6","6,799.00"],
            ["S0016","XPeria XA","Cellphone","14","10,690.00"],
            ["S0017","XPeria X","Cellphone","10","15,890.00"],
            ["S0018","XPeria XA2 Ultra","Cellphone","10","24,490.00"],
            ["S0019","XPeria XA1","Cellphone","13","14,890.00"],
            ["S0020","XPeria XA1 Ultra","Cellphone","3","19,090.00"],]

# nested list of admin usernames and their passwords
admin_users = [
    ["admin_name", "1234"]
]

# nested list of registered usernames and their passwords
registered_users = [
    ["username", "1234"]
]

# LOG IN METHOD
def log_in():
    while True:
        print("\nLog-In")
        username = input("Enter username: ")
        password = input("Enter password: ")

        credentials = [username, password]
        
        if credentials in admin_users:
            print("Admin User: {}".format(username))
            return 1 
        elif credentials in registered_users:
            print("Registered User: {}".format(username))
            return 2 
        else:
            print("User not found. Try again :(\n")
    
# REGISTER METHOD
def register(): # admin registers are closed, no outside user can be an admin
    print("\nRegister") 
    r_username = input("Enter your username: ")
    r_password = input("Enter password: ")
    # more information details can be implemented if necessary

    r_credentials = [r_username, r_password]

    registered_users.append(r_credentials)
    print("Successfully registered! Now please log in :)\n")
    user_prompt()
    return 

# USER PROMPT METHOD (Log in or register)
def user_prompt():
    user_input = input("(1) Log-In or (2) Register (Enter #): ")

    if user_input.isdigit():
        if int(user_input) == 1:
            return_value = log_in()
        elif int(user_input) == 2:
            return_value = register()
        else:
            print("Invalid input. Please try again :(\n")
            user_prompt()
    else:
        print("Invalid input. Please try again :(\n")
        user_prompt()
    return return_value

# MAIN FUNCTION
def main():
    print("Sales Inventory System")

    # prompt the user if they want to log-in or register
    admin_or_user = user_prompt()

    if admin_or_user == 1:
        print("Access to all admin functions")
    elif admin_or_user == 2:
        print("Access to all registered user functions")
    else:
        print("Something went wrong. Please try again :(\n")
        user_prompt()

main() # calls the main function for the code to run
