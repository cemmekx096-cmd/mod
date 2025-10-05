



screen w3ExNavMenuStage1:

    imagemap:
        idle "gui/screens/imagemaps/w3ExNavMenu1_idle.png"
        hover "gui/screens/imagemaps/w3ExNavMenu1_hover.png"
        ground "gui/screens/imagemaps/w3ExNavMenu1_ground.png"

        hotspot (292,267,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w3ExHallwayStage1")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        hotspot (758,267,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w3ExCDR")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        hotspot (1223,267,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w3ExBarStage1")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        hotspot (10, 22, 180, 180) action [ Play ("menu_click","sound effects/click2.wav") ], Rollback() hovered [ Play ("hover_load", "sound effects/click.wav")]



label w3ExNavMenuStage1:
    call screen w3ExNavMenuStage1 with pixellate



screen w3ExHallwayStage1:

    imagemap:

        imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage1")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]

        idle "gui/screens/imagemaps/w3ExHallway1_idle.png"
        hover "gui/screens/imagemaps/w3ExHallway1_hover.png"
        ground "gui/screens/imagemaps/w3ExHallway1_ground.png"
        if w3ExKimberGone == False:
            hotspot (196,465,200,600) action Jump("w3ExHallwayKimberStage1")
        if w3ExHallwaySammyVinceMove == True:
            hotspot (384,370,600,700) action Jump("w3ExHallwayJustSammyVinceStage1")
        else:
            hotspot (1505,399,600,700) action Jump("w3ExHallwayRosalindFlirtStage1")
        hotspot (1090,396,400,800) action Jump("w3ExHallwayJacobStage1")


label w3ExHallwayStage1:
    show black
    $ renpy.music.play("music/cello-suite-No-1-G-Major-Prelude.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w3ExHallwayStage1 with pixellate


label w3ExHallwayKimberStage1:
    if w3ExKimberStage1Repeat == False:
        $ w3ExKimberStage1Repeat = True
        scene w3_12446 with dissolve
        mct "(Hmm...)"
        "Off and out of the way, looking impatient, was a new face."
        scene w3_12447 with dissolve
        "Quite the pretty one, actually. It did not take a detective to realize she fit the demographic of a house girl."
        "The odd thing was, despite there being club patrons about, she was casually dressed. Even stranger is that she didn't seem too concerned about either fact."
        scene w3_12446 with dissolve
        "I briefly considered introducing myself and solving the mystery, but whoever she was, she had made a point to stand far away from where anyone might naturally wander."
        mct "({b}Eh{/b}, whatever...)"
    else:
        $ randint = renpy.random.randint(1, 3)
        if randint == 1:
            scene w3_12446 with dissolve
            "Cool it, weirdo. I probably shouldn't stand around staring."
        elif randint == 2:
            scene w3_12447 with dissolve
            "Don't I have something better to do than to stare at weird woman?"
        elif randint == 3:
            scene w3_12448 with dissolve
            mct "(Come on, dude. She sees you staring.)"
            "Move along."

    jump w3ExHallwayStage1


label w3ExHallwayJacobStage1:
    if w3ExJacobStage1Repeat == False:
        $ w3ExJacobStage1Repeat = True
        scene w3_12455 with dissolve
        "Along the way, I decided to swing by and confirm what Jacob had suspected."
        scene w3_12456 with dissolve
        mc "You were right, my dude."
        scene w3_12457 with dissolve
        jacob "Haha, {i}babysitting duty.{/i}"
        scene w3_12458 with dissolve
        mc "Yeah, except I don't have to worry about anyone putting their fingers in an electrical socket."
        mc "{size=-15}{i}Just their dicks...{/i}{/size}"
        scene w3_12459 with dissolve
        jacob "I've seen someone do worse."

        if w3RosalindViolentSolution == True:
            scene w3_12455 with dissolve
            "It was weird. It wasn't lost on me that just the other night, Jacob put someone in a coma."
            scene w3_12458 with dissolve
            mc "Tell me about it."
            scene w3_12455 with dissolve
            "Yet, gabbing with him was pretty easy."
        else:
            scene w3_12458 with dissolve
            mc "Tell me about it."

        scene w3_12460 with dissolve
        jacob "Honey and bees, man."
        scene w3_12461 with dissolve
        mc "...uh, haha, what?"
        scene w3_12460 with dissolve
        jacob "Not a great substitute for a vibrator."
        scene w3_12461 with dissolve
        mc "...what the fuck?!"

        scene w3_12459 with dissolve
        jacob "A couple of stings, a swollen colon, and they got nowhere else to go."
        scene w3_12458 with dissolve
        mc "You're full of shit."
        scene w3_12457 with dissolve
        jacob "Behold, the leaders of man."
        scene w3_12456 with dissolve
        mc "Jesus... so, you know who the new member is, right?"
        scene w3_12459 with dissolve
        jacob "Of course. Heard his name on the news before, but you don't really know a man until you run a security check on him."
        scene w3_12458 with dissolve
        mc "What can't you do, Jacob?"
        scene w3_12457 with dissolve
        jacob "You should try my bucatini."

        if w3ExHallwayRosalindFlirtSeen == True:
            $ w3ExKimberGone = True
            scene w3_12462 with dissolve
            dal "{size=-25}What are you doing here?{/size}"
            "Over the sound of Samson and Vincenzo's voice, I picked out a more pleasantly familiar one."
            scene w3_12449 with dissolve
            "...Dalia?"
            "Guess she is a house girl."
            "...but Mamma Bee doesn't look too happy to see the mystery whore."
            scene w3_12450 with dissolve
            "No, she doesn't..."
            scene w3_12451 with dissolve
            mc "Who's the girl Dalia is pissed at?"
            scene w3_12463 with dissolve
            jacob "That's Kimber."
            scene w3_12456 with dissolve
            mc "Ah! Hana's troublemaker."
            scene w3_12459 with dissolve
            jacob "I don't know nothing about that, but sounds like Kimber."
            scene w3_12455 with dissolve
            "And also sounds like none of my business. Mystery solved, I can move on with my life."

            if w3ExCarnationDressingRoomVeronica == True or w3ExCarnationDressingRoomDuo == True:
                scene w3_12458 with dissolve
                mc "Well, I'm off. Gotta go find Elias. He still at the bar?"
                scene w3_12459 with dissolve
                jacob "Yep, him and that movie star."
            else:
                scene w3_12458 with dissolve
                mc "Huh, alright. Anyway, I'm off. Gonna pop in on the Carnations before I find Elias."
                scene w3_12459 with dissolve
                jacob "Alright. He and that movie star is still at the bar."

            scene w3_12458 with dissolve
            mc "Thanks, Jacob. Take it easy."
        else:

            if w3ExCarnationDressingRoomVeronica == True or w3ExCarnationDressingRoomDuo == True:
                scene w3_12456 with dissolve
                mc "Bring some next week. Anyway, I'm off. Gotta go find Elias. He still at the bar?"
                scene w3_12459 with dissolve
                jacob "Yep, him and that movie star."

            elif w3ExHallwayRosalindFlirtSeen == True:
                scene w3_12456 with dissolve
                mc "Bring some next week. Anyway, I'm off. Gonna pop in on the Carnations before I find Elias."
                scene w3_12459 with dissolve
                jacob "Him and that movie star are still at the bar."
            else:
                scene w3_12458 with dissolve
                mc "Huh, alright. Anyway, I'm off. Gonna go check in with Rosalind."
                scene w3_12457 with dissolve
                jacob "Peace, man."

            scene w3_12458 with dissolve
            mc "Take it easy."
    else:

        $ randint = renpy.random.randint(1, 3)
        scene w3_12468 with dissolve
        if randint == 1:
            "I've already prattled more than enough with Jacob. Let the man stand around like a tough guy in peace!"
        elif randint == 2:
            "Jacob's really got that standing around thing down packed."
        elif randint == 3:
            "I should find something else to do."

    jump w3ExHallwayStage1

label w3ExHallwayRosalindFlirtStage1:
    $ w3ExHallwayRosalindFlirtSeen = True
    $ w3ExHallwaySammyVinceMove = True
    scene w3_12417 with dissolve
    "Looks like Samson and the fat one caught Rosalind on her way up to the dressing room."
    scene w3_12418 with dissolve
    sam "You've seen my movies?"
    scene w3_12419 with dissolve
    rose "I, uh..."
    "Sounds like Rosalind is still a little hungover..."
    scene w3_12420 with dissolve
    rose "Of course! I love your, uh... {i}films.{/i}"
    scene w3_12421 with dissolve
    vinc "Bahaha, sounds like Andrea when she's bullshitting me about La Traviata."
    rose "No, I've seen them! I--"
    scene w3_12422 with dissolve
    vinc "Name one!"
    rose "Uh--"
    "{i}That's my cue to help Rosie save a little face.{/i}"
    scene w3_12423 with dissolve
    mc "Soldier of Misfortune, he played--"
    scene w3_12424 with dissolve
    rose "You played a former special forces soldier who gets pulled out of retirement to defeat an old enemy!"
    sam "Bahaha, she has seen it!"
    "{i}That only described about half his filmography...{/i}"
    scene w3_12425 with dissolve
    rose "How could I forget? You were {b}SO{/b} big and handsome in it."
    "Credit where credit was due, Rosalind could lay it on thick even when she felt sick. Maybe {b}too{/b} thick, but--"
    scene w3_12426 with dissolve
    "Samson either bought it or didn't mind it as part of the due course."
    sam "You like that one, eh?"
    scene w3_12427 with dissolve
    vinc "Good afternoon, [mcf]."
    mc "Hello, sir."
    scene w3_12428 with dissolve
    vinc "You're as red as ever. And Rosalind, you..."
    vinc "It's a nice change of pace to see you in regular clothes. You're very pretty, dear."
    scene w3_12429 with dissolve
    rose "Thank you, Mr.--"
    rose "Actually, I'm so sorry, I don't know your--"
    scene w3_12430 with dissolve
    vinc "Think nothing of it. I find my last name is too stuffy coming from American lips. Enzo is fine."
    scene w3_12431 with dissolve
    rose "Ah... well... I love your accent, Enzo."
    scene w3_12432 with dissolve
    vinc "It's one of my few redeeming qualities."
    scene w3_12431 with dissolve
    rose "That's not true, you're very distinguished."
    scene w3_12432 with dissolve
    vinc "That's one way of putting it, but as my ex-wife used to say, I'm built for the opera halls!"
    scene w3_12433 with dissolve
    sam "Bahaha, you fat fuck."
    vinc "{i}Stronzo!{/i} Muscles are ugly on a man your age!"
    scene w3_12434 with dissolve
    sam "Fuck you, asshole. I'm built to last."
    vinc "Yet, I outpace you every week."
    sam "We'll see about that!"
    scene w3_12435 with dissolve
    "........."
    "......"
    scene w3_12436 with dissolve
    rose "...ah, well... speaking of regular clothes... I need to go see Mrs. Pulman and then get dressed."
    scene w3_12437 with dissolve
    sam "Aw, come on... you don't want to stay with us?"
    rose "I'm sure there'll be time for that later, Mr. Garcia..."
    scene w3_12438 with dissolve
    vinc "You're already breaking the rules, Sammy."
    sam "What rule?"
    vinc "No touching the Carnations without the old woman's permission."
    sam "Mmmh, but she's not dressed yet! She's off the clock!"
    scene w3_12439 with dissolve
    mc "Think of it this way: the fun doesn't start until she's dressed for war."
    "I was largely silent up to this point, but now was my chance to politely extract Rosalind."
    scene w3_12440 with dissolve
    rose "Uh... really, if you would excuse me, I'm short on time..."
    sam "Alright, alright! Don't want that old bat angry at me!"
    scene w3_12441 with dissolve
    mc "...you have any idea what you're meeting Mrs. Pulman about?"
    scene w3_12442 with dissolve
    rose "No idea..."
    scene w3_12443 with dissolve
    "Naturally, my mind was on the impending Felicia shitstorm and how she might extend that very same energy to the other two Carnations."
    scene w3_12441 with dissolve
    mc "Go get dressed."
    scene w3_12444 with dissolve
    "Rosalind nodded, and on her way out, dropped the peppy facade and returned to the semi-nauseated one she wore before being caught off guard."

    if w3ExJacobStage1Repeat == True:
        $ w3ExKimberGone = True
        scene w3_12445 with dissolve
        dal "{size=-10}What are you doing here?{/size}"
        "As Samson and Vincenzo began another conversation, I picked out a distant but pleasantly familiar voice."
        scene w3_12449 with dissolve
        "...Dalia?"
        "Guess she is a house girl."
        "...but Mamma Bee doesn't look too happy to see the mystery whore."
        scene w3_12450 with dissolve
        "No, she doesn't..."
        scene w3_12451 with dissolve
        mc "Either of you two know who that house girl is?"
        scene w3_12452 with dissolve
        sam "Her, uh..."
        vinc "No clue. Never seen her."
        "Ah, well. That mystery continues to go unsolved."
        scene w3_12453 with dissolve
        mc "I'll see you two around tonight."
        sam "See ya, kid!"
    else:
        scene w3_12454 with dissolve
        mc "I'll see you two around tonight."
        sam "See ya, kid!"

    jump w3ExHallwayStage1

label w3ExHallwayJustSammyVinceStage1:
    if w3ExHallwayRosalindFlirtSeen == True:
        $ randint = renpy.random.randint(1, 3)
        scene w3_12464 with dissolve
        if randint == 1:
            "The two are in the midst of a rather heated conversation. I should stay out of it."
        elif randint == 2:
            "I've already said my hello to Abbott and Costello. Let's find something else to do."
        elif randint == 3:
            "No need to insert myself in the middle of that again. I should go find something else to do."
    else:

        if w3ExSammyVinceStage1Repeat == False:
            $ w3ExSammyVinceStage1Repeat = True
            scene w3_12464 with dissolve
            "On my way to see Elias, I spotted a conspicuous pair: the muscley one and the fat one."
            scene w3_12465 with dissolve
            mc "How's it going, Mr. Garcia?"
            scene w3_12466 with dissolve
            vinc "He thinks he can fuck better than me!"
            sam "Of course, I can!"
            scene w3_12467 with dissolve
            vinc "We'll see about that, old man."
            "I'll leave them alone."
        else:
            $ randint = renpy.random.randint(1, 3)
            scene w3_12464 with dissolve
            if randint == 1:
                "The two are in the midst of a rather heated conversation. I should stay out of it."
            elif randint == 2:
                "I've already said my hello to Abbot and Constello. Let's find something else to do."
            elif randint == 3:
                "No need to insert myself in the middle of that again. I should go find something else to do."

    jump w3ExHallwayStage1



screen w3ExCDR:

    imagemap:

        imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage1")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]

        idle "gui/screens/imagemaps/w3ExCDR_idle.png"
        hover "gui/screens/imagemaps/w3ExCDR_hover.png"
        ground "gui/screens/imagemaps/w3ExCDR_ground.png"
        if w3ExCarnationDressingRoomVeronica== True:
            hotspot (374,180,500,500) action Jump("w3ExCDRMenu")
        else:
            hotspot (870,263,500,500) action Jump("w3ExCDRMenu")


label w3ExCDR:
    show black
    $ renpy.music.play("music/blue-mood.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w3ExCDR with pixellate


label w3ExCDRMenu:
    if w3ExHallwayRosalindFlirtSeen == False:
        $ w3ExKimberGone = True
        $ w3ExHallwaySammyVinceMove = True

    if w3ExCarnationDressingRoomVeronica == False:
        $ w3ExCarnationDressingRoomVeronica = True
        scene w3_12500 with fade
        "When I entered, I found only one Carnation."

        if w1ExVeroRepeat == True:
            mct "(Huh, déjà vu...)"
            scene w1_2309 with pixellate
            "But, whereas last time Veronica stood tall like a goddess, peering into the mirror and obsessing over her looks, now..."
            scene w3_12469 with pixellate
            "She sat eerily still and loose, not a muscle contracting in her perfectly sculpted back and shoulders weighed down by unseen concerns."
        else:
            "The one and only fiery hair muscle mommy, sitting eerily still, not a muscle contracting in her perfectly sculpted back."
            scene w3_12469 with pixellate
            "She appeared to be thinking long and hard about something, having not heard me come in."

        scene w3_12470 with dissolve
        mc "*You know... if you stare too long in a mirror, you'll start to see things."
        scene w3_12471 with dissolve
        ver "Ah, who--!"
        scene w3_12472 with dissolve
        ver "Oh, it's you..."
        mc "Sorry to intrude."

        if veronicaFriend == True:
            scene w3_12473 with dissolve
            ver "No, uh... I'm glad it's you, [mcf]. Ummm... all this quiet comes with the bad side effect of making me think."
        else:
            scene w3_12474 with dissolve
            ver "*Sigh* No, uh it's fine. It was too quiet in here."

        scene w3_12475 with dissolve
        mc "I know what you mean. This building can be pretty eerie, can't it? Like you could get lost and die in it if you're not careful."
        scene w3_12476 with dissolve
        ver "So... what are you doing here? Perving out or something."
        scene w3_12477 with dissolve
        mc "That's just the added benefit to wanting to see if you three made it here safely."
        scene w3_12478 with dissolve
        ver "I'm afraid it's just me so far..."
        scene w3_12477 with dissolve
        mc "What were you thinking so hard about?"
        scene w3_12478 with dissolve
        ver "Just picturing all the horrible things that old bitch has in her toolbox tonight."
        scene w3_12477 with dissolve
        mc "It's better for your mental health if you {i}don't{/i} do that."
        scene w3_12479 with dissolve
        ver "Yeah... *sigh* I probably shouldn't, but..."
        ver "At least the things I can imagine feel surmountable, y'know? The most chilling things are what I {b}can't{/b} picture. It could be {i}anything.{/i}"
        scene w3_12480 with dissolve
        mc "That... that actually makes a twisted amount of sense, I suppose."
        scene w3_12481 with dissolve
        ver "Eugh! Plus, every time I've closed my eyes this week I feel those disgusting legs crawling up my back."
        scene w3_12482 with dissolve
        "A good look at Veronica's face was all I needed to understand the extent of her anxiety; she was literally pale with worry and borderline anemic-looking, but what did I expect?"
        "{i}A tree that is unbending is easily broken.{/i} It should be no surprise that she's still skittish after she broke down last week, given her personality."
        scene w3_12483 with dissolve
        mc "You've endured worse than the other two. You {i}can{i} handle whatever's thrown at you, Veronica. Imagined or otherwise."
        scene w3_12484 with dissolve
        ver "Yeah, and that's your job, right? Telling me dumb shit like that?"
        scene w3_12485 with dissolve
        "Anxiety turned into agitation, as I realized I should probably come up with something more than a trite vote of confidence."

        menu w3ExCDRVeroMenu:
            "{color=#FF1493}[[You fucked]{/color} Playfully take her mind off things."(chg=["veronica_passion_up","veronica_up2"]) if w3VeronicaSex == True:
                $ w3VeronicaGetOwned = True
                $ Veronica_Horniness += 2
                $ Veronica_Affection += 2
                scene w3_12486 with dissolve
                mc "Give me some more credit than that. We shared some real moments this week, didn't we?"
                scene w3_12487 with dissolve
                "She looked away, neither rejecting my claim nor taking ownership of it."
                scene w3_12488 with dissolve
                mc "Seriously...? Look at me!"
                scene w3_12489 with dissolve
                "........."
                "......"
                scene w3_12490 with dissolve
                ver "...what? What do you want from me?"
                scene w3_12491 with dissolve
                mc "I want you to come here."
                scene w3_12492 with dissolve
                ver "No, thanks."
                scene w3_12493 with dissolve
                "...was she pouting?"
                scene w3_12492 with dissolve
                ver "Fuck you! You and your goddamn hugs!"
                scene w3_12494 with dissolve
                mc "Pffft, hahaha...! If you don't come over here, I'll go over there!"
                scene w3_12495 with dissolve
                ver "Try it and you'll lose an arm!"
                "Feeling childish, and maybe a bit suicidal, I darted forward."
                play music "music/timeless.ogg"
                scene w3_12496 with dissolve
                ver "Aeeah--?!"
                scene w3_12497 with dissolve
                "Veronica easily shook off my grasp, but I was persistent, darting in when she stepped aside and grabbing her waist and holding onto her as if my life depended on it."
                scene w3_12498 with dissolve
                ver "What do you think you're doing, string bean? I could throw you ten yards."
                scene w3_12499 with dissolve
                mc "I'm calling your bluff about maiming me."
                scene w3_12501 with dissolve
                ver "Y-you! Let--"
                "Not being able to wiggle out of my grapple, she resorted to using her strength, gripping my forearms and trying to pull them off."
                scene w3_12502 with dissolve
                ver "Let go!"
                "However, I had {b}physics{/b} on my side, between Veronica locking her knees and a quick shift in weight--"
                scene w3_12503 with dissolve
                ver "What the--"
                play sound "sound effects/thud-floor.mp3"
                scene w3_12504 with vpunch
                "Soon I had her pinned, bearing down on her in victory."
                scene w3_12505 with dissolve
                ver "What- I mean, h-how did you do that?!"
                scene w3_12506 with dissolve
                mc "Surprised I can handle a big woman like you?"
                scene w3_12507 with dissolve
                ver "{b}That...!{/b}"
                ver "You just got lucky... I wasn't being serious."
                scene w3_12509 with dissolve
                mc "Look at me, Ronnie."
                scene w3_12510 with dissolve
                "Like a caveman dragging a woman home, being on top of the world-class athlete was igniting something primal in me."
                scene w3_12511 with dissolve
                mc "You like a man who can move your weight around, don't you?"
                scene w3_12507 with dissolve
                ver "That's chauvinistic bullshit."
                scene w3_12511 with dissolve
                mc "Sure it is, but nothing wrong with the fantasy."
                scene w3_12512 with dissolve
                mc "You're leaking."
                scene w3_12513 with dissolve
                "She didn't say anything, just looked away once more in shame."
                scene w3_12514 with dissolve
                mc "You CAN handle anything that old bitch throws at you, and I'll be right in your corner as you do."
                scene w3_12513 with dissolve
                "........."
                "......"
                scene w3_12515 with dissolve
                ver "...moron."
                scene w3_12516 with dissolve
                "To my utmost satisfaction, she moved in for a kiss, but I--"
                scene w3_12517 with dissolve
                mc "Nope!"
                ver "W-what? What do you mean no? Don't just get me worked up and leave me like this."
                scene w3_12518 with dissolve
                mc "Rosalind could be here any moment, plus it gives you something to look forward to rather than worry about."
                scene w3_12519 with dissolve
                ver "Y-you... you! You cock shit! {b}You fucker!{/b}"
                scene w3_12518 with dissolve
                mc "Mmmh, be nice to me tonight and I'll show you a good time."
                scene w3_12519 with dissolve
                ver "You mother fuck--"
                scene black with fade
                "......"
                "..."
                rose "Uh, why is Veronica so mad?"
            "Do your job and put the fire back into her. ":

                scene w3_12486 with dissolve
                mc "Yes, my job is to be in your corner. Is that so bad?"
                scene w3_12520 with dissolve
                ver "Well, you're shit at pep talks."
                scene w3_12486 with dissolve
                mc "Don't be so sure of that. Can you do something for me?"
                scene w3_12520 with dissolve
                ver "...what?"
                scene w3_12486 with dissolve
                mc "Stand up straight, stick your chest out, and put your hands behind your back."
                scene w3_12521 with dissolve
                "Veronica wasn't a complicated person. That was evidenced by her own admitted cost analysis that landed her here."
                scene w3_12522 with dissolve
                ver "What are--"
                scene w3_12524 with dissolve
                mc "Do it, {i}Miss Lynch.{/i}"
                scene w3_12521 with dissolve
                "She looked at me confused, but with my added emphasis, I think part of her understood I was getting at something."
                scene w3_12523 with dissolve
                "And so she did, putting me face-to-tit without compunction or question, and giving me more rope than I was honestly expecting. She must really be looking for something to take her mind off things."

                menu:
                    "Hit her with some tough love."(chg=["veronica_passion_up","veronica_up"]):
                        $ Veronica_Affection += 1
                        $ Veronica_Horniness += 1

                        scene w3_12525 with dissolve
                        "However, if she was looking for further explanation, she would have to wait as I was {b}purposefully{/b} preoccupied with Veronica's massive, freckled rack, flushing whatever semblance of geniality down the drain and replacing it with a thick boorishness."
                        "Making sure that, without a doubt, she could feel me peering at her as if she was a piece of meat to be fucked."
                        scene w3_12526 with dissolve
                        ver "What--"
                        scene w3_12527 with dissolve
                        mc "Don't say anything, {b}cunt.{/b}"
                        scene w3_12528 with dissolve
                        "She looked at me with further confusion, justifiably so, as if I had suddenly become a different person."
                        scene w3_12529 with dissolve
                        ver "You...!"
                        scene w3_12530 with dissolve
                        mc "I said shut the fuck up!"
                        play sound "sound effects/spit2.wav"
                        scene w3_12531 with dissolve
                        ver "{b}--?!{/b}"
                        scene w3_12532 with dissolve
                        "No, Veronica wasn't a complicated person. She was an athlete, and a good way of getting her head into the game was to put her right in it."
                        scene w3_12533 with dissolve
                        mc "You don't get it, do you? You don't get to whine after you took the \"good and fast\" solution to saving your shithole gym."
                        "Plus... deep down, under the guise of motivation, it was an excellent excuse to be {i}mean.{/i}"
                        scene w3_12534 with dissolve
                        ver "I, I--"
                        "So fed up with my tone, she couldn't get out the words."
                        scene w3_12535 with dissolve
                        mc "What? You're gonna win tonight by getting flustered by a little spit?"
                        scene w3_12536 with dissolve
                        ver "Who the fuck do you think you're talking to?!"
                        scene w3_12537 with dissolve
                        mc "I don't know, you tell me! Who are you?!"
                        scene w3_12538 with dissolve
                        ver "I, {i}I...{/i}"
                        scene w3_12539 with dissolve
                        "........."
                        "......"
                        scene w3_12540 with dissolve
                        ver "...keep my eyes on the prize, is that it?"
                        scene w3_12541 with dissolve
                        mc "Something like that. You're a woman of action, Veronica."
                        scene w3_12542 with dissolve
                        mc "You came here prepared, with a purpose... and if Mrs. Pulman tells you to suck every dirty cock in this building, {b}you'll do it.{/b}"
                        scene w3_12543 with dissolve
                        mc "You're not a quitter, so why think about unnecessary things?"
                        scene w3_12544 with dissolve
                        ver "God, {b}that is a fucked up pep talk...{/b}"
                        scene w3_12545 with dissolve
                        mc "Yeah, it is... but you'll make it through."
                        scene w3_12546 with dissolve
                        ver "...*sigh* Yeah, {i}thanks coach.{/i} Why not? I'll be the best whore I can be tonight."
                        scene w3_12545 with dissolve
                        mc "'atta girl."
                        scene w3_12547 with dissolve
                        ver "Asshole. You just wanted to take advantage."
                        scene w3_12548 with dissolve
                        mc "Sorry for spitting on you."
                        scene w3_12547 with dissolve
                        ver "Fuck you! No you're not, you sadistic prick."
                        scene w3_12549 with dissolve
                        rose "Uh, hey [mcf]... what's going on...?"
                        scene black with fade
                        "That was my cue to find Elias."
                    "Double down on your earlier confidence."(chg=["veronica_up"]):


                        $ Veronica_Affection += 1
                        scene w3_12486 with dissolve
                        mc "I think part of you enjoys being here."
                        scene w3_12550 with dissolve
                        ver "And what makes you say that?"
                        scene w3_12486 with dissolve
                        mc "Because I've never met someone quite like you, Veronica. I've seen you up there and I've watched you kick the hornet's nest just because you can."
                        scene w3_12551 with dissolve
                        mc "You elbowed Samson, you put that rat Isaak in his place, and you pissed off the old woman by talking about bargaining power. There are parts of this ugly event where you {b}thrive.{/b}"
                        mc "It doesn't always make sense, it's not always to your direct benefit, {b}but{/b} in the moment you perform - {i}like you always do.{/i}"
                        scene w3_12552 with dissolve
                        ver "That's bullshit?"
                        scene w3_12553 with dissolve
                        mc "Is it really? Are you telling me there's not some part of you that likes the thrill of competition?"
                        scene w3_12552 with dissolve
                        ver "This isn't a sport, [mcf]."
                        scene w3_12553 with dissolve
                        mc "So? You like to win, you have a goal, and you like to do it with flair. I haven't known you very long, but that's clear as day to me."
                        scene w3_12554 with dissolve
                        "........."
                        scene w3_12546 with dissolve
                        ver "...{b}okay{/b}, slightly better pep talk."
                        scene w3_12545 with dissolve
                        mc "Cut me some slack, I'm new at this job."
                        scene w3_12547 with dissolve
                        ver "Fuck you. Want to switch places?"
                        scene w3_12548 with dissolve
                        mc "Naaaaaah, I'm good."
                        scene w3_12555 with dissolve
                        ver "Pfft, hah, ah... {b}moron.{/b}"
                        scene w3_12549 with dissolve
                        rose "Uh, hey [mcf]... what's going on...?"
                        scene black with fade
                        "That was my cue to find Elias."


            "{color=#696969}[[You fucked]Playfully take her mind off things.{/color}" if w3VeronicaSex == False:
                jump w3ExCDRVeroMenu

        call screen w3ExCDR
    else:
        $ randint = renpy.random.randint(1, 3)
        if randint == 1:
            scene w3_12556 with dissolve
            "As fun as it is to watch the pair get dressed, Bukowski should get back to Mr. Ford. "
        elif randint == 2:
            scene w3_12557 with dissolve
            "I'm finished here. I should find Elias and get this night on the road."
        elif randint == 3:
            scene w3_12558 with dissolve
            "Well, I've checked in. I should go find Elias."

        call screen w3ExCDR



screen w3ExBarStage1:

    imagemap:

        imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage1")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        idle "gui/screens/imagemaps/w3ExBar1_idle.png"
        hover "gui/screens/imagemaps/w3ExBar1_hover.png"
        ground "gui/screens/imagemaps/w3ExBar1_ground.png"
        if w3ExBarSluttyGaggleRepeat == True:
            hotspot (1100,263,900,900) action Jump("w3ExBarGaggleOfSluts")
            hotspot (14,280,500,500) action Jump("w3ExBarHarperStage1")
            hotspot (679,250,500,500) action Jump("w3ExBarEliasStage1")
        else:
            hotspot (1100,263,900, 900) action Jump("w3ExBarGaggleOfSlutsJump")
            hotspot (14,280,500,500) action Jump("w3ExBarGaggleOfSlutsHarperJump")
            hotspot (679,250,500,500) action Jump("w3ExBarGaggleOfSlutsEliasJump")


label w3ExBarStage1:
    show black
    $ renpy.music.play("music/jazz-apricot.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w3ExBarStage1 with pixellate

label w3ExBarGaggleOfSlutsEliasJump:
    scene w3_12559 with dissolve
    "As soon as I entered, I started to make my way to Elias, but--"
    jump w3ExBarGaggleOfSluts
label w3ExBarGaggleOfSlutsHarperJump:
    scene w3_12559 with dissolve
    "As soon as you entered, it was impossible to miss the group of people surrounding Elias. Before I jumped into that, I figured I'd plan my entry point at the bar and--"
    jump w3ExBarGaggleOfSluts
label w3ExBarGaggleOfSlutsJump:
    scene w3_12559 with dissolve
    "As soon as you walked into the bar, you couldn't miss them. A horde of house girls, milling about, with yet little to do."
    "A few of them found a place next to the money, vying for attention, but the rest of them were off to the side just waiting for things to kick off."
    jump w3ExBarGaggleOfSluts

label w3ExBarGaggleOfSluts:
    if w3ExBarSluttyGaggleRepeat == False:
        $ w3ExBarSluttyGaggleRepeat = True
        scene w3_12560 with dissolve
        andrea "Bossman! Bossman, bossman, bossman!"
        "And just as soon, Andrea clocked me, brightening up the room with a boisterous greeting and briefly pulling the attention of the room."
        scene w3_12561 with dissolve
        merc "You know he's not {i}technically{/i} your boss, Andy..."
        scene w3_12562 with dissolve
        serena "There's no tangible difference, hun. You should smile and wave too."
        scene w3_12563 with dissolve

        if w2ExEmmaFavor == "fulfilled":
            emma "He's a nice guy. He helped me out last week, plus Dalia said he's alright and we should always--"
        else:
            emma "Dalia said he's alright and we should--"

        scene w3_12564 with dissolve
        nico "--{i}listen to Dalia?{/i} That's how she keeps you stupid."
        scene w3_12565 with dissolve
        "I couldn't hear what they were chirping, but two of them met me halfway."
        scene w3_12566 with dissolve
        andrea "{b}Heeeeeeeeeeeeeeeeeey!{/b} Did you get Isla those love letters?"
        scene w3_12567 with dissolve
        mc "Not yet... still waiting to hear from her."
        scene w3_12568 with dissolve
        serena "...you know Isla?"
        scene w3_12569 with dissolve
        "She looked at me with caution, betraying a level of experience and mindfulness that reminded me of Dalia."
        scene w3_12570 with dissolve
        mc "Sorry. I've seen you about, but I've never--"
        scene w3_12571 with dissolve
        serena "Serena."
        "However, whereas Dalia gave the impression of a cat ready to flee at a moment's notice, the classical beauty in front of me had a calming demeanor."
        scene w3_12572 with dissolve
        mc "{b}Nope!{/b} Never met her, but Andrea helped me try to get some junk to her."
        andrea "Don't call 'em junk! They're love letters."
        serena "...from Darius?"
        scene w3_12570 with dissolve
        mc "Yeah, he--"
        scene w3_12573 with dissolve
        serena "{i}Sorry.{/i} It's none of my business to begin with."
        scene w3_12574 with dissolve
        "Thinking better of it, the full-figured brunette quickly and suspiciously retracted her question."
        scene w3_12575 with dissolve
        mc "No, it's alright. I moved into his old place."
        scene w3_12573 with dissolve
        serena "Oh... I see..."
        scene w3_12574 with dissolve
        mct "(Suspicious indeed...)"
        scene w3_12576 with dissolve
        andrea "Rena and Isla were pretty close."
        serena "We shared some recurring bookings is all. That didn't make us sisters."
        scene w3_12577 with dissolve
        mc "What did you think about Darius?"
        scene w3_12578 with dissolve
        serena "Are you trying to trick me into saying something I shouldn't?"
        scene w3_12577 with dissolve
        mc "Just wondering what kind of shoes I'm filling."
        "{i}I had heard both good things and bad things, after all...{/i}"
        scene w3_12578 with dissolve
        serena "Darius... he was... I always thought he could use a haircut."
        scene w3_12579 with dissolve
        andrea "Pfft! What a line! Serena's got a 10-year-old kid, if that didn't tip you off."
        serena "Andrea..."
        scene w3_12580 with dissolve
        "She whispered something to the redhead that I couldn't hear."
        andrea "Ah, yeah... s-sorry."
        scene w3_12581 with dissolve
        mc "Don't mind me, I didn't hear anything."
        scene w3_12582 with dissolve
        serena "It's not a secret or anything, I just don't like bringing personal business up at work."
        scene w3_12581 with dissolve
        mc "That's alright. I'm guessing the place should fill up soon..."
        scene w3_12583 with dissolve
        serena "Yes, you can feel it in the air. The floodgates will open any moment now."
        scene w3_12584 with dissolve
        "I gave Serena an out, which she exchanged for a smile."
        scene w3_12585 with dissolve
        andrea " Heaah! Auggy says we should always look like we're doing something, but it's not like this place has trap doors for us to hide."
        scene w3_12586 with dissolve
        serena "You shouldn't use that nickname, Andrea."
        scene w3_12587 with dissolve


        if w3AndreaFoolAround == True:
            andrea "Naaaaaaah! It's cool! [mcf]'s not as stuffy as Dalia, and I'm pretty much his best girl! Ain't I, bossman?"
        else:
            andrea "Naaaah! It's cool! [mcf]'s not as stuffy as Dalia. Besides, Auggy likes it! I can tell!"

        mc "I--"
        scene w3_12586 with dissolve
        serena "It's a matter of respect, hun."
        scene w3_12587 with dissolve
        andrea "He says it makes him feel young!"
        scene w3_12588 with dissolve
        "........."
        "......"
        scene w3_12581 with dissolve
        mc "...anyway, I'll leave you girls to get back to ambushing your prey. I've got my own brand of schmoozing cut out for me."
        scene w3_12589 with dissolve
        andrea "Aaaaw, alright!"
        "Andrea looked disappointed and Serena..."
        scene black with fade
        "I think she appreciated me cutting the conversation short."
    else:

        $ randint = renpy.random.randint(1, 3)
        scene w3_12590 with dissolve
        if randint == 1:
            if w3ExCarnationDressingRoomVeronica == False:
                "I've already spoken to the girls."
                "Don't forget: I wanted to drop by the Carnation dressing room."
            else:
                "If I have nothing else to do, I should rejoin Elias."
        elif randint == 2:
            if w3ExCarnationDressingRoomVeronica == False:
                "I shouldn't bother the house girls."
                "Wasn't I going to drop by the dressing room and see the Carnations?"
            else:
                "I need to play buddy-buddy with Elias."
        elif randint == 3:
            if w3ExCarnationDressingRoomVeronica == False:
                "That's enough chit chat with the whores."
                "I wanted to check in with the Carnations. The dressing room is downstairs."
            else:
                "I can't keep putting it off forever. I should check in with Elias."

    jump w3ExBarStage1

label w3ExBarHarperStage1:

    if w3ExBarHarperStage1Repeat == False:
        $ w3ExBarHarperStage1Repeat = True
        scene w3_12591 with dissolve
        mc "You on bar duty, tonight?"
        scene w3_12592 with dissolve

        if w2ExLezSeen == True:
            harp "For the time being. It's Dalia's punishment for sneaking off with Lucy last week."
        else:
            harp "I did a bad thing last week, and no, I'm not going to tell you about it. Long story short, it's Dalia's idea of punishment."

        scene w3_12591 with dissolve
        mc "Punishment? How so? *Scoff* I'd rather serve drinks than suck some old man's dick."
        scene w3_12593 with dissolve
        harp "Pfft, ha! Don't let anyone hear you say that..."
        scene w3_12594 with dissolve

        if w2ExLezSeen == True:
            harp "...I'm not complaining about having a half night off, but she's mainly putting me here to keep my paws off of Lucy."
            scene w3_12595 with dissolve
            mc "Aren't you like number two around here? Shouldn't you know better than that?"
            scene w3_12594 with dissolve
            harp "I know you've seen her tits. It's not every month we get a whore that's in over her head without a fuckin' clue. You expect me not to eat?"
            scene w3_12595 with dissolve
            mc "You fit right in, huh?"
        else:
            harp "...I'm not complaining about having a half night off, but she's mainly putting me here to keep me away from Lucy."
            scene w3_12595 with dissolve
            mc "That part of the \"not telling about it\" thing? Why would she want to do that?"
            scene w3_12594 with dissolve
            harp "Because she likes spoiling my fun."

        scene w3_12596 with dissolve
        harp "Speaking of Lucy, keep an eye on her for me tonight, will 'ya? I've heard you're good at that sort of thing."
        scene w3_12597 with dissolve
        mc "Sure, but what are you worried about?"
        scene w3_12598 with dissolve
        harp "Nothing in particular, just want to make sure she doesn't fumble too hard, y'know? She's a fast learner, but she's not as flexible about certain things."
        scene w3_12599 with dissolve
        mc "{i}Certain{/i} things?"
        scene w3_12600 with dissolve
        harp "Sooner or later she's gonna have to fuck that Mr. Miller. There's no way around it."
        scene w3_12601 with dissolve


        if w2ExLezSeen == True:
            mc "Isaak? You want to throw your girlfriend to that rat? That's harsh."
            scene w3_12602 with dissolve
            harp "It's a harsh reality, and she's not my girlfriend. She's been seeing Mr. Waylon this week, and maybe he'll claim her tonight as well, but... she can't avoid him forever."
            scene w3_12600 with dissolve
            harp "Mr. Miller may be low on the totem pole, but he's got a position on it."
            scene w3_12601 with dissolve

        mc "She doesn't get a say in who she fucks?"
        scene w3_12602 with dissolve
        harp "Not if she wants to keep that dumbass brat of hers in school. I've got a pretty good read for her: she'll fucking spiral if this is all for naught and she stepped out on that \"perfect\" husband of hers."
        scene w3_12603 with dissolve
        mc "Damn, Harper. You almost sound like you don't like her."
        scene w3_12602 with dissolve
        harp "She's not a victim in any of this, is she? All I'm doing is acknowledging that and helping her survive and reach her goal. That's what I promised her in exchange for her wearing me like a hat."
        scene w3_12603 with dissolve
        "........."
        scene w3_12601 with dissolve
        "......"
        mc "...alright, I'll keep an eye. Not really my job and I'm not forcing her into anything, though."
        scene w3_12598 with dissolve

        if w2HarpRainCheck == True:
            harp "Thanks. I guess I'll owe you twice."
        else:
            harp "I'll owe you one."
        scene black with fade

        if w3ExCarnationDressingRoomVeronica == False:
            "I haven't checked on the Carnations yet."
        else:
            "Guess it's time for me to insert myself into the mass of people congregating around Elias."
    else:

        $ randint = renpy.random.randint(1, 2)
        scene w3_12604 with dissolve
        if randint == 1:
            if w3ExCarnationDressingRoomVeronica == False:
                "I've already chatted up Harper. I should go to the dressing rooms before I rejoin Elias."
            else:
                "I can't put off shadowing Elias. I should get over there..."
        elif randint == 2:
            if w3ExCarnationDressingRoomVeronica == False:
                "Still want to check in and see if the Carnations all got here."
            else:
                "I shouldn't waste any more time. Let's go interject with my new best friend."

    jump w3ExBarStage1



label w3ExBarEliasStage1:
    scene w3_12605 with dissolve
    $ randint = renpy.random.randint(1, 3)
    "Once I go over there, Elias and I will likely be joined at the hip for the foreseeable future."

    "Proceed?"
    menu:
        "Approach the wealthy talent agent.":
            jump w3ExBarEliasStageTransition
        "Maybe you'll wait a little longer...":
            jump w3ExBarStage1

label w3ExBarEliasStageTransition:
    scene w3_12606 with dissolve
    frank "You should speak with Kristoff."
    elias "Is he another member?"
    frank "He is indeed. I finance things through him."
    scene w3_12607 with dissolve
    elias "I don't understand. Why would you need an intermediary for a campaign donation?"
    frank "Oh, well... look me up some time. It's better if my name isn't attached to you."
    "What did he need me for? Elias had already started rubbing elbows without me."
    scene w3_12608 with dissolve
    elias "Bukowski!"
    frank "...who? The kid?"
    mc "You can call me [mcf]."
    scene w3_12609 with dissolve
    elias "{b}Fuck that,{/b} bahaha. What with the subterfuge, we have a special connection."
    "Maybe he was just in a good mood, but Elias cackled like a fool."
    scene w3_12610 with dissolve
    mc "Hello, ladies. Cassandra, right? Celine?"
    "They both acknowledged me with their eyes and smiles, but drew closer to their respective targets."
    "Allison, meanwhile, looked positively aloof. Like a fine piece of porcelain displayed on a shelf."
    scene w3_12611 with dissolve
    frank "You've got yourself quite the lap warmer, Elias."
    scene w3_12612 with dissolve
    frank "If only you could've seen her last year. Mmmh, you might not want her!"
    scene w3_12613 with dissolve
    elias "I doubt that very much - not when I suspect you and I have done nastier things."
    scene w3_12614 with dissolve
    allison "Jealous, Mr. Grenier? I thought you were gay."
    scene w3_12615 with dissolve
    frank "Huh? Why the fuck would I be here if I was gay?"
    scene w3_12614 with dissolve
    allison "Oh, sorry. I just assumed... you know, you and Mr. Jameson..."
    scene w3_12616 with dissolve
    allison "I remembered you two seemed more interested in each other than any of the Carnations."
    scene w3_12617 with dissolve
    "........."
    "......"
    scene w3_12618 with dissolve
    frank "...that's why everyone remembers you, beautiful. You leave an impression."
    scene w3_12619 with dissolve
    cass "Oh, Frankie is very straight. I can attest to that... he and Mr. Jameson often--"
    scene w3_12620 with dissolve
    frank "Not helping your repartee, sweetheart."
    scene w3_12621 with dissolve
    frank "It's good to have you here, Elias. You're gonna make quite the {i}splash{/i} tonight."
    frank "We will all have a bright future together, won't we?"
    elias "Thank you, Frank."
    scene w3_12622 with dissolve
    frank "I'm off to have a soak, come with me sweethearts."
    scene w3_12623 with dissolve
    "........."
    "......"
    scene w3_12624 with dissolve
    elias "...nice man, for a criminal."
    scene w3_12625 with dissolve
    mc "You already knew who he was?"
    scene w3_12626 with dissolve
    elias "Who do you take me for? Kathy was kind enough to tell me who my new brothers were, and very few actually needed research."
    scene w3_12625 with dissolve
    mc "...but Mr. Grenier?"
    scene w3_12626 with dissolve
    elias "Frank is ahead of the curve when it comes to international trade. The world just hasn't caught up to him yet, in many senses."
    scene w3_12625 with dissolve
    mc "It sounds like you don't need me, then."
    scene w3_12627 with dissolve
    elias "Of course I do, Bukowski! You and I are going to be friends! And I think I'm going to need them in a place like this."
    scene w3_12628 with dissolve
    mc "Uh... what makes you say that?"
    scene w3_12629 with dissolve
    "That sounded a bit {i}too{/i} astute of what was to come."
    scene w3_12630 with dissolve
    elias "Just a life lesson from my late father. If you can believe it, his best friend was the man who ran the newspaper stand outside our building."
    scene w3_12631 with dissolve
    elias "He even invited him to Christmas dinner every year for a decade. It drove my mother mad having some poor immigrant at her table, but my father could always count on Juan telling him the truth. You know why?"
    scene w3_12632 with dissolve
    mc "...because Juan was an honest man?"
    scene w3_12631 with dissolve
    elias "Who knows, there. I'm sure he lied to himself and his family, {i}for things that mattered.{/i}"
    scene w3_12632 with dissolve
    mc "Are you saying your father didn't matter to him?"
    scene w3_12630 with dissolve
    elias "I'm saying my father mattered exactly 50 cents a day to Juan, just the same as anyone else who came to read the news. That's where {i}real{/i} honesty lies, isn't it?"
    elias "When you're equal to everything else. So, have a drink with me, [mcf]. Please."
    scene w3_12628 with dissolve
    mc "You're finally dropping the Bukowski thing?"
    scene w3_12627 with dissolve
    elias "Absolutely not. You'd better get used to hearing it!"
    scene w3_12633 with dissolve
    mc "Alright, whatever. Let's get boozey and live up to my namesake."
    scene black with fade
    "So I shared a drink with Elias Ford alongside a rising A-Lister star - {i}a fact that wasn't lost on me.{/i}"
    play sound "sound effects/ice-glass.wav"
    scene w3_12634 with fade
    mc "...you casted {i}Ignition Point?{/i}"
    scene w3_12635 with dissolve
    elias "God, and what a turkey of a movie."
    "--and no, he wasn't the pontificating dunce I remembered."
    scene w3_12636 with dissolve
    mc "Yeah, but tricking the villain into microwaving a grenade, that was--"
    elias "It sucked, Bukowski. End of story."
    scene w3_12637 with dissolve
    mc "Yeah... {i}it sucked.{/i}"
    "I could actually see how he and Felicia might have once got on together."
    scene w3_12638 with dissolve
    harp "You guys, good?"
    elias "More than good. By the way, those are some stunning tattoos. {i}Really{/i} beautiful."
    scene w3_12639 with dissolve
    harp "Thank you, Mr. Ford. Lot of time, pain, and money went into them."
    elias "You know, I've always wanted one? But--"
    scene w3_12640 with dissolve
    harp "Why don't you get one then? Mr. Byrnes owns a tattoo parlor. I'm sure he'd give you a discount."
    elias "You're joking."
    scene w3_12641 with dissolve
    harp "Nothing gets past you."
    "As we talked, the place had filled out."
    harp "What's the point of being so successful if you're not doing what you want?"
    elias "Ha! That's--"
    scene w3_12642 with dissolve
    "I took a second to scan the room. While we drank, the place had filled out."
    "The police chief and Mr. Waylon secured a corner of the room, a house girl for each, laughing and cutting up."
    "On the opposite end, Mr. Chatterjee had his usual compatriots in tow, quietly talking amongst themselves."
    scene w3_12643 with dissolve
    mct "(Aaaaaand lastly, ah shit... I don't remember his name. All that I remember is that he likes milky tits.)"
    "I'll need a little tact when I introduce Elias, although he's thankfully not such an important member..."
    scene w3_12644 with dissolve
    allison "What happened to the other guy?"
    scene w3_12645 with dissolve
    mc "What guy?"
    scene w3_12646 with dissolve
    allison "Darius."
    scene w3_12645 with dissolve
    mc "Ah, right... he looked after you, didn't he?"
    scene w3_12647 with dissolve
    "She was one of {i}his{/i} Carnations."
    scene w3_12648 with dissolve
    allison "Is that what you call fucking all three of us?"
    scene w3_12649 with dissolve
    mc "What, like outside the club?"
    scene w3_12648 with dissolve
    allison "What does where he did it matter? We were {i}sold{/i} that entire month."
    scene w3_12650 with dissolve
    mc "It's just, uh... {i}pretty unprofessional{/i} if you ask me..."
    scene w3_12651 with dissolve
    "........."
    scene w3_12652 with dissolve
    "......"
    scene w3_12653 with dissolve
    allison "...so, {i}Canvas of Stars and Dreams.{/i}"
    scene w3_12654 with dissolve
    mc "Local guerrilla filmmaking. {b}Very cool.{/b}"
    scene w3_12653 with dissolve
    allison "No one's brought that up in years, not even during press junkets. I'd prefer to keep it that way, it's embarrassing."
    scene w3_12654 with dissolve
    mc "Right, okay... won't mention it again."
    scene w3_12652 with dissolve
    "............"
    "........."
    "......"
    scene w3_12655 with dissolve
    mc "...you were awesome in it. I'll leave it at that."
    scene w3_12656 with dissolve
    "{i}She showed her tits.{/i}"
    scene w3_12657 with dissolve
    elias "So, you're going to show me around, or what?"
    scene w3_12658 with dissolve
    mc "I was just thinking about that."
    scene black with fade
    "I'll make the rounds in here before moving on to the building's amenities."
    jump w3ExBarStage2



screen w3ExBarStage2:

    imagemap:
        idle "gui/screens/imagemaps/w3ExBar2_idle.png"
        hover "gui/screens/imagemaps/w3ExBar2_hover.png"
        ground "gui/screens/imagemaps/w3ExBar2_ground.png"
        hotspot (51,443,800,800) action Jump("w3ExBarJimEric")
        hotspot (911,316,500,500) action Jump("w3ExBarMihirCompany")
        hotspot (1384,326,650,650) action Jump("w3ExBarThomas")

label w3ExBarStage2:
    show black
    $ renpy.music.play("music/devious-little-smile.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w3ExBarStage2 with pixellate

label w3ExBarThomas:
    if w3ExBarThomasRepeat == False:
        $ w3ExBarThomasRepeat = True
        $ w3ExBarProgress += 1

        if w3ExBarProgress == 1:
            "Let's start with who's closest."
        elif w3ExBarProgress == 2:
            "Next, let's move on to what's-his-name."
        else:
            "Last, let's introduce what's-his-name."

        scene w3_12659 with dissolve
        mc "Why the long face?"
        scene w3_12660 with dissolve
        harp "Yoo-ri's not here tonight."
        scene w3_12661 with dissolve
        mc "Aw, that sucks, is she--"
        scene w3_12660 with dissolve
        harp "She's in labor."
        scene w3_12661 with dissolve
        mc "Oh, wow! That's... good news?"
        scene w3_12662 with dissolve
        tom "I wanted to be there for the birth. The bitch said no, even though I offered to pay her... {i}can you believe that?{/i}"
        tom "Who does that whore think she is?"
        scene w3_12663 with dissolve
        mc "Ah, that..."
        elias "What's he talking about, Bukowski?"
        "{i}Fucking freak.{/i}"
        scene w3_12664 with dissolve
        mc "His... \"favorite\" girl is out. She's..."
        scene w3_12665 with dissolve
        tom "At least she left me some of this."
        elias "Is that...?"
        mc "Uh huh..."
        scene w3_12666 with dissolve
        elias "Ah, yeeeeah, okay, {b}ha...!{/b}"
        tom "So, you must be Elias Ford. I'm Thomas Blake-Esquire the third."
        scene w3_12667 with dissolve
        elias "Oh! I know you! Your firm represented a complaint from one of my former talents."
        tom "...did we win?"
        elias "It could've been worse. No one walked away {i}too{/i} unhappy with what was paid. Pleased to meet you."
        scene w3_12668 with dissolve
        tom "I hear you're running for mayor. {b}Good.{/b}"
        scene w3_12669 with dissolve
        tom "Cedric Goldie is a fuckwit. It's about time someone {i}real{/i} ran against him."
        scene w3_12668 with dissolve
        tom "He doesn't know his asshole from the hole he uses to suck cock."
        scene w3_12670 with dissolve
        elias "The iron's hot. Scandal after scandal, it's time for a changing of the guard."
        scene w3_12669 with dissolve
        tom "Oh? Besides one of his staffers misappropriating funds, what has he done recently?"
        scene w3_12670 with dissolve
        elias "I'm told some photographs of him with some prostitutes are about to come out."
        scene w3_12668 with dissolve
        tom "The {i}gall{/i}..."
        scene w3_12670 with dissolve
        elias "My sentiments exactly. By the way, have you seen my init--"
        scene black with fade
        mct "(Ugh...)"
        "The two talked about politics for some time, while I ignored the feeling in my gut that democracy was an illusion."

        if w3ExBarProgress == 3:
            jump w3ExStage2Transition
    else:

        scene w3_12671 with dissolve
        $ randint = renpy.random.randint(1, 2)
        if randint == 1:
            "I've already introduced Thomas. Let's keep it moving."
        elif randint == 2:
            "Let's not go over there again after I finally got them to stop talking about Elias' damn city park plan."
    jump w3ExBarStage2

label w3ExBarJimEric:
    if w3ExBarJimEricRepeat == False:
        $ w3ExBarJimEricRepeat = True
        $ w3ExBarProgress += 1

        if w3ExBarProgress == 1:
            "It makes sense to start with the most powerful pair in the room."
        if w3ExBarProgress == 2:
            "Next, let's move on to our city's esteemed police chief."
        else:
            "Last, let's introduce the head cop who will serve at our future mayor's pleasure...."

        scene w3_12672 with dissolve
        mc "Mr. O'Doherety, Mr. Waylon, let me--"
        scene w3_12673 with dissolve
        jim "I was waiting for you to come over, Elias."
        scene w3_12674 with dissolve
        elias "You could've just come over to say hello."
        scene w3_12675 with dissolve
        "........."
        "......"
        scene w3_12676 with dissolve
        elias "...what's his deal?"
        eric "Don't mind Jim. The asshole's not sociable while he's still sober and full of cum."
        scene w3_12677 with dissolve
        jim "It's just I hear your welcoming party is going to be quite something. I was remembering the last time we gave a new member a proper welcome."
        "My stomach jumped at even the hint of somebody spilling the beans before it was time."
        scene w3_12678 with dissolve
        mc "Abel Van Doren?"
        scene w3_12679 with dissolve
        jim "No, not him... he got next to no fanfare..."
        scene w3_12678 with dissolve
        mc "Is that odd?"
        scene w3_12680 with dissolve
        jim "Yeah..."
        scene w3_12678 with dissolve
        mc "Who was the last one to get a \"big\" welcome?"
        scene w3_12681 with dissolve
        eric "It was me. The old woman was very {i}welcoming{/i}, but..."
        "...he only let it show for a second, but judging by his sour expression, the old woman was telling the truth about hazing new members."
        scene w3_12682 with dissolve
        eric "I hear she's outdone herself tonight."
        scene w3_12683 with dissolve
        mc "Careful, sirs... don't ruin the surprise, eh?"
        scene w3_12684 with dissolve
        "It was a weird fucking feeling, doing my job playing hall monitor and protecting a plan that I knew was a bad idea - complicit as all hell, choking on the irony that Elias was about to be made a cuckold in front of his peers."
        jim "I'm not ruining shit! I'm building anticipation!"
        scene w3_12685 with dissolve
        eric "Hello, Allison. It's hard to believe it's been a year since I last saw you in person. You've done well for yourself."
        eric "Are you seeing anyone?"
        scene w3_12686 with dissolve
        allison "No... I'm focusing on my career right now."
        scene w3_12687 with dissolve
        jim "...which one? Playing make-believe or being a prostitute?"
        allison "--!"
        scene w3_12688 with dissolve
        jim "I hear Kathy still calls on you from time to time, for the biggest spenders."
        "The odious prick smiled in a way that made my stomach churn, but more than the starlet's humiliation, I was concerned with the implication that Carnations are kept on the hook even after the exhibition is--"
        scene w3_12689 with dissolve
        elias "All I'm hearing is public service doesn't pay much."
        eric "Ha!"
        scene w3_12692 with dissolve
        jim "No, it doesn't. I'd say you'd find out about that soon enough, but lucky for you, you were born into money."
        scene w3_12691 with dissolve
        elias "I've built where I stand, you fat asshole. Just like you have."
        scene w3_12690 with dissolve
        "{i}Ah, shit.{/i} Elias sounded mad. Did I need to help course correct?"
        scene w3_12691 with dissolve
        elias "I steered the ship after my father ran us into the rocks, finding other ways to make money."
        scene w3_12690 with dissolve
        "Was that my job? Was this just banter? Should I--"
        scene w3_12692 with dissolve
        jim "Bullshit. You started pretty fuckin' high, so don't pat yourself on the back."
        scene w3_12691 with dissolve
        elias "Right back at you, you feckless thug. You're just a pig who got in best with the local government - which, by the way, {i}is{/i} an unelected position easily prone to shakeups when the regime changes?"
        scene w3_12692 with dissolve
        jim "My approval ratings are sky fuckin' high, {b}brother.{/b}"
        scene w3_12691 with dissolve
        elias "If my brother was as ugly as you, my mother would've drowned him."
        scene w3_12693 with dissolve
        "............"
        scene w3_12694 with dissolve
        "........."
        "......"
        scene w3_12695 with dissolve
        jim "...fuck, man. Alright, but I'll wait until you're elected to kiss your ass. Is that fair, your highness?"
        elias "It's all I ask, brother."
        scene w3_12696 with dissolve
        jim "Ha, I like him!"
        "{i}Oh.{/i} So that is what it was. {b}Measuring cocks.{/b}"
        eric "Bahaa! He said you were so ugly that--"
        scene w3_12697 with dissolve
        serena "I didn't want to interrupt, but Mr. Waylon shamed me."
        scene w3_12698 with dissolve
        jim "What the fuck are you talking about, bitch?"
        scene w3_12699 with dissolve
        serena "You're still sober and have a full {i}tank.{/i} I should do something about that... which would you prefer we start with?"
        scene w3_12700 with dissolve
        jim "Ohoh...you beautiful, {b}cunt.{/b}"
        scene w3_12701 with dissolve
        mc "Anyway, I see you know our police chief, but this is--"
        scene w3_12702 with dissolve
        elias "We've met a couple of times at the chamber of commerce dinner, actually. It's nice to drop the pretense, though."
        scene w3_12703 with dissolve
        mct "(...ah, what am I even here for? Surely he doesn't know everyone, right?)"
        scene w3_12704 with dissolve
        eric "How's your wife?"
        scene w3_12702 with dissolve
        elias "To be honest, I'm not thinking about her too much tonight."
        scene w3_12704 with dissolve
        eric "You certainly have a type..."
        scene black with fade
        "Okay, those introductions are out of the way."

        if w3ExBarProgress == 3:
            jump w3ExStage2Transition
    else:
        scene w3_12705 with dissolve
        $ randint = renpy.random.randint(1, 2)
        if randint == 1:
            "I should introduce Elias to other parts of the room."
        elif randint == 2:
            "There's a lot of building to cover, and those three have already measured dicks."

    jump w3ExBarStage2

label w3ExBarMihirCompany:
    if w3ExBarMihirCompany == False:
        $ w3ExBarMihirCompany = True
        $ w3ExBarProgress += 1

        if w3ExBarProgress == 1:
            "Let's start with the motley crew in the corner."
        if w3ExBarProgress == 2:
            "Next, let's move on to the mismatched group in the corner."
        else:
            "Last, let's swing by and say hello to Mihir and company...."

        scene w3_12706 with dissolve
        mc "Hello, sirs. Allow me to introduce our newest member."
        mc "Elias, this is Mihir Chatterjee - the dean of Allerton University."
        mc "Andrew Reeve, the ambassador to New Zealand, and--"
        scene w3_12707 with dissolve
        "{i}Shit.{/i}"
        mc "Isaak. He works for St. Ives Academy."
        "{i}I forgot his last name.{/i}"
        scene w3_12708 with dissolve
        isak "I'm the admissions officer..."
        scene w3_12709 with dissolve
        mc "And a very important member! He finds women for Mrs. Pulman's show."
        scene w3_12710 with dissolve
        elias "Oh, so you're a headhunter? We have that in common."
        drew "Haha, yes - {i}Isaak has a way with the ladies.{/i}"
        scene w3_12711 with dissolve
        mc "This is--"
        dal "The talk of the evening."
        scene w3_12712 with dissolve
        elias "Hello, Dalia. It's nice to see you again so soon."
        scene w3_12713 with dissolve
        mihir "It's so, so good to have you here. Are you having a good time, Mr. Ford? "
        elias "Well, the night's just begun, but it's looking promising. I've got Bukowski here and--"
        scene w3_12714 with dissolve
        elias "The most beautiful girl in the building without peer, apart from you two of course."
        scene w3_12715 with dissolve
        emma "Oh, sir... stop..."
        scene w3_12716 with dissolve
        elias "I hope we didn't interrupt your discussion."
        scene w3_12717 with dissolve
        drew "No, no... we were just talking about last night's cricket match and enjoying--"
        scene w3_12718 with dissolve
        drew "Ah, uh sorry.... no... you didn't..."
        scene w3_12719 with dissolve
        drew "No, you didn't say I could touch..."
        scene w3_12720 with dissolve
        "Elias looked at me, eyebrow raised, but now wasn't the time to explain the ambassador's proclivities."
        scene w3_12721 with dissolve
        mc "I'm giving Mr. Ford a tour of the place, and we've only just begun."
        scene w3_12722 with dissolve
        mihir "It's a veritable Shangri-La, is it not? I'd love to hear about your work sometime. It must be quite glamorous, especially compared to academia."
        scene w3_12723 with dissolve
        elias "It's a lot of stupidity, is what it is. Lotta ass kissing, placating entitled women, and--"
        scene w3_12724 with dissolve
        isak "That's every job! They worm their way into high positions and you can't say anything to them even though they're half as smart as you are."
        scene w3_12725 with dissolve
        "........."
        "......"
        scene w3_12726 with dissolve
        elias "...uh huh. You look lonely, Isaak. Haven't found a girl that suits your tastes yet?"
        isak "Um... uh..."
        scene w3_12727 with dissolve
        dal "Mr. Miller has his pick."
        isak "I have {i}someone{/i} in mind..."
        mc "Lucy?"
        scene w3_12728 with dissolve
        isak "Yes, {b}that cow...{/b}"
        scene w3_12729 with dissolve
        "The mere mention of his co-worker's name and Isaak was enspelled, an unsettling sneer stretched across his ugly face as he looked beyond our conversation."
        scene w3_12728 with dissolve
        isak "She's still acting like she's better than me at school..."
        scene w3_12730 with dissolve
        elias "...uh, okay."
        elias "It was nice meeting you three. If you'll excuse us, I still have a lot to see..."
        scene w3_12731 with dissolve
        "Thankfully, Elias saw fit to eject us from this conversation, but as everyone began saying their goodbyes, I wasn't so lucky."
        scene w3_12732 with dissolve
        isak "Retrieve her for me, [mcf]."
        scene w3_12733 with dissolve
        mc "I'm sure she'll turn up. I have my hands full with--"
        scene w3_12732 with dissolve
        isak "I wasn't asking."
        scene w3_12733 with dissolve
        mc "...{i}excuse me?{/i}"
        scene w3_12735 with dissolve
        isak "Am I wrong? It's your job to make sure the customer is happy."
        scene w3_12734 with dissolve
        "I understood what he was saying on an intellectual level, but having this balding pencil-pushing fuck pull rank on me made me want to smack him."
        scene w3_12733 with dissolve
        mc "No, you're not wrong..."
        scene w3_12737 with dissolve

        menu:
            "{b}Promise{/b} him you'll find Lucy.":
                $ w3ExIsaakPromise = True
                scene w3_12736 with dissolve
                mc "When I run into her, I'll send her your way."
                scene w3_12738 with dissolve
                isak "What if she's with someone else?"
                scene w3_12736 with dissolve
                mc "I'll work something out. I know how much you want to spend time with her."
                scene w3_12732 with dissolve
                isak "{b}Good.{/b} I'm getting fed up. All this fanfare for El--"
            "Only offer a vague assurance.":
                scene w3_12736 with dissolve
                mc "It's a big place and a big night. {i}If{/i} I see her, I'll send her your way."
                scene w3_12738 with dissolve
                isak "What if she's with someone else?"
                scene w3_12733 with dissolve
                mc "...first come, first serve?"
                scene w3_12735 with dissolve
                isak "I found her! I'm entitled to some time with--"

        scene w3_12739 with dissolve
        elias "Let's go, Bukowski."
        scene w3_12733 with dissolve
        mc "I'll do what I can, Mr. Miller."
        scene black with fade
        "{i}Dumb fuck.{/i}"

        if w3ExBarProgress == 3:
            jump w3ExStage2Transition
    else:
        scene w3_12740 with dissolve
        $ randint = renpy.random.randint(1, 2)
        if randint == 1:
            "We've already been over there."
        elif randint == 2 and w3ExBarThomasRepeat == False:
            "I still have more people to introduce Elias to."
        else:
            "I still have one more person to introduce Elias to."

    jump w3ExBarStage2


label w3ExStage2Transition:
    scene w3_12741 with dissolve
    elias "So, Bukowski, how did that go?"
    scene w3_12742 with dissolve
    mc "Everyone seemed to like you..."
    scene w3_12741 with dissolve
    elias "Is that your honest takeaway?"
    scene w3_12743 with dissolve
    mc "What do you mean? Did you get a feeling otherwise?"
    scene w3_12744 with dissolve
    elias "It's not a question if they like me or not, {i}they don't.{/i} I know they don't--"
    scene w3_12745 with dissolve
    mc "Jim seemed quite smitten with you after you held your ground."
    scene w3_12744 with dissolve
    elias "Lucky me, but I'm talking about the general vibe. {i}A cagey vibe...{/i}"
    scene w3_12745 with dissolve
    "Ah, crude... his intuition is sharp."
    scene w3_12746 with dissolve
    mc "Well, you are the new guy and this is a very insular club, right?"
    scene w3_12747 with dissolve
    elias "Right..."
    scene w3_12751 with dissolve
    mc "I haven't been here very long, but uh... you want {i}real honesty?{/i} Talking to these people is exhausting."
    scene w3_12749 with dissolve
    mc "Everyone's meaning is three layers obscured from what they say, everything is a push and pull, and most think they're the top dog."
    scene w3_12751 with dissolve
    mc "You know what I'm talking about though, it's your world..."
    scene w3_12748 with dissolve
    elias "It's not quite, not yet..."
    scene w3_12751 with dissolve
    mc "...how so? You're richer than all those guys."
    scene w3_12748 with dissolve
    elias "It's not always about money, although if you don't have it, it's a non-starter. There are, however, levels - not just for wealth, but also how you wield it."
    scene w3_12750 with dissolve
    elias "I don't bend the world like some of them do, I just play the middleman for pretty people."
    scene w3_12743 with dissolve
    mc "Maybe you're projecting...?"
    scene w3_12752 with dissolve
    elias "What do you think, beautiful?"
    scene w3_12753 with dissolve
    allison "Why are you asking me?"
    scene w3_12752 with dissolve
    elias "Because I know you know how to read the room. You're smarter than they give you credit for AND you handled those pricks looking down on you wonderfully."
    scene w3_12754 with dissolve
    "........."
    "......"
    scene w3_12755 with dissolve
    allison "...they don't respect you."
    scene w3_12754 with dissolve
    "...I wasn't really sure what my input here should be. My job was to kiss Elias' ass, but I don't think he was looking for that."
    scene w3_12756 with dissolve
    mc "She's right. They don't respect anyone that can't squash 'em."
    scene w3_12757 with dissolve
    elias "And I haven't even met the big dicks yet... oh, well. I'm used to that. Time will prove them wrong."
    scene black with fade
    elias "Let's go, Bukowski."
    "It was time to properly show him around."
    jump w3ExHallwayStage2
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
