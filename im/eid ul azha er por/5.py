print("Hi Welcome! In i'm helper. How can I help you? If you want to close the program type exit and press enter.")
import datetime
import pygame
import pyjokes
import pywhatkit
import wikipedia
import time
import pyautogui
import random
import cv2
truefalse = True
while truefalse:
    language = input("Enter your language : ")
    if ("English" in language or "english" in language):
        # import googlemaps
        while truefalse:
            a = input("Listening.............. \n")
            time.sleep(1)
            print("Your question is : " + a)
            if ("Hi!" in a or "How are you?" in a or "Hi! how are you?" in a):
                print("It is not a question. But i'm fine you?")
                finetoo = input()
                if ("not" in finetoo or "Not" in finetoo):
                    print("So sad.")
                elif ('exit' in finetoo or 'Exit' in finetoo):
                    truefalse = False
                else:
                    print("Welcome")
            elif (a in "How to update all driver?"):
                print(
                    "You can use the driver booster app. If you download this link run this code again and write Driver Booster. ")

                # myname your name



            elif ("What is your name?" in a):
                print("My name is i'm helper.")
            elif ('game' in a or 'Game' in a or 'GAME' in a):

                import pygame
                import time

                pygame.init()
                display = pygame.display.set_mode((320, 568))
                bg = pygame.image.load('bg.png')  # 320 568
                bird = pygame.image.load('bird_1.png')
                bird_x = 10
                bird_y = 10
                move = 'Right'
                gun = pygame.image.load('gun.jpg')
                gun_x = 5
                bullet = pygame.image.load('bullet.png')
                bullet_y = 401
                bullet_x = 5
                but = False
                blast = pygame.image.load('blast2.jpg')
                showblast = False
                showbird = True
                count = 0
                win = pygame.image.load('win.jpg')
                last = True
                time = 10
                while last:
                    pygame.event.get()
                    key = pygame.key.get_pressed()
                    display.blit(bg, (0, 0))
                    if showbird:
                        display.blit(bird, (bird_x, bird_y))
                    if move == 'Right':
                        bird_x = bird_x + .1
                        # print(bird_x)
                        if bird_x == 265.999999999992:
                            move = 'Left'
                    elif move == 'Left':
                        bird_x = bird_x - .1
                        # print(bird_x)
                        if bird_x == 4.200000000000015:
                            move = 'Right'
                    display.blit(gun, (gun_x, 400))
                    if key[pygame.K_LEFT]:
                        gun_x = gun_x - .1
                    elif key[pygame.K_RIGHT]:
                        gun_x = gun_x + .1
                    display.blit(bullet, (bullet_x, bullet_y))
                    if key[pygame.K_UP]:
                        but = True
                    if but:
                        bullet_y = bullet_y - .1
                        # print(bullet_y)
                    if key[pygame.K_RIGHT]:
                        bullet_x = bullet_x + .1
                    elif key[pygame.K_LEFT]:
                        bullet_x = bullet_x - .1
                    if bullet_y == 0.0999999999773255:
                        showblast = True
                    if showblast:
                        display.blit(blast, (bird_x, bird_y))
                        if bullet_y == -871.9000000001524:
                            showblast = False
                            showbird = False
                    if bullet_y == -2803.4999999985685:
                        showbird = True
                    if bullet_y == -3181.6999999982245:
                        # bullet ke false korte hobe ba bondho
                        but = False
                        bullet_y = 401
                    count = count + 1
                    print(count)
                    time = time - 1
                    if count >= 61633:
                        # time.sleep(10)
                        display.blit(win, (0, 0))
                        # last = False
                        # print("The game is close in ",time,'seconds.')
                    pygame.display.update()

                # win
                '''
                    if poss==50 or poss==51 or poss==52 or poss==53 or poss==54 or poss==55 or poss==56 or poss==57 or poss==12 or poss==13 or poss==14:
                        display.blit(win,(0,0))

                    pygame.display.update()
                '''


            elif ('What is my name?' in a):
                i74 = True
                i84 = True
                i83 = True
                allgussname = ['Ismail', 'Ullash', 'Mohith', 'Sadia', 'Ali', 'Nazmul', 'Samia', 'Sumi', 'Moon',
                               'Justin Bieber']
                i77 = random.choice(allgussname)
                print('Is your name : ', i77,
                      '? If yes write y and press the enter button or no write n and press the enter button.')
                i79 = input("")
                if ('y' in i79 or 'Y' in i79):
                    print("Wow! Thanks for using this program", i77)
                elif ('n' in i79 or 'N' in i79):
                    while i83:
                        i85 = random.choice(allgussname)
                        print('If your name ', i85, 'If yes write y and press the enter button')
                        i87 = input('')
                        if ('y' in i87 or 'Y' in i87):
                            print("Wow!")
                            i83 = False
                        elif ('No' in i87 or 'my' in i87 or 'it' in i87):
                            i91 = input("What is your name ? ")
                            print("Wow your name = ", i91)
                            i83 = False

                # while i74:


            elif (a == "What is my name?"):
                print("I dont khow you. Please tell me your name : ")
                youname = input("")
                print("Wow! Your name is " + youname)
            elif (
                    a == "There are many error in this app." or a == "Error" or a == "i'm helper app is not working properly."):
                print("I'am a new developer. I will try.")
            elif (a == "Are you a robot?" or a == "You==Robot?"):
                print("No. It is only a program.")
            # download
            elif ("download" in a):
                print(
                    "Please search on google. Maybe i have this fiie. You  contact with me. My facebook url= https://tinyurl.com/facebookismail")
            # Google Map
            # I'm a porgrammer. I am 13 years old but 1 have hot world record✔
            elif ("Where is the" in a):
                place = input("Enter the name of the place : ")
                googlemap = pywhatkit.search(place)
                # linkplace = "https://www.google.com.bd/maps/place/" + place
                # lastplace = linkplace.replace(" ", "+")
                # print(lastplace)
            # waiting
            elif (a == "What is my name?"):
                print("I don't khow what is  your name at 1st you say what is my name?")
                myname = input("")
                if ("i'm" in myname or "I'M" in myname or "I'm" in myname):
                    print(myname + ". It is correct.")
                else:
                    print("Not " + myname + "is not my name. My name is i'm helper.")
                print(
                    "Is your name is Hasina? If yes press y and if answar is no press n . If no name in my list please type incorrect and add your name on my list.")
                hasian = input("")

                lotariname = True
                while lotariname:
                    if ('y' in hasian):
                        print("Oh,,,i'm great.")
                        lotariname = False
                    else:
                        allnameofuser = ['Ali', 'Hasina', 'Ismail', 'Sadia', 'Hasan']
                        lotari = random.randint(0, len(allnameofuser) - 1)
                        print(lotari)

                        print("Is your name if yes press y and enter or no press n and hit the enter button =  " + str(
                            lotari + 1) + ". " + allnameofuser[lotari])
                        # time.sleep(5)
                        tryyn = input('')
                        if ('y' in tryyn):
                            print("Thanks for using this program. Developed by Ismail Mazumder.")
                            lotariname = False
                        elif (
                                'no my name' in tryyn or 'No my name is' in tryyn or 'incorrect' in tryyn or 'Incorrect' in tryyn):
                            print("So,,sad. Please tell me what is your name?")
                            username = input('')
                            allnameofuser.append(username)
                            print("Your name is", username)
                            print("Look my list's all name.", allnameofuser)
                            lotariname = False
                        elif ('n' in tryyn):
                            lotariname = True
                        elif ("Exit" in a or "exit" in a):
                            lotariname = False
                        else:
                            lotariname = False

            elif ("i'm Developer" in a or "developer" in a or "Developer" in a):
                print("i'm developer is Ismail Mazumder.")

            elif ('exit' in a or 'Exit' in a or 'EXIT' in a):
                truefalse = False
            # Youtube
            elif ("How to" in a):

                inputyoutube = input("Enter specific name : ")
                pywhatkit.playonyt(inputyoutube)
                # youtubelink = "https://www.youtube.com/results?search_query=" + inputyoutube
                # lastyoutube = youtubelink.replace(" ", "+")
                # print(lastyoutube)



            elif ("What is " in a or "Who is" in a or "Where is" in a):
                wikiinput = input("Enter only subject name :  ")
                history = wikipedia.summary(wikiinput, 10)
                print(history)
                # wikilink = "https://en.wikipedia.org/wiki/" + wkiinput
                # wikilast = wikilink.replace(" ", "+")
                # print(wikilast)

            elif ("developer" in a or 'Developer' in a):
                print("i'm 's developer is Ismai Mazumder.")

            elif ("I want to see movie" in a):
                print("Visit netfix")
            # time
            elif ("Time" in a):
                time = datetime.datetime.now().strftime('%H:%M')
                print("Time is = " + time)

            # play
            elif ("play" in a or "Play" in a):
                songname = input("Enter the song name only : ")
                pywhatkit.playonyt(songname)
            # send message 123
            elif ("Send " in a or "message" in a or "send message" in a):
                whatmessage = input("Enter the message : ")
                message = 0
                messageno = int(input("How many message i can send?"))
                timetimeinput = int(input("Enter the time (give 2) : "))
                while message <= messageno:
                    if (message==0):
                        time.sleep(4)
                    #print("Move the text cursor to where you want to send the message. Total time ", "4",
                          #"second. \n")
                    if (message ==1):
                        print("Move the text cursor to where you want to send the message. Total time 10",
                              timetimeinput, "second. \n")

                    time.sleep(timetimeinput)
                    pyautogui.typewrite(whatmessage)
                    time.sleep(timetimeinput)
                    pyautogui.press('enter')
                    message = message + 1
                    '''
                    if message==messageno:
                        print("Succes")
                    else:
                        print("Working..")
                    '''
            elif ('joke' in a or 'Joke' in a):
                mr_been = pyjokes.get_joke()
                print(mr_been)
            elif ('camera' in a):
                #import cv2

                cap = cv2.VideoCapture(0)
                True_False = True
                l239 = 0
                while True_False:
                    l239 = l239 + 1
                    if (l239==1):
                        print("press q for close this program")
                    # _,frame = cap
                    ret, frame = cap.read()
                    cv2.imshow('frame', frame)
                    #print("press q for close this program")
                    if cv2.waitKey(10) == ord('q'):
                        break
                cap.release()
                cv2.destroyWindow()
            # else
            else:
                # print("There are no informatin")
                lastinput = input("Enter the spesefic name - ")
                last = pywhatkit.search(lastinput)




    # bangla
    elif ("Bangla" in language or "bangla" in language or "Bangla." in language or "bangla" in language):
        while True:
            a = input(
                "শুনছি......... \nListen bangla we can't show Bangla,\n so you should use English language please close the app and open the app again. \n শুনছি......... \n")
            time.sleep(1)
            print("আপনার প্রশ্নটি হলঃ " + a)
            if ("Hi" in a or "How are you?" in a or "Hi! how are you?" in a):
                print("এটি কুনো প্রশ্ন নয়। কিন্ত আমি ভাল আছি।")
                finetoo = input()
                if ("not" in finetoo or "Not" in finetoo):
                    print("আল্লাহর উপর ভরশা রাখুন।")
                else:
                    print("বলুন আলহামদুলিলাহ।")
            elif (a in "How to update all driver?"):
                print(
                    "You can use the driver booster app. If you download this link run this code again and write Driver Booster. ")
            elif (a in "Name" or a in "What is your name?" or a == "Is your name i'm?"):
                print("My name is i'm helper.")
            elif (a == "What is your name?"):
                print("আমি জানি আপনার নাম কি প্রথম এ  আপনি আমার নাম  বলুন! ")
                myname = input("")
                if ("i'm" in myname or "I'M" in myname or "I'm" in myname):
                    print(myname + "এটি  সঠিক। ")
                else:
                    print("না " + myname + "এটি আমার নাম না. আমার নাম হল  i'm helper.")


            elif ('game' in a or 'Game' in a or 'GAME' in a):


	import time
	pygame.init()
	display = pygame.display.set_mode((320,568))
	bg = pygame.image.load('bg.png')# 320 568
	bird = pygame.image.load('bird_1.png')
	bird_x = 10
	bird_y = 10
	move = 'Right'
	gun = pygame.image.load('gun.jpg')
	gun_x = 5
	bullet  = pygame.image.load('bullet.png')
	bullet_y = 401
	bullet_x = 5
	but = False
	blast  = pygame.image.load('blast2.jpg')
	showblast = False
	showbird = True
	count = 0
	win = pygame.image.load('win.jpg')
	last = True
	time = 10
	while last:
	    pygame.event.get()
	    key = pygame.key.get_pressed()
	    display.blit(bg,(0,0))
	    if showbird:
	        display.blit(bird,(bird_x,bird_y))
	    if move == 'Right':
	        bird_x = bird_x + .1
	        #print(bird_x)
	        if bird_x == 265.999999999992:
	            move ='Left'
	    elif move == 'Left':
	        bird_x = bird_x - .1
	        #print(bird_x)
	        if bird_x == 4.200000000000015:
	            move = 'Right'
	    display.blit(gun,(gun_x,400))
	    if key[pygame.K_LEFT]:
	        gun_x = gun_x - .1
	    elif key[pygame.K_RIGHT]:
	        gun_x = gun_x + .1
	    display.blit(bullet,(bullet_x,bullet_y))
	    if key[pygame.K_UP]:
	        but = True
	    if but:
	        bullet_y = bullet_y - .1
	        #print(bullet_y)
	    if key[pygame.K_RIGHT]:
	        bullet_x = bullet_x + .1
	    elif key[pygame.K_LEFT]:
	        bullet_x = bullet_x - .1
	    if bullet_y == 0.0999999999773255:
	        showblast = True
	    if showblast:
	        display.blit(blast,(bird_x,bird_y))
	        if bullet_y == -871.9000000001524:
	            showblast = False
	            showbird = False
	    if bullet_y == -2803.4999999985685:
	        showbird = True
	    if bullet_y == -3181.6999999982245:
	        #bullet ke false korte hobe ba bondho
	        but = False
	        bullet_y = 401
	    count = count + 1
	    print(count)
	    time = time - 1
	    if count >= 61633:
	        #time.sleep(10)
	        display.blit(win,(0,0))
	        #last = False
	        #print("The game is close in ",time,'seconds.')
	    pygame.display.update()                '''
	




            # wait
            elif (
                    a == "There are many error in this app." or a == "Error" or a == "i'm helper app is not working properly."):
                print("আমি একজন নতুন প্রোগ্রামার আমি চেষ্টা করছি ।")
            elif (a == "Are you a robot?" or a == "You==Robot?"):
                print("না । এটি শুধু মাত্র একটি প্রোগ্রাম । ")
            # download'
            # ''
            elif ("download" in a):
                print(
                    "Please search on google. Maybe i have this fiie. You  contact with me. My facebook url= https://tinyurl.com/facebookismail")

            # Google Map

            elif ("Where is the" in a):
                place = input("Enter the name of the place : ")
                googlemap = pywhatkit.search(place)
                # linkplace = "https://www.google.com.bd/maps/place/" + place
                # lastplace = linkplace.replace(" ", "+")
                # print(lastplace)



            # Youtube
            elif ("How to" in a):

                inputyoutube = input("Enter specific name : ")
                pywhatkit.playonyt(inputyoutube)
                # youtubelink = "https://www.youtube.com/results?search_query=" + inputyoutube
                # lastyoutube = youtubelink.replace(" ", "+")
                # print(lastyoutube)



            elif ("What is " in a or "Who is" in a or "Where is" in a):
                wikiinput = input("Enter only subject name :  ")
                history = wikipedia.summary(wikiinput, 10)
                print(history)
                # wikilink = "https://en.wikipedia.org/wiki/" + wkiinput
                # wikilast = wikilink.replace(" ", "+")
                # print(wikilast)

            elif ("I want to see movie" in a):
                print("Visit netfix")
            # time
            elif ("Time" in a):
                time = datetime.datetime.now().strftime('%H:%M')
                print("Time is = " + time)

            # play
            elif ("play" in a or "Play" in a):
                songname = input("Enter the song name only : ")
                pywhatkit.playonyt(songname)
            # send message
            elif ("Send " in a or "message" in a or "send message" in a):
                whatmessage = input("Enter the message : ")
                message = 0
                l357 = int(input("Enter the time : "))
                messageno = int(input("How many message i can send?"))

                while message <= messageno:
                    print("Move the text cursor to where you want to send the message. Total time ", l357, "second. \n")

                    time.sleep(l357)
                    pyautogui.typewrite(whatmessage)
                    time.sleep(2)
                    pyautogui.press('enter')
                    message = message + 1
                    '''
                    if message==messageno:
                        print("Succes")
                    else:
                        print("Working..")
                    '''
            elif ("i'm Developer" in a or "developer" in a or "Developer" in a or 'developed'):
                print("i'm 's developer is ইস্মাইল মাযুমদের।.")

            elif ('joke' in a or 'Joke' in a):
                mr_been = pyjokes.get_joke()
                print(mr_been)
            # else
            else:
                # print("There are no informatin")
                lastinput = input("Enter the spesefic name - ")
                last = pywhatkit.search(lastinput)
    else:
        print(
            "I am learning. Therer are two language i know 1st is English 2nd is Bangla. \n You can try English because English is a international language. \n If you are a Bangladeshi you can try the Bangla language. ")
print("Thanks for using thisg program.")
