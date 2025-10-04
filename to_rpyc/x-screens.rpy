










init -1 style default:
    properties gui.text_properties()
    language gui.language
    emoji_font None

init -1 style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

init -1 style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

init -1 style gui_text:
    properties gui.text_properties("interface")


init -1 style button:
    properties gui.button_properties("button")

init -1 style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


init -1 style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

init -1 style prompt_text is gui_text:
    properties gui.text_properties("prompt")


init -1 style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

init -1 style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

init -1 style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

init -1 style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

init -1 style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


init -1 style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)





















init -501 screen textbox2:
    add "gui/textbox2.png" xalign 0.5 yalign 1.0

define -1 persistent.say_window_alpha = 1.0

init -501 screen qmenu:
    zorder 1000















init -501 screen points():

    vbox ypos 0.01 xpos 0.01:

        text "Toughness: [toughness]" ypos 0.01
        text "Killian Bromance: [Killian_Bromance]" ypos 0.03
        text "Rosalind Affection: [Rosalind_Affection]" ypos 0.1
        text "Felicia Affection: [Felicia_Affection]" ypos 0.18
        text "Veronica Affection: [Veronica_Affection]" ypos 0.26
        text "Mina Affection: [Mina_Affection]" ypos 0.34
        text "Hana Affection: [Hana_Affection]" ypos 0.42
        textbutton "Close" action Hide("points") ypos 0.48


init -501 screen say(who, what):

    style_prefix "say"

    window:



        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"
                ypos 0.02

        text what id "what"




    add SideImage() xalign 0.0 yalign 1.0



init -1 python:
    config.character_id_prefixes.append('namebox')

init -1 style window is default
init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue

init -1 style namebox is default
init -1 style namebox_label is say_label


init -1 style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height



init -1 style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

init -1 style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

init -1 style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos












init -501 screen input(prompt):
    style_prefix "input"

    window:

        has vbox
        xalign gui.dialogue_text_xalign
        xpos gui.dialogue_xpos
        xsize gui.dialogue_width
        ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

init -1 style input_prompt is default

init -1 style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

init -1 style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width










init -501 screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action




define -1 config.narrator_menu = True


init -1 style choice_vbox is vbox
init -1 style choice_button is button
init -1 style choice_button_text is button_text

init -1 style choice_vbox:
    xalign 0.5
    ypos 500
    yanchor 0.5

    spacing gui.choice_spacing

init -1 style choice_button is default:
    properties gui.button_properties("choice_button")
    hover_sound "sound effects/click.wav"
    activate_sound "sound effects/click2.wav"


init -1 style choice_button_text is default:
    properties gui.button_text_properties("choice_button")







init -501 screen quick_menu():


    zorder 100




init -501 screen qmenutextdisplay:

    key "hide_windows" action NullAction()
    zorder 100
    default displayText = ("")

    vbox:
        xalign 0.7485
        ypos 0.69
        frame:
            style "app_gui"
            text "{size=+6}[displayText]{/size}"




init -1 python:
    config.overlay_screens.append("quick_menu")

default -1 quick_menu = True
default -1 qmenu = True
init -1 style quick_button is default
init -1 style quick_button_text is button_text

init -1 style quick_button:
    properties gui.button_properties("quick_button")

init -1 style quick_button_text:
    properties gui.button_text_properties("quick_button")















init -501 screen navigation():
    tag nav_screen
    on "show" action Play("menu_click", "sound effects/page-turn.wav")

    imagemap:

        idle "gui/screens/imagemaps/navigation_idle.png"
        hover "gui/screens/imagemaps/navigation_hover.png"
        ground "gui/screens/imagemaps/navigation_ground.png"

        hotspot (1414,6,550,90) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu('history') hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (1414,97,550,109) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu('preferences') hovered [ Play ("hover_load", "sound effects/click.wav") ]
        if profilehubunlock == True:
            hotspot (1500, 200, 550, 80) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu('profile_hub') hovered [ Play ("hover_load", "sound effects/click.wav") ]
        if statisticsunlock == True:
            hotspot (1519, 290, 450, 109) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu('statistics') hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (1500,385,550,109) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu('leisureroom') hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (1605,509,550,109) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu('save') hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (1620,625,550,112) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu('load') hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (1698,720,550,203) action [ Play ("menu_click","sound effects/page-turn.wav") ], MainMenu() hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (1700,900,550,200) action [ Play ("menu_click","sound effects/page-turn.wav") ], Quit('quit') hovered [ Play ("hover_load", "sound effects/click.wav") ]
        imagebutton auto "gui/screens/imagebuttons/return_%s.png" action Return() xpos 20 ypos 180

    if date == "introNight":
        add "images/misc/date/intronight.png"
    if date == "may07day":
        add "images/misc/date/may07day.png"
    if date == "may07night":
        add "images/misc/date/may07night.png"
    if date == "may08day":
        add "images/misc/date/may08day.png"
    if date =="may08night":
        add "images/misc/date/may08night.png"
    if date == "may09night":
        add "images/misc/date/may09night.png"
    if date == "may10day":
        add "images/misc/date/may10day.png"
    if date == "may10night":
        add "images/misc/date/may10night.png"
    if date == "may11day":
        add "images/misc/date/may11day.png"
    if date == "may11night":
        add "images/misc/date/may11night.png"
    if date == "may12day":
        add "images/misc/date/may12day.png"
    if date == "may12night":
        add "images/misc/date/may12night.png"
    if date == "may13night":
        add "images/misc/date/may13night.png"
    if date == "may14day":
        add "images/misc/date/may14day.png"
    if date == "may15night":
        add "images/misc/date/may15night.png"
    if date == "may16night":
        add "images/misc/date/may16night.png"
    if date == "june01day":
        add "images/misc/date/june01day.png"
    if date == "june01night":
        add "images/misc/date/june01night.png"
    if date == "june02day":
        add "images/misc/date/june02day.png"
    if date == "june02night":
        add "images/misc/date/june02night.png"
    if date == "june03day":
        add "images/misc/date/june03day.png"
    if date == "june03night":
        add "images/misc/date/june03night.png"
    if date == "june04day":
        add "images/misc/date/june04day.png"
    if date == "june04night":
        add "images/misc/date/june04night.png"
    if date == "june05day":
        add "images/misc/date/june05day.png"
    if date == "june05night":
        add "images/misc/date/june05night.png"
    if date == "june06night":
        add "images/misc/date/june06night.png"
    if date == "june07day":
        add "images/misc/date/june07day.png"
    if date == "june07night":
        add "images/misc/date/june07night.png"
    if date == "june08day":
        add "images/misc/date/june08day.png"
    if date == "june08night":
        add "images/misc/date/june08night.png"
    if date == "june09day":
        add "images/misc/date/june09day.png"
    if date == "june09night":
        add "images/misc/date/june09night.png"
    if date == "june10day":
        add "images/misc/date/june10day.png"
    if date == "june10night":
        add "images/misc/date/june10night.png"
    if date == "june11day":
        add "images/misc/date/june11day.png"
    if date == "june11night":
        add "images/misc/date/june11night.png"
    if date == "june12day":
        add "images/misc/date/june12day.png"
    if date == "june12night":
        add "images/misc/date/june12night.png"
    if date == "june13day":
        add "images/misc/date/june13day.png"
    if date == "june13night":
        add "images/misc/date/june13night.png"
    if date == "june14day":
        add "images/misc/date/june14day.png"
    if date == "june14night":
        add "images/misc/date/june14night.png"
    if date == "june15day":
        add "images/misc/date/june15day.png"
    if date == "june15night":
        add "images/misc/date/june15night.png"
    if date == "june16day":
        add "images/misc/date/june16day.png"
    if date == "june16night":
        add "images/misc/date/june16night.png"
    if date == "june17day":
        add "images/misc/date/june17day.png"
    if date == "june17night":
        add "images/misc/date/june17night.png"
    if date == "june18day":
        add "images/misc/date/june18day.png"
    if date == "june18night":
        add "images/misc/date/june18night.png"
    if date == "june19day":
        add "images/misc/date/june19day.png"
    if date == "june19night":
        add "images/misc/date/june19night.png"
    if date == "june20day":
        add "images/misc/date/june20day.png"
    if date == "june20night":
        add "images/misc/date/june20night.png"







init -1 style navigation_button is gui_button
init -1 style navigation_button_text is gui_button_text

init -1 style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

init -1 style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font "gui/fonts/FIGHTT3_.ttf"
    idle_color "#000"
    hover_color "#fde571"
    selected_color "#fde571"
    idle_outlines [(2, "#e8efed")]
    hover_outlines [(2, "#0f0f0f")]
    selected_outlines [(2, "#0f0f0f")]









init -501 screen main_menu():
    tag menu

    add "gui/screens/backgrounds/main_menu.png"

    add SnowBlossom("gui/particle.png", count=10, border=50, xspeed=(25, 50), yspeed=-100, start=3, horizontal=False)




    imagebutton auto "gui/screens/imagebuttons/new_%s.png" xpos 815 ypos 645 focus_mask True action [ Play ("menu_click","sound effects/sting-mumbaieffect.wav") ] , Start() hovered [ Play ("hover_start", "sound effects/click.wav") ]
    imagebutton auto "gui/screens/imagebuttons/continue_%s.png" xpos 815 ypos 710 focus_mask True action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu('load') hovered [ Play ("hover_load", "sound effects/click.wav") ]
    imagebutton auto "gui/screens/imagebuttons/extra_%s.png" xpos 815 ypos 775 focus_mask True action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("leisureroom") hovered [ Play ("hover_extra", "sound effects/click.wav") ]
    imagebutton auto "gui/screens/imagebuttons/settings_%s.png" xpos 815 ypos 840 focus_mask True action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu('preferences') hovered [ Play ("hover_settings", "sound effects/click.wav") ]
    imagebutton auto "gui/screens/imagebuttons/credits_%s.png" xpos 815 ypos 905 focus_mask True action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu('credits') hovered [ Play ("hover_exit", "sound effects/click.wav") ]
    imagebutton auto "gui/screens/imagebuttons/exit_%s.png" xpos 815 ypos 970 focus_mask True action [ Play ("menu_click","sound effects/page-turn.wav") ], Quit(confirm=False) hovered [ Play ("hover_exit", "sound effects/click.wav") ]
    imagebutton auto "gui/screens/imagebuttons/patreon_%s.png" xpos 0 ypos 340 focus_mask True action [ Play ("menu_click","sound effects/page-turn.wav") ], OpenURL("https://www.patreon.com/GIL3D") hovered [ Play ("hover_exit", "sound effects/click.wav") ]
    imagebutton auto "gui/screens/imagebuttons/discord_%s.png" xpos 0 ypos 475 focus_mask True action [ Play ("menu_click","sound effects/page-turn.wav") ], OpenURL("https://discord.com/invite/5W6CWUk") hovered [ Play ("hover_exit", "sound effects/click.wav") ]










init -501 screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"


    frame:
        style "game_menu_outer_frame"

        has hbox


        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            if scroll == "viewport":

                viewport:
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1
                    yinitial yinitial

                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    transclude

            else:

                transclude




    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


init -1 style game_menu_outer_frame is empty
init -1 style game_menu_navigation_frame is empty
init -1 style game_menu_content_frame is empty
init -1 style game_menu_viewport is gui_viewport
init -1 style game_menu_side is gui_side
init -1 style game_menu_scrollbar is gui_vscrollbar
init -1 style return_button is navigation_button
init -1 style return_button_text is navigation_button_text

init -1 style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

init -1 style game_menu_navigation_frame:
    xsize 420
    yfill False

init -1 style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

init -1 style game_menu_viewport:
    xsize 1380

init -1 style game_menu_vscrollbar:
    unscrollable gui.unscrollable

init -1 style game_menu_side:
    spacing 15

init -1 style game_menu_label:
    xpos 100000
    ysize 180

init -1 style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

init -1 style return_button:
    xpos 0.465
    ypos 0.94










init -501 screen about():
    tag menu
    add "gui/menu/about_screen.png"
    add SnowBlossom("gui/particle.png", count=10, border=50, xspeed=(25, 50), yspeed=-100, start=3, horizontal=False)



    use game_menu(_(""), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")



define -1 gui.about = ""


init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text
init -1 style about_text is gui_text

init -1 style about_label_text:
    size gui.label_text_size




















init -501 screen save():
    tag menu

    add "gui/screens/backgrounds/save_screen2.png"
    use file_slots(_("Save"))
    imagebutton auto "gui/screens/imagebuttons/return_%s.png" action Return() xpos 10 ypos 22


init -501 screen load():
    tag menu

    add "gui/screens/backgrounds/load_screen2.png"
    use file_slots(_("Load"))
    imagebutton auto "gui/screens/imagebuttons/return_%s.png" action Return() xpos 10 ypos 22



init -501 screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Auto"), quick=_("Quick"))

    use game_menu(title):



        grid 3 2:
            xpos -100
            ypos -20

            xspacing 30
            yspacing 50

            for i in range(6):

                $ slot = i + 1
                $ _name = FileSaveName(slot)

                button:
                    xysize (465, 285)
                    background "gui/button/panel_2.png"


                    add FileScreenshot(slot) xpos 35 ypos 25
                    text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("")):
                        style "slot_time_text" xalign 0.5 yalign 1.125

                    if _name:
                        add Solid("#000000", xysize=(370, 35)) alpha 0.8 xpos 45 ypos 208
                        text _name size 28 xalign 0.5 ypos 208

                    hover_foreground "gui/button/slot_glow_2.png" xpos 35 ypos 25
                    action If(title.lower() == "save", true=Show("give_save_name", slotIndex = slot), false=FileLoad(slot))
                    key "save_delete" action FileDelete(slot)


    hbox:
        xpos 300
        ypos 930

        spacing 16

        imagebutton:
            idle "gui/button/prev-tab.png"
            hover "gui/button/prev-tab.png"
            xpos 70
            action FilePagePrevious()
            ypos -800
            yalign 1.0

        if config.has_autosave:
            button:
                style "slot_button"
                ypos -900
                xpos 50
                text "A" align (0.5, 0.5) style "slot_button_text"
                action FilePage("auto")

        if config.has_quicksave:
            button:
                style "slot_button"
                ypos -900
                xpos 50
                text "Q" align (0.5, 0.5) style "slot_button_text"
                action FilePage("quick")


        for page in range(1, 10):
            button:
                style "slot_button"
                ypos -900
                xpos 50
                text "[page]" align (0.5, 0.5) style "slot_button_text"
                action FilePage(page)

        imagebutton:
            idle "gui/button/Next-tab.png"
            hover "gui/button/Next-tab.png"
            ypos -800
            action FilePageNext()
            xpos 30
            yalign 1.0

    button:
        style "page_label"

        key_events True
        xalign 0.6
        yalign 0.133
        action page_name_value.Toggle()

        input:
            style "page_label_text"
            value page_name_value


init -1 style page_label is gui_label
init -1 style page_label_text is gui_label_text
init -1 style page_button is gui_button
init -1 style page_button_text is gui_button_text

init -1 style slot_button is gui_button
init -1 style slot_button_text is gui_button_text
init -1 style slot_time_text:
    size 22
    idle_color "#F080D4b0"
    hover_color "#F080D4"
    hover_bold True
    hover_kerning -2
init -1 style slot_name_text is slot_button_text

init -1 style page_label:
    xpadding 75
    ypadding 5

init -1 style page_label_text:
    text_align 0.5
    color "#e61ab4"
    layout "subtitle"
    hover_color gui.hover_color

init -1 style page_button:
    properties gui.button_properties("page_button")

init -1 style page_button_text:
    properties gui.button_text_properties("page_button")

init -1 style slot_button:
    xysize (108, 108)

    idle_background "gui/button/Save-Tab-Unselected.png"
    hover_background "gui/button/Save-Tab-Selected.png"
    selected_idle_background "gui/button/Save-Tab-Selected.png"

init -1 style slot_button_text:
    font "gui/fonts/LeagueGothic-Regular.otf"
    size 60
    color "#ffffff"









init -501 screen preferences():
    tag menu

    imagemap:
        auto "gui/screens/imagemaps/prefs_%s.png"

        hotspot (1565, 185, 130, 120) action Preference("display", "fullscreen") alt _("Display Fullscreen")
        hotspot (1682, 185, 150, 120) action Preference("display", "window") alt _("Display Window")
        hotspot (1340, 330, 150, 200) action Preference("skip", "seen")
        hotspot (1480, 330, 125, 200) action Preference("skip", "all")
        hotspot (1627, 330, 125, 200) action Preference("transitions", "all")
        hotspot (1758, 330, 125, 200) action Preference("transitions", "none")
        if not _in_replay:
            hotspot (10, 22, 180, 180) action Return()
        hotbar (1495, 594, 400, 90) value Preference("music volume") alt _("Music Volume")
        hotbar (1500, 718, 400, 90) value Preference("sound volume") alt _("Sound Volume")
        hotbar (1504, 855, 400, 90) value Preference("text speed") alt _("Text Speed")
        hotbar (1508, 979, 400, 90) value Preference("auto-forward time")
        if _in_replay:
            hotspot (10, 22, 180, 180) action Return()
            imagebutton auto "gui/screens/imagebuttons/exitm_%s.png" action EndReplay(confirm=True) xpos 150 ypos 14

    vbox:
        style_prefix "check"
        label _("Powersave") ypos 150
        textbutton _("Enable") action Preference("gl powersave", True) ypos 150
        textbutton _("Disable") action Preference("gl powersave", False) ypos 150

    vbox:
        style_prefix "check"
        label _("Quick Menu Vars") ypos 150 xpos 250
        textbutton _("QM") action ToggleVariable("qmenu", True, False) ypos 150 xpos 250
        textbutton _("QM ICON") action ToggleVariable("persistent.quickmenu",2,1) ypos 150 xpos 250

    vbox:
        style_prefix "check"
        label _("Others") ypos 400
        textbutton "Change MC name" action [ui.callsinnewcontext("MCrename")] ypos 400
        textbutton _("GL2(For Powervr CPU)") action ToggleField(persistent, "gl2", True, False) ypos 400

    vbox:
        style_prefix "radio"
        label _("HWA Video") ypos 450 xpos 250
        textbutton _("Enable") action SetVariable("config.hw_video", True) ypos 450 xpos 250
        textbutton _("Disable") action SetVariable("config.hw_video", False) ypos 450 xpos 250

    ## LANGUAGE SELECTOR - TAMBAHAN BARU
    vbox:
        style_prefix "radio"
        label _("Language") ypos 550 xpos 250
        textbutton _("English") action Function(set_language, None) ypos 550 xpos 250
        textbutton _("Bahasa Indonesia") action Function(set_language, "id") ypos 550 xpos 250

    label _("Text Box Opacity: " + str(int(persistent.say_window_alpha*100)) + "%") xpos 500 ypos 150

    bar value FieldValue(persistent, 'say_window_alpha', 1.0, max_is_zero=False, offset=0, step=1, style=u"slider") xsize 475 ysize 41 xpos 500 ypos 200

    label _("Text Size:  [persistent.pref_text_size]") xpos 500 ypos 350

    bar value FieldValue(persistent, 'pref_text_size', range=76, max_is_zero=False, style=u'slider', offset=0, step=1) xsize 475 ysize 41 xpos 500 ypos 400


init -1 style pref_label is gui_label
init -1 style pref_label_text is gui_label_text
init -1 style pref_vbox is vbox

init -1 style radio_label is pref_label
init -1 style radio_label_text is pref_label_text
init -1 style radio_button is gui_button
init -1 style radio_button_text is gui_button_text
init -1 style radio_vbox is pref_vbox

init -1 style check_label is pref_label
init -1 style check_label_text is pref_label_text
init -1 style check_button is gui_button
init -1 style check_button_text is gui_button_text
init -1 style check_vbox is pref_vbox

init -1 style slider_label is pref_label
init -1 style slider_label_text is pref_label_text
init -1 style slider_slider is gui_slider
init -1 style slider_button is gui_button
init -1 style slider_button_text is gui_button_text
init -1 style slider_pref_vbox is pref_vbox

init -1 style mute_all_button is check_button
init -1 style mute_all_button_text is check_button_text

init -1 style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

init -1 style pref_label_text:
    yalign 1.0

init -1 style pref_vbox:
    xsize 338

init -1 style radio_vbox:
    spacing gui.pref_button_spacing
init -1 style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"
    xsize 150

init -1 style radio_button_text:
    properties gui.button_text_properties("radio_button")

init -1 style check_vbox:
    spacing gui.pref_button_spacing

init -1 style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
    xsize 175

init -1 style check_button_text:
    properties gui.button_text_properties("check_button")

init -1 style slider_slider:
    xsize 525

init -1 style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

init -1 style slider_button_text:
    properties gui.button_text_properties("slider_button")

init -1 style slider_vbox:
    xsize 675










init -501 screen history():
    tag menu


    imagemap:

        idle "gui/screens/imagemaps/history_idle.png"
        hover "gui/screens/imagemaps/history_hover.png"
        ground "gui/screens/imagemaps/history_ground.png"

        hotspot (1757,60,800,120) action Hide('history')


    predict False

    use game_menu(_(""), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:


                has fixed
                yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False



                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")




define -1 gui.history_allow_tags = set()


init -1 style history_window is empty

init -1 style history_name is gui_label
init -1 style history_name_text is gui_label_text
init -1 style history_text is gui_text

init -1 style history_text is gui_text

init -1 style history_label is gui_label
init -1 style history_label_text is gui_label_text

init -1 style history_window:
    xfill True
    ysize gui.history_height

init -1 style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

init -1 style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

init -1 style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

init -1 style history_label:
    xfill True

init -1 style history_label_text:
    xalign 0.5








init -501 screen help():
    tag menu

    add "gui/menu/help_screen.png"
    add SnowBlossom("gui/particle.png", count=10, border=50, xspeed=(25, 50), yspeed=-100, start=3, horizontal=False)
    default device = "keyboard"

    use game_menu(_(""), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


init -501 screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


init -501 screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


init -501 screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


init -1 style help_button is gui_button
init -1 style help_button_text is gui_button_text
init -1 style help_label is gui_label
init -1 style help_label_text is gui_label_text
init -1 style help_text is gui_text

init -1 style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

init -1 style help_button_text:
    properties gui.button_text_properties("help_button")

init -1 style help_label:
    xsize 375
    right_padding 30

init -1 style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0















init -501 screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox
        xalign .5
        yalign .5
        spacing 45

        label _(message):
            style "confirm_prompt"
            xalign 0.5


        hbox:
            xalign 0.5
            spacing 150

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action


    key "game_menu" action no_action


init -1 style confirm_frame is gui_frame
init -1 style confirm_prompt is gui_prompt
init -1 style confirm_prompt_text is gui_prompt_text
init -1 style confirm_button is gui_medium_button
init -1 style confirm_button_text is gui_medium_button_text

init -1 style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/confirm_frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

init -1 style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

init -1 style confirm_button:
    properties gui.button_properties("confirm_button")
    xsize 100

init -1 style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









init -501 screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox
        spacing 9

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform -1 delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


init -1 style skip_frame is empty
init -1 style skip_text is gui_text
init -1 style skip_triangle is skip_text

init -1 style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

init -1 style skip_text:
    size gui.notify_text_size

init -1 style skip_triangle:


    font "DejaVuSans.ttf"









init -501 screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform -1 notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


init -1 style notify_frame is empty
init -1 style notify_text is gui_text

init -1 style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

init -1 style notify_text:
    properties gui.text_properties("notify")









init -501 screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox
        spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


init -501 screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed
            yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id




define -1 config.nvl_list_length = gui.nvl_list_length

init -1 style nvl_window is default
init -1 style nvl_entry is default

init -1 style nvl_label is say_label
init -1 style nvl_dialogue is say_dialogue

init -1 style nvl_button is button
init -1 style nvl_button_text is button_text

init -1 style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

init -1 style nvl_entry:
    xfill True
    ysize gui.nvl_height

init -1 style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

init -1 style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

init -1 style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

init -1 style nvl_button_text:
    properties gui.button_text_properties("nvl_button")


init -501 screen statistics():
    tag nav_screen
    imagemap:

        idle "gui/screens/imagemaps/stats_idle.png"
        hover "gui/screens/imagemaps/stats_hover.png"
        ground "gui/screens/imagemaps/stats_ground.png"
        hotspot (985,162,150,140) action [ Play ("menu_click","sound effects/page-turn.wav") ], Show("stats_pcian") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (1138,162,150,140) action [ Play ("menu_click","sound effects/page-turn.wav") ], Show("stats_mina") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (1285,162,150,140) action [ Play ("menu_click","sound effects/page-turn.wav") ], Show("stats_hana") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (988,301,150,140) action [ Play ("menu_click","sound effects/page-turn.wav") ], Show("stats_rosalind") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (1140,301,150,140) action [ Play ("menu_click","sound effects/page-turn.wav") ], Show("stats_veronica") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (1288,301,150,140) action [ Play ("menu_click","sound effects/page-turn.wav") ], Show("stats_felicia") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (985,442,150,140) action [ Play ("menu_click","sound effects/page-turn.wav") ], Show("stats_kathleen") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (1138,442,150,140) action [ Play ("menu_click","sound effects/page-turn.wav") ], Show("stats_chuckaugust") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (1289,442,150,140) action [ Play ("menu_click","sound effects/page-turn.wav") ], Show("stats_misc") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        textbutton "{size=+20}Return to game{/size=+20}" action [Hide("stats_hub"), Hide("stat_menu"), Show("navigation")] xpos 0.53 ypos 0.85



init -501 screen stats_pcian():
    tag stat_menu
    add "gui/screens/backgrounds/stats_pcian.png"
    text "{color=#4169E1}{u}Toughness{/u}:{/color=#4169E1} [toughness]" xpos 0.509 ypos 0.59
    if Killian_Bromance == 40:
        text "{color=#8B0000}{u}Killian Bromance{/u}:{/color=#8B0000} Maxed" xpos 0.509 ypos 0.63
    else:
        text "{color=#8B0000}{u}Killian Bromance{/u}:{/color=#8B0000} [Killian_Bromance]" xpos 0.509 ypos 0.63
    if trait_inquisitive == True:
        text "{u}Trait{/u}: Inquisitive" xpos 0.509 ypos 0.67
    if trait_tireless == True:
        text "{u}Trait{/u}: Tireless" xpos 0.509 ypos 0.67
    if trait_governor == True:
        text "{u}Trait{/u}: Governor" xpos 0.509 ypos 0.67
    if history_firestarter == True:
        text "{u}Histor{/u}y: Firestarter" xpos 0.509 ypos 0.71
    if history_voyeur == True:
        text "{u}History{/u}: Voyeur" xpos 0.509 ypos 0.71
    if history_stickyFingers == True:
        text "{u}History{/u}: Sticky Fingers" xpos 0.509 ypos 0.71
    if perk_strongman == True:
        text "{u}Perk{/u}: Strongman" xpos 0.509 ypos 0.75
    if perk_socialButterfly == True:
        text "{u}Perk{/u}: Social Butterfly" xpos 0.509 ypos 0.75
    if perk_socialChameleon == True:
        text "{u}Perk{/u}: Social Chameleon" xpos 0.509 ypos 0.75




init -501 screen stats_mina():
    tag stat_menu
    add "gui/screens/backgrounds/stats_mina.png"
    if Mina_Affection == 40:
        text "{color=#4169E1}{u}Affection Score{/u}:{/color=#4169E1} Maxed" xpos 0.509 ypos 0.59
    else:
        text "{color=#4169E1}{u}Affection Score{/u}:{/color=#4169E1} [Mina_Affection]" xpos 0.509 ypos 0.59
    text "{color=#8B0000}{u}Killian Romance{/u}:{/color=#8B0000} [Mina_KLove]" xpos 0.509 ypos 0.63
    text "{color=#DB7093}{u}Bi-curious Score{/u}:{/color=#DB7093} [Mina_BiCurious]" xpos 0.509 ypos 0.67
    text "{u}Relation{/u}: [Mina_Relations]" xpos 0.509 ypos 0.71

init -501 screen stats_hana():
    tag stat_menu
    add "gui/screens/backgrounds/stats_hana.png"
    if Hana_Affection == 40:
        text "{color=#4169E1}{u}Affection Score{/u}:{/color=#4169E1} Maxed" xpos 0.509 ypos 0.59
    else:
        text "{color=#4169E1}{u}Affection Score{/u}:{/color=#4169E1} [Hana_Affection]" xpos 0.509 ypos 0.59
    text "{color=#8B0000}{u}Anger Score{/u}:{/color=#8B0000} [Hana_Anger]" xpos 0.509 ypos 0.63
    text "{u}Relation{/u}: [Hana_Relations]" xpos 0.509 ypos 0.67


init -501 screen stats_rosalind():
    tag stat_menu
    add "gui/screens/backgrounds/stats_rosalind.png"
    if Rosalind_Affection == 40:
        text "{color=#4169E1}{u}Affection Score{/u}:{/color=#4169E1} Maxed" xpos 0.509 ypos 0.59
    else:
        text "{color=#4169E1}{u}Affection Score{/u}:{/color=#4169E1} [Rosalind_Affection]" xpos 0.509 ypos 0.59
    text "{color=#FF1493}{u}Libido Score{/u}:{/color=#FF1493} [Rosalind_Libido]" xpos 0.509 ypos 0.63
    text "{u}Relation{/u}: [Rosalind_Relations]" xpos 0.509 ypos 0.67


init -501 screen stats_veronica():
    tag stat_menu
    add "gui/screens/backgrounds/stats_veronica.png"
    if Veronica_Affection == 40:
        text "{color=#4169E1}{u}Affection Score{/u}:{/color=#4169E1} Maxed" xpos 0.509 ypos 0.59
    else:
        text "{color=#4169E1}{u}Affection Score{/u}:{/color=#4169E1} [Veronica_Affection]" xpos 0.509 ypos 0.59
    text "{color=#800000}{u}Horniness Score{/u}:{/color=#800000} [Veronica_Horniness]" xpos 0.509 ypos 0.63
    text "{u}Relation{/u}: [Veronica_Relations]" xpos 0.509 ypos 0.67

init -501 screen stats_felicia():
    tag stat_menu
    add "gui/screens/backgrounds/stats_felicia.png"
    if Felicia_Affection == 40:
        text "{color=#4169E1}{u}Affection Score{/u}:{/color=#4169E1} Maxed" xpos 0.509 ypos 0.59
    else:
        text "{color=#4169E1}{u}Affection Score{/u}:{/color=#4169E1} [Felicia_Affection]" xpos 0.509 ypos 0.59
    text "{color=#F0E68C}{u}Self-confidence Score{/u}:{/color=#F0E68C} [Felicia_Confidence]" xpos 0.509 ypos 0.63
    text "{u}Relation{/u}: [Felicia_Relations]" xpos 0.509 ypos 0.67

init -501 screen stats_kathleen():
    tag stat_menu
    add "gui/screens/backgrounds/stats_kat.png"
    if Kathleen_Affection == 30:
        text "{color=#4169E1}{u}Affection Score{/u}:{/color=#4169E1} Maxed" xpos 0.509 ypos 0.59
    else:
        text "{color=#4169E1}{u}Affection Score{/u}:{/color=#4169E1} [Kathleen_Affection]" xpos 0.509 ypos 0.59
    text "{color=#9f9f9f}{u}Trust Score{/u}:{/color=#9f9f9f} [Kathleen_Trust]" xpos 0.509 ypos 0.63
    text "{u}Relation{/u}: [Kathleen_Relations]" xpos 0.509 ypos 0.67


init -501 screen stats_chuckaugust():
    tag stat_menu
    add "gui/screens/backgrounds/stats_chuckaugust.png"
    if Chuck_Friendship == 10:
        text "{color=#FAEBD7}{u}Chuck Friendship Score{/u}:{/color=#FAEBD7} Maxed" xpos 0.509 ypos 0.59
    else:
        text "{color=#FAEBD7}{u}Chuck Friendship Score{/u}:{/color=#FAEBD7} [Chuck_Friendship]" xpos 0.509 ypos 0.59
    if August_Friendship == 10:
        text "{color=#FF8C00}{u}August Friendship Score{/u}:{/color=#FF8C00} Maxed" xpos 0.509 ypos 0.63
    else:
        text "{color=#FF8C00}{u}August Friendship Score{/u}:{/color=#FF8C00} [August_Friendship]" xpos 0.509 ypos 0.63
    if chuckTrust == True:
        text "{color=#FAEBD7}{u}Trusted by Dr. Chuck{/u}:{/color=#FAEBD7} Yes" xpos 0.509 ypos 0.67
    if chuckTrust == False:
        text "{color=#FAEBD7}{u}Trusted by Dr. Chuck{/u}:{/color=#FAEBD7} No" xpos 0.509 ypos 0.67
    if augustTrust == True:
        text "{color=#FF8C00}{u}Trusted by August{/u}:{/color=#FF8C00} Yes" xpos 0.509 ypos 0.71
    if augustTrust == False:
        text "{color=#FF8C00}{u}Trusted by August{/u}:{/color=#FF8C00} No" xpos 0.509 ypos 0.71

init -501 screen stats_misc():
    tag stat_menu
    add "gui/screens/backgrounds/stats_misc.png"
    text "{color=#33A625}{u}Jacob Friendship Score{/u}:{/color=#33A625} [Jacob_Friendship]" xpos 0.509 ypos 0.59
    text "{color=#8B4513}{u}Warren Friendship Score{/u}:{/color=#8B4513} [Warren_Friendship]" xpos 0.509 ypos 0.63
    text "{color=#A9A9A9}{u}Samson Friendship Score{/u}:{/color=#A9A9A9} [Sam_Friendship]" xpos 0.509 ypos 0.67


init -501 screen profile_hub():
    tag nav_screen
    add "gui/screens/backgrounds/profile_hub.png"


    textbutton "Return to game" action [Hide("profile_hub"), Hide("profile_screen"), Show("navigation")] xpos 0.19 ypos 0.84


    if met_august == True and unread_august == True:
        textbutton "August Byrnes" action [Show("profile_august"), SetVariable("unread_august", False)] xpos 0.177 ypos 0.15
        add "new" xpos 0.292 ypos 0.156
    if met_august == True and unread_august == False:
        textbutton "August Byrnes" action Show("profile_august") xpos 0.177 ypos 0.15
    if met_august == False and unread_august == True:
        textbutton "??? ???" action Show("profile_august") xpos 0.177 ypos 0.15


    if unread_chuck == True:
        textbutton "Charles Kohler" action [Show("profile_chuck"), SetVariable("unread_chuck", False)] xpos 0.177 ypos 0.18
        add "new" xpos 0.292 ypos 0.186
    else:
        textbutton "Charles Kohler" action Show("profile_chuck") xpos 0.177 ypos 0.18


    if met_felicia == True and unread_felicia == True:
        textbutton "Felicia Ford" action [Show("profile_felicia"), SetVariable("unread_felicia", False)] xpos 0.177 ypos 0.21
        add "new" xpos 0.292 ypos 0.216
    if met_felicia == True and unread_felicia == False:
        textbutton "Felicia Ford" action Show("profile_felicia") xpos 0.177 ypos 0.21
    if met_felicia == False and unread_felicia == True:
        textbutton "??? ???" action Show("profile_felicia") xpos 0.177 ypos 0.21


    if met_hana == True and unread_hana == True:
        textbutton "Hana Rhodes" action [Show("profile_hana"), SetVariable("unread_hana", False)] xpos 0.177 ypos 0.24
        add "new" xpos 0.292 ypos 0.246
    if met_hana == True and unread_hana == False:
        textbutton "Hana Rhodes" action Show("profile_hana") xpos 0.177 ypos 0.24
    if met_hana == False and unread_hana == True:
        textbutton "??? ???" action Show("profile_hana") xpos 0.177 ypos 0.24


    if met_isaak == True and unread_isaak == True:
        textbutton "Isaak Miller" action [Show("profile_isaak"), SetVariable("unread_isaak", False)] xpos 0.177 ypos 0.27
        add "new" xpos 0.292 ypos 0.276
    if met_isaak == True and unread_isaak == False:
        textbutton "Isaak Miller" action Show("profile_isaak") xpos 0.177 ypos 0.27
    if met_isaak == False and unread_isaak == True:
        textbutton "??? ???" action Show("profile_isaak") xpos 0.177 ypos 0.27


    if met_jacob == True and unread_jacob == True:
        textbutton "Jacob Clark" action [Show("profile_jacob"), SetVariable ("unread_jacob", False)] xpos 0.177 ypos 0.30
        add "new" xpos 0.292 ypos 0.306
    if met_jacob == True and unread_jacob == False:
        textbutton "Jacob Clark" action Show("profile_jacob") xpos 0.177 ypos 0.30
    if met_jacob == False and unread_jacob == True:
        textbutton "??? ???" action Show("profile_jacob") xpos 0.177 ypos 0.30


    if met_kathleen == True and unread_kathleen == True:
        textbutton "Kathleen Pulman" action [Show("profile_kathleen"), SetVariable("unread_kathleen", False)] xpos 0.177 ypos 0.33
        add "new" xpos 0.292 ypos 0.336
    if met_kathleen == True and unread_kathleen == False:
        textbutton "Kathleen Pulman" action Show("profile_kathleen") xpos 0.177 ypos 0.33
    if met_kathleen == False and unread_kathleen == True:
        textbutton "??? ???" action Show("profile_kathleen") xpos 0.177 ypos 0.33


    if unread_killian == True:
        textbutton "Killian Beaufort" action [Show("profile_killian"), SetVariable ("unread_killian", False)] xpos 0.177 ypos 0.36
        add "new" xpos 0.292 ypos 0.366
    else:
        textbutton "Killian Beaufort" action Show("profile_killian") xpos 0.177 ypos 0.36


    if met_lucy == True and unread_lucy == True:
        textbutton "Lucy Long" action [Show("profile_lucy"), SetVariable ("unread_lucy", False)] xpos 0.177 ypos 0.39
        add "new" xpos 0.292 ypos 0.396
    if met_lucy == True and unread_lucy == False:
        textbutton "Lucy Long" action Show("profile_lucy") xpos 0.177 ypos 0.39
    if met_lucy == False and unread_lucy == True:
        textbutton "??? ???" action Show("profile_lucy") xpos 0.177 ypos 0.39


    if met_mina == True and unread_mina == True:
        textbutton "Mina Harper" action [Show("profile_mina"), SetVariable("unread_mina", False)] xpos 0.177 ypos 0.42
        add "new" xpos 0.292 ypos 0.426
    if met_mina == True and unread_mina == False:
        textbutton "Mina Harper" action Show("profile_mina") xpos 0.177 ypos 0.42
    if met_mina == False and unread_mina == True:
        textbutton "??? ???" action Show("profile_mina") xpos 0.177 ypos 0.42


    if met_rosalind == True and unread_rosalind == True:
        textbutton "Rosalind Carter" action [Show("profile_rosalind"), SetVariable("unread_rosalind", False)] xpos 0.177 ypos 0.45
        add "new" xpos 0.292 ypos 0.456
    if met_rosalind == True and unread_rosalind == False:
        textbutton "Rosalind Carter" action Show("profile_rosalind") xpos 0.177 ypos 0.45
    if met_rosalind == False and unread_rosalind == True:
        textbutton "??? ???" action Show("profile_rosalind") xpos 0.177 ypos 0.45


    if met_samson == True and unread_samson == True:
        textbutton "Samson Garcia" action [Show("profile_samson"), SetVariable("unread_samson", False)] xpos 0.177 ypos 0.48
        add "new" xpos 0.292 ypos 0.486
    if met_samson == True and unread_samson == False:
        textbutton "Samson Garcia" action Show("profile_samson") xpos 0.177 ypos 0.48
    if met_samson == False and unread_samson == True:
        textbutton "??? ???" action Show("profile_samson") xpos 0.177 ypos 0.48



    if met_veronica == True and unread_veronica == True:
        textbutton "Veronica Lynch" action [Show("profile_veronica"), SetVariable ("unread_veronica", False)] xpos 0.177 ypos 0.51
        add "new" xpos 0.292 ypos 0.516
    if met_veronica == True and unread_veronica == False:
        textbutton "Veronica Lynch" action Show("profile_veronica") xpos 0.177 ypos 0.51
    if met_veronica == False and unread_veronica == True:
        textbutton "??? ???" action Show("profile_veronica") xpos 0.177 ypos 0.51


    if unread_victoria == True:
        textbutton "Victoria [mcl]" action [Show("profile_victoria"), SetVariable ("unread_victoria", False)] xpos 0.177 ypos 0.54
        add "new" xpos 0.292 ypos 0.546
    else:
        textbutton "Victoria [mcl]" action Show("profile_victoria") xpos 0.177 ypos 0.54


    if met_warren == True and unread_warren == True:
        textbutton "Warren" action [Show("profile_warren"), SetVariable ("unread_warren", False)] xpos 0.177 ypos 0.57
        add "new" xpos 0.292 ypos 0.576
    if met_warren == True and unread_warren == False:
        textbutton "Warren" action Show("profile_warren") xpos 0.177 ypos 0.57
    if met_warren == False and unread_warren == True:
        textbutton "??? ???" action Show("profile_warren") xpos 0.177 ypos 0.57


    if met_dalia == True and unread_dalia == True:
        textbutton "Dalia Rivera" action [Show("profile_dalia"), SetVariable("unread_dalia", False)] xpos 0.177 ypos 0.60
        add "new" xpos 0.292 ypos 0.606
    if met_dalia == True and unread_dalia == False:
        textbutton "Dalia Rivera" action Show("profile_dalia") xpos 0.177 ypos 0.60
    if met_dalia == False and unread_dalia == True:
        textbutton "??? ???" action Show("profile_dalia") xpos 0.177 ypos 0.60


    if met_harper == True and unread_harper == True:
        textbutton "Harper Ivanova" action [Show("profile_harper"), SetVariable("unread_harper", False)] xpos 0.177 ypos 0.63
        add "new" xpos 0.292 ypos 0.636
    if met_harper == True and unread_harper == False:
        textbutton "Harper Ivanova" action Show("profile_harper") xpos 0.177 ypos 0.63
    if met_harper == False and unread_harper == True:
        textbutton "??? ???" action Show("profile_harper") xpos 0.177 ypos 0.63


    if met_jerrica == True and unread_jerrica == True:
        textbutton "Jerrica Nash" action [Show("profile_jerrica"), SetVariable("unread_jerrica", False)] xpos 0.177 ypos 0.66
        add "new" xpos 0.292 ypos 0.666
    if met_jerrica == True and unread_jerrica == False:
        textbutton "Jerrica Nash" action Show("profile_jerrica") xpos 0.177 ypos 0.66
    if met_jerrica == False and unread_jerrica == True:
        textbutton "??? ???" action Show("profile_jerrica") xpos 0.177 ypos 0.66


    if met_spider == True and unread_spider == True:
        textbutton "Spider" action [Show("profile_spider"), SetVariable("unread_spider", False)] xpos 0.177 ypos 0.69
        add "new" xpos 0.292 ypos 0.696
    if met_spider == True and unread_spider == False:
        textbutton "Spider" action Show("profile_spider") xpos 0.177 ypos 0.69
    if met_spider == False and unread_spider == True:
        textbutton "??? ???" action Show("profile_spider") xpos 0.177 ypos 0.69


    if met_grace == True and unread_grace == True:
        textbutton "Grace Beaufort" action [Show("profile_grace"), SetVariable("unread_grace", False)] xpos 0.177 ypos 0.72
        add "new" xpos 0.292 ypos 0.726
    if met_grace == True and unread_grace == False:
        textbutton "Grace Beaufort" action Show("profile_grace") xpos 0.177 ypos 0.72
    if met_grace == False and unread_grace == True:
        textbutton "??? ???" action Show("profile_grace") xpos 0.177 ypos 0.72


    if met_abel == True and unread_abel == True:
        textbutton "Abel van Doren" action [Show("profile_abel"), SetVariable("unread_abel", False)] xpos 0.177 ypos 0.75
        add "new" xpos 0.292 ypos 0.756
    if met_abel == True and unread_abel == False:
        textbutton "Abel van Doren" action Show("profile_abel") xpos 0.177 ypos 0.75
    if met_abel == False and unread_abel == True:
        textbutton "??? ???" action Show("profile_abel") xpos 0.177 ypos 0.75


    if met_sophia == True and unread_sophia == True:
        textbutton "Sophia Lundgren" action [Show("profile_sophia"), SetVariable("unread_sophia", False)] xpos 0.177 ypos 0.78
        add "new" xpos 0.292 ypos 0.786
    if met_sophia == True and unread_sophia == False:
        textbutton "Sophia Lundgren" action Show("profile_sophia") xpos 0.177 ypos 0.78
    if met_sophia == False and unread_sophia == True:
        textbutton "??? ???" action Show("profile_sophia") xpos 0.177 ypos 0.78





init -501 screen profile_august():
    tag profile_screen
    if met_august == True:
        add "gui/screens/backgrounds/profile_august.png"
        fixed xmaximum 930:
            xpos 680
            ypos 690
            text "[history_august]"
    else:
        add "gui/screens/backgrounds/profile_august_unknown.png"

init -501 screen profile_chuck():
    tag profile_screen
    add "gui/screens/backgrounds/profile_chuck.png"
    fixed xmaximum 920:
        xpos 680
        ypos 690
        text "[history_chuck]"

init -501 screen profile_felicia():
    tag profile_screen

    if met_felicia == True:
        add "gui/screens/backgrounds/profile_felicia.png"
        fixed xmaximum 920:
            xpos 680
            ypos 690
            text "[history_felicia]"
    else:
        add "gui/screens/backgrounds/profile_felicia_unknown.png"


init -501 screen profile_hana():
    tag profile_screen

    if met_hana == True and hanaGF == True:
        add "gui/screens/backgrounds/profile_hana2.png"
        fixed xmaximum 920:
            xpos 680
            ypos 690
            text "[history_hana]"
    if met_hana == True and hanaGF == False:
        add "gui/screens/backgrounds/profile_hana.png"
        fixed xmaximum 920:
            xpos 680
            ypos 690
            text "[history_hana]"
    if met_hana == False and hanaGF == False:
        add "gui/screens/backgrounds/profile_hana_unknown.png"


init -501 screen profile_isaak():
    tag profile_screen

    if met_isaak == True:
        add "gui/screens/backgrounds/profile_isaak.png"
        fixed xmaximum 920:
            xpos 680
            ypos 690
            text "[history_isaak]"
    else:
        add "gui/screens/backgrounds/profile_isaak_unknown.png"

init -501 screen profile_jacob():
    tag profile_screen

    if met_jacob == True:
        add "gui/screens/backgrounds/profile_jacob.png"
        fixed xmaximum 920:
            xpos 680
            ypos 690
            text "[history_jacob]"
    else:
        add "gui/screens/backgrounds/profile_jacob_unknown.png"

init -501 screen profile_kathleen():
    tag profile_screen

    if met_kathleen == True:
        add "gui/screens/backgrounds/profile_kathleen.png"
        fixed xmaximum 920:
            xpos 680
            ypos 690
            text "[history_kathleen]"
    else:
        add "gui/screens/backgrounds/profile_kathleen_unknown.png"


init -501 screen profile_killian():
    tag profile_screen
    add "gui/screens/backgrounds/profile_killian.png"
    fixed xmaximum 920:
        xpos 680
        ypos 690
        text "[history_killian]"


init -501 screen profile_lucy():
    tag profile_screen

    if met_lucy == True and lucyProstitute == True:
        add "gui/screens/backgrounds/profile_lucy2.png"
        fixed xmaximum 920:
            xpos 680
            ypos 690
            text "[history_lucy]"

    if met_lucy == True and lucyProstitute == False:
        add "gui/screens/backgrounds/profile_lucy.png"
        fixed xmaximum 920:
            xpos 680
            ypos 690
            text "[history_lucy]"
    if met_lucy == False and lucyProstitute == False:
        add "gui/screens/backgrounds/profile_lucy_unknown.png"

init -501 screen profile_mina():
    tag profile_screen

    if met_mina == True:
        add "gui/screens/backgrounds/profile_mina.png"
        fixed xmaximum 920:
            xpos 680
            ypos 690
            text "[history_mina]"
    else:
        add "gui/screens/backgrounds/profile_mina_unknown.png"

init -501 screen profile_rosalind():
    tag profile_screen

    if met_rosalind == True:
        add "gui/screens/backgrounds/profile_rosalind.png"
        fixed xmaximum 920:
            xpos 680
            ypos 690
            text "[history_rosalind]"
    else:
        add "gui/screens/backgrounds/profile_rosalind_unknown.png"

init -501 screen profile_samson():
    tag profile_screen

    if met_samson == True:
        add "gui/screens/backgrounds/profile_samson.png"
        fixed xmaximum 920:
            xpos 680
            ypos 690
            text "[history_samson]"
    else:
        add "gui/screens/backgrounds/profile_samson_unknown.png"

init -501 screen profile_veronica():
    tag profile_screen

    if met_veronica == True:
        add "gui/screens/backgrounds/profile_veronica.png"
        fixed xmaximum 920:
            xpos 680
            ypos 690
            text "[history_veronica]"
    else:
        add "gui/screens/backgrounds/profile_veronica_unknown.png"

init -501 screen profile_victoria():
    tag profile_screen
    add "gui/screens/backgrounds/profile_victoria.png"
    fixed xmaximum 920:
        xpos 680
        ypos 690
        text "[history_victoria]"

init -501 screen profile_warren():
    tag profile_screen

    if met_warren == True:
        add "gui/screens/backgrounds/profile_warren.png"
        fixed xmaximum 920:
            xpos 680
            ypos 690
            text "[history_warren]"
    else:
        add "gui/screens/backgrounds/profile_warren_unknown.png"

init -501 screen profile_spider():
    tag profile_screen

    if met_spider == True:
        add "gui/screens/backgrounds/profile_spider.png"
        fixed xmaximum 920:
            xpos 680
            ypos 690
            text "[history_spider]"
    else:
        add "gui/screens/backgrounds/profile_spider_unknown.png"

init -501 screen profile_dalia():
    tag profile_screen

    if met_dalia == True:
        add "gui/screens/backgrounds/profile_dalia.png"
        fixed xmaximum 920:
            xpos 680
            ypos 690
            text "[history_dalia]"
    else:
        add "gui/screens/backgrounds/profile_dalia_unknown.png"

init -501 screen profile_harper():
    tag profile_screen

    if met_harper == True:
        add "gui/screens/backgrounds/profile_harper.png"
        fixed xmaximum 920:
            xpos 680
            ypos 690
            text "[history_harper]"
    else:
        add "gui/screens/backgrounds/profile_harper_unknown.png"

init -501 screen profile_jerrica():
    tag profile_screen

    if met_jerrica == True:
        add "gui/screens/backgrounds/profile_jerrica.png"
        fixed xmaximum 920:
            xpos 680
            ypos 690
            text "[history_jerrica]"
    else:
        add "gui/screens/backgrounds/profile_jerrica_unknown.png"

init -501 screen profile_grace():
    tag profile_screen

    if met_grace == True:
        add "gui/screens/backgrounds/profile_grace.png"
        fixed xmaximum 920:
            xpos 680
            ypos 690
            text "[history_grace]"
    else:
        add "gui/screens/backgrounds/profile_grace_unknown.png"

init -501 screen profile_abel():
    tag profile_screen

    if met_abel == True:
        add "gui/screens/backgrounds/profile_abel.png"
        fixed xmaximum 920:
            xpos 680
            ypos 690
            text "[history_abel]"
    else:
        add "gui/screens/backgrounds/profile_abel_unknown.png"

init -501 screen profile_sophia():
    tag profile_screen

    if met_sophia == True:
        add "gui/screens/backgrounds/profile_sophia.png"
        fixed xmaximum 920:
            xpos 680
            ypos 690
            text "[history_sophia]"
    else:
        add "gui/screens/backgrounds/profile_sophia_unknown.png"

init -501 screen credits():
    tag menu
    modal True

    add "screen"


    imagemap:

        idle "gui/screens/imagemaps/credits_idle.png"
        hover "gui/screens/imagemaps/credits_hover.png"
        ground "gui/screens/backgrounds/credits.png"


        hotspot (10, 50, 100, 100) action [ Play ("menu_click","sound effects/page-turn.wav") ], [Return()]

    viewport id "creds":
        area (100,200,1750,850)
        scrollbars "vertical"
        mousewheel True
        draggable True

        has vbox
        fixed xmaximum 1500:
            text "Thanks to everyone who reads our game, but a special thanks to the following club owners: \n\nMasterSav \nRodney \nMETDeath \nsauron93 \nSen \nShdwB \nMerky \nStone Forest\nnotVVLX\nJibXorz\n...and the many more unnamed. Please contact us on our discord or on Patreon to be added."


init -501 screen thanksforplaying():
    modal True
    add "gui/screens/backgrounds/thanks.png"
    textbutton "Save Game" action [ Play ("menu_click","sound effects/page-turn.wav"), ShowMenu('save')] xpos 0.51 ypos 0.4
    textbutton "Load Game" action [ Play ("menu_click","sound effects/page-turn.wav"), ShowMenu('load')] xpos 0.51 ypos 0.43
    textbutton "Return to Main Menu" action MainMenu() xpos 0.51 ypos 0.46
    textbutton "Support Us on Patreon" action OpenURL("https://www.patreon.com/GIL3D") xpos 0.51 ypos 0.49
    textbutton "Exit Game" action Quit(confirm=False) xpos 0.51 ypos 0.52

init -501 screen camcorder():
    add "camcorder"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
