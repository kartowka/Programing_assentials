from tkinter import *
#course info
class Course():
    def __init__(self,courseName,courseNumber):
        self.courseName=courseName
        self.courseNumber=courseNumber

#exam date and moed
class Exam(): 
    def __init__(self,year=None,semester=None,moed=None):
        self.year=year
        self.semester=semester
        self.moed=moed

#question info
class Question(Exam):
    """class Question that inhrite from base class -Exam"""



    def __init__(self,noQuestion=None,questionSubject=None,subQuestionSubject=None,numberOfParagraphs=None,difLvl=None,terms=None):
        Exam.__init__(Exam,year=None,semester=None,moed=None)
        self.noQuestion=noQuestion
        self.numberOfParagraphs
        self.questionSubject=questionSubject
        self.subQuestionSubject=subQuestionSubject
        self.difLvl=difLvl
        self.terms=terms

#user info
class User():
    def __init__(self, firstName, lastName, userName, password,phoneNumber):
        User.firstName=firstName
        User.lastName=lastName
        User.userName=userName
        User.password=password
        User.phoneNumber=phoneNumber

#student info
class Student(User):
    """class Question that inhrite from base class -User"""



    def __init__(self, year=0):
        User.__init__(User, firstName=None, lastName=None, userName=None, password=None,phoneNumber=None)
        self.year=year

#Lecturer info
class Lecturer(User,Course):
    """class Question that inhrite from base class -User,Course"""



    def __init__(yearOfExprience):
        User.__init__(User,firstName=None,lastName=None , userName=None, password=None ,year=None)
        Course.__init__(Course,courseName=None,courseNumber=None)
        Lecturer.yearOfExprience=yearOfExprience

#Rakaz info
class Coordinator(Lecturer,User):
    """class Question that inhrite from base class -Lecturer,User"""



    def __init__(self,department):
        Lecturer.__init__(self)
        self.department=department
