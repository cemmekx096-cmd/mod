screen LI_menu():

    zorder 50

    hbox:

        xpos 330
        xoffset -15
        ypos 0.83
        yoffset 10

        imagebutton:

            idle Transform ("gui/LI_personnages/LI_idle.webp")
            hover Transform ("gui/LI_personnages/LI_hover.webp")
            action ShowMenu("LI_profils")



        $ nbProgressLI = sum([q.nbProgressRecu for q in AllLI if q.isKnow])
        $ nbProgressTotal = nbProgressLI + pl.nbProgressRecu
        if nbProgressTotal > 0:

            frame:
                background Frame("gui/LI_personnages/entree_LI.webp")
                xpos -27

                left_padding 7
                right_padding 7
                top_padding 4
                bottom_padding 4

                text str(nbProgressTotal):
                    yoffset -1
                    size 12
                    font "SF-Pro-Display-Light.otf"



screen LI_profils():

    add "gui/LI_personnages/LI_background.webp"
    use LI_image
    use LI_details

    use LI_List

    use LI_groupe






screen LI_details():
    zorder -5

    if LI_name == "Player":


        frame:
            background "gui/LI_personnages/1px.webp"
            xsize 670
            ysize 100
            xpos 1220
            ypos 0

            has text _("Profil du joueur")

            if lang == "russian":
                style "grosTitreNeonCyrillique"
                yoffset 40
            else:
                style "grosTitreNeon"
            xalign 0.5


        frame:
            background "gui/LI_personnages/UI_sous description perso.webp"
            xsize 650
            xpos 1220
            ypos 130



            has vbox
            xpos 30
            ypos 15
            spacing 5

            hbox:
                text pl.name:
                    yalign 0.0
                    font "corbel.ttf"
                    size 40
                null:
                    width 15

                if persistent.interdit >= 1:
                    $ boutonInterdit = True
                else:
                    $ boutonInterdit = False

                imagebutton:
                    yoffset -5
                    at zoomLogoFree
                    insensitive "gui/logo_free_NOCENSITIVE.png"
                    idle "gui/logo_free_NOVALID.png"
                    hover "gui/logo_free_NOVALID.png"
                    selected_idle "gui/logo_free_VALID.png"
                    selected_hover "gui/logo_free_VALID.png"
                    sensitive boutonInterdit
                    selected pl.contenuInterdit
                    action [
                    SetVariable("pl.contenuInterdit", (False if pl.contenuInterdit == True else True)),
                    Function(invert_boolean_for_interdit),
                    Function(renpy.notify, [_("Taboo patch désactivé"), "notify"]) if pl.contenuInterdit else Function(renpy.notify, [_("Taboo patch activé"), "notify"])
                    ]



            text pl.description:
                yalign 0.0
                font "corbell.ttf"
                size 25

            grid 2 2:
                xspacing 30
                yspacing 3

                style_prefix "Grid"

                text _("Age :")
                text str(pl.age)

                text _("Orientation sexuelle :")
                text str(pl.orientationSexuelle)




        frame:
            hbox:
                ypos 180
                if pl.energiePendentif in range(-5000, -45 ):
                    xpos 0
                    add "gui/LI_personnages/bullet.webp"
                elif pl.energiePendentif in range(-45, -40):
                    xpos 25
                    add "gui/LI_personnages/bullet.webp"
                elif pl.energiePendentif in range(-40, -35):
                    xpos 50
                    add "gui/LI_personnages/bullet.webp"
                elif pl.energiePendentif in range(-35, -30):
                    xpos 75
                    add "gui/LI_personnages/bullet.webp"
                elif pl.energiePendentif in range(-30, -25):
                    xpos 100
                    add "gui/LI_personnages/bullet.webp"
                elif pl.energiePendentif in range(-25, -20):
                    xpos 125
                    add "gui/LI_personnages/bullet.webp"
                elif pl.energiePendentif in range(-20, -15):
                    xpos 150
                    add "gui/LI_personnages/bullet.webp"
                elif pl.energiePendentif in range(-15, -10):
                    xpos 175
                    add "gui/LI_personnages/bullet.webp"
                elif pl.energiePendentif in range(-10, -5):
                    xpos 200
                    add "gui/LI_personnages/bullet.webp"
                elif pl.energiePendentif in range(-5, 0):
                    xpos 225
                    add "gui/LI_personnages/bullet.webp"
                elif pl.energiePendentif in range(0, 5):
                    xpos 250
                    add "gui/LI_personnages/bullet.webp"
                elif pl.energiePendentif in range(5, 10):
                    xpos 275
                    add "gui/LI_personnages/bullet.webp"
                elif pl.energiePendentif in range(10, 15):
                    xpos 300
                    add "gui/LI_personnages/bullet.webp"
                elif pl.energiePendentif in range(15, 20):
                    xpos 325
                    add "gui/LI_personnages/bullet.webp"
                elif pl.energiePendentif in range(20, 25):
                    xpos 350
                    add "gui/LI_personnages/bullet.webp"
                elif pl.energiePendentif in range(25, 30):
                    xpos 375
                    add "gui/LI_personnages/bullet.webp"
                elif pl.energiePendentif in range(30, 35):
                    xpos 400
                    add "gui/LI_personnages/bullet.webp"
                elif pl.energiePendentif in range(35, 40 ):
                    xpos 425
                    add "gui/LI_personnages/bullet.webp"
                elif pl.energiePendentif in range(40, 50):
                    xpos 450
                    add "gui/LI_personnages/bullet.webp"
                elif pl.energiePendentif in range(50, 5000):
                    xpos 500
                    add "gui/LI_personnages/bullet.webp"

            background "gui/LI_personnages/1px.webp"
            xsize 660
            xpos 1250
            ypos 250
            add "gui/LI_personnages/good_bad.webp"




        frame:
            background "gui/LI_personnages/1px.webp"
            xsize 670
            ysize 100
            xpos 1220
            ypos 485

            has text _("Journal")

            if lang == "russian":
                style "grosTitreNeonCyrillique"
                yoffset 40
            else:
                style "grosTitreNeon"
            xalign 0.5




        frame:
            background "gui/LI_personnages/UI_sous description chronologoe.webp"
            xsize 650
            xpos 1220
            ypos 560




            has viewport id "pl"
            xmaximum 635
            ymaximum 340
            scrollbars "vertical"
            mousewheel True
            draggable True
            side_yfill True

            vbox:
                if pl.Progress:
                    for i in pl.Progress:
                        if i.Visible:
                            $ progress_time = i.progressTime.strftime("%A, %B %#d, %Y - %I:%M %p").capitalize() if persistent.lang == "english" else i.progressTime.strftime("%A %#d %B %Y - %H:%M").capitalize()
                            $ progress_color = i.progressColor

                            text progress_time + " :":
                                color progress_color
                                bold True
                                style "Progress"
                            text renpy.substitute(i.ProgressText, scope=None, translate=True) + "\n":
                                color progress_color
                                style "Progress"

            xpos 20
            ypos 60
            yinitial 1.0





        frame:
            background "gui/LI_personnages/1px.webp"
            xpos 1700
            ypos 995

            has button
            text _("SORTIR"):
                style "filtreNeon",
                size 30
            action Return()






    else:





        frame:
            background "gui/LI_personnages/1px.webp"
            xsize 670
            ysize 100
            xpos 1220
            ypos 0

            has text _("Compendium")

            if lang == "russian":
                style "grosTitreNeonCyrillique"
                yoffset 40
            else:
                style "grosTitreNeon"
            xalign 0.5



        frame:
            background "gui/LI_personnages/UI_sous description perso.webp"
            xsize 630
            xpos 1220
            ypos 130

            has vbox
            xpos 30
            ypos 15
            spacing 10

            text AllLI[ElementIndex].display_name:
                yalign 0.0
                font "corbel.ttf"
                size 40


            text AllLI[ElementIndex].description:

                yalign 0.0
                font "corbell.ttf"
                size 25


            grid 2 4:
                xspacing 30
                yspacing 3
                style_prefix "Grid"

                text _("Age :")
                text str(AllLI[ElementIndex].age)

                text _("Orientation sexuelle :")
                text str(AllLI[ElementIndex].liOrientationSexuelle):
                    style "unknown"

                text _("Taille :")
                text str(AllLI[ElementIndex].taille)

                text _("Tour de poitrine :")
                text str(AllLI[ElementIndex].poitrine)






        frame:
            background "gui/LI_personnages/1px.webp"
            xsize 670
            ysize 100
            xpos 1220
            ypos 485

            has text _("Journal")

            if lang == "russian":
                style "grosTitreNeonCyrillique"
                yoffset 40
            else:
                style "grosTitreNeon"
            xalign 0.5



        frame:
            background "gui/LI_personnages/UI_sous description chronologoe.webp"
            xsize 650
            xpos 1220
            ypos 560


            has viewport id "LI"
            xmaximum 635
            ymaximum 340
            scrollbars "vertical"
            mousewheel True
            draggable True
            side_yfill True


            vbox:
                if AllLI[ElementIndex].Progress:
                    for i in AllLI[ElementIndex].Progress:
                        if i.Visible:
                            $ progress_time = i.progressTime.strftime("%A, %B %#d, %Y - %I:%M %p").capitalize() if persistent.lang == "english" else i.progressTime.strftime("%A %#d %B %Y - %H:%M").capitalize()
                            $ progress_color = i.progressColor

                            text progress_time + " :":
                                color progress_color
                                bold True
                                style "Progress"
                            text renpy.substitute(i.ProgressText, scope=None, translate=True) + "\n":
                                color progress_color
                                style "Progress"


            xpos 20
            ypos 60
            yinitial 1.0





        frame:
            background "gui/LI_personnages/1px.webp"
            xpos 1700
            ypos 995

            has button
            text _("SORTIR"):
                style "filtreNeon",
                size 30
            action Return()





        if AllLI[ElementIndex].isFemale:

            $ Lexie.poilsPubien = persistent.lexieChatte_gallery
            $ Alex.poilsPubien = persistent.alexChatte_gallery
            $ Marya.poilsPubien = persistent.maryaChatte_gallery
            $ Carolina.poilsPubien = persistent.carolinaChatte_gallery

            frame:

                at zoomCustomChatte

                background "gui/LI_personnages/1px.webp"
                xpos 500
                ypos 0.5
                yoffset 200


                imagebutton:

                    idle "gui/choices/" + str(AllLI[ElementIndex].name) + "Pussy" + str(AllLI[ElementIndex].poilsPubien) + ".webp"
                    hover "gui/choices/" + str(AllLI[ElementIndex].name) + "Pussy" + str(AllLI[ElementIndex].poilsPubien) + ".webp"

                    insensitive "gui/choices/LIPussydefault.webp"

                    sensitive AllLI[ElementIndex].customChatte


                    action [Return(), Replay(AllLI[ElementIndex].name + "_customChatte")]




style Grid_text is text:
    size 25
    font "corbell.ttf"


style Progress is text:
    size 25
    font "corbell.ttf"


style filtreNeon is text:
    size 21
    color "#ffffff"
    font "corbell.ttf"
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

style filtreNeon_active:
    color "#ffffff"
    font "corbell.ttf"
    size 21
    outlines [   (13, "#31302f0a"), (12, "#342e2e0a"), (11, "#3a2d2d0a"), (10, "#422c2c0a"), 
                 (9, "#4d2c2c0a"), (8, "#5c2b2a64"), (7, "#6d2b2a96"), (6, "#802f2bc8"), 
                 (5, "#9737344f"), (4, "#b24945ff"), (3, "#c7635eff"), (2, "#da807bff"),  
                 (1, "#eebcb9ff") ]



style grosTitreNeon is text:

    size 120
    color "#ffffff"
    font "Grindline Demo.ttf"
    outlines [   (13, (49,47,47,2), 0, 0),  
                    (12, (52,46,46,5), 0, 0),
                    (11, (58,45,45,20), 0, 0),
                    (10, (80,15,14,30), 0, 0),
                    (9, (107,20,18,30), 0, 0),
                    (8, (92,43,42,80), 0, 0),
                    (7, (138,27,24,80), 0, 0),
                    (6, (173,42,36,180), 0, 0),
                    (5, (204,65,59,200), 0, 0),
                    (4, (230,96,88,200), 0, 0),
                    (3, (247,133,124,230), 0, 0),
                    (2, (254,174,167,230), 0, 0),  
                    (1, (255,238,238,230), 0, 0) ]

style grosTitreNeonCyrillique is text:

    size 60
    color "#ffffff"
    font "corbell.ttf"
    outlines [   (13, (49,47,47,2), 0, 0),  
                    (12, (52,46,46,5), 0, 0),
                    (11, (58,45,45,20), 0, 0),
                    (10, (80,15,14,30), 0, 0),
                    (9, (107,20,18,30), 0, 0),
                    (8, (92,43,42,80), 0, 0),
                    (7, (138,27,24,80), 0, 0),
                    (6, (173,42,36,180), 0, 0),
                    (5, (204,65,59,200), 0, 0),
                    (4, (230,96,88,200), 0, 0),
                    (3, (247,133,124,230), 0, 0),
                    (2, (254,174,167,230), 0, 0),  
                    (1, (255,238,238,230), 0, 0) ]





style unknown is text:
    size 25
    color "#ffffff"
    font "corbell.ttf"



style Label is text:
    size 25
    font "corbell.ttf"

transform half_size:
    zoom 0.4
transform zoomLogoFree:
    zoom 0.15
transform zoomCustomChatte:
    zoom 0.15

transform test_transform:
    blur 1.0


    linear 1.0 zoom 0.152
    linear 1.0 zoom 0.15
    repeat

transform LI_coeurBrise:
    blur 6.28
    matrixcolor SaturationMatrix(0.0)





screen LI_List():
    zorder 2

    frame:

        background "gui/LI_personnages/1px.webp"
        xpos 5
        ypos 80
        xsize 450
        ysize 980
        has viewport
        scrollbars "vertical"
        mousewheel True
        draggable True
        side_yfill True
        yadjustment scroll_position_menuli_liste_personnage


        vbox:
            xsize 427

            button:

                action [Function(SetNewPl, Value=False), SetVariable("LI_name", "Player"), Function(renpy.restart_interaction)]

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
                        $ plIconeFileName = "gui/LI_personnages/icones_personnages/LI_Jason_" + str(pl.ID_avatar) + ".webp"
                        add plIconeFileName:
                            xpos 7
                            ypos -7
                    vbox:
                        xsize 250
                        ysize 122

                        text renpy.substitute(pl.name, scope = None , translate = True).upper():
                            font "corbel.ttf"
                            xoffset -15
                            size 35
                            xalign 0.5
                            ypos 8
                            idle_color "#cccc"
                            hover_color "#fff"

                        text _("Le beau gosse"):
                            font "corbel.ttf"
                            xoffset -15
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

                    if pl.nbProgressRecu > 0:
                        frame:
                            left_padding 9
                            right_padding 10
                            top_padding 3
                            bottom_padding 3
                            background Frame("gui/LI_personnages/entree_LI.webp")
                            text str(pl.nbProgressRecu):
                                size 18
                                font "SF-Pro-Display-Light.OTF"



            if info_groupe == "Tous":
                $ indexed_AllLI = [(index, item) for index, item in enumerate(AllLI)]
                $ sorted_AllLI = sorted(indexed_AllLI, key=lambda x: renpy.substitute(x[1].display_name, scope=None, translate=True).lower())
                $ count = -1
                for original_index, q in sorted_AllLI:
                    $ count += 1
                    if q.isKnow:
                        $ actor_name = renpy.substitute(q.display_name, scope = None , translate = True).upper()
                        $ who_is = renpy.substitute(q.whoIs, scope = None , translate = True)
                        $ ID_avatar = str(q.ID_avatar)
                        $ name_lower = actor_name.lower()
                        if q.Matrice[q.ID_avatar-1][2] == "interdit":

                            $ avatarFileName = "images/interdit/LI/icones_personnages/LI_"+ q.name.lower() + "_" + ID_avatar + ".webp"
                        else:
                            $ avatarFileName = "gui/LI_personnages/icones_personnages/LI_"+ q.name.lower() + "_" + ID_avatar + ".webp"

                        button:
                            action [Function(SetNew, Value=False, InDex=count), SetVariable("LI_name", q.name), SetVariable("ElementIndex", original_index), Function(renpy.restart_interaction)]

                            xsize 401
                            ysize 122
                            idle_background "gui/LI_personnages/personnage_idle.webp"
                            hover_background "gui/LI_personnages/personnage_hover.webp"

                            if q.HatePoints <= -10:
                                at LI_coeurBrise

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
                                        font "corbel.ttf"
                                        xoffset -12
                                        size 35
                                        xalign 0.5
                                        ypos 8
                                        idle_color "#cccc"
                                        hover_color "#fff"

                                    text who_is:
                                        font "corbel.ttf"
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
                                if q.nbProgressRecu > 0:
                                    frame:
                                        left_padding 9
                                        right_padding 10
                                        top_padding 3
                                        bottom_padding 3
                                        background Frame("gui/LI_personnages/entree_LI.webp")
                                        text str(q.nbProgressRecu):
                                            size 18
                                            font "SF-Pro-Display-Light.OTF"

                            if q.LovePoints >= 10:
                                frame:
                                    yoffset 0
                                    xoffset 320
                                    xysize (64, 79)
                                    background None

                                    add Frame("gui/LI_personnages/Certified_LI.webp")


            elif info_groupe == "LI":
                $ indexed_AllLI = [(index, item) for index, item in enumerate(AllLI)]
                $ sorted_AllLI = sorted(indexed_AllLI, key=lambda x: renpy.substitute(x[1].display_name, scope=None, translate=True).lower())
                $ count = -1
                for original_index, q in sorted_AllLI:
                    $ count += 1
                    if q.isKnow and q.LovePoints >= 10:

                        $ actor_name = renpy.substitute(q.display_name, scope = None , translate = True).upper()
                        $ who_is = renpy.substitute(q.whoIs, scope = None , translate = True)
                        $ ID_avatar = str(q.ID_avatar)
                        $ name_lower = actor_name.lower()

                        if q.Matrice[q.ID_avatar-1][2] == "interdit":

                            $ avatarFileName = "images/interdit/LI/icones_personnages/LI_"+ q.name.lower() + "_" + ID_avatar + ".webp"
                        else:
                            $ avatarFileName = "gui/LI_personnages/icones_personnages/LI_"+ q.name.lower() + "_" + ID_avatar + ".webp"

                        button:
                            action [Function(SetNew, Value=False, InDex=count), SetVariable("LI_name", q.name), SetVariable("ElementIndex", original_index), Function(renpy.restart_interaction)]

                            xsize 401
                            ysize 122
                            idle_background "gui/LI_personnages/personnage_idle.webp"
                            hover_background "gui/LI_personnages/personnage_hover.webp"

                            if q.HatePoints <= -10:
                                at LI_coeurBrise

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
                                        font "corbel.ttf"
                                        xoffset -12
                                        size 35
                                        xalign 0.5
                                        ypos 8
                                        idle_color "#cccc"
                                        hover_color "#fff"

                                    text who_is:
                                        font "corbel.ttf"
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
                                if q.nbProgressRecu > 0:
                                    frame:
                                        left_padding 9
                                        right_padding 10
                                        top_padding 3
                                        bottom_padding 3
                                        background Frame("gui/LI_personnages/entree_LI.webp")
                                        text str(q.nbProgressRecu):
                                            size 18
                                            font "SF-Pro-Display-Light.OTF"


                            frame:
                                yoffset 0
                                xoffset 320
                                xysize (64, 79)
                                background None

                                add Frame("gui/LI_personnages/Certified_LI.webp")

            else:
                $ indexed_AllLI = [(index, item) for index, item in enumerate(AllLI)]
                $ sorted_AllLI = sorted(indexed_AllLI, key=lambda x: renpy.substitute(x[1].display_name, scope=None, translate=True).lower())
                $ count = -1
                for original_index, q in sorted_AllLI:
                    $ count += 1
                    if q.isKnow and info_groupe in q.Groupe:
                        $ actor_name = renpy.substitute(q.display_name, scope = None , translate = True).upper()
                        $ who_is = renpy.substitute(q.whoIs, scope = None , translate = True)
                        $ ID_avatar = str(q.ID_avatar)
                        $ name_lower = actor_name.lower()

                        if q.Matrice[q.ID_avatar-1][2] == "interdit":

                            $ avatarFileName = "images/interdit/LI/icones_personnages/LI_"+ q.name.lower() + "_" + ID_avatar + ".webp"
                        else:
                            $ avatarFileName = "gui/LI_personnages/icones_personnages/LI_"+ q.name.lower() + "_" + ID_avatar + ".webp"

                        button:
                            action [Function(SetNew, Value=False, InDex=count), SetVariable("LI_name", q.name), SetVariable("ElementIndex", original_index), Function(renpy.restart_interaction)]

                            xsize 401
                            ysize 122
                            idle_background "gui/LI_personnages/personnage_idle.webp"
                            hover_background "gui/LI_personnages/personnage_hover.webp"

                            if q.HatePoints <= -10:
                                at LI_coeurBrise

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
                                        font "corbel.ttf"
                                        xoffset -12
                                        size 35
                                        xalign 0.5
                                        ypos 8
                                        idle_color "#cccc"
                                        hover_color "#fff"

                                    text who_is:
                                        font "corbel.ttf"
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
                                if q.nbProgressRecu > 0:
                                    frame:
                                        left_padding 9
                                        right_padding 10
                                        top_padding 3
                                        bottom_padding 3
                                        background Frame("gui/LI_personnages/entree_LI.webp")
                                        text str(q.nbProgressRecu):
                                            size 18
                                            font "SF-Pro-Display-Light.OTF"

                            if q.LovePoints >= 10:
                                frame:
                                    yoffset 0
                                    xoffset 320
                                    xysize (64, 79)
                                    background None

                                    add Frame("gui/LI_personnages/Certified_LI.webp")






image glow_anim:
    "gui/glow_anim/1.webp" with Dissolve(0.5, alpha=True)
    pause 1
    "gui/glow_anim/2.webp" with Dissolve(0.5, alpha=True)
    pause 1
    "gui/glow_anim/3.webp" with Dissolve(0.5, alpha=True)
    pause 1
    "gui/glow_anim/4.webp" with Dissolve(0.5, alpha=True)
    pause 1
    "gui/glow_anim/5.webp" with Dissolve(0., alpha=True)
    pause 1
    repeat

screen LI_image():
    frame:
        background "gui/LI_personnages/1px.webp"
        xsize 787
        ysize 1080
        xpos 463
        ypos 0
        add "glow_anim"

        if LI_name == "Player":
            $ PlavatarFileName = "gui/LI_personnages/avatars/"+ "LI_" + LI_name.lower() + "_" + str(pl.ID_avatar) + ".webp"
            add PlavatarFileName
            if pl.NbAvatarMax > 1:
                hbox:
                    yalign 1.0
                    xalign 0.5
                    imagebutton:

                        auto "gui/LI_personnages/left_%s.webp"

                        action (SensitiveIf(pl.ID_avatar > 1), SetVariable("pl.ID_avatar", pl.ID_avatar-1), Function(renpy.restart_interaction))

                    imagebutton:

                        auto "gui/LI_personnages/right_%s.webp"

                        action (SensitiveIf(pl.ID_avatar < pl.NbAvatarMax), SetVariable("pl.ID_avatar", pl.ID_avatar+1), Function(renpy.restart_interaction))

        else:
            for q in AllLI:
                if q.name == LI_name:

                    $ actor = q
                    $ name_lower = q.name.lower()
                    $ ID_avatar = str(q.ID_avatar)
                    $ ElementIndex = q.IDkey


                    if q.isFemale:
                        $ poilsPubien = str(q.poilsPubien)
                    else:
                        $ poilsPubien = "default"


                    if q.Matrice[q.ID_avatar-1][2] == "interdit":

                        $ avatarFileName = "images/interdit/LI/portrait/" + "LI_" + name_lower + "_" + ID_avatar + "_" + poilsPubien + ".webp"
                    else:

                        $ avatarFileName = "gui/LI_personnages/avatars/" + "LI_" + name_lower + "_" + ID_avatar + "_" + poilsPubien + ".webp"


                    if q.HatePoints <= -10:
                        add avatarFileName at LI_coeurBrise
                    else:
                        add avatarFileName



                    if q.NbAvatarMax > 1:
                        hbox:
                            yalign 1.0
                            xalign 0.5
                            imagebutton:
                                auto "gui/LI_personnages/left_%s.webp"
                                action (SensitiveIf(q.find_prev_avatar() is not None), Function(Set_minus_avatar, q.name), Function(renpy.restart_interaction))

                            imagebutton:
                                auto "gui/LI_personnages/right_%s.webp"
                                action (SensitiveIf(q.find_next_avatar() is not None), Function(Set_plus_avatar, q.name), Function(renpy.restart_interaction))







init python:
    def get_filtre_style(groupe):
        if info_groupe == groupe:
            return "filtreNeon_active"
        else:
            return "filtreNeon"




screen LI_groupe():

    frame:
        background "gui/LI_personnages/1px.webp"
        xsize 500
        ysize 30
        xpos 0
        ypos 0


        has hbox
        yoffset -5
        yalign 0
        xalign 0
        spacing -25
        xpos 5

        button:
            text _("TOUS"):
                style get_filtre_style("Tous")

            action [SetVariable("info_groupe", "Tous"), Function(renpy.restart_interaction)]


        if CheckGroupeAvalible("Homme"):
            button:
                text _("HOMMES"):
                    style get_filtre_style("Homme")
                action [SetVariable("info_groupe", "Homme"), Function(renpy.restart_interaction)]


        if CheckGroupeAvalible("Femme"):
            button:
                text _("FEMMES"):
                    style get_filtre_style("Femme")
                action [SetVariable("info_groupe", "Femme"), Function(renpy.restart_interaction)]

        if CheckGroupeAvalible("LI"):
            button:
                text _("LI"):
                    style get_filtre_style("LI")
                action [SetVariable("info_groupe", "LI"), Function(renpy.restart_interaction)]



    frame:
        background "gui/LI_personnages/1px.webp"
        xsize 500
        ysize 30
        xpos 0
        ypos 0

        has hbox
        yoffset 28
        yalign 0.0
        xalign 0.0
        xpos 30
        spacing -25


        if CheckGroupeAvalible("Amis"):
            button:
                text _("AMIS"):
                    style get_filtre_style("Amis")
                action [SetVariable("info_groupe", "Amis"), Function(renpy.restart_interaction)]


        if CheckGroupeAvalible("Voisinage"):
            button:
                text _("VOISINAGE"):
                    style get_filtre_style("Voisinage")
                action [SetVariable("info_groupe", "Voisinage"), Function(renpy.restart_interaction)]


        if CheckGroupeAvalible("Travail"):
            button:
                text _("TRAVAIL"):
                    style get_filtre_style("Travail")
                action [SetVariable("info_groupe", "Travail"), Function(renpy.restart_interaction)]


        if CheckGroupeAvalible("Famille"):
            button:
                text _("FAMILLE"):
                    style get_filtre_style("Famille")
                action [SetVariable("info_groupe", "Famille"), Function(renpy.restart_interaction)]


        if CheckGroupeAvalible("Autre"):
            button:
                text _("AUTRES"):
                    style get_filtre_style("Autre")
                action [SetVariable("info_groupe", "Autre"), Function(renpy.restart_interaction)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
