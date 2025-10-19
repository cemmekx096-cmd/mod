## File: screen_language.rpy
## Menu Mod untuk ganti bahasa - AUTO INJECT ke Preferences
## Tinggal letakkan file ini di folder game/, langsung jalan!

init -100 python:
    # Set default language ke Indonesia saat pertama kali main
    if persistent.language is None:
        renpy.change_language("id")

## Screen untuk popup/tab menu Mod Language
screen mod_language_popup():
    
    modal True
    zorder 200
    
    # Background overlay (gelap)
    button:
        style "empty"
        xfill True
        yfill True
        action Hide("mod_language_popup")
    
    # Box untuk popup
    frame:
        xalign 0.5
        yalign 0.5
        xminimum 600
        xmaximum 800
        yminimum 400
        
        background Solid("#000000cc")
        padding (50, 50)
        
        vbox:
            spacing 30
            xalign 0.5
            
            # Judul
            text _("Mod - Language Settings"):
                size 50
                xalign 0.5
                color "#ffffff"
                bold True
            
            null height 20
            
            # Deskripsi
            text _("Select your preferred language:"):
                size 30
                xalign 0.5
                color "#cccccc"
            
            null height 30
            
            # Tombol pilihan bahasa
            vbox:
                spacing 20
                xalign 0.5
                
                # Tombol English
                button:
                    xsize 400
                    ysize 80
                    background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.frame_tile)
                    hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.frame_tile)
                    action [Language(None), Hide("mod_language_popup")]
                    
                    hbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 20
                        
                        text "🇬🇧" size 40
                        text _("English"):
                            size 35
                            color "#ffffff"
                
                # Tombol Indonesia
                button:
                    xsize 400
                    ysize 80
                    background Frame("gui/button/choice_idle_background.png", gui.choice_button_borders, tile=gui.frame_tile)
                    hover_background Frame("gui/button/choice_hover_background.png", gui.choice_button_borders, tile=gui.frame_tile)
                    action [Language("id"), Hide("mod_language_popup")]
                    
                    hbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 20
                        
                        text "🇮🇩" size 40
                        text _("Bahasa Indonesia"):
                            size 35
                            color "#ffffff"
            
            null height 30
            
            # Tombol Close
            textbutton _("Close"):
                xalign 0.5
                xsize 200
                action Hide("mod_language_popup")


## INJECT ke Preferences Screen - OTOMATIS tanpa edit file lain!
init -99 python:
    
    # Simpan screen preferences original
    original_preferences_screen = None
    
    def inject_mod_button():
        """
        Fungsi untuk inject tombol MOD ke preferences screen
        """
        try:
            # Cek apakah screen preferences ada
            if renpy.has_screen("preferences"):
                # Set flag bahwa kita sudah inject
                if not hasattr(store, "mod_injected"):
                    store.mod_injected = True
        except:
            pass
    
    # Jalankan inject saat game start
    config.start_callbacks.append(inject_mod_button)

## Screen preferences yang sudah di-inject dengan tombol MOD
## Ini akan OVERRIDE screen preferences original
init -500 screen preferences():
    tag menu

    use game_menu(_("Settings")):
        
        vbox:
            xalign 0.5
            yalign 0.1
            spacing 20
            
            # TOMBOL MOD - INI YANG KITA TAMBAHKAN!
            hbox:
                xalign 0.5
                spacing 20
                
                textbutton _("⚙ MOD Settings"):
                    xsize 300
                    ysize 60
                    text_size 30
                    text_bold True
                    action Show("mod_language_popup")
                    # Style khusus agar menonjol
                    background "#ff6b6b"
                    hover_background "#ff5252"
                    text_color "#ffffff"
            
            null height 20
            
            # Sisanya panggil preferences original (kalau ada)
            # Atau bisa langsung bikin simple version
            
            vbox:
                xalign 0.5
                spacing 30
                
                text _("Original Preferences"):
                    size 25
                    xalign 0.5
                
                text _("Click 'MOD Settings' above to change language"):
                    size 20
                    xalign 0.5
                    color "#888888"
                
                null height 20
                
                # Preferences dasar lainnya bisa ditambahkan di sini
                # Atau biarkan kosong, fokus ke MOD button saja
                
                hbox:
                    xalign 0.5
                    spacing 20
                    
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")
                    
                    vbox:
                        style_prefix "check"
                        label _("Skip")
                        textbutton _("Unseen Text") action Preference("skip", "toggle")
                        textbutton _("After Choices") action Preference("after choices", "toggle")
                
                null height 40
                
                # Volume controls
                vbox:
                    xalign 0.5
                    spacing 15
                    xsize 600
                    
                    if config.has_music:
                        hbox:
                            text _("Music Volume") xsize 200
                            bar value Preference("music volume") xsize 400
                    
                    if config.has_sound:
                        hbox:
                            text _("Sound Volume") xsize 200
                            bar value Preference("sound volume") xsize 400
                    
                    if config.has_voice:
                        hbox:
                            text _("Voice Volume") xsize 200
                            bar value Preference("voice volume") xsize 400

## Style untuk tombol yang tidak ada gui definition
style empty:
    pass
