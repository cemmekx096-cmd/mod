screen screen_tutorial(imgs):
    tag tutorial_screen
    modal True

    add "gui/%s.webp" % imgs[0]



    key "game_menu" action NullAction()
    key "dismiss":
        action Play("ch_one", "sfx/paper_click.mp3"), If(len(imgs) < 2,
            true=Return(),
            false=Show('screen_tutorial', transition=short, imgs=imgs[1:])
        )


label label_tutorial(imgs):
    call screen screen_tutorial(imgs) with dissolve
    show screen screen_tutorial([imgs[len(imgs) - 1]])
    hide screen screen_tutorial with short

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
