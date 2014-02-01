from random import random
from random import choice
from math import floor
import names
'''
Names is required to run this script.
download from https://pypi.python.org/pypi/names/.
'''

elder_population = 0
married_population = 0
single_population = 0
runtime = 0
born_this_year = 0


living = []
the_dead = []
'''
A bunch of global functions to store
statistical and simulation data.
'''


class Person(object):
    '''
    This creates a class called person.
    '''
    def __init__(self, name, gender, value, dad = "None", mom = "None"):
        '''
        Everything a person needs to be a person
        is contained here.
        '''
        self.value = value
        self.name = name
        self.gender = gender
        self.age = 0
        self.status = "alive"
        self.single = True
        self.love_value = 0
        self.love = ""
        """
        flagged for removal^
        """
        self.dad = dad
        self.mom = mom
        self.fertility = round(random() * 10)
        self.want_child = round(random() * 5)
        self.children = 0
        self.child_name = []
        self.friends = {}
        self.mood = 0
        self.health = 0 
        self.personality = round(random()*10)
        self.antisocial = round(random()*10)
        self.shallow = round(random()*20)-10
        self.charisma = round(random()*20)-10
        self.love_status = "None"
        self.child_status = []
        self.hunger = 0
        
    def __str__(self):
        '''
        This displays all attributes of the person.
        '''
        if self.single:
            return "My name is %s and I am %s and I am %s.\n and I want to have %s children.\n" % (self.name, self.gender,
                                                                                                self.age, self.want_child)
        elif self.children == 0:
            return "My name is %s and I am %s and I am %s.\n I am married to %s and I want to have %s children.\n" % (self.name, self.gender, self.age,
                                                                                                                       self.love, self.want_child)
        else:
            return "My name is %s and I am %s and I am %s.\n I am married to %s and I have %s children.\n" % (self.name, self.gender, self.age,
                                                                                                               self.love, self.children)
 
    def get_age(self):
        '''
        This is a method to get the age
        '''
        return "%s is %s years old" % (self.name, self.age)
    def get_family(self):
        '''
        This method gets the family members
        '''
        if (self.dad == "none"):
            if not self.single:
                if self.children > 0:
                    return "%s is married to %s.\n%s has %s kids named %s." % (self.name, self.love, self.name,
                                                                              self.children,self.child_name)
                else:
                    return "%s is married to %s.\n%s has no kids" % (self.name, self.love, self.name)           
            else:
                return "%s has no family!" % self.name
        elif not self.single:
            if self.children > 0:
                return "%s parents are %s and %s\n%s is married to %s.\n%s has %s kids named %s." % (self.name, self.dad, self.mom,
                                                                                                   self.name, self.love, self.name,
                                                                                                   self.children,self.child_name)
            else:
                return "%s parents are %s and %s\n%s is married to %s.\n%s has no kids" % (self.name, self.dad, self.mom,
                                                                                         self.name, self.love, self.name)
                
        else:
            return "%s parents are %s and %s" % (self.name, self.dad, self.mom)
            return "%s is not married" % self.name

    def get_friends(self):
        '''
        This method lists the friends the person has
        '''
        for key in self.friends:
            print key, self.friends[key]


'''
functions that are called by elapse_time()
'''


def elapse_time(years=100):
    '''
    This moves time forward in the simulation.
    '''
    global runtime
    global born_this_year
    global single_population
    elder_population = 0
    single_population = 0
    born_this_year = 0
    print "running simulation for %s years..." % years
    print "Would you like to monitor the population? (y/n)"
    response = raw_input()
    for i in range(years):
        t = 0
        while t < len(living)-1:
            if living [t].status != "dead":
                time(living [t])
                if (living [t].love == "" and living[t].single == False):
                    print living [t].name
                    print living [t].value
                    print living [t].love_value
                    print living [t]
                    print living [t].get_family()
                    print len(living)
                    print("something")
                    wait = input("PRESS ENTER TO CONTINUE.")
                    break
            t += 1
        runtime += 1
        if response == "y":
            print "Population is %s in the year %s" % (len(living), runtime)


    sim_stats.present_stats(years)


class Statistics(object):
    """
    statistical data & methods stored here.
    """
    def __init__(self):
        self.counter = 0
        self.name = ""


    def most_popular(self):
        for t in living:
            if  t.single: 
                single_population += 1
            if len(t.friends) > counter:
                   self.name = t.name
                   
    def present_stats(self,years): 
        print "\nSimulation ran for %s years this time. Total runtime %s" % (str(years), runtime)
        print "Population is %s" % len(living) 
        print "\nOut of %s people, %s made it to their 80s" % (len(living), elder_population)
        print "%s babies we born in %s years" % (born_this_year, years)
        print "Out of %s people, %s married and have changed their sirnames" % (len(living), married_population)
        print "Out of %s people, %s never married" % (len(living), single_population)
        print "%s have died since the beginning of this simulation." % len(the_dead)
        print "%s has the most friends" % self.name


    def get_info(self):
        '''
        A function that searches the person list for a match.
        '''
        if type(name) == str and len(living)>0:

            for i in living:
                if living [i].name == name:
                    return living [i].__str__()
        else:
            return "Invalid entry. Please enter a string."

        
    def who_is(self, s):
        '''
        Lists people's names based on parameters
        '''
        if (s == living or s == the_dead):

            for i in s:
                print s [i].name


    def count_people(self, s):
        '''
        Lists people with parameters
        '''
        if (s == the_dead or s == living):
            return len(s)

        else:
            return totalPop


    def who_is_married(self, s = "all"):
        '''
        A function that lists married people.
        '''
        if s != "all":
            for i in s:
                if not s [i].single:

                    print s [i].name

        else:
            for i in living:
                if not living [i].single:

                    print living [i].name

            for i in the_dead:
                if not the_dead [i].single:

                    print the_dead [i].name


    def who_is_has_children(self, s="all",t = True):
        '''
        Lists who has children
        '''
        if t:
            
            if s != "all":

                for i in s:
                    if s [i].children > 0:

                        return s [i].name

            else:
                for i in living:
                    if s [i].children > 0:
                        return s [i].name
                for i in the_dead:
                    if s [i].children > 0:

                        return s [i].name

        else:
            if s != "all":
                for i in s:
                    if s [i].children < 1:

                        return s [i].name

            else:
                for i in living:
                    if s [i].children < 1:
                        return s [i].name
                for i in the_dead:
                    if s [i].children < 1:

                        return s [i].name


    def count_has_children(self, s = "all",t = True):
        '''
        counts parents
        '''
        counter = 0
        if (t and s!= "all"):
            
            for i in s:
                if s [i].children > 0:
                    counter += 1

            return counter
                

        elif (not t and s!= "all"):
            for i in s:
                if s [i].children < 1:
                    counter += 1

            return counter


        elif t:
            for i in living:
                if s [i].children > 0:
                    counter += 1

            for i in the_dead:
                if s [i].children > 0:
                    counter += 1

            return counter


        else:
            for i in living:
                if s [i].children < 1:
                    counter += 1

            for i in the_dead:
                if s [i].children < 1:
                    counter += 1

            return counter


    def count_married(self, s=0):
        '''
        counts married
        '''
        if (s == the_dead or s == living):
            counter = 0
            for i in living:
                    if not i.single:
                        counter += 1
            return counter
        else:
            return married_population


def time(your):
        '''
        This simulates a year of living for the person
        and his likelihood of dying that year
        '''
        global living
        global elder_population
        global born_this_year

        your.age += 1
        if your.age > 79:
            elder_population += 1
        """if round(random() * 100)/100 + float(your.age) / 800 > 1:   #This is the mortality algorithm.
            mortality(your)
        """
        if round(random() * 100)/100 + float(your.age) / 800 > 1:
                    your.status = "dead"
                    
                    the_dead.append(living[your.value])

                    if your.love_status != "none":
                        if (not your.single and your.love_status):
                            living[your.love_value].love_status = False
                            living[your.love_value].love_value = len(the_dead)-1
                        elif not your.single and your.love_status:
                            the_dead[your.love_value].love_status = False
                            the_dead[your.love_value].love_value = len(the_dead)-1
                    number = len(living)-1-your.value

                    for i in range(number):
                        if not living[i+(len(living)-number)].single:
                            if living[i+(len(living)-number)].love_status:
                                if living[i+(len(living)-number)].love_value > living[i+(len(living)-number)].value:

                                    living[i+(len(living)-number)].love_value -= 1
                        living[i+(len(living)-number)].value -= 1
                            

                    del living[your.value]

        else:
            make_friends(your)                                      #Every year entities meet new people
            if your.single:
                get_love(your)
                make_friends(your)                                      #And have a chance to find love.
            if not your.single and your.love_status:
                born_this_year += repro(your, living[your.love_value])
    

def make_friends(your):
    '''
    allows people to gain friends
    '''
    randomFactor = int(round(((your.age/100)+random())*10))
    for i in range(randomFactor):
        their = living[int(round(random()*(len(living)-1)))]
        found = False
        for j in your.friends:
            if j == their.name or j == your.name:
                found = True
                break
        if found != True:
            test_of_friendship(your, their)


def test_of_friendship(your,their):
    '''
    The initial test of friendship between strangers
    '''
    friendship_constant = 5
    personality_score = (your.personality + their.personality) - (your.antisocial + their.antisocial)

    attraction = (your.charisma + their.shallow + your.shallow + their.charisma)

    totalScore = personality_score + attraction*random()
                     
    if totalScore > (your.antisocial + their.antisocial)*random():
        your.friends [their.name] = their.charisma + their.personality
        their.friends [your.name] = your.charisma + your.personality
        #print str(your.name) +" has made a friend with "+str(their.name)

    else:
        pass
        #print str(your.name) +" failed to make friends."


def get_love(your):
    '''
    This function searches for a couple
    '''
    if (your.age > 18 and your.single): 
        global married_population

        for i in range(5):
            y = int(round(random() * len(living)) - 1)

            if (your.gender != living [y].gender and living [y].age > 18 and living [y].status == "alive" and living [y].single):
                #print "%s courts %s" % (your.name, living [y].name)

                if (round(random() * your.age) / 40) > 0:
                    your.single = False
                    living [y].single = False
                    your.love_status = True
                    living [y].love_status = True

                    if your.gender == "female":
                        your.name = changeName(your.name, living [y].name)
                        married_population += 2
                        living [y].love_value = your.value
                        your.love_value = y
                        your.love = living [y].name
                        living [y].love = your.name
                        break

                    else:
                        living [y].name = changeName(living [y].name, your.name)
                        your.love = living [y].name
                        living [y].love = your.name
                        married_population += 2
                        living [y].love_value = your.value
                        your.love_value = y
                        break


def changeName (hers, his):
    """
    This changes the wife's surname
    """
    oldName = hers
    newName = ""

    for i in range(len(hers)):
        if hers [i] == " ":
            newName = hers [:i]
            break

    for i in range (len(his)):
        if his[i] == " ":
            newName = newName + his [i:]

            break
        
    return newName


def repro(his, hers):
    """
    This function tests if a couple will have a child.
    """
    global born_this_year
    fertilityrate = ((his.fertility+hers.fertility) * (1 - ((his.age+hers.age) / 100))) / 2
    if (his.children < (round((his.want_child + hers.want_child) / 2)) and random()*fertilityrate > 1):
        his.children += 1
        hers.children += 1
        gender = choice(["male", "female"])
        child_name = changeName (str(names.get_first_name(gender))+" ",his.name)
        living.append(Person(str(child_name), gender, len(living),his.name,hers.name))
        his.child_name.append(child_name)
        hers.child_name.append(child_name)
        return 1
    else:
        return 0

"""
Simulation setup and restart functions below
"""




"""
Information gathering functions below
"""




'''
The menu activates on startup.
'''

def main_menu():
    answer = ""
    while answer != "0":
        '''
        This is the main menu where the simulation
        is controlled from.
        '''
        print "\nWhat would you like to do?"
        print "1. Start Simulation\n2. Elapse Simulation\n3. Population Information\n4. Quick Start\n5. Restart Simulation\n0. Quit"
        answer = raw_input()

        if answer == "1" or answer == "5":
            print "\nhow large of a population would you like to simulate? 100 should be the max."
            answer = raw_input()
            if type(answer) != str or answer == "":
                print "\nApologies. You entered an invalid input.\n \n"
            else:
                restart(int(answer))
                

        elif answer == "2":
            print "\nhow long do you wish to elapse? no more than 300."
            answer = raw_input()
            if type(answer) != str:
                print "\nApologies. You entered an invalid input.\n \n"
            else:
                elapse_time(int(answer))

        elif answer == "4":
            restart(20)
            elapse_time(200)

        elif answer == "3":
            """
            This is where the crap starts.
            Statistics galore!
            God help me.
            """
            while answer != "0":
                print "\n1. Count alive\n2. Count dead\n3. Count married\n4. Name search \n5. List Alive \n6. List dead\n7. List Married\n8. List Married and Alive\n9. List Married and Dead\n10. Count Has Children and Alive\n0. Return"
                answer = raw_input()

                if answer == "1":
                    """
                    Count alive
                    """
                    print sim_stats.count_people(living)
                                
                elif answer == "2":
                    """
                    Count dead
                    """
                    print sim_stats.count_people(the_dead)

                elif answer == "3":
                    print sim_stats.count_married()

                elif answer == "4":
                    print "\nPlease enter his or her name."
                    answer = raw_input()
                    if type(answer) != str or answer ==  "":
                        print "\nApologies. You entered an invalid input.\n \n"
                    else:
                        search_value = "nothing"
                        gender = ""
                        for i in living:
                            if answer == living [i].name:        
                                search_value = i
                                break
                        if search_value != "nothing":
                            print "found %s! What do you want to do?" % gender
                            while answer != "0":
                                print "\n1. About %s\n2. Family\n3. Age\n4. Friends\n0. Return" % gender
                                answer = raw_input()
                                if type(answer) != str:
                                    print "\nApologies. You entered an invalid input.\n \n"
                                elif answer == "1":
                                    print "searching..."
                                    print living[search_value].__str__()
                                elif answer == "2":
                                    print living[search_value].get_family()
                                elif answer == "3":
                                    print living[search_value].get_age()
                                elif answer == "4":
                                    print living[search_value].get_friends()
                                elif answer == "0":
                                    pass
                                else:
                                    print "\nCould you repeat that? \n \n"
                            answer = 1
                        else:
                            print "Didn't find answer."
                elif answer == "5":
                    print sim_stats.who_is(living)

                elif answer == "6":
                    sim_stats.who_is(the_dead)
                elif answer == "7":
                    sim_stats.who_is_married()
                elif answer == "8":
                    sim_stats.who_is_married(living)
                elif answer == "9":
                    sim_stats.who_is_married(the_dead)
                elif answer == "10":
                    print sim_stats.count_has_children(living)
                    
            answer = 1
            print "\nreturning to main menu"
        else:
            print "\nCould you repeat that? \n \n"


def sim_setup(p):
    '''
    This starts the simulation by preparing
    the first group of people.
    '''
    print "\nJust a moment...\n\n"
    for i in range(p):
        living.append(i)
        gender = choice(["male", "female"])
        living[i] = Person (str(nahttps://github.com/jackellice2/Population-Simulator/new/master#fullscreen_blob_contentsmes.get_full_name(gender)), gender, i)

    print "%s people successfully created!\n" % len(living)


def restart(p):
    '''
    Restarts the simulation.
    '''
    global living
    global the_dead
    global runtime
    global elder_population
    global married_population
    global single_population
    runtime = 0
    elder_population = 0
    married_population = 0
    single_population = 0
    del living[:]
    del the_dead[:]
    sim_setup(p)
sim_stats = Statistics()
main_menu()

print "\nGood Bye!"
