#course info   
class Course():
    def __init__(self,courseName,courseNumber):
        self.courseName=courseName
        self.courseNumber=courseNumber
#exam date and moed
class Exam(): 
    def __init__(self,year):
        self.year=year
#question info
class Question(Exam):
    def __init__(self,NoQuestion,questionType,difficultyLevel):
        Exam.__init__(Exam,year=None)
        self.NoQuestion=NoQuestion
        self.questionType=questionType
        self.difficultyLevel=difficultyLevel
#student info
class Student():
    def __init__(self,firstName,lastName,year=0):
        self.firstName=firstName
        self.lastName=lastName
        self.year=year
#Lecturer info
class Lecturer(Student,Course):
    def __init__(yearOfExprience):
        Student.__init__(Student,firstName=None,lastName=None,year=None)
        Course.__init__(Course,courseName=None,courseNumber=None)
        Lecturer.yearOfExprience=yearOfExprience          
#Rakaz info
class Coordinator(Lecturer):
    def __init__(self,department):
        Lecturer.__init__(self)
        self.department=department