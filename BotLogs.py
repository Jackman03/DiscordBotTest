#Logging system that exports every command to a csv file and prints to the console in a readable format
#Timestamp,Username,command,successful,extrainfo

def LogCommand(Command,Username):
    print(f"{Username} has run the {Command} command")  #Print to console

#If a member leaves or joins the server, logs the user and amount of users
def LogMemberFluctation(Command,Username):
    print(f"{Username} has the {Command} the server") #Print to console