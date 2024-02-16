linesClean = []
with open("items.txt", "r") as file:
    lines = file.readlines()
    linesClean = [("execute if score finalItem votesRandomized = " + i.capitalize()[:-1] + " votes run tag @a add exists\n")  for i in lines ]

with open("items.txt", "w") as file:
    for i in linesClean:
        file.write(i)