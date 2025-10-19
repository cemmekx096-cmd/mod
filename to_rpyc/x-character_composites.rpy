







image lena = Composite(
    (640, 1080),
    (0, 0),"lenanude.webp", 
    (0, 0), ConditionSwitch( 
        "lena_makeup == 1", "lena_eyeshadow1.webp",
        "lena_makeup == 2", "lena_eyeshadow2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_necklace == 'choker2'", "lena_choker2.webp", 
        "lena_necklace == 'choker'", "lena_choker.webp",
        "lena_necklace == 'seymour'", "lena_sy_collar.webp",
        "lena_necklace == 'seymour2'", "lena_sy_collar2.webp",
        "lena_necklace == 'seymour3'", "lena_sy_collar3.webp",
        "lena_necklace == 'gift'", "lena_giftnecklace.webp",
        "lena_necklace == 'gift2'", "lena_giftnecklace2.webp", 
        "True", Null()
    ),
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
        "lena_extras == 'stockings'", "lena_lust1_stockings.webp",
        "True", Null()
    ),
    
    (0, 0), ConditionSwitch( 
        "lena_look == 'black_dress'", "lena_dress_posh_thigh.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_extras == 'black_dress'", "lena_dress_posh_bag.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 'black_dress'", "lenamoon.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 1", "lena1.webp",
        "lena_look == 2", "lenagym.webp",
        "lena_look == 3", "lenadress1.webp",
        "lena_look == 'sexy'", "lena_sexy.webp",
        "lena_look == 'sexy1'", "lena_sexy1.webp",
        "lena_look == 'charisma'", "lena_charisma1.webp",
        "lena_look == 'wits'", "lena_wits1.webp",
        "lena_look == 'athletics'", "lena_athletics1.webp",
        "lena_look == 'lust'", "lena_lust1.webp",
        "lena_look == 'towel'", "lena_towel.webp",
        "lena_look == 'summer'", "lena_summer.webp",
        "lena_look == 4", "lenacasual.webp",
        "lena_look == 'black_dress'", "lena_dress_posh1.webp",
        "lena_look == 'clubdress' and v11_lena_dress == 1", "lenadress_wits.webp",
        "lena_look == 'clubdress' and v11_lena_dress == 2", "lenadress_charisma.webp",
        "lena_look == 'clubdress' and v11_lena_dress == 3", "lenadress_athletics.webp",
        "lena_look == 'clubdress' and v11_lena_dress == 4", "lenadress_lust.webp",
        "lena_look == 'bikini' and lena_bikini == 1", "lenabikini1.webp",
        "lena_look == 'bikini' and lena_bikini == 2", "lenabikini2.webp",
        "lena_look == 'bikini' and lena_bikini == 3", "lenabikini3.webp",
        "lena_look == 'nymph'", "lena_nymph.webp",
        "lena_look == 'nymph2'", "lena_nymphb.webp",

        "lena_look == 'summer2' and lena_bikini == 1", "lenabikini1b.webp",
        "lena_look == 'summer2' and lena_bikini == 2", "lenabikini2b.webp",
        "lena_look == 'summer2' and lena_bikini == 3", "lenabikini3aa.webp",

        "lena_look == 'lingerie2b'", "lena_lingerie2b.webp",
        "lena_look == 'lingerie2w'", "lena_lingerie2w.webp",
        "lena_look == 'comfystan' and lena_lust > 7", "lena_comfyb.webp",
        "lena_look == 'comfystan' and lena_lust < 8", "lena_comfya.webp",
        "True", "lena1.webp"
    ),
    (0, 0), ConditionSwitch( 
        "lena_extras == 'nymph_shorts'", "lena_jeanshorts.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "flena == 'sad' and lena_makeup == 'z'", "lenasad_mk.webp",
        "flena == 'crazy' and lena_makeup == 'z'", "lenacrazy_mk.webp",
        "flena == 'crazyslut' and lena_makeup == 'z'", "lenacrazyslut_mk.webp",
        "flena == 'crazyserious' and lena_makeup == 'z'", "lenacrazyserious_mk.webp",
        "flena == 'crazysmile' and lena_makeup == 'z'", "lenacrazysmile_mk.webp",
        "flena == 'blush' and lena_makeup == 'z'", "lenablush_mk.webp",
        "flena == 'cry' and lena_makeup == 'z'", "lenacry_mk.webp",
        "flena == 'drama' and lena_makeup == 'z'", "lenadrama_mk.webp",
        "flena == 'evil' and lena_makeup == 'z'", "lenaevil_mk.webp",
        "flena == 'flirt' and lena_makeup == 'z'", "lenaflirt_mk.webp",
        "flena == 'flirtevil' and lena_makeup == 'z'", "lenaflirtevil_mk.webp",
        "flena == 'flirtshy' and lena_makeup == 'z'", "lenaflirtshy_mk.webp",
        "flena == 'happy' and lena_makeup == 'z'", "lenahappy_mk.webp",
        "flena == 'mad' and lena_makeup == 'z'", "lenamad_mk.webp",
        "flena == 'serious' and lena_makeup == 'z'", "lenaserious_mk.webp",
        "flena == 'shy' and lena_makeup == 'z'", "lenashy_mk.webp",
        "flena == 'slut' and lena_makeup == 'z'", "lenaslut_mk.webp",
        "flena == 'slutshy' and lena_makeup == 'z'", "lenaslutshy_mk.webp",
        "flena == 'smile' and lena_makeup == 'z'", "lenasmile_mk.webp",
        "flena == 'surprise' and lena_makeup == 'z'", "lenasurprise_mk.webp",
        "flena == 'worried' and lena_makeup == 'z'", "lenaworried_mk.webp",
        "flena == 'n' and lena_makeup == 'z'", "lena_mk.webp",
        "flena == 'sad'", "lenasad.webp",
        "flena == 'crazy'", "lenacrazy.webp",
        "flena == 'crazyslut'", "lenacrazyslut.webp",
        "flena == 'crazyserious'", "lenacrazyserious.webp",
        "flena == 'crazysmile'", "lenacrazysmile.webp",
        "flena == 'blush'", "lenablush.webp",
        "flena == 'cry'", "lenacry.webp",
        "flena == 'drama'", "lenadrama.webp",
        "flena == 'evil'", "lenaevil.webp",
        "flena == 'flirt'", "lenaflirt.webp",
        "flena == 'flirtevil'", "lenaflirtevil.webp",
        "flena == 'flirtshy'", "lenaflirtshy.webp",
        "flena == 'happy'", "lenahappy.webp",
        "flena == 'mad'", "lenamad.webp",
        "flena == 'serious'", "lenaserious.webp",
        "flena == 'shy'", "lenashy.webp",
        "flena == 'slut'", "lenaslut.webp",
        "flena == 'slutshy'", "lenaslutshy.webp",
        "flena == 'smile'", "lenasmile.webp",
        "flena == 'surprise'", "lenasurprise.webp",
        "flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp"
    )
)

image lena2 = Composite(
    (640, 1080),
    (0, 0),"lenanude_b.webp", 
    (0, 0), ConditionSwitch( 
        "lena_makeup == 1", "lena_eyeshadow1.webp",
        "lena_makeup == 2", "lena_eyeshadow2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_necklace == 'choker'", "lena_choker.webp",
        "lena_necklace == 'choker2'", "lena_choker2.webp",
        "lena_necklace == 'seymour'", "lena_sy_collar.webp",
        "lena_necklace == 'seymour2'", "lena_sy_collar2.webp",
        "lena_necklace == 'seymour3'", "lena_sy_collar3.webp",
        "lena_necklace == 'gift'", "lena_giftnecklace.webp",
        "lena_necklace == 'gift2'", "lena_giftnecklace2.webp", 
        "True", Null()
    ),
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
        "lena_extras == 'stockings'", "lena_lust1_stockings.webp",
        "True", Null()
    ),
    
    (0, 0), ConditionSwitch( 
        "lena_look == 'black_dress'", "lena_dress_posh_thigh.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 'black_dress'", "lenamoon.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 1", "lena1_b.webp",
        "lena_look == 2", "lenagym_b.webp",
        "lena_look == 3", "lenadress2.webp",
        "lena_look == 'sexy'", "lena_sexy_b.webp",
        "lena_look == 'sexy1'", "lena_sexy1_b.webp",
        "lena_look == 'charisma'", "lena_charisma1b.webp",
        "lena_look == 'wits'", "lena_wits1b.webp",
        "lena_look == 'athletics'", "lena_athletics1b.webp",
        "lena_look == 'lust'", "lena_lust1b.webp",
        "lena_look == 'towel'", "lena_towel.webp",
        "lena_look == 'summer'", "lena_summer_b.webp",
        "lena_look == 4", "lenacasual_b.webp",
        "lena_look == 'black_dress'", "lena_dress_posh2.webp",
        "lena_look == 'clubdress' and v11_lena_dress == 1", "lenadress_wits2.webp",
        "lena_look == 'clubdress' and v11_lena_dress == 2", "lenadress_charisma2.webp",
        "lena_look == 'clubdress' and v11_lena_dress == 3", "lenadress_athletics2.webp",
        "lena_look == 'clubdress' and v11_lena_dress == 4", "lenadress_lust2.webp",
        "lena_look == 'bikini' and lena_bikini == 1", "lenabikini1.webp",
        "lena_look == 'bikini' and lena_bikini == 2", "lenabikini2.webp",
        "lena_look == 'bikini' and lena_bikini == 3", "lenabikini3.webp",
        "lena_look == 'nymph'", "lena_nymph.webp",
        "lena_look == 'nymph2'", "lena_nymphb.webp",

        "lena_look == 'summer2' and lena_bikini == 1", "lenabikini1b2.webp",
        "lena_look == 'summer2' and lena_bikini == 2", "lenabikini2b2.webp",
        "lena_look == 'summer2' and lena_bikini == 3", "lenabikini3aa2.webp",

        "lena_look == 'lingerie2b'", "lena_lingerie2b.webp",
        "lena_look == 'lingerie2w'", "lena_lingerie2w.webp",
        "lena_look == 'comfystan' and lena_lust > 7", "lena_comfyb2.webp",
        "lena_look == 'comfystan' and lena_lust < 8", "lena_comfya2.webp",
        "True", "lena1_b.webp",
    ),
    (0, 0), ConditionSwitch( 
        "lena_extras == 'nymph_shorts'", "lena_jeanshorts_b.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "flena == 'sad' and lena_makeup == 'z'", "lenasad_mk.webp",
        "flena == 'crazy' and lena_makeup == 'z'", "lenacrazy_mk.webp",
        "flena == 'crazyslut' and lena_makeup == 'z'", "lenacrazyslut_mk.webp",
        "flena == 'crazyserious' and lena_makeup == 'z'", "lenacrazyserious_mk.webp",
        "flena == 'crazysmile' and lena_makeup == 'z'", "lenacrazysmile_mk.webp",
        "flena == 'blush' and lena_makeup == 'z'", "lenablush_mk.webp",
        "flena == 'cry' and lena_makeup == 'z'", "lenacry_mk.webp",
        "flena == 'drama' and lena_makeup == 'z'", "lenadrama_mk.webp",
        "flena == 'evil' and lena_makeup == 'z'", "lenaevil_mk.webp",
        "flena == 'flirt' and lena_makeup == 'z'", "lenaflirt_mk.webp",
        "flena == 'flirtevil' and lena_makeup == 'z'", "lenaflirtevil_mk.webp",
        "flena == 'flirtshy' and lena_makeup == 'z'", "lenaflirtshy_mk.webp",
        "flena == 'happy' and lena_makeup == 'z'", "lenahappy_mk.webp",
        "flena == 'mad' and lena_makeup == 'z'", "lenamad_mk.webp",
        "flena == 'serious' and lena_makeup == 'z'", "lenaserious_mk.webp",
        "flena == 'shy' and lena_makeup == 'z'", "lenashy_mk.webp",
        "flena == 'slut' and lena_makeup == 'z'", "lenaslut_mk.webp",
        "flena == 'slutshy' and lena_makeup == 'z'", "lenaslutshy_mk.webp",
        "flena == 'smile' and lena_makeup == 'z'", "lenasmile_mk.webp",
        "flena == 'surprise' and lena_makeup == 'z'", "lenasurprise_mk.webp",
        "flena == 'worried' and lena_makeup == 'z'", "lenaworried_mk.webp",
        "flena == 'n' and lena_makeup == 'z'", "lena_mk.webp",
        "flena == 'sad'", "lenasad.webp",
        "flena == 'crazy'", "lenacrazy.webp",
        "flena == 'crazyslut'", "lenacrazyslut.webp",
        "flena == 'crazyserious'", "lenacrazyserious.webp",
        "flena == 'crazysmile'", "lenacrazysmile.webp",
        "flena == 'blush'", "lenablush.webp",
        "flena == 'cry'", "lenacry.webp",
        "flena == 'drama'", "lenadrama.webp",
        "flena == 'evil'", "lenaevil.webp",
        "flena == 'flirt'", "lenaflirt.webp",
        "flena == 'flirtevil'", "lenaflirtevil.webp",
        "flena == 'flirtshy'", "lenaflirtshy.webp",
        "flena == 'happy'", "lenahappy.webp",
        "flena == 'mad'", "lenamad.webp",
        "flena == 'serious'", "lenaserious.webp",
        "flena == 'shy'", "lenashy.webp",
        "flena == 'slut'", "lenaslut.webp",
        "flena == 'slutshy'", "lenaslutshy.webp",
        "flena == 'smile'", "lenasmile.webp",
        "flena == 'surprise'", "lenasurprise.webp",
        "flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp")
    )

image lena_phone = Composite(
    (640, 1080),
    (0, 0),"lenanude_phone.webp", 
    (0, 0), ConditionSwitch( 
        "lena_makeup == 1", "lena_eyeshadow1.webp",
        "lena_makeup == 2", "lena_eyeshadow2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_necklace == 'choker'", "lena_choker.webp",
        "lena_necklace == 'choker2'", "lena_choker2.webp",
        "lena_necklace == 'seymour'", "lena_sy_collar.webp",
        "lena_necklace == 'seymour2'", "lena_sy_collar2.webp",
        "lena_necklace == 'seymour3'", "lena_sy_collar3.webp",
        "lena_necklace == 'gift'", "lena_giftnecklace.webp",
        "lena_necklace == 'gift2'", "lena_giftnecklace2.webp", 
        "True", Null()
    ),
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
        "lena_extras == 'stockings'", "lena_lust1_stockings.webp",
        "True", Null()
    ),
    
    (0, 0), ConditionSwitch( 
        "lena_look == 'black_dress'", "lena_dress_posh_thigh.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 'black_dress'", "lenamoon.webp",
        "True", Null()
    ),
    
    (0, 0), ConditionSwitch( 
        "lena_look == 1", "lena1_phone.webp",
        "lena_look == 2", "lenagym_phone.webp",
        "lena_look == 3", "lenadress1_phone.webp",
        "lena_look == 'sexy'", "lena_sexy_phone.webp",
        "lena_look == 'sexy1'", "lena_sexy1_phone.webp",
        "lena_look == 'charisma'", "lena_charisma1_phone.webp",
        "lena_look == 'wits'", "lena_wits1_phone.webp",
        "lena_look == 'athletics'", "lena_athletics1_phone.webp",
        "lena_look == 'lust'", "lena_lust1_phone.webp",
        "lena_look == 'summer'", "lena_summer_phone.webp",
        "lena_look == 4", "lenacasual_phone.webp",
        "lena_look == 'black_dress'", "lena_dress_posh3.webp",
        "lena_look == 'clubdress' and v11_lena_dress == 1", "lenadress_wits_phone.webp",
        "lena_look == 'clubdress' and v11_lena_dress == 2", "lenadress_charisma_phone.webp",
        "lena_look == 'clubdress' and v11_lena_dress == 3", "lenadress_athletics_phone.webp",
        "lena_look == 'clubdress' and v11_lena_dress == 4", "lenadress_lust_phone.webp",
        "lena_look == 'bikini' and lena_bikini == 1", "lenabikini1_phone.webp",
        "lena_look == 'bikini' and lena_bikini == 2", "lenabikini2_phone.webp",
        "lena_look == 'bikini' and lena_bikini == 3", "lenabikini3_phone.webp",

        "lena_look == 'summer2' and lena_bikini == 1", "lenabikini1b_phone.webp",
        "lena_look == 'summer2' and lena_bikini == 2", "lenabikini2b_phone.webp",
        "lena_look == 'summer2' and lena_bikini == 3", "lenabikini3aa_phone.webp",
        "lena_look == 'nymph'", "lena_nymph_smoke.webp",

        "lena_look == 'lingerie2b'", "lena_lingerie2b.webp",
        "lena_look == 'lingerie2w'", "lena_lingerie2w.webp",
        "lena_look == 'comfystan' and lena_lust > 7", "lena_comfyb_phone.webp",
        "lena_look == 'comfystan' and lena_lust < 8", "lena_comfya_phone.webp",
        "True", "lena1_phone.webp"
    ),
    (0, 0), ConditionSwitch( 
        "lena_extras == 'nymph_shorts'", "lena_jeanshorts.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "flena == 'sad' and lena_makeup == 'z'", "lenasad_mk.webp",
        "flena == 'crazy' and lena_makeup == 'z'", "lenacrazy_mk.webp",
        "flena == 'crazyslut' and lena_makeup == 'z'", "lenacrazyslut_mk.webp",
        "flena == 'crazyserious' and lena_makeup == 'z'", "lenacrazyserious_mk.webp",
        "flena == 'crazysmile' and lena_makeup == 'z'", "lenacrazysmile_mk.webp",
        "flena == 'blush' and lena_makeup == 'z'", "lenablush_mk.webp",
        "flena == 'cry' and lena_makeup == 'z'", "lenacry_mk.webp",
        "flena == 'drama' and lena_makeup == 'z'", "lenadrama_mk.webp",
        "flena == 'evil' and lena_makeup == 'z'", "lenaevil_mk.webp",
        "flena == 'flirt' and lena_makeup == 'z'", "lenaflirt_mk.webp",
        "flena == 'flirtevil' and lena_makeup == 'z'", "lenaflirtevil_mk.webp",
        "flena == 'flirtshy' and lena_makeup == 'z'", "lenaflirtshy_mk.webp",
        "flena == 'happy' and lena_makeup == 'z'", "lenahappy_mk.webp",
        "flena == 'mad' and lena_makeup == 'z'", "lenamad_mk.webp",
        "flena == 'serious' and lena_makeup == 'z'", "lenaserious_mk.webp",
        "flena == 'shy' and lena_makeup == 'z'", "lenashy_mk.webp",
        "flena == 'slut' and lena_makeup == 'z'", "lenaslut_mk.webp",
        "flena == 'slutshy' and lena_makeup == 'z'", "lenaslutshy_mk.webp",
        "flena == 'smile' and lena_makeup == 'z'", "lenasmile_mk.webp",
        "flena == 'surprise' and lena_makeup == 'z'", "lenasurprise_mk.webp",
        "flena == 'worried' and lena_makeup == 'z'", "lenaworried_mk.webp",
        "flena == 'n' and lena_makeup == 'z'", "lena_mk.webp",
        "flena == 'sad'", "lenasad.webp",
        "flena == 'crazy'", "lenacrazy.webp",
        "flena == 'crazyslut'", "lenacrazyslut.webp",
        "flena == 'crazyserious'", "lenacrazyserious.webp",
        "flena == 'crazysmile'", "lenacrazysmile.webp",
        "flena == 'blush'", "lenablush.webp",
        "flena == 'cry'", "lenacry.webp",
        "flena == 'drama'", "lenadrama.webp",
        "flena == 'evil'", "lenaevil.webp",
        "flena == 'flirt'", "lenaflirt.webp",
        "flena == 'flirtevil'", "lenaflirtevil.webp",
        "flena == 'flirtshy'", "lenaflirtshy.webp",
        "flena == 'happy'", "lenahappy.webp",
        "flena == 'mad'", "lenamad.webp",
        "flena == 'serious'", "lenaserious.webp",
        "flena == 'shy'", "lenashy.webp",
        "flena == 'slut'", "lenaslut.webp",
        "flena == 'slutshy'", "lenaslutshy.webp",
        "flena == 'smile'", "lenasmile.webp",
        "flena == 'surprise'", "lenasurprise.webp",
        "flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp")
    )



image lenawork = Composite(
    (640, 1080),
    (0, 0),"lenanude.webp", 
    (0, 0), ConditionSwitch( 
        "lena_makeup == 1", "lena_eyeshadow1.webp",
        "lena_makeup == 2", "lena_eyeshadow2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_necklace == 'choker'", "lena_choker.webp",
        "lena_necklace == 'choker2'", "lena_choker2.webp",
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
        "lena_look == 1", "lenacafe.webp",
        "lena_look == 2", "lenawaitress.webp",
        "True", "lenacafe.webp"
    ),
    (0, 0), ConditionSwitch( 
        "flena == 'sad' and lena_makeup == 'z'", "lenasad_mk.webp",
        "flena == 'crazy' and lena_makeup == 'z'", "lenacrazy_mk.webp",
        "flena == 'crazyslut' and lena_makeup == 'z'", "lenacrazyslut_mk.webp",
        "flena == 'crazyserious' and lena_makeup == 'z'", "lenacrazyserious_mk.webp",
        "flena == 'crazysmile' and lena_makeup == 'z'", "lenacrazysmile_mk.webp",
        "flena == 'blush' and lena_makeup == 'z'", "lenablush_mk.webp",
        "flena == 'cry' and lena_makeup == 'z'", "lenacry_mk.webp",
        "flena == 'drama' and lena_makeup == 'z'", "lenadrama_mk.webp",
        "flena == 'evil' and lena_makeup == 'z'", "lenaevil_mk.webp",
        "flena == 'flirt' and lena_makeup == 'z'", "lenaflirt_mk.webp",
        "flena == 'flirtevil' and lena_makeup == 'z'", "lenaflirtevil_mk.webp",
        "flena == 'flirtshy' and lena_makeup == 'z'", "lenaflirtshy_mk.webp",
        "flena == 'happy' and lena_makeup == 'z'", "lenahappy_mk.webp",
        "flena == 'mad' and lena_makeup == 'z'", "lenamad_mk.webp",
        "flena == 'serious' and lena_makeup == 'z'", "lenaserious_mk.webp",
        "flena == 'shy' and lena_makeup == 'z'", "lenashy_mk.webp",
        "flena == 'slut' and lena_makeup == 'z'", "lenaslut_mk.webp",
        "flena == 'slutshy' and lena_makeup == 'z'", "lenaslutshy_mk.webp",
        "flena == 'smile' and lena_makeup == 'z'", "lenasmile_mk.webp",
        "flena == 'surprise' and lena_makeup == 'z'", "lenasurprise_mk.webp",
        "flena == 'worried' and lena_makeup == 'z'", "lenaworried_mk.webp",
        "flena == 'n' and lena_makeup == 'z'", "lena_mk.webp",
        "flena == 'sad'", "lenasad.webp",
        "flena == 'crazy'", "lenacrazy.webp",
        "flena == 'crazyslut'", "lenacrazyslut.webp",
        "flena == 'crazyserious'", "lenacrazyserious.webp",
        "flena == 'crazysmile'", "lenacrazysmile.webp",
        "flena == 'blush'", "lenablush.webp",
        "flena == 'cry'", "lenacry.webp",
        "flena == 'drama'", "lenadrama.webp",
        "flena == 'evil'", "lenaevil.webp",
        "flena == 'flirt'", "lenaflirt.webp",
        "flena == 'flirtevil'", "lenaflirtevil.webp",
        "flena == 'flirtshy'", "lenaflirtshy.webp",
        "flena == 'happy'", "lenahappy.webp",
        "flena == 'mad'", "lenamad.webp",
        "flena == 'serious'", "lenaserious.webp",
        "flena == 'shy'", "lenashy.webp",
        "flena == 'slut'", "lenaslut.webp",
        "flena == 'slutshy'", "lenaslutshy.webp",
        "flena == 'smile'", "lenasmile.webp",
        "flena == 'surprise'", "lenasurprise.webp",
        "flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp")
    )

image lenawork_phone = Composite(
    (640, 1080),
    (0, 0),"lenanude_phone.webp", 
    (0, 0), ConditionSwitch( 
        "lena_makeup == 1", "lena_eyeshadow1.webp",
        "lena_makeup == 2", "lena_eyeshadow2.webp",
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
        "lena_necklace == 'choker'", "lena_choker.webp",
        "lena_necklace == 'choker2'", "lena_choker2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 1", "lenacafe_phone.webp",
        "lena_look == 2", "lenawaitress_phone.webp",
        "True", "lenacafe_phone.webp"
    ),
    (0, 0), ConditionSwitch( 
        "flena == 'sad' and lena_makeup == 'z'", "lenasad_mk.webp",
        "flena == 'crazy' and lena_makeup == 'z'", "lenacrazy_mk.webp",
        "flena == 'crazyslut' and lena_makeup == 'z'", "lenacrazyslut_mk.webp",
        "flena == 'crazyserious' and lena_makeup == 'z'", "lenacrazyserious_mk.webp",
        "flena == 'crazysmile' and lena_makeup == 'z'", "lenacrazysmile_mk.webp",
        "flena == 'blush' and lena_makeup == 'z'", "lenablush_mk.webp",
        "flena == 'cry' and lena_makeup == 'z'", "lenacry_mk.webp",
        "flena == 'drama' and lena_makeup == 'z'", "lenadrama_mk.webp",
        "flena == 'evil' and lena_makeup == 'z'", "lenaevil_mk.webp",
        "flena == 'flirt' and lena_makeup == 'z'", "lenaflirt_mk.webp",
        "flena == 'flirtevil' and lena_makeup == 'z'", "lenaflirtevil_mk.webp",
        "flena == 'flirtshy' and lena_makeup == 'z'", "lenaflirtshy_mk.webp",
        "flena == 'happy' and lena_makeup == 'z'", "lenahappy_mk.webp",
        "flena == 'mad' and lena_makeup == 'z'", "lenamad_mk.webp",
        "flena == 'serious' and lena_makeup == 'z'", "lenaserious_mk.webp",
        "flena == 'shy' and lena_makeup == 'z'", "lenashy_mk.webp",
        "flena == 'slut' and lena_makeup == 'z'", "lenaslut_mk.webp",
        "flena == 'slutshy' and lena_makeup == 'z'", "lenaslutshy_mk.webp",
        "flena == 'smile' and lena_makeup == 'z'", "lenasmile_mk.webp",
        "flena == 'surprise' and lena_makeup == 'z'", "lenasurprise_mk.webp",
        "flena == 'worried' and lena_makeup == 'z'", "lenaworried_mk.webp",
        "flena == 'n' and lena_makeup == 'z'", "lena_mk.webp",
        "flena == 'sad'", "lenasad.webp",
        "flena == 'crazy'", "lenacrazy.webp",
        "flena == 'crazyslut'", "lenacrazyslut.webp",
        "flena == 'crazyserious'", "lenacrazyserious.webp",
        "flena == 'crazysmile'", "lenacrazysmile.webp",
        "flena == 'blush'", "lenablush.webp",
        "flena == 'cry'", "lenacry.webp",
        "flena == 'drama'", "lenadrama.webp",
        "flena == 'evil'", "lenaevil.webp",
        "flena == 'flirt'", "lenaflirt.webp",
        "flena == 'flirtevil'", "lenaflirtevil.webp",
        "flena == 'flirtshy'", "lenaflirtshy.webp",
        "flena == 'happy'", "lenahappy.webp",
        "flena == 'mad'", "lenamad.webp",
        "flena == 'serious'", "lenaserious.webp",
        "flena == 'shy'", "lenashy.webp",
        "flena == 'slut'", "lenaslut.webp",
        "flena == 'slutshy'", "lenaslutshy.webp",
        "flena == 'smile'", "lenasmile.webp",
        "flena == 'surprise'", "lenasurprise.webp",
        "flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp")
    )



image lenabra = Composite(
    (640, 1080),
    (0, 0),"lenanude.webp", 
    (0, 0), ConditionSwitch( 
        "lena_makeup == 1", "lena_eyeshadow1.webp",
        "lena_makeup == 2", "lena_eyeshadow2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_necklace == 'choker'", "lena_choker.webp",
        "lena_necklace == 'choker2'", "lena_choker2.webp",
        "lena_necklace == 'seymour'", "lena_sy_collar.webp",
        "lena_necklace == 'seymour2'", "lena_sy_collar2.webp",
        "lena_necklace == 'seymour3'", "lena_sy_collar3.webp",
        "lena_necklace == 'gift'", "lena_giftnecklace.webp",
        "lena_necklace == 'gift2'", "lena_giftnecklace2.webp", 
        "True", Null()
    ),
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
        "lena_look == 'charisma' or lena_look == 'black_dress'" , "lena_charisma1_earrings.webp",
        "True", Null()
    ),
    
    (0, 0), ConditionSwitch( 
        "lena_extras == 'stockings'", "lena_lust1_stockings.webp",
        "True", Null()
    ),
    
    (0, 0), ConditionSwitch( 
        "lena_look == 'black_dress'", "lena_dress_posh_thigh.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 'black_dress'", "lenamoon.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 1 and lena_lust > 5 and chapter > 5", "lenacomfy2.webp",       
        "lena_look == 1", "lenacomfy.webp",                         
        "lena_look == 2", "lenabra.webp",                           
        "lena_look == 3", "lenabra2.webp",                          
        "lena_look == 'sexy'", "lenanobra2.webp",                   
        "lena_look == 'sexy1'", "lenabra2.webp",                    
        "lena_look == 'underwear2'", "lena_underwear2.webp",        
        "lena_look == 4", "lenabra2.webp",                          
        "lena_look == 'summer'", "lenanobra2.webp",
        "lena_look == 'gold'", "lena_jewel1.webp",
        "lena_look == 'charisma'", "lenanobra2.webp",               
        "lena_look == 'wits'", "lenabra2.webp",                     
        "lena_look == 'athletics'", "lenabra2.webp",                
        "lena_look == 'lust'", "lena_lust1_bra.webp",               
        "lena_look == 'black_lingerie2'", "lena_lingerie1b.webp",   
        "lena_look == 'black_lingerie3'", "lena_lingerie1c.webp",   
        "lena_look == 'black_lingerie'", "lena_lingerie1a.webp",    
        "lena_look == 'bunny'", "lena_bunny2.webp",                 
        "lena_look == 'udw2'", "lena_underwear2b.webp",             
        "lena_look == 'bikini' and lena_bikini == 1", "lenabikini1.webp",
        "lena_look == 'bikini' and lena_bikini == 2", "lenabikini2.webp",
        "lena_look == 'bikini' and lena_bikini == 3", "lenabikini3b.webp", 
        "lena_look == 'comfystan' and lena_lust > 7", "lena_comfyb.webp",
        "lena_look == 'comfystan' and lena_lust < 8", "lena_comfya.webp",
        "True", "lenacomfy.webp"
    ),
    (0, 0), ConditionSwitch( 
        "flena == 'sad' and lena_makeup == 'z'", "lenasad_mk.webp",
        "flena == 'crazy' and lena_makeup == 'z'", "lenacrazy_mk.webp",
        "flena == 'crazyslut' and lena_makeup == 'z'", "lenacrazyslut_mk.webp",
        "flena == 'crazyserious' and lena_makeup == 'z'", "lenacrazyserious_mk.webp",
        "flena == 'crazysmile' and lena_makeup == 'z'", "lenacrazysmile_mk.webp",
        "flena == 'blush' and lena_makeup == 'z'", "lenablush_mk.webp",
        "flena == 'cry' and lena_makeup == 'z'", "lenacry_mk.webp",
        "flena == 'drama' and lena_makeup == 'z'", "lenadrama_mk.webp",
        "flena == 'evil' and lena_makeup == 'z'", "lenaevil_mk.webp",
        "flena == 'flirt' and lena_makeup == 'z'", "lenaflirt_mk.webp",
        "flena == 'flirtevil' and lena_makeup == 'z'", "lenaflirtevil_mk.webp",
        "flena == 'flirtshy' and lena_makeup == 'z'", "lenaflirtshy_mk.webp",
        "flena == 'happy' and lena_makeup == 'z'", "lenahappy_mk.webp",
        "flena == 'mad' and lena_makeup == 'z'", "lenamad_mk.webp",
        "flena == 'serious' and lena_makeup == 'z'", "lenaserious_mk.webp",
        "flena == 'shy' and lena_makeup == 'z'", "lenashy_mk.webp",
        "flena == 'slut' and lena_makeup == 'z'", "lenaslut_mk.webp",
        "flena == 'slutshy' and lena_makeup == 'z'", "lenaslutshy_mk.webp",
        "flena == 'smile' and lena_makeup == 'z'", "lenasmile_mk.webp",
        "flena == 'surprise' and lena_makeup == 'z'", "lenasurprise_mk.webp",
        "flena == 'worried' and lena_makeup == 'z'", "lenaworried_mk.webp",
        "flena == 'n' and lena_makeup == 'z'", "lena_mk.webp",
        "flena == 'sad'", "lenasad.webp",
        "flena == 'crazy'", "lenacrazy.webp",
        "flena == 'crazyslut'", "lenacrazyslut.webp",
        "flena == 'crazyserious'", "lenacrazyserious.webp",
        "flena == 'crazysmile'", "lenacrazysmile.webp",
        "flena == 'blush'", "lenablush.webp",
        "flena == 'cry'", "lenacry.webp",
        "flena == 'drama'", "lenadrama.webp",
        "flena == 'evil'", "lenaevil.webp",
        "flena == 'flirt'", "lenaflirt.webp",
        "flena == 'flirtevil'", "lenaflirtevil.webp",
        "flena == 'flirtshy'", "lenaflirtshy.webp",
        "flena == 'happy'", "lenahappy.webp",
        "flena == 'mad'", "lenamad.webp",
        "flena == 'serious'", "lenaserious.webp",
        "flena == 'shy'", "lenashy.webp",
        "flena == 'slut'", "lenaslut.webp",
        "flena == 'slutshy'", "lenaslutshy.webp",
        "flena == 'smile'", "lenasmile.webp",
        "flena == 'surprise'", "lenasurprise.webp",
        "flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp")
    )

image lenabra2 = Composite(
    (640, 1080),
    (0, 0),"lenanude_b.webp", 
    (0, 0), ConditionSwitch( 
        "lena_makeup == 1", "lena_eyeshadow1.webp",
        "lena_makeup == 2", "lena_eyeshadow2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_necklace == 'choker'", "lena_choker.webp",
        "lena_necklace == 'choker2'", "lena_choker2.webp",
        "lena_necklace == 'seymour'", "lena_sy_collar.webp",
        "lena_necklace == 'seymour2'", "lena_sy_collar2.webp",
        "lena_necklace == 'seymour3'", "lena_sy_collar3.webp",
        "lena_necklace == 'gift'", "lena_giftnecklace.webp",
        "lena_necklace == 'gift2'", "lena_giftnecklace2.webp", 
        "True", Null()
    ),
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
        "lena_look == 'charisma' or lena_look == 'black_dress'" , "lena_charisma1_earrings.webp",
        "True", Null()
    ),
    
    (0, 0), ConditionSwitch( 
        "lena_extras == 'stockings'", "lena_lust1_stockings.webp",
        "True", Null()
    ),
    
    (0, 0), ConditionSwitch( 
        "lena_look == 'black_dress'", "lena_dress_posh_thigh.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 'black_dress'", "lenamoon.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "flena == 'sad' and lena_makeup == 'z'", "lenasad_mk.webp",
        "flena == 'crazy' and lena_makeup == 'z'", "lenacrazy_mk.webp",
        "flena == 'crazyslut' and lena_makeup == 'z'", "lenacrazyslut_mk.webp",
        "flena == 'crazyserious' and lena_makeup == 'z'", "lenacrazyserious_mk.webp",
        "flena == 'crazysmile' and lena_makeup == 'z'", "lenacrazysmile_mk.webp",
        "flena == 'blush' and lena_makeup == 'z'", "lenablush_mk.webp",
        "flena == 'cry' and lena_makeup == 'z'", "lenacry_mk.webp",
        "flena == 'drama' and lena_makeup == 'z'", "lenadrama_mk.webp",
        "flena == 'evil' and lena_makeup == 'z'", "lenaevil_mk.webp",
        "flena == 'flirt' and lena_makeup == 'z'", "lenaflirt_mk.webp",
        "flena == 'flirtevil' and lena_makeup == 'z'", "lenaflirtevil_mk.webp",
        "flena == 'flirtshy' and lena_makeup == 'z'", "lenaflirtshy_mk.webp",
        "flena == 'happy' and lena_makeup == 'z'", "lenahappy_mk.webp",
        "flena == 'mad' and lena_makeup == 'z'", "lenamad_mk.webp",
        "flena == 'serious' and lena_makeup == 'z'", "lenaserious_mk.webp",
        "flena == 'shy' and lena_makeup == 'z'", "lenashy_mk.webp",
        "flena == 'slut' and lena_makeup == 'z'", "lenaslut_mk.webp",
        "flena == 'slutshy' and lena_makeup == 'z'", "lenaslutshy_mk.webp",
        "flena == 'smile' and lena_makeup == 'z'", "lenasmile_mk.webp",
        "flena == 'surprise' and lena_makeup == 'z'", "lenasurprise_mk.webp",
        "flena == 'worried' and lena_makeup == 'z'", "lenaworried_mk.webp",
        "flena == 'n' and lena_makeup == 'z'", "lena_mk.webp",
        "lena_look == 1 and lena_lust > 5 and chapter > 5", "lenacomfy2.webp",       
        "lena_look == 1", "lenacomfy.webp",                         
        "lena_look == 2", "lenabra.webp",                           
        "lena_look == 4", "lenabra2.webp",                          
        "lena_look == 3", "lenabra2.webp",                          
        "lena_look == 'sexy'", "lenanobra2.webp",                   
        "lena_look == 'sexy1'", "lenabra2.webp",                    
        "lena_look == 'underwear2'", "lena_underwear2.webp",        
        "lena_look == 'gold'", "lena_jewel1.webp",
        "lena_look == 'charisma'", "lenanobra2.webp",               
        "lena_look == 'wits'", "lenabra2.webp",                     
        "lena_look == 'athletics'", "lenabra2.webp",                
        "lena_look == 'lust'", "lena_lust1_bra.webp",               
        "lena_look == 'black_lingerie2'", "lena_lingerie1b.webp",   
        "lena_look == 'black_lingerie3'", "lena_lingerie1c.webp",   
        "lena_look == 'black_lingerie'", "lena_lingerie1a.webp",    
        "lena_look == 'bunny'", "lena_bunny2.webp",                 
        "lena_look == 'udw2'", "lena_underwear2b.webp",             
        "lena_look == 'summer'", "lenanobra2.webp",
        "lena_look == 'bikini' and lena_bikini == 1", "lenabikini1.webp",
        "lena_look == 'bikini' and lena_bikini == 2", "lenabikini2.webp",
        "lena_look == 'bikini' and lena_bikini == 3", "lenabikini3b.webp", 
        "lena_look == 'comfystan' and lena_lust > 7", "lena_comfyb2.webp",
        "lena_look == 'comfystan' and lena_lust < 8", "lena_comfya2.webp",
        "True", "lenacomfy.webp"
    ),
    (0, 0), ConditionSwitch( 
        "flena == 'sad'", "lenasad.webp",
        "flena == 'crazy'", "lenacrazy.webp",
        "flena == 'crazyslut'", "lenacrazyslut.webp",
        "flena == 'crazyserious'", "lenacrazyserious.webp",
        "flena == 'crazysmile'", "lenacrazysmile.webp",
        "flena == 'blush'", "lenablush.webp",
        "flena == 'cry'", "lenacry.webp",
        "flena == 'drama'", "lenadrama.webp",
        "flena == 'evil'", "lenaevil.webp",
        "flena == 'flirt'", "lenaflirt.webp",
        "flena == 'flirtevil'", "lenaflirtevil.webp",
        "flena == 'flirtshy'", "lenaflirtshy.webp",
        "flena == 'happy'", "lenahappy.webp",
        "flena == 'mad'", "lenamad.webp",
        "flena == 'serious'", "lenaserious.webp",
        "flena == 'shy'", "lenashy.webp",
        "flena == 'slut'", "lenaslut.webp",
        "flena == 'slutshy'", "lenaslutshy.webp",
        "flena == 'smile'", "lenasmile.webp",
        "flena == 'surprise'", "lenasurprise.webp",
        "flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp"
    )
)

image lenabra_phone = Composite(
    (640, 1080),
    (0, 0),"lenanude_phone.webp", 
    (0, 0), ConditionSwitch( 
        "lena_makeup == 1", "lena_eyeshadow1.webp",
        "lena_makeup == 2", "lena_eyeshadow2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_necklace == 'choker'", "lena_choker.webp",
        "lena_necklace == 'choker2'", "lena_choker2.webp",
        "lena_necklace == 'seymour'", "lena_sy_collar.webp",
        "lena_necklace == 'seymour2'", "lena_sy_collar2.webp",
        "lena_necklace == 'seymour3'", "lena_sy_collar3.webp",
        "lena_necklace == 'gift'", "lena_giftnecklace.webp",
        "lena_necklace == 'gift2'", "lena_giftnecklace2.webp", 
        "True", Null()
    ),
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
        "lena_look == 'charisma' or lena_look == 'black_dress'" , "lena_charisma1_earrings.webp",
        "True", Null()
    ),
    
    (0, 0), ConditionSwitch( 
        "lena_extras == 'stockings'", "lena_lust1_stockings.webp",
        "True", Null()
    ),
    
    (0, 0), ConditionSwitch( 
        "lena_look == 'black_dress'", "lena_dress_posh_thigh.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 'black_dress'", "lenamoon.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 1 and lena_lust > 5 and chapter > 5", "lenacomfy2_phone.webp",       
        "lena_look == 1", "lenacomfy_phone.webp",
        "lena_look == 2", "lenabra_phone.webp",
        "lena_look == 3", "lenabra2_phone.webp",
        "lena_look == 4", "lenabra2_phone.webp",
        "lena_look == 'sexy'", "lenabra2_phone.webp",
        "lena_look == 'sexy1'", "lenabra2_phone.webp",
        "lena_look == 'underwear2'", "lena_underwear2_phone.webp",
        "lena_look == 'charisma'", "lenabra2_phone.webp",
        "lena_look == 'wits'", "lenabra2_phone.webp",
        "lena_look == 'athletics'", "lenabra2_phone.webp",
        "lena_look == 'lust'", "lena_lust1_bra.webp",
        "lena_look == 'black_lingerie2'", "lena_lingerie1b.webp",
        "lena_look == 'black_lingerie3'", "lena_lingerie1c.webp",
        "lena_look == 'black_lingerie'", "lena_lingerie1a.webp",
        "lena_look == 'bunny'", "lena_bunny2.webp",
        "lena_look == 'udw2'", "lena_underwear2b.webp",
        "lena_look == 'summer'", "lenanobra2.webp",
        "lena_look == 'comfystan' and lena_lust > 7", "lena_comfyb_phone.webp",
        "lena_look == 'comfystan' and lena_lust < 8", "lena_comfya_phone.webp",
        "True", "lenacomfy_phone.webp"
    ),
    (0, 0), ConditionSwitch( 
        "flena == 'sad' and lena_makeup == 'z'", "lenasad_mk.webp",
        "flena == 'crazy' and lena_makeup == 'z'", "lenacrazy_mk.webp",
        "flena == 'crazyslut' and lena_makeup == 'z'", "lenacrazyslut_mk.webp",
        "flena == 'crazyserious' and lena_makeup == 'z'", "lenacrazyserious_mk.webp",
        "flena == 'crazysmile' and lena_makeup == 'z'", "lenacrazysmile_mk.webp",
        "flena == 'blush' and lena_makeup == 'z'", "lenablush_mk.webp",
        "flena == 'cry' and lena_makeup == 'z'", "lenacry_mk.webp",
        "flena == 'drama' and lena_makeup == 'z'", "lenadrama_mk.webp",
        "flena == 'evil' and lena_makeup == 'z'", "lenaevil_mk.webp",
        "flena == 'flirt' and lena_makeup == 'z'", "lenaflirt_mk.webp",
        "flena == 'flirtevil' and lena_makeup == 'z'", "lenaflirtevil_mk.webp",
        "flena == 'flirtshy' and lena_makeup == 'z'", "lenaflirtshy_mk.webp",
        "flena == 'happy' and lena_makeup == 'z'", "lenahappy_mk.webp",
        "flena == 'mad' and lena_makeup == 'z'", "lenamad_mk.webp",
        "flena == 'serious' and lena_makeup == 'z'", "lenaserious_mk.webp",
        "flena == 'shy' and lena_makeup == 'z'", "lenashy_mk.webp",
        "flena == 'slut' and lena_makeup == 'z'", "lenaslut_mk.webp",
        "flena == 'slutshy' and lena_makeup == 'z'", "lenaslutshy_mk.webp",
        "flena == 'smile' and lena_makeup == 'z'", "lenasmile_mk.webp",
        "flena == 'surprise' and lena_makeup == 'z'", "lenasurprise_mk.webp",
        "flena == 'worried' and lena_makeup == 'z'", "lenaworried_mk.webp",
        "flena == 'n' and lena_makeup == 'z'", "lena_mk.webp",
        "flena == 'sad'", "lenasad.webp",
        "flena == 'crazy'", "lenacrazy.webp",
        "flena == 'crazyslut'", "lenacrazyslut.webp",
        "flena == 'crazyserious'", "lenacrazyserious.webp",
        "flena == 'crazysmile'", "lenacrazysmile.webp",
        "flena == 'blush'", "lenablush.webp",
        "flena == 'cry'", "lenacry.webp",
        "flena == 'drama'", "lenadrama.webp",
        "flena == 'evil'", "lenaevil.webp",
        "flena == 'flirt'", "lenaflirt.webp",
        "flena == 'flirtevil'", "lenaflirtevil.webp",
        "flena == 'flirtshy'", "lenaflirtshy.webp",
        "flena == 'happy'", "lenahappy.webp",
        "flena == 'mad'", "lenamad.webp",
        "flena == 'serious'", "lenaserious.webp",
        "flena == 'shy'", "lenashy.webp",
        "flena == 'slut'", "lenaslut.webp",
        "flena == 'slutshy'", "lenaslutshy.webp",
        "flena == 'smile'", "lenasmile.webp",
        "flena == 'surprise'", "lenasurprise.webp",
        "flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp"
    )
)

image lenaunder = Composite(
    (640, 1080),
    (0, 0),"lenanude.webp", 
    (0, 0), ConditionSwitch( 
        "lena_makeup == 1", "lena_eyeshadow1.webp",
        "lena_makeup == 2", "lena_eyeshadow2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_necklace == 'choker'", "lena_choker.webp",
        "lena_necklace == 'choker2'", "lena_choker2.webp",
        "lena_necklace == 'seymour'", "lena_sy_collar.webp",
        "lena_necklace == 'seymour2'", "lena_sy_collar2.webp",
        "lena_necklace == 'seymour3'", "lena_sy_collar3.webp",
        "lena_necklace == 'gift'", "lena_giftnecklace.webp",
        "lena_necklace == 'gift2'", "lena_giftnecklace2.webp", 
        "True", Null()
    ),
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
        "lena_look == 'charisma' or lena_look == 'black_dress'" , "lena_charisma1_earrings.webp",
        "True", Null()
    ),
    
    (0, 0), ConditionSwitch( 
        "lena_extras == 'stockings'", "lena_lust1_stockings.webp",
        "True", Null()
    ),
    
    (0, 0), ConditionSwitch( 
        "lena_look == 'black_dress'", "lena_dress_posh_thigh.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 1 and lena_lust > 5 and chapter > 5", "lenabra2.webp", 
        "lena_look == 1", "lenabra.webp",
        "lena_look == 'towel'", "lena_towel.webp",
        "lena_look == 'sexy'", "lenabra2.webp",
        "lena_look == 'underwear2'", "lena_underwear2.webp",
        "lena_look == 'ianshirt'", "lena_ianshirt.webp",
        "lena_look == 'ianshirt2'", "lena_ianshirt2.webp",
        "lena_look == 'lust'", "lena_lust1_bra.webp",
        "lena_look == 4", "lenabra2.webp",
        "lena_look == 2", "lenabra.webp",
        "lena_look == 'clubdress' and v11_lena_dress == 1", "lena_dress_undone1.webp",
        "lena_look == 'clubdress' and v11_lena_dress == 2", "lena_dress_undone2.webp",
        "lena_look == 'clubdress' and v11_lena_dress == 3", "lena_dress_undone3.webp",
        "lena_look == 'clubdress' and v11_lena_dress == 4", "lena_dress_undone4.webp",
        "True", "lenabra.webp"
    ),
    (0, 0), ConditionSwitch( 
        "flena == 'sad' and lena_makeup == 'z'", "lenasad_mk.webp",
        "flena == 'crazy' and lena_makeup == 'z'", "lenacrazy_mk.webp",
        "flena == 'crazyslut' and lena_makeup == 'z'", "lenacrazyslut_mk.webp",
        "flena == 'crazyserious' and lena_makeup == 'z'", "lenacrazyserious_mk.webp",
        "flena == 'crazysmile' and lena_makeup == 'z'", "lenacrazysmile_mk.webp",
        "flena == 'blush' and lena_makeup == 'z'", "lenablush_mk.webp",
        "flena == 'cry' and lena_makeup == 'z'", "lenacry_mk.webp",
        "flena == 'drama' and lena_makeup == 'z'", "lenadrama_mk.webp",
        "flena == 'evil' and lena_makeup == 'z'", "lenaevil_mk.webp",
        "flena == 'flirt' and lena_makeup == 'z'", "lenaflirt_mk.webp",
        "flena == 'flirtevil' and lena_makeup == 'z'", "lenaflirtevil_mk.webp",
        "flena == 'flirtshy' and lena_makeup == 'z'", "lenaflirtshy_mk.webp",
        "flena == 'happy' and lena_makeup == 'z'", "lenahappy_mk.webp",
        "flena == 'mad' and lena_makeup == 'z'", "lenamad_mk.webp",
        "flena == 'serious' and lena_makeup == 'z'", "lenaserious_mk.webp",
        "flena == 'shy' and lena_makeup == 'z'", "lenashy_mk.webp",
        "flena == 'slut' and lena_makeup == 'z'", "lenaslut_mk.webp",
        "flena == 'slutshy' and lena_makeup == 'z'", "lenaslutshy_mk.webp",
        "flena == 'smile' and lena_makeup == 'z'", "lenasmile_mk.webp",
        "flena == 'surprise' and lena_makeup == 'z'", "lenasurprise_mk.webp",
        "flena == 'worried' and lena_makeup == 'z'", "lenaworried_mk.webp",
        "flena == 'n' and lena_makeup == 'z'", "lena_mk.webp",
        "flena == 'sad'", "lenasad.webp",
        "flena == 'crazy'", "lenacrazy.webp",
        "flena == 'crazyslut'", "lenacrazyslut.webp",
        "flena == 'crazyserious'", "lenacrazyserious.webp",
        "flena == 'crazysmile'", "lenacrazysmile.webp",
        "flena == 'blush'", "lenablush.webp",
        "flena == 'cry'", "lenacry.webp",
        "flena == 'drama'", "lenadrama.webp",
        "flena == 'evil'", "lenaevil.webp",
        "flena == 'flirt'", "lenaflirt.webp",
        "flena == 'flirtevil'", "lenaflirtevil.webp",
        "flena == 'flirtshy'", "lenaflirtshy.webp",
        "flena == 'happy'", "lenahappy.webp",
        "flena == 'mad'", "lenamad.webp",
        "flena == 'serious'", "lenaserious.webp",
        "flena == 'shy'", "lenashy.webp",
        "flena == 'slut'", "lenaslut.webp",
        "flena == 'slutshy'", "lenaslutshy.webp",
        "flena == 'smile'", "lenasmile.webp",
        "flena == 'surprise'", "lenasurprise.webp",
        "flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp"
    )
)

image lenaunder2 = Composite(
    (640, 1080),
    (0, 0),"lenanude_b.webp", 
    (0, 0), ConditionSwitch( 
        "lena_makeup == 1", "lena_eyeshadow1.webp",
        "lena_makeup == 2", "lena_eyeshadow2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_necklace == 'choker'", "lena_choker.webp",
        "lena_necklace == 'choker2'", "lena_choker2.webp",
        "lena_necklace == 'seymour'", "lena_sy_collar.webp",
        "lena_necklace == 'seymour2'", "lena_sy_collar2.webp",
        "lena_necklace == 'seymour3'", "lena_sy_collar3.webp",
        "lena_necklace == 'gift'", "lena_giftnecklace.webp",
        "lena_necklace == 'gift2'", "lena_giftnecklace2.webp", 
        "True", Null()
    ),
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
        "lena_look == 'charisma' or lena_look == 'black_dress'" , "lena_charisma1_earrings.webp",
        "True", Null()
    ),
    
    (0, 0), ConditionSwitch( 
        "lena_extras == 'stockings'", "lena_lust1_stockings.webp",
        "True", Null()
    ),
    
    (0, 0), ConditionSwitch( 
        "lena_look == 'black_dress'", "lena_dress_posh_thigh.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 1 and lena_lust > 5 and chapter > 5", "lenabra2.webp", 
        "lena_look == 1", "lenabra.webp",
        "lena_look == 'towel'", "lena_towel.webp",
        "lena_look == 'sexy'", "lenabra2.webp",
        "lena_look == 'underwear2'", "lena_underwear2.webp",
        "lena_look == 'ianshirt'", "lena_ianshirt.webp",
        "lena_look == 'ianshirt2'", "lena_ianshirt2.webp",
        "lena_look == 'lust'", "lena_lust1_bra.webp",
        "lena_look == 4", "lenabra2.webp",
        "lena_look == 2", "lenabra.webp",
        "True", "lenabra.webp"
    ),
    (0, 0), ConditionSwitch( 
        "flena == 'sad' and lena_makeup == 'z'", "lenasad_mk.webp",
        "flena == 'crazy' and lena_makeup == 'z'", "lenacrazy_mk.webp",
        "flena == 'crazyslut' and lena_makeup == 'z'", "lenacrazyslut_mk.webp",
        "flena == 'crazyserious' and lena_makeup == 'z'", "lenacrazyserious_mk.webp",
        "flena == 'crazysmile' and lena_makeup == 'z'", "lenacrazysmile_mk.webp",
        "flena == 'blush' and lena_makeup == 'z'", "lenablush_mk.webp",
        "flena == 'cry' and lena_makeup == 'z'", "lenacry_mk.webp",
        "flena == 'drama' and lena_makeup == 'z'", "lenadrama_mk.webp",
        "flena == 'evil' and lena_makeup == 'z'", "lenaevil_mk.webp",
        "flena == 'flirt' and lena_makeup == 'z'", "lenaflirt_mk.webp",
        "flena == 'flirtevil' and lena_makeup == 'z'", "lenaflirtevil_mk.webp",
        "flena == 'flirtshy' and lena_makeup == 'z'", "lenaflirtshy_mk.webp",
        "flena == 'happy' and lena_makeup == 'z'", "lenahappy_mk.webp",
        "flena == 'mad' and lena_makeup == 'z'", "lenamad_mk.webp",
        "flena == 'serious' and lena_makeup == 'z'", "lenaserious_mk.webp",
        "flena == 'shy' and lena_makeup == 'z'", "lenashy_mk.webp",
        "flena == 'slut' and lena_makeup == 'z'", "lenaslut_mk.webp",
        "flena == 'slutshy' and lena_makeup == 'z'", "lenaslutshy_mk.webp",
        "flena == 'smile' and lena_makeup == 'z'", "lenasmile_mk.webp",
        "flena == 'surprise' and lena_makeup == 'z'", "lenasurprise_mk.webp",
        "flena == 'worried' and lena_makeup == 'z'", "lenaworried_mk.webp",
        "flena == 'n' and lena_makeup == 'z'", "lena_mk.webp",
        "flena == 'sad'", "lenasad.webp",
        "flena == 'crazy'", "lenacrazy.webp",
        "flena == 'crazyslut'", "lenacrazyslut.webp",
        "flena == 'crazyserious'", "lenacrazyserious.webp",
        "flena == 'crazysmile'", "lenacrazysmile.webp",
        "flena == 'blush'", "lenablush.webp",
        "flena == 'cry'", "lenacry.webp",
        "flena == 'drama'", "lenadrama.webp",
        "flena == 'evil'", "lenaevil.webp",
        "flena == 'flirt'", "lenaflirt.webp",
        "flena == 'flirtevil'", "lenaflirtevil.webp",
        "flena == 'flirtshy'", "lenaflirtshy.webp",
        "flena == 'happy'", "lenahappy.webp",
        "flena == 'mad'", "lenamad.webp",
        "flena == 'serious'", "lenaserious.webp",
        "flena == 'shy'", "lenashy.webp",
        "flena == 'slut'", "lenaslut.webp",
        "flena == 'slutshy'", "lenaslutshy.webp",
        "flena == 'smile'", "lenasmile.webp",
        "flena == 'surprise'", "lenasurprise.webp",
        "flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp"
    )
)



image lenatopless = Composite(
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
        "lena_makeup == 1", "lena_eyeshadow1.webp",
        "lena_makeup == 2", "lena_eyeshadow2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_necklace == 'choker'", "lena_choker.webp",
        "lena_necklace == 'choker2'", "lena_choker2.webp",
        "lena_necklace == 'seymour'", "lena_sy_collar.webp",
        "lena_necklace == 'seymour2'", "lena_sy_collar2.webp",
        "lena_necklace == 'seymour3'", "lena_sy_collar3.webp",
        "lena_necklace == 'gift'", "lena_giftnecklace.webp",
        "lena_necklace == 'gift2'", "lena_giftnecklace2.webp", 
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 'charisma' or lena_look == 'black_dress'" , "lena_charisma1_earrings.webp",
        "True", Null()
    ),
    
    (0, 0), ConditionSwitch( 
        "lena_extras == 'stockings'", "lena_lust1_stockings.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 1", "lenanobra.webp",
        "lena_look == 'sexy'", "lenanobra2.webp",
        "lena_look == 'sexy1'", "lenanobra2.webp",
        "lena_look == 'charisma'", "lenanobra2.webp",
        "lena_look == 'wits'", "lenanobra2.webp",
        "lena_look == 'athletics'", "lenanobra2.webp",
        "lena_look == 'lust'", "lena_lust1_thong.webp",
        "lena_look == 'underwear2'", "lena_underwear2_topless.webp",
        "lena_look == 4", "lenanobra2.webp",
        "lena_look == 2", "lenanobra.webp",
        "lena_look == 'bikini' and lena_bikini == 1", "lenabikini1_topless.webp",
        "lena_look == 'bikini' and lena_bikini == 2", "lenabikini2_topless.webp",
        "lena_look == 'bikini' and lena_bikini == 3", "lenabikini3_topless.webp",
        "lena_look == 'summer'", "lena_summer_top.webp",
        "True", "lenanobra.webp"
    ),
    (0, 0), ConditionSwitch( 
        "flena == 'sad' and lena_makeup == 'z'", "lenasad_mk.webp",
        "flena == 'crazy' and lena_makeup == 'z'", "lenacrazy_mk.webp",
        "flena == 'crazyslut' and lena_makeup == 'z'", "lenacrazyslut_mk.webp",
        "flena == 'crazyserious' and lena_makeup == 'z'", "lenacrazyserious_mk.webp",
        "flena == 'crazysmile' and lena_makeup == 'z'", "lenacrazysmile_mk.webp",
        "flena == 'blush' and lena_makeup == 'z'", "lenablush_mk.webp",
        "flena == 'cry' and lena_makeup == 'z'", "lenacry_mk.webp",
        "flena == 'drama' and lena_makeup == 'z'", "lenadrama_mk.webp",
        "flena == 'evil' and lena_makeup == 'z'", "lenaevil_mk.webp",
        "flena == 'flirt' and lena_makeup == 'z'", "lenaflirt_mk.webp",
        "flena == 'flirtevil' and lena_makeup == 'z'", "lenaflirtevil_mk.webp",
        "flena == 'flirtshy' and lena_makeup == 'z'", "lenaflirtshy_mk.webp",
        "flena == 'happy' and lena_makeup == 'z'", "lenahappy_mk.webp",
        "flena == 'mad' and lena_makeup == 'z'", "lenamad_mk.webp",
        "flena == 'serious' and lena_makeup == 'z'", "lenaserious_mk.webp",
        "flena == 'shy' and lena_makeup == 'z'", "lenashy_mk.webp",
        "flena == 'slut' and lena_makeup == 'z'", "lenaslut_mk.webp",
        "flena == 'slutshy' and lena_makeup == 'z'", "lenaslutshy_mk.webp",
        "flena == 'smile' and lena_makeup == 'z'", "lenasmile_mk.webp",
        "flena == 'surprise' and lena_makeup == 'z'", "lenasurprise_mk.webp",
        "flena == 'worried' and lena_makeup == 'z'", "lenaworried_mk.webp",
        "flena == 'n' and lena_makeup == 'z'", "lena_mk.webp",
        "flena == 'sad'", "lenasad.webp",
        "flena == 'crazy'", "lenacrazy.webp",
        "flena == 'crazyslut'", "lenacrazyslut.webp",
        "flena == 'crazyserious'", "lenacrazyserious.webp",
        "flena == 'crazysmile'", "lenacrazysmile.webp",
        "flena == 'blush'", "lenablush.webp",
        "flena == 'cry'", "lenacry.webp",
        "flena == 'drama'", "lenadrama.webp",
        "flena == 'evil'", "lenaevil.webp",
        "flena == 'flirt'", "lenaflirt.webp",
        "flena == 'flirtevil'", "lenaflirtevil.webp",
        "flena == 'flirtshy'", "lenaflirtshy.webp",
        "flena == 'happy'", "lenahappy.webp",
        "flena == 'mad'", "lenamad.webp",
        "flena == 'serious'", "lenaserious.webp",
        "flena == 'shy'", "lenashy.webp",
        "flena == 'slut'", "lenaslut.webp",
        "flena == 'slutshy'", "lenaslutshy.webp",
        "flena == 'smile'", "lenasmile.webp",
        "flena == 'surprise'", "lenasurprise.webp",
        "flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp"
    )
)

image lenatopless2 = Composite(
    (640, 1080),
    (0, 0),"lenanude_b.webp", 
    (0, 0), ConditionSwitch( 
        "lena_makeup == 1", "lena_eyeshadow1.webp",
        "lena_makeup == 2", "lena_eyeshadow2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_necklace == 'choker'", "lena_choker.webp",
        "lena_necklace == 'choker2'", "lena_choker2.webp",
        "lena_necklace == 'seymour'", "lena_sy_collar.webp",
        "lena_necklace == 'seymour2'", "lena_sy_collar2.webp",
        "lena_necklace == 'seymour3'", "lena_sy_collar3.webp",
        "lena_necklace == 'gift'", "lena_giftnecklace.webp",
        "lena_necklace == 'gift2'", "lena_giftnecklace2.webp", 
        "True", Null()
    ),
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
        "lena_look == 'charisma' or lena_look == 'black_dress'" , "lena_charisma1_earrings.webp",
        "True", Null()
    ),
    
    (0, 0), ConditionSwitch( 
        "lena_extras == 'stockings'", "lena_lust1_stockings.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 1", "lenanobra.webp",
        "lena_look == 'sexy'", "lenanobra2.webp",
        "lena_look == 'sexy1'", "lenanobra2.webp",
        "lena_look == 4", "lenanobra2.webp",
        "lena_look == 'charisma'", "lenanobra2.webp",
        "lena_look == 'wits'", "lenanobra2.webp",
        "lena_look == 'athletics'", "lenanobra2.webp",
        "lena_look == 'lust'", "lena_lust1_thong.webp",
        "lena_look == 'underwear2'", "lena_underwear2_topless.webp",
        "lena_look == 2", "lenanobra.webp",
        "lena_look == 'bikini' and lena_bikini == 1", "lenabikini1_topless.webp",
        "lena_look == 'bikini' and lena_bikini == 2", "lenabikini2_topless.webp",
        "lena_look == 'bikini' and lena_bikini == 3", "lenabikini3_topless.webp",
        "True", "lenanobra.webp"
    ),
    (0, 0), ConditionSwitch( 
        "flena == 'sad' and lena_makeup == 'z'", "lenasad_mk.webp",
        "flena == 'crazy' and lena_makeup == 'z'", "lenacrazy_mk.webp",
        "flena == 'crazyslut' and lena_makeup == 'z'", "lenacrazyslut_mk.webp",
        "flena == 'crazyserious' and lena_makeup == 'z'", "lenacrazyserious_mk.webp",
        "flena == 'crazysmile' and lena_makeup == 'z'", "lenacrazysmile_mk.webp",
        "flena == 'blush' and lena_makeup == 'z'", "lenablush_mk.webp",
        "flena == 'cry' and lena_makeup == 'z'", "lenacry_mk.webp",
        "flena == 'drama' and lena_makeup == 'z'", "lenadrama_mk.webp",
        "flena == 'evil' and lena_makeup == 'z'", "lenaevil_mk.webp",
        "flena == 'flirt' and lena_makeup == 'z'", "lenaflirt_mk.webp",
        "flena == 'flirtevil' and lena_makeup == 'z'", "lenaflirtevil_mk.webp",
        "flena == 'flirtshy' and lena_makeup == 'z'", "lenaflirtshy_mk.webp",
        "flena == 'happy' and lena_makeup == 'z'", "lenahappy_mk.webp",
        "flena == 'mad' and lena_makeup == 'z'", "lenamad_mk.webp",
        "flena == 'serious' and lena_makeup == 'z'", "lenaserious_mk.webp",
        "flena == 'shy' and lena_makeup == 'z'", "lenashy_mk.webp",
        "flena == 'slut' and lena_makeup == 'z'", "lenaslut_mk.webp",
        "flena == 'slutshy' and lena_makeup == 'z'", "lenaslutshy_mk.webp",
        "flena == 'smile' and lena_makeup == 'z'", "lenasmile_mk.webp",
        "flena == 'surprise' and lena_makeup == 'z'", "lenasurprise_mk.webp",
        "flena == 'worried' and lena_makeup == 'z'", "lenaworried_mk.webp",
        "flena == 'n' and lena_makeup == 'z'", "lena_mk.webp",
        "flena == 'sad'", "lenasad.webp",
        "flena == 'crazy'", "lenacrazy.webp",
        "flena == 'crazyslut'", "lenacrazyslut.webp",
        "flena == 'crazyserious'", "lenacrazyserious.webp",
        "flena == 'crazysmile'", "lenacrazysmile.webp",
        "flena == 'blush'", "lenablush.webp",
        "flena == 'cry'", "lenacry.webp",
        "flena == 'drama'", "lenadrama.webp",
        "flena == 'evil'", "lenaevil.webp",
        "flena == 'flirt'", "lenaflirt.webp",
        "flena == 'flirtevil'", "lenaflirtevil.webp",
        "flena == 'flirtshy'", "lenaflirtshy.webp",
        "flena == 'happy'", "lenahappy.webp",
        "flena == 'mad'", "lenamad.webp",
        "flena == 'serious'", "lenaserious.webp",
        "flena == 'shy'", "lenashy.webp",
        "flena == 'slut'", "lenaslut.webp",
        "flena == 'slutshy'", "lenaslutshy.webp",
        "flena == 'smile'", "lenasmile.webp",
        "flena == 'surprise'", "lenasurprise.webp",
        "flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp"
    )
)

image lenatopless_phone = Composite(
    (640, 1080),
    (0, 0),"lenanude_phone.webp", 
    (0, 0), ConditionSwitch( 
        "lena_makeup == 1", "lena_eyeshadow1.webp",
        "lena_makeup == 2", "lena_eyeshadow2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_necklace == 'choker'", "lena_choker.webp",
        "lena_necklace == 'choker2'", "lena_choker2.webp",
        "lena_necklace == 'seymour'", "lena_sy_collar.webp",
        "lena_necklace == 'seymour2'", "lena_sy_collar2.webp",
        "lena_necklace == 'seymour3'", "lena_sy_collar3.webp",
        "lena_necklace == 'gift'", "lena_giftnecklace.webp",
        "lena_necklace == 'gift2'", "lena_giftnecklace2.webp", 
        "True", Null()
    ),
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
        "lena_look == 'charisma' or lena_look == 'black_dress'" , "lena_charisma1_earrings.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 1", "lenanobra.webp",
        "lena_look == 'sexy'", "lenanobra2.webp",
        "lena_look == 4", "lenabra2.webp",
        "lena_look == 'charisma'", "lenanobra2.webp",
        "lena_look == 'wits'", "lenanobra2.webp",
        "lena_look == 'athletics'", "lenanobra2.webp",
        "lena_look == 'lust'", "lena_lust1_bra.webp",
        "lena_look == 'underwear2'", "lena_underwear2_topless.webp",
        "lena_look == 2", "lenanobra.webp",
        "lena_look == 'bikini' and lena_bikini == 1", "lenabikini1_topless.webp",
        "lena_look == 'bikini' and lena_bikini == 2", "lenabikini2_topless.webp",
        "lena_look == 'bikini' and lena_bikini == 3", "lenabikini3_topless.webp",
        "True", "lenanobra.webp"
    ),
    (0, 0), ConditionSwitch( 
        "flena == 'sad' and lena_makeup == 'z'", "lenasad_mk.webp",
        "flena == 'crazy' and lena_makeup == 'z'", "lenacrazy_mk.webp",
        "flena == 'crazyslut' and lena_makeup == 'z'", "lenacrazyslut_mk.webp",
        "flena == 'crazyserious' and lena_makeup == 'z'", "lenacrazyserious_mk.webp",
        "flena == 'crazysmile' and lena_makeup == 'z'", "lenacrazysmile_mk.webp",
        "flena == 'blush' and lena_makeup == 'z'", "lenablush_mk.webp",
        "flena == 'cry' and lena_makeup == 'z'", "lenacry_mk.webp",
        "flena == 'drama' and lena_makeup == 'z'", "lenadrama_mk.webp",
        "flena == 'evil' and lena_makeup == 'z'", "lenaevil_mk.webp",
        "flena == 'flirt' and lena_makeup == 'z'", "lenaflirt_mk.webp",
        "flena == 'flirtevil' and lena_makeup == 'z'", "lenaflirtevil_mk.webp",
        "flena == 'flirtshy' and lena_makeup == 'z'", "lenaflirtshy_mk.webp",
        "flena == 'happy' and lena_makeup == 'z'", "lenahappy_mk.webp",
        "flena == 'mad' and lena_makeup == 'z'", "lenamad_mk.webp",
        "flena == 'serious' and lena_makeup == 'z'", "lenaserious_mk.webp",
        "flena == 'shy' and lena_makeup == 'z'", "lenashy_mk.webp",
        "flena == 'slut' and lena_makeup == 'z'", "lenaslut_mk.webp",
        "flena == 'slutshy' and lena_makeup == 'z'", "lenaslutshy_mk.webp",
        "flena == 'smile' and lena_makeup == 'z'", "lenasmile_mk.webp",
        "flena == 'surprise' and lena_makeup == 'z'", "lenasurprise_mk.webp",
        "flena == 'worried' and lena_makeup == 'z'", "lenaworried_mk.webp",
        "flena == 'n' and lena_makeup == 'z'", "lena_mk.webp",
        "flena == 'sad'", "lenasad.webp",
        "flena == 'crazy'", "lenacrazy.webp",
        "flena == 'crazyslut'", "lenacrazyslut.webp",
        "flena == 'crazyserious'", "lenacrazyserious.webp",
        "flena == 'crazysmile'", "lenacrazysmile.webp",
        "flena == 'blush'", "lenablush.webp",
        "flena == 'cry'", "lenacry.webp",
        "flena == 'drama'", "lenadrama.webp",
        "flena == 'evil'", "lenaevil.webp",
        "flena == 'flirt'", "lenaflirt.webp",
        "flena == 'flirtevil'", "lenaflirtevil.webp",
        "flena == 'flirtshy'", "lenaflirtshy.webp",
        "flena == 'happy'", "lenahappy.webp",
        "flena == 'mad'", "lenamad.webp",
        "flena == 'serious'", "lenaserious.webp",
        "flena == 'shy'", "lenashy.webp",
        "flena == 'slut'", "lenaslut.webp",
        "flena == 'slutshy'", "lenaslutshy.webp",
        "flena == 'smile'", "lenasmile.webp",
        "flena == 'surprise'", "lenasurprise.webp",
        "flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp"
    )
)



image lenanude = Composite(
    (640, 1080),
    (0, 0),"lenanude.webp", 
    (0, 0), ConditionSwitch( 
        "lena_makeup == 1", "lena_eyeshadow1.webp",
        "lena_makeup == 2", "lena_eyeshadow2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_necklace == 'choker'", "lena_choker.webp",
        "lena_necklace == 'choker2'", "lena_choker2.webp",
        "lena_necklace == 'seymour'", "lena_sy_collar.webp",
        "lena_necklace == 'seymour2'", "lena_sy_collar2.webp",
        "lena_necklace == 'seymour3'", "lena_sy_collar3.webp",
        "lena_necklace == 'gift'", "lena_giftnecklace.webp",
        "lena_necklace == 'gift2'", "lena_giftnecklace2.webp", 
        "True", Null()
    ),
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
        "lena_look == 'charisma' or lena_look == 'black_dress'" , "lena_charisma1_earrings.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 'lust'", "lena_lust1_stockings.webp",
        "True", Null()
    ),
    
    (0, 0), ConditionSwitch( 
        "lena_look == 'black_dress'", "lena_dress_posh_thigh.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "flena == 'sad' and lena_makeup == 'z'", "lenasad_mk.webp",
        "flena == 'crazy' and lena_makeup == 'z'", "lenacrazy_mk.webp",
        "flena == 'crazyslut' and lena_makeup == 'z'", "lenacrazyslut_mk.webp",
        "flena == 'crazyserious' and lena_makeup == 'z'", "lenacrazyserious_mk.webp",
        "flena == 'crazysmile' and lena_makeup == 'z'", "lenacrazysmile_mk.webp",
        "flena == 'blush' and lena_makeup == 'z'", "lenablush_mk.webp",
        "flena == 'cry' and lena_makeup == 'z'", "lenacry_mk.webp",
        "flena == 'drama' and lena_makeup == 'z'", "lenadrama_mk.webp",
        "flena == 'evil' and lena_makeup == 'z'", "lenaevil_mk.webp",
        "flena == 'flirt' and lena_makeup == 'z'", "lenaflirt_mk.webp",
        "flena == 'flirtevil' and lena_makeup == 'z'", "lenaflirtevil_mk.webp",
        "flena == 'flirtshy' and lena_makeup == 'z'", "lenaflirtshy_mk.webp",
        "flena == 'happy' and lena_makeup == 'z'", "lenahappy_mk.webp",
        "flena == 'mad' and lena_makeup == 'z'", "lenamad_mk.webp",
        "flena == 'serious' and lena_makeup == 'z'", "lenaserious_mk.webp",
        "flena == 'shy' and lena_makeup == 'z'", "lenashy_mk.webp",
        "flena == 'slut' and lena_makeup == 'z'", "lenaslut_mk.webp",
        "flena == 'slutshy' and lena_makeup == 'z'", "lenaslutshy_mk.webp",
        "flena == 'smile' and lena_makeup == 'z'", "lenasmile_mk.webp",
        "flena == 'surprise' and lena_makeup == 'z'", "lenasurprise_mk.webp",
        "flena == 'worried' and lena_makeup == 'z'", "lenaworried_mk.webp",
        "flena == 'n' and lena_makeup == 'z'", "lena_mk.webp",
        "flena == 'sad'", "lenasad.webp",
        "flena == 'crazy'", "lenacrazy.webp",
        "flena == 'crazyslut'", "lenacrazyslut.webp",
        "flena == 'crazyserious'", "lenacrazyserious.webp",
        "flena == 'crazysmile'", "lenacrazysmile.webp",
        "flena == 'blush'", "lenablush.webp",
        "flena == 'cry'", "lenacry.webp",
        "flena == 'drama'", "lenadrama.webp",
        "flena == 'evil'", "lenaevil.webp",
        "flena == 'flirt'", "lenaflirt.webp",
        "flena == 'flirtevil'", "lenaflirtevil.webp",
        "flena == 'flirtshy'", "lenaflirtshy.webp",
        "flena == 'happy'", "lenahappy.webp",
        "flena == 'mad'", "lenamad.webp",
        "flena == 'serious'", "lenaserious.webp",
        "flena == 'shy'", "lenashy.webp",
        "flena == 'slut'", "lenaslut.webp",
        "flena == 'slutshy'", "lenaslutshy.webp",
        "flena == 'smile'", "lenasmile.webp",
        "flena == 'surprise'", "lenasurprise.webp",
        "flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp")
    )

image lenanude2 = Composite(
    (640, 1080),
    (0, 0),"lenanude_b.webp", 
    (0, 0), ConditionSwitch( 
        "lena_makeup == 1", "lena_eyeshadow1.webp",
        "lena_makeup == 2", "lena_eyeshadow2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_necklace == 'choker'", "lena_choker.webp",
        "lena_necklace == 'choker2'", "lena_choker2.webp",
        "lena_necklace == 'seymour'", "lena_sy_collar.webp",
        "lena_necklace == 'seymour2'", "lena_sy_collar2.webp",
        "lena_necklace == 'seymour3'", "lena_sy_collar3.webp",
        "lena_necklace == 'gift'", "lena_giftnecklace.webp",
        "lena_necklace == 'gift2'", "lena_giftnecklace2.webp",
        "True", Null()
    ),
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
        "lena_look == 'charisma' or lena_look == 'black_dress'" , "lena_charisma1_earrings.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 'lust'", "lena_lust1_stockings.webp",
        "True", Null()
    ),
    
    (0, 0), ConditionSwitch( 
        "lena_look == 'black_dress'", "lena_dress_posh_thigh.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "flena == 'sad' and lena_makeup == 'z'", "lenasad_mk.webp",
        "flena == 'crazy' and lena_makeup == 'z'", "lenacrazy_mk.webp",
        "flena == 'crazyslut' and lena_makeup == 'z'", "lenacrazyslut_mk.webp",
        "flena == 'crazyserious' and lena_makeup == 'z'", "lenacrazyserious_mk.webp",
        "flena == 'crazysmile' and lena_makeup == 'z'", "lenacrazysmile_mk.webp",
        "flena == 'blush' and lena_makeup == 'z'", "lenablush_mk.webp",
        "flena == 'cry' and lena_makeup == 'z'", "lenacry_mk.webp",
        "flena == 'drama' and lena_makeup == 'z'", "lenadrama_mk.webp",
        "flena == 'evil' and lena_makeup == 'z'", "lenaevil_mk.webp",
        "flena == 'flirt' and lena_makeup == 'z'", "lenaflirt_mk.webp",
        "flena == 'flirtevil' and lena_makeup == 'z'", "lenaflirtevil_mk.webp",
        "flena == 'flirtshy' and lena_makeup == 'z'", "lenaflirtshy_mk.webp",
        "flena == 'happy' and lena_makeup == 'z'", "lenahappy_mk.webp",
        "flena == 'mad' and lena_makeup == 'z'", "lenamad_mk.webp",
        "flena == 'serious' and lena_makeup == 'z'", "lenaserious_mk.webp",
        "flena == 'shy' and lena_makeup == 'z'", "lenashy_mk.webp",
        "flena == 'slut' and lena_makeup == 'z'", "lenaslut_mk.webp",
        "flena == 'slutshy' and lena_makeup == 'z'", "lenaslutshy_mk.webp",
        "flena == 'smile' and lena_makeup == 'z'", "lenasmile_mk.webp",
        "flena == 'surprise' and lena_makeup == 'z'", "lenasurprise_mk.webp",
        "flena == 'worried' and lena_makeup == 'z'", "lenaworried_mk.webp",
        "flena == 'n' and lena_makeup == 'z'", "lena_mk.webp",
        "flena == 'sad'", "lenasad.webp",
        "flena == 'crazy'", "lenacrazy.webp",
        "flena == 'crazyslut'", "lenacrazyslut.webp",
        "flena == 'crazyserious'", "lenacrazyserious.webp",
        "flena == 'crazysmile'", "lenacrazysmile.webp",
        "flena == 'blush'", "lenablush.webp",
        "flena == 'cry'", "lenacry.webp",
        "flena == 'drama'", "lenadrama.webp",
        "flena == 'evil'", "lenaevil.webp",
        "flena == 'flirt'", "lenaflirt.webp",
        "flena == 'flirtevil'", "lenaflirtevil.webp",
        "flena == 'flirtshy'", "lenaflirtshy.webp",
        "flena == 'happy'", "lenahappy.webp",
        "flena == 'mad'", "lenamad.webp",
        "flena == 'serious'", "lenaserious.webp",
        "flena == 'shy'", "lenashy.webp",
        "flena == 'slut'", "lenaslut.webp",
        "flena == 'slutshy'", "lenaslutshy.webp",
        "flena == 'smile'", "lenasmile.webp",
        "flena == 'surprise'", "lenasurprise.webp",
        "flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp"
    )
)

image lenanude_phone = Composite(
    (640, 1080),
    (0, 0),"lenanude_phone.webp", 
    (0, 0), ConditionSwitch( 
        "lena_makeup == 1", "lena_eyeshadow1.webp",
        "lena_makeup == 2", "lena_eyeshadow2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_necklace == 'choker'", "lena_choker.webp",
        "lena_necklace == 'choker2'", "lena_choker2.webp",
        "lena_necklace == 'seymour'", "lena_sy_collar.webp",
        "lena_necklace == 'seymour2'", "lena_sy_collar2.webp",
        "lena_necklace == 'seymour3'", "lena_sy_collar3.webp",
        "lena_necklace == 'gift'", "lena_giftnecklace.webp",
        "lena_necklace == 'gift2'", "lena_giftnecklace2.webp", 
        "True", Null()
    ),
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
        "lena_look == 'charisma' or lena_look == 'black_dress'" , "lena_charisma1_earrings.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 'lust'", "lena_lust1_stockings.webp",
        "True", Null()
    ),
    
    (0, 0), ConditionSwitch( 
        "lena_look == 'black_dress'", "lena_dress_posh_thigh.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "flena == 'sad' and lena_makeup == 'z'", "lenasad_mk.webp",
        "flena == 'crazy' and lena_makeup == 'z'", "lenacrazy_mk.webp",
        "flena == 'crazyslut' and lena_makeup == 'z'", "lenacrazyslut_mk.webp",
        "flena == 'crazyserious' and lena_makeup == 'z'", "lenacrazyserious_mk.webp",
        "flena == 'crazysmile' and lena_makeup == 'z'", "lenacrazysmile_mk.webp",
        "flena == 'blush' and lena_makeup == 'z'", "lenablush_mk.webp",
        "flena == 'cry' and lena_makeup == 'z'", "lenacry_mk.webp",
        "flena == 'drama' and lena_makeup == 'z'", "lenadrama_mk.webp",
        "flena == 'evil' and lena_makeup == 'z'", "lenaevil_mk.webp",
        "flena == 'flirt' and lena_makeup == 'z'", "lenaflirt_mk.webp",
        "flena == 'flirtevil' and lena_makeup == 'z'", "lenaflirtevil_mk.webp",
        "flena == 'flirtshy' and lena_makeup == 'z'", "lenaflirtshy_mk.webp",
        "flena == 'happy' and lena_makeup == 'z'", "lenahappy_mk.webp",
        "flena == 'mad' and lena_makeup == 'z'", "lenamad_mk.webp",
        "flena == 'serious' and lena_makeup == 'z'", "lenaserious_mk.webp",
        "flena == 'shy' and lena_makeup == 'z'", "lenashy_mk.webp",
        "flena == 'slut' and lena_makeup == 'z'", "lenaslut_mk.webp",
        "flena == 'slutshy' and lena_makeup == 'z'", "lenaslutshy_mk.webp",
        "flena == 'smile' and lena_makeup == 'z'", "lenasmile_mk.webp",
        "flena == 'surprise' and lena_makeup == 'z'", "lenasurprise_mk.webp",
        "flena == 'worried' and lena_makeup == 'z'", "lenaworried_mk.webp",
        "flena == 'n' and lena_makeup == 'z'", "lena_mk.webp",
        "flena == 'sad'", "lenasad.webp",
        "flena == 'crazy'", "lenacrazy.webp",
        "flena == 'crazyslut'", "lenacrazyslut.webp",
        "flena == 'crazyserious'", "lenacrazyserious.webp",
        "flena == 'crazysmile'", "lenacrazysmile.webp",
        "flena == 'blush'", "lenablush.webp",
        "flena == 'cry'", "lenacry.webp",
        "flena == 'drama'", "lenadrama.webp",
        "flena == 'evil'", "lenaevil.webp",
        "flena == 'flirt'", "lenaflirt.webp",
        "flena == 'flirtevil'", "lenaflirtevil.webp",
        "flena == 'flirtshy'", "lenaflirtshy.webp",
        "flena == 'happy'", "lenahappy.webp",
        "flena == 'mad'", "lenamad.webp",
        "flena == 'serious'", "lenaserious.webp",
        "flena == 'shy'", "lenashy.webp",
        "flena == 'slut'", "lenaslut.webp",
        "flena == 'slutshy'", "lenaslutshy.webp",
        "flena == 'smile'", "lenasmile.webp",
        "flena == 'surprise'", "lenasurprise.webp",
        "flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp"
    )
)


image lena_jewel = Composite(
    (640, 1080),
    (0, 0),"lenanude.webp", 
    (0, 0),"lena_jewel1.webp",
    (0, 0), ConditionSwitch( 
        "lena_makeup == 1", "lena_eyeshadow1.webp",
        "lena_makeup == 2", "lena_eyeshadow2.webp",
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
        "flena == 'sad'", "lenasad.webp",
        "flena == 'crazy'", "lenacrazy.webp",
        "flena == 'crazyslut'", "lenacrazyslut.webp",
        "flena == 'crazyserious'", "lenacrazyserious.webp",
        "flena == 'crazysmile'", "lenacrazysmile.webp",
        "flena == 'blush'", "lenablush.webp",
        "flena == 'cry'", "lenacry.webp",
        "flena == 'drama'", "lenadrama.webp",
        "flena == 'evil'", "lenaevil.webp",
        "flena == 'flirt'", "lenaflirt.webp",
        "flena == 'flirtevil'", "lenaflirtevil.webp",
        "flena == 'flirtshy'", "lenaflirtshy.webp",
        "flena == 'happy'", "lenahappy.webp",
        "flena == 'mad'", "lenamad.webp",
        "flena == 'serious'", "lenaserious.webp",
        "flena == 'shy'", "lenashy.webp",
        "flena == 'slut'", "lenaslut.webp",
        "flena == 'slutshy'", "lenaslutshy.webp",
        "flena == 'smile'", "lenasmile.webp",
        "flena == 'surprise'", "lenasurprise.webp",
        "flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp"
    )
)

image lena_smoke = Composite(
    (640, 1080),
    (0, 0),"lena_smoke.webp", 
    (0, 0), ConditionSwitch( 
        "lena_makeup == 1", "lena_eyeshadow1.webp",
        "lena_makeup == 2", "lena_eyeshadow2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_necklace == 'choker'", "lena_choker.webp",
        "lena_necklace == 'choker2'", "lena_choker2.webp",
        "lena_necklace == 'seymour'", "lena_sy_collar.webp",
        "lena_necklace == 'seymour2'", "lena_sy_collar2.webp",
        "lena_necklace == 'seymour3'", "lena_sy_collar3.webp",
        "lena_necklace == 'gift'", "lena_giftnecklace.webp",
        "lena_necklace == 'gift2'", "lena_giftnecklace2.webp", 
        "True", Null()
    ),
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
        "lena_extras == 'stockings'", "lena_lust1_stockings.webp",
        "True", Null()
    ),
    
    (0, 0), ConditionSwitch( 
        "lena_look == 'black_dress'", "lena_dress_posh_thigh.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 'black_dress'", "lenamoon.webp",
        "True", Null()
    ),
    
    (0, 0), ConditionSwitch( 
        "lena_look == 1", "lena1_phone.webp",
        "lena_look == 2", "lenagym_phone.webp",
        "lena_look == 3", "lenadress1_phone.webp",
        "lena_look == 'sexy'", "lena_sexy_phone.webp",
        "lena_look == 'sexy1'", "lena_sexy1_phone.webp",
        "lena_look == 'charisma'", "lena_charisma1_phone.webp",
        "lena_look == 'wits'", "lena_wits1_phone.webp",
        "lena_look == 'athletics'", "lena_athletics1_phone.webp",
        "lena_look == 'lust'", "lena_lust1_phone.webp",
        "lena_look == 'summer'", "lena_summer_phone.webp",
        "lena_look == 4", "lenacasual_phone.webp",
        "lena_look == 'black_dress'", "lena_dress_posh3.webp",
        "lena_look == 'clubdress' and v11_lena_dress == 1", "lenadress_wits_phone.webp",
        "lena_look == 'clubdress' and v11_lena_dress == 2", "lenadress_charisma_phone.webp",
        "lena_look == 'clubdress' and v11_lena_dress == 3", "lenadress_athletics_phone.webp",
        "lena_look == 'clubdress' and v11_lena_dress == 4", "lenadress_lust_phone.webp",
        "lena_look == 'bikini' and lena_bikini == 1", "lenabikini1_phone.webp",
        "lena_look == 'bikini' and lena_bikini == 2", "lenabikini2_phone.webp",
        "lena_look == 'bikini' and lena_bikini == 3", "lenabikini3_phone.webp",

        "lena_look == 'summer2' and lena_bikini == 1", "lenabikini1b_phone.webp",
        "lena_look == 'summer2' and lena_bikini == 2", "lenabikini2b_phone.webp",
        "lena_look == 'summer2' and lena_bikini == 3", "lenabikini3aa_phone.webp",
        "lena_look == 'nymph'", "lena_nymph_smoke.webp",
        "True", "lena1_phone.webp"
    ),
    (0, 0), ConditionSwitch( 
        "lena_extras == 'nymph_shorts'", "lena_jeanshorts.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "flena == 'sad' and lena_makeup == 'z'", "lenasad_mk.webp",
        "flena == 'crazy' and lena_makeup == 'z'", "lenacrazy_mk.webp",
        "flena == 'crazyslut' and lena_makeup == 'z'", "lenacrazyslut_mk.webp",
        "flena == 'crazyserious' and lena_makeup == 'z'", "lenacrazyserious_mk.webp",
        "flena == 'crazysmile' and lena_makeup == 'z'", "lenacrazysmile_mk.webp",
        "flena == 'blush' and lena_makeup == 'z'", "lenablush_mk.webp",
        "flena == 'cry' and lena_makeup == 'z'", "lenacry_mk.webp",
        "flena == 'drama' and lena_makeup == 'z'", "lenadrama_mk.webp",
        "flena == 'evil' and lena_makeup == 'z'", "lenaevil_mk.webp",
        "flena == 'flirt' and lena_makeup == 'z'", "lenaflirt_mk.webp",
        "flena == 'flirtevil' and lena_makeup == 'z'", "lenaflirtevil_mk.webp",
        "flena == 'flirtshy' and lena_makeup == 'z'", "lenaflirtshy_mk.webp",
        "flena == 'happy' and lena_makeup == 'z'", "lenahappy_mk.webp",
        "flena == 'mad' and lena_makeup == 'z'", "lenamad_mk.webp",
        "flena == 'serious' and lena_makeup == 'z'", "lenaserious_mk.webp",
        "flena == 'shy' and lena_makeup == 'z'", "lenashy_mk.webp",
        "flena == 'slut' and lena_makeup == 'z'", "lenaslut_mk.webp",
        "flena == 'slutshy' and lena_makeup == 'z'", "lenaslutshy_mk.webp",
        "flena == 'smile' and lena_makeup == 'z'", "lenasmile_mk.webp",
        "flena == 'surprise' and lena_makeup == 'z'", "lenasurprise_mk.webp",
        "flena == 'worried' and lena_makeup == 'z'", "lenaworried_mk.webp",
        "flena == 'n' and lena_makeup == 'z'", "lena_mk.webp",
        "flena == 'sad'", "lenasad.webp",
        "flena == 'crazy'", "lenacrazy.webp",
        "flena == 'crazyslut'", "lenacrazyslut.webp",
        "flena == 'crazyserious'", "lenacrazyserious.webp",
        "flena == 'crazysmile'", "lenacrazysmile.webp",
        "flena == 'blush'", "lenablush.webp",
        "flena == 'cry'", "lenacry.webp",
        "flena == 'drama'", "lenadrama.webp",
        "flena == 'evil'", "lenaevil.webp",
        "flena == 'flirt'", "lenaflirt.webp",
        "flena == 'flirtevil'", "lenaflirtevil.webp",
        "flena == 'flirtshy'", "lenaflirtshy.webp",
        "flena == 'happy'", "lenahappy.webp",
        "flena == 'mad'", "lenamad.webp",
        "flena == 'serious'", "lenaserious.webp",
        "flena == 'shy'", "lenashy.webp",
        "flena == 'slut'", "lenaslut.webp",
        "flena == 'slutshy'", "lenaslutshy.webp",
        "flena == 'smile'", "lenasmile.webp",
        "flena == 'surprise'", "lenasurprise.webp",
        "flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp")
    )
image lenabra_smoke = Composite(
    (640, 1080),
    (0, 0),"lena_smoke.webp", 
    (0, 0), ConditionSwitch( 
        "lena_makeup == 1", "lena_eyeshadow1.webp",
        "lena_makeup == 2", "lena_eyeshadow2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_necklace == 'choker'", "lena_choker.webp",
        "lena_necklace == 'choker2'", "lena_choker2.webp",
        "lena_necklace == 'seymour'", "lena_sy_collar.webp",
        "lena_necklace == 'seymour2'", "lena_sy_collar2.webp",
        "lena_necklace == 'seymour3'", "lena_sy_collar3.webp",
        "lena_necklace == 'gift'", "lena_giftnecklace.webp",
        "lena_necklace == 'gift2'", "lena_giftnecklace2.webp", 
        "True", Null()
    ),
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
        "lena_extras == 'stockings'", "lena_lust1_stockings.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 1 and lena_lust > 5 and chapter > 5", "lenacomfy2_phone.webp",       
        "lena_look == 1", "lenacomfy_phone.webp",
        "lena_look == 2", "lenabra_phone.webp",
        "lena_look == 3", "lenabra2_phone.webp",
        "lena_look == 4", "lenabra2_phone.webp",
        "lena_look == 'sexy'", "lenabra2_phone.webp",
        "lena_look == 'sexy1'", "lenabra2_phone.webp",
        "lena_look == 'underwear2'", "lena_underwear2_phone.webp",
        "lena_look == 'charisma'", "lenabra2_phone.webp",
        "lena_look == 'wits'", "lenabra2_phone.webp",
        "lena_look == 'athletics'", "lenabra2_phone.webp",
        "lena_look == 'lust'", "lena_lust1_bra.webp",
        "lena_look == 'black_lingerie2'", "lena_lingerie1b.webp",
        "lena_look == 'black_lingerie3'", "lena_lingerie1c.webp",
        "lena_look == 'black_lingerie'", "lena_lingerie1a.webp",
        "lena_look == 'bunny'", "lena_bunny2.webp",
        "lena_look == 'udw2'", "lena_underwear2b.webp",
        "lena_look == 'summer'", "lenanobra2.webp",
        "lena_look == 'bikini' and lena_bikini == 1", "lenabikini1_phone.webp",
        "lena_look == 'bikini' and lena_bikini == 2", "lenabikini2_phone.webp",
        "lena_look == 'bikini' and lena_bikini == 3", "lenabikini3b_phone.webp", 
        "True", "lenacomfy_phone.webp"
    ),
    (0, 0), ConditionSwitch( 
        "flena == 'sad' and lena_makeup == 'z'", "lenasad_mk.webp",
        "flena == 'crazy' and lena_makeup == 'z'", "lenacrazy_mk.webp",
        "flena == 'crazyslut' and lena_makeup == 'z'", "lenacrazyslut_mk.webp",
        "flena == 'crazyserious' and lena_makeup == 'z'", "lenacrazyserious_mk.webp",
        "flena == 'crazysmile' and lena_makeup == 'z'", "lenacrazysmile_mk.webp",
        "flena == 'blush' and lena_makeup == 'z'", "lenablush_mk.webp",
        "flena == 'cry' and lena_makeup == 'z'", "lenacry_mk.webp",
        "flena == 'drama' and lena_makeup == 'z'", "lenadrama_mk.webp",
        "flena == 'evil' and lena_makeup == 'z'", "lenaevil_mk.webp",
        "flena == 'flirt' and lena_makeup == 'z'", "lenaflirt_mk.webp",
        "flena == 'flirtevil' and lena_makeup == 'z'", "lenaflirtevil_mk.webp",
        "flena == 'flirtshy' and lena_makeup == 'z'", "lenaflirtshy_mk.webp",
        "flena == 'happy' and lena_makeup == 'z'", "lenahappy_mk.webp",
        "flena == 'mad' and lena_makeup == 'z'", "lenamad_mk.webp",
        "flena == 'serious' and lena_makeup == 'z'", "lenaserious_mk.webp",
        "flena == 'shy' and lena_makeup == 'z'", "lenashy_mk.webp",
        "flena == 'slut' and lena_makeup == 'z'", "lenaslut_mk.webp",
        "flena == 'slutshy' and lena_makeup == 'z'", "lenaslutshy_mk.webp",
        "flena == 'smile' and lena_makeup == 'z'", "lenasmile_mk.webp",
        "flena == 'surprise' and lena_makeup == 'z'", "lenasurprise_mk.webp",
        "flena == 'worried' and lena_makeup == 'z'", "lenaworried_mk.webp",
        "flena == 'n' and lena_makeup == 'z'", "lena_mk.webp",
        "flena == 'sad'", "lenasad.webp",
        "flena == 'crazy'", "lenacrazy.webp",
        "flena == 'crazyslut'", "lenacrazyslut.webp",
        "flena == 'crazyserious'", "lenacrazyserious.webp",
        "flena == 'crazysmile'", "lenacrazysmile.webp",
        "flena == 'blush'", "lenablush.webp",
        "flena == 'cry'", "lenacry.webp",
        "flena == 'drama'", "lenadrama.webp",
        "flena == 'evil'", "lenaevil.webp",
        "flena == 'flirt'", "lenaflirt.webp",
        "flena == 'flirtevil'", "lenaflirtevil.webp",
        "flena == 'flirtshy'", "lenaflirtshy.webp",
        "flena == 'happy'", "lenahappy.webp",
        "flena == 'mad'", "lenamad.webp",
        "flena == 'serious'", "lenaserious.webp",
        "flena == 'shy'", "lenashy.webp",
        "flena == 'slut'", "lenaslut.webp",
        "flena == 'slutshy'", "lenaslutshy.webp",
        "flena == 'smile'", "lenasmile.webp",
        "flena == 'surprise'", "lenasurprise.webp",
        "flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp")
    )
image lenanude_smoke = Composite(
    (640, 1080),
    (0, 0),"lena_smoke.webp", 
    (0, 0), ConditionSwitch( 
        "lena_makeup == 1", "lena_eyeshadow1.webp",
        "lena_makeup == 2", "lena_eyeshadow2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_necklace == 'choker'", "lena_choker.webp",
        "lena_necklace == 'choker2'", "lena_choker2.webp",
        "lena_necklace == 'seymour'", "lena_sy_collar.webp",
        "lena_necklace == 'seymour2'", "lena_sy_collar2.webp",
        "lena_necklace == 'seymour3'", "lena_sy_collar3.webp",
        "lena_necklace == 'gift'", "lena_giftnecklace.webp",
        "lena_necklace == 'gift2'", "lena_giftnecklace2.webp", 
        "True", Null()
    ),
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
        "lena_look == 'charisma' or lena_look == 'black_dress'" , "lena_charisma1_earrings.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_look == 'lust'", "lena_lust1_stockings.webp",
        "True", Null()
    ),
    
    (0, 0), ConditionSwitch( 
        "lena_look == 'black_dress'", "lena_dress_posh_thigh.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "flena == 'sad' and lena_makeup == 'z'", "lenasad_mk.webp",
        "flena == 'crazy' and lena_makeup == 'z'", "lenacrazy_mk.webp",
        "flena == 'crazyslut' and lena_makeup == 'z'", "lenacrazyslut_mk.webp",
        "flena == 'crazyserious' and lena_makeup == 'z'", "lenacrazyserious_mk.webp",
        "flena == 'crazysmile' and lena_makeup == 'z'", "lenacrazysmile_mk.webp",
        "flena == 'blush' and lena_makeup == 'z'", "lenablush_mk.webp",
        "flena == 'cry' and lena_makeup == 'z'", "lenacry_mk.webp",
        "flena == 'drama' and lena_makeup == 'z'", "lenadrama_mk.webp",
        "flena == 'evil' and lena_makeup == 'z'", "lenaevil_mk.webp",
        "flena == 'flirt' and lena_makeup == 'z'", "lenaflirt_mk.webp",
        "flena == 'flirtevil' and lena_makeup == 'z'", "lenaflirtevil_mk.webp",
        "flena == 'flirtshy' and lena_makeup == 'z'", "lenaflirtshy_mk.webp",
        "flena == 'happy' and lena_makeup == 'z'", "lenahappy_mk.webp",
        "flena == 'mad' and lena_makeup == 'z'", "lenamad_mk.webp",
        "flena == 'serious' and lena_makeup == 'z'", "lenaserious_mk.webp",
        "flena == 'shy' and lena_makeup == 'z'", "lenashy_mk.webp",
        "flena == 'slut' and lena_makeup == 'z'", "lenaslut_mk.webp",
        "flena == 'slutshy' and lena_makeup == 'z'", "lenaslutshy_mk.webp",
        "flena == 'smile' and lena_makeup == 'z'", "lenasmile_mk.webp",
        "flena == 'surprise' and lena_makeup == 'z'", "lenasurprise_mk.webp",
        "flena == 'worried' and lena_makeup == 'z'", "lenaworried_mk.webp",
        "flena == 'n' and lena_makeup == 'z'", "lena_mk.webp",
        "flena == 'sad'", "lenasad.webp",
        "flena == 'crazy'", "lenacrazy.webp",
        "flena == 'crazyslut'", "lenacrazyslut.webp",
        "flena == 'crazyserious'", "lenacrazyserious.webp",
        "flena == 'crazysmile'", "lenacrazysmile.webp",
        "flena == 'blush'", "lenablush.webp",
        "flena == 'cry'", "lenacry.webp",
        "flena == 'drama'", "lenadrama.webp",
        "flena == 'evil'", "lenaevil.webp",
        "flena == 'flirt'", "lenaflirt.webp",
        "flena == 'flirtevil'", "lenaflirtevil.webp",
        "flena == 'flirtshy'", "lenaflirtshy.webp",
        "flena == 'happy'", "lenahappy.webp",
        "flena == 'mad'", "lenamad.webp",
        "flena == 'serious'", "lenaserious.webp",
        "flena == 'shy'", "lenashy.webp",
        "flena == 'slut'", "lenaslut.webp",
        "flena == 'slutshy'", "lenaslutshy.webp",
        "flena == 'smile'", "lenasmile.webp",
        "flena == 'surprise'", "lenasurprise.webp",
        "flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp")
    )

image lenabikini = Composite(
    (640, 1080),
    (0, 0),"lenanude.webp", 
    (0, 0), ConditionSwitch( 
        "lena_makeup == 1", "lena_eyeshadow1.webp",
        "lena_makeup == 2", "lena_eyeshadow2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_necklace == 'choker2'", "lena_choker2.webp",
        "lena_necklace == 'choker'", "lena_choker.webp",
        "lena_necklace == 'seymour'", "lena_sy_collar.webp",
        "lena_necklace == 'seymour2'", "lena_sy_collar2.webp",
        "lena_necklace == 'seymour3'", "lena_sy_collar3.webp",
        "lena_necklace == 'gift'", "lena_giftnecklace.webp",
        "lena_necklace == 'gift2'", "lena_giftnecklace2.webp", 
        "True", Null()
    ),
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
        "lena_extras == 'stockings'", "lena_lust1_stockings.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_bikini == 2" , "lenabikini2.webp",
        "lena_bikini == 3" , "lenabikini3.webp",
        "True", "lenabikini1.webp"
    ),
    (0, 0), ConditionSwitch( 
        "flena == 'sad'", "lenasad.webp",
        "flena == 'crazy'", "lenacrazy.webp",
        "flena == 'crazyslut'", "lenacrazyslut.webp",
        "flena == 'crazyserious'", "lenacrazyserious.webp",
        "flena == 'crazysmile'", "lenacrazysmile.webp",
        "flena == 'blush'", "lenablush.webp",
        "flena == 'cry'", "lenacry.webp",
        "flena == 'drama'", "lenadrama.webp",
        "flena == 'evil'", "lenaevil.webp",
        "flena == 'flirt'", "lenaflirt.webp",
        "flena == 'flirtevil'", "lenaflirtevil.webp",
        "flena == 'flirtshy'", "lenaflirtshy.webp",
        "flena == 'happy'", "lenahappy.webp",
        "flena == 'mad'", "lenamad.webp",
        "flena == 'serious'", "lenaserious.webp",
        "flena == 'shy'", "lenashy.webp",
        "flena == 'slut'", "lenaslut.webp",
        "flena == 'slutshy'", "lenaslutshy.webp",
        "flena == 'smile'", "lenasmile.webp",
        "flena == 'surprise'", "lenasurprise.webp",
        "flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp"
    )
)
image lenabikini_phone = Composite(
    (640, 1080),
    (0, 0),"lenanude_phone.webp", 
    (0, 0), ConditionSwitch( 
        "lena_makeup == 1", "lena_eyeshadow1.webp",
        "lena_makeup == 2", "lena_eyeshadow2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_necklace == 'choker2'", "lena_choker2.webp",
        "lena_necklace == 'choker'", "lena_choker.webp",
        "lena_necklace == 'seymour'", "lena_sy_collar.webp",
        "lena_necklace == 'seymour2'", "lena_sy_collar2.webp",
        "lena_necklace == 'seymour3'", "lena_sy_collar3.webp",
        "lena_necklace == 'gift'", "lena_giftnecklace.webp",
        "lena_necklace == 'gift2'", "lena_giftnecklace2.webp", 
        "True", Null()
    ),
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
        "lena_extras == 'stockings'", "lena_lust1_stockings.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "lena_bikini == 2" , "lenabikini2_phone.webp",
        "lena_bikini == 3" , "lenabikini3_phone.webp",
        "True", "lenabikini1_phone.webp"
    ),
    (0, 0), ConditionSwitch( 
        "flena == 'sad'", "lenasad.webp",
        "flena == 'crazy'", "lenacrazy.webp",
        "flena == 'crazyslut'", "lenacrazyslut.webp",
        "flena == 'crazyserious'", "lenacrazyserious.webp",
        "flena == 'crazysmile'", "lenacrazysmile.webp",
        "flena == 'blush'", "lenablush.webp",
        "flena == 'cry'", "lenacry.webp",
        "flena == 'drama'", "lenadrama.webp",
        "flena == 'evil'", "lenaevil.webp",
        "flena == 'flirt'", "lenaflirt.webp",
        "flena == 'flirtevil'", "lenaflirtevil.webp",
        "flena == 'flirtshy'", "lenaflirtshy.webp",
        "flena == 'happy'", "lenahappy.webp",
        "flena == 'mad'", "lenamad.webp",
        "flena == 'serious'", "lenaserious.webp",
        "flena == 'shy'", "lenashy.webp",
        "flena == 'slut'", "lenaslut.webp",
        "flena == 'slutshy'", "lenaslutshy.webp",
        "flena == 'smile'", "lenasmile.webp",
        "flena == 'surprise'", "lenasurprise.webp",
        "flena == 'worried'", "lenaworried.webp",
        "True", "lena.webp"
    )
)








image ian = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch(  
        "ian_fit == 1 and chapter > 9", "iannude_soft_fit.webp",
        "True", "iannude_soft.webp"),
    (0, 0), ConditionSwitch( 
        "ian_look == 1", "ian1.webp", 
        "ian_look == 2", "ian2.webp", 
        "ian_look == 3", "ian3.webp", 
        "ian_look == 'cool'", "ian_cool.webp", 
        "ian_look == 4", "ian4.webp", 
        "ian_look == 5", "ian4b.webp", 
        "ian_look == 6", "ian5.webp", 
        "ian_look == 7", "iangym.webp", 
        "ian_look == 8", "iangym_c.webp", 
        "ian_look == 'wits1'", "ian_wits1.webp",
        "ian_look == 'charisma1'", "ian_charisma1.webp",
        "ian_look == 'athletics1'", "ian_athletics1.webp",
        "ian_look == 'lust1'", "ian_lust1.webp",
        "ian_look == 'gi'", "ian_gi.webp", 
        "ian_look == 'mma'", "ian_mma.webp", 
        "ian_look == 'summer' and ian_summer_look == 'wits'", "ian_summer_wits.webp",
        "ian_look == 'summer' and ian_summer_look == 'charisma'", "ian_summer_charisma.webp",
        "ian_look == 'summer' and ian_summer_look == 'athletics'", "ian_summer_athletics.webp",
        "ian_look == 'summer' and ian_summer_look == 'lust'", "ian_summer_lust.webp",
        "ian_look == 'summer2' and ian_summer_look == 'lust'", "ian_summer_lust2.webp",
        "ian_look == 'swim'", "ian_swim.webp", 
        "True", "ian1.webp"),
    (0, 0), ConditionSwitch( 
        "fian == 'sad'", "iansad.webp",
        "fian == 'blush'", "ianblush.webp",
        "fian == 'confident'", "ianconfident.webp",
        "fian == 'cry'", "iancry.webp",
        "fian == 'depress'", "iandepress.webp",
        "fian == 'disgusted'", "iandisgusted.webp",
        "fian == 'evil'", "ianevil.webp",
        "fian == 'furious'", "ianfurious.webp",
        "fian == 'happy'", "ianhappy.webp",
        "fian == 'insecure'", "ianinsecure.webp",
        "fian == 'mad'", "ianmad.webp",
        "fian == 'serious'", "ianserious.webp",
        "fian == 'smile'", "iansmile.webp",
        "fian == 'surprise'", "iansurprise.webp",
        "fian == 'worried'", "ianworried.webp",
        "fian == 'shy'", "ianshy.webp",
        "True", "ian.webp"),
    (0, 0), ConditionSwitch( 
        "ian_headgear == True", "headgear.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "ian_hurt == 1", "ian_hurt.webp",
        "ian_hurt == 3", "ian_hurt3.webp",
        "ian_hurt == 4", "ian_hurt4.webp",
        "ian_hurt == 2", "ian_hurt2.webp",
        "True", Null()
    )
    )

image ian_phone = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch(  
        "ian_fit == 1 and chapter > 9", "iannude_phone_fit.webp",
        "True", "iannude_phone.webp"
        ),
    (0, 0), ConditionSwitch( 
        "ian_look == 1", "ian1_phone.webp", 
        "ian_look == 2", "ian2_phone.webp", 
        "ian_look == 3", "ian3_phone.webp", 
        "ian_look == 'cool'", "ian_cool_phone.webp", 
        "ian_look == 4", "ian4_phone.webp", 
        "ian_look == 5", "ian4b_phone.webp", 
        "ian_look == 6", "ian5_phone.webp", 
        "ian_look == 'wits1'", "ian_wits1_phone.webp",
        "ian_look == 'charisma1'", "ian_charisma1_phone.webp",
        "ian_look == 'athletics1'", "ian_athletics1_phone.webp",
        "ian_look == 'lust1'", "ian_lust1_phone.webp",
        "ian_look == 7", "iangym.webp", 
        "ian_look == 'summer' and ian_summer_look == 'wits'", "ian_summer_wits_phone.webp",
        "ian_look == 'summer' and ian_summer_look == 'charisma'", "ian_summer_charisma_phone.webp",
        "ian_look == 'summer' and ian_summer_look == 'athletics'", "ian_summer_athletics.webp",
        "ian_look == 'summer' and ian_summer_look == 'lust'", "ian_summer_lust_phone.webp",
        "ian_look == 'summer2' and ian_summer_look == 'lust'", "ian_summer_lust2.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "fian == 'sad'", "iansad.webp",
        "fian == 'blush'", "ianblush.webp",
        "fian == 'confident'", "ianconfident.webp",
        "fian == 'cry'", "iancry.webp",
        "fian == 'depress'", "iandepress.webp",
        "fian == 'disgusted'", "iandisgusted.webp",
        "fian == 'evil'", "ianevil.webp",
        "fian == 'furious'", "ianfurious.webp",
        "fian == 'happy'", "ianhappy.webp",
        "fian == 'insecure'", "ianinsecure.webp",
        "fian == 'mad'", "ianmad.webp",
        "fian == 'serious'", "ianserious.webp",
        "fian == 'smile'", "iansmile.webp",
        "fian == 'surprise'", "iansurprise.webp",
        "fian == 'worried'", "ianworried.webp",
        "fian == 'shy'", "ianshy.webp",
        "True", "ian.webp"),
    (0, 0), ConditionSwitch( 
        "ian_headgear == True", "headgear.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "ian_hurt == 1", "ian_hurt.webp",
        "ian_hurt == 3", "ian_hurt3.webp",
        "ian_hurt == 4", "ian_hurt4.webp",
        "ian_hurt == 2", "ian_hurt2.webp",
        "True", Null()
    )
    )

image ian_smoke = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch(  
        "ian_fit == 1 and chapter > 9", "iannude_smoke_fit.webp",
        "True", "iannude_smoke.webp"),
    (0, 0), ConditionSwitch( 
        "ian_look == 1", "ian1_smoke.webp", 
        "ian_look == 2", "ian2_smoke.webp", 
        "ian_look == 'cool'", "ian_cool_smoke.webp", 
        "ian_look == 'summer' and ian_summer_look == 'wits'", "ian_summer_wits_smoke.webp",
        "ian_look == 'summer' and ian_summer_look == 'charisma'", "ian_summer_charisma_smoke.webp",
        "ian_look == 'summer' and ian_summer_look == 'athletics'", "ian_summer_athletics.webp",
        "ian_look == 'summer' and ian_summer_look == 'lust'", "ian_summer_lust_smoke.webp",
        "True", "ian2_smoke.webp"),
    (0, 0), ConditionSwitch( 
        "fian == 'sad'", "iansad.webp",
        "fian == 'blush'", "ianblush.webp",
        "fian == 'confident'", "ianconfident.webp",
        "fian == 'cry'", "iancry.webp",
        "fian == 'depress'", "iandepress.webp",
        "fian == 'disgusted'", "iandisgusted.webp",
        "fian == 'evil'", "ianevil.webp",
        "fian == 'furious'", "ianfurious.webp",
        "fian == 'happy'", "ianhappy.webp",
        "fian == 'insecure'", "ianinsecure.webp",
        "fian == 'mad'", "ianmad.webp",
        "fian == 'serious'", "ianserious.webp",
        "fian == 'smile'", "iansmile.webp",
        "fian == 'surprise'", "iansurprise.webp",
        "fian == 'worried'", "ianworried.webp",
        "fian == 'shy'", "ianshy.webp",
        "True", "ian.webp"),
    (0, 0), ConditionSwitch( 
        "ian_hurt == 1", "ian_hurt.webp",
        "ian_hurt == 3", "ian_hurt3.webp",
        "ian_hurt == 4", "ian_hurt4.webp",
        "ian_hurt == 2", "ian_hurt2.webp",
        "True", Null()
    )
    )



image ianunder = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch(  
        "ian_fit == 1 and chapter > 9", "iannude_soft_fit.webp",
        "True", "iannude_soft.webp"),
    (0, 0), ConditionSwitch( 
        "ian_look == 1", "ian2.webp",
        "ian_look == 2", "iannoshirt.webp",
        "ian_look == '3b'", "iannoshirt2.webp",
        "ian_look == 3", "ianunder.webp",
        "ian_look == 'cool'", "ian_coolb.webp",
        "ian_look == 4", "ian4b.webp",
        "ian_look == 5", "ian4b.webp",
        "ian_look == 6", "ian5b.webp",
        "ian_look == 'wits1'", "iannoshirt3.webp",
        "ian_look == 'charisma1'", "iannoshirt3.webp",
        "ian_look == 'athletics1'", "iannoshirt3.webp",
        "ian_look == 'lust1'", "iannoshirt3.webp",
        "ian_look == 'pantless'", "ian1_pantless.webp",
        "ian_look == 7", "iangym_b.webp",
        "ian_look == 'summer' and ian_summer_look == 'wits'", "ian_summer_wits_pants.webp",
        "ian_look == 'summer' and ian_summer_look == 'charisma'", "ian_summer_charisma_pants.webp",
        "ian_look == 'summer' and ian_summer_look == 'athletics'", "ian_summer_athletics_pants.webp",
        "ian_look == 'summer' and ian_summer_look == 'lust'", "ian_summer_lust_pants.webp",
        "True", "ian2.webp"),
    (0, 0), ConditionSwitch( 
        "fian == 'sad'", "iansad.webp",
        "fian == 'blush'", "ianblush.webp",
        "fian == 'confident'", "ianconfident.webp",
        "fian == 'cry'", "iancry.webp",
        "fian == 'depress'", "iandepress.webp",
        "fian == 'disgusted'", "iandisgusted.webp",
        "fian == 'evil'", "ianevil.webp",
        "fian == 'furious'", "ianfurious.webp",
        "fian == 'happy'", "ianhappy.webp",
        "fian == 'insecure'", "ianinsecure.webp",
        "fian == 'mad'", "ianmad.webp",
        "fian == 'serious'", "ianserious.webp",
        "fian == 'smile'", "iansmile.webp",
        "fian == 'surprise'", "iansurprise.webp",
        "fian == 'worried'", "ianworried.webp",
        "fian == 'shy'", "ianshy.webp",
        "True", "ian.webp"),
    (0, 0), ConditionSwitch ( 
        "ian_hurt == 1", "ian_hurt.webp",
        "ian_hurt == 3", "ian_hurt3.webp",
        "ian_hurt == 4", "ian_hurt4.webp",
        "ian_hurt == 2", "ian_hurt2.webp",
        "True", Null()
    )
    )

image ianunder_phone = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch(  
        "ian_fit == 1 and chapter > 9", "iannude_phone_fit.webp",
        "True", "iannude_phone.webp"),
    (0, 0), ConditionSwitch( 
        "ian_look == 1", "ian2_phone.webp",
        "ian_look == 2", "iannoshirt.webp",
        "ian_look == 3", "ianunder.webp",
        "ian_look == 'cool'", "ian_coolb.webp",
        "ian_look == 'topless'", "iannoshirt.webp",
        "ian_look == 4", "ian4b.webp",
        "ian_look == 5", "ian4b.webp",
        "ian_look == 6", "ian5b.webp",
        "ian_look == 7", "iangym_b.webp",
        "ian_look == 'wits1'", "iannoshirt3.webp",
        "ian_look == 'charisma1'", "iannoshirt3.webp",
        "ian_look == 'athletics1'", "iannoshirt3.webp",
        "ian_look == 'lust1'", "iannoshirt3.webp",
        "ian_look == 'summer' and ian_summer_look == 'wits'", "ian_summer_wits_pants.webp",
        "ian_look == 'summer' and ian_summer_look == 'charisma'", "ian_summer_charisma_pants.webp",
        "ian_look == 'summer' and ian_summer_look == 'athletics'", "ian_summer_athletics_pants.webp",
        "ian_look == 'summer' and ian_summer_look == 'lust'", "ian_summer_lust_pants.webp",
        "True", "ian2_phone.webp"),
    (0, 0), ConditionSwitch( 
        "fian == 'sad'", "iansad.webp",
        "fian == 'blush'", "ianblush.webp",
        "fian == 'confident'", "ianconfident.webp",
        "fian == 'cry'", "iancry.webp",
        "fian == 'depress'", "iandepress.webp",
        "fian == 'disgusted'", "iandisgusted.webp",
        "fian == 'evil'", "ianevil.webp",
        "fian == 'furious'", "ianfurious.webp",
        "fian == 'happy'", "ianhappy.webp",
        "fian == 'insecure'", "ianinsecure.webp",
        "fian == 'mad'", "ianmad.webp",
        "fian == 'serious'", "ianserious.webp",
        "fian == 'smile'", "iansmile.webp",
        "fian == 'surprise'", "iansurprise.webp",
        "fian == 'worried'", "ianworried.webp",
        "fian == 'shy'", "ianshy.webp",
        "True", "ian.webp"),
    (0, 0), ConditionSwitch ( 
        "ian_hurt == 1", "ian_hurt.webp",
        "ian_hurt == 3", "ian_hurt3.webp",
        "ian_hurt == 4", "ian_hurt4.webp",
        "ian_hurt == 2", "ian_hurt2.webp",
        "True", Null()
    )
    )
image ianunder_smoke = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch(  
        "ian_fit == 1 and chapter > 9", "iannude_smoke_fit.webp",
        "True", "iannude_smoke.webp"),
    (0, 0), ConditionSwitch( 
        "ian_look == 1", "ian2.webp",
        "ian_look == 2", "iannoshirt.webp",
        "ian_look == '3b'", "iannoshirt2.webp",
        "ian_look == 3", "ianunder.webp",
        "ian_look == 'cool'", "ian_coolb.webp",
        "ian_look == 4", "ian4b.webp",
        "ian_look == 5", "ian4b.webp",
        "ian_look == 6", "ian5b.webp",
        "ian_look == 'wits1'", "iannoshirt3.webp",
        "ian_look == 'charisma1'", "iannoshirt3.webp",
        "ian_look == 'athletics1'", "iannoshirt3.webp",
        "ian_look == 'lust1'", "iannoshirt3.webp",
        "ian_look == 'pantless'", "ian1_pantless.webp",
        "ian_look == 7", "iangym_b.webp",
        "ian_look == 'summer' and ian_summer_look == 'wits'", "ian_summer_wits_pants.webp",
        "ian_look == 'summer' and ian_summer_look == 'charisma'", "ian_summer_charisma_pants.webp",
        "ian_look == 'summer' and ian_summer_look == 'athletics'", "ian_summer_athletics_pants.webp",
        "ian_look == 'summer' and ian_summer_look == 'lust'", "ian_summer_lust_pants.webp",
        "True", "ian2.webp"),
    (0, 0), ConditionSwitch( 
        "fian == 'sad'", "iansad.webp",
        "fian == 'blush'", "ianblush.webp",
        "fian == 'confident'", "ianconfident.webp",
        "fian == 'cry'", "iancry.webp",
        "fian == 'depress'", "iandepress.webp",
        "fian == 'disgusted'", "iandisgusted.webp",
        "fian == 'evil'", "ianevil.webp",
        "fian == 'furious'", "ianfurious.webp",
        "fian == 'happy'", "ianhappy.webp",
        "fian == 'insecure'", "ianinsecure.webp",
        "fian == 'mad'", "ianmad.webp",
        "fian == 'serious'", "ianserious.webp",
        "fian == 'smile'", "iansmile.webp",
        "fian == 'surprise'", "iansurprise.webp",
        "fian == 'worried'", "ianworried.webp",
        "fian == 'shy'", "ianshy.webp",
        "True", "ian.webp"),
    (0, 0), ConditionSwitch( 
        "ian_hurt == 1", "ian_hurt.webp",
        "ian_hurt == 3", "ian_hurt3.webp",
        "ian_hurt == 4", "ian_hurt4.webp",
        "ian_hurt == 2", "ian_hurt2.webp",
        "True", Null()
    )
    )


image ianpantless = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch(  
        "ian_fit == 1 and chapter > 9", "iannude_fit.webp",
        "True", "iannude.webp"),
    (0, 0), ConditionSwitch( 
        "ian_look == 1", "ian1_pantless.webp",
        "ian_look == 2", "ian2_pantless.webp",
        "ian_look == 3", "ian3_pantless.webp", 
        "ian_look == 'cool'", "ian_cool_shirt.webp",
        "ian_look == 'pantless'", "ian1_pantless.webp",
        "ian_look == 'wits1'", "ian_wits1.webp", 
        "ian_look == 'charisma1'", "ian_charisma1.webp", 
        "ian_look == 'athletics1'", "ian_athletics1.webp", 
        "ian_look == 'lust1'", "ian_lust1.webp", 
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "fian == 'sad'", "iansad.webp",
        "fian == 'blush'", "ianblush.webp",
        "fian == 'confident'", "ianconfident.webp",
        "fian == 'cry'", "iancry.webp",
        "fian == 'depress'", "iandepress.webp",
        "fian == 'disgusted'", "iandisgusted.webp",
        "fian == 'evil'", "ianevil.webp",
        "fian == 'furious'", "ianfurious.webp",
        "fian == 'happy'", "ianhappy.webp",
        "fian == 'insecure'", "ianinsecure.webp",
        "fian == 'mad'", "ianmad.webp",
        "fian == 'serious'", "ianserious.webp",
        "fian == 'smile'", "iansmile.webp",
        "fian == 'surprise'", "iansurprise.webp",
        "fian == 'worried'", "ianworried.webp",
        "fian == 'shy'", "ianshy.webp",
        "True", "ian.webp"),
    (0, 0), ConditionSwitch ( 
        "ian_hurt == 1", "ian_hurt.webp",
        "ian_hurt == 3", "ian_hurt3.webp",
        "ian_hurt == 4", "ian_hurt4.webp",
        "ian_hurt == 2", "ian_hurt2.webp",
        "True", Null()
    )
    )

image ianpantless2 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch(  
        "ian_fit == 1 and chapter > 9", "iannude_soft_fit.webp",
        "True", "iannude_soft.webp"),
    (0, 0), ConditionSwitch( 
        "ian_look == 1", "ian1_pantless.webp",
        "ian_look == 2", "ian2_pantless.webp",
        "ian_look == 3", "ian3_pantless.webp", 
        "ian_look == 'cool'", "ian_cool_shirt.webp",
        "ian_look == 'pantless'", "ian1_pantless.webp",
        "ian_look == 'wits1'", "ian_wits1.webp", 
        "ian_look == 'charisma1'", "ian_charisma1.webp", 
        "ian_look == 'athletics1'", "ian_athletics1.webp", 
        "ian_look == 'lust1'", "ian_lust1.webp", 
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "fian == 'sad'", "iansad.webp",
        "fian == 'blush'", "ianblush.webp",
        "fian == 'confident'", "ianconfident.webp",
        "fian == 'cry'", "iancry.webp",
        "fian == 'depress'", "iandepress.webp",
        "fian == 'disgusted'", "iandisgusted.webp",
        "fian == 'evil'", "ianevil.webp",
        "fian == 'furious'", "ianfurious.webp",
        "fian == 'happy'", "ianhappy.webp",
        "fian == 'insecure'", "ianinsecure.webp",
        "fian == 'mad'", "ianmad.webp",
        "fian == 'serious'", "ianserious.webp",
        "fian == 'smile'", "iansmile.webp",
        "fian == 'surprise'", "iansurprise.webp",
        "fian == 'worried'", "ianworried.webp",
        "fian == 'shy'", "ianshy.webp",
        "True", "ian.webp"),
    (0, 0), ConditionSwitch ( 
        "ian_hurt == 1", "ian_hurt.webp",
        "ian_hurt == 3", "ian_hurt3.webp",
        "ian_hurt == 4", "ian_hurt4.webp",
        "ian_hurt == 2", "ian_hurt2.webp",
        "True", Null()
    )
    )


image iannude = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch(  
        "ian_fit == 1 and chapter > 9", "iannude_fit.webp",
        "True", "iannude.webp"),
    (0, 0), ConditionSwitch( 
        "ian_look == 'pantless'", "ian1_pantless.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "fian == 'sad'", "iansad.webp",
        "fian == 'blush'", "ianblush.webp",
        "fian == 'confident'", "ianconfident.webp",
        "fian == 'cry'", "iancry.webp",
        "fian == 'depress'", "iandepress.webp",
        "fian == 'disgusted'", "iandisgusted.webp",
        "fian == 'evil'", "ianevil.webp",
        "fian == 'furious'", "ianfurious.webp",
        "fian == 'happy'", "ianhappy.webp",
        "fian == 'insecure'", "ianinsecure.webp",
        "fian == 'mad'", "ianmad.webp",
        "fian == 'serious'", "ianserious.webp",
        "fian == 'smile'", "iansmile.webp",
        "fian == 'surprise'", "iansurprise.webp",
        "fian == 'worried'", "ianworried.webp",
        "fian == 'shy'", "ianshy.webp",
        "True", "ian.webp"),
    (0, 0), ConditionSwitch ( 
        "ian_hurt == 1", "ian_hurt.webp",
        "ian_hurt == 3", "ian_hurt3.webp",
        "ian_hurt == 4", "ian_hurt4.webp",
        "ian_hurt == 2", "ian_hurt2.webp",
        "True", Null()
    )
    )

image iannude_phone = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch(  
        "ian_fit == 1 and chapter > 9", "iannude_phone_fit.webp",
        "True", "iannude_phone.webp"),
    (0, 0), ConditionSwitch( 
        "fian == 'sad'", "iansad.webp",
        "fian == 'blush'", "ianblush.webp",
        "fian == 'confident'", "ianconfident.webp",
        "fian == 'cry'", "iancry.webp",
        "fian == 'depress'", "iandepress.webp",
        "fian == 'disgusted'", "iandisgusted.webp",
        "fian == 'evil'", "ianevil.webp",
        "fian == 'furious'", "ianfurious.webp",
        "fian == 'happy'", "ianhappy.webp",
        "fian == 'insecure'", "ianinsecure.webp",
        "fian == 'mad'", "ianmad.webp",
        "fian == 'serious'", "ianserious.webp",
        "fian == 'smile'", "iansmile.webp",
        "fian == 'surprise'", "iansurprise.webp",
        "fian == 'worried'", "ianworried.webp",
        "fian == 'shy'", "ianshy.webp",
        "True", "ian.webp"),
    (0, 0), ConditionSwitch ( 
        "ian_hurt == 1", "ian_hurt.webp",
        "ian_hurt == 3", "ian_hurt3.webp",
        "ian_hurt == 4", "ian_hurt4.webp",
        "ian_hurt == 2", "ian_hurt2.webp",
        "True", Null()
    )
    )

image iannude2 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch(  
        "ian_fit == 1 and chapter > 9", "iannude_soft_fit.webp",
        "True", "iannude_soft.webp"),
    (0, 0), ConditionSwitch( 
        "fian == 'sad'", "iansad.webp",
        "fian == 'blush'", "ianblush.webp",
        "fian == 'confident'", "ianconfident.webp",
        "fian == 'cry'", "iancry.webp",
        "fian == 'depress'", "iandepress.webp",
        "fian == 'disgusted'", "iandisgusted.webp",
        "fian == 'evil'", "ianevil.webp",
        "fian == 'furious'", "ianfurious.webp",
        "fian == 'happy'", "ianhappy.webp",
        "fian == 'insecure'", "ianinsecure.webp",
        "fian == 'mad'", "ianmad.webp",
        "fian == 'serious'", "ianserious.webp",
        "fian == 'smile'", "iansmile.webp",
        "fian == 'surprise'", "iansurprise.webp",
        "fian == 'worried'", "ianworried.webp",
        "fian == 'shy'", "ianshy.webp",
        "True", "ian.webp"),
    (0, 0), ConditionSwitch ( 
        "ian_hurt == 1", "ian_hurt.webp",
        "ian_hurt == 3", "ian_hurt3.webp",
        "ian_hurt == 4", "ian_hurt4.webp",
        "ian_hurt == 2", "ian_hurt2.webp",
        "True", Null()
    )
    )








image alison = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "alison_look == 'cool'", "alison_cool.webp",
        "alison_look == 'lingerie'", "alison_lingerie.webp",
        "alison_look == 'lingerie2'", "alison_lingerie2.webp",
        "alison_look == 'dress'", "alison3.webp",
        "alison_look == 'bimbo'", "alison4.webp",
        "alison_look == 1", "alison1.webp",
        "alison_look == 2", "alison2.webp",
        "alison_look == 'summer'", "alison5.webp",
        "True", "alison1.webp"
    ),
    (0, 0), ConditionSwitch( 
        "alison_makeup > 0 and (falison == 'mad' or falison == 'serious' or falison == 'flirt' or falison == 'smile' or falison == 'slut')", "alison_makeupb.webp",
        "alison_makeup > 0 and (falison == 'n' or falison == 'blush' or falison == 'sad' or falison == 'surprise')", "alison_makeup.webp",
        "True", Null()
    ),
    
    
    
    
    (0, 0), ConditionSwitch( 
        "alison_necklace", "alison_necklace.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "chapter > 10 and alison_blonde > 0.5", "alison_blonde.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "falison == 'sad'", "alisonsad.webp",
        "falison == 'smile'", "alisonsmile.webp",
        "falison == 'mad'", "alisonmad.webp",
        "falison == 'serious'", "alisonserious.webp",
        "falison == 'surprise'", "alisonsurprise.webp",
        "falison == 'flirt'", "alisonflirt.webp",
        "falison == 'blush'", "alisonblush.webp",
        "falison == 'slut'", "alisonslut.webp",
        "True", "alison.webp"
    )
)

image alison_phone = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "alison_look == 'cool'", "alison_cool_phone.webp",
        "alison_look == 'lingerie'", "alison_lingerie.webp",
        "alison_look == 1", "alison1_phone.webp",
        "alison_look == 2", "alison2_phone.webp",
        "alison_look == 'summer'", "alison5_phone.webp",
        "True", "alison1_phone.webp"
    ),
    
    
    
    
    (0, 0), ConditionSwitch( 
        "alison_makeup > 0 and (falison == 'mad' or falison == 'serious' or falison == 'flirt' or falison == 'smile' or falison == 'slut')", "alison_makeupb.webp",
        "alison_makeup > 0 and (falison == 'n' or falison == 'blush' or falison == 'sad' or falison == 'surprise')", "alison_makeup.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "alison_necklace", "alison_necklace.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "chapter > 10 and alison_blonde > 0.5", "alison_blonde.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "falison == 'sad'", "alisonsad.webp",
        "falison == 'smile'", "alisonsmile.webp",
        "falison == 'mad'", "alisonmad.webp",
        "falison == 'serious'", "alisonserious.webp",
        "falison == 'surprise'", "alisonsurprise.webp",
        "falison == 'flirt'", "alisonflirt.webp",
        "falison == 'blush'", "alisonblush.webp",
        "falison == 'slut'", "alisonslut.webp",
        "True", "alison.webp"
    )
)



image alisonnude = Composite(
    (640, 1080),
    (0, 0), "alisonnude.webp",
    (0, 0), ConditionSwitch( 
        "alison_nipple", "alison_nips.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "alison_makeup > 0 and (falison == 'mad' or falison == 'serious' or falison == 'flirt' or falison == 'smile' or falison == 'slut')", "alison_makeupb.webp",
        "alison_makeup > 0 and (falison == 'n' or falison == 'blush' or falison == 'sad' or falison == 'surprise')", "alison_makeup.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "alison_necklace", "alison_necklace.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "chapter > 10 and alison_blonde > 0.5", "alison_blonde.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "falison == 'sad'", "alisonsad.webp",
        "falison == 'smile'", "alisonsmile.webp",
        "falison == 'mad'", "alisonmad.webp",
        "falison == 'serious'", "alisonserious.webp",
        "falison == 'surprise'", "alisonsurprise.webp",
        "falison == 'flirt'", "alisonflirt.webp",
        "falison == 'blush'", "alisonblush.webp",
        "falison == 'slut'", "alisonslut.webp",
        "True", "alison.webp"
    )
)
image alisonnude_phone = Composite(
    (640, 1080),
    (0, 0), "alisonnude_phone.webp",
    (0, 0), ConditionSwitch( 
        "alison_nipple", "alison_nips.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "alison_makeup > 0 and (falison == 'mad' or falison == 'serious' or falison == 'flirt' or falison == 'smile' or falison == 'slut')", "alison_makeupb.webp",
        "alison_makeup > 0 and (falison == 'n' or falison == 'blush' or falison == 'sad' or falison == 'surprise')", "alison_makeup.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "chapter > 10 and alison_blonde > 0.5", "alison_blonde.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "alison_necklace", "alison_necklace.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "falison == 'sad'", "alisonsad.webp",
        "falison == 'smile'", "alisonsmile.webp",
        "falison == 'mad'", "alisonmad.webp",
        "falison == 'serious'", "alisonserious.webp",
        "falison == 'surprise'", "alisonsurprise.webp",
        "falison == 'flirt'", "alisonflirt.webp",
        "falison == 'blush'", "alisonblush.webp",
        "falison == 'slut'", "alisonslut.webp",
        "True", "alison.webp"
    )
)



image alisonbra = Composite(
    (640, 1080),
    (0, 0), "alisonbra.webp",
    
    
    
    
    (0, 0), ConditionSwitch( 
        "alison_makeup > 0 and (falison == 'mad' or falison == 'serious' or falison == 'flirt' or falison == 'smile' or falison == 'slut')", "alison_makeupb.webp",
        "alison_makeup > 0 and (falison == 'n' or falison == 'blush' or falison == 'sad' or falison == 'surprise')", "alison_makeup.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "chapter > 10 and alison_blonde > 0.5", "alison_blonde.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "alison_necklace", "alison_necklace.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "falison == 'sad'", "alisonsad.webp",
        "falison == 'smile'", "alisonsmile.webp",
        "falison == 'mad'", "alisonmad.webp",
        "falison == 'serious'", "alisonserious.webp",
        "falison == 'surprise'", "alisonsurprise.webp",
        "falison == 'flirt'", "alisonflirt.webp",
        "falison == 'blush'", "alisonblush.webp",
        "falison == 'slut'", "alisonslut.webp",
        "True", "alison.webp"
    )
)


image alison2 = Composite(
    (640, 1080),
    (0, 0), "alison3b.webp",
    
    
    
    
    (0, 0), ConditionSwitch( 
        "chapter > 10 and alison_blonde > 0.5", "alison_blonde.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "alison_necklace", "alison_necklace.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "falison == 'sad'", "alisonsad.webp",
        "falison == 'smile'", "alisonsmile.webp",
        "falison == 'mad'", "alisonmad.webp",
        "falison == 'serious'", "alisonserious.webp",
        "falison == 'surprise'", "alisonsurprise.webp",
        "falison == 'flirt'", "alisonflirt.webp",
        "falison == 'blush'", "alisonblush.webp",
        "falison == 'slut'", "alisonslut.webp",
        "True", "alison.webp"
    ),
    (0, 0), ConditionSwitch( 
        "alison_makeup > 0 and (falison == 'mad' or falison == 'serious' or falison == 'flirt' or falison == 'smile' or falison == 'slut')", "alison_makeupb.webp",
        "alison_makeup > 0 and (falison == 'n' or falison == 'blush' or falison == 'sad' or falison == 'surprise')", "alison_makeup.webp",
        "True", Null()
    )
)







image axel = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "axel_look == 1", "axel1.webp",
        "axel_look == 2", "axel2.webp",
        "True", "axel1.webp"
    ),
    (0, 0), ConditionSwitch( 
        "faxel == 'furious'", "axelfurious.webp",
        "faxel == 'happy'", "axelhappy.webp",
        "faxel == 'mad'", "axelmad.webp",
        "faxel == 'sad'", "axelsad.webp",
        "faxel == 'smile'", "axelsmile.webp",
        "faxel == 'cry'", "axelcry.webp", 
        "True", "axel.webp")
    )



image axel_topless = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "axel_look == 1", "axel1_topless.webp",
        "axel_look == 2", "axel2_topless.webp",
        "True", "axel1_topless.webp"
    ),
    (0, 0), ConditionSwitch( 
        "faxel == 'furious'", "axelfurious.webp",
        "faxel == 'happy'", "axelhappy.webp",
        "faxel == 'mad'", "axelmad.webp",
        "faxel == 'sad'", "axelsad.webp",
        "faxel == 'smile'", "axelsmile.webp",
        "faxel == 'cry'", "axelcry.webp", 
        "True", "axel.webp")
    )



image axelnude = Composite(
    (640, 1080),
    (0, 0), "axelnude.webp",
    (0, 0), ConditionSwitch( 
        "faxel == 'furious'", "axelfurious.webp",
        "faxel == 'happy'", "axelhappy.webp",
        "faxel == 'mad'", "axelmad.webp",
        "faxel == 'sad'", "axelsad.webp",
        "faxel == 'smile'", "axelsmile.webp",
        "faxel == 'cry'", "axelcry.webp", 
        "True", "axel.webp")
    )









image cherry = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "cherry_look == 1", "cherry1.webp",
        "cherry_look == 2", "cherry_dress.webp",
        "True", "cherry1.webp"
    ),
    (0, 0), ConditionSwitch( 
        "cherry_stockings == True", "cherry_stockings.webp", 
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "fcherry == 'mad'", "cherrymad.webp",
        "fcherry == 'blush'", "cherryblush.webp",
        "fcherry == 'sad'", "cherrysad.webp",
        "fcherry == 'cry'", "cherrycry.webp",
        "fcherry == 'smile'", "cherrysmile.webp",
        "fcherry == 'happy'", "cherryhappy.webp",
        "fcherry == 'flirt'", "cherryflirt.webp",
        "True", "cherry.webp")
    )



image cherrybra = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "cherry_look == 1", "cherrybra.webp",
        "cherry_look == 3", "cherry_shorts.webp",
        "cherry_look == 2", "cherrybra_b.webp",
        "True", "cherrybra.webp"
    ),
    (0, 0), ConditionSwitch( 
        "cherry_stockings == True", "cherry_stockings.webp", 
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "fcherry == 'mad'", "cherrymad.webp",
        "fcherry == 'blush'", "cherryblush.webp",
        "fcherry == 'sad'", "cherrysad.webp",
        "fcherry == 'cry'", "cherrycry.webp",
        "fcherry == 'smile'", "cherrysmile.webp",
        "fcherry == 'happy'", "cherryhappy.webp",
        "fcherry == 'flirt'", "cherryflirt.webp",
        "True", "cherry.webp")
    )



image cherrynude = Composite(
    (640, 1080),
    (0, 0), "cherrynude.webp",
    (0, 0), ConditionSwitch( 
        "cherry_stockings == True", "cherry_stockings.webp", 
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "fcherry == 'mad'", "cherrymad.webp",
        "fcherry == 'blush'", "cherryblush.webp",
        "fcherry == 'sad'", "cherrysad.webp",
        "fcherry == 'cry'", "cherrycry.webp",
        "fcherry == 'smile'", "cherrysmile.webp",
        "fcherry == 'happy'", "cherryhappy.webp",
        "fcherry == 'flirt'", "cherryflirt.webp",
        "True", "cherry.webp")
    )








image cindy = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "cindy_look == 'summer'", "cindy_summer.webp",
        "cindy_look == 'posh'", "cindy_posh.webp",
        "cindy_look == 'party'", "cindy_party.webp",
        "cindy_look == 2", "cindy4.webp",
        "True", "cindy1.webp"
    ),
    (0, 0), ConditionSwitch( 
        "cindy_necklace == 'gift'", "cindy_necklace.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "cindy_look == 'summer'", "cindy_earrings.webp",
        "cindy_look == 'posh'", "cindy_earrings.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "cindy_makeup", "cindy_makeup.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "fcindy == 'blush'", "cindyblush.webp",
        "fcindy == 'flirt'", "cindyflirt.webp",
        "fcindy == 'mad'", "cindymad.webp",
        "fcindy == 'sad'", "cindysad.webp",
        "fcindy == 'serious'", "cindyserious.webp",
        "fcindy == 'smile'", "cindysmile.webp",
        "fcindy == 'surprise'", "cindysurprise.webp",
        "fcindy == 'slut'", "cindyslut.webp", 
        "fcindy == 'cry'", "cindycry.webp", 
        "fcindy == 'shy'", "cindyshy.webp",
        "True", "cindy.webp")
    )

image cindy2 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "cindy_look == 'summer'", "cindy_summer2.webp",
        "cindy_look == 'posh'", "cindy_posh2.webp",
        "cindy_look == 'party'", "cindy_partyb.webp",
        "cindy_look == 2", "cindy4_b.webp",
        "cindy_look == 1", "cindy1_b.webp",
        "True", "cindy1_b.webp"
    ),
    (0, 0), ConditionSwitch( 
        "cindy_necklace == 'gift'", "cindy_necklace.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "cindy_look == 'summer'", "cindy_earrings.webp",
        "cindy_look == 'posh'", "cindy_earrings.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "cindy_makeup", "cindy_makeup.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "fcindy == 'blush'", "cindyblush.webp",
        "fcindy == 'flirt'", "cindyflirt.webp",
        "fcindy == 'mad'", "cindymad.webp",
        "fcindy == 'sad'", "cindysad.webp",
        "fcindy == 'serious'", "cindyserious.webp",
        "fcindy == 'smile'", "cindysmile.webp",
        "fcindy == 'surprise'", "cindysurprise.webp",
        "fcindy == 'slut'", "cindyslut.webp", 
        "fcindy == 'cry'", "cindycry.webp", 
        "fcindy == 'shy'", "cindyshy.webp",
        "True", "cindy.webp")
    )



image cindybra = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "cindy_look == 1", "cindybra.webp", 
        "cindy_look == 'party'", "cindy_partybra.webp",
        "cindy_look == 2", "cindybra.webp", 
        "cindy_look == 'comfy'", "cindycomfy.webp",
        "cindy_look == 'comfytopless'", "cindycomfy2.webp",
        "True", "cindybra.webp" 
    ),
    (0, 0), ConditionSwitch( 
        "cindy_necklace == 'gift'", "cindy_necklace.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "cindy_makeup", "cindy_makeup.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "fcindy == 'blush'", "cindyblush.webp",
        "fcindy == 'flirt'", "cindyflirt.webp",
        "fcindy == 'mad'", "cindymad.webp",
        "fcindy == 'sad'", "cindysad.webp",
        "fcindy == 'serious'", "cindyserious.webp",
        "fcindy == 'smile'", "cindysmile.webp",
        "fcindy == 'surprise'", "cindysurprise.webp",
        "fcindy == 'slut'", "cindyslut.webp", 
        "fcindy == 'cry'", "cindycry.webp", 
        "fcindy == 'shy'", "cindyshy.webp",
        "True", "cindy.webp")
    )

image cindybra2 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "cindy_look == 1", "cindybra_b.webp", 
        "cindy_look == 'party'", "cindy_partybra_b.webp",
        "cindy_look == 2", "cindybra_b.webp", 
        "cindy_look == 'comfy'", "cindycomfy_b.webp",
        "cindy_look == 'comfytopless'", "cindycomfy2_b.webp",
        "True", "cindybra_b.webp" 
    ),
    (0, 0), ConditionSwitch( 
        "cindy_necklace == 'gift'", "cindy_necklace.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "cindy_makeup", "cindy_makeup.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "fcindy == 'blush'", "cindyblush.webp",
        "fcindy == 'flirt'", "cindyflirt.webp",
        "fcindy == 'mad'", "cindymad.webp",
        "fcindy == 'sad'", "cindysad.webp",
        "fcindy == 'serious'", "cindyserious.webp",
        "fcindy == 'smile'", "cindysmile.webp",
        "fcindy == 'surprise'", "cindysurprise.webp",
        "fcindy == 'slut'", "cindyslut.webp", 
        "fcindy == 'cry'", "cindycry.webp", 
        "fcindy == 'shy'", "cindyshy.webp",
        "True", "cindy.webp")
    )



image cindynude = Composite(
    (640, 1080),
    (0, 0), "cindynude.webp",
    (0, 0), ConditionSwitch( 
        "cindy_necklace == 'gift'", "cindy_necklace.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "cindy_makeup", "cindy_makeup.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "fcindy == 'blush'", "cindyblush.webp",
        "fcindy == 'flirt'", "cindyflirt.webp",
        "fcindy == 'mad'", "cindymad.webp",
        "fcindy == 'sad'", "cindysad.webp",
        "fcindy == 'serious'", "cindyserious.webp",
        "fcindy == 'smile'", "cindysmile.webp",
        "fcindy == 'surprise'", "cindysurprise.webp",
        "fcindy == 'slut'", "cindyslut.webp",
        "fcindy == 'cry'", "cindycry.webp",
        "fcindy == 'shy'", "cindyshy.webp",
        "True", "cindy.webp")
    )

image cindynude2 = Composite(
    (640, 1080),
    (0, 0), "cindynude_b.webp",
    (0, 0), ConditionSwitch( 
        "cindy_necklace == 'gift'", "cindy_necklace.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "cindy_makeup", "cindy_makeup.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "fcindy == 'blush'", "cindyblush.webp",
        "fcindy == 'flirt'", "cindyflirt.webp",
        "fcindy == 'mad'", "cindymad.webp",
        "fcindy == 'sad'", "cindysad.webp",
        "fcindy == 'serious'", "cindyserious.webp",
        "fcindy == 'smile'", "cindysmile.webp",
        "fcindy == 'surprise'", "cindysurprise.webp",
        "fcindy == 'slut'", "cindyslut.webp", 
        "fcindy == 'cry'", "cindycry.webp", 
        "fcindy == 'shy'", "cindyshy.webp",
        "True", "cindy.webp")
    )








image danny = Composite(
    (640, 1080),
    (0, 0), "danny2.webp",
    (0, 0), ConditionSwitch(
        "fdanny == 'sad'", "dannysad.webp",
        "fdanny == 'smile'", "dannysmile.webp",
        "fdanny == 'mad'", "dannymad.webp",
        "fdanny == 'surprise'", "dannysurprise.webp",
        "True", "danny.webp")
    )

image danny2 = Composite(
    (640, 1080),
    (0, 0), "danny1.webp",
    (0, 0), ConditionSwitch(
        "fdanny == 'sad'", "dannysad.webp",
        "fdanny == 'smile'", "dannysmile.webp",
        "fdanny == 'mad'", "dannymad.webp",
        "fdanny == 'surprise'", "dannysurprise.webp",
        "True", "danny.webp")
    )







image emma = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "emma_hair", "emmanude_hair.webp",
        "True", "emmanude.webp"
    ),
    (0, 0), ConditionSwitch( 
        "emma_pubes == True", "emma_pubes.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "emma_hot", "emma_choker.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "emma_hot", "emma_hot.webp",
        "emma_look == 'bikini' and emma_bikini == False", "emmabikini1.webp",
        "emma_look == 'bikini' and emma_bikini", "emmabikini2.webp",
        "emma_look == 'summer' and chapter > 12", "emma_dress2.webp",
        "emma_look == 'summer'", "emma_summer_dress.webp",
        "emma_look == 'cool'", "emma_cool.webp",
        "emma_look == 2", "emma2.webp",
        "emma_look == 'under' and emma_bikini == False", "emma_comfy1.webp",
        "emma_look == 'under' and emma_bikini", "emma_comfy2.webp",
        "True", "emma1.webp"
    ),
    (0, 0), ConditionSwitch( 
        "emma_tattoo == True", "emma_tattoo.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch(  
        "emma_hot and femma == 'sad'", "emmasadb.webp",
        "emma_hot and femma == 'smile'", "emmasmileb.webp",
        "emma_hot and femma == 'mad'", "emmamadb.webp",
        "emma_hot and femma == 'serious'", "emmaseriousb.webp",
        "emma_hot and femma == 'surprise'", "emmasurpriseb.webp",
        "emma_hot and femma == 'flirt'", "emmaflirtb.webp",
        "emma_hot and femma == 'slut'", "emmaslutb.webp",
        "emma_hot and femma == 'n'", "emmab.webp",
        "femma == 'sad'", "emmasad.webp",
        "femma == 'smile'", "emmasmile.webp",
        "femma == 'mad'", "emmamad.webp",
        "femma == 'serious'", "emmaserious.webp",
        "femma == 'surprise'", "emmasurprise.webp",
        "femma == 'flirt'", "emmaflirt.webp",
        "femma == 'slut'", "emmaslut.webp",
        "True", "emma.webp"
    ),
    (0, 0), ConditionSwitch( 
        "emma_hot", "emma_hairlock3.webp",
        "emma_hair == 'pink'", "emma_hairlock2.webp",
        "emma_hair == 2", "emma_hairlock1.webp",
        "emma_hair == 'long'", "emma_hairlock4.webp",
        "True", Null())
    )



image emmanude = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "emma_hair", "emmanude_hair.webp",
        "True", "emmanude.webp"
    ),
    (0, 0), ConditionSwitch( 
        "emma_pubes == True", "emma_pubes.webp",
        "True", "emma_pubes.webp"
    ),
    (0, 0), ConditionSwitch( 
        "emma_hot", "emma_choker.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "emma_tattoo == True", "emma_tattoo.webp",
        "True", Null(),
    ),
    (0, 0), ConditionSwitch( 
        "emma_look == 'bikini' and emma_bikini == False", "emmabikini1_topless.webp",
        "emma_look == 'bikini' and emma_bikini", "emmabikini2_topless.webp",
        "True", Null(),
    ),
    (0, 0), ConditionSwitch(
        "emma_hot and femma == 'sad'", "emmasadb.webp",
        "emma_hot and femma == 'smile'", "emmasmileb.webp",
        "emma_hot and femma == 'mad'", "emmamadb.webp",
        "emma_hot and femma == 'serious'", "emmaseriousb.webp",
        "emma_hot and femma == 'surprise'", "emmasurpriseb.webp",
        "emma_hot and femma == 'flirt'", "emmaflirtb.webp",
        "emma_hot and femma == 'slut'", "emmaslutb.webp",
        "emma_hot and femma == 'n'", "emmab.webp",
        "femma == 'sad'", "emmasad.webp",
        "femma == 'smile'", "emmasmile.webp",
        "femma == 'mad'", "emmamad.webp",
        "femma == 'serious'", "emmaserious.webp",
        "femma == 'surprise'", "emmasurprise.webp",
        "femma == 'flirt'", "emmaflirt.webp",
        "femma == 'slut'", "emmaslut.webp",
        "True", "emma.webp"
    ),
    (0, 0), ConditionSwitch( 
        "emma_hot", "emma_hairlock3.webp",
        "emma_hair == 'pink'", "emma_hairlock2.webp",
        "emma_hair == 2", "emma_hairlock1.webp",
        "emma_hair == 'long'", "emma_hairlock4.webp",
        "True", Null())
    )

image emmabikini = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "emma_hair", "emmanude_hair.webp",
        "True", "emmanude.webp"
    ),
    (0, 0), ConditionSwitch( 
        "emma_pubes == True", "emma_pubes.webp",
        "True", "emma_pubes.webp"
    ),
    (0, 0), ConditionSwitch( 
        "emma_hot", "emma_choker.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "emma_look == 2", "emmabikini2.webp",
        "emma_look == 'hot'", "emma_hotb2.webp", 
        "True", "emmabikini1.webp"
    ),
    (0, 0), ConditionSwitch( 
        "emma_tattoo == True", "emma_tattoo.webp",
        "True", Null(),
    ),
    (0, 0), ConditionSwitch(
        "emma_hot and femma == 'sad'", "emmasadb.webp",
        "emma_hot and femma == 'smile'", "emmasmileb.webp",
        "emma_hot and femma == 'mad'", "emmamadb.webp",
        "emma_hot and femma == 'serious'", "emmaseriousb.webp",
        "emma_hot and femma == 'surprise'", "emmasurpriseb.webp",
        "emma_hot and femma == 'flirt'", "emmaflirtb.webp",
        "emma_hot and femma == 'slut'", "emmaslutb.webp",
        "emma_hot and femma == 'n'", "emmab.webp",
        "femma == 'sad'", "emmasad.webp",
        "femma == 'smile'", "emmasmile.webp",
        "femma == 'mad'", "emmamad.webp",
        "femma == 'serious'", "emmaserious.webp",
        "femma == 'surprise'", "emmasurprise.webp",
        "femma == 'flirt'", "emmaflirt.webp",
        "femma == 'slut'", "emmaslut.webp",
        "True", "emma.webp"
    ),
    (0, 0), ConditionSwitch( 
        "emma_hot", "emma_hairlock3.webp",
        "emma_hair == 'pink'", "emma_hairlock2.webp",
        "emma_hair == 2", "emma_hairlock1.webp",
        "emma_hair == 'long'", "emma_hairlock4.webp",
        "True", Null())
    )






image holly = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "holly_fit", "hollynudefit.webp",
        "True", "hollynude.webp"
    ),
    (0, 0), ConditionSwitch( 
        "holly_gym == True and chapter > 9 and holly_fit == False", "holly_abs.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "holly_extras == 'gift'", "holly_giftnecklace.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "holly_look == 'summer' and v11_holly_change and holly_fit", "holly_summer2_fit.webp",
        "holly_look == 'summer' and v11_holly_change and holly_fit == False", "holly_summer2.webp",
        "holly_look == 'summer' and holly_fit", "holly_summer1_fit.webp",
        "holly_look == 'summer' and holly_fit == False", "holly_summer1.webp",
        "holly_look == 'bikini' and v11_holly_change and holly_fit", "holly_bikini2.webp",
        "holly_look == 'bikini' and v11_holly_change and holly_fit == False", "holly_bikini1b.webp",
        "holly_look == 'bikini' and v11_holly_change == False", "holly_bikini1.webp",
        "holly_look == 1", "holly1.webp",
        "holly_look == 3", "hollygym.webp",
        "holly_look == 4", "holly_gymb.webp",
        "holly_look == 'sexy'", "holly2.webp",
        "holly_look == '1skirt'", "holly1_n.webp",
        "holly_look == 2", "holly2.webp",
        "holly_look == 5", "holly4.webp",
        "holly_look == 'summer2'", "holly_summer_skirt.webp",
        "True", "holly1.webp"),
    (0, 0), ConditionSwitch( 
        "fholly == 'flirtshy'", "hollyflirtshyb.webp",
        "fholly == 'flirt'", "hollyflirtb.webp",
        "fholly == 'surprise'", "hollysurpriseb.webp",
        "fholly == 'shy'", "hollysmileshyb.webp",
        "fholly == 'smileshy'", "hollysmileshyb.webp",
        "fholly == 'serious'", "hollyseriousb.webp",
        "fholly == 'mad'", "hollymadb.webp",
        "fholly == 'smile'", "hollysmileb.webp",
        "fholly == 'happy'", "hollyhappyb.webp",
        "fholly == 'happyshy'", "hollyhappyshyb.webp",
        "fholly == 'sad'", "hollysadb.webp",
        "fholly == 'blush'", "hollyblushb.webp",
        "fholly == 'cry'", "hollycryb.webp",
        "fholly == 'shy'", "hollysmileshyb.webp",
        "fholly == 'worried'", "hollyworried.webp",
        "True", "hollyb.webp"),
    (0, 0), ConditionSwitch( 
        "holly_hair == 2", "holly_hair2.webp",
        "True", "holly_hair.webp"),
    (0, 0), ConditionSwitch( 
        "chapter > 10 and holly_glasses and v11_holly_change", "hollysglasses.webp",
        "holly_glasses == 2", "hollysglasses.webp",
        "holly_glasses == True", "hollyglasses.webp",
        "True", Null()
    )
)
image holly2 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "holly_fit", "hollynudefit_b.webp",
        "True", "hollynude_b.webp"
    ),
    (0, 0), ConditionSwitch( 
        "holly_gym == True and chapter > 9 and holly_fit == False", "holly_abs.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "holly_extras == 'gift'", "holly_giftnecklace.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "holly_look == 'summer' and v11_holly_change and holly_fit", "holly_summer2_fit.webp",
        "holly_look == 'summer' and v11_holly_change and holly_fit == False", "holly_summer2.webp",
        "holly_look == 'summer' and holly_fit", "holly_summer1_fit.webp",
        "holly_look == 'summer' and holly_fit == False", "holly_summer1.webp",
        "holly_look == 'bikini' and v11_holly_change and holly_fit", "holly_bikini2.webp",
        "holly_look == 'bikini' and v11_holly_change and holly_fit == False", "holly_bikini1b.webp",
        "holly_look == 'bikini' and v11_holly_change == False", "holly_bikini1.webp",
        "holly_look == 1", "holly1_b.webp",
        "holly_look == 3", "hollygym.webp",
        "holly_look == 4", "holly_gymb.webp",
        "holly_look == 'sexy'", "holly2.webp",
        "holly_look == '1skirt'", "holly1_bn.webp",
        "holly_look == 2", "holly2.webp",
        "holly_look == 5", "holly4.webp",
        "holly_look == 'summer2'", "holly_summer_skirt2.webp",
        "True", "holly1_b.webp"),
    (0, 0), ConditionSwitch( 
        "fholly == 'flirtshy'", "hollyflirtshyb.webp",
        "fholly == 'flirt'", "hollyflirtb.webp",
        "fholly == 'surprise'", "hollysurpriseb.webp",
        "fholly == 'shy'", "hollysmileshyb.webp",
        "fholly == 'smileshy'", "hollysmileshyb.webp",
        "fholly == 'serious'", "hollyseriousb.webp",
        "fholly == 'mad'", "hollymadb.webp",
        "fholly == 'smile'", "hollysmileb.webp",
        "fholly == 'happy'", "hollyhappyb.webp",
        "fholly == 'happyshy'", "hollyhappyshyb.webp",
        "fholly == 'sad'", "hollysadb.webp",
        "fholly == 'blush'", "hollyblushb.webp",
        "fholly == 'cry'", "hollycryb.webp",
        "fholly == 'shy'", "hollysmileshyb.webp",
        "fholly == 'worried'", "hollyworried.webp",
        "True", "hollyb.webp"),
    
    (0, 0), ConditionSwitch( 
        "holly_hair == 2", "holly_hair2.webp",
        "True", "holly_hair.webp"),
    (0, 0), ConditionSwitch( 
        "chapter > 10 and holly_glasses and v11_holly_change", "hollysglasses.webp",
        "holly_glasses == 2", "hollysglasses.webp",
        "holly_glasses == True", "hollyglasses.webp",
        "True", Null()
    )
)
image holly3 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "holly_fit", "hollynudefit_c.webp",
        "True", "hollynude_c.webp"
    ),
    (0, 0), ConditionSwitch( 
        "holly_gym == True and chapter > 9 and holly_fit == False", "holly_abs.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "holly_extras == 'gift'", "holly_giftnecklace.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "holly_look == 'summer' and v11_holly_change and holly_fit", "holly_summer2_fit.webp",
        "holly_look == 'summer' and v11_holly_change and holly_fit == False", "holly_summer2.webp",
        "holly_look == 'summer' and holly_fit", "holly_summer1c_fit.webp",
        "holly_look == 'summer' and holly_fit == False", "holly_summer1c.webp",
        "holly_look == 'bikini' and v11_holly_change and holly_fit", "holly_bikini2.webp",
        "holly_look == 'bikini' and v11_holly_change and holly_fit == False", "holly_bikini1b.webp",
        "holly_look == 'bikini' and v11_holly_change == False", "holly_bikini1.webp",
        "holly_look == 1", "holly1_c.webp",
        "holly_look == 3", "hollygym.webp",
        "holly_look == 4", "holly_gymb.webp",
        "holly_look == 'sexy'", "holly2_c.webp",
        "holly_look == '1skirt'", "holly1_cn.webp",
        "holly_look == 2", "holly2_c.webp",
        "holly_look == 5", "holly4.webp",
        "holly_look == 'summer2'", "holly_summer_skirt3.webp",
        "True", "holly1_c.webp"),
    (0, 0), ConditionSwitch( 
        "fholly == 'flirtshy'", "hollyflirtshyb.webp",
        "fholly == 'flirt'", "hollyflirtb.webp",
        "fholly == 'surprise'", "hollysurpriseb.webp",
        "fholly == 'shy'", "hollysmileshyb.webp",
        "fholly == 'smileshy'", "hollysmileshyb.webp",
        "fholly == 'serious'", "hollyseriousb.webp",
        "fholly == 'mad'", "hollymadb.webp",
        "fholly == 'smile'", "hollysmileb.webp",
        "fholly == 'happy'", "hollyhappyb.webp",
        "fholly == 'happyshy'", "hollyhappyshyb.webp",
        "fholly == 'sad'", "hollysadb.webp",
        "fholly == 'blush'", "hollyblushb.webp",
        "fholly == 'cry'", "hollycryb.webp",
        "fholly == 'shy'", "hollysmileshyb.webp",
        "fholly == 'worried'", "hollyworried.webp",
        "True", "hollyb.webp"),
    (0, 0), ConditionSwitch( 
        "holly_hair == 2", "holly_hair2b.webp",
        "True", "holly_hairb.webp"),
    (0, 0), ConditionSwitch( 
        "chapter > 10 and holly_glasses and v11_holly_change", "hollysglasses.webp",
        "holly_glasses == 2", "hollysglasses.webp",
        "holly_glasses == True", "hollyglasses.webp",
        "True", Null()
    )
)


image hollybra = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "holly_fit", "hollynudefit.webp",
        "True", "hollynude.webp"
    ),
    (0, 0), ConditionSwitch( 
        "holly_gym == True and chapter > 9 and holly_fit == False", "holly_abs.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "holly_extras == 'gift'", "holly_giftnecklace.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "holly_look == 'summer' and v11_holly_change and holly_fit", "holly_summer2_under.webp",
        "holly_look == 1", "hollybra.webp",
        "holly_look == 3", "hollybra.webp",
        "holly_look == 'sexy'", "hollybra_sexy.webp",
        "holly_look == 'sexytopless'", "hollybra_sexytopless.webp",
        "holly_look == '1skirt'", "hollybra_sexy.webp",
        "holly_look == 2", "hollybra.webp",
        "holly_look == 5", "hollybra_sexytopless.webp",
        "True", "hollybra.webp"),
    (0, 0), ConditionSwitch( 
        "fholly == 'flirtshy'", "hollyflirtshyb.webp",
        "fholly == 'flirt'", "hollyflirtb.webp",
        "fholly == 'surprise'", "hollysurpriseb.webp",
        "fholly == 'shy'", "hollysmileshyb.webp",
        "fholly == 'smileshy'", "hollysmileshyb.webp",
        "fholly == 'serious'", "hollyseriousb.webp",
        "fholly == 'mad'", "hollymadb.webp",
        "fholly == 'smile'", "hollysmileb.webp",
        "fholly == 'happy'", "hollyhappyb.webp",
        "fholly == 'happyshy'", "hollyhappyshyb.webp",
        "fholly == 'sad'", "hollysadb.webp",
        "fholly == 'blush'", "hollyblushb.webp",
        "fholly == 'cry'", "hollycryb.webp",
        "fholly == 'shy'", "hollysmileshyb.webp",
        "fholly == 'worried'", "hollyworried.webp",
        "True", "hollyb.webp"),
    (0, 0), ConditionSwitch( 
        "holly_hair == 2", "holly_hair2.webp",
        "True", "holly_hair.webp"),
    (0, 0), ConditionSwitch( 
        "chapter > 10 and holly_glasses and v11_holly_change", "hollysglasses.webp",
        "holly_glasses == 2", "hollysglasses.webp",
        "holly_glasses == True", "hollyglasses.webp",
        "True", Null()
    )
)

image hollybra2 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "holly_fit", "hollynudefit_b.webp",
        "True", "hollynude_b.webp"
    ),
    (0, 0), ConditionSwitch( 
        "holly_gym == True and chapter > 9 and holly_fit == False", "holly_abs.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "holly_extras == 'gift'", "holly_giftnecklace.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "holly_look == 'summer' and v11_holly_change and holly_fit", "holly_summer2_under.webp",
        "holly_look == 1", "hollybra.webp",
        "holly_look == 3", "hollybra.webp",
        "holly_look == 'sexy'", "hollybra_sexy.webp",
        "holly_look == 'sexytopless'", "hollybra_sexytopless.webp",
        "holly_look == '1skirt'", "hollybra_sexy.webp",
        "holly_look == 2", "hollybra.webp",
        "holly_look == 5", "hollybra_sexytopless.webp",
        "True", "hollybra.webp"),
    (0, 0), ConditionSwitch( 
        "fholly == 'flirtshy'", "hollyflirtshyb.webp",
        "fholly == 'flirt'", "hollyflirtb.webp",
        "fholly == 'surprise'", "hollysurpriseb.webp",
        "fholly == 'shy'", "hollysmileshyb.webp",
        "fholly == 'smileshy'", "hollysmileshyb.webp",
        "fholly == 'serious'", "hollyseriousb.webp",
        "fholly == 'mad'", "hollymadb.webp",
        "fholly == 'smile'", "hollysmileb.webp",
        "fholly == 'happy'", "hollyhappyb.webp",
        "fholly == 'happyshy'", "hollyhappyshyb.webp",
        "fholly == 'sad'", "hollysadb.webp",
        "fholly == 'blush'", "hollyblushb.webp",
        "fholly == 'cry'", "hollycryb.webp",
        "fholly == 'shy'", "hollysmileshyb.webp",
        "fholly == 'worried'", "hollyworried.webp",
        "True", "hollyb.webp"),
    (0, 0), ConditionSwitch( 
        "holly_hair == 2", "holly_hair2.webp",
        "True", "holly_hair.webp"),
    (0, 0), ConditionSwitch( 
        "chapter > 10 and holly_glasses and v11_holly_change", "hollysglasses.webp",
        "holly_glasses == 2", "hollysglasses.webp",
        "holly_glasses == True", "hollyglasses.webp",
        "True", Null()
    )
)

image hollybra3 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "holly_fit", "hollynudefit_c.webp",
        "True", "hollynude_c.webp"
    ),
    (0, 0), ConditionSwitch( 
        "holly_gym == True and chapter > 9 and holly_fit == False", "holly_abs.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "holly_extras == 'gift'", "holly_giftnecklace.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "holly_look == 'summer' and v11_holly_change and holly_fit", "holly_summer2_under.webp",
        "holly_look == 1", "hollybra.webp",
        "holly_look == 3", "hollybra.webp",
        "holly_look == 'sexy'", "hollybra_sexy.webp",
        "holly_look == 'sexytopless'", "hollybra_sexytopless.webp",
        "holly_look == '1skirt'", "hollybra_sexy.webp",
        "holly_look == 2", "hollybra.webp",
        "holly_look == 5", "hollybra_sexytopless.webp",
        "True", "hollybra.webp"),
    (0, 0), ConditionSwitch( 
        "fholly == 'flirtshy'", "hollyflirtshyb.webp",
        "fholly == 'flirt'", "hollyflirtb.webp",
        "fholly == 'surprise'", "hollysurpriseb.webp",
        "fholly == 'shy'", "hollysmileshyb.webp",
        "fholly == 'smileshy'", "hollysmileshyb.webp",
        "fholly == 'serious'", "hollyseriousb.webp",
        "fholly == 'mad'", "hollymadb.webp",
        "fholly == 'smile'", "hollysmileb.webp",
        "fholly == 'happy'", "hollyhappyb.webp",
        "fholly == 'happyshy'", "hollyhappyshyb.webp",
        "fholly == 'sad'", "hollysadb.webp",
        "fholly == 'blush'", "hollyblushb.webp",
        "fholly == 'cry'", "hollycryb.webp",
        "fholly == 'shy'", "hollysmileshyb.webp",
        "fholly == 'worried'", "hollyworried.webp",
        "True", "hollyb.webp"),
    (0, 0), ConditionSwitch( 
        "holly_hair == 2", "holly_hair2b.webp",
        "True", "holly_hairb.webp"),
    (0, 0), ConditionSwitch( 
        "chapter > 10 and holly_glasses and v11_holly_change", "hollysglasses.webp",
        "holly_glasses == 2", "hollysglasses.webp",
        "holly_glasses == True", "hollyglasses.webp",
        "True", Null()
    )
)


image hollynude = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "holly_fit", "hollynudefit.webp",
        "True", "hollynude.webp"
    ),
    (0, 0), ConditionSwitch( 
        "holly_gym == True and chapter > 9 and holly_fit == False", "holly_abs.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "holly_extras == 'gift'", "holly_giftnecklace.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "fholly == 'flirtshy'", "hollyflirtshyb.webp",
        "fholly == 'flirt'", "hollyflirtb.webp",
        "fholly == 'surprise'", "hollysurpriseb.webp",
        "fholly == 'shy'", "hollysmileshyb.webp",
        "fholly == 'smileshy'", "hollysmileshyb.webp",
        "fholly == 'serious'", "hollyseriousb.webp",
        "fholly == 'mad'", "hollymadb.webp",
        "fholly == 'smile'", "hollysmileb.webp",
        "fholly == 'happy'", "hollyhappyb.webp",
        "fholly == 'happyshy'", "hollyhappyshyb.webp",
        "fholly == 'sad'", "hollysadb.webp",
        "fholly == 'blush'", "hollyblushb.webp",
        "fholly == 'cry'", "hollycryb.webp",
        "fholly == 'shy'", "hollysmileshyb.webp",
        "fholly == 'worried'", "hollyworried.webp",
        "True", "hollyb.webp"),
    (0, 0), ConditionSwitch( 
        "holly_hair == 2", "holly_hair2.webp",
        "True", "holly_hair.webp"),
    (0, 0), ConditionSwitch( 
        "chapter > 10 and holly_glasses and v11_holly_change", "hollysglasses.webp",
        "holly_glasses == 2", "hollysglasses.webp",
        "holly_glasses == True", "hollyglasses.webp",
        "True", Null()
    )
)

image hollynude2 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "holly_fit", "hollynudefit_b.webp",
        "True", "hollynude_b.webp"
    ),
    (0, 0), ConditionSwitch( 
        "holly_gym == True and chapter > 9 and holly_fit == False", "holly_abs.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "holly_extras == 'gift'", "holly_giftnecklace.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "fholly == 'flirtshy'", "hollyflirtshyb.webp",
        "fholly == 'flirt'", "hollyflirtb.webp",
        "fholly == 'surprise'", "hollysurpriseb.webp",
        "fholly == 'shy'", "hollysmileshyb.webp",
        "fholly == 'smileshy'", "hollysmileshyb.webp",
        "fholly == 'serious'", "hollyseriousb.webp",
        "fholly == 'mad'", "hollymadb.webp",
        "fholly == 'smile'", "hollysmileb.webp",
        "fholly == 'happy'", "hollyhappyb.webp",
        "fholly == 'happyshy'", "hollyhappyshyb.webp",
        "fholly == 'sad'", "hollysadb.webp",
        "fholly == 'blush'", "hollyblushb.webp",
        "fholly == 'cry'", "hollycryb.webp",
        "fholly == 'shy'", "hollysmileshyb.webp",
        "fholly == 'worried'", "hollyworried.webp",
        "True", "hollyb.webp"),
    (0, 0), ConditionSwitch( 
        "holly_hair == 2", "holly_hair2.webp",
        "True", "holly_hair.webp"),
    (0, 0), ConditionSwitch( 
        "chapter > 10 and holly_glasses and v11_holly_change", "hollysglasses.webp",
        "holly_glasses == 2", "hollysglasses.webp",
        "holly_glasses == True", "hollyglasses.webp",
        "True", Null()
    )
)

image hollynude3 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "holly_fit", "hollynudefit_c.webp",
        "True", "hollynude_c.webp"
    ),
    (0, 0), ConditionSwitch( 
        "holly_gym == True and chapter > 9 and holly_fit == False", "holly_abs.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "holly_extras == 'gift'", "holly_giftnecklace.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "fholly == 'flirtshy'", "hollyflirtshyb.webp",
        "fholly == 'flirt'", "hollyflirtb.webp",
        "fholly == 'surprise'", "hollysurpriseb.webp",
        "fholly == 'shy'", "hollysmileshyb.webp",
        "fholly == 'smileshy'", "hollysmileshyb.webp",
        "fholly == 'serious'", "hollyseriousb.webp",
        "fholly == 'mad'", "hollymadb.webp",
        "fholly == 'smile'", "hollysmileb.webp",
        "fholly == 'happy'", "hollyhappyb.webp",
        "fholly == 'happyshy'", "hollyhappyshyb.webp",
        "fholly == 'sad'", "hollysadb.webp",
        "fholly == 'blush'", "hollyblushb.webp",
        "fholly == 'cry'", "hollycryb.webp",
        "fholly == 'shy'", "hollysmileshyb.webp",
        "fholly == 'worried'", "hollyworried.webp",
        "True", "hollyb.webp"),
    (0, 0), ConditionSwitch( 
        "holly_hair == 2", "holly_hair2b.webp",
        "True", "holly_hairb.webp"),
    (0, 0), ConditionSwitch( 
        "chapter > 10 and holly_glasses and v11_holly_change", "hollysglasses.webp",
        "holly_glasses == 2", "hollysglasses.webp",
        "holly_glasses == True", "hollyglasses.webp",
        "True", Null()
    )
)
































































































































































































































































































































































































































































































































































































image ivy = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "ivy_look == 1", "ivy1.webp",
        "ivy_look == 2", "ivygym.webp",
        "ivy_look == 'sexy'", "ivy2.webp",
        "ivy_look == 'gogo'", "ivy3.webp",
        "ivy_look == 'dress'", "ivy_dress.webp",
        "ivy_look == 'pantless'", "ivy_topbottom.webp",
        "ivy_look == 'bikini'", "ivy4.webp",
        "ivy_look == 'summer2'", "ivy4c.webp",
        "ivy_look == 'nymph'", "ivy_nymph.webp",
        "ivy_look == 'nymph2'", "ivy_nymphb.webp",
        "True", "ivy1.webp"
    ),
    (0, 0), "ivy_makeup1.webp",
    (0, 0), ConditionSwitch( 
        "ivy_navel == True and ivy_look != 'nymph' and ivy_look != 'nymph2'", "ivy_navel.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "ivy_look == 'dress'", "ivy_dress_cover.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "ivy_extras == 'bag'", "ivy_bag.webp",
        "ivy_extras == 'smoke'", "ivy_smoke.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "fivy == 'sad'", "ivysad.webp",
        "fivy == 'slut'", "ivyslut.webp",
        "fivy == 'flirt'", "ivyflirt.webp",
        "fivy == 'mad'", "ivymad.webp",
        "fivy == 'serious'", "ivyserious.webp",
        "fivy == 'smile'", "ivysmile.webp",
        "fivy == 'surprise'", "ivysurprise.webp",
        "fivy == 'blush'", "ivyblush.webp",
        "True", "ivy.webp")
    )

image ivy2 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "ivy_look == 1", "ivy1_b.webp",
        "ivy_look == 2", "ivygym_b.webp",
        "ivy_look == 'sexy'", "ivy2_b.webp",
        "ivy_look == 'gogo'", "ivy3_b.webp",
        "ivy_look == 'dress'", "ivy_dress_b.webp",
        "ivy_look == 'pantless'", "ivy_topbottom_b.webp",
        "ivy_look == 'bikini'", "ivy4_b.webp",
        "ivy_look == 'summer2'", "ivy4_c.webp",
        "ivy_look == 'nymph'", "ivy_nymph_b.webp",
        "ivy_look == 'nymph2'", "ivy_nymphb_b.webp",
        "True", "ivy1_b.webp"
    ),
    (0, 0), "ivy_makeup1.webp",
    (0, 0), ConditionSwitch( 
        "ivy_navel == True and ivy_look != 'nymph' and ivy_look != 'nymph2'", "ivy_navel.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "ivy_look == 'dress'", "ivy_dress_cover.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "ivy_extras == 'bag'", "ivy_bag.webp",
        "ivy_extras == 'smoke'", "ivy_smoke.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "fivy == 'sad'", "ivysad.webp",
        "fivy == 'slut'", "ivyslut.webp",
        "fivy == 'flirt'", "ivyflirt.webp",
        "fivy == 'mad'", "ivymad.webp",
        "fivy == 'serious'", "ivyserious.webp",
        "fivy == 'smile'", "ivysmile.webp",
        "fivy == 'surprise'", "ivysurprise.webp",
        "fivy == 'blush'", "ivyblush.webp",
        "True", "ivy.webp")
    )



image ivybra = Composite(
    (640, 1080),
    (0, 0), "ivybra.webp",
    (0, 0), "ivy_makeup1.webp",
    (0, 0), ConditionSwitch( 
        "ivy_navel == True", "ivy_navel.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "fivy == 'sad'", "ivysad.webp",
        "fivy == 'slut'", "ivyslut.webp",
        "fivy == 'flirt'", "ivyflirt.webp",
        "fivy == 'mad'", "ivymad.webp",
        "fivy == 'serious'", "ivyserious.webp",
        "fivy == 'smile'", "ivysmile.webp",
        "fivy == 'surprise'", "ivysurprise.webp",
        "fivy == 'blush'", "ivyblush.webp",
        "True", "ivy.webp")
    )

image ivybra2 = Composite(
    (640, 1080),
    (0, 0), "ivybra_b.webp",
    (0, 0), "ivy_makeup1.webp",
    (0, 0), ConditionSwitch( 
        "ivy_navel == True", "ivy_navel.webp",
        "ivy_extras == 'smoke'", "ivy_smoke.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "fivy == 'sad'", "ivysad.webp",
        "fivy == 'slut'", "ivyslut.webp",
        "fivy == 'flirt'", "ivyflirt.webp",
        "fivy == 'mad'", "ivymad.webp",
        "fivy == 'serious'", "ivyserious.webp",
        "fivy == 'smile'", "ivysmile.webp",
        "fivy == 'surprise'", "ivysurprise.webp",
        "fivy == 'blush'", "ivyblush.webp",
        "True", "ivy.webp")
    )



image ivynude = Composite(
    (640, 1080),
    (0, 0), "ivynude.webp",
    (0, 0), "ivy_makeup1.webp",
    (0, 0), ConditionSwitch( 
        "ivy_navel == True", "ivy_navel.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "fivy == 'sad'", "ivysad.webp",
        "fivy == 'slut'", "ivyslut.webp",
        "fivy == 'flirt'", "ivyflirt.webp",
        "fivy == 'mad'", "ivymad.webp",
        "fivy == 'serious'", "ivyserious.webp",
        "fivy == 'smile'", "ivysmile.webp",
        "fivy == 'surprise'", "ivysurprise.webp",
        "fivy == 'blush'", "ivyblush.webp",
        "True", "ivy.webp")
    )

image ivynude2 = Composite(
    (640, 1080),
    (0, 0), "ivynude_b.webp",
    (0, 0), "ivy_makeup1.webp",
    (0, 0), ConditionSwitch( 
        "ivy_navel == True", "ivy_navel.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "fivy == 'sad'", "ivysad.webp",
        "fivy == 'slut'", "ivyslut.webp",
        "fivy == 'flirt'", "ivyflirt.webp",
        "fivy == 'mad'", "ivymad.webp",
        "fivy == 'serious'", "ivyserious.webp",
        "fivy == 'smile'", "ivysmile.webp",
        "fivy == 'surprise'", "ivysurprise.webp",
        "fivy == 'blush'", "ivyblush.webp",
        "True", "ivy.webp")
    )







image jeremy = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "jeremy_look == 2", "jeremygym.webp",
        "jeremy_look == 3", "jeremy1b.webp",
        "jeremy_look == 1", "jeremy1.webp",
        "jeremy_look == 'mma'", "jeremy_mma.webp",
        "jeremy_look == 'summer'", "jeremy_summer1.webp",
        "jeremy_look == 'swim'", "jeremy_summer2.webp",
        "jeremy_look == 'pantless'", "jeremy_summer1.webp",
        "True", "jeremy1.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fjeremy == 'serious'", "jeremyserious.webp",
        "fjeremy == 'evil'", "jeremyevil.webp",
        "fjeremy == 'flirt'", "jeremyflirt.webp",
        "fjeremy == 'surprise'", "jeremysurprise.webp",
        "fjeremy == 'happy'", "jeremyhappy.webp",
        "fjeremy == 'mad'", "jeremymad.webp",
        "fjeremy == 'sad'", "jeremysad.webp",
        "fjeremy == 'smile'", "jeremysmile.webp",
        "True", "jeremy.webp")
    )



image jeremynude = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "jeremy_look == 3", "jeremynude.webp",
        "jeremy_look == 2", "jeremy_noshirt.webp",
        "jeremy_look == 1", "jeremynude.webp",
        "jeremy_look == 'cock'", "jeremy_openfly.webp",
        "jeremy_look == 'pantless'", "jeremy_summer3.webp",
        "True", "jeremynude.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fjeremy == 'serious'", "jeremyserious.webp",
        "fjeremy == 'evil'", "jeremyevil.webp",
        "fjeremy == 'flirt'", "jeremyflirt.webp",
        "fjeremy == 'surprise'", "jeremysurprise.webp",
        "fjeremy == 'happy'", "jeremyhappy.webp",
        "fjeremy == 'mad'", "jeremymad.webp",
        "fjeremy == 'sad'", "jeremysad.webp",
        "fjeremy == 'smile'", "jeremysmile.webp",
        "True", "jeremy.webp"
    ),
    (0, 0), ConditionSwitch( 
        "jeremy_look == 'summer' or jeremy_look == 'swim'", "jeremy_jewels.webp",
        "True", Null())
    )


image jeremytopless = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "jeremy_look == 'cock'", "jeremy_openfly.webp",
        "jeremy_look == 'summer'", "jeremy_summer2.webp",
        "True", "jeremy_noshirt.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fjeremy == 'serious'", "jeremyserious.webp",
        "fjeremy == 'evil'", "jeremyevil.webp",
        "fjeremy == 'flirt'", "jeremyflirt.webp",
        "fjeremy == 'surprise'", "jeremysurprise.webp",
        "fjeremy == 'happy'", "jeremyhappy.webp",
        "fjeremy == 'mad'", "jeremymad.webp",
        "fjeremy == 'sad'", "jeremysad.webp",
        "fjeremy == 'smile'", "jeremysmile.webp",
        "True", "jeremy.webp")
    )







image louise = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "louise_look == 1", "louise1.webp",
        "louise_look == 2", "louise2.webp",
        "louise_look == 3", "louise3.webp", 
        "True", "louise1.webp"
    ),
    (0, 0), ConditionSwitch( 
        "flouise == 'sad'", "louisesad.webp",
        "flouise == 'happy'", "louisehappy.webp",
        "flouise == 'mad'", "louisemad.webp",
        "flouise == 'blush'", "louiseblush.webp",
        "flouise == 'blush2'", "louiseblush2.webp",
        "flouise == 'serious'", "louiseserious.webp",
        "flouise == 'smile'", "louisesmile.webp",
        "flouise == 'surprise'", "louisesurprise.webp",
        "flouise == 'flirt'", "louiseflirt.webp",
        "flouise == 'slut'", "louiseslut.webp",
        "flouise == 'cry'", "louisecry.webp",
        "flouise == 'worried'", "louiseworried.webp",
        "True", "louise.webp")
    )

image louise2 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "louise_look == 1", "louise1_b.webp",
        "louise_look == 2", "louise2_b.webp",
        "louise_look == 3", "louise3_b.webp", 
        "True", "louise1_b.webp"
    ),
    (0, 0), ConditionSwitch( 
        "flouise == 'sad'", "louisesad.webp",
        "flouise == 'happy'", "louisehappy.webp",
        "flouise == 'mad'", "louisemad.webp",
        "flouise == 'blush'", "louiseblush.webp",
        "flouise == 'blush2'", "louiseblush2.webp",
        "flouise == 'serious'", "louiseserious.webp",
        "flouise == 'smile'", "louisesmile.webp",
        "flouise == 'surprise'", "louisesurprise.webp",
        "flouise == 'flirt'", "louiseflirt.webp",
        "flouise == 'slut'", "louiseslut.webp",
        "flouise == 'cry'", "louisecry.webp",
        "flouise == 'worried'", "louiseworried.webp",
        "True", "louise.webp")
    )



image louisebra = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "louise_look == 1", "louisebra.webp",
        "louise_look == 3", "louisetopless.webp",
        "louise_look == 2", "louisecomfy.webp",
        "True", "louisebra.webp"
    ),
    (0, 0), ConditionSwitch( 
        "flouise == 'sad'", "louisesad.webp",
        "flouise == 'happy'", "louisehappy.webp",
        "flouise == 'mad'", "louisemad.webp",
        "flouise == 'blush'", "louiseblush.webp",
        "flouise == 'blush2'", "louiseblush2.webp",
        "flouise == 'serious'", "louiseserious.webp",
        "flouise == 'smile'", "louisesmile.webp",
        "flouise == 'surprise'", "louisesurprise.webp",
        "flouise == 'flirt'", "louiseflirt.webp",
        "flouise == 'slut'", "louiseslut.webp",
        "flouise == 'cry'", "louisecry.webp",
        "flouise == 'worried'", "louiseworried.webp",
        "True", "louise.webp")
    )
image louisebra2 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "louise_look == 1", "louisebra_b.webp",
        "louise_look == 3", "louisetopless_b.webp",
        "louise_look == 2", "louisecomfy_b.webp",
        "True", "louisebra_b.webp"
    ),
    (0, 0), ConditionSwitch( 
        "flouise == 'sad'", "louisesad.webp",
        "flouise == 'happy'", "louisehappy.webp",
        "flouise == 'mad'", "louisemad.webp",
        "flouise == 'blush'", "louiseblush.webp",
        "flouise == 'blush2'", "louiseblush2.webp",
        "flouise == 'serious'", "louiseserious.webp",
        "flouise == 'smile'", "louisesmile.webp",
        "flouise == 'surprise'", "louisesurprise.webp",
        "flouise == 'flirt'", "louiseflirt.webp",
        "flouise == 'slut'", "louiseslut.webp",
        "flouise == 'cry'", "louisecry.webp",
        "flouise == 'worried'", "louiseworried.webp",
        "True", "louise.webp")
    )
image louisetopless = Composite(
    (640, 1080),
    (0, 0), "louisetopless_b.webp",
    (0, 0), ConditionSwitch( 
        "flouise == 'sad'", "louisesad.webp",
        "flouise == 'happy'", "louisehappy.webp",
        "flouise == 'mad'", "louisemad.webp",
        "flouise == 'blush'", "louiseblush.webp",
        "flouise == 'blush2'", "louiseblush2.webp",
        "flouise == 'serious'", "louiseserious.webp",
        "flouise == 'smile'", "louisesmile.webp",
        "flouise == 'surprise'", "louisesurprise.webp",
        "flouise == 'flirt'", "louiseflirt.webp",
        "flouise == 'slut'", "louiseslut.webp",
        "flouise == 'cry'", "louisecry.webp",
        "flouise == 'worried'", "louiseworried.webp",
        "True", "louise.webp")
    )

image louisenude = Composite(
    (640, 1080),
    (0, 0), "louisenude.webp",
    (0, 0), ConditionSwitch( 
        "flouise == 'sad'", "louisesad.webp",
        "flouise == 'happy'", "louisehappy.webp",
        "flouise == 'mad'", "louisemad.webp",
        "flouise == 'blush'", "louiseblush.webp",
        "flouise == 'blush2'", "louiseblush2.webp",
        "flouise == 'serious'", "louiseserious.webp",
        "flouise == 'smile'", "louisesmile.webp",
        "flouise == 'surprise'", "louisesurprise.webp",
        "flouise == 'flirt'", "louiseflirt.webp",
        "flouise == 'slut'", "louiseslut.webp",
        "flouise == 'cry'", "louisecry.webp",
        "flouise == 'worried'", "louiseworried.webp",
        "True", "louise.webp")
    )
image louisenude2 = Composite(
    (640, 1080),
    (0, 0), "louisenude_b.webp",
    (0, 0), ConditionSwitch( 
        "flouise == 'sad'", "louisesad.webp",
        "flouise == 'happy'", "louisehappy.webp",
        "flouise == 'mad'", "louisemad.webp",
        "flouise == 'blush'", "louiseblush.webp",
        "flouise == 'blush2'", "louiseblush2.webp",
        "flouise == 'serious'", "louiseserious.webp",
        "flouise == 'smile'", "louisesmile.webp",
        "flouise == 'surprise'", "louisesurprise.webp",
        "flouise == 'flirt'", "louiseflirt.webp",
        "flouise == 'slut'", "louiseslut.webp",
        "flouise == 'cry'", "louisecry.webp",
        "flouise == 'worried'", "louiseworried.webp",
        "True", "louise.webp")
    )







image minerva = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "minerva_look == 1", "minerva1.webp",
        "minerva_look == 2 and ian_minerva_sex and chapter > 9", "minervagym_b.webp", 
        "minerva_look == 2", "minervagym.webp", 
        "minerva_look == 3", "minerva_sexy.webp", 
        "minerva_look == 'hot'", "minerva_sexyb.webp", 
        "minerva_look == 'dress'", "minerva2.webp", 
        "True", "minerva1.webp"
    ),
    (0, 0), ConditionSwitch( 
        "minerva_necklace", "minerva_necklace.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "fminerva == 'mad'", "minervamad.webp",
        "fminerva == 'smile'", "minervasmile.webp",
        "fminerva == 'furious'", "minervafurious.webp",
        "fminerva == 'evil'", "minervaevil.webp",
        "fminerva == 'sad'", "minervasad.webp",
        "fminerva == 'flirt'", "minervaflirt.webp",
        "fminerva == 'happy'", "minervahappy.webp",
        "fminerva == 'blush'", "minervablush.webp",
        "fminerva == 'worried'", "minervaworried.webp",
        "True", "minerva.webp")
    )

image minerva2 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "minerva_look == 1", "minerva1b.webp", 
        "minerva_look == 2", "minerva1b.webp",
        "minerva_look == 3", "minerva_sexy_phone.webp", 
        "minerva_look == 'hot'", "minerva_sexyb_phone.webp", 
        "True", "minerva1b.webp"
    ),
    (0, 0), ConditionSwitch( 
        "minerva_necklace", "minerva_necklace.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "fminerva == 'mad'", "minervamad.webp",
        "fminerva == 'smile'", "minervasmile.webp",
        "fminerva == 'furious'", "minervafurious.webp",
        "fminerva == 'evil'", "minervaevil.webp",
        "fminerva == 'sad'", "minervasad.webp",
        "fminerva == 'flirt'", "minervaflirt.webp",
        "fminerva == 'happy'", "minervahappy.webp",
        "fminerva == 'blush'", "minervablush.webp",
        "fminerva == 'worried'", "minervaworried.webp",
        "True", "minerva.webp")
    )

image minerva3 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "minerva_look == 1", "minerva1c.webp", 
        "minerva_look == 2", "minerva1c.webp",
        "minerva_look == 3", "minerva1c.webp",
        "True", "minerva1c.webp"
    ),
    (0, 0), ConditionSwitch( 
        "minerva_necklace", "minerva_necklace.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "fminerva == 'mad'", "minervamad.webp",
        "fminerva == 'smile'", "minervasmile.webp",
        "fminerva == 'furious'", "minervafurious.webp",
        "fminerva == 'evil'", "minervaevil.webp",
        "fminerva == 'sad'", "minervasad.webp",
        "fminerva == 'flirt'", "minervaflirt.webp",
        "fminerva == 'happy'", "minervahappy.webp",
        "fminerva == 'blush'", "minervablush.webp",
        "fminerva == 'worried'", "minervaworried.webp",
        "True", "minerva.webp")
    )

image minerva4 = Composite( 
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "minerva_look == 'dress'", "minerva2.webp",
        "True", "minerva_sexyb.webp"
    ),
    (0, 0), ConditionSwitch( 
        "minerva_necklace", "minerva_necklace.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "fminerva == 'mad'", "minervamad_mk.webp",
        "fminerva == 'smile'", "minervasmile_mk.webp",
        "fminerva == 'furious'", "minervafurious_mk.webp",
        "fminerva == 'evil'", "minervaevil_mk.webp",
        "fminerva == 'sad'", "minervasad_mk.webp",
        "fminerva == 'flirt'", "minervaflirt_mk.webp",
        "fminerva == 'happy'", "minervahappy_mk.webp",
        "fminerva == 'blush'", "minervablush_mk.webp",
        "fminerva == 'worried'", "minervaworried_mk.webp",
        "True", "minerva_mk.webp")
    )



image minervanude = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "minerva_look == 'hot'", "minervanude_b.webp", 
        "minerva_look == 'dress'", "minerva3.webp",
        "chapter > 9 and ian_minerva_sex", "minervanude_b.webp", 
        "True", "minervanude.webp"
    ),
    (0, 0), ConditionSwitch( 
        "minerva_necklace", "minerva_necklace.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "minerva_look == 3", "minerva_stockings.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "fminerva == 'mad'", "minervamad.webp",
        "fminerva == 'smile'", "minervasmile.webp",
        "fminerva == 'furious'", "minervafurious.webp",
        "fminerva == 'evil'", "minervaevil.webp",
        "fminerva == 'sad'", "minervasad.webp",
        "fminerva == 'flirt'", "minervaflirt.webp",
        "fminerva == 'happy'", "minervahappy.webp",
        "fminerva == 'blush'", "minervablush.webp",
        "fminerva == 'worried'", "minervaworried.webp",
        "True", "minerva.webp")
)
image minervanude2 = Composite( 
    (640, 1080),
    (0, 0), "minerva3.webp", 
    (0, 0), ConditionSwitch( 
        "minerva_necklace", "minerva_necklace.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "fminerva == 'mad'", "minervamad_mk.webp",
        "fminerva == 'smile'", "minervasmile_mk.webp",
        "fminerva == 'furious'", "minervafurious_mk.webp",
        "fminerva == 'evil'", "minervaevil_mk.webp",
        "fminerva == 'sad'", "minervasad_mk.webp",
        "fminerva == 'flirt'", "minervaflirt_mk.webp",
        "fminerva == 'happy'", "minervahappy_mk.webp",
        "fminerva == 'blush'", "minervablush_mk.webp",
        "fminerva == 'worried'", "minervaworried_mk.webp",
        "True", "minerva_mk.webp")
)
image minervanude2b = Composite( 
    (640, 1080),
    (0, 0), "minervanude_b.webp", 
    (0, 0), ConditionSwitch( 
        "minerva_necklace", "minerva_necklace.webp",
        "True", Null()),
    (0, 0), ConditionSwitch( 
        "fminerva == 'mad'", "minervamad_mk.webp",
        "fminerva == 'smile'", "minervasmile_mk.webp",
        "fminerva == 'furious'", "minervafurious_mk.webp",
        "fminerva == 'evil'", "minervaevil_mk.webp",
        "fminerva == 'sad'", "minervasad_mk.webp",
        "fminerva == 'flirt'", "minervaflirt_mk.webp",
        "fminerva == 'happy'", "minervahappy_mk.webp",
        "fminerva == 'blush'", "minervablush_mk.webp",
        "fminerva == 'worried'", "minervaworried_mk.webp",
        "True", "minerva_mk.webp")
)





image perry = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "perry_look == 1", "perry1.webp",
        "perry_look == 2", "perry3.webp",
        "perry_look == 'cafe'", "perry_cafe.webp",
        "perry_look == 'summer'", "perry_summer.webp",
        "perry_look == 'swim'", "perry_summer2.webp",
        "perry_look == 'under'", "perry_under.webp",
        "True", "perry1.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fperry == 'sad'", "perrysadb.webp",
        "fperry == 'happy'", "perryhappyb.webp",
        "fperry == 'smile'", "perryhappyb.webp",
        "fperry == 'mad'", "perrymadb.webp",
        "fperry == 'meh'", "perrymehb.webp",
        "fperry == 'blush'", "perryblush.webp",
        "fperry == 'serious'", "perryseriousb.webp",
        "fperry == 'surprise'", "perrysurpriseb.webp",
        "fperry == 'flirt'", "perryflirtb.webp",
        "True", "perryb.webp"),
    (0, 0), ConditionSwitch( 
        "perry_glasses == True", "perryglasses.webp",
        "True", Null()
    )
)

image perry2 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "perry_look == 1", "perry2.webp",
        "perry_look == 2", "perry4.webp",
        "perry_look == 'cafe'", "perry_cafe2.webp", 
        "perry_look == 'summer'", "perry_summer2.webp",
        "True", "perry2.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fperry == 'sad'", "perrysadb.webp",
        "fperry == 'happy'", "perryhappyb.webp",
        "fperry == 'smile'", "perryhappyb.webp",
        "fperry == 'mad'", "perrymadb.webp",
        "fperry == 'meh'", "perrymehb.webp",
        "fperry == 'blush'", "perryblush.webp",
        "fperry == 'serious'", "perryseriousb.webp",
        "fperry == 'surprise'", "perrysurpriseb.webp",
        "fperry == 'flirt'", "perryflirtb.webp",
        "True", "perryb.webp"),
    (0, 0), ConditionSwitch( 
        "perry_glasses == True", "perryglasses.webp",
        "True", Null()
    )
)








image robert = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "robert_look == 1", "robert1.webp",
        "robert_look == 2", "robert2.webp",
        "True", "robert1.webp"
    ),
    (0, 0), ConditionSwitch( 
        "frobert == 'flirt'", "robertflirt.webp",
        "frobert == 'mad'", "robertmad.webp",
        "frobert == 'sad'", "robertsad.webp",
        "frobert == 'smile'", "robertsmile.webp",
        "frobert == 'serious'", "robertserious.webp",
        "frobert == 'evil'", "robertevil.webp",
        "True", "robert.webp"),
    (0, 0), ConditionSwitch( 
        "robert_splash == True", "robert_splash.webp",
        "True", Null(),
    ),
    (0, 0), ConditionSwitch( 
        "robert_hurt == 1", "roberthurt.webp",
        "robert_hurt == 3", "roberthurt3.webp",
        "robert_hurt == 4", "roberthurt4.webp",
        "robert_hurt == 2", "roberthurt2.webp",
        "True", Null(),
    )
)


image robertunder = Composite(
    (640, 1080),
    (0, 0), "robertnoshirt.webp",
    (0, 0), ConditionSwitch( 
        "frobert == 'flirt'", "robertflirt.webp",
        "frobert == 'mad'", "robertmad.webp",
        "frobert == 'sad'", "robertsad.webp",
        "frobert == 'smile'", "robertsmile.webp",
        "frobert == 'serious'", "robertserious.webp",
        "frobert == 'evil'", "robertevil.webp",
        "True", "robert.webp"),
    (0, 0), ConditionSwitch( 
        "robert_hurt == 1", "roberthurt.webp",
        "robert_hurt == 3", "roberthurt3.webp",
        "robert_hurt == 4", "roberthurt4.webp",
        "robert_hurt == 2", "roberthurt2.webp",
        "True", Null(),
    )
)



image robertnude = Composite(
    (640, 1080),
    (0, 0), "robertnude.webp",
    (0, 0), ConditionSwitch( 
        "frobert == 'flirt'", "robertflirt.webp",
        "frobert == 'mad'", "robertmad.webp",
        "frobert == 'sad'", "robertsad.webp",
        "frobert == 'smile'", "robertsmile.webp",
        "frobert == 'serious'", "robertserious.webp",
        "frobert == 'evil'", "robertevil.webp",
        "True", "robert.webp"),
    (0, 0), ConditionSwitch( 
        "robert_hurt == 1", "roberthurt.webp",
        "robert_hurt == 3", "roberthurt3.webp",
        "robert_hurt == 4", "roberthurt4.webp",
        "robert_hurt == 2", "roberthurt2.webp",
        "True", Null(),
    )
)







image seymour = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch ( 
        "seymour_look == 1", "seymour1.webp",
        "seymour_look == 'stain'", "seymour_stain1.webp",
        "seymour_look == 2", "seymour2.webp",
        "seymour_look == 3","seymour3.webp",
        "seymour_look == 4","seymour4.webp",
        "True", "seymour1.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fseymour == 'sad'", "seymoursad.webp",
        "fseymour == 'happy'", "seymourhappy.webp",
        "fseymour == 'serious'", "seymourserious.webp",
        "fseymour == 'smile'", "seymoursmile.webp",
        "fseymour == 'surprise'", "seymoursurprise.webp",
        "fseymour == 'evil'", "seymourevil.webp",
        "fseymour == 'mad'", "seymourmad.webp", 
        "True", "seymour.webp")
    )

image seymour2 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch ( 
        "seymour_look == 1", "seymour1_b.webp",
        "seymour_look == 'stain'", "seymour_stain1b.webp",
        "seymour_look == 2", "seymour2_b.webp",
        "seymour_look == 3","seymour3_b.webp",
        "seymour_look == 4","seymour4_b.webp",
        "True", "seymour1_b.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fseymour == 'sad'", "seymoursad.webp",
        "fseymour == 'happy'", "seymourhappy.webp",
        "fseymour == 'serious'", "seymourserious.webp",
        "fseymour == 'smile'", "seymoursmile.webp",
        "fseymour == 'surprise'", "seymoursurprise.webp",
        "fseymour == 'evil'", "seymourevil.webp",
        "fseymour == 'mad'", "seymourmad.webp", 
        "True", "seymour.webp")
    )



image seymournude = Composite(
    (640, 1080),
    (0, 0), "seymournude.webp",
    (0, 0), ConditionSwitch( 
        "fseymour == 'sad'", "seymoursad.webp",
        "fseymour == 'happy'", "seymourhappy.webp",
        "fseymour == 'serious'", "seymourserious.webp",
        "fseymour == 'smile'", "seymoursmile.webp",
        "fseymour == 'surprise'", "seymoursurprise.webp",
        "fseymour == 'evil'", "seymourevil.webp",
        "fseymour == 'mad'", "seymourmad.webp", 
        "True", "seymour.webp")
    )








image stan = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "stan_look == 4", "stan4.webp",
        "stan_look == 3", "stan2.webp",
        "stan_look == 2", "stan1.webp",
        "stan_look == 1", "stan1.webp",
        "True", "stan1.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fstan == 'surprise'", "stansurprise.webp",
        "fstan == 'smile'", "stansmile.webp",
        "fstan == 'shy'", "stanshy.webp",
        "fstan == 'serious'", "stanserious.webp",
        "fstan == 'sad'", "stansad.webp",
        "fstan == 'perv'", "stanperv.webp",
        "fstan == 'mad'", "stanmad.webp",
        "fstan == 'happy'", "stanhappy.webp",
        "fstan == 'worried'", "stanworried.webp",
        "fstan == 'blush'", "stanblush.webp",
        "fstan == 'drama'", "standrama.webp",
        "True", "stan.webp"),
    (0, 0), ConditionSwitch( 
        "stan_camera == True", "stancamera.webp",
        "True", Null(),
    )
)

image stan2 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "stan_look == 2", "stan1_b.webp",
        "stan_look == 3", "stan2.webp",
        "stan_look == 1", "stan1_c.webp",
        "True", "stan1_c.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fstan == 'surprise'", "stansurprise.webp",
        "fstan == 'smile'", "stansmile.webp",
        "fstan == 'shy'", "stanshy.webp",
        "fstan == 'serious'", "stanserious.webp",
        "fstan == 'sad'", "stansad.webp",
        "fstan == 'perv'", "stanperv.webp",
        "fstan == 'mad'", "stanmad.webp",
        "fstan == 'happy'", "stanhappy.webp",
        "fstan == 'worried'", "stanworried.webp",
        "fstan == 'blush'", "stanblush.webp",
        "fstan == 'drama'", "standrama.webp",
        "True", "stan.webp"),
    (0, 0), ConditionSwitch( 
        "stan_camera == True", "stancamera.webp",
        "True", Null(),
    )
)



image stannude = Composite(
    (640, 1080),
    (0, 0), "stannude.webp",
    (0, 0), ConditionSwitch( 
        "fstan == 'surprise'", "stansurprise.webp",
        "fstan == 'smile'", "stansmile.webp",
        "fstan == 'shy'", "stanshy.webp",
        "fstan == 'serious'", "stanserious.webp",
        "fstan == 'sad'", "stansad.webp",
        "fstan == 'perv'", "stanperv.webp",
        "fstan == 'mad'", "stanmad.webp",
        "fstan == 'happy'", "stanhappy.webp",
        "fstan == 'worried'", "stanworried.webp",
        "fstan == 'blush'", "stanblush.webp",
        "fstan == 'drama'", "standrama.webp",
        "True", "stan.webp"),
    (0, 0), ConditionSwitch( 
        "stan_camera == True", "stancamera.webp",
        "True", Null(),
    )
)

image stannude2 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "stan_look == 1", "stan1_d.webp",
        "stan_look == 3", "stannude_soft.webp",
        "stan_look == 2", "stan2_pantless.webp",
        "True", "stan1_d.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fstan == 'surprise'", "stansurprise.webp",
        "fstan == 'smile'", "stansmile.webp",
        "fstan == 'shy'", "stanshy.webp",
        "fstan == 'serious'", "stanserious.webp",
        "fstan == 'sad'", "stansad.webp",
        "fstan == 'perv'", "stanperv.webp",
        "fstan == 'mad'", "stanmad.webp",
        "fstan == 'happy'", "stanhappy.webp",
        "fstan == 'worried'", "stanworried.webp",
        "fstan == 'blush'", "stanblush.webp",
        "fstan == 'drama'", "standrama.webp",
        "True", "stan.webp"),
    (0, 0), ConditionSwitch( 
        "stan_camera == True", "stancamera.webp",
        "True", Null(),
    )
)







image molly = Composite(
    (640, 1080),
    (0, 0), "molly1.webp",
    (0, 0), ConditionSwitch( 
        "fmolly == 'sad'", "mollysad.webp",
        "fmolly == 'smile'", "mollysmile.webp",
        "fmolly == 'mad'", "mollymad.webp",
        "fmolly == 'serious'", "mollyserious.webp",
        "True", "molly.webp")
    )



image ed = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch ( 
        "ed_look == 2", "ed2.webp",
        "True", "ed1.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fed == 'perv'", "edperv.webp",
        "fed == 'smile'", "edsmile.webp",
        "fed == 'surprise'", "edsurprise.webp",
        "fed == 'mad'", "edmad.webp",
        "fed == 'sad'", "edsad.webp",
        "True", "ed.webp")
    )








image wade = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch ( 
        "wade_look == 'summer'", "wade_summer.webp",
        "wade_look == 'swim'", "wade_summer2.webp",
        "wade_look == 2", "wade5.webp",
        "True", "wade1.webp"
    ),
    (0, 0), ConditionSwitch ( 
        "wade_extras == 'smoke'", "wade_smoke.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "fwade == 'sad'", "wadesad.webp",
        "fwade == 'happy'", "wadehappy.webp",
        "fwade == 'smile'", "wadesmile.webp",
        "fwade == 'serious'", "wadeserious.webp",
        "fwade == 'mad'", "wademad.webp",
        "fwade == 'surprise'", "wadesurprise.webp",
        "True", "wade.webp")
    )
image wade2 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch ( 
        "wade_look == 'summer'", "wade_summer2.webp",
        "wade_look == 2", "wade6.webp",
        "True", "wade2.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fwade == 'sad'", "wadesad.webp",
        "fwade == 'happy'", "wadehappy.webp",
        "fwade == 'smile'", "wadesmile.webp",
        "fwade == 'serious'", "wadeserious.webp",
        "fwade == 'mad'", "wademad.webp",
        "fwade == 'surprise'", "wadesurprise.webp",
        "True", "wade.webp")
    )
image wade3 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch ( 
        "wade_look == 2", "wade7.webp",
        "True", "wade3.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fwade == 'sad'", "wadesad.webp",
        "fwade == 'happy'", "wadehappy.webp",
        "fwade == 'smile'", "wadesmile.webp",
        "fwade == 'serious'", "wadeserious.webp",
        "fwade == 'mad'", "wademad.webp",
        "fwade == 'surprise'", "wadesurprise.webp",
        "True", "wade.webp")
    )
image wade4 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch ( 
        "wade_look == 2", "wade8.webp",
        "True", "wade4.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fwade == 'sad'", "wadesad.webp",
        "fwade == 'happy'", "wadehappy.webp",
        "fwade == 'smile'", "wadesmile.webp",
        "fwade == 'serious'", "wadeserious.webp",
        "fwade == 'mad'", "wademad.webp",
        "fwade == 'surprise'", "wadesurprise.webp",
        "True", "wade.webp")
    )
image wade_phone = Composite(
    (640, 1080),
    (0, 0), "wade_phone.webp",
    (0, 0), ConditionSwitch( 
        "fwade == 'sad'", "wadesad.webp",
        "fwade == 'happy'", "wadehappy.webp",
        "fwade == 'smile'", "wadesmile.webp",
        "fwade == 'serious'", "wadeserious.webp",
        "fwade == 'mad'", "wademad.webp",
        "fwade == 'surprise'", "wadesurprise.webp",
        "True", "wade.webp")
    )







image mom = Composite(
    (640, 1080),
    (0, 0), "mom2.webp",
    (0, 0), ConditionSwitch( 
        "fmom == 'sad'", "momsad.webp",
        "fmom == 'smile'", "momsmile.webp",
        "fmom == 'surprise'", "momsurprise.webp",
        "fmom == 'serious'", "momserious.webp",
        "fmom == 'cry'", "momcry.webp",
        "True", "mom.webp")
    )



image dad = Composite(
    (640, 1080),
    (0, 0), "dad1.webp",
    (0, 0), ConditionSwitch( 
        "fdad == 'sad'", "dadsad.webp",
        "fdad == 'smile'", "dadsmile.webp",
        "fdad == 'mad'", "dadmad.webp",
        "True", "dad.webp")
    )






default fmike = "n"
default mike_look = 1
default mike_hurt = 0
default mike_extras = 0



image mike = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "mike_look == 1", "mike1.webp",
        "mike_look == 'mma'", "mike_mma.webp",
        "mike_look == 2", "mike3.webp",
        "mike_look == 'summer'", "mike_summer1.webp",
        "mike_look == 'summer2'", "mike_summer2.webp",
        "mike_look == 'summer3'", "mike_summer3.webp",
        "mike_look == 'swim'", "mike_summer4.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fmike == 'sad'", "mikesad.webp",
        "fmike == 'happy'", "mikehappy.webp",
        "fmike == 'smile'", "mikesmile.webp",
        "fmike == 'blush'", "mikeblush.webp",
        "fmike == 'mad'", "mikemad.webp",
        "fmike == 'serious'", "mikeserious.webp",
        "fmike == 'flirt'", "mikeflirt.webp",
        "fmike == 'worried'", "mikeworried.webp",
        "True", "mike.webp"),
    (0, 0), ConditionSwitch( 
        "mike_extras == 'chain'", "mike_chain.webp",
        "True", Null()
    )
)
image mike2 = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "mike_look == 1", "mike2.webp",
        "mike_look == 2", "mike4.webp",
        "mike_look == 'summer2'", "mike_summer4.webp",
    ),
    (0, 0), ConditionSwitch( 
        "fmike == 'sad'", "mikesad.webp",
        "fmike == 'happy'", "mikehappy.webp",
        "fmike == 'smile'", "mikesmile.webp",
        "fmike == 'blush'", "mikeblush.webp",
        "fmike == 'mad'", "mikemad.webp",
        "fmike == 'serious'", "mikeserious.webp",
        "fmike == 'flirt'", "mikeflirt.webp",
        "fmike == 'worried'", "mikeworried.webp",
        "True", "mike.webp"),
    (0, 0), ConditionSwitch( 
        "mike_extras == 'chain'", "mike_chain.webp",
        "True", Null()
    )
)
image mikenude = Composite(
    (640, 1080),
    (0, 0), "mikenude.webp",
    (0, 0), ConditionSwitch( 
        "fmike == 'sad'", "mikesad.webp",
        "fmike == 'happy'", "mikehappy.webp",
        "fmike == 'smile'", "mikesmile.webp",
        "fmike == 'blush'", "mikeblush.webp",
        "fmike == 'mad'", "mikemad.webp",
        "fmike == 'serious'", "mikeserious.webp",
        "fmike == 'flirt'", "mikeflirt.webp",
        "fmike == 'worried'", "mikeworried.webp",
        "True", "mike.webp"),
    (0, 0), ConditionSwitch( 
        "mike_extras == 'chain'", "mike_chain.webp",
        "True", Null()
    )
)
image miketopless = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "mike_look == 'summer' or mike_look == 'summer2' or mike_look == 'summer3' or mike_look == 'swim'", "mike_summer4.webp",
        "True", "mike_topless.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fmike == 'sad'", "mikesad.webp",
        "fmike == 'happy'", "mikehappy.webp",
        "fmike == 'smile'", "mikesmile.webp",
        "fmike == 'blush'", "mikeblush.webp",
        "fmike == 'mad'", "mikemad.webp",
        "fmike == 'serious'", "mikeserious.webp",
        "fmike == 'flirt'", "mikeflirt.webp",
        "fmike == 'worried'", "mikeworried.webp",
        "True", "mike.webp"),
    (0, 0), ConditionSwitch( 
        "mike_extras == 'chain'", "mike_chain.webp",
        "True", Null()
    )
)
image mike_phone = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "mike_look == 'summer2'", "mike_summer_phone.webp",
        "True", "mike_summer_phone.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fmike == 'sad'", "mikesad.webp",
        "fmike == 'happy'", "mikehappy.webp",
        "fmike == 'smile'", "mikesmile.webp",
        "fmike == 'blush'", "mikeblush.webp",
        "fmike == 'mad'", "mikemad.webp",
        "fmike == 'serious'", "mikeserious.webp",
        "fmike == 'flirt'", "mikeflirt.webp",
        "fmike == 'worried'", "mikeworried.webp",
        "True", "mike.webp"),
    (0, 0), ConditionSwitch( 
        "mike_extras == 'chain'", "mike_chain.webp",
        "True", Null()
    )
)
image mike_pantless = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "mike_look == 'summer2'", "mike_summer_pantless.webp",
        "True", "mike_summer_pantless.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fmike == 'sad'", "mikesad.webp",
        "fmike == 'happy'", "mikehappy.webp",
        "fmike == 'smile'", "mikesmile.webp",
        "fmike == 'blush'", "mikeblush.webp",
        "fmike == 'mad'", "mikemad.webp",
        "fmike == 'serious'", "mikeserious.webp",
        "fmike == 'flirt'", "mikeflirt.webp",
        "fmike == 'worried'", "mikeworried.webp",
        "True", "mike.webp"),
    (0, 0), ConditionSwitch( 
        "mike_extras == 'chain'", "mike_chain.webp",
        "True", Null()
    )
)


image agnes = Composite(
    (640, 1080),
    (0, 0), "agnes1.webp",
    (0, 0), ConditionSwitch( 
        "fagnes == 'mad'", "agnesmad.webp",
        "fagnes == 'smile'", "agnessmile.webp",
        "fagnes == 'flirt'", "agnesflirt.webp",
        "True", "agnes.webp")
    )

image jessg = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "jess_look == 'summer'", "jessg_summer.webp",
        "jess_look == 'summer2'", "jessg_summer2.webp",
        "jess_look == 'bikini'", "jessg_bikini.webp",
        "jess_look == 'nymph'", "jess_nymph.webp",
        "True", "jessg1.webp"),
    (0, 0), ConditionSwitch( 
        "jess_look == 'nymph' and jess_bad", "jess_nymph_bad.webp",
        "True", "jessg.webp"),
    (0, 0), ConditionSwitch( 
        "fjess == 'mad' and jess_bad", "jessbmad.webp",
        "fjess == 'serious' and jess_bad", "jessbserious.webp",
        "fjess == 'smile' and jess_bad", "jessbsmile.webp",
        "fjess == 'sad' and jess_bad", "jessbsad.webp",
        "fjess == 'flirt' and jess_bad", "jessbflirt.webp",
        "fjess == 'n' and jess_bad", "jessb.webp",

        "fjess == 'mad'", "jessgmad.webp",
        "fjess == 'serious'", "jessgserious.webp",
        "fjess == 'smile'", "jessgsmile.webp",
        "fjess == 'sad'", "jessgsad.webp",
        "fjess == 'flirt'", "jessg.webp",
        "True", "jessg.webp")
    )

image jessb = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "jess_look == 'under'", "jessbunder.webp",
        "jess_look == 'under2'", "jessbunder2.webp",
        "jess_look == 2", "jessb2.webp",
        "jess_look == 1 and v12_jess_date == 3", "jessb3.webp",
        "jess_look == 'summer' and v12_jess_date == 3", "jessbg_summer.webp",
        "jess_look == 'summer2' and v12_jess_date == 3", "jessbg_summer2.webp",
        "jess_look == 'summer2' and v12_jess_date < 3", "jessb_summer2.webp",
        "jess_look == 'bikini' and v12_jess_date == 3", "jessbg_bikini.webp",
        "jess_look == 'bikini' and v12_jess_date < 3", "jessb_bikini.webp",
        "True", "jessb1.webp"),
    (0, 0), ConditionSwitch( 
        "fjess == 'mad'", "jessbmad.webp",
        "fjess == 'serious'", "jessbserious.webp",
        "fjess == 'smile'", "jessbsmile.webp",
        "fjess == 'sad'", "jessbsad.webp",
        "fjess == 'flirt'", "jessbflirt.webp",
        "True", "jessb.webp")
    )
image jessbnude = Composite(
    (640, 1080),
    (0, 0), "jessb_nude.webp",
    (0, 0), ConditionSwitch( 
        "fjess == 'mad'", "jessbmad.webp",
        "fjess == 'serious'", "jessbserious.webp",
        "fjess == 'smile'", "jessbsmile.webp",
        "fjess == 'sad'", "jessbsad.webp",
        "fjess == 'flirt'", "jessbflirt.webp",
        "True", "jessb.webp")
    )



default ian_victor = 3
default ian_victor_agenda = False
default lena_victor_agenda = False
default lena_billy = 3
default lena_billy_agenda = False
default ian_billy = 3
default ian_billy_agenda = False
default fvictor = "n"
default billy_look = 1
default fbilly = "n"
default billy_extras = 0
default billy_tattoo = 0

image billy = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "billy_look == 1", "billy1.webp",
        "billy_look == 2", "billy1.webp",
        "billy_look == 'summer'", "billy_summer.webp",
        "billy_look == 'swim'", "billy_swim.webp",
        "True", "billy1.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fbilly == 'smile'", "billysmile.webp",
        "fbilly == 'happy'", "billyhappy.webp",
        "fbilly == 'flirt'", "billyflirt.webp",
        "fbilly == 'sad'", "billysad.webp",
        "fbilly == 'serious'", "billyserious.webp",
        "True", "billy.webp"
    ),
    (0, 0), ConditionSwitch( 
        "billy_extras == 'phone'", "billy_phone.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "billy_tattoo", "billy_tattoo.webp",
        "True", Null()
    ),
)
image billynude = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "billy_look == 'soft'", "billynudesoft.webp",
        "True", "billynude.webp"
    ),
    (0, 0), "billy_chain2.webp",
    (0, 0), ConditionSwitch( 
        "fbilly == 'smile'", "billysmile.webp",
        "fbilly == 'happy'", "billyhappy.webp",
        "fbilly == 'flirt'", "billyflirt.webp",
        "fbilly == 'sad'", "billysad.webp",
        "fbilly == 'serious'", "billyserious.webp",
        "True", "billy.webp"
    ),
    (0, 0), ConditionSwitch( 
        "billy_tattoo", "billy_tattoo.webp",
        "True", Null()
    ),
)


image victor = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "fvictor == 'smile'", "victor_smile.webp",
        "True", "victor.webp"
    ),
)







image gillian = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "gillian_look == 'office'", "gillian3.webp",
        "gillian_look == 1", "gillian1.webp",
        "gillian_look == 2", "gillian2.webp"
    ),
    (0, 0), ConditionSwitch( 
        "gillian_extras == 'ring'", "gillian_ring.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "fgillian == 'sad'", "gilliansad.webp",
        "fgillian == 'happy'", "gillianhappy.webp",
        "fgillian == 'smile'", "gilliansmile.webp",
        "fgillian == 'blush'", "gillianblush.webp",
        "fgillian == 'slut'", "gillianslut.webp",
        "fgillian == 'surprise'", "gilliansurprise.webp",
        "fgillian == 'cry'", "gilliancry.webp", 
        "fgillian == 'worried'", "gillianworried.webp", 
        "True", "gillian.webp")
)

image gillian2 = Composite(
    (640, 1080), 
    (0, 0), ConditionSwitch( 
        "gillian_look == 'office'", "gillian3b.webp",
        "gillian_look == 1", "gillian1b.webp",
        "gillian_look == 2", "gillian2b.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fgillian == 'sad'", "gilliansad.webp",
        "fgillian == 'happy'", "gillianhappy.webp",
        "fgillian == 'smile'", "gilliansmile.webp",
        "fgillian == 'blush'", "gillianblush.webp",
        "fgillian == 'slut'", "gillianslut.webp",
        "fgillian == 'surprise'", "gilliansurprise.webp",
        "fgillian == 'cry'", "gilliancry.webp", 
        "fgillian == 'worried'", "gillianworried.webp", 
        "True", "gillian.webp")
)






image mark = Composite(
    (640, 1080),
    (0, 0), "mark1.webp",
    (0, 0), ConditionSwitch( 
        "fmark == 'sad'", "marksad.webp",
        "fmark == 'smile'", "marksmile.webp",
        "fmark == 'serious'", "markserious.webp",
        "fmark == 'flirt'", "markflirt.webp",
        "True", "mark.webp")
)
image marktopless = Composite(
    (640, 1080),
    (0, 0), "mark2.webp",
    (0, 0), ConditionSwitch( 
        "fmark == 'sad'", "marksad.webp",
        "fmark == 'smile'", "marksmile.webp",
        "fmark == 'serious'", "markserious.webp",
        "fmark == 'flirt'", "markflirt.webp",
        "True", "mark.webp")
)
image marknude = Composite(
    (640, 1080),
    (0, 0), "marknude.webp",
    (0, 0), ConditionSwitch( 
        "fmark == 'sad'", "marksad.webp",
        "fmark == 'smile'", "marksmile.webp",
        "fmark == 'serious'", "markserious.webp",
        "fmark == 'flirt'", "markflirt.webp",
        "True", "mark.webp")
)





image nat = Composite(
    (640, 1080),
    (0, 0), "nat1.webp",
    (0, 0), ConditionSwitch( 
        "fnat == 'sad'", "natsad.webp",
        "fnat == 'smile'", "natsmile.webp",
        "True", "nat.webp")
)


default fcharles = "n"
default lena_charles_agenda = False
default ian_charles_agenda = False

image charles = Composite(
    (640, 1080),
    (0, 0), "charles1.webp",
    (0, 0), ConditionSwitch( 
        "fcharles == 'sad'", "charlessad.webp",
        "fcharles == 'smile'", "charlessmile.webp",
        "fcharles == 'serious'", "charlesserious.webp",
        "True", "charles.webp")
    )

image peter = Composite(
    (640, 1080),
    (0, 0), "peter1.webp",
    (0, 0), ConditionSwitch( 
        "fpeter == 'serious'", "peterserious.webp",
        "fpeter == 'sad'", "petersad.webp",
        "fpeter == 'evil'", "peterevil.webp",
        "fpeter == 'smile'", "petersmile.webp",
        "True", "peter.webp")
    )

image marcel = Composite(
    (640, 1080),
    (0, 0), "marcel1.webp",
    (0, 0), ConditionSwitch( 
        "fcharles == 'sad'", "marcelsad.webp",
        "fcharles == 'smile'", "marcelsmile.webp",
        "fcharles == 'mad'", "marcelmad.webp",
        "True", "marcel.webp")
    )

image eli = Composite(
    (640, 1080),
    (0, 0), "eli1.webp",
    (0, 0), ConditionSwitch( 
        "feli == 'shy'", "elishy.webp",
        "feli == 'blush'", "eliblush.webp",
        "True", "eli.webp")
    )

image finley = Composite(
    (640, 1080),
    (0, 0), "finley1.webp",
    (0, 0), ConditionSwitch( 
        "ffinley == 'sad'", "finleysad.webp",
        "ffinley == 'smile'", "finleysmile.webp",
        "True", "finley.webp")
    )

image sen = Composite(
    (640, 1080),
    (0, 0), "sen1.webp",
    (0, 0), ConditionSwitch( 
        "fsen == 'sad'", "sensad.webp",
        "fsen == 'smile'", "sensmile.webp",
        "fsen == 'mad'", "senmad.webp",
        "True", "sen.webp")
    )

image john = Composite(
    (640, 1080),
    (0, 0), "john1.webp",
    (0, 0), ConditionSwitch( 
        "fjohn == 'sad'", "johnsad.webp",
        "fjohn == 'smile'", "johnsmile.webp",
        "fjohn == 'serious'", "johnserious.webp",
        "True", "john.webp")
    )

image rosa = Composite(
    (640, 1080),
    (0, 0), "rosa1.webp",
    (0, 0), ConditionSwitch( 
        "frosa == 'sad'", "rosasurprise.webp",
        "frosa == 'smile'", "rosasmile.webp",
        "frosa == 'mad'", "rosamad.webp",
        "frosa == 'surprise'", "rosasurprise.webp",
        "frosa == 'serious'", "rosaserious.webp",
        "True", "rosa.webp")
    )

image jack = Composite(
    (640, 1080),
    (0, 0), "jack1.webp",
    (0, 0), ConditionSwitch( 
        "fjack == 'mad'", "jackmad.webp",
        "fjack == 'smile'", "jacksmile.webp",
        "fjack == 'serious'", "jackserious.webp",
        "True", "jack.webp")
    )


image marcel = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "fmarcel == 'sad'", "bouncersad.webp",
        "fmarcel == 'mad'", "bouncermad.webp",
        "fmarcel == 'smile'", "bouncersmile.webp",
        "True", "bouncer.webp")
    )


image arthur = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "arthur_look == 1", "arthur1.webp",
        "True", "arthur1.webp"
    ),
    (0, 0), ConditionSwitch( 
        "farthur == 'smile'", "arthursmile.webp",
        "farthur == 'sad'", "arthursad.webp",
        "farthur == 'mad'", "arthurmad.webp",
        "True", "arthur.webp"
    ),
)


image anthony = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "anthony_look == 'swim'", "anthony5.webp",
        "anthony_look == 2", "anthony2.webp",
        "anthony_look == 3", "anthony3.webp",
        "True", "anthony1.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fanthony == 'smile'", "anthonysmile.webp",
        "fanthony == 'sad'", "anthonysad.webp",
        "fanthony == 'serious'", "anthonyserious.webp",
        "fanthony == 'mad'", "anthonymad.webp",
        "True", "anthony.webp")
)
image anthony_topless = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "anthony_look > 1", "anthony5.webp",
        "True", "anthony4.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fanthony == 'smile'", "anthonysmile.webp",
        "fanthony == 'sad'", "anthonysad.webp",
        "fanthony == 'serious'", "anthonyserious.webp",
        "fanthony == 'mad'", "anthonymad.webp",
        "True", "anthony.webp")
)
image anthonynude = Composite(
    (640, 1080),
    (0, 0), "anthony_nude.webp",
    (0, 0), ConditionSwitch( 
        "fanthony == 'smile'", "anthonysmile.webp",
        "fanthony == 'sad'", "anthonysad.webp",
        "fanthony == 'serious'", "anthonyserious.webp",
        "fanthony == 'mad'", "anthonymad.webp",
        "True", "anthony.webp")
)
image anthony_pantless = Composite(
    (640, 1080),
    (0, 0), "anthony_pantless.webp",
    (0, 0), ConditionSwitch( 
        "fanthony == 'smile'", "anthonysmile.webp",
        "fanthony == 'sad'", "anthonysad.webp",
        "fanthony == 'serious'", "anthonyserious.webp",
        "fanthony == 'mad'", "anthonymad.webp",
        "True", "anthony.webp")
)

image zarina = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "zarina_look == 2", "zarina2.webp",
        "zarina_look == 'nymph'", "zarina3.webp",
        "True", "zarina1.webp"
    ),
    (0, 0), ConditionSwitch( 
        "zarina_extras == 'bag'", "zarina_bag.webp",
        "True", Null()
    ),
    (0, 0), ConditionSwitch( 
        "fzarina == 'smile'", "zarinasmile.webp",
        "fzarina == 'sad'", "zarinasad.webp",
        "fzarina == 'serious'", "zarinaserious.webp",
        "fzarina == 'happy'", "zarinahappy.webp",
        "True", "zarina.webp")
)
image zarinanude = Composite(
    (640, 1080),
    (0, 0), "zarina_nude.webp",
    (0, 0), ConditionSwitch( 
        "fzarina == 'smile'", "zarinasmile.webp",
        "fzarina == 'sad'", "zarinasad.webp",
        "fzarina == 'serious'", "zarinaserious.webp",
        "fzarina == 'happy'", "zarinahappy.webp",
        "True", "zarina.webp")
)

image sonia = Composite(
    (640, 1080),
    (0, 0), ConditionSwitch( 
        "sonia_look == 2", "sonia2.webp",
        "sonia_look == 'nymph'", "sonia3.webp",
        "True", "sonia1.webp"
    ),
    (0, 0), ConditionSwitch( 
        "fsonia == 'smile'", "soniasmile.webp",
        "fsonia == 'sad'", "soniasad.webp",
        "fsonia == 'serious'", "soniaserious.webp",
        "True", "sonia.webp")
)
image sonianude = Composite(
    (640, 1080),
    (0, 0), "sonia_nude.webp",
    (0, 0), ConditionSwitch( 
        "fsonia == 'smile'", "soniasmile.webp",
        "fsonia == 'sad'", "soniasad.webp",
        "fsonia == 'serious'", "soniaserious.webp",
        "True", "sonia.webp")
)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
