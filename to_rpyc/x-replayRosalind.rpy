screen replayrosalind():
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
