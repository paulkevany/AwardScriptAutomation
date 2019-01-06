
import pandas as pd
import requests
import random

def blackKnightWinners():


    #Define csv file containing the users who won

    userFile = "results.csv" #If filename changes change it here

    #Read results.csv content


    content = pd.read_csv(userFile, delimiter=',', names = ['email', 'prize', 'date', 'ID'])

    blackKnightPrizes = content[content["prize"] == "Black Knight"]

    blackKnightEmails = blackKnightPrizes["email"]

    #Emails received, go to distributeBlackNight method

    print("\n \n")
    #print( "BlackKnight Winners: \n" , blackKnightEmails)


    prizeType = "Black Knight"

    distributePrizes(blackKnightEmails, prizeType)



def galaxyWinners():


    #Define csv file containing the users who won

    userFile = "results.csv" #If filename changes change it here

    #Read results.csv content


    content = pd.read_csv(userFile, delimiter=',', names = ['email', 'prize', 'date', 'ID'])

    galaxyPrizes = content[content["prize"] == "Galaxy Set"]

    galaxyEmails = galaxyPrizes["email"]


    print("\n \n")
    #print("Galaxy Winners\n", galaxyEmails)

    #Emails retrieved

    #Send email method

    prizeType = "Galaxy Set"

    distributePrizes(galaxyEmails, prizeType)


def normalWinners():

    userFile = "results.csv"  # If filename changes change it here

    # Read results.csv content

    content = pd.read_csv(userFile, delimiter=',', names=['email', 'prize', 'date', 'ID'])

    normalPrizes = content[content["prize"] == "Normal Account"]

    normalEmails = normalPrizes["email"]

    # Emails retrieved

    # Send email method

    print("\n \n ")
    #print("Normal Winners \n", normalEmails)

    prizeType = "Normal Account"

    distributePrizes(normalEmails, prizeType)


def SCYTHE_PICKAXEWinners():
    userFile = "results.csv"  # If filename changes change it here

    # Read results.csv content

    content = pd.read_csv(userFile, delimiter=',', names=['email', 'prize', 'date', 'ID'])

    scytheWinners = content[content["prize"] == "Scythe Pickaxe"]

    scytheEmails = scytheWinners["email"]

    # Emails retrieved

    # Send email method

    print("\n \n ")
    #print("Scythe Pickaxe Winners: \n", scytheEmails)

    prizeType = "Scythe Pickkaxe"

    distributePrizes(scytheEmails, prizeType)




def skullTrooperWinners():
    userFile = "results.csv"  # If filename changes change it here

    # Read results.csv content

    content = pd.read_csv(userFile, delimiter=',', names=['email', 'prize', 'date', 'ID'])

    skullTroopWinners = content[content["prize"] == "Skull Trooper"]

    skullTrooperEmails = skullTroopWinners["email"]

    # Emails retrieved

    # Send email method

    prizeType = "Skull Trooper"
    print("\n \n ")
   # print("Skull Troop Winners: \n", skullTrooperEmails)


    distributePrizes(skullTrooperEmails, prizeType)



def stackedWinners():
    userFile = "results.csv"  # If filename changes change it here

    # Read results.csv content

    content = pd.read_csv(userFile, delimiter=',', names=['email', 'prize', 'date', 'ID'])

    stackedWinners = content[content["prize"] == "Stacked Account"]

    stackedEmails = stackedWinners["email"]

    # Emails retrieved

    # Send email method
    prizeType = "Stacked Account"
    print("\n \n ")
    #print("Stacked Winners: \n", stackedEmails)

    distributePrizes(stackedEmails, prizeType)


def STWWinners():
    userFile = "results.csv"  # If filename changes change it here

    # Read results.csv content

    content = pd.read_csv(userFile, delimiter=',', names=['email', 'prize', 'date', 'ID'])

    stwWinners = content[content["prize"] == "Save The World"]

    stwEmails = stwWinners["email"]

    # Emails retrieved

    # Send email method

    prizeType = "Save The World"

    print("\n \n ")
    #print("Save The World Winners: \n", stwEmails)

    distributePrizes(stwEmails, prizeType)


def VBucksWinners():
    userFile = "results.csv"  # If filename changes change it here

    # Read results.csv content

    content = pd.read_csv(userFile, delimiter=',', names=['email', 'prize', 'date', 'ID'])

    VBuckWinners= content[content["prize"] == "V-Bucks Account"]

    VBucksEmails = VBuckWinners["email"]

    # Emails retrieved

    # Send email method

    prizeType = "V-Bucks Account"

    print("\n \n ")
    #print("VBucks Winners: \n", VBucksEmails)

    distributePrizes(VBucksEmails, prizeType)







def distributePrizes(emailList, prizeType):



    #print("Here is the email list")

    #print(emailList)

    #Check prize type and use relevant file
    global prizeFile

    if prizeType == "Black Knight":

         prizeFile = "BLACK_KNIGHT.txt"

    if prizeType == "Galaxy Set":

        prizeFile = "GALAXY_SET.txt"

    if prizeType == "Normal Account":

        prizeFile = "NORMAL.txt"

    if prizeType == "Scythe Pickaxe":

        prizeFile = "SCYTHE_PICKAXE.txt"

    if prizeType == "Skull Trooper":

        prizeFile = "SKULL_TROOPER.txt"

    if prizeType == "Stacked Account":

        prizeFile = "STACKED.txt"

    if prizeType == "Save The World":

        prizeFile = "STW.txt"

    if prizeType == "V-Bucks Account":

        prizefile = "VBUCKS.txt"


    file = open(prizeFile)
    text = file.readlines() #Read File content line by line




    prizeList = []
    winnerList = []



    #Put prizes into a list


    for prize in text:
        # For every prize in the prize file, add it to its own array

        prizeList.append(prize)



    if len(prizeList) < len(emailList):
        print("Not enough prizes for all " + prizeType + " winners")


    if(len(prizeList) == 0):

       print("No prizes left for " + prizeType)



    for prize, winner in zip(prizeList, emailList):

        #print(len(prizeList))
        #print(len(emailList))

        print(f'{prize} goes to {winner}')

        prizeList.remove(prize)


        print(str(len(prizeList)) + " " + prizeType + ' prizes left.')


        emailUserWithPrize(winner, prize, prizeType)


    writeTo = open(prizeFile, "w")


    prizes = ""
    for i in prizeList:


        writeTo.write(i)

        prizes = i

   # for e in emailList:

      #  writeFile.write(e + "," + "\n")

    if len(prizeList) < 1:
        print("No more prizes for " + prizeType)









def emailUserWithPrize(winnerEmailAddress, winnerPrize, prizeType):

    writeFile = open("emailSentTo.csv", "a")

    writeFile.write(winnerEmailAddress + ":" + winnerPrize + ":" + prizeType + "," + "\n")


    #generate random num

    randomNum = random.randint(11111,99999)


    subject = "ZaneRewards.com: "+ prizeType +" [R" + str(randomNum) + "]"


    username = (winnerPrize.split(":")[0])  # split credentials, store username
    password = (winnerPrize.split(":")[1])  # Store password

    emailBody = "<p><span style='font-family:verdana,geneva,sans-serif;'>Congratulations, your reward has processed!<br /> <br /> Here are your details for... <strong>" + prizeType + "</strong><br /> <br /> <strong>Username: </strong>"+username+"<br /> <strong>Password: </strong>"+password+"<br /> <br /> Important: It&#39;s an Epic Games account, so you&#39;ll need to log in via PC or Mobile.<br /> <br /> Check your account, visit: <a href='http://epicgames.com/login' rel='noopener' target='_blank'>epicgames.com/login</a><br /> -<br /> <br /> Keep in mind that you can claim as many accounts as you&#39;d like, so long as you have the points to claim them. You can also download the same apps on different devices, just make sure you are logged in to your rewards account.<br /> <br /> <strong>If you want to earn a lot of points...</strong><br /> <br /> There are new apps every day at 12AM EST MIDNIGHT. We make announcements every night when there&#39;s new apps (on Telegram), so have your notifications enabled as most of them expire a few hours after midnight.<br /> <br /> If you are not part of our Telegram group yet, you can join by using this link:<br /> <br /> <a href='http://zanerewards.com/telegram'rel='noopener' target='_blank'>zanerewards.com/telegram</a></span></p>"

    print("Sending Email to: " + winnerEmailAddress + " for prize: " + prizeType + "\n")
    #Construct email template

    return requests.post(
            "mailGunLink here",
            auth=("api", "APIKey Here"),
            data={"from": "email@example.com",
                  "to": winnerEmailAddress,
                  "subject": subject,
                  "html": emailBody})






blackKnightWinners()
galaxyWinners()
normalWinners()
SCYTHE_PICKAXEWinners()
skullTrooperWinners()
stackedWinners()
STWWinners()
VBucksWinners()
