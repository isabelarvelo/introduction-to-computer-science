# STUDENTS: In this file place utilities specific to answering trivia questions.
# Please write a method for each question that demonstrates your approach.

from faculty import *

def q1(fac):
    """Answers: How many faculty are there at Williams?
    """
    #there is one faculty member for each row in the database

    print("Q1: There are {} faculty.".format(len(fac)))


def q2(fac):
    "Who has two Bachelor's degrees from two different universities?"

    answer = []
    for i in fac:
        if len(i.degrees) >= 2:
            #assuming degrees appear in order they were granted a
            #assuming no more than two bachelor degrees
            d = i.degrees[0]
            b = i.degrees[1]
            #check if they are both bachelors degrees from different institutions
            if (b.isbac() and d.isbac()) and (b.institution != d.institution):
                answer.append(i.name)
    print("Q2: The faculty members are {}, {}, {}.".format(answer[0], answer[1],answer[2]))


def q3(fac):
    "What is the name and department of the faculty member with the longest title?"

    #list name, department, and title of each professor
    title = [[i.name, i.dept, i.title] for i in fac]

    #sort by length of title
    title.sort(key = lambda triple: len(triple[2]), reverse = True)

    #return name and department
    result = title[0][:2]

    print ("Q3: {} in the {} department has the longest title.".format(result[0], result[1]))


def q4(fac):
    "Who has the largest gap between their latest Bachelor's Degree and Ph.D.? How long is it?"

    #Don't know anybody has a Bachelor's Degree and Ph.D
    maxdiff = 0
    names = []
    #Have to set the variables for latest degrees within for loop so it resets
    #for each professor
    for i in fac:
        byear = None
        dyear = None
        for d in i.degrees:
            #set variables to most recent degree earned for each
            if d.isbac():
                byear = d.year
            if d.isdoc():
                dyear = d.year
        #return to top of loop if they don't have both Bachelor and Ph.D degrees
        if byear == None:
            continue
        if dyear == None:
            continue
        idiff = dyear - byear
        #compare difference to the max difference
        if idiff > maxdiff: #assuming there are no ties- insider knowledge from Duane
            result = [i.name, idiff]
            names.append(result)
            #reset max largest difference
            maxdiff = idiff
    result = names[-1]
    print ("Q4: {} has the largest gap of {} years between her latest Bachelor's Degree and latest Ph.D.".format(result[0], result[1]))


def q5(fac):
    "Which department has the most faculty?"

    depts = [i.dept for i in fac]
    #sort list before applying uniqCount because it assumes list is sorted
    sorteddepts = sorted(depts)
    uc = uniqCount(sorteddepts)
    #reverse sort by number of faculty in each department
    uc.sort(key = lambda pair: pair[1], reverse = True)
    result = uc[0][0]
    print ("Q5: The {} department has most the most faculty.".format(result))


def q6(fac):
    """Which four types of Master's Degrees are only held by one faculty member
    at Williams?"""

    #create a list of how many faculty have each type of Master's Degree
    types = []
    for i in fac:
        for d in i.degrees:
            if d.ismas():
                types.append(d.kind)
    degrees = sorted(types)
    degs = uniqCount(degrees)
    degs.sort(key = lambda pair: pair[1])

    print ("Q6: The four types of Master's Degrees only held by one faculty member are {}, {}, {}, and {}.".format(degs[0][0], degs[1][0], degs[2][0], degs[3][0]))


def q7(fac):
    "What is the most popular undergraduate institution."

    #list of each undergraduate institution attended by each professor
    ugs = []
    for i in fac:
        insts = set()
         #create a set of institutions just in case a professor received two
         #degrees from the same school at the same time (eg. Susan Loepp)
        for j in i.degrees:
            insts.add(str(j))
        for inst in insts:
            if j.isbac():
                ugs.append(j.institution)

    ugssort = sorted(ugs)
    pop = uniqCount(ugssort)
    pop.sort(key = lambda pair: pair[1], reverse = True)

    result = pop[0]
    print ("Q7: {} is the most popular undergraduate institution.".format(result[0]))

if __name__ == "__main__":
    db = readDB()
    q1(db)
    q2(db)
    q3(db)
    q4(db)
    q5(db)
    q6(db)
    q7(db)
