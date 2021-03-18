#----------------------------------------------------- #
#----------------------RoamWear  ----------------------#
#----------------------- v0.1  ------------------------#
'''
A personal knowledge management system for the Vuzix Blade 
Running on Android Lolipop 5.1
RoamWear/main.py
Last Edited: 2021-03-18
Edited by: Adrian Papineau
 

MODULES YOU NEED INSTALLED FOR THIS TO RUN: kivymd,kivy,uuid,sqlite3,re,random. 
You also need Layout.py to be in the same folder as this file. 
'''
from kivymd.app import MDApp; from kivymd.theming import ThemeManager; from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase; from kivymd.icon_definitions import md_icons; import kivymd.color_definitions as clr
from kivy.core.window import Window; from kivy.properties import ObjectProperty, StringProperty; from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen,ScreenManager; from kivymd.uix.list import OneLineListItem,ILeftBodyTouch, OneLineIconListItem, ThreeLineListItem
from Layout import layout; from kivymd.utils import asynckivy; from kivymd.uix.refreshlayout import MDScrollViewRefreshLayout
import uuid; from kivymd.toast import toast; from kivy.animation import Animation; from kivymd.uix.list import TwoLineAvatarListItem
import sqlite3; from kivymd.uix.bottomsheet import MDCustomBottomSheet; from kivy.factory import Factory
import time; import datetime; from kivy.uix.textinput import TextInput; from textwrap import dedent; from kivy.app import App
import re
import random

Window.size = (480,480) # resolution of Vuzix Blade is 480x480. 

path = "RoamWearDatabase.db" #Change this to whatever directory you want the db to go. 
con = sqlite3.connect(path)     
c = con.cursor()

class HomeScreen(Screen): #defines the main layout objects, screens. 
	pass
class EditorScreen(Screen):
	pass
class FinderScreen(Screen):
	pass
class CustomBottomScreen(Screen):
	pass

sm = ScreenManager()
sm.add_widget(HomeScreen(name='Home'))
sm.add_widget(EditorScreen(name='Editor'))
sm.add_widget(FinderScreen(name='Finder'))
sm.add_widget(CustomBottomScreen(name='bottomscreen'))

def create_table(): #Creates the db file in the same directory as this file, does nothing if it already exists. 
    c.execute('CREATE TABLE IF NOT EXISTS RoamWearDB(datestamp TEXT, id TEXT, title TEXT, content TEXT)') 
    con.commit() #Gotta make sure to commit after every time you change the db. 

create_table()

class MainApp(MDApp):
	custom_sheet = None
	def build(self):
		self.theme_cls.primary_palette = "Green"
		self.theme_cls.accent_palette = "Teal"
		#self.theme_cls.colors = colors
		self.theme_cls.theme_style = "Dark"
		self.screen = Builder.load_string(layout)
		return self.screen
	
	titlevar = StringProperty()
	contentvar = StringProperty()
	inputvar = StringProperty()

	con = sqlite3.connect(path)     
	c = con.cursor()

	def refresh(self): #TODO figure out how to refresh the screen 
		pass 			#(more difficult with screen manager)

	def fetch_all_titles(self): #returns a list of tuples - not a list of strings. 
		c.execute('SELECT title FROM RoamWearDB ORDER BY datestamp')
		list_of_tuples =c.fetchall()
		return list_of_tuples

	def fetch_all_content(self):#also returns a list of tuples.
		c.execute('SELECT content FROM RoamWearDB ORDER BY datestamp')
		list_of_tuples =c.fetchall()
		return list_of_tuples

	def convert_list(self,xlist): #converts list(tuples) to list(strings).
		new_list = [] 
		fetchtuples = xlist	
		for i in fetchtuples:
		    if i == (None,): #DO NOT REMOVE COMMA 
		        continue
		    new_list.append(' '.join(i))
		return(new_list)

	def on_start(self): #SQLite returns a list of empty tuples, so this converts to a list. 
		new_list = [] 
		fetchtuples = self.fetch_all_titles()		
		for i in fetchtuples:
		    if i == (None,): #DO NOT REMOVE COMMA 
		        continue
		    new_list.append(' '.join(i))
		print(new_list)

		for each in new_list:
			self.screen.get_screen('finder').ids.container.add_widget(
                OneLineListItem(text=f"{each}"))
		return new_list

	def note_id(self): #called when saving or deleting to select the current note id.  
		try:
			return new_entry_id		
		except:
			title = self.screen.get_screen('editor').ids.title.text
			c.execute('SELECT id FROM RoamWearDB WHERE title = ?',(title,))
			xID = c.fetchone()
			yID = ' '.join(xID)
			return yID 

	def fetch_content(self,notenumber): # notenumber= index of which note in order by most recent.
		new_list = [] 
		fetchtuples = self.fetch_all_content()		
		for i in fetchtuples:
		    if i == (None,): #DO NOT REMOVE COMMA 
		        continue
		    new_list.append(' '.join(i))
		one_note = new_list[notenumber]
		return one_note #returns a single note content depending on how recent it is.

	def fetch_title(self,notenumber):
		new_list = [] 
		fetchtuples = self.fetch_all_titles()		
		for i in fetchtuples:
		    if i == (None,): #DO NOT REMOVE COMMA 
		        continue
		    new_list.append(' '.join(i))
		one_note = new_list[notenumber]
		return one_note #returns a single note title.

	def db_save(self,Current_title,Current_content): #Updates the database
		title = self.screen.get_screen('editor').ids.title.text
		entry_id = self.note_id()
		c.execute('''UPDATE RoamWearDB SET title = ?, content = ? WHERE id=?''',(Current_title,Current_content,entry_id))
		con.commit()

	def save(self): #'save' button in editor- not just called from button though
		try:
			title = self.screen.get_screen('editor').ids.title.text
			content = self.screen.get_screen('editor').ids.content.text
			self.db_save(title,content)
			self.LinkFinder(content)
			print("saved: "+str(self.note_id()))
			#print(title)
			#print(contentTime)						
		except:
			self.show_toast("savefailure")
		
	def LinkFinder(self,inputValue): # inputValue = content or text body which to identify links. 
		pat = r'\[\[([^]]*)\]\]' # Finds string between double brackets [[]]
		matches = re.findall(pat,inputValue) 
		print(matches) # returns a list of the titles refrenced when called. 

	def find_backlinks(self,searchstr): # searches all note content for similar strings to the argument searchstr. 
		c.execute("SELECT content FROM RoamWearDB WHERE content LIKE ?",('%'+searchstr+'%',)) 	 
		list_of_tuples =c.fetchall() 														
		new_list = [] 
		fetchtuples = list_of_tuples		
		for i in fetchtuples:
		    if i == (None,): # DO NOT REMOVE COMMA 
		        continue
		    new_list.append(' '.join(i)) # converts to list(strings).
		return new_list 

	def return_backlinks(self,number): 	# number = index of backlink in order by most recent.
		self.save()						# saves first to update the current note title, can replace with refresh() once finished. 
		title = self.fetch_title(-1)	# index at -1 returns the most recent title.
		new_list = self.find_backlinks(title) # new_list = list of all backlinks for the most recent title.
		one_note = new_list[number] 
		print(one_note)
		return one_note # returns a single specified note content string from the list of backlinks.
		
	def arr_backlink(self): # returns each* backlinked note's title and content as a newline to be read by the layout. 
		combinedx = ""
		for i in range(-1,-15,-1): # *: up to a specified amount (range determines how many backlinks to show).
			try:
				oneb = self.return_backlinks(i)
				c.execute('SELECT title FROM RoamWearDB WHERE content = ?',(oneb,)) # finds title associated with selected content string. 
				rtitle = c.fetchone()
				rtitle = ' '.join(rtitle) # converts the title from an empty tuple to a string. 
				combined = "* " + str(rtitle) + " |   " + oneb + "\n" # formats the displayed backlink string. 
				combinedx += combined
			except:
				print("no backlinks")
		return combinedx

	def clear_screen(self): # sketchy but the only way that works.
		self.titlevar = ":"
		self.contentvar = ":"
		time.sleep(.01) # inneficient method but not sure how to improve yet. 
		self.titlevar = ""
		self.contentvar = ""

	def push(self):
		pass

	def new_entry(self): # creates a blank new entry, assigns id and datestamp. 
		global new_entry_id	# probably shouldn't use a global variable here, but it works for now. 	
		Time = time.time()   
		date = str(datetime.datetime.fromtimestamp(Time).strftime('%Y-%m-%d %I:%M %p')) #Automatically ads the datestamp. May vary depending on timezone.
		new_entry_id = str(uuid.uuid1()) # generates a sring of random characters to be used as an id.
		c.execute("INSERT INTO RoamWearDB (datestamp, id) VALUES (?,?)", (date,new_entry_id))
		con.commit()
		self.clear_screen()

	def new(self): #'new' button in home screen.
		self.new_entry()
		print("new entry id: " + new_entry_id)
		self.clear_screen()


	def show_toast(self,action): #displays a toast with specified action. 
		if action == "savetoast":
			toast(("saved: " + str(self.note_id())),1)
		elif action == "deleteblanktoast":
			toast("deleted blank note",1)
		elif action == "nomatch":
			toast("no match, creating new",1)
		elif action == "deletenote":
			toast("deleted note",1)
		elif action == "savefailure":
			toast("failed to save!",1)

	def populate_UI(self,Title): #grabs all fileds with only the title
		try:
			c.execute("SELECT * FROM RoamWearDB WHERE title=?", (Title,))
			ftch = c.fetchone()
			print(ftch)
			self.titlevar = str(ftch[2])
			self.contentvar = str(ftch[3])
		except:
			print("no match")
			self.show_toast("nomatch")
			self.new_entry()
			self.titlevar = Title
			self.contentvar = ""

	def find(self): #'find' button in findern screen. 
		#print("find")
		title = self.screen.get_screen('finder').ids.findHere.text
		#print(title)
		self.populate_UI(title)

	def delete_blank(self):
		title = self.screen.get_screen('editor').ids.title.text
		content = self.screen.get_screen('editor').ids.content.text
		if len(title) == 0  and len(content) == 0:
			c.execute('''DELETE FROM RoamWearDB WHERE id =?''',(new_entry_id,))
			print('deleted: '+str(self.note_id()))
			self.show_toast("deleteblanktoast")

	def delete_note(self):
		c.execute('''DELETE FROM RoamWearDB WHERE id =?''',(self.note_id(),))
		print('deleted: '+str(self.note_id()))
		self.show_toast("deletenote")

	def show_custom_bottom_sheet(self): #displays the backlinks. 
		self.custom_sheet = MDCustomBottomSheet(screen=Factory.CustomBottomScreen())
		self.custom_sheet.open()

if __name__ == "__main__":
	MainApp().run()

