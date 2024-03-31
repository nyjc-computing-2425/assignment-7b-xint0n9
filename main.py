# Built-in imports
import math
GRADE = {}
studentdata = []
for i in range(101):
    if i < 40:
        GRADE[i] = 'U'
    elif i < 45:
        GRADE[i] = 'S'
    elif i < 50:
        GRADE[i] = 'E'
    elif i < 55:
        GRADE[i] = 'D'
    elif i < 60:
        GRADE[i] = 'C'
    elif i < 70:
        GRADE[i] = 'B'
    else:
        GRADE[i] = 'A'

def read_testscores(filename):
    """
    extracting info
    """
    with open(filename,'r') as f:
        for line in f:
            info = f.readline().strip().split(',')
            for i in range(4):
                info[i+2] = int(info[i+2])
            
            overall = (info[2]/30 * 15) + (info[3]/40 * 45) + (info[5]/30 * 20)
            overall = math.ceil(overall)
            grade = GRADE.get(overall)
            studentdata.append({'class':info[0],'name':info[1],'overall':overall,'grade':grade})
        return studentdata
def analyze_grades(studentdata):
    """
    counting number of grades in each class
    """
    analysis = {}
    for i in range(18):
        n = f'class{i+1}'
        analysis[n] = {}
        analysis[n]['A'] = 0
        analysis[n]['B'] = 0
        analysis[n]['C'] = 0
        analysis[n]['D'] = 0
        analysis[n]['E'] = 0
        analysis[n]['S'] = 0
        analysis[n]['U'] = 0
        while studentdata[i]['class'] == n:
            if studentdata[i]['grade'] == 'A':
                analysis[n]['A'] += 1
            elif studentdata[i]['grade'] == 'B':
                analysis[n]['B'] += 1
            elif studentdata[i]['grade'] == 'C':
                analysis[n]['C'] += 1
            elif studentdata[i]['grade'] == 'D':
                analysis[n]['D'] += 1
            elif studentdata[i]['grade'] == 'E':
                analysis[n]['E'] += 1
            elif studentdata[i]['grade'] == 'S':
                analysis[n]['S'] += 1
            elif studentdata[i]['grade'] == 'U':
                analysis[n]['U'] += 1
    return analysis
n = read_testscores('testscores.csv')
print(analyze_grades(n))