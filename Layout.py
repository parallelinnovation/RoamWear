layout = """

ScreenManager:
	id: scr_mngr

	HomeScreen:
	EditorScreen:
	FinderScreen:

<HomeScreen>:
	id: screen1
	name: 'home'
	MDRectangleFlatButton:
		text: 'New'
		pos_hint: {'center_x':0.85,'center_y':0.15}
		on_release: root.manager.current = 'editor'
		on_release: app.new()
	MDRectangleFlatButton:
		text: 'Find(F)'
		pos_hint: {'center_x':0.85,'center_y':0.25}
		on_release: root.manager.current = 'finder'
		on_release: app.refresh()

<EditorScreen>:
	background_color: (0,0,0,1)
	canvas.before:
		Color:
			rgba:self.background_color
	id: screen2
	name: 'editor'
	MDRectangleFlatButton:
		text: 'home(h)'
		pos_hint: {'center_x':0.15,'center_y':0.1}
		on_release: root.manager.current = 'home'
		

	MDTextField:	
		id: title
		name:'title'
    	size_hint_x: .8
    	pos_hint: {'center_x':0.5,'center_y':0.9}
    	hint_text: "Title"
    	hint_text_color: 0,1,0,1
    	font_size: 30
    	cursor_color: 0,0,1,1
    	foreground_color: 0,1,0,1
    	normal_color: 0,0,0,1
    	color_active: 0,0,0,1
    	text: app.titlevar
	MDTextFieldRect: 
		id: content
		name:'content'
		background_color: 0,0,0,0
		foreground_color: 0,1,0,1
		size_hint: .9,.7
		pos_hint: {'center_x':0.5,'center_y':0.5}
		hint_text: "Start typing here"
    	color_mode: 'custom'
    	helper_text_mode: "on_focus"
    	line_color_focus: 1,1,0,1
    	cursor_color: 0,0,1,1
    	font_size: 30
    	text: app.contentvar

	MDRectangleFlatButton:
	    text: "Save"
    	pos_hint: {'center_x':0.85,'center_y':0.1}
	    on_release: app.save()
    MDRectangleFlatButton:
    	text: "prompt"
    	pos_hint: {'center_x':0.60,'center_y':0.1}
    	on_release: app.push()
    MDRectangleFlatButton:
    	text: "clear"
    	pos_hint: {'center_x':0.35,'center_y':0.1}
    	on_release: app.clear_screen()

<FinderScreen>:
	id: screen3
	name: 'finder'

	MDRectangleFlatButton:
		text: 'home'
		pos_hint: {'center_x':0.15,'center_y':0.1}
		on_release: root.manager.current = 'home'
	MDRectangleFlatButton:
		text: 'Find'
		pos_hint: {'center_x':0.85,'center_y':0.1}
		on_release: app.find()
		on_release: root.manager.current = 'editor'	

	MDTextField:
		id: findHere
		name:'findHere'
    	size_hint_x: .8
    	pos_hint: {'center_x':0.5,'center_y':0.9}
    	hint_text: "type to find..."
    	hint_text_color: 0,1,0,1
    	font_size: 30
    	cursor_color: 0,0,1,1
    	foreground_color: 0,1,0,1
    	normal_color: 0,0,0,1
    	color_active: 0,0,0,1

    BoxLayout:
    	size_hint: .9,.7
    	pos_hint: {'center_x':.5,'center_y':.5}


		ScrollView:	
		    MDList:
		    	id: container
		    	name:'listfield'
		    	on_touch_up:
		    		
		    		root.manager.current = 'editor'
		    		



"""