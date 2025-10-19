








init -501 screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:
        has hbox
        spacing 9
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

init -1 style skip_frame is empty:
    ypos gui.skip_ypos
    padding gui.skip_frame_borders.padding

init -1 style skip_text is gui_text:
    size gui.label_text_size

init -1 style skip_triangle is skip_text:


    font "DejaVuSans.ttf"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
