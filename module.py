import time
from sympy import simplify

import numpy
import random
import itertools
from PyQt4.QtGui import QWidget
from PyQt4.QtCore import QTimer

def moduleInitial(A):
    globals().update(A)

class password(QWidget):
    def __init__(self,structurs):
        '''"structue" is a list in follow form:
                s1=['abc','abcd','abd']
                s2=['a12','b34']
                s3=['ade','gt!']
                structue=[s1,s2,s3]
                
                generated password is in this si structurs:
                for example s1:
                    pass[0] in 'abc'
                    pass[1] in 'abcd'
                    pass[2] in 'abd'
                    len(pass)==3'''
        structurs=[[''.join(sorted(set(sti))) for sti in st] for st in structurs]
        self.structurs=structurs
        self.stoped=False
        self.active=True
        self.timer=QTimer()
        self.timer.timeout.connect(self.setStop)

    def setNew(self):
        self.stoped=False
        self.active=True
        
    def setStop(self):
        self.stoped=True
        self.active=False

    def setStopArgs(self,N,T):
        self.N=N
        self.T=T

    def initDatabase(self,dist,treshold):
        for st in self.structurs:
            if dist=='Mono frequency':
                    temp1db(st,treshold)
            elif dist=='Dual frequency':
                temp2db(st,treshold)
            elif dist=='Triple frequency':
                temp3db(st,treshold)
            elif dist=='Brut force':
                tempdb(st,treshold)

            import temp
            return temp.G(st)


def temp1db(args,treshold):
    L=len(args)
    f=open('temp.py','w')
    f.write('''from database import *
def G(args):\n''')
    for i in range(L):
        f.write('    '*i+'    for a'+str(i)+' in '+repr(args[i])+':\n')
        f.write('    '*i+'        p'+str(i)+'=freq1[a'+str(i)+']*p'+str(i-1)+'\n')
        f.write('    '*i+'        if p'+str(i)+'<'+str(treshold)+': continue\n')
    f.write('    '*i+'        yield a'+'+ a'.join([str(i) for i in range(L)])+'\n')

    f.close()

def temp2db(args,treshold):
    L=len(args)
    f=open('temp.py','w')
    f.write('''from database import *
def G(args):
    for a0 in '''+repr(args[i])+''':
        p0=freq1[a0]\n
        if p0<'''+str(treshold)+': continue\n')
    for i in range(1,L):
        f.write('    '*i+'    for a'+str(i)+' in '+repr(args[i])+':\n')
        f.write('    '*i+'        p'+str(i)+'=freq2[a'+str(i-1)+'+a'+str(i)+']*p'+str(i-1)+'\n')
        f.write('    '*i+'        if p'+str(i)+'<'+str(treshold)+': continue\n')
    f.write('    '*i+'        yield str(a'+'+ a'.join([str(i) for i in range(L)])+')\n')

    f.close()

def temp3db(args,treshold):
    L=len(args)
    f=open('temp.py','w')
    f.write('''from database import *
def temp3db(args):
    for a0 in '''+repr(args[i])+''':
        p0=freq1[a0]\n
        if p0<'''+str(treshold)+''': continue
        for a1 in '''+repr(args[i])+''':
            p1=p0*freq2[a0+a1]
            if p1<'''+str(treshold)+': continue\n')
            
    for i in range(2,L):
        f.write('    '*i+'    for a'+str(i)+' in '+repr(args[i])+':\n')
        f.write('    '*i+'        p'+str(i)+'=freq3[a'+str(i-2)+'+a'+str(i-1)+'+a'+str(i)+']*p'+str(i-1)+'\n')
        f.write('    '*i+'        if p'+str(i)+'<'+str(treshold)+':continue\n')
    f.write('    '*i+'        yield a'+'+ a'.join([str(i) for i in range(L)])+'\n')

    f.close()

def tempdb(args,treshold):
    L=len(args)
    f=open('temp.py','w')
    f.write('''from sympy import simplify
def G(args):\n''')
    for i in range(L):
        f.write('    '*i+'    for a'+str(i)+' in '+repr(args[i])+':\n')
    f.write('    '*i+'            yield a'+'+ a'.join([str(i) for i in range(L)])+'\n')
    f.close()




