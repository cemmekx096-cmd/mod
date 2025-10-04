default persistent.modGalleryUnlock = False

init 100 screen replayfelicia():
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
            if i[0] or persistent.modGalleryUnlock:
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

    vbox:
        xalign 0.7
        yalign 0.975
        if persistent.modGalleryUnlock:
            textbutton "Lock Scenes":
                action SetVariable("persistent.modGalleryUnlock", False)
                text_size 40
                text_idle_color "#E19ACD"
                text_hover_color gui.hover_color
        else:
            textbutton "Unlock Scenes":
                action SetVariable("persistent.modGalleryUnlock", True)
                text_size 40
                text_idle_color "#E19ACD"
                text_hover_color gui.hover_color

        text "By DA":
            size 20
            color "#03b420"
            xalign 0.5
            ypos 5

init 100 screen replayhana():
    modal True tag menu

    add "screen"
    imagemap:
        idle "gui/screens/imagemaps/replay_idle.png"
        hover "gui/screens/imagemaps/replay_hover.png"
        ground "gui/screens/backgrounds/replay_hana.png"
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
        [persistent.w2HanaZaraFBGallery, "w2HanaZaraFB", "w2HanaLezStory", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "During Never Have I Ever, ask a spicy question."],
        [persistent.w2HanaBDGallery, "w2HanaBD", "w2BirthDayHanaPresent", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Accept Hana's birthday present."],
        [persistent.hanaW2Dream, "hanaW2Dream", "w2HanaDream", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Unlocked if you accept Hana's birthday present and then choose to hold her."],
        [persistent.hanaW2DryHump, "hanaw2DryHump", "w2HanaDryHump", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Unlocked if you accept Hana's birthday present and then choose to hold her."],
        [persistent.hanaMCKiss, "hanaMCKiss", "w2HanaMCKiss", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "hanaFlag":True, "w2HanaHump":True, "w2HanaSex":True}, "Unlocked if you accept Hana's birthday present and then choose to hold her."],
        [persistent.w3dream, "w3dream", "w3KathleenStart", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"After the week 2 Exhibition, visit Kathleen."],
        [persistent.w3moviemakeout, "w3moviemakeout", "w3HanaMovieMakeout", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"Get physical during the movie date with Hana."],
        [persistent.w3karaokemakeout, "w3karaokemakeout", "w3HanaDateKaraoke", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w3HanaDP":99},"Get physical during the karaoke date with Hana."],
        [persistent.w3hanafuckfest, "w3hanafuckfest", "w3HanaDateFuckFest", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w3HanaDP":99},"Hana was sufficiently revved up during the date."],
        [persistent.w3HanaRomanceSex, "w3HanaRomanceSex", "w3HanaRomanceSex", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w3HanaDP":99},"Promise Hana."],
        [persistent.w3HanaPhoneSex, "w3HanaPhoneSex", "w3CutieCallHana", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"Call Hana when you can't sleep."],
        [persistent.w3HanaFacefuck, "w3HanaFacefuck", "w3HanaSuckSuckSuck", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w3HanaCutieCall": True, "w3HanaDP":99},"Publicly show your affection."],
        [persistent.w3HanaMinaLez, "w3HanaMinaLez", "w3RockShowHanaMinaParkingLot", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "Mina_BiCurious":99},"While in a relationship with Mina and Hana, go on stage..."],
        [persistent.w3HanaRSKiss, "w3HanaRSKiss", "w3RockShowMCJam", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w3HanaDP":99, "hanaGF":True},"During Hana's show, cheer for your goth bae."],
        [persistent.w3HanaRoom, "w3HanaRoom", "w3PreExHanaVisit", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w3HanaClubKiss":True},"Visit your girlfriend after a heavy morning at your Mom's."],
        [persistent.w3HanaPaizuri, "w3HanaPaizuri", "w3ExHanaPhotoShoot", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w3HanaBrothelRP":True, "hanaGF":True},"Stick with Hana after showing Elias around."],
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
            if i[0] or persistent.modGalleryUnlock:
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

    vbox:
        xalign 0.7
        yalign 0.975
        if persistent.modGalleryUnlock:
            textbutton "Lock Scenes":
                action SetVariable("persistent.modGalleryUnlock", False)
                text_size 40
                text_idle_color "#E19ACD"
                text_hover_color gui.hover_color
        else:
            textbutton "Unlock Scenes":
                action SetVariable("persistent.modGalleryUnlock", True)
                text_size 40
                text_idle_color "#E19ACD"
                text_hover_color gui.hover_color

        text "By DA":
            size 20
            color "#03b420"
            xalign 0.5
            ypos 5

init 100 screen replaykathleen():
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
            if i[0] or persistent.modGalleryUnlock:
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

    vbox:
        xalign 0.7
        yalign 0.975
        if persistent.modGalleryUnlock:
            textbutton "Lock Scenes":
                action SetVariable("persistent.modGalleryUnlock", False)
                text_size 40
                text_idle_color "#E19ACD"
                text_hover_color gui.hover_color
        else:
            textbutton "Unlock Scenes":
                action SetVariable("persistent.modGalleryUnlock", True)
                text_size 40
                text_idle_color "#E19ACD"
                text_hover_color gui.hover_color

        text "By DA":
            size 20
            color "#03b420"
            xalign 0.5
            ypos 5

init 100 screen replaymina():
    modal True tag menu

    add "screen"
    imagemap:
        idle "gui/screens/imagemaps/replay_idle.png"
        hover "gui/screens/imagemaps/replay_hover.png"
        ground "gui/screens/backgrounds/replay_mina.png"
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
        [persistent.minaFeliciaKissGallery, "minaFeliciaKiss", "prAfterPartyMinaFeliciaKiss", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Afterparty: Use your get out of jail card on Felicia."],
        [persistent.minaMCKissGallery, "minaMCKiss", "prAfterPartyMinaKiss", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Afterparty: The bottle has spoken. Kiss Mina."],
        [persistent.w1MinaVeroGym, "w1MinaVeroGym", "w1VeroMinaExercise", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Go to the gym with Mina."],
        [persistent.w2MinaKissGallery, "w2MinaKiss", "w2MinaLineReadingPart2", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2MinaScenePoints":99, "Mina_KLove":0}, "Put on a convincing performance  with a doubting Mina."],
        [persistent.w2MinaMindBlown, "w2MinaMindBlown", "w2MinaMindBlown", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "Mina_BiCurious":5},"While on Mina's path, cross the line."],
        [persistent.minaW3HJ, "minaW3HJ", "w3MinaStart", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"After the week 2 Exhibition, \visit Mina."],
        [persistent.w3dream, "w3dream", "w3KathleenStart", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"After the week 2 Exhibition, \visit Kathleen."],
        [persistent.w3MinaParkKiss, "w3MinaParkKiss", "w3MinaParkKiss", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "Mina_Affection":99},"After rejecting Mina's advances, change your mind."],
        [persistent.w3MinaHotelSex, "w3MinaHotelSex", "w3MinaHotel", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "feliciaSex":True, "w2HanaSex":True},"Be on Mina's Path."],
        [persistent.w3FeliciaMinaThreesome, "w3FeliciaMinaThreesome", "w3FeliciaMinaFun", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "feliciaDaddy":True},"The more the merrier."],
        [persistent.w3VeroMinaKiss, "w3VeroMinaKiss", "w3RockShowVeroMinaGetPersonal", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w3RockShowHanaPath":True},"During Hana's second rock show, push Mina toward Veronica."],
        [persistent.w3VeroMinaLez, "w3VeroMinaLez", "w3RockShowVeroMinaVIP", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w3RockShowHanaPath":True},"During Hana's second rock show, push Mina toward Veronica."],
        [persistent.w3HanaMinaLez, "w3HanaMinaLez", "w3RockShowHanaMinaParkingLot", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "Mina_BiCurious":99},"While in a relationship with Mina and Hana, go on stage..."],
        [persistent.w3RockshowMinaKiss, "w3RockshowMinaKiss", "w3RockShowMinaKiss", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w3MinaJealous":True, "w3MinaHotelFucked":True},"Out of jealousy, kiss Mina."],
        [persistent.w3MinaRoom, "w3MinaRoom", "w3PreExMinaVisit", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "perk_strongman":True},"After a heavy talk at your Mom's, go see Mina."],
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
            if i[0] or persistent.modGalleryUnlock:
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

    vbox:
        xalign 0.7
        yalign 0.975
        if persistent.modGalleryUnlock:
            textbutton "Lock Scenes":
                action SetVariable("persistent.modGalleryUnlock", False)
                text_size 40
                text_idle_color "#E19ACD"
                text_hover_color gui.hover_color
        else:
            textbutton "Unlock Scenes":
                action SetVariable("persistent.modGalleryUnlock", True)
                text_size 40
                text_idle_color "#E19ACD"
                text_hover_color gui.hover_color

        text "By DA":
            size 20
            color "#03b420"
            xalign 0.5
            ypos 5

init 100 screen replaymisc():
    modal True tag menu

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
            if i[0] or persistent.modGalleryUnlock:
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

    vbox:
        xalign 0.7
        yalign 0.975
        if persistent.modGalleryUnlock:
            textbutton "Lock Scenes":
                action SetVariable("persistent.modGalleryUnlock", False)
                text_size 40
                text_idle_color "#E19ACD"
                text_hover_color gui.hover_color
        else:
            textbutton "Unlock Scenes":
                action SetVariable("persistent.modGalleryUnlock", True)
                text_size 40
                text_idle_color "#E19ACD"
                text_hover_color gui.hover_color

        text "By DA":
            size 20
            color "#03b420"
            xalign 0.5
            ypos 5

init 100 screen replayrosalind():
    modal True tag menu

    add "screen"
    imagemap:
        idle "gui/screens/imagemaps/replay_idle.png"
        hover "gui/screens/imagemaps/replay_hover.png"
        ground "gui/screens/backgrounds/replay_rosalind.png"
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
        [persistent.RoseTAGallery, "roseTakeAdvantage", "rosetakeadvantage", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "trait_governor":True}, "Take advantage of Rosalind during the prologue to unlock."],
        [persistent.roseGonzoGallery, "roseGonzo", "w1RoseInterview", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "perk_socialChameleon":True, "perk_socialButterfly":True, "prAfterParty":True, "history_voyeur":True, "kat_polite":True}, "Interview Rosalind during Week 1."],
        [persistent.roseW1SexGallery, "roseW1Sex", "w1RoseFlag", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "trait_governor":True, "perk_socialButterfly":True, "w1RoseGonzo":True, "kat_polite":True, "roseGonzoPositions":True}, "Rosalind route: Accept her proposal."],
        [persistent.roseBodyWritingText, "roseBodyWritingText", "w1RosalindSelfies", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Having fully accepted Rosalind's terms, make her prove it."],
        [persistent.roseExhibition1Game1, "roseExhibition1Game1", "w1ExIntuitionGameRosalind", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Progress through the story."],
        [persistent.w1ExGame2VeroRoseGallery, "w1ExGame2VeroRose", "w1ExFollowThroughVeroRose", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Felicia won week 1, game 1."],
        [persistent.w1ExGame2RoseFelGallery, "w1ExGame2RoseFel", "w1ExFollowThroughRoseFel", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Veronica won week 1, game 1."],
        [persistent.w1ExGame3RoseGallery, "w1ExGame3Rose", "w1ExEarningsGameRosalind", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True}, "Rosalind lost some variation of week 1, game 2."],
        [persistent.w2ShamePhotoshootGallery, "w2ShamePhotoshoot", "w2ShamePhotoshoot", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w1FelAss":True, "kat_polite":True, "Veronica_Horniness":99}, "Progress through the story."],
        [persistent.roseW2ParkSceneGallery, "roseW2Park", "w2RosalindParkStartForReal", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True, "roseFlag":True, "roseTAapology":True, "minaFlag":True, "roseSeduceFlag":True}, "Progress through the story."],
        [persistent.roseW2BoobjobSceneGallery, "roseW2Boobjob", "w2RosalindParkBathroom", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w1GonzoReward":True}, "Progress through the story."],
        [persistent.roseW2KitchenSceneGallery, "roseW2Kitchen", "w2RosaFlag", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2RoseGag":True, "perk_strongman":True, "trait_tireless":True}, "You and Rosalind are in a deal."],
        [persistent.hanaW2Dream, "hanaW2Dream", "w2HanaDream", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl}, "Unlocked if you accept Hana's birthday present and then choose to hold her."],
        [persistent.roseW2Spank, "roseW2Spank", "w2RoseSpank", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"Having fully embraced Rosalind's terms in week 1, push it further in week 2."],
        [persistent.roseW2Sausage, "roseW2Sausage", "w2RosalindSelfie", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"Having fully embraced Rosalind's terms in week 1, push it further in week 2."],
        [persistent.roseW2Sgrope, "roseW2grope", "w2ExRosalindMingleA", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "roseFlag": True, "Rosalind_Affection":99},"Publicly grope Rosalind during Week 2's Exhibition."],
        [persistent.roseW2Shame, "roseW2Shame", "w2ExRosalindHumiliation", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "kat_polite":True, "Killian_Bromance":99, "w2RosalindPhoto": True, "perk_socialChameleon":True},"Progress through the story."],
        [persistent.w3ShockGame, "w3ShockGame", "w3ShockGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl},"Progress through the story."],
        [persistent.w3PunishGame, "w3VeroPunish", "w3PunishGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2ExLoserVeronica": True, "w1GonzoReward":True, "w1ExIntuitionGameWinnerRose":True},"Progress through the story."],
        [persistent.w3PunishGame, "w3FelPunish", "w3PunishGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2ExLoserFelicia":True, "w1GonzoReward":True},"Progress through the story."],
        [persistent.w3PunishGame, "w3VeroFel", "w3PunishGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2ExLoserDuo":True, "w1GonzoReward":True},"Progress through the story."],
        [persistent.w3PunishGame, "w3AllPunish", "w3PunishGame", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2ExLosersAll":True, "w1GonzoReward":True},"Progress through the story."],
        [persistent.w3RoseCouchHJ, "w3RoseCouchHJ", "w3RosalindNightInLewd", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2RosalindPhoto": True},"Don't ask Veronica out."],
        [persistent.w3RoseThreesome, "w3RoseThreesome", "w3TalkingAboutCeasar", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "feliciaFlag": True, "w3AliceOffer":True},"Approach Ian to solve Rosalind's money problems."],
        [persistent.w3RosalindRomance, "w3RosalindRomance", "w3RosalindAmore", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "roseFlag":True, "Rosalind_Affection":99},"After a successful dinner with Rosalind, offer her a tender touch."],
        [persistent.w3RosalindKing, "w3RosalindKing", "w3RosalindKnowsHerPlace", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "w2RosalindPhoto":True},"After having dinner with Rosalind, capitalize on your deal."],
        [persistent.w3RosaVIPKiss, "w3RosaVIPKiss", "w3RockShowRosaVIP", {"mcf":persistent.galleryMcf, "mcl":persistent.galleryMcl, "roseFlag":True, "feliciaFlag":True, "w3RosalindRomanticSex":True},"Focus on a romanced Rosalind during the rock show."],
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
            if i[0] or persistent.modGalleryUnlock:
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

    vbox:
        xalign 0.7
        yalign 0.975
        if persistent.modGalleryUnlock:
            textbutton "Lock Scenes":
                action SetVariable("persistent.modGalleryUnlock", False)
                text_size 40
                text_idle_color "#E19ACD"
                text_hover_color gui.hover_color
        else:
            textbutton "Unlock Scenes":
                action SetVariable("persistent.modGalleryUnlock", True)
                text_size 40
                text_idle_color "#E19ACD"
                text_hover_color gui.hover_color

        text "By DA":
            size 20
            color "#03b420"
            xalign 0.5
            ypos 5

init 100 screen replayveronica():
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
            if i[0] or persistent.modGalleryUnlock:
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

    vbox:
        xalign 0.7
        yalign 0.975
        if persistent.modGalleryUnlock:
            textbutton "Lock Scenes":
                action SetVariable("persistent.modGalleryUnlock", False)
                text_size 40
                text_idle_color "#E19ACD"
                text_hover_color gui.hover_color
        else:
            textbutton "Unlock Scenes":
                action SetVariable("persistent.modGalleryUnlock", True)
                text_size 40
                text_idle_color "#E19ACD"
                text_hover_color gui.hover_color

        text "By DA":
            size 20
            color "#03b420"
            xalign 0.5
            ypos 5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
