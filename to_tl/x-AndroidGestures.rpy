define config.gl2 = False
define config.hw_video = False
define quick_menu = True
define config.has_autosave = True

define config.autosave_on_quit = True
define config.autosave_on_choice = True
define config.save_on_mobile_background = True

define config.language = "english"
define config.allow_skipping = True
define config.hard_rollback_limit = 100


init python:
    config.gestures["n"] = "game_menu"
    config.gestures["s"] = "hide_windows"
    config.gestures["e"] = "skip"
    config.gestures["w"] = "rollback"

style input_window:
    variant "touch"
    yalign .1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
