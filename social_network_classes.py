import time
# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        
    ## For more challenge try this
    def save_social_media(self,file):
        
        f = open(file,"w")
        data = ""
        
        for person in self.list_of_people:
            flist = ""
            mq = ""

            for p in person.friendlist:
                flist+=str(self.indexOf(p))+"^*"
            for m in person.messageQueue:
                flist+=str(self.indexOf(m[0]))+"|"+m[1]+"|"+m[2]+"^*"
            
            data += person.id+","+str(person.year)+","+str(flist)+","+str(mq)+","+person.numberId+"\n"

        
        f.write(data)
        f.close()
        

    ## For more challenge try this
    def reload_social_media(self,file):
        
        f = open(file,"r")
        data = f.readlines()
        f.close()

        for i in range(len(data)):
            data[i] = data[i].replace("\n","").split(",")

        self.list_of_people = []
        count = 0
        for p in data:
            try:
                self.list_of_people.append(Person(p[0],int(p[1]),numberId=p[4]))
                data[count][2] = data[count][2].split("^*")
                data[count][3] = data[count][3].split("^*")
                if (data[count][2] == ""):
                    data[count][2] = []
                if (data[count][3] == ""):
                    data[count][3] = []

                for i in range(len(data[count][3])):
                    data[count][3][i] = data[count][3][i].split("|")


            except IndexError:
                print("err:loading",p,"failed")
            count += 1

        count = 0
        for p in data:
            try:
                self.list_of_people[count].friendlist=[]

                self.list_of_people[count].messageQueue=[]

                for x in p[2]:
                    self.list_of_people[count].friendlist.append(self.list_of_people[int(x)])
                for y in p[3]:
                    self.list_of_people[count].messageQueue.append([self.list_of_people[int(y[0])],y[1],y[2]])


            except IndexError:
                print("err:loading",p,"failed")
            count+=1

        

    def  create_account(self):
        #implement function that creates account here
        print("Account Created")
        self.list_of_people.append(Person("default",0))

        input("press enter to continue")
        print("\n\n\n")
        pass

    def indexOf(self,person):

        return self.list_of_people.index(person)


class Person:
    def __init__(self, name, age,**kwargs):
        self.id = name
        self.year = age
        self.friendlist = []
        self.messageQueue = []
        self.numberId = "0000"
        for name,value in kwargs.items():
            print(value)
            if (name == "numberId"):
                self.numberId = value

    def add_friend(self, person_object):
        #implement adding friend. Hint add to self.friendlist
        pass

    def send_message(self,friend,message):
        friend.messageQueue.append([self,message,time.time,False])
        pass





