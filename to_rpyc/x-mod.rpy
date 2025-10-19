## File: screen_language.rpy
## Menu Mod untuk ganti bahasa - STANDALONE VERSION
## Tidak bergantung pada game_menu atau screen lain
## Compatible dengan Ren'Py 8.0.3

## Set default language ke Indonesia
define config.language = "id"

init python:
    # Set default language saat game start
    def set_default_language():
        if persistent.language is None:
            try:
                renpy.change_language("id")
            except:
                pass
    
    # Jalankan setelah game benar-benar start
    config.start_callbacks.append(set_default_language)

## Screen popup untuk ganti bahasa - STANDALONE
screen mod_language_popup():
    
    modal True
    zorder 200
    
    # Background overlay gelap
    add Solid("#000000dd")
    
    # Container utama
    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        ysize 500
        
        background Solid("#1a1a1a")
        padding (40, 40)
        
        vbox:
            spacing 25
            xalign 0.5
            yalign 0.5
            
            # Header
            text "MOD - Language Settings":
                size 45
                xalign 0.5
                color "#ffffff"
                bold True
            
            # Garis pemisah
            null height 10
            
            text "Select your preferred language:":
                size 25
                xalign 0.5
                color "#aaaaaa"
            
            null height 30
            
            # Tombol bahasa
            vbox:
                spacing 20
                xalign 0.5
                
                # English Button
                button:
                    xsize 500
                    ysize 90
                    background Solid("#2d2d2d")
                    hover_background Solid("#3d3d3d")
                    action [Language(None), Hide("mod_language_popup")]
                    
                    hbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 25
                        
                        text "🇬🇧":
                            size 50
                        
                        text "English":
                            size 35
                            color "#ffffff"
                
                # Indonesia Button  
                button:
                    xsize 500
                    ysize 90
                    background Solid("#2d2d2d")
                    hover_background Solid("#3d3d3d")
                    action [Language("id"), Hide("mod_language_popup"), renpy.restart_interaction]
                    
                    hbox:
                        xalign 0.5
                        yalign 0.5
                        spacing 25
                        
                        text "🇮🇩":
                            size 50
                        
                        text "Bahasa Indonesia":
                            size 35
                            color "#ffffff"
            
            null height 30
            
            # Close button
            button:
                xalign 0.5
                xsize 250
                ysize 60
                background Solid("#ff4444")
                hover_background Solid("#ff6666")
                action Hide("mod_language_popup")
                
                text "Close":
                    xalign 0.5
                    yalign 0.5
                    size 28
                    color "#ffffff"
                    bold True


## Tombol untuk membuka popup - bisa dipanggil dari mana saja
screen mod_language_button():
    
    zorder 100
    
    # Tombol di pojok kanan bawah
    button:
        xalign 0.98
        yalign 0.98
        xsize 200
        ysize 70
        
        background Solid("#ff4444ee")
        hover_background Solid("#ff6666ee")
        
        action Show("mod_language_popup")
        
        hbox:
            xalign 0.5
            yalign 0.5
            spacing 10
            
            text "⚙":
                size 35
                color "#ffffff"
            
            text "MOD":
                size 28
                color "#ffffff"
                bold True


## Auto-show tombol MOD HANYA di main menu dan preferences
init python:
    
    def show_mod_button():
        """Tampilkan tombol MOD hanya di screen tertentu"""
        try:
            # Cek screen apa yang sedang aktif
            current_screen = renpy.get_screen("preferences") or renpy.get_screen("main_menu") or renpy.get_screen("navigation")
            
            # Hanya tampilkan jika di main menu atau preferences
            if current_screen is not None:
                if renpy.get_screen("mod_language_button") is None:
                    renpy.show_screen("mod_language_button")
            else:
                # Sembunyikan tombol jika tidak di menu
                if renpy.get_screen("mod_language_button") is not None:
                    renpy.hide_screen("mod_language_button")
        except:
            pass
    
    # Tambahkan ke interact callbacks
    config.interact_callbacks.append(show_mod_button)


## Hotkey untuk membuka menu MOD (tekan M)
init python:
    
    config.keymap['mod_menu'] = ['m', 'M']
    
    def open_mod_menu():
        renpy.show_screen("mod_language_popup")
        return True
    
    config.underlay.append(
        renpy.Keymap(
            mod_menu = open_mod_menu
        )
    )


## Style definitions yang aman
init python:
    try:
        style.mod_button = Style(style.button)
        style.mod_button.background = Solid("#ff4444")
        style.mod_button.hover_background = Solid("#ff6666")
    except:
        pass
