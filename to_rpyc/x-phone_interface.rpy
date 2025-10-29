define stock_i.ImagePath = ""
image visionage_image_phone_message:
    stock_i.ImagePath


default ecran_affiche = "Phone_Home"

default webifeApp = False





screen ouverture_phone_interface():

    zorder 50

    hbox:

        xpos 326
        ypos 0.90


        imagebutton:
            at icone_phone

            idle Transform ("gui/phone_jeu/phone_idle.webp")
            hover Transform ("gui/phone_jeu/phone_hover.webp")
            action [
        SetVariable("ecran_affiche", "Phone_Home"),
        SetVariable("datePhoneHeure", (dateJeu + timedelta(seconds=int(renpy.get_game_runtime()))).strftime("%I:%M %p" if persistent.lang == "english" else "%H:%M")),
        SetVariable("datePhoneJour", (dateJeu + timedelta(seconds=int(renpy.get_game_runtime()))).strftime("%A, %B %#d, %Y").capitalize() if persistent.lang == "english" else dateJeu.strftime("%A %#d %B %Y").capitalize()),
        ShowMenu("Phone")
                    ]



        $ nbMessageTotal = sum([q.nbMessageRecu for q in AllLI if q.isKnow and q.phoneNumber])
        if nbMessageTotal > 0:
            frame:
                background Frame("gui/phone_jeu/messages_red.webp")
                xpos -27

                left_padding 7
                right_padding 9
                top_padding 4
                bottom_padding 4

                text str(nbMessageTotal):
                    yoffset -1
                    size 12
                    font "SF-Pro-Display-Light.otf"

transform icone_phone:
    zoom 0.6







screen Phone():


    frame:

        style "Phone_Commun"

        if ecran_affiche == "Phone_Home":
            use Phone_Home
        elif ecran_affiche == "Appels":
            use Phone_Appels
        elif ecran_affiche == "Messages":
            use Phone_Messages
        elif ecran_affiche == "Details_Messages":
            use Phone_Details_Messages
        elif ecran_affiche == "Photos":
            use Phone_Photos
        elif ecran_affiche == "Phone_Photo_Gallery":
            use Phone_Photo_Gallery
        elif ecran_affiche == "Phone_Photo_Category":
            use Phone_Photo_Category


        imagebutton:
            focus_mask True
            idle "gui/phone_jeu/exit_phone_idle.webp"
            hover "gui/phone_jeu/exit_phone_hover.webp"
            action [Return()]


        if ecran_affiche == "Messages":
            imagebutton:
                focus_mask True
                idle "gui/phone_jeu/phone_menu_idle.webp"
                hover "gui/phone_jeu/phone_menu_hover.webp"
                action SetVariable("ecran_affiche", "Phone_Home")

        if ecran_affiche == "Details_Messages":
            imagebutton:
                focus_mask True
                idle "gui/phone_jeu/back_menu_idle.webp"
                hover "gui/phone_jeu/back_menu_hover.webp"
                action SetVariable("ecran_affiche", "Messages")

        if ecran_affiche == "Appels":
            imagebutton:
                focus_mask True
                idle "gui/phone_jeu/phone_menu_idle.webp"
                hover "gui/phone_jeu/phone_menu_hover.webp"
                action SetVariable("ecran_affiche", "Phone_Home")

        if ecran_affiche == "Photos":
            imagebutton:
                focus_mask True
                idle "gui/phone_jeu/back_menu_idle.webp"
                hover "gui/phone_jeu/back_menu_hover.webp"
                action SetVariable("ecran_affiche", "Details_Messages")

        if ecran_affiche == "Phone_Photo_Gallery":
            imagebutton:
                focus_mask True
                idle "gui/phone_jeu/phone_menu_idle.webp"
                hover "gui/phone_jeu/phone_menu_hover.webp"
                action SetVariable("ecran_affiche", "Phone_Home")

        if ecran_affiche == "Phone_Photo_Category":
            imagebutton:
                focus_mask True
                idle "gui/phone_jeu/back_menu_idle.webp"
                hover "gui/phone_jeu/back_menu_hover.webp"
                action SetVariable("ecran_affiche", "Phone_Photo_Gallery")

style Phone_Commun:

    background "gui/phone_jeu/phone_main.webp"
    xsize 468
    ysize 1016
    xpos 300
    ypos 30





style fontTextIcone:
    xcenter 0.5
    size 22
    font "SF-Pro-Display-Light.otf"


screen Phone_Home():

    vbox:

        xcenter 0.5
        ypos 100

        text datePhoneJour:
            xcenter 0.5
            size 25
            font "SF-Pro-Display-Light.otf"

        text datePhoneHeure:
            xcenter 0.5
            size 90
            font "SF-Pro-Display-Medium.otf"

    frame:
        background "gui/LI_personnages/1px.webp"

        ypos 0.25
        xcenter 0.5


        has grid 3 3

        xspacing 25
        yspacing 25


        vbox:
            imagebutton:
                xcenter 0.5
                mouse "hand"
                focus_mask True
                idle ("gui/phone_jeu/appel_icon_idle.webp")
                action SetVariable("ecran_affiche", "Appels")
            text _("Contacts"):
                style "fontTextIcone"

        vbox:
            imagebutton:
                xcenter 0.5
                mouse "hand"
                focus_mask True
                idle ("gui/phone_jeu/message_icon_new_phone_message.webp")
                action SetVariable("ecran_affiche", "Messages")
            text _("Messages"):
                style "fontTextIcone"

        vbox:
            imagebutton:
                xcenter 0.5
                mouse "hand"
                focus_mask True
                idle ("gui/phone_jeu/photos_icon_idle.webp")
                action SetVariable("ecran_affiche", "Phone_Photo_Gallery")

            text _("Photos"):
                style "fontTextIcone"

        vbox:
            imagebutton:
                xcenter 0.5
                mouse "hand"
                focus_mask True
                idle ("gui/phone_jeu/C2C_icon.webp")

            text _("CdeC"):
                style "fontTextIcone"

        vbox:
            imagebutton:
                xcenter 0.5
                mouse "hand"
                focus_mask True
                if webifeApp == True:
                    idle ("gui/phone_jeu/webife_icon_idle.webp")
                else:
                    idle ("gui/phone_jeu/1px.webp")


            if webifeApp == True:
                text _("We-Bife"):
                    style "fontTextIcone"
            else:
                text _(""):
                    style "fontTextIcone"


        vbox:
            imagebutton:
                xcenter 0.5
                mouse "hand"
                focus_mask True
                idle ("gui/phone_jeu/1px.webp")

            text _(""):
                style "fontTextIcone"


        vbox:
            imagebutton:
                xcenter 0.5
                mouse "hand"
                focus_mask True
                idle ("gui/phone_jeu/1px.webp")

            text _(""):
                style "fontTextIcone"

        vbox:
            imagebutton:
                xcenter 0.5
                mouse "hand"
                focus_mask True
                idle ("gui/phone_jeu/1px.webp")

            text _(""):
                style "fontTextIcone"

        vbox:
            imagebutton:
                xcenter 0.5
                mouse "hand"
                focus_mask True
                idle ("gui/phone_jeu/1px.webp")

            text _(""):
                style "fontTextIcone"




    $ nbMessageTotal = sum([q.nbMessageRecu for q in AllLI if q.isKnow and q.phoneNumber])
    if nbMessageTotal > 0:
        frame:
            xanchor 1.0
            xpos 0.70
            ypos 0.24
            xoffset -25
            yoffset 0

            left_padding 12
            right_padding 13
            top_padding 4
            bottom_padding 4

            background Frame("gui/phone_jeu/messages_red.webp")

            text str(nbMessageTotal):
                text_align 0.5
                size 22
                font "SF-Pro-Display-Light.OTF"







screen Phone_Details_Messages():



    frame:
        background "gui/LI_personnages/1px.webp"

        vbox:
            xcenter 0.5
            ypos 0.06
            xoffset 9

            add AllLI[ElementIndex].display_name + "_texto"

            text AllLI[ElementIndex].display_name:
                xalign 0.5

        viewport:

            xmaximum 420
            ymaximum 680

            xcenter 0.5
            ypos 0.21
            yoffset 20


            scrollbars "vertical"
            mousewheel True
            draggable True
            yinitial 1.0

            has vbox

            spacing 10

            if AllLI[ElementIndex].Message:

                $ messages = AllLI[ElementIndex].Message
                $ messages.sort(key=lambda x: x.timestamp)

                for i in messages:
                    if i.Visible:

                        $ bulles_droite = "gui/phone_jeu/phone_send_frame.webp"
                        $ bulles_gauche = "gui/phone_jeu/phone_received_frame.webp"
                        $ bulles_droite_alpha = "gui/phone_jeu/foreground_phone_send_frame.webp"
                        $ bulles_gauche_alpha = "gui/phone_jeu/foreground_phone_received_frame.webp"

                        $ message_text = renpy.substitute(i.MessageText, scope=None, translate=True)


                        if i.MessageTime is not None:

                            if (dateJeu - i.MessageTime) < timedelta(days=1):

                                if i.MessageTime.date() == dateJeu.date():

                                    if persistent.lang == "english":
                                        $ message_time = renpy.substitute(_("Aujourd'hui "), scope = None , translate = True) + i.MessageTime.strftime("%I:%M %p")
                                    else:
                                        $ message_time = renpy.substitute(_("Aujourd'hui "), scope = None , translate = True) + i.MessageTime.strftime("%H:%M")
                                else:

                                    if persistent.lang == "english":
                                        $ message_time = renpy.substitute(_("Hier à "), scope = None , translate = True) + i.MessageTime.strftime("%I:%M %p")
                                    else:
                                        $ message_time = renpy.substitute(_("Hier à "), scope = None , translate = True) + i.MessageTime.strftime("%H:%M")

                            elif timedelta(days=1) < (dateJeu - i.MessageTime) < timedelta(days=2):

                                if persistent.lang == "english":
                                    $ message_time = renpy.substitute(_("Avant-hier à "), scope = None , translate = True) + i.MessageTime.strftime("%I:%M %p")
                                else:
                                    $ message_time = renpy.substitute(_("Avant-hier à "), scope = None , translate = True) + i.MessageTime.strftime("%H:%M")

                            else:

                                if persistent.lang == "english":
                                    $ message_time = i.MessageTime.strftime("%A, %B %#d, %Y").capitalize()
                                else:
                                    $ message_time = i.MessageTime.strftime("%A %#d %B %Y").capitalize()



                        if i.MessageText is not "":

                            hbox:

                                spacing 10

                                if i.MessageKey != "gauche":
                                    box_reverse True


                                vbox:
                                    frame:


                                        if i.MessageKey == "gauche":
                                            background Frame(bulles_gauche, 23,23,23,23)
                                            padding (16, 16, 20, 16)

                                            xalign 0.0
                                            xoffset 8

                                            text message_text:
                                                xanchor 0.0
                                                text_align 0.0
                                                style "Bulles"

                                        else:
                                            background Frame(bulles_droite, 23,23,23,23)
                                            padding (16, 16, 20, 16)

                                            xpos 400
                                            xanchor 1.0

                                            text message_text:
                                                xanchor 1.0
                                                text_align 1.0
                                                xpos 1.0
                                                style "Bulles"


                        if i.ImagePath is not None:



                            if i.MessageKey == "gauche":

                                frame:


                                    background Frame(bulles_gauche, 23,23,23,23)
                                    foreground Frame(bulles_gauche_alpha, 23,23,23,23)
                                    padding (5,5,5,5)

                                    xalign 0.0
                                    xoffset 8

                                    imagebutton:
                                        xcenter 0.5
                                        mouse "hand"
                                        idle i.ImagePath
                                        at diminution_image_phone_message
                                        action [SetVariable("stock_i.ImagePath", i.ImagePath), Show("Phone_Photos", transition=fade)]

                            else:

                                frame:


                                    background Frame(bulles_droite, 23,23,23,23)
                                    foreground Frame(bulles_gauche_alpha, 23,23,23,23)
                                    padding (5, 5, 5, 5)

                                    xpos 400
                                    xanchor 1.0

                                    imagebutton:
                                        xcenter 0.5
                                        mouse "hand"
                                        idle i.ImagePath
                                        at diminution_image_phone_message
                                        action [SetVariable("stock_i.ImagePath", i.ImagePath), Show("Phone_Photos", transition=fade)]


                        if i.MessageKey == "centre":
                            if i.MessageTime is not None:

                                frame:
                                    background "gui/LI_personnages/1px.webp"
                                    xpos 210
                                    xanchor 0.5

                                    text message_time:
                                        text_align 0.5
                                        font "SF-Pro-Display-Light.otf"
                                        size 20








screen Phone_Photos():

    add "visionage_image_phone_message" at look

    viewport:

        imagebutton:
            idle "gui/extra_exit_idle.webp"
            action Show("Phone_Photos_bis", transition=fade)

        imagebutton:
            focus_mask True
            idle "gui/close_galerry_icon_idle.webp"
            action Hide("Phone_Photos", transition=fade)


        key "game_menu" action Hide("Phone_Photos", transition=fade)

screen Phone_Photos_bis():

    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)

        imagebutton:
            idle "visionage_image_phone_message"

    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("Phone_Photos_bis", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"







transform diminution_image_phone_message:
    xzoom 0.12
    yzoom 0.12



transform Transform_Home:
    zoom 0.8


transform diminution_image_phone_galerie:
    xzoom 0.18
    yzoom 0.18

transform diminution_image_phone_galerie_locked:
    xzoom 0.5
    yzoom 0.5






style Base is text:
    size 22
    font "SF-Pro-Display-Light.otf"

style Bulles is text:
    color "#393a4c"
    ycenter 0.5
    size 22
    font "SF-Pro-Display-Light.otf"
    line_spacing 1
    kerning 0.3
    xmaximum 300
    xsize 300







screen Phone_Messages():

    use Phone_groupe

    vbox:
        xcenter 0.5
        ypos 100

        text _("Messages")

    frame:
        background "gui/LI_personnages/1px.webp"
        ypos 0.15
        xcenter 0.5

        has viewport

        scrollbars "vertical"
        mousewheel True
        draggable True

        xmaximum 420
        ymaximum 650


        vbox:
            xsize 427

            if info_groupe_phone == "Tous":
                $ count = -1
                for q in AllLI:
                    $ count +=1
                    if q.isKnow:
                        if q.phoneNumber:
                            $ actor_name = renpy.substitute(q.display_name, scope = None , translate = True).upper()
                            $ who_is = renpy.substitute(q.whoIs, scope = None , translate = True)
                            $ ID_avatar = str(q.ID_avatar)
                            $ name_lower = actor_name.lower()

                            if q.Matrice[q.ID_avatar-1][2] == "interdit":

                                $ avatarFileName = "images/interdit/LI/icones_personnages/LI_"+ q.name.lower() + "_" + ID_avatar + ".webp"
                            else:
                                $ avatarFileName = "gui/LI_personnages/icones_personnages/LI_"+ q.name.lower() + "_" + ID_avatar + ".webp"




                            button:
                                action [Function(SetNewMessage, Value=False, InDex=count), SetVariable("LI_name", q.name), SetVariable("ElementIndex", count), SetVariable("ecran_affiche", "Details_Messages"), Function(renpy.restart_interaction)]

                                xsize 401
                                ysize 122
                                idle_background "gui/LI_personnages/personnage_idle.webp"
                                hover_background "gui/LI_personnages/personnage_hover.webp"

                                hbox:
                                    xsize 401
                                    ysize 122

                                    vbox:
                                        xsize 110
                                        ysize 110
                                        add avatarFileName:
                                            xpos 7
                                            ypos -7
                                    vbox:
                                        xsize 250
                                        ysize 122
                                        text actor_name:
                                            font "SF-Pro-Display-Light.otf"
                                            xoffset -12
                                            size 35
                                            xalign 0.5
                                            ypos 8
                                            idle_color "#cccc"
                                            hover_color "#fff"

                                        text who_is:
                                            font "SF-Pro-Display-Light.otf"
                                            xoffset -12
                                            size 25
                                            xsize 200
                                            xalign 0.5
                                            ypos -6
                                            idle_color "#cccc"
                                            hover_color "#fff"
                                frame:
                                    background "gui/LI_personnages/1px.webp"
                                    xsize 37
                                    ysize 37
                                    ypos 76
                                    xpos 3


                                    if q.nbMessageRecu > 0:
                                        frame:
                                            left_padding 9
                                            right_padding 11
                                            top_padding 3
                                            bottom_padding 3
                                            background Frame("gui/phone_jeu/messages_red.webp")
                                            text str(q.nbMessageRecu):
                                                size 18
                                                font "SF-Pro-Display-Light.otf"
                                if q.LovePoints >= 10:
                                    frame:
                                        yoffset 0
                                        xoffset 320
                                        xysize (64, 79)
                                        background None

                                        add Frame("gui/LI_personnages/Certified_LI.webp")

            elif info_groupe_phone == "LI":
                $ count = -1
                for q in AllLI:
                    $ count +=1
                    if q.isKnow:
                        if q.LovePoints >= 10:
                            if q.phoneNumber:
                                $ actor_name = renpy.substitute(q.display_name, scope = None , translate = True).upper()
                                $ who_is = renpy.substitute(q.whoIs, scope = None , translate = True)
                                $ ID_avatar = str(q.ID_avatar)
                                $ name_lower = actor_name.lower()

                                if q.Matrice[q.ID_avatar-1][2] == "interdit":

                                    $ avatarFileName = "images/interdit/LI/icones_personnages/LI_"+ q.name.lower() + "_" + ID_avatar + ".webp"
                                else:
                                    $ avatarFileName = "gui/LI_personnages/icones_personnages/LI_"+ q.name.lower() + "_" + ID_avatar + ".webp"




                                button:
                                    action [Function(SetNewMessage, Value=False, InDex=count), SetVariable("LI_name", q.name), SetVariable("ElementIndex", count), SetVariable("ecran_affiche", "Details_Messages"), Function(renpy.restart_interaction)]

                                    xsize 401
                                    ysize 122
                                    idle_background "gui/LI_personnages/personnage_idle.webp"
                                    hover_background "gui/LI_personnages/personnage_hover.webp"

                                    hbox:
                                        xsize 401
                                        ysize 122

                                        vbox:
                                            xsize 110
                                            ysize 110
                                            add avatarFileName:
                                                xpos 7
                                                ypos -7
                                        vbox:
                                            xsize 250
                                            ysize 122
                                            text actor_name:
                                                font "SF-Pro-Display-Light.otf"
                                                xoffset -12
                                                size 35
                                                xalign 0.5
                                                ypos 8
                                                idle_color "#cccc"
                                                hover_color "#fff"

                                            text who_is:
                                                font "SF-Pro-Display-Light.otf"
                                                xoffset -12
                                                size 25
                                                xsize 200
                                                xalign 0.5
                                                ypos -6
                                                idle_color "#cccc"
                                                hover_color "#fff"
                                    frame:
                                        background "gui/LI_personnages/1px.webp"
                                        xsize 37
                                        ysize 37
                                        ypos 76
                                        xpos 3


                                        if q.nbMessageRecu > 0:
                                            frame:
                                                left_padding 9
                                                right_padding 11
                                                top_padding 3
                                                bottom_padding 3
                                                background Frame("gui/phone_jeu/messages_red.webp")
                                                text str(q.nbMessageRecu):
                                                    size 18
                                                    font "SF-Pro-Display-Light.otf"


                                    frame:
                                        yoffset 0
                                        xoffset 320
                                        xysize (64, 79)
                                        background None

                                        add Frame("gui/LI_personnages/Certified_LI.webp")

            else:
                $ count = -1
                for q in AllLI:
                    $ count +=1
                    if q.isKnow:
                        if q.phoneNumber:
                            if info_groupe_phone in q.Groupe:
                                $ actor_name = renpy.substitute(q.display_name, scope = None , translate = True).upper()
                                $ who_is = renpy.substitute(q.whoIs, scope = None , translate = True)
                                $ ID_avatar = str(q.ID_avatar)
                                $ name_lower = actor_name.lower()
                                if q.Matrice[q.ID_avatar-1][2] == "interdit":

                                    $ avatarFileName = "images/interdit/LI/icones_personnages/LI_"+ q.name.lower() + "_" + ID_avatar + ".webp"
                                else:
                                    $ avatarFileName = "gui/LI_personnages/icones_personnages/LI_"+ q.name.lower() + "_" + ID_avatar + ".webp"

                                button:

                                    action [Function(SetNewMessage, Value=False, InDex=count), SetVariable("LI_name", q.name), SetVariable("ElementIndex", count), SetVariable("ecran_affiche", "Details_Messages"), Function(renpy.restart_interaction)]

                                    xsize 401
                                    ysize 122
                                    idle_background "gui/LI_personnages/personnage_idle.webp"
                                    hover_background "gui/LI_personnages/personnage_hover.webp"

                                    hbox:
                                        xsize 401
                                        ysize 122

                                        vbox:
                                            xsize 110
                                            ysize 110
                                            add avatarFileName:
                                                xpos 7
                                                ypos -7
                                        vbox:
                                            xsize 250
                                            ysize 122
                                            text actor_name:
                                                font "SF-Pro-Display-Light.otf"
                                                xoffset -12
                                                size 35
                                                xalign 0.5
                                                ypos 8
                                                idle_color "#cccc"
                                                hover_color "#fff"

                                            text who_is:
                                                font "SF-Pro-Display-Light.otf"
                                                xoffset -12
                                                size 25
                                                xsize 200
                                                xalign 0.5
                                                ypos -6
                                                idle_color "#cccc"
                                                hover_color "#fff"
                                    frame:
                                        background "gui/LI_personnages/1px.webp"
                                        xsize 37
                                        ysize 37
                                        ypos 76
                                        xpos 3


                                        if q.nbMessageRecu > 0:
                                            frame:
                                                left_padding 9
                                                right_padding 11
                                                top_padding 3
                                                bottom_padding 3
                                                background Frame("gui/phone_jeu/messages_red.webp")
                                                text str(q.nbMessageRecu):
                                                    size 18
                                                    font "SF-Pro-Display-Light.otf"

                                    if q.LovePoints >= 10:
                                        frame:
                                            yoffset 0
                                            xoffset 320
                                            xysize (64, 79)
                                            background None

                                            add Frame("gui/LI_personnages/Certified_LI.webp")







screen Phone_Appels():

    use Phone_groupe

    vbox:
        xcenter 0.5
        ypos 100

        text _("Contacts")


    frame:
        background "gui/LI_personnages/1px.webp"
        ypos 0.15
        xcenter 0.5

        has viewport

        scrollbars "vertical"
        mousewheel True
        draggable True

        xmaximum 420
        ymaximum 650


        vbox:
            xsize 427

            if info_groupe_phone == "Tous":
                $ count = -1
                for q in AllLI:
                    $ count +=1
                    if q.isKnow:
                        if q.phoneNumber:
                            $ actor_name = renpy.substitute(q.display_name, scope = None , translate = True).upper()
                            $ who_is = renpy.substitute(q.whoIs, scope = None , translate = True)
                            $ ID_avatar = str(q.ID_avatar)
                            $ name_lower = actor_name.lower()
                            if q.Matrice[q.ID_avatar-1][2] == "interdit":

                                $ avatarFileName = "images/interdit/LI/icones_personnages/LI_"+ q.name.lower() + "_" + ID_avatar + ".webp"
                            else:
                                $ avatarFileName = "gui/LI_personnages/icones_personnages/LI_"+ q.name.lower() + "_" + ID_avatar + ".webp"



                            button:
                                action [Function(SetNewMessage, Value=False, InDex=count), SetVariable("LI_name", q.name), SetVariable("ElementIndex", count), Function(renpy.restart_interaction)]

                                xsize 401
                                ysize 122
                                idle_background "gui/LI_personnages/personnage_idle.webp"
                                hover_background "gui/LI_personnages/personnage_hover.webp"

                                has hbox
                                xsize 401
                                ysize 122

                                vbox:
                                    xsize 110
                                    ysize 110
                                    add avatarFileName:
                                        xpos 7
                                        ypos -7
                                vbox:
                                    xsize 250
                                    ysize 122
                                    text actor_name:
                                        font "SF-Pro-Display-Light.otf"
                                        xoffset -12
                                        size 35
                                        xalign 0.5
                                        ypos 8
                                        idle_color "#cccc"
                                        hover_color "#fff"

                                    text who_is:
                                        font "SF-Pro-Display-Light.otf"
                                        xoffset -12
                                        size 25
                                        xsize 200
                                        xalign 0.5
                                        ypos -6
                                        idle_color "#cccc"
                                        hover_color "#fff"



            else:
                $ count = -1
                for q in AllLI:
                    $ count +=1
                    if q.isKnow:
                        if q.phoneNumber:
                            if info_groupe_phone in q.Groupe:
                                $ actor_name = renpy.substitute(q.display_name, scope = None , translate = True).upper()
                                $ who_is = renpy.substitute(q.whoIs, scope = None , translate = True)
                                $ ID_avatar = str(q.ID_avatar)
                                $ name_lower = actor_name.lower()
                                if q.Matrice[q.ID_avatar-1][2] == "interdit":

                                    $ avatarFileName = "images/interdit/LI/icones_personnages/LI_"+ q.name.lower() + "_" + ID_avatar + ".webp"
                                else:
                                    $ avatarFileName = "gui/LI_personnages/icones_personnages/LI_"+ q.name.lower() + "_" + ID_avatar + ".webp"

                                button:


                                    xsize 401
                                    ysize 122
                                    idle_background "gui/LI_personnages/personnage_idle.webp"
                                    hover_background "gui/LI_personnages/personnage_hover.webp"

                                    has hbox
                                    xsize 401
                                    ysize 122

                                    vbox:
                                        xsize 110
                                        ysize 110
                                        add avatarFileName:
                                            xpos 7
                                            ypos -7
                                    vbox:
                                        xsize 250
                                        ysize 122
                                        text actor_name:
                                            font "SF-Pro-Display-Light.otf"
                                            xoffset -12
                                            size 35
                                            xalign 0.5
                                            ypos 8
                                            idle_color "#cccc"
                                            hover_color "#fff"

                                        text who_is:
                                            font "SF-Pro-Display-Light.otf"
                                            xoffset -12
                                            size 25
                                            xsize 200
                                            xalign 0.5
                                            ypos -6
                                            idle_color "#cccc"
                                            hover_color "#fff"






init python:
    def get_filtre_style_phone(groupe):
        if info_groupe_phone == groupe:
            return "filtreNeon_active"
        else:
            return "filtreNeonPhone"

screen Phone_groupe():

    vbox:

        xpos 0.05
        ypos 0.8
        yoffset -20

        xanchor 0.0
        spacing -20

        hbox:

            spacing -20


            button:
                text _("TOUS"):
                    style get_filtre_style_phone("Tous")

                action [SetVariable("info_groupe_phone", "Tous"), Function(renpy.restart_interaction)]

            if CheckGroupeAvalible("Homme"):
                button:
                    text _("HOMMES"):
                        style get_filtre_style_phone("Homme")
                    action [SetVariable("info_groupe_phone", "Homme"), Function(renpy.restart_interaction)]

            if CheckGroupeAvalible("Femme"):
                button:
                    text _("FEMMES"):
                        style get_filtre_style_phone("Femme")
                    action [SetVariable("info_groupe_phone", "Femme"), Function(renpy.restart_interaction)]

            if CheckGroupeAvalible("LI"):
                button:
                    text _("LI"):
                        style get_filtre_style_phone("LI")
                    action [SetVariable("info_groupe_phone", "LI"), Function(renpy.restart_interaction)]

        hbox:

            spacing -20

            if CheckGroupeAvalible("Amis"):
                button:
                    text _("AMIS"):
                        style get_filtre_style_phone("Amis")
                    action [SetVariable("info_groupe_phone", "Amis"), Function(renpy.restart_interaction)]

            if CheckGroupeAvalible("Voisinage"):
                button:
                    text _("VOISINAGE"):
                        style get_filtre_style_phone("Voisinage")
                    action [SetVariable("info_groupe_phone", "Voisinage"), Function(renpy.restart_interaction)]

            if CheckGroupeAvalible("Travail"):
                button:
                    text _("TRAVAIL"):
                        style get_filtre_style_phone("Travail")
                    action [SetVariable("info_groupe_phone", "Travail"), Function(renpy.restart_interaction)]

            if CheckGroupeAvalible("Famille"):
                button:
                    text _("FAMILLE"):
                        style get_filtre_style_phone("Famille")
                    action [SetVariable("info_groupe_phone", "Famille"), Function(renpy.restart_interaction)]

        hbox:

            spacing -20

            if CheckGroupeAvalible("Autre"):
                button:
                    text _("AUTRES"):
                        style get_filtre_style_phone("Autre")
                    action [SetVariable("info_groupe_phone", "Autre"), Function(renpy.restart_interaction)]








style filtreNeonPhone is text:

    size 17
    color "#ffffff"
    font "SF-Pro-Display-Light.otf"
    idle_outlines [   (13, (49,47,47,0), 0, 0),  
                (12, (52,46,46,0), 0, 0),
                (11, (58,45,45,0), 0, 0),
                (10, (66,44,44,0), 0, 0),
                (9, (77,44,44,0), 0, 0),
                (8, (92,43,42,0), 0, 0),
                (7, (109,43,42,0), 0, 0),
                (6, (128,47,43,0), 0, 0),
                (5, (151,55,52,0), 0, 0),
                (4, (178,73,69,0), 0, 0),
                (3, (199,99,94,0), 0, 0),
                (2, (218,128,123,50), 0, 0),  
                (1, (238,188,185,200), 0, 0) ]

    hover_outlines [   (13, (49,47,47,10), 0, 0),  
                (12, (52,46,46,10), 0, 0),
                (11, (58,45,45,10), 0, 0),
                (10, (66,44,44,10), 0, 0),
                (9, (77,44,44,10), 0, 0),
                (8, (92,43,42,100), 0, 0),
                (7, (109,43,42,150), 0, 0),
                (6, (128,47,43,200), 0, 0),
                (5, (151,55,52,255), 0, 0),
                (4, (178,73,69,255), 0, 0),
                (3, (199,99,94,255), 0, 0),
                (2, (218,128,123,255), 0, 0),  
                (1, (238,188,185,255), 0, 0) ]































screen Phone_Photo_Gallery():



    $ gallery_items = sorted([cat for cat in extra_gallery() if cat['unlocked']], key=lambda x: x['text'].lower())

    vbox:
        xcenter 0.5
        ypos 100
        text _("Galerie Photos")

    frame:
        background "gui/LI_personnages/1px.webp"
        ypos 0.15
        xcenter 0.5

        has viewport id "Phone_Photo_Gallery_viewport"
        scrollbars "vertical"
        mousewheel True
        draggable True
        xmaximum 420
        ymaximum 750
        yadjustment scroll_position_phone_galerie_photos

        vbox:
            spacing 2
            xsize 427

            for category in gallery_items:
                button:
                    action If(category['unlocked'], 
                              true=[
                              SetVariable("current_category", category['menu']),
                              SetVariable("current_category_text", category['text']),
                              SetVariable("ecran_affiche", "Phone_Photo_Category"),
                              ],
                              false=NullAction())

                    xsize 401
                    ysize 122
                    idle_background "gui/LI_personnages/personnage_idle.webp"
                    hover_background "gui/LI_personnages/personnage_hover.webp"

                    has hbox
                    xsize 401
                    ysize 122

                    vbox:
                        xsize 110
                        ysize 110

                        if category['unlocked']:
                            add category['image']:
                                size (178, 100)
                                yalign 0.5
                                yoffset -3
                        else:
                            add "gui/locked.webp":
                                size (178, 100)
                                yalign 0.5
                                yoffset -3
                                xoffset 6

                    vbox:
                        xsize 250
                        ysize 110
                        text category['text']:
                            font "SF-Pro-Display-Light.otf"
                            xoffset -12
                            size 35
                            xalign 0.5

                            idle_color "#cccc"
                            hover_color "#fff"


screen Phone_Photo_Category():
    modal True


    $ update_current_category_gallery()
    $ gallery_items = current_category_gallery.get(current_category, lambda: [])()
    $ current_adjustment = scroll_adjustments_phone_photo_category[current_category]


    vbox:
        xcenter 0.5
        ypos 100
        text (current_category_text).capitalize()

    frame:
        background "gui/LI_personnages/1px.webp"
        ypos 0.15
        xcenter 0.5

        has viewport id "Phone_Photo_Category_viewport"
        scrollbars "vertical"
        mousewheel True
        draggable True
        xmaximum 420
        ymaximum 750
        yadjustment current_adjustment

        vbox:
            spacing 20
            xfill True
            xcenter 0.5


            for extra_object in gallery_items:
                vbox:
                    spacing 8
                    xalign 0.5

                    imagebutton:

                        xalign 0.5
                        mouse "hand"
                        if extra_object.get('unlocked', False):
                            idle extra_object.get('image', 'gui/locked.webp')
                            at diminution_image_phone_galerie
                            action gallery_action(extra_object)
                        else:
                            idle "gui/locked.webp"

                    text extra_object.get('text', 'No text'):
                        xalign 0.5
                        style "phone_photo_text"

    imagebutton:
        focus_mask True
        idle "gui/phone_jeu/back_menu_idle.webp"
        hover "gui/phone_jeu/back_menu_hover.webp"
        action SetVariable("ecran_affiche", "Phone_Photo_Gallery")
        xalign 0.1
        yalign 0.95






screen Phone_Photo_Viewer():
    modal True
    add visionage_image_phone_message at look
    viewport:
        imagebutton:
            idle "gui/extra_exit_idle.webp"
            action Show("Phone_Photo_Viewer_Scrollable", transition=fade)
        imagebutton:
            focus_mask True
            idle "gui/close_galerry_icon_idle.webp"
            action Hide("Phone_Photo_Viewer", transition=fade)

    key "game_menu" action Hide("Phone_Photo_Viewer", transition=fade)

screen Phone_Photo_Viewer_Scrollable():
    modal True
    viewport:
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        side_yfill True
        edgescroll (200, 600)
        imagebutton:
            idle visionage_image_phone_message
    imagebutton:
        focus_mask True
        idle "gui/close_galerry_icon_idle.webp"
        action Hide("Phone_Photo_Viewer_Scrollable", transition=fade)
    imagebutton:
        idle "gui/scroll_galerry_icon_idle.webp"










style phone_photo_text:
    font "SF-Pro-Display-Light.otf"
    size 22
    color "#FFFFFF"
    text_align 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
