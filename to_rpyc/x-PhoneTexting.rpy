define nvl_mode = "texto"


init -1 python:


    def Phone_ReceiveSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/ReceiveText.ogg")
    def Phone_SendSound(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("audio/SendText.ogg")


screen PhoneDialogue(dialogue, items=None):

    frame:

        at inclinaison
        background "gui/phone_jeu/1px.webp"



        if len(items)>=2:
            ysize 600-(len(items)-2)*(120+10)-20
        else:
            ymaximum 1100

        viewport:



            yinitial 1.0

            has vbox

            null height 20
            use nvl_phonetext(dialogue, items)
            null height 100



screen nvl_phonetext(dialogue, items):

    $ previous_d_who = None

    vbox:
        xsize 700


        spacing 12

        for id_d, d in enumerate(dialogue):

            if d.who == "narator":

                null height 30
                text d.what:

                    text_align 0.5
                    italic True
                    size 40
                    slow_cps False
                    id d.what_id
                    if d.current and len(items)==0:
                        at message_narrator
                null height 30

            else:
                if d.who == jason or d.who == jasonRU:
                    $ message_frame = "gui/phone_jeu/phone_send_frame_testing.webp"
                else:
                    $ message_frame = "gui/phone_jeu/phone_received_frame_testing.webp"

                hbox:

                    spacing 10

                    if d.who == jason or d.who == jasonRU:
                        box_reverse True
                        xalign 1.0



                    if previous_d_who != d.who:

                        if d.who == jason or d.who == jasonRU:
                            $ message_icon = Jason_texto
                        elif d.who == nicole or d.who == nicoleRU:
                            $ message_icon = Nicole_texto
                        elif d.who == lexie or d.who == lexieRU:
                            $ message_icon = Lexie_texto
                        elif d.who == alex or d.who == alexRU:
                            $ message_icon = Alex_texto
                        elif d.who == feng or d.who == MissFengRU:
                            $ message_icon = Feng_texto
                        elif d.who == julienne or d.who == julienneRU:
                            $ message_icon = Julienne_texto
                        elif d.who == marvin or d.who == marvinRU:
                            $ message_icon = Marvin_texto
                        elif d.who == marya or d.who == maryaRU:
                            $ message_icon = Marya_texto



                        else:
                            $ message_icon = "gui/phone_jeu/phone_received_icon.webp"

                        add message_icon:
                            if d.current and len(items)==0:
                                at message_appear_icon()

                    else:
                        null width 107


                    vbox:


                        if previous_d_who != d.who:
                            if d.who == jason or d.who == jasonRU:
                                text d.who:
                                    xalign 1.0
                                    xoffset -10
                                    size 30

                            else:
                                text d.who:
                                    xalign 0.0
                                    xoffset 10
                                    size 30


                        frame:

                            padding (20,20)
                            background Frame(message_frame, 23,23,23,23)
                            xsize 300

                            if d.current and len(items)==0:
                                if d.who == jason:
                                    at message_appear(1)

                                else:
                                    at message_appear(-1)

                            text d.what:
                                xsize 300
                                slow_cps False
                                size 35


                                if d.who == jason:
                                    color "#393a4c"
                                    text_align 1.0
                                    xanchor 1.0
                                    xpos 1.0
                                    ypos 0.0
                                else:
                                    text_align 0.0
                                    xanchor 0.0
                                    color "#393a4c"
                                    xpos 0.0
                                    ypos 0.0


                                id d.what_id

            $ previous_d_who = d.who




transform message_appear(pDirection):
    alpha 0.0
    xoffset 50 * pDirection
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0

transform message_appear_icon():
    zoom 0.0
    easein_back 0.5 zoom 1.0

transform message_narrator:
    alpha 0.0
    yoffset -50

    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0

transform inclinaison:

    on show:
        perspective (True)
        matrixtransform ScaleMatrix(0.9, 0.92, 1.0)*RotateMatrix(0, -4, 1.8)*OffsetMatrix(1150, 0, 0)

    on hide:
        linear 0.5 xpos -1200
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
