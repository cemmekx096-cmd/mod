









init -501 screen about():
    tag menu



    use game_menu(_("Credits"), scroll="viewport"):
        style_prefix "about"
        vbox:
            null height 86

            label "[config.name!t]"
            text _("Version [config.version!t]\n")
            if steam:
                text _("Game design, writing, art and coding by {a=https://evakiss.net/}Eva Kiss{/a}")
            else:
                text _("Game design, writing, art and coding by {a=https://www.patreon.com/Evakiss/}Eva Kiss{/a}")
            text _("Coloring by {a=https://revolgraphstore.com/}Lenadai{/a}")
            text _("Background art by {a=https://gvio.art/}GVIO Art Team{/a}, Art Direction by Giao Nguyen")
            text _("Original Sound Track by {a=https://ericsero.com/}Èric Seró{/a}")
            text _("Additional music from {a=https://www.bensound.com/}Bensound{/a}, {a=http://www.purple-planet.com/home/4593438321}Purple Planet Music{/a}, {a=https://soundcloud.com/litespots69}Jaime Restrepo{/a} and {a=https://www.incompetech.com}Kevin MacLeod{/a}")
            text _("")


            text _("VIP team:  {image=gui/vip_lara.webp} {u}Pilot Lara{/u} ,  {image=gui/vip_mares.webp} {u}BloodyMares{/u} ,  {image=gui/vip_fable.webp}{u} TheDarkFable{/u}. This game wouldn't be possible without them!")
            if not steam:
                text _("Get the {a=https://patreon.com/BloodyMares}Official Walkthrough{/a} for the game!")
            text _("Additional thanks to {u}vBerlichingen{/u} for his invaluable proofreading and to {u}Breadloaf{/u} for his continued help")

            text _("")
            text _("Special thanks to:  {i}Dennis Sp. Bera, ProfoundSugar, Gus Chiggings, Sinnipe, Prnxcutor, art, Whyarewestillhere, JJ Walker, Reddy1124, Gerry 'Helion' Hornung and Spidey96{/i} !")
            text _("")




            if gui.about:
                text "[gui.about!t]\n"

            if not steam:
                text _ ("Please, support this game on {a=https://www.patreon.com/Evakiss/}PATREON{/a}!")
            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")





define -1 gui.about = ""



init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text:
    size gui.label_text_size

init -1 style about_text is gui_text
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
