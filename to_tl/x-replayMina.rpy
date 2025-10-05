screen replaymina():
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
