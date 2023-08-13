# Aiden Shepler
# March 5, 2023
# purpose: To recommend college majors to students based on Holland scores, personality, and SAT scores

import csv


# prints the menu to show users which input to choose
def research():
    print("------")
    print("RIASEC")
    print("------")
    print("")
    print("RAISEC is an acronym that identifies talents/interests with possible majors using "
          "6 different occupational groups.")
    print("It was developed by John Holland and can be used to match hobbies, interests, "
          "and talents to possible majors. ")
    print("")
    print("R: Realistic | Doers")
    print("I: Investigative | Thinkers")
    print("A: Artistic | Creators")
    print("S: Social | Helpers")
    print("E: Enterprising | Persuaders")
    print("C: Conventional | Organizers")
    print("")
    print("Using this knowledge, and more in-depth descriptions of the letters, majors can be classified into 3-letter"
          "Holland codes")
    print("Using a test--like the one provided in "
          "https://laborfiles.delaware.gov/main/lmi/publications/Career_Compass_2021-2022.pdf"
          ", one can determine their occupational code and match it to a major.")
    print("It is important to note that this code does not 'define' or predetermine your major or career. It is just a "
          "helpful tool to lead you in the right direction to determining the proper college major that best suits "
          "you.")
    print("Here are some other sources to look further into Holland Codes: ")
    print("")
    print("https://acd.iupui.edu/careers/choose-your-major/connect-majors-to-careers/interests/index.html")
    print("http://career.iresearchnet.com/career-development/hollands-theory-of-vocational-choice/")
    print("https://www.hopkinsmedicine.org/fac_development/_documents/lisa_heiser_faculty_development_handout.pdf")
    print("")

    print("----------")
    print("SAT scores")
    print("----------")
    print("")
    print("Using research conducted by The College Board, which can be located at, "
          "https://reports.collegeboard.org/media/pdf/2022-total-group-sat-suite-of-assessments-annual-report.pdf,"
          "I was able to create a csv table to extract information for the program.")
    print("This table gives the mean score of a report conducted by The College Board for the SAT and relates them to"
          "undergraduate students in different degrees")
    print("Because of this research, the program's majors were limited, though still offering a wide range of choices."
          "Therefore, if you do not recieve a result from the RIASEC test, google the corresponding major. ")
    print("This was said in the SAT score function, but it is important to note that the SAT score does not and should"
          "not determine your choice of major going into college. ")
    print("This could be a possible tool to measure difficulty, but it is not an absolute reflection of your "
          "performance in certain majors, nor does it determine your major "
          "by certain interests. For that, take the RIASEC test.")


def choice():

    print("Given the menu, choose what test you would like to take. ")
    decision = input("What test would you like to take? (input the corresponding number; press Q to quit)")

    if decision == "1":
        riasecTest()
    elif decision == "2":
        satScore()
    elif decision == "3":
        research()
    elif decision == "Q":
        return


def menu():

    print("________________________")
    print("Choosing a College Major")
    print("________________________")
    print("")
    print("1: RIASEC Test | Receive your 3-letter Holland Code")
    print("2: SAT scores  | Receive a recommended major based on SAT score")
    print("3: Research | Recieve the research used to create this program")
    print("Q: Quit")
    print("")


# contains the code to recommend a major based on SAT scores
def careerReturn(ns, cn):
    # ns = nearestScore
    # cn = column number
    # initializing number to end for loop
    n = 0
    with open("satintendedmajors.csv") as intendmajor:
        readCSV = csv.reader(intendmajor, delimiter=',')
        for column in readCSV:

            career = column[0]
            scoreSat = column[cn]

            if ns == scoreSat and cn == 2:

                print("Your SAT ERW score is closest to the mean ERW score among most undergraduates in the major of "
                      + str(career))
                print("")

            if ns == scoreSat and cn == 3:
                print("Your SAT Math score is closest to mean Math score among most undergraduates in the major of "
                      + str(career))
                print("")

            n += 1
            if n > 34:
                intendmajor.close()
                break


# evaluates score to determine which major it is closest to
def closestScore(s, cn):
    # s = test score
    # cn = column number
    with open("satintendedmajors.csv") as intendmajor:

        readCSV = csv.reader(intendmajor, delimiter=',')

        scoreList = []
        diff = []

        # initializes value to count over iterations and end loop when certain number is reached\
        n = 0
        # appends differences between the user's test score and each column score
        for column in readCSV:
            if n > 33:
                break
            scores = column[cn]
            if scores == "Math" or scores == "" or scores == "Evidence-based reading and writing (ERW)":
                continue
            difference = abs(int(s) - int(scores))
            diff.append(difference)
            scoreList.append(scores)
            n += 1
    intendmajor.close()

    # finds index position of the closest score
    for m in range(len(diff)):
        if diff[m] == min(diff):
            indexPos = m
            nearestScore = scoreList[indexPos]
            careerReturn(nearestScore, cn)


def satScore():
    print("This test will ask for your Evidence-Based Reading and Writing Score and your Math score scored on the SAT.")
    print("NOTE: This test is merely to give you the idea of what the average test range is for a given major. Do not"
          "think that this score is required or even necessary to pursue a certain career.")
    print("")
    erw = input("What is your highest score achieved on the Evidence-Based Reading and Writing section?")
    math = input("What is your highest score achieved on the Math section?")

    with open("satintendedmajors.csv") as intendmajor:

        readCSV = csv.reader(intendmajor, delimiter=',')

        # initializes a value to count iterations. Once over the row count, sends to new function to find next closest
        # match
        # m and j are used to count iterations over the if statements. Used to determine if equality has been found
        n = 0
        m = 0
        j = 0
        # case when equality is found for erw and math
        for column in readCSV:

            erwScores = column[2]
            mathScores = column[3]
            career = column[0]

            if erwScores == erw:
                print("Your SAT ERW score falls in the mean ERW score among most undergraduates in the major of "
                      + str(career))
                print("")
                m += 1
            if mathScores == math:
                print("Your SAT Math score falls in the mean Math score among most undergraduates in the major of "
                      + str(career))
                print("")
                m += 1
            n = n + 1
            # case of no matching scores
            if n > 34 and m == 0 and j == 0:
                closestScore(int(erw), 2)
                closestScore(int(math), 3)
                return
            # case of both matching scores
            elif n > 34 and m > 0 and j > 0:
                return
            # case of matching erw but not math
            elif n > 34 and m > 0 and j == 0:
                closestScore(int(math), 3)
                return
            # case of matching math but not erw
            elif n > 34 and m == 0 and j > 0:
                closestScore(int(erw), 2)
                return


# contains the information to conduct the RIASEC test
def riasecTest():

    # Menu print for general information of test
    print("---RIASEC Test---")
    print("General Information: You will be asked a series of questions to determine your 3-letter Holland Code")
    print("This testing information is taken from the laborfiles on delware.gov")
    print("link: https://laborfiles.delaware.gov/main/lmi/publications/Career_Compass_2021-2022.pdf")
    print("")

    # initializes Holland letters at value 0 as a list, each question function will add to each of these scores
    # riasecscore[0] = R score, riasecscore[1] = I score
    riasecscore = [0, 0, 0, 0, 0, 0]

    # "I am" questions
    # defines lists for different "I am", "I can", "I like to" questions
    rtraits = ["practical", "athletic", "mechanically inclined", "a nature lover", "shy or modest", "persistent"]
    itraits = ["scientific", "precise", "self-motivated", "analytical", "observant", "curious"]
    atraits = ["creative", "imaginative", "innovative", "sensitive or emotional", "independent", "intuitive"]
    straits = ["friendly", "generous", "helpful", "patient", "cooperative", "idealistic"]
    etraits = ["self-confident", "persuasive", "sociable", "ambitious", "impulsive", "optimistic"]
    ctraits = ["well organized", "efficient", "systematic", "conscientious", "accurate", "polite"]

    rabilities = ["fix electronic equipment", "play a sport", "work on cars", "read a blueprint",
                  "operate tools and machinery", "pitch a tent"]
    iabilities = ["think abstractly", "solve math problems", "analyze data", "use a microscope or computer",
                  "do complex calculations", "conduct research"]
    aabilities = ["sketch, draw, paint", "play a musical instrument", "write stories or poems", "sing, act or dance",
                  "design fashion or interiors", "work independently"]
    sabilities = ["teach others", "express myself clearly", "lead a group discussion", "mediate disputes",
                  "plan or supervise an activity", "offer others guidance"]
    eabilities = ["convince others to do things my way", "sell things or promote ideas", "give talks or speeches",
                  "lead a group", "initiate projects", "manage people or products"]
    cabilities = ["work well within a system", "keep accurate records", "use a computer",
                  "write effective business letters", "operate office machines", "create charts and graphs"]

    rinterests = ["work with my hands", "be physically active", "train/tend to animals", "work outdoors",
                  "hunt or fish", "build or repair things"]
    iinterests = ["use computers", "perform lab experiments", "solve math or science questions",
                  "analyze situations and find solutions", "do puzzles", "work independently"]
    ainterests = ["attend concerts/plays", "paint, sculpt, do ceramics", "read fiction and poetry", "take photographs",
                  "decorate", "work on crafts"]
    sinterests = ["work and socialize with others", "help people solve problems", "do volunteer work",
                  "work with children or elderly", "play team sports", "organize parties"]
    einterests = ["make decisions affecting others", "run a political campaign", "start own business",
                  "be with leaders", "work on a sales campaign", "win awards"]
    cinterests = ["work with numbers", "be responsible for details", "collect or organize things", "follow a budget",
                  "keep things neat", "play board games"]

    # uses questions from laborfiles.delware.gov to sum Holland code letters
    iAm(riasecscore, rtraits, 0)
    iAm(riasecscore, itraits, 1)
    iAm(riasecscore, atraits, 2)
    iAm(riasecscore, straits, 3)
    iAm(riasecscore, etraits, 4)
    iAm(riasecscore, ctraits, 5)

    iCan(riasecscore, rabilities, 0)
    iCan(riasecscore, iabilities, 1)
    iCan(riasecscore, aabilities, 2)
    iCan(riasecscore, sabilities, 3)
    iCan(riasecscore, eabilities, 4)
    iCan(riasecscore, cabilities, 5)

    iLikeTo(riasecscore, rinterests, 0)
    iLikeTo(riasecscore, iinterests, 1)
    iLikeTo(riasecscore, ainterests, 2)
    iLikeTo(riasecscore, sinterests, 3)
    iLikeTo(riasecscore, einterests, 4)
    iLikeTo(riasecscore, cinterests, 5)

    # sends riasecscore to function to deal with ties
    tie(riasecscore)

    # calls letterscore() function to obtain a variable for the 3-letter Holland Code
    hollandCode = letterscore(riasecscore)

    printAll(riasecscore)
    print("Taking your three highest letter scores, your 3-letter Holland Code is:" + str(hollandCode))

    findMajor(hollandCode)


# given the riasecscore, print all outcomes of the test
def findMajor(hc):
    # hc = Holland Code

    # open csv file to search for Holland code
    with open("satintendedmajors.csv") as intendmajor:

        readCSV = csv.reader(intendmajor, delimiter=',')

        # initializes values to track printing
        n = 0
        m = 0
        for column in readCSV:
            # ohc = occupational holland code
            # defines variables to the columns that contain necessary information
            ohc = column[4]
            matchCareer = column[0]
            # if user's holland code matches one in the csv file, it prints the output
            if ohc == hc:
                print("The major corresponding to your Holland code, " + hc + " is " + str(matchCareer))
                m = m + 1

            n = n + 1

            # if all columns have been searched (n > 35) and no matching career has been printed (m < 1)
            if n > 35 and m == 0:
                print("There was not a holland code that matches a career in the database. "
                      "Because of the small selection of majors chosen by SAT in the table used, some combinations "
                      "of Holland codes may not be present in the database. Future expansions of the program may "
                      "yield a larger pool of Holland code combinations.")
                break
            elif n > 35 and m > 0:
                break
    intendmajor.close()


# determines the strength of the user's three letter score by averaging the 3 letter values
def scoreStrength(ts):
    # ts = three scores of three largest Holland letters
    avg = sum(ts)/len(ts)
    print(" ")
    print("Your strength of score is " + str(avg))
    print("Your strength of score is an average of the largest Holland letter scores. The closer the average is to 18,"
          "the more 1s you responded with in each section and therefore, the more strongly you identify with your "
          "score")
    print(" ")


def printAll(rs):
    # rs = riasecscore
    letterCode = {0: "R", 1: "I", 2: "A", 3: "S", 4: "E", 5: "C"}
    rsprint = " "

    for n in range(len(rs)):
        rsprint = rsprint + letterCode[n] + ": " + str(rs[n]) + "  "
    print(rsprint)


# deals with ties in holland scores
def tie(rs):
    # rs = riasecscore
    # based on information from
    # link: https://www.hopkinsmedicine.org/fac_development/_documents/lisa_heiser_faculty_development_handout.pdf

    # find ties/repeats ties[] contains duplicates, newTies[] does not
    ties = []
    newTies = []

    # compares first index value to all others to find equality, appends to list, then repeats with next index value
    for n in range(len(rs)):
        for m in range(len(rs)):
            if rs[n] == rs[m]:
                # condition to avoid equality among same positions
                if m == n:
                    continue
                else:
                    ties.append(n)

    # exits function if no ties are found
    if len(ties) == 0:
        return
    # removes duplicates
    for n in ties:
        # if the same value is in the newties list (a duplicate) then the function does not add this value
        if n in newTies:
            continue
        else:
            newTies.append(n)

    riasecQuestions = ["1. active, stable, enjoy hands-on activities\n",
                       "2. analytical, intellectual, observant\n",
                       "3. original, intuitive, imaginative\n",
                       "4. humanistic, idealistic, responsible\n",
                       "5. energetic, ambitious, adventurous\n",
                       "6. efficient, careful, organized\n"]
    questionSet = ""
    for n in range(0, len(newTies)):
        questionSet = questionSet + riasecQuestions[newTies[n]]
    number = int(input("Which trait list do you believe best describes you (input corresponding number)?"
                       "\n" + questionSet))

    indexPos = number - 1
    rs[indexPos] = rs[indexPos] + 1


# creates the 3-letter Holland code based on user's survey
def letterscore(rs):
    # rs = riasecscore
    # dictionary to relate index positions to RIASEC letters
    letterCode = {0: "R", 1: "I", 2: "A", 3: "S", 4: "E", 5: "C"}
    threeLetters = ""
    n = 0

    # stores the three scores of the riasecscore as numbers
    threeScores = []
    while len(threeLetters) < 3:
        # finds index position of maximum values and appends them to threeLetters
        # rs[n] sets the maximum's value to 0 so that other (smaller) maximums can be found
        if rs[n] == max(rs):
            threeLetters = threeLetters + str(letterCode[n])
            threeScores.append(rs[n])
            rs[n] = 0
        n = n + 1

        # if another max has been passed over because previous max was larger
        # (say rs[0] = 12 and rs[1] = 18),
        # resets n to 0 to continue searching through rs from beginning
        if n > 5:
            n = 0

        # terminating case
        if len(threeLetters) >= 4:
            # ensures code is only 3 letters by indexing first 3 letters
            threeLetters = threeLetters[0:3]
            break
    scoreStrength(threeScores)
    return threeLetters


# riasecscore = [12, 8, 8, 15, 6, 3]
# print(letterscore(riasecscore))
# functions for asking survey for Holland code
def iAm(sl, tl, num):
    # sl = score list
    # tl = trait list
    # num = index for riasec score
    for n in range(len(tl)):
        response = int(input("Respond with 1 for yes or 0 for no: I am " + tl[n]))
        sl[num] = sl[num] + response


def iCan(sl, tl, num):
    # sl = score list
    # tl = trait list
    # num = index for riasec score
    for n in range(len(tl)):
        response = int(input("Respond with 1 for yes or 0 for no: I can " + tl[n]))
        sl[num] = sl[num] + response


def iLikeTo(sl, tl, num):
    # sl = score list
    # tl = trait list
    # num = index for riasec score
    for n in range(len(tl)):
        response = int(input("Respond with 1 for yes or 0 for no: I like to " + tl[n]))
        sl[num] = sl[num] + response


def main():

    menu()
    choice()


main()
