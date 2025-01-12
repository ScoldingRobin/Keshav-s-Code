
questions = {
1:(1, "Select ALL Instance where AI can be used: ", ("Organize Data", "Personal Reminders", "Doing Homework", "Making a Study Plan"), (1,2,4)),
2:(1, "Please select ALL instances where third party cookies can be exploited", ("Selling Personal Information", "Saving Website Information", "Giving AD companies your prefrences"), (1,)),
3:(2, "what does IOT stand for?", ("Internet of Things", "International Online Topics", "Internet of Tech"), (1,)),
4:(2, "Please Select Non IOT device", ("Computer", "Samsung Fridge", "Incandescent lightbulb"), (3,)),
5:(2, "Please select the best definition of Environmental Considerations in Tech.", ("Considering direct and indirect implications of a Certain Device and its manufacturing, usage, and disposal", "Considering direct implications of the usage of a device", "Considering the C02 emissions caused by the production of a certain device"), (1,)),
6:(1, "How can batteries harm the environment?", ("Labour Violations", "Cobalt Mining", "High Commerical Costs", "Improper Disposal"), (2,4)),
7:(2, "What are Attitudinal Barriers?", ("Physical barriers outside or present in infrastructure that does not accommodate/ creates barriers for people with disabilities.", "Behaviors, perceptions, or assumptions that are prejudiced and/or discriminate against an individual.", "Barriers that occur when experiencing sensory disabilities, such as sight, or hearing. ", "Barriers formed when a device or technological medium is not available to everyone or cant be used with an assistive device. "), (2,)),
8:(2, "What are Systemic Barriers?", ("Physical barriers outside or present in infrastructure that does not accommodate/ creates barriers for people with disabilities.", "Behaviors, perceptions, or assumptions that are prejudiced and/or discriminate against an individual.", "Procedures that unfairly discriminate against people and can prevent people from fully participating ", "Barriers formed when a device or technological medium is not available to everyone or cant be used with an assistive device. "), (3,)),
9:(2, "Most Secure way to store and move data? ", ("In transit Encryption", "At rest Encryption", "Both 1 and 2", "None of the Above"), (3,)),
10:(2, "What of the following is Endpoint Security?", ("Securing IOT devices at the end of networks that are susceptible to malware attacks", "Protecting Data that is stored in the cloud", "Protecting networks in commercial applications", "None of the Above"), (1,)),
11:(0, "Cloud Storage is a way of storing computer data in which it is stored on servers in off-site locations. True or False?", ("True", "False"), ("t",)),
12:(2, "What is Hybrid Storage?", ("Storage systems that use a blend of SSD's and physical HDD’s. This is to provide high performance at an affordable cost", "Storage Systems that use HDD’s to provide large amounts of storage capacity at a lower cost.", "Storage Systems that use SSD’s to provide efficiency and speed. "), (1,)),
13:(2, "What is Cognitive Computing", ("Artificially making new data from existing data to train new AI models.", "Model where an already trained deep learning model generalizes on a set of new samples", "Artificially making new data from existing data to train new AI models", "An attempt to have computers emulating human thinking, and overall mimicking the human brain."), (4,)),
14:(2, "What is Deep Learning", ("Lowering the accuracy of the prediciting power of AI due to change in the real world", "Align human values and goals into AI models to keep them safe", "A method that teached AI to process data in a simialar/inspired wat to human brain"), (3,)),
15:(0, "Can AI help in Data Managment?", ("True", "False"), ("f",)),
16:(1, "What can AI help with",("Personal Assistant", "Data Managment", "Making Study Plans"), (1,2,3))
}

score = 0
def readQuestions(key):
'''
Reads Questions and print them to terminal
preconditions: key is a integer that corresponds to a valid key inside the questions dictionary
parameters: int key
returns NOTHING
'''
Quesiton = questions[key][1]
Options = questions[key][2]
print(Quesiton)
for idx, option in enumerate(Options):
print(f"#{idx+1}. {option} ")

def userInput(mode, key):
'''
takes input from the user depending on the type of question
preconditions: key is a integer that corresponds to a valid key inside the questions dictionary, and int mode is a valid mode present in the funciton
parameters: int key, int mode
returns a tuple of answers that have been validated
'''
if mode == "ans":
m = questions[key][0]
#Single Answer
if m == 2:
answers = []
data = input("Please Enter Answer(E to Skip): ")
if data == "e":
return tuple(answers)
#Validates Data
while data.isdigit() == False or int(data) > len(questions[key][2]) or int(data) < 1:
data = input("Please enter a single valid option(E to Skip): ")
if data == "e":
return tuple(answers)
answers.append(int(data))
return tuple(answers)
#Multiple Answers
if m == 1:
answers = []
#Loop so that it asks questions until the amount of options.
while len(answers) < len(questions[key][2]):
data = input("Please Enter Answer (Enter E if Done): ").strip().lower()
if data == "e":
return tuple(answers)
#Validates Data
while data.isdigit() == False or int(data) > len(questions[key][2]) or int(data) < 1:
data = input("Please enter a valid option (Enter E if done): ").strip().lower()
if data == "e":
return tuple(answers)
answers.append(int(data))
return tuple(answers)
#True and False
if m == 0:
answers = []
data = input("Please Enter Answer (T/F)(E to Skip): ").strip().lower()
if data == "e":
return tuple(answers)
while data not in ("t", "f"):
data = input("Please enter a valid option (T/F)(E to Skip):").strip().lower()
if data == "e":
return tuple(answers)
answers.append(data)
return tuple(answers)

def checkAns(questionNum, userAns):
'''
Checks if the user answer is correct
preconditions: questionNum is a integer that corresponds to a valid key inside the questions dictionary, userAns is the ans from the user
parameters: int questionNum, tuple userAns
returns NOTHING
'''
global score
#Gets the correct answers
answers = questions[questionNum][3]
#checks if it is correct
if answers == userAns:
score+=1
#Main Loop
for i in range(len(questions)):
#Checks mode and and prints the question type according to that
mode = questions[i+1][0]
if mode == 2:
type = "Single Answer"
elif mode == 1:
type = "Multichoice"
elif mode == 0:
type = "True&False"
#Prints Question Number and type
print(f"\nQuestion #{i+1} {type}\n")
#prints Question, and gets answers
readQuestions(i+1)
userAns = userInput("ans", i+1)
#checks if ans is correct
checkAns(i+1, userAns)
#Calculates Mark
mark = (score/len(questions))*100
#Prints Mark
print(f" Your Mark was {round(mark,2)}%")

