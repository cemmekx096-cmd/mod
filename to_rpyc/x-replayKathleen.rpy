screen replaykathleen():
    modal True tag menu

    add "screen"


    imagemap:

        idle "gui/screens/imagemaps/replay_idle.png"
        hover "gui/screens/imagemaps/replay_hover.png"
        ground "gui/screens/backgrounds/replay_kathleen.png"
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
        [persistent.FEG1Gallery, "FauxExhibitionGame1", "prFaceOffEndurance", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Progress through the story."],
        [persistent.FEG2Gallery, "FauxExhibitionGame2", "prFaceOffServility", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Progress through the story."],
        [persistent.FEG3VeroGallery, "FauxExhibitionGame3Vero", "prFaceOffCarnalityVer", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "perk_socialChameleon":True, "perk_socialButterfly":True, "history_voyeur":True, "kat_polite":True}, "Progress through the story."],
        [persistent.gonzoRewardGallery, "gonzoReward", "w1GonzoRewardStart", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "history_voyeur":True, "kat_polite":True}, "Nail the Carnation interview during week 1."],
        [persistent.w1ExGame2VeroFelGallery, "w1ExGame2VeroFel", "w1ExFollowThroughVeroFel", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Rosalind won week 1, game 1."],
        [persistent.w1ExGame2VeroRoseGallery, "w1ExGame2VeroRose", "w1ExFollowThroughVeroRose", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Felicia won week 1, game 1."],
        [persistent.w1ExGame2RoseFelGallery, "w1ExGame2RoseFel", "w1ExFollowThroughRoseFel", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Veronica won week 1, game 1."],
        [persistent.w2KatBirthdayGiftGallery, "w2KatBirthdayGift", "w2KatBirthdayGift", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Accept Mrs. Pulman's gift."],
        [persistent.w2KatSceneGallery, "w2KatScene", "w2EdwinKatScene", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True, "w1ExGame2WinnerRose":True }, "Mrs. Pulman trusts you."],
        [persistent.veroW2Shame, "veroW2Shame", "w2ExVeronicaHumiliation", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True},"Progress through the story."],
        [persistent.felW2Shame, "felW2Shame", "w2ExFeliciaHumiliation", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True, "feliciaFlag":True, "w2FeliciaImpressed":True},"Progress through the story."],
        [persistent.roseW2Shame, "roseW2Shame", "w2ExRosalindHumiliation", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True, "Killian_Bromance":99, "w2RosalindPhoto": True, "perk_socialChameleon":True},"Progress through the story."],
        [persistent.w3dream, "w3dream", "w3KathleenStart", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"After the week 2 Exhibition, \visit Kathleen."],
        [persistent.w3ShockGame, "w3ShockGame", "w3ShockGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"Progress through the story."],
        [persistent.w3PunishGame, "w3VeroPunish", "w3PunishGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2ExLoserVeronica": True, "w1GonzoReward":True, "w1ExIntuitionGameWinnerRose":True},"Progress through the story."],
        [persistent.w3PunishGame, "w3FelPunish", "w3PunishGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2ExLoserFelicia":True, "w1GonzoReward":True},"Progress through the story."],
        [persistent.w3PunishGame, "w3VeroFel", "w3PunishGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2ExLoserDuo":True, "w1GonzoReward":True},"Progress through the story."],
        [persistent.w3PunishGame, "w3AllPunish", "w3PunishGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2ExLosersAll":True, "w1GonzoReward":True},"Progress through the story."],
        [persistent.w3KathleenTest, "w3KathleenTest", "w3KatEnlightenmentContinue", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True, "hanaFlag":True},"Progress through the story."],
        [persistent.w3KatFlirt, "w3KatFlirt", "w3ExHallwayKatBother", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w3KatSnare":True, "kat_polite":True, "Kathleen_Affection":99},"Do something stupid."],


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
