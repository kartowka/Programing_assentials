#Rakaz info
class Coordinator(Lecturer):
    department
#Lecturer info
class Lecturer(Student):
    yearOfExprience
    subjectOfTeaching
#course info   
class Cousre():
    courseName
    courseNumber
#exam date and moed
class Exam:
    year
    moed
#question info     
class Question(Exam):
    NoQuestion
    questionType
    difficultyLevel
#student info
class Student():
    firstName
    lastName
    year