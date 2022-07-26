# You can implement user interface functions here.
from re import S
from  social_network_classes import SocialNetwork,Person

def loginMenu(network):

    attempt = str(input("account id:"))

    for user in network.list_of_people:
        if (user.numberId==attempt.replace("\n","").replace(" ","")):
            print("Hello " + user.id)
            return user
    print("Login Failed")
    return None
def mainMenuGuest():

    print("\n")
    print("1. Create a new account")
    print("2. Login to account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")


def mainMenuLoggedIn():

    print("\n\n\n")
    print("")
    print("1. Create a new account")
    print("2. Actions")
    print("3. Quit")
    print("4. Logout")
    print("********************************************************")
    return input("Please Choose a number: ")
    

def manageAccountMenu():


    print("\n\n\n")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. View all my messages")
    print("5. Send message")
    print("6. <- Go back ")
    return input("Please Choose a number: ")
    

def editDetailsMenu(Person):
    print("\n\n\n")
    print("id:",Person.numberId)
    print("1. Change Name from "+str(Person.id))
    print("2. Change Age from "+str(Person.year))
    print("3. <- Go back ")
    return input("Please Choose a number: ")
  
def addFriendsMenu(Person,network):
    print("\n\n\n")

    People = sorted(network.list_of_people,key = lambda x : x.id)
    pageLength =  5
    pages = []

    while (len(People) > 0):

        pages.append([])

        for i in range(pageLength):
            if (len(People)>0):
                if (not People[0] in Person.friendlist and People[0] != Person):
                    pages[-1].append(People[0])
                People.pop(0)
            else:
                break

    selectedPage = 0
    
        

    print("find a friend")

    count = 1
    for person in pages[selectedPage]:

        print(str(count)+"."+person.id)
        count+=1

    print("page 1 of "+str(len(pages)))
    print("\n")
    print("1. change page")
    print("2. select friend")
    print("3. <- Go back")
    selection = input("Please Choose a number:")

    if (selection == "1"):
        
        number = 0
        while True:
            
            try:
                number = int(input("Please Choose a number: "))
                if (number > 0 and number <= len(pages)):
                    break
                else:
                    print("incorrect range")
            except TypeError:
                print("not a number")
        selectedPage = number-1

    elif(selection == "2"):

        number = 0
        while True:
            
            try:
                number = int(input("Please Choose The Number Corresponding To the User: "))
                if (number > 0 and number <= pageLength):
                    return pages[selectedPage][number-1]
                else:
                    print("incorrect range")
            except TypeError:
                print("not a number")
        

    elif (selection == "3"):
        
        return None
            
def sendMessageMenu(Person):
    print("\n\n\n")

    People = sorted(Person.friendlist,key = lambda x : x.id)
    pageLength =  5
    pages = []

    while (len(People) > 0):

        pages.append([])

        for i in range(pageLength):
            if (len(People)>0):
                if (not People[0] in Person.friendlist):
                    pages[-1].append(People[0])
                People.pop(0)
            else:
                break

    selectedPage = 0

    if (len(People > 0)):
        while True:
            

            print("find a friend")

            count = 1
            for person in pages[selectedPage]:

                print(str(count)+"."+person.id)
                count+=1

            print("page 1 of "+str(len(pages)))
            print("\n\n")
            print("1. change page")
            print("2. select friend")
            print("3. <- Go back")
            selection = input("Please Choose a number: ")

            if (selection == "1"):
                
                number = 0
                while True:
                    
                    try:
                        number = int(input("Please Choose a number: "))
                        if (number > 0 and number <= len(pages)):
                            break
                        else:
                            print("incorrect range")
                    except TypeError:
                        print("not a number")
                selectedPage = number-1

            elif(selection == "2"):

                number = 0
                while True:
                    
                    try:
                        number = int(input("Please Choose The Number Corresponding To the User: "))
                        if (number > 0 and number <= pageLength):
                            break
                        else:
                            print("incorrect range")
                    except TypeError:
                        print("not a number")
                return pages[selectedPage][number-1]

            elif (selection == "3"):
                
                return None
    else:
        print("No Friends")
        return None
  