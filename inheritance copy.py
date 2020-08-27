class Person:
    def __init__(self,firstName,lastName,idNum):
        
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
            print("Name:", self.lastName + ",", self.firstName)
            print("ID:", self.idNumber)
class Student(Person):
    def __init__(self,firstName,lastName,idNum,scores):
        self.firstName=firstName
        self.lastName=lastName
        self.idNumber=idNum
        self.scores=scores
    def calculate(self):
        tot = (int(sum(scores)/len(scores)))
        if tot >= 90 and tot <= 100:
            return('O')
        elif tot >= 80 and tot <90:
            return('E')
        elif tot >= 70 and tot <80:
            return('A')
        elif tot >= 55 and tot <70:
            return('P')
        elif tot >= 40 and tot <55:
            return('D')
        elif tot < 40:
            return('T')
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
