class Course:
    def __init__(self,  prefix: str , number: int, semester: str): # e. g. prefix = "CS", number = 3140, semester = "Fall 24"
        return

    content_difficulty = 0.0
    meeting_days = () #A tuple with the days of the week that you meet. 0 = sunday, 1 = monday, 2 = tues, etc.
    meeting_times = [()] #A list of tuples that correspond to the meeting days - in every tuple, first entry is begin, second is end
    prereqs = [] #A list of courses
    coreqs = []
    subsequents = [] # everything this course is a prereq for

    #TODO: make getters/setters for each of the above instance variables

class Major: #a barebones structure involving the names of courses and the requirement structure.
    def __init__(self, name) : #e.g. name = "Computer Science, B.A."
        return
    
    declaration_prereqs = [] # e.g.["CS 111X", "CS 2100"]
    core_courses = [] #["CS 2120", "CS 2130", ... "CS 3140"]
    electives = [] #["CS 3240", "CS 4774", ...]
    


    