# -*- coding: utf-8 -*-
import sys
import time
import string
import numpy
import webbrowser
import random
import itertools
import operator 
import threading
from module import *
from PyQt4.QtGui import QMdiSubWindow,QMdiArea,QMainWindow
from PyQt4.QtGui import QApplication,QTextEdit, QPushButton
from PyQt4.QtCore import QTimer
from sympy import simplify
import matplotlib.pyplot as plt

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class generator(QMdiSubWindow):
    def __init__(self,  parent = None):
        super(generator, self).__init__(parent)
        self.parent=parent
        self.setFixedSize(670,580)
        self.frame = QtGui.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(340, 430, 321, 131))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))

        self.checkBox_4 = QtGui.QCheckBox(self.frame)
        self.checkBox_4.setEnabled(False)
        self.checkBox_4.setGeometry(QtCore.QRect(5, 5, 221, 25))
        self.checkBox_4.setCheckable(True)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))

        self.genPass = QtGui.QPushButton(self.frame)
        self.genPass.setGeometry(QtCore.QRect(65, 90, 181, 28))
        self.genPass.setObjectName(_fromUtf8("genPass"))
        self.genPass.clicked.connect(self.strongPassword)

        self.genAPass = QtGui.QPushButton(self.frame)
        self.genAPass.setGeometry(QtCore.QRect(65, 62, 181, 28))
        self.genAPass.setObjectName(_fromUtf8("genAPass"))
        self.genAPass.clicked.connect(self.randomAPass)

        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 35, 131, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.prCombo2 = QtGui.QComboBox(self.frame)
        self.prCombo2.setGeometry(QtCore.QRect(145, 30, 141, 30))
        self.prCombo2.setObjectName(_fromUtf8("prCombo2"))
        self.prCombo2.addItem(_fromUtf8(""))
        self.prCombo2.addItem(_fromUtf8(""))
        self.prCombo2.addItem(_fromUtf8(""))

        self.frame_2 = QtGui.QFrame(self)
        self.frame_2.setGeometry(QtCore.QRect(10, 290, 651, 131))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        #self.Time = QtGui.QLineEdit(self.frame_2)
        #self.Time.setGeometry(QtCore.QRect(180, 10, 71, 31))
        #self.Time.setObjectName(_fromUtf8("Time"))
        self.tr = QtGui.QLineEdit(self.frame_2)
        self.tr.setGeometry(QtCore.QRect(240, 30, 71, 31))
        self.tr.setObjectName(_fromUtf8("tr"))

        self.label_3 = QtGui.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 35, 231, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.multiThread = QtGui.QCheckBox(self.frame_2)
        self.multiThread.setEnabled(False)
        self.multiThread.setGeometry(QtCore.QRect(400, 5, 181, 25))
        self.multiThread.setCheckable(True)
        self.multiThread.setObjectName(_fromUtf8("multiThread"))

        self.multiThreadG = QtGui.QCheckBox(self.frame_2)
        self.multiThreadG.setEnabled(False)
        self.multiThreadG.setGeometry(QtCore.QRect(400, 35, 181, 25))
        self.multiThreadG.setCheckable(True)
        self.multiThreadG.setObjectName(_fromUtf8("multiThreadG"))

        self.multiHard = QtGui.QCheckBox(self.frame_2)
        self.multiHard.setEnabled(False)
        self.multiHard.setGeometry(QtCore.QRect(400, 65, 151, 25))
        self.multiHard.setCheckable(True)
        self.multiHard.setObjectName(_fromUtf8("multiHard"))

        self.hashCrack = QtGui.QPushButton(self.frame_2)
        self.hashCrack.setGeometry(QtCore.QRect(400, 95, 100, 28))
        self.hashCrack.setEnabled(False)
        
        self.archiveCrack = QtGui.QPushButton(self.frame_2)
        self.archiveCrack.setGeometry(QtCore.QRect(500, 95, 100, 28))
        self.archiveCrack.setEnabled(False)


        #self.TimeCheck = QtGui.QCheckBox(self.frame_2)
        #self.TimeCheck.setGeometry(QtCore.QRect(10, 12, 171, 25))
        #self.TimeCheck.setObjectName(_fromUtf8("TimeCheck"))
        self.label_6 = QtGui.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(10, 80, 141, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.Address = QtGui.QLineEdit(self.frame_2)
        self.Address.setGeometry(QtCore.QRect(140, 75, 150, 32))
        self.Address.setObjectName(_fromUtf8("Address"))
        self.setAddr = QtGui.QPushButton(self.frame_2)
        self.setAddr.setGeometry(QtCore.QRect(290, 75, 90, 28))
        self.setAddr.setObjectName(_fromUtf8("setAddr"))
        self.frame_3 = QtGui.QFrame(self)
        self.frame_3.setGeometry(QtCore.QRect(10, 30, 651, 231))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.input = QtGui.QLineEdit(self.frame_3)
        self.input.setGeometry(QtCore.QRect(140, 10, 501, 32))
        self.input.setObjectName(_fromUtf8("input"))
        self.input.setText('{setLower}->{23}+{setLower}->{12}=4')# + {setDigit}->{34} =9')
        self.label = QtGui.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(10, 15, 131, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.executText = QtGui.QTextEdit(self.frame_3)
        self.executText.setGeometry(QtCore.QRect(10, 50, 631, 171))
        self.executText.setObjectName(_fromUtf8("executText"))
        self.executText.setText(r"""setLower=r"abcdefghijklmnopqrstuvwxyz"
setUpper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
setDigit=r"0123456789"
setSym=r"!\#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ '"
setAscii=''.join([chr(i) for i in range(256)] )
setAllChars=r" !#$%&\"\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
setMyOwn="1234"
setMyOwn2="567"
""")
        self.frame_4 = QtGui.QFrame(self)
        self.frame_4.setGeometry(QtCore.QRect(10, 430, 321, 131))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.label_4 = QtGui.QLabel(self.frame_4)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(10, 15, 141, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.splitSize = QtGui.QLineEdit(self.frame_4)
        self.splitSize.setEnabled(False)
        self.splitSize.setGeometry(QtCore.QRect(155, 10, 113, 32))
        self.splitSize.setObjectName(_fromUtf8("splitSize"))
        self.genData = QtGui.QPushButton(self.frame_4)
        self.genData.setGeometry(QtCore.QRect(70, 90, 181, 28))
        self.genData.setObjectName(_fromUtf8("genData"))
        self.genData.clicked.connect(self.generateDatabase)
        self.prCombo1 = QtGui.QComboBox(self.frame_4)
        self.prCombo1.setGeometry(QtCore.QRect(110, 50, 141, 30))
        self.prCombo1.setObjectName(_fromUtf8("prCombo1"))
        self.prCombo1.addItem(_fromUtf8(""))
        self.prCombo1.addItem(_fromUtf8(""))
        self.prCombo1.addItem(_fromUtf8(""))
        self.prCombo1.addItem(_fromUtf8(""))
        self.label_2 = QtGui.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(10, 55, 91, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.futureBtn = QtGui.QPushButton(self)
        self.futureBtn.setGeometry(QtCore.QRect(170, 260, 341, 28))
        self.futureBtn.setObjectName(_fromUtf8("pushButton"))
        self.futureBtn.clicked.connect(parent.future.show)

        self.setWindowTitle('Main window')
        self.checkBox_4.setText(_translate("MainWindow", "Use quantum randombit server", None))
        self.genPass.setText(_translate("MainWindow", "Generate strong password", None))
        self.genAPass.setText(_translate("MainWindow", "A random strong password", None))
        #self.Time.setText(_translate("MainWindow", "1", None))
        self.tr.setText(_translate("MainWindow", "-35", None))
        self.label_3.setText(_translate("MainWindow", "Log_2 of each password probablity:", None))
        self.multiThread.setText(_translate("MainWindow", "Use multiThread by CPU", None))
        self.multiThreadG.setText(_translate("MainWindow", "Use multiThread by GPU", None))
        self.multiHard.setText(_translate("MainWindow", "Use multiHardDisk", None))
        self.hashCrack.setText(_translate("MainWindow", "Crack hashes", None))
        self.archiveCrack.setText(_translate("MainWindow", "Crack archives", None))
        #self.TimeCheck.setText(_translate("MainWindow", "Time to stop (hourse):", None))
        self.label_6.setText(_translate("MainWindow", "Output file Address:", None))
        self.Address.setText(_translate("MainWindow", "output.txt", None))
        self.setAddr.setText(_translate("MainWindow", "SetAddress", None))
        self.label.setText(_translate("MainWindow", "Password structure:", None))
        self.label_4.setText(_translate("MainWindow", "Split output files (GB): ", None))
        self.splitSize.setText(_translate("MainWindow", "100", None))
        self.genData.setText(_translate("MainWindow", "Generate database", None))
        self.prCombo1.setItemText(0, _translate("MainWindow", "Dual frequency", None))
        self.prCombo1.setItemText(1, _translate("MainWindow", "Mono frequency", None))
        self.prCombo1.setItemText(2, _translate("MainWindow", "Triple frequency", None))
        self.prCombo1.setItemText(3, _translate("MainWindow", "Brut force", None))
        self.label_2.setText(_translate("MainWindow", "Filter method:", None))
        self.futureBtn.setText(_translate("MainWindow", "See \"futurer\" window for disabled items", None))
        self.label_5.setText(_translate("MainWindow", "Probablity method:", None))
        self.prCombo2.setItemText(0, _translate("MainWindow", "Dual frequency", None))
        self.prCombo2.setItemText(1, _translate("MainWindow", "Mono frequency", None))
        self.prCombo2.setItemText(2, _translate("MainWindow", "Triple frequency", None))

    def initOp(self):
        def externExecutText(cmd):
            try:
                exec(cmd)
            except Exception as msg:
                sendErr(msg)

            A=locals()
            ret={}
            for ai in A:
                if ai[:3]=='set':
                    ret[ai]=A[ai]
            return ret
        def externStruct(command,Vars,L):
            locals().update(Vars)
            cmd=[]
            cmdFlag=False
            ctr=0
            for i in range(len(command)):
                if cmdFlag:
                    cmd[-1]+=command[i]

                if command[i]=='{':
                    if ctr==0:
                        cmdFlag=True
                        cmd+=['']
                    ctr+=1
                if command[i]=='}':
                    ctr-=1
                    if ctr==0:
                        cmd[-1]=cmd[-1][:-1]
                        cmdFlag=False
            
            cmd=[cmd[i:i+2]  for i in range(0,len(cmd),2)]
            chars=[[Vars[cij] for cij in ci[0].split(',')] for ci in cmd]
            tempStruct=[[int(cij)  for cij in ci[1]] for ci in cmd]
            chars=[''.join(set(''.join(si))) for si in chars]
            ret=[]
            for a in itertools.product(*tempStruct):
                if sum(a)==L:
                    r=[]
                    for i in range(len(a)):
                        r+=[chars[i]]*a[i]
                    ret+=[r]
            return ret

        Vars=externExecutText(str(self.executText.toPlainText()))

        """try:
            self.T=float(str(self.Time.text()))
            print('t=',self.T)
        except Exception as a:
            sendErr('time of password generation must be a float. if you want to generate cantinusly enter 0.\n\t'+str(a))
            return"""

        try:
            inp=str(self.input.text())
            for i in range(-1,-len(inp),-1):
                if inp[i]=='=':
                    break
            L=int(inp[i+1:].replace(' ',''))
            struct=externStruct(inp,Vars,L)
            if len(struct)==0 or struct==None:
                sendErr('Nothing to do!')
                return
        except Exception as a:
            print('inputLineEdit',a)
            sendErr('Bad syntax detected in inputed structure!')
            return

        try:
            self.treshold=2**float(str(self.tr.text()))
        except Exception as a:
            print('tr',a)
            sendErr('log_2(treashold) must be a float. (negative)')
            return
        self.passworder=password(struct)
        self.output=open(str(self.Address.text()),'w')

    def randomAPass(self):
        class dialogOutput(QMdiSubWindow):
            def __init__(self,text,parent=None):
                super(dialogOutput,self).__init__(parent)
                self.setWindowTitle('Practical strong password')
                self.setFixedSize(250,75)
                self.output=QtGui.QLineEdit(text,self)
                self.output.setGeometry(10,25,230,45)
        self.initOp()
        ret=''
        global a
        a=self.passworder
        dist=str(self.prCombo2.currentText())
        if dist=='Mono frequency':
            f=f1
        elif dist=='Dual frequency':
            f=f2
        elif dist=='Triple frequency':
            f=f3
        while ret=='' or f(ret)>self.treshold:
            st=random.sample(self.passworder.structure,1)[0]
            ret=''.join([random.sample(sti,1)[0] for sti in st])
            print(ret)
        W=dialogOutput(ret,self)
        self.parent.mdi.addSubWindow(W)
        W.show()
    def generateDatabase(self):
        self.initOp()
        global database
        database=self.passworder.initDatabase(str(self.prCombo1.currentText()),self.treshold)
        self.timer=QTimer(self)
        self.time=0
        self.counter=0
        self.timer.start(1)
        for pw in database:
            self.output.write(pw)
            self.output.write('\n')
            self.counter+=1
            if self.passworder.stoped:
                break
        self.output.close()

    def timeOutEvent(self):
        self.passworder.time+=1
        print('time :{t}, pass: {p}'.format(t=passworder.time, p=passworder.counter))
        if self.passworder.time>=self.passworder.T:
            self.passworder.setStop()
            self.timer.stop()
        self.passworder.output.flush()
            #print(passwordGenerator.active)

    def strongPassword(self):
        self.initOp()
        self.setEnabled(False)
        global f,database
        database=self.passworder.initDatabase('Brut force',self.treshold)
        self.timer=QTimer(self)
        self.time=0
        self.counter=0
        self.timer.start(1)
        dist=str(self.prCombo2.currentText())
        if dist=='Mono frequency':
            f=f1
        elif dist=='Dual frequency':
            f=f2
        elif dist=='Triple frequency':
            f=f3
        for pw in database:
            if f(pw)<self.treshold:
                self.output.write(pw)
                self.output.write('\n')
                self.counter+=1
            if self.passworder.stoped:
                break
        self.output.close()
        self.setEnabled(True)
class App(QMainWindow):
    def __init__(self,parent=None):
        super(App,self).__init__(parent)
        self.resize(700,700)
        self.mdi=QMdiArea(self)
        self.setCentralWidget(self.mdi)
        self.future=future(self)
        self.mdi.addSubWindow(self.future)

        self.generator=generator(self)
        self.generator.show()
        self.mdi.addSubWindow(self.generator)
        self.About=About(self)
        self.About.hide()
        self.mdi.addSubWindow(self.About)
        self.mdi.addSubWindow(Errors)

        exitAction = QtGui.QAction(QtGui.QIcon('generator.png'), 'generator', self)
        exitAction.setShortcut('Ctrl+M')
        exitAction.triggered.connect(self.generator.show)
        self.toolbar = self.addToolBar('main')
        self.toolbar.addAction(exitAction)

        exitAction = QtGui.QAction(QtGui.QIcon('future.png'), 'future', self)
        exitAction.setShortcut('Ctrl+F')
        exitAction.triggered.connect(self.future.show)
        self.toolbar = self.addToolBar('future')
        self.toolbar.addAction(exitAction)

        exitAction = QtGui.QAction(QtGui.QIcon('Errors.png'), 'Errors', self)
        exitAction.setShortcut('Ctrl+E')
        exitAction.triggered.connect(self.About.show)
        self.toolbar = self.addToolBar('Errors')
        self.toolbar.addAction(exitAction)

        exitAction = QtGui.QAction(QtGui.QIcon('About_us.png'), 'About', self)
        exitAction.setShortcut('Ctrl+A')
        exitAction.triggered.connect(self.About.show)
        self.toolbar = self.addToolBar('About')
        self.toolbar.addAction(exitAction)

        self.future.show()
        self.future.setFocus()

    def load(self):
        fname=[str(f) for f in QFileDialog.getOpenFileNames(self, 'Open file', '.')]
        #set_database(fname)

     #def export(self):
       #       fname=QFileDialog.getSaveFileName(self, 'Save file', '.')

    def closeEvent(self,event):
          quit_msg = "Are you sure you want to exit the program?"
          event.accept()
          return
          reply = QMessageBox.question(self, 'Message', 
                     quit_msg, QMessageBox.Yes, QMessageBox.No)
          
          if reply == QMessageBox.Yes:
               event.accept()
          else:
               event.ignore()
    

class About(QMdiSubWindow):	
    def __init__(self, title='', parent = None):
        super(About, self).__init__(parent)
        self.setFixedSize(351, 350)
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 30, 261, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Utopia"))
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(10, 260, 331, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Utopia"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 351, 171))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Utopia"))
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_3.setFont(font)

        self.okBtn = QtGui.QPushButton(self)
        self.okBtn.setGeometry(QtCore.QRect(140, 310, 90, 28))
        self.okBtn.setObjectName(_fromUtf8("OK"))

        self.label.setText(_translate("MainWindow", "ShutToPasswords v0.38", None))
        self.label_2.setText(_translate("MainWindow", "grayWolvesSecurity group", None))
        self.label_3.setText(_translate("MainWindow", "We are anonymous. If anybody claim that he\n"
" write this package, ask he to DeHash our sign.\n"
" Hash is our identity.\n\nhash1:8A61109CD86F44BD0CEA1E542CAE93622E\n8A31CA4C3DE7B17EBF6DB20656BC79\n\nhash2:F1034D07999BFCD5A9C54D68352DFD205\n49C7A6975D0A2DEE237600FFDF27C1A", None))
        self.okBtn.setText(_translate("MainWindow", "OK", None))


        self.okBtn.clicked.connect(self.hide)

class future(QMdiSubWindow):
    def __init__(self,title='',parent=None):
        super(future,self).__init__(parent)
        self.resize(455, 450)
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 40, 281, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Utopia"))
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(20, 75, 415, 330))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Utopia"))
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Shit = QtGui.QPushButton(self)
        self.Shit.setGeometry(QtCore.QRect(230, 415, 90, 28))
        self.Shit.setObjectName(_fromUtf8("pushButton"))
        self.Shit.clicked.connect(self.hide)
        self.Denote = QtGui.QPushButton(self)
        self.Denote.setGeometry(QtCore.QRect(130, 415, 90, 28))
        self.Denote.setObjectName(_fromUtf8("pushButton_2"))
        self.Denote.clicked.connect(self.denote)
        self.label.setText(_translate("MainWindow", "future", None))
        self.label_2.setText(_translate("MainWindow", '''This software is first public releas of "ShutToPasswords". In
this version I provided usefull tools for crackers which bases
on social engineering on leaked password on the net.
In next version(s) we enable all option in "ShutToPasswords".
1) MultiThreading by Cpu to import processing speed
2) MultiThreading by Gpu (Graphic card) to import processing
speed and earn the shortest time for dictionary generation.
3) Cracking hash or archive, without need to hard space
4) Split output files,
5) Use quantum true random bit generator to genarate most
strong password
***Next version(s) such this version will be free and openSource.
I will have been started the "ShutToPasswords v1" project after I get
only 4.800$ in my bitcoin address. denote me (even 1$) and
I make you most powerful cracker.

my BTC: 1FDxQdMj26H41yUVW7KyCEyTyV5yRqZFPT

''', None))
        self.bitcoin=QtGui.QLineEdit('bitcoin',self)
        self.bitcoin.setGeometry(25,385,405,25)
        self.Shit.setText(_translate("MainWindow", "Shit!", None))
        self.Denote.setText(_translate("MainWindow", "Denote", None))
    def show(self):
        super(future,self).show()
        self.setFocus()
    def denote(self):
        webbrowser.open('bitcoin:')
class Err(QMdiSubWindow):
    def __init__(self,title='',parent=None):
        super(Err,self).__init__(parent)
        self.Msg=QTextEdit(self)
        self.Msg.setGeometry(5,25,490,430)
        self.setFixedSize(500,500)
        self.index=0
        self.message=''
        self.okBtn=QPushButton('ok',self)
        self.okBtn.setGeometry(220,460,70,30)
        self.okBtn.clicked.connect(self.hide)
        global sendErr
        sendErr=self.sendErr
        self.hide()
    def sendErr(self,msg):
        self.index+=1
        self.message+=str(self.index)+' : '+str(msg)+'\n'+'-.'*40+'\n'
        self.Msg.setText(self.message)
        self.showNormal()
        self.setFocus()

    def clear(self):
        self.index=0
        self.message=''
        self.Msg.setText(self.message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Errors=Err('Errors')
    ex = App()
    ex.show()
    sys.exit(app.exec_())
#one=sympy.simplify(1)
