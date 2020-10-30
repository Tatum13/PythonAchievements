import random
people = ["Waldo","Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)



x = "Waldo"
stoel = 0
print(people)

for y in people:
    stoel += 1
    if y == "Waldo":
        print("Waldo zit op stoel nummer:" + str(stoel))
