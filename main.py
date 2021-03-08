#---------------------------------------------------------------------------#
#-------------------------------- RoamWear  --------------------------------#
#--------------------------------- v0.1  -----------------------------------#

# A personal knowledge management system for the Vuzix Blade 
# Running on Android Lolipop 5.1

# RoamWear/main.py
# Last Edited: 2021-3-07 20:36
# Edited by: Adrian Papineau
# Changes: Created a basic structure. Probably will scrap once a better solution is found. 

from kivymd.app import MDApp; from kivymd.uix.screen import Screen #~~~kivymd
from kivy.core.window import Window;from kivy.clock import Clock; from kivy.lang import Builder #~~~kivy
import time; import datetime; # Time and date management.
import markdown2 as md2 # The file format for notes. 
import sqlite3 # To store the database.
import re # Regular expressions.
import uuid # Module to generate an ID tag. 

import random
#480x480 is the correct resolution for the Vuzix Blade
Window.size = (480,480)
#Window.clearcolor = (0, 0, 0, 0)

path = "RoamWearDatabase.db" #Change this to whatever directory you want the db to go. 
con = sqlite3.connect(path)     
c = con.cursor()

def create_table(): #Creates the db file in the same directory as this file, does nothing if it already exists. 
    c.execute('CREATE TABLE IF NOT EXISTS reminders(datestamp TEXT, memo TEXT, tags TEXT)') 
    con.commit() #Gotta make sure to commit after every time you change the db. 

def variable_entry(memo): 
    Time = time.time()
    date = str(datetime.datetime.fromtimestamp(Time).strftime('%Y-%m-%d %I:%M %p')) #Automatically ads the datestamp | May vary depending on timezone
    c.execute("INSERT INTO reminders (datestamp, memo) VALUES (?,?)", (date,memo))
    con.commit()

def fetch(): 
    c.execute('SELECT memo FROM reminders ORDER BY memo')
    tup =c.fetchall()
    rand_items = [tup[random.randrange(len(tup))]
              for item in range(20)]
    print(rand_items)

create_table()
variable_entry("TEST OF CREATING A NOTE [[tag]] <<linking phrase>> [[second tag]]") #Just a test. So variable_entry will go somewhere inside the editor section. 
print(fetch())

#Layout to display a bottom navigation menu.
KvMdLayout = """ 
MDBoxLayout: 
    orientation:'vertical'
    MDToolbar:
        title: 'RoamWear v0.1'
    MDBottomNavigation:   	
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'search'           
            MDLabel:
                text: 'Frame 1 content'
                halign: 'center'
        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'editor'
            MDLabel:
                text: 'Frame 2 content'
                halign: 'center'
        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'recent'
            MDLabel:
                text: 'Frame 3 content'
                halign: 'center'
"""

class RoamWearMain(MDApp): #Builds the layout that was defined in the commented section above.    
    def build(self):
    	return Builder.load_string(KvMdLayout)

class NameType(): #Returns whatever note type you want to use. notefilename is the static id tag, while notename is the variable 	
	def __init__(self,notename,notefilename):
		self.notename = notename
		self.notefilename = notefilename		
	def N_FileName():
		notefilename = str(uuid.uuid1())
		return notefilename
	def N_Name(name):
		notename = name
		return notename

#I don't know if we should include the note name in the file name, since it could change. Org-roam in Emacs does it this way. 
'''		
	def CreateID(NoteName): #CreateID("Example name")
		id = str(uuid.uuid1()) + "---" + str(NoteName)
		return(id)
'''
print("File name: " + NameType.N_FileName())
print("Note name: " + NameType.N_Name("ththth"))

#----------------Editor section--------------------#

#In the editor, this is the start of the mechanism that knows that can find links in between [[square brackets]].
# The variable 'matches' represents the outputted link. 
TextFromEditor = "[[motivation]] <is related to> [[volition]] somehow" #Just a general example.

def LinkFinder(inputValue):
	#print(inputValue)
	pat = r'\[\[([^]]*)\]\]' #Finds string between double brackets [[]]
	matches = re.findall(pat,inputValue)
	print(matches)

	# This is not really needed, but I thought I'd include it anyway so "linking phrases" could be added. 
	patz = r'\<\<([^]]*)\>\>'
	matchesz = re.findall(patz,inputValue) #Finds string between double greater than/less than symbols <<>>
	print(matchesz)

LinkFinder(TextFromEditor)

def CreateNote(NoteContent):
	variable_entry(NoteContent)

def UpdateNote():
	pass

def RemoveBacklink():
	pass

RoamWearMain().run()

