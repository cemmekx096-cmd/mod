




define skill_array = ['wits', 'charisma', 'athletics', 'lust']


define skills_and_xp = {
    0: 1,
    1: 2,
    2: 3,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
}

init python:
    _preferences.show_empty_window = False

    def get_active_character_name():
        if ian_active:
            return 'ian'
        else:
            return 'lena'

    def get_skill_points_needed(skill):
        level = eval("{}_{}".format(get_active_character_name(), skill))
        if level > 9:
            return 6
        else:
            return skills_and_xp[level]

    def skillsup():
        char = get_active_character_name()
        
        skills_and_points = {}
        for skill in skill_array:
            skills_and_points[skill] = eval("{}_{}_xp".format(get_active_character_name(), skill))
        
        updated_skill = False
        for skill, points in skills_and_points.items():
            points_needed = get_skill_points_needed(skill)
            
            if points >= points_needed:
                var = "%s_%s" % (char, skill)
                SetVariable(var, eval(var)+1)()
                SetVariable(var+"_xp", eval(var+"_xp")-points_needed)()
                updated_skill = skill
                break
        
        if updated_skill:
            global quick_menu
            renpy.pause(0.2)
            quick_menu = False
            renpy.pause(0.2)
            renpy.call_screen("screen_skillsup", skill=updated_skill)
            renpy.pause(0.2)
            quick_menu = True

    def willup():
        global quick_menu
        renpy.pause(0.2)
        quick_menu = False
        renpy.pause(0.2)
        renpy.call_screen("screen_willup")
        renpy.pause(0.2)
        quick_menu = True

transform transform_skill_card:
    on show:
        zoom 0.0
        alpha 0.0
        block:
            parallel:
                linear 0.3 zoom 1.3
            parallel:
                linear 0.3 alpha 1.0

        linear 0.1 zoom 1.0

transform transform_skill_bg:
    on show:
        zoom 0.0
        alpha 0.9

        pause 0.1

        block:
            parallel:
                linear 0.7 zoom 2.5
            parallel:
                pause 0.5
                linear 0.2 alpha 0.0


screen screen_skillsup(skill):
    modal True
    timer 0.3 action Play("ch_one", "sfx/levelup.mp3")

    add "gui/levelup_popup_front.webp" at transform_skill_bg align (0.5, 0.5) yoffset -50
    add "gui/levelup_%s.webp" % skill at transform_skill_card align (0.5, 0.5) yoffset -50

    key "game_menu" action NullAction()
    key "dismiss" action Play("ch_one", "sfx/phone_back.mp3"), Return()


screen screen_willup():
    modal True
    timer 0.3 action Play("ch_one", "sfx/willup.mp3")

    add "gui/levelup_popup_front.webp" at transform_skill_bg align (0.5, 0.5) yoffset -50
    add "gui/levelup_will.webp" at transform_skill_card align (0.5, 0.5) yoffset -50

    $ char = get_active_character_name()

    key "game_menu" action NullAction()
    key "dismiss" action Play("ch_one", "sfx/phone_back.mp3"), SetVariable(char+"_will", eval(char+"_will")+1), Return()


screen screen_notif_unlock():
    timer 0.2 action Play("ch_one", "sfx/xp.mp3")

    imagebutton:
        at transform_gallery_unlock
        xalign 1.0
        yanchor 0.5
        yoffset 170
        idle "gui/scene_unlock.webp"
        action Play("ch_one", "sfx/phone_back.mp3"), Hide('screen_notif_unlock')

    timer 5.0 action Hide('screen_notif_unlock')

image athletics_up = "gui/xp_athletics.webp"
image charisma_up = "gui/xp_charisma.webp"
image friend_up = "gui/xp_friend.webp"
image friend_down = "gui/unxp_friend.webp"


image lust_up = "gui/xp_lust.webp"
image money_up = "gui/xp_money.webp"
image money_down = "gui/unxp_money.webp"
image will_down = "gui/unxp_will.webp"
image wits_up = "gui/xp_wits.webp"



label xp_up(stat_name, skillup_screen=True):
    play sound "sfx/xp.mp3"

    $ renpy.show("{}_up".format(stat_name), [transform_stat_up])
    $ exec("{}_{}_xp += 1".format(get_active_character_name(), stat_name))

    if skillup_screen:
        $ skillsup()

    return

label will_up():
    $ willup()
    return


label friend_xp(char_name, inc=1):
    if inc == 0:
        return

    $ temp_char_name = char_name

    $ temp_parent = get_active_character_name()
    if temp_parent == char_name or (temp_parent == 'lena' and char_name == 'ian'):
        $ temp_parent = 'ian'
        $ char_name = 'lena'

    if inc < 0 and eval("{}_{}".format(temp_parent, char_name)) < 1:
        $ exec("{}_{} = 0".format(temp_parent, char_name))
        return
    elif inc > 0 and eval("{}_{}".format(temp_parent, char_name)) > 11:
        $ exec("{}_{} = 12".format(temp_parent, char_name))
        return

    $ exec("{}_{} += {}".format(temp_parent, char_name, inc))
    $ exec("{0}_{1} = min(12, max(0, {0}_{1}))".format(temp_parent, char_name))

    $ char_name = temp_char_name

    if char_name == 'lenamom':
        $ char_name = 'mom'
    if char_name == 'lenadad':
        $ char_name = 'dad'
    elif get_active_character_name() == char_name:
        if char_name == 'ian':
            $ char_name = 'lena'
        else:
            $ char_name = 'ian'

    show screen screen_friend_xp(char_name, inc)
    return

screen screen_friend_xp(char_name, inc=1):
    style_prefix "friend_xp"

    if inc > 0:
        timer 0.01 action Play("ch_one", "sfx/friendup.mp3")
        frame at transform_stat_up:
            imagebutton idle "gui/xp_friend.webp" action Hide('screen_friend_xp')
            text "[char_name!c]" yoffset 170
    else:
        timer 0.01 action Play("ch_one", "sfx/frienddown.mp3")
        frame at transform_stat_down:
            imagebutton idle "gui/unxp_friend.webp" action Hide('screen_friend_xp')
            text "[char_name!c]" yoffset -46

    timer 1.0 action Hide('screen_friend_xp')

style friend_xp_frame is empty:
    xysize (112, 160)

style friend_xp_text:
    outlines [(2, "#221f1f88", 1, 1)]
    xalign 0.5
    font font_big_noodle
    size 34
    xoffset 2


label money(inc=1):
    if inc == 0:
        return

    if inc > 0:
        play sound "sfx/moneyup.mp3"
        show money_up at transform_stat_up
    else:
        play sound "sfx/moneydown.mp3"
        show money_down at transform_stat_down

    $ exec("{}_money += {}".format(get_active_character_name(), inc))
    return


label willdown:
    play sound "sfx/willdown.mp3"
    show will_down at transform_stat_down
    $ exec("{}_will -= 1".format(get_active_character_name()))
    return


























screen tutorial2screen():
    imagebutton idle "gui/tutorial3.webp" action Hide('tutorial2screen')  , ShowMenu('tutorial3screen')

screen tutorial3screen():
    imagebutton idle "gui/tutorial4.webp" action Hide('tutorial3screen')  , ShowMenu('tutorial4screen')

screen tutorial4screen():
    imagebutton idle "gui/tutorial5.webp" action Hide('tutorial4screen') , ShowMenu('tutorial5screen')

screen tutorial5screen():
    imagebutton idle "gui/tutorial6.webp" action Hide('tutorial5screen')  , Start('tutorial_diverge')

screen tutorialagenda():
    imagebutton idle "gui/tutorial7.webp" action Hide('tutorialagenda')  , ShowMenu('tutorialagenda2')

screen tutorialagenda2():
    imagebutton idle "gui/tutorial8.webp" action Hide('tutorialagenda2')  , Start('endtutorial')


screen basetutorial():
    imagebutton idle "gui/tutorial1.webp" action Hide('basetutorial')  , ShowMenu('basetutorialb')

screen basetutorialb():
    imagebutton idle "gui/tutorial2.webp" action Hide('basetutorialb')  , Start('chapterone')

screen tutorialquit():
    imagebutton:
        align (0.5, 0.44)
        auto "gui/tutorialquit_%s.webp"
        action Play("ch_one", "sfx/phone_back.mp3"), MainMenu(True, False)



define calendar_months = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}
define calendar_days = {
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6,
    'Sunday': 7
}
screen screen_calendar():
    style_prefix "calendar"

    if ian_active:
        $ parent = 'ian'
    else:
        $ parent = 'lena'

    frame style "empty":
        imagebutton idle "gui/%scalendar.webp" % parent action Return()
        if prev_day != day:
            text prev_day size 120 ypos 430 at prev_day_transform(direction=anim_day_dir)
            text day size 120 ypos 430 at curr_day_transform(direction=anim_day_dir)
        else:
            text day size 120 ypos 430

        vbox:
            ypos 705
            xalign 0.5
            hbox:
                frame style "empty" xsize max_len_month * 20:
                    if prev_month != month:
                        text "[prev_month]" size 60 xalign 1.0 at prev_day_transform(w=1.7, direction=anim_month_dir * 0.5)
                        text "[month]" size 60 xalign 1.0 at curr_day_transform(w=1.8, direction=anim_month_dir * 0.5)
                    else:
                        text "[month]" size 60 xalign 1.0

                text ", week " size 60

                frame style "empty" xsize 30:
                    if prev_week != week:
                        text "[prev_week]" size 60 at prev_day_transform(w=1.7, direction=anim_week_dir * 0.5)
                        text "[week]" size 60 at curr_day_transform(w=1.8, direction=anim_week_dir * 0.5)
                    else:
                        text "[week]" size 60

    key "dismiss" action Return()

style calendar_text:
    font font_peach_pen
    xalign 0.5


transform prev_day_transform(w=0.9, direction=1):

    alpha 1.0
    yoffset 0
    pause w

    block:
        parallel:
            ease 0.6 alpha 0.0
        parallel:
            ease 0.6 yoffset -100 * direction

transform curr_day_transform(w=1.0, direction=1):

    alpha 0.0
    yoffset 100 * direction
    pause w

    block:
        parallel:
            ease 0.6 alpha 1.0
        parallel:
            ease 0.6 yoffset 0


define chapter_titles = {
    0: ('Zero', ''),
    1: ('One', 'Two sides of the coin'),
    2: ('Two', 'Close at hand'),
    3: ('Three', 'Knots'),
    4: ('Four', 'Elastic Hearts'),
    5: ('Five', 'Playing the field'),
    6: ('Six', 'In full swing'),
    7: ('Seven', 'Heavenly Sins'),
    8: ('Eight', 'Falling into place'),
    9: ('Nine', 'Lust and Power'),
    10: ('Ten', 'Thread the needle'),
    11: ('Eleven', 'Wounds'),
    12: ('Twelve', 'Waves'),
    13: ('Thirteen', 'Taking root'),
    14: ('Fourteen', 'Blazing'),
    15: ('Fifteen', ''),
    16: ('Sixteen', ''),
    17: ('Seventeen', ''),
    18: ('Eighteen', ''),
    19: ('Nineteen', ''),
    20: ('Twenty', ''),
}

init python:
    def get_chapter_number_text():
        global chapter, chapter_titles
        return chapter_titles[chapter][0]

    def get_chapter_subtitle():
        global chapter, chapter_titles
        return chapter_titles[chapter][1]

screen chapter_title():
    tag chapter_title
    style_prefix "chapter_title"

    add "gui/bg.webp"

    vbox:
        align (0.5, 0.4)
        spacing 50
        text "Chapter {color=#c4002e}%s{/color}" % get_chapter_number_text() style "chapter_title_text_title"
        text get_chapter_subtitle()

    imagebutton idle "#0000" action Return()
    key "dismiss" action Return()

style chapter_title_text:
    font font_peach_pen
    xalign 0.5
    size 100

style chapter_title_text_title is chapter_title_text:
    size 190
    font font_red_string
    xoffset -40

label label_chapter_title:
    $ quick_menu = False
    pause 0.3
    scene blackbg with long_dissolve
    $ renpy.checkpoint()
    call screen chapter_title with long_dissolve
    show screen chapter_title
    hide screen chapter_title with long_dissolve
    $ renpy.pause(0.5)
    scene black with long_dissolve
    $ quick_menu = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
