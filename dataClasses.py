#course info   
class Course():
    def _init_(courseName,courseNumber):
        self.courseName=courseName
        self.courseNumber=courseNumber
#exam date and moed
class Exam:
    def _init_(self,year):
        self.year=year
#question info
class Question(Exam):
    def _init_(self,NoQuestion,questionType,difficultyLevel):
        self.NoQuestion=NoQuestion
        self.questionType=questionType
        self.difficultyLevel=difficultyLevel
#student info
class Student():
    def _init_(self,firstName,lastName,year=0):
        self.firstName=firstName
        self.lastName=lastName
        self.year=year
#Lecturer info
class Lecturer(Student,Course):
    def _init_(yearOfExprience):
        super()._init_(firstName,lastName,year)
        super()._init_(courseName,courseNumber)
        self.yearOfExprience=yearOfExprience          
#Rakaz info
class Coordinator(Lecturer):
    def _init_(self,department):
        self.department
