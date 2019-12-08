import re
days_list = ['M', 'W', 'Tu', 'Th', 'F', 'TBA']
desctypes = ['-DIS', '-LEC', '-LAB']
removals = ['1.0', '2.0', '3.0', '4.0', '5.0', 'Discussion', 'Lecture', 'Laboratory','\t']
inp = '''AFRICAM 27AC	Discussion -DIS
W 4:00P-4:59P
AFRICAM 27AC	Lecture -LEC
TuTh 2:00P-3:29P
3.0'''
inpfull = '''
AFRICAM 27AC	Discussion -DIS
W 4:00P-4:59P
AFRICAM 27AC	Lecture -LEC
TuTh 2:00P-3:29P
3.0
ASTRON C10	Lecture -LEC
MWF 3:00P-3:59P
4.0
ASTRON C10	Discussion -DIS
Th 11:00A-11:59A
COMPSCI 61A	Discussion -DIS
TBA
COMPSCI 61A	Laboratory -LAB
COMPSCI 61A	Lecture -LEC
MW 2:00P-2:59P
F 2:00P-2:59P
4.0
COMPSCI 70	Discussion -DIS
TBA
COMPSCI 70	Lecture -LEC
TuTh 3:30P-4:59P
4.0
'''
inpramesh = ''' COMLIT 60AC	Discussion -DIS
F 12:00P-12:59P
COMLIT 60AC	Lecture -LEC
MWF 10:00A-10:59A
4.0
COMPSCI 61A	Discussion -DIS
TBA
COMPSCI 61A	Laboratory -LAB
COMPSCI 61A	Lecture -LEC
MW 2:00P-2:59P
F 2:00P-2:59P
4.0
ELENG 16A	Laboratory -LAB
Th 5:00P-7:59P
ELENG 16A	Discussion -DIS
TBA
ELENG 16A	Lecture -LEC
TuTh 12:30P-1:59P
4.0
RHETOR R1A	Lecture -LEC
MWF 4:00P-4:59P
4.0'''

class Class():
    classes = []
    def __init__(self, desc, days, times):
        self.desc = desc
        self.days = [day for day in days_list if day in days]
        if len(times)<12:
            self.tstart = times[:5]
            self.tend = times[6:]
        else:
            self.tstart = times[:6]
            self.tend = times[7:]
        Class.classes.append(self)

def cleaner(inp):
    for s in removals:
        if s in inp:
            inp = inp.replace(s, '')
    return inp

def classifier(s):
    for t in desctypes:
        if t in s:
            return 'desc'
    try: l = s.split()[0]
    except: l=''
    for day in days_list:
        if day in l:
            l = l.replace(day, '')
    return 'time' if not len(l) else 'unknown'

def main_func(s):
    split_input = re.split('\n',cleaner(s))
    while True:
        try: split_input.remove('')
        except: break

    for i in range(len(split_input)):
        currtoken = split_input[i]
        try: nexttoken = split_input[i+1]
        except: nexttoken = ''
        currclass = classifier(currtoken)
        nextclass = classifier(nexttoken)
        if currclass == 'desc' and nextclass == 'time':
            split_nexttoken = nexttoken.split()
            try: temp = Class(currtoken, split_nexttoken[0], split_nexttoken[1])
            except: temp = Class(currtoken, split_nexttoken[0], split_nexttoken[0])

    return [[self.desc,self.days,self.tstart,self.tend] for self in Class.classes]

#print(main_func(inpfull))

# main_func() returns a list of lists, each of which has three elements representing a class
# (description, days, and time). These can also be accessed through Class.classes, which
# contains the class instances, which can then be used to access class properties
# (description, days, and time).
