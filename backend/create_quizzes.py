from quizzes.models import Quiz, Question, Choice

# Create Python Quiz
python_quiz = Quiz.objects.create(
    title="Python Fundamentals",
    description="Test your knowledge of Python basics and core concepts",
    subject="Programming",
    difficulty="medium",
    time_limit=10  # 10 minutes
)

# Question 1
q1 = Question.objects.create(
    quiz=python_quiz,
    text="What is the output of print(type([]))?",
    explanation="In Python, [] creates an empty list. The type() function returns the type of the object, which for a list is <class 'list'>.",
    order=1
)

Choice.objects.create(question=q1, text="<class 'list'>", is_correct=True)
Choice.objects.create(question=q1, text="<class 'array'>", is_correct=False)
Choice.objects.create(question=q1, text="<class 'dict'>", is_correct=False)
Choice.objects.create(question=q1, text="<class 'tuple'>", is_correct=False)

# Question 2
q2 = Question.objects.create(
    quiz=python_quiz,
    text="Which of the following is NOT a valid way to create a dictionary in Python?",
    explanation="In Python, dictionaries can be created using {}, dict(), or dict comprehension. The syntax dict[key] = value is used to add items to an existing dictionary, not to create a new one.",
    order=2
)

Choice.objects.create(question=q2, text="a = {}", is_correct=False)
Choice.objects.create(question=q2, text="a = dict()", is_correct=False)
Choice.objects.create(question=q2, text="a = {x: x**2 for x in range(3)}", is_correct=False)
Choice.objects.create(question=q2, text="a = dict[1:2, 3:4]", is_correct=True)

# Question 3
q3 = Question.objects.create(
    quiz=python_quiz,
    text="What does the 'self' parameter in a class method refer to?",
    explanation="In Python class methods, 'self' refers to the instance of the class. It's a convention to name the first parameter 'self', which allows you to access the attributes and methods of the class within the method.",
    order=3
)

Choice.objects.create(question=q3, text="It refers to the instance of the class", is_correct=True)
Choice.objects.create(question=q3, text="It refers to the class itself", is_correct=False)
Choice.objects.create(question=q3, text="It refers to the parent class", is_correct=False)
Choice.objects.create(question=q3, text="It is a reserved keyword in Python", is_correct=False)

# Question 4
q4 = Question.objects.create(
    quiz=python_quiz,
    text="What is the output of the following code?\nlist = [1, 2, 3, 4]\nprint(list[-2])",
    explanation="In Python, negative indices count from the end of the list. list[-1] is the last element, list[-2] is the second-to-last element, and so on. So list[-2] with list = [1, 2, 3, 4] returns 3.",
    order=4
)

Choice.objects.create(question=q4, text="3", is_correct=True)
Choice.objects.create(question=q4, text="2", is_correct=False)
Choice.objects.create(question=q4, text="4", is_correct=False)
Choice.objects.create(question=q4, text="Error", is_correct=False)

# Question 5
q5 = Question.objects.create(
    quiz=python_quiz,
    text="Which of the following is a mutable data type in Python?",
    explanation="In Python, lists are mutable (can be changed after creation), while strings, tuples, and integers are immutable (cannot be changed after creation).",
    order=5
)

Choice.objects.create(question=q5, text="List", is_correct=True)
Choice.objects.create(question=q5, text="String", is_correct=False)
Choice.objects.create(question=q5, text="Tuple", is_correct=False)
Choice.objects.create(question=q5, text="Integer", is_correct=False)

# Create JavaScript Quiz
js_quiz = Quiz.objects.create(
    title="JavaScript Essentials",
    description="Test your knowledge of JavaScript fundamentals",
    subject="Programming",
    difficulty="medium",
    time_limit=10  # 10 minutes
)

# Question 1
q1 = Question.objects.create(
    quiz=js_quiz,
    text="What will be the output of console.log(typeof []);",
    explanation="In JavaScript, typeof [] returns 'object'. Arrays are a special type of object in JavaScript.",
    order=1
)

Choice.objects.create(question=q1, text="'object'", is_correct=True)
Choice.objects.create(question=q1, text="'array'", is_correct=False)
Choice.objects.create(question=q1, text="'list'", is_correct=False)
Choice.objects.create(question=q1, text="'undefined'", is_correct=False)

# Question 2
q2 = Question.objects.create(
    quiz=js_quiz,
    text="Which of the following is NOT a JavaScript data type?",
    explanation="JavaScript has six primitive data types: string, number, boolean, null, undefined, and symbol (added in ES6). 'Character' is not a separate data type in JavaScript; individual characters are represented as strings of length 1.",
    order=2
)

Choice.objects.create(question=q2, text="String", is_correct=False)
Choice.objects.create(question=q2, text="Number", is_correct=False)
Choice.objects.create(question=q2, text="Boolean", is_correct=False)
Choice.objects.create(question=q2, text="Character", is_correct=True)

# Question 3
q3 = Question.objects.create(
    quiz=js_quiz,
    text="What is the correct way to check if a variable 'x' is equal to 5 in value and type?",
    explanation="In JavaScript, the === operator checks for both value and type equality, while == only checks for value equality after type conversion.",
    order=3
)

Choice.objects.create(question=q3, text="x === 5", is_correct=True)
Choice.objects.create(question=q3, text="x == 5", is_correct=False)
Choice.objects.create(question=q3, text="x = 5", is_correct=False)
Choice.objects.create(question=q3, text="x.equals(5)", is_correct=False)

# Question 4
q4 = Question.objects.create(
    quiz=js_quiz,
    text="What will be the output of console.log(2 + '2');",
    explanation="In JavaScript, when you use the + operator with a string and a number, the number is converted to a string and concatenated. So 2 + '2' becomes '22'.",
    order=4
)

Choice.objects.create(question=q4, text="'22'", is_correct=True)
Choice.objects.create(question=q4, text="4", is_correct=False)
Choice.objects.create(question=q4, text="'4'", is_correct=False)
Choice.objects.create(question=q4, text="NaN", is_correct=False)

# Question 5
q5 = Question.objects.create(
    quiz=js_quiz,
    text="Which method is used to add an element to the end of an array in JavaScript?",
    explanation="In JavaScript, the push() method adds one or more elements to the end of an array and returns the new length of the array.",
    order=5
)

Choice.objects.create(question=q5, text="push()", is_correct=True)
Choice.objects.create(question=q5, text="append()", is_correct=False)
Choice.objects.create(question=q5, text="add()", is_correct=False)
Choice.objects.create(question=q5, text="insert()", is_correct=False)

print("Successfully created 2 quizzes with 5 questions each!")
