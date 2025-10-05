define -2 gui.name_text_outlines = [ (3, "#000000F0", 0, 0) ]

init 999:
    define gui.name_xpos = 60
    define gui.name_ypos = 80
    define gui.textbox_height = 360
    define gui.dialogue_xpos = 60
    define gui.dialogue_ypos = 140
    define gui.dialogue_width = 1750
    define gui.choice_button_width = 1200
    define gui.choice_button_text_size = 30
    define gui.file_slot_cols = 3
    define gui.file_slot_rows = 2
    define gui.name_text_size = 46
    define gui.interface_text_size = 35
    define gui.button_text_size = 35
    define gui.label_text_size = 40
    default persistent.gl2 = True
    define config.gl2 = persistent.gl2
    define persistent.renset = True

label MCrename:
    $ mcf = renpy.input("What's Main Character's name?")
    $ mcf = mcf.strip() or "MC"
    scene black
return


init python:
    config.overlay_screens.append("quick_menu")

style game_menu_navigation_frame:
    variant "small"
    xsize 420
style pref_vbox:
    variant "small"
    xsize 300
style slider_slider:
    variant "small"
    xsize 900

default persistent.quickmenu = 2
define quick_menu = True
default quick_menu = True
define config.hw_video = False
define persistent.TextOutline1 = 2
define persistent.pref_text_size = 33
define persistent.say_window_alpha = 1.0
define -1 config.gestures = {"w" : "rollback", "n" : "game_menu", "e" : "skip", "s" : "hide_windows"}
screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        background Transform(style.window.background, alpha=persistent.say_window_alpha)

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what" size persistent.pref_text_size




    add SideImage() xalign 0.0 yalign 1.0

init 999 style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        if persistent.quickmenu == 1:

            hbox:
                style_prefix "quick"

                xalign 1.0
                yalign 1.0
                spacing -80

                textbutton "{size=24}{font=gui/fonts/BebasNeue-Regular.ttf}Back" action Rollback()
                textbutton "{size=24}{font=gui/fonts/BebasNeue-Regular.ttf}Auto" action Preference("auto-forward", "toggle")
                textbutton "{size=24}{font=gui/fonts/BebasNeue-Regular.ttf}Skip" action Hide("qmenutextdisplay"), Skip() alternate Skip(fast=True, confirm=True)
                textbutton "{size=24}{font=gui/fonts/BebasNeue-Regular.ttf}Log" action ShowMenu('history')
                textbutton "{size=24}{font=gui/fonts/BebasNeue-Regular.ttf}Q. Save" action QuickSave()
                textbutton "{size=24}{font=gui/fonts/BebasNeue-Regular.ttf}Q. Load" action QuickLoad()
                textbutton "{size=24}{font=gui/fonts/BebasNeue-Regular.ttf}Mute" action Preference("all mute", "toggle")
                textbutton "{size=24}{font=gui/fonts/BebasNeue-Regular.ttf}Menu" action ShowMenu('navigation')

    if quick_menu:

        if persistent.quickmenu == 2:

            hbox:
                style_prefix "quick"

                xalign 0.99
                yalign 0.99
                spacing 30

                imagebutton auto "gui/quick_menu/back_%s.png":
                    action Rollback()
                imagebutton auto "gui/quick_menu/skip_%s.png":
                    action Skip() alternate Skip(fast=True, confirm=True)
                imagebutton auto "gui/quick_menu/auto_write_%s.png":
                    action Preference("auto-forward", "toggle")
                imagebutton auto "gui/quick_menu/save_%s.png":
                    action ShowMenu('save')
                imagebutton auto "gui/quick_menu/load_%s.png":
                    action ShowMenu('load')
                imagebutton auto "gui/quick_menu/settings_%s.png":
                    action ShowMenu('navigation')

screen pc_clock():
    python:
        import time

        current_time = time.strftime("%H:%M", time.localtime())

    vbox:
        style "main_menu_vbox"
        text "Clock [current_time]"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
