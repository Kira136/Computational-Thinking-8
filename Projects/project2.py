Elevan_points =0
Will_points =0
Lucas_points =0
Mike_points =0
Dustin_points =0

answer1=input("wich charecter do you like better A mike B Will C Lucas D Elevan E Dustin ")
if answer1 == " A":
    Mike_points += 1
elif answer1 == " B":
    Will_points += 1
elif answer1 == " C":
    Lucas_points += 1
elif answer1 == " D":
    Elevan_points += 1
elif answer1 == " E":
    Dustin_points += 1

answer2 = input("what stranger things season is the best 1 A 2 B 3 C 4 D 5 E ")
if answer2 == " A":
    Mike_points += 1
elif answer2 == " B":
    Will_points += 1
elif answer2 == " C":
    Lucas_points += 1
elif answer2 == " D":
    Elevan_points =+ 1
elif answer2 == " E":
    Dustin_points += 1

answer3 = input(" what is the best stranger things villan A demegorgon B Vecna C demedog D mind flayer E Martin  ")
if answer3 == " A":
    Mike_points += 1
elif answer3 == " B":
    Will_points += 1
elif answer3 == " C":
    Lucas_points += 1
elif answer3 == " D":
    Elevan_points += 1
elif answer3 == " D":
    Dustin_points += 1

answer4 = input(" What is the best side chareter A hopper B Bob C derek  D eddie E Max ")
if answer4 == " A":
    Mike_points += 1
elif answer4 == " B":
    Will_points += 1
elif answer4 == " C":
    Lucas_points += 1
elif answer4 == " D":
    Elevan_points += 1
elif answer4 == " E":
    Dustin_points += 1

answer5 = input(" what is better the upside or the upside down A upsid B upside down C nether")
if answer5 == " A" or " C":
 Mike_points += 1
 Will_points += 1
elif answer5 == " B":
    Lucas_points += 1
    Elevan_points += 1 
    Dustin_points += 1

print(" if you got the most for  Elaven points your Elevan if you got the most Dustin points your Dustin if you got the most Mike points your mike if you got the most Lucas points you Lucas if you got the most Will points your will")

print(f"  Elevan {Elevan_points}")
print(f"  Dustin {Dustin_points}")

if Mike_points==(5):
    print(f" Mike {Mike_points} If we're both going crazy, then we'll go crazy together, right?")

print(f"  Will { Will_points}")
if Lucas_points==(5):
    print(f"  Lucas {Lucas_points} toltly dubular")
if Lucas_points and Elevan_points==(5):
    print("how did you get here ")