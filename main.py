
# Welcome to the last version of my spammer
#Spammer made by K0M1

#just the import

import pyautogui
import random
import time

time.sleep(0.5)

#just a little logo

print('''
 __    __   ______   __       __    __          __       __                                                                     ______                                                                      
/  |  /  | /      \ /  \     /  | _/  |        /  \     /  |                                                                   /      \  
$$ | /$$/ /$$$$$$  |$$  \   /$$ |/ $$ |        $$  \   /$$ |  ______    _______   _______   ______    ______    ______        /$$$$$$  |  ______    ______   _____  ____   _____  ____    ______    ______
$$ |/$$/  $$$  \$$ |$$$  \ /$$$ |$$$$ |        $$$  \ /$$$ | /      \  /       | /       | /      \  /      \  /      \       $$ \__$$/  /      \  /      \ /     \/    \ /     \/    \  /      \  /      \ 
$$  $$<   $$$$  $$ |$$$$  /$$$$ |  $$ |        $$$$  /$$$$ |/$$$$$$  |/$$$$$$$/ /$$$$$$$/  $$$$$$  |/$$$$$$  |/$$$$$$  |      $$      \ /$$$$$$  | $$$$$$  |$$$$$$ $$$$  |$$$$$$ $$$$  |/$$$$$$  |/$$$$$$  |
$$$$$  \  $$ $$ $$ |$$ $$ $$/$$ |  $$ |        $$ $$ $$/$$ |$$    $$ |$$      \ $$      \  /    $$ |$$ |  $$ |$$    $$ |       $$$$$$  |$$ |  $$ | /    $$ |$$ | $$ | $$ |$$ | $$ | $$ |$$    $$ |$$ |  $$/
$$ |$$  \ $$ \$$$$ |$$ |$$$/ $$ | _$$ |_       $$ |$$$/ $$ |$$$$$$$$/  $$$$$$  | $$$$$$  |/$$$$$$$ |$$ \__$$ |$$$$$$$$/       /  \__$$ |$$ |__$$ |/$$$$$$$ |$$ | $$ | $$ |$$ | $$ | $$ |$$$$$$$$/ $$ |
$$ | $$  |$$   $$$/ $$ | $/  $$ |/ $$   |      $$ | $/  $$ |$$       |/     $$/ /     $$/ $$    $$ |$$    $$ |$$       |      $$    $$/ $$    $$/ $$    $$ |$$ | $$ | $$ |$$ | $$ | $$ |$$       |$$ |      
$$/   $$/  $$$$$$/  $$/      $$/ $$$$$$/       $$/      $$/  $$$$$$$/ $$$$$$$/  $$$$$$$/   $$$$$$$/  $$$$$$$ | $$$$$$$/        $$$$$$/  $$$$$$$/   $$$$$$$/ $$/  $$/  $$/ $$/  $$/  $$/  $$$$$$$/ $$/       
                                                                                                    /  \__$$ |                          $$ |
                                                                                                    $$    $$/                           $$ |                                                                
                                                                                                     $$$$$$/                            $$/
''')

time.sleep(3)

#menu selection

Selection = input('''
1. Message Spammer
2. Random word list generator
3. Word lister

Insert the number here -> ''')

S = int(Selection)

#option 1
#message spammer

if S == 1:
    print(''' \n \n \n \n \n \n \n \n \n \n \n \n
    Welcome to the message spammer''')

    time.sleep(1.5)

    msg = input("Insert the message to spam -> ")
    msg_num = input("insert the number of message you like to send -> ")
    num = int(msg_num)
    time.sleep(1)
    print("The spamming will start in 5 seconds")
    time.sleep(5)

    for word in range(num):
        pyautogui.typewrite(msg + "\n")

#option 2
#Random word list generator

elif S == 2:
    print(''' \n \n \n \n \n \n \n \n \n \n \n \n
    Welcome to the random word list generator''')

    time.sleep(1.5)

    wordnumber = input("insert the number of random word to generate -> ")
    intwordnumb = int(wordnumber)

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    for i in range(intwordnumb):
        name = ''.join((random.choice(chars) for i in range(10)))

        result = name

        output = open("RandomWordGenerated.txt", "a")
        output.write(result + "\n")

    time.sleep(1.5)

    print("please check the RandomWordGenerated.txt file")

#option 3
#word lister

elif S == 3:
    print(''' \n \n \n \n \n \n \n \n \n \n \n \n
        Welcome to the word lister''')

    time.sleep(1.5)

    w = input("insert the word or the phrase -> ")
    n1 = input("insert the number of row -> ")
    nt = int(n1)

    for i in range(nt):
        o = open("WordLister.txt", "a")
        o.write(w + "\n")

    time.sleep(1.5)

    print("Please check the WordLister.txt file")

#option for other inserted number

else:
    print("the number inserted is not valid")

