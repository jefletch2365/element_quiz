import argparse
import csv
import random
import sys

def main():
    #CLI optional: -e -m -x, -q questions(int)
    elem_max, quest_max = parse()
    try:
        score = question(quest_max, elem_max)
    except EOFError:
        sys.exit("incomplete")
    print(f"{score} correct out of {quest_max}")
    final = int(outcome(score, quest_max))
    g = grade(final)
    if final == 100:
        print("💯 - you get and A!")
    else:
        print(f"{final}% is a {g}")

def parse():
    max = 54
    q = 10
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group() #type=class
    group.add_argument("-e", help="easy mode", action="store_true")
    group.add_argument("-m", help="medium mode", action="store_true")
    group.add_argument("-x", help="hard mode", action="store_true")
    parser.add_argument("-q", "--questions",type=int, help="how many questions") #
    args = parser.parse_args()
    if args.e:
        max = 18
    elif args.x:
        max = 102
    if args.questions != None:
        q = args.questions
    return max, q

def what_element(max):
    element_number = random.randint(1, max)
    return element_number

def question_type():
    element_type = random.choice(["name", "symbol"])
    return element_type

def choose(elem_max):
        n = what_element(elem_max)
        element_type = question_type()
        return n, element_type

def outcome(score, q):
    percent = (score / q * 100)
    return(percent)

def grade(score):
    if 90 <= score:
        g = "A"
    elif 80 <= score:
        g = "B"
    elif 70 <= score:
        g = "C"
    elif 60 <= score:
        g = "D"
    else:
        g = "F"
    return g

def question(q, elem_max): #, element_number, element_type):
    correct = 0
    n = 5
    elements = []
    with open("LeanPeriodicTable.csv", "r") as read_file:
        reader = csv.DictReader(read_file)
        for row in reader:
            #name, number, symbol = (row["name"], int(row["number"]), row["symbol"])
            elements.append(row)
        for _ in range(q): # how many questions
            n, element_type = choose(elem_max)
            #print(n, element_type)
            for element in elements:
                if (n == int(element["number"]) and element_type == "symbol"):
                    print(f"{element['symbol']}: ")
                    name_answer = input().capitalize()
                    if name_answer == element["name"]:
                        print("Correct! 😎")
                        correct += 1
                    else:
                        print("Incorrect")

                elif (n == int(element["number"]) and element_type == "name"):
                    print(f"{element["name"]}: ")
                    symbol_answer = input()
                    if symbol_answer == element["symbol"]:
                        print("Correct! 😎")
                        correct += 1
                    else:
                        print("Incorrect")
        return correct

if __name__ == "__main__":
    main()
