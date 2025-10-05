screen replayveronica():
    modal True tag menu

    add "screen"


    imagemap:

        idle "gui/screens/imagemaps/replay_idle.png"
        hover "gui/screens/imagemaps/replay_hover.png"
        ground "gui/screens/backgrounds/replay_veronica.png"
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
        
        [persistent.katCarnationInterviewReplay, "katCarnationInterview", "prMay12meeting", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "perk_socialChameleon":True}, "Progress through the story."],
        [persistent.VeroEggInsertGallery, "VeroEggInsert", "prFaceOffVerRotor", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Progress through the story."],
        [persistent.FEG1Gallery, "FauxExhibitionGame1", "prFaceOffEndurance", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Progress through the story."],
        [persistent.FEG2Gallery, "FauxExhibitionGame2", "prFaceOffServility", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Progress through the story."],
        [persistent.FEG3VeroGallery, "FauxExhibitionGame3Vero", "prFaceOffCarnalityVer", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "perk_socialChameleon":True, "perk_socialButterfly":True, "history_voyeur":True, "kat_polite":True}, "Progress through the story."],
        [persistent.veroGonzoGallery, "veroGonzo", "w1VeroInterview", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Interview Veronica during Week 1."],
        [persistent.w1MinaVeroGym, "w1MinaVeroGym", "w1VeroMinaExercise", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Go to the gym with Mina."],
        [persistent.veroEx1Grope, "veroEx1Grope", "w1ExVeronica", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "Veronica_Horniness":99}, "Visit Veronica before exhibition #1."],
        [persistent.veroExhibition1Game1, "veroExhibition1Game1", "w1ExIntuitionGameVeronica", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Progress through the story."],
        [persistent.w1ExGame2VeroFelGallery, "w1ExGame2VeroFel", "w1ExFollowThroughVeroFel", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Rosalind won week 1, game 1."],
        [persistent.w1ExGame2VeroRoseGallery, "w1ExGame2VeroRose", "w1ExFollowThroughVeroRose", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Felicia won week 1, game 1."],
        [persistent.w1ExGame3VeroGallery, "w1ExGame3Vero", "w1ExEarningsGameVeronica", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Veronica lost some variation of week 1, game 2."],
        [persistent.w2ShamePhotoshootGallery, "w2ShamePhotoshoot", "w2ShamePhotoshoot", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w1FelAss":True, "kat_polite":True, "Veronica_Horniness":99}, "Progress through the story."],
        [persistent.veroW2GymSceneGallery, "veroW2Gym", "w2VeronicaGymphotoshoot", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True, "Veronica_Affection":99, "minaGym":True}, "Progress through the story."],
        [persistent.veroW2ScratchGallery, "veroW2Scratch", "w2VeronicaphotoshootExtended", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "Veronica_Affection":99, "w2VeronicaSquirm":True}, "Have Veronica propose a deal."],
        [persistent.veroW2MCScratchGallery, "veroW2MCScratch", "w2VeronicaEdwinScratch", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "Veronica_Affection":99, "prVero_Facial":True, "VeroFlag":True}, "Scratch Veronica's back."],
        [persistent.hanaW2Dream, "hanaW2Dream", "w2HanaDream", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Unlocked if you accept Hana's birthday present and then choose to hold her."],
        [persistent.veroW2Shame, "veroW2Shame", "w2ExVeronicaHumiliation", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True},"Progress through the story."],
        [persistent.w3ShockGame, "w3ShockGame", "w3ShockGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"Progress through the story."],
        [persistent.w3PunishGame, "w3VeroPunish", "w3PunishGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2ExLoserVeronica": True, "w1GonzoReward":True, "w1ExIntuitionGameWinnerRose":True},"Progress through the story."],
        [persistent.w3PunishGame, "w3FelPunish", "w3PunishGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2ExLoserFelicia":True, "w1GonzoReward":True},"Progress through the story."],
        [persistent.w3PunishGame, "w3VeroFel", "w3PunishGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2ExLoserDuo":True, "w1GonzoReward":True},"Progress through the story."],
        [persistent.w3PunishGame, "w3AllPunish", "w3PunishGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2ExLosersAll":True, "w1GonzoReward":True},"Progress through the story."],
        [persistent.w3VeronicaDance, "w3VeronicaDance", "w3VeronicaDanceOff", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"Dance!"],
        [persistent.w3VeronicaKiss, "w3VeronicaKiss", "w3VeronicaBeachKiss", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"After inviting Veronica to dance, n\take it further.."],
        [persistent.w3VeronicaSex, "w3VeronicaSex", "w3VeronicaFinallyFuckingPraiseBe", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"A kiss leads to..."],
        [persistent.w3VeronicaStory, "w3VeronicaStory", "w3VeroCheckingIn", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "feliciaFlag":True, "w3VeronicaWingman":True},"Play wingman."],
        [persistent.w3VeroMinaKiss, "w3VeroMinaKiss", "w3RockShowVeroMinaGetPersonal", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w3RockShowHanaPath":True},"During Hana's second rock show, push Mina toward Veronica."],
        [persistent.w3VeroMinaLez, "w3VeroMinaLez", "w3RockShowVeroMinaVIP", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w3RockShowHanaPath":True},"During Hana's second rock show, push Mina toward Veronica."],
        [persistent.w3VeroVIPKiss, "w3VeroVIPKiss", "w3RockShowVeroVIP", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"During Hana's second rock show, while on her path, focus on Veronica."],
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
