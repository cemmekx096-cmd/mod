define mod_version = "Ch4Up5"
define mod_revision = ""
define outdated_game_versions = ["Ch4Up4","Ch4Up3"]
define mod_game_build = ""

init 1:
    if config.version == (mod_version or mod_version+mod_game_build):
        define mod_ver_text = "{{color=#FFFFFF}}{{b}}VER: {{/b}}{{/color}} {{color=#FFFFFF}}{{alpha=0.7}}{}{{/alpha}}{{/color}}".format(config.version + mod_revision)

    elif config.version in outdated_game_versions:
        define mod_ver_text = "{{color=#FFFFFF}}{{b}}GAME IS OUTDATED{{/b}}{{/color}}   {{color=#FFFFFF}}Game: {}   Mod: {}{{/color}}".format(config.version, mod_version + mod_revision)
    elif True:

        define mod_ver_text = "{{color=#FFFFFF}}{{b}}MOD IS OUTDATED{{/b}}      {{color=#FFFFFF}}Mod: {}     Game: {}     {{a=https://www.patreon.com/Shawnchapp}}{{font=mod/OSB.ttf}}*Download update here!*{{/font}}{{/a}}{{/color}}".format(mod_version + mod_revision, config.version)

init -1 python:
    class mod_stats_info:
        def __init__(self, girl, name, show_pane, max_level, image, step, love, corruption, route, guides):
            self.girl = girl
            self.name = name
            self.show_pane = show_pane
            self.max_level = max_level
            self.image = image
            self.step = step
            self.lov = love
            self.cor = corruption
            self.rou = route
            self.guides = guides

define girl1_mod_stats = mod_stats_info(1, "{color=#22b1f8}Rosalind", False, "", "rosalind", "", "Rosalind_Affection", ["Libido","Rosalind_Libido"], "Rosalind_Relations", "")
define girl2_mod_stats = mod_stats_info(2, "{color=#F0E68C}Felicia", False, "", "felicia", "", "Felicia_Affection", ["Confidence","Felicia_Confidence", "#F0E68C"], "Felicia_Relations", "")
define girl3_mod_stats = mod_stats_info(3, "{color=#800000}Veronica", False, "", "veronica", "", "Veronica_Affection", ["Horniness","Veronica_Horniness"], "Veronica_Relations", "")
define girl4_mod_stats = mod_stats_info(4, "{color=#DB7093}Mina", False, "", "mina", "", "Mina_Affection", ["Bi-Curious","Mina_BiCurious"], "Mina_Relations", "")
define girl5_mod_stats = mod_stats_info(5, "{color=#000000}Hana", False, "", "hana", "", "Hana_Affection", ["Anger","Hana_Anger", "#8B0000"], "Hana_Relations", "")

define girl6_mod_stats = mod_stats_info(6, "{color=#F0E68C}Kathleen", False, "", "kathleen", "", "Kathleen_Affection", ["Trust","Kathleen_Trust", "#1BEFF6"], "Kathleen_Relations", "")
define girl7_mod_stats = mod_stats_info(7, "{color=#8B0000}Killian", False, "", "killian", "", "Killian_Bromance", ["killian/Mina Love","Mina_KLove"], "", "")
define girl8_mod_stats = mod_stats_info(8, "{size=26}{color=#FAEBD7}Chuck{/color} & {color=#FF8C00}August", False, "", "chuck_august", "", ["Friendship", "Chuck_Friendship", "#FAEBD7"], ["Friendship", "August_Friendship", "#FF8C00"], "", "")

define girl9_mod_stats = mod_stats_info(9, "{color=#33A625}Jacob", False, "", "jacob", "", ["Friendship", "Jacob_Friendship", "#1BEFF6"], "", "", "")
define girl10_mod_stats = mod_stats_info(10, "{color=#8B4513}Warren", False, "", "warren", "", ["Friendship", "Warren_Friendship", "#1BEFF6"], "", "", "")
define girl11_mod_stats = mod_stats_info(11, "{color=#A9A9A9}Samson", False, "", "sam", "", ["Friendship", "Sam_Friendship", "#1BEFF6"], "", "", "")

define girl12_mod_stats = mod_stats_info(12, "{color=#4169E1}[mcf]", False, "", "player", "", ["Toughness", "toughness", "#FF8C00"], "", "", "")

define m_main_girls = [girl1_mod_stats, girl2_mod_stats, girl3_mod_stats, girl4_mod_stats, girl5_mod_stats, girl6_mod_stats, girl7_mod_stats, girl8_mod_stats, girl9_mod_stats,
                        girl10_mod_stats, girl11_mod_stats, girl12_mod_stats]


screen modmenu():
    default m_current_tab = "stats"
    default m_column2 = None
    default m_column2_name = ""
    default m_girl_tab = "main"
    default m_page_tab = "1"

    zorder 151

    drag:
        drag_name "modmenu"
        align (0.5, 0.5)
        drag_handle (0, 0, 1.0, 53)

        has fixed
        xysize (1102, 756)
        align (0.5, 0.5)

        button style "mod_textbutton" xysize (1102, 703) yalign 1.0 action NullAction()
        add "mod/images/modmenu_empty.png"
        textbutton "X" style "mod_textbutton" action Hide("modmenu") align (1.0, 0.0) text_font "mod/OSB.ttf" yoffset -6 xoffset -15 text_idle_color "#ffffff" text_hover_color "#51087E"
        text "[mod_ver_text]" size 18 align (0.99, 0.99) font "mod/OS.ttf"


        hbox:
            style_prefix "navbtn"
            xalign 0.5

            add "mod/images/nav_cap_left.png"
            textbutton "Stats" selected m_current_tab == "stats" text_style "mod_toolbar_textbutton" action [SetScreenVariable("m_current_tab", "stats"), SetScreenVariable("m_column2", None), SetScreenVariable("m_column2_name", "")]
            textbutton "Settings" selected m_current_tab == "settings" text_style "mod_toolbar_textbutton" action [SetScreenVariable("m_current_tab", "settings"), SetScreenVariable("m_column2", None), SetScreenVariable("m_column2_name", "")]
            if mod_show_cheats:
                textbutton "Cheats" selected m_current_tab == "cheats" text_style "mod_toolbar_textbutton" action [SetScreenVariable("m_current_tab", "cheats"), SetScreenVariable("m_column2", None), SetScreenVariable("m_column2_name", "")]
            add "mod/images/nav_cap_right.png"

        hbox:
            align (0.970, 0.96)
            spacing 10
            imagebutton idle "mod/images/bt_pat_logo.png" hover im.MatrixColor("mod/images/bt_pat_logo.png", im.matrix.brightness(0.16)) action OpenURL("https://www.patreon.com/Shawnchapp") yoffset 5.0
            imagebutton idle "mod/images/btn_substar.png" hover im.MatrixColor("mod/images/btn_substar.png", im.matrix.brightness(0.16)) action OpenURL("https://subscribestar.adult/shawnchapp") yoffset 7.5

            imagebutton idle "mod/images/discord.png" hover im.MatrixColor("mod/images/discord.png", im.matrix.brightness(0.16)) action OpenURL("https://discord.gg/6uyJXgRkaJ") yoffset 7.5 xoffset 10.0

        if m_current_tab == "stats":

            vpgrid id "mod_vp" pos (50, 80):
                style_prefix "walk_menu"
                xysize (1050, 580)
                xfill True
                cols 4
                draggable True
                mousewheel True
                for i in m_main_girls:
                    vbox:
                        spacing -5
                        add ImageReference("{}".format(i.image)) xalign 0.5
                        null height 15
                        text i.name bold True
                        if i.rou != "":
                            text "(" + str(eval(i.rou)) + ")" size 20
                        vbox:
                            yoffset -10
                            xalign 0.5
                            frame:
                                style "stats_f_outline"
                                yalign 0.5
                                xalign 0.5
                                has frame
                                style "stats_f_main"

                                vbox:

                                    spacing -10
                                    vbox:
                                        spacing 5
                                        xalign 0.5
                                        if isinstance(i.lov, list):
                                            text i.lov[0]:
                                                style "walk_menu_stats"
                                                size 25
                                                if len(i.lov) > 2:
                                                    color i.lov[2]
                                                else:
                                                    color "#FF9CE9"
                                                xalign 0.5
                                            hbox:
                                                xalign 0.5
                                                spacing 5
                                                if mod_show_cheats:
                                                    textbutton "-" action SetVariable(i.lov[1], eval(i.lov[1]) -1) text_style "red_cross" yoffset -10
                                                text str(eval(i.lov[1])) size 24
                                                if mod_show_cheats:
                                                    textbutton "+" action SetVariable(i.lov[1], eval(i.lov[1]) +1) text_style "green_check" yoffset -10
                                        else:
                                            text "Love" style "walk_menu_stats" size 25 color "#f00" xalign 0.5
                                            hbox:
                                                xalign 0.5
                                                spacing 5
                                                if mod_show_cheats:
                                                    textbutton "-" action SetVariable(i.lov, eval(i.lov) -1) text_style "red_cross" yoffset -10
                                                text str(eval(i.lov)) size 24
                                                if mod_show_cheats:
                                                    textbutton "+" action SetVariable(i.lov, eval(i.lov) +1) text_style "green_check" yoffset -10
                                    if isinstance(i.cor, list):
                                        vbox:
                                            spacing 5
                                            xalign 0.5
                                            text i.cor[0]:
                                                style "walk_menu_stats"
                                                size 25
                                                if len(i.cor) > 2:
                                                    color i.cor[2]
                                                else:
                                                    color "#FF9CE9"
                                                xalign 0.5
                                            hbox:
                                                xalign 0.5
                                                spacing 5
                                                if mod_show_cheats:
                                                    textbutton "-" action SetVariable(i.cor[1], eval(i.cor[1]) -1) text_style "red_cross" yoffset -10
                                                text str(eval(i.cor[1])) size 24
                                                if mod_show_cheats:
                                                    textbutton "+" action SetVariable(i.cor[1], eval(i.cor[1]) +1) text_style "green_check" yoffset -10

            vbar value YScrollValue("mod_vp"):
                xpos 0.97
                ypos 80
                ysize 580

        elif m_current_tab == "settings":
            text "Settings" style "mod_home_title"
            frame:
                style "cheat_f_outline"
                has frame
                style "cheat_f_main"

                hbox:
                    style_prefix "mod_settingsCheats"
                    align (0.5, 0.62)
                    spacing 80
                    vbox:
                        spacing 20
                        text "Use improved game UI:"
                        text "Textbox opacity: {}%".format(int(persistent.dialogueBoxOpacity * 100))
                        text "Show quick menu:"
                        text "Skip game startup splash screen:"
                        text "Bahasa Indonesia:"
                        text "CHEATS"

                    vbox:
                        spacing 20
                        if persistent.mod_use_improved_ui:
                            textbutton "Enabled" style "mod_textbutton" action ui.callsinnewcontext("shawn_setting_improvedui") selected persistent.mod_use_improved_ui text_style "mod_textbuttong"
                        else:
                            textbutton "Disabled" style "mod_textbutton" action ui.callsinnewcontext("shawn_setting_improvedui") selected persistent.mod_use_improved_ui text_style "mod_textbuttonr"

                        bar value FieldValue(persistent, "dialogueBoxOpacity", range=1.0, style="mod_slider")

                        if mod_qmenu:
                            textbutton "Enabled" style "mod_textbutton" action SetVariable("mod_qmenu", False) selected mod_qmenu text_style "mod_textbuttong"
                        else:
                            textbutton "Disabled" style "mod_textbutton" action SetVariable("mod_qmenu", True) selected mod_qmenu text_style "mod_textbuttonr"

                        if persistent.mod_skip_splashscreen:
                            textbutton "Enabled" style "mod_textbutton" action SetVariable("persistent.mod_skip_splashscreen", False) selected persistent.mod_skip_splashscreen text_style "mod_textbuttong"
                        else:
                            textbutton "Disabled" style "mod_textbutton" action SetVariable("persistent.mod_skip_splashscreen", True) selected persistent.mod_skip_splashscreen text_style "mod_textbuttonr"
                        
                        if _preferences.language == "id":
                            textbutton "Enabled" style "mod_textbutton" action Language(None) selected True text_style "mod_textbuttong"
                        else:
                            textbutton "Disabled" style "mod_textbutton" action Language("id") selected False text_style "mod_textbuttonr"
                        
                        if mod_show_cheats:
                            textbutton "Enabled" action SetVariable("mod_show_cheats", False) selected mod_show_cheats text_style "mod_textbuttong"
                        else:
                            textbutton "Disabled" action SetVariable("mod_show_cheats", True) selected mod_show_cheats text_style "mod_textbuttonr"

        elif m_current_tab == "cheats":
            text "Cheats" style "mod_home_title"

            frame:
                style "cheat_f_outline"
                has frame
                style "cheat_f_main"
                hbox:
                    style_prefix "mod_settingsCheats"

                    vbox:
                        spacing 11
                        style_prefix "cheatmenu"
                        text "Desires" xalign 0.5
                        hbox:
                            xalign 0.5
                            spacing 5
                            if id_greed:
                                textbutton "Money" action SetVariable("id_greed", False) selected id_greed text_style "green_check"
                            else:
                                textbutton "Money" action SetVariable("id_greed", True) selected id_greed text_style "red_cross"
                            if id_power:
                                textbutton "Power" action SetVariable("id_power", False) selected id_power text_style "green_check"
                            else:
                                textbutton "Power" action SetVariable("id_power", True) selected id_power text_style "red_cross"
                            if id_lust:
                                textbutton "Lust" action SetVariable("id_lust", False) selected id_lust text_style "green_check"
                            else:
                                textbutton "Lust" action SetVariable("id_lust", True) selected id_lust text_style "red_cross"


                        text "Traits" xalign 0.5
                        hbox:
                            xalign 0.5
                            spacing 5
                            if trait_inquisitive:
                                textbutton "Iinquisitive" action SetVariable("trait_inquisitive", False) selected trait_inquisitive text_style "green_check"
                            else:
                                textbutton "Iinquisitive" action SetVariable("trait_inquisitive", True) selected trait_inquisitive text_style "red_cross"
                            if trait_tireless:
                                textbutton "Tireless" action SetVariable("trait_tireless", False) selected trait_tireless text_style "green_check"
                            else:
                                textbutton "Tireless" action SetVariable("trait_tireless", True) selected trait_tireless text_style "red_cross"
                            if trait_governor:
                                textbutton "Governor" action SetVariable("trait_governor", False) selected trait_governor text_style "green_check"
                            else:
                                textbutton "Governor" action SetVariable("trait_governor", True) selected trait_governor text_style "red_cross"

                        text "History" xalign 0.5
                        hbox:
                            xalign 0.5
                            spacing 5
                            if history_firestarter:
                                textbutton "Firestarter" action SetVariable("history_firestarter", False) selected history_firestarter text_style "green_check"
                            else:
                                textbutton "Firestarter" action SetVariable("history_firestarter", True) selected history_firestarter text_style "red_cross"
                            if history_voyeur:
                                textbutton "Voyeur" action SetVariable("history_voyeur", False) selected history_voyeur text_style "green_check"
                            else:
                                textbutton "Voyeur" action SetVariable("history_voyeur", True) selected history_voyeur text_style "red_cross"
                            if history_stickyFingers:
                                textbutton "Sticky Fingers" action SetVariable("history_stickyFingers", False) selected history_stickyFingers text_style "green_check"
                            else:
                                textbutton "Sticky Fingers" action SetVariable("history_stickyFingers", True) selected history_stickyFingers text_style "red_cross"

                        text "Perks" xalign 0.5
                        hbox:
                            xalign 0.5
                            spacing 5
                            if perk_strongman:
                                textbutton "Strongman" action SetVariable("perk_strongman", False) selected perk_strongman text_style "green_check"
                            else:
                                textbutton "Strongman" action SetVariable("perk_strongman", True) selected perk_strongman text_style "red_cross"
                            if perk_socialButterfly:
                                textbutton "Social Butterfly" action SetVariable("perk_socialButterfly", False) selected perk_socialButterfly text_style "green_check"
                            else:
                                textbutton "Social Butterfly" action SetVariable("perk_socialButterfly", True) selected perk_socialButterfly text_style "red_cross"
                            if perk_socialChameleon:
                                textbutton "Social Chameleon" action SetVariable("perk_socialChameleon", False) selected perk_socialChameleon text_style "green_check"
                            else:
                                textbutton "Social Chameleon" action SetVariable("perk_socialChameleon", True) selected perk_socialChameleon text_style "red_cross"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc