#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui


loggedInAs = None

def MainMenu():

    if (loggedInAs != None):
        return social_network_ui.mainMenuLoggedIn()
    else:

        result = social_network_ui.mainMenuGuest()

        if (result == "1"):
            return "1"
        if (result == "2"):
            return "5"
        if (result == "3"):
            return "3"
        else:
            return "0"

#Create instance of main social network object
ai_social_network = SocialNetwork()
ai_social_network.reload_social_media("data.txt")


#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = MainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()
            loggedInAs = ai_social_network.list_of_people[-1]
            

        elif choice == "2":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:

                if (inner_menu_choice == "1"):

                    detailsChangeMenu = social_network_ui.editDetailsMenu(loggedInAs)
                    
                    selection = ""
                    if (detailsChangeMenu == "1"):
                        while True:
                            selection = str(input("enter a new name:"))
                            if (str(input("is " + selection + " correct? y/n")) == "y"):
                                break
                        ai_social_network.list_of_people[ai_social_network.indexOf(loggedInAs)].id = selection.replace(",","")
                    elif (detailsChangeMenu == "2"):
                        while True:

                            try:
                                selection = int(input("enter a new age:"))
                                if (str(input("is " + selection + " correct? y/n")) == "y"):
                                    break
                            except TypeError:
                                pass
                        ai_social_network.list_of_people[ai_social_network.indexOf(loggedInAs)].age = selection
                    else:
                        break

                elif (inner_menu_choice == "2"):
                    friend = social_network_ui.addFriendsMenu(loggedInAs,ai_social_network)
                    ai_social_network.list_of_people[ai_social_network.indexOf(loggedInAs)].friendlist.append(friend)
                
                elif (inner_menu_choice == "3"):
                    
                    count = 0
                    for f in loggedInAs.friendlist:
                        print(count,f.id,f.year)
                        count+=1
                    


                elif (inner_menu_choice == "5"):
                    friend = social_network_ui.sendMessageMenu(loggedInAs)
                    message = str(input("message:"))
                    ai_social_network.list_of_people[ai_social_network.indexOf(friend)].messageQueue.append([self,message,time.time()])

                        
                elif (inner_menu_choice == "4"):
                    #readMessages

                    print("          Messages")

                    for message in loggedInAs.messageQueue:
                        print(message[0].name+message[1])

                    cont = input("press enter to continue")
                    break
                elif (inner_menu_choice == "6"):
                    break
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()



        elif choice == "3":
            ai_social_network.save_social_media("data.txt")
            print("Thank you for visiting. Goodbye")
            break

        elif choice == "4":

            loggedInAs = None

        elif choice == "5":
            loggedInAs = social_network_ui.loginMenu(ai_social_network)
            

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = MainMenu()



        
