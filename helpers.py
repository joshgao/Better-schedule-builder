class Course:
    def __init__(self, prefix, number): # e. g. prefix = CS, number = 3140
        return

    content_difficulty = 0.0
    meeting_days = () #A tuple with the days of the week that you meet. 0 = sunday, 1 = monday, 2 = tues, etc.
    meeting_times = [()] #A list of tuples that correspond to the meeting days - in every tuple, first entry is begin, second is end
    prereqs = [] #A list of courses
    coreqs = []
    subsequents = [] # everything this course is a prereq for

