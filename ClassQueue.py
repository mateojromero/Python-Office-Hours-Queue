import random

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class OfficeHours:
    def __init__(self, apm):
        self.answerRate = apm
        self.currentStudent = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentStudent != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentStudent = None

    def busy(self):
        return self.currentStudent is not None

    def startNext(self,newstudent):
        self.currentStudent = newstudent
        self.timeRemaining = newstudent.getQuestions() * 60/self.answerRate

class Student:
    def __init__(self, time, ctr):
        self.timestamp = time
        self.questions = random.randrange(1, 10)
        self.position = ctr

    def getStamp(self):
        return self.timestamp

    def getQuestions(self):
        return self.questions

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, questionsPerMinute):

    teachingassistant = OfficeHours(questionsPerMinute)
    TAqueue = Queue()
    waitingtimes = []
    ctr = 0

    for currentSecond in range(numSeconds):

        if newStudent():
            ctr+= 1
            student = Student(currentSecond, ctr)
            TAqueue.enqueue(student)
            print(f"Student {student.position} arrived at second {currentSecond}. Questions: {student.getQuestions()}")

        if (not teachingassistant.busy()) and (not TAqueue.isEmpty()):
            nextStudent = TAqueue.dequeue()
            wait = nextStudent.waitTime(currentSecond)
            waitingtimes.append(wait)
            print(f"Student {nextStudent.position} started at second {currentSecond}. Wait time: {wait} seconds.")
            teachingassistant.startNext(nextStudent)
            
            
        teachingassistant.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes) if waitingtimes else 0
    print(f"Average Wait: {averageWait:.2f} seconds | {TAqueue.size()} Students remaining in the queue.")

def newStudent():
    num = random.randrange(1, 301)
    return num == 300

for i in range(5):
    print(f"\nSimulation {i + 1}:")
    simulation(3600, 1)
