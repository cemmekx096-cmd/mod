







init -501 screen main_menu():
    tag menu
    style_prefix "main_menu"

    add gui.main_menu_background

    imagebutton:
        auto "gui/main_newgame_%s.webp"
        focus_mask True
        hovered Play("ch_one", "sfx/paper_hover.mp3")
        action Play("ch_two", "sfx/paper_click.mp3"), Start(label='start_debug' if renpy.has_label('start_debug') else 'start')
    imagebutton:
        auto "gui/main_load_%s.webp"
        focus_mask True
        hovered Play("ch_two", "sfx/paper_hover.mp3")
        action Play("ch_three", "sfx/paper_click.mp3"), ShowMenu("load")

    hbox:
        imagebutton:
            auto "gui/main_gallery_%s.webp"
            focus_mask True
            hovered [ Play ("ch_one", "sfx/paper_hover.mp3") ]
            action [ Play ("ch_three", "sfx/paper_click.mp3") ] , ShowMenu("screen_gallery")
        imagebutton:
            auto "gui/main_settings_%s.webp"
            focus_mask True
            hovered Play("ch_one", "sfx/paper_hover.mp3")
            action Play("ch_three", "sfx/paper_click.mp3"), ShowMenu("preferences")
        imagebutton:
            auto "gui/main_credits_%s.webp"
            focus_mask True
            hovered Play ("ch_one", "sfx/paper_hover.mp3")
            action Play("ch_three", "sfx/paper_click.mp3"), ShowMenu("about")

        if renpy.variant("pc"):


            imagebutton:
                auto "gui/main_controls_%s.webp"
                focus_mask True
                hovered Play ("ch_one", "sfx/paper_hover.mp3")
                action Play("ch_two", "sfx/paper_click.mp3"), ShowMenu("help")
            imagebutton:
                auto "gui/main_quit_%s.webp"
                focus_mask True
                hovered Play ("ch_one", "sfx/paper_hover.mp3")
                action Play("ch_three", "sfx/paper_click.mp3"), Quit(confirm=not main_menu)

    if not steam:
        imagebutton:
            xalign 1.0
            offset (-40, 20)
            auto "gui/main_patreon_%s.webp"
            hovered Play ("ch_one", "sfx/paper_hover.mp3")
            action Play("ch_three", "sfx/paper_click.mp3"), OpenURL ("https://www.patreon.com/Evakiss")

    imagebutton:
        offset (40, 20)
        auto "gui/main_discord_%s.webp"
        hovered Play ("ch_one", "sfx/paper_hover.mp3")
        action Play("ch_three", "sfx/paper_click.mp3"), OpenURL ("https://discord.com/invite/QtRYCsA")

init -1 style main_menu_hbox:
    align (0.5, 1.0)
    yoffset -40

init -1 style main_menu_hbox:
    variant "small"
    spacing 80
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
