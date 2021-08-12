print("Hi Welcome! In i'm helper. How can i help you? (Use only English language)")
import datetime
import pywhatkit
import wikipedia
import time
import pyautogui

language = input("Enter your language : ")
if ("English" in language or "english" in language):
    # import googlemaps
    while True:
        a = input("Listening.............. \n")
        time.sleep(1)
        print("Your question is : " + a)
        if ("Hi!" in a or "How are you?" in a or "Hi! how are you?" in a):
            print("It is not a question. But i'm fine you?")
            finetoo = input()
            if ("not" in finetoo or "Not" in finetoo):
                print("So sad.")
            else:
                print("Welcome")
        elif (a in "How to update all driver?"):
            print(
                "You can use the driver booster app. If you download this link run this code again and write Driver Booster. ")
        elif (a in "Name" or a in "What is your name?" or a == "Is your name i'm?"):
            print("My name is i'm helper.")
        elif (a == "What is your name?"):
            print("I khow what is  you name at 1st you say what is my name?")
            myname = input("")
            if (myname == "i'm" or myname == "I'M" or myname == "I'm"):
                print(myname + "It is correct.")
            else:
                print("Not " + myname + "is not my name. My name is i'm helper.")
        elif (a == "What is my name?"):
            print("I dont khow you. Please tell me your name : ")
            youname = input("")
            print("Wow! Your name is " + youname)
        elif (
                a == "There are many error in this app." or a == "Error" or a == "i'm helper app is not working properly."):
            print("I'am a new developer. I will try.")

        elif ("Not working" in a or "Rule" in a):
            print(
                "At 1st you should know some rule . \n Rule no (1)If the questin is very hard or unic don't give space on the text. \n Rule no (2)Click on this link (Press Ctrl button and click on this link.)")

        elif (a == "Are you a robot?" or a == "You==Robot?"):
            print("No. It is only a program.")
        # download
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
            messageno = int(input("How many message i can send?"))
            while message <= messageno:
                print("Move the text cursor to where you want to send the message. Total time 10second. \n")

                time.sleep(10)
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
        # else
        else:
            # print("There are no informatin")
            lastinput = input("Enter the spesefic name - ")
            last = pywhatkit.search(lastinput)

# bangla
else:
    while True:
        a = input("শুনছি......... \n")
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
        elif (a == "What is my name?"):
            print("আমি জানি না। আপনি আমাকে বলুন আপনার নাম কি  : ")
            youname = input("")
            print("আপনার নাম হল । যদিও আমি আপনার নাম মনে রাখতে পারি না । " + youname)
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
            messageno = int(input("How many message i can send?"))
            while message <= messageno:
                print("Move the text cursor to where you want to send the message. Total time 10second. \n")

                time.sleep(10)
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
        # else
        else:
            # print("There are no informatin")
            lastinput = input("Enter the spesefic name - ")
            last = pywhatkit.search(lastinput)
