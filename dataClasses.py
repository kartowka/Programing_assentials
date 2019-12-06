#course info   
class Cousre():
    def _init_(courseName,courseNumber):
        self.courseName=courseName
        self.courseNumber=courseNumber
 
#exam date and moed
class Exam:
    def _init_(year):
        self.year=year
#question info     
class Question(Exam):
    def _init_(NoQuestion,questionType,difficultyLevel):
        self.NoQuestion=NoQuestion
        self.questionType=questionType
        self.difficultyLevel=difficultyLevel
#student info
class Student():
    def _init_(firstName,lastName,year):
        self.firstName=firstName
        self.lastName=lastName
        self.year=year
#Lecturer info
class Lecturer(Student):
    def _init_(yearOfExprience,subjectOfTeaching):
        self.yearOfExprience=yearOfExprience
        self.subjectOfTeaching=subjectOfTeaching            
#Rakaz info
class Coordinator(Lecturer): 
    def _init_(department):
        self.department