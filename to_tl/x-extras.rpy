









screen leisureroom():
    modal True tag menu

    add "screen"


    imagemap:

        idle "gui/screens/imagemaps/replay_idle.png"
        hover "gui/screens/imagemaps/replay_hover.png"
        ground "gui/screens/backgrounds/replay_main.png"
        selected_idle "gui/screens/imagemaps/replay_selected_idle.png"
        selected_hover "gui/screens/imagemaps/replay_selected_hover.png"


        hotspot (105,28,300,50) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("leisureroom"), [ Play ("hover_load", "sound effects/click.wav") ]

        hotspot (70, 130, 80, 80) action [ Play ("menu_click","sound effects/page-turn.wav") ], [Return()]

        hotspot (168,142, 80, 80) action [ Play ("menu_click","sound effects/page-turn.wav") ], ui.callsinnewcontext("galleryNameChange2")

        hotspot (59,223, 300, 100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("replayrosalind") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (57, 323, 300, 100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("replaymina") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (59, 428, 300, 100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("replayhana") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (49, 518, 300, 100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("replayfelicia") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (55, 617, 300, 100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("replayveronica") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (47, 717, 300, 100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("replaykathleen") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (47, 824, 300, 100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("replaymisc") hovered [ Play ("hover_load", "sound effects/click.wav") ]

        hotspot (1572,985,300,100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("jukebox") hovered [ Play ("hover_load", "sound effects/click.wav") ]


label galleryNameChange:

    default persistent.galleryMcf = ""
    default persistent.galleryMcl = ""


    if persistent.galleryMcf == "":
        show namechange with cmet
        show screen textbox2 with dissolve
        "Please enter the name the player character will go by in the scene replay mode."
        hide screen textbox2 with dissolve
        $ persistent.galleryMcf = renpy.input("Enter the player character's given name: ")
    if persistent.galleryMcl == "":
        $ persistent.galleryMcl = renpy.input("Enter the player character's surname: ")
        show screen textbox2 with dissolve
        "You've chosen the name [persistent.galleryMcf] [persistent.galleryMcl]. Is this correct?"
        hide screen textbox2 with dissolve
        menu:
            "Yes, I'll go with [persistent.galleryMcf] [persistent.galleryMcl].":
                pass
            "No, let me rethink that.":
                $ persistent.galleryMcf = ""
                $ persistent.galleryMcl = ""
                jump galleryNameChange

    return


label galleryNameChange2:
    show namechange with cmet
    show screen textbox2 with dissolve
    "Do you want to change the name the main character will go by in the scene replay?"
    hide screen textbox2 with dissolve
    menu:
        "Yes, change the name.":
            $ persistent.galleryMcf = renpy.input("Enter the player character's given name: ")
            $ persistent.galleryMcl = renpy.input("Enter the player character's surname: ")
        "No. Keep it as [persistent.galleryMcf] [persistent.galleryMcl].":

            return




init python:

    mr = MusicRoom(fadeout=1.0)

    mr.add("music/Still_Standing.ogg")
    mr.add("music/organic.ogg")
    mr.add("music/FeelinIt.ogg")
    mr.add("music/cello-suite-No-1-G-Major-Prelude.ogg")
    mr.add("music/philly-crew.ogg")
    mr.add("music/jazz-piano-bar.ogg")
    mr.add("music/frame-of-mine.ogg")
    mr.add("music/ill-remember-you.ogg")
    mr.add("music/hold-on-a-second.ogg")
    mr.add("music/helping-hands.ogg")
    mr.add("music/as-i-figure.ogg", always_unlocked=True)
    mr.add("music/big-rock.ogg")
    mr.add("music/crinoline-dreams.ogg")
    mr.add("music/despair-and-triumph.ogg")
    mr.add("music/george-street-shuffle.ogg")
    mr.add("music/happy-boy-end-theme.ogg")
    mr.add("music/i-knew-a-guy.ogg")
    mr.add("music/leaving-home.ogg")
    mr.add("music/lobby-time.ogg")
    mr.add("music/myst-on-the-moor.ogg")
    mr.add("music/night-on-the-docks-sax.ogg")
    mr.add("music/on-the-ground.ogg")
    mr.add("music/plans-in-motion.ogg")
    mr.add("music/sonatina-in-c-minor.ogg")
    mr.add("music/study-and-relax.ogg")
    mr.add("music/take-the-lead.ogg")
    mr.add("music/there-it-is.ogg")
    mr.add("music/thief-in-the-night.ogg")
    mr.add("music/horrible.ogg")
    mr.add("music/six-days-of-heat-pt2.ogg")
    mr.add("music/Darkdub.ogg")
    mr.add("music/love-or-lust.ogg")
    mr.add("music/hotshot.ogg")
    mr.add("music/called-upon.ogg")
    mr.add("music/thief-in-the-night.ogg")
    mr.add("music/edm-detection-mode.ogg")
    mr.add("music/Moonlight-Sonata.ogg")
    mr.add("music/a-lost-map-of-a-heaven.ogg")
    mr.add("music/beginning-of-conflict.ogg")
    mr.add("music/romantic-motivation.ogg")
    mr.add("music/jack-the-lumberer.ogg")
    mr.add("music/sneaky-snitch.ogg")
    mr.add("music/ukulele-fun.ogg")
    mr.add("music/a-brand-new-start.ogg")
    mr.add("music/happy-whistling-ukulele.ogg")
    mr.add("music/guiton-sketch.ogg")
    mr.add("music/heavy-trailer-1.ogg")
    mr.add("music/rifts-for-days.ogg")
    mr.add("music/pure-energy-9.ogg")
    mr.add("music/st-francis.ogg")
    mr.add("music/jazz-apricot.ogg")
    mr.add("music/swagger.ogg")
    mr.add("music/time-piece.ogg")
    mr.add("music/hep-cats.ogg")
    mr.add("music/epic-battle-speech.ogg")
    mr.add("music/doll-dancing.ogg")
    mr.add("music/victim-to-victor.ogg")
    mr.add("music/echo-sclavi.ogg")
    mr.add("music/anacaptainslogue.ogg")
    mr.add("music/dancebroom-riddim.ogg")
    mr.add("music/no1-a-minor-waltz.ogg")
    mr.add("music/everything-you-wanted.ogg")
    mr.add("music/sugar-zone.ogg")
    mr.add("music/you-should.ogg")
    mr.add("music/higher-octane.ogg")
    mr.add("music/that-one-bar-scene.ogg")
    mr.add("music/together-with-you.ogg")
    mr.add("music/from-russia-with-love.ogg")
    mr.add("music/thunder.ogg")
    mr.add("music/inner-light.ogg")
    mr.add("music/scissor-vision.ogg")
    mr.add("music/burlesque-heartache.ogg")
    mr.add("music/dog-park.ogg")
    mr.add("music/ninja-tortoise.ogg")
    mr.add("music/hypnosis.ogg")
    mr.add("music/devious-little-smile.ogg")
    mr.add("music/modern-situations.ogg")
    mr.add("music/landing.ogg")
    mr.add("music/ob1.ogg")
    mr.add("music/the-loner.ogg")
    mr.add("music/future-rennaisance.ogg")
    mr.add("music/ode-to-joy.ogg")
    mr.add("music/impertinence.ogg")
    mr.add("music/bellissimo.ogg")
    mr.add("music/air-on-g.ogg")
    mr.add("music/wanderlust.ogg")
    mr.add("music/too-cool.ogg")
    mr.add("music/your-big-rock-concert.ogg")
    mr.add("music/unsafe-roads.ogg")
    mr.add("music/stoned.ogg")
    mr.add("music/happy-clappy.ogg")
    mr.add("music/select.ogg")
    mr.add("music/rockville.ogg")
    mr.add("music/crazy.ogg")
    mr.add("music/addict.ogg")
    mr.add("music/no7-alone-with-my-thoughts.ogg")
    mr.add("music/timeless.ogg")
    mr.add("music/ily-baby.ogg")
    mr.add("music/drop-the-tapes.ogg")
    mr.add ("music/smooth-and-cool.ogg")
    mr.add("music/blue-mood.ogg")
    mr.add("music/brooklyn-nights.ogg")
    mr.add("music/ocean-view.ogg")
    mr.add("music/drum-bass.ogg")
    mr.add("music/speak-the-truth.ogg")
    mr.add("music/georges-lament.ogg")
    mr.add("music/helium.ogg")
    mr.add("music/a-nice-dream.ogg")
    mr.add("music/ethereal-rest.ogg")
    mr.add("music/dont-fret.ogg")
    mr.add("music/the-gentleman.ogg")
    mr.add("music/mourning-dove.ogg")
    mr.add("music/i-love-my-mom.ogg")
    mr.add("music/just-stay.ogg")
    mr.add("music/with-a-rose-in-your-teeth.ogg")
    mr.add("music/campfire.ogg")
    mr.add("music/house-on-the-hill.ogg")
    mr.add("music/blacksmith.ogg")
    mr.add("music/running-it-down.ogg")
    mr.add("music/outreach.ogg")
    mr.add("music/finland.ogg")
    mr.add("music/knockout.ogg")
    mr.add("music/positioned.ogg")
    mr.add("music/young-squire.ogg")
    mr.add("music/for-time-to-disappear.ogg")
    mr.add("music/jah-jah-bangs.ogg")
    mr.add("music/no-turning-back.mp3")

screen jukebox():
    modal True tag menu

    add "screen"

    imagemap:

        idle "gui/screens/imagemaps/replay_idle.png"
        hover "gui/screens/imagemaps/replay_hover.png"
        ground "gui/screens/backgrounds/replay_jukebox.png"
        selected_idle "gui/screens/imagemaps/replay_selected_idle.png"
        selected_hover "gui/screens/imagemaps/replay_selected_hover.png"


        hotspot (73, 140, 80, 80) action [ Play ("menu_click","sound effects/page-turn.wav") ], [Return()]

        hotspot (73, 140, 80, 80) action [ Play ("menu_click","sound effects/page-turn.wav") ], [Return()]

        hotspot (168,142, 80, 80) action [ Play ("menu_click","sound effects/page-turn.wav") ], ui.callsinnewcontext("galleryNameChange2")

        hotspot (59,223, 300, 100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("replayrosalind") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (57, 323, 300, 100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("replaymina") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (59, 428, 300, 100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("replayhana") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (49, 518, 300, 100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("replayfelicia") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (55, 617, 300, 100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("replayveronica") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (47, 717, 300, 100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("replaykathleen") hovered [ Play ("hover_load", "sound effects/click.wav") ]
        hotspot (47, 824, 300, 100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("replaymisc") hovered [ Play ("hover_load", "sound effects/click.wav") ]

        hotspot (1572,985,300,100) action [ Play ("menu_click","sound effects/page-turn.wav") ], ShowMenu("jukebox") hovered [ Play ("hover_load", "sound effects/click.wav") ]

    vpgrid:
        cols 1
        spacing 10
        scrollbars "vertical"
        mousewheel True
        draggable True
        xpos 0.59
        ypos 0.12
        ymaximum 800


        vbox:

            textbutton "Just Stay - Aakash Gandhi" action mr.Play("music/just-stay.ogg")
            textbutton "Romantic Motivation by Aleksound" action mr.Play("music/romantic-motivation.ogg")
            textbutton "Jack the Lumberer - Alexander Nakarada" action mr.Play("music/jack-the-lumberer.ogg")
            textbutton "Stoned - Alexander Nakarada" action mr.Play("music/stoned.ogg")
            textbutton "Unsafe Roads - Alexander Nakarada" action mr.Play("music/unsafe-roads.ogg")
            textbutton "Drum Bass - Andrew Huang" action mr.Play("music/drum-bass.ogg")
            textbutton "Air on G - Andy LM-Leung" action mr.Play("music/air-on-g.ogg")
            textbutton "Still Standing - Anno Domini Beats" action mr.Play("music/Still_Standing.ogg")
            textbutton "Moonlight Sonata - Beethoven" action mr.Play("music/Moonlight-Sonata.ogg")
            textbutton "Organic - Beat Doctor" action mr.Play("music/organic.ogg")
            textbutton "Feelin It - Bobby Renz / Text Me Records" action mr.Play("music/FeelinIt.ogg")
            textbutton "Bach Cello Suite No. 1, G Major, Prelude - Cooper Cannel" action mr.Play("music/cello-suite-No-1-G-Major-Prelude.ogg")
            textbutton "Ode to Joy - Cooper Cannel" action mr.Play("music/ode-to-joy.ogg")
            textbutton "Philly Crew - Danny Kean / Doug Maxwell" action mr.Play("music/philly-crew.ogg")
            textbutton "Everything You Wanted - Dan Lebowitz" action mr.Play("music/everything-you-wanted.ogg")
            textbutton "Thunder - Delicate Steve" action mr.Play("music/thunder.ogg")
            textbutton "The Gentleman - DivKid" action mr.Play("music/the-gentleman.ogg")
            textbutton "The Loner - DJ Williams" action mr.Play("music/the-loner.ogg")
            textbutton "Bellissimo - Doug Maxwell" action mr.Play("music/bellissimo.ogg")
            textbutton "Jazz Piano Bar - Doug Maxwell / Media Right Productions" action mr.Play("music/jazz-piano-bar.ogg")
            textbutton "ILY Baby - Dyalla" action mr.Play("music/ily-baby.ogg")
            textbutton "No. 1 A Minor Waltz - Esther Abrami" action mr.Play("music/no1-a-minor-waltz.ogg")
            textbutton "Frame of Mine - Freedom Trial Studio" action mr.Play("music/frame-of-mine.ogg")
            textbutton "Devious Little Smile - God Mode" action mr.Play("music/devious-little-smile.ogg")
            textbutton "Alone With My Thoughts - Esther Abrami" action mr.Play("music/no7-alone-with-my-thoughts.ogg")
            textbutton "House on the Hill - Everet Almond" action mr.Play("music/house-on-the-hill.ogg")
            textbutton "Running It Down - Everet Almond" action mr.Play("music/running-it-down.ogg")
            textbutton "For Time To Disappear - Go By Ocean / Ryan McCaffrey" action mr.Play("music/for-time-to-disappear.ogg")
            textbutton "George's Lament - Go By Ocean" action mr.Play("music/georges-lament.ogg")
            textbutton "Speak the Truth - Go By Ocean" action mr.Play("music/speak-the-truth.ogg")
            textbutton "Outreach - Go By Ocean / Ryan McCaffrey" action mr.Play("music/outreach.ogg")
            textbutton "Blacksmith - God Mode" action mr.Play("music/blacksmith.ogg")
            textbutton "Future Renaissance - God Mode" action mr.Play("music/future-rennaisance.ogg")
            textbutton "Hypnosis - God Mode" action mr.Play("music/hypnosis.ogg")
            textbutton "Landing - God Mode" action mr.Play("music/landing.ogg")
            textbutton "From Russia With Love - Huma-Huma" action mr.Play("music/from-russia-with-love.ogg")
            textbutton "I'll Remember You - Jeremy Black" action mr.Play("music/ill-remember-you.ogg")
            textbutton "Wanderlust - Jim Hall" action mr.Play("music/wanderlust.ogg")
            textbutton "Impertinence - Joel Cummins" action mr.Play("music/impertinence.ogg")
            textbutton "Jazz Appricot - Joey Pecoraro" action mr.Play("music/jazz-apricot.ogg")
            textbutton "Happy Clappy - John Bartmann" action mr.Play("music/happy-clappy.ogg")
            textbutton "Hold On a Second - John Deley and the 41 Players" action mr.Play("music/hold-on-a-second.ogg")
            textbutton "St. Francis - Josh Lippi and The Overtimers" action mr.Play("music/st-francis.ogg")
            textbutton "Together With You - Jr. Tundra" action mr.Play("music/together-with-you.ogg")
            textbutton "Heling Hands - Ketsa" action mr.Play("music/helping-hands.ogg")
            textbutton "As I figure - Kevin MacLeod" action mr.Play("music/as-i-figure.ogg")
            textbutton "Big Rock - Kevin MacLeod" action mr.Play("music/big-rock.ogg")
            textbutton "Crinoline Dreams - Kevin MacLeod" action mr.Play("music/crinoline-dreams.ogg")
            textbutton "Despair and Triumph - Kevin MacLeod" action mr.Play("music/despair-and-triumph.ogg")
            textbutton "George Street Shuffle - Kevin MacLeod" action mr.Play("music/george-street-shuffle.ogg")
            textbutton "Guiton Sketch - Kevin MacLeod" action mr.Play("music/guiton-sketch.ogg")
            textbutton "Happy Boy End Theme - Kevin MacLeod" action mr.Play("music/happy-boy-end-theme.ogg")
            textbutton "Hep Cats - Kevin MacLeod" action mr.Play("music/hep-cats.ogg")
            textbutton "I Knew a Guy - Kevin MacLeod" action mr.Play("music/i-knew-a-guy.ogg")
            textbutton "Inner Light - Kevin MacLeod" action mr.Play("music/inner-light.ogg")
            textbutton "Leaving Home - Kevin MacLeod" action mr.Play("music/leaving-home.ogg")
            textbutton "Lobby Time - Kevin MacLeod" action mr.Play("music/lobby-time.ogg")
            textbutton "Myst on the Moor - Kevin MacLeod" action mr.Play("music/myst-on-the-moor.ogg")
            textbutton "Night on the Docks (Sax) - Kevin MacLeod" action mr.Play("music/night-on-the-docks-sax.ogg")
            textbutton "On the Ground - Kevin MacLeod" action mr.Play("music/on-the-ground.ogg")
            textbutton "Plans in Motion - Kevin MacLeod" action mr.Play("music/plans-in-motion.ogg")
            textbutton "Sneaky Snitch - Kevin MacLeod" action mr.Play("music/sneaky-snitch.ogg")
            textbutton "Sonatina in C-Minor - Kevin MacLeod" action mr.Play("music/sonatina-in-c-minor.ogg")
            textbutton "Study and Relax - Kevin MacLeod" action mr.Play("music/study-and-relax.ogg")
            textbutton "Take the Lead - Kevin MacLeod" action mr.Play("music/take-the-lead.ogg")
            textbutton "There It Is - Kevin MacLeod" action mr.Play("music/there-it-is.ogg")
            textbutton "Too Cool - Kevin MacLeod" action mr.Play("music/too-cool.ogg")
            textbutton "EDM Detection Mode - Kevin MacLeod" action mr.Play("music/edm-detection-mode.ogg")
            textbutton "Dancebroom Riddim - Konrad OldMoney" action mr.Play("music/dancebroom-riddim.ogg")
            textbutton "Scissor Vision - Letter Box" action mr.Play("music/scissor-vision.ogg")
            textbutton "Horrible - Mela" action mr.Play("music/horrible.ogg")
            textbutton "Echo Sclavi - The Mini Vandals" action mr.Play("music/echo-sclavi.ogg")
            textbutton "Ethereal Rest - MusicLFiles" action mr.Play("music/a-nice-dream.ogg")
            textbutton "With a Rose in Your Teeth - Nathan Moore" action mr.Play("music/with-a-rose-in-your-teeth.ogg")
            textbutton "Addict - NEFFEX" action mr.Play("music/addict.ogg")
            textbutton "No Turning Back - NEFFEX" action mr.Play("music/no-turning-back.mp3")
            textbutton "Smooth and Cool - Nico Staf" action mr.Play("music/smooth-and-cool.ogg")
            textbutton "AnaCaptainslogue - Noir Et Blanc Vie" action mr.Play("music/anacaptainslogue.ogg")
            textbutton "Six Days of Heat - Principles of Modeling" action mr.Play("music/six-days-of-heat-pt2.ogg")
            textbutton "Darkdub - Quincas Moreira" action mr.Play("music/Darkdub.ogg")
            textbutton "Don't Fret - Quincas Moreira" action mr.Play("music/dont-fret.ogg")
            textbutton "Jah Jah Bangs - Quincas Moreira" action mr.Play("music/jah-jah-bangs.ogg")
            textbutton "Love or Lust - Quincas Moreira" action mr.Play("music/love-or-lust.ogg")
            textbutton "Swagger - Quincas Moreira" action mr.Play("music/swagger.ogg")
            textbutton "Crazy - Patrick Patrikios" action mr.Play("music/crazy.ogg")
            textbutton "Rockville - Patrick Patrikios" action mr.Play("music/rockville.ogg")
            textbutton "Ocean View - Patrick Patrikios" action mr.Play("music/ocean-view.ogg")
            textbutton "Select - Patrick Patrikios" action mr.Play("music/select.ogg")
            textbutton "You Should - Patrick Patrikios" action mr.Play("music/you-should.ogg")
            textbutton "Doll Dancing - Puddle of Infinity" action mr.Play("music/doll-dancing.ogg")
            textbutton "Beginning of Conflict - Rafael Krux" action mr.Play("music/beginning-of-conflict.ogg")
            textbutton "Happy Whistling Ukulele - Rafael Krux" action mr.Play("music/happy-whistling-ukulele.ogg")
            textbutton "Ukulele Fun - Rafael Krux" action mr.Play("music/ukulele-fun.ogg")
            textbutton "OB1 - Ralph Real" action mr.Play("music/ob1.ogg")
            textbutton "I Love My Mom - Reed Mathis" action mr.Play("music/i-love-my-mom.ogg")
            textbutton "Burlesque - RKVC" action mr.Play("music/burlesque-heartache.ogg")
            textbutton "That One Bar Scene - RKVC" action mr.Play("music/that-one-bar-scene.ogg")
            textbutton "Victim to Victor - RKVC" action mr.Play("music/victim-to-victor.ogg")
            textbutton "Blue Mood - Robert Munzinger" action mr.Play("music/blue-mood.ogg")
            textbutton "Heavy Trailer 1 - Sascha Ende" action mr.Play("music/heavy-trailer-1.ogg")
            textbutton "Pure Energy 9 - Sascha Ende" action mr.Play("music/pure-energy-9.ogg")
            textbutton "Hotshot - Scott Holmes" action mr.Play("music/hotshot.ogg")
            textbutton "A Lost Map Of A Heaven - Shaoqing Li (Luna)" action mr.Play("music/a-lost-map-of-a-heaven.ogg")
            textbutton "Called Upon - Silent Partner" action mr.Play("music/called-upon.ogg")
            textbutton "Dog Park - Silent Partner" action mr.Play("music/dog-park.ogg")
            textbutton "Sugar Zone - Silent Partner" action mr.Play ("music/sugar-zone.ogg")
            textbutton "Time Piece - Silent Partner" action mr.Play ("music/time-piece.ogg")
            textbutton "Timeless - Slender Beats" action mr.Play ("music/timeless.ogg")
            textbutton "Campfire - Telecasted" action mr.Play ("music/campfire.ogg")
            textbutton "Brooklyn Nights - Tim Kulig" action mr.Play ("music/brooklyn-nights.ogg")
            textbutton "A Brand New Start - TrackTribe" action mr.Play("music/a-brand-new-start.ogg")
            textbutton "Drop the Tapes - TrackTribe" action mr.Play("music/drop-the-tapes.ogg")
            textbutton "Finland - TrackTribe" action mr.Play("music/finland.ogg")
            textbutton "Helium - TrackTribe" action mr.Play("music/helium.ogg")
            textbutton "Knockout - TrackTribe" action mr.Play("music/knockout.ogg")
            textbutton "Positioned - TrackTribe" action mr.Play("music/positioned.ogg")
            textbutton "Riffs For Days - TrackTribe" action mr.Play("music/rifts-for-days.ogg")
            textbutton "Young Squire - TrackTribe" action mr.Play("music/young-squire.ogg")
            textbutton "Modern Situation - Unicorn Heads" action mr.Play("music/modern-situations.ogg")
            textbutton "Higher Octane - Vans in Japan" action mr.Play("music/higher-octane.ogg")
            textbutton "Ninja Tortoise - Verified Picasso" action mr.Play("music/ninja-tortoise.ogg")
            textbutton "Epic Battle Speech - Wayne Jones" action mr.Play("music/epic-battle-speech.ogg")
            textbutton "Your Big Rock Concert - WinnieTheMoog" action mr.Play("music/your-big-rock-concert.ogg")
            textbutton "Mourning Dove - Zachariah Hickman" action mr.Play("music/mourning-dove.ogg")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
