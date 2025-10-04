













define config.name = _("Pale Carnations")





define gui.show_name = False




define config.version = "Ch4Up6"





define gui.about = _p("""
""")






define build.name = "PaleCarnations"







define config.has_sound = True
define config.has_music = True
define config.has_voice = True













define config.main_menu_music = "music/despair-and-triumph.ogg"










define config.enter_transition = dissolve
define config.exit_transition = dissolve




define config.intra_transition = dissolve




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 0





default preferences.afm_time = 15
















define config.save_directory = "PaCaGame-1554919452"






define config.window_icon = "gui/icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)









    build.documentation('*.html')
    build.documentation('*.txt')



















    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("audio", "all")
    build.classify("game/**.rpy", "scripts")
    build.classify("game/**.rpyc", "scripts")
    build.classify("game/**.ogg", "audio")
    build.classify("game/**.wav", "audio")
    build.classify("game/**.mp3", "audio")
    build.classify("game/**.webm", "images")
    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")
    build.classify("game/**.webp", "images")


    renpy.music.register_channel("menu_click", "sfx", False)
    renpy.music.register_channel("hover_start", "sfx", False)
    renpy.music.register_channel("hover_load", "sfx", False)
    renpy.music.register_channel("hover_extra", "sfx", False)
    renpy.music.register_channel("hover_settings", "sfx", False)
    renpy.music.register_channel("hover_exit", "sfx", False)
    renpy.music.register_channel("ambient","sfx",True,tight=True)
    renpy.music.register_channel("ambient2","sfx",True,tight=True)
    renpy.music.register_channel("ambient3","sfx",True,tight=True)
    renpy.music.register_channel("sound2", "sfx", False)


define config.movie_mixer = "sfx"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
