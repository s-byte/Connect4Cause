lista = [""]


import json
finished = True
while finished:

    answers = {}

    q1 = input("\nHow many kids do you want? ")
    answers["How many kids do you want? "] = q1


    # f = open("answers.json", "w")
    # json.dump(q1, f)


    q2 = input("\nWhat do you want you future profession to be? ")
    answers["What do you want you future profession to be? "] = q2


    # g = open("answers.json", "w")
    # json.dump(q2, g)


    q3 = input("\nWhere do you want to go to college? ")
    answers["Where do you want to go to college? "] = q3


    # h = open("answers.json", "w")
    # json.dump(q3, h) 


    q4 = input("\nWhere do you want to live? ")
    answers["Where do you want to live? "] = q4


    # i = open("answers.json", "w")
    # json.dump(q4, i)


    q5 = input("\nWhat would you rate your hair on a scale of 1-10? ")
    answers["What would you rate your hair on a scale of 1-10? "] = q5

    # j = open("answers.json", "w")
    # json.dump(q5, j)
    # f.close()

    lista.append(answers)
#

    print('These are you answers:\n')
    for x in answers.keys():
        print(answers)


    results = input("\nWould you like to see all the results?")
    if results == "yes":
        # print(*lista)
        # for y,z in answers.items():
        #      print(y,z)
        #     print(z)
        f = open("answers.json", "w")
        json.dump(answers, f) #reads form the json file and converts json to python
        f.close()

        f = open("answers.json", "r")
        olddata = json.load(f)
        print(olddata)
        f.close()

    stop = input("\nDo you want to take the survey again? Type 'yes' to take again or 'no' to stop.  ")
    if stop == "yes":
        finished != False

        if stop == "no":
            finsihed = False
            if finished == True:
                print("Thanks for taking the survey!")
                break


    else:
        # stop = input("Do you want to take the survey again? Type 'yes' to take again or 'no' to stop.  ")
        # if stop == "yes":
        #     finished != False
        #
        # if stop == "no":
        #     finsihed = False
            if finished == True:
                print("\nThanks for taking the survey!")
                break



# for a in answers.keys():
#     print(a, answers[a])
#
# for b in answers.keys():
#         print(b, answers[b])
#
# for c in answers.keys():
#     print(c, answers[c])
#
# for d in answers.keys():
#     print(d, answers[d])
#
# for e in answers.keys():
#     print(e, answers[e])
