# PERIODIC TABLE QUIZ GAME
#### Video Demo:  https://youtu.be/WQg6-MYycVI
#### Description: This is a quiz game where users can test their knowledge of the periodic table.

I am a chemist and my kids are taking chemistry this year. I thought it would be fun to have them review the periodic table by playing a game.
There are 3 different levels of difficulty, and the user can choose the number of questions per quiz.

Questions will display elements' symbol or name based on a random function. It will expect the user to type the opposite (If name is given, user will respond with symbol. If symbol is given, user will respons with name).

At the end of the quiz, the user will be provided with the number of questions correct out of total questions, their percent correct, and a letter grade based on the score.

Seven functions were written to facilitate use of this game.

## parse()
Parse function will accept Command Line Interface inputs and return values to be used in other functions.
CLI is optional for difficulty and number of questions

```
     -e (easy) elements 1-18
     -m (med) elements 1-54
     -x (hard) elements 1-102
     -q + number of questions
```

This function returns two values:
     max (maximum number of elements)
     q (number of questions)
If no CLI is used, default is medium difficulty and 10 questions.

## what_element(max)
A random function was used to select a random element number between 1 and max.

## question_type()
A random function used to choose between name or symbol. This determines what type of question will present to the user.

## choose(elem_max)
The choose function will run the what_element and question_type functions to choose a random element and question type.

## outcome(score, q)
The outcome function calculates the score as a percentage of total questions.

## grade(score)
Calculates a grade based on the percent returned in outcome().

90 <= score = "A"
80 <= score = "B"
70 <= score = "C"
60 <= score = "D"
0  <= score = "F"

## question(q, elem_max)
This function is the heart of the quiz. It opens the LeanPeriodicTable.csv to read element data. It appends data to a list called elements. For each question (q), the function will read the list, print either a name or symbol of an element based on choose(), compare user input to the elements list, and print either "Correct" or "Incorrect."

# python project.py
CLI optional for for difficulty and number of questions
```
     -e (easy) elements 1-18
     -m (med) elements 1-54
     -x  (hard) elements all
     -q number of Qs
     If no CLI is used, default is medium difficulty and 10 questions
```
The user will be presented with the requested number of questions.
A random question of an element's name or symbol will be shown.
User types the answer (If Symbol is shown, enter name. If name is shown, enter symbol)
Program will output "Correct" or "Incorrect" after each question.

## After all questions have been answered, quiz score (%) and grade (A-F) will be posted
```
90 <= score = "A"
80 <= score = "B"
70 <= score = "C"
60 <= score = "D"
0  <= score = "F"
```

# Exit Early
Ctrl-d to exit the quiz early for an "incomplete"
CLI errors will exit the program

#
Questions will display elements' symbol or name based on a random function. It will expect the user to type the opposite.

At the end of the quiz, the user will be provided with the number of questions correct out of total questions, their percent correct, and a letter grade based on the score.
LeanPeriodicTable.csv utilizes source data from
https://github.com/Bowserinator/Periodic-Table-JSON
