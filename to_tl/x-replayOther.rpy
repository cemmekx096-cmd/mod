screen replaymisc():
    tag menu
    modal True

    add "screen"


    imagemap:

        idle "gui/screens/imagemaps/replay_idle.png"
        hover "gui/screens/imagemaps/replay_hover.png"
        ground "gui/screens/backgrounds/replay_misc.png"
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
        [persistent.HarpSaunaBJGallery, "HarpSaunaBJ", "prLeisureTime", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Progress through the story."],
        [persistent.FEG1Gallery, "FauxExhibitionGame1", "prFaceOffEndurance", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Progress through the story."],
        [persistent.FEG3LucyGallery, "FauxExhibitionGame3Lucy", "prFaceOffCarnalityLucy", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Progress through the story."],
        [persistent.gonzoRewardGallery, "gonzoReward", "w1GonzoRewardStart", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "history_voyeur":True, "kat_polite":True}, "Nail the Carnation interview during week 1."],
        [persistent.w2HanaZaraFBGallery, "w2HanaZaraFB", "w2HanaLezStory", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "During Never Have I Ever, ask a spicy question."],
        [persistent.w2KatBirthdayGiftGallery, "w2KatBirthdayGift", "w2KatBirthdayGift", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Accept Mrs. Pulman's gift."],
        [persistent.w2IanMaid3some, "w2IanMaid3some", "w2MinaStart", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Unlocked automatically."],
        [persistent.daliaW2Sauna, "daliaW2Sauna", "w2ExSauna", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2HarpRainCheck":True, "w2VeronicaScratch":True},"Get to the bottom of Samson's duplicity."],
        [persistent.harperlucyW2Lez, "harperlucyW2Lez", "w2ExLezB", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "history_voyeur":True},"During Week 2's Exhibition indulge your voyeuristic tendencies."],
        [persistent.w3PunishGame, "w3VeroPunish", "w3PunishGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2ExLoserVeronica": True, "w1GonzoReward":True, "w1ExIntuitionGameWinnerRose":True},"Progress through the story."],
        [persistent.w3PunishGame, "w3FelPunish", "w3PunishGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2ExLoserFelicia":True, "w1GonzoReward":True},"Progress through the story."],
        [persistent.w3PunishGame, "w3VeroFel", "w3PunishGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2ExLoserDuo":True, "w1GonzoReward":True},"Progress through the story."],
        [persistent.w3PunishGame, "w3AllPunish", "w3PunishGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2ExLosersAll":True, "w1GonzoReward":True},"Progress through the story."],
        [persistent.w3VicMidTierFBSex, "w3VicMidTierFBSex", "w3MinaPornWatch", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"Be on Mina's Path."],
        [persistent.w3AlicePhoneSex, "w3AlicePhoneSex", "w3AliceFakeThreesome", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"Let your curiosity get the better of you."],
        [persistent.w3LBBathroomBJ, "w3LBBathroomBJ", "w3BathroomFrollick", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"Play Wingman for Veronica."],
        [persistent.w3LucyAffable, "w3LucyAffable", "w3LucyCommiserate", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w3LucyAffability":99}, "Be a little understanding."],
        [persistent.w3LucyQPQ, "w3LucyQPQ", "w3LucyGrabby", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "toughness":99, "w1GonzoReward":True, "w3LucyPressure":99},"Do what you know you really want to do."],
        [persistent.w3AndreaPublic, "w3AndreaPublic", "w3AndreaAction", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"Meeting Donovan: how hard can it be to charm an air head?"],
        [persistent.w3VickyTapePart1, "w3VickyTapePart1", "w3VickySmutPart1", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"Progress through the story."],
        [persistent.w3BartenderFun, "w3BartenderFun", "w3RockShowBartenderPaysOff", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"Pretty much ignore everyone at Hana's 2nd rock show."],
        [persistent.w3VickyTapePart2, "w3VickyTapePart2", "w3VickySmutPart4", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"Watch Vicky's tape."],
        [persistent.w3LucyFuck, "w3LucyFuck", "w3ExLucyFuck", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "perk_strongman":True},"Make a move on a sad Lucy."],
        [persistent.w3OrgyStart, "w3OrgyStart", "w3ExOrgyStart", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "Allison_Interest":99},"Progress through the story."],
        [persistent.w3OrgySophia, "w3OrgySophia", "w3ExSophiaOrgy", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"Build a rapport with Sophia and distract her at the orgy."],
        [persistent.w3OrgyAllison, "w3OrgyAllison", "w3ExOrgyAllison", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "feliciaSex":True},"Build a rapport with Allison and make a move during the orgy."],

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
