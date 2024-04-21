#Given a list of courses_taken and courses_wishlist under a Major, find whether or not there exists any conflicts in the schedule (e. g. missing requisites, time conficts, etc. )
import requests
import json
from helpers import Course, Major

bacs = Major(name = "Computer Science, B.A.")

courses_taken = []
wishlist = []