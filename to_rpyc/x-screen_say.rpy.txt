














init -501 screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        ysize gui.textbox_height
        xfill True

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"




    if not renpy.variant("small"):
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
    yalign gui.textbox_yalign
    yoffset -26

    background Image("gui/textbox.webp", xalign=0.5, yalign=1.0)

init -1 style window:
    variant "small"
    yoffset -40
    background Frame(Image("gui/textbox.webp", xalign=0.5, yalign=1.0))

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
    outlines [(2, "#000a", 1, 1)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
