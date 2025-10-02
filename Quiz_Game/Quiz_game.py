print("Welcome To Quiz")
play=input ("Do you want to play: yes or no \n" ).lower() 
if play!="yes":
    quit()

print("let's play")
score=0

answer=input("Expand RGB \n").lower()
if answer=="red green blue":
    print("Bingooo!\n")
    score +=1
else:
    print("incorrect, it is red green blue \n")

answer=input("Expand YOLO \n").lower()
if answer=="you only live once":
    print("Bingooo! \n")
    score +=1
else:
    print("incorrect, it is you only live once \n")

answer=input("Expand GPU \n").lower()
if answer=="graphics processing unit":
    print("Bingooo! \n")
    score +=1
else:
    print("incorrect, it is graphics processing unit\n")

answer=input("Expand UFO \n").lower()
if answer=="unidentified flying object":
    print("Bingooo! \n")
    score +=1
else:
    print("incorrect, it is unidentified flying object \n")

answer=input("Expand GTA \n").lower()
if answer=="grand theft auto":
    print("Bingooo! \n")
    score +=1
else:
    print("incorrect, it is grand theft auto \n")

print ("you got " + str(score) + " correct")
print ("you got " + str((score/5)*100) + "%")




