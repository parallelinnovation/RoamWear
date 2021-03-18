layout = """

ScreenManager:
	id: scr_mngr

	HomeScreen:
	EditorScreen:
	FinderScreen:
	CustomBottomScreen:

<HomeScreen>:
	id: screen1
	name: 'home'
	MDFloatingActionButton:
    	icon: "plus-thick"
    	md_bg_color: app.theme_cls.primary_color
    	pos_hint: {'center_x':.9,'center_y':.1}
    	on_release: root.manager.current = 'editor'
		on_release: app.new()
	MDIconButton:
		icon: "file-find-outline"
		pos_hint: {'center_x':0.7,'center_y':0.1}
		on_release: root.manager.current = 'finder'
		on_release: app.refresh()
	MDBoxLayout:
		id: box
		name: 'Box'
		spacing: "20dp"
		adaptive_height: True
		size_hint: .9,.7
    	pos_hint: {'center_x':.5,'center_y':.8}
		MDCard:
			size_hint: None, None
			md_bg_color: (1,1,0,.1)
			padding: "10dp"
			size: "210dp", "160dp"
			pos_hint: {"center_x": .5, "center_y": .5}
			MDLabel:
				#text: app.fetch_content(-1)
				color: (1,1,1,1)
			MDIconButton:
    			icon: "open-in-new"
    			on_release: app.populate_UI(app.fetch_title(-1))
    			on_release: root.manager.current = 'editor'
		MDCard:
			size_hint: None, None
			md_bg_color: (0,1,1,.1)
			padding: "10dp"
			size: "210dp", "160dp"
			pos_hint: {"center_x": 0.5, "center_y": .5}
			MDLabel:
				#text: app.fetch_content(-2)	
				color: (1,1,1,1)
			MDIconButton:
    			icon: "open-in-new"
    			on_release: app.populate_UI(app.fetch_title(-2))
    			on_release: root.manager.current = 'editor'
	MDBoxLayout:
		id: box2
		name: 'Box2'
		spacing: "20dp"
		adaptive_height: True
		size_hint: .9,.7
    	pos_hint: {'center_x':.5,'center_y':.43}
		MDCard:
			size_hint: None, None
			md_bg_color: (0,1,0,.1)
			padding: "10dp"
			size: "210dp", "160dp"
			pos_hint: {"center_x": .5, "center_y": .5}
			MDLabel:
				#text: app.fetch_content(-3)
				color: (1,1,1,1)
			MDIconButton:
    			icon: "open-in-new"
    			on_release: app.populate_UI(app.fetch_title(-3))
    			on_release: root.manager.current = 'editor'
		MDCard:
			size_hint: None, None
			md_bg_color: (1,0,1,.1)
			padding: "10dp"
			size: "210dp", "160dp"
			pos_hint: {"center_x": 0.5, "center_y": .5}
			MDLabel:
				#text: app.fetch_content(-4)	
				color: (1,1,1,1)
			MDIconButton:
    			icon: "open-in-new"
    			on_release: app.populate_UI(app.fetch_title(-4))
    			on_release: root.manager.current = 'editor'    
<EditorScreen>:
	background_color: (0,0,0,1)
	canvas.before:
		Color:
			rgba:self.background_color
	id: screen2
	name: 'editor'
	MDIconButton:
		icon: "home"
		pos_hint: {'center_x':0.15,'center_y':0.1}
		on_release: root.manager.current = 'home'
		on_release: app.delete_blank()
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

    #MyTextInput:
		#id: xinput
		#name: 'MyTextInput'
		#readonly: False
		#multiline: False	
		#size_hint: .9,.7
		#pos_hint: {'center_x':0.5,'center_y':0.5}

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
    	cursor_color: 1,0,1,1
    	font_size: 30
    	text: app.contentvar
	MDIconButton:
    	icon: "delete"
    	pos_hint: {'center_x':0.95,'center_y':0.92}
    	on_release: app.new()
    	on_release: app.delete_note()

	MDIconButton:
		icon: "content-save"
    	pos_hint: {'center_x':0.85,'center_y':0.1}
	    on_release: app.save()
	    on_release: app.show_toast("savetoast")
    MDIconButton:
    	icon: "view-agenda-outline"
    	pos_hint: {'center_x':0.60,'center_y':0.1}
    	on_release: app.show_custom_bottom_sheet()
    MDIconButton:
    	icon: "delete-empty-outline"
    	pos_hint: {'center_x':0.35,'center_y':0.1}
    	on_release: app.clear_screen()

<CustomBottomScreen>:
	id: screen25
	name: 'bottomscreen'
    orientation: "vertical"
    size_hint_y: None
    height: "400dp"

    MDLabel:
    	text: "Backlinks"
    	pos_hint: {'center_x':0.5,'center_y':.9}
    	font_size: 15
    	color: 1,1,0,1
    ScrollView:
    	pos_hint: {'center_x':0.5,'center_y':.3}
        MDGridLayout:
            cols: 1
            adaptive_height: True
			MDLabel:
			    color: 0,1,0,1
				text: app.arr_backlink()
				font_size: 20
		
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

		    		



"""