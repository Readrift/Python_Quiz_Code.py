# Question
class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer
    
# Quiz
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        self.displayProgress()
        question = self.getQuestion()
        print(f'Question {self.questionIndex + 1}: {question.text}')
        for q in question.choices:
            print('('+q)
    
        answer = input('Answer: ')
        self.guess(answer)
        self.loadQuestion()
    
    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 10
        self.questionIndex += 1
    
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.displayProgress()
        else:
            self.displayQuestion()

    def showScore(self):
        print('score: ', self.score)
    
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print('Quiz Finished')
            self.showScore()
        else:
            print(f'Question {str(questionNumber)} of {str(totalQuestion)}'.center(100,'*'))

q1 = Question('What is a correct syntax to output "Hello World" in Python?', ['A) echo("Hello World");','B) echo "Hello World"','C) p("Hello World")','D) print("Hello World")'], 'D')
q2 = Question('How do you insert COMMENTS in Python code?', ['A) /* This is a comment */','B) #This is a comment','C) //This is a comment', 'D) *** This is a comment ***'], 'B')
q3 = Question('Which one is NOT a legal variable name?', ['A) my-var','B) my_var','C) _myvar','D) Myvar'], 'A')
q4 = Question('How do you create a variable with the numeric value 5?', ['A) x = 5','B) x = "5"',"C) x = '5'",'D) x = str(5)'], 'A')
q5 = Question('What is the correct file extension for Python files?', ['A) .py','B) .pt','C) .pyt','D) .pyth'], 'A')
q6 = Question('How do you create a variable with the floating number 2.8?', ['A) x = flt(2.8)','B) x = 2.8','C) x = int(2.8)','D) x = str(2.8)'], 'B')
q7 = Question('What is the correct syntax to output the type of a variable or object in Python?', ['A) print(type(x))','B) print(typeOf(x))','C) print(typeof(x))','D) print(typeofx)'], 'A')
q8 = Question('What is the correct way to create a function in Python?', ['A) create myFunction()','B) def myFunction ','C) function myFunction ','D) funct myFunction'], 'B')
q9 = Question('What is a correct syntax to return the first character in a string?', ['A) x = sub("Hello", 0, 1)','B) x = "Hello"[0] ','C) x = "Hello".sub(0, 1)'], 'B')
q10 = Question('Which method can be used to remove any whitespace from both the beginning and the end of a string?', ['A) trim() ','B) strip()','C) len()','D) ptrim()'], 'B')
questions = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]

quiz = Quiz(questions)
question = quiz.getQuestion()
quiz.displayQuestion()