








init -501 screen notify(message):
    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message]"

    timer 3.25 action Hide('notify')


transform -1 notify_appear:
    on show:
        yoffset -50
        linear .25 yoffset 0
    on hide:
        yoffset 0
        linear .25 yoffset -50

init -1 style notify_frame is empty:
    ypos gui.notify_ypos
    xalign 0.5
    background "#000a"

    padding gui.notify_frame_borders.padding

init -1 style notify_text is gui_text:
    properties gui.text_properties("notify")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
