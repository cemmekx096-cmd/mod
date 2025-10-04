








init 5:

    style phone_message_vbox:
        xalign 0.5
        yalign 0
        ypos 380
        xsize 360
        xoffset -40

    style phone_message_frame:
        background Solid("#d9398c")
        ypadding 10
        xpadding 10

    style phone_message_frame2:
        background Solid("0d88ff")
        ypadding 10
        xpadding 10

    style phone_message_contents:
        spacing 10

    style phone_message is say_dialogue:
        xoffset 0
        outlines []
        xalign 1
        yalign 0

    style phone_message2 is say_dialogue:
        xoffset 0
        outlines []
        xalign 1
        yalign 0


    style phone_message_who is phone_message:
        color "#ecf0f1"
        size 25

    style phone_message_what is phone_message:
        color "#ffffff"
        size 24

    style phone_reply is default:
        size 18
        xalign 0.5
        xsize 475
        background Solid("#666")
        hover_background Solid("0d88ff")
        ypadding 10
        xpadding 10

screen phone_message(who, what):

    vbox at incoming_message:
        style_group "phone_message"
        add "images/bubble-tip.png" at phone_message_bubble_tip

        frame:
            style_group "phone_message"

            has vbox
            style "phone_message_contents"
            text who style "phone_message_who"
            text what style "phone_message_what"

screen phone_message2(who, what):
    vbox at incoming_message:
        style_group "phone_message"
        xoffset -584
        xalign 1.0


        add "images/bubble-tip2.png" at phone_message_bubble_tip2

        frame:
            style_group "phone_message2"
            background Solid("0d88ff")
            xsize 200

            has vbox
            style "phone_message_contents"
            text who style "phone_message_who"
            text what style "phone_message_what"

screen phone_message3(what):
    vbox at incoming_message:
        style_group "phone_message"
        xoffset -584
        xalign 1.0


        add "images/bubble-tip2.png" at phone_message_bubble_tip2

        frame:
            style_group "phone_message2"
            background Solid("0d88ff")
            xsize 200

            has vbox
            style "phone_message_contents"

            text what style "phone_message_what"

screen phone_reply(reply1, label1, reply2, label2):
    modal True
    vbox:
        xalign 0.5
        yalign 0.8
        spacing 5

        textbutton "[reply1]" action Jump(label1) style "phone_reply"
        textbutton "[reply2]" action Jump(label2) style "phone_reply"




screen phone_reply3(reply1, label1, reply2, label2, reply3, label3):
    modal True
    vbox:
        xalign 0.5
        yalign 0.8
        spacing 5

        textbutton "[reply1]" action Jump(label1) style "phone_reply"
        textbutton "[reply2]" action Jump(label2) style "phone_reply"
        textbutton "[reply3]" action Jump(label3) style "phone_reply"


style phone_reply_text:
    xalign 0.5

screen phone_message_image(who, what, img):
    vbox at incoming_message:
        style_group "phone_message"

        add "images/bubble-tip.png" at phone_message_bubble_tip

        frame:
            style_group "phone_message"

            has vbox
            style "phone_message_contents"
            text who style "phone_message_who"
            text what style "phone_message_what"
            add img







image text_killian = "gui/phone/text_killian.png"
image text_victoria = "gui/phone/text_victoria.png"
image text_chuck = "gui/phone/text_chuck.png"
image text_unknown = "gui/phone/text_unknown.png"
image text_mina = "gui/phone/text_mina.png"
image text_felicia = "gui/phone/text_felicia.png"
image text_rosalind = "gui/phone/text_rosalind.png"
image text_hana = "gui/phone/text_hana.png"
image text_veronica = "gui/phone/text_veronica.png"


transform phone_pickup:
    yalign 1.0 xalign 0.5
    yoffset 900
    easein 0.3 yoffset 100

transform phone_hide:
    yalign 1.0 xalign 0.5
    yoffset 100
    easein 0.3 yoffset 1300


transform phone_message_bubble_tip:
    xoffset 10
    yoffset 1

transform phone_message_bubble_tip2:
    xoffset 165
    yoffset 1

transform scrolling_out_message:
    easeout 0.1 yoffset -30 alpha 0

transform incoming_message:
    yoffset 100
    alpha 0
    parallel:
        easein 0.1 alpha 1
    parallel:
        easein 0.2 yoffset 0

    on hide:
        scrolling_out_message




label phone_start_kil:
    window hide
    show text_killian at phone_pickup
    $ renpy.pause(0.2)
    return

label phone_start_vic:
    window hide
    show text_victoria at phone_pickup
    $ renpy.pause(0.2)
    return

label phone_start_chuck:
    window hide
    show text_chuck at phone_pickup
    $ renpy.pause(0.2)
    return

label phone_start_unknown:
    window hide
    show text_unknown at phone_pickup
    $ renpy.pause(0.2)
    return

label phone_start_mina:
    window hide
    show text_mina at phone_pickup
    $ renpy.pause(0.2)
    return

label phone_start_fel:
    window hide
    show text_felicia at phone_pickup
    $ renpy.pause(0.2)
    return

label phone_start_rose:
    window hide
    show text_rosalind at phone_pickup
    $ renpy.pause(0.2)
    return

label phone_start_hana:
    window hide
    show text_hana at phone_pickup
    $ renpy.pause(0.2)
    return

label phone_start_ver:
    window hide
    show text_veronica at phone_pickup
    $ renpy.pause(0.2)
    return

label phone_msg:
    hide screen phone_message
    $ renpy.pause(0.1)
    pause
    return

label phone_msg2:
    hide screen phone_message2
    $ renpy.pause(0.1)
    pause
    return

label phone_msgi:
    hide screen phone_message_image
    $ renpy.pause(0.1)
    pause
    return


label phone_after_menu:
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    return

label phone_end_kil:
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    hide text_killian
    $ renpy.pause(0.2)
    return

label phone_end_vic:
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    hide text_victoria
    $ renpy.pause(0.2)
    return

label phone_end_chuck:
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    hide text_chuck
    $ renpy.pause(0.2)
    return

label phone_end_unknown:
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    hide text_unknown
    $ renpy.pause(0.2)
    return

label phone_end_mina:
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    hide text_mina
    $ renpy.pause(0.2)
    return

label phone_end_fel:
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    hide text_felicia
    $ renpy.pause(0.2)
    return

label phone_end_rose:
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    hide text_rosalind
    $ renpy.pause(0.2)
    return

label phone_end_hana:
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    hide text_hana
    $ renpy.pause(0.2)
    return

label phone_end_ver:
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    hide text_hana
    $ renpy.pause(0.2)
    return

label message(who, what):
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)

    if who.lower() == "me":
        show screen phone_message2(who, what)
    else:
        show screen phone_message(who, what)
    play sound "sound effects/sms-bloop.wav"
    if preferences.afm_enable == True:
        pause (1.0 * (len(what) + config.afm_bonus) * preferences.afm_time / config.afm_characters) + 0.5
    else:
        pause
    return

label reply_message(what):
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    show screen phone_message3(what)
    play sound "sound effects/sms-bloop.wav"
    if preferences.afm_enable == True:
        pause (1.0 * (len(what) + config.afm_bonus) * preferences.afm_time / config.afm_characters) + 0.5
    else:
        pause
    return

label message_img(who, what, img):
    hide screen phone_message
    hide screen phone_message2
    hide screen phone_message3
    hide screen phone_message_image
    $ renpy.pause(0.1)
    show screen phone_message_image(who, what,img)
    play sound "sound effects/sms-bloop.wav"
    if preferences.afm_enable == True:
        pause (1.0 * (len(what) + config.afm_bonus) * preferences.afm_time / config.afm_characters) + 1.5
    else:
        pause
    return


label message_start(who, what):

    if who.lower() == "[mcf]":
        show screen phone_message2(who, what)
    else:
        show screen phone_message(who, what)
    play sound "sound effects/sms-bloop.wav"
    if preferences.afm_enable == True:
        pause (1.0 * (len(what) + config.afm_bonus) * preferences.afm_time / config.afm_characters) + 1.5
    else:
        pause
    return


label windowhide:
    window hide
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
