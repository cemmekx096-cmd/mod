




transform bing:
    xalign 0.5 yalign 0.5
    linear 0.5 yalign 0.0

transform slide:
    xalign 0.5 yalign 0.5
    linear 0.5 yalign 0.0
    linear 1.0 yalign 0.5

define flash = Fade(0.1, 0.0, 0.5, color="#fff")
define long_dissolve = Dissolve(1.0)
define long = Dissolve (0.6)
define short = Dissolve (0.3)
define fps = Dissolve (0.25)
define fps2 = Dissolve (0.2)
define fps3 = Dissolve (0.15)


transform right5:
    xalign 1.09
transform rig4b:
    xalign 0.94
transform rig4:
    xalign 0.90
transform rig3:
    xalign 0.85
transform rig2:
    xalign 0.80
transform rig5b:
    xalign 0.80
transform rig1:
    xalign 0.75
transform rig5:
    xalign 0.75

transform rig:
    xalign 0.70

transform centerrig2:
    xalign 0.60
transform centerrig:
    xalign 0.55



transform centerlef2:
    xalign 0.40
transform centerlef:
    xalign 0.35

transform lef:
    xalign 0.30


transform lef5:
    xalign 0.20
transform lef2:
    xalign 0.20
transform lef3:
    xalign 0.15
transform lef4:
    xalign 0.10


transform left5:
    xpos -80
transform left_peek:
    xpos -170
transform left_peek2:
    xpos -200



transform phone_img_left:
    xpos -620
transform phone_img_right:
    xpos 620

transform fade_in_skill:
    alpha 0.0
    easein 1.0 alpha 1.0


transform transform_gallery_unlock:
    on show:
        zoom 0.8
        alpha 0.0
        block:
            parallel:
                linear 0.3 zoom 1.0
            parallel:
                linear 0.3 alpha 1.0

        pause 3
        linear 0.4 alpha 0.0

transform transform_stat_up(yoffset=0):
    alpha 0.0
    zoom 0.25
    yoffset yoffset
    align (0.5, 0.5)
    pos (236, 880)

    parallel:
        linear 0.2 alpha 1.0
    parallel:
        linear 0.2 zoom 1.0
    parallel:
        linear 0.9 ypos 580
    parallel:
        pause 0.65
        linear 0.25 alpha 0.0

transform transform_stat_down(yoffset=0):
    alpha 0.0
    zoom 0.25
    yoffset yoffset
    align (0.5, 0.5)
    pos (236, 530)

    parallel:
        linear 0.2 alpha 1.0
    parallel:
        linear 0.2 zoom 1.0
    parallel:
        linear 0.9 ypos 830
    parallel:
        pause 0.65
        linear 0.25 alpha 0.0


image village = Composite(
    (1920, 1080),
    (0, 0), "village_bg.webp",
    (0, 0), ConditionSwitch(
        "chapter < 9", "village_carp.webp",
        "True", Null()
    ),
)
image villagenight = Composite(
    (1920, 1080),
    (0, 0), "villagenight_bg.webp",
    (0, 0), ConditionSwitch(
        "chapter < 9", "villagenight_carp.webp",
        "True", Null()
    ),
)
image ianroom = Composite(
    (1920, 1080),
    (0, 0), "ianroom.webp",
    (0, 0), ConditionSwitch(
        "v12_cherry_painting", "ianroom_painting.webp",
        "True", Null()
    ),
)
image ianroomnight = Composite(
    (1920, 1080),
    (0, 0), "ianroomnight.webp",
    (0, 0), ConditionSwitch(
        "v12_cherry_painting", "ianroomnight_painting.webp",
        "True", Null()
    ),
)
image ianroomnight_dark = Composite(
    (1920, 1080),
    (0, 0), "ianroomnight_dark.webp",
    (0, 0), ConditionSwitch(
        "v12_cherry_painting", "ianroomnight_dark_painting.webp",
        "True", Null()
    ),
)







image v1_ianfap_animation:
    "images/v1_ianfap.webp" with fps
    pause 0.6
    "images/v1_ianfapb.webp" with fps
    pause 0.6
    repeat



image v2_robert5_animation:
    "images/v2_robert5.webp" with fps
    pause 0.7
    "images/v2_robert5b.webp" with fps
    pause 0.7
    repeat
image v2_robert6_animation:
    "images/v2_robert6.webp" with fps
    pause 0.7
    "images/v2_robert6b.webp" with fps
    pause 0.7
    repeat
image v2_robert6_animation2:
    "images/v2_robert6.webp" with fps
    pause 0.3
    "images/v2_robert6b.webp" with fps
    pause 0.3
    repeat
image v2_robert7_animation1:
    "images/v2_robert7b.webp" with fps
    pause 0.7
    "images/v2_robert7bb.webp" with fps
    pause 0.7
    repeat
image v2_robert7_animation2:
    "images/v2_robert7.webp" with fps
    pause 0.7
    "images/v2_robert7a.webp" with fps
    pause 0.7
    repeat
image v2_alison5_animation:
    "images/v2_alison5.webp" with fps
    pause 0.7
    "images/v2_alison5b.webp" with fps
    pause 0.7
    repeat
image v2_alison6_animation:
    "images/v2_alison6.webp" with fps
    pause 0.7
    "images/v2_alison6a.webp" with fps
    pause 0.7
    repeat
image v2_alison6_animation2:
    "images/v2_alison6.webp" with fps
    pause 0.4
    "images/v2_alison6a.webp" with fps
    pause 0.4
    repeat
image v2_alison6b_animation:
    "images/v2_alison6b.webp" with fps
    pause 0.7
    "images/v2_alison6ba.webp" with fps
    pause 0.7
    repeat
image v2_alison6b_animation2:
    "images/v2_alison6b.webp" with fps
    pause 0.4
    "images/v2_alison6ba.webp" with fps
    pause 0.4
    repeat
image v2_cherry4_animation:
    "images/v2_cherry4.webp" with fps
    pause 0.7
    "images/v2_cherry4a.webp" with fps
    pause 0.7
    repeat
image v2_cherry4b_animation:
    "images/v2_cherry4b.webp" with fps
    pause 0.7
    "images/v2_cherry4ba.webp" with fps
    pause 0.7
    repeat
image v2_cherry5_animation:
    "images/v2_cherry5.webp" with fps
    pause 0.7
    "images/v2_cherry5b.webp" with fps
    pause 0.7
    repeat
image v2_cherry5_animation2:
    "images/v2_cherry5.webp" with fps
    pause 0.4
    "images/v2_cherry5b.webp" with fps
    pause 0.4
    repeat



image v3_cherry2_animation:
    "images/v3_cherry2.webp" with fps
    pause 0.7
    "images/v3_cherry2b.webp" with fps
    pause 0.7
    repeat
image v3_cherry2_animation2:
    "images/v3_cherry2.webp" with fps
    pause 0.4
    "images/v3_cherry2b.webp" with fps
    pause 0.4
    repeat
image v3_alison5_animation:
    "images/v3_alison5.webp" with fps
    pause 0.7
    "images/v3_alison5b.webp" with fps
    pause 0.7
    repeat
image v3_alison6_animation:
    "images/v3_alison6.webp" with fps
    pause 0.4
    "images/v3_alison6b.webp" with fps
    pause 0.4
    repeat
image v3_alison7_animation:
    "images/v3_alison7.webp" with fps
    pause 0.7
    "images/v3_alison7b.webp" with fps
    pause 0.7
    repeat
image v3_alison7cum_animation:
    "images/v3_alison7cum.webp" with fps
    pause 0.7
    "images/v3_alison7cumb.webp" with fps
    pause 0.7
    repeat
image v3_alison8_animation:
    "images/v3_alison8.webp" with fps
    pause 0.7
    "images/v3_alison8b.webp" with fps
    pause 0.7
    repeat
image v3_solo1_animation:
    "images/v3_solo1.webp" with fps
    pause 0.7
    "images/v3_solo1b.webp" with fps
    pause 0.7
    repeat
image v3_louise2_animation:
    "images/v3_louise2.webp" with vpunch
    pause 0.7
    "images/v3_louise2b.webp" with fps
    pause 0.7
    repeat
image v3_louise3_animation:
    "images/v3_louise3.webp" with fps
    pause 0.5
    "images/v3_louise3b.webp" with fps
    pause 0.5
    repeat



image v4_solo2_animation:
    "images/v4_solo2.webp" with short
    pause 1
    "images/v4_solo2b.webp" with short
    pause 1
    repeat
image v4_solo3_animation:
    "images/v4_solo3.webp" with short
    pause 0.7
    "images/v4_solo3b.webp" with short
    pause 0.7
    repeat
image v4_robert_animation:
    "images/v4_restaurant3.webp" with fps
    pause 0.5
    "images/v4_restaurant3b.webp" with fps
    pause 0.5
    repeat
image v4_robert_animation2:
    "images/v4_restaurant4.webp" with fps
    pause 0.4
    "images/v4_restaurant4b.webp" with fps
    pause 0.4
    repeat



image v5_emma7_animation:
    "images/v5_emma7.webp" with fps
    pause 0.7
    "images/v5_emma7b.webp" with fps
    pause 0.7
    repeat
image v5_emma7_animation_slow:
    "images/v5_emma7.webp" with fps
    pause 1
    "images/v5_emma7b.webp" with fps
    pause 1
    repeat
image v5_emma7_animation_fast:
    "images/v5_emma7.webp" with fps
    pause 0.4
    "images/v5_emma7b.webp" with fps
    pause 0.4
    repeat
image v5_emma8_animation:
    "images/v5_emma8.webp" with fps2
    pause 0.5
    "images/v5_emma8b.webp" with fps2
    pause 0.5
    repeat
image v5_alison4_animation:
    "images/v5_alison4.webp" with fps
    pause 0.7
    "images/v5_alison4b.webp" with fps
    pause 0.7
    repeat
image v5_louise6_animation:
    "images/v5_louise6.webp" with fps
    pause 0.7
    "images/v5_louise6b.webp" with fps
    pause 0.7
    repeat
image v5_mike5_animation:
    "images/v5_mike5a.webp" with fps
    pause 0.7
    "images/v5_mike5aa.webp" with fps
    pause 0.7
    repeat

image v5_stalkfap1_comp = Composite(
    (1920, 1080),
    (0, 0), "images/v5_stalkfap1.webp",
    (0, 0), ConditionSwitch(
        "v4_piercing == 1", "v5_stalkfap1_p1.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch(
        "v4_piercing == 2", "v5_stalkfap1_p2.webp",
        "True", Null()
    ),
)
image v5_stalkfap_post_comp = Composite(
    (1920, 1080),
    (0, 0), "images/v5_stalkfap_post.webp",
    (0, 0), ConditionSwitch(
        "v4_piercing == 1", "v5_stalkfap_post_p1.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch(
        "v4_piercing == 2", "v5_stalkfap_post_p2.webp",
        "True", Null()
    ),
)

image v5_sexting1_comp = Composite(
    (1920, 1080),
    (0, 0), "images/v5_sexting1.webp",
    (0, 0), ConditionSwitch(
        "v4_piercing == 1", "v5_sexting1_p1.webp",
        "v4_piercing == 2", "v5_sexting1_p2.webp",
        "True", Null()
    ),
)
image v5_sexting3_comp = Composite(
    (1920, 1080),
    (0, 0), "images/v5_sexting3.webp",
    (0, 0), ConditionSwitch(
        "v4_piercing == 1", "v5_sexting3_p1.webp",
        "v4_piercing == 2", "v5_sexting3_p2.webp",
        "True", Null()
    ),
)
image v5_sexting4_comp = Composite(
    (1920, 1080),
    (0, 0), "images/v5_sexting4.webp",
    (0, 0), ConditionSwitch(
        "v4_piercing == 1", "v5_sexting4_p1.webp",
        "v4_piercing == 2", "v5_sexting4_p2.webp",
        "True", Null()
    ),
)
image v5_sexting5_comp = Composite(
    (1920, 1080),
    (0, 0), "images/v5_sexting5.webp",
    (0, 0), ConditionSwitch(
        "v4_piercing == 1", "v5_sexting5_p1.webp",
        "v4_piercing == 2", "v5_sexting5_p2.webp",
        "True", Null()
    ),
)




image v6_cherry5_animation:
    "images/v6_cherry5.webp" with short
    pause 0.7
    "images/v6_cherry5b.webp" with short
    pause 0.7
    repeat
image v6_cherry5_animation2:
    "images/v6_cherry5.webp" with fps
    pause 0.4
    "images/v6_cherry5b.webp" with fps
    pause 0.4
    repeat


image v6_lena5_animation:
    "images/v6_lena5.webp" with fps
    pause 0.7
    "images/v6_lena6a.webp" with fps
    pause 0.7
    repeat
image v6_lena5_choker_animation:
    "images/v6_lena5_choker.webp" with fps
    pause 0.7
    "images/v6_lena6_choker.webp" with fps
    pause 0.7
    repeat
image v6_lena6_animation:
    "images/v6_lena7.webp" with fps
    pause 0.7
    "images/v6_lena6.webp" with fps
    pause 0.7
    repeat
image v6_lena6_choker_animation:
    "images/v6_lena7_choker.webp" with fps
    pause 0.7
    "images/v6_lena6_choker.webp" with fps
    pause 0.7
    repeat
image v6_lena7_animation:
    "images/v6_lena7.webp" with fps
    pause 0.4
    "images/v6_lena6.webp" with fps
    pause 0.4
    repeat
image v6_lena7_choker_animation:
    "images/v6_lena7_choker.webp" with fps
    pause 0.4
    "images/v6_lena6_choker.webp" with fps
    pause 0.4
    repeat
image v6_lena7_hand_animation:
    "images/v6_lena7_hand2.webp" with fps
    pause 0.4
    "images/v6_lena7_hand1.webp" with fps
    pause 0.4
    repeat


image v6_minerva5_animation:
    "images/v6_minerva5.webp" with fps
    pause 0.7
    "images/v6_minerva5b.webp" with fps
    pause 0.7
    repeat
image v6_minerva8_animation:
    "images/v6_minerva8.webp" with vpunch
    pause 1.5
    "images/v6_minerva8.webp" with vpunch
    repeat


image v6_stalkfap_twerk:
    "images/v6_stalkfap_twerk1.webp" with fps3
    pause 0.2
    "images/v6_stalkfap_twerk2.webp" with fps3
    pause 0.2
    "images/v6_stalkfap_twerk3.webp" with fps3
    pause 0.2
    repeat


image v6_solo3_animation:
    "images/v6_solo3a.webp" with fps
    pause 0.6
    "images/v6_solo3b.webp" with fps
    pause 0.6
    repeat


image v6_mike4_comp = Composite(
    (1920, 1080),
    (0, 0), "v6_mike4.webp",
    (0, 0), "v6_ian2_spit.webp",
    )
image v6_mike2_animation:
    "images/v6_mike2.webp" with fps
    pause 0.6
    "images/v6_mike2b.webp" with fps
    pause 0.6
    repeat
image v6_mike4_animation:
    "v6_mike4_comp" with fps
    pause 0.6
    "images/v6_mike4b.webp" with fps
    pause 0.6
    repeat
image v6_mike5_animation:
    "images/v6_mike5.webp" with fps
    pause 0.8
    "images/v6_mike5b.webp" with fps
    pause 0.8
    repeat
image v6_mike6_animation:
    "images/v6_mike6b.webp" with fps
    pause 0.7
    "images/v6_mike6a.webp" with fps
    pause 0.7
    repeat


image v6_robert2_comp = Composite(
    (1920, 1080),
    (0, 0), "v6_robert2.webp",
    (0, 0), "v6_ian2_spit.webp",
    )
image v6_robert2_animation:
    "v6_robert2_comp" with fps
    pause 0.6
    "images/v6_robert2b.webp" with fps
    pause 0.6
    repeat

image v6_robert2_bunny_animation:
    "images/v6_robert2_bunny.webp" with fps
    pause 0.6
    "images/v6_robert2b_bunny.webp" with fps
    pause 0.6
    repeat

image v6_robert4_animation:
    "images/v6_robert4.webp" with fps
    pause 0.8
    "images/v6_robert4b.webp" with fps
    pause 0.8
    repeat


image v6_ian2_comp = Composite(
    (1920, 1080),
    (0, 0), "v6_ian2.webp",
    (0, 0), "v6_ian2_spit.webp",
    )
image v6_ian2_animation:
    "v6_ian2_comp" with fps
    pause 0.6
    "images/v6_ian2b.webp" with fps
    pause 0.6
    repeat
image v6_ian3_animation:
    "images/v6_ian3b.webp" with fps
    pause 0.8
    "images/v6_ian3.webp" with fps
    pause 0.8
    repeat


image v6_axel6_animation:
    "images/v6_axel6b.webp" with fps
    pause 0.7
    "images/v6_axel6a.webp" with fps
    pause 0.7
    repeat

image v6_lena_selfie2_comp = Composite(
    (1920, 1080),
    (0, 0), "images/v6_lena_selfie2.webp",
    (0, 0), ConditionSwitch(
        "v4_piercing == 1", "v6_lena_selfie2_p1.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch(
        "v4_piercing == 2", "v6_lena_selfie2_p2.webp",
        "True", Null()
    ),
)
image v6_robertpic1b_comp = Composite(
    (1920, 1080),
    (0, 0), "images/v6_robertpic1b.webp",
    (0, 0), ConditionSwitch(
        "v4_piercing == 1", "v6_robertpic1_p1.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch(
        "v4_piercing == 2", "v6_robertpic1_p2.webp",
        "True", Null()
    ),
)
image v6_robertpic1a_comp = Composite(
    (1920, 1080),
    (0, 0), "images/v6_robertpic1a.webp",
    (0, 0), ConditionSwitch(
        "v4_piercing == 1", "v6_robertpic1_p1.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch(
        "v4_piercing == 2", "v6_robertpic1_p2.webp",
        "True", Null()
    ),
)
image v6_mikepic1_comp = Composite(
    (1920, 1080),
    (0, 0), "images/v6_mikepic1.webp",
    (0, 0), ConditionSwitch(
        "v4_piercing == 1", "v6_robertpic1_p1.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch(
        "v4_piercing == 2", "v6_robertpic1_p2.webp",
        "True", Null()
    ),
)




image v7_jerkoff_animation1:
    "images/v7_jerkoff1.webp" with fps
    pause 0.8
    "images/v7_jerkoff2.webp" with fps
    pause 0.8
    repeat
image v7_jerkoff_animation2:
    "images/v7_jerkoff1.webp" with fps
    pause 0.4
    "images/v7_jerkoff2.webp" with fps
    pause 0.4
    repeat
image v7_jerkoff_animation1b:
    "images/v7_jerkoff1b.webp" with fps
    pause 0.8
    "images/v7_jerkoff2b.webp" with fps
    pause 0.8
    repeat
image v7_jerkoff_animation2b:
    "images/v7_jerkoff1b.webp" with fps
    pause 0.4
    "images/v7_jerkoff2b.webp" with fps
    pause 0.4
    repeat


image v7_minerva4_animation:
    "images/v7_minerva4a.webp" with fps
    pause 0.4
    "images/v7_minerva4b.webp" with fps
    pause 0.4
    repeat


image v7_solo2_animation:
    "v7_solo2b_comp" with fps
    pause 0.7
    "v7_solo2a_comp" with fps
    pause 0.7
    repeat
image v7_solo3_animation:
    "v7_solo3b_comp" with fps
    pause 0.7
    "v7_solo3a_comp" with fps
    pause 0.7
    repeat
image v7_solo4_animation:
    "v7_solo4b_comp" with fps
    pause 0.7
    "v7_solo4a_comp" with fps
    pause 0.7
    repeat


image v7_lena4_animation:
    "images/v7_lena4b.webp" with fps
    pause 0.7
    "images/v7_lena4a.webp" with fps
    pause 0.7
    repeat
image v7_lena7_animation:
    "images/v7_lena7b.webp" with vpunch
    pause 1.0
    "images/v7_lena7.webp" with fps
    pause 1.0
    repeat
image v7_lena7_cum_animation:
    "images/v7_lena7_cum.webp" with vpunch
    pause 1.0
    "images/v7_lena7_cum.webp" with fps
    pause 1.0
    repeat
image v7_lena8_animation:
    "images/v7_lena8b.webp" with fps
    pause 1.0
    "images/v7_lena8.webp" with fps
    pause 1.0
    repeat


image v7_mike2a_animation:
    "images/v7_mike3a.webp" with fps
    pause 0.6
    "images/v7_mike2a.webp" with fps
    pause 0.6
    repeat
image v7_mike2b_animation:
    "images/v7_mike3b.webp" with fps
    pause 0.6
    "images/v7_mike2b.webp" with fps
    pause 0.6
    repeat
image v7_mike2c_animation:
    "images/v7_mike3c.webp" with fps
    pause 0.6
    "images/v7_mike2c.webp" with fps
    pause 0.6
    repeat
image v7_mike2a_animation_fast:
    "images/v7_mike3a.webp" with fps
    pause 0.3
    "images/v7_mike2a.webp" with fps
    pause 0.3
    repeat
image v7_mike2b_animation_fast:
    "images/v7_mike3b.webp" with fps
    pause 0.3
    "images/v7_mike2b.webp" with fps
    pause 0.3
    repeat
image v7_mike2c_animation_fast:
    "images/v7_mike3c.webp" with fps
    pause 0.3
    "images/v7_mike2c.webp" with fps
    pause 0.3
    repeat
image v7_mike4a_animation:
    "images/v7_mike5a.webp" with short
    pause 1.2
    "images/v7_mike4a.webp" with short
    pause 1
    repeat
image v7_mike4b_animation:
    "images/v7_mike5b.webp" with short
    pause 1.2
    "images/v7_mike4b.webp" with short
    pause 1
    repeat
image v7_mike4c_animation:
    "images/v7_mike5c.webp" with short
    pause 1.2
    "images/v7_mike4c.webp" with short
    pause 1
    repeat
image v7_mike4_choker_animation:
    "images/v7_mike5_choker.webp" with short
    pause 1.2
    "images/v7_mike4_choker.webp" with short
    pause 1
    repeat
image v7_mike4_sy_animation:
    "images/v7_mike5_sy.webp" with short
    pause 1.2
    "images/v7_mike4_sy.webp" with short
    pause 1
    repeat


image v7_jeremy4_animation1:
    "images/v7_jeremy4a.webp" with Dissolve (0.2)
    pause 0.4
    "images/v7_jeremy4b.webp" with Dissolve (0.2)
    pause 0.4
    "images/v7_jeremy4c.webp" with Dissolve (0.2)
    pause 0.4
    "images/v7_jeremy4b.webp" with Dissolve (0.2)
    pause 0.4
    repeat
image v7_jeremy4_animation2:
    "images/v7_jeremy4a.webp" with Dissolve (0.1)
    pause 0.2
    "images/v7_jeremy4b.webp" with Dissolve (0.1)
    pause 0.2
    "images/v7_jeremy4c.webp" with Dissolve (0.1)
    pause 0.2
    "images/v7_jeremy4b.webp" with Dissolve (0.1)
    pause 0.2
    repeat


image v7_dance6_animation:
    "images/v7_dance6a.webp" with fps
    pause 0.3
    "images/v7_dance6b.webp" with fps
    pause 0.3
    repeat
image v7_dance7_animation:
    "images/v7_dance7a.webp" with fps
    pause 0.3
    "images/v7_dance7b.webp" with fps
    pause 0.3
    repeat


image v7_emma1_animation:
    "images/v7_emma1.webp" with fps
    pause 0.5
    "images/v7_emma1b.webp" with fps
    pause 0.5
    repeat
image v7_emma3_animation:
    "images/v7_emma3b.webp" with fps
    pause 0.6
    "images/v7_emma3.webp" with fps
    pause 0.6
    repeat


image v7_alison3_animation_arm:
    "images/v7_alison3b_arm.webp" with fps
    pause 0.5
    "images/v7_alison3_arm.webp" with vpunch
    pause 0.5
    repeat
image v7_alison3_animation:
    "images/v7_alison3b.webp" with fps
    pause 0.5
    "images/v7_alison3.webp" with vpunch
    pause 0.5
    repeat
image v7_alison4_animation:
    "images/v7_alison4.webp" with fps
    pause 0.4
    "images/v7_alison4b.webp" with fps
    pause 0.4
    repeat


image v7_cindy11_animation:
    "images/v7_cindy11.webp" with vpunch
    pause 1
    "images/v7_cindy11b.webp" with fps
    pause 0.6
    repeat
image v7_cindy12_animation:
    "images/v7_cindy12.webp" with fps
    pause 0.6
    "images/v7_cindy12b.webp" with vpunch
    pause 1
    repeat


image v7_holly5_animation:
    "images/v7_holly5.webp" with fps
    pause 0.8
    "images/v7_holly5b.webp" with fps
    pause 0.8
    repeat

image v7_solo2a_comp = Composite(
    (1920, 1080),
    (0, 0), "images/v7_solo2a.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", "v7_solo2a_t2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch(
        "v10_lena_masturbate == 2", "v7_solo2_plug.webp",
        "True", Null()
    ),
)
image v7_solo2b_comp = Composite(
    (1920, 1080),
    (0, 0), "images/v7_solo2b.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", "v7_solo2b_t2.webp",
        "True", Null()
    ),
)
image v7_solo3a_comp = Composite(
    (1920, 1080),
    (0, 0), "images/v7_solo3a.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", "v7_solo2a_t2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch(
        "v10_lena_masturbate == 2", "v7_solo2_plug.webp",
        "True", Null()
    ),
)
image v7_solo3b_comp = Composite(
    (1920, 1080),
    (0, 0), "images/v7_solo3b.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", "v7_solo2b_t2.webp",
        "True", Null()
    ),
)
image v7_solo4a_comp = Composite(
    (1920, 1080),
    (0, 0), "images/v7_solo4a.webp",
    (0, 0), ConditionSwitch(
        "lena_piercing1", "v7_solo4_p1.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch(
        "lena_piercing2", "v7_solo4_p2.webp",
        "True", Null()
    ),
)
image v7_solo4b_comp = Composite(
    (1920, 1080),
    (0, 0), "images/v7_solo4b.webp",
    (0, 0), ConditionSwitch(
        "lena_piercing1", "v7_solo4_p1.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch(
        "lena_piercing2", "v7_solo4_p2.webp",
        "True", Null()
    ),
)
image v7_solo4c_comp = Composite(
    (1920, 1080),
    (0, 0), "images/v7_solo4c.webp",
    (0, 0), ConditionSwitch(
        "lena_piercing1", "v7_solo4_p1.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch(
        "lena_piercing2", "v7_solo4_p2.webp",
        "True", Null()
    ),
)




image v8_hotel4_animation:
    "images/v8_hotel4.webp" with fps
    pause 0.5
    "images/v8_hotel4b.webp" with fps
    pause 0.5
    repeat


image v8_stalkfap3:
    "images/v8_stalkfap3a.webp" with fps
    pause 0.3
    "images/v8_stalkfap3b.webp" with fps
    pause 0.3
    repeat
image v8_stalkfap4:
    "images/v8_stalkfap4a.webp" with fps
    pause 0.3
    "images/v8_stalkfap4b.webp" with fps
    pause 0.3
    repeat
image lsd1:
    "images/lsd1a.webp" with Dissolve (2)
    pause 2
    "images/lsd1b.webp" with Dissolve (2)
    pause 2
    repeat
image lsd2:
    "images/lsd2a.webp" with Dissolve (2)
    pause 2
    "images/lsd2b.webp" with Dissolve (2)
    pause 2
    repeat
image lsd3:
    "images/lsd3a.webp" with Dissolve (1.5)
    pause 1.5
    "images/lsd3b.webp" with Dissolve (1.5)
    pause 1.5
    repeat
image lsd4:
    "images/lsd4a.webp" with Dissolve (2)
    pause 2
    "images/lsd4b.webp" with Dissolve (2)
    pause 2
    repeat


image v8_jeremy3_comp = Composite(
    (1920, 1080),
    (0, 0), "v8_jeremy3.webp",
    (0, 0), ConditionSwitch(
        "chapter == 8", "v8_jeremy3_spit.webp",
        "True", Null()
    ),
)
image v8_jeremy3_animation:
    "v8_jeremy3_comp" with fps
    pause 0.6
    "images/v8_jeremy3b.webp" with fps
    pause 0.6
    repeat
image v8_jeremy3_animation2:
    "v8_jeremy3_comp" with fps
    pause 0.3
    "images/v8_jeremy3b.webp" with fps
    pause 0.3
    repeat
image v8_jeremy4_animation:
    "images/v8_jeremy4.webp" with fps
    pause 0.3
    "images/v8_jeremy4a.webp" with fps
    pause 0.3
    repeat
image v8_mike4_animation:
    "images/v8_mike4a.webp" with fps
    pause 0.6
    "images/v8_mike4b.webp" with fps
    pause 0.6
    repeat

image v8_sexting2_comp = Composite(
    (1920, 1080),
    (0, 0), "images/v8_sexting2.webp",
    (0, 0), ConditionSwitch( 
        "v7_piercing == 1", "v8_sexting2_p1.webp", 
        "v7_piercing == 2", "v8_sexting2_p2.webp",
        "v4_piercing == 1", "v8_sexting2_p1.webp", 
        "v4_piercing == 2", "v8_sexting2_p2.webp",
        "True", Null()
    ),
)

image v8_stalkfap1_comp = Composite(
    (1920, 1080),
    (0, 0), "images/v8_stalkfap1.webp",
    (0, 0), ConditionSwitch( 
        "v7_piercing == 1", "v8_stalkfap1_p1.webp", 
        "v7_piercing == 2", "v8_stalkfap1_p2.webp",
        "v4_piercing == 1", "v8_stalkfap1_p1.webp", 
        "v4_piercing == 2", "v8_stalkfap1_p2.webp",
        "True", Null()
    ),
)

image v8_stalkfap2_comp = Composite(
    (1920, 1080),
    (0, 0), "images/v8_stalkfap2.webp",
    (0, 0), ConditionSwitch( 
        "v7_piercing == 1", "v8_stalkfap2_p1.webp", 
        "v7_piercing == 2", "v8_stalkfap2_p2.webp",
        "v4_piercing == 1", "v8_stalkfap2_p1.webp", 
        "v4_piercing == 2", "v8_stalkfap2_p2.webp",
        "True", Null()
    ),
)

image v8_stalkfap5_comp = Composite(
    (1920, 1080),
    (0, 0), ConditionSwitch(
        "v7_dance == 0", "v8_stalkfap5a.webp",
        "v7_dance == 1", "v8_stalkfap5b.webp",
        "v7_dance == 2", "v8_stalkfap5c.webp"),
    (0, 0), ConditionSwitch( 
        "v7_piercing == 1", "v8_stalkfap5_p1.webp", 
        "v7_piercing == 2", "v8_stalkfap5_p2.webp",
        "v4_piercing == 1", "v8_stalkfap5_p1.webp", 
        "v4_piercing == 2", "v8_stalkfap5_p2.webp",
        "True", Null()
    ),
)

image v8_selfie_alison3_comp = Composite(
    (1920, 1080),
    (0, 0), "v8_selfie_alison3.webp",
    (0, 0), ConditionSwitch(

        "True", Null()
    ),
)



transform fireworks_anim:
    alpha 0.0
    yoffset 100
    parallel:
        linear 1.0 alpha 1.0
    parallel:
        linear 2.2 yoffset -200
    parallel:
        pause 2.0
        linear 0.2 alpha 0.5
    yoffset 0
    linear 0.2 alpha 1.0

transform fireworks_anim2:
    alpha 0.0
    yoffset 100
    xoffset -200
    parallel:
        linear 1.0 alpha 1.0
    parallel:
        linear 2.2 yoffset -100
    parallel:
        pause 2.0
        linear 0.2 alpha 0.5
    yoffset 0
    linear 0.2 alpha 1.0

transform fireworks_anim3:
    alpha 0.0
    yoffset 300
    xoffset -400
    parallel:
        linear 1.0 alpha 1.0
    parallel:
        linear 2.2 yoffset -100
    parallel:
        pause 2.0
        linear 0.2 alpha 0.5
    yoffset 200
    linear 0.2 alpha 1.0

image fireworks:
    "images/fireworks1.webp"
    pause 2.2
    "images/fireworks2.webp"


image v9_lena9a_animation:
    "images/v9_lena9a.webp" with vpunch
    pause 0.3
    "images/v9_lena10a.webp" with fps3
    pause 0.2
    "images/v9_lena11a.webp" with fps3
    pause 0.2
    "images/v9_lena10a.webp" with fps3
    pause 0.1
    repeat
image v9_lena9b_animation:
    "images/v9_lena9b.webp" with vpunch
    pause 0.3
    "images/v9_lena10b.webp" with fps3
    pause 0.2
    "images/v9_lena11b.webp" with fps3
    pause 0.2
    "images/v9_lena10b.webp" with fps3
    pause 0.1
    repeat


image v9_axel6_animation:
    "images/v9_axel6a.webp" with short
    pause 0.6
    "images/v9_axel6b.webp" with vpunch
    pause 0.4
    repeat
image v9_axel_bj_animation1:
    "v9_axel9_comp" with fps
    pause 0.6
    "v9_axel10_comp" with fps
    pause 0.6
    repeat
image v9_axel_bj_animation2:
    "v9_axel9b_comp" with fps
    pause 0.5
    "v9_axel10b_comp" with fps
    pause 0.5
    repeat
image v9_axel9_comp = Composite(
    (1920, 1080),
    (0, 0), "v9_axel9.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2 == True", "v9_axel9_t2.webp",
        "True", Null()
    ),
)
image v9_axel10_comp = Composite(
    (1920, 1080),
    (0, 0), "v9_axel10.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2 == True", "v9_axel10_t2.webp",
        "True", Null()
    ),
)
image v9_axel9b_comp = Composite(
    (1920, 1080),
    (0, 0), "v9_axel9b.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2 == True", "v9_axel9_t2.webp",
        "True", Null()
    ),
)
image v9_axel10b_comp = Composite(
    (1920, 1080),
    (0, 0), "v9_axel10b.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2 == True", "v9_axel10_t2.webp",
        "True", Null()
    ),
)


image v9_emma4_animation:
    "images/v9_emma4a.webp" with fps
    pause 0.6
    "images/v9_emma4b.webp" with fps
    pause 0.6
    repeat

image v9_lena_selfie1_comp = Composite(
    (1920, 1080),
    (0, 0), "v9_lena_selfie1.webp",
    (0, 0), ConditionSwitch( 
        "v7_piercing == 1", "v9_lena_selfie1_p1.webp", 
        "v7_piercing == 2", "v9_lena_selfie1_p2.webp",
        "v4_piercing == 1", "v9_lena_selfie1_p1.webp", 
        "v4_piercing == 2", "v9_lena_selfie1_p2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch(  
        "lena_tattoo1 == True and not (v9_tat == 1 or v10_tat == 1)", "v9_lena_selfie1_t1.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_tattoo3 == True and not (v9_tat == 3 or v10_tat == 3)", "v9_lena_selfie1_t3.webp",
        "True", Null()
    ),
)
image v9_alison_pic1_comp = Composite(
    (1920, 1080),
    (0, 0), "v9_alison_pic1.webp",
    (0, 0), ConditionSwitch(

        "True", Null()
    ),
)
image v9_alison_pic3_comp = Composite(
    (1920, 1080),
    (0, 0), "v9_alison_pic3.webp",
    (0, 0), ConditionSwitch(

        "True", Null()
    ),
)
image v9_alison_pic3b_comp = Composite(
    (1920, 1080),
    (0, 0), "v9_alison_pic3b.webp",
    (0, 0), ConditionSwitch(

        "True", Null()
    ),
)
image v9_alison_pic4_comp = Composite(
    (1920, 1080),
    (0, 0), "v9_alison_pic4.webp",
    (0, 0), ConditionSwitch(

        "True", Null()
    ),
)
image v9_alison_pic5_comp = Composite(
    (1920, 1080),
    (0, 0), "v9_alison_pic5.webp",
    (0, 0), ConditionSwitch(

        "True", Null()
    ),
)
image v9_stalkfap2_comp = Composite(
    (1920, 1080),
    (0, 0), "v9_stalkfap2.webp",
    (0, 0), ConditionSwitch( 
        "lena_tattoo2 == True and not (v9_tat == 2 or v10_tat == 2)", "v9_stalkfap2_t2.webp",
        "True", Null()
    ),
)
image v9_stalkfap3_comp = Composite(
    (1920, 1080),
    (0, 0), "v9_stalkfap3.webp",
    (0, 0), ConditionSwitch( 
        "lena_tattoo2 == True and not (v9_tat == 2 or v10_tat == 2)", "v9_stalkfap2_t2.webp",
        "True", Null()
    ),
)




image v10_holly7_animation:
    "images/v10_holly7a.webp" with fps
    pause 0.4
    "images/v10_holly7b.webp" with fps
    pause 0.4
    repeat
image v10_holly7_animation2:
    "images/v10_holly7a.webp" with fps
    pause 0.7
    "images/v10_holly7b.webp" with fps
    pause 0.7
    repeat


image v10_emma4_animation:
    "images/v10_emma4a.webp" with fps
    pause 0.4
    "images/v10_emma4b.webp" with fps
    pause 0.4
    repeat


image v10_alison7_animation:
    "images/v10_alison7.webp" with fps
    pause 0.5
    "images/v10_alison7b.webp" with hpunch
    pause 0.5
    repeat
image v10_alison7_condom_animation:
    "images/v10_alison7_condom.webp" with fps
    pause 0.5
    "images/v10_alison7_condomb.webp" with hpunch
    pause 0.5
    repeat


image v10_wc_animation2:
    "v10_wc2" with fps
    pause 0.4
    "v10_wc3" with fps
    pause 0.4
    "v10_wc2" with fps
    pause 0.4
    "v10_wc3" with fps
    pause 0.4
    "v10_wc2" with fps
    pause 0.4
    "v10_wc3" with fps
    pause 0.4
    "v10_wc2" with fps
    pause 0.4
    "v10_wc3" with vpunch
    pause 1.5
    "v10_wc2" with fps
    pause 0.2
    "v10_wc1b" with fps
    pause 0.8
    repeat

image v10_wc_animation:
    "v10_wc2" with fps
    pause 0.3
    "v10_wc3" with vpunch
    pause 0.4
    "v10_wc2" with fps
    pause 0.3
    "v10_wc3" with vpunch
    pause 0.4
    "v10_wc2" with fps
    pause 0.3
    "v10_wc3" with vpunch
    pause 1
    "v10_wc2" with fps
    pause 0.2
    "v10_wc1b" with fps
    pause 1.5
    "v10_wc2" with fps
    pause 0.2
    "v10_wc3" with vpunch
    pause 0.4
    repeat
image v10_wc_animation_full:
    "v10_wc2" with fps
    pause 0.4
    "v10_wc3" with vpunch
    pause 1.5
    "v10_wc2" with fps
    pause 0.2
    "v10_wc1b" with fps
    pause 0.8

    "v10_wc2" with fps
    pause 0.2
    "v10_wc3" with fps
    pause 0.4
    "v10_wc2" with fps
    pause 0.3
    "v10_wc1b" with fps
    pause 0.5

    "v10_wc2" with fps
    pause 0.2
    "v10_wc3" with fps
    pause 0.3
    "v10_wc2" with fps
    pause 0.2
    "v10_wc1b" with fps
    pause 0.3

    "v10_wc2" with fps
    pause 0.2
    "v10_wc3" with fps
    pause 0.3
    "v10_wc2" with fps
    pause 0.2
    "v10_wc1b" with fps
    pause 0.3
    repeat


image v10_shoot9_ian1_animation:
    "images/v10_shoot9_ian1.webp" with fps
    pause 0.4
    "images/v10_shoot9_ian2.webp" with fps
    pause 0.4
    repeat

image v10_shoot9_stan1_animation:
    "images/v10_shoot9_stan1.webp" with fps
    pause 0.3
    "images/v10_shoot9_stan2.webp" with fps
    pause 0.3
    repeat


image v10_jeremy5_animation:
    "images/v10_jeremy5b.webp" with fps
    pause 0.7
    "v10_jeremy5c" with fps
    pause 0.5
    "images/v10_jeremy5b.webp" with fps
    pause 0.7
    "v10_jeremy5c" with fps
    pause 0.5
    "images/v10_jeremy5b.webp" with fps
    pause 0.7
    "v10_jeremy5c" with fps
    pause 1
    repeat
image v10_jeremy5_animation2:
    "images/v10_jeremy5b.webp" with vpunch
    pause 0.6
    "v10_jeremy5c" with fps
    pause 0.4
    "images/v10_jeremy5b.webp" with vpunch
    pause 0.6
    "v10_jeremy5c" with fps
    pause 0.4
    "images/v10_jeremy5b.webp" with vpunch
    pause 0.6
    "v10_jeremy5c" with fps
    pause 1
    repeat
image v10_jeremy9_animation:
    "v10_jeremy9b_comp" with vpunch
    pause 0.6
    "v10_jeremy9a_comp" with fps
    pause 0.4
    repeat
image v10_jeremy9b_comp = Composite(
    (1920, 1080),
    (0, 0), "v10_jeremy9b.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2 == True", "v10_jeremy9_t2.webp",
        "True", Null()
    ),
)
image v10_jeremy9a_comp = Composite(
    (1920, 1080),
    (0, 0), "v10_jeremy9a.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2 == True", "v10_jeremy9_t2.webp",
        "True", Null()
    ),
)
image v10_jeremy10_animation:
    "images/v10_jeremy10b.webp" with vpunch
    pause 0.6
    "images/v10_jeremy10a.webp" with fps
    pause 0.4
    repeat


image v10_minerva6_animation:
    "images/v10_minerva6a.webp" with fps
    pause 0.4
    "images/v10_minerva6b.webp" with vpunch
    pause 0.5
    "images/v10_minerva6a.webp" with fps
    pause 0.4
    "images/v10_minerva6b.webp" with vpunch
    pause 0.5
    "images/v10_minerva6a.webp" with fps
    pause 0.4
    "images/v10_minerva6b.webp" with vpunch
    pause 1.0
    "images/v10_minerva6a.webp" with fps
    pause 0.4
    "images/v10_minerva6b.webp" with fps
    pause 0.5
    "images/v10_minerva6a.webp" with fps
    pause 0.4
    "images/v10_minerva6b.webp" with fps
    pause 0.5
    "images/v10_minerva6a.webp" with fps
    pause 0.4
    "images/v10_minerva6b.webp" with fps
    pause 0.5
    "images/v10_minerva6a.webp" with fps
    pause 0.4
    "images/v10_minerva6b.webp" with vpunch
    pause 1.0
    "images/v10_minerva6a.webp" with fps
    pause 0.4
    "images/v10_minerva6b.webp" with fps
    pause 0.5
    "images/v10_minerva6a.webp" with fps
    pause 0.4
    "images/v10_minerva6b.webp" with fps
    pause 0.5
    "images/v10_minerva6a.webp" with fps
    pause 0.4
    "images/v10_minerva6b.webp" with fps
    pause 0.5
    repeat

image v10_pg_lena2b_comp = Composite(
    (1920, 1080),
    (0, 0), "v10_pg_lena2b.webp",
    (0, 0), ConditionSwitch( 
        "lena_tattoo2 == True and not v10_tat == 2", "v10_pg_lena2_t2.webp",
        "True", Null()
    ),
)

image v10_selfie_lena1_comp = Composite(
    (1920, 1080),
    (0, 0), "v10_selfie_lena1.webp",
    (0, 0), ConditionSwitch( 
        "lena_piercing1 == True and not v10_piercing", "v10_selfie_lena1_p1.webp",
        "lena_piercing2 == True and not v10_piercing", "v10_selfie_lena1_p2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_tattoo1 == True and not v10_tat == 1", "v10_selfie_lena1_t1.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_tattoo2 == True and not v10_tat == 2", "v10_selfie_lena1_t2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_tattoo3 == True and not v10_tat == 3", "v10_selfie_lena1_t3.webp",
        "True", Null()
    ),
)

image v10_stalkfap2c_comp = Composite(
    (1920, 1080),
    (0, 0), "v10_stalkfap2c.webp",
    (0, 0), ConditionSwitch( 
        "lena_piercing1 == True and not v10_piercing", "v10_stalkfap2c_p1.webp",
        "lena_piercing2 == True and not v10_piercing", "v10_stalkfap2c_p2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_tattoo1 == True and not v10_tat == 1", "v10_stalkfap2c_t1.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_tattoo2 == True and not v10_tat == 2", "v10_stalkfap2c_t2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_tattoo3 == True and not v10_tat == 3", "v10_stalkfap2c_t3.webp",
        "True", Null()
    ),
)

image v10_ian7_phone_comp = Composite(
    (1920, 1080),
    (0, 0), "v10_ian7_phone.webp",
    (0, 0), ConditionSwitch( 
        "lena_necklace == 'seymour'", "v10_ian7_phone_sy.webp",
        "lena_necklace == 'choker'", "v10_ian7_phone_choker.webp",
        "True", Null()
    )
)
image v10_phone_axel2_comp = Composite(
    (1920, 1080),
    (0, 0), "v10_phone_axel2a.webp",
    (0, 0), ConditionSwitch( 
        "v9_axel_pose == 2", "v10_phone_axel2b.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_tattoo2 == True and not v10_tat == 2", "v10_phone_axel2_t2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_tattoo3 == True and not v10_tat == 3", "v10_phone_axel2_t3.webp",
        "True", Null()
    ),
)

image v10_blazer_lena = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch(
        "lena_look == 'wits'", "v10_blazer_lena_wits.webp",
        "lena_look == 'charisma'", "v10_blazer_lena_charisma.webp",
        "lena_look == 'athletics'", "v10_blazer_lena_athletics.webp",
        "lena_look == 'lust'", "v10_blazer_lena_lust.webp",
        "lena_look == 'black_dress'", "v10_blazer_lena_dress.webp",
        "True", "v10_blazer_lena_base.webp"),
    (0, 0), ConditionSwitch( 
        "v8_choker == True", "v10_blazer_lena_choker.webp",
        "v8_sy == True", "v10_blazer_lena_sy.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "lena_piercing1 == True and not lena_look in ['wits', 'charisma']", "v10_blazer_lena_p1.webp",
        "lena_piercing2 == True and not lena_look in ['wits', 'charisma']", "v10_blazer_lena_p2.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "not lena_tattoo1 or lena_look in ['wits', 'charisma']", Null(),
        "lena_look == 'athletics'", "v10_blazer_lena_athletics_t1.webp",
        "lena_look == 'lust'", "v10_blazer_lena_lust_t1.webp",
        "lena_look == 'black_dress'", "v10_blazer_lena_dress_t1.webp",
        "True", "v10_blazer_lena_base_t1.webp"),
    (0, 0), ConditionSwitch( 
        "not lena_tattoo3", Null(),
        "lena_look == 'wits'", "v10_blazer_lena_wits_t3.webp",
        "lena_look == 'charisma'", "v10_blazer_lena_charisma_t3.webp",
        "lena_look == 'athletics'", "v10_blazer_lena_athletics_t3.webp",
        "lena_look == 'lust'", "v10_blazer_lena_lust_t3.webp",
        "lena_look == 'black_dress'", "v10_blazer_lena_dress_t3.webp",
        "True", "v10_blazer_lena_base_t3.webp")
)
image v10_blazer_lena2 = Composite(
    (1920, 1080),
    (0, 0), ConditionSwitch(
        "lena_look == 'wits'", "v10_blazer_lena2_wits.webp",
        "lena_look == 'charisma'", "v10_blazer_lena2_charisma.webp",
        "lena_look == 'athletics'", "v10_blazer_lena2_athletics.webp",
        "lena_look == 'lust'", "v10_blazer_lena2_lust.webp",
        "lena_look == 'black_dress'", "v10_blazer_lena2_dress.webp",
        "True", "v10_blazer_lena2_base.webp"),
    (0, 0), ConditionSwitch( 
        "v8_choker == True", "v10_blazer_lena2_choker.webp",
        "v8_sy == True", "v10_blazer_lena2_sy.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "lena_piercing1 == True and not lena_look in ['wits', 'charisma']", "v10_blazer_lena2_p1.webp",
        "lena_piercing2 == True and not lena_look in ['wits', 'charisma']", "v10_blazer_lena2_p2.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "not lena_tattoo1 or lena_look in ['wits', 'charisma']", Null(),
        "lena_look == 'athletics'", "v10_blazer_lena2_athletics_t1.webp",
        "lena_look == 'black_dress'", "v10_blazer_lena2_dress_t1.webp",
        "True", "v10_blazer_lena2_t1.webp"),
    (0, 0), ConditionSwitch( 
        "not lena_tattoo2 or lena_look in ['wits', 'black_dress']", Null(),
        "lena_look in ['charisma', 'athletics', 'lust']", "v10_blazer_lena2_t2.webp",
        "True", "v10_blazer_lena2_base_t2.webp"),
    (0, 0), ConditionSwitch( 
        "not lena_tattoo3 or lena_look == 'wits'", Null(),
        "lena_look == 'charisma'", "v10_blazer_lena2_charisma_t3.webp",
        "lena_look == 'athletics'", "v10_blazer_lena2_athletics_t3.webp",
        "lena_look == 'lust'", "v10_blazer_lena2_lust_t3.webp",
        "lena_look == 'black_dress'", "v10_blazer_lena2_dress_t3.webp",
        "True", "v10_blazer_lena2_base_t3.webp")
)
image v10_blazer_ian = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch(
        "ian_look == 'charisma1'", "v10_blazer_ian_charisma.webp",
        "ian_look == 'lust1'", "v10_blazer_ian_lust.webp",
        "True", "v10_blazer_ian_base.webp")
)
image v10_blazer_ian2 = Composite(
    (1920, 1080),
    (0, 0), ConditionSwitch(
        "ian_look == 'charisma1'", "v10_blazer_ian2_charisma.webp",
        "ian_look == 'lust1'", "v10_blazer_ian2_lust.webp",
        "True", "v10_blazer_ian2_base.webp")
)

image v10_wc1 = Composite(
    (1920, 1080),
    (0, 0), ConditionSwitch(
        "lena_look == 'wits'", "v10_wc1_wits.webp",
        "lena_look == 'charisma'", "v10_wc1_charisma.webp",
        "lena_look == 'athletics'", "v10_wc1_athletics.webp",
        "lena_look == 'lust'", "v10_wc1_lust.webp",
        "lena_look == 'black_dress'", "v10_wc1_dress.webp",
        "True", "v10_wc1_base.webp"),
    (0, 0), ConditionSwitch(
        "not lena_tattoo2 or lena_look in ['wits', 'black_dress']", Null(),
        "lena_look in ['athletics', 'charisma', 'lust']", "v10_wc1_tfull.webp",
        "True", "v10_wc1_thalf.webp"),
    (0, 0), ConditionSwitch(
        "v10_wc_bj == 'mike'", 'v10_wc1_mike.webp',
        "v10_wc_bj == 'ian' and ian_look == 'charisma1'", "v10_wc_ian2.webp",
        "v10_wc_bj == 'ian'", "v10_wc_ian.webp",
        "True", Null())
)
image v10_wc1b = Composite(
    (1920, 1080),
    (0, 0), ConditionSwitch(
        "lena_look == 'wits'", "v10_wc1_wits.webp",
        "lena_look == 'charisma'", "v10_wc1_charisma.webp",
        "lena_look == 'athletics'", "v10_wc1_athletics.webp",
        "lena_look == 'lust'", "v10_wc1_lust.webp",
        "lena_look == 'black_dress'", "v10_wc1_dress.webp",
        "True", "v10_wc1_base.webp"),
    (0, 0), ConditionSwitch(
        "not lena_tattoo2 or lena_look in ['wits', 'black_dress']", Null(),
        "lena_look in ['athletics', 'charisma', 'lust']", "v10_wc1_tfull.webp",
        "True", "v10_wc1_thalf.webp"),
    (0, 0), ConditionSwitch(
        "v10_wc_bj == 'mike'", 'v10_wc1_mike.webp',
        "v10_wc_bj == 'ian' and ian_look == 'charisma1'", "v10_wc_ian2.webp",
        "v10_wc_bj == 'ian'", "v10_wc_ian.webp",
        "True", Null()),
    (0, 0), "v10_wc1_saliva.webp"
)
image v10_wc2 = Composite(
    (1920, 1080),
    (0, 0), ConditionSwitch(
        "lena_look == 'wits'", "v10_wc2_wits.webp",
        "lena_look == 'charisma'", "v10_wc2_charisma.webp",
        "lena_look == 'athletics'", "v10_wc2_athletics.webp",
        "lena_look == 'lust'", "v10_wc2_lust.webp",
        "lena_look == 'black_dress'", "v10_wc2_dress.webp",
        "True", "v10_wc2_base.webp"),
    (0, 0), ConditionSwitch(
        "not lena_tattoo2 or lena_look in ['wits', 'black_dress']", Null(),
        "lena_look in ['athletics', 'charisma', 'lust']", "v10_wc2_tfull.webp",
        "True", "v10_wc2_thalf.webp"),
    (0, 0), ConditionSwitch(
        "v10_wc_bj == 'mike'", 'v10_wc2_mike.webp',
        "v10_wc_bj == 'ian' and ian_look == 'charisma1'", "v10_wc_ian2.webp",
        "v10_wc_bj == 'ian'", "v10_wc_ian.webp",
        "True", Null())
)
image v10_wc3 = Composite(
    (1920, 1080),
    (0, 0), ConditionSwitch(
        "lena_look == 'wits'", "v10_wc3_wits.webp",
        "lena_look == 'charisma'", "v10_wc3_charisma.webp",
        "lena_look == 'athletics'", "v10_wc3_athletics.webp",
        "lena_look == 'lust'", "v10_wc3_lust.webp",
        "lena_look == 'black_dress'", "v10_wc3_dress.webp",
        "True", "v10_wc3_base.webp"),
    (0, 0), ConditionSwitch(
        "not lena_tattoo2 or lena_look in ['wits', 'black_dress']", Null(),
        "lena_look in ['athletics', 'charisma', 'lust']", "v10_wc3_tfull.webp",
        "True", "v10_wc3_thalf.webp"),
    (0, 0), ConditionSwitch(
        "v10_wc_bj == 'mike'", 'v10_wc3_mike.webp',
        "v10_wc_bj == 'ian' and ian_look == 'charisma1'", "v10_wc_ian2.webp",
        "v10_wc_bj == 'ian'", "v10_wc_ian.webp",
        "True", Null())
)
image v10_wc4 = Composite(
    (1920, 1080),
    (0, 0), ConditionSwitch(
        "lena_look == 'wits'", "v10_wc4_wits.webp",
        "lena_look == 'charisma'", "v10_wc4_charisma.webp",
        "lena_look == 'athletics'", "v10_wc4_athletics.webp",
        "lena_look == 'lust'", "v10_wc4_lust.webp",
        "lena_look == 'black_dress'", "v10_wc4_dress.webp",
        "True", "v10_wc4_base.webp"),
    (0, 0), ConditionSwitch(
        "not lena_tattoo2 or lena_look in ['wits', 'black_dress']", Null(),
        "lena_look in ['athletics', 'charisma', 'lust']", "v10_wc4_tfull.webp",
        "True", "v10_wc4_thalf.webp")
)

image v10_wc5 = Composite(
    (1920, 1080),
    (0, 0), ConditionSwitch(
        "v10_wc_bj == 'mike'", 'v10_wc5_mike.webp',
        "v10_wc_bj == 'mark'", 'v10_wc5_mark.webp',
        "v10_wc_bj == 'ian' and ian_look == 'charisma1'", "v10_wc5_ian_charisma.webp",
        "v10_wc_bj == 'ian' and ian_look == 'lust1'", "v10_wc5_ian_lust.webp",
        "True", "v10_wc5_ian_base.webp"),
    (0, 0), ConditionSwitch(
        "lena_look == 'wits'", "v10_wc5_wits.webp",
        "lena_look == 'charisma'", "v10_wc5_charisma.webp",
        "lena_look == 'athletics'", "v10_wc5_athletics.webp",
        "lena_look == 'lust'", "v10_wc5_lust.webp",
        "lena_look == 'black_dress'", "v10_wc5_dress.webp",
        "True", "v10_wc5_base.webp")
)


image v10_jeremy5c = Composite(
    (1920, 1080),
    (0, 0), "v10_jeremy5.webp",
    (0, 0), "v10_jeremy5_saliva.webp"
)




image v11_louise5_animation1:
    "images/v11_louise5a.webp" with fps
    pause 0.7
    "images/v11_louise5b.webp" with fps
    pause 0.5
    repeat
image v11_louise5_animation2:
    "images/v11_louise5a.webp" with fps
    pause 0.3
    "images/v11_louise5b.webp" with vpunch
    pause 0.4
    repeat


image v11_ian2_animation:
    "images/v11_ian2a.webp" with fps
    pause 0.3
    "images/v11_ian2b.webp" with vpunch
    pause 0.4
    repeat
image v11_ian2_t2_animation:
    "images/v11_ian2_t2.webp" with fps
    pause 0.3
    "images/v11_ian2_t2.webp" with vpunch
    pause 0.4
    repeat
image v11_ian2_t3_animation:
    "images/v11_ian2_t3.webp" with fps
    pause 0.3
    "images/v11_ian2_t3.webp" with vpunch
    pause 0.4
    repeat


image v11_cindy3_animation1:
    "images/v11_cindy3a.webp" with fps3
    pause 0.2
    "images/v11_cindy3b.webp" with fps3
    pause 0.2
    "images/v11_cindy3c.webp" with fps3
    pause 0.2
    repeat
image v11_cindy3_animation2:
    "images/v11_cindy3a.webp" with fps2
    pause 0.2
    "images/v11_cindy3b.webp" with vpunch
    pause 0.3
    "images/v11_cindy3c.webp" with fps2
    pause 0.2
    repeat
image v11_cindy3_animation3:
    "images/v11_cindy3a.webp" with fps3
    pause 0.15
    "images/v11_cindy3b.webp" with vpunch
    pause 0.2
    "images/v11_cindy3c.webp" with fps3
    pause 0.1
    repeat
image v11_cindy5_animation:
    "images/v11_cindy5a.webp" with fps
    pause 0.4
    "images/v11_cindy5b.webp" with fps
    pause 0.4
    repeat


transform v11hollykiss:
    xpos 400
image v11_holly4_animation:
    "images/v11_holly4a.webp" with fps
    pause 0.3
    "images/v11_holly4b.webp" with fps
    pause 0.3
    "images/v11_holly4c.webp" with fps
    pause 0.3
    "images/v11_holly4b.webp" with fps
    pause 0.3
    repeat
image v11_holly9_animation1:
    "images/v11_holly9b.webp" with fps
    pause 0.3
    "images/v11_holly9c.webp" with fps
    pause 0.4
    "images/v11_holly9b.webp" with fps
    pause 0.3
    "images/v11_holly9a.webp" with fps
    pause 0.5
    repeat
image v11_holly9_animation2:
    "images/v11_holly9b.webp" with fps
    pause 0.2
    "images/v11_holly9c.webp" with fps
    pause 0.3
    "images/v11_holly9b.webp" with fps
    pause 0.2
    "images/v11_holly9a.webp" with vpunch
    pause 0.4
    repeat


image v11_cherry6_animation1:
    "images/v11_cherry6a.webp" with fps
    pause 0.3
    "images/v11_cherry6b.webp" with fps
    pause 0.2
    "images/v11_cherry6c.webp" with fps
    pause 0.4
    "images/v11_cherry6b.webp" with fps
    pause 0.2
    repeat
image v11_cherry6_animation2:
    "images/v11_cherry6a.webp" with vpunch
    pause 0.2
    "images/v11_cherry6b.webp" with fps
    pause 0.1
    "images/v11_cherry6c.webp" with fps
    pause 0.3
    "images/v11_cherry6b.webp" with fps
    pause 0.1
    repeat
image v11_cherry7_animation1:
    "images/v11_cherry7a.webp" with fps
    pause 0.4
    "images/v11_cherry7b.webp" with fps
    pause 0.4
    repeat
image v11_cherry7_animation2:
    "images/v11_cherry7a.webp" with fps
    pause 0.3
    "images/v11_cherry7b.webp" with vpunch
    pause 0.3
    repeat
image v11_cherry10_animation:
    "images/v11_cherry10b.webp" with fps
    pause 0.5
    "images/v11_cherry10a.webp" with fps
    pause 0.4
    "images/v11_cherry10b.webp" with fps
    pause 0.5
    "images/v11_cherry10a.webp" with fps
    pause 0.4
    "images/v11_cherry10b.webp" with fps
    pause 0.5
    "images/v11_cherry10a.webp" with fps
    pause 0.4
    "images/v11_cherry10b.webp" with vpunch
    pause 1
    "images/v11_cherry10a.webp" with fps
    pause 1
    "images/v11_cherry10b.webp" with fps
    pause 0.3
    "images/v11_cherry10a.webp" with fps
    pause 0.3
    "images/v11_cherry10b.webp" with fps
    pause 0.3
    "images/v11_cherry10a.webp" with fps
    pause 0.3
    "images/v11_cherry10b.webp" with vpunch
    pause 0.8
    "images/v11_cherry10a.webp" with fps
    pause 1
    repeat


image v11_alison1a = Composite(
    (1920, 1080),
    (0, 0), "v11_alison1a.webp",
    (0, 0), ConditionSwitch(
        "alison_blonde", 'v11_alison1a_blonde.webp',
        "True", Null()),
)
image v11_alison1b = Composite(
    (1920, 1080),
    (0, 0), "v11_alison1b.webp",
    (0, 0), ConditionSwitch(
        "alison_blonde", 'v11_alison1b_blonde.webp',
        "True", Null()),
)
image v11_alison1_animation:
    "v11_alison1b" with fps
    pause 0.3
    "v11_alison1a" with fps
    pause 0.4
    "v11_alison1b" with fps
    pause 0.3
    "v11_alison1a" with fps
    pause 0.4
    "v11_alison1b" with fps
    pause 0.3
    "v11_alison1a" with fps
    pause 0.4
    "v11_alison1b" with fps
    pause 0.3
    "v11_alison1a" with vpunch
    pause 0.4
    "v11_alison1b" with fps
    pause 0.3
    "v11_alison1a" with vpunch
    pause 0.3
    "v11_alison1b" with fps
    pause 0.3
    "v11_alison1a" with vpunch
    pause 0.3
    "v11_alison1b" with fps
    pause 0.3
    "v11_alison1a" with vpunch
    pause 1
    repeat
image v11_alison1_animation_condom:
    "images/v11_alison1b_condom.webp" with fps
    pause 0.3
    "images/v11_alison1a_condom.webp" with fps
    pause 0.4
    "images/v11_alison1b_condom.webp" with fps
    pause 0.3
    "images/v11_alison1a_condom.webp" with fps
    pause 0.4
    "images/v11_alison1b_condom.webp" with fps
    pause 0.3
    "images/v11_alison1a_condom.webp" with fps
    pause 0.4
    "images/v11_alison1b_condom.webp" with fps
    pause 0.3
    "images/v11_alison1a_condom.webp" with vpunch
    pause 0.4
    "images/v11_alison1b_condom.webp" with fps
    pause 0.3
    "images/v11_alison1a_condom.webp" with vpunch
    pause 0.3
    "images/v11_alison1b_condom.webp" with fps
    pause 0.3
    "images/v11_alison1a_condom.webp" with vpunch
    pause 0.3
    "images/v11_alison1b_condom.webp" with fps
    pause 0.3
    "images/v11_alison1a_condom.webp" with vpunch
    pause 1
    repeat
image v11_alison3b = Composite(
    (1920, 1080),
    (0, 0), "v11_alison3b.webp",
    (0, 0), ConditionSwitch(
        "alison_blonde", 'v11_alison3b_blonde.webp',
        "True", Null()),
)
image v11_alison3c = Composite(
    (1920, 1080),
    (0, 0), "v11_alison3c.webp",
    (0, 0), ConditionSwitch(
        "alison_blonde", 'v11_alison3c_blonde.webp',
        "True", Null()),
)
image v11_alison3_animation:
    "images/v11_alison3a.webp" with fps
    pause 0.4
    "v11_alison3b" with fps
    pause 0.3
    "v11_alison3c" with fps
    pause 0.5
    "v11_alison3b" with fps
    pause 0.3
    repeat


image v11_lena5_animation:
    "images/v11_lena5b.webp" with fps
    pause 0.4
    "images/v11_lena5a.webp" with fps
    pause 0.4
    repeat
image v11_lena6a = Composite(
    (1920, 1080),
    (0, 0), "v11_lena6a.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v10_wc1_tfull.webp',
        "True", Null()),
)
image v11_lena6aa = Composite(
    (1920, 1080),
    (0, 0), "v11_lena6aa.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v10_wc1_tfull.webp',
        "True", Null()),
)
image v11_lena6b = Composite(
    (1920, 1080),
    (0, 0), "v11_lena6b.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v10_wc2_tfull.webp',
        "True", Null()),
)
image v11_lena6c = Composite(
    (1920, 1080),
    (0, 0), "v11_lena6c.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v10_wc3_tfull.webp',
        "True", Null()),
)
image v11_lena6d = Composite(
    (1920, 1080),
    (0, 0), "v11_lena6d.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v13_ian_bj4_t2.webp',
        "True", Null()),
)
image v11_lena6e = Composite(
    (1920, 1080),
    (0, 0), "v11_lena6e.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v10_wc2_tfull.webp',
        "True", Null()),
)
image v11_lena6e_up = Composite(
    (1920, 1080),
    (0, 0), "v11_lena6e_up.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v10_wc2_tfull.webp',
        "True", Null()),
)
image v11_lena6f = Composite(
    (1920, 1080),
    (0, 0), "v11_lena6f.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v10_wc2_tfull.webp',
        "True", Null()),
)
image v11_lena6g = Composite(
    (1920, 1080),
    (0, 0), "v11_lena6g.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v10_wc1_tfull.webp',
        "True", Null()),
)
image v11_lena6e1 = Composite(
    (1920, 1080),
    (0, 0), "v11_lena6e1.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v13_ian_bj5_t2.webp',
        "True", Null()),
)
image v11_lena6e2 = Composite(
    (1920, 1080),
    (0, 0), "v11_lena6e2.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v13_ian_bj5_t2.webp',
        "True", Null()),
)
image v11_lena6e3 = Composite(
    (1920, 1080),
    (0, 0), "v11_lena6e3.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v13_ian_bj5_t2.webp',
        "True", Null()),
)
image v11_lena6b2 = Composite(
    (1920, 1080),
    (0, 0), "v11_lena6b2.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v10_wc2_tfull.webp',
        "True", Null()),
)
image v11_lena6_animation1:
    "v11_lena6b" with fps
    pause 0.4
    "v11_lena6c" with fps
    pause 0.2
    "v11_lena6d" with vpunch
    pause 1
    "v11_lena6c" with fps
    pause 0.2
    "v11_lena6e3" with fps
    pause 0.2
    "v11_lena6e" with fps
    pause 0.25
    "v11_lena6f" with fps
    pause 0.3
    "v11_lena6aa" with fps
    pause 0.3

    "v11_lena6f" with fps
    pause 0.3
    "v11_lena6b" with fps
    pause 0.3


    "v11_lena6f" with fps
    pause 0.3

    "v11_lena6b" with fps
    pause 0.2
    "v11_lena6e_up" with fps
    pause 0.2
    "v11_lena6f" with fps
    pause 0.3

    "v11_lena6b" with fps
    pause 0.2
    "v11_lena6e_up" with fps
    pause 0.2
    "v11_lena6f" with fps
    pause 0.3

    "v11_lena6b" with fps
    pause 0.2
    "v11_lena6e_up" with fps
    pause 0.2
    "v11_lena6f" with fps
    pause 0.3
    "v11_lena6a" with fps
    pause 0.4
    "v11_lena6f" with fps
    pause 0.3
    repeat

image v11_lena6_animation2:
    "v11_lena6b" with fps
    pause 0.3
    "v11_lena6d" with fps
    pause 0.35
    "v11_lena6e" with fps
    pause 0.3
    "v11_lena6f" with fps
    pause 0.2

    "v11_lena6b" with fps
    pause 0.3
    "v11_lena6d" with fps
    pause 0.3
    "v11_lena6e" with fps
    pause 0.3
    "v11_lena6f" with fps
    pause 0.2

    "v11_lena6b" with fps
    pause 0.3
    "v11_lena6d" with fps
    pause 0.3
    "v11_lena6e" with fps
    pause 0.3
    "v11_lena6f" with fps
    pause 0.2
    "v11_lena6aa" with fps
    pause 0.25
    "v11_lena6f" with fps
    pause 0.2

    "v11_lena6b" with fps
    pause 0.2
    "v11_lena6c" with fps
    pause 0.2
    "v11_lena6d" with vpunch
    pause 0.6
    "v11_lena6d" with vpunch
    pause 1.2

    "v11_lena6e2" with fps
    pause 0.2
    "v11_lena6e3" with fps3
    pause 0.15

    "v11_lena6e" with fps
    pause 0.15
    "v11_lena6f" with fps
    pause 0.3
    "v11_lena6aa" with fps
    pause 0.25
    "v11_lena6g" with fps
    pause 1.5
    "v11_lena6a" with fps
    pause 0.5
    "v11_lena6f" with fps
    pause 0.2
    repeat
image v11_lena6_animation3:
    "v11_lena6b" with fps
    pause 0.25
    "v11_lena6d" with vpunch
    pause 0.3
    "v11_lena6e1" with fps
    pause 0.15
    "v11_lena6e" with fps
    pause 0.2
    "v11_lena6f" with fps
    pause 0.2
    "v11_lena6aa" with fps
    pause 0.25
    "v11_lena6f" with fps
    pause 0.2
    repeat

image v11_lena6_animation4:
    "v11_lena6aa" with fps
    pause 0.25
    "v11_lena6f" with fps
    pause 0.2
    "v11_lena6b" with flash
    pause 0.2
    "v11_lena6d" with vpunch
    pause 0.4
    "v11_lena6e" with vpunch
    pause 0.3
    "v11_lena6f" with vpunch
    pause 0.2

    "v11_lena6b" with fps
    pause 0.3
    "v11_lena6d" with vpunch
    pause 0.4
    "v11_lena6e" with vpunch
    pause 0.3
    "v11_lena6f" with vpunch
    pause 0.2

    "v11_lena6b" with fps
    pause 0.4
    "v11_lena6d" with vpunch
    pause 0.2
    "v11_lena6d" with flash
    pause 0.5
    "v11_lena6d" with vpunch
    pause 1

    "v11_lena6c" with fps3
    pause 0.15
    "v11_lena6e1" with fps3
    pause 0.15
    "v11_lena6e2" with fps3
    pause 0.15
    "v11_lena6e3" with fps3
    pause 0.12
    "v11_lena6e" with fps3
    pause 0.12
    "v11_lena6f" with fps3
    pause 0.12
    "v11_lena6aa" with fps3
    pause 0.12
    "v11_lena6g" with fps3
    pause 1.5

image v11_lena6_animation_test:
    "v11_lena6b2" with fps3
    pause 0.15
    "v11_lena6d" with vpunch
    pause 0.2
    "v11_lena6c" with fps3
    pause 0.1
    "v11_lena6e" with fps3
    pause 0.15
    "v11_lena6f" with fps3
    pause 0.1
    "v11_lena6aa" with fps3
    pause 0.15
    "v11_lena6f" with fps3
    pause 0.1

    "v11_lena6b2" with fps3
    pause 0.15
    "v11_lena6d" with vpunch
    pause 0.2
    "v11_lena6c" with fps3
    pause 0.1
    "v11_lena6e" with fps3
    pause 0.15
    "v11_lena6f" with fps3
    pause 0.1
    "v11_lena6aa" with fps3
    pause 0.15
    "v11_lena6f" with fps3
    pause 0.1

    "v11_lena6b2" with fps3
    pause 0.15
    "v11_lena6d" with vpunch
    pause 0.2
    "v11_lena6c" with fps3
    pause 0.1
    "v11_lena6e" with fps3
    pause 0.15
    "v11_lena6f" with fps3
    pause 0.1
    "v11_lena6aa" with fps3
    pause 0.15
    "v11_lena6f" with fps3
    pause 0.1

    "v11_lena6b2" with fps3
    pause 0.15
    "v11_lena6d" with vpunch
    pause 0.4
    "v11_lena6d" with vpunch
    pause 0.7
    "v11_lena6c" with fps3
    pause 0.15
    "v11_lena6e1" with fps3
    pause 0.15
    "v11_lena6e2" with fps3
    pause 0.15
    "v11_lena6e3" with fps3
    pause 0.12
    "v11_lena6e" with fps3
    pause 0.12
    "v11_lena6f" with fps3
    pause 0.12
    "v11_lena6aa" with fps3
    pause 0.12
    "v11_lena6g" with fps3
    pause 1
    "v11_lena6a" with short
    pause 0.4
    "v11_lena6f" with fps3
    pause 0.3
    repeat


image v11_solo3_animation:
    "images/v11_solo3a.webp" with fps
    pause 0.4
    "images/v11_solo3b.webp" with fps
    pause 0.4
    repeat
image v11_solo3_animation_t:
    "images/v11_solo3a_t2.webp" with fps
    pause 0.4
    "images/v11_solo3b_t2.webp" with fps
    pause 0.4
    repeat
image v11_solo4_animation:
    "images/v11_solo4a.webp" with fps
    pause 0.4
    "images/v11_solo4b.webp" with fps
    pause 0.4
    repeat


transform v11hollylenakiss:
    xpos 600


image v11_bbc2a = Composite(
    (1920, 1080),
    (0, 0), "v11_bbc2a.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v11_bbc2a_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v11_lena_dress == 2", 'v11_bbc2a_charisma.webp',
        "v11_lena_dress == 4", 'v11_bbc2a_lust.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v11_bbc2a_t2.webp',
        "True", Null()),
)
image v11_bbc2b = Composite(
    (1920, 1080),
    (0, 0), "v11_bbc2b.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v11_bbc2b_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v11_lena_dress == 2", 'v11_bbc2b_charisma.webp',
        "v11_lena_dress == 4", 'v11_bbc2b_lust.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v11_bbc2b_t2.webp',
        "True", Null()),
)
image v11_bbc2_animation:
    "v11_bbc2b" with fps
    pause 0.6
    "v11_bbc2a" with fps
    pause 0.5
    repeat
image v11_bbc2a_marcel = Composite(
    (1920, 1080),
    (0, 0), "v11_bbc2a_marcel.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v11_bbc2a_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v11_lena_dress == 2", 'v11_bbc2a_charisma.webp',
        "v11_lena_dress == 4", 'v11_bbc2a_lust.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v11_bbc2a_t2.webp',
        "True", Null()),
)
image v11_bbc2b_marcel = Composite(
    (1920, 1080),
    (0, 0), "v11_bbc2b_marcel.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v11_bbc2b_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v11_lena_dress == 2", 'v11_bbc2b_charisma.webp',
        "v11_lena_dress == 4", 'v11_bbc2b_lust.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v11_bbc2b_t2.webp',
        "True", Null()),
)
image v11_bbc2_marcel_animation:
    "v11_bbc2b_marcel" with fps
    pause 0.5
    "v11_bbc2a_marcel" with fps
    pause 0.5
    repeat


image v11_axel5a = Composite(
    (1920, 1080),
    (0, 0), "v11_axel5a.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v11_axel5a_earrings.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v11_axel5a_t2.webp',
        "True", Null())
)
image v11_axel5b = Composite(
    (1920, 1080),
    (0, 0), "v11_axel5b.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v11_axel5b_earrings.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v11_axel5b_t2.webp',
        "True", Null())
)
image v11_axel5c = Composite(
    (1920, 1080),
    (0, 0), "v11_axel5c.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v11_axel5c_earrings.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v11_axel5c_t2.webp',
        "True", Null())
)
image v11_axel5_animation1:
    "v11_axel5b" with fps
    pause 0.2
    "v11_axel5c" with fps
    pause 0.4
    "v11_axel5b" with fps
    pause 0.3
    "v11_axel5a" with fps
    pause 0.3
    repeat
image v11_axel5_animation2:
    "v11_axel5b" with fps
    pause 0.3
    "v11_axel5c" with vpunch
    pause 0.4
    "v11_axel5b" with fps
    pause 0.3
    "v11_axel5c" with vpunch
    pause 0.4
    "v11_axel5b" with fps
    pause 0.3
    "v11_axel5c" with vpunch
    pause 1
    "v11_axel5b" with fps
    pause 0.3
    "v11_axel5a" with fps
    pause 0.3
    "v11_axel5b" with fps
    pause 0.2
    "v11_axel5c" with fps
    pause 0.4
    "v11_axel5b" with fps
    pause 0.3
    "v11_axel5a" with fps
    pause 0.2
    "v11_axel5b" with fps
    pause 0.2
    "v11_axel5c" with fps
    pause 0.4
    "v11_axel5b" with fps
    pause 0.3
    "v11_axel5a" with fps
    pause 0.2
    "v11_axel5b" with fps
    pause 0.2
    "v11_axel5c" with vpunch
    pause 0.8
    "v11_axel5b" with fps
    pause 0.3
    "v11_axel5a" with fps
    pause 0.2
    repeat
image v11_axel6 = Composite(
    (1920, 1080),
    (0, 0), ConditionSwitch(
        "v11_lena_dress == 1", 'v11_axel6a.webp',
        "v11_lena_dress == 2", 'v11_axel6b.webp',
        "v11_lena_dress == 3", 'v11_axel6c.webp',
        "v11_lena_dress == 4", 'v11_axel6d.webp'),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v11_axel6a_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v11_axel6_earrings.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_extras == 'stockings'", 'v11_axel6_stockings.webp',
        "True", Null())
)
image v11_axel7 = Composite(
    (1920, 1080),
    (0, 0), ConditionSwitch(
        "v11_lena_dress == 1", 'v11_axel7a.webp',
        "v11_lena_dress == 2", 'v11_axel7b.webp',
        "v11_lena_dress == 3", 'v11_axel7c.webp',
        "v11_lena_dress == 4", 'v11_axel7d.webp'),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v11_axel7a_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v11_axel7_earrings.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_extras == 'stockings'", 'v11_axel7_stockings.webp',
        "True", Null())
)
image v11_axel6_animation:
    "v11_axel6" with fps
    pause 0.5
    "v11_axel7" with fps
    pause 0.5
    "v11_axel6" with fps
    pause 0.5
    "v11_axel7" with fps
    pause 0.5
    "v11_axel6" with fps
    pause 0.4
    "v11_axel7" with vpunch
    pause 0.5
    "v11_axel6" with fps
    pause 0.4
    "v11_axel7" with vpunch
    pause 0.5
    "v11_axel6" with fps
    pause 0.4
    "v11_axel7" with vpunch
    pause 0.5
    repeat

image v11_lenaian6_animation:
    "images/v11_lenaian6b.webp" with fps
    pause 0.2

    "images/v11_lenaian6a.webp" with fps
    pause 0.3
    "images/v11_lenaian6b.webp" with fps
    pause 0.2
    "images/v11_lenaian6c.webp" with vpunch
    pause 0.4
    repeat
image v11_mark6_animation:
    "images/v11_mark6b.webp" with fps
    pause 0.2

    "images/v11_mark6a.webp" with fps
    pause 0.3
    "images/v11_mark6b.webp" with fps
    pause 0.2
    "images/v11_mark6c.webp" with vpunch
    pause 0.4
    repeat

image v11_mark7_animation:
    "images/v11_mark7a.webp" with fps
    pause 0.3
    "images/v11_mark7b.webp" with fps
    pause 0.2
    "images/v11_mark7c.webp" with fps
    pause 0.2
    "images/v11_mark7d.webp" with fps
    pause 0.2


transform v11lenabikinishopping:
    xpos 200
transform v11emmabikinishopping:
    xpos -200


image v11_jack3a = Composite(
    (1920, 1080),
    (0, 0), "v11_jack3a.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v11_axel5a_earrings.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v11_axel5a_t2.webp',
        "True", Null())
)
image v11_jack3b = Composite(
    (1920, 1080),
    (0, 0), "v11_jack3b.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v11_axel5b_earrings.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v11_axel5b_t2.webp',
        "True", Null())
)
image v11_jack3c = Composite(
    (1920, 1080),
    (0, 0), "v11_jack3c.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v11_axel5c_earrings.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v11_axel5c_t2.webp',
        "True", Null())
)
image v11_jack3_animation1:
    "v11_jack3b" with fps
    pause 0.2
    "v11_jack3c" with fps
    pause 0.4
    "v11_jack3b" with fps
    pause 0.3
    "v11_jack3a" with fps
    pause 0.3
    repeat
image v11_jack3_animation2:
    "v11_jack3b" with fps
    pause 0.3
    "v11_jack3c" with vpunch
    pause 0.4
    "v11_jack3b" with fps
    pause 0.3
    "v11_jack3c" with vpunch
    pause 0.4
    "v11_jack3b" with fps
    pause 0.3
    "v11_jack3c" with vpunch
    pause 1
    "v11_jack3b" with fps
    pause 0.3
    "v11_jack3a" with fps
    pause 0.3
    "v11_jack3b" with fps
    pause 0.2
    "v11_jack3c" with fps
    pause 0.4
    "v11_jack3b" with fps
    pause 0.3
    "v11_jack3a" with fps
    pause 0.2
    "v11_jack3b" with fps
    pause 0.2
    "v11_jack3c" with fps
    pause 0.4
    "v11_jack3b" with fps
    pause 0.3
    "v11_jack3a" with fps
    pause 0.2
    "v11_jack3b" with fps
    pause 0.2
    "v11_jack3c" with vpunch
    pause 0.8
    "v11_jack3b" with fps
    pause 0.3
    "v11_jack3a" with fps
    pause 0.2
    repeat
image v11_jack6_squirt_animation:
    "images/v11_jack6_squirt1.webp" with flash
    pause 0.4
    "images/v11_jack6_squirt2.webp" with fps
    pause 0.2
    "images/v11_jack6_squirt3.webp" with fps
    pause 0.2
    "images/v11_jack6_squirt4.webp" with fps
    pause 0.3
    "images/v11_jack6_squirt1.webp" with flash
    pause 0.3
    "images/v11_jack6_squirt2.webp" with fps
    pause 0.2
    "images/v11_jack6_squirt3.webp" with fps
    pause 0.2
    "images/v11_jack6_squirt4.webp" with fps
    pause 0.2
    "images/v11_jack6_squirt1.webp" with flash
    pause 0.3
    "images/v11_jack6_squirt2.webp" with fps
    pause 0.2
    "images/v11_jack6_squirt3.webp" with fps
    pause 0.2
    "images/v11_jack6_squirt4.webp" with fps
    pause 0.3
image v11_seymour7_squirt0:
    "images/v11_seymour7_squirt1a.webp" with fps
    pause 0.5
    "images/v11_seymour7_squirt1b.webp" with fps
    pause 0.2
    "images/v11_seymour7_squirt1c.webp" with fps
    pause 0.2
image v11_seymour7_squirt1:
    "images/v11_seymour7_squirt1a.webp" with fps
    pause 0.3
    "images/v11_seymour7_squirt1b.webp" with fps
    pause 0.2
    "images/v11_seymour7_squirt1c.webp" with vpunch
    pause 0.2

image v11_seymour7_squirt2:
    "images/v11_seymour7_squirt2b.webp" with fps
    pause 0.3
    "images/v11_seymour7_squirt2c.webp" with fps
    pause 0.2
    "images/v11_seymour7_squirt2d.webp" with vpunch
    pause 0.2
image v11_seymour7_squirt3:
    "images/v11_seymour7_squirt3a.webp" with fps
    pause 0.3
    "images/v11_seymour7_squirt3b.webp" with fps
    pause 0.2
    "images/v11_seymour7_squirt3c.webp" with fps
    pause 0.2


image v11_bbc4_jeremy_base_animation:
    "images/v11_bbc4a_jeremy_base.webp" with fps
    pause 0.3
    "images/v11_bbc4b_jeremy_base.webp" with fps
    pause 0.2
    "images/v11_bbc4c_jeremy_base.webp" with fps
    pause 0.3
    "images/v11_bbc4b_jeremy_base.webp" with fps
    pause 0.2
    repeat
image v11_bbc4_jeremy_lust_animation:
    "images/v11_bbc4a_jeremy_lust.webp" with fps
    pause 0.3
    "images/v11_bbc4b_jeremy_lust.webp" with fps
    pause 0.2
    "images/v11_bbc4c_jeremy_lust.webp" with fps
    pause 0.3
    "images/v11_bbc4b_jeremy_lust.webp" with fps
    pause 0.2
    repeat
image v11_bbc4_jeremy_charisma_animation:
    "images/v11_bbc4a_jeremy_charisma.webp" with fps
    pause 0.3
    "images/v11_bbc4b_jeremy_charisma.webp" with fps
    pause 0.2
    "images/v11_bbc4c_jeremy_charisma.webp" with fps
    pause 0.3
    "images/v11_bbc4b_jeremy_charisma.webp" with fps
    pause 0.2
    repeat

image v11_bbc4_marcel_base_animation:
    "images/v11_bbc4a_marcel_base.webp" with fps
    pause 0.3
    "images/v11_bbc4b_marcel_base.webp" with fps
    pause 0.2
    "images/v11_bbc4c_marcel_base.webp" with fps
    pause 0.3
    "images/v11_bbc4b_marcel_base.webp" with fps
    pause 0.2
    repeat
image v11_bbc4_marcel_lust_animation:
    "images/v11_bbc4a_marcel_lust.webp" with fps
    pause 0.3
    "images/v11_bbc4b_marcel_lust.webp" with fps
    pause 0.2
    "images/v11_bbc4c_marcel_lust.webp" with fps
    pause 0.3
    "images/v11_bbc4b_marcel_lust.webp" with fps
    pause 0.2
    repeat
image v11_bbc4_marcel_charisma_animation:
    "images/v11_bbc4a_marcel_charisma.webp" with fps
    pause 0.3
    "images/v11_bbc4b_marcel_charisma.webp" with fps
    pause 0.2
    "images/v11_bbc4c_marcel_charisma.webp" with fps
    pause 0.3
    "images/v11_bbc4b_marcel_charisma.webp" with fps
    pause 0.2
    repeat




image v12_stalkfap10 = Composite(
    (1920, 1080),
    (0, 0), "images/v12_stalkfap10.webp",
    (0, 0), ConditionSwitch(
        "v10_shoot_look == 'bunny'", 'v12_stalkfap10_bunny.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v12_stalkfap10_t2.webp',
        "True", Null())
)
image v12_solobbc1_animation:
    "images/v12_solobbc1.webp" with fps
    pause 0.4
    "images/v12_solobbc2.webp" with fps
    pause 0.4
    repeat
image v12_solobbc5:
    "images/v12_solobbc5a.webp" with fps
    pause 0.5
    "images/v12_solobbc5b.webp" with fps
    pause 0.8
    repeat


image v12_alison6_animation:
    "images/v12_alison6a.webp" with fps
    pause 0.3
    "images/v12_alison6b.webp" with fps
    pause 0.2
    "images/v12_alison6c.webp" with fps
    pause 0.2
    "images/v12_alison6d.webp" with fps
    pause 0.3
    "images/v12_alison6c.webp" with fps
    pause 0.2
    repeat
image v12_alison6_animation_blonde:
    "images/v12_alison6a_blonde.webp" with fps
    pause 0.3
    "images/v12_alison6b_blonde.webp" with fps
    pause 0.2
    "images/v12_alison6c_blonde.webp" with fps
    pause 0.2
    "images/v12_alison6d_blonde.webp" with fps
    pause 0.3
    "images/v12_alison6c_blonde.webp" with fps
    pause 0.2
    repeat
image v12_alison6_phone:
    "v12_alison6_phonea" with fps
    pause 0.3
    "v12_alison6_phoneb" with fps
    pause 0.2
    "v12_alison6_phonec" with fps
    pause 0.2
    "v12_alison6_phoned" with fps
    pause 0.3
    "v12_alison6_phonec" with fps
    pause 0.2
    repeat
image v12_alison6_phonea = Composite(
    (1920, 1080),
    (0, 0), ConditionSwitch(
        "v12_alison_pics == 'blonde'", 'v12_alison6_phone_blondea.webp',
        "True", 'v12_alison6_phone_a.webp')
)
image v12_alison6_phoneb = Composite(
    (1920, 1080),
    (0, 0), ConditionSwitch(
        "v12_alison_pics == 'blonde'", 'v12_alison6_phone_blondeb.webp',
        "True", 'v12_alison6_phone_b.webp')
)
image v12_alison6_phonec = Composite(
    (1920, 1080),
    (0, 0), ConditionSwitch(
        "v12_alison_pics == 'blonde'", 'v12_alison6_phone_blondec.webp',
        "True", 'v12_alison6_phone_c.webp')
)
image v12_alison6_phoned = Composite(
    (1920, 1080),
    (0, 0), ConditionSwitch(
        "v12_alison_pics == 'blonde'", 'v12_alison6_phone_blonded.webp',
        "True", 'v12_alison6_phone_d.webp')
)


image v12_cherry3_animation:
    "images/v12_cherry3a.webp" with fps
    pause 0.7
    "images/v12_cherry3b.webp" with fps
    pause 0.7
    repeat
image v12_cherry8_animation1:
    "images/v12_cherry8c.webp" with short
    pause 0.3
    "images/v12_cherry8b.webp" with fps
    pause 0.15
    "images/v12_cherry8a.webp" with vpunch
    pause 0.2
    "images/v12_cherry8b.webp" with fps
    pause 0.15
    repeat


image v12_minerva5_animation:
    "images/v12_minerva5a.webp" with fps
    pause 0.4
    "images/v12_minerva5b.webp" with vpunch
    pause 0.4
    repeat


image v12_jess2_animation1:
    "images/v12_jess2b.webp" with fps
    pause 0.2
    "images/v12_jess2c.webp" with fps
    pause 0.3
    "images/v12_jess2b.webp" with fps
    pause 0.2
    "images/v12_jess2a.webp" with fps
    pause 0.4
    repeat
image v12_jess2_animation2:
    "images/v12_jess2b.webp" with fps
    pause 0.1
    "images/v12_jess2c.webp" with fps
    pause 0.1
    "images/v12_jess2d.webp" with hpunch
    pause 0.5
    "images/v12_jess2b.webp" with fps
    pause 0.1
    "images/v12_jess2a.webp" with fps
    pause 0.2
    repeat
image v12_jess2_animation3:
    "images/v12_jess2b.webp" with fps
    pause 0.1
    "images/v12_jess2c.webp" with fps
    pause 0.1
    "images/v12_jess2d.webp" with hpunch
    pause 0.2
    "images/v12_jess2b.webp" with fps
    pause 0.1
    "images/v12_jess2a.webp" with fps
    pause 0.1
    "images/v12_jess2b.webp" with fps
    pause 0.1
    "images/v12_jess2c.webp" with fps
    pause 0.1
    "images/v12_jess2d.webp" with hpunch
    pause 0.2
    "images/v12_jess2b.webp" with fps
    pause 0.1
    "images/v12_jess2a.webp" with fps
    pause 0.1
    "images/v12_jess2b.webp" with fps
    pause 0.1
    "images/v12_jess2c.webp" with fps
    pause 0.1
    "images/v12_jess2d.webp" with hpunch
    pause 0.2
    "images/v12_jess2b.webp" with fps
    pause 0.1
    "images/v12_jess2a.webp" with fps
    pause 0.1
    "images/v12_jess2b.webp" with fps
    pause 0.1
    "images/v12_jess2c.webp" with fps
    pause 0.1
    "images/v12_jess2d.webp" with hpunch
    pause 0.2
    "images/v12_jess2d.webp" with hpunch
    pause 0.2
    "images/v12_jess2d.webp" with hpunch
    pause 0.2
    "images/v12_jess2d.webp" with fps
    pause 1
    "images/v12_jess2b.webp" with fps
    pause 0.2
    "images/v12_jess2a.webp" with fps
    pause 0.5
    repeat
image v12_jess4_animation1:
    "images/v12_jess4a.webp" with fps
    pause 0.5
    "images/v12_jess4b.webp" with fps
    pause 0.4
    repeat
image v12_jess4_animation2:
    "images/v12_jess4a.webp" with fps
    pause 0.2
    "images/v12_jess4b.webp" with fps
    pause 0.1
    "images/v12_jess4c.webp" with vpunch
    pause 0.2
    "images/v12_jess4b.webp" with fps
    pause 0.1
    repeat
image v12_jess6_animation:
    "images/v12_jess6a.webp" with fps
    pause 0.5
    "images/v12_jess6b.webp" with vpunch
    pause 0.4
    repeat

transform beachskybg1:
    yalign 0.0

transform beachskybg2:
    subpixel True
    yalign 0.0
    ease 4 yalign 1.0

transform beachskybg3:
    subpixel True
    yalign 1.0
    ease 4 yalign 0.0

transform beachskybg4:
    subpixel True
    yalign 1.0
    ease 3.5 yalign 0.3
transform beachskybg5:
    subpixel True
    yalign 0.3
    ease 3.5 yalign 1.0

transform beach:
    yalign 0.0
    yalign 1.0
transform sky:
    yalign 1.0
    yalign 0.0




image v12_axel10a = Composite(
    (1920, 1080),
    (0, 0), "images/v12_axel10a.webp",
    (0, 0), ConditionSwitch(
        "lena_look == 'summer'", 'v12_axel10_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v12_axel10_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v12_axel10_p2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v12_axel10_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v12_axel10_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v12_axel10_t3.webp',
        "True", Null())
)
image v12_axel10b = Composite(
    (1920, 1080),
    (0, 0), "images/v12_axel10b.webp",
    (0, 0), ConditionSwitch(
        "lena_look == 'summer'", 'v12_axel10_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v12_axel10_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v12_axel10_p2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v12_axel10_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v12_axel10_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v12_axel10_t3.webp',
        "True", Null())
)
image v12_axel10c = Composite(
    (1920, 1080),
    (0, 0), "images/v12_axel10c.webp",
    (0, 0), ConditionSwitch(
        "lena_look == 'summer'", 'v12_axel10_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v12_axel10_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v12_axel10_p2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v12_axel10_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v12_axel10_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v12_axel10_t3.webp',
        "True", Null())
)


image v12_axel15a = Composite(
    (1920, 1080),
    (0, 0), "images/v12_axel15a.webp",
    (0, 0), ConditionSwitch(
        "lena_look == 'summer'", 'v12_axel15a_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v12_axel15a_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v12_axel15a_t3.webp',
        "True", Null())
)
image v12_axel15b = Composite(
    (1920, 1080),
    (0, 0), "images/v12_axel15b.webp",
    (0, 0), ConditionSwitch(
        "lena_look == 'summer'", 'v12_axel15b_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v12_axel15b_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v12_axel15b_t3.webp',
        "True", Null())
)
image v12_axel15c = Composite(
    (1920, 1080),
    (0, 0), "images/v12_axel15c.webp",
    (0, 0), ConditionSwitch(
        "lena_look == 'summer'", 'v12_axel15c_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v12_axel15c_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v12_axel15c_t3.webp',
        "True", Null())
)
image v12_axel15_animation1:
    "v12_axel15b" with fps
    pause 0.3
    "v12_axel15a" with fps
    pause 0.25
    "v12_axel15b" with fps
    pause 0.3
    "v12_axel15c" with fps
    pause 0.3
    repeat

image v12_axel15_animation2:
    "v12_axel15b" with fps
    pause 0.2
    "v12_axel15a" with fps
    pause 0.2
    "v12_axel15b" with fps
    pause 0.2
    "v12_axel15c" with vpunch
    pause 0.3
    repeat
image v12_axel15_animation3:
    "v12_axel15b" with fps
    pause 0.10
    "v12_axel15a" with fps
    pause 0.15
    "v12_axel15b" with fps
    pause 0.1
    "v12_axel15c" with vpunch
    pause 0.2
    repeat


image v12_axel16a = Composite(
    (1920, 1080),
    (0, 0), "images/v12_axel16a.webp",
    (0, 0), ConditionSwitch(
        "lena_look == 'summer'", 'v12_axel16a_choker.webp',
        "True", Null())
)
image v12_axel16b = Composite(
    (1920, 1080),
    (0, 0), "images/v12_axel16b.webp",
    (0, 0), ConditionSwitch(
        "lena_look == 'summer'", 'v12_axel16b_choker.webp',
        "True", Null())
)
image v12_axel16c = Composite(
    (1920, 1080),
    (0, 0), "images/v12_axel16c.webp",
    (0, 0), ConditionSwitch(
        "lena_look == 'summer'", 'v12_axel16c_choker.webp',
        "True", Null())
)
image v12_axel16_animation:
    "v12_axel16b" with fps
    pause 0.2
    "v12_axel16c" with vpunch
    pause 0.3
    "v12_axel16b" with fps
    pause 0.2
    "v12_axel16a" with fps
    pause 0.3
    repeat
image v12_axel16_animation2:
    "v12_axel16b" with fps
    pause 0.15
    "v12_axel16c" with vpunch
    pause 0.2
    "v12_axel16b" with fps
    pause 0.15
    "v12_axel16a" with fps
    pause 0.25
    repeat


image v12_emma7_animation:
    "images/v12_emma7a.webp" with fps
    pause 0.5
    "images/v12_emma7b.webp" with vpunch
    pause 0.4
    repeat
image v12_emma7_animationn:
    "images/v12_emma7an.webp" with fps
    pause 0.5
    "images/v12_emma7bn.webp" with vpunch
    pause 0.4
    repeat
image v12_emma7_animation2:
    "images/v12_emma7a.webp" with fps
    pause 0.35
    "images/v12_emma7b.webp" with vpunch
    pause 0.25
    repeat
image v12_emma7_animation2n:
    "images/v12_emma7an.webp" with fps
    pause 0.35
    "images/v12_emma7bn.webp" with vpunch
    pause 0.25
    repeat


image v12_emma13_animation:
    "images/v12_emma13a.webp" with fps
    pause 0.4
    "images/v12_emma13b.webp" with vpunch
    pause 0.3
    repeat


image v12_emma15_animation:
    "images/v12_emma15a.webp" with fps
    pause 0.4
    "images/v12_emma15b.webp" with fps
    pause 0.4
    repeat
image v12_emma15_animation2:
    "images/v12_emma15a.webp" with fps
    pause 0.3
    "images/v12_emma15b.webp" with hpunch
    pause 0.3
    repeat




image v12_holly3_animation1:
    "images/v12_holly3a.webp" with fps
    pause 0.5
    "images/v12_holly3b.webp" with fps
    pause 0.5
    repeat
image v12_holly3_animation2:
    "images/v12_holly3a.webp" with fps
    pause 0.4
    "images/v12_holly3b.webp" with fps
    pause 0.3
    "images/v12_holly3c.webp" with fps
    pause 0.4
    "images/v12_holly3b.webp" with fps
    pause 0.3
    repeat
image v12_holly3_animation3:
    "images/v12_holly3a.webp" with fps
    pause 0.3
    "images/v12_holly3b.webp" with fps
    pause 0.2
    "images/v12_holly3c.webp" with fps
    pause 0.3
    "images/v12_holly3b.webp" with fps
    pause 0.2
    repeat


image v12_holly14_animation1:
    "images/v12_holly14a.webp" with fps
    pause 0.6
    "images/v12_holly14b.webp" with fps
    pause 0.8
    repeat
image v12_holly14_animation2:
    "images/v12_holly14a.webp" with fps
    pause 0.5
    "images/v12_holly14b.webp" with fps
    pause 0.6
    repeat
image v12_holly14_animation3:
    "images/v12_holly14a.webp" with fps
    pause 0.4
    "images/v12_holly14b.webp" with vpunch
    pause 0.5
    repeat


image v12_holly15_animation1:
    "images/v12_holly15a.webp" with fps3
    pause 0.25
    "images/v12_holly15b.webp" with fps3
    pause 0.2
    "images/v12_holly15c.webp" with fps3
    pause 0.2
    "images/v12_holly15d.webp" with fps3
    pause 0.2
    "images/v12_holly15c.webp" with fps3
    pause 0.2
    "images/v12_holly15b.webp" with fps3
    pause 0.2
    repeat

image v12_holly15_animation2:
    "images/v12_holly15a.webp" with vpunch
    pause 0.25
    "images/v12_holly15b.webp" with fps3
    pause 0.15
    "images/v12_holly15c.webp" with fps3
    pause 0.15
    "images/v12_holly15d.webp" with fps3
    pause 0.2
    "images/v12_holly15c.webp" with fps3
    pause 0.15
    "images/v12_holly15b.webp" with fps3
    pause 0.15
    repeat

image v12_holly22a = Composite(
    (1920, 1080),
    (0, 0), "v12_holly22a.webp",
    (0, 0), ConditionSwitch(
        "holly_tattoo", 'v12_holly22a_t.webp',
        "True", Null()),
)
image v12_holly22b = Composite(
    (1920, 1080),
    (0, 0), "v12_holly22b.webp",
    (0, 0), ConditionSwitch(
        "holly_tattoo", 'v12_holly22b_t.webp',
        "True", Null()),
)
image v12_holly22c = Composite(
    (1920, 1080),
    (0, 0), "v12_holly22c.webp",
    (0, 0), ConditionSwitch(
        "holly_tattoo", 'v12_holly22c_t.webp',
        "True", Null()),
)
image v12_holly22_animation:
    "v12_holly22b" with vpunch
    pause 0.15
    "v12_holly22a" with fps3
    pause 0.25
    "v12_holly22b" with fps3
    pause 0.15
    "v12_holly22c" with vpunch
    pause 0.20
    repeat


image v12_holly24_animation:
    "images/v12_holly24a.webp" with fps
    pause 0.3
    "images/v12_holly24b.webp" with fps
    pause 0.3
    repeat

image v12_holly27_animation:
    "images/v12_holly27a.webp" with fps
    pause 0.4
    "images/v12_holly27b.webp" with fps
    pause 0.4
    repeat

image v12_holly30_animation:
    "images/v12_holly30b.webp" with fps3
    pause 0.15
    "images/v12_holly30a.webp" with fps3
    pause 0.20
    "images/v12_holly30b.webp" with fps3
    pause 0.15
    "images/v12_holly30c.webp" with fps3
    pause 0.20
    repeat

image v12_holly28_animation:
    "images/v12_holly28a.webp" with fps
    pause 0.3
    "images/v12_holly28b.webp" with fps
    pause 0.3
    "images/v12_holly28c.webp" with fps
    pause 0.3
    repeat



image v12_lena5a = Composite(
    (1920, 1080),
    (0, 0), "images/v12_lena5a.webp",
    (0, 0), ConditionSwitch(
        "lena_look == 'summer'", 'v12_lena5a_choker.webp',
        "True", Null())
)
image v12_lena5b = Composite(
    (1920, 1080),
    (0, 0), "images/v12_lena5b.webp",
    (0, 0), ConditionSwitch(
        "lena_look == 'summer'", 'v12_lena5b_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v12_lena_facefuck", 'v12_lena5b_spit.webp',
        "True", Null())
)
image v12_lena5bb = Composite(
    (1920, 1080),
    (0, 0), "images/v12_lena5bb.webp",
    (0, 0), ConditionSwitch(
        "lena_look == 'summer'", 'v12_lena5b_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v12_lena_facefuck", 'v12_lena5b_spit.webp',
        "True", Null())
)
image v12_lena5c = Composite(
    (1920, 1080),
    (0, 0), "images/v12_lena5c.webp",
    (0, 0), ConditionSwitch(
        "lena_look == 'summer'", 'v12_lena5c_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v12_lena_facefuck", 'v12_lena5c_spit.webp',
        "True", Null())
)
image v12_lena5cb = Composite(
    (1920, 1080),
    (0, 0), "images/v12_lena5cb.webp",
    (0, 0), ConditionSwitch(
        "lena_look == 'summer'", 'v12_lena5c_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v12_lena_facefuck", 'v12_lena5c_spit.webp',
        "True", Null())
)
image v12_lena5d = Composite(
    (1920, 1080),
    (0, 0), "images/v12_lena5d.webp",
    (0, 0), ConditionSwitch(
        "lena_look == 'summer'", 'v12_lena5d_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v12_lena_facefuck", 'v12_lena5d_spit.webp',
        "True", Null())
)
image v12_lena5db = Composite(
    (1920, 1080),
    (0, 0), "images/v12_lena5db.webp",
    (0, 0), ConditionSwitch(
        "lena_look == 'summer'", 'v12_lena5d_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v12_lena_facefuck", 'v12_lena5d_spit.webp',
        "True", Null())
)
image v12_lena5_animation1:
    "v12_lena5b" with fps
    pause 0.6
    "v12_lena5c" with fps
    pause 0.8
    repeat
image v12_lena5_animation2:
    "v12_lena5c" with fps
    pause 0.3
    "v12_lena5d" with hpunch
    pause 0.4
    "v12_lena5c" with fps
    pause 0.3
    "v12_lena5b" with fps
    pause 0.4
    repeat
image v12_lena5_animation3:
    "v12_lena5cb" with fps
    pause 0.25
    "v12_lena5db" with hpunch
    pause 0.35
    "v12_lena5cb" with fps
    pause 0.25
    "v12_lena5bb" with fps
    pause 0.3
    repeat

image v12_lena27_animation:
    "images/v12_lena_27a.webp" with fps
    pause 0.6
    "images/v12_lena_27b.webp" with fps
    pause 0.6
    repeat

image v12_lena_feet2_animation:
    "images/v12_lena_feet4.webp" with fps
    pause 0.6
    "images/v12_lena_feet3.webp" with fps
    pause 0.6
    repeat
image v12_lena_feet2_animation2:
    "images/v12_lena_feet4.webp" with fps
    pause 0.35
    "images/v12_lena_feet3.webp" with fps
    pause 0.35
    repeat
image v12_lena_feet3_animation:
    "images/v12_lena_feet6.webp" with fps
    pause 0.6
    "images/v12_lena_feet5.webp" with fps
    pause 0.6
    repeat
image v12_lena_feet4_animation:
    "images/v12_lena_feet6.webp" with fps
    pause 0.4
    "images/v12_lena_feet5.webp" with fps
    pause 0.4
    "images/v12_lena_feet4.webp" with fps
    pause 0.4
    "images/v12_lena_feet3.webp" with fps
    pause 0.4
    repeat


image v12_lena_30_animation:
    "images/v12_lena_30b.webp" with fps
    pause 0.7
    "images/v12_lena_30a.webp" with fps
    pause 0.7
    repeat

image v12_lena28_animation:
    "v12_lena28a" with fps3
    pause 0.2
    "v12_lena28b" with fps3
    pause 0.2
    "v12_lena28c" with fps3
    pause 0.25
    "v12_lena28d" with fps3
    pause 0.25
    "v12_lena28e" with fps3
    pause 0.2
    repeat
image v12_lena28a = Composite(
    (1920, 1080),
    (0, 0), "v12_lena28a.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v12_lena28a_choker.webp',
        "lena_necklace == 'gift2'", 'v12_lena28a_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v12_lena28a_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v12_lena28a_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v12_lena28a_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v12_lena28a_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v12_lena28a_p2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v12_gift == 'lena' and ian_lena_pure", 'v12_lena28a_necklace.webp',
        "lena_necklace == 'gift'", 'v12_lena28a_necklace.webp',
        "lena_necklace == 'gift2'", 'v12_lena28a_necklace.webp',
        "True", Null())
)
image v12_lena28b = Composite(
    (1920, 1080),
    (0, 0), "v12_lena28b.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v12_lena28b_choker.webp',
        "lena_necklace == 'gift2'", 'v12_lena28b_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v12_lena28b_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v12_lena28b_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v12_lena28b_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v12_lena28b_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v12_lena28b_p2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v12_gift == 'lena' and ian_lena_pure", 'v12_lena28b_necklace.webp',
        "lena_necklace == 'gift'", 'v12_lena28b_necklace.webp',
        "lena_necklace == 'gift2'", 'v12_lena28b_necklace.webp',
        "True", Null())
)
image v12_lena28c = Composite(
    (1920, 1080),
    (0, 0), "v12_lena28c.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v12_lena28c_choker.webp',
        "lena_necklace == 'gift2'", 'v12_lena28c_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v12_lena28c_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v12_lena28c_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v12_lena28c_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v12_lena28c_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v12_lena28c_p2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v12_gift == 'lena' and ian_lena_pure", 'v12_lena28c_necklace.webp',
        "lena_necklace == 'gift'", 'v12_lena28c_necklace.webp',
        "lena_necklace == 'gift2'", 'v12_lena28c_necklace.webp',
        "True", Null())
)
image v12_lena28d = Composite(
    (1920, 1080),
    (0, 0), "v12_lena28d.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v12_lena28d_choker.webp',
        "lena_necklace == 'gift2'", 'v12_lena28d_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v12_lena28d_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v12_lena28d_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v12_lena28d_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v12_lena28d_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v12_lena28d_p2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v12_gift == 'lena' and ian_lena_pure", 'v12_lena28d_necklace.webp',
        "lena_necklace == 'gift'", 'v12_lena28d_necklace.webp',
        "lena_necklace == 'gift2'", 'v12_lena28d_necklace.webp',
        "True", Null())
)
image v12_lena28e = Composite(
    (1920, 1080),
    (0, 0), "v12_lena28e.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v12_lena28e_choker.webp',
        "lena_necklace == 'gift2'", 'v12_lena28e_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v12_lena28e_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v12_lena28e_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v12_lena28e_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v12_lena28e_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v12_lena28e_p2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v12_gift == 'lena' and ian_lena_pure", 'v12_lena28e_necklace.webp',
        "lena_necklace == 'gift'", 'v12_lena28e_necklace.webp',
        "lena_necklace == 'gift2'", 'v12_lena28e_necklace.webp',
        "True", Null())
)
image v12_lena38_animation:
    "images/v12_lena38a.webp" with fps
    pause 0.3
    "images/v12_lena38b.webp" with vpunch
    pause 0.4
    repeat

image v12_trinity_animation:
    "v12_trinity9a" with fps
    pause 0.4
    "v12_trinity9b" with fps
    pause 0.35
    "v12_trinity9c" with fps
    pause 0.35
    "v12_trinity9d" with fps
    pause 0.4
    repeat

image v12_trinity17_animation:
    "images/v12_trinity17a.webp" with fps
    pause 0.3
    "images/v12_trinity17b.webp" with vpunch
    pause 0.4
    repeat

image v12_trinity9a = Composite(
    (1920, 1080),
    (0, 0), "v12_trinity9a.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v12_trinity9a_choker.webp',
        "True", Null())
)
image v12_trinity9b = Composite(
    (1920, 1080),
    (0, 0), "v12_trinity9b.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v12_trinity9b_choker.webp',
        "True", Null())
)
image v12_trinity9c = Composite(
    (1920, 1080),
    (0, 0), "v12_trinity9c.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v12_trinity9c_choker.webp',
        "True", Null())
)
image v12_trinity9d = Composite(
    (1920, 1080),
    (0, 0), "v12_trinity9d.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v12_trinity9d_choker.webp',
        "True", Null())
)

image v12_cindy_pg2 = Composite(
    (1920, 1080),
    (0, 0), "v12_cindy_pg2.webp",
    (0, 0), ConditionSwitch(
        "v12_gift == 'cindy' and v12_cindy_rel == 2 or v12_gift == 'cindy' and ian_cindy > 9", 'v12_cindy_pg2_necklace.webp',
        "True", Null())
)
image v12_cindy_pg2b = Composite(
    (1920, 1080),
    (0, 0), "v12_cindy_pg2b.webp",
    (0, 0), ConditionSwitch(
        "v12_gift == 'cindy' and v12_cindy_rel == 2 or v12_gift == 'cindy' and ian_cindy > 9", 'v12_cindy_pg2b_necklace.webp',
        "True", Null())
)


image v12_lena30 = Composite(
    (1920, 1080),
    (0, 0), "v12_lena30.webp",
    (0, 0), ConditionSwitch(
        "ian_summer_look == 'wits'", 'v12_lena30_wits.webp',
        "ian_summer_look == 'charisma'", 'v12_lena30_charisma.webp',
        "ian_summer_look == 'lust'", 'v12_lena30_lust.webp',
        "ian_summer_look == 'athletics'", 'v12_lena30_athletics.webp',
        "True", Null())
)


image v12_lena37a = Composite(
    (1920, 1080),
    (0, 0), "v12_lena37a.webp",
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v12_lena37a_p1.webp',
        "lena_piercing2", 'v12_lena37a_p2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v12_lena37a_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v12_lena37a_t2.webp',
        "True", Null())
)
image v12_lena37b = Composite(
    (1920, 1080),
    (0, 0), "v12_lena37b.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v12_lena37b_t2.webp',
        "True", Null())
)
image v12_lena37c = Composite(
    (1920, 1080),
    (0, 0), "v12_lena37c.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v12_lena37c_t2.webp',
        "True", Null())
)
image v12_lena37_animation1:
    "v12_lena37b" with fps
    pause 0.35
    "v12_lena37c" with fps
    pause 0.4
    "v12_lena37b" with fps
    pause 0.35
    "v12_lena37a" with fps
    pause 0.5
    repeat
image v12_lena37_animation2:
    "v12_lena37b" with fps
    pause 0.25
    "v12_lena37c" with fps
    pause 0.3
    "v12_lena37b" with fps
    pause 0.25
    "v12_lena37a" with fps
    pause 0.3
    repeat
image v12_lena37_animation3:
    "v12_lena37b" with fps
    pause 0.15
    "v12_lena37c" with fps
    pause 0.2
    "v12_lena37b" with fps
    pause 0.2
    "v12_lena37a" with fps
    pause 0.2
    repeat




image v13_stan5a = Composite(
    (1920, 1080),
    (0, 0), "v13_stan5a.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v13_stan5a_t2.webp',
        "True", Null())
)
image v13_stan5b = Composite(
    (1920, 1080),
    (0, 0), "v13_stan5b.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v13_stan5b_t2.webp',
        "True", Null())
)
image v13_stan5_animation1:
    "v13_stan5b" with fps
    pause 0.4
    "v13_stan5a" with fps
    pause 0.4
    repeat
image v13_stan5_animation2:
    "v13_stan5b" with fps
    pause 0.2
    "v13_stan5a" with fps
    pause 0.2
    repeat


image v13_guy5_ian_animation:
    "images/v13_guy5a_ian.webp" with fps
    pause 0.4
    "images/v13_guy5b_ian.webp" with vpunch
    pause 0.6
    repeat
image v13_guy5_mark_animation:
    "images/v13_guy5a_mark.webp" with fps
    pause 0.4
    "images/v13_guy5b_mark.webp" with vpunch
    pause 0.6
    repeat
image v13_guy5_robert_animation:
    "images/v13_guy5a_robert.webp" with fps
    pause 0.4
    "images/v13_guy5b_robert.webp" with vpunch
    pause 0.6
    repeat
image v13_guy5_dildo_animation:
    "images/v13_guy5a_dildo.webp" with fps
    pause 0.4
    "images/v13_guy5b_dildo.webp" with vpunch
    pause 0.6
    repeat

image v13_guy6_ian_animation:
    "images/v13_guy6a_ian.webp" with fps
    pause 0.3
    "images/v13_guy6b_ian.webp" with vpunch
    pause 0.4
    repeat
image v13_guy6_mark_animation:
    "images/v13_guy6a_mark.webp" with fps
    pause 0.3
    "images/v13_guy6b_mark.webp" with vpunch
    pause 0.4
    repeat
image v13_guy6_robert_animation:
    "images/v13_guy6a_robert.webp" with fps
    pause 0.3
    "images/v13_guy6b_robert.webp" with vpunch
    pause 0.4
    repeat
image v13_guy6_john_animation:
    "images/v13_guy6a_john.webp" with fps
    pause 0.3
    "images/v13_guy6b_john.webp" with vpunch
    pause 0.4
    repeat

image v13_stan11_animation:
    "images/v13_stan11a.webp" with fps
    pause 0.3
    "images/v13_stan11b.webp" with vpunch
    pause 0.4
    repeat

image v13_glory1_animation:
    "images/v13_glory1a.webp" with fps
    pause 0.6
    "images/v13_glory1b.webp" with fps
    pause 0.6
    repeat
image v13_glory3_animation:
    "images/v13_glory3b.webp" with fps
    pause 0.4
    "images/v13_glory3a.webp" with fps
    pause 0.4
    repeat
image v13_glory5_animation:
    "images/v13_glory5b.webp" with fps
    pause 0.2
    "images/v13_glory5c.webp" with fps
    pause 0.3
    "images/v13_glory5b.webp" with fps
    pause 0.2
    "images/v13_glory5a.webp" with fps
    pause 0.25
    repeat
image v13_glory5_animation2:
    "images/v13_glory5b.webp" with fps
    pause 0.15
    "images/v13_glory5c.webp" with vpunch
    pause 0.25
    "images/v13_glory5b.webp" with fps
    pause 0.15
    "images/v13_glory5a.webp" with fps
    pause 0.15
    repeat
image v13_glory6_animation:
    "images/v13_glory6b.webp" with fps
    pause 0.3
    "images/v13_glory6a.webp" with fps
    pause 0.4
    repeat


image v13_lena_mast1_animation:
    "images/v13_lena_mast1a.webp" with fps
    pause 0.3
    "images/v13_lena_mast1b.webp" with fps
    pause 0.4
    repeat
image v13_lena_mast2_animation:
    "images/v13_lena_mast2a.webp" with fps
    pause 0.3
    "images/v13_lena_mast2b.webp" with fps
    pause 0.4
    repeat
image v13_solo2a = Composite(
    (1920, 1080),
    (0, 0), "images/v13_solo2a.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v13_solo2_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v13_solo2_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v13_solo2_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v13_solo2_p2.webp',
        "True", Null())
)
image v13_solo2b = Composite(
    (1920, 1080),
    (0, 0), "images/v13_solo2b.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v13_solo2_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v13_solo2_t2b.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v13_solo2_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v13_solo2_p2.webp',
        "True", Null())
)
image v13_solo2c = Composite(
    (1920, 1080),
    (0, 0), "images/v13_solo2c.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v13_solo2_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v13_solo2_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v13_solo2_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v13_solo2_p2.webp',
        "True", Null())
)
image v13_solo2ab = Composite(
    (1920, 1080),
    (0, 0), "images/v13_solo2a.webp",
    (0, 0), "images/v13_solo2bb.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v13_solo2_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v13_solo2_t2b.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v13_solo2_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v13_solo2_p2.webp',
        "True", Null())
)
image v13_solo2_animation:
    "v13_solo2ab" with fps
    pause 0.4
    "v13_solo2b" with fps
    pause 0.4
    repeat


image v13_jeremy3_animation:
    "images/v13_jeremy3b.webp" with fps
    pause 0.4
    "images/v13_jeremy3a.webp" with fps
    pause 0.4
    repeat

image v13_jeremy5_animation1:
    "images/v13_jeremy5b.webp" with fps
    pause 0.4
    "images/v13_jeremy5a.webp" with fps
    pause 0.4
    repeat
image v13_jeremy5_animation2:
    "images/v13_jeremy5b.webp" with fps
    pause 0.3
    "images/v13_jeremy5c.webp" with fps
    pause 0.4
    "images/v13_jeremy5b.webp" with fps
    pause 0.3
    "images/v13_jeremy5a.webp" with fps
    pause 0.4
    repeat
image v13_jeremy5_animation3:
    "images/v13_jeremy5b.webp" with fps
    pause 0.2
    "images/v13_jeremy5c.webp" with vpunch
    pause 0.3
    "images/v13_jeremy5b.webp" with fps
    pause 0.2
    "images/v13_jeremy5a.webp" with fps
    pause 0.3
    repeat
image v13_jeremy5_animation4:
    "images/v13_jeremy5b.webp" with fps
    pause 0.2
    "images/v13_jeremy5c.webp" with fps
    pause 0.2
    "images/v13_jeremy5d.webp" with vpunch
    pause 0.3
    "images/v13_jeremy5b.webp" with fps
    pause 0.2
    "images/v13_jeremy5a.webp" with fps
    pause 0.3
    repeat



image v13_emma8 = Composite(
    (1920, 1080),
    (0, 0), "images/v13_emma8.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v13_emma8_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v13_emma8_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v13_emma8_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v13_emma8_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v13_emma8_p2.webp',
        "True", Null())
)
image v13_emma9 = Composite(
    (1920, 1080),
    (0, 0), "images/v13_emma9.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v13_emma9_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v13_emma9_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v13_emma9_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v13_emma9_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v13_emma9_p2.webp',
        "True", Null())
)
image v13_emma10 = Composite(
    (1920, 1080),
    (0, 0), "images/v13_emma10.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v13_emma10_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v13_emma10_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v13_emma10_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v13_emma10_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v13_emma10_p2.webp',
        "True", Null())
)
image v13_emma8_animation1:
    "v13_emma9" with fps
    pause 0.25
    "v13_emma10" with fps
    pause 0.35
    "v13_emma8" with fps
    pause 0.32
    repeat
image v13_emma8_animation2:
    "v13_emma9" with fps
    pause 0.2
    "v13_emma10" with hpunch
    pause 0.3
    "v13_emma8" with fps
    pause 0.3
    repeat
image v13_emma11_animation1:
    "images/v13_emma14.webp" with fps
    pause 0.2
    "images/v13_emma11.webp" with fps
    pause 0.3
    "images/v13_emma12.webp" with fps
    pause 0.15
    "images/v13_emma13.webp" with vpunch
    pause 0.2
    repeat
image v13_emma11_animation2:
    "images/v13_emma11.webp" with fps
    pause 0.25
    "images/v13_emma12.webp" with fps
    pause 0.2
    "images/v13_emma13.webp" with vpunch
    pause 0.25
    repeat
image v13_emma11_animation3:
    "images/v13_emma11.webp" with fps
    pause 0.25
    "images/v13_emma12.webp" with fps
    pause 0.2
    "images/v13_emma13.webp" with vpunch
    pause 0.12
    "images/v13_emma14.webp" with fps
    pause 0.15
    "images/v13_emma11.webp" with fps
    pause 0.25
    "images/v13_emma12.webp" with fps
    pause 0.2
    "images/v13_emma13.webp" with vpunch
    pause 0.12
    "images/v13_emma14.webp" with fps
    pause 0.15
    "images/v13_emma11.webp" with fps
    pause 0.25
    "images/v13_emma12.webp" with fps
    pause 0.2
    "images/v13_emma13.webp" with vpunch
    pause 0.12
    "images/v13_emma13.webp" with flash
    pause 0.3
    "images/v13_emma13.webp" with vpunch
    pause 1


image v13_ian_bj1 = Composite(
    (1920, 1080),
    (0, 0), "v13_ian_bj1.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v10_wc1_tfull.webp',
        "True", Null()),
)
image v13_ian_bj1b = Composite(
    (1920, 1080),
    (0, 0), "v13_ian_bj1b.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v10_wc1_tfull.webp',
        "True", Null()),
)
image v13_ian_bj1a = Composite(
    (1920, 1080),
    (0, 0), "v13_ian_bj1b.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v10_wc1_tfull.webp',
        "True", Null()),
)
image v13_ian_bj2 = Composite(
    (1920, 1080),
    (0, 0), "v13_ian_bj2.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v10_wc2_tfull.webp',
        "True", Null()),
)
image v13_ian_bj3 = Composite(
    (1920, 1080),
    (0, 0), "v13_ian_bj3.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v10_wc3_tfull.webp',
        "True", Null()),
)
image v13_ian_bj4 = Composite(
    (1920, 1080),
    (0, 0), "v13_ian_bj4.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v13_ian_bj4_t2.webp',
        "True", Null()),
)
image v13_ian_bj5 = Composite(
    (1920, 1080),
    (0, 0), "v13_ian_bj5.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v10_wc2_tfull.webp',
        "True", Null()),
)
image v13_ian_bj5_up = Composite(
    (1920, 1080),
    (0, 0), "v13_ian_bj5_up.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v10_wc2_tfull.webp',
        "True", Null()),
)
image v13_ian_bj6 = Composite(
    (1920, 1080),
    (0, 0), "v13_ian_bj6.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v10_wc2_tfull.webp',
        "True", Null()),
)
image v13_ian_bj7 = Composite(
    (1920, 1080),
    (0, 0), "v13_ian_bj7.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v10_wc1_tfull.webp',
        "True", Null()),
)
image v13_ian_bj5a = Composite(
    (1920, 1080),
    (0, 0), "v13_ian_bj5a.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v13_ian_bj5_t2.webp',
        "True", Null()),
)
image v13_ian_bj5b = Composite(
    (1920, 1080),
    (0, 0), "v13_ian_bj5b.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v13_ian_bj5_t2.webp',
        "True", Null()),
)
image v13_ian_bj5c = Composite(
    (1920, 1080),
    (0, 0), "v13_ian_bj5c.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v13_ian_bj5_t2.webp',
        "True", Null()),
)
image v13_ian_bj2a = Composite(
    (1920, 1080),
    (0, 0), "v13_ian_bj2a.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v10_wc2_tfull.webp',
        "True", Null()),
)

image v13_ian_bj_animation1:

    "v13_ian_bj6" with fps
    pause 0.3
    "v13_ian_bj2" with fps
    pause 0.3
    "v13_ian_bj6" with fps
    pause 0.3

    "v13_ian_bj2" with fps
    pause 0.2
    "v13_ian_bj5_up" with fps
    pause 0.2
    "v13_ian_bj6" with fps
    pause 0.3

    "v13_ian_bj2" with fps
    pause 0.2
    "v13_ian_bj5_up" with fps
    pause 0.2
    "v13_ian_bj6" with fps
    pause 0.3

    "v13_ian_bj2" with fps
    pause 0.2
    "v13_ian_bj5_up" with fps
    pause 0.2
    "v13_ian_bj6" with fps
    pause 0.3
    "v13_ian_bj1" with fps
    pause 0.3
    repeat

image v13_ian_bj_animation2:
    "v13_ian_bj2" with fps
    pause 0.15
    "v13_ian_bj3" with fps
    pause 0.15
    "v13_ian_bj4" with vpunch
    pause 0.6
    "v13_ian_bj4" with vpunch
    pause 1.2

    "v13_ian_bj5b" with fps
    pause 0.2
    "v13_ian_bj5c" with fps3
    pause 0.15

    "v13_ian_bj5" with fps3
    pause 0.15

    "v13_ian_bj6" with fps
    pause 0.25
    "v13_ian_bj1b" with fps
    pause 0.25
    "v13_ian_bj7" with fps
    pause 1.5
    "v13_ian_bj1" with fps
    pause 0.5
    "v13_ian_bj6" with fps
    pause 0.2

    "v13_ian_bj2" with fps
    pause 0.3
    "v13_ian_bj4" with fps
    pause 0.35
    "v13_ian_bj5" with fps
    pause 0.3
    "v13_ian_bj6" with fps
    pause 0.2

    "v13_ian_bj2" with fps
    pause 0.2
    "v13_ian_bj4" with fps
    pause 0.3
    "v13_ian_bj5" with fps
    pause 0.3
    "v13_ian_bj6" with fps
    pause 0.2

    "v13_ian_bj2" with fps
    pause 0.2
    "v13_ian_bj4" with fps
    pause 0.3
    "v13_ian_bj5" with fps
    pause 0.3
    "v13_ian_bj6" with fps
    pause 0.2
    "v13_ian_bj1b" with fps
    pause 0.25
    "v13_ian_bj6" with fps
    pause 0.2

    repeat
image v13_ian_bj_animation3:
    "v13_ian_bj2a" with fps
    pause 0.25
    "v13_ian_bj4" with vpunch
    pause 0.3
    "v13_ian_bj5a" with fps
    pause 0.15
    "v13_ian_bj5" with fps
    pause 0.2
    "v13_ian_bj6" with fps
    pause 0.2
    "v13_ian_bj1b" with fps
    pause 0.25
    "v13_ian_bj6" with fps
    pause 0.2
    repeat

image v13_ian_bj_animation3b:
    "v13_ian_bj4" with vpunch
    pause 0.4
    "v13_ian_bj3" with fps3
    pause 0.15
    "v13_ian_bj5a" with fps3
    pause 0.15
    "v13_ian_bj5b" with fps3
    pause 0.15
    "v13_ian_bj5c" with fps3
    pause 0.12
    "v13_ian_bj5" with fps3
    pause 0.15
    "v13_ian_bj6" with fps3
    pause 0.2
    "v13_ian_bj1b" with fps3
    pause 0.2
    "v13_ian_bj7" with fps3
    pause 1.5

image v13_ian_bj_animation4:
    "v13_ian_bj1b" with fps
    pause 0.25
    "v13_ian_bj6" with fps
    pause 0.2
    "v13_ian_bj2a" with flash
    pause 0.2
    "v13_ian_bj4" with vpunch
    pause 0.4
    "v13_ian_bj5c" with vpunch
    pause 0.3
    "v13_ian_bj6" with vpunch
    pause 0.2

    "v13_ian_bj2a" with fps
    pause 0.3
    "v13_ian_bj4" with vpunch
    pause 0.4
    "v13_ian_bj5c" with vpunch
    pause 0.3
    "v13_ian_bj6" with vpunch
    pause 0.2

    "v13_ian_bj2a" with fps
    pause 0.4
    "v13_ian_bj4" with vpunch
    pause 0.2
    "v13_ian_bj4" with flash
    pause 0.5
    "v13_ian_bj4" with vpunch
    pause 1


    "v13_ian_bj3" with fps3
    pause 0.15
    "v13_ian_bj5a" with fps3
    pause 0.15
    "v13_ian_bj5b" with fps3
    pause 0.15
    "v13_ian_bj5c" with fps3
    pause 0.12
    "v13_ian_bj5" with fps3
    pause 0.12
    "v13_ian_bj6" with fps3
    pause 0.12
    "v13_ian_bj1b" with fps3
    pause 0.12
    "v13_ian_bj7" with fps3
    pause 1.5

image v13_ian_bj_animation_test:
    "v13_ian_bj2a" with fps3
    pause 0.15
    "v13_ian_bj4" with vpunch
    pause 0.2
    "v13_ian_bj5b" with fps3
    pause 0.1
    "v13_ian_bj5" with fps3
    pause 0.15
    "v13_ian_bj6" with fps3
    pause 0.1
    "v13_ian_bj1b" with fps3
    pause 0.15
    "v13_ian_bj6" with fps3
    pause 0.1

    "v13_ian_bj2a" with fps3
    pause 0.15
    "v13_ian_bj4" with vpunch
    pause 0.2
    "v13_ian_bj5b" with fps3
    pause 0.1
    "v13_ian_bj5" with fps3
    pause 0.15
    "v13_ian_bj6" with fps3
    pause 0.1
    "v13_ian_bj1b" with fps3
    pause 0.15
    "v13_ian_bj6" with fps3
    pause 0.1

    "v13_ian_bj2a" with fps3
    pause 0.15
    "v13_ian_bj4" with vpunch
    pause 0.2
    "v13_ian_bj5b" with fps3
    pause 0.1
    "v13_ian_bj5" with fps3
    pause 0.15
    "v13_ian_bj6" with fps3
    pause 0.1
    "v13_ian_bj1b" with fps3
    pause 0.15
    "v13_ian_bj6" with fps3
    pause 0.1

    "v13_ian_bj2a" with fps3
    pause 0.15
    "v13_ian_bj4" with vpunch
    pause 0.4
    "v13_ian_bj4" with vpunch
    pause 0.7
    "v13_ian_bj3" with fps3
    pause 0.15
    "v13_ian_bj5a" with fps3
    pause 0.15
    "v13_ian_bj5b" with fps3
    pause 0.15
    "v13_ian_bj5c" with fps3
    pause 0.12
    "v13_ian_bj5" with fps3
    pause 0.12
    "v13_ian_bj6" with fps3
    pause 0.15
    "v13_ian_bj1b" with fps3
    pause 0.15
    "v13_ian_bj7" with short
    pause 1.2
    "v13_ian_bj1" with short
    pause 0.5
    "v13_ian_bj6" with fps3
    pause 0.3
    repeat



image v13_louise4_animation:
    "images/v13_louise4b.webp" with fps
    pause 0.4
    "images/v13_louise4a.webp" with fps
    pause 0.4
    repeat
image v13_louise5_animation:
    "images/v13_louise5a.webp" with fps
    pause 0.3
    "images/v13_louise5b.webp" with fps
    pause 0.35
    repeat
image v13_louise8_animation:
    "images/v13_louise8a.webp" with fps
    pause 0.4
    "images/v13_louise8b.webp" with hpunch
    pause 0.5
    repeat
image v13_louise11_animation:
    "images/v13_louise11_h1.webp" with fps
    pause 0.2
    "images/v13_louise11_h2.webp" with fps
    pause 0.2
    "images/v13_louise11_h3.webp" with fps
    pause 0.2
    "images/v13_louise11_h2.webp" with fps
    pause 0.2
    repeat
image v13_louise12_animation:
    "images/v13_louise12a.webp" with fps
    pause 0.25
    "images/v13_louise12b.webp" with fps
    pause 0.15
    "images/v13_louise12c.webp" with hpunch
    pause 0.3
    "images/v13_louise12b.webp" with fps
    pause 0.15
    repeat


image v13_emma16b = Composite(
    (1920, 1080),
    (0, 0), "v13_emma16b.webp",
    (0, 0), ConditionSwitch(
        "ian_emma_dom == 3", 'v13_emma16_sp.webp',
        "True", Null()),
)
image v13_emma16c = Composite(
    (1920, 1080),
    (0, 0), "v13_emma16c.webp",
    (0, 0), ConditionSwitch(
        "ian_emma_dom == 3", 'v13_emma16_sp.webp',
        "True", Null()),
)
image v13_emma16b_pic = Composite(
    (1920, 1080),
    (0, 0), "v13_emma16b_pic.webp",
    (0, 0), ConditionSwitch(
        "ian_emma_dom == 3", 'v13_emma16b_sp.webp',
        "True", Null()),
)
image v13_emma16c_pic = Composite(
    (1920, 1080),
    (0, 0), "v13_emma16c_pic.webp",
    (0, 0), ConditionSwitch(
        "ian_emma_dom == 3", 'v13_emma16b_sp.webp',
        "True", Null()),
)
image v13_emma17 = Composite(
    (1920, 1080),
    (0, 0), "v13_emma17.webp",
    (0, 0), ConditionSwitch(
        "ian_emma_dom == 3", 'v13_emma20_sp5.webp',
        "True", Null()),
)
image v13_emma18 = Composite(
    (1920, 1080),
    (0, 0), "v13_emma18.webp",
    (0, 0), ConditionSwitch(
        "ian_emma_dom == 3", 'v13_emma18_sp.webp',
        "True", Null()),
)
image v13_emma19 = Composite(
    (1920, 1080),
    (0, 0), "v13_emma19.webp",
    (0, 0), ConditionSwitch(
        "ian_emma_dom == 3", 'v13_emma19_sp.webp',
        "True", Null()),
)
image v13_emma20 = Composite(
    (1920, 1080),
    (0, 0), "v13_emma20.webp",
    (0, 0), ConditionSwitch(
        "ian_emma_dom == 3", 'v13_emma20_sp5.webp',
        "True", Null()),
)
image v13_emma20b = Composite(
    (1920, 1080),
    (0, 0), "v13_emma20b.webp",
    (0, 0), ConditionSwitch(
        "ian_emma_dom == 3", 'v13_emma20_sp5.webp',
        "True", Null()),
)
image v13_emma21 = Composite(
    (1920, 1080),
    (0, 0), "v13_emma21.webp",
    (0, 0), ConditionSwitch(
        "ian_emma_dom == 3", 'v13_emma21_sp.webp',
        "True", Null()),
)
image v13_emma22 = Composite(
    (1920, 1080),
    (0, 0), "v13_emma22.webp",
    (0, 0), ConditionSwitch(
        "ian_emma_dom == 3", 'v13_emma22_sp.webp',
        "True", Null()),
)
image v13_emma17_animation_pussy1:
    "v13_emma17" with fps
    pause 0.3
    "v13_emma18" with fps
    pause 0.2
    "v13_emma19" with fps
    pause 0.35
    "v13_emma18" with fps
    pause 0.2
    repeat
image v13_emma17_animation_pussy2:
    "v13_emma17" with fps
    pause 0.2
    "v13_emma18" with fps
    pause 0.15
    "v13_emma19" with vpunch
    pause 0.3
    "v13_emma18" with fps
    pause 0.15
    repeat

image v13_emma17_animation_anal1:
    "v13_emma21" with fps
    pause 0.45
    "v13_emma22" with fps
    pause 0.35
    repeat
image v13_emma17_animation_anal2:
    "v13_emma22" with vpunch
    pause 0.3
    "v13_emma21" with fps
    pause 0.35
    repeat

image v13_emma17_animation_switch1:
    "v13_emma19" with fps
    pause 0.3
    "v13_emma18" with fps
    pause 0.2
    "v13_emma17" with fps
    pause 0.35
    "v13_emma20b" with fps
    pause 0.8
    "v13_emma21" with fps
    pause 0.4
    "v13_emma22" with vpunch
    pause 0.4

image v13_emma17_animation_switch2:

    "v13_emma22" with vpunch
    pause 0.4
    "v13_emma21" with fps
    pause 0.3
    "v13_emma20" with fps
    pause 0.8
    "v13_emma17" with fps
    pause 0.3
    "v13_emma18" with fps
    pause 0.2
    "v13_emma19" with vpunch
    pause 0.35
    "v13_emma18" with fps
    pause 0.2

    "v13_emma17" with fps
    pause 0.25
    "v13_emma18" with fps
    pause 0.2
    "v13_emma19" with fps
    pause 0.3
    "v13_emma18" with fps
    pause 0.2
    "v13_emma17" with fps
    pause 0.25

    "v13_emma18" with fps
    pause 0.2
    "v13_emma19" with fps
    pause 0.3
    "v13_emma18" with fps
    pause 0.2
    "v13_emma17" with fps
    pause 0.25

    "v13_emma18" with fps
    pause 0.2
    "v13_emma19" with fps
    pause 0.3
    "v13_emma18" with fps
    pause 0.2
    "v13_emma17" with fps
    pause 0.25

    "v13_emma20b" with fps
    pause 0.8
    "v13_emma21" with fps
    pause 0.3
    "v13_emma22" with vpunch
    pause 0.3

    "v13_emma21" with fps
    pause 0.25
    "v13_emma22" with fps
    pause 0.3
    "v13_emma21" with fps
    pause 0.25
    "v13_emma22" with fps
    pause 0.3
    "v13_emma21" with fps
    pause 0.25
    "v13_emma22" with fps
    pause 0.3
    "v13_emma21" with fps
    pause 0.25
    "v13_emma22" with fps
    pause 0.3
    "v13_emma21" with fps
    pause 0.25
    repeat


image v13_alison3a = Composite(
    (1920, 1080),
    (0, 0), "v13_alison3a.webp",
    (0, 0), ConditionSwitch(
        "alison_nipple > 1", 'v13_alison3a_nips.webp',
        "True", Null()),
)
image v13_alison3b = Composite(
    (1920, 1080),
    (0, 0), "v13_alison3b.webp",
    (0, 0), ConditionSwitch(
        "alison_nipple > 1", 'v13_alison3b_nips.webp',
        "True", Null()),
)
image v13_alison3c = Composite(
    (1920, 1080),
    (0, 0), "v13_alison3c.webp",
    (0, 0), ConditionSwitch(
        "alison_nipple > 1", 'v13_alison3c_nips.webp',
        "True", Null()),
)
image v13_alison3d = Composite(
    (1920, 1080),
    (0, 0), "v13_alison3d.webp",
    (0, 0), ConditionSwitch(
        "alison_nipple > 1", 'v13_alison3d_nips.webp',
        "True", Null()),
)
image v13_alison3_animation:
    "v13_alison3a" with fps
    pause 0.3
    "v13_alison3b" with fps
    pause 0.2
    "v13_alison3c" with fps
    pause 0.2
    "v13_alison3d" with fps
    pause 0.3
    "v13_alison3c" with fps
    pause 0.2
    repeat
image v13_alison8_animation:
    "images/v13_alison8a.webp" with fps
    pause 0.35
    "images/v13_alison8b.webp" with fps
    pause 0.4
    repeat
image v13_alison9_animation:
    "images/v13_alison9b.webp" with fps
    pause 0.3
    "images/v13_alison9a.webp" with fps
    pause 0.3
    repeat
image v13_alison14 = Composite(
    (1920, 1080),
    (0, 0), "v13_alison14.webp",
    (0, 0), ConditionSwitch(
        "alison_blonde", 'v13_alison14b.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v12_gift == 'alison'", 'v13_alison14_necklace.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v13_alison_condom", 'v13_alison14_condom.webp',
        "True", Null()),
)
image v13_alison15 = Composite(
    (1920, 1080),
    (0, 0), "v13_alison15.webp",
    (0, 0), ConditionSwitch(
        "alison_blonde", 'v13_alison15b.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v12_gift == 'alison'", 'v13_alison15_necklace.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v13_alison_condom", 'v13_alison15_condom.webp',
        "True", Null()),
)
image v13_alison14_animation:
    "v13_alison15" with fps
    pause 0.4
    "v13_alison14" with hpunch
    pause 0.5
    repeat


image v13_alison21 = Composite(
    (1920, 1080),
    (0, 0), "v13_alison21.webp",
    (0, 0), ConditionSwitch(
        "alison_blonde", 'v13_alison21b.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v12_gift == 'alison'", 'v13_alison21_necklace.webp',
        "True", Null()),
)
image v13_alison22 = Composite(
    (1920, 1080),
    (0, 0), "v13_alison22.webp",
    (0, 0), ConditionSwitch(
        "alison_blonde", 'v13_alison22b.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v12_gift == 'alison'", 'v13_alison22_necklace.webp',
        "True", Null()),
)
image v13_alison23 = Composite(
    (1920, 1080),
    (0, 0), "v13_alison23.webp",
    (0, 0), ConditionSwitch(
        "alison_blonde", 'v13_alison23b.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v12_gift == 'alison'", 'v13_alison23_necklace.webp',
        "True", Null()),
)
image v13_alison24 = Composite(
    (1920, 1080),
    (0, 0), "v13_alison24.webp",
    (0, 0), ConditionSwitch(
        "alison_blonde", 'v13_alison24b.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v12_gift == 'alison'", 'v13_alison24_necklace.webp',
        "True", Null()),
)

image v13_alison21_animation1:
    "v13_alison21" with fps
    pause 0.3
    "v13_alison22" with fps
    pause 0.2
    "v13_alison23" with fps
    pause 0.2
    "v13_alison24" with fps
    pause 0.3
    "v13_alison23" with fps
    pause 0.2
    repeat

image v13_alison21_animation2:
    "v13_alison21" with fps
    pause 0.2
    "v13_alison22" with fps
    pause 0.15
    "v13_alison23" with fps
    pause 0.2
    "v13_alison24" with vpunch
    pause 0.2
    "v13_alison23" with fps
    pause 0.2
    "v13_alison21" with fps
    pause 0.2
    "v13_alison22" with fps
    pause 0.15
    "v13_alison23" with fps
    pause 0.2
    "v13_alison24" with vpunch
    pause 0.2
    "v13_alison23" with fps
    pause 0.2
    "v13_alison21" with fps
    pause 0.2
    "v13_alison22" with fps
    pause 0.15
    "v13_alison23" with fps
    pause 0.2
    "v13_alison24" with vpunch
    pause 0.2


image v13_minerva2_animation:
    "images/v13_minerva2a.webp" with fps
    pause 0.4
    "images/v13_minerva2b.webp" with hpunch
    pause 0.4
    repeat

image v13_minerva6a = Composite(
    (1920, 1080),
    (0, 0), "v13_minerva6a.webp",
    (0, 0), ConditionSwitch(
        "ian_minerva_dating < 3", 'v13_minerva6a_makeup.webp',
        "True", Null()),
)
image v13_minerva6b = Composite(
    (1920, 1080),
    (0, 0), "v13_minerva6b.webp",
    (0, 0), ConditionSwitch(
        "ian_minerva_dating < 3", 'v13_minerva6b_makeup.webp',
        "True", Null()),
)
image v13_minerva6c = Composite(
    (1920, 1080),
    (0, 0), "v13_minerva6c.webp",
    (0, 0), ConditionSwitch(
        "ian_minerva_dating < 3", 'v13_minerva6c_makeup.webp',
        "True", Null()),
)
image v13_minerva6d = Composite(
    (1920, 1080),
    (0, 0), "v13_minerva6d.webp",
    (0, 0), ConditionSwitch(
        "ian_minerva_dating < 3", 'v13_minerva6d_makeup.webp',
        "True", Null()),
)
image v13_minerva9a = Composite(
    (1920, 1080),
    (0, 0), "v13_minerva9a.webp",
    (0, 0), ConditionSwitch(
        "ian_minerva_dating < 3", 'v13_minerva9a_makeup.webp',
        "True", Null()),
)
image v13_minerva9b = Composite(
    (1920, 1080),
    (0, 0), "v13_minerva9b.webp",
    (0, 0), ConditionSwitch(
        "ian_minerva_dating < 3", 'v13_minerva9b_makeup.webp',
        "True", Null()),
)
image v13_minerva9c = Composite(
    (1920, 1080),
    (0, 0), "v13_minerva9c.webp",
    (0, 0), ConditionSwitch(
        "ian_minerva_dating < 3", 'v13_minerva9c_makeup.webp',
        "True", Null()),
)
image v13_minerva9d = Composite(
    (1920, 1080),
    (0, 0), "v13_minerva9d.webp",
    (0, 0), ConditionSwitch(
        "ian_minerva_dating < 3", 'v13_minerva9d_makeup.webp',
        "True", Null()),
)

image v13_minerva6_animation:
    "v13_minerva6b" with fps
    pause 0.3
    "v13_minerva6c" with fps
    pause 0.3
    "v13_minerva6d" with fps
    pause 0.3
    "v13_minerva6a" with fps
    pause 0.3
    repeat

image v13_minerva9_animation1:
    "v13_minerva9b" with fps
    pause 0.25
    "v13_minerva9c" with fps
    pause 0.2
    "v13_minerva9d" with fps
    pause 0.2
    "v13_minerva9a" with fps
    pause 0.3
    repeat

image v13_minerva9_animation2:
    "v13_minerva9b" with vpunch
    pause 0.2
    "v13_minerva9c" with fps
    pause 0.15
    "v13_minerva9d" with fps
    pause 0.15
    "v13_minerva9a" with fps
    pause 0.25
    repeat
image v13_minerva9_animation3:
    "v13_minerva9b" with vpunch
    pause 0.2
    "v13_minerva9c" with vpunch
    pause 0.15
    "v13_minerva9d" with fps
    pause 0.15
    "v13_minerva9a" with fps
    pause 0.2
    "v13_minerva9b" with vpunch
    pause 0.2
    "v13_minerva9c" with vpunch
    pause 0.15
    "v13_minerva9d" with fps
    pause 0.15
    "v13_minerva9a" with fps
    pause 0.2
    "v13_minerva9b" with flash
    pause 0.2
    "v13_minerva9b" with vpunch
    pause 0.2
    "v13_minerva9b" with flash
    pause 0.6
    "v13_minerva9b" with vpunch
    pause 0.6
    "v13_minerva9b" with vpunch



image v13_holly26a = Composite(
    (1920, 1080),
    (0, 0), "v13_holly26a.webp",
    (0, 0), ConditionSwitch(
        "v13_holly_abuse", 'v13_holly26a_sp.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v12_gift == 'trinity'", 'v13_holly26a_necklace.webp',
        "True", Null()),
)
image v13_holly26b = Composite(
    (1920, 1080),
    (0, 0), "v13_holly26b.webp",
    (0, 0), ConditionSwitch(
        "v13_holly_abuse", 'v13_holly26b_sp.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v12_gift == 'trinity'", 'v13_holly26b_necklace.webp',
        "True", Null()),
)
image v13_holly26c = Composite(
    (1920, 1080),
    (0, 0), "v13_holly26c.webp",
    (0, 0), ConditionSwitch(
        "v13_holly_abuse", 'v13_holly26c_sp.webp',
        "True", Null()),
)
image v13_holly26d = Composite(
    (1920, 1080),
    (0, 0), "v13_holly26d.webp",
    (0, 0), ConditionSwitch(
        "v13_holly_abuse", 'v13_holly26d_sp.webp',
        "True", Null()),
)
image v13_holly14a = Composite(
    (1920, 1080),
    (0, 0), "v13_holly14a.webp",
    (0, 0), ConditionSwitch(
        "holly_tattoo", 'v13_holly14a_t.webp',
        "True", Null()),
)
image v13_holly14b = Composite(
    (1920, 1080),
    (0, 0), "v13_holly14b.webp",
    (0, 0), ConditionSwitch(
        "holly_tattoo", 'v13_holly14b_t.webp',
        "True", Null()),
)
image v13_holly14c = Composite(
    (1920, 1080),
    (0, 0), "v13_holly14c.webp",
    (0, 0), ConditionSwitch(
        "holly_tattoo", 'v13_holly14c_t.webp',
        "True", Null()),
)
image v13_holly14d = Composite(
    (1920, 1080),
    (0, 0), "v13_holly14d.webp",
    (0, 0), ConditionSwitch(
        "holly_tattoo", 'v13_holly14d_t.webp',
        "True", Null()),
)
image v13_holly22a = Composite(
    (1920, 1080),
    (0, 0), "v13_holly22a.webp",
    (0, 0), ConditionSwitch(
        "holly_tattoo", 'v13_holly22a_t.webp',
        "True", Null()),
)
image v13_holly22b = Composite(
    (1920, 1080),
    (0, 0), "v13_holly22b.webp",
    (0, 0), ConditionSwitch(
        "holly_tattoo", 'v13_holly22b_t.webp',
        "True", Null()),
)
image v13_holly22c = Composite(
    (1920, 1080),
    (0, 0), "v13_holly22c.webp",
    (0, 0), ConditionSwitch(
        "holly_tattoo", 'v13_holly22c_t.webp',
        "True", Null()),
)
image v13_holly22d = Composite(
    (1920, 1080),
    (0, 0), "v13_holly22d.webp",
    (0, 0), ConditionSwitch(
        "holly_tattoo", 'v13_holly22d_t.webp',
        "True", Null()),
)
image v13_holly22e = Composite(
    (1920, 1080),
    (0, 0), "v13_holly22e.webp",
    (0, 0), ConditionSwitch(
        "holly_tattoo", 'v13_holly22e_t.webp',
        "True", Null()),
)
image v13_holly26_animation1:
    "images/v13_holly26b.webp" with fps
    pause 0.3
    "images/v13_holly26c.webp" with fps
    pause 0.2
    "images/v13_holly26d.webp" with fps
    pause 0.3
    "images/v13_holly26c.webp" with fps
    pause 0.2
    "images/v13_holly26b.webp" with fps
    pause 0.2
    "images/v13_holly26a.webp" with fps
    pause 0.3
    repeat
image v13_holly26_animation2:
    "v13_holly26a" with fps
    pause 0.2
    "v13_holly26b" with fps
    pause 0.15
    "v13_holly26c" with fps
    pause 0.15
    "v13_holly26d" with fps
    pause 0.15
    "images/v13_holly26e.webp" with hpunch
    pause 0.15
    "images/v13_holly26f.webp" with fps
    pause 0.15
    "images/v13_holly26g.webp" with fps
    pause 0.15
    "images/v13_holly26h.webp" with fps
    pause 0.15
    repeat
image v13_holly26_animation3:
    "v13_holly26b" with fps
    pause 0.3
    "v13_holly26c" with fps
    pause 0.4
    "v13_holly26b" with fps
    pause 0.3
    "v13_holly26a" with fps
    pause 0.4
    repeat


image v13_holly25_animation:
    "images/v13_holly25a.webp" with fps3
    pause 0.3
    "images/v13_holly25b.webp" with fps3
    pause 0.3
    "images/v13_holly25c.webp" with fps3
    pause 0.3
    repeat

image v13_holly24_animation:
    "images/v13_holly24a.webp" with fps
    pause 0.3
    "images/v13_holly24b.webp" with fps
    pause 0.3
    repeat

image v13_holly22_animation:
    "v13_holly22a" with fps3
    pause 0.25
    "v13_holly22b" with fps3
    pause 0.2
    "v13_holly22c" with fps3
    pause 0.2
    "v13_holly22d" with fps3
    pause 0.2
    "v13_holly22e" with fps3
    pause 0.2
    "v13_holly22b" with fps3
    pause 0.2
    repeat

image v13_holly14_animation:
    "v13_holly14a" with fps
    pause 0.25
    "v13_holly14b" with fps
    pause 0.2
    "v13_holly14c" with hpunch
    pause 0.25
    "v13_holly14d" with fps
    pause 0.2
    repeat



image v13_cindy8_animation1:
    "images/v13_cindy8a.webp" with fps
    pause 0.3
    "images/v13_cindy8b.webp" with fps
    pause 0.25
    "images/v13_cindy8c.webp" with fps
    pause 0.2
    "images/v13_cindy8d.webp" with fps
    pause 0.15
    repeat
image v13_cindy8_animation2:
    "images/v13_cindy8a.webp" with fps
    pause 0.3
    "images/v13_cindy8b.webp" with fps
    pause 0.25
    "images/v13_cindy8c.webp" with vpunch
    pause 0.2
    "images/v13_cindy8d.webp" with fps
    pause 0.15
    repeat

image v13_cindy8_animation3:
    "images/v13_cindy8a.webp" with fps
    pause 0.3
    "images/v13_cindy8b.webp" with flash
    pause 0.25
    "images/v13_cindy8c.webp" with vpunch
    pause 0.2
    "images/v13_cindy8d.webp" with fps
    pause 0.15
    "images/v13_cindy8a.webp" with fps
    pause 0.3
    "images/v13_cindy8b.webp" with flash
    pause 0.25
    "images/v13_cindy8c.webp" with vpunch
    pause 0.2
    "images/v13_cindy8d.webp" with vpunch
    pause 0.15
    "images/v13_cindy8a.webp" with fps
    pause 0.3
    "images/v13_cindy8b.webp" with flash
    pause 0.25
    "images/v13_cindy8c.webp" with vpunch
    pause 0.2




image v13_cindy_bj3 = Composite(
    (1920, 1080),
    (0, 0), "v13_cindy_bj3.webp",
    (0, 0), ConditionSwitch(
        "v12_gift == 'cindy' and v12_cindy_rel == 2", 'v13_cindy_bj3_necklace.webp',
        "True", Null()),
)
image v13_cindy_bj4 = Composite(
    (1920, 1080),
    (0, 0), "v13_cindy_bj4.webp",
    (0, 0), ConditionSwitch(
        "v12_gift == 'cindy' and v12_cindy_rel == 2", 'v13_cindy_bj4_necklace.webp',
        "True", Null()),
)
image v13_cindy_bj5 = Composite(
    (1920, 1080),
    (0, 0), "v13_cindy_bj5.webp",
    (0, 0), ConditionSwitch(
        "v12_gift == 'cindy' and v12_cindy_rel == 2", 'v13_cindy_bj5_necklace.webp',
        "True", Null()),
)
image v13_cindy_bj6 = Composite(
    (1920, 1080),
    (0, 0), "v13_cindy_bj6.webp",
    (0, 0), ConditionSwitch(
        "v12_gift == 'cindy' and v12_cindy_rel == 2", 'v13_cindy_bj6_necklace.webp',
        "True", Null()),
)
image v13_cindy_bj7 = Composite(
    (1920, 1080),
    (0, 0), "v13_cindy_bj7.webp",
    (0, 0), ConditionSwitch(
        "v12_gift == 'cindy' and v12_cindy_rel == 2", 'v13_cindy_bj7_necklace.webp',
        "True", Null()),
)

image v13_cindy_bj_animation1:
    "v13_cindy_bj4" with fps
    pause 0.3
    "v13_cindy_bj6" with fps
    pause 0.3
    "v13_cindy_bj3" with fps
    pause 0.3
    repeat

image v13_cindy_bj_animation2:
    "v13_cindy_bj4" with fps
    pause 0.2
    "v13_cindy_bj5" with fps2
    pause 0.25
    "v13_cindy_bj6" with fps2
    pause 0.15
    "v13_cindy_bj7" with fps
    pause 0.3
    "v13_cindy_bj3" with short
    pause 0.25
    repeat




image v14_seymour0a = Composite(
    (1920, 1080),
    (0, 0), "v14_seymour0a.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_seymour0a_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_seymour0a_t3.webp',
        "True", Null()),
)
image v14_seymour0b = Composite(
    (1920, 1080),
    (0, 0), "v14_seymour0b.webp",
    (0, 0), ConditionSwitch(
        "v13_seymour_shoot == 3", 'v14_seymour0b_hand.webp',
        "True", Null()),
)
image v14_seymour1 = Composite(
    (1920, 1080),
    (0, 0), "v14_seymour1.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_seymour1_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_seymour1_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v13_seymour_lingerie == 1", 'v14_seymour1_b.webp',
        "v13_seymour_lingerie == 2", 'v14_seymour1_w.webp',
        "True", Null()),     
)
image v14_seymour2 = Composite(
    (1920, 1080),
    (0, 0), "v14_seymour2.webp",
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v14_seymour2_p1.webp',
        "True", Null()),
        (0, 0), ConditionSwitch(
        "lena_piercing2", 'v14_seymour2_p2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v14_seymour2_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_seymour2_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_seymour2_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v13_seymour_lingerie == 1", 'v14_seymour2_b.webp',
        "v13_seymour_lingerie == 2", 'v14_seymour2_w.webp',
        "True", Null()),     
)


image v14_pool_selfie = Composite(
    (1920, 1080),
    (0, 0), "v14_pool_selfie.webp",
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v14_pool_selfie_p1.webp',
        "True", Null()),
        (0, 0), ConditionSwitch(
        "lena_piercing2", 'v14_pool_selfie_p2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v14_pool_selfie_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_pool_selfie_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_pool_selfie_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_bikini == 1", 'v14_pool_selfie1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_bikini == 1 and v14_topless == False", 'v14_pool_selfie1_top.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_bikini == 2", 'v14_pool_selfie2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_bikini == 2 and v14_topless == False", 'v14_pool_selfie2_top.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_bikini == 3", 'v14_pool_selfie3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_bikini == 3 and v14_topless == False", 'v14_pool_selfie3_top.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_smoke", 'v14_pool_selfie_smoke.webp',
        "True", Null()),
)





image v14_anthony2_animation:
    "images/v14_anthony2a.webp" with short
    pause 1
    "images/v14_anthony2b.webp" with short
    pause 1
    repeat
image v14_anthony3_animation:
    "images/v14_anthony3a.webp" with short
    pause 1
    "images/v14_anthony3b.webp" with short
    pause 1
    repeat
image v14_anthony4a = Composite(
    (1920, 1080),
    (0, 0), "v14_anthony4a.webp",
    (0, 0), ConditionSwitch(
        "v14_anthony_massage_naked < 2 and lena_bikini == 1", 'v14_anthony4a_bk1.webp',
        "v14_anthony_massage_naked < 2 and lena_bikini == 2", 'v14_anthony4a_bk2.webp',
        "v14_anthony_massage_naked < 2 and lena_bikini == 3", 'v14_anthony4a_bk3.webp',
        "True", Null()),
)
image v14_anthony4b = Composite(
    (1920, 1080),
    (0, 0), "v14_anthony4b.webp",
    (0, 0), ConditionSwitch(
        "v14_anthony_massage_naked < 2 and lena_bikini == 1", 'v14_anthony4b_bk1.webp',
        "v14_anthony_massage_naked < 2 and lena_bikini == 2", 'v14_anthony4b_bk2.webp',
        "v14_anthony_massage_naked < 2 and lena_bikini == 3", 'v14_anthony4b_bk3.webp',
        "True", Null()),
)
image v14_anthony4_animation:
    "v14_anthony4a" with fps
    pause 0.7
    "v14_anthony4b" with fps
    pause 0.7
    repeat
image v14_anthony7a = Composite(
    (1920, 1080),
    (0, 0), "v14_anthony7a.webp",
    (0, 0), ConditionSwitch(
        "v14_anthony_massage_naked < 2 and lena_bikini == 1", 'v14_anthony7a_bk1.webp',
        "v14_anthony_massage_naked < 2 and lena_bikini == 2", 'v14_anthony7a_bk2.webp',
        "v14_anthony_massage_naked < 2 and lena_bikini == 3", 'v14_anthony7a_bk3.webp',
        "True", Null()),
)
image v14_anthony7b = Composite(
    (1920, 1080),
    (0, 0), "v14_anthony7b.webp",
    (0, 0), ConditionSwitch(
        "v14_anthony_massage_naked < 2 and lena_bikini == 1", 'v14_anthony7b_bk1.webp',
        "v14_anthony_massage_naked < 2 and lena_bikini == 2", 'v14_anthony7b_bk2.webp',
        "v14_anthony_massage_naked < 2 and lena_bikini == 3", 'v14_anthony7b_bk3.webp',
        "True", Null()),
)
image v14_anthony7_animation:
    "v14_anthony7b" with fps
    pause 0.7
    "v14_anthony7a" with fps
    pause 0.7
    repeat

image v14_anthony9a = Composite(
    (1920, 1080),
    (0, 0), "v14_anthony9a.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_anthony9a_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_anthony9a_t3.webp',
        "True", Null()),
)
image v14_anthony9b = Composite(
    (1920, 1080),
    (0, 0), "v14_anthony9b.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_anthony9b_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_anthony9b_t3.webp',
        "True", Null()),
)
image v14_anthony9_animation1:
    "v14_anthony9b" with fps
    pause 0.3
    "v14_anthony9a" with fps
    pause 0.4
    repeat
image v14_anthony9_animation2:
    "v14_anthony9b" with vpunch
    pause 0.3
    "v14_anthony9a" with fps
    pause 0.3
    repeat

image v14_anthony11a = Composite(
    (1920, 1080),
    (0, 0), "v14_anthony11a.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_anthony11a_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_anthony11a_t3.webp',
        "True", Null()),
)
image v14_anthony11b = Composite(
    (1920, 1080),
    (0, 0), "v14_anthony11b.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_anthony11b_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_anthony11b_t3.webp',
        "True", Null()),
)
image v14_anthony11c = Composite(
    (1920, 1080),
    (0, 0), "v14_anthony11c.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_anthony11c_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_anthony11c_t3.webp',
        "True", Null()),
)
image v14_anthony11_animation:
    "v14_anthony11b" with fps
    pause 0.2
    "v14_anthony11c" with vpunch
    pause 0.3
    "v14_anthony11b" with fps
    pause 0.2
    "v14_anthony11a" with fps
    pause 0.25
    repeat


image v14_ivy2_animation:
    "images/v14_ivy2c.webp" with short
    pause 0.8
    "images/v14_ivy2b.webp" with short
    pause 0.8
    repeat
image v14_billy8_lena1 = Composite(
    (1920, 1080),
    (0, 0), "v14_billy8_lena1.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_billy8_lena1_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_billy8_lena1_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_bikini == 2 and v14_billy_shoot < 2", 'v14_billy8_lena1_bk2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_bikini == 3 and v14_billy_shoot < 2", 'v14_billy8_lena1_bk3.webp',
        "True", Null()),
)
image v14_billy8_lena2 = Composite(
    (1920, 1080),
    (0, 0), "v14_billy8_lena2.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_billy8_lena2_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_billy8_lena2_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_bikini == 2 and v14_billy_shoot < 2", 'v14_billy8_lena2_bk2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_bikini == 3 and v14_billy_shoot < 2", 'v14_billy8_lena2_bk3.webp',
        "True", Null()),
)
image v14_billy8_lena3 = Composite(
    (1920, 1080),
    (0, 0), "v14_billy8_lena3.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_billy8_lena3_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_billy8_lena3_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_bikini == 2 and v14_billy_shoot < 2", 'v14_billy8_lena3_bk2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_bikini == 3 and v14_billy_shoot < 2", 'v14_billy8_lena3_bk3.webp',
        "True", Null()),
)
image v14_billy8_lena_animation1:
    "v14_billy8_lena1" with fps3
    pause 0.25
    "v14_billy8_lena2" with fps3
    pause 0.25
    repeat
image v14_billy8_lena_animation2:
    "v14_billy8_lena1" with fps3
    pause 0.25
    "v14_billy8_lena2" with fps3
    pause 0.25
    "v14_billy8_lena1" with fps3
    pause 0.2
    "v14_billy8_lena3" with fps3
    pause 0.28
    repeat

image v14_billy8_ivy_animation:
    "v14_billy8_ivy2" with fps3
    pause 0.2
    "v14_billy8_ivy3" with fps3
    pause 0.25
    "v14_billy8_ivy2" with fps3
    pause 0.15
    "v14_billy8_ivy1" with fps3
    pause 0.25
    repeat


image v14_jeremy1a = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy1_bg2.webp",
    (0, 0), ConditionSwitch(
        "v14_jeremy_sex and v14_3some_jeremy_mike == False", 'v14_jeremy1_bg1.webp',
        "True", Null()),
    (0, 0), "v14_jeremy1_lena.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy1_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy1_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_jeremy1_t2.webp',
        "True", Null()),
    (0, 0), "v14_jeremy1_j1.webp",
)
image v14_jeremy1b = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy1_bg2.webp",
    (0, 0), ConditionSwitch(
        "v14_jeremy_sex and v14_3some_jeremy_mike == False", 'v14_jeremy1_bg1.webp',
        "True", Null()),
    (0, 0), "v14_jeremy1_lena.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy1_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy1_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_jeremy1_t2.webp',
        "True", Null()),
    (0, 0), "v14_jeremy1_j2.webp",
)
image v14_jeremy1c = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy1_bg2.webp",
    (0, 0), ConditionSwitch(
        "v14_jeremy_sex and v14_3some_jeremy_mike == False", 'v14_jeremy1_bg1.webp',
        "True", Null()),
    (0, 0), "v14_jeremy1_lena.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy1_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy1_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_jeremy1_t2.webp',
        "True", Null()),
    (0, 0), "v14_jeremy1_j3.webp",
)
image v14_jeremy1d = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy1_bg2.webp",
    (0, 0), ConditionSwitch(
        "v14_jeremy_sex and v14_3some_jeremy_mike == False", 'v14_jeremy1_bg1.webp',
        "True", Null()),
    (0, 0), "v14_jeremy1_lena.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy1_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy1_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_jeremy1_t2.webp',
        "True", Null()),
    (0, 0), "v14_jeremy1_j4.webp",
)
image v14_jeremy1e = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy1_bg2.webp",
    (0, 0), ConditionSwitch(
        "v14_jeremy_sex and v14_3some_jeremy_mike == False", 'v14_jeremy1_bg1.webp',
        "True", Null()),
    (0, 0), "v14_jeremy1_lena.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy1_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy1_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_jeremy1_t2.webp',
        "True", Null()),
    (0, 0), "v14_jeremy1_j5.webp",
)
image v14_jeremy1f = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy1_bg2.webp",
    (0, 0), ConditionSwitch(
        "v14_jeremy_sex and v14_3some_jeremy_mike == False", 'v14_jeremy1_bg1.webp',
        "True", Null()),
    (0, 0), "v14_jeremy1_lena.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy1_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy1_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_jeremy1_t2.webp',
        "True", Null()),
    (0, 0), "v14_jeremy1_j6.webp",
)
image v14_jeremy1a_animation:
    "v14_jeremy1b" with fps
    pause 0.2
    "v14_jeremy1c" with fps
    pause 0.2
    "v14_jeremy1d" with fps
    pause 0.2
    "v14_jeremy1f" with fps
    pause 0.2
    "v14_jeremy1e" with fps
    pause 1

image v14_jeremy1a_ivy = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy1_bg2.webp",
    (0, 0), "v14_jeremy1_ivy.webp",
    (0, 0), "v14_jeremy1_j1.webp",
    (0, 0), "v14_jeremy1_j1_ivy.webp",
)
image v14_jeremy1b_ivy = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy1_bg2.webp",
    (0, 0), "v14_jeremy1_ivy.webp",
    (0, 0), "v14_jeremy1_j2.webp",
    (0, 0), "v14_jeremy1_j2_ivy.webp",
)
image v14_jeremy1c_ivy = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy1_bg2.webp",
    (0, 0), "v14_jeremy1_ivy.webp",
    (0, 0), "v14_jeremy1_j3.webp",
    (0, 0), "v14_jeremy1_j3_ivy.webp",
)
image v14_jeremy1d_ivy = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy1_bg2.webp",
    (0, 0), "v14_jeremy1_ivy.webp",
    (0, 0), "v14_jeremy1_j4.webp",
    (0, 0), "v14_jeremy1_j3_ivy.webp",
)
image v14_jeremy1e_ivy = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy1_bg2.webp",
    (0, 0), "v14_jeremy1_ivy.webp",
    (0, 0), "v14_jeremy1_j5.webp",
    (0, 0), "v14_jeremy1_j3_ivy.webp",
)
image v14_jeremy1f_ivy = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy1_bg2.webp",
    (0, 0), "v14_jeremy1_ivy.webp",
    (0, 0), "v14_jeremy1_j6.webp",
    (0, 0), "v14_jeremy1_j3_ivy.webp",
)

image v14_jeremy1c_animation:
    "v14_jeremy1b_ivy" with fps
    pause 0.2
    "v14_jeremy1c_ivy" with fps
    pause 0.2
    "v14_jeremy1d_ivy" with fps
    pause 0.2
    "v14_jeremy1f_ivy" with fps
    pause 0.2
    "v14_jeremy1e_ivy" with fps
    pause 1



image v14_jeremy5a = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy5a.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo4", 'v14_jeremy5a_t4.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy5a_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy5a_mk.webp',
        "True", Null()),
)
image v14_jeremy5b = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy5b.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo4", 'v14_jeremy5a_t4.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy5a_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy5b_mk.webp',
        "True", Null()),
)
image v14_jeremy5c = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy5c.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo4", 'v14_jeremy5a_t4.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy5a_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy5c_mk.webp',
        "True", Null()),
)
image v14_jeremy5d = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy5d.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo4", 'v14_jeremy5d_t4.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy5d_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy5d_mk.webp',
        "True", Null()),
)
image v14_jeremy5e = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy5e.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo4", 'v14_jeremy5e_t4.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy5e_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy5e_mk.webp',
        "True", Null()),
)
image v14_jeremy5f = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy5f.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo4", 'v14_jeremy5f_t4.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy5f_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy5f_mk.webp',
        "True", Null()),
)
image v14_jeremy5_animation1:
    "v14_jeremy5c" with fps
    pause 0.2
    "v14_jeremy5b" with fps
    pause 0.3
    "v14_jeremy5c" with fps
    pause 0.2
    "v14_jeremy5d" with fps
    pause 0.3
    repeat
image v14_jeremy5_animation2:
    "v14_jeremy5c" with fps
    pause 0.2
    "v14_jeremy5d" with fps
    pause 0.2
    "v14_jeremy5e" with fps
    pause 0.2
    "v14_jeremy5f" with vpunch
    pause 0.3
    "v14_jeremy5e" with fps
    pause 0.2
    "v14_jeremy5d" with fps
    pause 0.2
    "v14_jeremy5c" with fps
    pause 0.2
    "v14_jeremy5b" with fps
    pause 0.2
    repeat
image v14_jeremy5_animation2b:
    "v14_jeremy5c" with fps
    pause 0.1
    "v14_jeremy5d" with fps
    pause 0.1
    "v14_jeremy5e" with fps
    pause 0.1
    "v14_jeremy5f" with vpunch
    pause 0.25
    "v14_jeremy5e" with fps
    pause 0.1
    "v14_jeremy5d" with fps
    pause 0.1
    "v14_jeremy5c" with fps
    pause 0.1
    "v14_jeremy5b" with fps
    pause 0.2
    repeat
image v14_jeremy5_animation3:
    "v14_jeremy5c" with fps
    pause 0.2
    "v14_jeremy5d" with fps
    pause 0.2
    "v14_jeremy5e" with fps
    pause 0.3
    "v14_jeremy5d" with fps
    pause 0.2
    "v14_jeremy5c" with fps
    pause 0.2
    "v14_jeremy5b" with fps
    pause 0.2
    repeat
image v14_jeremy5_animation4:
    "v14_jeremy5c" with fps
    pause 0.3
    "v14_jeremy5b" with fps
    pause 0.4
    "v14_jeremy5c" with fps
    pause 0.3
    "v14_jeremy5d" with fps
    pause 0.4
    repeat
image v14_jeremy5_pullout:
    "v14_jeremy5e" with fps
    pause 0.5
    "v14_jeremy5d" with fps
    pause 0.2
    "v14_jeremy5c" with fps
    pause 0.2
    "v14_jeremy5b" with fps
    pause 0.2
    "v14_jeremy5a" with fps
    pause 0.4

image v14_jeremy12a = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy12a.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v11_bbc2a_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v11_bbc2a_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy12a_mk.webp',
        "True", Null()),
)
image v14_jeremy12b = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy12b.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v11_bbc2b_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v11_bbc2b_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy12b_mk.webp',
        "True", Null()),
)
image v14_jeremy12_animation:
    "v14_jeremy12a" with fps
    pause 0.6
    "v14_jeremy12b" with fps
    pause 0.5
    repeat


image v14_jeremy16a = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy16a.webp",
    (0, 0), ConditionSwitch(
        "v14_jeremy_anal", 'v14_jeremy16a_anal.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_jeremy16a_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_jeremy16a_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo4", 'v14_jeremy16a_t4.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy16a_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy16a_mk.webp',
        "True", Null()),
)
image v14_jeremy16b = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy16b.webp",
    (0, 0), ConditionSwitch(
        "v14_jeremy_anal", 'v14_jeremy16b_anal.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_jeremy16b_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_jeremy16b_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo4", 'v14_jeremy16b_t4.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy16b_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy16b_mk.webp',
        "True", Null()),
)
image v14_jeremy16c = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy16c.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_jeremy16c_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_jeremy16c_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo4", 'v14_jeremy16c_t4.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy16c_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy16c_mk.webp',
        "True", Null()),
)
image v14_jeremy16d = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy16d.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_jeremy16d_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_jeremy16d_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo4", 'v14_jeremy16d_t4.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy16d_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy16d_mk.webp',
        "True", Null()),
)
image v14_jeremy16_animation1:
    "v14_jeremy16b" with fps
    pause 0.2
    "v14_jeremy16c" with fps
    pause 0.3
image v14_jeremy16_animation2:
    "v14_jeremy16b" with fps
    pause 0.2
    "v14_jeremy16a" with fps
    pause 0.3
    "v14_jeremy16b" with fps
    pause 0.2
    "v14_jeremy16c" with fps
    pause 0.25
    repeat
image v14_jeremy16_animation3b:
    "v14_jeremy16a" with fps
    pause 0.3
    "v14_jeremy16b" with fps
    pause 0.2
    "v14_jeremy16c" with fps
    pause 0.2
    "v14_jeremy16d" with vpunch
    pause 0.3
    "v14_jeremy16c" with fps
    pause 0.2
    "v14_jeremy16b" with fps
    pause 0.2
    repeat
image v14_jeremy16_animation3a:
    "v14_jeremy16a" with fps
    pause 0.2
    "v14_jeremy16b" with fps
    pause 0.15
    "v14_jeremy16c" with fps
    pause 0.15
    "v14_jeremy16d" with vpunch
    pause 0.25
    "v14_jeremy16c" with fps
    pause 0.15
    "v14_jeremy16b" with fps
    pause 0.15
    repeat


image v14_jeremy17a = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy17a.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_anthony23a_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy17a_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_anthony23a_t2.webp',
        "True", Null()),
)
image v14_jeremy17b = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy17b.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy17b_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy17b_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_anthony23b_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v14_anthony23b_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v14_anthony23b_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v14_anthony23b_p2.webp',
        "True", Null()),
)
image v14_jeremy17c = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy17c.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy17c_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy17c_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_anthony23c_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v14_anthony23c_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v14_anthony23c_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v14_anthony23c_p2.webp',
        "True", Null()),
)
image v14_jeremy17d = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy17d.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_anthony23d_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy17d_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_anthony23b_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v14_anthony23b_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v14_anthony23b_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v14_anthony23b_p2.webp',
        "True", Null()),
)
image v14_jeremy17_animation:
    "v14_jeremy17d" with fps
    pause 0.2
    "v14_jeremy17a" with fps
    pause 0.3
    "v14_jeremy17b" with fps
    pause 0.2
    "v14_jeremy17c" with vpunch
    pause 0.3
    repeat


image v14_jeremy18 = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy18.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy18_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy18_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_jeremy18_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v14_jeremy18_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v14_jeremy18_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v14_jeremy18_p2.webp',
        "True", Null()),
)
image v14_jeremy18d = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy18d.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy18_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy18b_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy18b_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_jeremy18_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v14_jeremy18_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v14_jeremy18_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v14_jeremy18_p2.webp',
        "True", Null()),
)


image v14_jeremy19 = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy19.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy19_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy19_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_jeremy19_t2.webp',
        "True", Null()),
)
image v14_jeremy19b = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy19b.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy19b_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy19b_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_jeremy19b_t2.webp',
        "True", Null()),
)

image v14_jeremy19_animation1:
    "v14_jeremy19b" with fps
    pause 0.5
    "v14_jeremy19" with fps
    pause 0.6
    repeat
image v14_jeremy19_animation2:
    "v14_jeremy19b" with fps
    pause 0.4
    "v14_jeremy19" with fps
    pause 0.45
    repeat


image v14_jeremy14a = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy14a.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_jeremy14a_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_jeremy14a_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo4", 'v14_jeremy14a_t4.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy14a_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v14_3some_jeremy_mike", 'v14_jeremy14a_mike.webp',
        "True", Null()),
)
image v14_jeremy14b = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy14b.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_jeremy14b_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_jeremy14b_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo4", 'v14_jeremy14b_t4.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy14b_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v14_3some_jeremy_mike", 'v14_jeremy14b_mike.webp',
        "True", Null()),
)
image v14_jeremy14c = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy14c.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_jeremy14c_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_jeremy14c_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo4", 'v14_jeremy14c_t4.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy14c_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v14_3some_jeremy_mike", 'v14_jeremy14c_mike.webp',
        "True", Null()),
)
image v14_jeremy14_animation:
    "v14_jeremy14a" with fps
    pause 0.3
    "v14_jeremy14b" with fps
    pause 0.2
    "v14_jeremy14c" with fps
    pause 0.3
    "v14_jeremy14b" with fps
    pause 0.2
    repeat

image v14_jeremy15c = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy15c.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy15c_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy15c_mk.webp',
        "True", Null()),
)
image v14_jeremy15d = Composite(
    (1920, 1080),
    (0, 0), "v14_jeremy15d.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_jeremy15d_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_jeremy15d_mk.webp',
        "True", Null()),
)
image v14_jeremy15c_animation:
    "v14_jeremy15d" with fps
    pause 0.5
    "v14_jeremy15c" with fps
    pause 0.3
    repeat

image v14_mike3 = Composite(
    (1920, 1080),
    (0, 0), "v14_mike3.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_mike3_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_mike3_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_mike3_makeup.webp',
        "True", Null()),
)
image v14_mike4 = Composite(
    (1920, 1080),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_mike4_makeup.webp',
        "lena_makeup != 'z'", 'v14_mike4.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_mike4_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_mike4_t3.webp',
        "True", Null()),
)
image v14_mike4b = Composite(
    (1920, 1080),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_mike4b_makeup.webp',
        "lena_makeup != 'z'", 'v14_mike4b.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_mike4_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_mike4_t3.webp',
        "True", Null()),
)
image v14_mike5 = Composite(
    (1920, 1080),
    (0, 0), "v14_mike5.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_mike5_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_mike5_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_mike5_makeup.webp',
        "True", Null()),
)
image v14_mike3_animation:
    "v14_mike4b" with fps
    pause 0.5
    "v14_mike3" with short
    pause 0.4
    repeat
image v14_mike3_animation2:
    "v14_mike4b" with vpunch
    pause 0.5
    "v14_mike3" with short
    pause 0.4
    repeat

image v14_mike14 = Composite(
    (1920, 1080),
    (0, 0), "v14_mike14.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_mike14_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_mike14_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_mike14_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_mike14_mk.webp',
        "True", Null()),
)
image v14_mike15 = Composite(
    (1920, 1080),
    (0, 0), "v14_mike15.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_mike14_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_mike14_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_mike14_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_mike15_mk.webp',
        "True", Null()),
)
image v14_mike16 = Composite(
    (1920, 1080),
    (0, 0), "v14_mike16.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_mike16_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_mike16_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_mike16_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_mike16_mk.webp',
        "True", Null()),
)
image v14_mike17 = Composite(
    (1920, 1080),
    (0, 0), "v14_mike17.webp",
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_mike16_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo3", 'v14_mike16_t3.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_mike17_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_mike17_mk.webp',
        "True", Null()),
)
image v14_mike14_animation:
    "v14_mike16" with fps
    pause 0.3
    "v14_mike17" with hpunch
    pause 0.4
    "v14_mike16" with fps
    pause 0.3
    "v14_mike15" with fps
    pause 0.4
    repeat
image v14_mike14_animation2:
    "v14_mike16" with fps
    pause 0.2
    "v14_mike17" with hpunch
    pause 0.3
    "v14_mike16" with fps
    pause 0.2
    "v14_mike15" with fps
    pause 0.35
    repeat
image v14_mike19a = Composite(
    (1920, 1080),
    (0, 0), "v14_mike19a.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_mike19a_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_mike19a_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_anthony23a_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v14_mike19a_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v14_mike19a_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v14_mike19a_p2.webp',
        "True", Null()),
)
image v14_mike19aa = Composite(
    (1920, 1080),
    (0, 0), "v14_mike19a.webp",
    (0, 0), "v14_mike19a_f2.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_mike19a_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_mike19a_f2_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_anthony23a_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v14_mike19a_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v14_mike19a_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v14_mike19a_p2.webp',
        "True", Null()),
)
image v14_mike19b = Composite(
    (1920, 1080),
    (0, 0), "v14_mike19b.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_mike19b_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_mike19b_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_anthony23b_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v14_anthony23b_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v14_anthony23b_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v14_anthony23b_p2.webp',
        "True", Null()),
)
image v14_mike19c = Composite(
    (1920, 1080),
    (0, 0), "v14_mike19c.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_mike19c_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_mike19c_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_anthony23c_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v14_anthony23c_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v14_anthony23c_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v14_anthony23c_p2.webp',
        "True", Null()),
)
image v14_mike19cc = Composite(
    (1920, 1080),
    (0, 0), "v14_mike19c.webp",
    (0, 0),'v14_mike19c_f2.webp',
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_mike19c_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_mike19c_f2_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_anthony23c_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v14_anthony23c_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v14_anthony23c_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v14_anthony23c_p2.webp',
        "True", Null()),
)
image v14_mike19d = Composite(
    (1920, 1080),
    (0, 0), "v14_mike19d.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_mike19d_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_mike19d_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_anthony23b_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v14_anthony23b_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v14_anthony23b_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v14_anthony23b_p2.webp',
        "True", Null()),
)
image v14_mike19dd = Composite(
    (1920, 1080),
    (0, 0), "v14_mike19d.webp",
    (0, 0), "v14_mike19d_f1.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_mike19d_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_mike19d_f1_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_anthony23b_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v14_anthony23b_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v14_anthony23b_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v14_anthony23b_p2.webp',
        "True", Null()),
)
image v14_mike19_animation0:
    "v14_mike19b" with fps
    pause 0.2
    "v14_mike19cc" with vpunch
    pause 0.3
image v14_mike19_animation1:
    "v14_mike19dd" with fps
    pause 0.2
    "v14_mike19a" with fps
    pause 0.3
    "v14_mike19b" with fps
    pause 0.2
    "v14_mike19cc" with vpunch
    pause 0.3
    repeat
image v14_mike19_animation2:
    "v14_mike19d" with fps
    pause 0.15
    "v14_mike19aa" with fps
    pause 0.20
    "v14_mike19b" with fps
    pause 0.15
    "v14_mike19c" with vpunch
    pause 0.25
    repeat


image v14_mike24 = Composite(
    (1920, 1080),
    (0, 0), ConditionSwitch(
        "v14_3some_jeremy_mike", 'v14_mike24_j1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v14_3some_jeremy_mike == False", 'v14_mike24.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v14_3some_jeremy_mike", 'v14_mike24_f1_j.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v14_3some_jeremy_mike == False", 'v14_mike24_f1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_mike24_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2' and v14_3some_jeremy_mike == False", 'v14_mike24_f1_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2' and v14_3some_jeremy_mike", 'v14_mike24_f1_choker_j.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z' and v14_3some_jeremy_mike == False", 'v14_mike24_f1_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z' and v14_3some_jeremy_mike", 'v14_mike24_f1_mk_j.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_mike24_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v14_mike24_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo4", 'v14_mike24_t4.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v14_mike24_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v14_mike24_p2.webp',
        "True", Null()),
)
image v14_mike24b = Composite(
    (1920, 1080),
    (0, 0), ConditionSwitch(
        "v14_3some_jeremy_mike", 'v14_mike24_j2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v14_3some_jeremy_mike == False", 'v14_mike24.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v14_3some_jeremy_mike", 'v14_mike24_f1_j.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "v14_3some_jeremy_mike == False", 'v14_mike24_f1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_mike24_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2' and v14_3some_jeremy_mike == False", 'v14_mike24_f1_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2' and v14_3some_jeremy_mike", 'v14_mike24_f1_choker_j.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z' and v14_3some_jeremy_mike == False", 'v14_mike24_f1_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z' and v14_3some_jeremy_mike", 'v14_mike24_f1_mk_j.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_mike24_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v14_mike24_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo4", 'v14_mike24_t4.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v14_mike24_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v14_mike24_p2.webp',
        "True", Null()),
)
image v14_mike24_animation:
    "v14_mike24b" with fps
    pause 0.4
    "v14_mike24" with fps
    pause 0.4
    repeat



image v14_anthony17a = Composite(
    (1920, 1080),
    (0, 0), "v14_anthony17a.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_anthony17a_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_anthony17a_mk.webp',
        "True", Null()),
)
image v14_anthony17b = Composite(
    (1920, 1080),
    (0, 0), "v14_anthony17b.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_anthony17b_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_anthony17b_mk.webp',
        "True", Null()),
)
image v14_anthony17c = Composite(
    (1920, 1080),
    (0, 0), "v14_anthony17c.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_anthony17c_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_anthony17c_mk.webp',
        "True", Null()),
)
image v14_anthony17d = Composite(
    (1920, 1080),
    (0, 0), "v14_anthony17d.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_anthony17d_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_anthony17d_mk.webp',
        "True", Null()),
)
image v14_anthony17_animation1:
    "v14_anthony17b" with fps
    pause 0.2
    "v14_anthony17d" with vpunch
    pause 0.3
    "v14_anthony17c" with fps
    pause 0.2
    "v14_anthony17b" with fps
    pause 0.2
    "v14_anthony17a" with fps
    pause 0.35
    repeat
image v14_anthony17_animation2:
    "v14_anthony17d" with vpunch
    pause 0.25
    "v14_anthony17c" with fps
    pause 0.15
    "v14_anthony17b" with fps
    pause 0.15
    "v14_anthony17a" with fps
    pause 0.20
    "v14_anthony17b" with fps
    pause 0.15
    repeat

image v14_anthony23a = Composite(
    (1920, 1080),
    (0, 0), "v14_anthony23a.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_anthony23a_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_anthony23a_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_anthony23a_t2.webp',
        "True", Null()),
)
image v14_anthony23b = Composite(
    (1920, 1080),
    (0, 0), "v14_anthony23b.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_anthony23b_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_anthony23b_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_anthony23b_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v14_anthony23b_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v14_anthony23b_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v14_anthony23b_p2.webp',
        "True", Null()),
)
image v14_anthony23c = Composite(
    (1920, 1080),
    (0, 0), "v14_anthony23c.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_anthony23c_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_anthony23c_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_anthony23c_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v14_anthony23c_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v14_anthony23c_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v14_anthony23c_p2.webp',
        "True", Null()),
)
image v14_anthony23d = Composite(
    (1920, 1080),
    (0, 0), "v14_anthony23d.webp",
    (0, 0), ConditionSwitch(
        "lena_necklace == 'choker2'", 'v14_anthony23d_choker.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_makeup == 'z'", 'v14_anthony23d_mk.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo2", 'v14_anthony23b_t2.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_tattoo1", 'v14_anthony23b_t1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing1", 'v14_anthony23b_p1.webp',
        "True", Null()),
    (0, 0), ConditionSwitch(
        "lena_piercing2", 'v14_anthony23b_p2.webp',
        "True", Null()),
)
image v14_anthony23_animation0:
    "v14_anthony23b" with fps
    pause 0.2
    "v14_anthony23c" with vpunch
    pause 0.3

image v14_anthony23_animation:
    "v14_anthony23d" with fps
    pause 0.2
    "v14_anthony23a" with fps
    pause 0.3
    "v14_anthony23b" with fps
    pause 0.2
    "v14_anthony23c" with vpunch
    pause 0.3
    repeat


transform transf_ch14_bg_camera_up(yalign=0.25):
    subpixel True
    zoom 2.0
    align (0.5, 1.0)
    ease 5 yalign yalign


transform transf_ch14_camera_up(xoffset=0, yalign=-0.05):
    subpixel True
    align (0.5, 1.0)
    xoffset xoffset
    ease 5 yalign yalign

transform transf_ch14_group(xoffset=0, yoffset=0):
    zoom 0.56
    align (0.5, 1.0)
    xoffset xoffset
    yoffset yoffset

transform transf_ch14_pose(xoffset=0, yoffset=0):
    zoom 1.6
    align (0.5, 1.0)



image v14_test2:
    "images/z1.png" with fps
    pause 0.3
    "images/z2.png" with fps
    pause 0.25
    "images/z3.png" with vpunch
    pause 0.35
    "images/z4.png" with fps
    pause 0.25
    repeat

image v14_test3:
    "images/z5.png" with fps
    pause 0.2
    "images/z6.png" with fps
    pause 0.25
    "images/z7.png" with fps
    pause 0.2
    repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
