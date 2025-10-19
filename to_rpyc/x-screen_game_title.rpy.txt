screen screen_game_title():
    modal True
    add "#000" at transform_game_title_black
    add "gui/main_title_1.webp" align (0.5, 0.5) at transform_game_title_1
    add "gui/main_title_2.webp" align (0.5, 0.5) at transform_game_title_2

    timer 11 action Return()

    key "game_menu" action NullAction()
    key "dismiss" action Return()

transform transform_game_title_black:
    on show:
        alpha 0.0
        parallel:
            linear 3.0 alpha 1.0

transform transform_game_title_1:
    subpixel True
    on show:
        alpha 0.0
        zoom 0.7

        parallel:
            linear 4.0 alpha 1.0
        parallel:
            linear 7.0 zoom 1.0

        pause 1.0
        linear 2.0 alpha 0.0

transform transform_game_title_2:
    subpixel True
    on show:
        alpha 0.0
        zoom 0.7

        parallel:
            linear 7.0 zoom 1.0
        parallel:
            pause 6.0
            linear 1.0 alpha 1.0

        pause 1.0
        linear 2.0 alpha 0.0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
