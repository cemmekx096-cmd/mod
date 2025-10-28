init offset = -1










style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.webp", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.webp", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.webp", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.webp", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.webp"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.webp", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.webp"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.webp", gui.frame_borders, tile=gui.frame_tile)





















screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    if who != None:

        use hide_icon

        if not _in_replay:
            if MenuLI_interface == True:
                use LI_menu
            if phone_interface == True:
                use ouverture_phone_interface
        add SideImage()


    if not _in_replay and not config.version in version_ajour:
        use updateSave

    if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
        if what:
            textbutton _('Copier dans le presse papier') style 'quick_button' action Function(scrubs, what) at right


init python:
    config.character_id_prefixes.append('namebox')





style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label



style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.webp", xalign=0.5, yalign=1.0)

style namebox:

    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.webp", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

style say_dialogue_nvl:
    properties gui.text_properties("dialogue")

    font "SF-Pro-Display-Thin.otf"

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos












screen input(prompt):
    style_prefix "input"

    window:

        has vbox
        xalign gui.dialogue_text_xalign
        xpos gui.dialogue_xpos
        xsize gui.dialogue_width
        ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width



















screen choice(items):
    style_prefix "choice"
    vbox:
        if items[0].caption.startswith("^A^"):
            yalign 1.0
        for i in items:
            $ scaption = i.caption.replace("*", "")
            for a in listeIconChoicesAEffacer:
                $ scaption = scaption.replace(a, "")
            hbox:
                frame:
                    xysize (300, 120)
                    background None
                textbutton scaption:
                    if "*" in i.caption:
                        text_color "#7daeff"
                        text_hover_color "#f63440"

                    text_xoffset 0
                    if not i.caption.endswith("(WIP)"):
                        action i.action
                    at choice_zoom
                hbox:
                    xsize 270
                    xoffset -60
                    yoffset -35
                    spacing -10

                    for b in listeIconChoicesFichier:
                        if b in i.caption:
                            frame:
                                yoffset -5
                                xalign 0.0
                                xysize (130, 130)
                                background None
                                add Frame("gui/choices/"+ b.replace("|", "", 2) + ".webp")

                hbox:
                    xsize 270
                    xoffset -60
                    yoffset -35
                    spacing -10

                    for c in listeIconChoicesAdd:
                        if c in i.caption:
                            frame:
                                yoffset 27
                                xoffset -355
                                xysize (129, 110)
                                background None
                                at LI_zoom
                                add Frame("gui/choices/"+ c.replace("|", "", 2) + ".webp")

transform choice_zoom:
    zoom 0.9

transform LI_zoom:
    zoom 0.65



define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 550
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")







screen quick_menu():


    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.0

            textbutton _("Hide") action HideInterface()
            textbutton _("Retour") action Rollback()
            textbutton _("Avance rapide") action Skip() alternate Skip(fast=True, confirm=True)

            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Sauvegarde") action ShowMenu('save')
            textbutton _("Charger") action ShowMenu('load')




init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")






































screen navigation():

    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        yoffset -80
        spacing gui.navigation_spacing

        if main_menu:
            hbox:

                imagebutton:
                    at icone_start
                    xpos 0
                    ypos 0
                    idle "gui/choixJASON_idle.png"
                    hover "gui/choixJASON_hover.png"
                    action Show("startJASON")
                null:
                    width 15
                imagebutton:
                    at icone_start
                    xpos 0
                    ypos 0
                    idle "gui/choixGHD_idle.png"
                    hover "gui/choixGHD_hover.png"
                    insensitive "gui/choixGHD_insensitive.png"
                    sensitive persistent.unlockGHD
                    action Show("startGHD")
                null:
                    width 15
                imagebutton:
                    at icone_start
                    xpos 0
                    ypos 0
                    idle "gui/choixONESHOT_idle.png"
                    hover "gui/choixONESHOT_hover.png"
                    insensitive "gui/choixONESHOT_insensitive.png"
                    sensitive persistent.unlockOneShot
                    action Show("startONESHOT")

            null:
                height 10

            textbutton _ ("Continuer"):
                text_yoffset gui.navigation_text_yoffset
                style "newButton"
                text_style "newButton"
                action FileLoad (1, confirm = False, page = "auto", newest = True)

        else:
            if not _in_replay:
                textbutton _("{size=45}Sauvegarder{/size}"):
                    text_yoffset gui.navigation_text_yoffset
                    style "newButton"
                    text_style "newButton"
                    action ShowMenu("save")
        if not _in_replay:
            textbutton _("Charger"):
                text_yoffset gui.navigation_text_yoffset
                style "newButton"
                text_style "newButton"
                action ShowMenu("load")

        if _in_replay:
            textbutton _("Fin de la diffusion"):
                text_yoffset gui.navigation_text_yoffset
                style "newButton"
                text_style "newButton"
                action EndReplay(confirm=True)

        if not _in_replay and main_menu:
            textbutton "Extras":
                text_yoffset gui.navigation_text_yoffset
                style "newButton"
                text_style "newButton"
                action ShowMenu("extras")

        textbutton _("{size=38}Quitter{/size}"):
            text_yoffset gui.navigation_text_yoffset
            style "newButton"
            text_style "newButton"
            action Quit(False)

        hbox:
            imagebutton:
                padding gui.navigation_padding
                background gui.navigation_background
                xpos 5
                ypos 12
                if persistent.lang == "french":
                    idle "gui/button/param_FR_idle.webp"
                    hover "gui/button/param_FR_hover.webp"
                if persistent.lang == "english":
                    idle "gui/button/param_UK_idle.webp"
                    hover "gui/button/param_UK_hover.webp"
                if persistent.lang == "id":
                    idle "gui/button/param_UK_idle.webp"
                    hover "gui/button/param_UK_hover.webp"
                if persistent.lang == "german":
                    idle "gui/button/param_DE_idle.webp"
                    hover "gui/button/param_DE_hover.webp"
                if persistent.lang == "italian":
                    idle "gui/button/param_IT_idle.webp"
                    hover "gui/button/param_IT_hover.webp"
                if persistent.lang == "spanish":
                    idle "gui/button/param_ES_idle.webp"
                    hover "gui/button/param_ES_hover.webp"
                if persistent.lang == "portuguese":
                    idle "gui/button/param_PO_idle.webp"
                    hover "gui/button/param_PO_hover.webp"
                if persistent.lang == "russian":
                    idle "gui/button/param_RU_idle.webp"
                    hover "gui/button/param_RU_hover.webp"
                action ShowMenu("preferences")

            null:
                width 10

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                imagebutton:
                    padding gui.navigation_padding
                    background gui.navigation_background
                    xpos 5
                    ypos 12
                    idle "gui/button/aide_idle.webp"
                    hover "gui/button/aide_hover.webp"
                    action ShowMenu("help")

            null:
                width 50

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                textbutton _("Code"):
                    yoffset 12
                    text_yoffset gui.navigation_text_yoffset
                    style "newButton"
                    text_style "newButton"
                    action ShowMenu("enterCode")
            else:
                textbutton _("Code"):
                    xoffset -45
                    yoffset 12
                    text_yoffset gui.navigation_text_yoffset
                    style "newButton"
                    text_style "newButton"
                    action ShowMenu("enterCode")


    if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
        imagebutton:
            xpos 88
            ypos 740
            idle "gui/button/subscribe_idle.webp"
            hover "gui/button/subscribe_hover.webp"
            action OpenURL('https://subscribestar.adult/coeurdecochon')
        imagebutton:
            xpos 70
            ypos 900
            idle "gui/button/Patreon_idle.webp"
            hover "gui/button/Patreon_hover.webp"
            action OpenURL('https://www.patreon.com/coeur2cochon')
        imagebutton:
            xpos 300
            ypos 907
            idle "gui/button/discord_idle.webp"
            hover "gui/button/discord_hover.webp"
            action OpenURL('https://discord.gg/QFRWH7FFb8')
        imagebutton:
            focus_mask True
            xpos 0
            yoffset -25
            idle "gui/button/WallOfFame_idle.webp"
            hover "gui/button/WallOfFame_hover.webp"
            action ShowMenu("WallOfFame")
    else:
        imagebutton:
            xpos 88
            ypos 740
            idle "gui/button/subscribe_idle.webp"
            hover "gui/button/subscribe_hover.webp"
            action OpenURL('https://subscribestar.adult/coeurdecochon')
        imagebutton:
            xpos 70
            ypos 900
            idle "gui/button/Patreon_idle.webp"
            hover "gui/button/Patreon_hover.webp"
            action OpenURL('https://www.patreon.com/coeur2cochon')
        imagebutton:
            xpos 300
            ypos 907
            idle "gui/button/discord_idle.webp"
            hover "gui/button/discord_hover.webp"
            action OpenURL('https://discord.gg/QFRWH7FFb8')
        imagebutton:
            focus_mask True
            xpos 0
            yoffset -25
            idle "gui/button/WallOfFame_idle.webp"
            hover "gui/button/WallOfFame_hover.webp"
            action ShowMenu("WallOfFame")



transform miniSanta:
    zoom 0.38
transform icone_start:
    zoom 0.15
transform icone_return:
    zoom 0.15
    xpos 0.17
    ypos 0.272
    yoffset 20
transform icone_return_jeu:
    zoom 0.15
    xpos 0.17
    ypos 0.1
    yoffset 20
transform icone_return_mobile:
    zoom 0.15
    xpos 0.17
    ypos 0.279
    yoffset 12

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


































screen extras():
    tag menu


    use game_menu(_("{size=33}Extras{/size}")):

        style_prefix "extras"

        vbox:
            yoffset 111
            spacing gui.navigation_spacing
            textbutton _("Galerie"):
                text_yoffset gui.navigation_text_yoffset
                style "newButton"
                text_style "newButton"
                action ShowMenu("gallery")
            textbutton "Replay":
                text_yoffset gui.navigation_text_yoffset
                style "newButton"
                text_style "newButton"
                action ShowMenu("replay")
            textbutton _("Succès"):
                text_yoffset gui.navigation_text_yoffset
                style "newButton"
                text_style "newButton"
                action ShowMenu("achievements")


    if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
        if main_menu:
            imagebutton:
                at icone_return
                idle "gui/returnJASON_idle.png"
                hover "gui/returnJASON_hover.png"
                action Return()
        else:
            if _in_replay:
                imagebutton:
                    at icone_return
                    yoffset -150
                    idle "gui/returnJASON_idle.png"
                    hover "gui/returnJASON_hover.png"
                    action Return()
            else:
                imagebutton:
                    at icone_return
                    yoffset -150
                    idle "gui/returnJASON_idle.png"
                    hover "gui/returnJASON_hover.png"
                    action Return()
    else:
        if main_menu:
            imagebutton:
                at icone_return_mobile

                idle "gui/returnJASON_idle.png"
                hover "gui/returnJASON_hover.png"
                action Return()
        else:
            imagebutton:
                at icone_return_mobile
                yoffset -140
                idle "gui/returnJASON_idle.png"
                hover "gui/returnJASON_hover.png"
                action Return()

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")









screen main_menu():
    tag menu



    style_prefix "main_menu"


    add "main_menu_dynamique"



    frame





    use navigation

    if gui.show_name:

        vbox:
            xoffset -50
            yoffset -38

            text _("Renaissance"):
                if lang == "russian":
                    font "AmaticSC-Regular.ttf"
                    size 50
                    yoffset -20
                else:
                    font "ShadowsIntoLight-Regular.ttf"
                    size 40
                    yoffset 0
                    xoffset 0
                xalign 1.0
                yalign 1.0
                color "#870500"

            text "[config.version]":
                style "main_menu_version"
                font "Anton-Regular.ttf"
                xoffset -40
                yoffset 10
                color "#bcbcbc"

    frame:
        background "gui/LI_personnages/1px.webp"
        xsize 1920
        ysize 1080

        text _("JASON"):
            xalign 1.0
            xoffset -35
            yalign 1.0
            yoffset -170
            size 200
            color "#ffffff"
            font "Anton-Regular.ttf"

        text _("Coming of age :"):
            if lang == "russian":
                font "AmaticSC-Bold.ttf"
                size 60
                yoffset -155
            else:
                font "ShadowsIntoLight-Regular.ttf"
                size 65
                yoffset -140
            xalign 1.0
            xoffset -35
            yalign 1.0
            color "#ffffff"

        text _("Episode 2"):
            if lang == "russian":
                font "AmaticSC-Regular.ttf"
                size 50
            else:
                size 40
                font "Anton-Regular.ttf"
            color "#ffffff"
            xalign 1.0
            yalign 1.0
            xoffset -35
            yoffset -415





        if persistent.interdit >= 1:
            frame:
                yoffset -5
                xoffset -5
                xysize (80, 70)
                background None

                xalign 1.0
                yalign 1.0

                if persistent.interdit == 2:
                    add Frame("gui/logo_free_VALID.png")
                else:
                    add Frame("gui/logo_free_NOVALID.png")

    if 10 <= day <= 31 and month == 12 or 1 <= day <= 10 and month == 1:
        imagebutton:
            at miniSanta
            xalign 1.0
            xoffset -100
            ypos 50
            idle "gui/iconeLancementSanta_idle.png"
            hover "gui/iconeLancementSanta_hover.png"
            action SetVariable("startSANTA", True), Start()

    imagebutton:
        yoffset 0
        xoffset 0
        xalign 0.35
        yalign 0.95
        idle "gui/JASON Coming of Age on Steam.png"
        hover "gui/JASON Coming of Age on Steam.png"
        action OpenURL ("https://store.steampowered.com/app/3165830/JASON_Coming_of_Age")

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.webp"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")











screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"
    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background
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

    use navigation

    imagebutton:
        xpos 15
        ypos 65
        idle "gui/button/main_menu_idle.webp"
        hover "gui/button/main_menu_hover.webp"
        if main_menu:
            action ShowMenu("main_menu")
        else:
            action MainMenu()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.webp"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45










screen about():
    tag menu



    use game_menu(_("Extras / {size=33}À propos{/size}"), scroll="viewport"):
        style_prefix "about"
        vbox:
            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"
            text _("Conçu avec {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

    imagebutton:
        at icone_return
        idle "gui/returnJASON_idle.png"
        hover "gui/returnJASON_hover.png"
        action Return()

    if not main_menu:
        imagebutton:
            xpos 350
            ypos 0.6
            yoffset -10
            idle "gui/button/close_idle.webp"
            hover "gui/button/close_hover.webp"
            action Return()



define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size












screen save():
    tag menu

    use file_slots(_("{size=33}Sauvegarde{/size}"))
    if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
        if main_menu:
            imagebutton:
                at icone_return
                idle "gui/returnJASON_idle.png"
                hover "gui/returnJASON_hover.png"
                action Return()
        else:
            if _in_replay:
                imagebutton:
                    at icone_return
                    yoffset -150
                    idle "gui/returnJASON_idle.png"
                    hover "gui/returnJASON_hover.png"
                    action Return()
            else:
                imagebutton:
                    at icone_return
                    yoffset -150
                    idle "gui/returnJASON_idle.png"
                    hover "gui/returnJASON_hover.png"
                    action Return()
    else:
        if main_menu:
            imagebutton:
                at icone_return_mobile

                idle "gui/returnJASON_idle.png"
                hover "gui/returnJASON_hover.png"
                action Return()
        else:
            imagebutton:
                at icone_return_mobile
                yoffset -140
                idle "gui/returnJASON_idle.png"
                hover "gui/returnJASON_hover.png"
                action Return()

screen load():
    tag menu

    use file_slots(_("{size=33}Charger{/size}"))
    if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
        if main_menu:
            imagebutton:
                at icone_return
                idle "gui/returnJASON_idle.png"
                hover "gui/returnJASON_hover.png"
                action Return()
        else:
            if _in_replay:
                imagebutton:
                    at icone_return
                    yoffset -150
                    idle "gui/returnJASON_idle.png"
                    hover "gui/returnJASON_hover.png"
                    action Return()
            else:
                imagebutton:
                    at icone_return
                    yoffset -150
                    idle "gui/returnJASON_idle.png"
                    hover "gui/returnJASON_hover.png"
                    action Return()
    else:
        if main_menu:
            imagebutton:
                at icone_return_mobile

                idle "gui/returnJASON_idle.png"
                hover "gui/returnJASON_hover.png"
                action Return()
        else:
            imagebutton:
                at icone_return_mobile
                yoffset -140
                idle "gui/returnJASON_idle.png"
                hover "gui/returnJASON_hover.png"
                action Return()


screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Sauvegardes automatiques"), quick=_("Sauvegardes rapides"))
    use game_menu(title):
        frame:
            style "empty"
            style_prefix "check"
            xsize 300
            xalign 0
            xpos -405
            ypos -80

            if persistent.save_naming:
                textbutton _("{size=20}Nommage des sauvegardes activé{/size}"):
                    xoffset -80
                    action ToggleField(persistent,"save_naming")
            else:
                textbutton _("{size=20}Nommage des sauvegarde désactivé{/size}"):
                    xoffset -80
                    action ToggleField(persistent,"save_naming")

        fixed:


            order_reverse True

            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()
                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.4
                spacing gui.slot_spacing
                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    if FileNewest(slot):
                        button:
                            if renpy.current_screen().screen_name[0] == "load":
                                action FileAction(slot)
                            else:

                                selected (str(persistent._file_page) + "-" + str(slot) == renpy.newest_slot("[0-9]"))
                                if persistent.save_naming:
                                    action SetVariable("save_name", FileSaveName(slot)), Show("screen_save_name", slot=slot)
                                else:
                                    action SetVariable("save_name", FileSaveName(slot)), FileAction(slot)
                            vbox:
                                add FileScreenshot(slot) xalign 0.5
                                null:
                                    height 15
                                text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                    style "slot_time_text"
                                text FileSaveName(slot):
                                    style "slot_name_text"
                                text _("Dernière sauvegarde"):
                                    yalign 0
                                    yoffset 0
                                    xalign 0.5
                                    size 22
                                    color "#f63440"
                                key "save_delete" action FileDelete(slot)
                    else:
                        button:
                            if renpy.current_screen().screen_name[0] == "load":
                                action FileAction(slot)
                            else:

                                selected (str(persistent._file_page) + "-" + str(slot) == renpy.newest_slot("[0-9]"))
                                if persistent.save_naming:
                                    action SetVariable("save_name", FileSaveName(slot)), Show("screen_save_name", slot=slot)
                                else:
                                    action SetVariable("save_name", FileSaveName(slot)), FileAction(slot)
                            vbox:
                                add FileScreenshot(slot) xalign 0.5
                                null:
                                    height 15
                                text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                    style "slot_time_text"
                                text FileSaveName(slot):
                                    style "slot_name_text"
                                key "save_delete" action FileDelete(slot)





            hbox:
                style_prefix "page"
                ypos 0.96
                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing
                textbutton _("<") action FilePagePrevious()
                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")
                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                for page in range(1, 16):
                    textbutton "[page]" action FilePage(page)
                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")



style extra_text:
    size 20
    xalign 0.5
    yalign 1.0
    yoffset 50
    color '#b2bccc'
    hover_color '#f63440'
    font "corbel.ttf"

style extra_button:
    xsize 396
    ysize 227
    hover_background "gui/button/slot_hover_background.webp"

style newButton:
    color gui.idle_color
    hover_color gui.hover_color
    font "corbel.ttf"


    right_padding gui.navigation_right_padding
    left_padding gui.navigation_left_padding
    padding gui.navigation_padding
    background gui.navigation_background








screen preferences():
    tag menu
    use game_menu(_("{size=33}Préférences{/size}"), scroll="viewport"):
        vbox:
            hbox:
                box_wrap True
                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Affichage")
                        textbutton _("Fenêtre") action Preference("display", "window")
                        textbutton _("Plein écran") action Preference("display", "fullscreen")
                vbox:
                    style_prefix "radio"
                    label _("Rembobinage côté")
                    textbutton _("Désactivé") action Preference("rollback side", "disable")
                    textbutton _("Gauche") action Preference("rollback side", "left")
                    textbutton _("Droite") action Preference("rollback side", "right")
                vbox:
                    style_prefix "check"
                    label _("Avance rapide")
                    textbutton _("Texte non lu") action Preference("skip", "toggle")
                    textbutton _("Après les choix") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                vbox:
                    style_prefix "radio"
                    label _("Langage")
                    textbutton _("Français") action [Language(None), SetVariable("persistent.lang", "french")]
                    textbutton _("Anglais") action [Language("English"), SetVariable("persistent.lang", "english")]
                    textbutton _("Indonesia") action [Language("id"), SetVariable("persistent.lang", "id")]
                    textbutton _("Allemand") action [Language("German"), SetVariable("persistent.lang", "german")]
                    textbutton _("Italien") action [Language("Italian"), SetVariable("persistent.lang", "italian")]

                    textbutton _("Russe") action [Language("russian"), SetVariable("persistent.lang", "russian")]


            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True
                vbox:
                    label _("Vitesse du texte")
                    bar value Preference("text speed")
                    label _("Avance automatique")
                    bar value Preference("auto-forward time")
                vbox:
                    if config.has_music:
                        label _("Volume de la musique")
                        hbox:
                            bar value Preference("music volume")
                    if config.has_sound:
                        label _("Volume des sons")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)
                    if config.has_voice:
                        label _("Volume des voix")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)
                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        textbutton _("Couper tous les sons"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
            hbox:
                style_prefix "slider"
                box_wrap True
                vbox:
                    $ percent_value = int(persistent.textbox_pensee_opacity * 100)
                    label _("Opacité de la Textbox pensée ([percent_value]%)")
                    bar:
                        value FieldValue(persistent, "textbox_pensee_opacity", range=1.0, style="slider")
                    textbutton _("Default") action InvertSelected(SetVariable("persistent.textbox_pensee_opacity", 1.0))


    if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
        if main_menu:
            imagebutton:
                at icone_return
                idle "gui/returnJASON_idle.png"
                hover "gui/returnJASON_hover.png"
                action Return()
        else:
            if _in_replay:
                imagebutton:
                    at icone_return
                    yoffset -150
                    idle "gui/returnJASON_idle.png"
                    hover "gui/returnJASON_hover.png"
                    action Return()
            else:
                imagebutton:
                    at icone_return
                    yoffset -150
                    idle "gui/returnJASON_idle.png"
                    hover "gui/returnJASON_hover.png"
                    action Return()
    else:
        if main_menu:
            imagebutton:
                at icone_return_mobile

                idle "gui/returnJASON_idle.png"
                hover "gui/returnJASON_hover.png"
                action Return()
        else:
            imagebutton:
                at icone_return_mobile
                yoffset -140
                idle "gui/returnJASON_idle.png"
                hover "gui/returnJASON_hover.png"
                action Return()

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.webp"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.webp"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675










screen history():
    tag menu




    predict False

    use game_menu(_("{size=33}Historique{/size}"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

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
            label _("L'historique des dialogues est vide.")




define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5








screen help():
    tag menu


    default device = "keyboard"

    use game_menu(_("{size=33}Aide{/size}"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:
                textbutton _("Clavier") action SetScreenVariable("device", "keyboard")
                textbutton _("Souris") action SetScreenVariable("device", "mouse")
                textbutton _("À propos") action ShowMenu("about")

                if GamepadExists():
                    textbutton _("Manette") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help

    if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
        if main_menu:
            imagebutton:
                at icone_return
                idle "gui/returnJASON_idle.png"
                hover "gui/returnJASON_hover.png"
                action Return()
        else:
            if _in_replay:
                imagebutton:
                    at icone_return
                    yoffset -150
                    idle "gui/returnJASON_idle.png"
                    hover "gui/returnJASON_hover.png"
                    action Return()
            else:
                imagebutton:
                    at icone_return
                    yoffset -150
                    idle "gui/returnJASON_idle.png"
                    hover "gui/returnJASON_hover.png"
                    action Return()
    else:
        if main_menu:
            imagebutton:
                at icone_return_mobile

                idle "gui/returnJASON_idle.png"
                hover "gui/returnJASON_hover.png"
                action Return()
        else:
            imagebutton:
                at icone_return_mobile
                yoffset -140
                idle "gui/returnJASON_idle.png"
                hover "gui/returnJASON_hover.png"
                action Return()



screen keyboard_help():

    hbox:
        label _("Entrée")
        text _("Avance dans les dialogues et active l’interface (effectue un choix).")

    hbox:
        label _("Espace")
        text _("Avance dans les dialogues sans effectuer de choix.")

    hbox:
        label _("Flèches directionnelles")
        text _("Permet de se déplacer dans l’interface.")

    hbox:
        label _("Echap.")
        text _("Ouvre le menu du jeu.")

    hbox:
        label _("Ctrl")
        text _("Fait défiler les dialogues tant que la touche est pressée.")

    hbox:
        label _("Tab")
        text _("Active ou désactives les «sauts des dialogues».")

    hbox:
        label _("Page Haut")
        text _("Retourne au précédent dialogue.")

    hbox:
        label _("Page Bas")
        text _("Avance jusqu'au prochain dialogue.")

    hbox:
        label "H"
        text _("Cache l’interface utilisateur.")

    hbox:
        label "S"
        text _("Prend une capture d’écran.")

    hbox:
        label "V"
        text _("Active la {a=https://www.renpy.org/l/voicing}{size=24}vocalisation automatique{/size}{/a}.")


screen mouse_help():

    hbox:
        label _("Bouton gauche")
        text _("Avance dans les dialogues et active l’interface (effectue un choix).")

    hbox:
        label _("Bouton central")
        text _("Cache l’interface utilisateur.")

    hbox:
        label _("Bouton droit")
        text _("Ouvre le menu du jeu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Retourne au précédent dialogue.")

    hbox:
        label _("Molette vers le bas")
        text _("Avance jusqu'au prochain dialogue.")


screen gamepad_help():

    hbox:
        label _("Bouton R1\nA/Bouton du bas")
        text _("Avance dans les dialogues et active l’interface (effectue un choix).")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Retourne au précédent dialogue.")

    hbox:
        label _("Bouton R1")
        text _("Avance jusqu'au prochain dialogue.")


    hbox:
        label _("Boutons directionnels, stick gauche")
        text _("Permet de se déplacer dans l’interface.")

    hbox:
        label _("Start, Guide")
        text _("Ouvre le menu du jeu.")

    hbox:
        label _("Y/Bouton du haut")
        text _("Cache l’interface utilisateur.")

    textbutton _("Calibrage") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0















screen confirm(message, yes_action, no_action):



    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.webp"

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

            textbutton _("Oui") action yes_action
            textbutton _("Non") action no_action



    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.webp", "gui/frame.webp"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox
        spacing 9

        text _("Avance rapide")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"




transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.webp", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:


    font "DejaVuSans.ttf"















screen notify(message):


    zorder 100

    if isinstance(message, list):

        if "justLI" in message[1] or "unlockLI" in message[1] or "journal" in message[1]:

            frame:

                style_prefix message[1]
                at notify_appear

                has hbox

                if "justLI" in message[1]:


                    $ count = -1
                    for q in AllLI:
                        $ count +=1
                        if q.isKnow:

                            if renpy.substitute(q.display_name, scope = None , translate = True) in message[0]:
                                textbutton message[0]:
                                    text_style "justLI_text"
                                    action Function(SetNew, Value=False, InDex=count), SetVariable("LI_name", q.name), SetVariable("ElementIndex", count),SetVariable("info_groupe", "LI"), Function(renpy.restart_interaction), ShowMenu("LI_profils")

                elif "unlockLI" in message[1]:

                    if renpy.substitute(pl.name, scope = None , translate = True) in message[0]:
                        textbutton message[0]:
                            text_style "unlockLI_text"
                            action Function(SetNewPl, Value=False), SetVariable("LI_name", "Player"), Function(renpy.restart_interaction), ShowMenu("LI_profils")

                    else:

                        $ count = -1
                        for q in AllLI:
                            $ count +=1
                            if q.isKnow:

                                if renpy.substitute(q.display_name, scope = None , translate = True) in message[0]:
                                    textbutton message[0]:
                                        text_style "unlockLI_text"
                                        action Function(SetNew, Value=False, InDex=count), SetVariable("LI_name", q.name), SetVariable("ElementIndex", count), Function(renpy.restart_interaction), ShowMenu("LI_profils")

                elif "journal" in message[1]:

                    if renpy.substitute(pl.name, scope = None , translate = True) in message[0]:
                        textbutton message[0]:
                            text_style "journal_text"
                            action Function(SetNewPl, Value=False), SetVariable("LI_name", "Player"), Function(renpy.restart_interaction), ShowMenu("LI_profils")

                    else:
                        $ count = -1
                        for q in AllLI:
                            $ count +=1
                            if q.isKnow:

                                if renpy.substitute(q.display_name, scope = None , translate = True) in message[0]:
                                    textbutton message[0]:
                                        text_style "journal_text"
                                        action Function(SetNew, Value=False, InDex=count), SetVariable("LI_name", q.name), SetVariable("ElementIndex", count), Function(renpy.restart_interaction), ShowMenu("LI_profils")

            timer 5 action Hide('notify')

        elif "new_phone_message" in message[1]:

            $ count = -1
            for q in AllLI:
                $ count +=1
                if q.isKnow:


                    if renpy.substitute(q.display_name, scope = None , translate = True) in message[0]:

                        button:

                            at new_phone_message


                            background Frame("gui/phone_jeu/new_phone_message.webp",23,23,23,23)
                            padding (20,20,20,20)

                            action [Function(SetNew, Value=False, InDex=count), SetVariable("LI_name", q.name), SetVariable("ElementIndex", count),
                                    SetVariable("ecran_affiche", "Messages"),
                                    SetVariable("datePhoneHeure", (dateJeu + timedelta(seconds=int(renpy.get_game_runtime()))).strftime("%I:%M %p" if persistent.lang == "english" else "%H:%M")),
                                    SetVariable("datePhoneJour", (dateJeu + timedelta(seconds=int(renpy.get_game_runtime()))).strftime("%A, %B %#d, %Y").capitalize() if persistent.lang == "english" else dateJeu.strftime("%A %#d %B %Y").capitalize()),
                                    ShowMenu("Phone"),
                                    Function(renpy.restart_interaction)
                                    ]

                            has hbox
                            xmaximum 300
                            xsize 250

                            vbox:

                                hbox:
                                    add "gui/phone_jeu/message_icon_new_phone_message.webp":
                                        zoom 0.3
                                    null:
                                        width 10
                                    text _("MESSAGES"):
                                        ycenter 0.5
                                        yoffset 2
                                        size 23
                                        font "SF-Pro-Display-Light.otf"
                                        color "#393a4c"

                                null:
                                    height 12

                                text message[0]:
                                    size 25
                                    bold True
                                    font "SF-Pro-Display-Light.otf"
                                    color "#393a4c"

                                null:
                                    height 6


                                text q.last_message:
                                    size 23
                                    font "SF-Pro-Display-Light.otf"
                                    color "#393a4c"

                                null:
                                    height 6

                            text "Now":
                                xpos 1.0
                                ypos 0
                                xanchor 1.0

                                size 20
                                font "SF-Pro-Display-Light.otf"
                                color "#393a4c"

            timer 7 action Hide('notify')


        elif "music" in message[1]:

            frame:
                style_prefix message[1]
                at notify_appear
                has hbox
                textbutton message[0]:
                    text_style "justLI_text"

            timer 5 action Hide('notify')


        elif "unlock" in message[1]:

            frame:
                style_prefix message[1]
                at notify_appear
                has hbox
                textbutton message[0]:
                    text_style "justLI_text"

            timer 5 action Hide('notify')


        elif "notify" in message[1]:

            frame:
                style_prefix message[1]
                at notify_appear
                has hbox
                textbutton message[0]:
                    text_style "justLI_text"

            timer 5 action Hide('notify')


transform new_phone_message:

    xpos 20
    ypos 20
    alpha 0.0
    yoffset -50

    parallel:
        ease 0.1 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0

    on hide:
        linear 0.5 xpos -400

transform notify_appear:

    on show:
        alpha 0
        xalign -0.2
        linear 0.6 alpha 1.0 xalign 0.0
    on hide:
        linear 0.3 alpha 0.0



style justLI_frame:
    ysize 70
    ypos 40
    background Frame("gui/LI_notify.webp", Borders(150, 10, 10, 10), tile=gui.frame_tile)
    padding (120, 10, 80, 10)

style justLI_text:
    yoffset 6
    size 28
    font "corbell.ttf"




style notify_frame:
    ysize 70
    ypos 40
    background Frame("gui/notify.webp", Borders(150, 10, 10, 10), tile=gui.frame_tile)
    padding (100, 10, 80, 10)

style notify_text:
    yoffset 6
    size 28
    font "corbell.ttf"





style music_frame:
    ysize 70
    ypos 40
    background Frame("gui/music_notify.webp", Borders(150, 10, 10, 10), tile=gui.frame_tile)
    padding (100, 10, 80, 10)

style music_text:
    yoffset 6
    size 28
    font "corbell.ttf"





style unlock_frame:
    ysize 70
    ypos 40
    background Frame("gui/unlock_notify.webp", Borders(150, 10, 10, 10), tile=gui.frame_tile)
    padding (100, 10, 80, 10)

style unlock_text:
    yoffset 6
    size 28
    font "corbell.ttf"




style unlockLI_frame:
    ysize 70
    ypos 40
    background Frame("gui/unlock_notify.webp", Borders(150, 10, 10, 10), tile=gui.frame_tile)
    padding (100, 10, 80, 10)

style unlockLI_text:
    yoffset 6
    size 28
    font "corbell.ttf"



style journal_frame:
    ysize 70
    ypos 40
    background Frame("gui/journal_notify.webp", Borders(150, 10, 10, 10), tile=gui.frame_tile)
    padding (100, 10, 80, 10)

style journal_text:
    yoffset 6
    size 28
    font "corbell.ttf"














screen nvl(dialogue, items=None):

    if nvl_mode == "texto":
        use PhoneDialogue(dialogue, items)

    else:

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


screen nvl_dialogue(dialogue):

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




define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue_nvl

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.webp"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







style pref_vbox:
    variant "medium"
    xsize 450




screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.0

            textbutton _("Retour") action Rollback()
            textbutton _("Avance rapide") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/phone/textbox.webp", xalign=0.5, yalign=1.0)

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.webp"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.webp"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.webp"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.webp"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.webp"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 420

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.webp", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.webp", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.webp", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.webp", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.webp", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.webp", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.webp", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.webp"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.webp", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.webp"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900








init -2 image main_menu_dynamique:


    "splash01" with fade
    pause 30
    "splash02" with fade
    pause 15
    "splash03" with fade
    pause 15
    "splash04" with fade
    pause 15
    "splash05" with fade
    pause 15
    "splash06" with fade
    pause 15
    repeat




init:
    $ import time
    $ year, month, day, hour, minute, second, dow, doy, dst = time.localtime()


screen WallOfFame():

    add "gui/WallOfFame 04_2022.webp"
    imagebutton auto "gui/extra_exit_%s.webp" action Hide("WallOfFame", transition=fade)












default 100 persistent.save_naming = True

init -400 screen screen_save_name(slot):
    modal True
    zorder 200
    style_prefix "confirm"

    add "gui/overlay/confirm.webp"

    frame:
        has vbox
        spacing 25
        xsize 650

        if FileLoadable(slot):
            label _("Nom de la sauvegarde à {color=#f63440}écraser{/color} :") style "confirm_prompt"
        else:
            label _("Nom de la nouvelle sauvegarde :") style "confirm_prompt"

        input:
            value VariableInputValue('save_name')
            length 30
            xalign 0.5
            exclude "\\[{"

        hbox:
            xfill True
            textbutton _("Oui") action FileAction(slot, confirm=False), Hide("screen_save_name") xalign 0.5
            textbutton _("Non") action Hide("screen_save_name") xalign 0.5


    key "game_menu" action Hide("screen_save_name")


    key "K_RETURN" action FileAction(slot, confirm=False), Hide("screen_save_name")
    key "K_KP_ENTER" action FileAction(slot, confirm=False), Hide("screen_save_name")

































init 100 python:

    def verifier_code(code_input):
        
        if code_input == "taboo_v0.9":
            renpy.store.persistent.interdit = 2
            renpy.notify([_("Code correct ! Taboo patch V-i2 appliqué"), "notify"])
        elif code_input == "reset_taboo":
            renpy.store.persistent.interdit = 0
            renpy.notify([_("Code correct ! Taboo patch retiré"), "notify"])
        elif code_input == "unlock_santa_GHD":
            renpy.store.persistent.noel_s04 = True
            renpy.notify([_("Code correct ! Replay de Noël débloqué"), "notify"])
        
        else:
            renpy.notify([_("Code incorrect !"), "notify"])


default 100 code_input = ""


init -400 screen enterCode():
    modal True
    zorder 200
    style_prefix "confirm"

    add "gui/overlay/confirm.webp"

    frame:
        has vbox
        spacing 25
        xsize 650

        label _("Veuillez entrer un code") style "confirm_prompt"

        input:
            value VariableInputValue('code_input')

            length 30
            xalign 0.5
            exclude "\\[{"

        hbox:
            xfill True
            textbutton _("Ok je valide") action [
                                                Hide("enterCode"),
                                                Function(verifier_code, code_input)  
                                                    ] xalign 0.5
            textbutton _("Annuler") action Hide("enterCode") xalign 0.5





    key "game_menu" action Hide("enterCode")


    key "K_RETURN" action [Function(verifier_code, code_input), Hide("enterCode")]
    key "K_KP_ENTER" action [Function(verifier_code, code_input), Hide("enterCode")]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
