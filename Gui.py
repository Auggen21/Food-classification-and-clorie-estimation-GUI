# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import Process
import re
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(813, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(50, 10, 50, 50)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.Age = QtWidgets.QLineEdit(self.frame)
        self.Age.setObjectName("Age")
        self.horizontalLayout_2.addWidget(self.Age)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.Name = QtWidgets.QLineEdit(self.frame)
        self.Name.setObjectName("Name")
        self.horizontalLayout.addWidget(self.Name)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(16)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.Height = QtWidgets.QLineEdit(self.frame)
        self.Height.setObjectName("Height")
        self.horizontalLayout_3.addWidget(self.Height)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.Weight = QtWidgets.QLineEdit(self.frame)
        self.Weight.setObjectName("Weight")
        self.horizontalLayout_4.addWidget(self.Weight)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.comboBoxGender = QtWidgets.QComboBox(self.frame)
        self.comboBoxGender.setObjectName("comboBoxGender")
        self.comboBoxGender.addItem("")
        self.comboBoxGender.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBoxGender)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.comboBoxActivity = QtWidgets.QComboBox(self.frame)
        self.comboBoxActivity.setObjectName("comboBoxActivity")
        self.comboBoxActivity.addItem("")
        self.comboBoxActivity.addItem("")
        self.comboBoxActivity.addItem("")
        self.comboBoxActivity.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBoxActivity)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_6, 3, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.Required = QtWidgets.QLineEdit(self.frame)
        self.Required.setObjectName("Required")
        self.horizontalLayout_7.addWidget(self.Required)
        self.gridLayout.addLayout(self.horizontalLayout_7, 7, 0, 1, 2)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_19.addWidget(self.label_10)
        self.comboBoxRecent = QtWidgets.QComboBox(self.frame)
        self.comboBoxRecent.setObjectName("comboBoxRecent")
        
        self.horizontalLayout_19.addWidget(self.comboBoxRecent)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_19, 0, 0, 1, 1)
        self.checkBoxReduce = QtWidgets.QCheckBox(self.frame)
        self.checkBoxReduce.setObjectName("checkBoxReduce")
        self.gridLayout.addWidget(self.checkBoxReduce, 4, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setContentsMargins(6, -1, 6, -1)
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 1, 4, 1, 1)
        self.CalculatButton = QtWidgets.QPushButton(self.frame_3)
        self.CalculatButton.setMinimumSize(QtCore.QSize(10, 40))
        self.CalculatButton.setIconSize(QtCore.QSize(100, 100))
        self.CalculatButton.setObjectName("CalculatButton")
        self.CalculatButton.clicked.connect(self.on_click)
        
        self.gridLayout_4.addWidget(self.CalculatButton, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 6, 0, 1, 2)
        self.gridLayout_8.addWidget(self.frame, 0, 0, 1, 1)
        self.OutputTable = QtWidgets.QTableWidget(self.frame_2)
        self.OutputTable.setObjectName("OutputTable")
        self.OutputTable.setColumnCount(6)
        self.OutputTable.horizontalHeader().setStretchLastSection(1);
        self.OutputTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.OutputTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.OutputTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.OutputTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.OutputTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.OutputTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.OutputTable.setHorizontalHeaderItem(5, item)
        self.gridLayout_8.addWidget(self.OutputTable, 2, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.BrowseText = QtWidgets.QLineEdit(self.frame_2)
        self.BrowseText.setObjectName("BrowseText")
        self.horizontalLayout_8.addWidget(self.BrowseText)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)
        self.BrowseButton = QtWidgets.QPushButton(self.frame_2)
        self.BrowseButton.setObjectName("BrowseButton")
        self.BrowseButton.clicked.connect(self.getImage)
        
        self.horizontalLayout_9.addWidget(self.BrowseButton)
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_9.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_9.addWidget(self.pushButton)
        self.horizontalLayout_9.setStretch(0, 1)
        self.gridLayout_8.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)
        self.labelTotal = QtWidgets.QLabel(self.frame_2)
        self.labelTotal.setObjectName("labelTotal")
        self.gridLayout_8.addWidget(self.labelTotal, 3, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 813, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.checkDb()
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Age (Years)"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Height (cm)"))
        self.label_4.setText(_translate("MainWindow", "Weight (kg)"))
        self.label_5.setText(_translate("MainWindow", "Gender"))
        self.comboBoxGender.setItemText(0, _translate("MainWindow", "male"))
        self.comboBoxGender.setItemText(1, _translate("MainWindow", "female"))
        self.label_6.setText(_translate("MainWindow", "Activity"))
        self.comboBoxActivity.setItemText(0, _translate("MainWindow", "No Activity"))
        self.comboBoxActivity.setItemText(1, _translate("MainWindow", "High Activity"))
        self.comboBoxActivity.setItemText(2, _translate("MainWindow", "Medium Activity"))
        self.comboBoxActivity.setItemText(3, _translate("MainWindow", "Low Activity"))
        self.label_7.setText(_translate("MainWindow", "Required Calories per day"))
        self.label_10.setText(_translate("MainWindow", "Recent User"))
        self.checkBoxReduce.setText(_translate("MainWindow", "Reduce 1/2 Kg per week"))
        self.CalculatButton.setText(_translate("MainWindow", "Calculate"))
        item = self.OutputTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.OutputTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Item No"))
        item = self.OutputTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Food Name"))
        item = self.OutputTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Calorie / 100 gm "))
        item = self.OutputTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Total Calorie"))
        item = self.OutputTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Date and Time"))
        # self.OutputTable.resizeColumnsToContents()
        self.label_8.setText(_translate("MainWindow", "Add food"))
        self.BrowseButton.setText(_translate("MainWindow", "Browse"))
        self.label_9.setText(_translate("MainWindow", "Gram"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.pushButton.clicked.connect(self.ProcessImg)
        self.labelTotal.setText(_translate("MainWindow", ""))
        
        
    def on_click(self):
        
        self.name=self.Name.text()
        self.age=self.Age.text()
        self.height=self.Height.text()
        self.weight=self.Weight.text()
        self.gender=self.comboBoxGender.currentText()
        
        self.activity=self.comboBoxActivity.currentText()
        
        outputTxt=Process.func1(self.name,self.age,self.height,self.weight,self.gender,self.activity,self.checkBoxReduce.isChecked())
        self.Required.setText(outputTxt)
                
    def getImage(self):
        
        fname = QtWidgets.QFileDialog.getOpenFileName(MainWindow,  'Open file','.../images//', "Image files (*.jpg *.gif *.png)")
        self.BrowseText.setText(fname[0])
        
        
    def ProcessImg(self):
        
        data=Process.imageProcess(self.Name.text(),self.BrowseText.text(),self.lineEdit.text())
        # self.OutputTable.clear() 
        # self.OutputTable.setRowCount(0)
        self.UpdateTable2(data)   
        # self.Name.text('')
        self.comboBoxRecent.addItems([self.Name.text()])
        
        
        if self.labelTotal.text()!="":
             valu_text=self.labelTotal.text()
             valu_conv=re.findall("\d+\.\d+",valu_text)
             value=float(valu_conv[0])
             value=value+float(data[-2])
    
             
        else: value=float(data[-2])
        
        self.labelTotal.setText("Total Consumed calories per day: " +str(round(value, 2)))
             
             
        
        
    def checkDb(self):
        
        self.comboBoxRecent.clear()
        self.comboBoxRecent.addItems([""])
        names=Process.DatabaseName()
        if names!=None:
            names1=[name[0] for name in names]
            names=[]
            for name in names1:
                if name not in names:
                    names.append(name)
                
                
            self.comboBoxRecent.addItems(names)
 
            self.comboBoxRecent.currentTextChanged.connect(self.comboChange) 
            
            # else:
            
        else:
            self.comboBoxRecent.addItems(["No data"])
   
    def comboChange(self,value):
        if not self.comboBoxRecent.currentText():
            self.Name.setText('')
            self.Age.setText('')
            self.Height.setText('')
            self.Weight.setText('')
            self.comboBoxGender.setCurrentText('male')
            self.comboBoxActivity.setCurrentText('')
            self.Required.setText('')
      
        
            self.checkBoxReduce.setChecked(False) 
           
            self.OutputTable.setRowCount(0)
            self.labelTotal.setText('')

        else:    
            data =value
            # print(value)
            tableOutput=Process.checkDatabase(data)
            top=tableOutput[0]
            self.UpdateTable1(top)
            
            cal=[]
            bottom=tableOutput[1] 
            # self.OutputTable.clear() 
            self.OutputTable.setRowCount(0)
            
            for row in bottom:
                    cal.append(float(row[-2]) )           
                    self.UpdateTable2(row)
                    
            self.labelTotal.setText("Total Consumed calories per day: " +str(sum(cal)))
        
                
        
    def UpdateTable1(self,data):
        self.Name.setText(data[0][0])
        self.Age.setText(data[0][1])
        self.Height.setText(data[0][2])
        self.Weight.setText(data[0][3])
        self.comboBoxGender.setCurrentText((data[0][4]))
        self.comboBoxActivity.setCurrentText((data[0][5]))
        
        if int(data[0][6])==1:
            self.checkBoxReduce.setChecked(True) 
        else:  self.checkBoxReduce.setChecked(False)  
        
        self.on_click()
        
    def UpdateTable2(self,data):
        # print(data)
        tableOutput=data
        currentRowCount = self.OutputTable.rowCount()
        self.OutputTable.insertRow(currentRowCount)        
        self.OutputTable.setItem(currentRowCount, 0, QtWidgets.QTableWidgetItem(str(tableOutput[0])))
        self.OutputTable.setItem(currentRowCount, 1, QtWidgets.QTableWidgetItem(str(tableOutput[1])))
        self.OutputTable.setItem(currentRowCount, 2, QtWidgets.QTableWidgetItem(str(tableOutput[2])))
        self.OutputTable.setItem(currentRowCount, 3, QtWidgets.QTableWidgetItem(str(tableOutput[3])))
        self.OutputTable.setItem(currentRowCount, 4, QtWidgets.QTableWidgetItem(str(tableOutput[4])))
        self.OutputTable.setItem(currentRowCount, 5, QtWidgets.QTableWidgetItem(str(tableOutput[5])))
    

        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

