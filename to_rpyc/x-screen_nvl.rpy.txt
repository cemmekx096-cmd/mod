







define -1 gui.phone_text_bg = {
    'ian': im.MatrixColor('gui/phone_text_bg.webp',im.matrix.colorize("#000", "#507859")),
    'lena': im.MatrixColor('gui/phone_text_bg.webp',im.matrix.colorize("#000", "#507859")),
    'other': im.MatrixColor('gui/phone_text_bg.webp',im.matrix.colorize("#000", "#333")),
}

define -1 gui.phone_text_arrow = {
    'ian': im.MatrixColor('gui/phone_text_arrow.webp',im.matrix.colorize("#000", "#507859")),
    'lena': im.MatrixColor('gui/phone_text_arrow.webp',im.matrix.colorize("#000", "#507859")),
    'other': im.MatrixColor('gui/phone_text_arrow.webp',im.matrix.colorize("#000", "#333")),
}

define -1 phone_text_icon_size = 84

init 499 image phone_text_icon_unk = im.Scale('gui/phone_text_icon_unk.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_alison = ConditionSwitch(
    "alison_blonde", im.Scale('gui/phone_text_icon_alison_blonde.webp', phone_text_icon_size, phone_text_icon_size),
    "True", im.Scale('gui/phone_text_icon_alison.webp', phone_text_icon_size, phone_text_icon_size)
)
init 499 image phone_text_icon_axel = im.Scale('gui/phone_text_icon_axel.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_billy = im.Scale('gui/phone_text_icon_billy.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_cherry = im.Scale('gui/phone_text_icon_cherry.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_cindy = im.Scale('gui/phone_text_icon_cindy.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_clark = im.Scale('gui/phone_text_icon_clark.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_danis = im.Scale('gui/phone_text_icon_danis.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_danny = im.Scale('gui/phone_text_icon_danny.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_emma = im.Scale('gui/phone_text_icon_emma.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_gillian = im.Scale('gui/phone_text_icon_gillian.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_holly = im.Scale('gui/phone_text_icon_holly.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_ian = im.Scale('gui/phone_text_icon_ian.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_ivy = im.Scale('gui/phone_text_icon_ivy.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_jack = im.Scale('gui/phone_text_icon_jack.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_jeremy = im.Scale('gui/phone_text_icon_jeremy.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_jessica = ConditionSwitch(
    "jess_bad", im.Scale('gui/phone_text_icon_jessica_bad.webp', phone_text_icon_size, phone_text_icon_size),
    "True", im.Scale('gui/phone_text_icon_jessica.webp', phone_text_icon_size, phone_text_icon_size)
)
init 499 image phone_text_icon_john = im.Scale('gui/phone_text_icon_john.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_kent = im.Scale('gui/phone_text_icon_kent.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_lena = im.Scale('gui/phone_text_icon_lena.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_perry = im.Scale('gui/phone_text_icon_perry.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_dad = im.Scale('gui/phone_text_icon_lena_dad.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_mom = im.Scale('gui/phone_text_icon_lena_mom.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_louise = im.Scale('gui/phone_text_icon_louise.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_marcel = im.Scale('gui/phone_text_icon_marcel.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_mark = im.Scale('gui/phone_text_icon_mark.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_martin = im.Scale('gui/phone_text_icon_martin.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_mike = im.Scale('gui/phone_text_icon_mike.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_minerva = im.Scale('gui/phone_text_icon_minerva.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_nat = im.Scale('gui/phone_text_icon_nat.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_robert = im.Scale('gui/phone_text_icon_robert.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_rosa = im.Scale('gui/phone_text_icon_rosa.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_seymour = im.Scale('gui/phone_text_icon_seymour.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_stan = im.Scale('gui/phone_text_icon_stan.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_victor = im.Scale('gui/phone_text_icon_victor.webp', phone_text_icon_size, phone_text_icon_size)
init 499 image phone_text_icon_wade = im.Scale('gui/phone_text_icon_wade.webp', phone_text_icon_size, phone_text_icon_size)

init -501 screen nvl(dialogue, items=None):
    window:
        style "nvl_window"
        if ian_active:
            xalign 1.0
            xoffset -52

        vbox:
            xfill True
            spacing gui.nvl_spacing

            use nvl_dialogue(dialogue)



            for i in items:
                textbutton i.caption:
                    action i.action
                    style "nvl_button"


init -501 screen nvl_dialogue(dialogue):
    for i, d in enumerate(dialogue):
        $ protagonist = (ian_active and d.who == 'Ian') or (not ian_active and d.who == 'Lena')
        hbox:
            spacing 20
            if i == len(dialogue) - 1:
                at phone_message_text

            if not protagonist:
                box_reverse True
                xalign 1.0

            hbox:
                if not protagonist:
                    box_reverse True
                xsize phone_text_icon_size
                spacing 0
                add 'phone_text_icon_%s' % (d.who.lower() if d.who.lower() != '???' else 'unk')
                frame style "empty":
                    xsize 0
                    has add gui.phone_text_arrow[d.who.lower() if protagonist else 'other']
                    if not protagonist:
                        xalign 1.0
                        xoffset -2
                    else:
                        xoffset 2

            window:
                id d.window_id
                background Frame(
                    gui.phone_text_bg[d.who.lower() if protagonist else 'other'],
                    8, 8, 12, 12
                )
                text d.what:
                    id d.what_id


transform -1 phone_message_text:
    alpha 0.0
    yoffset 50
    parallel:
        ease 0.35 yoffset 0
    parallel:
        ease 0.25 alpha 1.0



define -1 config.nvl_list_length = gui.nvl_list_length

init -1 style nvl_window is default:
    xysize (586, 780)
    xoffset 52
    yoffset 100

    align (0.0, 0.0)

init -1 style nvl_entry is default:
    padding (16,12,16,12)
    align (0.0, 0.0)
    yoffset 0
    xmaximum 586 - 20 - phone_text_icon_size










init -1 style nvl_dialogue is say_dialogue:
    outlines []
    color "#fff"
    align (0.0,0.0)





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

init -1 style nvl_button is button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

init -1 style nvl_button_text is button_text:
    properties gui.button_text_properties("nvl_button")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
