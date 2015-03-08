# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.
##############################################################################
# CUSTOM SOUND CHANNEL
# This is the block where we declare the individual sound channels. This enables us to play several sound FX's without overlapping
init python:
    renpy.music.register_channel("test_one", "sfx", False)
    renpy.music.register_channel("test_two", "sfx", False)
    renpy.music.register_channel("test_three", "sfx", False)
    renpy.music.register_channel("test_four", "sfx", False)
    renpy.music.register_channel("test_five", "sfx", False)
    renpy.music.register_channel("test_six", "sfx", False)

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

    # Decide if we want to use the one-window or two-window varaint.
    if not two_window:

        # The one window variant.        
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:            
                window:
                    style "say_who_window"

                    text who:
                        id "who"
                        
            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"
              
    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window: 
        style "menu_window"        
        xalign 0.5
        yalign 0.5
        
        vbox:
            style "menu"
            spacing 2
            
            for caption, action, chosen in items:
                
                if action:  
                    
                    button:
                        action action
                        style "menu_choice_button"                        

                        text caption style "menu_choice"
                    
                else:
                    text caption style "menu_caption"

init -2 python:
    config.narrator_menu = True
    
    style.menu_window.set_parent(style.default)
    style.menu_choice.set_parent(style.button_text)
    style.menu_choice.clear()
    style.menu_choice.line_leading = 5
    style.menu_choice.line_spacing = 2
    style.menu_choice.hover_color = "#ffffff"
    style.menu_choice_button.set_parent(style.button)
    style.menu_choice_button.xminimum = int(config.screen_width * 0.75)
    style.menu_choice_button.xmaximum = int(config.screen_width * 0.75)
    style.menu_choice_button.background = Frame("gui/choice_idle.png",3, 3)
    style.menu_choice_button.hover_background = Frame("gui/choice_hover.png", 3, 3)
    

##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu
        
##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0
    
    use quick_menu
        
##############################################################################
# Main Menu 
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu
screen main_menu:
    tag menu # This ensures that any other menu screen is replaced.
    add "gui/start/screen_ground.png" # Add a background image for the main menu.

    $ y=47 # To make things easier, we define a variable y and use it to set positions for our imagebuttons
    imagebutton auto "gui/start/start_%s.png" xpos 480 ypos y focus_mask True action Start() hovered [ Play ("test_one", "sfx/click.wav") ] at main_eff1
    # Imagebutton documentation: http://www.renpy.org/doc/html/screens.html#imagebutton
    
    # auto - is used to automatically define the images used by this button. We could also use:
    # imagebutton idle "main_start_idle.png" hover "main_start_hover.png"
    
    # xpos 773 ypos y - are used set the coordinates to position the button at 773, 114 (y has a value of 114)
    
    # focus_mask True ensures that only non-transparent areas of the button can be focused. focus_mask defines which parts of the image can be focused, and hence clicked on. http://www.renpy.org/doc/html/style.html#button-style-properties
    
    # action - action to run when the button is activated. This also controls if the button is sensitive, and if the button is selected.
    
    # hovered - action to run when the button gains focus. Square brackets are used to run multiple actions. In this case we play a sound effect and show a tooltip.
    
    # unhovered - action to run when the button loses focus. In this case we hide a tooltip.
    
    $ y+=126
    imagebutton auto "gui/start/load_%s.png" xpos 480 ypos y focus_mask True  action ShowMenu('load') hovered [ Play ("test_two", "sfx/click.wav") ]  at main_eff2
    $ y+=126
    imagebutton auto "gui/start/options_%s.png" xpos 480 ypos y focus_mask True action ShowMenu('preferences') hovered [ Play ("test_three", "sfx/click.wav") ] at main_eff3
    $ y+=126
#    if persistent.extra_unlocked: # We only show the extras, if they have been unlocked. Because we are using a variable (y) for ypos, we don't need to worry about positioning the rest of the button(s).
#        imagebutton auto "gui/start_extras_%s.png" xpos 480 ypos y focus_mask True action Start('extras') hovered [ Play ("test_four", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_extra.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")] at main_eff4
#        $ y+=71
    imagebutton auto "gui/start/quit_%s.png" xpos 480 ypos y focus_mask True action Quit(confirm=False) hovered [ Play ("test_five", "sfx/click.wav") ] at main_eff5

# The code below defines the ATL transform effects for each button on the main menu. These effects are triggered when the buttons are shown.
# ATL transform properties: http://www.renpy.org/wiki/renpy/doc/reference/Animation_and_Transformation_Language#Transform_Properties
#begin main_eff
init -2:
    transform main_eff1:
        zoom 0.5
        easein 0.3 zoom 1.0
        on hover:
            easein 0.15 zoom 1.05
            easein 0.15 zoom 0.95
            easein 0.1 zoom 1.0
        on idle:
            easein 0.3 zoom 1.0
    transform main_eff2:
        zoom 0.5
        easein 0.6 zoom 1.0
        on hover:
            easein 0.15 zoom 1.05
            easein 0.15 zoom 0.95
            easein 0.1 zoom 1.0
        on idle:
            easein 0.3 zoom 1.0
    transform main_eff3:
        zoom 0.5
        easein 0.9 zoom 1.0
        on hover:
            easein 0.15 zoom 1.05
            easein 0.15 zoom 0.95
            easein 0.1 zoom 1.0
        on idle:
            easein 0.3 zoom 1.0
    transform main_eff4:
        zoom 0.5
        easein 1.2 zoom 1.0
        on hover:
            easein 0.15 zoom 1.05
            easein 0.15 zoom 0.95
            easein 0.1 zoom 1.0
        on idle:
            easein 0.3 zoom 1.0
    transform main_eff5:
        zoom 0.5
        easein 1.5 zoom 1.0
        on hover:
            easein 0.15 zoom 1.05
            easein 0.15 zoom 0.95
            easein 0.1 zoom 1.0
        on idle:
            easein 0.3 zoom 1.0
    
#end main_eff


##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation_options:
    imagebutton auto "gui/nav/main_%s.png" xpos 617 ypos 21 focus_mask True action MainMenu() hovered [ Play ("test_one", "sfx/click.wav") ] at nav_eff
    imagebutton auto "gui/nav/options_%s.png" xpos 617 ypos 85 focus_mask True action ShowMenu('preferences') hovered [ Play ("test_two", "sfx/click.wav") ] at nav_eff
    imagebutton auto "gui/nav/save_%s.png" xpos 617 ypos 149 focus_mask True action ShowMenu('save') hovered [ Play ("test_two", "sfx/click.wav") ] at nav_eff
    imagebutton auto "gui/nav/load_%s.png" xpos 617 ypos 213 focus_mask True action ShowMenu('load') hovered [ Play ("test_three", "sfx/click.wav") ] at nav_eff
    imagebutton auto "gui/nav/return_%s.png" xpos 617 ypos 277 focus_mask True action Return() hovered [ Play ("test_four", "sfx/click.wav") ] at nav_eff
    imagebutton auto "gui/nav/quit_%s.png" xpos 617 ypos 341 focus_mask True action Quit() hovered [ Play ("test_five", "sfx/click.wav") ] at nav_eff
# The code below defines the ATL transform effects for the buttons on the game menu. These effects are triggered when we hover the mouse over them (hover and selected_hover).
# Effects that are triggered by idle and selected_idle events (when we stop hovering the mouse over them) ensure that the buttons are moved back to the initial state.
init -2:
    transform nav_eff:
        on idle:
            easein 0.3 xpos 617
        on selected_idle:
            easein 0.3 xpos 647
        on hover:
            easein 0.2 xpos 637
            easein 0.25 xpos 587
        on selected_hover:
            easein 0.2 xpos 647

screen navigation:

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98
        
        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2 python:
    style.gm_nav_button.size_group = "gm_nav"
    
##############################################################################
# Save Load Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation_saveload:
    imagebutton auto "gui/saveload/main_%s.png" xpos 617 ypos 21 focus_mask True action MainMenu() hovered [ Play ("test_one", "sfx/click.wav") ] at nav_eff
    imagebutton auto "gui/saveload/options_%s.png" xpos 617 ypos 85 focus_mask True action ShowMenu('preferences') hovered [ Play ("test_two", "sfx/click.wav") ] at nav_eff
    imagebutton auto "gui/saveload/save_%s.png" xpos 617 ypos 149 focus_mask True action ShowMenu('save') hovered [ Play ("test_two", "sfx/click.wav") ] at nav_eff
    imagebutton auto "gui/saveload/load_%s.png" xpos 617 ypos 213 focus_mask True action ShowMenu('load') hovered [ Play ("test_three", "sfx/click.wav") ] at nav_eff
    imagebutton auto "gui/saveload/return_%s.png" xpos 617 ypos 277 focus_mask True action Return() hovered [ Play ("test_four", "sfx/click.wav") ] at nav_eff
    imagebutton auto "gui/saveload/quit_%s.png" xpos 617 ypos 341 focus_mask True action Quit() hovered [ Play ("test_five", "sfx/click.wav") ] at nav_eff

##############################################################################
# Save, Load Slot
#
init -2 python: #we initialize x and y, so the load_save_slot screen below works at startup
    x=0
    y=0
screen load_save_slot:
    $ file_text = "% s\n  %s" % (FileTime(number, empty="Empty Slot."), FileSaveName(number))
    $x1=x+20
    $y1=y+50
    add FileScreenshot(number) xpos x1 ypos y1
    $x2=x+20
    $y2=y+20
    text file_text xpos x2 ypos y2 size 20 color "#cc00ff"

##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.
    
screen file_picker:
    use navigation_saveload # We include the navigation/game menu screen
    # Buttons for selecting the save/load page:
    imagebutton auto "gui/saveload/page1_%s.png" xpos 27 ypos 21 focus_mask True action FilePage(1) hover_sound "sfx/click.wav"
    imagebutton auto "gui/saveload/page2_%s.png" xpos 116 ypos 21 focus_mask True action FilePage(2) hover_sound "sfx/click.wav"
    imagebutton auto "gui/saveload/page3_%s.png" xpos 205 ypos 21 focus_mask True action FilePage(3) hover_sound "sfx/click.wav"
    imagebutton auto "gui/saveload/page4_%s.png" xpos 304 ypos 21 focus_mask True action FilePage(3) hover_sound "sfx/click.wav"
    imagebutton auto "gui/saveload/page5_%s.png" xpos 394 ypos 21 focus_mask True action FilePage(3) hover_sound "sfx/click.wav"
    imagebutton auto "gui/saveload/page6_%s.png" xpos 484 ypos 21 focus_mask True action FilePage(3) hover_sound "sfx/click.wav"

    imagebutton auto "gui/saveload/fileslot_top_row_%s.png" xpos 24 ypos 86 focus_mask True action FileAction(0)
    use load_save_slot(number=0, x=24, y=86) # This calls the load_save_slot screen defined above. We pass variable i as the slot number and x, y coordinates.

    imagebutton auto "gui/saveload/fileslot_top_row_%s.png" xpos 302 ypos 86 focus_mask True action FileAction(1)
    use load_save_slot(number=1, x=303, y=86) # This calls the load_save_slot screen defined above. We pass variable i as the slot number and x, y coordinates.

    imagebutton auto "gui/saveload/fileslot_bottom_row_%s.png" xpos 24 ypos 334 focus_mask True action FileAction(2)
    use load_save_slot(number=2, x=24, y=334) # This calls the load_save_slot screen defined above. We pass variable i as the slot number and x, y coordinates.

    imagebutton auto "gui/saveload/fileslot_bottom_row_%s.png" xpos 302 ypos 334 focus_mask True action FileAction(3)
    use load_save_slot(number=3, x=303, y=334) # This calls the load_save_slot screen defined above. We pass variable i as the slot number and x, y coordinates.

##############################################################################
# Save
#
screen save:
    tag menu # This ensures that any other menu screen is replaced.
    add "gui/saveload/screen_ground.png" # We add the file picker background image. This image is the same for save and load screens.
    use file_picker # We include the file_picker screen

##############################################################################
# Load
#
screen load:
    tag menu # This ensures that any other menu screen is replaced.
    add "gui/saveload/screen_ground.png" # We add the file picker background image. This image is the same for save and load screens.
    use file_picker # We include the file_picker screen


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
screen preferences:
    tag menu # This ensures that any other menu screen is replaced.
    add "gui/options/screen_ground.png" # We add the image that is shown in the background of the preferences screen.
    # Display windowed/full screen:
    imagebutton auto "gui/options/windowed_%s.png" xpos 30 ypos 64 focus_mask True action Preference('display', 'window') at config_eff hovered [ Play ("test_one", "sfx/click.wav") ]
    imagebutton auto "gui/options/full_screen_%s.png" xpos 30 ypos 111 focus_mask True action Preference('display', 'fullscreen') at config_eff hovered [ Play ("test_two", "sfx/click.wav") ]
    # Transitions on/off:
    imagebutton auto "gui/options/show_all_%s.png" xpos 30 ypos 225 focus_mask True action Preference('transitions', 'all') at config_eff hovered [ Play ("test_four", "sfx/click.wav") ] 
    imagebutton auto "gui/options/none_%s.png" xpos 30 ypos 272 focus_mask True action Preference('transitions', 'none') at config_eff hovered [ Play ("test_four", "sfx/click.wav") ]
    # Skip all/seen text
    imagebutton auto "gui/options/read_messages_%s.png" xpos 318 ypos 64 focus_mask True action Preference('skip', 'seen') at config_eff hovered [ Play ("test_one", "sfx/click.wav") ]
    imagebutton auto "gui/options/all_messages_%s.png" xpos 318 ypos 111 focus_mask True action Preference('skip', 'all') at config_eff hovered [ Play ("test_two", "sfx/click.wav") ]
    # Stop/continue skipping after choices
    imagebutton auto "gui/options/keep_skipping_%s.png" xpos 318 ypos 225 focus_mask True action Preference('after choices', 'skip') at config_eff hovered [ Play ("test_two", "sfx/click.wav") ]
    imagebutton auto "gui/options/stop_skipping_%s.png" xpos 318 ypos 272 focus_mask True action Preference('after choices', 'stop') at config_eff hovered [ Play ("test_one", "sfx/click.wav") ] 
    # Button to begin skipping. Only active/visible if the game is started. Image config_begin_skipping_insensitive.png is used when the button is not active.
    ## todo: need begin skipping button
    #imagebutton auto "gui/config_begin_skipping_%s.png" xpos 420 ypos 117 focus_mask True action Preference('begin skipping') hovered [ Play ("test_one", "sfx/click.wav") ]
    # bar sliders for volume control, text speed and auto-forward time
    frame xpos 24 ypos 386:
        style_group "pref"
        has vbox
        bar value Preference("music volume")
    frame xpos 24 ypos 495:
        style_group "pref"
        has vbox
        bar value Preference("sound volume")
    frame xpos 311 ypos 386:
        style_group "pref"
        has vbox
        bar value Preference("auto-forward time")
    use navigation_options # We include the navigation screen (game menu)
      
init -2 python: 
    # Styling for the bar sliders:
    # Aleema's Customizing Menus tutorial: http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=9812
    # Bar style properties documentation: http://www.renpy.org/doc/html/style.html#bar-style-properties
    style.pref_frame.background = None
    style.pref_slider.left_bar = "gui/options/bar_full.png"
    style.pref_slider.right_bar = "gui/options/bar_empty.png"
    style.pref_slider.hover_left_bar = "gui/options/bar_hover.png"
    style.pref_slider.thumb = None
    style.pref_slider.xmaximum = 260 # width of bar + 5
    style.pref_slider.ymaximum = 48  # height of bar
    
init -2:
    transform config_eff:
        on idle:
            easein 0.2 zoom 1.0
        on selected_idle:
            easein 0.2 zoom 1.0
        on hover:
            easein 0.15 zoom 1.02
            easein 0.15 zoom 0.95
            easein 0.15 zoom 1.0
        on selected_hover:
            easein 0.15 zoom 1.02
            easein 0.15 zoom 0.95
            easein 0.15 zoom 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt
    
screen yesno_prompt:
    on "show" action Play("sound", "sfx/alert.wav")
    modal True # A modal screen prevents the user from interacting with displayables below it, except for the default keymap.
    
    add "gui/yesno/ground.png" #"gui/yesno/menu_demo.png"
    imagebutton auto "gui/yesno/yes_%s.png" xpos 180 ypos 393 action yes_action hover_sound "sfx/click.wav"
    imagebutton auto "gui/yesno/no_%s.png" xpos 400 ypos 393 action no_action hover_sound "sfx/click.wav"

    if message == layout.ARE_YOU_SURE:
        add "gui/yesno/are_you_sure.png"
    elif message == layout.DELETE_SAVE:
        add "gui/yesno/delete_save.png"
    elif message == layout.OVERWRITE_SAVE:
        add "gui/yesno/overwrite_save.png"
    elif message == layout.LOADING:
        add "gui/yesno/loading.png"
    elif message == layout.QUIT:
        add "gui/yesno/quit.png"
    elif message == layout.MAIN_MENU:
        add "gui/yesno/main_menu.png"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"
    
        xalign 1.0
        yalign 1.0

        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Skip") action Skip()
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')
        
init -2 python:
    style.quick_button.set_parent('default')
    style.quick_button.background = None
    style.quick_button.xpadding = 5

    style.quick_button_text.set_parent('default')
    style.quick_button_text.size = 12
    style.quick_button_text.idle_color = "#8888"
    style.quick_button_text.hover_color = "#ccc"
    style.quick_button_text.selected_idle_color = "#cc08"
    style.quick_button_text.selected_hover_color = "#cc0"
    style.quick_button_text.insensitive_color = "#4448"
    
    # Set a default value for the auto-forward time, and note that AFM is
    # turned off by default.
    config.default_afm_time = 10
    config.default_afm_enable = False
    
    
