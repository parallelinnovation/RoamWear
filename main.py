from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.core.window import Window 
from kivy.clock import Clock
import sqlite3
from kivy.lang import Builder
import re
import uuid
#480x480 is the correct resolution for the Vuzix Blade
Window.size = (480,480)
#Window.clearcolor = (0, 0, 0, 0)

#Layout to display a bottom navigation menu.
KV = """ 
MDBoxLayout:
    orientation:'vertical'

    MDToolbar:
        title: 'ND App Test1.1'

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

class Example(MDApp):
    def build(self):
    	return Builder.load_string(KV)

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

def CreateNote():
	pass

def UpdateNote():
	pass

def RemoveBacklink():
	pass

def CreateID(NoteName):
	id = str(uuid.uuid1()) + "---" + str(NoteName)
	return(id)

#CreateID("Example name")

Example().run()

