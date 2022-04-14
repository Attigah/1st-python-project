print("Welcome to my 1st comp quiz proj")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Make we play :)")

answer = input("What does FTP stand for? ")
if answer == "file transfer protocol":
    print('correct!')
else:
    print('Incorrect!')


answer = input("What is the full meaning of RAM? ")
if answer == "random access memory":
    print("correct!")
else:
    print("incorrect!")

answer = input("What is the full meaning of cpu? ")
if answer == "control processing unit":
    print("correct!")
else:
    print("incorrect!")

answer = input("What does GPU stand for? ")
if answer == "graphics display unit":
    print("correct!")
else:
    print("incorrect!")