print("Welcome to my 1st comp quiz proj")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Make we play :)")
score = 0

answer = input("What does FTP stand for? ").lower()
if answer == "file transfer protocol":
    print('correct!')
    score += 1
else:
    print('Incorrect!')


answer = input("What is the full meaning of RAM? ").lower()
if answer == "random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What is the full meaning of cpu? ").lower()
if answer == "control processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics display unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")