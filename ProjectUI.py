# to do:
# set text of currentNoteCardSS to text of note card front
# flip card --> set text of currentNoteCardSS to text of note card back
# flip card --> move to front of next card
#


from PyQt6 import QtCore, QtGui, QtWidgets

import card
import deck
from notes import Notes

class Ui_MainWindow(object):
    listofcard = [] # temp list for testing save card button
    DECKS = {}
    # used in new_document_button_clicked() method to keep track of how many new notes have been added
    NOTE_DOCUMENT_INDEX = 0
    # increments for each deck created, used by new_deck_button_clicked()
    DECK_INDEX = 0
    # shows index of which card the user is currently editing in Card Edit tab
    CURRENT_CARD_INDEX = 1
    # shows how many cards are in the current deck being edited
    CARDS_IN_DECK = 1

    def setupUi(self, MainWindow):
        defaultWindowWidth, defaultWindowHeight = 670,380
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(defaultWindowWidth, defaultWindowHeight)
        MainWindow.setMinimumSize(QtCore.QSize(int(defaultWindowWidth*0.75), int(defaultWindowHeight*0.75))) # window minimum size

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")

        self.cardEditTab = QtWidgets.QWidget()
        self.cardEditTab.setObjectName("cardEditTab")

        self.frame = QtWidgets.QFrame(parent=self.cardEditTab)
        self.frame.setGeometry(QtCore.QRect(195, 240, 170, 60))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setObjectName("frame")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backButton = QtWidgets.QPushButton(parent=self.frame)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout.addWidget(self.backButton)

        self.backButton.clicked.connect(self.back_button_clicked)

        self.deckIndex = QtWidgets.QLabel(parent=self.frame)
        self.deckIndex.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.deckIndex.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.deckIndex.setObjectName("deckIndex")
        self.horizontalLayout.addWidget(self.deckIndex)

        self.forwardButton = QtWidgets.QPushButton(parent=self.frame)
        self.forwardButton.setObjectName("forwardButton")
        self.horizontalLayout.addWidget(self.forwardButton)

        self.forwardButton.clicked.connect(self.forward_button_clicked)

        self.deckSelectCE = QtWidgets.QComboBox(parent=self.cardEditTab)
        self.deckSelectCE.setGeometry(QtCore.QRect(255, 5, 70, 25))
        self.deckSelectCE.setObjectName("deckSelectCE")
        self.deckSelectCE.addItem("")

        self.frame_2 = QtWidgets.QFrame(parent=self.cardEditTab)
        self.frame_2.setGeometry(QtCore.QRect(550, 20, 100, 250))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.newDeckCEButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.newDeckCEButton.setObjectName("newDeckCEButton")
        self.verticalLayout_2.addWidget(self.newDeckCEButton)

        self.newDeckCEButton.clicked.connect(self.new_deck_button_clicked)

        self.newCardCEButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.newCardCEButton.setObjectName("newCardCEButton")
        self.verticalLayout_2.addWidget(self.newCardCEButton)

        self.newCardCEButton.clicked.connect(self.new_card_button_clicked)

        self.deleteDeckButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.deleteDeckButton.setObjectName("deleteDeckButton")
        self.verticalLayout_2.addWidget(self.deleteDeckButton)
        # delete deck button
        self.deleteDeckButton.clicked.connect(self.delete_deck_button_clicked)

        self.deleteCardButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.deleteCardButton.setObjectName("deleteCardButton")
        self.verticalLayout_2.addWidget(self.deleteCardButton)
        # delete card button
        self.deleteCardButton.clicked.connect(self.delete_card_button_clicked)

        # save card button card edit tab
        self.saveCardButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.saveCardButton.setObjectName("saveCardButton")
        self.verticalLayout_2.addWidget(self.saveCardButton)

        self.saveCardButton.clicked.connect(self.save_card_button_clicked)

        # save deck button card edit tab
        self.saveDeckButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.saveDeckButton.setObjectName("saveDeckButton")
        self.verticalLayout_2.addWidget(self.saveDeckButton)

        self.saveDeckButton.clicked.connect(self.save_deck_button_clicked)

        self.frame_4 = QtWidgets.QFrame(parent=self.cardEditTab)
        self.frame_4.setGeometry(QtCore.QRect(15, 15, 530, 230))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")

        self.cardFrontText = QtWidgets.QTextEdit(parent=self.frame_4)
        self.cardFrontText.setGeometry(QtCore.QRect(0, 20, 250, 210))
        self.cardFrontText.setObjectName("cardFrontText")

        self.cardBackText = QtWidgets.QTextEdit(parent=self.frame_4)
        self.cardBackText.setGeometry(QtCore.QRect(280, 20, 250, 210))
        self.cardBackText.setObjectName("cardBackText")

        self.frontLabel = QtWidgets.QLabel(parent=self.frame_4)
        self.frontLabel.setGeometry(QtCore.QRect(100, 0, 50, 20))
        self.frontLabel.setObjectName("frontLabel")

        self.backLabel = QtWidgets.QLabel(parent=self.frame_4)
        self.backLabel.setGeometry(QtCore.QRect(400, 0, 50, 20))
        self.backLabel.setObjectName("backLabel")

        self.tabWidget.addTab(self.cardEditTab, "")

        self.overviewTab = QtWidgets.QWidget()
        self.overviewTab.setObjectName("overviewTab")

        self.frame_5 = QtWidgets.QFrame(parent=self.overviewTab)
        self.frame_5.setGeometry(QtCore.QRect(230, 0, 141, 41))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.currentSetLabel = QtWidgets.QLabel(parent=self.frame_5)
        self.currentSetLabel.setObjectName("currentSetLabel")
        self.horizontalLayout_2.addWidget(self.currentSetLabel)

        self.deckSelectOverview = QtWidgets.QComboBox(parent=self.frame_5)
        self.deckSelectOverview.setObjectName("deckSelectOverview")
        self.deckSelectOverview.addItem("")
        self.horizontalLayout_2.addWidget(self.deckSelectOverview)

        self.tabWidget.addTab(self.overviewTab, "")

        self.notesTab = QtWidgets.QWidget()
        self.notesTab.setObjectName("notesTab")

        self.notesText = QtWidgets.QTextEdit(parent=self.notesTab)
        self.notesText.setGeometry(QtCore.QRect(0, 0, int(defaultWindowWidth*.7), int(defaultWindowHeight*.75)))
        self.notesText.setLineWrapColumnOrWidth(0)
        self.notesText.setObjectName("notesText")

        self.frame_3 = QtWidgets.QFrame(parent=self.notesTab)
        self.frame_3.setGeometry(QtCore.QRect(510, 150, 150, 150))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.newDocumentButton = QtWidgets.QPushButton(parent=self.frame_3)
        self.newDocumentButton.setObjectName("newDocumentButton")
        self.verticalLayout_3.addWidget(self.newDocumentButton)
        # new notes document button
        self.newDocumentButton.clicked.connect(self.new_document_button_clicked)

        self.deleteNotesButton = QtWidgets.QPushButton(parent=self.frame_3)
        self.deleteNotesButton.setObjectName("deleteNotesButton")
        self.verticalLayout_3.addWidget(self.deleteNotesButton)
        # delete button for the notes tab
        self.deleteNotesButton.clicked.connect(self.delete_notes_button_clicked)

        self.saveNotesButton = QtWidgets.QPushButton(parent=self.frame_3)
        self.saveNotesButton.setObjectName("saveNotesButton")
        self.verticalLayout_3.addWidget(self.saveNotesButton)
        # save button for the notes tab
        self.saveNotesButton.clicked.connect(self.notes_save_button_clicked)

        self.notesSelect = QtWidgets.QComboBox(parent=self.notesTab)
        self.notesSelect.setGeometry(QtCore.QRect(510, 0, 120, 25))
        self.notesSelect.setObjectName("notesSelect")
        self.notesSelect.addItem("")
        self.tabWidget.addTab(self.notesTab, "")
        self.notesSelect.currentIndexChanged.connect(self.dropdown_changed)

        self.studySessionTab = QtWidgets.QWidget()
        self.studySessionTab.setObjectName("studySessionTab")

        self.currentNoteCardSS = QtWidgets.QTextEdit(parent=self.studySessionTab)
        self.currentNoteCardSS.setGeometry(QtCore.QRect(190, 40, 250, 210))
        self.currentNoteCardSS.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.NoTextInteraction)
        self.currentNoteCardSS.setObjectName("currentNoteCardSS")


        self.frame_6 = QtWidgets.QFrame(parent=self.studySessionTab)
        self.frame_6.setGeometry(QtCore.QRect(240, 0, 141, 41))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.currentSetLabel_2 = QtWidgets.QLabel(parent=self.frame_6)
        self.currentSetLabel_2.setObjectName("currentSetLabel_2")
        self.horizontalLayout_3.addWidget(self.currentSetLabel_2)

        self.deckSelectSS = QtWidgets.QComboBox(parent=self.frame_6)
        self.deckSelectSS.setObjectName("deckSelectSS")
        self.deckSelectSS.addItem("")
        self.horizontalLayout_3.addWidget(self.deckSelectSS)

        self.flipCardButton = QtWidgets.QPushButton(parent=self.studySessionTab)
        self.flipCardButton.setGeometry(QtCore.QRect(500, 200, 100, 50))
        self.flipCardButton.setObjectName("flipCardButton")

        self.flipCardButton.clicked.connect(self.testMethod)

        self.tabWidget.addTab(self.studySessionTab, "")
        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 20))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(parent=self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.secondary_window = None

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backButton.setText(_translate("MainWindow", "<--"))
        self.deckIndex.setText(_translate("MainWindow", str(self.CURRENT_CARD_INDEX)+"/"+str(self.CARDS_IN_DECK)))
        self.forwardButton.setText(_translate("MainWindow", "-->"))
        self.deckSelectCE.setItemText(0, _translate("MainWindow", "Deck_ex"))
        self.newDeckCEButton.setText(_translate("MainWindow", "+New Deck"))
        self.newCardCEButton.setText(_translate("MainWindow", "+New Card"))
        self.saveCardButton.setText(_translate("MainWindow", "Save Card"))
        self.saveDeckButton.setText(_translate("MainWindow", "Save Deck"))
        self.frontLabel.setText(_translate("MainWindow", "FRONT"))
        self.backLabel.setText(_translate("MainWindow", "BACK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cardEditTab), _translate("MainWindow", "Card Edit"))
        self.currentSetLabel.setText(_translate("MainWindow", "Current set "))
        self.deckSelectOverview.setItemText(0, _translate("MainWindow", "Deck_ex"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.overviewTab), _translate("MainWindow", "Overview"))
        self.newDocumentButton.setText(_translate("MainWindow", "+New Document"))
        self.deleteNotesButton.setText(_translate("MainWindow", "-Delete Document"))
        self.deleteDeckButton.setText(_translate("MainWindow", "-Delete Deck"))
        self.deleteCardButton.setText(_translate("MainWindow", "-Delete Card"))
        self.saveNotesButton.setText(_translate("MainWindow", "Save"))
        self.notesSelect.setCurrentText(_translate("MainWindow", "notes_example"))
        self.notesSelect.setItemText(0, _translate("MainWindow", "notes_example"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.notesTab), _translate("MainWindow", "Notes"))
        self.currentSetLabel_2.setText(_translate("MainWindow", "Current set "))
        self.deckSelectSS.setItemText(0, _translate("MainWindow", "Deck_ex"))
        self.flipCardButton.setText(_translate("MainWindow", "Flip card"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.studySessionTab), _translate("MainWindow", "Study Session"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))

    def testMethod(self):
        print("JAAAAANK!")
        print(self.DECKS)

    def dropdown_changed(self):
        print("Dropdown changed.")

    # updates the contents in the card index label in the card edit tab
    def update_index_label(self):
        self.deckIndex.setText(str(self.CURRENT_CARD_INDEX) + "/" + str(self.CARDS_IN_DECK))

    # save the contents of the notes text field (notesText)
    def notes_save_button_clicked(self):
        print(self.notesSelect.currentText())  # this shows what notes document user is currently on
        print(self.notesText.toPlainText())  # shows contents of notes document
        notes = Notes(self.notesSelect.currentText(), self.notesText.toPlainText())
        notes.store()

    def save_card_button_clicked(self):
        # creates a new Card object
        newCard = card.Card(self.cardFrontText.toPlainText(), self.cardBackText.toPlainText())
        currentDeck = self.deckSelectCE.currentText()
        if currentDeck in self.DECKS:
            self.DECKS[currentDeck].add_card(newCard)
            print("fucking added " + str(newCard) + " to " + str(currentDeck))
        else:
            print("fucking error")

        print(self.deckSelectCE.currentText()) # this shows what deck user is currently on
        print(self.cardFrontText.toPlainText()) # shows contents of front of card
        print(self.cardBackText.toPlainText()) # shows contents of back of card

    def save_deck_button_clicked(self):
        # creates a new Deck object
        newDeck = deck.Deck(str(self.deckSelectCE.currentText()))
        # create a new Deck object if it doesn't yet exist
        if newDeck not in self.DECKS:
            self.DECKS[newDeck] = deck.Deck(str(newDeck))


        print(self.deckSelectCE.currentText()) # this shows what deck user is currently on
        print(self.cardFrontText.toPlainText()) # shows contents of front of card
        print(self.cardBackText.toPlainText()) # shows contents of back of card

    #add a new item to the notes select dropdown box
    #allow user to change the name of document and switch between notes
    def new_document_button_clicked(self):
        self.NOTE_DOCUMENT_INDEX += 1 #increments by 1 for each new document added
        self.notesSelect.addItem("")
        #self.notesSelect.setItemText(self.NOTE_DOCUMENT_INDEX, str(NotesPopupWindow.TITLE_TEXT)) #sets drop down index and example title
        self.notesSelect.setItemText(self.NOTE_DOCUMENT_INDEX, "notes_"+str(self.NOTE_DOCUMENT_INDEX))

    def new_deck_button_clicked(self):
        self.DECK_INDEX += 1 #increments by 1 for each new deck added
        self.deckSelectCE.addItem("")
        self.deckSelectCE.setItemText(self.DECK_INDEX, "deck_"+str(self.DECK_INDEX)) #sets drop down index and example title

        self.deckSelectSS.addItem("")
        self.deckSelectSS.setItemText(self.DECK_INDEX, "deck_"+str(self.DECK_INDEX))

        self.deckSelectOverview.addItem("")
        self.deckSelectOverview.setItemText(self.DECK_INDEX, "deck_"+str(self.DECK_INDEX))

    # this method increments the number of cards in a deck and updates the label
    def new_card_button_clicked(self):
        self.CARDS_IN_DECK += 1
        print(self.CARDS_IN_DECK)
        # place user on the most recently added card
        if self.CURRENT_CARD_INDEX < self.CARDS_IN_DECK:
            self.CURRENT_CARD_INDEX = self.CARDS_IN_DECK
        # clear front and back text
        self.cardFrontText.clear()
        self.cardBackText.clear()
        # label update
        self.update_index_label()

    # this decrements the current card and loops around to the last card in the deeck
    def back_button_clicked(self):
        print("back")
        self.CURRENT_CARD_INDEX -= 1
        if self.CURRENT_CARD_INDEX < 1:
            self.CURRENT_CARD_INDEX = self.CARDS_IN_DECK
        #label update
        self.update_index_label()

    # this increments the current card and loops around to the first card in the deck
    # this increments the current card and loops around to the first card in the deckec
    def forward_button_clicked(self):
        print("forward")
        self.CURRENT_CARD_INDEX += 1
        if self.CURRENT_CARD_INDEX > self.CARDS_IN_DECK:
            self.CURRENT_CARD_INDEX = 1
        #label update
        self.update_index_label()

    def delete_notes_button_clicked(self):
        print("Notes deleted")
    def delete_deck_button_clicked(self):
        print("Deck deleted")
        #self.deckSelectCE.removeItem()
    def delete_card_button_clicked(self):
        print("Card deleted")
        self.CARDS_IN_DECK -= 1
        if self.CARDS_IN_DECK == 0:
            self.CARDS_IN_DECK += 1
        if self.CURRENT_CARD_INDEX > self.CARDS_IN_DECK:
            self.CURRENT_CARD_INDEX = self.CARDS_IN_DECK
        self.update_index_label()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

