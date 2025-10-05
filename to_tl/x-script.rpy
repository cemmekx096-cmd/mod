






label splashscreen:

    scene tmj
    play sound "sound effects/sting-afterall.wav"
    $ renpy.pause(7, hard=True)
    play music "music/despair-and-triumph.ogg"
    scene adults_only
    with blinds
    with Dissolve(1.0)
    $ renpy.pause(4, hard=True)
    scene clicktocontinue
    with blinds
    call screen clicktocontinue

    return


label start:
    $ _game_menu_screen = "navigation"
    show screen qmenu

    jump prStart




    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
