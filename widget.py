# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QMessageBox
from PySide6.QtCore import Slot, Qt
from PySide6.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PySide6.QtGui import QStandardItemModel, QStandardItem, QColorConstants

import x12
import csv

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    filetype = ""
    lista = []
    maxcol = []
    whereClause = []
    where = []
    files = []
    model = QStandardItemModel()

    colors = [QColorConstants.Yellow, QColorConstants.Green, QColorConstants.Blue, QColorConstants.Gray, QColorConstants.Cyan, QColorConstants.Magenta, QColorConstants.White]

    colorIndex = 0
    colorIndex2 = 0

    database = QSqlDatabase.addDatabase("QODBC")

    def openDatabase(self):
        connectString = "odbcexpress"
        self.database.setDatabaseName(connectString)
        self.database.open()

    def closeDatabase(self):
        self.database.close()

    @Slot()
    def insertData(self):
        c = 0
        for h in self.files:
#            if h[-2:] == 'x12':
#                queryMemberName = QSqlQuery()
#                querySubscriberIdentifier =QSqlQuery()

#                memberKey = 1

#                queryMemberName.prepare("""INSERT INTO MEMBERNAME(MEMBERNAMEKEY, ENTITYIDENTIFIERCODE, ENTITYTYPEQUALIFIER, NAMELAST,
#                                 NAMEFIRST, NAMEMIDDLE, NAMEPREFIX, NAMESUFFIX, IDENTIFICATIONCODEQUALIFIER, IDENTIFICATIONCODE)
#                                 VALUES(:memberNameKey, :entityIdentifierCode, :entityTypeQualifier, :nameLast, :nameFirst,
#                                 :nameMiddle, :namePrefix, :nameSuffix, :identificationCodeQualifier, :identificationCode)""")

#                querySubscriberIdentifier.prepare("""INSERT INTO SUBSCRIBERIDENTIFIER(SUBSCRIBERIDENTIFIERKEY,
#                                                     REFERENCEIDENTIFICATIONQUALIFIER, REFERENCEIDENTIFICATION)
#                                                     VALUES(:subscriberIdentifierKey, :referenceIdentificationQualifier, :referenceIdentification)""")

#                for i in self.lista:
#                    if i[0] == 'SubscriberIdentifier':
#                        querySubscriberIdentifier.bindValue(":subscriberIdentifierKey", memberKey)
#                        querySubscriberIdentifier.bindValue(":referenceIdentificationQualifier", i[1])
#                        querySubscriberIdentifier.bindValue(":referenceIdentification", i[2])

#                        querySubscriberIdentifier.exec()

#                    if i[0] == 'MemberName':
#                        queryMemberName.bindValue(":memberNameKey", memberKey)
#                        queryMemberName.bindValue(":entityIdentifierCode", i[1])
#                        queryMemberName.bindValue(":entityTypeQualifier", i[2])
#                        queryMemberName.bindValue(":nameLast", i[3])
#                        queryMemberName.bindValue(":nameFirst", i[4])
#                        queryMemberName.bindValue(":nameMiddle", i[5])
#                        queryMemberName.bindValue(":namePrefix", i[6])
#                        queryMemberName.bindValue(":nameSuffix", i[7])
#                        queryMemberName.bindValue(":identificationCodeQualifier", i[8])
#                        queryMemberName.bindValue(":identificationCode", i[9])

#                        queryMemberName.exec()

#                        memberKey+=1
#            elif h[-2:] == 'sv':
            if True:
                l = h.rfind('/') + 1 # + 1 to remove the / from the filename
                s = h[l:] # get just the filename
                s = s.replace('.', '_') # replace . in filename for _

                counter = 0
                columns = ' nvarchar(max)'
                columnas = []
                queryCreate = QSqlQuery()
                queryInsert = QSqlQuery()
                insertString = ""
                insertHeader = ""
                queryString = 'create table ' + s + ' ('

                for j in self.lista[c][0]:
                    queryString += j
                    queryString += columns
                    columnas.append(j)
                    queryString += ','

                queryString = queryString[0:-1]

                queryString += ')'
                queryCreate.prepare(queryString)
                queryCreate.exec()

                insertHeader = 'INSERT INTO ' + s + '('

                for i in columnas:
                    insertHeader += i
                    insertHeader += ','

                insertHeader = insertHeader[0:-1]
                insertHeader += ')VALUES('

                for i in self.lista[c]:
                    if counter == 0:
                        counter = 1
                        continue
                    for j in i:
                        insertString += "'"
                        insertString += j.strip()
                        insertString += "'"
                        insertString += ','
                    insertString = insertString[0:-1]
                    insertString += ')'
                    queryInsert.prepare(insertHeader + insertString)
                    queryInsert.exec()
                    insertString = ''

                c+=1

#       model = QStandardItemModel()
#       model.setColumnCount(1)

        c = 0
        self.model.setHeaderData(0, Qt.Horizontal, 'File')
        self.model.setHeaderData(1, Qt.Horizontal, 'Column')

        for q in self.files:
            l = q.rfind('/') + 1 # + 1 to remove the / from the filename
            s = q[l:] # get just the filename
            s = s.replace('.', '_') # replace . in filename for _
            r = QStandardItem(s)
            self.model.appendRow(r)

            for i in self.lista[c][0]:
                col = QStandardItem('')
                row = QStandardItem(i)
                listita = []
                listita.append(col)
                listita.append(row)
                self.model.appendRow(listita)

            c+=1

        self.ui.treeView.setModel(self.model)
        self.ui.treeView.show()

        #widget.buildWhereClause()

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Database loading process")
        dlg.setText("Database successfully loaded")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.exec()

    @Slot()
    def runQuery(self):
        if self.ui.tabWidget.currentIndex() == 0:
            model = QSqlQueryModel()
            model.setQuery(self.ui.sqlTextEdit.toPlainText())

            self.ui.tableView.setModel(model)

            self.ui.tableView.show()
        elif self.ui.tabWidget.currentIndex() == 1:
            columnas = self.ui.treeView.selectedIndexes()

            cadena = "SELECT "

            lens = []
            columns = []

            oldCount = 0
            anotherCount = 1

            for q in self.lista:
                lens.append(len(q[0])+oldCount+anotherCount) # length of file headers
                oldCount += len(q[0])
                anotherCount += 1

            tablas = set()

            for i in range(len(columnas)):
                col = columnas[i].column()
                ren = columnas[i].row()
                if col == 1:
                    if (self.model.item(ren, col) != None):
                        for index, w in enumerate(lens, start=0):
                            if ren < w:
                                table = index
                                break

                        l = self.files[table].rfind('/') + 1 # + 1 to remove the / from the filename
                        s = self.files[table][l:] # get just the filename
                        s = s.replace('.', '_') # replace . in filename for _
                        tablas.add(s)
                        columns.append(s + '.' + self.model.item(ren,col).text().strip())

            for i in columns:
                cadena += i
                cadena += ','

            cadena = cadena [:-1]

            cadena += ' FROM '

            for u in tablas:
                cadena += u
                cadena += ','

            cadena = cadena[:-1]

            if (self.where != None and self.where != []):
                cadena += ' WHERE '
                for w in self.where:
                    cadena += w
                    cadena += ' AND '

            cadena = cadena[:-5]

            if self.ui.whereTextEdit.toPlainText() != '':
                cadena += ' AND ' + self.ui.whereTextEdit.toPlainText()

            model = QSqlQueryModel()
            model.setQuery(cadena)

            self.ui.tableView.setModel(model)

            self.ui.tableView.show()

    @Slot()
    def buildWhereClause(self):
        tablas = []

        for i in range(len(self.files)):
            l = self.files[i].rfind('/') + 1 # + 1 to remove the / from the filename
            s = self.files[i][l:] # get just the filename
            s = s.replace('.', '_') # replace . in filename for _
            tablas.append(s)

        cadena = ''

        if self.whereClause[0] == None:
            return ''

        lista= ['']*len(self.whereClause[0])

        outter = 0
        counter = 0
        light = True # =

        tabla = 0

        for i in self.whereClause:
            if i == None:
                return ''
            for j in i:
                if light == True:
                    if counter == 0:
                        lista[outter] += tablas[tabla] + '.' + j + ' = '
                    else:
                        lista[outter] += tablas[tabla] + '.' + j
                    light = False
                else:
                     lista[outter] += tablas[tabla] + '.' + j + ' AND '
                     light = True

                light = True

                if counter > 0:
                    lista[outter] += ' AND '
                    if light == True:
                        lista[outter] += tablas[tabla] + '.' + j + ' = '
                        light = False
                    else:
                        lista[outter] += tablas[tabla] + '.' + j + ' AND '
                        light = True

                light = True
                outter += 1
            counter += 1
            outter = 0
            tabla += 1

        self.where = []

        for i in lista:
            x = i.rfind(' AND ')
            #cadena += i[0:x] + '\n'
            self.where.append(cadena + i[0:x])

        dlg = QMessageBox(self)
        dlg.setWindowTitle("Join columns")
        dlg.setText("Columns successfully joined")
        dlg.setStandardButtons(QMessageBox.Ok)
        dlg.exec()

    def __del__(self, parent=None):
        tablas = []

        for i in range(len(self.files)):
            l = self.files[i].rfind('/') + 1 # + 1 to remove the / from the filename
            s = self.files[i][l:] # get just the filename
            s = s.replace('.', '_') # replace . in filename for _
            tablas.append(s)

        for i in tablas:
            query = QSqlQuery()
            query.exec('drop table ' + i);

        self.closeDatabase()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.model.setColumnCount(2)
        self.ui.tabWidget.setTabText(0, "SQL")
        self.ui.tabWidget.setTabText(1, "Tree")
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.pushButton_2.clicked.connect(self.insertData)
        self.ui.pushButton.clicked.connect(self.runQuery)
        self.ui.pushButton_3.clicked.connect(self.buildWhereClause)
        self.openDatabase()

    def populateComboBoxes(self):
        if len(filenames) == 1:
            l = filenames[0].rfind('/') + 1 # + 1 to remove the / from the filename
            self.ui.comboBox.addItem(filenames[0][l:])
        else:
            for k in range(len(filenames)):
                l = filenames[k].rfind('/') + 1 # + 1 to remove the / from the filename

                self.ui.comboBox.addItem(filenames[k][l:])
                self.ui.comboBox_2.addItem(filenames[k][l:])

        if len(filenames) > 1:
            self.ui.comboBox_2.setCurrentIndex(1)

        self.ui.comboBox.activated.connect(self.activated)
        self.ui.comboBox.currentTextChanged.connect(self.text_changed)
        self.ui.comboBox.currentIndexChanged.connect(self.index_changed)

        self.ui.comboBox_2.activated.connect(self.activated_2)
        self.ui.comboBox_2.currentTextChanged.connect(self.text_changed_2)
        self.ui.comboBox_2.currentIndexChanged.connect(self.index_changed_2)


    def populateLists(self):
        self.ui.listWidget.addItems(self.lista[0][0])

        if len(self.lista) > 1:
            self.ui.listWidget_2.addItems(self.lista[1][0])

        self.ui.listWidget.itemSelectionChanged.connect(self.listChanged)
        self.ui.listWidget_2.itemSelectionChanged.connect(self.listChanged_2)
        self.ui.listWidget.itemClicked.connect(self.listClicked)
        self.ui.listWidget_2.itemClicked.connect(self.listClicked2)

    @Slot()
    def listClicked(self, item):
        brush = item.background()
        color = brush.color()

        if (color.name() == '#000000' or color.name() == '#ffffff'):

            if self.colorIndex == len(self.colors)-2 or self.colorIndex == len(self.colors)-1:
                self.colorIndex = 0
            else:
                self.colorIndex += 1

            item.setBackground(self.colors[self.colorIndex])

        else:
            item.setBackground(self.colors[len(self.colors)-1])

    @Slot()
    def listClicked2(self, item):
        brush = item.background()
        color = brush.color()

        if (color.name() == '#000000' or color.name() == '#ffffff'):

            if self.colorIndex2 == len(self.colors)-2 or self.colorIndex2 == len(self.colors)-1:
                self.colorIndex2 = 0
            else:
                self.colorIndex2 += 1

            item.setBackground(self.colors[self.colorIndex2])

        else:
            item.setBackground(self.colors[len(self.colors)-1])

    @Slot()
    def listChanged(self):
        items = self.ui.listWidget.selectedItems()
        x = []
        for i in range(len(items)):
            x.append(str(self.ui.listWidget.selectedItems()[i].text().strip()))

        self.whereClause[self.ui.comboBox.currentIndex()] = x

#        if len(items) == 1:
#            items[0].setBackground(QColor(255, 255, 0))
#        elif len(items) == 2:
#            items[0].setBackground(QColor(255, 255, 0))
#            items[1].setBackground(QColor(255, 0, 255))
#        elif len(items) == 3:
#            items[0].setBackground(QColor(255, 255, 0))
#            items[1].setBackground(QColor(255, 0, 255))
#            items[2].setBackground(QColor(0, 255, 255))

    @Slot()
    def listChanged_2(self):
        items = self.ui.listWidget_2.selectedItems()

        #items[0].setBackground(QColor("red"))
        #items[0].setBackground(QColor(255, 255, 0))

        x = []
        for i in range(len(items)):
            x.append(str(self.ui.listWidget_2.selectedItems()[i].text().strip()))

        self.whereClause[self.ui.comboBox_2.currentIndex()] = x

#        if len(items) == 1:
#            items[0].setBackground(QColor(255, 255, 0))
#        elif len(items) == 2:
#            items[0].setBackground(QColor(255, 255, 0))
#            items[1].setBackground(QColor(255, 0, 255))
#        elif len(items) == 3:
#            items[0].setBackground(QColor(255, 255, 0))
#            items[1].setBackground(QColor(255, 0, 255))
#            items[2].setBackground(QColor(0, 255, 255))

    @Slot()
    def activated(self, index):
        pass

    @Slot()
    def text_changed(self, s):
        pass

    @Slot()
    def index_changed(self, index):
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(self.lista[index][0])
        self.colorIndex = 0


    @Slot()
    def activated_2(Self, index):
        pass

    @Slot()
    def text_changed_2(self, s):
        pass

    @Slot()
    def index_changed_2(self, index):
        self.ui.listWidget_2.clear()
        self.ui.listWidget_2.addItems(self.lista[index][0])
        self.colorIndex2 = 0

#    def populateTable(self, list, maxcol):
#        #Row count
#        self.ui.tableWidget_2.setRowCount(len(list))

#        #Column count
#        self.ui.tableWidget_2.setColumnCount(maxcol)

#        k = 0

#        for i in list:
#            l = 0
#            for j in i:
#                self.ui.tableWidget_2.setItem(k, l, QTableWidgetItem(j))
#                l+=1
#            k+=1

#        self.ui.tableWidget_2.resizeColumnsToContents()

    def fileDialog(self):
        dialog = QFileDialog(self)
        #dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFileMode(QFileDialog.ExistingFiles) # this method lets us select more than one file
        dialog.setDirectory("C:\\Users\erix\OneDrive\Masters")
        dialog.setNameFilter("Files (*.gz *.csv)")
        dialog.setViewMode(QFileDialog.List)
        if dialog.exec():
            fileNames = dialog.selectedFiles()
        return fileNames

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

    def dbLoaded(self):
        self.setWindowTitle("Data loading process")
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Database successfully loaded")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    filenames = widget.fileDialog()

    widget.files = filenames

    for i in filenames:
        if i[-2:] == 'gz':
            widget.filetype = 'x12'
            #widget.lista, maxcol = x12.func(i)
            listaTemp, maxcolTemp = x12.func(i)
            widget.lista.append(listaTemp)
            widget.maxcol.append(maxcolTemp)
        elif i[-2:] == 'sv':
            widget.filetype = 'csv'
            #widget.lista, maxcol = csv.func(i)
            listaTemp, maxcolTemp = csv.func(i)
            widget.lista.append(listaTemp)
            widget.maxcol.append(maxcolTemp)

    #widget.populateTable(widget.lista, maxcol)
    widget.populateComboBoxes()
    widget.populateLists()
    widget.whereClause = [None] * len(filenames)

    app.exec()
    del widget
    sys.exit()

