









default -1 timeout = 4.0

default -1 timeout_label = None

default -1 persistent.timed_choices = True
init -501 screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    if (timeout_label is not None) and persistent.timed_choices:

        bar:
            xalign 0.5
            yalign 0.1

            xsize 1100
            ysize 10
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)
        timer timeout action Jump(timeout_label)




define -1 config.narrator_menu = True


init -1 style choice_vbox is vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

init -1 style choice_vbox:
    variant "small"
    align (0.5, 0.5)

init -1 style choice_button is button:
    properties gui.button_properties("choice_button")
    hover_sound "sfx/paper_hover.mp3"
    activate_sound "sfx/paper_click.mp3"

init -1 style choice_button_text is button_text:
    properties gui.button_text_properties("choice_button")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
