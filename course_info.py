### THIS APPLICATION PARSES INFORMATION FROM THE UNDERGRADUATE SCHOOL OF INFORMATICS COMPUTING AND ENGINEERING AND ALLOWS USERS TO SEARCH THE COURSES AND OPEN THEM IN BROWSER TABS

import os
import re
import urllib.request
import random
import webbrowser
import time


def sice_courses(url):
    '''This function parses the SICE undergraduate courses webpage (accepts the url for sice.indiana.edu/undergraduate/courses/index.html) and then parses the page using a regular expression to return a list of courses available.'''

    # opening the web page and downloading the html content
    web_page = urllib.request.urlopen(url)
    contents = web_page.read() .decode(errors="replace")
    web_page.close()

    # using a regular expression to find all the courses available as a list of strings
    csci_courses = re.findall('CSCI .+?(?=</a>)', contents)

    info_courses = re.findall('INFO .+?(?=</a>)', contents)

    # ils_courses = re.findall('ILS .+?(?=</a>)', contents)

    # ise_courses = re.findall('ISE .+?(?=</a>)', contents)

    # return the courses
    return csci_courses, info_courses


def sice_browse(url, csci_courses, info_courses):
    '''Accepts the sice url and a list of csci_courses and info_courses that the user had searched for and will open up the links to them.'''

    # opening the web page and downloading the html content
    web_page = urllib.request.urlopen(url)
    contents = web_page.read() .decode(errors="replace")
    web_page.close()


    # opening up CSCI courses using the webbrowser module in new tabs
    if csci_courses:
        for course in csci_courses:
            # Key here is that findall cannot take too much of an argument, so had to index the course to the first 9 digits!
            pattern = '(?<=href=").+?(?=">' + course[0:9] + ')'
            link = re.findall(pattern, contents)
            webbrowser.open_new_tab(link[0])

    # opening up INFO courses using the webbrowser module in new tabs
    if info_courses:
        for course in info_courses:
            pattern = '(?<=href=").+?(?=">' + course[0:9] + ')'
            link = re.findall(pattern, contents)
            webbrowser.open_new_tab(link[0])


# ------------------------------------------------
#main
# ------------------------------------------------

url = 'https://www.sice.indiana.edu/undergraduate/courses/index.html'


# running the parser function and saving that to 2 lists
csci_courses, info_courses = sice_courses(url)

# outputting the information
print('Parsing: ' + url + '\n')
time.sleep(1)
print('CSCI Undergraduate Courses:')
for course in csci_courses:
    print(course)
print('\nINFO Undergraduate Courses:')
for course in info_courses:
    print(course)
print()


# Searching the INFO and CSCI courses:
while True:
    print('Parsing the CSCI and INFO courses: ' + url)
    word = input('Please enter a word to search for (or STOP): ')
    if word.upper() == 'STOP':
        break
    
    # doing a list comprehension of courses that have the word in it
    csci_search = [course for course in csci_courses if word.upper() in course.upper()]
    info_search = [course for course in info_courses if word.upper() in course.upper()]

    # printing out the results only if there was a match
    if csci_search:
        print('\nCSCI Undergraduate Courses that match:')
        for course in csci_search:
            print(course)
    else:
        print('\nNo CSCI Matches.')
    if info_search:
        print('\nINFO Undergraduate Courses that match:')
        for course in info_search:
            print(course)
    else:
        print('\nNo INFO Matches.')

    # Entering the browser opening portion of the app
    while True:
        decision = input('\nWould you like to open searched courses in your browser through this portal? (Y or N) ')
        if decision.upper() == 'Y':
            print('\nParsing the CSCI and INFO courses: ' + url)
            word = input('Enter the name of the course to open (ex: I210): ')
            
            # doing a list comprehension of courses that have the word in it (will open up in new tabs any courses that have those words in int)
            csci_search = [course for course in csci_courses if word.upper() in course.upper()]
            info_search = [course for course in info_courses if word.upper() in course.upper()]

            # sending those lists of courses to the browser opening function which will open the links in new tabs
            if csci_search or info_search:
                sice_browse(url, csci_search, info_search)
            else:
                print('There were no matches.')

        elif decision.upper() == 'N':
            break

        else:
            print('Invalid input.')
    
    print()


    
