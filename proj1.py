print("Welcome to my 1st comp quiz proj")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Make we play :)")

answer = input("What does FTP stand for? ")
if answer == "file transfer protocol":
    print('correct')
else:
    print('Incorrect, try again')