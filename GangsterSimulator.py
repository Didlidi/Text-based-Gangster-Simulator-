import random
import time

currentCrew = ['You']
possibleCrew = ['Scott', 'Preston', 'Harry', 'Larry', 'Gary', 'Barry', 'Carrie']
Money = 30
roundsPlayed = 0

def introRules():
    print ('''

1920'S GANGSTER SIMULATOR: PRE-PRE-PRE ALPHA EDITION 0.000002
-----------------------------------------------------------------------------------------
Congratulations!!!


The "big boss" has decided that you are his new 'Cappo' for Pythonville Scotland
and has generously supplied you with 30 'money' of start up capital!

Use your acumen to build a crew and make money. The boss wants 120 Money by the end
of 10 weeks. The bigger your crew, the more money you can make but also the more you
pay when wages are due.

Goons are necessary to protecting your money and planning bigger heists. Simple crimes
will generate revenue when they go smoothly but may result in goons being locked up if they
go wrong. Risky crimes can generate huge amounts of income, especially with a bigger crew,
but can be punishing on the bank balance if they fail.



Build a crew, take your chances and make 120 before the 10 weeks are up! 


-------------------------------------------------------------------------------------------''')

def displayWeek():
    time.sleep(1)
    print ('Week:', roundsPlayed + 1)

def display():
    time.sleep(1)
    print ('Crewsize:',len(currentCrew),'members.')
    print ('Crewmember names:', *currentCrew, sep = " ")
    print ('You have:', Money,'Money.')
    print ()
    
def turnChoice():
    time.sleep(1)
    choice = ''
    print ('''What shall we do this week, boss?
Enter [1] do a basic crime.
Enter [2] hire a goon.
Enter [3] do a risky crime.''')
    while choice != '1' and choice !='2' and choice != '3':
        choice = input()
        if choice == '1':
            doCrime()
        if choice == '2':
            getGoon()
        if choice == '3':
            riskyCrime()
        return choice

def riskyCrime():
    print ('''You invest some funds and your crew go about scoring info, contacts and specialist equipment...''')
    print ()
    time.sleep(1)
    global Money
    global currentCrew
    outcome = 0

    if len(currentCrew) <= 2:
        print ('You are a small crew, but you give it a go!''')
    if len(currentCrew) > 2 and len(currentCrew) <= 4:
        print ('You have a decent sized crew, and with it the potential to earn some money.''')
    if len(currentCrew) > 4:
        print ('''With a crew this size. You are ready for the big score!''')
        

    while outcome == 0:
        time.sleep(1)
        outcome = random.randint (1, 3)

        if outcome == 1 and len(currentCrew) <= 2:
            print ('''You and your crew obtain some "revealing" letters, signed to and from a local politician.
This will make for good blackmail. You earn 30 money.''')
            Money = Money + 25

        if outcome == 1 and len(currentCrew) <= 4 and len(currentCrew) > 2:
            print ('''An inside man and a bit of luck helps your crew pull of a daring robbery of government bonds.
You are gone before the police even arrive. The bonds sell for 50 money.''')
            Money = Money + 50
            
        if outcome == 1 and len(currentCrew) > 4:
            print ('''The "Pythonian Art and Precious Gem Gallery" is silently robbed during the night. A masterful heist.
Your crew earns 70 Money''')
            Money = Money + 70


        if outcome == 2 and len(currentCrew) <=2:
            print ('''Your crew earns 20 Money carrying out a relatively lucrative hit for a foriegn businessman.''')
            Money = Money + 20

        if outcome == 2 and len(currentCrew) > 2 and len(currentCrew) <= 4:
            print ('''Your crew disguise themselves as police officers and 'raid' an illegal high-stakes card-game.
The evenings takings are 40 money.''')
            Money = Money + 40
            
        if outcome == 2 and len(currentCrew) > 4:
            print ('''After bribing a fire-inspector and buring down a warehouse, your crew collects, via a crooked accountant
on a rather generous insurance policy. 50 Money is awarded.''')
            Money = Money + 50
            

        if outcome == 3 and len(currentCrew) >2 and len (currentCrew) <= 4:
            print ('''Things went badly last night. Not only did someone get locked up. But the tools you bought for the job
were confiscated. You lose 5 Money for each crewmember and you lose a crewmember!''')
            Money = Money - 8*len(currentCrew)
            lostGuy = random.randint (0, len(currentCrew) - 1)
            possibleCrew.append(currentCrew[lostGuy])
            currentCrew.pop(lostGuy)
            break

        if outcome == 3 and len(currentCrew) > 4:
            print ('''Someone talked! Your crew killed him but not before he snitched on the whole operation. The cops locked up another
one of your crew, and you lost the money spent on the job. You lose 5 Money for every crewmember and you lose two crewmembers.''')

            Money = Money - 5*len(currentCrew)
            lostGuy = random.randint (0, len(currentCrew) - 1)
            possibleCrew.append(currentCrew[lostGuy])
            currentCrew.pop(lostGuy)
            lostGuy = random.randint (0, len(currentCrew) - 1)
            possibleCrew.append(currentCrew[lostGuy])
            currentCrew.pop(lostGuy)

            
        if outcome == 3 and len(currentCrew) <=2:
            print ('''Your crew tried to plan a big score this week, but nothing was gained except the attention of the cops.
You pay out 15 Money in bribes''')
            Money = Money - 15
            
def doCrime():
    global currentCrew
    result = 0
    if len(currentCrew) <= 2:
        print ('Your team is small...')
    if len(currentCrew) > 2 and len(currentCrew) <= 4:
        print ('You have a reasonable sized crew capable of some mid-tier crime...')
    if len(currentCrew) > 4:
        print ('You have a big team behind you. It is time to earn some serious cash!')
        
    while result == 0:
        result = random.randint (1, 4)
        global Money
        time.sleep(1)
        if result == 1 and len(currentCrew) <= 2:
            print ('You earned 15 Money from various small time robberies carried out in shady parking lots.')
            Money = Money + 15
        if result == 2 and len(currentCrew) <= 2:
            print ('You earned 10 Money selling counterfeit watches at the local flea-market.')
            Money = Money + 10


        if result == 1 and len(currentCrew) > 2 and len(currentCrew) <= 4:
            print ('Your crew held up a bank and made 30 Money!')
            Money = Money + 30

        if result == 2 and len(currentCrew) > 2 and len(currentCrew) <= 4:
            print ('Your crew robbed a truck and made off with 25 Money')
            Money = Money + 25


            
        if result == 1 and len(currentCrew) > 4:
            print ('Your team extorted the local business and taxed other small time crooks. You earn 50 money!!')
            Money = Money + 50

        if result == 2 and len(currentCrew) > 4:
            print ('A smuggling operation your team has been running paid out 50 money!!')
            Money = Money + 40

            
        if result == 3:
            print ('''Unfortunately it didn't work out. Something went wrong and your crew walked away with nothing.''')

       
            
        if result == 4 and len(currentCrew) < 2:
            print ('You earned 15 Money from various small time robberies carried out in shady parking lots.')
            Money = Money + 15
            
        if result == 4 and len(currentCrew) >= 2:
            lostGuy = random.randint (0, len(currentCrew) - 1)
            if lostGuy == 0:
                print ('Something went wrong, your crew earned nothing but everyone got away!')
            else:
                possibleCrew.append(currentCrew[lostGuy])
                currentCrew.pop(lostGuy)
                print ('Something went wrong, your crew earned nothing and we lost one of our crew!')


def getGoon():
    if len(possibleCrew) == 0:
        print ('There is no one else in the city to recruit.')
    else:
        newGuy = random.randint (0, len(possibleCrew) -1)
        currentCrew.append(possibleCrew[newGuy])
        possibleCrew.pop(newGuy)
        print ('Your crew is getting bigger', end=' ')
    if len(currentCrew) <= 2:
        print('..but you are still quite a small crew.')
    if len(currentCrew) > 2 and len(currentCrew) <= 4:
              print ('..and you can start making a respectable amount of money.')
    if len(currentCrew) > 4:
              print ('..and it is large enough to run a serious criminal empire.')

    if len(currentCrew) >= 5:
           print ('..but there is not much point to growing it more.')


def muscleCheck():
    check = 0
    while check == 0:
        check = random.randint (1, 2)
        
        if check == 1:
            if Money > 80 and len(currentCrew) < 3:
                print ('''While you were out being a gangster. Your place was robbed. If you want
to keep your money, you are going to need a bigger gang.''')
        if check == 2 and Money > 80 and len(currentCrew) < 3:
            print ('''WARNING: No one robbed you today. But you are a very wealthy man with few friends. Change that.''') 






def thisWeek():
    result = 0
    while result == 0:
        result = random.randint (1, 6)
        global Money
        global currentCrew
        global possibleCrew
        time.sleep(1)
        if result == 1:
            if Money < 50:
                print ('A rival gang raided your hideout. They took 10 money.')
                Money = Money - 10
            if Money >= 50:
                print ('A rival gang raided your hideout. They took 20 money.')
                Money = Money - 20
            if Money >= 80:
                print ('A rival gang heard about your wealth and raided your safe for 50 Money!')
                Money = Money - 50
            break
        if result == 2 and len(currentCrew) > 3:
            print ('One of our guys turned out to be a rat. He was dealt with.')
            rat = random.randint( 0, len(currentCrew) - 1)
            possibleCrew.append(currentCrew[rat])
            currentCrew.pop(rat)
            break
        
        if result == 2 and len(currentCrew) <= 3:
            print ('Nothing much to report. Business as usual.')
            break
        
        if result == 2 and len(currentCrew) < 3 and Money > 70:
            print ('''With that much money in your account and so few goons to guard it. It is no wonder you got robbed.
A rival gang raided your hideout. They took 20 Money.''')
            Money = Money - 20
            break
            
        if result == 3 and len(currentCrew) < 3 and Money > 70:
             print ('''With that much money in your account and so few goons to guard it. It is no wonder you got robbed.
A rival gang raided your hideout. They took 20 Money.''')
             Money = Money - 20
        else:
            if result == 3:
                print ('Nothing much to report. Business as usual.')
            
        if result == 4:
            print ('Profits at the speakeasy have been good. You recieve a 10 money protection fee.')
            Money = Money + 10
        if result == 5:
            print ('Bills are due. You pay out 3 money for every goon you employ.')
            Money = Money - 3*len(currentCrew)
        if result == 6 and len(possibleCrew) >= 4:
            print('''A new guy has asked to join your crew. He seems reliable.''')
            newGuy = random.randint (0, len(possibleCrew) -1)
            currentCrew.append(possibleCrew[newGuy])
            possibleCrew.pop(newGuy)
        


introRules()
print()
display()
turnChoice()
print()
time.sleep(1)
for roundsPlayed in range (10):
    displayWeek()
    thisWeek()
    if Money <= 0:
        print ('''You are broke! You lost all the boss' money and so... HE WHACKS YOU!''')
        break
    if Money >= 120:
        print ('''YOU WIN!''')
        print ('In total you earned:', Money, 'Money.')
        print ('''You have made the 'La Cosa Pythona' filthy rich and have permission to retire from your life of crime!''')
        break
    display()
    turnChoice()
    print ()
    print ()
    input()
    if Money <= 0:
        print ('''You are broke! You lost all the boss' money and so... HE WHACKS YOU!''')
        break
    if Money >= 120:
        print ('''YOU WIN!
You earned''', Money, '''Money. You have made the 'La Cosa Pythona' filthy rich and can retire from your life of crime!''')
        break
    muscleCheck()
if Money < 120 and Money > 0:
    print ('In total you earned:', Money, 'Money.')
    print ('The boss is disappointed with your inability to generate funds... AND WHACKS YOU!')
