screen replayhana():
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
