






default -1 quick_menu_stats = False

transform -1 transform_show_hide(offset, bounce_offset):
    on show:
        offset offset
        ease 0.2 offset bounce_offset
        ease 0.1 offset (0, 0)
    on hide:
        ease 0.1 offset bounce_offset
        ease 0.2 offset offset

init -501 screen quick_menu():
    zorder 100
    style_prefix "quick"

    showif quick_menu and not renpy.get_screen('chapter_title'):
        imagebutton style "gamemenu_btn" at transform_show_hide((0, 89), (0, -12)):
            yalign 1.0
            idle Frame("gui/menu_icon_idle.webp")
            hover Frame("gui/menu_icon_hover.webp")
            action Play("ch_one", "sfx/phone_up.ogg"), ShowMenu('phone')

        hbox at transform_show_hide((0, 50), (0, -10)):
            if not _in_replay:
                textbutton _("Hide") action HideInterface()
                textbutton _("Back") action Rollback()
                textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("Auto") action Preference("auto-forward", "toggle")
                textbutton _("Save") action ShowMenu('phone_save')
                textbutton _("Q.Save") action QuickSave()
                textbutton _("Q.Load") action QuickLoad()
                textbutton _("Settings") action ShowMenu('phone_settings')
                textbutton _("Stats") action ToggleVariable('quick_menu_stats')
            elif _in_replay:
                textbutton _("Hide") action HideInterface()
                textbutton _("Back") action Rollback()
                textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
                textbutton _("Auto") action Preference("auto-forward", "toggle")
                textbutton _("Settings") action ShowMenu("preferences")

        showif quick_menu_stats:
            use stats_ingame

init -1 style gamemenu_btn:
    xysize (143, 89)

init -1 style gamemenu_btn:
    variant "small"
    xysize (186, 116)



init -1 python:
    config.overlay_screens.append("quick_menu")

default -1 quick_menu = True

init -1 style quick_hbox:
    align (1.0, 1.0)
    xoffset -20

init -1 style quick_button is default:
    properties gui.button_properties("quick_button")

init -1 style quick_button_text is button_text:
    properties gui.button_text_properties("quick_button")
    outlines [(2, "#000a", 1, 1)]

init -1 style quick_button_text:
    variant "small"
    outlines [(2, "#000a", 1, 1)]




init -501 screen stats_ingame():
    style_prefix "stats_ingame"

    if ian_active:
        $ parent = 'ian'
    else:
        $ parent = 'lena'

    frame at transform_show_hide((102,0), (-14,0)):
        has vbox
        text "[%s_wits]" % parent
        text "[%s_charisma]" % parent
        text "[%s_athletics]" % parent
        text "[%s_lust]" % parent
        text "[%s_money]" % parent
        text "[%s_will]" % parent color "#E0CE39"

init -1 style stats_ingame_frame:
    background "gui/stat_popup.webp"
    xysize (102, 527)
    align (1.0, 0.6)
    top_padding 21

init -1 style stats_ingame_frame:
    variant "small"
    yalign 0.4
    top_padding 17

init -1 style stats_ingame_vbox:
    spacing 48
    xalign 1.0
    xoffset -64

init -1 style stats_ingame_vbox:
    variant "small"
    xoffset -60
    spacing 42

init -1 style stats_ingame_text:
    font font_big_noodle_oblique
    color "#000"
    size gui.label_text_size
    xalign 1.0
    outlines [(0, "#fffa", 1, 1)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
