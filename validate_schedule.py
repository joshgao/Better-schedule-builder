#Given a list of courses_taken and courses_wishlist under a Major, find whether or not there exists any conflicts in the schedule (e. g. missing requisites, time conficts, etc. )
import requests
import json
from helpers import Course, Major


def validate(courses_taken, wishlist, Major):
    for i in range(len(wishlist)):
        if wishlist[i] in courses_taken: return("You have already taken " + wishlist[i].prefix + wishlist[i].number + "and can not receive credit for it")
        for j in range(i, len(wishlist)):
            if wishlist[i] != wishlist[j] and wishlist[i].time_overlap(wishlist[j]):
                return("Time conflict")
    
    return("schedule is valid")


bacs = Major(name = "Computer Science, B.A.")
courses_taken = []
wishlist = []

