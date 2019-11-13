class Class():
    classes = []
    def __init__(self, name, place, day, tstart, tend):
        self.name = name
        self.place = place
        self.day = day
        self.tstart = tstart
        self.tend = tend
        Class.classes.append(self)


inp = '''
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

def Spacer(lines):
    ret = ''
    for l in lines:
        if l == 'A' or l == 'P':
            yield ret
            ret = ''
        elif l == '\n':
            ret += ' '
        else:
            ret += l

def Tokenizer(line):
    line = line.split()
    line[0] += line[1]
    line.pop(1)
    line.pop(1)
    return line



