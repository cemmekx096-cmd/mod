






label alt_cam_toggle:

    if alt_cam == True:
        $ alt_cam = False
    else:
        $ alt_cam = True

    call alt_cam_switch from _call_alt_cam_switch
    return


label alt_cam_switch:
    if alt_cam == True:
        $ renpy.scene()
        $ renpy.show(cam_secondaire)
        extend ""
    else:
        $ renpy.scene()
        $ renpy.show(cam_principale)
        extend ""
    return





screen hide_icon():
    zorder 100
    imagebutton:
        focus_mask True
        idle "gui/hide_icon_idle.webp"
        hover "gui/hide_icon_hover.webp"
        action HideInterface()


screen prologue_s01_09():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/prologue_s01_09_idle.webp")
        action Call ("Prologue_s01_09_b")

label Prologue_s01_09_b:
    hide screen prologue_s01_09
    hide screen UI_alerte_eye

    scene prologue_s01_09_b with dissolve
    pause
    return

screen prologue_s01_09_a():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/prologue_s01_09_a_idle.webp")
        action Call ("Prologue_s01_09_c")

label Prologue_s01_09_c:
    hide screen prologue_s01_09_a
    hide screen UI_alerte_eye

    scene prologue_s01_09_c with dissolve
    pause
    return

screen prologue_s02_03_c():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/prologue_s02_03_c_idle.webp")
        action Call ("Prologue_s02_03_c")

label Prologue_s02_03_c:
    hide screen prologue_s02_03_c
    scene prologue_s02_03_bonus with dissolve

    if persistent.gallery_voyeur_01 == True:
        pass
    else:
        $ update_achievement("voyeur", trans=achievement_transform)
        $ persistent.achievements_voyeur += 1

        $ renpy.music.set_volume(1, 0, channel = "sfx2")
        play sfx2 achievement
        $ persistent.gallery_voyeur_01 = True

    pause

    return


screen prologue_s03_07_a():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/prologue_s03_07_a_idle.webp")
        action Call ("Prologue_S03_07_b")

label Prologue_S03_07_b:
    hide screen prologue_s03_07_a

    scene prologue_s03_07_b with dissolve
    show screen UI_alerte_eye
    show screen prologue_s03_07_b
    jap p "Hummm je n'imaginais pas qu'elle avait un si joli petit cul !"

    $ choices.append("regarderLexieWC")



    hide screen prologue_s03_07_b
    hide screen UI_alerte_eye

    if "aJouerAvecLeFeu" in choices:
        pass
    else:


        if persistent.gallery_lexie_04 == False:
            $ renpy.notify([_("Image galerie débloquée"), "unlock"])
        else:
            pass
        $ persistent.gallery_lexie_04 = True


        $ update_dateJeu(datetime(2021, 5, 22, 15, 22, 0))

        $ Lexie.add_progress("lexie035", _("Elle a laissé la porte de la salle de bain entrouverte et j'ai jeté un rapide coup d'œil. J'ai vu ses fesses."))

    return

screen prologue_s03_07_b():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/prologue_s03_07_b_idle.webp")
        action Call ("Prologue_S03_07_c")

label Prologue_S03_07_c:
    hide screen prologue_s03_07_b
    hide screen UI_alerte_eye

    scene prologue_s03_07_c with dissolve

    stop music fadeout 3

    play sfx1 scratch
    $ renpy.music.set_volume(0.4, 0.0, channel = "sfx1")
    with hpunch

    jap p "Ohhh putain, à jouer avec le feu ..."
    ja -p "[lexie] on descend, tu nous rejoins ?"
    l "Oui, oui, je vous ai dit que j'arrivais."

    $ update_dateJeu(datetime(2021, 5, 22, 15, 22, 0))

    $ Lexie.add_progress("lexie036", _("Elle a laissé la porte de la salle de bain entrouverte et je suis resté un peu trop longtemps à la regarder. J'ai failli me faire griller."))

    $ choices.append("aJouerAvecLeFeu")

    return


screen prologue_s04_02_d_1():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/prologue_s04_02_d_1_idle.webp")
        action Call ("prologue_s04_02_d_2")

label prologue_s04_02_d_2:
    hide screen prologue_s04_02_d_1
    hide screen UI_alerte_eye


    scene prologue_s04_02_d_2 with dissolve
    pause


    if persistent.gallery_michelle_02 == False:
        $ renpy.notify([_("Image galerie débloquée"), "unlock"])
    else:
        pass
    $ persistent.gallery_michelle_02 = True


    return


screen prologue_s04_10_c():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/prologue_s04_10_c_idle.webp")
        action Call ("prologue_s04_10_e")

label prologue_s04_10_e:
    hide screen prologue_s04_10_c
    hide screen UI_alerte_eye

    scene prologue_s04_10_e with dissolve
    pause


    scene prologue_s04_11 with dissolve
    pause


    scene prologue_s04_12 with dissolve

    play sfx1 scratch
    $ renpy.music.set_volume(0.4, 0.0, channel = "sfx1")
    with hpunch

    $ avatarLexie = "avatar/Avatar_Lexie_NoBra.webp"

    l "Non mais qu'est-ce que tu fais ?"





    play music retrosoul
    $ renpy.music.set_volume(0.1, 3, channel = "music")

    l "Retourne toi tout de suite coquin !"
    ja "Oupsss !{w} pardon."
    jap p "Merde !{p}A jouer avec le feu, je me suis fait griller."


    scene prologue_s04_13 with dissolve
    jap p "Whaouwwww !{w} Je n'arrive pas à le croire.{w} [lexie] est quasiment nue dans mon salon."

    scene prologue_s04_13_a with dissolve
    jap p "Et moi je la regarde se changer."
    ja "Elle va me tuer."


    scene prologue_s04_10_b
    with dissolve
    l "J'espère que tu t'es bien rincé l’œil !{w} Ça t'a plu ?"

    if "prefereLesGrosSeins" in choices:
        l "Toi qui aime les gros seins, t'es mal servi avec moi, t'as vu ?"
        l "Les miens ne sont pas très gros."
        jap p "Mais c'est qu'elle me lance des piques..."
    else:
        l "Toi qui aime les petits seins, tu dois aimer les miens non ?{w} Tu les trouves comment ?"
        l "Moi je trouve qu'ils ne sont pas très gros."
        jap p "Heuuuu !{w} je dois répondre là !?!"
        ja -p "J'avoue, je ne regrette pas de t'avoir regardé. Excuse-moi !"
        l "Petit vicieux !"

    l "Tu peux regarder maintenant, j'ai enfilé ton tee-shirt."
    l "Il a l'air de m'aller non ?"


    scene prologue_s04_14
    with dissolve
    ja "Ouais il te va très bien."

    $ avatarLexie = "avatar/Avatar_Lexie_Tshirt.webp"

    l "Hum !{w} Il est court !{w} Tu vas pouvoir te rincer l’œil encore un petit peu"
    jap p "Mais elle me chauffe !"
    jap p "Elle n'a pas l'air de trop m'en vouloir."

    $ choices.append("regarderLexieSeChanger")
    $ update_dateJeu(datetime(2021, 5, 22, 18, 30, 0))
    $ Lexie.add_progress("lexie037", _("La tentation était trop grande. Je l'entendais se changer tout juste derrière moi et je me suis retourné pour voir ça. Je ne regrette pas, sa dentelle était superbe. Mais je me suis fait grillé. [lexie] l'a plutôt bien pris, elle n'a pas l'air très pudique."))

    return



screen prologue_s04_10_d():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/prologue_s04_10_d_idle.webp")
        action Call ("Prologue_s04_10_d_bis")

label Prologue_s04_10_d_bis:
    hide screen prologue_s04_10_d
    scene prologue_s04_10_d_bis with dissolve

    show screen prologue_s04_10_d_bis
    jap p "Oh ! Mais qui est-ce ?"
    hide screen prologue_s04_10_d_bis

    return


screen prologue_s04_10_d_bis():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/prologue_s04_10_d_bis_idle.webp")
        action Call ("Prologue_s04_10_d_bis_bonus")

label Prologue_s04_10_d_bis_bonus:
    hide screen prologue_s04_10_d_bis
    scene prologue_s04_10_d_bis_bonus with dissolve
    jap p "Hummm!{w} Intéressant !"
    pause

    if _in_replay:
        pass
    else:
        if persistent.gallery_voyeur_02 == True:
            pass
        else:
            $ update_achievement("voyeur", trans=achievement_transform)
            $ persistent.achievements_voyeur += 1
            $ renpy.music.set_volume(1, 0, channel = "sfx2")
            play sfx2 achievement
            $ persistent.gallery_voyeur_02 = True
    pause

    return


screen prologue_s05_06_c():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/prologue_s05_06_idle.webp")
        action Call ("prologue_s05_06_c_eye")

label prologue_s05_06_c_eye:

    hide screen prologue_s05_06_c
    scene prologue_s05_06_c_eye with dissolve

    ja "[marvin] !{w} La fenêtre éclairée en bas à gauche,{w} regarde !"
    show screen prologue_s05_06_c_eye
    m "Pas mal du tout !"
    hide screen prologue_s05_06_c_eye

    return


screen prologue_s05_06_c_eye():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/prologue_s05_06_c_eye_idle.webp")
        action Call ("prologue_s05_06_c_eye_01")

label prologue_s05_06_c_eye_01:
    hide screen prologue_s05_06_c_eye
    scene prologue_s05_06_c_eye_01 with dissolve
    m "Putain !{w} Elle se matte la chatte !"
    pause

    if _in_replay:
        pass
    else:
        if persistent.gallery_voyeur_03 == True:
            pass
        else:
            $ update_achievement("voyeur", trans=achievement_transform)
            $ persistent.achievements_voyeur += 1
            $ renpy.music.set_volume(1, 0, channel = "sfx2")
            play sfx2 achievement
            $ persistent.gallery_voyeur_03 = True
    pause

    return

screen prologue_s06_03_b():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/prologue_s06_03_b_idle.webp")
        action Call ("prologue_s06_03_c")

label prologue_s06_03_c:
    hide screen prologue_s06_03_b

    scene prologue_s06_03_c with dissolve
    hide screen UI_alerte_eye    
    pause
    return

screen prologue_s06_33_a_bas():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/prologue_s06_33_a_culotte_idle.webp")
        action Call ("prologue_s06_33_b")

label prologue_s06_33_b:
    hide screen prologue_s06_33_a_bas
    hide screen prologue_s06_33_a_haut

    scene prologue_s06_33_b with dissolve
    hide screen UI_alerte_eye    
    $ choices.append("regarderCulotteLexieLit")
    pause
    return

screen prologue_s06_33_a_haut():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/prologue_s06_33_a_hautlexie_idle.webp")
        action Call ("prologue_s06_33_c")

label prologue_s06_33_c:
    hide screen prologue_s06_33_a_bas
    hide screen prologue_s06_33_a_haut

    scene prologue_s06_33_c with dissolve
    hide screen UI_alerte_eye    
    pause
    return


screen prologue_s07_19_a():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/prologue_s07_19_a_idle.webp")
        action Call ("prologue_s07_19_e")

label prologue_s07_19_e:
    hide screen prologue_s07_19_a

    $ avatarVanille = "avatar/Avatar_vanille_joker.webp"


    scene prologue_s07_19_e with dissolve
    hide screen UI_alerte_eye
    vap p "Te revoilà ! Tu brilles enfin de mille feux."

    scene prologue_s07_20_c_ooo with dissolve
    vap p "Ton sommeil a été long, trop long !"

    scene prologue_s07_20_b_ooo with dissolve
    vap p "Je vais venir te rendre visite [pendentif]. Ce n'est qu'une question de temps."
    vap p "Le maître veut savoir si tu as retrouvé toutes tes capacités"

    scene prologue_s07_20_a_ooo with dissolve
    stop music fadeout 6
    vap p "Ne t'éloigne pas trop [jason]. J'arrive."

    pause
    return


screen prologue_s08_26_b():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/prologue_s08_26_b_idle.webp")
        action Call ("prologue_s08_26_b")

label prologue_s08_26_b:
    hide screen prologue_s08_26_b


    scene prologue_s08_26_c with dissolve
    hide screen UI_alerte_eye
    $ choices.append("tatooMainInconnu")
    pause
    return




screen prologue_s09_05_c_GF():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/prologue_s09_05_c_idle.webp")
        action Call ("prologue_s09_05_c_GF")

label prologue_s09_05_c_GF:
    hide screen prologue_s09_05_c_GF
    hide screen UI_alerte_eye


    show rita01:
        linear 6.0 yalign 1.0
        linear 1.0 yalign 0.1
        repeat 1
    $ renpy.pause (7)
    pause




    if persistent.gallery_rita_01 == False:

        $ renpy.notify([_("Image galerie débloquée"), "unlock"])
    else:
        pass
    $ persistent.gallery_rita_01 = True


    return




screen prologue_s11_00_2_d_GF():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/prologue_s11_00_2_d_idle.webp")
        action Call ("prologue_s11_00_2_d_GF")

label prologue_s11_00_2_d_GF:
    hide screen prologue_s11_00_2_d_GF
    hide screen UI_alerte_eye 


    show kateb01:
        linear 6.0 yalign 1.0
        linear 1.0 yalign 0.1
        repeat 1
    $ renpy.pause (7)
    pause




    if persistent.gallery_kateb_01 == False:

        $ renpy.notify([_("Image galerie débloquée"), "unlock"])
    else:
        pass
    $ persistent.gallery_kateb_01 = True


    return




screen prologue_s13_07_g_GF():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/prologue_s13_07_g_idle.webp")
        action Call ("prologue_s13_07_g_GF")

label prologue_s13_07_g_GF:
    hide screen prologue_s13_07_g_GF
    hide screen UI_alerte_eye 


    show alex01:
        linear 6.0 yalign 1.0
        linear 1.0 yalign 0.1
        repeat 1
    $ renpy.pause (7)
    pause




    if persistent.gallery_alex_01 == False:

        $ renpy.notify([_("Image galerie débloquée"), "unlock"])
    else:
        pass
    $ persistent.gallery_alex_01 = True


    return




screen prologue_s13_23_a_GF():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/prologue_s13_23_a_idle.webp")
        action Call ("prologue_s13_23_a_GF")

label prologue_s13_23_a_GF:
    hide screen prologue_s13_23_a_GF
    hide screen UI_alerte_eye 


    show kate01:
        linear 6.0 yalign 1.0
        linear 1.0 yalign 0.1
        repeat 1
    $ renpy.pause (7)
    pause




    if persistent.gallery_kate_01 == False:

        $ renpy.notify([_("Image galerie débloquée"), "unlock"])
    else:
        pass
    $ persistent.gallery_kate_01 = True


    return




screen bonus01_s01_09_c():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/Bonus01_S01_09_c_idle.webp")
        action Call ("bonus01_s01_09_d")

label bonus01_s01_09_d:
    hide screen bonus01_s01_09_c
    hide screen UI_alerte_eye

    scene bonus01_s01_09_d with dissolve
    pause
    return


screen bonus01_s01_13_d():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/Bonus01_S01_13_d_idle.webp")
        action Call ("bonus01_s01_13_f")

label bonus01_s01_13_f:
    hide screen bonus01_s01_13_d
    hide screen UI_alerte_eye

    scene bonus01_s01_13_f with dissolve
    pause
    return


screen bonus01_s01_16_a_d():
    imagebutton:
        mouse "look"
        focus_mask True
        idle ("roam/Bonus01_S01_16_a_d_idle.webp")
        action Call ("bonus01_s01_16_a_e")

label bonus01_s01_16_a_e:
    hide screen bonus01_s01_16_a_d
    hide screen UI_alerte_eye

    scene bonus01_s01_16_a_e with dissolve
    pause


    if persistent.gallery_lexie_13a == False:

        $ renpy.notify([_("Image galerie débloquée"), "unlock"])
    else:
        pass
    $ persistent.gallery_lexie_13a = True

    pause


    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
