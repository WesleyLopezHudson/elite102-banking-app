import mysql.connector

#Connects Python to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",      
    database="banking_db"
)
cursor = conn.cursor()

#Creates a table if it doesn't already exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS accounts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        balance DECIMAL(10, 2)
    )
''')


def banking_system():
    start_screen = input("\nWhat do you want to do?"
                        "\n1. Open an account" 
                        "\n2. View balance" \
                        "\n3. Withdraw balance" \
                         "\n4. Deposit balance" \
                        "\n5. View all account details" \
                        "\n6. Delete an account" \
                        "\n7. Exit" \
                        "\n"
                        "\n"
                            )


    if start_screen == "1":
        account_name = input("What is your name? ") # This gives an account a name. Its for personalization and isn't actually important
        balance = 0.0 
        try:
            initial_deposit = float(input("How much do you want to deposit?"))

        except ValueError: #Prevents the program from crashing
            print("Please enter a valid number for the initial deposit.")
            return
        
        balance += initial_deposit
        cursor.execute("INSERT INTO accounts VALUES (DEFAULT, '" + account_name + "', "+ str(balance) + ")") #DEFAULT sets it to the next available ID and only works because of AUTO_INCREMENT
        assigned_id = cursor.lastrowid #Gets the ID of the created account 
        print("Congratulations " + account_name + ", you have opened an account with $" + str(initial_deposit) + " in it! Your ID is " + str(assigned_id) + ", do not forget it as its also your password.")
        return
     


    elif start_screen == "2":
                #Query Data
        try:
            account_id = float(input("\nWhat was your account id?\n")) #This chooses which accounts balance to view
            cursor.execute("SELECT * FROM accounts WHERE id = " + str(account_id)) # The * makes it show everything in the account's row
            rows = cursor.fetchone()
            print("The information displayed below is your id, name, and balance in that order.\n\n")
            for row in rows:
                print(row)
        except ValueError:
            print("Please use a number for your id next time")



    elif start_screen == "3":
        try:
            account_id = float(input("\nWhat is your account id?\n")) #This chooses which account to withdraw from
            cursor.execute("SELECT balance FROM accounts WHERE id = " + str(account_id))
            current_balance = cursor.fetchone() #Fetches and stores the account as a variable for later use
            if current_balance == None: # Checks if accounts exists
                print("There isn't an account with that ID")
                return
            
            current_balance_float = float(current_balance[0]) # Converts the list to a float

        except ValueError: # Checks if an actual number was entered
            print("Sorry, your didn't enter in a valid ID number")
            return
        
        try:
            withdraw_ammount = float(input("How much do you want to withdraw?\n"))

        except ValueError: # Checks if an actual number was entered
            print("Sorry, your withdraw ammount isn't a valid number")
            return
        
        current_balance_float -= withdraw_ammount # This removes the withdrawn ammount
        print("You have withdrawn $" + str(withdraw_ammount) + " from your account. You now have " + str(current_balance_float) + " in your account.")
        cursor.execute("UPDATE accounts SET balance = " + str(current_balance_float) + " WHERE id = " + str(account_id))



    elif start_screen == "4":
        try:
            account_id = float(input("\nWhat is your account id?\n")) #This chooses which account to deposit to
            cursor.execute("SELECT balance FROM accounts WHERE id = " + str(account_id))
            current_balance = cursor.fetchone() #Fetches and stores the account as a variable for later use
            if current_balance == None: # Checks if accounts exists
                print("There isn't an account with that ID")
                return
            
            current_balance_float = float(current_balance[0]) # Converts the list to a float

        except ValueError: # Checks if an actual number was entered
            print("Sorry, your didn't enter in a valid ID number")
            return
        
        try:
            withdraw_ammount = float(input("How much do you want to deposit?\n"))

        except ValueError: # Checks if an actual number was entered
            print("Sorry, your deposit ammount isn't a valid number")
            return
        
        current_balance_float += withdraw_ammount # This removes the withdrawn ammount
        print("You have deposited $" + str(withdraw_ammount) + " from your account. You now have $" + str(current_balance_float) + " in your account.")
        cursor.execute("UPDATE accounts SET balance = " + str(current_balance_float) + " WHERE id = " + str(account_id))
        


    elif start_screen == "5":
                #Query Data
        cursor.execute("SELECT * FROM accounts") # The * makes it show everything in the table
        rows = cursor.fetchall()
        for row in rows:
            print(row)



    elif start_screen == "6":
        try:
            account_id = float(input("\nWhat is your account id?\n"))
            
        except ValueError: # Checks if an actual number was entered
            print("Sorry, your didn't enter in a valid ID number")
            return

        cursor.execute("SELECT * FROM accounts WHERE id = " + str(account_id))
        rows = cursor.fetchone()
        for row in rows:
            print(row)
        try:
            last_chance = float(input("\nIs this your information? 1 for yes, 2 for no:\n"))
            if last_chance == 1:
                cursor.execute("DELETE FROM accounts WHERE id = " + str(account_id))
                print("Account deleted successfully.")
            elif last_chance == 2:
                print("If you want to delete your account, make sure its your id you enter.")
            else:
                print("You didn't enter in one of the given options, terminating deletion process.")
        except ValueError:
            print("You didn't enter in one of the given options, terminating deletion process.")
            return

        
    elif start_screen == "7":    
        print("Connection Terminated"
        "\n")
        pass #exit() wouldn't allow anything outside of the function to happen, like saving data

    else:
        print("Please input a valid number correlating to an option below")
        banking_system()

banking_system()





###########################################################################
###########################################################################
######################### BELOW  IS  A  TEST LINE #########################
###########################################################################

#cursor.execute("INSERT INTO accounts VALUES (DEFAULT, 'Maria', 500.00)")

######################### ABOVE  IS  A  TEST LINE #########################
###########################################################################
###########################################################################

conn.commit() #Saves the changes
conn.close() # Closes the connection when done


