import json
import requests
import pandas as pd

#Example from CS3240 website
clist = [('CS', '3100')] #these are the courses we're interested in
url = 'https://sisuva.admin.virginia.edu/psc/ihprd/UVSS/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch?institution=UVA01&term=1248&page=1'
df = pd.DataFrame(columns=['subject','catalog_num','section','component', 'desc', 'course_idnum', 'enroll_cap', 'enroll_avail'])


for c in clist: #for each course
    #TODO: Pull from the json, populaitng the dataframe with data below.

    r = requests.get(url + '&subject=' + c[0] + '&catalog_nbr=' + c[1]) #get a json with the prefix and number
    for c in r.json():
        df.loc[len(df)] = [c['subject'], c['catalog_nbr'],c['class_section'], c['component'], c['descr'], c['class_nbr'], c['class_capacity'], c['enrollment_available'] ]
        print(c['subject'], c['catalog_nbr'] + '-' + c['class_section'], c['component'], c['descr'], 
                  c['class_nbr'], c['class_capacity'], c['enrollment_available']) #c['meetings']
        
print(df)