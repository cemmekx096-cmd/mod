screen replayfelicia():
    modal True tag menu

    add "screen"


    imagemap:

        idle "gui/screens/imagemaps/replay_idle.png"
        hover "gui/screens/imagemaps/replay_hover.png"
        ground "gui/screens/backgrounds/replay_felicia.png"
        selected_idle "gui/screens/imagemaps/replay_selected_idle.png"
        selected_hover "gui/screens/imagemaps/replay_selected_hover.png"


        hotspot (105,28,300,50) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("leisureroom"), [ Play ("hover_load", "sound effects/click.wav") ]

        hotspot (73, 140, 80, 80) action [ Play ("menu_click","sound effects/page-turn.wav") ], [Return()]

        hotspot (168,142, 80, 80) action [ Play ("menu_click","sound effects/page-turn.wav") ], ui.callsinnewcontext("galleryNameChange2")

        hotspot (59,223, 300, 100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("replayrosalind") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (57, 323, 300, 100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("replaymina") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (59, 428, 300, 100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("replayhana") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (49, 518, 300, 100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("replayfelicia") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (55, 617, 300, 100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("replayveronica") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (47, 717, 300, 100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("replaykathleen") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (47, 824, 300, 100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("replaymisc") hovered [ Play ("hover_load", "sound effects/click.wav") ]

        hotspot (1572,985,300,100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("jukebox"), Hide("scenereplay") hovered [ Play ("hover_load", "sound effects/click.wav") ]


    python:
        sceneGalleryList = [
        
        [persistent.felBathroomGallery, "felDiscoBathroom", "prDiscoFeliciaBathroomSexStart", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "perk_strongman":True, "history_voyeur":True}, "Ignore Mina at the club and do shots with Felicia."],
        [persistent.minaFeliciaKissGallery, "minaFeliciaKiss", "prAfterPartyMinaFeliciaKiss", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Afterparty: Use your get out of jail card on Felicia."],
        [persistent.felAfterPartyGallery, "felDiscoAfterParty", "prFelAfterPartyFun", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Afterparty: Accept Felicia's advances."],
        [persistent.felDiscoThreesomeGallery, "felDiscoThreesome", "prAfterPartyThreesome", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Afterparty, high bromance: invite Killian to jon you."],
        [persistent.felGonzoGallery, "felGonzo", "w1FelInterview", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "perk_socialChameleon":True, "perk_socialButterfly":True, "history_voyeur":True, "kat_polite":True}, "Interview Felicia during Week 1."],
        [persistent.felW1FantasyGallery, "felW1Fantasy", "w1FelFantasy", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Felicia route: progress through the story."],
        [persistent.felExhibition1Game1, "felExhibition1Game1", "w1ExIntuitionGameFelicia", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Progress through the story."],
        [persistent.w1ExGame2VeroFelGallery, "w1ExGame2VeroFel", "w1ExFollowThroughVeroFel", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Rosalind won week 1, game 1."],
        [persistent.w1ExGame2RoseFelGallery, "w1ExGame2RoseFel", "w1ExFollowThroughRoseFel", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Veronica won week 1, game 1."],
        [persistent.w1ExGame3FelGallery, "w1ExGame3Fel", "w1ExEarningsGameFelicia", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Felicia lost some variation of week 1, game 2."],
        [persistent.w2ShamePhotoshootGallery, "w2ShamePhotoshoot", "w2ShamePhotoshoot", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w1FelAss":True, "kat_polite":True, "Veronica_Horniness":99}, "Progress through the story."],
        [persistent.w2FeliciaEggStuff, "w2FeliciaEggStuff", "w2FeliciaStuffed", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "feliciaFlag":True},"Unlocked automatically."],
        [persistent.w2FeliciaConvoTease, "w2FeliciaConvoTease", "w2FeliciaConvoTease", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "feliciaFlag":True, "kat_polite":True, "Felicia_Affection":99, "w2FeliciaPacked":True},"Unlocked automatically."],
        [persistent.w2FeliciaBathroomJill, "w2FeliciaBathroomJill", "w2FeliciaBathroomJill", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "felPN":"Daddy", "kat_polite":True, "Felicia_Affection":99, "w2FeliciaPacked":True, "feliciaFlag":True},"Accept Felicia's video call."],
        [persistent.w2FeliciaSex, "w2FeliciaSex", "w2FeliciaSex", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "felPN":"Daddy", "kat_polite":True, "Felicia_Affection":99, "w2FeliciaPacked":True, "w2FeliciaExtra":True, "feliciaFlag":True},"While on Felcia's path, choose to take it further."],
        [persistent.felW2grope, "felW2grope", "w2ExFeliciaMingleA", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w1GonzoReward": True, "w2ExRosalindMingleARepeat": True},"During Week 2's Exhibition, settle a bet."],
        [persistent.felW2Shame, "felW2Shame", "w2ExFeliciaHumiliation", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True, "feliciaFlag":True, "w2FeliciaImpressed":True},"Progress through the story."],
        [persistent.w3dream, "w3dream", "w3KathleenStart", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"After the week 2 Exhibition, \visit Kathleen."],
        [persistent.w3ShockGame, "w3ShockGame", "w3ShockGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"Progress through the story."],
        [persistent.w3PunishGame, "w3VeroPunish", "w3PunishGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2ExLoserVeronica": True, "w1GonzoReward":True, "w1ExIntuitionGameWinnerRose":True},"Progress through the story."],
        [persistent.w3PunishGame, "w3FelPunish", "w3PunishGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2ExLoserFelicia":True, "w1GonzoReward":True},"Progress through the story."],
        [persistent.w3PunishGame, "w3VeroFel", "w3PunishGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2ExLoserDuo":True, "w1GonzoReward":True},"Progress through the story."],
        [persistent.w3PunishGame, "w3AllPunish", "w3PunishGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2ExLosersAll":True, "w1GonzoReward":True},"Progress through the story."],
        [persistent.w3FeliciaSoloPath, "w3FeliciaSoloPath", "w3FeliciaRomanceRising", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"After Felicia's art date, opt to spend time with her alone."],
        [persistent.w3FeliciaMinaThreesome, "w3FeliciaMinaThreesome", "w3FeliciaMinaFun", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "feliciaDaddy":True},"The more the merrier."],\
        [persistent.w3FeliciaRSKiss, "w3FeliciaRSKiss", "w3RockShowFeliciaGreeting", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w3FeliciaSoloEnd":True},"After spending the night with Felicia painting, call her during the rock show."],
        ]

    vpgrid:
        cols 3
        spacing 18
        scrollbars "vertical"
        mousewheel True
        draggable True
        pos (0.445, 0.165)
        ymaximum 725

        for i in sceneGalleryList:
            if i[0]:
                imagebutton:
                    auto "images/misc/scene replay/"+i[1]+"_%s.png"
                    action Replay(i[2], scope=i[3], locked=False)
            else:
                imagebutton:
                    action NullAction()
                    idle "images/misc/scene replay/"+i[1]+"_locked.png"
                    tooltip i[4]
    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]":
            pos (650, 8)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
