define config.name = _("Our Red String")
define chapters = 14

default preferences.fullscreen = True
define gui.show_name = False

default persistent.include_disabled = True
default greyed_out_disabled = False

default persistent.gallery_force_unlock = False
default persistent.cheat_rollback = False

init:
    if persistent.include_disabled:
        $ config.menu_include_disabled = True
    elif True:
        $ config.menu_include_disabled = False

label after_load:
    if persistent.include_disabled:
        if greyed_out_disabled:
            $ config.menu_include_disabled = False
        else:
            $ config.menu_include_disabled = True
    else:
        $ config.menu_include_disabled = False

init python:
    def greyed_out_setting():
        if persistent.include_disabled:
            if greyed_out_disabled:
                config.menu_include_disabled = False
            else:
                config.menu_include_disabled = True
        else:
            config.menu_include_disabled = False

    original_block_rollback = renpy.block_rollback  

    def cheat_rollback():                           
        if persistent.cheat_rollback:
            def unren_noblock( *args, **kwargs ):
                return
            renpy.block_rollback = unren_noblock
        else:
            renpy.block_rollback = original_block_rollback  

    if persistent.cheat_rollback:                   
        def unren_noblock( *args, **kwargs ):
            return
        renpy.block_rollback = unren_noblock
    else:
        pass

    # HAPUS semua setting bahasa di init python
    # Biarkan persistent.language = None (default English)

init 999:
    python:
        update_all_gallery_images()

define config.version = "v14.1.3"

define gui.about = _p("""
""")

define build.name = "OurRedString"

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.main_menu_music = "music/main_menu.mp3"

define config.enter_transition = fps
define config.exit_transition = fps

define config.intra_transition = fps

define config.after_load_transition = Fade(0.5, 0.5, 0.5)

define config.end_game_transition = Fade(0.5, 0.5, 0.5)

define config.window = "auto"

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

default preferences.text_cps = 80

default preferences.afm_time = 15

define config.save_directory = "RedString-1574621830"

define config.window_icon = "gui/window_icon.png"

init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.example', None) 
    build.classify('game/cache/**', None) 
    build.classify('game/saves/**', None) 
    build.classify('**/_ignore/**', None) 
    build.classify('**desktop.ini', None) 

    build.archive("scripts", "all")
    build.classify('game/scripts/**', 'scripts')

    build.archive("gui", "all")
    build.classify('game/gui/**', 'gui')

    build.archive("images", "all")
    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")
    build.classify("game/**.webp", "images")

    build.archive("audio", "all")
    build.classify('game/**.ogg', 'audio')
    build.classify('game/**.mp3', 'audio')
    build.classify('game/**.wav', 'audio')

    build.archive("videos", "all")
    build.classify('game/**.webm', 'videos')
    build.classify('game/**.mkv', 'videos')
    build.classify('game/**.mp4', 'videos')
    build.classify('game/**.mov', 'videos')

    build.archive("fonts", "all")
    build.classify('game/fonts/**', 'fonts')
    build.classify('game/**.ttf', 'fonts')
    build.classify('game/**.otf', 'fonts')

    build.documentation('*.html')
    build.documentation('*.txt')
