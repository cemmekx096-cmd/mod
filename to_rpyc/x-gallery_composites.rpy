







image gall_lena = Composite(
    (640, 1080),
    (0, 0),"lenanude.webp", 
    (0, 0), ConditionSwitch( 
        "lena_piercing1 == True", "lena_navel1.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_piercing2 == True", "lena_navel2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_tattoo1 == True", "lena_tattoo1.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_tattoo2 == True", "lena_tattoo2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_tattoo3 == True", "lena_tattoo3.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "gall_lena_look == 1", "lena1.webp",
        "gall_lena_look == 2", "lenagym.webp",
        "gall_lena_look == 3", "lenadress1.webp",
        "gall_lena_look == 'sexy'", "lena_sexy.webp",
        "gall_lena_look == 'sexy1'", "lena_sexy1.webp",
        "gall_lena_look == 'charisma'", "lena_charisma1.webp",
        "gall_lena_look == 'wits'", "lena_wits1.webp",
        "gall_lena_look == 'athletics'", "lena_athletics1.webp",
        "gall_lena_look == 'lust'", "lena_lust1.webp",
        "gall_lena_look == 'towel'", "lena_towel.webp",
        "gall_lena_look == 'summer'", "lena_summer.webp",
        "gall_lena_look == 4", "lenacasual.webp",
        "gall_lena_look == 'black_dress'", "lena_dress_posh1.webp",
        "gall_lena_look == 'clubdress' and v11_lena_dress == 1", "lenadress_wits.webp",
        "gall_lena_look == 'clubdress' and v11_lena_dress == 2", "lenadress_charisma.webp",
        "gall_lena_look == 'clubdress' and v11_lena_dress == 3", "lenadress_athletics.webp",
        "gall_lena_look == 'clubdress' and v11_lena_dress == 4", "lenadress_lust.webp",
        "gall_lena_look == 'bikini' and lena_bikini == 1", "lenabikini1.webp",
        "gall_lena_look == 'bikini' and lena_bikini == 2", "lenabikini2.webp",
        "gall_lena_look == 'bikini' and lena_bikini == 3", "lenabikini3.webp",
        "True", "lena1.webp"
    ),
    (0, 0), ConditionSwitch( 
        "gall_flena == 'sad'", "lenasad.webp",
        "gall_flena == 'crazy'", "lenacrazy.webp",
        "gall_flena == 'crazyserious'", "lenacrazyserious.webp",
        "gall_flena == 'crazysmile'", "lenacrazysmile.webp",
        "gall_flena == 'blush'", "lenablush.webp",
        "gall_flena == 'cry'", "lenacry.webp",
        "gall_flena == 'drama'", "lenadrama.webp",
        "gall_flena == 'evil'", "lenaevil.webp",
        "gall_flena == 'flirt'", "lenaflirt.webp",
        "gall_flena == 'flirtevil'", "lenaflirtevil.webp",
        "gall_flena == 'flirtshy'", "lenaflirtshy.webp",
        "gall_flena == 'happy'", "lenahappy.webp",
        "gall_flena == 'mad'", "lenamad.webp",
        "gall_flena == 'serious'", "lenaserious.webp",
        "gall_flena == 'shy'", "lenashy.webp",
        "gall_flena == 'slut'", "lenaslut.webp",
        "gall_flena == 'slutshy'", "lenaslutshy.webp",
        "gall_flena == 'smile'", "lenasmile.webp",
        "gall_flena == 'surprise'", "lenasurprise.webp",
        "gall_flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp"
    )
)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
