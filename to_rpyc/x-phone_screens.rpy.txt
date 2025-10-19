


transform phone_open_close:
    on show:
        alpha 0.0
        yoffset 1027
        parallel:
            ease 0.35 yoffset 0
        parallel:
            ease 0.25 alpha 1.0
        ease 0.2 yoffset 10
    on hide:
        ease 0.5 yoffset 1027

screen phone_base(parent, app=None, first=False):
    frame:
        xpos 40
        yalign 1.0
        xysize (572, 1027)
        padding (44, 86, 46, 20)
        background "gui/phone_%s.webp" % parent

        if not first:
            yoffset 10

        transclude

        if app:
            add app ypos 60
            imagebutton:
                align (1.0, 1.0)
                yoffset -40
                auto "gui/header_back_%s.webp"
                action Play("ch_one", "sfx/phone_back.mp3"), ShowMenu('phone', first=False, parent=parent)

        hbox style "phone_base_hbox_status":
            text day size 25 color "#E1E1E1" style "phone_base_text"
            text "[month], week [week]" size 18 color "#B7B7B7" style "phone_base_text"

    if app:
        key "game_menu" action ShowMenu('phone', first=False, parent=parent)

style phone_base_hbox_status:
    xpos 16
    ysize 34
    spacing 20

style phone_base_text:
    yalign 1.0
    font font_big_noodle

screen phone(parent=None, first=True):
    tag menu
    style_prefix "phone_home"

    if parent is None:
        if ian_active:
            $ parent = 'ian'
        else:
            $ parent = 'lena'

    frame style "empty" at phone_open_close:
        yalign 1.0
        use phone_base(parent=parent, first=first):
            vbox:
                hbox:
                    imagebutton auto "gui/icon_stats_%s.webp" action Play("ch_one", "sfx/phone_click.mp3"), ShowMenu('phone_stats', parent=parent)
                    imagebutton auto "gui/icon_agenda_%s.webp" action Play("ch_one", "sfx/phone_click.mp3"), ShowMenu('phone_agenda', parent=parent)
                    imagebutton auto "gui/icon_budget_%s.webp" action Play("ch_one", "sfx/phone_click.mp3"), ShowMenu('phone_budget', parent=parent)
                hbox:
                    imagebutton auto "gui/icon_save_%s.webp" action Play("ch_one", "sfx/phone_click.mp3"), ShowMenu('phone_save', parent=parent)
                    imagebutton auto "gui/icon_load_%s.webp" action Play("ch_one", "sfx/phone_click.mp3"), ShowMenu('load')
                    imagebutton auto "gui/icon_settings_%s.webp" action Play("ch_one", "sfx/phone_click.mp3"), ShowMenu('phone_settings', parent=parent)
                hbox:
                    imagebutton auto "gui/icon_mainmenu_%s.webp" action Play("ch_one", "sfx/phone_click.mp3"), MainMenu()
                    if not steam:
                        imagebutton auto "gui/icon_patreon_%s.webp" action Play("ch_one", "sfx/phone_click.mp3"), ShowMenu('phone_patreon', parent=parent)
                    imagebutton auto "gui/icon_gallery_%s.webp" action Play("ch_one", "sfx/phone_click.mp3"), ShowMenu('phone_gallery', parent=parent)

            imagebutton auto "gui/icon_back_%s.webp" action Play("ch_one", "sfx/phone_down.mp3"), Return():
                align (0.0, 1.0)
                offset (20, -20)

            if renpy.variant("pc"):
                imagebutton auto "gui/icon_quit_%s.webp" action Play("ch_one", "sfx/phone_click.mp3"), Quit(confirm=True):
                    align (1.0, 1.0)
                    offset (-20, -20)

style phone_home_vbox:
    ypos 60
    xalign 0.5
    spacing 20

style phone_home_hbox:
    spacing 20




screen phone_stats(parent=None):
    tag menu

    if parent is None:
        if ian_active:
            $ parent = 'ian'
        else:
            $ parent = 'lena'

    use phone_base(parent=parent, app="gui/header_stats.webp"):
        style_prefix "phone_stats"
        frame:
            has vbox
            ypos 85
            spacing 127
            for skill in skill_array:
                bar style "phone_stats_bar" range get_skill_points_needed(skill) value getattr(store, "%s_%s_xp" % (parent,skill))

        for skill in skill_array + ['money', 'will']:
            imagebutton idle "gui/subicon_%s.webp" % skill hover "gui/helptext_%s.webp" % skill keyboard_focus False focus_mask True action NullAction() offset (-90, -200)

        vbox style "phone_stats_vbox_numbers":
            pos (200, 160)
            for skill in skill_array:
                text "[%s_%s]" % (parent, skill)

        vbox style "phone_stats_vbox_numbers":
            pos (440, 296)
            text "[%s_money]" % parent
            text "[%s_will]" % parent color "#E0CE39"

style phone_stats_frame:
    xsize 399
    xalign 1.0
    ypos 136
    xoffset -10
    background "gui/subicon_stats.webp"

style phone_stats_vbox_numbers:
    xalign 1.0
    spacing 78

style phone_stats_bar:
    xysize (158,5)

style phone_stats_text:
    size 50
    font font_big_noodle_oblique
    color "#fff"
    xalign 1.0




init -1 python:
    class PhoneAgendaEntry:
        def __init__(self, id, name, show_if, use_ian_default=None, use_lena_default=None):
            self.id = id
            self.name = name
            self.show_if = show_if
            
            self.use_ian_default = use_ian_default
            if self.use_ian_default is None:
                self.use_ian_default = False
            
            self.use_lena_default = use_lena_default
            if self.use_lena_default is None:
                self.use_lena_default = False

screen phone_agenda(parent=None):
    tag menu

    on "hide" action Notify("gsagsa")

    default selectedChar = None
    default use_ian_default = False
    default use_lena_default = False

    if parent is None:
        if ian_active:
            $ parent = 'ian'
        else:
            $ parent = 'lena'

    use phone_base(parent=parent, app="gui/header_agenda.webp"):
        style_prefix "phone_agenda"
        vbox:
            for entry in phone_agenda_list[parent]:
                if eval(entry.show_if):
                    textbutton entry.name:
                        action [
                            SelectedIf(SetScreenVariable('selectedChar', entry.id)),
                            SetScreenVariable('use_ian_default', entry.use_ian_default),
                            SetScreenVariable('use_lena_default', entry.use_lena_default),
                            Play("ch_one", "sfx/phone_click.mp3")
                        ]

    if selectedChar is not None:
        use phone_agenda_bio(char=selectedChar, use_ian_default=use_ian_default, use_lena_default=use_lena_default)

style phone_agenda_vbox:
    pos (40, 120)
    ymaximum 655
    box_wrap True

style phone_agenda_vbox:
    variant "small"
    spacing 10
    ymaximum 700








init python:
    bio_characters['lena']['ian'] = bio_characters['ian']['lena']

    def get_character_bio_bar_thumb(parent, char, use_default=False):
        if char in bio_characters[parent]:
            temp = bio_characters[parent][char]
        else:
            if use_default:
                char = 'default'
            temp = [
                (parent + '_' + char + ' < 2', "mad"),
                (parent + '_' + char + ' < 4', "neutral"),
                ('True', "smile"),
            ]
        
        for show_if, bar_thumb in temp:
            if eval(show_if):
                return "gui/thumb_"+bar_thumb+".webp"
        
        return "gui/thumb_neutral.webp"

    def get_character_bio(char):
        for show_if, bio_text in bio_characters[char]['bio']:
            if eval(show_if):
                return bio_text
        return ""

screen phone_agenda_bio(char, use_lena_default=False, use_ian_default=False):
    add "gui/bio_[char].webp"
    style_prefix "screen_bio"

    if lena_active:
        $ parent = 'lena'
    else:
        $ parent = 'ian'

    if parent == char:
        add "gui/block_bio.webp" pos (1279, 607)
    elif char in ['lena', 'ian']:
        bar value ian_lena range 12 style "screen_bio_bar"
        add get_character_bio_bar_thumb('ian', 'lena') pos (1470, 753)
    elif char in ['jessg', 'jessb']:
        bar value eval(parent+"_jess") range 12 style "screen_bio_bar"
        add get_character_bio_bar_thumb(parent, 'jess') pos (1470, 753)
    else:
        if char  == 'wade' and chapter > 7:
            add "gui/bio_27y.webp"
        if char  == 'ivy' and chapter > 10:
            add "gui/bio_23y.webp"
        if (parent == 'lena' and use_lena_default) or (parent == 'ian' and use_ian_default):
            bar value eval(parent+"_default") range 12 style "screen_bio_bar"
            add get_character_bio_bar_thumb(parent, char, use_default=True) pos (1470, 753)
        else:
            bar value eval(parent+"_"+char) range 12 style "screen_bio_bar"
            add get_character_bio_bar_thumb(parent, char) pos (1470, 753)

    frame style "empty":
        pos (1300, 250)
        xmaximum 450
        ymaximum 470
        has viewport
        yinitial 0.0
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True

        side_yfill True

        text get_character_bio(char) style "screen_bio_text"

style screen_bio_imagebutton:
    pos (1470, 753)

style screen_bio_bar:
    xysize (405,10)
    pos (1317, 831)

style screen_bio_text:
    box_wrap True
    size 23
    font font_big_noodle_oblique

style screen_bio_text:
    variant "small"
    size gui.text_size

style bio:
    xpos 1300
    ypos 250
    xmaximum 450
    box_wrap True




init python:
    def try_get_pictures(parent, char):
        try:
            return eval("_".join([parent, char, 'pics']))
        except Exception as e:
            return None

screen phone_gallery(parent=None):
    tag menu

    if parent is None:
        if ian_active:
            $ parent = 'ian'
        else:
            $ parent = 'lena'

    use phone_base(parent=parent, app="gui/header_gallery.webp"):
        vbox style "phone_agenda_vbox":
            for char in ['alison', 'axel', 'cherry', 'cindy', 'emma', 'gillian', 'holly', 'ian', 'ivy', 'jeremy', 'lena', 'louise', 'marcel', 'mike', 'minerva', 'perry', 'robert', 'seymour', 'stan', 'wade', 'misc']:
                $ gallery = try_get_pictures(parent, char)
                if gallery is not None and len(gallery) > 0:
                    textbutton char.capitalize():
                        text_font font_big_noodle_oblique
                        action [ Play ("ch_one", "sfx/phone_click.mp3") ], ShowMenu('phone_gallery_pictures', parent=parent, char=char)

screen phone_gallery_pictures(parent, char):
    tag menu

    default gallery_index = 0

    key "game_menu" action ShowMenu('phone_gallery', parent=parent)

    $ gallery = eval('_'.join([parent, char, 'pics']))
    $ gallery_length = len(gallery)

    add "gui/phone_%s.webp" % parent xpos 40 yalign 1.0 yoffset 10

    frame style "empty":
        yoffset 10

        vbox pos (-632, 5):

            add gallery[gallery_index].replace(".png", ".webp")

        frame style "phone_gallery_pictures_bottom_bar_bg"



        imagebutton:
            style "phone_gallery_pictures_bottom_bar_prev"
            idle Frame("gui/gallery_prev_idle.webp")
            hover Frame("gui/gallery_prev_hover.webp")
            action Play ("ch_one", "sfx/phone_click.mp3"), SetScreenVariable("gallery_index", (gallery_index-1) % gallery_length)


        imagebutton:
            style "phone_gallery_pictures_bottom_bar_back"
            idle Frame("gui/gallery_back_idle.webp")
            hover Frame("gui/gallery_back_hover.webp")
            action Play ("ch_one", "sfx/phone_click.mp3"), ShowMenu('phone_gallery', parent=parent)


        imagebutton:
            style "phone_gallery_pictures_bottom_bar_next"
            idle Frame("gui/gallery_next_idle.webp")
            hover Frame("gui/gallery_next_hover.webp")
            action Play ("ch_one", "sfx/phone_click.mp3"), SetScreenVariable("gallery_index", (gallery_index+1) % gallery_length)


style phone_gallery_pictures_bottom_bar is empty:
    ypos 1066
    yanchor 1.0
    ysize 33

style phone_gallery_pictures_bottom_bar:
    variant "small"
    ysize 54

style phone_gallery_pictures_bottom_bar_bg is phone_gallery_pictures_bottom_bar:
    background Frame("gui/gallery_base.webp")
    xpos 87
    xsize 484

style phone_gallery_pictures_bottom_bar_prev is phone_gallery_pictures_bottom_bar:
    xpos 87
    xsize 60

style phone_gallery_pictures_bottom_bar_back is phone_gallery_pictures_bottom_bar:
    xpos 305
    xsize 48

style phone_gallery_pictures_bottom_bar_next is phone_gallery_pictures_bottom_bar:
    xpos 511
    xsize 60





screen phone_budget(parent=None):
    tag menu

    if parent is None:
        if ian_active:
            $ parent = 'ian'
        else:
            $ parent = 'lena'

    use phone_base(parent=parent, app="gui/header_budget.webp"):
        style_prefix "phone_budget"
        if ian_active:

            text "%+d" % (ian_job_magazine + ian_stipend):
                style "phone_budget_text_large"
                ypos 148
                color "#1ED50F"

            vbox style "phone_budget_income":
                if ian_job_magazine > 0:
                    text "Magazine internship   {color=#1ED50F}+[ian_job_magazine]{/color}"
                if ian_stipend > 0:
                    text "Family stipend   {color=#1ED50F}+[ian_stipend]{/color}"


            text "%-d" % (-int(ian_live_perry) - 1):
                style "phone_budget_text_large"
                ypos 403
                color "#C20B0B"

            vbox style "phone_budget_expenses":
                if ian_live_perry:
                    text "Rent   {color=#C20B0B}-1{/color}"
                text "Living expenses   {color=#C20B0B}-1{/color}"

        elif lena_active:

            text "%+d" % (lena_job_cafe + lena_job_restaurant + int(chapter > 5 and (stalkfap or stalkfap_pro > 0))):
                style "phone_budget_text_large"
                ypos 148
                color "#1ED50F"

            vbox style "phone_budget_income":
                if lena_job_cafe > 0:
                    text "Cafe job   {color=#1ED50F}+[lena_job_cafe]{/color}"

                if lena_job_restaurant > 0:
                    text "Restaurant job   {color=#1ED50F}+[lena_job_restaurant]{/color}"

                if chapter > 5 and (stalkfap or stalkfap_pro > 0):
                    text "Stalkfap subscriptions   {color=#1ED50F}+1{/color}"



            text "%-d" % (int(lena_live_stan_louise) * -2 - 1):
                style "phone_budget_text_large"
                ypos 403
                color "#C20B0B"

            vbox style "phone_budget_expenses":
                if lena_live_stan_louise:
                    text "Rent   {color=#C20B0B}-2{/color}"
                text "Living expenses   {color=#C20B0B}-1{/color}"



        text "[%s_money]" % parent style "phone_budget_global":
            xoffset 100

        text "[%s_owed_money]" % parent style "phone_budget_global":
            xalign 1.0
            xoffset -100

            if eval("%s_owed_money" % parent) > 0:
                color "#C20B0B"


style phone_budget_text:
    font font_big_noodle_oblique
    color "#fff"

style phone_budget_text_large is phone_budget_text:
    size 50
    xpos 328

style phone_budget_income:
    pos (26, 220)
    size 30
    ymaximum 655
    box_wrap True

style phone_budget_expenses is phone_budget_income:
    ypos 490

style phone_budget_global is phone_budget_text:
    size 50
    yalign 1.0
    yoffset -150





screen phone_patreon(parent=None):
    tag menu

    if parent is None:
        if ian_active:
            $ parent = 'ian'
        else:
            $ parent = 'lena'

    use phone_base(parent=parent, app="gui/header_patreon.webp"):
        imagebutton:
            ypos 270
            auto "gui/header_patreon_continue_%s.webp"
            action Play ("ch_one", "sfx/phone_click.mp3"), OpenURL ("https://www.patreon.com/Evakiss")






screen phone_settings(parent=None):
    tag menu

    if parent is None:
        if ian_active:
            $ parent = 'ian'
        else:
            $ parent = 'lena'

    use phone_base(parent=parent, app="gui/header_settings.webp"):

        vbox style "phone_settings_hbox_outer":

            hbox:
                spacing 33
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    label _("Rollback")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))




            vbox style "phone_settings_phonebar":
                label _("Text Speed")
                bar value Preference("text speed")

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")


                if config.has_music:
                    label _("Music Volume")
                    hbox:
                        bar value Preference("music volume")


                if config.has_sound:
                    label _("Sound Volume")
                    hbox:
                        bar value Preference("sound volume")


                if config.has_voice:
                    label _("Voice Volume")
                    hbox:
                        bar value Preference("voice volume")

                if config.has_music or config.has_sound or config.has_voice:
                    null height gui.pref_spacing


                    textbutton _("Mute All"):
                        action Preference("all mute", "toggle")
                        style "mute_all_button"




style phone_settings_hbox_outer:
    align (0.5, 0.5)
    spacing 10

style phone_settings_hbox_outer:
    variant "small"
    yoffset 10


style phone_settings_phonebar:
    xsize 427









screen phone_save(parent=None):
    tag menu

    if parent is None:
        if ian_active:
            $ parent = 'ian'
        else:
            $ parent = 'lena'

    use phone_base(parent=parent):
        imagebutton:
            align (1.0, 1.0)
            yoffset -40
            auto "gui/header_back_%s.webp"
            action Play("ch_one", "sfx/phone_back.mp3"), ShowMenu('phone', first=False, parent=parent)

    add "gui/header_save.webp"

    use file_slots2(_("Save"))

    if not renpy.variant('touch'):
        hbox xanchor 0.0 xalign 0.065 yalign 0.27:
            text "{font=[font_big_noodle_oblique]}{color=#FFFFFF}Save Name: {/color}"

        hbox xanchor 0.0 xalign 0.065 yalign 0.30:
            input:
                value VariableInputValue('save_name')
                length 25
                font font_big_noodle_oblique








screen phone_load():
    tag menu

    if ian_active:
        $ parent = 'ian'
    else:
        $ parent = 'lena'

    use phone_base(parent=parent):
        imagebutton:
            align (1.0, 1.0)
            yoffset -40
            auto "gui/header_back_%s.webp"
            action Play("ch_one", "sfx/phone_back.mp3"), ShowMenu('phone', first=False, parent=parent)

    add "gui/header_load.webp"

    use file_slots2(_("Load"))


screen file_slots2(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    default hover_slot = None

    vbox:
        xysize (1240, 900)
        pos (650, 94)
        spacing 40

        order_reverse True


        button style "page_label":
            key_events True
            action page_name_value.Toggle()

            input:
                style "page_label_text"
                value page_name_value


        grid gui.file_slot_cols gui.file_slot_rows:
            style_prefix "slot"
            xalign 0.5
            xspacing 20
            yspacing 36

            for i in range(gui.file_slot_cols * gui.file_slot_rows):
                $ slot = i + 1
                button:
                    hovered SetLocalVariable("hover_slot", slot)
                    unhovered SetLocalVariable('hover_slot', None)
                    action FileAction(slot)

                    has vbox spacing 2

                    add Frame(FileScreenshot(slot), xysize=(gui.slot_width, gui.slot_height)) xalign 0.5

                    text FileTime(slot, format="%c", empty=_("empty slot")):
                        style "slot_time_text"
                        xalign 0.5

                    text FileSaveName(slot):
                        style "slot_name_text"
                        xalign 0.5

                    key "save_delete" action FileDelete(slot)

                    if hover_slot == slot:
                        imagebutton:
                            auto "/gui/button/delete_%s_button.png"
                            action FileDelete(slot)
                            xpos 186
                            ypos -196
                            hovered SetLocalVariable("hover_slot", slot)
                            unhovered SetLocalVariable('hover_slot', None)
                    else:
                        add Null(30,30)


        hbox style "page_hbox":
            style_prefix "page"

            spacing gui.page_spacing

            $ realpage = int(FilePageName(0,0))
            $ page = realpage
            if page < 1:
                $ page = saveload_previus_page

            textbutton _("<<"):
                if page > 1:
                    action FilePage(1)
            textbutton _("<") action FilePagePrevious()

            if config.has_autosave:
                textbutton _("{#auto_page}A") action SelectedIf(FilePage("auto")), SetVariable('saveload_previus_page', page)

            if config.has_quicksave:
                textbutton _("{#quick_page}Q") action SelectedIf(FilePage("quick")), SetVariable('saveload_previus_page', page)

            $ start = max(page - 5 - max(5 + page - saveload_maxpages, 0), 1)
            $ end = min(page + 6 + min(max(6 - page, 0), 6), saveload_maxpages + 1)

            for p in range(start, end):
                textbutton "[p]" action FilePage(p)

            textbutton _(">"):
                if page < saveload_maxpages or realpage == 0:
                    action FilePageNext()
            textbutton _(">>"):
                if page < saveload_maxpages or realpage == 0:
                    action FilePage(saveload_maxpages)

    key "game_menu" action ShowMenu('phone', first=False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
