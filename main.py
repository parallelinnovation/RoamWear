from kivymd.app import MDApp; from kivymd.theming import ThemeManager; from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase; from kivymd.icon_definitions import md_icons; import kivymd.color_definitions as clr
from kivy.core.window import Window; from kivy.properties import ObjectProperty, StringProperty; from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen,ScreenManager; from kivymd.uix.list import OneLineListItem,ILeftBodyTouch, OneLineIconListItem
from Layout import layout; from kivymd.utils import asynckivy; from kivymd.uix.refreshlayout import MDScrollViewRefreshLayout
import uuid
import sqlite3
import time; import datetime
import re
import random

Window.size = (480,480)

path = "RoamWearDatabase.db" #Change this to whatever directory you want the db to go. 
con = sqlite3.connect(path)     
c = con.cursor()


#create_table()

class HomeScreen(Screen):
	pass
class EditorScreen(Screen):
	pass
class FinderScreen(Screen):
	pass

sm = ScreenManager()
sm.add_widget(HomeScreen(name='Home'))
sm.add_widget(EditorScreen(name='Editor'))
sm.add_widget(FinderScreen(name='Finder'))

def create_table(): #Creates the db file in the same directory as this file, does nothing if it already exists. 
    c.execute('CREATE TABLE IF NOT EXISTS RoamWearDB(datestamp TEXT, id TEXT, title TEXT, content TEXT)') 
    con.commit() #Gotta make sure to commit after every time you change the db. 

create_table()


class MainApp(MDApp):

	def build(self):
		self.theme_cls.primary_palette = "Green"
		self.theme_cls.accent_palette = "Teal"
		#self.theme_cls.colors = colors
		self.theme_cls.theme_style = "Dark"
		self.screen = Builder.load_string(layout)
		return self.screen

	titlevar = StringProperty("default")
	contentvar = StringProperty()

	con = sqlite3.connect(path)     
	c = con.cursor()

	def refresh(self):
		#self.screen.get_screen('finder').ids.container.refresh_done()
		pass
	def fetch_all_titles(self):
		c.execute('SELECT title FROM RoamWearDB ORDER BY title')
		list_of_tuples =c.fetchall()
		return list_of_tuples
	def on_start(self):
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
	def db_save(self,Current_title,Current_content):
		c.execute('''UPDATE RoamWearDB SET title = ?, content = ? WHERE id=?''',(Current_title,Current_content,new_entry_id))
		con.commit()

	def save(self): #'save' button in editor- not just called from button though
		try:
			title = self.screen.get_screen('editor').ids.title.text
			content = self.screen.get_screen('editor').ids.content.text
			self.db_save(title,content)
			self.LinkFinder(content)
			#print(title)
			#print(contentTime)
		except:
			print("failure to save")
		

	def LinkFinder(self,inputValue):
		pat = r'\[\[([^]]*)\]\]' #Finds string between double brackets [[]]
		matches = re.findall(pat,inputValue)
		print(matches)



	def clear_screen(self): #sketchy but the only way that works
		self.titlevar = ":"
		self.contentvar = ":"
		time.sleep(.01)
		self.titlevar = ""
		self.contentvar = ""

	def push(self):
		pass


	def new_entry(self):
		global new_entry_id		
		Time = time.time()   
		date = str(datetime.datetime.fromtimestamp(Time).strftime('%Y-%m-%d %I:%M %p')) #Automatically ads the datestamp | May vary depending on timezone
		new_entry_id = str(uuid.uuid1()) #generates a sring of random characters to be used as an id
		c.execute("INSERT INTO RoamWearDB (datestamp, id) VALUES (?,?)", (date,new_entry_id))
		con.commit()
		self.clear_screen()

	def new(self): #'new' button in home
		#print("new")
		self.new_entry()
		print(new_entry_id)
		self.clear_screen()
		#create a new entry with a new id tag
		#need a way to discard ID if editor is left when blank

	def populate_UI(self,Title): #grabs all fileds with only the title
	

		try:
			c.execute("SELECT * FROM RoamWearDB WHERE title=?", (Title,))
			ftch = c.fetchone()
			print(ftch)
			self.titlevar = str(ftch[2])
			self.contentvar = str(ftch[3])
 
		except:
			print("no match")
			self.new_entry()
			self.titlevar = Title
			self.contentvar = ""

	#titlevar = ""
	#contentvar = ""oo

	def find(self): #'find' button in finder
		#print("find")
		title = self.screen.get_screen('finder').ids.findHere.text
		#print(title)
		self.populate_UI(title)



MainApp().run()

