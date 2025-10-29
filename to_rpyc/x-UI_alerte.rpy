transform UI_transform:
    on show:
        alpha 1.0
        xpos -120
        ypos 0

        linear 0.2 xpos 0
    on hide:
        linear 0.2 xpos -120

screen UI_alerte_eye():
    zorder 100
    imagebutton:
        at UI_transform
        idle "UI_alerte_eye"

screen UI_alerte_hand():
    zorder 100
    imagebutton:
        at UI_transform
        idle "UI_alerte_hand"





screen alt_cam():
    zorder 100
    imagebutton:
        focus_mask True
        idle "alt_cam_right_left_idle"
        hover "alt_cam_right_left_hover"
        action Function(renpy.call, label="alt_cam_toggle")






screen tuto_01():

    style_prefix "tuto"

    frame:
        at tuto_transform

        xsize 900

        has vbox
        spacing 15

        text _("Ce symbole indique qu’il est possible d’interagir avec la scène.")
        text _("À l'aide du pointeur de la souris, cherchez sur l’écran, là ou les zone(s) d’interaction.")
        text _("Dès que ce curseur {image=mouse_eye} apparaît, vous pouvez effectuer l’action \"Regarder\".")
        text _("Très utile pour se focaliser sur un point précis ou déclencher des actions de voyeurisme.")
        text _("Restez vigilant, il est possible que vous ne soyez pas avertis qu’une zone \"Regarder\" existe.")
        text _("{b}Restez curieux !{/b}")

    timer 20 action Return()

    imagebutton:

        at tuto_transform

        xoffset -130
        yoffset -50

        focus_mask True
        idle "tuto_eye_closed"
        action Return()

transform tuto_transform:
    on show:
        alpha 1.0
        xpos -600
        ypos 50

        linear 0.5 xpos 150
    on hide:
        linear 0.5 xpos -1200

style tuto_text:
    font "corbel.ttf"
    size 25
    line_spacing 2
    kerning 0

style tuto_frame:
    background Frame("gui/tuto/background_tuto.png", gui.tuto_frame_borders, tile=gui.frame_tile)
    padding (45, 30, 65, 30)

image mouse_eye:
    "gui/mouse_eye.webp"



screen tuto_02():

    style_prefix "tuto"

    frame:
        at tuto_transform

        xsize 900

        has vbox
        spacing 15

        text _("Ce symbole apparaît pour changer l'angle de la caméra.")

    timer 20 action Return()

    imagebutton:

        at tuto_transform

        xoffset -130
        yoffset -50

        focus_mask True
        idle "tuto_eye_closed"
        action Return()





screen tuto_03():

    style_prefix "tuto"

    frame:
        at tuto_transform

        xsize 900

        has vbox
        spacing 15

        text _("Lorsque des choix vous sont proposés et qu’ils apparaissent en {color=#7daeff}bleu{/color}, alors vous êtes en présence de choix importants.")
        text _("Ces choix ont une influence majeure sur le déroulement de l’histoire et sur les relations que vous entretenez avec les personnes qui vous entourent.")
        text _("Les personnages impactés par votre choix vous seront présentés par des icônes les représentant.")

    timer 20 action Return()

    imagebutton:

        at tuto_transform

        xoffset -130
        yoffset -50

        focus_mask True
        idle "tuto_eye_closed"
        action Return()


transform tuto_choix:
    on show:
        alpha 1.0
        xpos -600
        ypos 0

        linear 0.5 xpos 0




screen rappel():

    style_prefix "tuto"

    frame:
        at tuto_transform

        xsize 900

        has vbox
        spacing 15

        text _("Avez-vous bien regardé la scène précédente ?")


    timer 20 action Return()

    imagebutton:

        at tuto_transform

        xoffset -130
        yoffset -50

        focus_mask True
        idle "tuto_eye_closed"
        action Return()








screen updateSave():

    modal True

    style_prefix "tuto"

    frame:

        xpos 50
        ypos 50
        padding (45, 30, 45, 45)

        has vbox

        text _("Vous devez mettre à jour votre sauvegarde."):
            xsize 250
            text_align 0.5
            xcenter 0.5

        imagebutton:

            xcenter 0.5
            yoffset 20
            mouse "hand"
            focus_mask True
            idle "gui/updateSave.png"
            hover "gui/updateSave_hover.png"
            action Call("updateSave")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
