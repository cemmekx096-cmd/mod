label w3FeliciaMinaOpening:
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionfelmina01 with blinds
    $ renpy.pause(6, hard=True)
    $ date = "june15day"
    $ w3MinaOpening = True
    scene w3_1478 with sunshine
    show screen qmenu with dissolve
    "......"
    "..."
    play music "music/love-or-lust.ogg"
    scene w3_1479 with dissolve
    mina "Hnnnzzzz...! Ah..."
    fel "Mmmhh... ehh...?"
    scene w3_1480 with dissolve
    show screen textbox2 with dissolve
    mina "Huuuuhnnzzz..."
    scene w3_1481 with dissolve
    fel "Ahhhmmm... your..."
    scene w3_1482 with dissolve
    fel "Your breath stinks, kid."
    scene w3_1483 with dissolve
    mina "Yeah, you too, slut."
    scene w3_1484 with dissolve
    fel "Who is waking up in a loose woman's bed right now?"
    scene w3_1485 with dissolve
    mina "Heh! {b}Good morning--!{/b}"
    scene w3_1486 with dissolve
    mina "Unng... ah... my head..."
    scene w3_1487 with dissolve
    mina "Why are wine hangovers the worst hangovers?"
    scene w3_1488 with dissolve
    fel "You should've listened to me and gone with vodka."
    scene w3_1489 with dissolve
    mina "Thanks for watching all those awful episodes with me.... I don't think that \"research\" did me any good, though."
    scene w3_1488 with dissolve
    fel "Why not?"
    scene w3_1490 with dissolve
    mina "It's ALL blending together right now..."
    fel "You're really going to be on that hokey show, huh?"
    scene w3_1491 with dissolve
    fel "......"
    mina "..."
    scene w3_1492 with dissolve
    fel "I do remember something from last night."
    scene w3_1494 with dissolve
    mina "...what?"
    scene w3_1495 with dissolve
    fel "You revealed something preeeetty juicy."
    scene w3_1496 with dissolve
    mina "Whaaaaat...?"

    if minaCheat == True:
        scene w3_1495 with dissolve
        fel "You got [mcf] to help with your little list."
        scene w3_1497 with dissolve
        mina "Well... you know... it was pretty easy to convince him."
        scene w3_1498 with dissolve
        fel "It always is... for stuff like {i}that{/i} at least."
        fel "Just be careful, okay?"
        scene w3_1499 with dissolve
        mina "Don't worry. [mcf]'s nice."
        scene w3_1500 with dissolve
        fel "...I know you think you're keeping a casual spin on it, but he's only your second man."
        hide screen textbox2 with dissolve
        scene w3_1501 with dissolve
        mina "My \"second man\"...? Jeez! Why make it sound so biblical?"
        mina "Besides, we haven't {i}done it{/i} done it yet."
        scene w3_1502 with dissolve
        fel "So you told me, but still... {b}be careful{/b}, please? Don't get {b}too{/b} serious about him."
        fel "He may be more like Ian than you'd like."
        scene w3_1503 with dissolve
        mina "Do you know what's funny? I told [mcf] the same thing about you."
        scene w3_1504 with dissolve
        fel "Heh. You're a good girl."
        scene w3_1505 with dissolve
        mina "What about you, though? Are you two...?"
        scene w3_1506 with dissolve
        fel "Fucking for funsies? Would that make you jealous?"
        scene w3_1507 with dissolve
        mina "Hmm... honestly? Naaaaah."
        mina "If he's still holding your interest, that bodes well for my bucket list, doesn't it?"
        scene w3_1508 with dissolve
        fel "You know, Mina... you're kinda scary."
        scene w3_1509 with dissolve
        show screen textbox2 with dissolve
        mina "Seriously though. Are you two still \"fucking for funsies\"...?"

        if feliciaFlag == True and Mina_BiCurious >= 3:
            scene w3_1510 with dissolve
            fel "{b}Yeah{/b}. We're actually going to Denise's art exhibit on Wednesday."
            scene w3_1511 with dissolve
            mina "Wait, r-really?!"
            scene w3_1512 with dissolve
            fel "You said you didn't care."
            mina "I don't; I'm just surprised. Isn't that kind of public?"
            scene w3_1513 with dissolve
            fel "Not really. Not the kind of public that would get back to Elias."
            fel "...and even if it did, not like we're gonna fuck on the exhibition floor."
            scene w3_1514 with dissolve
            mina "Eh, eheh, huh... I hope you have fun. I'd..."
            mina "I'd like to see you two go at it."
            scene w3_1515 with dissolve
            fel "Is voyeurism on your list?"
            scene w3_1514 with dissolve
            mina "It's not {i}not{/i} on my list, but... *ahem* speaking from experience, [mcf]'s kinda intense, isn't he?"
            scene w3_1515 with dissolve
            fel "I... suppose? Was that your experience?"
            scene w3_1516 with dissolve
            mina "Y-yeah... he {i}manhandled me{/i}, but like... in a good way?"
            mina "I could barely think. He had me back and forth, bent this way and that way... ah, anyway..."
            scene w3_1514 with dissolve
            mina "I just think watching you two have sex... would be interesting."
            scene w3_1517 with dissolve
            fel "What? Do you want to watch us go at it Wednesday?"
            mina "Are you seriously asking?"
            fel "I {i}do{/i} like an audience."
            scene w3_1518 with dissolve
            mina "Then... yes, I would."
            scene w3_1519 with dissolve
            fel "Ha, you're so cute when you're honest!"
            fel "I'll give you a call then when we do it."
            scene w3_1526 with dissolve
            fel "...by the way, good job breaking it off cleanly with Ian."

        elif feliciaSex == True and w2FeliciaAbort == False:
            scene w3_1520 with dissolve
            fel "Eh, we had some fun a couple weeks ago, but that's fizzled out by now."
            scene w3_1511 with dissolve
            mina "How come?"
            scene w3_1510 with dissolve
            fel "He turned me down."
            scene w3_1521 with dissolve
            mina "Really? That's..."
            scene w3_1522 with dissolve
            fel "Why are you smiling?"
            mina "It's just... that's all it takes for it to be over with you, huh?"
            fel "Absolutely."
            scene w3_1526 with dissolve
            fel "...by the way, good job breaking it off cleanly with Ian."

        elif feliciaSex == True and w2FeliciaAbort == True:
            scene w3_1520 with dissolve
            fel "We fooled around the night we met, but it stopped there."
            scene w3_1511 with dissolve
            mina "Did it? How come?"
            scene w3_1510 with dissolve
            fel "He turned me down."
            scene w3_1521 with dissolve
            mina "Really? That's..."
            scene w3_1522 with dissolve
            fel "Why are you smiling?"
            mina "It's just... that's all it takes for it to be over with you, huh?"
            fel "Absolutely."
            scene w3_1526 with dissolve
            fel "...by the way, good job breaking it off cleanly with Ian."
        else:

            scene w3_1520 with dissolve
            fel "We never did anything."
            scene w3_1511 with dissolve
            mina "What, really?! I thought you did."
            mina "How come?"
            scene w3_1523 with dissolve
            fel "Well, I did make a move the night we met, but he... heh, {b}he turned me down.{/b}"
            scene w3_1524 with dissolve
            mina "Ha!"
            fel "What's so funny?"
            mina "He turned you down and not me."
            scene w3_1525 with dissolve
            fel "...you bitch. {i}Savor{/i} that feeling."
            scene w3_1526 with dissolve
            fel "...by the way, good job breaking it off cleanly with Ian."
    else:

        scene w3_1528 with dissolve
        fel "Your clumsy attempt at seduction got rejected!"
        fel "I mean... pfhha, c'mon... \"..am I really not enough, sad face\"...?"
        scene w3_1529 with dissolve
        mina "Don't be a bitch! He didn't want to two-time his friend!"
        scene w3_1530 with dissolve
        fel "Ha! Perhaps!"
        fel "It must've been a shock."
        scene w3_1531 with dissolve
        mina "I felt like an idiot. {i}He{/i} told me we were still friends!"
        mina "He would've been so lucky."
        scene w3_1532 with dissolve
        fel "Don't feel stupid. It sounded like he-- aha, I mean...!"
        fel "He's the dumb one, girl. What kind of cockless idiot turns down a hot young blonde with an extensive sexual to-do list?"
        scene w3_1533 with dissolve
        mina "*Sigh* Ha, thanks. But, he went the extra distance to make me {i}not{/i} feel stupid afterward."
        mina "Still, it sucks being rejected."
        scene w3_1526 with dissolve
        fel "Growing pains, kid. Speaking of which... good job breaking it off cleanly with Ian."

    mina "I was too slow doing it. I should've done it the moment I saw that video."
    scene w3_1527 with dissolve
    fel "All that matters is that you did it."
    scene w3_1534 with dissolve
    mina "We had this conversation last night."
    scene w3_1535 with dissolve
    fel "We had something like it, but I didn't have the benefit of saying it sober."
    scene w3_1538 with dissolve
    mina "You've been a good friend to me these past few days, Felicia."
    scene w3_1539 with dissolve
    fel "Well, you're a good kid and I don't have any friends. Got to make it count."
    scene w3_1534 with dissolve
    mina "So, you're saying you like having someone young like me who'll listen to your old butt?"
    scene w3_1539 with dissolve
    fel "I just see a lot of myself in you. Not because of similar circumstances or anything, just..."
    scene w3_1540 with dissolve
    mina "Heh. I could only hope to be half as cool as you."
    scene w3_1541 with dissolve
    fel "Ah, c'mon... I--"
    scene w3_1542 with dissolve
    mina "Hopefully, I'll have it more put together than you and not be hanging out with a dumb 19-year-old."
    scene w3_1543 with dissolve
    fel "{b}Cunt!{/b}"
    scene w3_1544 with dissolve
    mina "Do you want to get breakfast?"
    scene w3_1545 with dissolve
    fel "Sure, but it's gotta be a quick one. I've got some stuff to do today."
    scene w3_1546 with dissolve
    mina "What stuff?"
    scene w3_1547 with dissolve
    fel "A meeting to discuss the week's theme for a sex club I'm involved in."
    scene w3_1548 with dissolve
    mina "Uh... um... ahuh...?"
    fel "I'm just kidding! I've got some errands!"
    scene black with fade
    fel "Let's get breakfast."
    stop music fadeout 3.0
    "......"
    "..."
    stop music

    if w3HanaDP >=4:
        jump w3June15HanaOpening
    elif w2HanaSex == False or w3HanaDP <= 3:
        jump w3June15SoloOpening



label w3June15HanaOpening:
    if w3MinaOpening == False:
        $ date = "june15day"
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/page-turn.wav"
    scene titlecard_base with blinds
    $ renpy.pause(1.5, hard=True)
    scene titlecard_week3 with dissolve
    $ renpy.pause(3, hard=True)
    scene titlecard_week3full with dissolve
    $ renpy.pause(3, hard=True)
    show screen qmenu with dissolve
    scene black with dissolve
    "We slept hard, and we slept in late."
    "Turns out fucking until you almost pass out is a pretty good non-prescription sleep aid."
    play music "music/lobby-time.ogg"
    scene w3_1549 with goslow
    show screen textbox2 with dissolve
    "........."
    scene w3_1550 with dissolve
    show june15day with squares
    "......"
    scene w3_1549 with dissolve
    "..."
    scene w3_1551 with dissolve
    hana "Christ, I fuckin' stunk. How did you not kick my ass out of bed?"
    scene w3_1552 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "You guess you were too tired to care.(Dialouge/render changes only)":
            show screen textbox2 with dissolve
            mc "I didn't even notice. You put my ass to sleep."
            scene w3_1553 with dissolve
            hana "Heh~ yeah..."
        "It's probably because she's so cute?":
            show screen textbox2 with dissolve
            mc "You're cuter than you smelled, I guess."
            scene w3_1555 with dissolve
            hana "You guess?"
            scene w3_1554 with dissolve
            mc "Okay, you're just too cute."
            scene w3_1553 with dissolve
            hana "Thought so."
        "Tell her you like the way she smelled.":

            show screen textbox2 with dissolve
            mc "I liked the way you smelled."
            scene w3_1555 with dissolve
            hana "Eh...? {i}Really{/i}?"
            scene w3_1552 with dissolve
            mc "Yep. I {b}made{/b} you smell that way."

            if w3HanaMutual == True:
                mc "It was hot. Reminded me of how you were screaming my name last night."
            else:
                mc "It was hot. Reminded me of how I had you calling me Daddy last night."

            scene w3_1556 with dissolve
            hana "Oh, fuck off."
            scene w3_1557 with dissolve
            mc "{b}I am{/b} a god among men."
            scene w3_1558 with dissolve
            hana "Well..."
            scene w3_1559 with dissolve

            if hanaGF == True:
                hana "I don't have an issue helping my boyfriend feel like a god."
            else:
                hana "You were pretty good, but don't get a big head."

    scene w3_1560 with dissolve
    hana "By the way, you should've taken a shower with me. I would've blown you."
    scene w3_1561 with dissolve
    mc "......"
    mc "..."
    scene w3_1562 with dissolve
    mc "I'll remember that in the future."
    hana "Hehe~"
    scene w3_1563 with dissolve
    mc "Still, you otherwise would not have had this warm breakfast waiting for you. So, hurry up and get down here and eat."
    scene w3_1564 with dissolve
    hana "Since when... are you so commanding?"
    scene black with fade
    mc "What's with that look?"
    scene w3_1565 with fade
    hana "Have I mentioned to you how much I love your shoulders?"
    scene w3_1566 with dissolve
    mc "You're gonna make me blush."
    scene w3_1567 with dissolve
    hana "*Chwup* Mhh..."
    hana "Haaa... you don't mind a little morning sugar, do you?"
    scene w3_1568 with dissolve
    mc "It's a good pick me up..."
    hana "Heh, hehh...!"
    scene w3_1569 with dissolve
    hana "*Fhwup* Haaah..."
    hana "I shouldn't let your hard work go to waste by letting the food get cold."
    stop music fadeout 3.0
    scene black with fade
    "My work wasn't the only hard thing, but I was pleased to let the morning go to a place..."
    play music "music/jazz-piano-bar.ogg"
    scene w3_1570 with circlewipe
    "...more lazy, listless, and comfortable. There was the nagging feeling that I should get up and prepare for my day, but I felt tethered to Hana."
    scene w3_1571 with dissolve
    hana "Hey, look."
    "Unwanting and adverse to leaving the cozy bubble we were in."
    scene w3_1572 with dissolve
    mc "Oh...?"
    mc "That's you and Jerrica."
    scene w3_1573 with dissolve
    hana "Yep."
    scene w3_1572 with dissolve
    mc "Cynthia was right. You haven't really changed much."
    mc "Not outwardly, at least. I like the pink hair."
    scene w3_1573 with dissolve
    hana "Right? Cute as fuck."
    scene w3_1574 with dissolve
    hana "Should I give it a spin again?"
    scene w3_1575 with dissolve
    mc "You're asking if you should dye your hair...?"
    scene w3_1576 with dissolve
    mc "Hmm..."
    scene w3_1577 with dissolve
    mc "{b}Nah{/b}. Your hair's beautiful - so black that you can get lost in it."
    mc "I like you the way you are."
    scene w3_1578 with dissolve
    hana "That's that."
    scene w3_1579 with dissolve
    mc "What about me?"
    scene w3_1580 with dissolve
    hana "I don't think pink's your color."
    scene w3_1581 with dissolve
    mc "No?"
    hana "{b}No...{/b}"
    hana "W~oooow, you're blind, huh?"
    scene w3_1582 with dissolve

    if hanaGF == True:
        "In short order, it was easy to see why I was so quick to promise Hana something I shouldn't have done last night."
        scene w3_1583 with dissolve
        mc "I can make you out just fine."
        scene w3_1582 with dissolve
        "Moments like this quieted the mind. Reduced and simplified."
        scene w3_1584 with dissolve
        mc "C'mere..."
        scene w3_1585 with dissolve
        hana "Mmmh..."

        if minaCheat == True or roseFlag == True or feliciaFlag == True:
            "But {b}I did{/b} promise her something difficult."

            if minaCheat == True:
                scene w3_1847 with pixellate
                "There was Mina, who in her loneliness and anger, spilled her guts to me. I promised to help her with her list."

            if roseFlag == True:
                scene w3_1848 with pixellate
                "There was Rosalind and our deal, with all the extracurricular activities that entailed..."
                if w2RosalindPhoto == True:
                    scene w3_1849 with pixellate
                    "{b}Especially{/b} the extracurricular activities..."

            if w2FeliciaImpressed == True and  feliciaFlag == True:
                scene w3_1850 with pixellate
                "There was Felicia, exhilarating to be around."

                if feliciaSugarBaby == True:
                    "I had her art exhibition this Wednesday, plus I promised I'd try out to be her sugar baby..."
                else:
                    "I promised I'd go to that art exhibition with her this Wednesday..."

            scene w3_1586 with pixellate
            "There was no point in explaining the convoluted circumstances to Hana."
            "The choice was simple: keep my promise to Hana or don't."
        else:
            scene w3_1586 with dissolve
            "......"
            "..."

        scene w3_1587 with dissolve
        hana "...I think you should go brush your teeth?"
        scene w3_1588 with dissolve
        mc "Ha! Same to you!"
        scene w3_1589 with dissolve
        hana "I don't have a toothbrush here."
    else:

        "I should savor moments like this, I thought."
        scene w3_1584 with dissolve
        mc "C'mere..."
        scene w3_1585 with dissolve
        hana "Mmmh..."
        "Really make the most of it and count my stars at being so lucky."

        if minaCheat == True or roseFlag == True or feliciaFlag == True:
            "My life is a lot of fun right now. There was cock-starved Hana and..."

            if minaCheat == True:
                scene w3_1847 with pixellate
                "Curious and perverted Mina."

            if roseFlag == True:
                scene w3_1848 with pixellate
                "Rosalind and our deal."
                if w2RosalindPhoto == True:
                    scene w3_1849 with pixellate
                    "Of which I've well taken advantage of..."

            if w2FeliciaImpressed == True and  feliciaFlag == True:
                scene w3_1850 with pixellate
                "There was Felicia, exhilarating to be around."

                if feliciaSugarBaby == True:
                    "I had her art exhibition this Wednesday, plus I promised I'd try out to be her sugar baby..."
                else:
                    "I promised I'd go to that art exhibition with her this Wednesday..."

            scene w3_1586 with pixellate
            "......"
            "..."
            mct "(Fuck yeah! My life is dope!)"
        else:

            scene w3_1586 with dissolve
            "......"
            "..."

        scene w3_1587 with dissolve
        hana "...I think you should go brush your teeth?"
        scene w3_1588 with dissolve
        mc "Ha! Same to you!"
        scene w3_1589 with dissolve
        hana "I don't have a tooth-brush here."

    stop music fadeout 3.0
    scene black with fade
    mc "Give me back my glasses!"
    "......"
    "..."
    "Inevitably though, that tether had to be cut. Hana had to check in on her mom and answer her many questions, and me... well..."
    jump w3ThemeIntro


label w3June15SoloOpening:
    if w3MinaOpening == False:
        $ date = "june15day"

    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/page-turn.wav"
    scene titlecard_base with blinds
    $ renpy.pause(1.5, hard=True)
    scene titlecard_week3 with dissolve
    $ renpy.pause(3, hard=True)
    scene titlecard_week3full with dissolve
    $ renpy.pause(3, hard=True)
    show screen qmenu with dissolve
    scene w3_1590 with dissolve
    mc "Mmmhh..."
    scene w3_1591 with dissolve
    "I wanted to go back to sleep, but..."
    show june15day with squares

    if w2HanaSex == True and  w3HanaDP <= 3:
        mc "I didn't get any play last night with Hana, did I? But so what...?"

    play music "music/sneaky-snitch.ogg"
    scene w3_1592 with dissolve
    "Why is this thing so out of control?"
    "......"
    "..."
    "Today was Monday, which meant I had to go to the club in a few hours... I should get ready... {b}also{/b}..."
    scene w3_1593 with dissolve
    "...and it would probably be best if I wasn't {i}pent up.{/b}"
    "Never know what that old woman has in store..."
    mct "(Sorry, Ian.)"
    scene w3_1594 with pixellate
    mc "...!"
    "A tried and true favorite."
    scene w3_1595 with wipeleft
    "She hated me for no good reason... I always wanted to see what that stuck-up bitch's face would look like getting fucked in the ass."
    mct "(Gah, s-stupid cunt!)"
    scene w3_1596 with wiperight
    "In my fantasies, my desires had free rein, without consequence."
    play sound "sound effects/spurt.wav"
    with vpunch
    mc "Hnngg...!"
    scene w3_1597 with pixellate
    mc "......"
    scene w3_1598 with dissolve
    mct "(...I should go clean up.)"
    scene black with fade
    "I {i}was{/i} free to do {b}some{/b} of the things I desired..."
    scene w3_1599 with dissolve
    show screen textbox2 with dissolve
    "........."
    scene w3_1600 with dissolve
    "......"
    scene w3_1601 with dissolve
    mc "..."
    mct "(I wonder what Kathleen has in store for us today.)"
    scene w3_1602 with dissolve
    "Us...?"
    "It seemed I unconsciously included myself among the Carnations."
    scene black with fade
    "Was that good or bad?"
    stop music fadeout 3.0
    "......"
    "..."
    jump w3ThemeIntro

label w3ThemeIntro:

    "The walk to the club was dull and uneventful, my mind preoccupied with countless trivialities - just as it might for anyone else's daily commute."
    play music "music/that-one-bar-scene.ogg"
    scene w3_1603 with circlewipe
    "Once inside, I saw a pair of familiar faces and was greeted by the friendly smile of my co-worker."
    scene w3_1604 with fade
    "The mundanity of it all was striking."
    scene w3_1605 with dissolve
    "Dr. Van Doren's assistant stood at Jacob's post. My arrival had either interrupted their exchange or had tidily coincided with its conclusion."
    jacob "[mcf]!"
    scene w3_1606 with dissolve
    mc "So... I've got a question."
    scene w3_1607 with dissolve
    jacob "Do I look like a help desk to you?"
    scene w3_1608 with dissolve
    mc "I've always wondered... you're posted way up here, so what happens if someone finds a way to wander in?"
    scene w3_1610 with dissolve
    jacob "The cameras will send me an alert."
    scene w3_1608 with dissolve
    mc "Oh, yeah... that makes sense."
    scene w3_1609 with dissolve
    jacob "Doesn't ever really happen anyway. It's just floor after floor of unoccupied office space, after all."
    scene w3_1608 with dissolve
    mc "Never?"
    scene w3_1611 with dissolve
    jacob "Well, there was one time a homeless guy pried open a service door we forgot to latch in order to get out of the cold."
    scene w3_1612 with dissolve
    mc "What did you do?"
    scene w3_1611 with dissolve
    jacob "I sent him on his way with a cup of coffee. The man was just cold and this is just an empty office building, right?"
    scene w3_1608 with dissolve
    mc "Right on."

    if w2ExEmmaFavor == "fulfilled":
        scene w3_1613 with dissolve
        jacob "Actually, I'm glad to see you. I wanted to say thanks for getting Emma the night off."

        if w2ExEmmaFavorIan == True:
            scene w3_1614 with dissolve
            mc "Well, it wasn't quite a night off, but I did manage to get her away from the patrons thanks to Ian."
            mc "Hopefully, he didn't give her too hard of a time."
            scene w3_1615 with dissolve
            jacob "She's dealt with worse."

        if w2ExEmmaFavorChuck == True:
            scene w3_1614 with dissolve
            mc "It wasn't much; I just asked Dr. Chuck for a favor."
            scene w3_1615 with dissolve
            jacob "It might not feel like much, but she and I appreciated it."

        if w2ExEmmaFavorSolo == True:
            scene w3_1614 with dissolve
            mc "It wasn't quite the night off, but I managed to take her away from the patrons."
            scene w3_1615 with dissolve
            jacob "Yeah, she explained your little ruse."
            scene w3_1616 with dissolve
            mc "Plausible deniability."
            scene w3_1615 with dissolve
            jacob "Heh, for sure."

        scene w3_1617 with dissolve
        jacob "Anyway, I owe you one. If you ever need a favor, I'm your man, alright?"
        mc "Sure, I'll remember that."
        mct "(I can't imagine what kind of favor that would be, though...)"

    scene w3_1618 with dissolve
    mc "So, Mrs. Pulman in her office?"
    scene w3_1619 with dissolve
    jacob "Her words were to tell you to report to the photo studio. You know where to find it?"
    scene w3_1620 with dissolve
    mc "Yep. Well-acquainted with it."
    scene w3_1621 with dissolve
    mc "I should get down there."
    scene w3_1620 with dissolve
    mc "Oh, by the way, is Dr. Van Doren here?"
    scene w3_1619 with dissolve
    jacob "He isn't."
    scene w3_1620 with dissolve
    mc "Oh... I've never seen Sophia without him."
    scene w3_1619 with dissolve
    jacob "For the last couple of weeks, Dr. Lundgren has come alone often. Almost daily, actually."
    scene w3_1620 with dissolve
    mc "Huh? What's she doing?"
    scene w3_1622 with dissolve
    jacob "No idea. I guess she and Mrs. Pulman are friends?"
    mct "(I doubt they were social visits...)"
    scene w3_1620 with dissolve
    mc "Yeah, that must be it."
    scene w3_1615 with dissolve
    jacob "Fine-ass woman, isn't she?"
    scene w3_1623 with dissolve
    mc "She's definitely beautiful."
    scene w3_1624 with dissolve
    jacob "Nah, man. It's more than that."
    jacob "Every time she passes by, I feel like I'm a fuckin' teenager again with all the urges."
    scene w3_1623 with dissolve
    mc "Ah, yeah... {b}it's the perfume{/b}. Try not to inhale it as much when she comes around."
    scene w3_1622 with dissolve
    jacob "Perfume? Yeah, {b}right{/b}. I don't think it's that."
    scene w3_1625 with dissolve
    mc "Juuuust give standing a couple more feet apart a try, alright? {b}Trust me.{/b}"
    mc "See you around, Jacob."
    stop music fadeout 2.0
    scene black with fade
    jacob "Later man."
    scene w3_1626 with cmet
    "In the studio, I was greeted by another increasingly mundane sight. The Carnations were all here, wearing very little, but..."
    scene w3_1627 with dissolve
    "{b}Scratch that.{/b}"
    play music "music/cello-suite-No-1-G-Major-Prelude.ogg"
    scene w3_1628 with dissolve
    "The three dolled up in red leather was still a glorious sight."
    "Each woman wore a corset, intricately distinguished from your bog standard BDSM attire by a few strategically placed straps of leather that both obscured and accentuated their naughty bits."
    scene w3_1629 with dissolve
    kat "[mcf], good, you're here."
    scene w3_1630 with dissolve
    mc "I am... and here I thought I was pretty early, but the girls are already dressed."
    scene w3_1631 with dissolve
    kat "Don't they look lovely?"
    scene w3_1632 with dissolve
    "I left the question unanswered, as given the dull looks on their faces, a yes felt like it would be ostentatious."
    scene w3_1633 with dissolve
    kat "{b}You are early{/b}, dear. Things still need to be fully prepared."
    scene w3_1629 with dissolve
    kat "Warren's prepping the Obsidian Room, and we'll need to wait for Ian to start the shoot. Have you spoken to him today?"
    scene w3_1630 with dissolve
    mc "I have not. Why?"
    scene w3_1629 with dissolve
    kat "Considering his historic {i}tardiness{/i}, I tried calling him."
    scene w3_1630 with dissolve
    mc "...no luck?"
    scene w3_1634 with dissolve
    kat "You may be more fortunate."
    scene w3_1635 with dissolve

    if kat_polite == True:
        "I finally noticed the cattle prod in Mrs. Pulman's hands... a portent of what's to come, no doubt."
    else:
        "I finally noticed the cattle prod in Kathleen's hands... a portent of what's to come, no doubt."

    scene w3_1636 with dissolve
    kat "We're not supposed to start for at least another thirty minutes, but it'd be nice to know if I can count on him today."
    scene w3_1637 with dissolve
    mc "I'll give him a call."
    scene w3_1638 with dissolve
    kat "Good!"
    stop music
    play sound "sound effects/shock4.wav"
    scene w3_1639 with vpunch
    "*Crack*"
    mc "Ah-- yyhhup-!!!"

    if kat_polite == True:
        "A jolt of pain seared my core as a playful smile spread on Mrs. Pulman's face."
    else:
        "A jolt of pain seared my core as a playful smile spread on Kathleen's face."

    scene w3_1640 with dissolve
    mc "Godda-- ah, what's the big-"
    kat "How's the intensity? Do you think it needs more juice?"
    mc "Gah..."
    "In the wake of the shock, the area she prodded was left with a slowly dissipating burning sensation."
    scene w3_1641 with dissolve
    mc "Ah... ha... maybe I'm a pussy, but that fucking sucked."
    scene w3_1642 with dissolve
    kat "I do appreciate your input, dear - {i}and the cute way you yelp.{/i}"
    scene w3_1641 with dissolve
    mc "...I'll make the call now."
    scene w3_1643 with dissolve
    kat "Please do-"
    kat "Ha! Don't be so jumpy!"
    play sound "sound effects/ringing-outbound.mp3"
    scene black with fade
    "*Ring, ring...*"
    "It was rare for Ian not to pick up on the first or second ring..."
    "*Ring, ring, ring...*"
    "Maybe he's..."
    stop sound
    play sound "sound effects/phonemenu.wav"

    if ianIntrospect == True:
        scene w3_1644 with radio
        kil "Ugh... y-yo...! D-doc!"
        play music "music/hotshot-slow.ogg"
        scene w3_1645 with dissolve
        mc "You sound like shit."
        scene w3_1644 with dissolve
        kil "I... guhh... I drank way too much last night."
        scene w3_1645 with dissolve
        "Considering his tolerance... {b}that couldn't be an understatement.{/b}"
        mc "Taking the breakup that hard, eh?"
        scene w3_1644 with dissolve
        kil "{b}No...!{/b} I just got a bit carried away fucking that old hag, that's all."
        scene w3_1646 with dissolve
        alice "Ah, don't--"
        kil "Relax. He already knows."
        scene w3_1647 with dissolve
        alice "..."
        scene w3_1648 with dissolve
        kil "Say he--..."
        scene w3_1649 with dissolve
        kil "Eughh...!"
        scene w3_1650 with dissolve
        "I could hear Ian momentarily fight back a wretch from his end of the phone."
        kil "Say hello."
        alice "*Sigh*..."
        scene w3_1651 with dissolve
        alice "Hi, [mcf]."
        scene w3_1652 with dissolve
        mc "Ah..."
        "I wasn't expecting... this..."
        scene w3_1651 with dissolve
        alice "...this is awkward, huh?"
        scene w3_1652 with dissolve
        mc "Not really..."
        "That was a fucking lie."
        mc "{b}You're both adults{/b}... *Ahem*... how are you doing, Alice?"
        scene w3_1653 with dissolve
        alice "Well, I'm about to..."
        scene w3_1655 with dissolve
        kil "Alice... help me..."
        kil "...bacon-egg-cheese sandwich."
        scene w3_1654 with dissolve
        mc "He's got you nursing his hangover?"
        scene w3_1656 with dissolve
        alice "What else?"
        scene w3_1654 with dissolve
        mc "He doesn't deserve it."
        scene w3_1653 with dissolve
        alice "I'm gonna give the phone back now."
        scene w3_1657 with dissolve
        mc "Sure. Good talking, Alice..."
        scene w3_1658 with dissolve
        kil "Ughh... hey, dude..."
        scene w3_1659 with dissolve
        mc "You're fucking shameless, you know that? Taking advantage of your nanny like that."
        scene w3_1660 with dissolve
        kil "Hey...! She enjoys it! ...for some fuckin' reason."
        scene w3_1661 with dissolve
        mc "You're not coming into work, are you?"
        scene w3_1662 with dissolve
        kil "Aaaaaaaaaaaah.... {i}shiiiiiit{/i}."
        kil "Kathy's dumb photo shoots... right..."
        scene w3_1663 with dissolve
        kil "...tell her I sounded like I'm dying? Through absolutely no fault of my own? Heh...?"
        scene w3_1661 with dissolve
        mc "..."
        scene w3_1663 with dissolve
        kil "You're not mad? You can point a camera and snap a few pictures."
        scene w3_1661 with dissolve
        mc "It's not that. I'm upset I won't see my friend's smiling face today."
        scene w3_1664 with dissolve
        kil "Yeah right, jackass!"
        scene w3_1661 with dissolve
        mc "...I'll cover for you, I guess."
        scene w3_1665 with dissolve
        kil "Yeah?"
    else:

        scene w3_1666 with radio
        kil "Ughh... h-hey man..."
        play music "music/hotshot-slow.ogg"
        scene w3_1667 with dissolve
        mc "You sound fucked up."
        scene w3_1666 with dissolve
        kil "I am... drank a little too much last night."
        scene w3_1667 with dissolve
        mc "A little?"
        scene w3_1666 with dissolve
        kil "A little bit of a lot... h-heh... ugh..."
        scene w3_1667 with dissolve
        mc "Taking the break up hard, eh?"
        scene w3_1668 with dissolve
        kil "N-no... I just got carried away with... ah..."
        scene w3_1669 with dissolve
        kil "Get off my arm, will you? It's fall--"
        scene w3_1670 with dissolve
        mc "I got the picture."
        scene w3_1671 with dissolve
        kil "Yeah?"
        scene w3_1670 with dissolve
        mc "{b}Yeah{/b}. You're not coming into work today."
        "......"
        scene w3_1672 with dissolve
        "..."
        scene w3_1673 with dissolve
        kil "Aaaaaaaaaaaah.... {i}shiiiiiit{/i}."
        kil "Kathy's dumb photo shoots... right..."
        scene w3_1674 with dissolve
        kil "...tell her I sounded like I'm dying? Through absolutely no fault of my own? Heh...?"
        scene w3_1670 with dissolve
        mc "..."
        scene w3_1671 with dissolve
        kil "You're not mad, are you?"
        scene w3_1670 with dissolve
        mc "It's not that. I'm upset I won't see my friend's smiling face today."
        scene w3_1675 with dissolve
        kil "Yeah right, jackass!"
        scene w3_1670 with dissolve
        mc "...yeah, alright. I'll cover for you, I guess."
        scene w3_1671 with dissolve
        kil "You will?"

    stop music
    play sound "sound effects/record-scratch.wav"
    scene w3_1676 with dissolve
    mc "{b}Yeeeeeeep.{/b}"
    scene w3_1677 with dissolve
    "Sorry dude, the jig is already up."
    scene w3_1676 with dissolve
    mc "I'll tell her you've got the crud going around right now."
    scene w3_1677 with dissolve
    kil "Thanks, man... ugh..."
    scene w3_1676 with dissolve
    mc "Talk to you later."
    scene w3_1677 with dissolve
    kil "Ugh... think I'm actually going to pu-- bye!"
    play sound "sound effects/phonemenu.wav"
    "*Beep*"
    scene w3_1678 with dissolve
    "......"
    "..."
    play music "music/covert-affair.ogg"
    scene w3_1679 with dissolve
    mc "...uhhh, he sounded pretty sick."
    scene w3_1680 with dissolve
    kat "Was that a question mark at the end?"
    scene w3_1679 with dissolve
    mc "No...?"
    scene w3_1681 with dissolve
    kat "Well, no matter. You can fill in for his side of things."
    kat "You had ample experience last week."
    scene w3_1682 with dissolve
    mc "I'm a professional by this point."
    scene w3_1683 with dissolve
    kat "*Sigh* I SHOULD just stop relying on him altogether. It would simplify things."
    scene w3_1684 with dissolve

    if Killian_Bromance >=17:
        mc "Don't you think he adds a bit of charm to the proceedings?"
        scene w3_1683 with dissolve
        kat "The only thing that scud adds is adequately pointing a camera."
        scene w3_1685 with dissolve
        mc "He's got other redeeming qualities..."
        "You've got to say it more enthusiastically, [mcf]..."
    else:
        mc "These things happen."
        scene w3_1683 with dissolve
        kat "Too often."
        scene w3_1686 with dissolve
        "Well, whatever. Not like any of this is actual work..."


    play music "music/from-russia-with-love.ogg"
    scene w3_1687 with dissolve
    kat "We are getting started early, girls. Please try and contain your excitement."
    scene w3_1688 with dissolve
    ver "Greeeeeat."
    scene w3_1689 with dissolve
    rose "Get started on what?"
    kat "This week's promotional material."
    scene w3_1690 with dissolve
    fel "I hope it will be more fun than the previous one. Unfortunately, it was a little too much talking for my tastes."
    scene w3_1691 with dissolve
    kat "Oh, have no fear, Mrs. Ford. This is {b}hell week{/b}."
    scene w3_1692 with dissolve
    fel "......"
    scene w3_1693 with dissolve
    ver "......"
    scene w3_1694 with dissolve
    rose "..."
    scene w3_1695 with dissolve
    ver "...okay?"
    scene w3_1696 with dissolve
    kat "I know that doesn't mean much right now."
    kat "It doesn't need to. Your experiences during this exhibition will impart my meaning in a way words won't suffice."
    scene w3_1697 with dissolve
    rose "Are you trying to scare us?"
    scene w3_1698 with dissolve
    kat "Grab the camera, [mcf]."
    scene w3_1699 with dissolve
    mc "On it."
    scene w3_1700 with dissolve

    if w2ExLosersAll == True:
        kat "We will play a brief game today and then move on to you three's punishment for failing to win week 2."
    if w2ExLoserDuo == True:
        kat "We will play a brief game today, then move on to Miss Lynch and Mrs. Ford's punishment for losing week 2."
    if w2ExLoserFelicia == True:
        kat "We will play a brief game today, then move on to Mrs. Ford's punishment for losing week 2."
    if w2ExLoserVeronica == True:
        kat "We will play a brief game today, then move on to Miss Lynch's punishment for losing week 2."

    kat "Both of which will be documented for our viewers' betting pleasure. So put on your best sad, miserable faces, girls."
    scene w3_1701 with dissolve
    "..."
    scene w3_1702 with dissolve

    if kat_polite == True:
        "They looked primarily unperturbed by Mrs. Pulman's words - and in some ways, it WAS the same old same old, but..."
    else:
        "They looked primarily unperturbed by Kathleen's words - and in some ways, it WAS the same old same old, but... "
    scene w3_1703 with dissolve
    kat "Get some good shots of their costumes before we begin."
    "Something about the cruel woman's newfound brevity waved a red flag."
    scene w3_1704 with dissolve
    mc "Like last week? You want poses and...?"
    "Unusually amongst the three, only Felicia's face showed a degree of distinguishable concern."
    scene w3_1703 with dissolve
    kat "Whatever you feel is appropriate. {b}Just keep it brief.{/b}"
    scene w3_1705 with dissolve
    mc "Alright, girls. Let's, uh..."
    hide screen textbox2 with dissolve
    scene black with fade
    stop music fadeout 2.0
    "With that missive in mind, I arranged a series of group shots. Shots that would hopefully be evocative of the Carnation's personality and--"
    play sound "sound effects/camera-phone-shutter.wav"
    scene w3_1706 with flash
    "{i}I decided to take a series of group shots that were hot as hell.{/i} But, I mean, what else was there to do beyond following my boner here?"
    play sound "sound effects/camera-phone-shutter.wav"
    scene w3_1707 with flash
    "I paired each of them off in every combination."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w3_1708 with flash
    mct "({i}Put your tits in her face!{/i} ...yeah.)"
    mct "(You're a goddamn {b}genius{/b}, [mcf].)"
    play sound "sound effects/camera-phone-shutter.wav"
    scene w3_1709 with flash
    kat "That should be good enough."
    play music "music/epic-battle-speech.ogg"
    scene w3_1710 with dissolve
    kat "The real meat of it is before us."
    scene w3_1711 with dissolve
    show screen textbox2 with dissolve
    if history_voyeur == True:
        "Part of me was a little disappointed that my fun was cut short. This aspect of the job stimulated the inner voyeur in me."
        "A trait Ian and I had in common, it seems..."
    else:
        "I was getting a taste for this aspect. Part of me was a little disappointed that my fun was cut short."

    scene w3_1712 with dissolve
    kat "Oh, before we continue, I should christen this week with a more formal title."
    kat "Let's see... service... shame... {i}suffering{/i} maybe?"
    scene w3_1713 with dissolve
    mc "I think \"hell week\" alone suffices. It has... {b}impact.{/b}"
    scene w3_1714 with dissolve
    kat "You think?"
    scene w3_1715 with dissolve
    "An honest, divorced thought slipped from my tongue as easily as if I were picking a team name for trivia night."
    scene w3_1713 with dissolve
    mc "The patrons will respond to it. I'm sure of it."
    scene w3_1716 with dissolve
    kat "What do you girls think?"
    scene w3_1717 with dissolve
    "She looked at the Carnations as if awaiting their opinion on the branding."
    carnations "..."
    "Naturally, they didn't have shit to say about it."
    scene w3_1718 with dissolve
    kat "Come on, you must have an opinion."
    kat "This month is all about YOU. Take an interest."
    scene w3_1719 with dissolve
    fel "...it kinda lends a sense of anticipation, doesn't it?"
    scene w3_1720 with dissolve
    kat "It's settled, then. Welcome to {b}hell{/b} week, girls."
    play sound "sound effects/shock5.wav"
    scene w3_1721 with vpunch
    fel "G-ahh, sh--"
    scene w3_1722 with dissolve
    fel "Don't suddenly--"
    scene w3_1723 with dissolve
    kat "All three of you: {b}on your knees.{/b}"
    fel "Gah...!"
    kat "{b}Hands behind your head.{/b}"
    scene w3_1724 with dissolve
    kat "Come on now, don't dally."
    "I was starting to think this was the old woman's favorite position."
    scene w3_1725 with dissolve
    kat "Grab the video camera on the table, [mcf]. Our patrons will appreciate some sound for this following sequence."
    ver "Which is...?"

label w3ShockGame:
    if _in_replay:
        play music "music/epic-battle-speech.ogg"
        show screen textbox2 with dissolve

    scene w3_1726 with dissolve
    kat "I told you. You girls are going to play a game."
    scene w3_1727 with dissolve
    kat "Starting at the lowest setting, I will use this on you."
    fel "Ah, goddamn it..."
    scene w3_1728 with dissolve
    kat "If you find it unpleasant, you only need to say... I don't know... 'switch' and you'll earn a reprieve. I will change my target to the next person in line."
    kat "However, just so you know, if it loops back to you... I go up a setting. {b}There's five{/b}."
    scene w3_1729 with dissolve
    kat "This is only a prelude to the main event, so we needn't drag this on. The game will last only five minutes."
    kat "Try to endure instead of selfishly passing your misery onto your neighbor."
    scene w3_1764 with dissolve
    ver "What's the upside to this?"
    scene w3_1765 with dissolve
    kat "What do you mean {i}upside{/i}?"
    scene w3_1766 with dissolve
    ver "You usually attach some strings to these things. Last week, during our photoshoots, there was an advantage at stake."
    scene w3_1765 with dissolve
    kat "You're asking what makes this worth your while?"
    scene w3_1767 with dissolve
    kat "Doesn't that go without saying?"
    kat "Our \"contract\" is void if you don't perform satisfactorily."
    scene w3_1768 with dissolve
    ver "Sounds like you could pull the rug out from underneath us whenever you want."
    scene w3_1769 with dissolve
    kat "This isn't a bank. We're all in the honor system, Miss Lynch."
    scene w3_1768 with dissolve
    ver "Exactly. Just saying... it wouldn't hurt to have an immediate incentive."
    scene w3_1770 with dissolve
    kat "You ballsy bitch. You're two weeks into this thing and you're getting ideas, huh?"
    scene w3_1771 with dissolve
    ver "Maybe I just don't feel like being shocked today after that shit you pulled with the spider. Calling my dad was off limits!"
    scene w3_1772 with dissolve
    kat "Limits...? {b}Limits?!{/b}"
    scene w3_1773 with dissolve
    ver "The way I see it, you need us to put on a good show. Not nearly as much as we need you clearly, but enough that--"
    "This was the same talk she brought up during our group lunch..."
    scene w3_1774 with dissolve
    kat "*Sigh* I was hoping to have successfully taught you just how small and pathetic you really were, but now you're threatening me with an ultimatum?"
    "It didn't seem like a good idea then, and the enraged look on the boss' face didn't make it sound like a good idea now."
    scene w3_1775 with dissolve
    kat "Come to think of it, on the subject of putting on a good show, replacing you would be a good bit of drama for the halfway mark."
    kat "I can understand if you decide your business isn't worth further degrading yourself."
    scene w3_1776 with dissolve
    ver "..."
    scene w3_1777 with dissolve
    kat "In fact, it'd be the first thing you did that made me feel an ounce of respect for you."
    scene w3_1778 with dissolve
    ver "..."
    "Veronica looked to either of her compatriots for help, but to no avail."
    "All sense of leverage she thought she had was immediately uprooted when she realized neither Rosalind nor Felicia was on her side."
    scene w3_1779 with dissolve
    kat "If you want, this can all be for naught. We can split amicably, although I caution you about getting overly emotional. If need be..."
    mct "(I didn't believe that for one fucking second.)"
    scene w3_1780 with dissolve
    kat "I can {b}ruin{/b} you, Veronica."
    scene w3_1781 with dissolve
    "Now, {b}that{/b} one, I did believe."
    scene w3_1782 with dissolve
    ver "..."
    kat "Assume the position, Miss Lynch."
    scene w3_1783 with dissolve
    ver "..."
    kat "Perfect! Now--"
    scene w3_1730 with dissolve
    kat "Now that is settled... let us..."
    scene w3_1731 with dissolve
    kat "Oh, dear... I forgot."
    scene w3_1732 with dissolve
    kat "Hold that position, girls. I'll be right back."
    stop music fadeout 3.0
    scene w3_1733 with dissolve
    mc "Ah..."
    scene w3_1734 with dissolve
    fel "......"
    scene w3_1735 with dissolve
    ver "......"
    scene w3_1736 with dissolve
    rose "..."
    play music "music/too-cool.ogg"
    scene w3_1737 with dissolve
    mc "So, uh... how are you three doing? Have a nice weekend?"
    scene w3_1738 with dissolve
    ver "Oh, yeah. Real fuckin' chipper. Can't you tell?"
    rose "She said to hold the position..."
    scene w3_1739 with dissolve
    ver "Save yourself some discomfort."
    scene w3_1740 with dissolve
    fel "...*sigh* the camera is rolling."
    ver "What's your point? She isn't going any easier on us than she plans to."
    hide screen textbox2 with dissolve
    show screen camcorder
    scene w3_1741 with dissolve
    rose "Do you think this is going to hurt?"
    scene w3_1742 with dissolve
    "Felicia alone held the position."
    scene w3_1743 with dissolve
    mc "It hurts, but nothing too bad."
    scene w3_1742 with dissolve
    fel "It {b}fucking{/b} hurts."
    scene w3_1744 with dissolve
    rose "Oh..."
    hide screen camcorder
    scene w3_1745 with dissolve
    fel "Which end do you think she's going to start with?"
    scene w3_1746 with dissolve
    ver "Definitely you. You put a target on your back last week."
    scene w3_1747 with dissolve
    fel "Did I?"
    show screen camcorder
    scene w3_1748 with dissolve
    ver "Gah. I bet the bitch didn't even need to make a call. This is some mind-game shit."
    scene w3_1749 with dissolve
    rose "Maybe..."
    rose "Old people are pretty forgetful."
    scene w3_1750 with dissolve
    fel "All I'm saying is, let's play this smart, alright? This is a classic prisoner's dilemma."
    hide screen camcorder
    scene w3_1751 with dissolve
    fel "We just need to bite our tongues for 100 seconds each, spread across maybe a couple of rounds. That'd be easiest for all of us."
    scene w3_1752 with dissolve
    rose "Heh. I'll try my best."
    scene w3_1753 with dissolve
    rose "I can be skittish when it comes to..."
    fel "..."
    scene w3_1754 with dissolve
    ver "Everyone has a plan until they get punched in the mouth, Blondie."
    ver "Every week, I see smart people who lack the willpower to endure the pain of even a little exercise."
    scene w3_1755 with dissolve
    fel "What's your point, Red?"
    scene w3_1754 with dissolve
    ver "My point is planning for this dumb game is setting yourself up for disappointment when you realize you don't have what it takes to see it through."
    scene w3_1755 with dissolve
    fel "For a bitch whose job is self-improvement, you sure are fatalistic."
    scene w3_1756 with dissolve
    ver "...I'm not saying {i}I'm{/i} the one who won't be able to endure it. Myself... I'll do my best to cut you a break."
    scene w3_1757 with dissolve
    fel "...*sigh* I guess we'll see how this goes, huh?"
    scene w3_1758 with dissolve
    ver "Besides, where did the crazy bluster you had on stage go? You were acting pretty damn invincible."
    scene w3_1759 with dissolve
    fel "Well, in the moment, two dozen eyes on you can have an intoxicating effect."
    fel "It's spending the following Sunday nursing the after-effects of having a sharp triangle shoved up your cooch that has a girl angling to play the next day a little more prudently."
    scene w3_1760 with dissolve
    ver "Hmmpfh. So you CAN bleed."
    rose "That's good to know."
    scene w3_1761 with dissolve
    fel "Gah, that's not the takeaway I was looking for here."
    scene w3_1762 with dissolve
    show screen textbox2 with dissolve
    if kat_polite == True:
        "From where I stood, even if she wasn't employing one, Mrs. Pulman's mind game was a rousing success."
    else:
        "From where I stood, even if she wasn't employing one, Mrs. Kathleen's mind game was a rousing success."

    "The Carnations fell into a collective silence, their expressions more scrutable than before."
    "A few minutes passed, and then..."
    scene w3_1763 with dissolve
    kat "Alright. My apologies, now we can--"
    stop music fadeout 2.0
    scene w3_1784 with dissolve
    kat "I thought I told you bitches to hold your position?"
    hide screen textbox2 with dissolve
    play music "music/hypnosis.ogg"
    scene black with fade
    show screen camcorder
    kat "What the hell is it with people today? Can't anyone do what they're fucking told?"
    play sound "sound effects/shock4.wav"
    scene w3_1785 with pixellate
    rose "G-ggguuu That-"
    play sound "sound effects/shock5.wav"
    scene w3_1786 with vpunch
    "*Tceeeek!*"
    rose "A-aah...!"
    "The game's beginning was heralded by the oppressive sound of electricity jumping from the wand's barbs and tailing off into a short yet painfully sharp yelp."
    scene w3_1785 with dissolve
    rose "Ow, g-gah...! Tha- sthin-..."
    scene w3_1787 with dissolve
    kat "{b}Remember{/b}, you may switch whenever you please."
    rose "Hnng..."
    scene w3_1788 with dissolve
    "........."
    "......"
    "..."
    play sound "sound effects/shock5.wav"
    scene w3_1789 with vpunch
    "*Thiiick~!*"
    rose "W-whwhaaa...!"

    if kat_polite == True:
        "Mrs. Pulman seemed to be playing for keeps, determined to get the MILF to quickly swap by targeting the sensitive gap between Rosalind's ribs."
    else:
        "Kathleen seemed to be playing for keeps, determined to get the MILF to quickly swap by targeting the sensitive gap between Rosalind's ribs."

    scene w3_1790 with dissolve
    rose "Unggh... fwwh--"
    scene w3_1791 with dissolve
    rose "-wahhha...?!"
    "A shockless touch drew an anticipatory flinch from her fat-tittied target."

    if kat_polite == True:
        "The game had barely begun, and I could already see Mrs. Pulman's plan: keep an unsteady rhythm to the shocks and wield the Carnation's resulting anticipation as a weapon."
    else:
        "The game had barely begun, and I could already see Kathleen's plan: keep an unsteady rhythm to the shocks and wield the Carnation's resulting anticipation as a weapon."

    scene w3_1792 with dissolve
    kat "No...?"
    "As visual punctuation for the camera's benefit, she toyed and physically prodded Rosalind's breast, letting the anticipation grow thick before--"
    play sound "sound effects/shock4.wav"
    scene w3_1793 with vpunch
    rose "G-eehh, s-switch...!"
    "Attacking a different target altogether."
    scene w3_1794 with dissolve
    fel "Ah, crap... already?!"
    rose "W-wait, I mean..."
    "Rather than being at her limit, it seemed Rosalind had blurted the words out of surprise, but it was too late. She had already passed the buck."
    scene w3_1795 with dissolve
    kat "Looks like it's your turn, Miss Lynch."
    scene w3_1796 with dissolve
    kat "Mmmh... hmm~ hmm~ hmm~ Veronica... ah..."
    "Mrs. Pulman's voice adopted an atypical, girlish lilt."
    scene w3_1797 with dissolve
    kat "A body like yours... was made to be put on its knees like this."
    ver "..."

    if kat_polite == True:
        "Veronica didn't say anything, most likely content with letting Mrs. Pulman run down the clock syllable by syllable."
    else:
        "Veronica didn't say anything, most likely content with letting Kathleen run down the clock syllable by syllable."

    scene w3_1798 with dissolve
    kat "You can take a lot without breaking, can't you?"
    "But if anyone was more keenly aware of the time than the Carnations, it would be the old woman. This was her dance, and every pause was a deliberate step for our unseen audience."
    kat "I bet you think you'll be the star of round 1~ that you'll hold out magnificently and show the other Carnations just..."
    play sound "sound effects/shock5.wav"
    scene w3_1799 with vpunch
    ver "Tsk...!"
    scene w3_1800 with dissolve
    kat "...how. Tough. You. Are."
    play sound "sound effects/shock5.wav"
    scene w3_1801 with vpunch
    "*Tchwiick!*"
    ver "Hnngg..."
    scene w3_1802 with dissolve
    "Two short shocks, delivered in quick succession to the tender skin of Veronica's armpit..."
    play sound "sound effects/shock4.wav"
    scene w3_1803 with vpunch
    "*Zhhhiip!*"
    ver "Hnngg...!"
    scene w3_1804 with dissolve
    "Three..."
    play sound "sound effects/shock5.wav"
    scene w3_1805 with vpunch
    "*Zhaaaaap!*"
    scene w3_1806 with dissolve
    "Four..."
    play sound "sound effects/shock5.wav"
    scene w3_1807 with vpunch
    ver "Ahh, hhnngg-!"
    scene w3_1808 with dissolve
    kat "Hmmmm, no doubt~ you really are a tough cookie, slut."
    scene w3_1809 with dissolve
    kat "Open your mouth and stick out your pretty pink tongue, please."
    scene w3_1810 with dissolve
    "Veronica naturally hesitated."
    play sound "sound effects/shock5.wav"
    scene w3_1811 with vpunch
    "*Thwiiiick!*"
    kat "Show me your tongue!"
    scene w3_1812 with dissolve
    ver "G-gahh...!"
    scene w3_1813 with dissolve
    kat "{b}Lick it{/b}."
    scene w3_1814 with dissolve
    ver "..."
    play sound "sound effects/shock5.wav"
    scene w3_1815 with vpunch
    "*Zaaaaap*!"
    scene punish_verol_a with dissolve
    show punish_verol with dissolve
    "For added effect, she shocked the air, urging Veronica's compliance."
    kat "Ah, that's right..."
    "I waited for the shoe to drop."
    kat "That's a good bitch..."
    "A shock delivered to the tongue would hurt like a bitch..."
    kat "...but don't think I've forgotten..."
    "It didn't come, however. Instead..."
    scene w3_1816 with dissolve
    scene w3_1817 with dissolve
    play sound "sound effects/shock4.wav"
    scene w3_1818 with vpunch
    "*Zap*"
    scene w3_1819 with dissolve
    play sound "sound effects/shock5.wav"
    scene w3_1820 with dissolve
    "*Za, zap!*"
    scene w3_1821 with dissolve
    play sound "sound effects/shock4.wav"
    scene w3_1822 with vpunch
    "*Za, thwack, craaaaack!*"
    ver "Gghhhuuu, ah {b}s-son of a bitch..!{/b}"
    "Another fake out in favor of a critical hit on the spot she had been working on."
    scene w3_1823 with dissolve
    ver "Switch!"
    scene w3_1824 with dissolve

    if kat_polite == True:
        "Despite the Amazon's earlier claims, Mrs. Pulman had made short, skillful work of her."
    else:
        "Despite the Amazon's earlier claims, Kathleen had made short, skillful work of her."

    fel "Ah, fuck..."
    "She had barely lasted longer than Rosalind."
    hide screen camcorder
    scene w3_1825 with dissolve
    kat "You're nothing, Miss Lynch. Absolutely nothing."
    kat "How many times do I have to prove that? Now, get your arms back up or it won't count~"
    scene w3_1826 with dissolve
    kat "Now, Mrs. Ford... our industrious, hard-working gold-digging bitch~ whore~ slut~"
    fel "Ah... you're really enjoying this--"
    show screen camcorder
    play sound "sound effects/shock5.wav"
    scene w3_1827 with vpunch
    fel "G-gaaah....!"
    scene w3_1828 with dissolve
    play sound "sound effects/shock4.wav"
    scene w3_1829 with vpunch
    fel "Tsk...! Hnngg..."
    scene w3_1830 with dissolve
    play sound "sound effects/shock5.wav"
    scene w3_1831 with vpunch
    fel "W-wuuuah, {b}switch!{/b}"
    hide screen camcorder
    scene w3_1832 with dissolve
    kat "Huh...? I..."

    if kat_polite == True:
        "Both the other Carnations and Mrs. Pulman herself looked dumbfounded at Felicia's quick submission."
    else:
        "Both the other Carnations and Kathleen herself looked dumbfounded at Felicia's quick submission."

    scene w3_1833 with dissolve
    ver "You got to be kidding me..."
    scene w3_1834 with dissolve
    "The quickest of any of them."
    scene w3_1835 with dissolve
    kat "{i}Interesting{/i}. After your showing Saturday, I was expecting you to hold out much longer."
    scene w3_1836 with dissolve
    fel "It fucking hurts!"
    scene w3_1837 with dissolve
    ver "No shit! And now it's going to--"
    play sound "sound effects/shock4.wav"
    scene w3_1838 with vpunch
    rose "Y-yyyeee!"
    "The round began anew, this time on the second setting."
    show screen camcorder
    scene w3_1839 with dissolve
    "This one went about as quick."
    "Rosalind lasted about the same."
    play sound "sound effects/shock4.wav"
    scene w3_1840 with fade
    "Veronica valiantly held out longer than previously."
    scene w3_1841 with fade
    fel "S-switch!"
    "...and Felicia once again folded to a couple of shocks."
    scene w3_1842 with dissolve
    rose "Again?!"
    scene w3_1843 with dissolve
    "It made sense. Felicia was a hedonist, not a masochist. This game, divorced from physical, sexual gratification or even the arousal of having many men view her naked body, didn't suit her."
    scene w3_1842 with dissolve
    rose "After all your talk about playing this smart?!"
    scene w3_1843 with dissolve
    "Rosalind, next up on the chopping block, was uncharacteristically pissed."
    hide screen camcorder
    scene w3_1844 with dissolve
    fel "I'd be more motivated if you two didn't fold in twenty seconds!"
    scene w3_1845 with dissolve
    ver "It's better than 5!"
    play sound "sound effects/shock5.wav"
    scene w3_1846 with vpunch
    "*Tchhiiiik!*"
    rose "Hnngg...! S-switch!"
    scene black with fade
    "Everyone quickly folded from there."
    scene w3_1851 with fade
    "To her credit, Veronica lasted longer in the third round but quickly gave up in the fourth."
    scene w3_1852 with dissolve
    fel "Switch!"
    scene w3_1853 with dissolve
    kat "Did you really just try that, Mrs. Ford? I have yet to even shock you."
    scene w3_1854 with dissolve
    fel "Hehehe... well... worth a fuckin' shot, right?"
    scene black with fade
    "Of all of them, Felicia proved to be the weakest link."
    kat "Get back into position!"
    scene w3_1855 with wipeleft
    "With just under two minutes to spare, the Carnations were already facing down round 5 and the highest setting."
    scene w3_1856 with dissolve
    kat "Somehow, you girls managed to subvert even my low expectations. I didn't believe we'd get past round 3."
    show screen camcorder
    scene w3_1857 with dissolve
    rose "Hnngg...?"
    scene w3_1858 with dissolve
    kat "Hmmm..."
    kat "..."
    scene w3_1859 with dissolve
    kat "Get some POV shots of you doing it."
    stop music fadeout 3.0
    scene w3_1860 with dissolve
    "......"
    "..."
    scene w3_1861 with dissolve
    kat "[mcf]?"
    hide screen camcorder
    scene w3_1862 with dissolve
    "By this point, I had practically melded with the video camera. After that, I hadn't a thought in my head."
    "It took me a moment to even register that the old woman was talking to me as {i}a person{/i}."
    scene w3_1863 with dissolve
    mc "...what about the time?"
    show screen camcorder
    scene w3_1864 with dissolve
    kat "Time's ticking, but since there's no point in switching anymore, let's say they each get three, and then we'll move on to the {b}fun{/b} part."
    scene w3_1865 with dissolve
    rose "Hehehe.. he... this... wasn't the fun part?"
    scene w3_1866 with dissolve
    mc "...s'okay."
    "It's not like me or her doing it really made a difference here."
    play music "music/unsafe-roads.ogg"
    hide screen camcorder
    scene w3_1867 with dissolve
    "At least, that is what I told myself as I felt a sickeningly sweet knot form in my stomach."
    "This baby was on the menu during Felicia's leg of the last exhibition, but I had purposefully avoided using it. If not for the gold digger's sake, then my own."

    scene w3_1868 with dissolve
    if w2HarpRainCheck == False:
        "I knew it would rival the feeling I got from torturing Harper."
    else:
        "Just the very thought of using this thing enflamed my urges."

    menu:
        "First, give yourself a test shock."(chg=["veronica_up2"]):
            $ Veronica_Affection += 2
            scene w3_1869 with dissolve
            "This will look stupid, but in my mind, it was a matter of utmost prudence. It was my opinion that if you're going to inflict pain on someone for either of your gratifications..."
            play sound "sound effects/shock4.wav"
            scene w3_1870 with vpunch
            mc "Hnngg...!"
            "...the person who inflicted it should try it themselves."
            scene w3_1871 with dissolve
            mct "(Ah, that was...)"
            "The first shock confirmed what I had suspected by watching: knowing the precise time it was coming lessened the effect of the shock."
            "Mind you, it still hurt like hell. At this setting, a horrible pinch immediately robbed me of whole seconds of my breath from me."
            scene w3_1872 with dissolve
            mct "(Again...!)"
            play sound "sound effects/shock5.wav"
            scene w3_1873 with vpunch
            mc "Huuung--!"
            scene w3_1874 with dissolve
            "On top of that, the place the barb made contact left a burning sensation that persisted, grew, and ached with time."
            scene w3_1875 with dissolve
            mct "(One more...)"
            play sound "sound effects/shock4.wav"
            scene w3_1876 with vpunch
            mc "Ah, ha-haak...!"
            scene w3_1878 with dissolve
            mct "(Fuck, that hhh...!)"
            "It was unpleasant, but it wasn't unbearable."
            scene w3_1879 with dissolve
            kat "Was that meant to be a show of solidarity?"
            "There were clearly things I could do to exacerbate or mitigate the effect."
            scene w3_1880 with dissolve
            mc "I was just curious."
            scene w3_1881 with dissolve
            mc "Let's get on with it."
        "Just get straight to it.":

            scene w3_1881 with dissolve
            mc "Let's get on with it."

    scene w3_1882 with dissolve
    "Rosalind looked up at me with a peculiar glint in her eye."
    "It read one part apprehensive, 2 parts get this the fuck over with..."


    menu:
        "Get it over with.":

            scene w3_1883 with dissolve
            mc "Stand up."
            scene w3_1884 with dissolve
            mc "I'm going on three."
            mc "One... two..."
            play sound "sound effects/shock4.wav"
            scene w3_1885 with vpunch
            rose "Hnngg, ah...!"
            "I made a point to target the least sensitive part of the body, the trunk."
            scene w3_1886 with dissolve
            mc "One, two..."
            play sound "sound effects/shock5.wav"
            scene w3_1887 with vpunch
            rose "G-gahhh...!"
            "Going again immediately after the first shock might've seemed like I was being rough. Still, I truly believed the anticipation was a multiplying factor. "
            scene w3_1888 with dissolve
            mc "One, two..."
            play sound "sound effects/shock4.wav"
            scene w3_1889 with vpunch
            rose "F-fhhhh, shit--"
            scene w3_1890 with dissolve
            mc "{b}All done{/b}, Rose."
            mc "That wasn't so bad, was it?"
            scene w3_1891 with dissolve
            rose "Actually..."
            scene w3_1892 with dissolve
            rose "I guess not?"
            scene w3_1893 with dissolve
            kat "Veronica is waiting, Mr. [mcl] - and put a little more pizzazz in it this time, please."
        "Put your all into it(w3RosalindMeanShock=True)."(chg=["kathleen_up","rosalind_down2","veronica_down2"]):

            $ Kathleen_Affection += 1
            $ Rosalind_Affection -= 2
            $ Veronica_Affection -= 1
            $ w3RosalindMeanShock = True

            scene w3_1883 with dissolve
            mc "On your feet."
            scene w3_1894 with dissolve
            mc "On your heels. Back straight."
            scene w3_1895 with dissolve
            "This was my job."
            scene w3_1896 with dissolve
            "{i}A convenient excuse for doing what I wanted to do anyway.{/i}"
            scene w3_1897 with dissolve

            if w2RosalindPhoto == True:
                mc "Push those sloppy tits of yours together, whore."
            else:
                mc "Push your tits together. Make it look good."

            scene w3_1898 with dissolve
            rose "Yes, sir..."
            scene w3_1899 with dissolve
            mc "I didn't tell you to speak. The only sound I want you to make..."
            play sound "sound effects/shock5.wav"
            scene w3_1900 with vpunch
            rose "Gyeee--!"
            "Rosalind had sensitive breasts. In choosing my target, this was a fact I was well aware of."
            scene w3_1901 with dissolve
            rose "Hnngg, f-fuck!"
            scene w3_1902 with dissolve
            mc "That's one..."
            mc "How many are left, Rose?"
            show screen camcorder
            scene w3_1903 with dissolve
            rose "T-two... h-ha..."
            rose "Two mor--"
            play sound "sound effects/shock4.wav"
            scene w3_1904 with vpunch
            rose "Morooorewwwa{b}SHIT-!!!{/b}"
            mc "One more - {i}can't you count?{/i}"
            scene w3_1905 with dissolve
            rose "Euughh...! Just get it over with!"
            "She was giving me the same pissed-off look she was giving Felicia earlier. A look that filled me with a conflicting sense of..."
            scene w3_1906 with dissolve

            if kat_polite == True:
                mct "(This is what Mrs. Pulman chases in her shows, right?)"
            else:
                mct "(This is what the old woman chases in her shows, right?)"

            scene w3_1907 with dissolve
            rose "..."
            "Almost instinctively, I had reached out and tenderly pawed at the tender stretch of tit-flesh I had targeted."
            scene w3_1908 with dissolve
            rose "Hnnggg..."
            hide screen camcorder
            scene w3_1909 with dissolve
            mc "Alright, but give the camera your best expression. You ready?"
            scene w3_1910 with dissolve
            rose "Yeah... go ahead..."
            scene punish_rosan_a with dissolve
            show punish_rosan with dissolve
            rose "Euuggh- ah..."
            "Her face twisted in anticipation of what didn't come."
            rose "Hnnggg..."
            mc "Count to 3."
            rose "Three--"
            play sound "sound effects/shock5.wav"
            scene w3_1911 with vpunch
            rose "Fh, hhhuu-- {b}goddamn it!{/b}"
            scene w3_1912 with dissolve
            mc "Hehe... you should've seen that one coming."
            rose "{b}Should I?!{/b}"
            mc "Well... there was precedent."
            scene w3_1913 with dissolve
            mc "Just... keep your eyes on the prize, Rose."
            rose "Right..."
            scene w3_1914 with dissolve
            kat "Cover back up, Mrs. Carter."
            kat "Veronica is waiting, Mr. [mcl]."


    scene w3_1915 with dissolve
    mc "Yes, Ma'am."
    scene w3_1916 with fade

    if w2ExEndingVeronica == True:
        mc "Hey, Ronnie."
        scene w3_1917 with dissolve
        "She gave me an unusual smile."
        scene w3_1918 with dissolve
        ver "Hey, bones."
        scene w3_1919 with dissolve
    else:
        mc "Hey, Veronica."
        scene w3_1919 with dissolve
        ver "Hey, yourself."

    ver "Well, what are you waiting for?"
    scene w3_1920 with dissolve
    mc "..."

    if w3RosalindMeanShock == True:
        "Veronica had previously encouraged me to not go easy on her but that WAS a different time and place..."
    else:
        "Veronica had previously encouraged me to not go easy on her but that WAS a different time and place..."

    menu:
        "Don't go easy on her.(w3VeronicaMeanShock=True,)"(chg=["kathleen_up"]):
            $ w3VeronicaMeanShock = True
            if w3RosalindMeanShock == True:
                $ Kathleen_Affection += 1
            else:
                $ Kathleen_Affection += 1
                $ Veronica_Affection -= 2

            scene w3_1921 with dissolve
            scene w3_1922 with dissolve
            mc "What do you think you're doing? Dogs don't look humans in the eyes."
            mc "{b}Avert your gaze.{/b}"
            "Since I was told it was such a hit, but mostly because I just enjoyed the dynamic, I decided to harken back to last week's promo."
            scene w3_1923 with dissolve
            ver "..."
            scene w3_1924 with dissolve
            mc "That's better."
            scene w3_1923 with dissolve

            if veronicaFriend == True:
                "This probably seemed contrary to all my talk of friendship, but I think she understood we were each playing the role we chose."
                mct "(At least, I hope she did...)"

            scene w3_1924 with dissolve
            mc "Now, on your arches. Hands like a begging puppy dog."
            scene w3_1925 with fade
            "I would've thought being repeatedly shocked would've put her more on edge than that, but thankfully she painlessly complied with my extraneous demand with only a {i}mildly{/i} annoyed look on her face."
            scene w3_1926 with dissolve
            ver "Let me guess... you want me to beg for it?"
            play sound "sound effects/shock4.wav"
            scene w3_1927 with hpunch
            ver "{b}Eeuugn{/b}-!"
            scene w3_1928 with dissolve
            ver "Ddd--"
            "I deliberately chose that unsteady position for a reason."
            play sound "sound effects/thud-floor.mp3"
            scene w3_1929 with vpunch
            ver "{b}Damn it!{/b}"
            "...and as expected, the recoil from being shocked caused the Amazon to lose her footing."
            scene w3_1930 with dissolve
            ver "The neck? Really--"
            play sound "sound effects/thud-floor.mp3"
            scene w3_1931 with vpunch
            mc "Down, girl."
            mct "(Ah, shit...)"
            scene w3_1932 with dissolve
            "It's gratifying when the plan in your head takes the physical form exactly as you imagined."
            scene w3_1933 with dissolve
            ver "...g-gah, w-why didn't we just start like this then?"
            scene w3_1932 with dissolve
            "I had the large woman pinned under my heel, my cock instantly growing hard from the unearned feeling of power I held over her."

            if veronicaFriend == True:
                "For all my talk of friendship, this seemed contrary indeed..."

            "I could feel myself slipping."
            play sound "sound effects/shock5.wav"
            scene w3_1934 with vpunch
            "*{b}Zhhiiiaaap!*{/b}"
            ver "Hnngg, ghgg--"
            mc "You know why."
            "For added emphasis, I pushed down harder and ground the redhead's breast beneath my foot, delighting in the feeling of resistance as her diaphragm struggled to adapt to my weight."
            scene w3_1932 with dissolve
            mc "If the {i}shoe{/i} was on the other foot..."
            scene w3_1935 with dissolve
            ver "Y-yeahh, yeah... I'd stick it up your ass."
            scene w3_1936 with dissolve
            ver "-- -ah, hehe... maybe I shouldn't have given you ideas, huh?"
            scene w3_1937 with dissolve
            mc "Get up."
            scene w3_1938 with dissolve
            ver "Up, down... up, down--"
            play sound "sound effects/shock4.wav"
            scene w3_1939 with hpunch
            ver "{b}Ghhhuuhuh...!{/b}"
            play sound "sound effects/thud-floor.mp3"
            scene w3_1940 with vpunch
            mc "That's three."
            scene w3_1941 with dissolve
            mc "Sorry, I went a little overboard."
            scene w3_1942 with dissolve
            ver "..."

            if w2ExEndingVeronica == True:
                scene w3_1943 with dissolve
                ver "Thanks."
                scene w3_1944 with dissolve
                if w3RosalindMeanShock == True:
                    ver "It wasn't so bad."
                else:
                    ver "Can't help but notice that you went easier on one of us..."
            else:
                scene w3_1945 with dissolve
                if w3RosalindMeanShock == True:
                    ver "It wasn't so bad."
                else:
                    ver "Can't help but notice that you went easier on one of us..."

            kat "Marvelous, [mcf]. You're a natural!"
        "Conclude this quickly.(if w3RosalindMeanShock=True)"(chg=["rosalind_down2","kathleen_down"]):



            if w3RosalindMeanShock == True:
                $ Rosalind_Affection -= 2
                $ Kathleen_Affection -= 1
            else:

                $ Kathleen_Affection -=2
                $ Kathleen_Trust -= 1

            scene w3_1916 with dissolve
            mc "Stand up and touch your toes."
            scene w3_1919 with dissolve
            ver "...you gotta work on your pick-up lines."
            scene w3_1946 with dissolve
            "An ass as large as Veronica's offered the best of both worlds."
            scene w3_1947 with dissolve

            if w3RosalindMeanShock == True:
                "It would look great for the camera while offering a relatively less painful target due to the sheer amount of fat and muscle."
            else:
                "It would add the bit of \"pizzazz\" the old woman instructed me to while offering a relatively less painful target due to the sheer amount of fat and muscle."

            ver "Well, let me fucking have it, eh?"
            scene w3_1948 with dissolve
            "Instead of a countdown, I let her know it was coming with a slight touch."
            scene w3_1949 with dissolve
            mc "Ready?"
            play sound "sound effects/shock4.wav"
            scene w3_1950 with hpunch
            ver "Ye--"
            scene w3_1951 with dissolve
            "One."
            scene w3_1952 with dissolve
            play sound "sound effects/shock5.wav"
            scene w3_1953 with vpunch
            "{b}*Thiiiik!*{/b}"
            scene w3_1952 with dissolve
            "Two."
            scene w3_1954 with dissolve
            mc "One more..."
            play sound "sound effects/shock4.wav"
            scene w3_1955 with vpunch
            ver "{b}G-gahh!{/b}"
            scene w3_1956 with dissolve
            "Oops, that one was a bit TOO close to her, uh..."

            if w3RosalindMeanShock == True:
                scene w3_1957 with dissolve
                rose "Hnng. She had it easier..."
            else:
                scene w3_1958 with dissolve
                kat "Not quite the added sauce I was hoping for, but..."

    scene w3_1914 with dissolve
    kat "Move onto Mrs. Ford, will you?"
    scene w3_1915 with dissolve
    mc "Yes, Ma'am."
    scene w3_1959 with dissolve
    kat "Oh... [mcf]?"
    kat "Come here!"


    if w3RosalindMeanShock == True and w3VeronicaMeanShock == True:
        $ w3PromoShockFullSadism = True
        scene w3_1960 with dissolve
        kat "You're enjoying yourself, aren't you?"
        scene w3_1961 with dissolve
        mc "I'm doing my job."
        scene w3_1962 with dissolve
        kat "Uh huh. Then why are you smiling right now?"
        scene w3_1961 with dissolve
        mc "If it's going to be done, I might as well--"
        scene w3_1963 with dissolve
        kat "You don't need to explain yourself to me. I just wanted to tell you..."
        scene w3_1962 with dissolve
        kat "Let that Felicia cunt REALLY have it. Consider it an {b}order{/b}."
        scene w3_1964 with dissolve
        mc "..."
        "I didn't quite know what that meant..."
    else:

        scene w3_1965 with dissolve
        kat "I {b}order you{/b} to go all out on Mrs. Ford."
        kat "I'd love to see it, you understand?"
        scene w3_1966 with dissolve
        mct "(...all out?)"

    scene black with fade
    mc "...understood."
    scene w3_1968 with fade
    fel "...ah, what's with that intense look on your face?"
    scene w3_1967 with dissolve
    mc "Just thinking for a second."
    scene w3_1968 with dissolve
    fel "If it's {i}just thinking{/i}, don't be so ominous! Damn!"
    scene w3_1969 with dissolve
    mc "......"
    mc "..."
    scene w3_1970 with dissolve
    fel "What are you--"
    scene w3_1971 with dissolve
    mc "--{b}got it!{/b}"
    fel "{b}Huh--?{/b}"
    scene w3_1972 with dissolve
    "With perhaps more force than I meant to, I grabbed Felicia by her ponytail and yanked her head back, forcing us to see eye-to-eye."
    "In this way, there'd be no mistaking it. I could convey my intentions and show Felicia where my head was at."
    scene w3_1973 with dissolve

    if kat_polite == True:
        mc "You know, it seems you have a target on your back. Mrs. Pulman ordered you to get the worst of it, so..."
    else:
        mc "You know, it seems you have a target on your back. Kathleen ordered you to get the worst of it, so..."

    menu:
        "Be cruel and COMMIT FULLY to your assigned role.(w3FeliciaMeanShock = True)"(chg=["felicia_down3","kathleen_up","kathleen_trust_up2"]):
            $ w3FeliciaMeanShock = True
            $ Felicia_Affection -=3
            $ Kathleen_Affection += 1
            $ Kathleen_Trust += 2

            mc "Apologies in advance. She was rather {b}emphatic{/b} about it."
            "I might be able to fool the camera, but I wouldn't fool the old woman. Felicia, of all people, surely understood getting your hands dirty to preserve your meal ticket."
            scene w3_1974 with dissolve
            fel "Hnng, {i}great{/i}."
            scene w3_1973 with dissolve
            mc "Ready?"
            scene w3_1974 with dissolve
            fel "As I'll ever be--"
            scene w3_1975 with dissolve
            mc "{b}You fuckin' sow{/b}... ahh~!"
            play sound "sound effects/spit2.wav"
            scene w3_1976 with dissolve
            mc "*Fweee!*"
            scene w3_1977 with dissolve
            "Instinctually, Felicia looked pissed. Anyone would."
            scene w3_1978 with dissolve
            fel "Grr, f-fuck you!"
            scene w3_1979 with dissolve
            "After all, spitting on someone was practically a {i}primal{/i} form of disrespect."
            mc "Damn, that's a good look..."

            if w2FelHalfMeasure == True:
                "That's twice in the past three days that I spit on the gold digging blonde... {b}shit{/b}, {i}was this going to be a new thing with me or what?{/i}"

            "A sickening feeling flooded my stomach, telling me to push it further."
            scene w3_1980 with dissolve
            fel "W-wah..!"
            play sound "sound effects/thud-floor.mp3"
            scene w3_1981 with hpunch
            mc "Crawl to the couch, pig."
            "With the exact amount of enthusiasm I intended, I tossed Felicia to the ground and barked my order."
            play sound "sound effects/shock5.wav"
            scene w3_1982 with hpunch
            "*Zhhiiiiiack!*"
            mc "Hurry the fuck up!"
            scene w3_1983 with dissolve
            fel "F-hwwha, j-Jesus Christ! I am!"
            scene black with fade
            "Along the way, I captured the hypnotic way her ass danced as she crawled on all fours. Relishing, not quite so secretly, the sight of the rich blonde on her knees."
            scene w3_1984 with pixellate
            show screen camcorder
            fel "Hnngg..."
            mc "The sow has a nice piggy-cunt."
            fel "S-stop dragging this out."
            hide screen camcorder
            scene w3_1985 with dissolve
            mc "..."
            play sound "sound effects/shock4.wav"
            scene w3_1986 with vpunch
            fel "G-gah...!"
            scene w3_1987 with dissolve
            mc "That one doesn't count. Spread your legs."
            fel "What the hell do you mean it doesn't count?!"
            scene w3_1988 with dissolve
            mc "Did that count, Mrs. Pulman?"
            scene w3_1989 with dissolve
            kat "I don't think you made clean contact. You still got two."
            scene w3_1990 with dissolve
            fel "This is bullshit!"
            scene w3_1991 with dissolve
            kat "It's what you signed up for, Mrs. Ford."
            fel "Hnggg..."
            mc "Spread your legs."
            scene w3_1992 with dissolve
            fel "You're enjoying this too much!"
            scene w3_1993 with dissolve
            mc "Tits out."
            scene w3_1994 with dissolve
            fel "*Sigh* Fair enough."
            scene w3_1995 with dissolve
            mc "You look beautiful, Felicia."
            scene w3_1996 with dissolve
            fel "Yeah, I fuckin--"
            play sound "sound effects/shock5.wav"
            scene w3_1997 with vpunch
            fel "Hnnng, s-shit....!"
            scene w3_1998 with dissolve
            mc "Dumb bitch."
            mc "That one didn't count ei--"
            show screen camcorder
            scene w3_1999 with dissolve
            fel "Are you fucking kidding me?!"
            scene w3_2000 with dissolve
            kat "It didn't count."
            scene w3_2001 with dissolve
            fel "Hnnng...! What the HELL is sexy about this?"
            scene w3_2002 with dissolve
            kat "Do you want to quit?"
            scene w3_2001 with dissolve
            fel "Of course not!"
            scene w3_2002 with dissolve
            kat "Then it didn't count."
            scene w3_2003 with dissolve
            fel "...{b}can't help but notice the disparity between my turn and the others here!{/b}"
            scene w3_2004 with dissolve
            "......"
            "..."
            scene w3_2005 with dissolve
            fel "Please... this isn't fucking fair. Two more... l-let them count?"
            scene w3_2006 with dissolve
            "I don't know if the pitiful look on her face was genuine right now or if she was trying to manipulate me, but her expression..."

            if w3RosalindMeanShock == True and w3VeronicaMeanShock == True:
                "It shamefully excited me even more."
                scene w3_2007 with dissolve
                mc "Okay, {b}two more{/b}."
            else:
                "It made me feel like a real prick."
                scene w3_2007 with dissolve
                mc "Okay, {b}two more{/b}."

            mc "You gotta make them count, though. So show your camera your best expression."
            hide screen camcorder
            scene w3_2008 with dissolve
            fel "*Gulp* Got it..."
            scene w3_2009 with dissolve
            fel "Go ahead."
            scene w3_2010 with dissolve
            mc "Good girl..."
            play sound "sound effects/shock4.wav"
            scene w3_2011 with vpunch
            mc "One...!"
            fel "H-hhhaaa...! HNngng... uuuhhh..."
            scene w3_2012 with dissolve
            fel "T-two...! Give me number two, you bast--"
            play sound "sound effects/shock5.wav"
            scene w3_2013 with vpunch
            fel "Huuunngghh-!"
            scene w3_2014 with dissolve
            mc "Now for number thr--"
            fel "W-whn, wait, what?"
            play sound "sound effects/shock4.wav"
            scene w3_2015 with vpunch
            fel "HNngguguuuuhgghh.....!"
            mc "Huh..."
            scene w3_2016 with dissolve
            "The last surprise shock caused the disheveled housewife to piss herself a little."
            fel "F-fuck...! Goddamn it-! Ah...!"
            scene w3_2017 with dissolve
            mc "..."
            fel "{b}You f-fuckin' jerk!{/b} Hnngg...!"
            scene w3_2018 with dissolve
            ver "Holy shit..."
            rose "Huh... that's..."
            stop music fadeout 3.0
            scene w3_2019 with dissolve
            mc "Was that to your satisfaction, Mrs. Pulman?"
            scene w3_2020 with dissolve
            kat "Was that to my...?"
            play music "music/together-with-you.ogg"
            scene w3_2021 with dissolve
            kat "{b}That was beautiful!{/b}"
            kat "I knew you had it in you..."
            scene w3_2022 with dissolve
            mc "I only did what you asked..."
            scene w3_2023 with dissolve
            kat "We gotta work on your modesty, but..."
            "Her eyes wandered down to my bulging crotch."
            scene w3_2024 with dissolve
            kat "...only in certain areas."
            $ renpy.end_replay()
            scene w3_2056 with dissolve
            mc "What's next?"
            scene w3_2060 with dissolve
            kat "For you? Go to the bar and kill some time for half an hour. I'll retrieve you when I need you."
            scene w3_2059 with dissolve
            "So that was that, huh?"
        "Be plausibly rough, but level and work with Felicia."(chg=["felicia_up2","kathleen_down2","kathleen_trust_down2"]):



            $ Felicia_Affection +=2
            $ Kathleen_Affection -= 2
            $ Kathleen_Trust -=2

            scene w3_2025 with dissolve
            scene w3_2026 with dissolve
            scene w3_2025 with dissolve
            "-- a wink. One that I hoped read, \"trust me\" rather than I'm about to sneeze."
            scene w3_2027 with dissolve
            mc "*Whisper* Work with me a little here, eh?"
            scene w3_2028 with dissolve
            "In a way, we were both on the hook here, but Felicia didn't have the luxury of being an active participant. That meant the onus was on me to deliver us to the end of this asinine game."
            scene w3_2029 with dissolve
            "........."
            scene w3_2028 with dissolve
            "......"
            scene w3_2030 with dissolve
            fel "...what are you waiting for?"
            scene w3_2028 with dissolve
            "Directing her with my own eyes, I said..."
            scene w3_2031 with dissolve
            mc "Now... {i}piggie{/i}..."
            mc "...*whisper* brace yourself."
            scene w3_2032 with dissolve
            fel "W-wah..."
            scene w3_1981 with dissolve
            mc "Crawl to the fuckin' couch."
            "With the exact amount of enthusiasm I intended, I threw Felicia off balance and barked my order."
            play sound "sound effects/shock5.wav"
            scene w3_1982 with vpunch
            mc "Hurry up!"
            fel "G-ghh...!"
            scene w3_1983 with dissolve
            "That was number {b}one{/b}, delivered as just one aspect of a flurry of activity that Felicia had no time to dwell on."
            fel "I'm going, I'm go--"
            scene black with fade
            "Along the way, I captured the hypnotic way her ass danced as she crawled on all fours, secretly relishing the sight of the rich blonde on her knees."
            scene w3_1984 with pixellate
            show screen camcorder
            fel "Hnngg... what are you doing?"
            mc "I'm documenting your body, but you shouldn't focus on what I'm doing now."
            hide screen camcorder
            scene w3_2033 with dissolve
            fel "Yeah...? What should I be...?"
            scene w3_2034 with dissolve
            mc "Spread your legs."
            scene w3_2035 with dissolve
            fel "..."
            scene w3_2036 with dissolve
            "She did as I asked, granting me further access down the long stretch of her toned legs."
            scene w3_2037 with dissolve
            mc "*Whisper* Lotta people are going to see this. Which Felicia are you going to show them?"
            scene w3_2038 with dissolve
            fel "..."
            scene w3_2039 with dissolve
            "She understood my words. This setup might seem cold and clinical, but she did have an audience - that held some meaning to Felicia, didn't it?"
            scene w3_2040 with dissolve
            mc "*Whisper* Just two shocks in just as many settings. You've done more unpleasant things, right?"
            mc "I mean, this has got to be more palatable than half the fat old bastards you've fucked. Am I wrong?"
            "This part, I said loud enough for the old woman to hear."
            scene w3_2041 with dissolve
            fel "Oh, fuck you, asshole!"
            mc "Yeah, yeah... Get your disgusting tits out, you sow."
            scene w3_1994 with dissolve
            fel "Fair enough."
            scene w3_2042 with fade
            fel "Is this--"
            play sound "sound effects/shock4.wav"
            scene w3_2043 with vpunch
            fel "G-hhggg...! D-damn it!"
            scene w3_2044 with dissolve
            "I aimed at a pretty tender area, but it wasn't the worst."
            scene w3_2045 with dissolve
            mc "You got one more. Let's make it count."
            scene w3_2046 with dissolve
            fel "What do you...?"
            scene w3_2047 with dissolve
            scene w3_2046 with dissolve
            "I did my best to gesture back to where Kat was."
            scene w3_2048 with dissolve
            "One more. {b}Make it count.{/b}"
            scene w3_2049 with pixellate
            show screen camcorder
            "Then it would be over."
            scene w3_2050 with dissolve
            fel "Heh... ah... s-shit..."
            hide screen camcorder
            scene w3_2051 with dissolve
            fel "Bah! Go ahead!"
            scene w3_2052 with dissolve
            "As a man, I couldn't imagine how this might feel, but Felicia had her game face on, and it should satisfy the old woman at the least."
            play sound "sound effects/shock5.wav"
            scene w3_2053 with vpunch
            fel "Ghh, ahhhoowowowow--"
            fel "WHYDIDISAY--"
            scene w3_2054 with dissolve
            fel "Ah... {i}that's three...{/i}"
            mc "Yep. All done."
            stop music fadeout 3.0
            scene w3_2055 with dissolve
            mc "Was that to your satisfaction, Mrs. Pulman?"
            scene w3_2057 with dissolve
            kat "......"
            play music "music/together-with-you.ogg"
            scene w3_2058 with dissolve
            kat "...good enough, I suppose. *Sigh* You didn't quite get that look about you I was hoping for."
            $ renpy.end_replay()
            scene w3_2059 with dissolve
            mc "Wasn't this about Felicia?"
            scene w3_2060 with dissolve
            kat "It's all connected..."
            scene w3_2059 with dissolve
            "She looked through me in a way that stopped me from asking further questions. The fact THAT wasn't rough enough to satisfy her was telling..."
            mc "What's next?"
            scene w3_2060 with dissolve
            kat "For you? Go to the bar and kill some time for half an hour. I'll retrieve you when I need you."
            scene w3_2059 with dissolve
            "So that was that, huh?"

    scene w3_2061 with dissolve
    if not persistent.w3ShockGame:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3ShockGame = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    kat "...and for them? I've got to get them set up and hooked in for the punishment game."
    scene w3_2062 with dissolve
    rose "Ummm, hooked in?"
    scene w3_2063 with dissolve

    if w2ExLosersAll == True:
        kat "Yep. All three of you are going to have some fun."
    if w2ExLoserDuo == True:
        kat "Well, Miss Lynch and Mrs. Ford, at least. Rosie, you'll take a more {i}active role.{/i}"
    if w2ExLoserFelicia == True:
        kat "Well, Mrs. Ford at least. You and Miss Lynch will take a more... {i}active{/i} role."
    if w2ExLoserVeronica == True:
        kat "Well, Miss Lynch at least. You and Mrs. Ford will take a more... {i}active{/i} role."

    scene w3_2064 with dissolve
    ver "Looking forward to it..."
    scene w3_2065 with dissolve
    kat "Before you go... do you want to hear something amusing?"
    mct "(This will be good...)"
    scene w3_2066 with dissolve
    kat "This thing doesn't even have multiple settings. It's all one power!"
    scene w3_2067 with dissolve
    mc "Huh... I did wonder about that."
    "The only button that I noticed was the trigger."
    mc "That's... that's actually kinda funny. It still stung like hell, though."
    scene w3_2068 with dissolve
    kat "True, but never more or less. Isn't the power of suggestion a wonderful thing?"
    scene w3_2069 with dissolve
    mc "Yeah, thanks for the teaching moment..."
    scene w3_2070 with dissolve
    "Suddenly, an intrusive thought took root in my brain. I wanted to..."

    menu:
        "Shock Mrs. Pulman.(Dialouge/render changes only)":
            scene w3_2071 with dissolve
            kat "Now, why don't you--"
            play sound "sound effects/shock5.wav"
            scene w3_2072 with vpunch
            kat "G-gh...! Y-you...!"
            "Without a second thought, I did just that."
            scene w3_2073 with dissolve
            kat "You've wanted to do that since before the phone call, haven't you?"
            scene w3_2074 with dissolve
            kat "Well... fair's fair. {b}I guess{/b}."
            scene w3_2075 with dissolve
            "......"
            "..."
            scene w3_2076 with dissolve
            kat "Now... why don't you get your ass to the bar and give that fanatical slut some company while you wait?"
            scene w3_2077 with dissolve
            mc "Um... who?"
            scene w3_2078 with dissolve
            kat "Sorry. I mean... {b}Miss Lundgren{/b}. That's just my pet name for her."
            scene w3_2077 with dissolve
            mc "Seems like you two are excellent friends."
            scene w3_2076 with dissolve
            kat "Go now."
            scene w3_2079 with dissolve
            mc "Yes, Ma'am."
        "Ignore it.":


            scene w3_2071 with dissolve
            kat "Now, why don't you go ahead and wait at the bar? While you're there, you can give Miss Lundgren company."
            scene w3_2080 with dissolve
            mc "Yes, Ma'am."
            scene w3_2081 with dissolve
            kat "Good boy."

    stop music fadeout 3.0
    scene black with fade
    "Even here, the worst part of any job is standing around waiting."
    "......"
    "..."
    jump w3SophiaBarRendezvous


label w3SophiaBarRendezvous:
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionsophia01 with blinds
    $ renpy.pause(6, hard=True)
    play music "music/air-on-g.ogg"
    scene w3_2082 with wipeleft
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    "The moment I entered the bar, Sophia's eyes were upon me."
    scene w3_2083 with dissolve
    sophia "Say... what do you have to do to get some service in this place?"
    scene w3_2084 with dissolve
    mc "Be the change you want to see in the world. Pour me a glass of water, babe."
    scene w3_2085 with dissolve
    sophia "...was that a joke?"
    scene w3_2086 with dissolve
    mc "...it was a joke, yes."
    scene w3_2087 with dissolve
    sophia "Hmmm..."
    scene w3_2085 with dissolve
    sophia "It wasn't very humorous."
    scene w3_2086 with dissolve
    mc "No, it really wasn't. You got any funny--"
    scene w3_2089 with dissolve
    sophia "......"
    scene w3_2090 with dissolve
    sophia "...okay, stop me if you've heard this one."
    "Well, {b}shit{/b}. I didn't expect that answer, especially not from her."
    scene w3_2091 with dissolve
    mc "S'alright..."
    "That's the first time anyone's ever called my bluff on that line..."
    mct "(This should be good.)"
    scene w3_2092 with dissolve
    sophia "A man walks into a bar and sees two large pieces of meat hanging from the ceiling. Naturally he's confused."
    scene w3_2093 with dissolve
    sophia "So he asks the bartender, pointedly, {i}what the hell is with the meat, Jim?{/i} - ah, Jim... that's the bartender's name by the way."
    scene w3_2094 with dissolve
    mc "I... {b}got it{/b}."
    scene w3_2092 with dissolve
    sophia "The bartender tells him {i}it's a game I like to play. I bet everyone who comes in here $20 they can't pull one of them down. Care to try?{/i}"
    scene w3_2095 with dissolve
    sophia "The man pauses a moment, giving it some serious thought, before finally answering..."
    sophia "{b}No.{/b} The {i}STEAKS{/i} are too high."
    scene w3_2096 with dissolve
    mc "........."
    mc "......"
    "She looked at me expectantly, confidently awaiting a laugh."
    scene w3_2097 with dissolve
    mc "...oh, yeah. I get it."
    scene w3_2098 with dissolve
    sophia "Your sense of humor must be off. Abel chuckled at that one."
    scene w3_2099 with dissolve
    mc "Did he...?"
    scene w3_2100 with dissolve
    mc "Well, never tell a pun to a kleptomaniac.... they're always taking things {i}literally.{/i}"
    scene w3_2089 with dissolve
    sophia "Hmmm..."
    scene w3_2085 with dissolve
    sophia "...that's a pretty good one."
    mct "(No, it fucking wasn't...)"
    scene w3_2088 with dissolve
    mc "Feel free to use it on Dr. Van Doren if you want."
    scene w3_2087 with dissolve
    "Ah... this was a bizarre way to start a conversation..."
    scene w3_2101 with dissolve
    sophia "Let's talk on the couch."
    scene w3_2102 with dissolve
    mc "I... no, thank you. I'd like to leave room for Jesus, if you know what I mean."
    scene w3_2103 with dissolve
    sophia "Are you always this reserved around women?"
    scene w3_2104 with dissolve
    mc "Only the women prone to chemically dosing me into a stupor. Do you always wear that perfume wherever you go?"
    scene w3_2103 with dissolve
    sophia "Only sometimes. Just whenever it doesn't represent a problem."
    scene w3_2105 with dissolve
    mc "What is it, field testing?"
    scene w3_2106 with dissolve
    sophia "Oh, no. That would be... {b}absurd.{/b}"
    scene w3_2107 with dissolve
    sophia "Chemistry is a discipline. It's rigid and controlled; this is..."
    scene w3_2108 with dissolve
    sophia "Just a bit of chaos."
    scene w3_2109 with dissolve
    sophia "{b}Come.{/b} Sit with me on the couch. I know you have some time to kill."
    scene w3_2110 with dissolve
    mc "Ah, shit..."
    "Guess the reason Mrs. Pulman pointed me this way for the interim was to babysit..."
    "I could already feel Sophia's \"just a bit of chaos\" work its way into my system, my skin growing flush as the already captivating beauty and her tendered hand made the turn to outright magnetic."
    hide screen textbox2 with dissolve
    menu:
        "Take her hand(w3SophiaPolite = True).":
            $ w3SophiaPolite = True
            scene w3_2111 with dissolve
            show screen textbox2 with dissolve
            mc "Alright. Turning you down twice would be rude."
            "Part of my job was to kiss up to the club's constituents, and silver lining, this would at least be an exercise in control. I was positive this wouldn't be my last time around Sophia's bewitching concoction."
            scene w3_2112 with dissolve
            sophia "Ah!"
            sophia "--{i}to make enemies by unnecessary and willful incivility is just as insane a proceeding as to set your house on fire. For politeness is like a counter--an avowedly false coin, with which it is foolish to be stingy.{/i}"
            scene w3_2113 with dissolve
            mc "Huh, no... I wasn't... uh, who said that?"
            scene w3_2114 with dissolve
            sophia "I... don't know who said it originally, but it's a maxim imparted to me by Abel."
            scene w3_2113 with dissolve
            mc "I see... well, for the record... is everything you do Machiavellian?"
            scene w3_2115 with dissolve
            sophia "--{i}a prince must want to have a reputation for compassion rather than for cruelty: nonetheless, he must be careful that he does not make bad use of compassion.{/i}"
            scene w3_2116 with dissolve
            mc "I'm... starting to think I should turn you down, Miss Lundgren."
            scene w3_2117 with dissolve
            sophia "No taksie backsies, [mcf]."
            scene w3_2118 with dissolve
            "I was fast gathering that Sophia was an odd woman, but maybe that was just the mark of a genius."
            scene w3_2122 with fade
            mc "So, you must be an amazing chemist."
            scene w3_2124 with dissolve
            "...and even if it wasn't, \"odd\" was just as quickly losing meaning as a qualifier within these walls."
        "Ignore her and lead the way to the sofa.":


            scene w3_2119 with dissolve
            show screen textbox2 with dissolve
            mc "Sure. Let's sit down."
            scene w3_2120 with dissolve
            "Schmoozing the club's constituents was part of the job and one I accepted, but the way my body rebelled under the effects of Sophia's bewitching concoction simply left a bad taste in my mouth. "
            sophia "..."
            scene w3_2121 with dissolve
            "Still, this woman was a certified genius. It wouldn't be such bad company - ah, gah... I couldn't even be sure if those were my own thoughts!"
            scene w3_2122 with fade
            mc "So, you must be an amazing chemist."
            scene w3_2124 with dissolve
            "The quality of her company withstanding, I trusted that aspect of my thoughts."

    scene w3_2123 with dissolve
    sophia "No, not at all. Amazing is a strong word."
    scene w3_2122 with dissolve
    mc "How old are you and don't give me never ask a woman her--"
    scene w3_2123 with dissolve
    sophia "Thirty-one."
    scene w3_2125 with dissolve
    mc "Considering your position at Waller Scientific, that is amazing."
    scene w3_2126 with dissolve
    sophia "No, no... a man like Herr Krüger was worthy of being called an amazing chemist. Me...?"
    scene w3_2127 with dissolve
    "Again she refuted me. She must be incredibly humbl--"
    scene w3_2128 with dissolve
    sophia "I am... {i}simply{/i} the best."
    scene w3_2127 with dissolve
    "{b}Nevermind.{/b}"
    scene w3_2129 with dissolve
    mc "...that you know of?"
    scene w3_2130 with dissolve
    sophia "I was precise with my words."
    scene w3_2131 with dissolve
    "The oddest thing was I detected not a single iota of pride or hubris in that statement. It was as if Sophia was telling me the sky was blue."
    mc "Herr Krüger was a mentor, I presume?"
    scene w3_2128 with dissolve
    sophia "Among many other things."
    scene w3_2129 with dissolve
    mc "...and did you always want to be a chemist?"
    scene w3_2130 with dissolve
    sophia "Are you conducting an interview, Mr. [mcl]?"
    scene w3_2131 with dissolve
    mc "Just call me [mcf]. Please. {b}Seriously.{/b?}"
    scene w3_2130 with dissolve
    sophia "Okay, [mcf] please seriously - {b}you are asking a lot of questions back-to-back.{/b}."
    scene w3_2127 with dissolve
    mc "Hey...! Maybe I'm just a shitty conversationalist, okay?"
    scene w3_2132 with dissolve
    "......"
    "..."
    scene w3_2133 with dissolve

    if w3SophiaPolite == True:
        mc "*Ahem* We're making small talk, so I won't promise that will be the last one you'll hear. You are a fascinating person."
        sophia "Uh huh, I bet..."
    else:
        mc "*Ahem* I was bidden to make small talk, so I can't promise that will be the last one you'll hear."

    scene w3_2126 with dissolve
    sophia "Are you feeling okay? Your eyes look a bit distant."
    scene w3_2125 with dissolve
    mc "You're... {i}very{/i} attractive."
    "Perhaps alarmingly, I said that all too easily."
    scene w3_2126 with dissolve
    sophia "What do you like better? My thighs or my stomach?"
    scene w3_2125 with dissolve
    mc "Why... those two?"
    "A better question might've been why she was even asking, but in the moment, questioning the question behind the question felt {i}laborious{/i}."
    scene w3_2130 with dissolve
    sophia "Following a man's eye line is an essential skill for any woman, especially one in a position like mine."
    sophia "Your glances are... not furtive."
    scene w3_2131 with dissolve

    if w3SophiaPolite == True:
        mc "I imagine they wouldn't, considering..."
    else:
        mc "Well, no shit, I imagine they wouldn't be. Considering..."

    scene w3_2134 with dissolve
    mct "(Yeah...)"
    scene w3_2135 with dissolve
    sophia "Now, answer my question. It's valuable information."
    scene w3_2136 with dissolve
    mc "Answer my question first."
    scene w3_2137 with dissolve
    sophia "...what did you ask? Did I {i}want{/i} to be a chemist?"
    scene w3_2138 with dissolve
    mc "The emphasis was supposed to be on {i}always.{/i}"
    scene w3_2139 with dissolve
    sophia "Asking me that is akin to me asking if you wanted to be born a human being. I AM a chemist."

    if w3SophiaPolite == True:
        scene w3_2140 with dissolve
        mc "Aha! I like it! That's intense!"
        "That... came out WAY stronger than I meant, but those were also my true feelings."
        scene w3_2142 with dissolve
        mc "You're saying you feel like you were born to do what you do. That kind of certainty is admirable."
    else:

        scene w3_2141 with dissolve
        mc "You're saying you feel like you were born to be a chemist? That kind of certainty is admirable."

    scene w3_2128 with dissolve
    sophia "Ah, that's not quite... is it admirable to be born tall?"
    scene w3_2127 with dissolve
    mc "You're taking your metaphor a little too seriously. I imagine you've worked hard to land where you're at."
    scene w3_2129 with dissolve

    if w3SophiaPolite == True:
        mc "There must be many people who have discounted you because of your age and gender. You're entitled to act like you kick ass."
    else:
        mc "There must be many people who have discounted you because of your age and gender. Is false humility a product of that?"

    scene w3_2127 with dissolve
    sophia "......"
    scene w3_2143 with dissolve
    sophia "...chemistry, in the loosest sense, is about systematically isolating inputs in a concerted effort to achieve a desired range of outputs."
    sophia "...in a lot of the same way, with efficacious foresight and the proper guidance, personal want becomes a dependent variable that can be controlled."
    scene w3_2131 with dissolve
    mc "...wait, you {i}literally{/i} think of yourself as an effect, not the cause?"
    "Not that I didn't sympathize with or understand that line of thinking or find it seductive, for that matter, but..."
    scene w3_2130 with dissolve
    sophia "We have gone down a rabbit hole I didn't remotely intend."
    scene w3_2129 with dissolve
    "Tossing away a sense of culpability in your life, even if it's ultimately an illusion, felt tantamount to admitting defeat. Defeat over {b}what{/b} I wasn't entirely sure, but it was a dreadful feeling that I emphatically rejected."
    scene w3_2128 with dissolve
    sophia "But what I've gathered from this is... you're a man who highly values certainty?"
    scene w3_2129 with dissolve
    mc "Well... kinda. I know that certainty is a pipe dream, but being sure of yourself is fundamental to every aspect of life."
    mc "Everything you do and every choice you make is built on the foundation of your own self-image. So maybe when I called it admirable, I should've used the word... enviable?"
    "The awkwardness of our initial words had quickly collapsed, and I was freely professing my thoughts almost unfiltered. Leaving me with the obvious question of {i}why{/i} did I find Sophia so easy to talk to?"
    scene w3_2144 with dissolve
    sophia "Self-image, huh...?"
    scene w3_2145 with dissolve
    "Sophia closes her eyes, letting herself momentarily get washed away in thought."
    scene w3_2128 with dissolve
    sophia "Sounds fickle and prone to change."
    scene w3_2146 with dissolve
    mc "It totally is, but... ah... heh. Actually, how did we even end up talking about this again?"
    scene w3_2147 with dissolve
    sophia "You lobbed an unfunny, sexist joke in my lap."
    scene w3_2146 with dissolve
    mc "Oh, {b}right{/b}..."
    scene w3_2147 with dissolve
    sophia "Men should find their self-worth in ideas and a purpose outside of themselves."
    scene w3_2148 with dissolve

    if w3SophiaPolite == True:
        mc "Is it another one of Dr. Van Doren's maxims?"
        scene w3_2149 with dissolve
        sophia "It is something I've learned myself."
        scene w3_2148 with dissolve
        mc "I don't disagree, but..."
    else:
        mc "I don't disagree, but..."

    scene w3_2150 with dissolve
    "For no rhyme or reason, the lush color of Sophia's lips and the cavernous suckhole that lay beyond their plump borders diverted my train of thought."
    mct "(Ah... focus, you dumb animal.)"
    scene w3_2151 with dissolve
    sophia "You don't disagree, buuuuut...?"
    scene w3_2150 with dissolve
    mc "...I don't disagree, but y-you got to know yourself to know which ideas are worthwhile, right?"
    scene w3_2152 with dissolve
    sophia "Hmmm... not really?"
    scene w3_2153 with dissolve
    sophia "In my experience, the most worthwhile of purposes finds you."
    scene w3_2154 with dissolve
    "Her voice dropped to a sultry octave, sending a shiver down my spine and wresting my attention from the hypnotizing curl of her cockholster and back on the devil herself."
    scene w3_2155 with dissolve
    mc "To be frank, I'm not sure what we're talking about anymore."
    scene w3_2156 with dissolve
    sophia "Neither do I. We're just kinda... yapping and killing time, are we not?"
    scene w3_2157 with dissolve
    mc "You're... waiting too?"
    scene w3_2158 with dissolve
    sophia "Do you think I'm just fucking around in an empty bar?"
    scene w3_2159 with dissolve
    mc "Um..."
    "......"
    scene w3_2160 with dissolve
    mc "...yeeeeees?"
    scene w3_2161 with dissolve
    sophia "Remember when I said I knew you had time to kill? Well, that's because I also have time to kill, for the same reason as you."
    scene w3_2162 with dissolve
    sophia "I'll be sitting alongside you for Kathleen's little farce."
    scene w3_2163 with dissolve
    sophia "Let's get along, Mr. [mcl]."
    scene w3_2164 with dissolve
    mc "Back to the mister shit, are we?"
    scene w3_2165 with dissolve
    sophia "By the way, you owe me an answer."
    scene w3_2166 with dissolve
    mc "To what?"
    scene w3_2167 with dissolve
    sophia "My stomach or my thighs?"
    scene w3_2168 with dissolve
    mc "Are you...?"
    scene w3_2169 with dissolve
    "She {b}was.{/b}"
    hide screen textbox2 with dissolve

    menu:
        "Stomach.(Dialouge/render changes only)":
            scene w3_2170 with dissolve
            show screen textbox2 with dissolve
            mc "Fine. Your stomach... you could balance a quarter on it."
            sophia "Noted, thank you -- but, uh... why did you pick a quarter of all things?"
            scene w3_2132 with dissolve
            mc "That wasn't really the point. I'm saying you have an abdomen that I want to eat soup out-- {b}d-damn it{/b}, why can I only think of object-based compliments right now?"
            sophia "Heh~ hehe."
            scene w3_2133 with dissolve
            mc "By the way, how is that \"useful\" information?"
            scene w3_2171 with dissolve
            sophia "It's not really. I was just bored."
            scene w3_2172 with dissolve
            sophia "Can I offer you a drink?"
            scene w3_2173 with dissolve
            mc "Are you...?"
            scene w3_2174 with dissolve
            sophia "Show me where this \"velvet room\" is, please."
            scene black with fade
            "She {b}wasn't{/b}, but her swinging hips held my attention hostage as we cut through the halls to yet another one of Mrs. Pulman's games."
            stop music fadeout 3.0
            "......"
            "..."
            jump w3Ex2PunishmentGame
        "Thighs.":


            scene w3_2132 with dissolve
            show screen textbox2 with dissolve
            mc "Fine. Your thighs."
            mc "They're like a horizon that entices you to journey to what's beyond."
            scene w3_2133 with dissolve
            sophia "Noted. Thank you."
            mc "By the way, how is that \"useful\" information?"
            scene w3_2171 with dissolve
            sophia "It's not really. I was just bored."
            scene w3_2175 with dissolve
            sophia "...but would you like to take a glimpse beyond the horizon?"
            scene w3_2176 with dissolve
            mc "Are you...?"
            scene w3_2174 with dissolve
            sophia "Show me where this \"velvet room\" is, please."
            scene black with fade
            "She {b}wasn't{/b}, but her swinging hips held attention hostage as we cut through the halls to yet another one of Mrs. Pulman's games."
            stop music fadeout 3.0
            "......"
            "..."
            jump w3Ex2PunishmentGame

        "Be glib. Sorry. You have a girlfriend, so you shouldn't say." if hanaGF == True:
            scene w3_2177 with dissolve
            mc "You know, I don't feel comfortable saying. I have a girlfriend."
            scene w3_2178 with dissolve
            "That... felt weird to say. How long had I been single...?"
            scene w3_2179 with dissolve
            sophia "Oh? That's, uh... is that a joke?"
            scene w3_2178 with dissolve
            "I didn't actually want to count."
            scene w3_2180 with dissolve
            mc "It actually isn't."
            scene w3_2181 with dissolve
            sophia "Too bad. That would've been the first humorous thing you said."
            mc "Fuuuuuck yoooou."
            scene w3_2182 with dissolve
            sophia "Well, We could. We may have some time before Kathleen finishes setting up."
            scene w3_2183 with dissolve
            mc "Are you...?"
            scene w3_2184 with dissolve
            sophia "Show me where this \"velvet room\" is, please."
            scene black with fade
            "She mercifully {b}wasn't{/b}. With how turned on I was, I wasn't exactly confident in the upper limits of my self-control..."
            "Still, her swinging hips held my attention hostage as we cut through the halls to yet another one of Mrs. Pulman's games."
            stop music fadeout 3.0
            "......"
            "..."
            jump w3Ex2PunishmentGame

label w3Ex2PunishmentGame:

    play music "music/i-knew-a-guy.ogg"
    scene w3_2185 with cmet
    "Once I had shown her to the big, dumb, blue room in question... I seized the chance to put some distance between us."
    sophia "I guess she's still...? How long does it take to set things up?"
    "Distance that I hoped would place my desire into a waning state, but..."
    scene w3_2186 with dissolve
    sophia "*Sigh* I should've offered my help with more insistence..."
    scene w3_2187 with dissolve
    "...instead, it just filled me with a wicked sense of yearning."
    scene w3_2188 with dissolve
    sophia "Let me ask you something. As I understand it, you haven't worked here for very long, correct?"
    scene w3_2189 with dissolve
    mc "......"
    mc "..."
    scene w3_2190 with dissolve
    sophia "I said... YOU HAVEN'T WORKED HERE VERY LONG, have you, Mr. [mcl]?"
    mc "...ah, um... yeah. That's right."
    scene w3_2191 with dissolve
    sophia "What's your take on Kathleen? How do you evaluate her as... {i}a person?{/i}"
    scene w3_2192 with dissolve
    mc "As a person...?"
    scene w3_2193 with dissolve
    mct "(She's...)"
    play sound "sound effects/high-heel-footsteps.wav"
    scene w3_2194 with dissolve
    "*Clack, clack, clack...*"
    scene w3_2195 with dissolve
    sophia "Forget that thought."
    stop sound
    scene w3_2196 with dissolve
    kat "You're here? I told you I'd come and get you at the bar when things had been fully prepared."
    sophia "I was getting impatient, so I asked [mcf] to show me here."
    scene w3_2197 with dissolve
    sophia "I don't understand why we can't watch the proceedings in person."
    kat "I've explained it already; that's the magic to--"
    scene w3_2198 with dissolve
    mc "Where are the Carnations?"
    kat "In the obsidian room, hooked up and... {i}growing antsy{/} themselves. You see..."
    scene w3_2199 with dissolve

    if w2ExLoserFelicia == True:
        kat "Mrs. Ford's punishment for coming in last will lie in the hands of her competitors."
        kat "...and as I've already explained to Miss Lundgren, we will review the scene remotely so that Rosalind and Veronica might act with more... {i}impunity.{/i}"
    if w2ExLoserVeronica == True:
        kat "Miss Lynch's punishment for coming in last will lie in the hands of her competitors."
        kat "...and as I've already explained to Miss Lundgren, we will review the scene remotely so that Rosalind and Felicia might act with more... {i}impunity.{/i}"
    if w2ExLoserDuo == True:
        kat "Miss Lynch and Mrs. Ford's punishment for tying for last place will lie in the hands of sweet little Rosalind."
        kat "...and as I've already explained to Miss Lundgren, we will review the scene remotely so that she might act with more... {i}impunity.{/i}"
    if w2ExLosersAll == True:
        kat "Those sluts' punishment over tying for last place lies in their own hands - well, more specifically, Miss Lynch drew lots to take a more \"active\" role... but she won't have an easy time with it."
        kat "...and as I've already explained to Miss Lundgren, we will review the scene remotely so that she might act with more... {i}impunity.{/i}"

    kat "A sense of privacy will let them play off each other more naturally, and more importantly, feel a greater responsibility and animosity for what transpires."
    scene w3_2200 with dissolve
    sophia "They {i}are{/i} aware they're being watched?"
    scene w3_2199 with dissolve
    kat "Of course. The girls aren't that stupid."
    scene w3_2200 with dissolve
    sophia "Then isn't it the same if I were to observe closely?"
    scene w3_2201 with dissolve
    kat "Trust me on this one. Just removing a physical presence can have a powerful effect on a person's psychology, camera or no camera."
    kat "I know you don't care about the artistry of this, but you {b}will{/b} observe a more potent result this way."
    scene w3_2202 with dissolve
    sophia "..."
    scene w3_2203 with dissolve
    kat "Sit down. {i}Kick your feet up.{/i}"
    kat "Perhaps [mcf] can go fetch you a drink while you wait for the show to begin?"
    scene w3_2204 with dissolve
    sophia "No, thank you."
    scene w3_2205 with fade
    mc "Uh... am I even needed for this?"
    mct "(If you don't mind, I'd like to find a toilet stall to beat off in...)"
    scene w3_2206 with dissolve
    kat "What a silly question. How could you fulfill your role as moral support if you don't know what the girls experience?"
    scene w3_2207 with dissolve
    kat "Besides, two is better than being alone in that woman's company."
    scene w3_2208 with dissolve
    mc "I... *ahem*... {b}got it{/b}."
    kat "Hmmm? What's the matter, [mcf]?"
    kat "Are you feeling alright? You're looking flushed."
    stop music fadeout 3.0
    scene w3_2209 with dissolve

    if w3SophiaPolite == True:
        mct "(An exercise in control {b}my ass.{/b})"
    else:
        mct "This... this is going to take a while, and I'm..."

    scene black with fade
    "I'm going to die."

label w3PunishGame:

    play music "music/landing.ogg"
    if w2ExLoserFelicia == True:
        scene w3_2210 with pixellate
        fel "Ugggh... aawwwahh... ahh..."
        scene w3_2211 with dissolve
        rose "How long has it been?"
        scene w3_2210 with dissolve
        fel "S-seriously, ug-ugh...!"
        scene w3_2212 with dissolve
        ver "About roughly fifteen minutes."
        scene w3_2213 with dissolve
        rose "{b}Oh.{/b} She said to begin after ten. I guess we should--"
        scene w3_2214 with dissolve
        fel "G-goddammit, you bitches! Let me have a drink of that water. That shit she gave me is making me--"
        scene w3_2215 with dissolve
        rose "I don't know what to do..."
        ver "No, the old bitch sure as shit wasn't explicit... I mean, \"have fun and make it a good show\"...?"
        scene w3_2216 with dissolve
        rose "You should start."
        ver "Are you trying to pawn this off on me?"
        fel "Unnggg....!"
        scene w3_2217 with dissolve
        rose "No! Just... I don't really have any experience with this sort of... {i}thing{/i}."
        ver "And you think I do?"
        scene w3_2218 with dissolve
        fel "J-just fucking begin...! The sooner you do, the sooner I can--"
        scene w3_2219 with dissolve
        ver "What about you, Blondie? You've done this sort of thing before, right?"
        ver "What should we do?"
        scene w3_2220 with dissolve
        fel "E-eh? I haven't ever-- unngg, whatever just-- g-grab one of the dildos..."
        scene w3_2221 with dissolve
        ver "Alright..."
        scene w3_2222 with dissolve
        rose "Wait... would that really be {i}tormenting{/i} her?"
        rose "Mrs. Pulman said to punish her..."
        scene w3_2223 with dissolve
        ver "I mean... I don't know? She's strung out of her mind on that aphrodisiac shit. A little touch and go could be pretty mean."
        scene w3_2224 with dissolve
        rose "..."
        scene w3_2225 with dissolve
        ver "What, you got a better idea?"
        scene w3_2226 with dissolve
        rose "I know what would work on me..."
        fel "CAN YOU GIVE ME SOME FUCKING WATER FIRST?!"
        ver "I just got an idea myself."
        scene w3_2276 with pixellate
        kat "Ha! By the end of this week, I will have these bitches hating each other."
        sophia "The blonde is abnormally thirsty..."


    if w2ExLoserVeronica == True:
        scene w3_2227 with pixellate
        ver "Unnngg, aaahh..."
        scene w3_2228 with dissolve
        rose "What do you think we should do?"
        scene w3_2229 with dissolve
        ver "C-c'mon...! It's--"
        scene w3_2230 with dissolve
        fel "You heard the lady. She told us to have fun, punish Red, and make it a good show."
        scene w3_2231 with dissolve
        rose "Y-yeah, but... uh, you want to start then?"
        scene w3_2232 with dissolve
        ver "It's past time! L-let's get this rolling!"
        scene w3_2233 with dissolve
        fel "I could. Lotta stuff to work with over there... just pick and point, right?"
        rose "A lot of that stuff is scary..."
        scene w3_2234 with dissolve
        fel "It all comes down to how you use it. We just got to remember that--"
        scene w3_2235 with dissolve
        ver "Haa, hhhaa... unnghh..."
        scene w3_2234 with dissolve
        fel "...she's hopped up on that sex drug. We might fry her brain or something if we're not careful."
        scene w3_2236 with dissolve
        rose "That's not possible, right?"
        fel "Who the hell knows..."
        scene w3_2237 with dissolve
        rose "Go ahead, pick something..."
        ver "Unnngggh, f-fuck I'm burning up..."
        scene w3_2238 with dissolve
        fel "Oh no. You think you'll be able to just stand around and not get your hands dirty, don't you?"
        scene w3_2239 with dissolve
        rose "N-no! It's just... I've never done anything like this before. I know you have, right?"
        scene w3_2240 with dissolve
        fel "Why the fuck would you think that?"
        scene w3_2241 with dissolve
        rose "Well... you know... you're kinda... um... n-nothing."
        scene w3_2242 with dissolve
        fel "......"

        if rosalindFelSolution == True:
            scene w3_2243 with dissolve
            fel "You make it a habit of pushing your problems on other people, don't you?"
            rose "What are you talking about?"
            scene w3_2244 with dissolve
            fel "I'm talking about [mcf] and the 5000 dollars I-- ah, whatever."
            scene w3_2245 with dissolve
        else:
            fel "..."
            scene w3_2246 with dissolve

        fel "Point is, you're going to help."
        scene w3_2247 with dissolve
        fel "I have a preeetty good idea what will make her cum unrelentingly, buuuut... you'll take the other end."
        rose "...sure. I have some ideas too."
        fel "I knew you did, you sneaky bitch."
        rose "Fuck you, Felicia."
        scene w3_2277 with pixellate
        kat "Ha! By the end of this week, I will have these bitches hating each other."
        scene w3_2278 with dissolve
        sophia "Did you get the dosage right? The redhead only seems mildly affected."
        mct "(You call that mild?!)"
        kat "Of course, I did. Veronica's just got a stiff upper lip."

    if w2ExLoserDuo == True:
        scene w3_2248 with pixellate
        ver "Hnnng, hhhhaaa..."
        scene w3_2249 with dissolve
        fel "C-can you get me some water, Rosie? Please?"
        scene w3_2250 with dissolve
        rose "Mrs. Pulman said not to start for ten minutes."
        scene w3_2251 with dissolve
        fel "It's been ten minutes!"
        scene w3_2250 with dissolve
        rose "Has it?"
        scene w3_2252 with dissolve
        fel "Y-yes! S-stop twiddling your thumbs and begin!"
        fel "This s-shit she gave us is making me... uugghh..."
        scene w3_2253 with dissolve
        ver "I a-agree with Blondie. Let's get this going...!"
        scene w3_2254 with dissolve
        rose "Okay..."
        scene w3_2255 with dissolve
        rose "What should I use?"
        scene w3_2256 with dissolve
        fel "Huuhgg, like I know!"
        scene w3_2257 with dissolve
        rose "All she said was to punish you and make it look good... ugh..."
        scene w3_2258 with dissolve
        ver "U-use what's on the table... g-grab one of those dildos or something!"
        scene w3_2259 with dissolve
        rose "...would that be enough?"
        scene w3_2260 with dissolve
        ver "P-probably!"
        fel "What the hell do you mean would that be--"
        scene w3_2261 with dissolve
        rose "I mean... I gotta do a good job, right? I need to... get creative."
        scene w3_2262 with dissolve
        ver "Ah- ha... y-yeah, I suppose she expects you to... gg-gah... damn it, my shoulders hurt. Just get started! Please, Rosie?"
        scene w3_2263 with dissolve
        rose "......"
        rose "..."
        rose "Don't bear a grudge over this, okay?"
        scene w3_2279 with pixellate
        kat "Ha! By the end of this week, I will have these bitches hating each other."
        scene w3_2280 with dissolve
        sophia "The blonde seems abnormally thirsty and the redhead only mildly affected."
        mct "(You call that mild?!)"
        sophia "Did you get the dosage right?"
        kat "Of course, I did. She's just got a stiff upper lip."

    if w2ExLosersAll == True:
        scene w3_2264 with pixellate
        rose "Hhhngg..."
        scene w3_2265 with dissolve
        fel "A-ah, fuck I'm thirsty... this stuff is making me... unngg..."
        fel "Why the fuck are you just standing there, staring like some perverted cunt?!"
        scene w3_2266 with dissolve
        ver "Because I'm... a-ah..."
        scene w3_2267 with dissolve
        ver "She gave that shit to all of us! Just standing here, I feel like my head's about to melt!"
        scene w3_2268 with dissolve
        fel "It's b-better than being locked into this thing! F-fucking...!"
        scene w3_2269 with dissolve
        ver "It's not my fault you drew the short straws! But, honestly, I'd rather be where you are than have to..."
        rose "...h-have to what?"
        scene w3_2270 with dissolve
        ver "...h-have to control my urges! That old bitch said to put on a good show and punish you... and the fucking worst thing is..."
        scene w3_2271 with dissolve
        ver "That sounds like SUCH a good idea right now! I'm so fuckin' horny... I just want t--"
        rose "A-hhn, hggg... wh-what?!"
        scene w3_2272 with dissolve
        ver "You two are gorgeous... no shit, but I've thought that... like always...? Ah... what am I saying...?"
        ver "Even Felicia, even though I think you're a dumb bitch for signing up for this, I can't deny that you're..."
        scene w3_2273 with dissolve
        fel "Oh, god damn it. Just do something! I feel like all the moisture in my body is oozing out my cunt!"
        scene w3_2274 with dissolve
        rose "Y-yeah... uh... I mean... go e-easy on us, but... you gotta do something, right?"
        rose "She said to start in ten minutes and, I... uh... it's been more than that, right?"
        scene w3_2275 with dissolve
        ver "I don't know... I have no concept of time right now. I guess so?"
        ver "So... there's a lot of stuff on here."
        ver "What should I..."
        scene w3_2281 with pixellate
        kat "Ha! By the end of this week, I will have these bitches hating each other."
        scene w3_2282 with dissolve
        sophia "The redhead seems particularly affected."
        kat "Deep down, she's a big pervert... but now a pervert with much less inhibition in the tank, two juicy slabs of meat at her fingertips, and a good excuse."


    "Like before, Mrs. Pulman was once again pitting the Carnations against each other... in one sense, I found this was directionless and crude, but the more affected part of me..."
    mct "(...\"feel a greater responsibility and animosity for what transpires\", huh?)"
    "--found it dramatic and compelling. The three were already separated by their status as competitors, but now she sought to drive an even greater wedge between them."

    if w2KatBottom == True or w2KatTop == True or w1GonzoReward == True:
        hide screen textbox2 with dissolve
        scene br_katrub_a with dissolve
        show br_katrub with dissolve
        kat "Anticipating the show, [mcf]?"
        mc "What are you...?"
        "The old woman's palm played across the length of my package with a fervor that rivaled even the most drunken letch."
        kat "Or did shocking the girls get you {i}this{/i} hot and bothered?"
        mc "Uunng... d-don't fuck with me."
        "Actually... come to think of it, why doesn't that foul perfume affect either of them? I know for a fact it affects women..."
        "The Carnations were proof enough of that. Was it as simple as them being used to it? Maybe even inoculated against it...?"
        mc "Hnngg..."

        if kat_polite == True:
            "...how did I even know it wasn't affecting Mrs. Pulman? After all, her hand was currently rubbing my cock."
        else:
            "...how did I even know it wasn't affecting Kathleen? After all, her hand was currently rubbing my cock."

        "...but that was kinda in character for her, wasn't it?"

        scene w3_2283 with dissolve
        sophia "...eh? {b}Heh.{/b}"
        scene w3_2284 with dissolve
        sophia "Him, I could understand, but you..."
        scene w3_2285 with dissolve
        kat "{i}Please{/i}, I've seen you in much worse states."
        scene w3_2284 with dissolve
        sophia "There's a fundamental difference."
        scene w3_2286 with dissolve
        kat "The difference is I'm my own woman, doing what I please and not what I'm told."
        scene w3_2287 with dissolve
        "Suddenly I thought... this might not even be about me, huh?"
        "Nevertheless, even just touching me over my pants offered a soothing proposition of release..."
        scene w3_2288 with dissolve
        mc "Hnnnggg..."
        "On top of it all, I was also getting extremely pissed..."
        "I felt the only reason she sent me to keep an eye on Sophia was to fuck with me. That was her very nature, to senselessly poke and prod."
        mc "I said, don't fuck with me, you stupid--"
        scene w3_2289 with dissolve
        kat "Oh! Looks like the girls are ready to begin!"
        scene w3_2303 with dissolve

        if kat_polite == True:
            "Mrs. Pulman's hand darted from my crotch and I felt an immediate and {b}massive{/b} pang of regret."
        else:
            "Kathleen's hand darted from my crotch and I felt an immediate and {b}massive{/b} pang of regret."

        menu:
            "Put her hand back where it belongs(w3HagHandie = True).":
                $ w3HagHandie = True
                scene w3_2304 with dissolve
                "By instinct, I roughly grabbed the old woman's wrist."
                scene w3_2305 with dissolve
                mc "Put your hand back."
                kat "Oh...?"
                "Turns out, my horniness outweighed my indignation at being chemically manipulated."
                scene w3_2306 with dissolve
                kat "My, my... you must really be hurt--"
                scene w3_2307 with dissolve
                mc "{b}Finish{/b} what you started."
                scene w3_2308 with dissolve
                kat "......"
                kat "..."
                scene w3_2309 with dissolve
                kat "Don't look at me. Watch {b}my{/b} show."
                scene w3_2310 with dissolve
                "Her fingers started moving and--"
                scene black with fade
                play sound "sound effects/zipper.wav"
                "*Ziiiiiiiiip*"

                if hanaGF == True:
                    "Although technically {i}inside the club{/i}, I knew Hana would balk if she saw this scene. Still... mitigating circumstances, right?"
                stop sound
            "Carry on, untouched.":

                scene w3_2311 with dissolve
                "Regret I would live with."
                "Somehow and someway, I fought against the violent urge to place the old hag's hand back on my dick."
                scene black with fade
                "Current plan: grit my teeth, sit here quietly, and then when it's all said and done... go jerk off in a stall or something."
                mct "(Yeah... solid plan...)"
    else:


        scene w3_2290 with dissolve
        kat "Anticipating the show, [mcf]?"
        mc "Ummm... h-huh?"
        scene w3_2291 with dissolve
        kat "Do I have to spell it out?"
        scene w3_2292 with dissolve
        "I knew what she meant."
        "Sophia knew what she meant too."
        "Both of them were acutely aware of the angry bulge in my pants before we even sat down and I felt zero shame about it."
        scene w3_2293 with dissolve
        kat "What do you think Sophie?"
        scene w3_2294 with dissolve
        "Hell, even if I was in my right mind right now, I still might not feel ashamed about it. By now, well... popping a boner in front of this stupid hag was pretty standard."
        scene w3_2293 with dissolve
        kat "Pretty impressive for a dim-looking guy, isn't it? You wanna see it up close?"
        scene w3_2295 with dissolve
        mc "Hnnng... don't fuck with me..."
        "Actually... come to think of it, why doesn't that foul perfume affect either of them? I know for a fact it affects women..."
        scene w3_2296 with dissolve
        sophia "Does he normally talk to you like that?"
        "The Carnations were proof enough of that, but neither of them seemed all that bothered. Did they hide it well?"
        scene w3_2297 with dissolve
        kat "I'll let it slide, considering the circumstances."
        scene w3_2298 with dissolve
        "Was it as simple as them being used to it? Maybe even inoculated against it...?"
        scene w3_2297 with dissolve
        kat "--seriously though, I could ask him to whip it out and he'd do it."
        scene w3_2299 with dissolve
        sophia "No, thank you. I'm not like you, Kathleen."
        scene w3_2300 with dissolve
        kat "Really? With what I've seen you do at the behest of Abel, all with a smile on your face, well..."
        kat "{b}Could've fooled me.{/b}"
        scene w3_2301 with dissolve
        sophia "There's a difference."
        scene w3_2300 with dissolve
        kat "The difference is I'm my own woman, doing what I please and not what I'm to-- oh!"
        scene w3_2302 with dissolve
        kat "Looks like it's getting started."

    kat "This should be good. Pay close attention, Mr. [mcl]."
    kat "This should be a good lesson for you."
    mc "What the hell are you...?"
    fel "You know what--"

    if w2ExLoserFelicia == True:
        play sound "sound effects/gulp.wav"
        scene w3_2312 with pixellate
        "*Glug, glug, guuuuuuuhg...!*"
        stop sound
        scene w3_2313 with dissolve
        fel "A-ah... shiiiiiit...! That's... {b}GOOD{/b}! So fucking... {b}hhhuuuaah{/b}...!"
        scene w3_2314 with dissolve
        ver "Huh... uh... want some more?"
        scene w3_2315 with dissolve
        fel "Hnnng... n-no. N-now my other end is {i}aching{/i} more than my... hhhnngg..."
        fel " C'mon... I've got places to be... s-so can we just get started doing whatever it is you bitches are going to do?"
        scene w3_2316 with dissolve
        ver "Hmm? You sure? There's two other bott--"
        scene w3_2317 with dissolve
        rose "{b}Sooooo{/b}.... I think I came up with the plan of attack..."
        scene w3_2318 with dissolve
        fel "Shit. Y-you're actually taking the initiative for once? Wow, {b}s-shocked{/b}!"
        scene w3_2319 with dissolve
        ver "What are you going to do with that?"
        scene w3_2320 with dissolve
        rose "Hold this, please."
        ver "...and do what with it?"
        rose "Just take it."
        scene w3_2321 with dissolve
        ver "Ooooookay."
        scene w3_2322 with dissolve
        rose "I... ah... huh..."
        rose "This is all new to me, so it might be a little clumsy, but..."
        scene w3_2323 with dissolve
        "*Chwup..."
        fel "Eh? What are you..."
        scene or_rosafel_kiss_a with dissolve
        show or_rosafel_kiss with dissolve
        fel "Mmmhh...!"
        ver "Whaa, huh?!"
        fel "Mmmmh, mmmhhh... mmmmhh...!"
        "The scene playing out on the television screen was..."
        "It was... it was..."
        "Kinda... uh..."
        mct "(Hnnng!!!!)"

        if w3HagHandie == True:
            scene br_haghandy_a with dissolve
            show br_haghandy with dissolve
            kat "Huh. I didn't expect that."
            "In my current over-cooked state, what was playing out on the television screen was a muddled mess of pixels that barely registered meaning to me."
            kat "Not a bad tactic, however~ mixing affection and punishment does funny things to a person's head."
            "No, in my current state, my mind was entirely consumed by the old woman's grip on my cock."
            mc "H-haahaa...!"
            kat "Doubt that's what the cow has in mind, though."
            sophia "Is that why you kissed the redhead the other night?"
            scene br_haghandy2_a with dissolve
            show br_haghandy2 with dissolve
            kat "Not at all. That was just the heat of the moment. Veronica really was beautiful, right then and there..."
            mc "G-gahh...!"
            "The pitiful noise of a rutting animal punctuated the women's conversation."
            kat "Sadly, that moment was quickly lost, and she's now back to being that contemptible creature on the screen. Beauty is fleeting, isn't it?"
            sophia "You have a {i}unique{/i} sense of aesthetics, Kathleen."
            kat "Well, what do you find hot, Miss Lundgren? I'm genuinely curious..."
            scene br_haghandy_a with dissolve
            show br_haghandy with dissolve
            mc "Huuuhghh...!"
            kat "What gets a woman like you going?"
            mc "H-huhh... ack...!"
            sophia "You ever give much thought to what makes your skin itch? I tend not to pontificate over my bodily responses."
            kat "Unlike me, you mean?"
            sophia "When I feel an itch, I simply scratch it."
            kat "We got that in common at least - {b}all three of us.{/b}"
            sophia "Stop distracting me. I'm trying to watch--"
        else:

            scene w3_2324 with dissolve
            kat "Huh. I didn't expect that."
            scene w3_2325 with dissolve
            "In my current over-cooked state, what was playing out on the television screen was a muddled mess of pixels that barely registered meaning to me."
            scene w3_2326 with dissolve
            kat "Not a bad tactic, however~ mixing affection and punishment does funny things to a human's head."
            kat "Doubt that's what the cow has in mind, though."
            scene w3_2327 with dissolve
            mc "She... ah... she definitely didn't."
            scene w3_2328 with dissolve
            sophia "Is that why you kissed the redhead the other night?"
            scene w3_2329 with dissolve
            kat "Not at all. That was just the heat of the moment. She really was beautiful right then and there..."
            scene w3_2326 with dissolve
            kat "Sadly, that moment was quickly lost, and she's now back to being that contemptible creature on the screen. Beauty is fleeting, isn't it??"
            scene w3_2328 with dissolve
            sophia "You have a {i}unique{/i} sense of aesthetics, Kathleen."
            scene w3_2329 with dissolve
            kat "Well, what do you find hot, Miss Lundgren? I'm genuinely curious... what gets a woman like you going?"
            scene w3_2328 with dissolve
            sophia "You ever give much thought to what makes your skin itch? I tend not to pontificate over my bodily responses."
            scene w3_2329 with dissolve
            kat "Unlike me, you mean?"
            scene w3_2330 with dissolve
            sophia "When I feel an itch, I simply scratch it."
            kat "Oh, lovely, at least we have that in common."
            sophia "Stop distracting me. I'm trying to watch--"

        scene or_rosafel_kiss_a with dissolve
        show or_rosafel_kiss with dissolve
        "*Cwhup, fhwhup, chuuup!*"
        "She was going for it."
        fel "Mmmh... mmmhhh..."
        "She was really, {b}really{/b} going for it."
        rose "*Chwup, fwhup...!* MMmhh--"
        scene w3_2331 with dissolve
        fel "Hnng, a-aaah...!"
        fel "W-wha was... hnnngg..."
        "Felicia and I both were in a fog; I could tell that much. Even a simple, if surprisingly passionate, kiss had upended all the sense in her head."
        scene w3_2332 with dissolve
        ver "What was that?"
        scene w3_2333 with dissolve
        rose "Well... ah... you should always begin the foreplay with a kiss, right? It's like a rule..."
        scene w3_2334 with dissolve
        fel "We're not making love you fat-tittied idiot! Hnngg... gah... even just that... I'm fucking burning up!"
        fel "Stuff that thing in my cunt already!"
        scene w3_2335 with dissolve
        rose "Sorry, Felicia. That's... NOT happening yet."
        scene w3_2336 with dissolve
        fel "...AND WHY THE HELL NOT?!"
        scene w3_2335 with dissolve
        rose "You know why, hun."
        scene w3_2336 with dissolve
        fel "S-so your plan is to just let me hang here?!"
        scene w3_2335 with dissolve
        rose "No... my plan is..."
        scene w3_2337 with dissolve
        play sound "sound effects/slap2.wav"
        play music "music/addict.ogg"
        scene w3_2338 with hpunch
        "*SWIIICK!*"
        fel "Hnnggg...! What the--"
        play sound "sound effects/slap1.wav"
        scene w3_2339 with hpunch
        "*THWAP!"
        fel "--t-he fuck!"
        scene w3_2340 with dissolve
        rose "I've always wondered just {i}how{/i} sensitive other girls are right here... I know what my girlfriends TOLD me, but it's hard to picture it without seeing it yourself..."
        rose "Me? I remember running around the school's track in my gym clothes made my chest feel so... uh... {b}yeah{/b}."
        scene w3_2341 with dissolve
        fel "What?! You're going to treat my tits like a guinea pig?!"
        scene w3_2342 with dissolve
        rose "I mean, it's not like I want to... it's part of the game."
        scene w3_2343 with dissolve
        fel "F-fine, whatever, just.... huuuunhh... give me some fucking r-relief from this, a-ahh...!"
        rose "Well, if you're anything like me..."

        if w3HagHandie == True:
            scene br_haghandy3_a with pixellate
            show br_haghandy3 with dissolve
            rose "...this might just make you faint."
            kat "I'm surprised you haven't soiled my hand yet."
            mc "Hnngg!"
            kat "I know one time won't suffice. You don't have to fear; I'll milk you as much as you require~"
            "At this point, a stiff breeze would have gotten me off, but for how slow it was, the old woman's technique was thorough and {i}immaculate{/i} in its consistency. She never slowed or sped up; she just jerked me like her wrist operated on a piston."
            mc "G-ahh, s-shut the fuck up and just k-keep--!"
            "The real magic lay in how she used her pinky, tracing its black nail up and down the underside of my shaft, never deviating a single millimeter from the same tract of overwrought nerve endings."
            kat "*Whisper* You should speak kindly to someone who's doing you a favor, [mcf]."
            mc "*Gulp* H-a, haa... favor...? Yeah right..."
            "It was like the words appeared on my lips without even being thought of. I said what I felt without control or filter."
            mc "T-take a seat and spin on it if you really want to do me a favor!"
            kat "You're adorable right now, you know that?"
            play sound "sound effects/lighter-flick.wav"
            fel "U-uh... W-WHAT THE HELL is that for?!"
            kat "Oh! Didn't expect that would even get used."
            stop sound
        else:
            scene w3_2344 with pixellate
            rose "...this might just make you faint."
            scene w3_2345 with dissolve
            kat "Well, well, well... this is taking an exciting turn."
            mc "Hhhngg... y-yeah..."
            scene w3_2346 with dissolve
            mct "(I couldn't argue against that...)"
            "With the way I counted it, I had a couple of options for managing my sickening arousal."
            "I could let my mind wander, try to think of something else... but invariably, my senses fell on the women next to me, to the curves of their busts and their waists..."
            scene w3_2347 with dissolve
            "These two women were so far above me... the old woman decades my senior. Sophia, a brilliant scientist... it was so easy to imagine the delight in grabbing one of them right now and just--"
            mct "(Y-yeah... no... I should focus on what's playing out in front of me...)"
            "The other option was to let Kathleen's game preoccupy my attention."
            scene w3_2348 with dissolve
            kat "A-aah..."
            mct "(...that's gotta be the best way of dealing with this, right?)"
            kat "Do you need to be excused, Mr. [mcl]? Perhaps you need to go to the bathroom?"
            scene w3_2349 with dissolve
            mc "N-no, I'm f-fine..."
            scene w3_2347 with dissolve
            "She teased me, and strangely, I felt an unusual rush of pride. Of course, it was irrational, but that would be akin to losing..."
            "Losing what and to who, I did not know... but my willpower... I was stronger than this..."
            mct "(I ain't a fucking animal... right?)"
            play sound "sound effects/lighter-flick.wav"
            scene w3_2350 with dissolve
            fel "U-uh... W-WHAT THE HELL is that for?!"
            kat "Oh! A {i}truly{/i} exciting turn."
            stop sound


        scene or_rosafire_a with pixellate
        show or_rosafire with dissolve
        fel "N-not funny, you fucking cunt!"
        rose "R-relax, stop wriggling around!"
        fel "Like hell I will! Get that thing away from me!"
        rose "Relax, Sweetie... I'm not planning on burning you... I'm just..."
        fel "Hnngg... g-gahh..."
        rose "I read about this sort of thing in a book."
        fel "G-gah, wh-what kinda fucking books do you read?!"
        scene w3_2351 with dissolve
        rose "Uh... it's something another mom recommended?"
        scene w3_2352 with dissolve
        fel "You're lying, you perverted cow! {b}Hnnngg--{/b} that's f-fucking hot!"
        scene w3_2353 with dissolve
        rose "Well, that IS the point, hun... but I'm not burning you am I?"
        scene w3_2354 with dissolve
        fel "H-huh...?! I g-guess not... it actually feels kinda... my s-skin is-- a-aahh...!"
        scene w3_2355 with dissolve
        rose "See, {b}trust me.{/b}"
        fel "Ahhhaaah, why does it feel like a massage? My head's all fuckin' hhngggg...!"
        rose "Ha, good... then I'm doing it right."
        scene w3_2356 with dissolve
        fel "Have you never done this before?!"
        rose "Oh, heavens no... I'm not a deviant like you. Like I said, I've only read about it..."
        scene w3_2357 with dissolve
        fel "W-well fuck you too, bitch!"
        scene w3_2358 with dissolve
        play sound "sound effects/slap3.wav"
        scene w3_2359 with hpunch
        "*Thwack!*"
        scene w3_2360 with dissolve
        rose "Don't be rude!"
        scene w3_2361 with dissolve
        fel "G-gah, w-what the fuck?! That... h-hnngg...! F-fuck me, why did I almost cum from that?"
        scene w3_2360 with dissolve
        rose "Because you're perverted."
        scene w3_2362 with dissolve
        ver "It's probably because of the drug..."
        scene w3_2363 with dissolve
        rose "Uh, sorry... I don't mean that... well, not all of it... there's a camera, so I must make it sound good too."
        scene w3_2364 with dissolve
        fel "B-bullshit... you're enjoying this..."
        scene w3_2365 with dissolve
        rose "Don't be rude."
        rose "Still... that felt more intense than the first time I slapped you, right?"
        scene w3_2366 with dissolve
        fel "Y-yeah...?"
        scene w3_2367 with dissolve
        rose "Good. It worked then."
        scene w3_2368 with dissolve
        fel "Gah, my head's all f-fucked right nooooow... mmmwww..."
        scene or_rfttease_a with dissolve
        show or_rfttease with dissolve
        fel "G-gah...?!"
        rose "You've got lovely skin, Felicia... I'm jealous of how evenly you tan."
        fel "N-not the time for a compliment y-you, a-hh, h-hey... Red... how about you stick that in my--"
        rose "{b}Not yet{/b}, please."
        ver "I wasn't planning on it. I'm actually curious to see where you're taking this..."
        fel "H-hatt, what are you... g-gah..."
        fel "H--haat, f-fhuck... every part of me is on fire and... hnngg... e-every time you touch it it's like my ah... I'm out of my body?"
        ver "You're more sadistic than you let on, huh?"
        rose "It's part of the game!"
        ver "You have a big smile on your face right now."
        rose "It's nothing like that. It's just nice to be on this side of things for a change...?"
        fel "Ha-hhaa, h-haaaat! Gah, s-stop blathering so much! I can't think!"
        ver "Awww, is Blondie frustrated she doesn't hold 100%% of the attention?"
        fel "G-ahh, why are you bitches getting so mean all of a sudden?! J-just... hng... m-make me feel good; I'm dying here!"
        scene w3_2369 with dissolve
        rose "Ask politely, please."
        scene w3_2370 with dissolve
        fel "Hhhngg... f-fuck no. I'm not begging you for a thing!"
        scene w3_2371 with dissolve
        rose "That kind of obstinacy is not really helping anything... you're sending some mixed messages here."
        rose "If you want something, you need to learn to ask. Even my daughter has more manners than you."
        scene w3_2372 with dissolve
        ver "Drink up, Blondie."
        fel "H-huh?"

        if w3HagHandie == True:
            scene br_haghandy3_a with pixellate
            show br_haghandy3 with dissolve
            ver "I said to drink up!"
            kat "It's always interesting when you give a woman like Rosalind the opportunity to blow off steam. They're so stressed, pent up, inhibited..."
            mc "H-haa..."
            kat "They don't show you their true colors as much as their whole color palette blends together in one fucked up mix."
            "Like hell my mind was registering any of her bullshit right now."
            scene w3_2373 with dissolve
            sophia "You counted on this kind of... {i}fervor{/i}?"
            scene w3_2374 with dissolve
            mc "H-a, hnnggaa..."
            "The inside of my head was mush right now. My capacity for language was utterly eroded."
            scene w3_2375 with dissolve
            kat "I've been doing this for a long time. Before the club, I had my {i}other{/i} enterprises."
            kat "I'm well acquainted with the peculiar ways people in desperate situations respond. In a way, it's a more potent means of control than any drug."
            scene w3_2376 with dissolve
            sophia "I'm actually impressed for once."
            scene w3_2377 with dissolve
            kat "You shouldn't be. I'm an amateur when compared to someone like your owner."
            kat "I think the way Van Doren has you under his thumb is much more impressive."
            scene w3_2376 with dissolve
            sophia "Thank you."
            scene w3_2377 with dissolve
            kat "You took that as a compliment?"
            scene w3_2376 with dissolve
            sophia "Of course I did. Abel only has the best things."
            scene w3_2378 with dissolve
            ver "Huh... that's an interesting direction..."
            scene w3_2379 with dissolve
            kat "Your self-awareness in your choice of words is commendable, dear."
            scene w3_2378 with dissolve
            ver "How are you...?"
        else:

            scene w3_2380 with dissolve
            ver "I said to drink up!"
            scene w3_2381 with dissolve
            kat "It's always interesting when you give a woman like Rosalind the opportunity to blow off steam. They're so stressed, pent up, inhibited..."
            kat "They don't show you their true colors as much as their whole color palette blends together in one fucked up mix."
            scene w3_2382 with dissolve
            "To my annoyance, whenever one of them spoke, my attention would turn back to just how fuckable the women next to me were. "
            scene w3_2383 with dissolve
            sophia "You counted on this kind of... {i}fervor{/i}?"
            scene w3_2382 with dissolve
            mct "(Christ, I want to make that mouthy hag choke on my dick until she passes out!)"
            "Intrusive thought upon intrusive thought flooded my head."
            scene w3_2384 with dissolve
            kat "I've been doing this for a long time. Before the club, I had my {i}other{/i} enterprises."
            kat "I'm well acquainted with the peculiar ways people in desperate situations respond. In a way, it's a more potent means of control than any drug."
            scene w3_2383 with dissolve
            sophia "I'm actually impressed for once."
            scene w3_2385 with dissolve
            kat "You shouldn't be. I'm an amateur when compared to someone like your Master."
            kat "I think the way Van Doren has you under his thumb is much more impressive."
            scene w3_2386 with dissolve
            sophia "Thank you."
            scene w3_2387 with dissolve
            kat "You took that as a compliment?"
            scene w3_2386 with dissolve
            sophia "Of course I did. Abel only has the best things."
            scene w3_2388 with dissolve
            ver "Huh... that's an interesting direction..."
            scene w3_2387 with dissolve
            kat "Your self-awareness in your choice of words is commendable, dear."
            scene w3_2388 with dissolve
            ver "How are you...?"

        scene w3_2389 with pixellate
        fel "G-gah, you read about this in a book too?!"
        rose "Not {i}quite{/i}... how does it feel?"
        fel "Hnngg... what do you mean how does it feel? It's like- It's like I'm getting my tits sucked on by a glass cup!"
        scene w3_2390 with dissolve
        fel "Gh-"
        scene w3_2391 with dissolve
        rose "How about now?"
        fel "Hhhn, s-shitt...!"
        rose "Not quite the reaction I was looking for, but I guess it has just been a couple of pumps..."
        scene w3_2392 with dissolve
        fel "Hhhhhhaaaaaa! Gh, haaa--! You c-cunt!"
        scene w3_2393 with dissolve
        rose "How many times do I have to ask you not to be rude?"
        scene w3_2394 with dissolve
        fel "Ga-, ggaaaah... ggaaahh...!"
        "The impact of the fourth pump was quite dramatic. Felicia's eyes rolled into the back of her head and she howled like a dying animal."
        scene w3_2395 with dissolve
        rose "I bet that feels heavy, like nursing a baby?"
        scene w3_2396 with dissolve
        ver "More like nursing a vacuum cleaner..."
        fel "G-ggaaah... it's pulling my nipples off!"
        scene w3_2397 with dissolve
        rose "Oh, come on, don't be dramatic."
        fel "H, haaaahht.. they're going to come off! They're coming off!"
        ver "Yeah, seriously, don't be so dramatic."
        scene w3_2398 with dissolve
        rose "Hang in there."
        scene w3_2399 with dissolve
        "With that particular choice of words, the two retreated back to let Felicia fight against the unyielding suck of the two pumps dangling off her chest in an unwinnable battle of time."
        fel "Hnnng, gaaahh...! Shit, shit, shit, shit, shit...!"
        "The longer she hung there, with the breast pumps dangling from her chest, the more desperate she sounded."
        scene w3_2400 with dissolve
        "It didn't take very long, maybe just two or three minutes, before the signs of defeat were plastered on her face."
        fel "Can't think...! It's alallllglhhhh...!"
        scene w3_2401 with dissolve
        fel "Gahhahaha, hggnnnggaaaa...! I'm ddddyyingg, my tits areee..."
        fel "I'm! I'm! I'm! I'm! I'm! I'm! I'm! CHwwwuummingngg!"
        scene w3_2402 with dissolve
        fel "*Hwugfff... hwhuuff... *Wheeeze* Hnnggaa..."
        "The unceasing suction brought Felicia to the brink in a snap instant."
        scene w3_2403 with dissolve
        ver "Holy shit. Did she just...?"
        rose "Woah..."
        ver "I think you broke her."
        scene w3_2404 with dissolve
        fel "Hngg, ahh... sgwwhohoo sshlloohpy, shwwaahh..."
        rose "I didn't think her reaction would be that extreme..."
        fel "Hnnggg... givehh mee... shhovovee it in mee..."
        scene w3_2405 with dissolve
        rose "Oh dear... I didn't realize it was that extreme."
        rose "Go ahead and give her what she wants, please."
        scene w3_2406 with dissolve
        ver "Hmm... not yet. She's still got one more water bottle left."

        if w3HagHandie == True:
            scene w3_2407 with pixellate
            kat "I'm starting to get offended, Mr. [mcl]. Does my hand not suffice?"
            kat "Don't you want to taste release?"
            scene w3_2408 with dissolve
            mc "G-gah, f-fuck! It's not like I have any control over it!"
            sophia "Hmm..."
            scene w3_2409 with dissolve
            "Every fiber of my being desperately anticipated climax. My reason had been eroded and my purpose replaced by the critical need to expunge every trace of nauseating desire from my body through my cock."
            "The hairs on my arm stood on end, the feeling in my extremities came and went like the tide, and a pervasive tingling feeling floated from my neck down to my tailbone - by all means, my body told me that I {b}should{/b} be coming."
            scene w3_2410 with dissolve
            sophia "Interesting."
            scene w3_2409 with dissolve
            "But I wasn't. My bloated dick burned against the soft palm of the old woman's hand, pulsating and twitching from the ceaseless stimulation, filling me with the irrational fear that I might literally explode if I didn't soon go careening into the void of sexual release."
            scene w3_2411 with dissolve
            sophia "All things considered, he is showing a {b}surprising{/b} degree of longevity..."
            scene w3_2412 with dissolve
            kat "Maybe your fragrance isn't as effective as you think it is."
            mc "G-gaahh!"
            scene w3_2411 with dissolve
            sophia "Maybe..."
            scene w3_2413 with dissolve
            mct "(No! It was definitely fucking effective!)"
            sophia "...but unlikely. Hey, [mcf]..."
            scene w3_2414 with dissolve
            "Through lidded eyes, I could sense the blonde scooching closer and closer."
            scene w3_2415 with dissolve
            sophia "The issue is that a young, well-traveled guy like you simply can't get off on an old woman's touch, right?"
            scene w3_2416 with dissolve
            mc "That's not--"
            scene w3_2417 with dissolve
            sophia "{b}{i}Isn't it?{/b}{/i}"
            "Even in my lust-addled state..."
            scene w3_2418 with dissolve
            "My brain registered amazement over the willful way Sophia flipped the switch, going from detached aloofness to a man-killer just as easily as one would shed their clothes. "
            scene w3_2419 with dissolve
            mc "Hnngg...!"
            kat "*Scoff* Feeling left out, were you?"
            sophia "Give them a comparison."
            scene w3_2420 with dissolve
            "My hand responded independently, sinking into the pleasant give of the doctor's tit-flesh in an instant as what remained of my faculties disappeared into the whirlpool of her eyes."
            sophia "You got a mess lurking somewhere in there that you want to get out?"
            mc "Ha... hnngg...! F-fuck it!"
            scene w3_2421 with dissolve
            sophia "...?!"
            "I kissed her, just as you'd expect a man on the brink of starvation to steal a loaf of bread."
            scene br_hhplus_a with dissolve
            show br_hhplus with dissolve
            sophia "Mmmhhhh....!"

            if kat_polite == True:
                "She might not have expected it or even wanted it, but she quickly accepted it as a consequence of the \"just a bit of chaos\" she wielded in her joust against Mrs. Pulman."
            else:
                "She might not have expected it or even wanted it, but she quickly accepted it as a consequence of the \"just a bit of chaos\" she wielded in her joust against Kathleen."

            kat "H-hey, ahh--"
            "Spurred on by having the attention of two beautiful women, even if it was just the fucked up equivalent of cooking ants with a magnifying glass to them, I knew it wouldn't be long until I finally had my release."
            kat "Gah, ah... ha... hmpfh."
            "Although I could feel her eyes on my neck, the old woman continued to milk me."
            "*Cwhup, fwhup, chwup...!*"
            kat "I've somehow ended up feeling like a third wheel."
            "I pawed at both women's breasts with a virgin-like fervor, wholly enamored by an opportunity I might never get again."
            mct "(The head of a charity and a world-class scientist... ha, fucking sluts!)"
            "I felt like a king, not of my own making of course, but my brain was so cooked as to not know the difference. Thinking was hard, but what few thoughts I could miraculously formulate were like tidal waves breaking against the shore."
            mct "(Who the hell do you think you're fucking with? You think you can toy with me just because of money?!)"
            "I felt smothered, suffocated, and hot. More akin to a wick that was about to burn out than a human being."
            mct "(I'M A GUINEA PIG TO YOU?!)"
            "Every sensation felt heightened, and every second felt prolonged... I genuinely feared that the moment I popped would be when I was snuffed out."

            mct "{size=+30}{font=/gui/fonts/MB-Thin_Worms.ttf}(You like to toy with pe-){/font}{/size}"


            "My brain gave out, but if I ceased to exist after this, I instinctively knew one thing: these last minutes of my life should be bold."

            menu:
                "Goad the old woman into letting you finish in her mouth.(w3KatPromoFinish = True)"(chg=["kathleen_trust_up"]):
                    $ w3KatPromoFinish = True
                    $ Kathleen_Trust += 1
                    scene w3_2422 with dissolve
                    mc "I'm about to b-blow..."
                    kat "You don't need my permission."
                    scene w3_2423 with dissolve
                    mc "Can you finish me with your mouth?"
                    kat "Hmmmmm, not going to happen."
                    mc "A-ah, pretty please? With a cherry on top?"
                    scene w3_2424 with dissolve
                    kat "Why don't you ask Miss Lundgren to do it?"
                    mc "...because I want you, Ma'am."
                    scene w3_2425 with dissolve
                    kat "...hmmmmmmmm. You have the eyes of a crazed animal, yet..."
                    scene w3_2426 with dissolve
                    kat "You're asking so nicely. God, I love that."
                    scene w3_2427 with dissolve
                    "She smirked like she had won against me, and perhaps even against Sophia."
                    scene w3_2428 with dissolve
                    kat "It really is goddamn adorable. Ask me again, [mcf]."
                    scene w3_2429 with dissolve
                    "A desperate, cloying urge inside me told me her mouth was the only place I wanted to be right now and if it took a bit of pleading to get me into a position where I could fill that mean bitch's stomach with my seed, then so be it."
                    scene w3_2430 with dissolve
                    mc "Hhh, haa... would you PLEASE finish me with your mouth, Mrs. Pulman?"
                    scene w3_2431 with dissolve

                    if kat_polite == True:
                        "Without another word, Mrs. Pulman lowered herself and..."
                    else:
                        "Without another word, Kathleen lowered herself and..."

                    scene br_hhplus_hbj_a with dissolve
                    mc "G-gah...!"
                    "The moment her lips wrapped themselves around my cock, I felt like I might pass out."
                    "Her seal was so airtight that her mouth felt like an oven. Steady puffs of hot breath passed over the head of my cock as it made its way out through her nose."
                    scene br_hhplus_hbj_a with dissolve
                    show br_hhplus_hbj with dissolve
                    mc "F-fuck, damn it!"
                    "*Shwuck, fgwhhuck, thwuuuck!*"
                    "What little air could escape from her lungs transformed into {b}obscene{/b} noises as she inched herself up and down my shaft."
                    mc "H-holy-!"
                    "The running narration in my head was a jumbled mess, but through all the muddied noise from the pleasure soaking into my brain, I grasped a simple truth."
                    mc "Hnnng, you've sucked a lot of cock in your time, haven't you?!"
                    "*Thwaahp, fwhap, swhhuck~!*"
                    "The answer to that question played across my glans every time I wedged myself comfortably in her throat with zero fuss."
                    "Swhuck, hhhwhuck, fhhggguuk!*"
                    "{b}Damn it!{/b} A rich woman like her had no business sucking dick this well."
                    mc "Ghhn, haaat, hnnngg...!"
                    "She sucked me with the skill of a woman who had {b}nothing{/b} to her name."
                    kat "Mmmhm, hhmhm~"
                    "Just like her hand job, there was no wasted effort. She didn't tackle it in a clumsy frenzy, nor did she need to cautiously get used to my size."
                    "*Shwhuhuck, fwhhucuk, ghhwhuhuk!*"
                    "She sucked me like she had been sucking {b}my{/b} dick her whole life, pleasuring me at a steady and comfortable pace. I marveled at how, through a mere blowjob, a woman so cold and cruel could instantly imprint herself on my body as warm and welcoming."
                    "I was quickly understanding that \"adorable\" disparity she had just spoken."
                    mc "Hnng, h-how?!"
                    sophia "It's not performing brain surgery."

                    if kat_polite == True:
                        "{b}There{/b} was another perverse delight, speeding me toward my climax. Sophia's attention was on the back of Mrs. Pulman's head, watching intently as she debased herself in pursuit of degrading me."
                    else:
                        "{b}There{/b} was another perverse delight, speeding me toward my climax. Sophia's attention was on the back of Kathleen's head, watching intently as she debased herself in pursuit of degrading me."

                    mct "(Haaaa... hope you like the show, bitch. You're the impetus for this.)"
                    "*Fwhhuck, ghhhukh, khggguuhhk*"
                    mc "Ahh... y-you dick swallowing--! Hnnngg...!"
                    "It was coming."
                    scene w3_2432 with dissolve
                    mc "You think I'm adorable?!"
                    "I was moments from blowing my load, and with it, the indignation from earlier swelled in me. I had wanted a bold finish before I met my end, and well..."
                    mct "(I'll show you adorable!)"
                    stop music
                    scene br_hhplus_gulp1_a with vpunch
                    mc "I'm c-cumming, fucking drown in it, you damn--"
                    play sound "sound effects/spurt.wav"
                    with flash
                    kat "Mmmmh?!"
                    "Before she could even register what was happening, ropes of piping hot cum barreled down her esophagus on a one-way trip to her stomach."
                    play ambient "sound effects/fel2.wav"
                    scene br_hhplus_gulp1_a with dissolve
                    show br_hhplus_gulp1 with dissolve
                    play sound "sound effects/spurt.wav"
                    with flash
                    kat "Ghhkka, hkkaa-!"
                    "I pressed down hard, holding the old woman's head in place as she gargled my seed in abject surprise."
                    mc "Hnngg, all of it!"
                    "I pressed down so hard it hurt my groin."
                    play sound "sound effects/spurt.wav"
                    with flash
                    kat "Ghhuk, hhuuuh, hwwwhuuuck...!"
                    "It was massive, like I was cumming my very soul down the old woman's throat."
                    kat "Ghuk, khak, uuhhk-!"
                    mc "Gah, c-choke on it!"
                    play sound "sound effects/spurt.wav"
                    with flash
                    "Not all of my load was making its way down her throat. To my perverse glee, I could {i}feel{/i} myself coating the lining of her throat."
                    kat "Ghhuk, hhuuuk...!"
                    scene br_hhplus_gulp2_a with flash
                    show br_hhplus_gulp2 with dissolve
                    play sound "sound effects/spurt.wav"
                    with flash
                    mc "Hope you like the fucking taste!"
                    kat "Mmmh, hhhngg?!?!"
                    sophia "I don't think she can breathe..."
                    mc "Good! She can breathe when I'm fucking--!"
                    stop ambient fadeout 4.0
                    play sound "sound effects/spurt.wav"
                    with flash
                    ".........!"
                    play sound "sound effects/spurt.wav"
                    with flash
                    "......!"
                    scene w3_2433 with dissolve
                    mc "A-aahh...!"
                    scene w3_2434 with dissolve
                    kat "Ugghhuhh..."
                    scene w3_2435 with dissolve
                    "Peace."
                    "Serenity."
                    "Satisfaction."
                    "In this moment, I had it all."
                    scene black with w20
                    "With that, I happily died. The oblivion I felt nipping at my heels finally sank its sharp teeth into my throat."
                    "............"
                    "........."
                    "......"
                    "..."
                    kat "Why are you holding your hands out like that? It's weird."
                    mct "(Ah, fuck... I {i}wasn't{/i} dead? {b}Oh no.{/b} Then that meant I just...)"
                    scene w3_2436 with w9
                    sophia "She's right. It's distracting."
                    scene w3_2437 with dissolve
                    "I didn't know how long I was out of it, but by the time I opened my eyes, the two women had collected themselves, and what I thought was a bold display of defiance was made pitiful and wholly expected by their bemused faces."

                    if kat_polite == True:
                        "Mrs. Pulman looked {i}totally{/i} unaffected by my rough treatment, showing no signs of having mercilessly guzzled my cum just moments ago..."
                    else:
                        "Kathleen looked {i}totally{/i} unaffected by my rough treatment, showing no signs of having mercilessly guzzled my cum just moments ago..."

                    scene w3_2438 with dissolve
                    kat "Oh, by the way... you said some pretty outlandish things to me."
                    scene w3_2439 with dissolve
                    mc "If I recall, I did more than that..."
                    scene w3_2440 with dissolve
                    kat "It was {b}adorable{/b}."
                    "She had indeed won."
                    fel "Gha--"
                "Leave an impression on the doctor.(w3SophiaPromoFinish = True)"(chg=["kathleen_down2"]):

                    $ w3SophiaPromoFinish = True
                    $ Kathleen_Affection -=2
                    "I knew what I wanted."
                    sophia "Mmmhh, hhhhh..."
                    "And that last act of defiance would be leaving the doctor, the root cause of all this, something to remember me by."
                    scene br_hhplus_doc1_a with dissolve
                    show br_hhplus_doc1 with dissolve
                    "*Chwup, fhwup~*"
                    "I wanted to hear this aloof bitch moan, so I focused everything on the woman whose mouth I was currently exploring."
                    sophia "Mmmh, hhmmm...?"
                    "It was a battle against my wits. Sophia was literally intoxicating. Focusing my senses all on her had me burning twice as fast."
                    "By instinct, I felt her breast over her clothes."
                    sophia "Mmhh..."
                    "Her coos told me she was receptive, but it wasn't quite the noise I wanted to drag out from the blonde."
                    scene br_hhplus_doc2_a with dissolve
                    show br_hhplus_doc2 with dissolve
                    sophia "Ghu, gha~ghhuu...!"
                    "Deciding that over the clothes touching wouldn't do it, I switched focus on the erogenous zone in her mouth, intensifying my efforts in an intricate dance to subdue her tongue with my own."
                    sophia "Mmmmh, mmhhhh- *chwuph, fhwhup~*"
                    "She wasn't a passive observer in my hunt; her tongue played coy, darting away and slipping from my grasp whenever I thought I had her pinned."
                    "It was mere seconds, but--"
                    "*Chwhu, fhwwwup, chup!*"
                    "--but, in my fogged-over state, time held little sway over my perception. What was in reality a clumsy tussle felt like a long and protracted siege."
                    "I don't know if it was because of the perfume, but all bodily sensations gradually began to meld into one."
                    "The feeling of the old woman's hand milking my cock, the wet warmness of our kiss, the bubbling desire so strong that I was confident it would be the end of me..."
                    mc "Mmmh, hhhmmm-!"
                    "All of it spelled an overload melded and combined into a singular feeling of otherness. I was sure I had lost this battle until..."
                    scene br_hhplus_doc3_a with dissolve
                    show br_hhplus_doc3 with dissolve
                    "My brain registered a change."
                    mct "Was she...?"
                    sophia "Mmmh, hhmhm~aahhh...!"
                    "She was closer."
                    "She was pressing into me."
                    "She felt it."
                    "She was {b}heated{/b}."
                    "{i}She was kissing me back.{/i}"
                    "Whether it was done deliberately or on an instinctual level, her body responded favorably."
                    sophia "Ahh, hhhnnggg, mmmmhh-!"
                    "My hand found a place on her ass and I used that to spur her on even more. With this, I had physical confirmation of my success."
                    mct "(Fuck, what a great-!)"
                    "I could feel the hot dampness of her delicate spot."
                    sophia "Mmhh, hhaa...♥♥♥"
                    "She purred openly and I felt a petty relief over my trivial victory. The succubus driving me to this desperate state wouldn't escape our battle unscathed."
                    "*Chwup, fhwwup, khwwup*!"
                    "--and that wasn't the only sense of relief I felt."
                    stop music
                    play sound "sound effects/spurt.wav"
                    scene w3_2441 with flash
                    mc "{b}Hnng, ah-!!!{/b}"
                    "I didn't know when it started, but ropes of cum geysered from my cock and rained down from the sky."
                    play sound "sound effects/spurt.wav"
                    scene w3_2442 with flash
                    mc "Ghh, aaahh- sssshit--"
                    kat "Huh, {b}WOW{/b}."
                    scene w3_2443 with dissolve
                    mc "Hngg, hhhhmmmhh-~"
                    "All the suffocating vileness in me was expelled and released into the world. All my desperation spilled out onto our clothes and thighs."
                    "Soon need was replaced with..."
                    scene w3_2444 with dissolve
                    "Peace."
                    "Serenity."
                    scene w3_2445 with dissolve
                    "Satisfaction."
                    "Emptiness."
                    "The oblivion I felt nipping at my heels finally sank its sharp teeth into my throat."
                    scene black with w20
                    "I was dead."
                    "............"
                    "........."
                    "......"
                    "..."
                    sophia "Great, now we'll spend the rest of the show reeking of semen."
                    mct "(Ah, fuck... I {i}wasn't{/i} dead? {b}Oh no.{/b} Then that meant I just...)"
                    scene w3_2446 with w9
                    kat "You should've thought of that before you entered the crossfire."
                    scene w3_2447 with dissolve
                    sophia "You were taking too long. I wanted to put an end to the distraction."
                    scene w3_2448 with dissolve
                    "I didn't know how long I was out of it. Still, by the time I opened my eyes, the two women had collected themselves. The damage I thought I had done to Sophia with my counter-attack was made pitiful by their bemused faces."
                    scene w3_2449 with dissolve
                    kat "Oh, please. Are those the kind of sounds you make matter-of-factly?"
                    scene w3_2450 with dissolve
                    "Sophia looked as composed as ever, and except for a little blush, her attention turned back to the Carnations."
                    scene w3_2451 with dissolve
                    kat "I hope that provided you a measure of relief, Mr. [mcl]. That certainly was an... {i}explosive{/i} finish."
                    mc "A, ahem... thaaaaaanks?"
                    scene w3_2452 with dissolve
                    kat "Don't mention it. It was... interesting."
                    fel "Gha--"
        else:

            scene w3_2453 with dissolve
            mc "........."
            mc "......"
            stop music
            play sound "sound effects/record-scratch.wav"
            scene w3_2454 with dissolve
            "...this was my limit."
            $ renpy.end_replay()
            scene w3_2455 with dissolve
            mc "Aaeeh, I'll be riiiiiight back."
            scene w3_2456 with dissolve
            "......"
            scene w3_2457 with dissolve
            "..."
            scene w3_2458 with dissolve
            kat "Is that a milder scent you are wearing?"
            sophia "It's the same batch as the bottle I gave you."
            scene w3_2459 with dissolve
            kat "The effect seemed... less? Why's that?"
            scene w3_2460 with dissolve
            sophia "It's possible that his body adapted and partially metabolized the odor molecules. All I can say is that it's remarkable he held out that long."
            sophia "It could be a matter of willpower."
            scene w3_2461 with dissolve
            kat "When I had dinner with Charles the other night, he didn't even flinch."
            scene w3_2462 with dissolve
            sophia "Dr. Kohler is a scary man."
            scene w3_2463 with dissolve
            kat "Is that your appraisal after demolishing him game after game?"
            scene w3_2464 with dissolve
            sophia "How else should I describe a man who has no need but keeps his passions tightly controlled."
            scene w3_2465 with dissolve
            kat "That's why he and I are incompatible. He treats fucking like it's Christmas."
            kat "You don't have anything to worry about as long as you don't lose."
            scene w3_2466 with dissolve
            sophia "I don't plan on it, but I have a feeling he eventually wins one way or another."
            scene w3_2459 with dissolve
            kat "Abel wouldn't let it come to that, would he?"
            scene w3_2467 with dissolve
            "......"
            "..."
            scene w3_2460 with dissolve
            sophia "Thank you for indulging my little whim, Kathleen. It was amusing."
            scene w3_2459 with dissolve
            kat "Don't mention it. One should make their own fun in life. Still..."
            kat "...you're very competent. Don't you ever desire more?"
            scene w3_2468 with dissolve
            sophia "A frivolous bitch like you has no business saying that to me."
            scene w3_2469 with dissolve
            kat "Ah, fuck. There it is."
            scene black with fade
            kat "I almost felt sorry for you."
            jump w3WashRoom

        play music "music/landing.ogg"
        scene w3_2470 with pixellate
        fel "--aaahhhhnn! It's t-to-tooooooo muuuuchh!"
        ver "C'mon, Blondie... A woman like you would be able to take as much."
        scene or_feldrip_a with dissolve
        show or_feldrip with dissolve
        fel "Gghh, hhhhhnnnggaaaaaawwwah! It's fucking strong!"
        mct "(Right, I was so caught up in my lust that I had forgotten that this was still happening...)"
        fel "Gh, hhnngg, hhnnngg...! Oh, hhhhnngngg...! N-no!"
        ver "Hmmm? This is what you asked for, isn't it?"
        fel "T-the vibe is m-moving the beads and m-making me wanna--"
        ver "Pee? Well, you did drink three water bottles..."
        rose "You planned this?"
        ver "Well, I had to pull my weight for this \"game\", right?"
        fel "It f-feels to-ttoooo good, but I d-don't w-wanna...!"
        ver "You don't want to piss yourself like an idiot in front of your future club members?"
        fel "Ghh, hh--"
        scene w3_2471 with dissolve
        ver "What an odd fucking line to draw, huh? You think volunteering for this gives you a veneer of dignity?"
        ver "Newsflash: sluts like you don't have any dignity."
        scene w3_2472 with dissolve
        rose "Eh, don't you think you're being too mean?"
        fel "Gghhh, f-hhh--"
        scene w3_2473 with dissolve
        ver "Mean? You and I are fighting for our futures, and she's just a bored rich bitch looking for a kick."
        ver "I'm just letting her know she isn't shit... for the purpose of the game, you know..."
        scene w3_2474 with dissolve
        rose "Right, yeah... the game."
        scene w3_2475 with dissolve
        fel "Why should I care about your sob stories? It d-doesn't matter who wins; it only matters if you lose!"
        fel "Do you think Rose will give a shit if you win over me? It's all the same to her as it would be to you!"
        scene w3_2476 with dissolve
        ver "Oh, yeah?"
        scene w3_2477 with dissolve
        fel "That's right! You should be happy to have a bored rich bitch as your opponent! Would you rather three desperate people get paraded like show dogs over two?! Why the hell are you even thinking about me?!"
        scene w3_2478 with dissolve
        fel "Focus on winning you--- gah, you're so fucking short-sight--"
        scene w3_2479 with dissolve
        fel "Gh, hhuhukhhh...?!"
        ver "Just shut up and piss yourself, you fucking cumrag."
        scene w3_2480 with dissolve
        fel "Mmmhhh, mmhmhh, hnnnggg!"
        ver "When you lose, you can go back to your damn penthouse! Take a dip in your pool! Eat your fancy grub!"
        scene w3_2481 with dissolve
        ver "A good price for your dignity, because I'm certainly selling mine for much less!"
        scene w3_2482 with dissolve
        ver "..."
        fel "Hnnngg, hhh--"
        scene w3_2483 with dissolve
        fel "Mmmhh, mmggmmhhh, hhhmmm--"
        rose "Hey..."
        scene w3_2484 with dissolve
        fel "UUUhh, hhhehhhh---"
        rose "You alright...?"
        scene w3_2485 with dissolve
        ver "Yeah, I'm fine, Rosie... I just thought being in the driver's seat would be more fun."
        scene w3_2486 with dissolve
        rose "That's what I mean; we all still have our dignity. None of this has--"
        scene w3_2487 with dissolve
        fel "Mmhmhwwahhahahh, ghhgaaa-a---hhhhhaaa"
        scene or_felpee_a with dissolve
        show or_felpee with dissolve
        ver "There she goes. Well..."
        fel "Hnnhhsshwwwiiiitt, n-nooohhh, fhhhkk---"
        ver "This {i}was{/i} kinda fun..."
        fel "Hnnggg..."
        rose "Better her than us, at least."
        "As things came to a close, I was left with a prickly thought."
        stop music fadeout 3.0
        scene black with fade
        "That was as honest as they had ever been with each other."
        jump w3WashRoom


    if w2ExLoserVeronica == True:
        scene w3_2488 with pixellate
        fel "It's kinda obvious, but you don't really like me, do you?"
        scene w3_2489 with dissolve
        ver "What the f-fuck does that matter, Blondie?"
        scene w3_2490 with dissolve
        fel "It matters because you're the one tied up right now."
        ver "Hnnng... I like you just fine?"
        scene w3_2491 with dissolve
        fel "No, you don't, Red. You've never hidden it before, don't try and hide the truth now just because you're in the palm of who's asking."
        fel "It's out of character."
        scene w3_2492 with dissolve
        ver "Again, w-what does it matter? Just hurry up and get rolling!"
        scene w3_2493 with dissolve
        fel "I know you think I'm frivolous and undeserving - and that's okay; I get where you're coming from."
        scene w3_2494 with dissolve
        ver "Oh, just shut up! If you don't start, how about you just kill me?"
        scene w3_2495 with dissolve
        ver "How about you, Rosie? Will you p-put me out of my m-misery here?"
        scene w3_2496 with dissolve
        rose "Heh, I'd like to start, but uh... she's got the lead right now. I wouldn't want to interrupt and be rude."
        scene w3_2493 with dissolve
        fel "I'm going to be nice to you, Red. I'm going to treat you how I'd like to be treated."
        fel "I know you don't care about this either, but I like you. I really do."
        scene w3_2497 with dissolve
        ver "Yeah, riiiiiight..."
        scene w3_2498 with dissolve
        fel "Oh, c'mon. I've caught you stealing glances before."
        fel "I'm used to people looking down on me and I'm also used to those same people wanting to fuck me."
        scene w3_2499 with dissolve
        fel "{b}You{/b} want to fuck me, Red. Admit it."
        scene w3_2500 with dissolve
        ver "G-gah, you're fucking full of yourself!"
        scene w3_2501 with dissolve
        ver "Mmmh, hhmmmm?!"
        "Felicia, as if on cue, kissed Veronica's neck. Nothing exaggerated, just something..."
        scene w3_2502 with dissolve
        ver "Mmmmhn, mmmhh...!"
        "Just something to make her point."
        scene w3_2503 with dissolve
        fel "You're about to be full of something too."
        scene w3_2504 with dissolve
        ver "W-what are you...? Ah, f-f--"
        fel "Just sit back and enjoy. Don't go anywhere."
        scene w3_2505 with dissolve
        fel "Oh, by the way... you have [mcf] to thank for this part. He taught me just how effective these little devils are."

        if w2FeliciaPacked ==True:
            fel "For the record, I managed four of these."
        else:
            fel "For the record, I managed three of these."

        if w3HagHandie == True:
            scene br_haghandy_a with dissolve
            show br_haghandy with dissolve
            kat "Oh, aren't you proud, Mr. [mcl]? It sounds like you left an impression on the girl."
            "In my current over-cooked state, what was playing out on the television screen was a muddled mess of pixels that barely registered meaning to me."
            kat "Although, honestly... I bet our slut wife friend could've handled five."
            "No, in my current state, my mind was completely consumed by the old woman's grip on my cock."
            mc "H-haahaa...!"
            kat "Still, all this talk about being nice. Did she forget this is supposed to be a punishment?"
            sophia "You know very well it can be both. You're the one who arranged the tools."
            scene br_haghandy2_a with dissolve
            show br_haghandy2 with dissolve
            kat "You're right... it might feel good, but she will resent being at their mercy. She's too pathetically predictable."
            mc "G-gahh...!"
            "The pitiful noise of a rutting animal punctuated the women's conversation."
            kat "...ah, I love it! I really do love Miss Lynch. I wish I had more than a month with her."
            sophia "You have a {i}unique{/i} sense of aesthetics, Kathleen."
            kat "Well, what do you find hot, Miss Lundgren? I'm genuinely curious..."
            scene br_haghandy_a with dissolve
            show br_haghandy with dissolve
            mc "Huuuhghh...!"
            kat "What gets a woman like you going?"
            mc "H-huhh... ack...!"
            sophia "You ever give much thought to what makes your skin itch? I tend not to pontificate over my bodily responses."
            kat "Unlike me, you mean?"
            sophia "When I feel an itch, I simply scratch it."
            kat "We got that in common at least - {b}all three of us.{/b}"
            sophia "Stop distracting me. I'm trying to watch--"
        else:

            scene w3_2324 with dissolve
            kat "Oh, aren't you proud, Mr. [mcl]? It sounds like you left an impression on the girl."
            scene w3_2325 with dissolve
            "In my current over-cooked state, what was playing out on the television screen was a muddled mess of pixels that barely registered meaning to me."
            scene w3_2326 with dissolve
            kat "Although, honestly... I bet our slut wife friend could've handled five."
            kat "Still, all this talk about being nice. Did she forget this is supposed to be a punishment?"
            scene w3_2327 with dissolve
            mc "She... ah..."
            scene w3_2328 with dissolve
            sophia "You know very well it can be both. You're the one who arranged the tools."
            scene w3_2329 with dissolve
            kat "You're right... it might feel good, but she will resent being at their mercy. She's too pathetically predictable."
            scene w3_2326 with dissolve
            kat "...ah, I love it! I really do love Miss Lynch. I wish I had more than a month with her."
            scene w3_2328 with dissolve
            sophia "You have a {i}unique{/i} sense of aesthetics, Kathleen."
            scene w3_2329 with dissolve
            kat "Well, what do you find hot, Miss Lundgren? I'm genuinely curious... what gets a woman like you going?"
            scene w3_2328 with dissolve
            sophia "You ever give much thought to what makes your skin itch? I tend not to pontificate over my bodily responses."
            scene w3_2329 with dissolve
            kat "Unlike me, you mean?"
            scene w3_2330 with dissolve
            sophia "When I feel an itch, I simply scratch it."
            kat "Oh, lovely, at least we have that in common."
            sophia "Stop distracting me. I'm trying to watch--"

        play music "music/addict.ogg"
        scene w3_2506 with pixellate
        play sound "sound effects/vib-start.wav"
        fel "...and THREE!"
        $ renpy.music.set_volume(.4, 0, channel = "ambient")
        play ambient "sound effects/vib-ongoing.wav"
        scene w3_2507 with dissolve
        fel "You had no trouble whatsoever. They just slid right in there!"
        ver "N-no shit, I'm fucking drippi-- gaaah, whwahaaha!"
        scene w3_2508 with dissolve
        fel "Yeah, I know. [mcf] had a whole remote, but I don't. So you're just going to have to deal with \"on\" for as long as they're in you."
        ver "Hnnngg hhhaaaaa..."
        scene w3_2509 with dissolve
        fel "Now, I said I would be nice, but there's two of us - and Rosie isn't as sweet as she pretends to be, are you beautiful?"
        $ renpy.music.set_volume(.2, 0, channel = "ambient")
        scene w3_2510 with dissolve
        rose "Ah... don't blame me... one of us has to be the bad cop..."
        scene w3_2511 with dissolve
        rose "It's part of the game, right?"
        ver "Ghh, hhhngngg--"
        scene w3_2512 with dissolve
        fel "That's not very convincing when you're smiling, Rosie. It's nice having the shoe on the other foot?"
        scene w3_2513 with dissolve
        rose "Not at all..."
        scene w3_2514 with dissolve
        fel "Would you rather switch places?"
        rose "I... uh... didn't say that either."
        scene w3_2515 with dissolve
        fel "Might as well enjoy it then. There's no need for pretenses between us."
        scene w3_2516 with dissolve
        fel "Let your mask come off."
        rose "T-tha, aahh... w-why are you?"
        scene w3_2517 with dissolve
        fel "Oh, right. Your tits are like mega-sensitive."
        scene w3_2518 with dissolve
        fel "My bad. Don't want to undermine your part here. What do you got cooking?"
        scene w3_2519 with dissolve
        rose "Well, uhhh... I just thought about what might work on me and... that position you're in, with your chest out... I just know that I would..."
        rose "It's better if I just show you."
        scene w3_2520 with dissolve
        fel "Well, whatever. Remember, you get the front, I got the back. We're going to two team this slut."
        fel "Get ready to have your mind melted, Red!"
        scene w3_2521 with dissolve
        ver "Ghh... hnnanaa, I'm already m-melting, you--"
        scene w3_2522 with dissolve
        ver "G-gahhh, your tongue's not going to--"


        if w3HagHandie == True:
            stop ambient
            scene br_haghandy3_a with pixellate
            show br_haghandy3 with dissolve
            ver "...fiiiiiiiiIIITIiiitttttthhh--!!!"
            kat "I'm surprised you haven't soiled my hand yet."
            mc "Hnngg!"
            kat "I know one time won't suffice. You don't have to fear; I'll milk you as much as you require~"
            "At this point, a stiff breeze would have gotten me off, but for how slow it was, the old woman's technique was thorough and {i}immaculate{/i} in its consistency. She never slowed down or sped up; she just jerked me like her wrist operated on a piston."
            mc "G-ahh, s-shut the fuck up and just k-keep--!"
            "The real magic lay in how she used her pinky, tracing its black nail up and down the underside of my shaft, never deviating a single millimeter from the same tract of overwrought nerve endings."
            kat "*Whisper* You should speak kindly to someone doing you a favor, [mcf]."
            mc "*Gulp* H-a, haa... favor...? Yeah right..."
            "It was like the words apparated on my lips without even being thought of. I said what I felt without control or filter."
            mc "T-take a sit and spin on it if you really want to do me a favor!"
            kat "You're adorable right now, you know that?"
            ver "G-uhaaah, y-you're pullingtheeehhmopffhh---!"
            kat "Oh! Look at them stretch!"
        else:

            stop ambient
            scene w3_2344 with pixellate
            ver "...fiiiiiiiiIIITIiiitttttthhh--!!!"
            scene w3_2345 with dissolve
            kat "Well, well, well... this is taking an interesting turn."
            kat "Oh, how I wish there were two of me."
            mc "Hhhngg... y-yeah..."
            scene w3_2346 with dissolve
            mct "(I couldn't argue against that...)"
            "With the way I counted it, I had a couple of options for managing my sickening arousal."
            "I could let my mind wander, try to think of something else... but invariably, my senses fell on the women next to me, to the curves of their busts and their waists..."
            scene w3_2347 with dissolve
            "These two women were so far above me... the old woman decades my senior. Sophia, a brilliant scientist... it was so easy to imagine the delight in grabbing one of them right now and just--"
            mct "(Y-yeah... no... I should focus on what's playing out in front of me...)"
            "The other option was to let Kathleen's game preoccupy my attention."
            scene w3_2348 with dissolve
            kat "A-aah..."
            mct "(...that's gotta be the best way of dealing with this, right?"
            kat "Do you need to be excused, Mr. [mcl]? Perhaps you need to go to the bathroom?"
            scene w3_2349 with dissolve
            mc "N-no, I'm f-fine..."
            scene w3_2347 with dissolve
            "She teased me, and strangely, I felt an unusual rush of pride. Of course, it was irrational, but that would be akin to losing..."
            "Losing what and to who, I did not know... but my willpower... I was stronger than this..."
            mct "(I ain't a fucking animal... right?)"
            scene w3_2350 with dissolve
            ver "G-uhaaah, y-you're pullingtheeehhmopffhh---!"
            kat "Oh! Look at them stretch!"

        scene or_onvero1_a with pixellate
        show or_onvero1 with dissolve
        "Back on screen, they were indeed doubling up on poor Veronica."
        ver "MMmh, hhhhhmm-!"
        "Felicia explored the Amazon's business end with her tongue, while Rosalind frenched the redheaded woman and roughly tugged at her nipples."
        ver "Ha, mmmwwwhaa~♥"
        "It wasn't what came to mind when I pictured \"bad cop\", but it wrenched muffled cries from Veronica's throat."
        ver "*Chwu, fwwhhup-!* Wwwhhaaauh-!"
        "Attacked on both ends, with Dr. Lundgren's poison coursing through her veins, she had little choice but to moan, jerk, and writhe as her brain was inundated with more endorphins than it knew what to do with."
        scene or_onvero2_a with dissolve
        show or_onvero2 with dissolve
        "*Chwup, fhwup, khhwwup-!*"
        ver "Mmmhh...♥ Hnn...♥"
        "As the pair persisted, the sweet sounds of lust pouring out from the tv's speakers became more agreeable and proactive."
        ver "Ghh, hhhaaa...♥♥ Mmmmhh...♥♥♥"
        "She was into it."
        ver "Hhhhyyeah, hhhhh-♥♥♥"
        "She was {i}definitely{/i} into it."
        "*Chwaup, fhhwwup!*"
        "The only distinction to be made lay in whether it was done for the camera's benefit or to egg the sources of her pleasure on."
        mct "(G-ahh...!)"
        "What was certain was that the unrestrained sounds of the physically restrained Amazon poured fuel on my already out-of-control lust."
        scene or_onvero1_a with dissolve
        show or_onvero1 with dissolve
        ver "*Shlick, fwhhick-!* Ghhh♥♥♥"
        "Meanwhile, dwarfed by Veronica's wide ass, Felicia was proving herself to be a dutiful cunt licker."
        ver "Dmmhmhheeeht! Hnnn...!"
        "At this angle, her exact technique was left a mystery for the camera, but even when you factored in Veronica's heightened state..."
        ver "Ghhh, mmmh, hhhtwwwahht♥♥♥♥♥♥"
        "You could tell she was putting on a riveting performance."
        "So the two carried on for about a minute or an eternity, not a single one slowing down."
        scene or_onvero2_a with dissolve
        show or_onvero2 with dissolve
        "Felicia licked, Rosalind manhandled, and Veronica accepted what the two offered - all until the MILF pulled herself from her lips."
        scene w3_2523 with dissolve
        rose "Mhh-ahh... haa...!"
        ver "W-what--♥♥ ahhh, that--hwwwha~!!!"
        scene w3_2524 with dissolve
        rose "Wo-woah... I feel lightheaded... "
        ver "Ah... that w-was... I mean, w-what is it, my birthday? Heh, haa...♥♥"
        scene w3_2525 with dissolve
        rose "Ha, hope that was alright... you should always begin foreplay with a kiss."
        scene w3_2526 with dissolve
        ver "T-that, aahhh, a p-personal rule of yours...?"
        scene w3_2527 with dissolve
        rose "...more of a wish?"
        scene w3_2528 with dissolve
        ver "Y-you {b}-hnnn!-{/b} e-ever kiss a-"
        scene w3_2529 with dissolve
        rose "First time."
        scene w3_2530 with dissolve
        ver "Well, aren't I spe-"
        play sound "sound effects/vib-start.wav"
        scene w3_2531 with dissolve
        "*Bzzzt, bzzzzt, bzzzzt!!!!*"
        ver "Hnn...! Fuck! {b}Y-you're moving them around with y-your tongue?!{/b}"
        scene w3_2532 with dissolve
        "*Bzzzt, bzzzzt, bzzzzt!!!!*"
        ver "Gyyy-♥♥♥♥♥♥. Y-you sure y-you're s-straight, Blondie?!"
        scene w3_2533 with dissolve
        ver "You're better at that than h-half the--"
        scene w3_2534 with dissolve
        ver "{b}Hhhhnnn--♥♥♥ What do you got t-there?{/b}"
        scene w3_2535 with dissolve
        rose "This? This is going up your keist-- *ahem."
        scene w3_2536 with dissolve
        rose "{b}I mean{/b}, this is going up your ass, you... slut."
        scene w3_2537 with dissolve
        ver "Ahh, hhaaa... y-you're not very convincing in that role, Rosie -- and besides, c'mon... it's kinda already -hnnn!- crowded b-back there!"
        scene w3_2538 with dissolve
        rose "We'll see about that."
        scene w3_2539 with dissolve
        "..."
        play ambient "sound effects/vib-ongoing.wav"
        $ renpy.music.set_volume(.5, 0, channel = "ambient")
        scene w3_2540 with dissolve
        rose "Swap sides with me for a minute, will you?"
        "*Shlick, fwhick, fwhick-!*"
        scene w3_2541 with dissolve
        fel "E-eh...?"
        scene w3_2542 with dissolve
        rose "Swap sides with me."
        ver "Seriously, I don't think that's going to--"
        scene w3_2543 with dissolve
        ver "*Bzzzzt!* {b}Gaaahfffeeiiiiiit!{/b} Hnn...!!!"
        fel "Of course it will fit. A big girl like her has plenty of room."
        scene w3_2544 with dissolve
        ver "Gh, hhh-- f-fuck!"
        rose "You're tight..."
        ver "Of c-course I am - ahh... I don't use my ass for s-stuff like this!"
        scene w3_2545 with dissolve
        ver "*Bzzzzt!* {b}Dddhhhhmmnit, it's m-making them r-rattle! G-gahhh...!"
        rose "Come on, honey. You can take it. Don't push ba--"
        ver "Ynnnggg-♥♥♥♥ S-sh-eeehhtt!"

        if w3HagHandie == True:
            stop ambient
            scene br_haghandy3_a with pixellate
            show br_haghandy3 with dissolve
            rose "Good job! I knew you could do it."
            kat "It's always interesting when you give a woman like Rosalind the opportunity to take the reins. They're so stressed, pent up, inhibited..."
            ver "Yyhhhhoooooohhhh♥♥♥♥♥"
            kat "They don't show you their true colors as much as their whole color palette blends together in one fucked up mix. I wonder where this will go."
            mc "H-hhhhngg...!"
            "Like hell my mind was registering any of her bullshit right now."
            ver "H-heuuuh?! Y-you're gonna use t-that t-too?!"
            scene w3_2373 with dissolve
            sophia "You counted on this kind of... {i}fervor{/i}?"
            scene w3_2374 with dissolve
            mc "H-a, hnnggaa..."
            "The inside of my head was mush right now. My capacity for language was utterly eroded."
            scene w3_2375 with dissolve
            kat "I've been doing this for a long time. Before the club, I had my {i}other{/i} enterprises."
            kat "I'm well acquainted with the peculiar ways people in desperate situations respond. In a way, it's a more potent means of control than any drug."
            scene w3_2376 with dissolve
            sophia "I'm actually impressed for once."
            scene w3_2377 with dissolve
            kat "You shouldn't be. I'm an amateur when compared to someone like your owner."
            kat "I think the way Van Doren has you under his thumb is much more impressive."
            scene w3_2376 with dissolve
            sophia "Thank you."
            scene w3_2377 with dissolve
            kat "You took that as a compliment?"
            scene w3_2376 with dissolve
            sophia "Of course I did. Abel only has the best things."
            scene w3_2378 with dissolve
            ver "Huh... that's an interesting direction..."
            scene w3_2379 with dissolve
            kat "Your self-awareness in your choice of words is commendable, dear."
        else:

            stop ambient
            scene w3_2380 with dissolve
            rose "Good job! I knew you could do it."
            scene w3_2381 with dissolve
            kat "It's always interesting when you give a woman like Rosalind the opportunity to take the reins. They're so stressed, pent up, inhibited..."
            ver "Yyhhhhoooooohhhh♥♥♥♥♥"
            kat "They don't show you their true colors as much as their whole color palette blends together in one fucked up mix. I wonder where this will go."
            scene w3_2382 with dissolve
            "To my annoyance, whenever one of them spoke, my attention would turn back to just how fuckable the women next to me were. "
            ver "H-heuuuh?! Y-you're gonna use t-that t-too?!"
            scene w3_2383 with dissolve
            sophia "You counted on this kind of... {i}fervor{/i}?"
            scene w3_2382 with dissolve
            mct "(Christ, I want to make that mouthy hag choke on my dick until she passes out!)"
            "Intrusive thought upon intrusive thought flooded my head."
            scene w3_2384 with dissolve
            kat "I've been doing this for a long time. Before the club, I had my {i}other{/i} enterprises."
            kat "I'm well acquainted with the peculiar ways people in desperate situations respond. In a way, it's a more potent means of control than any drug."
            scene w3_2383 with dissolve
            sophia "I'm actually impressed for once."
            scene w3_2385 with dissolve
            kat "You shouldn't be. I'm an amateur when compared to someone like your Master."
            kat "I think the way Van Doren has you under his thumb is much more impressive."
            scene w3_2386 with dissolve
            sophia "Thank you."
            scene w3_2387 with dissolve
            kat "You took that as a compliment?"
            scene w3_2386 with dissolve
            sophia "Of course I did. Abel only has the best things."
            scene w3_2388 with dissolve
            ver "Huh... that's an interesting direction..."
            scene w3_2387 with dissolve
            kat "Your self-awareness in your choice of words is commendable, dear."

        scene w3_2547 with pixellate
        play sound "sound effects/slap1.wav"
        scene w3_2548 with vpunch
        "*Thwick!*"
        ver "O-ohhh, gghhh..."
        scene w3_2546 with dissolve
        rose "This is..."
        scene w3_2547 with dissolve
        play sound "sound effects/slap1.wav"
        scene w3_2548 with vpunch
        "*Thwick!*"

        if w1ExIntuitionGameWinnerRose == True:
            scene w3_2546 with dissolve
            rose "This is just like when you and Felicia went head-to-head in the first week."
            scene w3_2547 with dissolve
            play sound "sound effects/slap1.wav"
            scene w3_2548 with vpunch
            "*Thwick!*"
            scene w3_2546 with dissolve
            rose "I didn't experience what it was like to have your butt smacked while it was so stuffed."
        if w1ExIntuitionGameWinnerFel == True:
            scene w3_2546 with dissolve
            rose "This is just like when you and I went head-to-head in the first week."
            scene w3_2547 with dissolve
            play sound "sound effects/slap1.wav"
            scene w3_2548 with vpunch
            "*Thwick!*"
            scene w3_2546 with dissolve
            rose "We both know what it's like to have your butt clamp down with every impact."
        if w1ExIntuitionGameWinnerVero == True:
            scene w3_2546 with dissolve
            rose "This is just like when Felicia and I went head-to-head in the first week."
            scene w3_2547 with dissolve
            play sound "sound effects/slap1.wav"
            scene w3_2548 with vpunch
            "*Thwick!*"
            scene w3_2546 with dissolve
            rose "You didn't experience what it was like to get your butt smacked while it was stuffed."

        scene w3_2549 with pixellate
        play sound "sound effects/slap1.wav"
        scene w3_2550 with vpunch
        "*Thwick!*"
        ver "Gyjhhh- hhhgnnngg-♥♥♥"
        scene w3_2551 with dissolve
        rose "We should all be used to this sort of play by now..."
        scene w3_2552 with dissolve
        ver "Gah, fuck you! Switch places with me and we'll s-see what kind of ugly sounds y-you make!"
        scene w3_2553 with dissolve
        rose "Fuck me...?"
        scene w3_2551 with dissolve
        rose "You were so tough when we were getting shocked. You know, if I'm being honest... {b}it was actually irritating.{/b}"
        scene w3_2554 with dissolve
        play sound "sound effects/slap1.wav"
        scene w3_2555 with vpunch
        "*Thwick!*"
        ver "Ghh, oohoh--oogogohohhhhhh--"
        scene w3_2554 with dissolve
        play sound "sound effects/slap1.wav"
        scene w3_2556 with vpunch
        "*Thwick!*"
        scene w3_2557 with dissolve
        fel "Holy shit, Red. Your pussy is amazing!"
        rose "Can I ask you something? Why do you act like you're better than Felicia? Better than me?"
        scene w3_2558 with dissolve
        fel "{size=10}Seriously... it was strong enough to...{/size}"
        ver "W-what, hhhaaa.. n-no I don't?!"
        scene w3_2559 with dissolve
        fel "{size=10}I mean, imagine if you were taking a...{/size}"
        rose "You constantly act like you're too good to be here."
        scene w3_2560 with dissolve
        ver "Hnn... wwhhhaay"
        rose "I swallow my pride, yet you always run your mouth and just say what I'm thinking too."
        rose "It's annoying. It's fucking arrogant! It's..."
        scene w3_2561 with dissolve
        "........."
        "......"
        scene w3_2562 with dissolve
        "..."
        scene w3_2563 with dissolve
        fel "Don't take it personally. I think she's madder at herself than you."
        scene w3_2564 with dissolve
        ver "Huuuaahh, s-shut the fuck up--"
        rose "Shut up!"
        scene w3_2565 with dissolve
        fel "Bah, you fucking bitches."
        scene w3_2566 with dissolve
        rose "I was thinking..."
        rose "...why should we do any work when we could just let some batteries and gravity do it for us?"

        if w3HagHandie == True:
            scene w3_2407 with pixellate
            kat "I'm starting to get offended, Mr. [mcl]. Does my hand not suffice?"
            kat "Don't you want to taste release?"
            scene w3_2408 with dissolve
            mc "G-gah, f-fuck! It's not like I have any control over it!"
            sophia "Hmm..."
            scene w3_2409 with dissolve
            "Every fiber of my being desperately anticipated climax. My reason had been eroded and my purpose replaced by the critical need to expunge every trace of nauseating desire from my body through my cock."
            "The hairs on my arm stood on end, the feeling in my extremities came and went like the tide, and a pervasive tingling feeling floated from my neck down to my tailbone - by all means, my body told me that I {b}should{/b} be coming."
            scene w3_2410 with dissolve
            sophia "Interesting."
            scene w3_2409 with dissolve
            "But I wasn't. My bloated dick burned against the soft palm of the old woman's hand, pulsating and twitching from the ceaseless stimulation, filling me with the irrational fear that I might literally explode if I didn't soon go careening into the void of sexual release."
            scene w3_2411 with dissolve
            sophia "All things considered, he is showing a {b}surprising{/b} degree of longevity..."
            scene w3_2412 with dissolve
            kat "Maybe your fragrance isn't as effective as you think it is."
            mc "G-gaahh!"
            scene w3_2411 with dissolve
            sophia "Maybe..."
            scene w3_2413 with dissolve
            mct "(No! It was definitely fucking effective!)"
            sophia "...but unlikely. Hey, [mcf]..."
            scene w3_2414 with dissolve
            "Through lidded eyes, I could sense the blonde scooching closer and closer."
            scene w3_2415 with dissolve
            sophia "The issue is that a young, well-traveled guy like you simply can't get off on an old woman's touch, right?"
            scene w3_2416 with dissolve
            mc "That's not--"
            scene w3_2417 with dissolve
            sophia "{b}{i}Isn't it?{/b}{/i}"
            "Even in my lust-addled state..."
            scene w3_2418 with dissolve
            "My brain registered amazement over the willful way Sophia flipped the switch, going from detached aloofness to a man-killer just as easily as one would shed their clothes. "
            scene w3_2419 with dissolve
            mc "Hnngg...!"
            kat "*Scoff* Feeling left out, were you?"
            sophia "Give them a comparison."
            scene w3_2420 with dissolve
            "My hand responded independently, sinking into the pleasant give of the doctor's tit-flesh in an instant as what remained of my faculties disappeared into the whirlpool of her eyes."
            sophia "You got a mess lurking somewhere in there that you want to get out?"
            mc "Ha... hnngg...! F-fuck it!"
            scene w3_2421 with dissolve
            sophia "...?!"
            "I kissed her, just as you'd expect a man on the brink of starvation to steal a loaf of bread."
            scene br_hhplus_a with dissolve
            show br_hhplus with dissolve
            sophia "Mmmhhhh....!"

            if kat_polite == True:
                "She might not have expected it or even wanted it, but she quickly accepted it as a consequence of the \"just a bit of chaos\" she wielded in her joust against Mrs. Pulman."
            else:
                "She might not have expected it or even wanted it, but she quickly accepted it as a consequence of the \"just a bit of chaos\" she wielded in her joust against Kathleen."

            kat "H-hey, ahh--"
            "Spurred on by having the attention of two beautiful women, even if it was just the fucked up equivalent of cooking ants with a magnifying glass to them, I knew it wouldn't be long until I finally had my release."
            kat "Gah, ah... ha... hmpfh."
            "Although I could feel her eyes on my neck, the old woman continued to milk me."
            "*Cwhup, fwhup, chwup...!*"
            kat "I've somehow ended up feeling like a third wheel."
            "I pawed at both women's breasts with a virgin-like fervor, wholly enamored by an opportunity I might never get again."
            mct "(The head of a charity and a world-class scientist... ha, fucking sluts!)"
            "I felt like a king, not of my own making of course, but my brain was so cooked as to not know the difference. Thinking was hard, but what few thoughts I could miraculously formulate were like tidal waves breaking against the shore."
            mct "(Who the hell do you think you're fucking with? You think you can toy with me just because of money?!)"
            "I felt smothered, suffocated, and hot. More akin to a wick that was about to burn out than a human being."
            mct "(I'M A GUINEA PIG TO YOU?!)"
            "Every sensation felt heightened, and every second felt prolonged... I genuinely feared that the moment I popped would be when I was snuffed out."

            mct "{size=+30}{font=/gui/fonts/MB-Thin_Worms.ttf}(You like to toy with pe-){/font}{/size}"


            "My brain gave out, but if I ceased to exist after this, I instinctively knew one thing: these last minutes of my life should be bold."

            menu:
                "Goad the old woman into letting you finish in her mouth.(w3KatPromoFinish = True)"(chg=["kathleen_trust_up"]):
                    $ w3KatPromoFinish = True
                    $ Kathleen_Trust += 1
                    scene w3_2422 with dissolve
                    mc "I'm about to b-blow..."
                    kat "You don't need my permission."
                    scene w3_2423 with dissolve
                    mc "Can you finish me with your mouth?"
                    kat "Hmmmmm, not going to happen."
                    mc "A-ah, pretty please? With a cherry on top?"
                    scene w3_2424 with dissolve
                    kat "Why don't you ask Miss Lundgren to do it?"
                    mc "...because I want you, Ma'am."
                    scene w3_2425 with dissolve
                    kat "...hmmmmmmmm. You have the eyes of a crazed animal, yet..."
                    scene w3_2426 with dissolve
                    kat "You're asking so nicely. God, I love that."
                    scene w3_2427 with dissolve
                    "She smirked like she had won against me, and perhaps even against Sophia."
                    scene w3_2428 with dissolve
                    kat "It really is goddamn adorable. Ask me again, [mcf]."
                    scene w3_2429 with dissolve
                    "A desperate, cloying urge inside me told me her mouth was the only place I wanted to be right now and if it took a bit of pleading to get me into a position where I could fill that mean bitch's stomach with my seed, then so be it."
                    scene w3_2430 with dissolve
                    mc "Hhh, haa... would you PLEASE finish me with your mouth, Mrs. Pulman?"
                    scene w3_2431 with dissolve

                    if kat_polite == True:
                        "Without another word, Mrs. Pulman lowered herself and..."
                    else:
                        "Without another word, Kathleen lowered herself and..."

                    scene br_hhplus_hbj_a with dissolve
                    mc "G-gah...!"
                    "The moment her lips wrapped themselves around my cock, I felt like I might pass out."
                    "Her seal was so airtight that her mouth felt like an oven. Steady puffs of hot breath passed over the head of my cock as it made its way out through her nose."
                    scene br_hhplus_hbj_a with dissolve
                    show br_hhplus_hbj with dissolve
                    mc "F-fuck, damn it!"
                    "*Shwuck, fgwhhuck, thwuuuck!*"
                    "What little air could escape from her hold transformed into {b}obscene{/b} noises as she inched herself up and down my shaft."
                    mc "H-holy-!"
                    "The running narration in my head was a jumbled mess, but through all the muddied noise from the pleasure soaking into my brain, I grasped a simple truth."
                    mc "Hnnng, you've sucked a lot of cock in your time, haven't you?!"
                    "*Thwaahp, fwhap, swhhuck~!*"
                    "The answer to that question played across my glans every time I wedged myself comfortably in her throat with zero fuss."
                    "Swhuck, hhhwhuck, fhhggguuk!*"
                    "{b}Damn it!{/b} A rich woman like her had no business sucking dick this well."
                    mc "Ghhn, haaat, hnnngg...!"
                    "She sucked me with the skill of a woman who had {b}nothing{/b} to her name."
                    kat "Mmmhm, hhmhm~"
                    "Just like her hand job, there was no wasted effort. She didn't tackle it in a clumsy frenzy, nor did she need to cautiously get used to my size."
                    "*Shwhuhuck, fwhhucuk, ghhwhuhuk!*"
                    "She sucked me like she had been sucking {b}my{/b} dick her whole life, pleasuring me at a steady and comfortable pace. I marveled at how, through a mere blowjob, a woman so cold and cruel could instantly imprint herself on my body as warm and welcoming."
                    "I was quickly understanding that \"adorable\" disparity she had just spoken."
                    mc "Hnng, h-how?!"
                    sophia "It's not performing brain surgery."

                    if kat_polite == True:
                        "{b}There{/b} was another perverse delight, speeding me toward my climax. Sophia's attention was on the back of Mrs. Pulman's head, watching intently as she debased herself in pursuit of degrading me."
                    else:
                        "{b}There{/b} was another perverse delight, speeding me toward my climax. Sophia's attention was on the back of Kathleen's head, watching intently as she debased herself in pursuit of degrading me."

                    mct "(Haaaa... hope you like the show, bitch. You're the impetus for this.)"
                    "*Fwhhuck, ghhhukh, khggguuhhk*"
                    mc "Ahh... y-you dick swallowing--! Hnnngg...!"
                    "It was coming."
                    scene w3_2432 with dissolve
                    mc "You think I'm adorable?!"
                    "I was moments from blowing my load, and with it, the indignation from earlier swelled in me. I had wanted a bold finish before I met my end, and well..."
                    mct "(I'll show you adorable!)"
                    stop music
                    scene br_hhplus_gulp1_a with vpunch
                    mc "I'm c-cumming, fucking drown in it, you damn--"
                    play sound "sound effects/spurt.wav"
                    with flash
                    kat "Mmmmh?!"
                    "Before she could even register what was happening, ropes of piping hot cum barreled down her esophagus on a one-way trip to her stomach."
                    play ambient "sound effects/fel2.wav"
                    scene br_hhplus_gulp1_a with dissolve
                    show br_hhplus_gulp1 with dissolve
                    play sound "sound effects/spurt.wav"
                    with flash
                    kat "Ghhkka, hkkaa-!"
                    "I pressed down hard, holding the old woman's head in place as she gargled my seed in abject surprise."
                    mc "Hnngg, all of it!"
                    "I pressed down so hard it hurt my groin."
                    play sound "sound effects/spurt.wav"
                    with flash
                    kat "Ghhuk, hhuuuh, hwwwhuuuck...!"
                    "It was massive, like I was cumming my very soul down the old woman's throat."
                    kat "Ghuk, khak, uuhhk-!"
                    mc "Gah, c-choke on it!"
                    play sound "sound effects/spurt.wav"
                    with flash
                    "Not all of my load was making its way down her throat. To my perverse glee, I could {i}feel{/i} myself coating the lining of her throat."
                    kat "Ghhuk, hhuuuk...!"
                    scene br_hhplus_gulp2_a with flash
                    show br_hhplus_gulp2 with dissolve
                    play sound "sound effects/spurt.wav"
                    with flash
                    mc "Hope you like the fucking taste!"
                    kat "Mmmh, hhhngg?!?!"
                    sophia "I don't think she can breathe..."
                    mc "Good! She can breathe when I'm fucking--!"
                    stop ambient fadeout 4.0
                    play sound "sound effects/spurt.wav"
                    with flash
                    ".........!"
                    play sound "sound effects/spurt.wav"
                    with flash
                    "......!"
                    scene w3_2433 with dissolve
                    mc "A-aahh...!"
                    scene w3_2434 with dissolve
                    kat "Ugghhuhh..."
                    scene w3_2435 with dissolve
                    "Peace."
                    "Serenity."
                    "Satisfaction."
                    "In this moment, I had it all."
                    scene black with w20
                    "With that, I happily died. The oblivion I felt nipping at my heels finally sank its sharp teeth into my throat."
                    "............"
                    "........."
                    "......"
                    "..."
                    kat "Why are you holding your hands out like that? It's weird."
                    mct "(Ah, fuck... I {i}wasn't{/i} dead? {b}Oh no.{/b} Then that meant I just...)"
                    scene w3_2436 with w9
                    sophia "She's right. It's distracting."
                    scene w3_2437 with dissolve
                    "I didn't know how long I was out of it, but by the time I opened my eyes, the two women had collected themselves, and what I thought was a bold display of defiance was made pitiful and wholly expected by their bemused faces."

                    if kat_polite == True:
                        "Mrs. Pulman looked {i}totally{/i} unaffected by my rough treatment, showing no signs of having mercilessly guzzled my cum just moments ago..."
                    else:
                        "Kathleen looked {i}totally{/i} unaffected by my rough treatment, showing no signs of having mercilessly guzzled my cum just moments ago..."

                    scene w3_2438 with dissolve
                    kat "Oh, by the way... you said some pretty outlandish things to me."
                    scene w3_2439 with dissolve
                    mc "If I recall, I did a bit more than that..."
                    scene w3_2440 with dissolve
                    kat "It was {b}adorable{/b}."
                    "She had indeed won."
                    ver "Ghh, hhaan, streetthhhchggingg-!!!"
                "Leave an impression on the doctor(w3SophiaPromoFinish = True)."(chg=["kathleen_down2"]):

                    $ w3SophiaPromoFinish = True
                    $ Kathleen_Affection -=2
                    "I knew what I wanted."
                    sophia "Mmmhh, hhhhh..."
                    "And that last act of defiance would be leaving the doctor, the root cause of all this, something to remember me by."
                    scene br_hhplus_doc1_a with dissolve
                    show br_hhplus_doc1 with dissolve
                    "*Chwup, fhwup~*"
                    "I wanted to hear this aloof bitch moan, so I focused everything on the woman whose mouth I was currently exploring."
                    sophia "Mmmh, hhmmm...?"
                    "It was a battle against my wits. Sophia was literally intoxicating. Focusing my senses all on her had me burning twice as fast."
                    "By instinct, I felt her breast over her clothes."
                    sophia "Mmhh..."
                    "Her coos told me she was receptive, but it wasn't quite the noise I wanted to drag out from the blonde."
                    scene br_hhplus_doc2_a with dissolve
                    show br_hhplus_doc2 with dissolve
                    sophia "Ghu, gha~ghhuu...!"
                    "Deciding that over the clothes touching wouldn't do it, I switched focus on the erogenous zone in her mouth, intensifying my efforts in an intricate dance to subdue her tongue with my own."
                    sophia "Mmmmh, mmhhhh- *chwuph, fhwhup~*"
                    "She wasn't a passive observer in my hunt; her tongue played coy, darting away and slipping from my grasp whenever I thought I had her pinned."
                    "It was mere seconds, but--"
                    "*Chwhu, fhwwwup, chup!*"
                    "--but, in my fogged-over state, time held little sway over my perception. What was in reality a clumsy tussle felt like a long and protracted siege."
                    "I don't know if it was because of the perfume, but all bodily sensations gradually began to meld into one."
                    "The feeling of the old woman's hand milking my cock, the wet warmness of our kiss, the bubbling desire so strong that I was confident it would be the end of me..."
                    mc "Mmmh, hhhmmm-!"
                    "All of it spelled an overload melded and combined into a singular feeling of otherness. I was sure I had lost this battle until..."
                    scene br_hhplus_doc3_a with dissolve
                    show br_hhplus_doc3 with dissolve
                    "My brain registered a change."
                    mct "Was she...?"
                    sophia "Mmmh, hhmhm~aahhh...!"
                    "She was closer."
                    "She was pressing into me."
                    "She felt it."
                    "She was {b}heated{/b}."
                    "{i}She was kissing me back.{/i}"
                    "Whether it was done deliberately or on an instinctual level, her body responded favorably."
                    sophia "Ahh, hhhnnggg, mmmmhh-!"
                    "My hand found a place on her ass and I used that to spur her on even more. With this, I had physical confirmation of my success."
                    mct "(Fuck, what a great-!)"
                    "I could feel the hot dampness of her delicate spot."
                    sophia "Mmhh, hhaa...♥♥♥"
                    "She purred openly and I felt a petty relief over my trivial victory. The succubus driving me to this desperate state wouldn't escape our battle unscathed."
                    "*Chwup, fhwwup, khwwup*!"
                    "--and that wasn't the only sense of relief I felt."
                    stop music
                    play sound "sound effects/spurt.wav"
                    scene w3_2441 with flash
                    mc "{b}Hnng, ah-!!!{/b}"
                    "I didn't know when it started, but ropes of cum geysered from my cock and rained down from the sky."
                    play sound "sound effects/spurt.wav"
                    scene w3_2442 with flash
                    mc "Ghh, aaahh- sssshit--"
                    kat "Huh, {b}WOW{/b}."
                    scene w3_2443 with dissolve
                    mc "Hngg, hhhhmmmhh-~"
                    "All the suffocating vileness in me was expelled and released into the world. All my desperation spilled out onto our clothes and thighs."
                    "Soon need was replaced with..."
                    scene w3_2444 with dissolve
                    "Peace."
                    "Serenity."
                    scene w3_2445 with dissolve
                    "Satisfaction."
                    "Emptiness."
                    "The oblivion I felt nipping at my heels finally sank its sharp teeth into my throat."
                    scene black with w20
                    "I was dead."
                    "............"
                    "........."
                    "......"
                    "..."
                    sophia "Great, now we'll spend the rest of the show reeking of semen."
                    mct "(Ah, fuck... I {i}wasn't{/i} dead? {b}Oh no.{/b} Then that meant I just...)"
                    scene w3_2446 with w9
                    kat "You should've thought of that before you entered the crossfire."
                    scene w3_2447 with dissolve
                    sophia "You were taking too long. I wanted to put an end to the distraction."
                    scene w3_2448 with dissolve
                    "I didn't know how long I was out of it. Still, by the time I opened my eyes, the two women had collected themselves. The damage I thought I had done to Sophia with my counter-attack was made pitiful by their bemused faces."
                    scene w3_2449 with dissolve
                    kat "Oh, please. Are those the kind of sounds you make matter-of-factly?"
                    scene w3_2450 with dissolve
                    "Sophia looked as composed as ever, and except for a little blush, her attention turned back to the Carnations."
                    scene w3_2451 with dissolve
                    kat "I hope that provided you a measure of relief, Mr. [mcl]. That certainly was an... {i}explosive{/i} finish."
                    mc "A, ahem... thaaaaaanks?"
                    scene w3_2452 with dissolve
                    kat "Don't mention it. It was... interesting."
                    ver "Ghh, hhaan, streetthhhchggingg-!!!"
        else:

            scene w3_2453 with dissolve
            mc "........."
            mc "......"
            stop music
            play sound "sound effects/record-scratch.wav"
            scene w3_2454 with dissolve
            "...this was my limit."
            $ renpy.end_replay()
            scene w3_2455 with dissolve
            mc "Aaeeh, I'll be riiiiiight back."
            scene w3_2456 with dissolve
            "......"
            scene w3_2457 with dissolve
            "..."
            scene w3_2458 with dissolve
            kat "Is that a milder scent you are wearing?"
            sophia "It's the same batch as the bottle I gave you."
            scene w3_2459 with dissolve
            kat "The effect seemed... less? Why's that?"
            scene w3_2460 with dissolve
            sophia "It's possible that his body adapted and partially metabolized the odor molecules. All I can say is that it's remarkable he held out that long."
            sophia "It could be a matter of willpower."
            scene w3_2461 with dissolve
            kat "When I had dinner with Charles the other night, he didn't even flinch."
            scene w3_2462 with dissolve
            sophia "Dr. Kohler is a scary man."
            scene w3_2463 with dissolve
            kat "Is that your appraisal after demolishing him game after game?"
            scene w3_2464 with dissolve
            sophia "How else should I describe a man who has no need but keeps his passions tightly controlled."
            scene w3_2465 with dissolve
            kat "That's why he and I are incompatible. He treats fucking like it's Christmas."
            kat "You don't have anything to worry about as long as you don't lose."
            scene w3_2466 with dissolve
            sophia "I don't plan on it, but I have a feeling he eventually wins one way or another."
            scene w3_2459 with dissolve
            kat "Abel wouldn't let it come to that, would he?"
            scene w3_2467 with dissolve
            "......"
            "..."
            scene w3_2460 with dissolve
            sophia "Thank you for indulging my little whim, Kathleen. It was amusing."
            scene w3_2459 with dissolve
            kat "Don't mention it. One should make their own fun in life. Still..."
            kat "...you're very competent. Don't you ever desire more?"
            scene w3_2468 with dissolve
            sophia "A frivolous bitch like you has no business saying that to me."
            scene w3_2469 with dissolve
            kat "Ah, fuck. There it is."
            scene black with fade
            kat "I almost felt sorry for you."
            jump w3WashRoom

        play music "music/landing.ogg"
        scene w3_2567 with pixellate
        ver "Hnngggg- hhaaa-"
        rose "......"
        fel "..."
        scene w3_2568 with dissolve
        ver "Waahh, wwwwhhhuuuat-"
        rose "......"
        fel "..."
        scene w3_2569 with dissolve
        ver "Ggaahhhk, y-you jerks are really j-just gonna stand there?! H-hhhaaa...!"
        scene w3_2570 with dissolve
        fel "I mean, I started out wanting to play nice, but Rosalind..."
        scene w3_2571 with dissolve
        rose "This is just part of the game."
        scene w3_2570 with dissolve
        fel "She does have a point."
        scene w3_2572 with dissolve
        ver "Haaa, phhh- can't you j-just- *Bzzzt, bzzzt!* hnnn!"
        scene w3_2573 with dissolve
        fel "It's not like you're not getting any satisfaction. How many times have those toys made you cum?"
        scene w3_2572 with dissolve
        ver "Gaa-h, it's n-not enough! E-every time I think I'm c-coming down-- I g-gett hho-tt, ag--gaggin..! Hnn!!"
        scene w3_2574 with dissolve
        ver "C'mon... u-use your mouth again, that was more..."
        scene w3_2575 with dissolve
        fel "Yeesh. I'm feeling kinda..."
        scene w3_2576 with dissolve
        rose "We're supposed to be punishing her."
        scene w3_2577 with dissolve
        fel "...she does have a point. Should we focus on winning?"
        scene w3_2578 with dissolve
        ver "Guhhk, hhhnnanaaa-♥ D-damn it! Focus on winning?!"
        scene w3_2572 with dissolve
        ver "W-what the hell do you stand to w-win here?! The company of other a-sshhholehhh?!"
        scene w3_2573 with dissolve
        fel "We all have our reasons, Red."
        scene w3_2579 with dissolve
        ver "Your reason is bullshit!"
        scene w3_2580 with dissolve
        fel "Why should I care about your sob stories? It doesn't matter who wins, it only matters if you lose."
        scene w3_2581 with dissolve
        fel "Do you think Rose will give a shit if you win over me? It's all the same to her as it would be to you."
        scene w3_2582 with dissolve
        ver "..y-yeah?"
        scene w3_2580 with dissolve
        fel "You should be happy to have a bored rich bitch as your opponent. Would you rather three desperate people get paraded like show dogs over two?"
        scene w3_2582 with dissolve
        ver "If you win, two desperate people are h-hosed! Gg-ah-♥"
        scene w3_2583 with dissolve
        fel "The math's the same either way. Just focus on what you have to do."
        rose "..."
        scene w3_2584 with dissolve
        ver "What the fuck are you even talking about?! Ahhhhh, d-damn it it pisses me off!"
        ver "W-when you l-lose, you can go back to your d-damn penthouse! Take a dip in your pool!"
        scene w3_2585 with dissolve
        fel "Sure I can."
        scene w3_2586 with dissolve
        ver "I get why you want to join! Y-you're not any fucking different than the old cunt!"
        scene w3_2584 with dissolve
        ver "You'd fit right in r-rreeeaeehhhl -hnnn!- nicely, if only y-you weren't b-born {b}TRAILER TRASH!{/b}"
        scene w3_2587 with dissolve
        fel "..."
        scene w3_2588 with dissolve
        rose "Ah... ha... heh, c'mon... this is all a game. Don't-"
        scene w3_2589 with dissolve
        fel "We're just going in circles - just hang there and cum, Red. It'll be more fun that way."
        scene w3_2590 with dissolve
        ver "You--"
        scene w3_2591 with dissolve
        ver "Gwwwhhhhahahahahhhh- hh-"
        ver "Huuuahhhht-! C-ccumm--!"
        scene w3_2592 with dissolve
        fel "Shit... right on cue..."
        ver "Hhgnn, ugugghh--♥♥♥♥"
        fel "Guess we're finished."
        scene w3_2593 with dissolve
        rose "I doubt it. We should probably keep going until Mrs. Pulman stops us."
        scene w3_2594 with dissolve
        fel "How long do you think that's going to be?"
        stop music fadeout 3.0
        scene black with fade
        rose "Who knows."
        jump w3WashRoom

    if w2ExLoserDuo == True:
        scene w3_2595 with pixellate
        rose "There's only one of me and two of you..."
        scene w3_2596 with dissolve
        rose "......"
        scene w3_2597 with dissolve
        rose "..."
        scene w3_2598 with dissolve
        rose "Do you girls have a preference on who I should start with?"
        scene w3_2599 with dissolve
        ver "Of-c-couuuurse n-ot--"
        fel "M-meeeh! I'm d-dying here! -Hnnn- C'mon!"
        scene w3_2600 with dissolve
        rose "Is it really that bad?"
        scene w3_2601 with dissolve
        fel "M-my whole body is on f-fire! I can't even think without--"
        scene w3_2602 with dissolve
        rose "Then I guess you'll have to sit tight while I give Veronica a hand."
        scene w3_2603 with dissolve
        fel "W-whaaa...?"
        scene w3_2602 with dissolve
        rose "She's hurting just as bad as you. The only difference is, well... she's not... {b}you{/b}."
        scene w3_2603 with dissolve
        fel "H-huh? What do you mean by that?!"
        scene w3_2604 with dissolve
        rose "It's nothing personal. Just... trying to be utilitarian here."
        fel "Bullshit, you two-faced bitch!"
        scene w3_2605 with dissolve
        rose "Is that how you ask nicely for something?"
        scene w3_2606 with dissolve
        fel "You want me to beg?!"

        if rosalindFelSolution == True:
            fel "Is t-that what you did with [mcf] when you got him barking up my tree for some money? O-or m-maybe you did something more like me than you'd care to--"
        else:
            pass

        scene w3_2607 with dissolve
        rose "No. I want you to be patient and \"sit there\" quietly. This is supposed to be a punishment."
        rose "Why would I just give you what you ask for?"
        scene w3_2608 with dissolve
        fel "A-aahh, y-yeah right... you and Red don't like me, do you?"
        scene w3_2609 with dissolve

        if rosalindFelSolution == True:
            rose "I'm grateful for your money, but... do you want me to be honest?"
        else:
            rose "Do you want me to be honest?"

        scene w3_2610 with dissolve
        rose "......"
        scene w3_2611 with dissolve
        rose "..."
        scene w3_2609 with dissolve
        rose "I don't care about either of you one way or another."
        scene w3_2612 with dissolve
        ver "H-haah! See? Not everything is about you, Blondie!"
        ver "Some of us have heavier shit on our mi--"
        play music "music/addict.ogg"
        play sound "sound effects/vib-start.wav"
        scene w3_2613 with dissolve
        ver "H--hhhnaaaaahh, fhhh-ddd--ahk--"
        rose "I wish you'd sit here quietly too."

        if w3HagHandie == True:
            scene br_haghandy_a with dissolve
            show br_haghandy with dissolve
            kat "It didn't take long for Rosalind to become comfortable with the situation, did it?"
            "In my current over-cooked state, what was playing out on the television screen was a muddled mess of pixels that barely registered meaning to me."
            kat "Sluts like her sure are adaptable. It's a strength, but it can be a little boring when they're totally obedient."
            "No, in my current state, my mind was completely consumed by the old woman's grip on my cock."
            mc "H-haahaa...!"
            scene br_haghandy2_a with dissolve
            show br_haghandy2 with dissolve
            sophia "Unlike Lynch?"
            mc "G-gahh...!"
            "The pitiful noise of a rutting animal punctuated the women's conversation."
            kat "Exactly! Ah, I love it! I really do love Miss Lynch. I wish I had more than a month with her."
            kat "Still, it should be fun to watch Mrs. Carter let loose. Of course, she'll justify it was done under instruction, but she won't be able to hide her enjoyment of this from the other two."
            sophia "You have a {i}unique{/i} sense of aesthetics, Kathleen."
            kat "Well, what do you find hot, Miss Lundgren? I'm genuinely curious..."
            scene br_haghandy_a with dissolve
            show br_haghandy with dissolve
            mc "Huuuhghh...!"
            kat "What gets a woman like you going?"
            mc "H-huhh... ack...!"
            sophia "You ever give much thought to what makes your skin itch? I tend not to pontificate over my bodily responses."
            kat "Unlike me, you mean?"
            sophia "When I feel an itch, I simply scratch it."
            kat "We got that in common at least - {b}all three of us.{/b}"
            sophia "Stop distracting me. I'm trying to watch--"
            kat "Oh, look at them stretch!"
        else:

            scene w3_2324 with dissolve
            kat "It didn't take long for Rosalind to become comfortable with the situation, did it?"
            scene w3_2325 with dissolve
            "In my current over-cooked state, what was playing out on the television screen was a muddled mess of pixels that barely registered meaning to me."
            scene w3_2326 with dissolve
            kat "Sluts like her sure are adaptable. It's a strength, but it can be a little boring when they're totally obedient."
            scene w3_2327 with dissolve
            mc "She... ah..."
            scene w3_2328 with dissolve
            sophia "Unlike Lynch?"
            scene w3_2326 with dissolve
            kat "Exactly! Ah, I love it! I really do love Miss Lynch. I wish I had more than a month with her."
            kat "Still, it should be fun to watch Mrs. Carter let loose. Of course, she'll justify it was done under instruction, but she won't be able to hide her enjoyment of this from the other two."
            scene w3_2328 with dissolve
            sophia "You have a {i}unique{/i} sense of aesthetics, Kathleen."
            scene w3_2329 with dissolve
            kat "Well, what do you find hot, Miss Lundgren? I'm genuinely curious... what gets a woman like you going?"
            scene w3_2328 with dissolve
            sophia "You ever give much thought to what makes your skin itch? I tend not to pontificate over my bodily responses."
            scene w3_2329 with dissolve
            kat "Unlike me, you mean?"
            scene w3_2330 with dissolve
            sophia "When I feel an itch, I simply scratch it."
            kat "Oh, lovely, at least we have that in common."
            sophia "Stop distracting me. I'm trying to watch--"
            kat "Oh, look at them stretch!"

        scene w3_2614 with pixellate
        ver "Hnngg, w-what the fuck?! My- ahh... p-pulling- hnhnn!"
        "Back on screen, Rosalind had selected an interesting tool and had carefully suctioned them around Veronica's pale teats."
        ver "HHh-hhh... ff-"
        scene w3_2615 with vpunch
        ver "Woooaoahhhnnn--"
        scene w3_2616 with dissolve
        rose "Two pumps. Let me know when to stop."
        ver "Stohh--"
        scene w3_2617 with vpunch
        ver "Hnnggh, hhkhk-ooohwwah--"
        scene w3_2618 with dissolve
        rose "Three."
        ver "Stop! It feels like my tieiits--"
        scene w3_2619 with vpunch
        ver "Hngngg, y-you cunt!"
        scene w3_2620 with dissolve
        rose "Sorry, Veronica."
        rose "One more than is comfortable is adequate punishment. This is-"
        ver "Hheee-ehheu-♥"
        scene w3_2621 with dissolve
        rose "Well, you seem taken care of on both ends."
        ver "W-wwhaaeeeuch...♥"
        scene w3_2622 with dissolve
        kat "Oh my. No edging into things."
        scene w3_2621 with dissolve
        rose "I should move on to Felicia now."
        scene w3_2623 with dissolve
        kat "The constant pull on her breasts and the ceaseless ribbed vibration on her sex might just end up breaking her in this state."
        scene w3_2624 with dissolve
        fel "E-hhuhhh...? Ah... fuck, what do you have in store for me?"
        scene w3_2625 with dissolve
        rose "That's a good question. The way you're set up kinda limits my options..."
        scene w3_2626 with dissolve
        ver "Hnngg, hhaaa- sghbh--"
        scene w3_2627 with dissolve
        fel "Hnng, w-whatever, j-just... d-do something! I'm dying-"
        scene w3_2628 with dissolve
        rose "Hold that thought."
        scene w3_2629 with dissolve
        rose "I read about this in a book once."

        if w3HagHandie == True:
            stop ambient
            scene br_haghandy3_a with pixellate
            show br_haghandy3 with dissolve
            fel "...eh?! What are you going to do with that?!"
            kat "I'm surprised you haven't soiled my hand yet."
            mc "Hnngg!"
            kat "I know one time won't suffice. You don't have to fear; I'll milk you as much as you require~"
            "At this point, a stiff breeze would have gotten me off, but for how slow it was, the old woman's technique was thorough and {i}immaculate{/i} in its consistency. She never slowed down or sped up; she just jerked me like her wrist operated on a piston."
            mc "G-ahh, s-shut the fuck up and just k-keep--!"
            "The real magic lay in how she used her pinky, tracing its black nail up and down the underside of my shaft, never deviating a single millimeter from the same tract of overwrought nerve endings."
            kat "*Whisper* You should speak kindly to someone doing you a favor, [mcf]."
            mc "*Gulp* H-a, haa... favor...? Yeah right..."
            "It was like the words apparated on my lips without even being thought of. I said what I felt without control or filter."
            mc "T-take a sit and spin on it if you really want to do me a favor!"
            kat "You're adorable right now, you know that?"
            fel "G-ggah, get that the fuck away from me!"
            rose "Relax, Sweetie, you don't think I'd actually..."
        else:
            stop ambient
            scene w3_2344 with pixellate
            fel "...eh?! What are you going to do with that?!"
            scene w3_2345 with dissolve
            kat "What a surprise. I didn't think she would use that."
            mc "Hhhngg...?"
            scene w3_2346 with dissolve
            "With the way I counted it, I had a couple of options for managing my sickening arousal."
            "I could let my mind wander, try to think of something else... but invariably, my senses fell on the women next to me, to the curves of their busts and their waists..."
            scene w3_2347 with dissolve
            "These two women were so far above me... the old woman decades my senior. Sophia, a brilliant scientist... it was so easy to imagine the delight in grabbing one of them right now and just--"
            mct "(Y-yeah... no... I should focus on what's playing out in front of me...)"
            "The other option was to let Kathleen's game preoccupy my attention."
            scene w3_2348 with dissolve
            kat "A-aah..."
            mct "(...that's gotta be the best way of dealing with this, right?"
            kat "Do you need to be excused, Mr. [mcl]? Perhaps you need to go to the bathroom?"
            scene w3_2349 with dissolve
            mc "N-no, I'm f-fine..."
            scene w3_2347 with dissolve
            "She teased me, and strangely, I felt an unusual rush of pride. Of course, it was irrational, but that would be akin to losing..."
            "Losing what and to who, I did not know... but my willpower... I was stronger than this..."
            mct "(I ain't a fucking animal... right?)"
            scene w3_2350 with dissolve
            fel "G-ggah, get that the fuck away from me!"
            rose "Relax, Sweetie, you don't think I'd actually..."


        scene or_felfire_a with pixellate
        show or_felfire with dissolve
        rose "...burn you do you? No way! This is just..."
        fel "What kind of fucking books do you read?!"
        rose "Eh...? Oh, it's... just something another mom recommended..."
        fel "Yeah, right! You perverted cow! Is this the kind of shit you're into?"
        rose "I don't like that insinuation, nor the tone in your voice..."
        fel "The tone in MY voice?! Fuck you! You're the one-- aahh- s-shit, that's fucking w-warm!"
        rose "Well, that IS the point, hun... but it's not hurting you, is it?"
        fel "H-huh...?! N-no... I g-guess not... it actually feels kinda... my s-skin is-- a-aahh...!"
        fel "Ah, hhnngg it must be this shit Kat gave me... it f-feels like a massage?"
        rose "Oh, good!"
        fel "Y-you're surprised?!"
        scene w3_2630 with dissolve
        rose "Well, this is the first time I've actually done this!"
        fel "G-gahh-!"
        scene w3_2631 with dissolve
        rose "It's supposed to be like an intense but relaxing massage... one that might leave your skin, or in this case your nipples, a little agitated..."
        fel "A-aahh-♥ You d-damn freak!"
        scene w3_2632 with dissolve
        rose "Don't be rude. This is part of the exhibition."
        scene w3_2633 with dissolve
        fel "Bullshit, there's a WHOLE lot of shit on the table and you picked-"
        scene or_feltitpad_a with dissolve
        show or_feltitpad with dissolve
        fel "Ghh, hnng, f-fuuuuck!"
        fel "G-, aaahn, hhhngg--"
        fel "Nueeeueuhh--"
        scene w3_2634 with dissolve
        fel "G-gah, w-what the fuck?! That... h-hnngg...! F-fuck me, why did I almost cum from that?"
        scene w3_2635 with dissolve
        rose "Maybe it's because you're the perverted one, Felicia."
        rose "I'm not the one doing this for--"
        scene w3_2636 with dissolve
        ver "Ghh-hhhnngg, hhaaa-- it, eehhhn waahhnt sttthhhoop--"
        scene w3_2637 with dissolve
        ver "Gguuuhhaahhh- sbnnbbbuuuzzzh--"
        scene w3_2638 with dissolve
        rose "I'm not the one doing this for fun or pretending like I'm too good to be here."
        scene w3_2639 with dissolve
        fel "W-what...?"
        scene w3_2640 with dissolve
        rose "Both of you are so damn annoying. You, for obvious reasons and even Veronica is..."
        scene w3_2641 with dissolve
        ver "GUgg-hhhnngg♥♥♥"
        scene w3_2642 with dissolve
        rose "I swallow my pride and she runs her mouth, saying what I'm thinking. It makes me feel..."
        scene w3_2643 with dissolve
        fel "How do you really feel, you two-faced bitch?"
        scene w3_2644 with dissolve
        rose "You got me figured out, don't you, hun?"

        if w3HagHandie == True:
            scene br_haghandy3_a with pixellate
            show br_haghandy3 with dissolve
            kat "It's always interesting when you give a woman like Rosalind the opportunity to take the reins. They're so stressed, pent up, inhibited..."
            play sound "sound effects/slap3.wav"
            fel "Guh, hhnng, s-shit!"
            kat "They don't show you their true colors as much as their whole color palette blends together in one fucked up mix. I wonder where this will go."
            mc "H-hhhhngg...!"
            "Like hell my mind was registering any of her bullshit right now."
            ver "H-heuuuh?! Y-you're gonna use t-that t-too?!"
            scene w3_2373 with dissolve
            sophia "You counted on this kind of... {i}fervor{/i}?"
            scene w3_2374 with dissolve
            mc "H-a, hnnggaa..."
            "The inside of my head was mush right now. My capacity for language was utterly eroded."
            scene w3_2375 with dissolve
            kat "I've been doing this for a long time. Before the club, I had my {i}other{/i} enterprises."
            kat "I'm well acquainted with the peculiar ways people in desperate situations respond. In a way, it's a more potent means of control than any drug."
            scene w3_2376 with dissolve
            sophia "I'm actually impressed for once."
            scene w3_2377 with dissolve
            kat "You shouldn't be. I'm an amateur when compared to someone like your owner."
            kat "I think the way Van Doren has you under his thumb is much more impressive."
            scene w3_2376 with dissolve
            sophia "Thank you."
            scene w3_2377 with dissolve
            kat "You took that as a compliment?"
            scene w3_2376 with dissolve
            sophia "Of course I did. Abel only has the best things."
            scene w3_2379 with dissolve
            kat "Your self-awareness in your choice of words is commendable, dear."
        else:

            scene w3_2381 with dissolve
            kat "It's always interesting when you give a woman like Rosalind the opportunity to take the reins. They're so stressed, pent up, inhibited..."
            play sound "sound effects/slap3.wav"
            fel "Guh, hhnng, s-shit!"
            kat "They don't show you their true colors as much as their whole color palette blends together in one fucked up mix. I wonder where this will go."
            scene w3_2382 with dissolve
            "To my annoyance, whenever one of them spoke, my attention would turn back to just how fuckable the women next to me were. "
            ver "H-heuuuh?! Y-you're gonna use t-that t-too?!"
            scene w3_2383 with dissolve
            sophia "You counted on this kind of... {i}fervor{/i}?"
            scene w3_2382 with dissolve
            mct "(Christ, I want to make that mouthy hag choke on my dick until she passes out!)"
            "Intrusive thought upon intrusive thought flooded my head."
            scene w3_2384 with dissolve
            kat "I've been doing this for a long time. Before the club, I had my {i}other{/i} enterprises."
            kat "I'm well acquainted with the peculiar ways people in desperate situations respond. In a way, it's a more potent means of control than any drug."
            scene w3_2383 with dissolve
            sophia "I'm actually impressed for once."
            scene w3_2385 with dissolve
            kat "You shouldn't be. I'm an amateur when compared to someone like your Master."
            kat "I think the way Van Doren has you under his thumb is much more impressive."
            scene w3_2386 with dissolve
            sophia "Thank you."
            scene w3_2387 with dissolve
            kat "You took that as a compliment?"
            scene w3_2386 with dissolve
            sophia "Of course I did. Abel only has the best things."
            scene w3_2387 with dissolve
            kat "Your self-awareness in your choice of words is commendable, dear."

        scene or_feltitpad_a with pixellate
        show or_feltitpad with dissolve
        fel "Ghhu, hnhng-♥"
        fel "Hnngg, hh-aaa-♥♥"
        fel "D-damn, it, gaaa♥♥♥"
        fel "W-what the f-fucckkhhh iswwrrggon♥♥♥♥"
        scene w3_2645 with dissolve
        fel "Wtrrrrornnggggweeethmeeeeee♥♥♥♥♥"
        rose "Wow..."
        scene w3_2646 with dissolve
        fel "Guhh, hh-aaa, d-did I just...?"
        rose "You came."
        fel "Ah- w-why am I still...?"
        scene w3_2647 with dissolve
        rose "I wanted to see if I could get you to with just your chest, but I didn't think it would be that easy..."
        rose "Me? I've always been so sensitive up top that I've been curious..."
        scene w3_2648 with dissolve
        fel "Oh...you're enjoying this. I don't actually care, I'm not j-judging you... I'd just love to hear you admit it."
        scene w3_2649 with dissolve
        ver "Huggg---aahh, wwwhooooaoahh--♥♥♥♥♥♥"
        ver "Guh, hhgguu--♥♥♥♥♥♥"
        scene w3_2650 with dissolve
        rose "Enjoying {i}this{/i}? I can honestly say I'm not."
        rose "I'm just happy to be on this side of things for once."
        scene w3_2651 with dissolve
        rose "You're still burning up, aren't you?"
        fel "H-hhuhh, aa-ahh..."
        scene or_ronfcrime1_a with dissolve
        show or_ronfcrime1 with dissolve
        fel "Guuaah-? Hnnng-♥ Y-you already tested your hypoth--"
        rose "*Shlurhp, shhwwwup, chwup~* Woohhh-♥♥"
        kat "Looks like she's done talking."
        fel "Gaah, hhnng-♥ W-wooaohhh-hhnnggg-- I'm-"

        scene w3_2652 with dissolve
        ver "Gguuphphh- hhngg, hgauuuh♥♥♥♥♥"
        ver "Ehhh--hhnngg♥♥♥"
        scene or_ronfcrime2_a with dissolve
        show or_ronfcrime2 with dissolve
        fel "GHhh, hhhu♥♥♥♥♥♥ Fghh-"
        "A delirious concert of fuck-numbed sounds flooded both the room they stood in and where we sat."
        fel "Wwhh, hhhnnggg- wwowoohh♥♥♥ *Slwhhup, chup, khwwuup!*"
        "Rosalind used the paddle in a much more tender and devious way, prying apart and rubbing the blonde's pink insides."
        fel "HHuugg-hhhaaat♥♥♥"
        "It was her own miniature version of Felicia's game from the last exhibition."
        fel "Www--aahhhhhheeeoo♥"
        "If she intended it to mirror that, Rosalind was really quite devious."
        "*Slwhhup, chup, khwwuup!*"
        "The sight was pitiful and sad, but even without being under the influence as I was, this sight was..."
        fel "Guhh-hhukk-! HHwwwwoho♥♥♥♥"
        "It was the kinda sight that moved me."
        mc "G-ghhuuh!"

        if w3HagHandie == True:
            scene w3_2407 with pixellate
            kat "I'm starting to get offended, Mr. [mcl]. Does my hand not suffice?"
            kat "Don't you want to taste release?"
            scene w3_2408 with dissolve
            mc "G-gah, f-fuck! It's not like I have any control over it!"
            sophia "Hmm..."
            scene w3_2409 with dissolve
            "Every fiber of my being desperately anticipated climax. My reason had been eroded and my purpose replaced by the critical need to expunge every trace of nauseating desire from my body through my cock."
            "The hairs on my arm stood on end, the feeling in my extremities came and went like the tide, and a pervasive tingling feeling floated from my neck down to my tailbone - by all means, my body told me that I {b}should{/b} be coming."
            scene w3_2410 with dissolve
            sophia "Interesting."
            scene w3_2409 with dissolve
            "But I wasn't. My bloated dick burned against the soft palm of the old woman's hand, pulsating and twitching from the ceaseless stimulation, filling me with the irrational fear that I might literally explode if I didn't soon go careening into the void of sexual release."
            scene w3_2411 with dissolve
            sophia "All things considered, he is showing a {b}surprising{/b} degree of longevity..."
            scene w3_2412 with dissolve
            kat "Maybe your fragrance isn't as effective as you think it is."
            mc "G-gaahh!"
            scene w3_2411 with dissolve
            sophia "Maybe..."
            scene w3_2413 with dissolve
            mct "(No! It was definitely fucking effective!)"
            sophia "...but unlikely. Hey, [mcf]..."
            scene w3_2414 with dissolve
            "Through lidded eyes, I could sense the blonde scooching closer and closer."
            scene w3_2415 with dissolve
            sophia "The issue is that a young, well-traveled guy like you simply can't get off on an old woman's touch, right?"
            scene w3_2416 with dissolve
            mc "That's not--"
            scene w3_2417 with dissolve
            sophia "{b}{i}Isn't it?{/b}{/i}"
            "Even in my lust-addled state..."
            scene w3_2418 with dissolve
            "My brain registered amazement over the willful way Sophia flipped the switch, going from detached aloofness to a man-killer just as easily as one would shed their clothes. "
            scene w3_2419 with dissolve
            mc "Hnngg...!"
            kat "*Scoff* Feeling left out, were you?"
            sophia "Give them a comparison."
            scene w3_2420 with dissolve
            "My hand responded independently, sinking into the pleasant give of the doctor's tit-flesh in an instant as what remained of my faculties disappeared into the whirlpool of her eyes."
            sophia "You got a mess lurking somewhere in there that you want to get out?"
            mc "Ha... hnngg...! F-fuck it!"
            scene w3_2421 with dissolve
            sophia "...?!"
            "I kissed her, just as you'd expect a man on the brink of starvation to steal a loaf of bread."
            scene br_hhplus_a with dissolve
            show br_hhplus with dissolve
            sophia "Mmmhhhh....!"

            if kat_polite == True:
                "She might not have expected it or even wanted it, but she quickly accepted it as a consequence of the \"just a bit of chaos\" she wielded in her joust against Mrs. Pulman."
            else:
                "She might not have expected it or even wanted it, but she quickly accepted it as a consequence of the \"just a bit of chaos\" she wielded in her joust against Kathleen."

            kat "H-hey, ahh--"
            "Spurred on by having the attention of two beautiful women, even if it was just the fucked up equivalent of cooking ants with a magnifying glass to them, I knew it wouldn't be long until I finally had my release."
            kat "Gah, ah... ha... hmpfh."
            "Although I could feel her eyes on my neck, the old woman continued to milk me."
            "*Cwhup, fwhup, chwup...!*"
            kat "I've somehow ended up feeling like a third wheel."
            "I pawed at both women's breasts with a virgin-like fervor, wholly enamored by an opportunity I might never get again."
            mct "(The head of a charity and a world-class scientist... ha, fucking sluts!)"
            "I felt like a king, not of my own making of course, but my brain was so cooked as to not know the difference. Thinking was hard, but what few thoughts I could miraculously formulate were like tidal waves breaking against the shore."
            mct "(Who the hell do you think you're fucking with? You think you can toy with me just because of money?!)"
            "I felt smothered, suffocated, and hot. More akin to a wick that was about to burn out than a human being."
            mct "(I'M A GUINEA PIG TO YOU?!)"
            "Every sensation felt heightened, and every second felt prolonged... I genuinely feared that the moment I popped would be when I was snuffed out."

            mct "{size=+30}{font=/gui/fonts/MB-Thin_Worms.ttf}(You like to toy with pe-){/font}{/size}"


            "My brain gave out, but if I ceased to exist after this, I instinctively knew one thing: these last minutes of my life should be bold."

            menu:
                "Goad the old woman into letting you finish in her mouth.(w3KatPromoFinish = True)"(chg=["kathleen_trust_up"]):
                    $ w3KatPromoFinish = True
                    $ Kathleen_Trust += 1
                    scene w3_2422 with dissolve
                    mc "I'm about to b-blow..."
                    kat "You don't need my permission."
                    scene w3_2423 with dissolve
                    mc "Can you finish me with your mouth?"
                    kat "Hmmmmm, not going to happen."
                    mc "A-ah, pretty please? With a cherry on top?"
                    scene w3_2424 with dissolve
                    kat "Why don't you ask Miss Lundgren to do it?"
                    mc "...because I want you, Ma'am."
                    scene w3_2425 with dissolve
                    kat "...hmmmmmmmm. You have the eyes of a crazed animal, yet..."
                    scene w3_2426 with dissolve
                    kat "You're asking so nicely. God, I love that."
                    scene w3_2427 with dissolve
                    "She smirked like she had won against me, and perhaps even against Sophia."
                    scene w3_2428 with dissolve
                    kat "It really is goddamn adorable. Ask me again, [mcf]."
                    scene w3_2429 with dissolve
                    "A desperate, cloying urge inside me told me her mouth was the only place I wanted to be right now and if it took a bit of pleading to get me into a position where I could fill that mean bitch's stomach with my seed, then so be it."
                    scene w3_2430 with dissolve
                    mc "Hhh, haa... would you PLEASE finish me with your mouth, Mrs. Pulman?"
                    scene w3_2431 with dissolve

                    if kat_polite == True:
                        "Without another word, Mrs. Pulman lowered herself and..."
                    else:
                        "Without another word, Kathleen lowered herself and..."

                    scene br_hhplus_hbj_a with dissolve
                    mc "G-gah...!"
                    "The moment her lips wrapped themselves around my cock, I felt like I might pass out."
                    "Her seal was so airtight that her mouth felt like an oven. Steady puffs of hot breath passed over the head of my cock as it made its way out through her nose."
                    scene br_hhplus_hbj_a with dissolve
                    show br_hhplus_hbj with dissolve
                    mc "F-fuck, damn it!"
                    "*Shwuck, fgwhhuck, thwuuuck!*"
                    "What little air could escape from her hold transformed into {b}obscene{/b} noises as she inched herself up and down my shaft."
                    mc "H-holy-!"
                    "The running narration in my head was a jumbled mess, but through all the muddied noise from the pleasure soaking into my brain, I grasped a simple truth."
                    mc "Hnnng, you've sucked a lot of cock in your time, haven't you?!"
                    "*Thwaahp, fwhap, swhhuck~!*"
                    "The answer to that question played across my glans every time I wedged myself comfortably in her throat with zero fuss."
                    "Swhuck, hhhwhuck, fhhggguuk!*"
                    "{b}Damn it!{/b} A rich woman like her had no business sucking dick this well."
                    mc "Ghhn, haaat, hnnngg...!"
                    "She sucked me with the skill of a woman who had {b}nothing{/b} to her name."
                    kat "Mmmhm, hhmhm~"
                    "Just like her hand job, there was no wasted effort. She didn't tackle it in a clumsy frenzy, nor did she need to cautiously get used to my size."
                    "*Shwhuhuck, fwhhucuk, ghhwhuhuk!*"
                    "She sucked me like she had been sucking {b}my{/b} dick her whole life, pleasuring me at a steady and comfortable pace. I marveled at how, through a mere blowjob, a woman so cold and cruel could instantly imprint herself on my body as warm and welcoming."
                    "I was quickly understanding that \"adorable\" disparity she had just spoken."
                    mc "Hnng, h-how?!"
                    sophia "It's not performing brain surgery."

                    if kat_polite == True:
                        "{b}There{/b} was another perverse delight, speeding me toward my climax. Sophia's attention was on the back of Mrs. Pulman's head, watching intently as she debased herself in pursuit of degrading me."
                    else:
                        "{b}There{/b} was another perverse delight, speeding me toward my climax. Sophia's attention was on the back of Kathleen's head, watching intently as she debased herself in pursuit of degrading me."

                    mct "(Haaaa... hope you like the show, bitch. You're the impetus for this.)"
                    "*Fwhhuck, ghhhukh, khggguuhhk*"
                    mc "Ahh... y-you dick swallowing--! Hnnngg...!"
                    "It was coming."
                    scene w3_2432 with dissolve
                    mc "You think I'm adorable?!"
                    "I was moments from blowing my load, and with it, the indignation from earlier swelled in me. I had wanted a bold finish before I met my end, and well..."
                    mct "(I'll show you adorable!)"
                    stop music
                    scene br_hhplus_gulp1_a with vpunch
                    mc "I'm c-cumming, fucking drown in it, you damn--"
                    play sound "sound effects/spurt.wav"
                    with flash
                    kat "Mmmmh?!"
                    "Before she could even register what was happening, ropes of piping hot cum barreled down her esophagus on a one-way trip to her stomach."
                    play ambient "sound effects/fel2.wav"
                    scene br_hhplus_gulp1_a with dissolve
                    show br_hhplus_gulp1 with dissolve
                    play sound "sound effects/spurt.wav"
                    with flash
                    kat "Ghhkka, hkkaa-!"
                    "I pressed down hard, holding the old woman's head in place as she gargled my seed in abject surprise."
                    mc "Hnngg, all of it!"
                    "I pressed down so hard it hurt my groin."
                    play sound "sound effects/spurt.wav"
                    with flash
                    kat "Ghhuk, hhuuuh, hwwwhuuuck...!"
                    "It was massive, like I was cumming my very soul down the old woman's throat."
                    kat "Ghuk, khak, uuhhk-!"
                    mc "Gah, c-choke on it!"
                    play sound "sound effects/spurt.wav"
                    with flash
                    "Not all of my load was making its way down her throat. To my perverse glee, I could {i}feel{/i} myself coating the lining of her throat."
                    kat "Ghhuk, hhuuuk...!"
                    scene br_hhplus_gulp2_a with flash
                    show br_hhplus_gulp2 with dissolve
                    play sound "sound effects/spurt.wav"
                    with flash
                    mc "Hope you like the fucking taste!"
                    kat "Mmmh, hhhngg?!?!"
                    sophia "I don't think she can breathe..."
                    mc "Good! She can breathe when I'm fucking--!"
                    stop ambient fadeout 4.0
                    play sound "sound effects/spurt.wav"
                    with flash
                    ".........!"
                    play sound "sound effects/spurt.wav"
                    with flash
                    "......!"
                    scene w3_2433 with dissolve
                    mc "A-aahh...!"
                    scene w3_2434 with dissolve
                    kat "Ugghhuhh..."
                    scene w3_2435 with dissolve
                    "Peace."
                    "Serenity."
                    "Satisfaction."
                    "In this moment, I had it all."
                    scene black with w20
                    "With that, I happily died. The oblivion I felt nipping at my heels finally sank its sharp teeth into my throat."
                    "............"
                    "........."
                    "......"
                    "..."
                    kat "Why are you holding your hands out like that? It's weird."
                    mct "(Ah, fuck... I {i}wasn't{/i} dead? {b}Oh no.{/b} Then that meant I just...)"
                    scene w3_2436 with w9
                    sophia "She's right. It's distracting."
                    scene w3_2437 with dissolve
                    "I didn't know how long I was out of it, but by the time I opened my eyes, the two women had collected themselves, and what I thought was a bold display of defiance was made pitiful and wholly expected by their bemused faces."

                    if kat_polite == True:
                        "Mrs. Pulman looked {i}totally{/i} unaffected by my rough treatment, showing no signs of having mercilessly guzzled my cum just moments ago..."
                    else:
                        "Kathleen looked {i}totally{/i} unaffected by my rough treatment, showing no signs of having mercilessly guzzled my cum just moments ago..."

                    scene w3_2438 with dissolve
                    kat "Oh, by the way... you said some pretty outlandish things to me."
                    scene w3_2439 with dissolve
                    mc "If I recall, I did a bit more than that..."
                    scene w3_2440 with dissolve
                    kat "It was {b}adorable{/b}."
                    "She had indeed won."
                    ver "Ghh, hhaan, streetthhhchggingg-!!!"
                "Leave an impression on the doctor.(w3SophiaPromoFinish = True)"(chg=["kathleen_down2"]):

                    $ w3SophiaPromoFinish = True
                    $ Kathleen_Affection -=2
                    "I knew what I wanted."
                    sophia "Mmmhh, hhhhh..."
                    "And that last act of defiance would be leaving the doctor, the root cause of all this, something to remember me by."
                    scene br_hhplus_doc1_a with dissolve
                    show br_hhplus_doc1 with dissolve
                    "*Chwup, fhwup~*"
                    "I wanted to hear this aloof bitch moan, so I focused everything on the woman whose mouth I was currently exploring."
                    sophia "Mmmh, hhmmm...?"
                    "It was a battle against my wits. Sophia was literally intoxicating. Focusing my senses all on her had me burning twice as fast."
                    "By instinct, I felt her breast over her clothes."
                    sophia "Mmhh..."
                    "Her coos told me she was receptive, but it wasn't quite the noise I wanted to drag out from the blonde."
                    scene br_hhplus_doc2_a with dissolve
                    show br_hhplus_doc2 with dissolve
                    sophia "Ghu, gha~ghhuu...!"
                    "Deciding that over the clothes touching wouldn't do it, I switched focus on the erogenous zone in her mouth, intensifying my efforts in an intricate dance to subdue her tongue with my own."
                    sophia "Mmmmh, mmhhhh- *chwuph, fhwhup~*"
                    "She wasn't a passive observer in my hunt; her tongue played coy, darting away and slipping from my grasp whenever I thought I had her pinned."
                    "It was mere seconds, but--"
                    "*Chwhu, fhwwwup, chup!*"
                    "--but, in my fogged-over state, time held little sway over my perception. What was in reality a clumsy tussle felt like a long and protracted siege."
                    "I don't know if it was because of the perfume, but all bodily sensations gradually began to meld into one."
                    "The feeling of the old woman's hand milking my cock, the wet warmness of our kiss, the bubbling desire so strong that I was confident it would be the end of me..."
                    mc "Mmmh, hhhmmm-!"
                    "All of it spelled an overload melded and combined into a singular feeling of otherness. I was sure I had lost this battle until..."
                    scene br_hhplus_doc3_a with dissolve
                    show br_hhplus_doc3 with dissolve
                    "My brain registered a change."
                    mct "Was she...?"
                    sophia "Mmmh, hhmhm~aahhh...!"
                    "She was closer."
                    "She was pressing into me."
                    "She felt it."
                    "She was {b}heated{/b}."
                    "{i}She was kissing me back.{/i}"
                    "Whether it was done deliberately or on an instinctual level, her body responded favorably."
                    sophia "Ahh, hhhnnggg, mmmmhh-!"
                    "My hand found a place on her ass and I used that to spur her on even more. With this, I had physical confirmation of my success."
                    mct "(Fuck, what a great-!)"
                    "I could feel the hot dampness of her delicate spot."
                    sophia "Mmhh, hhaa...♥♥♥"
                    "She purred openly and I felt a petty relief over my trivial victory. The succubus driving me to this desperate state wouldn't escape our battle unscathed."
                    "*Chwup, fhwwup, khwwup*!"
                    "--and that wasn't the only sense of relief I felt."
                    stop music
                    play sound "sound effects/spurt.wav"
                    scene w3_2441 with flash
                    mc "{b}Hnng, ah-!!!{/b}"
                    "I didn't know when it started, but ropes of cum geysered from my cock and rained down from the sky."
                    play sound "sound effects/spurt.wav"
                    scene w3_2442 with flash
                    mc "Ghh, aaahh- sssshit--"
                    kat "Huh, {b}WOW{/b}."
                    scene w3_2443 with dissolve
                    mc "Hngg, hhhhmmmhh-~"
                    "All the suffocating vileness in me was expelled and released into the world. All my desperation spilled out onto our clothes and thighs."
                    "Soon need was replaced with..."
                    scene w3_2444 with dissolve
                    "Peace."
                    "Serenity."
                    scene w3_2445 with dissolve
                    "Satisfaction."
                    "Emptiness."
                    "The oblivion I felt nipping at my heels finally sank its sharp teeth into my throat."
                    scene black with w20
                    "I was dead."
                    "............"
                    "........."
                    "......"
                    "..."
                    sophia "Great, now we'll spend the rest of the show reeking of semen."
                    mct "(Ah, fuck... I {i}wasn't{/i} dead? {b}Oh no.{/b} Then that meant I just...)"
                    scene w3_2446 with w9
                    kat "You should've thought of that before you entered the crossfire."
                    scene w3_2447 with dissolve
                    sophia "You were taking too long. I wanted to put an end to the distraction."
                    scene w3_2448 with dissolve
                    "I didn't know how long I was out of it. Still, by the time I opened my eyes, the two women had collected themselves. The damage I thought I had done to Sophia with my counter-attack was made pitiful by their bemused faces."
                    scene w3_2449 with dissolve
                    kat "Oh, please. Are those the kind of sounds you make matter-of-factly?"
                    scene w3_2450 with dissolve
                    "Sophia looked as composed as ever, and except for a little blush, her attention turned back to the Carnations."
                    scene w3_2451 with dissolve
                    kat "I hope that provided you a measure of relief, Mr. [mcl]. That certainly was an... {i}explosive{/i} finish."
                    mc "A, ahem... thaaaaaanks?"
                    scene w3_2452 with dissolve
                    kat "Don't mention it. It was... interesting."
                    ver "Ghh, hhaan, streetthhhchggingg-!!!"
        else:

            scene w3_2453 with dissolve
            mc "........."
            mc "......"
            stop music
            play sound "sound effects/record-scratch.wav"
            scene w3_2454 with dissolve
            "...this was my limit."
            $ renpy.end_replay()
            scene w3_2455 with dissolve
            mc "Aaeeh, I'll be riiiiiight back."
            scene w3_2456 with dissolve
            "......"
            scene w3_2457 with dissolve
            "..."
            scene w3_2458 with dissolve
            kat "Is that a milder scent you are wearing?"
            sophia "It's the same batch as the bottle I gave you."
            scene w3_2459 with dissolve
            kat "The effect seemed... less? Why's that?"
            scene w3_2460 with dissolve
            sophia "It's possible that his body adapted and partially metabolized the odor molecules. All I can say is that it's remarkable he held out that long."
            sophia "It could be a matter of willpower."
            scene w3_2461 with dissolve
            kat "When I had dinner with Charles the other night, he didn't even flinch."
            scene w3_2462 with dissolve
            sophia "Dr. Kohler is a scary man."
            scene w3_2463 with dissolve
            kat "Is that your appraisal after demolishing him game after game?"
            scene w3_2464 with dissolve
            sophia "How else should I describe a man who has no need but keeps his passions tightly controlled."
            scene w3_2465 with dissolve
            kat "That's why he and I are incompatible. He treats fucking like it's Christmas."
            kat "You don't have anything to worry about as long as you don't lose."
            scene w3_2466 with dissolve
            sophia "I don't plan on it, but I have a feeling he eventually wins one way or another."
            scene w3_2459 with dissolve
            kat "Abel wouldn't let it come to that, would he?"
            scene w3_2467 with dissolve
            "......"
            "..."
            scene w3_2460 with dissolve
            sophia "Thank you for indulging my little whim, Kathleen. It was amusing."
            scene w3_2459 with dissolve
            kat "Don't mention it. One should make their own fun in life. Still..."
            kat "...you're very competent. Don't you ever desire more?"
            scene w3_2468 with dissolve
            sophia "A frivolous bitch like you has no business saying that to me."
            scene w3_2469 with dissolve
            kat "Ah, fuck. There it is."
            scene black with fade
            kat "I almost felt sorry for you."
            jump w3WashRoom

        play music "music/landing.ogg"
        scene w3_2653 with pixellate
        ver "Hnngguuhh..."
        scene w3_2654 with dissolve
        fel "Hwhuuck, hhnanaa.."
        scene w3_2655 with dissolve
        rose "Wow... ahah..."
        rose "I don't smoke, but I feel like I should have a cigarette..."
        scene w3_2656 with dissolve
        ver "Ahhwwhh-"
        fel "Wwhhhaah- hnnn..."
        rose "Are you girls holding up alright?"
        scene w3_2657 with dissolve
        ver "Hnngg.. haa... w-what the fuck do you think?"
        scene w3_2658 with dissolve
        rose "I don't think it's over until Mrs. Pulman returns, but... I'd say a little break is in order."
        scene w3_2659 with dissolve
        fel "Y-you were j-juust s-shoving a paddle up my cooch and now you're playing n-nice? Goddamn it..."
        scene w3_2660 with dissolve
        rose "I--"
        scene w3_2661 with dissolve
        fel "F-for the love of God... p-please don't say this is part of the game again... f-fuck... hnnh... t-the itch is starting again...?"
        scene w3_2662 with dissolve
        ver "Ghha, hhaa... s-shit... you just left me hanging t-there?"
        scene w3_2663 with dissolve
        rose "Ahehe... there's only one of me."
        scene w3_2664 with dissolve
        ver "G-gah, you said I was annoying...?"
        rose "You remember that...?"
        scene w3_2665 with dissolve
        ver "Y-you think I'm no better than Blondie?"
        scene w3_2666 with dissolve
        rose "I didn't say {i}that{/i}..."
        fel "Y-yeah, she said you run your mouth, acting like you're better than everyone else!"
        rose "I didn't mean it like that, I..."
        scene w3_2665 with dissolve
        ver "Bah! So what if I do, we all have our fucking pretenses here! Rosie's m-mousey s-shit is just as annoying as my dumb bravado!"
        scene w3_2666 with dissolve
        fel "O-ohh, s-so you're aware of how you sound?!"
        scene w3_2665 with dissolve
        ver "Even if it's fucking futile, it's something, right? Both of you l-left me hanging when I tried to get ALL of us paid earlier! All of us!"
        scene w3_2666 with dissolve
        fel "It was deluded!"
        scene w3_2665 with dissolve
        ver "So what?! Of course it is! I wasn't expecting it to work!"
        scene w3_2667 with dissolve
        rose "If you know that, why do you draw Mrs. Pulman's ire then...?"
        scene w3_2668 with dissolve
        ver "......"
        scene w3_2669 with dissolve
        ver "...h-ow could I not?"
        scene w3_2670 with dissolve
        fel "You're making it purposefully harder on yourself? Stop being stupid!"
        scene w3_2671 with dissolve
        ver "I don't want to hear that from you, bitch."
        scene w3_2670 with dissolve
        fel "Well, you're hearing it!"
        scene w3_2672 with dissolve
        ver "Even if you're going to get your ass kicked... ahaa-- hnngg- hnnn-- you..."
        ver "...you don't just put your guard down and make it easy for them."
        ver "You just... {b}don't{/b}."
        scene w3_2673 with dissolve
        rose "......"
        rose "..."
        scene w3_2674 with dissolve
        rose "We should begin again."
        scene w3_2675 with dissolve
        fel "H-hhaaa... I think you struck a n-nerve with her..."
        scene w3_2676 with dissolve
        rose "Shut up, Felicia."
        scene w3_2677 with dissolve
        rose "You asked me if I actually found you annoying? If I put it mildly, it's not you; this whole thing is an annoyance."
        rose "When it comes to you or Felicia, I actually don't think much about either of you."
        scene w3_2678 with dissolve
        rose "What do I care if you're here for frivolous reasons?"
        scene w3_2679 with dissolve
        rose "Why would I give a damn about putting up a fight just to make myself feel better?"
        scene w3_2680 with dissolve
        ver "That's not what I was saying!"
        scene w3_2681 with dissolve
        rose "I know, hun. What I'm saying, though, is... there's only one thing important to me."
        play sound "sound effects/vib-start.wav"
        "Bzzzt, bzzzt!"
        stop music fadeout 3.0
        scene black with fade
        rose "So I gotta do a good job."
        jump w3WashRoom

    if w2ExLosersAll == True:
        scene w3_2682 with pixellate
        ver "It's kinda fucking weird being on this side of things... h-hhhnn, f-fuck, I'm feeling crazy..."
        scene w3_2683 with dissolve
        ver "I f-feel like I lose no matter what I do here."
        scene w3_2684 with dissolve
        rose "T-that's... uh... wow..."
        scene w3_2685 with dissolve
        rose "I d-don't have any that looks like that."
        ver "You like the looks of it, eh?"
        scene w3_2686 with dissolve
        ver "......"
        scene or_veromast_a with dissolve
        show or_veromast with dissolve
        ver "..."
        rose "W-what are--?"
        ver "A-ah, w-what am I doing? Fuuuuck... you're pretty... g-gahh...♥ T-total, {b}major{/b} MILF."
        rose "U-mmm... t-thanks...?"
        fel "H-hurry up! You're not the only one going crazy!"
        ver "Shut up, Blondie! This was meant to be a punishment, so you'll wait as long as I say."
        fel "G-aah, cooohm ooooon!"
        scene w3_2687 with dissolve
        ver "Hnnngg-♥"
        scene or_veromast_a with dissolve
        show or_veromast with dissolve
        ver "Why do I feel like not myself and completely like myself at the same time?"
        ver "I d-don't know which it is... or--hhnn! Or... if I hate it or love it..."
        fel "All I feel like is I need a cock more than I have my entire life?"
        ver "So a normal Monday for you, then?"
        rose "H-haa, aa-ck, s-shoot... d-don't make me laugh..."
        fel "Fuck you, don't just stand there!"
        ver "The more you complain...♥ Ahh-hhha...♥ The more I'm just going to leave you sitting there and focus on Rosie."
        fel "Earth to meathead! You're not even doing anything to her!"
        ver "Ahhh s-shit, I'm not, am I...?"
        scene w3_2688 with dissolve
        ver "S-suck on it. This is going in you."
        rose "Ah... I'm a-already so... ah... I don't think it'll have any trouble sliding in..."
        ver "I don't care. {b}I wanna see it.{/b}"
        scene w3_2689 with dissolve
        rose "....."
        scene w3_2690 with dissolve
        rose "A-ah--?"
        play music "music/addict.ogg"
        scene w3_2691 with vpunch
        rose "Hnngg, kuk-!"
        rose "Ah, hhhmmm-"
        play sound "sound effects/vib-start.wav"
        scene w3_2692 with vpunch
        "*Bzzz-bzzzt!*"
        rose "Hkkk, hhhuuk--aahh{b}SSSUUK?!{/b}"
        scene w3_2693 with dissolve
        ver "Hnngg... that's... {b}goddamn hot!{/b}"
        rose "HKkhuh, ghhuuhk-! {b}*cough*{/b} Gaah, hhnnk-!"
        ver "{b}SO{/b} goddamn--"

        if w3HagHandie == True:
            scene br_haghandy_a with dissolve
            show br_haghandy with dissolve
            kat "For all Miss Lynch's disdain, she does seem to be enjoying the situation, no?"
            "In my current over-cooked state, what was playing out on the television screen was a muddled mess of pixels that barely registered meaning to me."
            kat "Sluts like her are the best. I love it when they're a mess of contradictions."
            "No, in my current state, my mind was completely consumed by the old woman's grip on my cock."
            mc "H-haahaa...!"
            scene br_haghandy2_a with dissolve
            show br_haghandy2 with dissolve
            kat "I really do love Miss Lynch. I wish I had more than a month with her."
            mc "G-gahh...!"
            "The pitiful noise of a rutting animal punctuated the women's conversation."
            sophia "You have a {i}unique{/i} sense of aesthetics, Kathleen."
            kat "Well, what do you find hot, Miss Lundgren? I'm genuinely curious..."
            scene br_haghandy_a with dissolve
            show br_haghandy with dissolve
            mc "Huuuhghh...!"
            kat "What gets a woman like you going?"
            mc "H-huhh... ack...!"
            sophia "You ever give much thought to what makes your skin itch? I tend not to pontificate over my bodily responses."
            kat "Unlike me, you mean?"
            sophia "When I feel an itch, I simply scratch it."
            kat "We got that in common at least - {b}all three of us.{/b}"
            sophia "Stop distracting me. I'm trying to watch--"
            ver "S-shit, this isn't what I had in mind when I--"
        else:

            scene w3_2324 with dissolve
            kat "For all Miss Lynch's disdain, she does seem to be enjoying the situation, no?"
            scene w3_2325 with dissolve
            "In my current over-cooked state, what was playing out on the television screen was a muddled mess of pixels that barely registered meaning to me."
            scene w3_2326 with dissolve
            kat "Sluts like her are the best. I love it when they're a mess of contradictions."
            scene w3_2327 with dissolve
            mc "She... ah..."
            scene w3_2326 with dissolve
            kat "Oh, how I really do love Miss Lynch. I wish I had more than a month with her."
            scene w3_2328 with dissolve
            sophia "You have a {i}unique{/i} sense of aesthetics, Kathleen."
            scene w3_2329 with dissolve
            kat "Well, what do you find hot, Miss Lundgren? I'm genuinely curious... what gets a woman like you going?"
            scene w3_2328 with dissolve
            sophia "You ever give much thought to what makes your skin itch? I tend not to pontificate over my bodily responses."
            scene w3_2329 with dissolve
            kat "Unlike me, you mean?"
            scene w3_2330 with dissolve
            sophia "When I feel an itch, I simply scratch it."
            kat "Oh, lovely, at least we have that in common."
            sophia "Stop distracting me. I'm trying to watch--"
            ver "S-shit, this isn't what I had in mind when I--"

        play sound "sound effects/vib-start.wav"
        scene w3_2694 with pixellate
        "*Bzzzt*!"
        rose "HHnnhh...♥ Oo-oohohh...♥"
        scene w3_2695 with dissolve
        rose "It-♥♥♥"
        rose "Wooooaaah-- hnnng...♥"
        scene w3_2696 with dissolve
        ver "A-hh, h-hang in there, Rosie...♥"
        scene w3_2697 with dissolve
        play sound "sound effects/slap2.wav"
        scene w3_2698 with vpunch
        fel "U-ugh-!"
        "{b}*Swwwaaahp!*{/b}"
        scene w3_2699 with dissolve
        fel "D-damn it! Give me what she's having, at least!"
        ver "A-ahh... I'm curious just how skin as tan as yours will turn red..."
        scene w3_2700 with dissolve
        play sound "sound effects/slap3.wav"
        scene w3_2701 with vpunch
        fel "Ahh, f-f-hhhu...♥ Y-you're a real piece of work!"
        scene w3_2702 with dissolve
        fel "Despite all your bitching, you're having fun!"
        scene w3_2703 with dissolve
        ver "G-gah, hnn...♥ Maybe it's a bit hypocritical, b-buht..."
        scene w3_2700 with dissolve
        play sound "sound effects/slap3.wav"
        scene w3_2701 with vpunch
        fel "Ghhh♥"
        scene w3_2704 with dissolve
        ver "...silver linings or {b}whatever{/b}!"
        scene w3_2700 with dissolve
        play sound "sound effects/slap3.wav"
        scene w3_2701 with vpunch
        "*Thwap!*"
        scene w3_2705 with dissolve
        ver "Does that feel good, you crazy slut!"
        fel "G-gah... f-fuck... {b}k-kinda{/b}...?!"
        scene w3_2706 with dissolve
        ver "Judging by h-how I'm currently feeling... with h-how much my skin is burning... I bet this thing even feels like a brief distraction and relief...♥♥♥"
        fel "Maybe it does, but I'd still rather have-"
        scene w3_2707 with dissolve
        rose "Gh, hhh--♥"
        fel "...what she's having."
        scene w3_2708 with dissolve
        ver "N-no shit...♥ Me, t-tooo...♥"
        scene w3_2709 with dissolve
        ver "I've got it worse than you guys-♥ I have two of you in front of me, l-looking like you do...♥"
        scene w3_2708 with dissolve
        ver "Hnnn...♥♥♥ But no one to h-help me f-feel... aaach...♥ {b}D-damn it!{/b}"
        scene w3_2710 with dissolve
        ver "{b}This is inadequate...!{/b}"
        scene black with fade
        rose "W-what are you...?"
        fel "H-hey, what about me?"
        ver "What did I tell you about waiting your turn, Blondie?"
        scene w3_2711 with dissolve
        rose "W-woaahh...? Ahh...? Don't dro--"
        ver "You think you got that to worry about with me? Don't worry, I've got you, beautiful."
        rose "B-but... aah... I don't think you were supposed to take me down... Mrs. Pulman took a lot of time setting us-"

        if w3HagHandie == True:
            stop ambient
            scene br_haghandy3_a with pixellate
            show br_haghandy3 with dissolve
            kat "I figured it might go this way."
            mc "B-bba- y-you did?!"
            kat "Of course. It's no surprise that Veronica would go off script."
            kat "The real kicker was always going to come after she comes to her senses and realizes just how easily she gives into her lust."
            mc "You are--"
            kat "What I AM surprised about is how you haven't soiled my hand yet."
            mc "Hnngg!"
            kat "I know one time won't suffice. You don't have to fear; I'll milk you as much as you require~"
            "At this point, a stiff breeze would have gotten me off, but for how slow it was, the old woman's technique was thorough and {i}immaculate{/i} in its consistency. She never slowed down or sped up; she just jerked me like her wrist operated on a piston."
            mc "G-ahh, s-shut the fuck up and just k-keep--!"
            "The real magic lay in how she used her pinky, tracing its black nail up and down the underside of my shaft, never deviating a single millimeter from the same tract of overwrought nerve endings."
            kat "*Whisper* You should speak kindly to someone doing you a favor, [mcf]."
            mc "*Gulp* H-a, haa... favor...? Yeah right..."
            "It was like the words apparated on my lips without even being thought of. I said what I felt without control or filter."
            mc "T-take a sit and spin on it if you really want to do me a favor!"
            kat "You're adorable right now, you know that?"
        else:
            stop ambient
            scene w3_2345 with dissolve
            kat "I figured it might go this way."
            mc "Y-you did...?"
            scene w3_2346 with dissolve
            "With the way I counted it, I had a couple of options for managing my sickening arousal."
            "I could let my mind wander, try to think of something else... but invariably, my senses fell on the women next to me, to the curves of their busts and their waists..."
            scene w3_2347 with dissolve
            "These two women were so far above me... the old woman decades my senior. Sophia, a brilliant scientist... it was so easy to imagine the delight in grabbing one of them right now and just--"
            mct "(Y-yeah... no... I should focus on what's playing out in front of me...)"
            "The other option was to let Kathleen's game preoccupy my attention."
            scene w3_2348 with dissolve
            kat "Of course. It's no surprise that she'd go off script."
            kat "The real kicker was always going to come after she comes to her senses and realizes just how easily she gives into her lust."
            mct "(...that's gotta be the best way of dealing with this, right?)"
            kat "By the way... do you need to be excused, Mr. [mcl]? Perhaps you need to go to the bathroom?"
            scene w3_2349 with dissolve
            mc "N-no, I'm f-fine..."
            scene w3_2347 with dissolve
            "She teased me, and strangely, I felt an unusual rush of pride. Of course, it was irrational, but that would be akin to losing..."
            "Losing what and to who, I did not know... but my willpower... I was stronger than this..."
            mct "(I ain't a fucking animal... right?)"

        scene w3_2712 with pixellate
        rose "W-w-ah-? P-put me doo--"
        ver "Ahh- relax, you're in good hands!"
        "In an exceedingly impressive display of back strength, Veronica flipped Rosalind around and had the MILF hold onto her body as if she was climbing a tree."
        scene w3_2713 with dissolve
        rose "N-neee... d-don't drop-"
        ver "You have no idea how much I want to..."
        scene or_rosaveromb0_a with dissolve
        show or_rosaveromb0 with dissolve
        rose "Ah, m-my-♥"
        "Finishing her sentence, the redhead dived into Rosalind's bust, submerging herself in a sea of sensuous tit-flesh."
        rose "{b}Haaaaa-♥{/b}"
        "With how her head bobbed and shook, you could make a pretty good guess about what was going through Veronica's mind."
        fel "S-seriously?! Are you fucking motorboating her?!"
        "In my own state, I intimately sympathized with her. She was getting a fix and quelling a poisonous desire, breathing in Rosalind like her life depended on it."
        ver "Fwwwuuah, fmmmhmwww-♥"
        "-gnawing at her chest like she would sustain her."
        fel "Come- aah- w-what the fuck? You barely even-"
        "Felicia's complaint fell on deaf ears; Veronica was too rightfully enamored with the bounty before her."
        ver "Mmmh, mmhmhh-♥"
        scene or_rosaveromb1_a with dissolve
        show or_rosaveromb1 with dissolve
        "Before long, Rosalind became less concerned with her precarious footing and more concerned with scratching her own itch."
        rose "Mmmmmh-♥"
        "It started from a series of simple, pleasurable shudders. Her body squirmed and rocked until all that energy concentrated and found an outlet in her waist."
        rose "Oh, o-ohhhh-♥"
        "In a desperate bid for {i}something{/i}... {b}anything...{/b} like a cat in heat, Rosalind rubbed herself against Veronica's unbending form, looking for relief."
        rose "Oh, mmy-♥♥"
        scene or_rosaveromb2_a with dissolve
        show or_rosaveromb2 with dissolve
        "*Chwup, fwhup~!*"
        "The redhead knew where to attack. {b}She knew{/b} her weakness."
        rose "Oh, g-god-♥♥♥ Oh, g-gosh-♥♥♥♥"
        "That wonderfully perfect weakness for a woman like Rosalind."
        rose "V-vero-♥"

        if w3HagHandie == True:
            "The old woman's grip on my cock did nothing to assuage the envious pangs I felt as I desired to get my hands and cock inside all three women who occupied the screen."
            "{b}Damn it{/b}, this wasn't enough..."
        else:
            "Envious pangs assailed me as I desired to get my own hands and cock inside all three women who occupied the screen."
            mct "(I'm going crazy here...)"

        "*{b}Chwup, khwup, chwhhup!{/b}*"
        rose "W-wooah-♥ That feels... it's s-so h-hhoooot~ b-buh-burning up... every time - I f-forg-♥"
        "Every time Veronica {i}inhaled{/i}, Rosalind's expression said it all."
        rose "Woohh, g-god, gggoooood-♥ V-verhherronica-♥"
        "On a normal day, she was critically weak there... on a day like today, in a situation like this..."
        rose "Hhhnnwwooo, o-ohohhhgoawwwd-♥"
        "{b}She had no hope{/b}."
        rose "Wooohhaaa-♥"
        "No hope but to surrender to the strong woman's whims and desires."
        "{b}*Chwup, fhwwup, fhhwwup, gwhhup!*{/b}"

        if kat_polite == True:
            "No choice but to play her part in Mrs. Pulman's game of erotic theater and relinquish all control to her competitor."
        else:
            "No choice but to play her part in Kathleen's game of erotic theater and relinquish all control to her competitor."

        rose "Woohh-♥♥ G-gughh-♥"
        "If she didn't understand that intelligently, then at least her body was quick on the take."
        rose "Hhhuk-♥ Blawwwnkss-♥"
        "{b}*Chwup, fhwwup, fhhwwup, gwhhup, whhwhhup, chwup, chhup-!!!!*{/b}"
        scene w3_2714 with dissolve
        rose "Hngngggg- ohh, noo... ggghhhhoodd~♥"
        "Rosalind's expression soon went cross-eyed."
        scene or_rosaveromb3_a with dissolve
        show or_rosaveromb3 with dissolve
        "*Chwup, fwhup, kwhup!*"
        rose "Heehhy♥ Oohwwwh♥"
        "In no time at all, pleasure quickly replaced all semblance of intelligence in her eyes."
        rose "Feeelss-aaahh-"
        "Veronica's ministrations were her ticket to forget how badly her body burned."
        rose "Wwee-♥ Ggoowwdd, Verrrhho-♥"
        "A comfort that Veronica hadn't yet afforded her own self."
        rose "Ghh-♥ Huuhh-♥"
        "........."
        "......"
        scene w3_2715 with dissolve
        ver "{b}Ghhaah{/b}...!"
        rose "W-wwooah, ww-why you sttohp? Ahehh..."
        scene w3_2716 with dissolve
        ver "S-sorry, Rose."
        rose "Whha-?"
        ver "Felicia is looking extra fine over there."
        scene w3_2717 with dissolve
        rose "Ah...? Oh--"
        scene w3_2718 with dissolve
        ver "Sit tight for a minute."
        scene w3_2719 with dissolve
        fel "H-aahh... f-finally! G-give me one of those t-toys!"
        scene w3_2720 with dissolve
        ver "That's not what I had in mind..."


        if w3HagHandie == True:
            scene br_haghandy3_a with pixellate
            show br_haghandy3 with dissolve
            kat "Well, this direction is bringing up some recent memories."
            sophia "Is that right?"
            kat "She was much less friendly with me, but Miss Lynch is rather straightforward."
            mc "H-hhhhngg...!"
            "Like hell my mind was registering any of her bullshit right now."
            fel "H-heuuuh, w-waaah?"
            scene w3_2373 with dissolve
            sophia "Did you expect this kind of fervor?"
            scene w3_2374 with dissolve
            mc "H-a, hnnggaa..."
            play sound "sound effects/metal-drop.wav"
            ver "How the hell does this thing open?!"
            "The inside of my head was mush right now. My capacity for language was utterly eroded."
            scene w3_2375 with dissolve
            kat "I've been doing this for a long time. Before the club, I had my {i}other{/i} enterprises."
            kat "I'm well acquainted with the peculiar ways people respond when they're horny. For a woman like her, getting off is as simple as going from point A to point B."
            scene w3_2376 with dissolve
            sophia "I'm impressed."
            scene w3_2377 with dissolve
            kat "You shouldn't be. I'm an amateur when compared to someone like your owner."
            kat "I think the way Van Doren has you under his thumb is much more impressive."
            scene w3_2376 with dissolve
            sophia "Thank you."
            scene w3_2377 with dissolve
            kat "You took that as a compliment?"
            scene w3_2376 with dissolve
            sophia "Of course I did. Abel only has the best things."
            scene w3_2379 with dissolve
            kat "Your self-awareness in your choice of words is commendable, dear."
            fel "Ehh-? Where the hell do you think you're putting your fat--"
        else:

            scene w3_2381 with dissolve
            kat "Well, this direction is bringing up some recent memories."
            fel "H-heuuuh, w-waaah?"
            scene w3_2382 with dissolve
            "To my annoyance, whenever one of them spoke, my attention would turn back to just how fuckable the women next to me were. "
            play sound "sound effects/metal-drop.wav"
            ver "How the hell does this thing open?!"
            scene w3_2383 with dissolve
            sophia "Is that right? You counted on this kind of... {i}fervor{/i}?"
            scene w3_2382 with dissolve
            mct "(Christ, I want to make that mouthy hag choke on my dick until she passes out!)"
            "Intrusive thought upon intrusive thought flooded my head."
            scene w3_2384 with dissolve
            kat "I've been doing this for a long time. Before the club, I had my {i}other{/i} enterprises."
            kat "I'm well acquainted with the peculiar ways people respond when they're horny. For a woman like her, getting off is as simple as going from point A to point B."
            scene w3_2383 with dissolve
            sophia "I'm impressed."
            scene w3_2385 with dissolve
            kat "You shouldn't be. I'm an amateur when compared to someone like your Master."
            kat "I think the way Van Doren has you under his thumb is much more impressive."
            scene w3_2386 with dissolve
            sophia "Thank you."
            scene w3_2387 with dissolve
            kat "You took that as a compliment?"
            scene w3_2386 with dissolve
            sophia "Of course I did. Abel only has the best things."
            scene w3_2387 with dissolve
            kat "Your self-awareness in your choice of words is commendable, dear."
            fel "Ehh-? Where the hell do you think you're putting your fat--"

        scene w3_2721 with pixellate
        fel "E..eeh? Who do you think you are pushing me to the-"
        ver "I'm the one that old bat didn't tie up."
        scene w3_2722 with dissolve
        ver "We're in the middle of a show, or did you forget?"
        scene w3_2723 with dissolve
        fel "Euugh, yeah, but y-you're usually not so--"
        scene w3_2724 with dissolve
        ver "Feeling neglected? Like you're not the center of attention for once?"
        fel "Mmhuihhno-"
        scene w3_2725 with dissolve
        ver "That must be tough for you, Blondie."
        scene w3_2726 with dissolve
        ver "D-don't get mad at me if I take advantage a little... you understand, right? You're feeling the same thing I am... a-ahh...♥"
        scene w3_2727 with dissolve
        ver "Just be a good girl for me and I'll be nice in return."
        "Veronica's words came out husky and drenched in honey."
        scene w3_2728 with dissolve
        fel "Hnnggg-♥"
        "Felicia shuddered."
        scene w3_2729 with dissolve
        ver "'atta girl, you're a lot more passive when you have something in your mouth, aren't you?"
        "Hell, even I shuddered from the other side of TV land."
        scene w3_2730 with dissolve
        rose "This is supposed to be a punishment... Mrs. Pulman might get ma-"
        scene w3_2731 with dissolve
        ver "Shut up, Rosie. Where's that backbone you grew when you slapped that cunt?"
        scene w3_2732 with dissolve
        rose "I- tsssk-!"
        scene w3_2733 with dissolve
        ver "A good show is a good show, and if you haven't figured it out, she wants to see how we respond when she throws a lit match in a tinderbox and leaves us to our own devices."
        scene w3_2734 with dissolve
        ver "Well... this is how {b}I{/b} respond."
        scene w3_2735 with dissolve
        fel "Heheh... you don't like me, Red, but you sure want to {b}fuck me.{/b} I've s-seen the way you occasionally look at me during the shows."
        scene w3_2736 with dissolve
        ver "Well, Blondie... not {i}everything{/i} you say is bullshit. For now..."
        scene w3_2737 with dissolve
        fel "Mmmhh-?!"
        ver "{b}A-ah-♥{/b} L-let's be friends-♥"
        scene w3_2738 with dissolve
        fel "Mmmhh, mmhhh-!!!"
        "Without much warning, Veronica's large ass smothered Felicia's face and drummed up a startled reaction."
        ver "H-haa- a-and what better way of being friends than this?"
        scene black with fade
        ver "{b}...lick!{/b}"
        scene or_verofelmd_a with dissolve
        show or_verofelmd with dissolve
        ver "J-just FYI, I make it a habit to reciprocate the kindness of friends-♥"
        fel "Mmmhhmmhmhh-!"
        ver "How do I taste Blondie?"
        fel "Mmmhh-♥ Eeuhuh-♥"
        "From the looks of it, Felicia {i}was{/i} using her tongue, but she was on the back foot."
        ver "A-ah, don't try to multitask by answering t-that-♥ I want all your focus on-"
        "*Shlick, shlwap, fwhiich-!*"
        "Felicia fought desperately to match the Amazon's erratic rhythm, to find a way to consistently pry apart Veronica's sex and use her pink tongue to plumb her depths."
        fel "Eeuhh-♥ Eeuuhh-"
        "She was clearly {i}trying{/b}, but the unhinged way Veronica dragged her sex across her face made it difficult."
        ver "A-ah, o-oh-♥ I h-haven't been this turned on since I had that bitch over my knee-"
        "The scene playing out on screen was more akin to a desperate housewife grinding herself against the corner of a washing machine than the act of two people sharing in cunnilingus."
        fel "Mmhh, hhmhm-♥"
        ver "Or m-maybe since... a-ahh... last week's photo shoot? Aeeeuhh-♥ W-who can f-fucking sayyyy-♥♥"
        fel "Eeeuh, wwwhaa-♥"
        ver "N-nice work. You're not amazing at this, but I can tell you're hungry for it. Keep at it and you'll get-- nnggg!"
        "I don't think Veronica cared about Felicia's actual skill or effort. She was too high on the power of it all."
        fel "Hnnggg-♥ Hnngguuk-♥"
        "She was getting off on having the beautiful face of a woman she held in contempt buried in her ass."
        ver "Ah, y-yes. {b}YES!{/b} By the way, you were right..."
        "Veronica had been playing it remarkably slowly up to this point, enduring her sexual urge by teasing the girls, but now it was all coming out."
        fel "Mmhh, ueeeuhh-♥?"
        ver "I do think you're beautiful. I, m-mean... h-how could I not?"
        fel "Mmmffff-!"
        ver "Hnn-♥ N-now- a-ah, you've been a good friend! So I think it's time... ah..."
        scene or_verofel69_a with fade
        show or_verofel69 with dissolve
        fel "MMhmh.. ohmhmhwoohh..? A-aahammwwhh-♥"
        "Finally, Veronica made good on her promise of lick and be licked."
        fel "MMmhh, aaa-hh- hhaa-aaah♥♥♥"
        "Veronica leaned forward and buried herself in Felicia's crotch, creating an attractive, parallel line of two bodacious figures for the camera."
        "*Shlick, fwhiick...!"
        "It was a work of art how they grasped and held each other."
        fel "Hnngg-♥"
        "Long gorgeous legs moved to get out of the way, finding tight purchase hugging and forcing each other's bodies closer."
        "*Shlick, fwhiick, hhwwiick...!*"
        rose "Uugghh... now I'm the one left out..."
        scene black with fade
        "*Shlick, fwhiick, hhwwiick...!*"
        "Felicia and Veronica continued to pleasure each other, while I..."
        "{b}*Shlick, shlick, shlick, fwhhick, hwwwiiicki!*{/b}"
        ver "Then get over here!"


        if w3HagHandie == True:
            scene w3_2407 with pixellate
            kat "I'm starting to get offended, Mr. [mcl]. Does my hand not suffice?"
            kat "Don't you want to taste release?"
            scene w3_2408 with dissolve
            mc "G-gah, f-fuck! It's not like I have any control over it!"
            sophia "Hmm..."
            scene w3_2409 with dissolve
            "Every fiber of my being desperately anticipated climax. My reason had been eroded and my purpose replaced by the critical need to expunge every trace of nauseating desire from my body through my cock."
            "The hairs on my arm stood on end, the feeling in my extremities came and went like the tide, and a pervasive tingling feeling floated from my neck down to my tailbone - by all means, my body told me that I {b}should{/b} be coming."
            scene w3_2410 with dissolve
            sophia "Interesting."
            scene w3_2409 with dissolve
            "But I wasn't. My bloated dick burned against the soft palm of the old woman's hand, pulsating and twitching from the ceaseless stimulation, filling me with the irrational fear that I might literally explode if I didn't soon go careening into the void of sexual release."
            scene w3_2411 with dissolve
            sophia "All things considered, he is showing a {b}surprising{/b} degree of longevity..."
            scene w3_2412 with dissolve
            kat "Maybe your fragrance isn't as effective as you think it is."
            mc "G-gaahh!"
            scene w3_2411 with dissolve
            sophia "Maybe..."
            scene w3_2413 with dissolve
            mct "(No! It was definitely fucking effective!)"
            sophia "...but unlikely. Hey, [mcf]..."
            scene w3_2414 with dissolve
            "Through lidded eyes, I could sense the blonde scooching closer and closer."
            scene w3_2415 with dissolve
            sophia "The issue is that a young, well-traveled guy like you simply can't get off on an old woman's touch, right?"
            scene w3_2416 with dissolve
            mc "That's not--"
            scene w3_2417 with dissolve
            sophia "{b}{i}Isn't it?{/b}{/i}"
            "Even in my lust-addled state..."
            scene w3_2418 with dissolve
            "My brain registered amazement over the willful way Sophia flipped the switch, going from detached aloofness to a man-killer just as easily as one would shed their clothes. "
            scene w3_2419 with dissolve
            mc "Hnngg...!"
            kat "*Scoff* Feeling left out, were you?"
            sophia "Give them a comparison."
            scene w3_2420 with dissolve
            "My hand responded independently, sinking into the pleasant give of the doctor's tit-flesh in an instant as what remained of my faculties disappeared into the whirlpool of her eyes."
            sophia "You got a mess lurking somewhere in there that you want to get out?"
            mc "Ha... hnngg...! F-fuck it!"
            scene w3_2421 with dissolve
            sophia "...?!"
            "I kissed her, just as you'd expect a man on the brink of starvation to steal a loaf of bread."
            scene br_hhplus_a with dissolve
            show br_hhplus with dissolve
            sophia "Mmmhhhh....!"

            if kat_polite == True:
                "She might not have expected it or even wanted it, but she quickly accepted it as a consequence of the \"just a bit of chaos\" she wielded in her joust against Mrs. Pulman."
            else:
                "She might not have expected it or even wanted it, but she quickly accepted it as a consequence of the \"just a bit of chaos\" she wielded in her joust against Kathleen."

            kat "H-hey, ahh--"
            "Spurred on by having the attention of two beautiful women, even if it was just the fucked up equivalent of cooking ants with a magnifying glass to them, I knew it wouldn't be long until I finally had my release."
            kat "Gah, ah... ha... hmpfh."
            "Although I could feel her eyes on my neck, the old woman continued to milk me."
            "*Cwhup, fwhup, chwup...!*"
            kat "I've somehow ended up feeling like a third wheel."
            "I pawed at both women's breasts with a virgin-like fervor, wholly enamored by an opportunity I might never get again."
            mct "(The head of a charity and a world-class scientist... ha, fucking sluts!)"
            "I felt like a king, not of my own making of course, but my brain was so cooked as to not know the difference. Thinking was hard, but what few thoughts I could miraculously formulate were like tidal waves breaking against the shore."
            mct "(Who the hell do you think you're fucking with? You think you can toy with me just because of money?!)"
            "I felt smothered, suffocated, and hot. More akin to a wick that was about to burn out than a human being."
            mct "(I'M A GUINEA PIG TO YOU?!)"
            "Every sensation felt heightened, and every second felt prolonged... I genuinely feared that the moment I popped would be when I was snuffed out."

            mct "{size=+30}{font=/gui/fonts/MB-Thin_Worms.ttf}(You like to toy with pe-){/font}{/size}"


            "My brain gave out, but if I ceased to exist after this, I instinctively knew one thing: these last minutes of my life should be bold."

            menu:
                "Goad the old woman into letting you finish in her mouth(w3KatPromoFinish = True)."(chg=["kathleen_trust_up"]):
                    $ w3KatPromoFinish = True
                    $ Kathleen_Trust += 1
                    scene w3_2422 with dissolve
                    mc "I'm about to b-blow..."
                    kat "You don't need my permission."
                    scene w3_2423 with dissolve
                    mc "Can you finish me with your mouth?"
                    kat "Hmmmmm, not going to happen."
                    mc "A-ah, pretty please? With a cherry on top?"
                    scene w3_2424 with dissolve
                    kat "Why don't you ask Miss Lundgren to do it?"
                    mc "...because I want you, Ma'am."
                    scene w3_2425 with dissolve
                    kat "...hmmmmmmmm. You have the eyes of a crazed animal, yet..."
                    scene w3_2426 with dissolve
                    kat "You're asking so nicely. God, I love that."
                    scene w3_2427 with dissolve
                    "She smirked like she had won against me, and perhaps even against Sophia."
                    scene w3_2428 with dissolve
                    kat "It really is goddamn adorable. Ask me again, [mcf]."
                    scene w3_2429 with dissolve
                    "A desperate, cloying urge inside me told me her mouth was the only place I wanted to be right now and if it took a bit of pleading to get me into a position where I could fill that mean bitch's stomach with my seed, then so be it."
                    scene w3_2430 with dissolve
                    mc "Hhh, haa... would you PLEASE finish me with your mouth, Mrs. Pulman?"
                    scene w3_2431 with dissolve

                    if kat_polite == True:
                        "Without another word, Mrs. Pulman lowered herself and..."
                    else:
                        "Without another word, Kathleen lowered herself and..."

                    scene br_hhplus_hbj_a with dissolve
                    mc "G-gah...!"
                    "The moment her lips wrapped themselves around my cock, I felt like I might pass out."
                    "Her seal was so airtight that her mouth felt like an oven. Steady puffs of hot breath passed over the head of my cock as it made its way out through her nose."
                    scene br_hhplus_hbj_a with dissolve
                    show br_hhplus_hbj with dissolve
                    mc "F-fuck, damn it!"
                    "*Shwuck, fgwhhuck, thwuuuck!*"
                    "What little air could escape from her hold transformed into {b}obscene{/b} noises as she inched herself up and down my shaft."
                    mc "H-holy-!"
                    "The running narration in my head was a jumbled mess, but through all the muddied noise from the pleasure soaking into my brain, I grasped a simple truth."
                    mc "Hnnng, you've sucked a lot of cock in your time, haven't you?!"
                    "*Thwaahp, fwhap, swhhuck~!*"
                    "The answer to that question played across my glans every time I wedged myself comfortably in her throat with zero fuss."
                    "Swhuck, hhhwhuck, fhhggguuk!*"
                    "{b}Damn it!{/b} A rich woman like her had no business sucking dick this well."
                    mc "Ghhn, haaat, hnnngg...!"
                    "She sucked me with the skill of a woman who had {b}nothing{/b} to her name."
                    kat "Mmmhm, hhmhm~"
                    "Just like her hand job, there was no wasted effort. She didn't tackle it in a clumsy frenzy, nor did she need to cautiously get used to my size."
                    "*Shwhuhuck, fwhhucuk, ghhwhuhuk!*"
                    "She sucked me like she had been sucking {b}my{/b} dick her whole life, pleasuring me at a steady and comfortable pace. I marveled at how, through a mere blowjob, a woman so cold and cruel could instantly imprint herself on my body as warm and welcoming."
                    "I was quickly understanding that \"adorable\" disparity she had just spoken."
                    mc "Hnng, h-how?!"
                    sophia "It's not performing brain surgery."

                    if kat_polite == True:
                        "{b}There{/b} was another perverse delight, speeding me toward my climax. Sophia's attention was on the back of Mrs. Pulman's head, watching intently as she debased herself in pursuit of degrading me."
                    else:
                        "{b}There{/b} was another perverse delight, speeding me toward my climax. Sophia's attention was on the back of Kathleen's head, watching intently as she debased herself in pursuit of degrading me."

                    mct "(Haaaa... hope you like the show, bitch. You're the impetus for this.)"
                    "*Fwhhuck, ghhhukh, khggguuhhk*"
                    mc "Ahh... y-you dick swallowing--! Hnnngg...!"
                    "It was coming."
                    scene w3_2432 with dissolve
                    mc "You think I'm adorable?!"
                    "I was moments from blowing my load, and with it, the indignation from earlier swelled in me. I had wanted a bold finish before I met my end, and well..."
                    mct "(I'll show you adorable!)"
                    stop music
                    scene br_hhplus_gulp1_a with vpunch
                    mc "I'm c-cumming, fucking drown in it, you damn--"
                    play sound "sound effects/spurt.wav"
                    with flash
                    kat "Mmmmh?!"
                    "Before she could even register what was happening, ropes of piping hot cum barreled down her esophagus on a one-way trip to her stomach."
                    play ambient "sound effects/fel2.wav"
                    scene br_hhplus_gulp1_a with dissolve
                    show br_hhplus_gulp1 with dissolve
                    play sound "sound effects/spurt.wav"
                    with flash
                    kat "Ghhkka, hkkaa-!"
                    "I pressed down hard, holding the old woman's head in place as she gargled my seed in abject surprise."
                    mc "Hnngg, all of it!"
                    "I pressed down so hard it hurt my groin."
                    play sound "sound effects/spurt.wav"
                    with flash
                    kat "Ghhuk, hhuuuh, hwwwhuuuck...!"
                    "It was massive, like I was cumming my very soul down the old woman's throat."
                    kat "Ghuk, khak, uuhhk-!"
                    mc "Gah, c-choke on it!"
                    play sound "sound effects/spurt.wav"
                    with flash
                    "Not all of my load was making its way down her throat. To my perverse glee, I could {i}feel{/i} myself coating the lining of her throat."
                    kat "Ghhuk, hhuuuk...!"
                    scene br_hhplus_gulp2_a with flash
                    show br_hhplus_gulp2 with dissolve
                    play sound "sound effects/spurt.wav"
                    with flash
                    mc "Hope you like the fucking taste!"
                    kat "Mmmh, hhhngg?!?!"
                    sophia "I don't think she can breathe..."
                    mc "Good! She can breathe when I'm fucking--!"
                    stop ambient fadeout 4.0
                    play sound "sound effects/spurt.wav"
                    with flash
                    ".........!"
                    play sound "sound effects/spurt.wav"
                    with flash
                    "......!"
                    scene w3_2433 with dissolve
                    mc "A-aahh...!"
                    scene w3_2434 with dissolve
                    kat "Ugghhuhh..."
                    scene w3_2435 with dissolve
                    "Peace."
                    "Serenity."
                    "Satisfaction."
                    "In this moment, I had it all."
                    scene black with w20
                    "With that, I happily died. The oblivion I felt nipping at my heels finally sank its sharp teeth into my throat."
                    "............"
                    "........."
                    "......"
                    "..."
                    kat "Why are you holding your hands out like that? It's weird."
                    mct "(Ah, fuck... I {i}wasn't{/i} dead? {b}Oh no.{/b} Then that meant I just...)"
                    scene w3_2436 with w9
                    sophia "She's right. It's distracting."
                    scene w3_2437 with dissolve
                    "I didn't know how long I was out of it, but by the time I opened my eyes, the two women had collected themselves, and what I thought was a bold display of defiance was made pitiful and wholly expected by their bemused faces."

                    if kat_polite == True:
                        "Mrs. Pulman looked {i}totally{/i} unaffected by my rough treatment, showing no signs of having mercilessly guzzled my cum just moments ago..."
                    else:
                        "Kathleen looked {i}totally{/i} unaffected by my rough treatment, showing no signs of having mercilessly guzzled my cum just moments ago..."

                    scene w3_2438 with dissolve
                    kat "Oh, by the way... you said some pretty outlandish things to me."
                    scene w3_2439 with dissolve
                    mc "If I recall, I did a bit more than that..."
                    scene w3_2440 with dissolve
                    kat "It was {b}adorable{/b}."
                    "She had indeed won."
                "Leave an impression on the doctor.(w3SophiaPromoFinish = True)"(chg=["kathleen_down2"]):

                    $ w3SophiaPromoFinish = True
                    $ Kathleen_Affection -=2
                    "I knew what I wanted."
                    sophia "Mmmhh, hhhhh..."
                    "And that last act of defiance would be leaving the doctor, the root cause of all this, something to remember me by."
                    scene br_hhplus_doc1_a with dissolve
                    show br_hhplus_doc1 with dissolve
                    "*Chwup, fhwup~*"
                    "I wanted to hear this aloof bitch moan, so I focused everything on the woman whose mouth I was currently exploring."
                    sophia "Mmmh, hhmmm...?"
                    "It was a battle against my wits. Sophia was literally intoxicating. Focusing my senses all on her had me burning twice as fast."
                    "By instinct, I felt her breast over her clothes."
                    sophia "Mmhh..."
                    "Her coos told me she was receptive, but it wasn't quite the noise I wanted to drag out from the blonde."
                    scene br_hhplus_doc2_a with dissolve
                    show br_hhplus_doc2 with dissolve
                    sophia "Ghu, gha~ghhuu...!"
                    "Deciding that over the clothes touching wouldn't do it, I switched focus on the erogenous zone in her mouth, intensifying my efforts in an intricate dance to subdue her tongue with my own."
                    sophia "Mmmmh, mmhhhh- *chwuph, fhwhup~*"
                    "She wasn't a passive observer in my hunt; her tongue played coy, darting away and slipping from my grasp whenever I thought I had her pinned."
                    "It was mere seconds, but--"
                    "*Chwhu, fhwwwup, chup!*"
                    "--but, in my fogged-over state, time held little sway over my perception. What was in reality a clumsy tussle felt like a long and protracted siege."
                    "I don't know if it was because of the perfume, but all bodily sensations gradually began to meld into one."
                    "The feeling of the old woman's hand milking my cock, the wet warmness of our kiss, the bubbling desire so strong that I was confident it would be the end of me..."
                    mc "Mmmh, hhhmmm-!"
                    "All of it spelled an overload melded and combined into a singular feeling of otherness. I was sure I had lost this battle until..."
                    scene br_hhplus_doc3_a with dissolve
                    show br_hhplus_doc3 with dissolve
                    "My brain registered a change."
                    mct "Was she...?"
                    sophia "Mmmh, hhmhm~aahhh...!"
                    "She was closer."
                    "She was pressing into me."
                    "She felt it."
                    "She was {b}heated{/b}."
                    "{i}She was kissing me back.{/i}"
                    "Whether it was done deliberately or on an instinctual level, her body responded favorably."
                    sophia "Ahh, hhhnnggg, mmmmhh-!"
                    "My hand found a place on her ass and I used that to spur her on even more. With this, I had physical confirmation of my success."
                    mct "(Fuck, what a great-!)"
                    "I could feel the hot dampness of her delicate spot."
                    sophia "Mmhh, hhaa...♥♥♥"
                    "She purred openly and I felt a petty relief over my trivial victory. The succubus driving me to this desperate state wouldn't escape our battle unscathed."
                    "*Chwup, fhwwup, khwwup*!"
                    "--and that wasn't the only sense of relief I felt."
                    stop music
                    play sound "sound effects/spurt.wav"
                    scene w3_2441 with flash
                    mc "{b}Hnng, ah-!!!{/b}"
                    "I didn't know when it started, but ropes of cum geysered from my cock and rained down from the sky."
                    play sound "sound effects/spurt.wav"
                    scene w3_2442 with flash
                    mc "Ghh, aaahh- sssshit--"
                    kat "Huh, {b}WOW{/b}."
                    scene w3_2443 with dissolve
                    mc "Hngg, hhhhmmmhh-~"
                    "All the suffocating vileness in me was expelled and released into the world. All my desperation spilled out onto our clothes and thighs."
                    "Soon need was replaced with..."
                    scene w3_2444 with dissolve
                    "Peace."
                    "Serenity."
                    scene w3_2445 with dissolve
                    "Satisfaction."
                    "Emptiness."
                    "The oblivion I felt nipping at my heels finally sank its sharp teeth into my throat."
                    scene black with w20
                    "I was dead."
                    "............"
                    "........."
                    "......"
                    "..."
                    sophia "Great, now we'll spend the rest of the show reeking of semen."
                    mct "(Ah, fuck... I {i}wasn't{/i} dead? {b}Oh no.{/b} Then that meant I just...)"
                    scene w3_2446 with w9
                    kat "You should've thought of that before you entered the crossfire."
                    scene w3_2447 with dissolve
                    sophia "You were taking too long. I wanted to put an end to the distraction."
                    scene w3_2448 with dissolve
                    "I didn't know how long I was out of it. Still, by the time I opened my eyes, the two women had collected themselves. The damage I thought I had done to Sophia with my counter-attack was made pitiful by their bemused faces."
                    scene w3_2449 with dissolve
                    kat "Oh, please. Are those the kind of sounds you make matter-of-factly?"
                    scene w3_2450 with dissolve
                    "Sophia looked as composed as ever, and except for a little blush, her attention turned back to the Carnations."
                    scene w3_2451 with dissolve
                    kat "I hope that provided you a measure of relief, Mr. [mcl]. That certainly was an... {i}explosive{/i} finish."
                    mc "A, ahem... thaaaaaanks?"
                    scene w3_2452 with dissolve
                    kat "Don't mention it. It was... interesting."
        else:

            scene w3_2453 with dissolve
            mc "........."
            mc "......"
            stop music
            play sound "sound effects/record-scratch.wav"
            scene w3_2454 with dissolve
            "...this was my limit."
            $ renpy.end_replay()
            scene w3_2455 with dissolve
            mc "Aaeeh, I'll be riiiiiight back."
            scene w3_2456 with dissolve
            "......"
            scene w3_2457 with dissolve
            "..."
            scene w3_2458 with dissolve
            kat "Is that a milder scent you are wearing?"
            sophia "It's the same batch as the bottle I gave you."
            scene w3_2459 with dissolve
            kat "The effect seemed... less? Why's that?"
            scene w3_2460 with dissolve
            sophia "It's possible that his body adapted and partially metabolized the odor molecules. All I can say is that it's remarkable he held out that long."
            sophia "It could be a matter of willpower."
            scene w3_2461 with dissolve
            kat "When I had dinner with Charles the other night, he didn't even flinch."
            scene w3_2462 with dissolve
            sophia "Dr. Kohler is a scary man."
            scene w3_2463 with dissolve
            kat "Is that your appraisal after demolishing him game after game?"
            scene w3_2464 with dissolve
            sophia "How else should I describe a man who has no need but keeps his passions tightly controlled."
            scene w3_2465 with dissolve
            kat "That's why he and I are incompatible. He treats fucking like it's Christmas."
            kat "You don't have anything to worry about as long as you don't lose."
            scene w3_2466 with dissolve
            sophia "I don't plan on it, but I have a feeling he eventually wins one way or another."
            scene w3_2459 with dissolve
            kat "Abel wouldn't let it come to that, would he?"
            scene w3_2467 with dissolve
            "......"
            "..."
            scene w3_2460 with dissolve
            sophia "Thank you for indulging my little whim, Kathleen. It was amusing."
            scene w3_2459 with dissolve
            kat "Don't mention it. One should make their own fun in life. Still..."
            kat "...you're very competent. Don't you ever desire more?"
            scene w3_2468 with dissolve
            sophia "A frivolous bitch like you has no business saying that to me."
            scene w3_2469 with dissolve
            kat "Ah, fuck. There it is."
            scene black with fade
            kat "I almost felt sorry for you."
            jump w3WashRoom

        play music "music/landing.ogg"
        scene or_3some1_a with pixellate
        show or_3some1 with dissolve
        carnations "Mmhh, fweh...♥ Gheee..♥ Mmhhh...♥"
        "While I was preoccupied with expunging my nauseating urges, the Carnations were in the thick of it."
        rose "Mmhh, ummffh, heeehhuu-♥"
        "Rosalind had replaced Felicia beneath the Amazon's wide hips, and just like before, Veronica wasn't shy about crudely grinding the MILF's face under her weight."
        "With the redhead getting \"hers\", it was left to Felicia to find gratification for both herself and her physically-engaged, muff-diving cohort."
        fel "*Cwhwup, fwhup* Mmhh, hhueeeh-♥"
        scene or_3some2_a with dissolve
        show or_3some2 with dissolve
        "The result was a sapphic, Ouroboros-like blending of curves and limbs, making it hard to distinguish where one woman began and the other ended."
        "*Chwup, fwhup, kwhup~*"
        "All pretense had melted away."
        carnations "Fwweeh, hhnnggg, hhnn, ggwwwweh-♥"
        "Veronica's domineering streak had all but receded, the only trace remaining was in the decisive way she pawed, kissed, and shook her hips."
        fel "Mmhh, hhhnhnaaaatt-♥ Fwwweeeh-♥"
        scene or_3some1_a with dissolve
        show or_3some1 with dissolve
        "Felicia's bitching and moaning had been replaced with kiss-locked silence and focused, fiery concentration."
        carnations "Ghaa, gnnhhh, haaa *Chwup, shlick~* hhhaaa-♥"
        "Rosalind had practically disappeared off screen, perhaps even according to her own strategy, only to be used like a scratching post and as the engine source for a bevy of amorous noise."
        rose "{size=10}Mmhh, fweeh, ggwwweeh{/size=/10}"
        "Her muffled moans could barely be heard beneath the redhead's ass, and what made it through those freckled cheeks was co-opted into a chorus of sexual need that sounded anemic on the tv's piss-poor speakers."
        "*Cwhup, fwwhhuup-*"
        fel "N-hh, hhhnhn-♥"
        scene w3_2739 with dissolve
        "*Chwup, fhwwu, khwwup~!*"
        fel "Enh, hhhhnn, wwwhhaaannn-"
        scene w3_2740 with dissolve
        ver "A-ahh... you sing lovely for a caged bird..."
        scene w3_2741 with dissolve
        fel "H-heh... aaah, y-you think you get it? You're so fucking full of yourself. At least my cage-"
        scene w3_2742 with dissolve
        rose "MMmhh, mhhhww-"
        scene w3_2741 with dissolve
        fel "...isn't collapsing on itself in debt."
        scene or_3some2_a with dissolve
        show or_3some2 with dissolve
        rose "MMmhh, unnngg, wwwhaaa-"
        ver "This isn't y-your first time doing-"
        "*Shlick, fwhick, hwwwhick!-"
        fel "Of c-course not! I'm n-not seasoned like you, but sometimes... h-haaa... the ooc-occasion calls for it."
        rose "Unngng, hheee, ehuugg-"
        fel "Hubby has requests, y'know...?"
        ver "H-haa... y-you're a good wife, aren't you? F-fuck... I should've tried being rich-"
        scene or_3some3_a with dissolve
        show or_3some3 with dissolve
        fel "MMhh, mmhhhh-!!!"
        "In the wake of their exchange, Veronica intensified her affection, sucking Felicia's face and savoring it like the last pizza slice."
        carnations "Mmmh, eeueuuh, feewwwh... *Chwwup, shlick* fewwweee...♥♥♥"
        "Not since her crowning moment during her interview, a night that only Samson and Isaac witnessed, had Veronica looked so comfortable in her element within these four walls."
        "*Chwup, fhwwip~*"
        "She hadn't quite \"punished\" the girls, but she gave the camera an unfettered glimpse of what she truly desired."
        carnations "Mmmhh, heeeuuhh, gwwwuuuk-!!!"
        "And it turns out, what she desired was beautiful women and an opportunity to let her id roam free."
        carnations "Eeeuuhh, gwwwhhha, hwwwaanngg♥"
        "Veronica and I weren't so different in that regard."
        carnations "Hnnng, eeeuhuhh-♥♥"
        "On different terms, she might even fit in at a place like this..."
        scene w3_2743 with dissolve
        ver "Mmhh, hheee...?!"
        scene w3_2744 with dissolve
        ver "Mmhh, eehh-♥"
        scene w3_2745 with dissolve
        ver "Ahh, hhn... h-hang o-h, s-snaaaaap-ghh-♥♥♥"
        scene w3_2746 with vpunch
        rose "Hnngg, ggeehhh...?! Mmghhhh...!"
        "From my own vivid experience of being beneath that Amazon, I sympathized with Rosalind."
        scene w3_2747 with vpunch
        rose "Mmggwww-!!!"
        "As she came, Veronica instinctually pushed her ass toward the source of her pleasure, bearing down on Rosalind with a startling amount of her body weight."
        with vpunch
        rose "Mmhwwwh, hhhnnggg, gwwwhhh-"
        ver "Ah- y-yeeeahh...♥"
        scene w3_2748 with dissolve
        "........."
        "......"
        "..."
        scene w3_2749 with dissolve
        ver "I know you girls aren't finished, right?"
        scene w3_2750 with dissolve
        fel "Hell no."
        rose "Mmhh, hhnhhh...:"
        scene w3_2751 with dissolve
        ver "Good. I sure as shit ain't either."
        stop music fadeout 3.0
        scene black with fade
        "So they carried on, coming together with the common, selfish goal of getting themselves off."
        "I'm not sure how long it lasted; I just know..."
        jump w3WashRoom

label w3WashRoom:
    $ renpy.end_replay()
    scene w3_2752 with circlewipe
    mct "(Goddamn it...)"
    if not persistent.w3PunishGame:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3PunishGame = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    "It took me a while to collect myself."

    $ unread_sophia = True
    $ history_sophia = "I spent an unusual amount of time with Sophia, while she sat in during Kat's punishment game. I got the feeling it was more of a test than a game..."
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve

    if w3HagHandie == True:

        if w3KatPromoFinish == True:
            "Despite unleashing my need and blowing a fat wad down that hag's throat, I was still feeling... {i}out of sorts{/i}."
        else:
            "Despite that hag's handy and blowing my load into the stratosphere, I was still feeling... {i}out of sorts{/i}."
    else:

        "Despite jacking off a couple of times, I was still feeling a bit... {i}frazzled{/i} and out of sorts."

    "It wasn't quite enough... Although I could think clearly and function, everything felt just a little topsy-turvy."
    scene w3_2753 with dissolve
    mc "Gah..."
    "Strangely, I no longer felt the anger I had when I felt like I had no control."

    if w1GonzoReward == True:
        "I had overwhelmingly felt it when Mrs. Pulman jabbed me with that needle a week before. But now, it all felt {b}normal.{/b}"
    else:
        "But now, it all felt... {b}normal.{/b}"

    play music "music/sonatina-in-c-minor.ogg"
    scene w3_2754 with dissolve
    "Okay, maybe that's just a tinsy bit of bullshit. I still felt annoyed, but this madness, in an indirect way, was my own making... and I was on the comfortable side of things, unlike the scene I just witnessed."

    "........."
    "......"
    scene w3_2755 with dissolve
    "..."
    kat "There you are. How are you feeling?"
    scene w3_2756 with dissolve
    mc "Like I want to piss and jerk off all over your face."
    scene w3_2755 with dissolve
    kat "Amazing, isn't it? For the record, I wasn't aware she would be wearing that when she asked to sit and observe."
    scene w3_2756 with dissolve
    mc "I'm getting used to it. Did you have fun?"
    scene w3_2757 with dissolve
    kat "Oh, I {i}always{/i} enjoy myself."
    kat "Even when things don't go to plan or I... {i}lose{/i}, I never feel like I did."
    scene w3_2758 with dissolve
    kat "It's strange, but I don't think I ever felt an ounce of genuine anger in my life."
    scene w3_2759 with dissolve
    mc "I don't believe that."
    scene w3_2760 with dissolve
    kat "I'm not saying I don't ever get annoyed at the \"obstacles\" that get in my way, or find a situation that calls for the theatrics of anger."
    kat "But at the end of the day, what sense is there in getting angry over a game?"
    scene w3_2759 with dissolve
    mc "Spoken like a woman who can stack the deck in her favor."
    scene w3_2760 with dissolve
    kat "Oh, I don't know... I might very well be turning the corner into a major loss soon. We'll see."
    scene w3_2761 with dissolve
    mc "......"
    mc "..."
    scene w3_2762 with dissolve
    mc "How are the girls?"
    scene w3_2763 with dissolve
    kat "They're getting dressed."
    scene w3_2764 with dissolve
    mc "How {b}are{/b} they?"
    scene w3_2766 with dissolve
    kat "They probably feel pent up, but they seemed functional enough. It's understandably more soft feelings than hard ones right about now."
    scene w3_2764 with dissolve
    mc "So, do you need anything else from me? Am I done here today?"
    scene w3_2767 with dissolve
    kat "Nope, you're done! Good job, Mr. [mcl]."
    kat "Before you go, I wanted to ask: how did you find the club's hospitality last Saturday?"
    scene w3_2768 with dissolve
    mc "...?"
    scene w3_2767 with dissolve
    kat "Remember, I asked you to enjoy it and give me your thoughts."
    scene w3_2763 with dissolve
    kat "It was mostly an excuse to try and get you to let loose, but a task is a task. What did you think?"
    scene w3_2765 with dissolve

    if w2ExEmmaFavor == "fulfilled" or w2ExLezSeen == True:

        menu:
            "Tell her you just walked around.(Dialouge/render changes only)":
                scene w3_2764 with dissolve
                mc "I mostly just walked around... mingled."

                if VeroFlag == True:
                    scene w3_2766 with dissolve
                    kat "Oh, you did more than just mingle. You and Dalia joined Samson in the sauna."
                    scene w3_2764 with dissolve
                    mc "You know about that?"
                    scene w3_2773 with dissolve
                    kat "Of course."
                    scene w3_2775 with dissolve
                    mc "..."
                    scene w3_2773 with dissolve
                    kat "I did tell you to have fun, but I didn't expect you to go mano a mano in the sauna with a couple of whores."
                    scene w3_2774 with dissolve
                    mc "I like his movies."
                    scene w3_2773 with dissolve
                    kat "Oh, I bet you do..."
                    scene w3_2769 with dissolve
                    mc "...uh, Dalia was great?"
                    scene w3_2767 with dissolve
                    kat "She always is."
                    kat "Harper might give her a run for her money if only she was a more classical beauty, but they both have their uses."
                    scene w3_2764 with dissolve
                    mc "Right..."
                    scene w3_2770 with dissolve
                    kat "I do hope you got what you wanted out of that Has Been."
                    scene w3_2772 with dissolve
                    "......"
                    "..."
                    scene w3_2771 with dissolve
                    mc "...he's a giant prick."
                    scene w3_2770 with dissolve
                    kat "He has his uses."
                else:

                    scene w3_2773 with dissolve
                    kat "Oh, [mcf]. You're like a diabetic in a candy store."
                    scene w3_2774 with dissolve
                    mc "I mean... everything seemed fine? I don't really know what the criteria is."
                    scene w3_2773 with dissolve
                    kat "You most certainly do."
                    scene w3_2775 with dissolve
                    "......"
                    "..."
                    scene w3_2776 with dissolve
                    kat "Oh, for-- just... let loose next weekend. That's an order."
                    scene w3_2764 with dissolve
                    mc "Right."

            "Mention the Emma situation." if w2ExEmmaFavorIan == True or w2ExEmmaFavorChuck == True or w2ExEmmaFavorSolo == True:
                scene w3_2764 with dissolve
                mc "Nothing too interesting. Jacob did ask me to keep an eye on Emma for him."
                scene w3_2770 with dissolve
                kat "Ah yes, that... {i}romantic.{/i} For a man with such a bloody past, he sure is a softy."
                scene w3_2772 with dissolve
                "I chose to cautiously file away that bit of information but not draw attention to it."
                scene w3_2770 with dissolve
                kat "He sure is an interesting fellow. August did well in finding someone to offset Warren's personality."
                scene w3_2771 with dissolve
                mc "What are you talking about?"
                scene w3_2773 with dissolve
                kat "Eh, ask him sometime. He's the pimp."
                kat "The way I understand it, they each have their function when it comes to the discipline of this place."
                scene w3_2774 with dissolve
                mc "You should keep Warren on a tighter leash."
                scene w3_2767 with dissolve
                kat "Aw, don't fret. He never does any permanent damage."

                if w2ExEmmaFavorIan == True:
                    kat "Besides, the girls now have you to get them off the floor. Smart thinking sending her to Mr. Beaufort, you washed your hands of culpability."
                if w2ExEmmaFavorChuck == True:
                    kat "Besides, the girls now have you to get them off the floor. Leaning on Charle's fondness of you to get it done was pretty bold."
                    kat "August never has it in him to question Charles."
                if w2ExEmmaFavorSolo == True:
                    kat "Besides, the girls now have you to get them off the floor. Shielding Emma by getting her to film herself was an attractive solution."

                scene w3_2769 with dissolve
                mc "You know about that?"
                scene w3_2766 with dissolve
                kat "Of course."
                scene w3_2765 with dissolve
                "......"
                "..."
                scene w3_2767 with dissolve
                kat "Relax, unlike August, I don't give a shit about the minute-to-minute comings and goings of the house girls. If cutting them some slack where you can makes you feel better about yourself, go for it."
                scene w3_2766 with dissolve
                kat "I trust if you do, it'll be done with wisdom and discretion."
                scene w3_2764 with dissolve
                mc "...s'alright."

            "Mention Harper and Lucy(if w2ExLezSeen == True)"(chg=["kathleen_up"]) if w2ExLezSeen == True:
                $ Kathleen_Trust += 1
                $ w3KathleenLezTold = True
                scene w3_2764 with dissolve
                mc "Well, I..."
                scene w3_2765 with dissolve
                mct "(Was there any point in mentioning this?)"
                "It's not like I needed to score any points with the old woman, but it was the most notable thing I could mention."
                scene w3_2890 with pixellate
                mc "Nothing too interesting. I learned that Harper and Lucy are pretty fond of each other."
                scene w3_2766 with pixellate
                kat "Oh...?"
                scene w3_2764 with dissolve
                mc "Yeah, Dalia asked me to peek in on them."
                scene w3_2776 with dissolve
                kat "Really? On company time?"
                scene w3_2777 with dissolve
                "......"
                "..."
                scene w3_2770 with dissolve
                kat "Well, she's doing a better job than I expected."
                scene w3_2771 with dissolve
                mc "Wait... you're aware of them--"
                scene w3_2770 with dissolve
                kat "Of course. I was the one who told her to support our would-be Carnation and help her not go anywhere."
                scene w3_2771 with dissolve
                mc "Then Harper and Lucy are just because of you...?"
                scene w3_2770 with dissolve
                kat "Oh, it's nothing cynical. It's not like I ordered her to seduce that stupid whore; that must be how it developed between them. I'm sure they're actually quite fond of each other."
                scene w3_2773 with dissolve
                kat "You shouldn't mention it to August, though. He's a stickler when it comes to the discipline of the girls."
                kat "He wouldn't see the value of this kind of relationship as I do."
                scene w3_2774 with dissolve
                mc "I wasn't planning on it."
                scene w3_2773 with dissolve
                kat "...yet, you mentioned it to me?"
                scene w3_2775 with dissolve
                mc "..."
                scene w3_2778 with dissolve
                kat "Good boy."
    else:
        scene w3_2764 with dissolve
        mc "I mostly just walked around... mingled."

        if VeroFlag == True:
            scene w3_2766 with dissolve
            kat "Oh, you did more than just mingle. You and Dalia joined Samson in the Sauna."
            scene w3_2764 with dissolve
            mc "You know about that?"
            scene w3_2770 with dissolve
            kat "Of course."
            scene w3_2772 with dissolve
            mc "..."
            scene w3_2773 with dissolve
            kat "I did tell you to have fun, but I didn't expect you to go mano a mano in the sauna with a couple of whores"
            scene w3_2774 with dissolve
            mc "I like his movies."
            scene w3_2773 with dissolve
            kat "Oh, I bet you do..."
            scene w3_2769 with dissolve
            mc "...uh, Dalia was great?"
            scene w3_2767 with dissolve
            kat "She always is."
            scene w3_2763 with dissolve
            kat "Harper might give her a run for her money if only she were a more classical beauty, but they both have their uses."
            scene w3_2764 with dissolve
            mc "Right..."
            scene w3_2766 with dissolve
            kat "I do hope you got what you wanted out of that Has Been."
            scene w3_2765 with dissolve
            "......"
            "..."
            scene w3_2764 with dissolve
            mc "...he's a giant prick."
            scene w3_2763 with dissolve
            kat "He has his uses."
        else:

            scene w3_2773 with dissolve
            kat "Oh, [mcf]. You're like a diabetic in a candy store."
            scene w3_2774 with dissolve
            mc "I mean... everything seemed fine? I don't really know what the criteria is."
            scene w3_2773 with dissolve
            kat "You most certainly do."
            scene w3_2775 with dissolve
            "......"
            "..."
            scene w3_2776 with dissolve
            kat "Oh, for-- just... let loose next weekend. That's an order."
            scene w3_2764 with dissolve
            mc "Right."

    if minaFlag == True:
        play sound "sound effects/sms-chime.wav"
        scene w3_2779 with dissolve
        "*Beep*"
        scene w3_2780 with dissolve
        mct "(It's Mina...)"
        kat "Well, I'll leave you to it."
        mct "(What does she...?)"
        scene black with fade
        stop music fadeout 3.0
        if minaCheat == True:
            "She said she wanted to play some games and a very conspicuous \"whatever\"...?"

            if hanaGF == True:
                mct "(Well, this was inevitable. With what I promised Hana last night, I should probably tell her I can't help with her list anymore... {b}right{/b}...?)"
                "The least I can do is tell her in person."
            else:
                "Well, I am still feeling a little frisky... and quite frankly, Mina's company sounded like sweet relief from the tension of this place."
        else:

            "Shockingly, she said she was bored and wanted to hang out."
            mct "(I can't bring myself to say no after turning her down like I did the other night...)"

        "......"
        "..."
        jump w3IanVisit
    else:

        scene w3_2781 with dissolve
        mc "If you don't mind, I'm going to leave."
        scene w3_2782 with dissolve
        kat "Have an enjoyable rest of your evening, Mr. [mcl]."
        scene black with fade
        stop music fadeout 3.0
        "......"
        "..."
        "{i}Thanks{/i}."
        jump w3IanVisit


label w3MinaHanaGFHangStart:

    scene w3_2783 with circlewipe
    "After killing time at Ian's"
    "I thought it best if Mina and I met on familiar, intermediary grounds. If I was going to be frank with her about Hana, there was no sense in having one of us go all the way to the other's place only to awkwardly remain after ending our bizarre deal."
    scene w3_2784 with dissolve
    "Of course..."
    play music "music/happy-boy-end-theme.ogg"
    scene w3_2785 with dissolve
    mina "[mcf]! Hey!"
    scene w3_2786 with dissolve
    mc "Been waiting long?"
    mina "Nope, just--"
    scene w3_2787 with dissolve
    mina "Mmmmh, just got here."
    scene w3_2788 with dissolve
    "Of course, the moment I saw her glowing face and felt the force of her thermonuclear hug, I remembered why I had entered the deal with her in the first place."
    scene w3_2789 with dissolve
    mc "Come to think of it, this is where we first met, wasn't it?"
    scene w3_2790 with dissolve
    mina "Sure was!"
    scene w3_2789 with dissolve
    "I had come here, intending to do the right thing by Hana..."
    hide screen textbox2 with dissolve

    menu:
        "Hug her tighter.(Dialouge/render changes only)":

            show screen textbox2 with dissolve
            mct "(Ah, fuck it. There's no harm in being friendly.)"
            scene w3_2791 with dissolve
            "For the sake of recollection, even if it was just a few weeks ago."
            mc "How are you?"
            mina "I was bored, but now I'm better by the second!"
            scene w3_2793 with dissolve
            mc "I expected you might say that, but let's order while the line is so short."
        "Kiss her on the forehead.":

            show screen textbox2 with dissolve
            "I couldn't deny that-"
            scene w3_2792 with dissolve
            "*Cwhup!*"
            "...that even if I had only known her for a few weeks, moments like this conjured up a swell of affection."
            mina "That tickles!"
            scene w3_2793 with dissolve
            mc "Sorry, but let's order while the line is so short."
        "Suggest we order.":

            mc "We should order while the line is so short."

    scene black with fade
    mina "Good idea!"
    scene w3_2794 with fade
    mc "This is even the same table as the day we met."
    mina "Ha ha, is it?"
    scene w3_2795 with dissolve
    mc "Yep. I can recall it vividly... because, for a measly second, you actually looked annoyed to meet me."
    mina "No, I didn't!"
    mc "You did! I remember it because what came after that single second was one hell of a greeting."
    scene w3_2796 with dissolve
    mina "Oh no, you had me pegged as a fake bitch from the beginning, huh?"
    mc "I saw someone {i}choosing{/i} to make someone feel welcome."
    scene w3_2797 with dissolve
    mina "Hmpfh... feels like a long time ago."
    scene w3_2798 with dissolve
    mc "Yeah... you had a boyfriend back then, if I remember correctly."
    scene w3_2799 with dissolve
    mina "...did I?"
    mina "......"
    scene w3_2800 with dissolve
    mina "...feels more like an anchor wrapped around my neck in hindsight."

    if w2ExEndingMina == True:
        scene w3_2801 with dissolve
        mc "Are you over the hump?"
    else:
        scene w3_2802 with dissolve
        mina "I guess Ian told you?"
        scene w3_2801 with dissolve
        mc "Yep, we hung out Sunday morning, right after you broke the news. Are you over the hump?"

    scene w3_2800 with dissolve
    mina "Who knows? Too early to say I'm not gonna get weepy out of nowhere, but I'm feeling pretty good right now. It occurs to me..."
    scene w3_2803 with dissolve
    mina "This is my first time being single and out with a man in nearly a year."
    scene w3_2804 with dissolve
    mc "You know, the world's your oyster. You're free to do it with anyone you want now."
    scene w3_2805 with dissolve
    mina "Don't joke about that! You sound like Felicia~ trying to get me to play the field."
    scene w3_2806 with dissolve
    mc "Well... I mean... {i}shouldn't{/i} you? Your goal is to get some experience, right? Want me to play wingman for you so--"
    scene w3_2807 with dissolve
    mina "Are you TRYING to hurt my feelings? I know we're not dating, but WHO am I getting coffee with right now?"
    scene w3_2808 with dissolve
    "......"
    "..."
    "I came here to tell her I couldn't help her with her list, but looking at the anger on Mina's face at my mere suggestion..."
    scene w3_2809 with dissolve
    mct "(This must be what it feels like to {i}swoon{/i}.)"
    "......"
    "..."
    scene w3_2810 with dissolve
    mina "The only person... ah."
    scene w3_2811 with dissolve
    "I came here to tell her I had changed my mind, but with the way she was blushing..."
    scene w3_2812 with dissolve
    mina "Y-you are..."
    scene w3_2813 with dissolve
    mina "{size=-10}TheonlypersonIwanttobewithrightnowisyou.{/size=-10}"
    "......"
    "..."
    scene w3_2814 with dissolve
    mc "I couldn't hear you."
    scene w3_2815 with dissolve
    mina "I said..."
    scene w3_2816 with dissolve
    mina "Right now, the only person I want to do stuff like that with is you, [mcf]."
    scene w3_2817 with dissolve
    "Shit like {b}that{/b}, said with that face... made me realize just how susceptible I was to a woman's wiles despite other intentions."
    scene w3_2818 with dissolve
    mc "Goddamnit, you're an oustanding actress."
    scene w3_2819 with dissolve
    mina "What?! I'm embarrassed as hell right now!"
    scene w3_2820 with dissolve
    mc "Enough that you had to bury your face in your arms?"
    scene w3_2821 with dissolve
    mina "Body language is crucial..."
    "...or perhaps there was something about Mina that I couldn't resist."
    stop music fadeout 3.0
    hide screen textbox2 with dissolve
    scene w3_2822 with dissolve

    menu:
        "Reaffirm your intention to help her."(chg=["tough_up5"]):
            $ toughness += 5
            play music "music/ukulele-fun.ogg"
            show screen textbox2 with dissolve
            "I knew this was a violation of what I promised Hana last night."
            scene w3_2823 with dissolve
            mc "Sorry. I'm just teasing you."
            scene w3_2824 with dissolve
            "A promise I didn't have to make but did."
            scene w3_2825 with dissolve
            mc "You know I promised to help you."
            scene w3_2824 with dissolve
            "A promise that I made to Hana despite another promise given to Mina."
            scene w3_2826 with dissolve
            mc "Is... that why you called today?"
            scene w3_2827 with dissolve
            "My mind could justify this decision in any number of ways."
            mina "Mmmhh...?"
            scene w3_2828 with dissolve
            "Hana will probably never find out, but even if she did..."
            scene w3_2829 with dissolve
            mina "...a girl's got a hope?"
            scene w3_2828 with dissolve
            "What hope did we actually have to last?"
            scene w3_2830 with dissolve
            mc "Well, then... finish your coffee."
            "Besides, Mina would come to her senses and realize that our relationship is predicated on her girlish heartbreak and that this whole list thing was asinine and I had nothing to actually offer her as a person..."
            scene w3_2831 with dissolve
            mc "Finish your coffee and we'll start seeing about that list of yours."
            "--those kinds of justifications. I refused to make them. If you're going to be shitty, I believe you should embrace it."
            mina "O-oh..."
            scene w3_2832 with dissolve
            "Acknowledging the consequences of your actions is the most critical step in taking precautions against them."
            scene w3_2833 with dissolve
            "And at the end of the day, even if it casts light on me being a fool, I wanted to enjoy Mina's company more. That was all there was to it."
            stop music fadeout 2.0
            scene black with fade
            "I'm a selfish asshole."
            jump w3MinaOutsideFrisk
        "Resist. Tell Mina about your new relationship with Hana(hanaTwoTime = False,minaBreakOff = True)."(chg=["tough_down5"]):


            $ toughness -= 5
            $ hanaTwoTime = False
            $ minaBreakOff = True
            play music "music/future-rennaisance.ogg"
            scene w3_2834 with dissolve
            show screen textbox2 with dissolve
            mc "Things have changed."
            "Like diving into a cold pool, I shut off my brain and spit the words out."
            scene w3_2835 with dissolve
            mina "Things have... {i}changed{/i}?"
            mc "Yeah... uh... as it happened, I got myself into a committed relationship last night."
            scene w3_2836 with dissolve
            "......"
            "..."
            scene w3_2837 with dissolve
            mina "You know I came here, hoping... {b}w-wow.{/b}"
            scene w3_2838 with dissolve
            mina "Wow, that's a kick in the fucking stomach."
            scene w3_2839 with dissolve

            if w3MinaTransparent == True:
                mina "Hana, right...? Ha... you told me it was a casual thing."
                scene w3_2840 with dissolve
                mc "I {i}really{/i} thought that, but... ah... you have every right to be angry after I promised that I-"
            else:
                mina "I guess you two must've had a thing and then I went and forced myself on you the other day."
                scene w3_2840 with dissolve
                mc "It was unexpected and just happened."
                scene w3_2841 with dissolve
                mina "What kind of bullcrap- ah..."
                scene w3_2840 with dissolve
                mc "You have every right to be angry after I promised that I-"

            scene w3_2842 with dissolve
            mina "I'm not angre- ah, I mean, I kinda am? Feelin' kinda a lot of things..."
            mina "In my head, I knew this wasn't a-- I still kinda had some expectations-- and definitely didn't think our fun would end this soon."
            scene w3_2843 with dissolve
            mc "I shouldn't have been so haphazard with my promises."


            if w2ExEndingMina == True:
                scene w3_2842 with dissolve
                mina "When you dropped by the other night, I thought..."
                scene w3_2843 with dissolve
                mc "I'm sorry."
                scene w3_2842 with dissolve
                mina "Well, it's not like you strung me along... I came onto you."
            else:
                scene w3_2842 with dissolve
                mina "Well, I'm the one who came onto you so hard, so it's not like you strung me along."

            scene w3_2843 with dissolve
            mc "I feel like a fucking asshole considering the timing with you and Ian."
            scene w3_2842 with dissolve
            mina "...I want to agree with you, but those are hurt feelings. I'm actually glad you're a decent guy."
            scene w3_2844 with dissolve

            if w3MinaTransparent == True:
                mina "You could've dated her and fucked me on the side, but you didn't. You were... upfront. {i}Sort of{/i}."
            else:
                mina "You could've dated whoever and--"
                mc "It's Hana."
                mina "Hana..? Ha, that makes sense."
                mina "You could've dated her and fucked me on the side, but you didn't. You were... upfront. {i}Sort of{/i}."

            scene w3_2845 with dissolve
            mina "Gives me some hope about what's out there..."
            scene w3_2846 with dissolve
            mina "Still feel like rejected trash..."
            scene w3_2847 with dissolve
            mc "......"
            mina "..."
            stop music fadeout 4.0
            scene w3_2848 with dissolve
            "We awkwardly finished our coffee, and then Mina wisely thought it best for her to return home."
            "She reassured me that she was fine and that she was grateful for my honesty but it all sounded half-hearted."
            "She even said she hoped to remain friends and I said so too, but I doubted. Still, to her immense credit..."
            scene w3_2849 with dissolve
            mina "[mcf]...?"
            mc "Yeah?"
            scene w3_2850 with dissolve
            mina "Come here!"
            play music "music/inner-light.ogg"
            scene w3_2851 with dissolve
            mc "Mina..."
            scene w3_2852 with pixellate
            "To her credit, her hug goodbye had every ounce of goodwill and warmth as the day we met."
            "I knew, from her hug alone..."
            scene mina_farewell_a with pixellate
            show mina_farewell with dissolve
            mina "Hana's really cool."
            "I knew from her hug that she really did mean those words."
            mina "I hope you two build something that makes my dumb feelings right now worth it."
            "I knew from her hug that her fear of only imitating how to respond to situations was a load of crap."
            mc "Well, it's just starting out... so..."
            "I knew from her hug that Mina was graced with a beautiful, loving presence."
            mina "Thanks again for being there for me these past few days."
            stop music fadeout 3.0
            scene black with fade
            "I knew from her hug that Mina was the kind of warm person I wondered if I could ever be."
            jump w3ExNoMinaFuckCall


label w3MinaFullSpeedHangStart:

    scene w3_2783 with fade
    "After leaving Ian's..."
    "Naturally, given the nature of our relationship, I expected things might take an eventual horizontal turn, but Mina's public company was a treat unto itself."
    scene w3_2784 with dissolve
    mct "(Man, she looks--)"
    play music "music/ukulele-fun.ogg"
    scene w3_2785 with dissolve
    mina "[mcf]! Hey!"
    scene w3_2786 with dissolve
    mc "Been waiting long?"
    mina "Nope, just--"
    scene w3_2787 with dissolve
    mina "Mmmmh, just got here."
    "As she forcefully pressed her body into mine with her characteristic bubbly enthusiasm, I could feel my day getting sweeter by the second."
    scene w3_2789 with dissolve
    mc "Stop, you're going to give me diabetes."
    scene w3_2790 with dissolve
    mina "Ehehe~"
    scene w3_2789 with dissolve
    mc "Come to think of it, this is where we first met, wasn't it?"
    scene w3_2790 with dissolve
    mina "Sure was!"
    scene w3_2788 with dissolve
    "This brought me back to the time Ian introduced the two of us. Just mere weeks, but it..."
    mct "(Feels like a long time ago.)"
    hide screen textbox2 with dissolve

    menu:
        "Hug her tighter(Dialouge/render changes only).":

            show screen textbox2 with dissolve
            scene w3_2791 with dissolve
            mct "(Ah, fuck it. There's no harm in being friendly.)"
            mc "How are you?"
            mina "Mmmmh, I was bored, but now things are looking up!"
            scene w3_2793 with dissolve
            mc "I expected you might say that, but let's order while the line is so short."
        "Kiss her.":

            show screen textbox2 with dissolve
            scene w3_2853 with dissolve
            mc "Hey, look up for a second."
            mina "...huh? Wha-"
            scene w3_2854 with dissolve
            "*Chwup~"
            "That was the one remarkable difference between then and now."
            mina "Mmmhh..."
            "There was no Ian here, only Mina and myself, and she freely gave her lips to me."
            scene w3_2793 with dissolve
            mc "Let's order while the line is so short."


    scene black with fade
    mina "Mmmm-kay!"
    scene w3_2794 with fade
    mc "This is even the same table as the day we met."
    mina "Ha ha, is it?"
    scene w3_2795 with dissolve
    mc "Yep. I can recall it vividly... because, for a measly second, you actually looked annoyed to meet me."
    mina "No, I didn't!"
    mc "You did! I remember it because what came after that single second was one hell of a greeting."
    scene w3_2796 with dissolve
    mina "Oh no, you had me pegged as a fake bitch from the beginning, huh?"
    mc "I saw someone {i}choosing{/i} to make someone feel welcome."
    scene w3_2797 with dissolve
    mina "Hmpfh... feels like a long time ago."
    scene w3_2798 with dissolve
    mc "Funny, I thought that myself."
    scene w3_2797 with dissolve
    mina "Is that funny?"
    scene w3_2798 with dissolve
    mc "If I remember correctly... you had a boyfriend back then."
    scene w3_2799 with dissolve
    mina "...did I?"
    mina "......"
    scene w3_2800 with dissolve
    mina "...feels more like an anchor wrapped around my neck in hindsight."

    if w2ExEndingMina == True:
        scene w3_2801 with dissolve
        mc "Are you over the hump?"
    else:
        scene w3_2802 with dissolve
        mina "I guess Ian told you?"
        scene w3_2801 with dissolve
        mc "Yep, we hung out Sunday morning, right after you broke the news. Are you over the hump?"

    scene w3_2800 with dissolve
    mina "Who knows? Too early to say I'm not gonna get weepy out of nowhere, but I'm feeling pretty good right now. It occurs to me..."
    scene w3_2803 with dissolve
    mina "This is my first time being single and out with a man in nearly a year. I can flirt as much as I want!"
    scene w3_2804 with dissolve
    mc "If I also recall correctly, that didn't stop you before."
    scene w3_2855 with dissolve
    mina "....."
    mina "..."
    scene w3_2856 with dissolve
    mina "Can you blame me? ...and if *I* remember correctly, you flirted RIGHT back."
    mc "...you think *I* know how to flirt? That's all in your head."
    scene w3_2857 with dissolve
    mina " I do know some things about you for sure."
    scene w3_2858 with dissolve
    mc "...?"
    scene w3_2857 with dissolve
    mina "You know how to grab me... hold me..."
    scene w3_2859 with dissolve
    mina "Kiss me up here... and..."
    scene w3_2860 with dissolve
    mina "...kiss me down-"
    scene w3_2826 with dissolve
    mc "You didn't call to play games today, did you?"
    scene w3_2861 with dissolve
    mina "Ehehe, maybe not!"
    "Her smile was sumptuous and giggle infectious. Just looking at her filled me with a sense of importance."
    scene w3_2862 with dissolve

    if w2ExEndingMina == True:
        mina "You know, when you dropped by Saturday night... you left me hanging..."
    else:
        mina "After what you did to me last Friday, I've missed you..."

    scene w3_2863 with dissolve
    "This woman was a kingmaker. Her time was perhaps wasted on someone like me, but I would happily and greedily gobble it up if she allowed me."
    scene w3_2864 with dissolve
    mc "I figured you would've come to your senses by now about this arrangement."
    scene w3_2865 with dissolve
    mina "...it's not JUST about the list, stupid."
    scene w3_2866 with dissolve
    mc "What else is it about?"
    scene w3_2867 with dissolve
    mina "......"
    mina "..."
    scene w3_2868 with dissolve
    mina "Who you take the journey with is just as important as the destination."
    scene w3_2869 with dissolve
    "A kingmaker indeed. I was brimming with confidence I hadn't earned."
    scene w3_2870 with dissolve
    mc "Just the right time, right place..."
    "I was the most convenient person for her to latch onto, was my thought that was meant to temper my rapidly inflating self-worth."
    scene w3_2871 with dissolve
    mina "Right time, right place... some kindness, some acceptance..."
    mina "A REALLY killer tongue."
    scene w3_2872 with dissolve
    "Okay... that I felt I earned."
    scene w3_2873 with dissolve
    mina "So... will you... show me a \"nice\" time today, [mcf]?"
    scene w3_2874 with dissolve
    mc "After the day I've had... goddamnit, I'm happy to hear that."
    scene w3_2875 with dissolve
    mina "It's only early in the afternoon! What kind of day could you possibly have had?"
    mc "A *frustrating* one."
    mina "Oh..."
    scene w3_2876 with dissolve
    mc "{b}Finish{/b} your coffee."
    scene w3_2833 with dissolve
    mina "O-ohh-"
    stop music fadeout 2.0
    scene black with fade
    mc "You have a long list."
    jump w3MinaOutsideFrisk

label w3MinaPlatonicHangStart:

    scene w3_2783 with fade
    "After spending time at Ian's..."
    "I was glad to see that despite my rejection, Mina thought of me as a friend."
    scene w3_2784 with dissolve
    mct "(There she was!)"
    play music "music/happy-boy-end-theme.ogg"
    scene w3_2785 with dissolve
    mina "[mcf]! Hey!"
    scene w3_2786 with dissolve
    mc "Been waiting long?"
    mina "Nope, just--"
    scene w3_2787 with dissolve
    mina "Mmmmh, just got here."
    "Like always, she hugged me as if it was the most natural thing in the world, and she really made me believe it."
    scene w3_2789 with dissolve
    mc "Come to think of it, this is where we first met, wasn't it?"
    scene w3_2790 with dissolve
    mina "Sure was!"
    scene w3_2788 with dissolve
    "If she held any bitterness from me turning her down last Friday, then she didn't let it show through."
    hide screen textbox2 with dissolve

    menu:
        "Make a joke(Dialouge/render changes only)":
            scene w3_2877 with dissolve
            show screen textbox2 with dissolve
            mc "Killing me with kindness?"
            mina "...eh? What?"
            scene w3_2878 with dissolve
            mc "Nothing. I'm glad to see you too. How are you?"
            scene w3_2879 with dissolve
            mina "{b}Gooooooood!{/b}"
            scene w3_2878 with dissolve
            mc "Line's looking pretty short. Let's get some drinks."
        "Hug her tighter.":
            scene w3_2791 with dissolve
            show screen textbox2 with dissolve
            mct "(Ah, fuck it. There's no harm in being friendly.)"
            mc "How are you?"
            mina "Mmmmh, I was bored, but now things are looking up!"
            scene w3_2793 with dissolve
            mc "I expected you might say that, but let's order while the line is so short."


    scene black with fade
    mina "Good idea!"
    scene w3_2794 with fade
    mc "I didn't expect to hear from you, at least not so soon."
    mina "Oh, no. I hope I wasn't imposing by asking-"
    scene w3_2795 with dissolve
    mc "That's not what I was getting at. Just that I would understand if I never heard from you again."
    mc "I mean, what kind of idiot forces someone to stick around and watch a movie after... well..."
    mina "No, no, no! I'm glad you did! I said as much, didn't I?"
    scene w3_2796 with dissolve
    mc "I don't remember. Maybe?"
    "Honestly, the whole of June feels like a fog..."
    scene w3_2880 with dissolve
    mina "Well, what you did was extremely helpful... it put things into perspective for me..."
    mina "I thought a man's first priority was sex... that was what it seemed like to me..."
    scene w3_2881 with dissolve
    mina "Point is, the fact that you stuck around to be a friend, that was better than if you had given me what I was hoping for."
    scene w3_2801 with dissolve
    "......"
    "..."
    "Her words felt convenient and I didn't know how to respond without sounding full of myself."
    scene w3_2802 with dissolve
    mina "Like, {b}really{/b}."
    scene w3_2825 with dissolve
    mc "...I heard from Ian that you two broke up."
    scene w3_2824 with dissolve
    mina "That's right... it went..."
    mina "It went a lot smoother than I imagined it."
    scene w3_2826 with dissolve
    mc "Great, I'm glad. You got a dating history now!"
    scene w3_2882 with dissolve
    mina "I guess I do, huh? Pretty big baggage for the first go around..."
    scene w3_2883 with dissolve
    mc "Healthy dose of wisdom too perhaps. Don't fall for the same shit next time, right?"
    scene w3_2882 with dissolve
    mina "Pff, I'll try not to!"
    scene w3_2884 with dissolve
    mc "..."
    scene w3_2885 with dissolve
    mc "...you know, this is the same table we sat at when we first met."
    scene w3_2886 with dissolve
    mina "Ha ha, is it?"
    mc "Yep. I can recall it vividly... you looked pretty unhappy about meeting me."
    scene w3_2887 with dissolve
    mina "No I didn't! I didn't show that, did-"
    mc "You did! You looked unhappy, but you quickly bounced back in like a fraction of an instant. The only reason I remember it is you gave me a great, big, remarkably warm greeting after that."
    scene w3_2888 with dissolve
    mina "Uuuhg, you had me pegged as a fake bitch from the beginning?"
    mc "You didn't let your gut reaction control you. That's cool."
    scene w3_2889 with dissolve
    mina "Hmpfh... feels like a long time ago."
    mc "Ha, doesn't it?"
    scene w3_2891 with dissolve
    "......"
    "..."
    scene w3_2892 with dissolve
    "As a moment of silence came to pass, Mina just smiled warmly and waited patiently for a sprout of a conversation to grow, well aware that it would only become an {i}awkward{/i} silence if we allowed it to be so."
    "Following suit, I didn't let my mind turn inward and self-analyze. Instead, I just did what was natural: focus on the pretty lady before me."
    "Mina, like usual, looked stunning today. Of course, that went without saying, but there was just something about a blonde in a simple pair of daisy dukes that... and not to mention the sheerness of her blouse that... ah..."
    scene w3_2861 with dissolve
    "With any luck, to return hers in kind, looking Mina over put a smile on my face."
    scene w3_2826 with dissolve
    mc "So... what did you want to do today?"
    scene w3_2861 with dissolve
    "Because, failing that, I probably just look like a pervert."
    scene w3_2893 with dissolve
    mina "Umm... well, I don't actually know... ha, I asked you to hang with no plan whatsoever!"
    mina "I expected you to blow me off. The only thing we have in common is video games, which goes for everyone..."
    scene w3_2895 with dissolve
    mc "Don't worry. We'll come up with something. Actually, how about..."
    mina "Hmm...?"
    scene w3_2894 with dissolve
    mc "How 'bout we just spend the day figuring out what other interests we have in common."
    scene w3_2893 with dissolve
    mina "That... sounds {i}lovely{/i} to me, [mcf]."
    scene w3_2896 with dissolve
    mc "Let's start here. You like coffee?"
    mina "Yeah! Who doesn't?"
    scene w3_2897 with dissolve
    mc "Me."
    mina "Pffh, why are you drinking it?"
    mc "We're at a coffee shop."
    scene w3_2898 with dissolve
    mina "Pfffh, haa, hha- what kind of logic is that? Hahahaha!"
    mina "You should've got tea!"
    scene w3_2899 with dissolve
    mc "I'm even less of a tea drinker."
    scene w3_2900 with dissolve
    mina "I thought we were trying to find things we had in common."
    scene w3_2899 with dissolve
    mc "You don't ever find yourself going with the flow sometimes?"
    scene w3_2901 with dissolve
    mina "That- ah, I {b}do{/b}..."
    scene w3_2902 with dissolve
    mc "Let's mark that down as something we have in common."
    scene w3_2800 with dissolve
    mina "Ha! Yeah, okay, sure!"
    scene w3_2801 with dissolve
    mc "See? You're really good with going with the flow. So, let's keep that momentum going and say... go for a walk?"
    scene w3_2800 with dissolve
    mina "Hehehe, sure."
    mina "Let's finish the coffee you don't like first."
    stop music fadeout 3.0
    scene black with fade
    mc "This barely counts as coffee."
    play music "music/ukulele-fun.ogg"
    scene w3_2903 with circlewipe
    "So, we set out on a quest, chatting and aimlessly hoofing it around the city."
    "Naturally, we only shared a few interests. That was to be expected between me not having very many in the first place and our upbringings being so vastly different."
    scene w3_2905 with ccirclewipe
    "The one thing that our walk did help me understand was something that was vastly more important than common hobbies or geeking out over the same shit."
    "Mina simply had something that I lacked."
    "Like a cat basking in the warmth of a radiator, it was a delight to be around her."
    "I already knew this, but it confirmed her uncanny ability to make you feel important."
    scene w3_2906 with circlewipe
    "She was a great listener, eye contact and smile never wavering as I griped about the aspects of university life I found annoying."
    mct "(Wait, am I really bitching this much?)"
    "Sure, I'd admit a thing or two to my mom, but it was pouring freely with Mina."
    "Up to this point, all we had ever talked about was Ian, her work, her life... everything had a cause, and it was rarely about me. Of course, I preferred that way, but now she was extracting details from me that I was happy to provide."
    play sound "sound effects/car-beep.wav"
    scene w3_2904 with ccirclewipe
    "I told her about my experience growing up without a dad, which she related to herself as a child of divorce."
    "I yammered in detail about things I often thought about but rarely spoke... memories of summer camp and the rare vacation my mom managed to swing."
    "Yep, we had very little in common besides sharing a time, a place, and a mood. That was WONDERFULLY simple in my mind."

    if hanaGF == True:
        "That was all that was needed for a good friendship."
        stop music fadeout 3.0
        scene black with fade
        "...oh, and truth be told, on a superficial level, I enjoyed the jealous look of strangers trying to figure out what the deal was."
        jump w3ExNoMinaFuckCall
    else:
        scene black with fade
        "...oh, and truth be told, on a superficial level, I enjoyed the jealous look of strangers trying to figure out what the deal was."
        scene w3_2907 with blinds
        "I enjoyed our company so much that a root of self-doubt planted itself in my head."
        "What did the radiator get from the cat?"

    scene w3_2908 with cmet
    mc "Can I ask you something? Do you actually enjoy talking to me?"
    mina "Huh...? {b}Yeah!{/b} You're a lot of fun!"
    "No hesitation."
    scene w3_2909 with dissolve
    mc "Thanks..."
    scene w3_2910 with dissolve
    mina "Yeah, no problem! Why the heck do you ask?"
    scene w3_2909 with dissolve
    mc "Just being on brand for a guy like me."
    scene w3_2911 with dissolve
    mina "How do you figure you're like, [mcf]? I'd love to hear it!"
    scene w3_2909 with dissolve
    mc "...lacking in interpersonal value?"
    scene w3_2910 with dissolve
    mina "Where would you get that idea? Have we not been \"inter-personalizing\" the last month?"
    scene w3_2912 with dissolve
    mc "Eh... I chalk it all up to convenience, circumstance, and the brewing storm with Ian..."
    scene w3_2913 with dissolve
    mina "Well, fuck you too."
    scene w3_2914 with dissolve
    mc "Shit, I didn't mean to make you mad."
    scene w3_2915 with dissolve
    "......"
    "..."
    scene w3_2914 with dissolve
    mc "Why are you mad?"
    scene w3_2913 with dissolve
    mina "Figure it out, you geek!"
    scene w3_2916 with dissolve
    "......"
    "..."
    scene w3_2917 with dissolve
    mc "Sorry, I didn't mean to make you sound opportunistic."
    mina "Yeeeeeah, you did..."
    mc "I'm a cynical person. The things I say reflect more on me than others."
    scene w3_2918 with dissolve
    "......"
    "..."
    scene w3_2919 with dissolve
    mina "No, I get it..."
    scene w3_2920 with dissolve
    "......"
    "..."
    scene w3_2919 with dissolve
    mina "I mean, I confessed to you that I think I'm a freakin' robot sometimes. {b}I get it{/b}."
    scene w3_2921 with dissolve
    mina "I see those qualities in other people too. It's why I can't wrap my head around why you wanted to hang out today."
    mina "Men and women... what do they do together besides sex? If you don't want {i}that{/i}, then what the hell do I even offer?"
    scene w3_2922 with dissolve
    mc "Damn. You're just as bad as me."
    scene w3_2923 with dissolve
    mina "Maybe!"
    scene w3_2924 with dissolve
    mc "The all-girls-school into dating a shitbag did a number on how you think about guys, huh?"
    scene w3_2925 with dissolve
    mina "Definitely!"
    scene w3_2926 with dissolve
    mc "Truth be told, I find you very soothing to be around."
    scene w3_2927 with dissolve
    mina "H-huh...? Heh, I don't know how I should take that."
    scene w3_2928 with dissolve
    mc "That and I have next to no friends. Can't be picky, but what about you?"
    scene w3_2927 with dissolve
    mina "Hurt pride...?"
    scene w3_2928 with dissolve
    mc "Ha, that really it?"
    scene w3_2927 with dissolve
    mina "You decide, Mr. Cynic."
    scene w3_2929 with dissolve
    "......"
    "..."
    "Yet another silence, in a long series of silences today..."
    scene w3_2930 with dissolve
    "As always, Mina smiled openly without showing any doubt or fear."
    "All day I found that admirable, but it was also sad, wasn't it?"
    stop music fadeout 3.0
    hide screen textbox2 with dissolve

label w3MinaParkKiss:

    menu w3MinaPlatonicSwitch:
        "{color=#FF1493}[Romance]{/color} Fuck it. You're only a man.":
            scene w3_2931 with dissolve
            "This time, I went with the flow - pushing all doubts about motivation and circumstances back down into my gut."

            if Mina_Affection >=10:
                scene w3_2932 with dissolve
                "Was the situation all that different from the other day? Nah."
            else:
                $ Mina_Affection -=3
                scene w3_2952 with dissolve
                jump w3MinaKissRejection

            "Not at all."

            if Mina_Affection >=15:
                scene w3_2933 with dissolve
                "Did the fact she broke up with Ian change anything?"
            else:
                $ Mina_Affection -=1
                scene w3_2952 with dissolve
                jump w3MinaKissRejection

            "I mean... waiting a whole two days? Not to him, but it may have made an appreciable difference for us."
            "It was now in Mina's court if she wanted to return my rejection."

            if Mina_Affection >=23:
                $ Mina_Affection += 4
                $ minaCleanStart = True
                play music "music/inner-light.ogg"
                scene mina_parkiss_a with dissolve
                show mina_parkiss with dissolve
                mina "Mmmhhh..."
                "She accepted, and I refused to ruminate on why."
                " Did she really find my company worthwhile? I'll trust her."
                mina "A-aah...!"
                "I'll trust her and sit my ass as close to that radiator as I can get."
                scene w3_2934 with dissolve
                mina "Ha, haa...! S-seriously-!"
                scene w3_2936 with dissolve
                mc "What?"
                scene w3_2934 with dissolve
                mina "Mixed signals, much?!"
                scene w3_2936 with dissolve
                mc "As you astutely pointed out earlier... I'm a guy and you're a--"
                scene w3_2934 with dissolve
                mina "Shut up."
                scene mina_parkiss_a with dissolve
                show mina_parkiss with dissolve
                mina "MMmhh...!"
                "This time, she pressed her lips to mine, with an added dose of frustration."
                mct "(Man, I got to ask her where she gets her lip balm, she tastes-)"
                scene w3_2937 with dissolve
                mina "That was true the other day too, you pasty freak."
                scene w3_2936 with dissolve
                mc "Timing is important."
                scene w3_2934 with dissolve
                mina "What? Not good enough to pull you in the first go, but good enough to wear you down?"
                scene w3_2938 with dissolve
                mc "Last time it was about Ian."
                scene w3_2939 with dissolve
                mina "It was a lot of things..."
                scene w3_2938 with dissolve
                mc "Now it felt more like just the two of us sitting on a bench, so I forgot everything else."
                scene w3_2937 with dissolve
                mina "You don't know how close I was to spitting in your face."
                scene w3_2936 with dissolve
                mc "But you didn't."
                scene w3_2940 with dissolve
                mina "..."
                scene w3_2941 with dissolve
                mc "Thank you for not doing that."
                scene mina_parkiss2_a with dissolve
                show mina_parkiss2 with dissolve
                mina "Mmmhh...♥"
                "*Chwup, fwhup~*"
                scene w3_2942 with dissolve
                show screen textbox2 with dissolve
                if not persistent.w3MinaParkKiss:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w3MinaParkKiss = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                mina "Wanna go back to your place?"
                scene w3_2943 with dissolve
                "She was surprisingly forward."
                scene w3_2944 with dissolve
                mc "Ian's sick, but you never know; he could drop by. How about yours?"
                scene w3_2945 with dissolve
                mina "When I was brooding this weekend, I realized something."
                mc "...?"
                scene w3_2946 with dissolve
                mina "Way too pink!"
                mc "Pffh- really?"
                stop music fadeout 2.0
                scene w3_2947 with dissolve
                mina "*Gulp* Let's... let's get a hotel room..."
                mc "Okay."
                scene black with fade
                "Go with the flow."
                $ renpy.end_replay()
                play music "music/everything-you-wanted.ogg"
                jump w3MinaHotel
            else:

                scene w3_2953 with dissolve
                jump w3MinaKissRejection
        "{color=#FF1493}[Friend]{/color} Let's go play some video games.":



            play music "music/happy-whistling-ukulele.ogg"
            show screen textbox2 with dissolve
            "As I had previously, I felt a tug from inside of myself, compelling me to close the distance between myself and the pretty girl and see where it all led."
            "Just as I had previously, I ignored that urge."
            scene w3_2948 with dissolve
            "*Boop!*"
            scene w3_2949 with dissolve
            mina "Pffha, ha-haha- w-wha~ ah... you looked so serious for a moment!"
            scene w3_2950 with dissolve
            mc "Let's go drop by the arcade."
            mina "Hehe, sure!"
            scene w3_2951 with dissolve

            if w2MinaBetWin == True:
                mc "You know, I remember last time you ended up owing me a favor. Maybe we'll make it another one."
                mina "Fat chance! That's only because you got my brother to distract me!"
                mc "You knew?"
                scene black with fade
                mina "Pff, you try hard! Do you think he didn't tell me?"
                $ renpy.end_replay()
                jump w3ExNoMinaFuckCall
            else:
                mina "Maybe I'll get another piggyback out of it."
                mc "You should aim higher than that."
                stop music fadeout 3.0
                scene black with fade
                mina "Should I?"
                $ renpy.end_replay()
                jump w3ExNoMinaFuckCall


label w3MinaKissRejection:
    $ w3MinaRejection = True
    play music "music/happy-whistling-ukulele.ogg"
    show screen textbox2 with dissolve
    mina "You got something on your lip."
    mc "Oh..?"
    scene w3_2954 with dissolve
    "Mina was very kind."
    mc "Did I get it?"
    "I played along."
    scene w3_2955 with dissolve
    mina "Yeah, all gone."
    scene w3_2956 with dissolve
    mc "Thanks..."
    scene w3_2955 with dissolve
    mina "Don't mention it..."
    scene w3_2957 with dissolve
    "......"
    "..."
    "Even now, she smiled."
    scene w3_2958 with dissolve
    mina "Want to go watch a movie?"
    scene w3_2959 with dissolve
    mc "Ha, hahaha! Oh-"
    "Okay, she didn't let it {i}totally{/i} slide."
    mina "What's so funny? Isn't that like the only thing you do besides studying?"
    mc "Ha, ohhaoo..!"
    scene black with fade
    mina "Dang nerd, but no thanks. I think I'm going to head home."
    jump w3ExNoMinaFuckCall


label w3MinaOutsideFrisk:
    play ambient "sound effects/city-night.wav"
    scene w3_2960 with dissolve
    mina "So... uh..."
    mina "You were implying that we are going to-"
    scene w3_2961 with dissolve
    mc "So, what do you want to do?"
    mina "What?"
    scene w3_2962 with dissolve
    mc "It's up to you. I'm at your disposal."
    mina "Euech... don't say it like that!"
    mc "We could play games like you said, maybe watch a movie..."
    stop ambient fadeout 3.0
    play music "music/everything-you-wanted.ogg"
    scene w3_2963 with dissolve
    mc "You could pick anything on your \"list\" and we can see about making it a reality..."
    mina "*Gulp* A-anything...?"
    scene w3_2964 with dissolve
    mc "Why don't you tell me what's on it?"
    mina "That's, uh... ah..."
    mc "We're past the point of you being shy."
    scene w3_2965 with dissolve
    mina "You turd! Stop trying to be suave!"
    mc "You gotta tell me."
    scene w3_2966 with dissolve
    mina "You're suddenly putting me on the spot, like what do I- ah... let's..."
    mina "Let's go to a hotel."
    scene w3_2967 with dissolve
    mc "That's on your list?"
    scene w3_2966 with dissolve
    mina "Yeah... I want to see if it'll feel... {i}illicit{/i}... plus... "
    scene w3_2968 with dissolve
    mina "......"
    scene w3_2966 with dissolve
    mina "...we haven't even done {i}it{/i} yet."
    scene w3_2969 with dissolve
    "Seeing her conscious of her surroundings made me want to bully her a little."
    scene w3_2970 with dissolve
    mc "Done what...?"
    "I would have been mortified right there with her a few weeks ago."
    scene w3_2971 with dissolve
    mina "I told you to stop trying to be cool."
    scene w3_2972 with dissolve
    mc "Tell me."
    mina "Hnnn... waw-wahh-"
    scene w3_2973 with dissolve
    mc "How can I help without you being explicit about it? What do you want to do today?"
    scene w3_2974 with dissolve
    mina "......"
    scene w3_2975 with dissolve
    mina "..."
    scene w3_2976 with dissolve
    mc "We're the only people who matter."
    "I did wonder if her list included a public display like this."
    scene w3_2977 with dissolve
    mina "........."
    mina "....."
    scene w3_2978 with dissolve
    mina "...I want you to mess me up."
    scene w3_2979 with dissolve
    mct "(--!)"
    scene w3_2980 with dissolve
    mina "Let's just get a hotel and we can tick off a few of the minor items... okay...?"
    mc "I'm at your disposal."
    scene black with fade
    mina "Stop saying it like that!"
    jump w3MinaHotel

label w3MinaHotel:
    if _in_replay:
        play music "music/everything-you-wanted.ogg"
        show transitionmina03 with cmet
        show screen textbox2 with dissolve
        "Did you cheat with Mina or make a move after they broke up?"
        hide screen textbox2 with dissolve
        menu:
            "You cheated(minaCheat = True).":
                $ minaCheat = True
            "You waited(minaCleanStart = True).":
                $ minaCleanStart = True
        show screen textbox2 with dissolve

    scene w3_2981 with cmet
    play sound "sound effects/car-beep.wav"
    "We made our way to the hotel. I was the one that picked the place, a rather upscale accommodation by my old standards."

    if minaCleanStart == True:
        "I figured {i}what the hell.{/i} This would be our first time. Why not splurge?"
    else:
        "I figured {i}what the hell.{/i} Why not splurge? If she was hoping for something illicit, let her feel like an {i}expensive{/i} woman at least."

    "I was being paid generously for effectively nothing, after all."
    mct "(...I would do well to guard myself against becoming too indulgent.)"

    if minaCleanStart == True:
        scene w3_2982 with blinds
        mina "......"
        scene w3_2983 with dissolve
        mina "..."
        scene w3_2984 with dissolve
        mc "......"
        scene w3_2985 with dissolve
        mc "..."
        scene w3_2986 with dissolve
        play sound "sound effects/elevator-bell.wav"
        "*Ding!*"
    else:
        scene w3_2987 with blinds
        mina "......"
        mina "..."
        scene w3_2988 with dissolve
        mina "Huuh-"
        mc "*Whisper* So, how do you want me to mess you up?"
        mina "Tha--"
        play sound "sound effects/elevator-bell.wav"
        "*Ding!*"

    scene black with fade
    mc "Let's go."
    scene w3_2989 with dissolve
    mina "We didn't have to get such an expensive room..."
    scene w3_2990 with dissolve
    mc "I wanted to."
    scene w3_2991 with dissolve
    mina "Seriously, it's not like we're staying the night."
    scene w3_2992 with dissolve
    mc "We could if you want..."
    hide screen textbox2 with dissolve
    scene w3_2993 with dissolve
    mc "I don't have much going on. Do you?"
    scene w3_2994 with dissolve
    mina "Shut up! I don't have a change of clothes!"
    scene w3_2993 with dissolve
    mc "Mmmh... so? Do we need clothes?"
    scene w3_2995 with dissolve
    mc "Take 'em off so they won't get dirty."
    mina "Hnnngg..."
    scene w3_2996 with dissolve
    mina "I don't have any of my morning treatments!"
    scene w3_2995 with dissolve
    "*Chwup~*"
    mina "Ha, h-ha..."
    mc "This place has everything we need."
    scene w3_2996 with dissolve
    mina "W-we'll see... a whole day and night is a bit..."
    scene w3_2997 with dissolve
    mina "You'll treat me... {i}nice{/i}, right?"
    scene w3_2998 with dissolve

    if minaCleanStart == True:
        mc "How else would I possibly treat you?"
    else:
        mc "I'll treat you any way you ask me to, Mina."

    scene w3_2997 with dissolve
    mina "You know, you'll be the second man I've been with... it's funny..."
    scene w3_2998 with dissolve
    mc "What is?"
    scene w3_2997 with dissolve
    mina "I'm just as nervous as if it was the first time... it's like something's pushing down on my chest..."

    if minaCheat == True:
        mina "I know we've already messed around, but... we didn't..."

    scene w3_2998 with dissolve
    mc "You don't have anything to be nervous about."

    if minaCleanStart == True:
        mc "I have a feeling you're going to eat me alive."
        scene w3_2999 with dissolve
        mina "This isn't just about me..."
        mina "I want us to both feel good."
    else:
        mc "You call the shots here."
        scene w3_2999 with dissolve
        mina "This isn't just about me..."
        mina "I want to make some of your fantasies come true too."

    scene w3_3000 with dissolve
    mct "(Ah... this woman!)"
    scene w3_3001 with dissolve
    mina "Hmmm..."
    scene w3_3002 with dissolve
    mina "{size=-10}Probably not complimentary...{/size}"
    mc "What did you say?"
    scene w3_3003 with dissolve
    mina "Oooh, wow..."
    mc "What?"
    scene w3_3004 with dissolve
    mina "Heck of a bed."
    scene w3_3005 with dissolve
    mc "Think it'll do for our purposes?"
    mina "Uh huh... a lot of room ..."
    scene w3_3006 with dissolve
    mina "We're here... so there's only one thing to do..."
    mc "There's no rush."
    scene w3_3007 with dissolve
    mina "...?"
    mc "We have all the time in the world."
    scene w3_3009 with dissolve
    mina "That's different from what you told the front desk."
    scene w3_3008 with dissolve
    mc "I want to make the most of today."
    scene w3_3010 with dissolve
    mina "......"
    mina "..."
    mc "I'll pour us a drink."
    scene black with fade
    mina "What do they have?"
    "......"
    "..."
    scene w3_3011 with fade
    mc "By the way, what was in that bag?"
    scene w3_3012 with dissolve
    mina "Oh, uh... {b}you'll see.{/b} Later."
    mc "How mysterious."
    scene w3_3013 with dissolve
    mina "You won't have to wait long to find out."
    mc "Can't you just tell me now?"
    scene w3_3014 with dissolve
    "......"
    scene w3_3015 with dissolve
    "..."
    scene w3_3016 with dissolve
    mina "Nope!"
    scene w3_3017 with dissolve
    mc "Okay, keep your secrets."
    scene w3_3018 with dissolve
    mina "It's funny. We've only hung out a few times..."
    scene w3_3019 with dissolve
    mc "Let's not reminisce. I want to get to know you better, Mina."
    scene w3_3020 with dissolve
    mina "Sure, but... what should we talk about?"
    scene w3_3021 with dissolve
    mc "Hmmm..."
    scene w3_3022 with dissolve
    "*Glug, glug, glug*"
    scene w3_3023 with dissolve
    mc "How about... we ask each other some questions? "
    mc "Anything either of us would like to know, no matter how personal or embarrassing."
    scene w3_3024 with dissolve
    mina "I could think of a few things I'd like to ask, but..."
    scene w3_3025 with dissolve
    "......"
    "...."
    scene w3_3026 with dissolve
    mina "Whaaaaaaaaat if you don't want to answer them?"
    mc "Only one way to find out: ask me something."
    scene w3_3027 with dissolve
    mina "Anything? Even if it's weird and might kill the vibe?"
    scene w3_3028 with dissolve
    mc "Okay, now I got to know. Hit me."
    "......"
    scene w3_3030 with dissolve
    "..."
    scene w3_3027 with dissolve
    mina "How many women have you slept with, [mcf]?"
    scene w3_3028 with dissolve
    mc "That's what you want to know?"
    scene w3_3029 with dissolve
    mina "You know my complete, pitiful history."
    scene w3_3028 with dissolve
    mc "Fair enough, uh..."
    "This was easier to calculate before the club. Do I count the old woman tugging me off in her office when I first met Veronica?"
    scene w3_3030 with dissolve
    "Do I tell her the number before it began being served to me on a silver platter?"
    scene w3_3031 with dissolve
    mina "Ehehe... you have to think about it that long?"
    scene w3_3030 with dissolve
    mc "Hey! I got three years on you. Of course I have to think about it!"
    scene w3_3032 with dissolve
    mina "Reeeeeeallly?"
    scene w3_3030 with dissolve
    mc "I'm offended that you seem so surprised, quite frankly."
    scene w3_3033 with dissolve
    mina "It's not that! I just figured that was the kind of thing people kept track of!"
    scene w3_3030 with dissolve
    mc "{i}Especially{/i} guys?"
    scene w3_3033 with dissolve
    mina "Everyone!"
    scene w3_3034 with dissolve
    mc "Hmmm..."

    if feliciaSex == True and w2HanaSex == True:
        "I'll go with the number I feel I pulled on my own merit, absent club business, but including Hana and Felicia."
        scene w3_3035 with dissolve
        mc "I've been with five women."
    elif feliciaSex == True and w2HanaSex == False:
        "I'll go with the number I feel I pulled on my own merit, absent club business, but including Felicia."
        scene w3_3035 with dissolve
        mc "I've been with four women."
    elif feliciaSex == False and w2HanaSex == True:
        "I'll go with the number I feel I pulled on my own merit, absent club business, but including Hana."
        scene w3_3035 with dissolve
        mc "I've been with four women."
    else:
        "I'll go with the number I feel I pulled on my own merit, absent club business and before this Summer."
        scene w3_3035 with dissolve
        mc "I've been with three women."

    scene w3_3036 with dissolve
    mina "That's less than I expected..."
    mina "A-ah, I don't mean that in a bad way or anything!"
    scene w3_3037 with dissolve
    mc "I know you didn't."
    scene w3_3038 with dissolve
    "......"
    "..."
    scene w3_3039 with dissolve
    mc "I'm secure with that area of my life."
    scene w3_3040 with dissolve
    mina "Ha! I'm not!"
    scene w3_3041 with dissolve
    "......"
    scene w3_3042 with dissolve
    mina "I've got a lot of things to learn... and probably unlearn too."
    scene w3_3043 with dissolve
    mc "Can I ask you something now?"
    scene w3_3040 with dissolve
    mina "Ask away! I owe you something personal or embarrassing~"
    scene w3_3039 with dissolve
    mc "Whose idea was it to grab a bottle of vermouth and drink it straight?"
    scene w3_3044 with dissolve
    mina "You said the goal was to loosen up, not get blasted."
    mc "Oh, yeah..."
    scene w3_3045 with dissolve
    mina "Heh, feeling loose yet, [mcf]?"
    scene w3_3046 with dissolve
    mc "I've been entirely at ease since we walked into the hotel."
    scene w3_3047 with dissolve
    mina "You're not nervous? Not even... a {i}little{/i} bit?"
    scene w3_3048 with dissolve
    "The worried look on her face told me she'd like me to be - and a few weeks ago, I might've been, but it's not like I could tell her that."
    scene w3_3049 with dissolve

    if minaCleanStart == True:
        mc "I did mention that you had a soothing effect on me."

    mc "How could I be stuck in my head when what's outside of it has my full attention?"
    scene w3_3050 with dissolve
    mina "Ah... aha... you don't have to try so hard. We've already paid for the room..."
    scene w3_3051 with dissolve
    mc "{b}Come here.{/b}"
    mina "Why? What do you want?"
    scene w3_3052 with dissolve
    mc "Just come here. Please?"
    stop music fadeout 3.0
    scene w3_3053 with dissolve
    mina "Heh, sure..."
    scene w3_3054 with dissolve
    mina "What are you thi--"
    scene w3_3055 with dissolve
    mc "Do I seem nervous to you?"
    scene w3_3056 with dissolve
    mina "Guess not..."
    scene w3_3057 with dissolve
    mc "Do you think I'm bullshitting you when I say you're so beautiful that you occupy every thought in my head right now?"
    scene w3_3058 with dissolve
    mina "......"
    mina "..."
    play music "music/ob1.ogg"
    scene w3_3059 with dissolve
    mc "I'm not even sweating how cheesy that line was."
    scene w3_3060 with dissolve
    mina "Ha! Ah... it's getting stuffy..."
    scene w3_3061 with dissolve
    mc "May I?"
    mina "Uhhuh..."
    scene w3_3062 with fade
    mc "You look good in black."
    scene w3_3063 with dissolve
    mina "Thanks..."
    scene w3_3062 with dissolve
    mc "Is this better?"
    scene w3_3063 with dissolve
    mina "There's still one button to go..."
    scene w3_3064 with fade
    mc "By the way, are you still feeling nervous?"
    scene w3_3065 with dissolve
    mina "No... NERVOUS is not what I'm feeling..."
    scene w3_3064 with dissolve
    mc "We're on the same page, then."
    scene w3_3066 with dissolve
    mina "We're not QUITE even-Steven..."
    "Mina tugged cutely at my shirt, making her request known before she even said it."
    mina "Lift your arms."
    scene black with fade
    "I did as she asked, of course."
    scene w3_3067 with fade
    mina "There we go..."
    "In a lovely reversal, her eyes focused on MY chest for once, mapping out its broadness and following down, down, and down beyond the reaches of my stomach."
    scene w3_3068 with dissolve
    mina "........."
    scene w3_3069 with dissolve
    mina "......"
    scene w3_3070 with dissolve
    mina "...what were we talking about again?"
    scene w3_3071 with dissolve

    if w2ExEndingMina == True:
        mc "How did your day go after I left yesterday? You told me you were going to see Felicia?"
    else:
        mc "I was about to ask you how your weekend went."
        scene w3_3072 with dissolve
        mina "It was alright... after ending things with--"
        scene w3_3071 with dissolve
        mc "You can skip that part."
        scene w3_3073 with dissolve
        mina "Ehehe, I hung out with Felicia yesterday. That was nice."

    scene w3_3074 with dissolve
    mina "We went shopping! Then I went back to her place and we spent all afternoon together and into this morning."
    scene w3_3075 with dissolve
    mc "You slept over? Was Elias there?"
    scene w3_3076 with dissolve
    mina "Nope! It was just me, Felish, the bounty from our retail therapy, and one big and empty penthouse."
    scene w3_3075 with dissolve
    mc "Sounds like it was fun."
    scene w3_3073 with dissolve
    mina "It was a lot of wine and bad TV..."
    mina "Bless her heart, she doesn't like either of those things."
    scene w3_3071 with dissolve
    mc "She clearly likes you."
    scene w3_3077 with dissolve
    mina "Ehehe~ doesn't she?"
    scene w3_3078 with dissolve
    "Sitting chest to chest like this, so close to Mina's radiant smile, there was an inevitable pull."

    if minaCleanStart == True:
        "I wanted to kiss her as I had earlier."
    else:
        "I wanted to reach out and grab her."

    "I wanted to--"
    scene w3_3079 with dissolve
    mina "Oh! And speeeeeeeaking of wine..."
    "Mina reached back, jutting her chest out and securely grasping the nearby wine glass."
    scene w3_3080 with dissolve
    mina "I left mine aaaaaall the way over there. Hehe, can we...?"
    scene w3_3081 with dissolve
    mc "{b}We{/b} can share."
    scene w3_3080 with dissolve
    mina "Ehehe~"
    scene w3_3082 with dissolve
    "Without care, she threw her head back, sending flaxen ribbons of hair flittering and exposing the curve of her neck."
    "She knew what she was doing. Her nervous energy had been harnessed, redirected, and put toward a purpose."
    scene w3_3083 with dissolve
    "Her eyes fell on me, and the way her lips languidly parted from the glass rim was as loud as any spoken word."
    mina "Mmmhh..."
    "The way she danced between demureness and provocation was natural. Unforced."
    scene w3_3084 with dissolve
    mina "[mcf]..."
    "As if by instinct alone, she was going for blood."
    scene w3_3085 with dissolve
    mina "I kinda just want to squeeze you right now, [mcf]. This is... {b}easy{/b} company. You're very disarming."
    mina "I mean, I followed you here and crawled right into your lap like some sort of floozy."

    if minaCleanStart == True:
        mina "We only just kissed and HERE I am..."
        scene w3_3086 with dissolve
        mc "At the very least, we're both floozies..."
        scene w3_3087 with dissolve
        mina "Faaaaaair."
    else:
        scene w3_3086 with dissolve
        mc "Does looking at it that way excite you?"
        scene w3_3087 with dissolve
        mina "{b}Yeeeeep...{/b} heh."

    scene w3_3085 with dissolve
    mina "Should guys always be the ones to make a move?"
    scene w3_3086 with dissolve
    mc "Not at all. That's fucking stupid."
    scene w3_3087 with dissolve
    mina "Good..."
    scene w3_3088 with dissolve
    "Mina and I effortlessly fell into a kiss."
    mina "Hmmmwh~"
    "Soft, not {i}too{/i} aggressive, but an ample declaration nonetheless."
    scene w3_3089 with dissolve
    "......"
    scene w3_3090 with dissolve
    "..."
    scene w3_3091 with dissolve
    mina "What are you thinking about right now?"
    scene w3_3090 with dissolve
    mc "......."
    mc "..."
    scene mina_h_fore1_a with dissolve
    show mina_h_fore1 with dissolve
    mina "H-haa...♥ Hello!"
    "I didn't play shy. I grabbed her, {b}like a lover.{/b}"
    mina "I'm glad I didn't have to spell it out..."
    menu:
        "Be straight with her.(Dialouge/render changes only)":
            scene w3_3092 with dissolve
            mc "I told you: I'm not thinking a thing. It's all you up here."
            scene w3_3093 with dissolve
            mina "You're consistent with your sweet talk, I'll give you that."
        "Make a joke.":
            scene w3_3092 with dissolve
            mc "You're the most gropeable thing in this room."
            scene w3_3093 with dissolve
            mina "Heheh, weeeell... you're in the top two."
        "Talk dirty.":
            scene w3_3092 with dissolve
            mc "I'm thinking in 20 minutes, you'll be saying my name and panting like a bitch."
            scene mina_h_fore1_a with dissolve
            show mina_h_fore1 with dissolve
            mina "......"
            mina "...you starting the timer?"

    scene w3_3094 with dissolve
    "Once more, silken floss-like tresses swung arrestingly as the glass remaining contents poured into Mina's mouth."
    scene w3_3095 with dissolve
    "I watched her throat, eagerly awaiting her to swallow and make due on a look that told me she had something to share with me."
    scene w3_3096 with dissolve
    "......"
    "..."
    scene mina_h_fore2_a with dissolve
    show mina_h_fore2 with dissolve
    "What she had to share, it turns out, wasn't words. Once more, she made her move, bringing her lips to mine."
    "This time the kiss wasn't soft. I knew what she intended, and I met her halfway, parting my lips in tandem with hers and accepting the herbaceous and bitter elixir as best I could."
    mc "Mmhh-"
    "We shared the wine, keeping our lips sealed so as not to spill while our tongues entangled violently and worked against that endeavor."
    mina "Euuhwwh~ *gulp*"
    "Eventually, the wine disappeared down our throats, leaving nothing in between us except our lust."
    scene w3_3097 with dissolve
    mina "Ha, heheeh... haaa..."
    "Notes of vanilla carried on hot breath reached my nostrils as we parted and stared hazily into each other's eyes, waiting for either's initiative."
    mina "...saw that in a movie one time."
    scene w3_3098 with dissolve
    mc "That was a complicated maneuver."
    scene w3_3097 with dissolve
    mina "I know, right? Did I surprise you?"
    scene w3_3099 with dissolve
    "Mina was {b}full{/b} of surprises. That was for sure."
    scene w3_3098 with dissolve
    mc "Yeah, you were pretty cool just now."
    scene w3_3097 with dissolve
    mina "Hehehehehe~♥ You better believe it."
    scene w3_3100 with dissolve
    "......"
    "..."

    scene w3_3101 with dissolve
    if minaCleanStart == True:
        mina "There is A LOT I want to try with you..."
    else:
        mina "We're going to have A LOT of fun together..."

    mina "It's time to show you what's in that bag."
    scene w3_3102 with dissolve
    mc "I don't think I care what's in the bag anymore..."
    scene w3_3101 with dissolve
    mina "You will... you'll like it... I have {b}ample{/b} confidence in that."
    scene black with fade
    "So Mina darted to the bathroom, leaving me painfully bereft of a cute blonde in my lap."
    "In the meantime, I poured myself another glass of wine and waited..."
    scene w3_3103 with curtains
    mina "Okay, I'm ready! Close your eyes!"
    scene w3_3104 with dissolve
    "I didn't have to wait long."
    scene w3_3105 with dissolve
    mc "Come on, I... {i}alright{/i}."
    scene w3_3106 with dissolve
    mc "They're closed. Promise."
    scene w3_3107 with dissolve
    "......"
    scene w3_3108 with dissolve
    "..."
    mina "Umm... you can open them..."
    scene w3_3109 with dissolve
    "I thought she sounded so cute right now, but when I opened my eyes..."

    scene w3_3110 with dissolve:
        subpixel True
        yalign 0.7
        xalign 0.6
        linear 8 yalign 0.1
    mc "Wh- ah, {b}holy shit...{/b}"
    scene w3_3111 with dissolve
    "When I opened my eyes, there stood a man-killer, presenting herself with the complete confidence of a model."
    scene w3_3112 with dissolve
    mina "Judging by your reaction, I don't need to ask what you think..."
    scene w3_3113 with dissolve
    mc "You just had THAT in your car?"
    scene w3_3115 with dissolve
    mina "Something I picked up during my shopping trip yesterday..."
    scene w3_3116 with dissolve

    if minaCleanStart == True:
        mina "I was planning on returning it later, but..."
        scene w3_3113 with dissolve
        mc "Well, God bless my timing..."
    else:
        mina "I was hoping it might see some use today."
        scene w3_3113 with dissolve
        mc "Hope is a beautiful thing..."

    menu:
        "Ask her to turn around.(Dialouge/render changes only)":
            mc "Can I see it from behind?"
            scene w3_3114 with dissolve
            mina "..."
            scene w3_3117 with dissolve
            "She did as I asked, sticking her butt out with just the right amount of unnatural to make me want to immediately leap out of my seat."
            mc "Did Felicia help you pick that out?"
            scene w3_3118 with dissolve
            mina "She had a hand in it."

            scene w3_3119 with dissolve
            "I made a mental note to thank that wonderful slut."
            scene w3_3120 with dissolve
            mina "She did suggest I try a more traditional color like red or black, but..."
            scene w3_3119 with dissolve
            mc "You'd look good in both those colors, but no... this {i}suits{/i} you."
            scene w3_3121 with dissolve
            mina "I wear stuff like this for work, but it feels different when there's no camera."
            scene w3_3123 with dissolve
            "I knew the feeling... I've seen a lot of beautiful women in expensive clothing recently, but the intimacy and privacy of a hotel room had it feeling a whole lot different."
            scene w3_3124 with dissolve
            mina "Now, shall we pick back up where we left off?"
        "Fuck waiting. Beckon over the little minx.":

            mc "What the hell are you still doing over there? Get over here."
            scene w3_3114 with dissolve
            mina "..."
            scene w3_3122 with dissolve
            "She closed the gap with a purposeful slowness that had me on the edge of my seat."
            scene w3_3124 with dissolve
            mina "Want a touch?"
            scene w3_3125 with dissolve
            "Goddamn... what a piece of expensive lingerie does to an already impeccable body..."
            scene w3_3126 with dissolve
            "{i}Yeah, I wanted to touch.{/i}"
            scene mina_h_scoop_a with dissolve
            show mina_h_scoop with dissolve
            mina "O-ohh!"
            mc "Christ, you're fucking- ah... you don't mind me being...?"
            mina "Oh, ah... I don't mind. I like it."

            if minaCleanStart == True:
                mina "Why else would I put this on if not for this kind of reactio--?"
            else:
                mina "You had the same look in your eyes as when we first... ah..."

            mina "Mmmhh...♥"
            mina "Shall we pick back up where we left off?"

    scene w3_3127 with dissolve
    mc "I will have to work hard to live up to how you're making me feel..."
    scene w3_3128 with dissolve
    mina "........."
    scene w3_3129 with dissolve
    mina "......"
    scene w3_3130 with dissolve
    mina "..."

    if minaCleanStart == True:
        scene w3_3131 with dissolve
        mina "...you can do anything you want with me, [mcf]."
        scene w3_3132 with dissolve
        mc "Anything?"
        scene w3_3135 with dissolve
        mina "Like I said, I'm putting my trust in you, okay?"
        scene w3_3134 with dissolve
        mc "Mina..."
        scene w3_3135 with dissolve
        mina "Can I ask you something weird? Do you have any {i}fantasies{/i}?"
        scene w3_3134 with dissolve
        mc "Everyone does I would think..."
        scene w3_3135 with dissolve
        mina "A lot of them?"
        scene w3_3138 with dissolve
        mc "I've never counted... and I don't really know what's an abnormal amount..."
        scene w3_3137 with dissolve
        mina "Weeeeell... I've got an abnormal amount of them. {b}Tons{/b}."
        mina "Maybe even a disgusting amount..."
        scene w3_3141 with dissolve
        mc "I don't think fantasies are anything to fret over. What makes them disgusting?"
        scene w3_3142 with dissolve
        mina "Nothing, I guess... except... ah..."
        mina "Would you share one of yours with me?"
        scene w3_3140 with dissolve
        "It's funny. This was an area I've given little thought to, even though, in theory, the club could make any of my imaginations a reality..."
        scene w3_3141 with dissolve
        mc "...huh, are {i}you{/i} gonna make my fantasies come true?"
        scene w3_3142 with dissolve
        mina "Hehe, I don't know... maybe? I {b}cooooould...{/b}"
        scene w3_3136 with dissolve
        "The problem with being truthful was that telling her I'd like to fuck her in the ass while shoving her pretty face in a toilet wasn't keeping with the current mood..."
        "Probably wouldn't ever BE the mood, but I got the impression right now that she thought she was genuinely curious and open to my tastes."
        scene w3_3138 with dissolve
        mc "Why don't we just go with the flow? No need to complicate it."
        scene w3_3139 with dissolve
        mina "True, it's just... I'm curious about what other people like. I don't have many points of comparison, y'know?"
    else:

        scene w3_3132 with dissolve
        mc "Got any requests?"
        scene w3_3131 with dissolve
        mina "{b}Tons{/b}... but today, how about you... {i}just do anything you want?{/i}?"
        scene w3_3134 with dissolve
        mc "Anything? What about your list?"
        scene w3_3135 with dissolve
        mina "This is our first {b}real{/b} time; let's avoid getting bogged down with details..."
        mina "If anything, I want to get a taste of who {b}you{/b} are."
        scene w3_3134 with dissolve
        mc "Who am I?"
        scene w3_3133 with dissolve
        mct "(I'm someone who wants to fuck the shit out of you right now...)"
        scene w3_3135 with dissolve
        mina "You know, what kind of stuff do you like? What would you like to... {i}do{/i}?"
        scene w3_3138 with dissolve
        mc "I don't want for much right now."
        scene w3_3139 with dissolve
        mina "But... you have fantasies like I do, right? Things you might want to try? Helping me with my junk..."
        mina "I was thinking, {i}this{/i} doesn't have to be so one-sided."
        scene w3_3141 with dissolve
        mc "Sure, everyone's got fantasies, but... I try not to dwell on them too much."
        scene w3_3142 with dissolve
        mina "I've told you some of mine..."
        scene w3_3136 with dissolve
        "The problem with being truthful was that telling her I'd like to fuck her in the ass while shoving her pretty face in a toilet wasn't the current mood..."
        "Probably wouldn't ever BE the mood, but I got the impression right now that she might truly meet me halfway if I only asked."
        scene w3_3139 with dissolve
        mina "I'd at least like to hear about some of them... you know how much of a freak I am, and... I don't have many points of comparison, y'know?"

    scene mina_h_stare_a with dissolve
    show mina_h_stare with dissolve
    "Playing out my desires with the club was one thing, but having someone my age... happy and open.... it was a {b}tempting{/b} fantasy that was better saved for future consideration."
    mct "(What is something relatively benign I could share with her that wouldn't make things overly weird...?)"
    "I mean, I could come up with a lie, but the earnest expression on her face MADE me want to be truthful. "
    "......"
    "..."
    mc "Let's put a pin in that thought for now."
    scene w3_3143 with dissolve
    "I HAD what I thought to be an answer to her question, but the explanation was best worked up to."
    mc "Instead..."
    scene w3_3144 with dissolve
    "Plus, eating Mina up {i}too{/i} fast would be a shame. Some meals are best savored."
    mc "Come over here, sweetheart."
    scene w3_3145 with fade
    "I directed Mina to the table and had her sit as if putting her on display."
    scene w3_3146 with dissolve
    "We momentarily shared an exploratory look as I considered what part of her I wanted to taste first."
    scene w3_3147 with dissolve
    mina "[mcf]...? Could you...?"
    "It seemed Mina's mind had gone through a similar process."
    scene w3_3148 with dissolve
    mina "Could you take off your pants... I want to..."

    if minaCleanStart == True:
        mina "I want to see it..."
    else:
        mina "I want to see it again..."

    scene w3_3146 with dissolve
    "Now, it was my time to be put on display and gawked at."
    scene w3_3149 with dissolve
    mc "Should I do it slowly?"
    scene w3_3145 with dissolve
    "No matter... they had to come off at some point."
    scene w3_3147 with dissolve
    mina "J-just... take your {i}dick{/i} out."
    scene w3_3145 with dissolve
    "There was a deliberate emphasis that she knew fully well betrayed her girlishly coy cadence."
    scene w3_3150 with dissolve
    mc "As you wish."
    scene w3_3151 with fade
    "In no time, [mcf] had disappeared from her view. I no longer existed."
    mina "......"
    mina "..."
    "She wasn't looking at me so much as what stood proudly at half-mast."
    scene w3_3152 with dissolve

    if minaCleanStart == True:
        mina "It can get bigger, right? Could you... I mean, I want to see..."
    else:
        mina "I know it's bigger than that... Could you... I mean, I want to see..."

    scene w3_3153 with dissolve
    mina "{b}Stroke it for me.{/b}"
    scene w3_3151 with dissolve
    "Again, she oscillated between shyly choosing her words and a more forceful command. I didn't know if she intended for the contrast to turn me on or if she was simply feeling out her own feelings, but the former was the end result."
    scene mina_h_jerk_a with dissolve
    show mina_h_jerk with dissolve
    mc "What? You like watching men jerk off?"
    mina "Y-yeah, it's... {b}hot{/b}."

    if minaCleanStart == True:
        mc "Is this one of those fantasies you mentioned?"
    else:
        mc "Is this one of your things?"

    "She just nodded, too transfixed on my cock to say more than she had to."
    mina "Mmmhh... actually, more fetish than fantasy?"
    mc "What do you like about it?"
    mina "*Gulp* It's just so... {i}animalistic?{/i}"
    mina "You're going to be a doctor one day, [mcf]. You'll help people, but right now, you have a look in your eye that's so far removed from decent. I {b}love{/b} it..."
    mc "Mina, like... {b}damn{/b}."
    mina "Ahhhh, I'm w-weird, aren't I?"
    mc "You're not weird; all sex is weird... you just know what you like."
    "How she could articulate the underpinning of her desires surprised and impressed me."
    mc "The world would be better if everyone could be honest with themselves and find a healthy outlet."
    mina "Uyyhh... mmmhuh...♥"
    "It seems I had lost her to whatever deliberations were happening inside her head."
    scene black with fade
    mina "When did you-"
    scene w3_3154 with dissolve
    "Poor Mina was so caught up on me jacking off that she didn't even register me inching closer. The spell was only broken when my hand left my cock."
    scene w3_3155 with dissolve
    mc "You were REALLY into that..."
    scene w3_3156 with dissolve
    mina "Hnnngg... don't-"
    scene w3_3155 with dissolve
    mc "And why not? From where I stood, the look in your eyes was equally as fuck hungry as the one you saw in mine."
    mc "Don't be embarrassed about what you like."
    scene w3_3156 with dissolve
    mina "Share with me one of your fantasies and maybe I won't be..."
    scene w3_3157 with dissolve
    mc "It's that important to you, huh?"
    mina "Absolutely! What's more intimate than knowing what the other person gets off to?"
    scene w3_3158 with dissolve
    mc "Don't worry. I'm not avoiding your question."
    mina "O-ohh..."
    mc "I have a {b}show and tell{/b} in mind. But first..."
    scene mina_h_brub_a with dissolve
    show mina_h_brub with dissolve
    mina "{b}O-ooooooh!{/b}"
    "I mean, {i}how could I {b}fucking{/b} not?{/i} The pull of the fabric made Mina's already beautiful chest even more delectable. "

    if minaCleanStart == True:
        mc "Let's discover just how sensitive you are here."
    else:
        mc "Let's make you sing."

    "My hands possessed a will of their own, gripping the underside of the blonde's bust, teasing and massaging the mounds to create an eye-pleasing feast."
    mina "Hnn- ahh... aren't we past this?"
    mc "What do you mean?"
    mina "You c-can just put it in if you want... y-you're so hard, it's painful for a guy to hold back, right?"
    "I stopped myself short of asking who told her that. Maybe that was something invented in her own head, but more realistically, I could see that being a line Ian fed her."
    mc "Painful, no. This is one of my {b}favorite{/b} parts."
    scene w3_3159 with dissolve
    mct "(God, the sight of these things!)"
    mc "It's like when you slowly crawl to the top of a roller coaster, and you get that funny feeling in the pit of your stomach."
    scene w3_3160 with dissolve
    mina "Hhh- i-is it?"
    scene w3_3161 with dissolve
    mc "It is. The climb, the anticipation, is just as important as the fall."
    scene w3_3162 with dissolve
    mina "Roller coasters are scary..."
    scene w3_3161 with dissolve
    mc "Maybe, but... the ride to the top gives you time to think. Lets you come to terms with the inevitable."
    mc "In this case, that being... you're gonna get {b}fucked{/b}, Mina. So, go ahead and think about that for a bit."
    scene mina_h_tsuck_a with dissolve
    show mina_h_tsuck with dissolve
    mct "(Aha!)"
    mina "Eeeh, eeh?"
    "That taste I was looking for before I got sidetracked."
    "Mina's nipples struck a wonderful balance between puffy and hard, the perfect morsel to latch onto and gratify my own personal fixation."
    mina "Ah, wwhh--"

    if minaCleanStart == True:
        "Something in me compelled me to {i}devour{/i} these things."
    else:
        "I felt just as compelled to devour these things as if it was my first time sucking on these beauties."

    mina "S-sooo... ahhh..."
    "On the ride to the top, a thought occurred to me."
    mina "Alright... ha... t-thinking about it..."
    "Mina was like a canvas, and I felt the tremendous weight of knowing I would add my own touch to this painting."
    mina "Hnng- wwhhha, do whatever you want..."
    "Would I paint over some of what Ian added? Who knew, but it might be fun to try."
    mina "I-if you like my breasts that much, h-have your f-fill..."
    "Would the things I add be for better or worse? Beats the fuck out of me."
    mina "I'll learn all about y-you while you d-do-"
    "Would a little of her rub off onto me?"
    scene w3_3163 with dissolve
    mina "E-eehh?"
    "I hoped so."
    scene w3_3164 with dissolve
    mina "Oh, hhhnn-"
    "My exploratory taste confirmed what I already suspected to be the case: Mina was sufficiently tuned up and waiting for a cock."
    mina "Hyyeee-♥ [mcf]!"
    scene w3_3165 with dissolve

    if minaCleanStart == True:
        "I pried Mina apart with my tongue and explored her insides. This would serve as a nice appetizer."
    else:
        "I didn't plan on a repeat of the other day. This was just an appetizer."

    mina "G-give me a warning before you, o-ohhh-"
    scene w3_3166 with dissolve
    "As I shot up and angled my penis toward her opening..."
    mina "Oohwwooh- ahh.. hweh..."
    "...Mina's words stuck in her throat, waiting for the shoe to drop."
    scene w3_3167 with dissolve
    mina "......."
    mina "..."
    scene w3_3168 with dissolve
    mina "*Gulp* W-what are you doing?"
    scene w3_3169 with dissolve
    "Hovering this close, there was a very tempting prospect to simply put it in, but I couldn't fight my sadistic streak."
    "Let's hold out, just a little while longer..."

    menu:
        "Tease her silently(Dialouge/render changes only).":
            "Why use words when you can say a lot more with action?"
            scene mina_h_pussyr_a with dissolve
            show mina_h_pussyr with dissolve
            mina "Euug-!"
            "As the bottom of my shaft came in contact with her sweet parts, the breath Mina held in abruptly escaped her throat."
            mina "Hnngg... ehhh... "
            "The tip of my cock agonizingly poked through the cleft of her sex, prying apart and teasing Mina's sex."
            mina "You're still on this t-teasing thing, huh?"
            "{i}This{/i} approach was a double-edged sword."
            "Every time the underside of my shaft would meander over her precipice, a warmness spread down my length and all the way to my nuts."
            "Every time my head bumbled into her ridges, a violent, tingling feeling shot up my body."
            "Still, standing over her like this, I could drink in every bit of her frustrated expression. I could bask in the foreknowledge of how tight she would be once we finally joined."
            mina "Or... eheh... d-do you not know how to do it?"
            "I wondered... what would her face look like when I entered her for the first time?"
            "Would it be on me? Would she carefully observe where we were connected?"
            mina "Hnnngg... ggahh... c'mon [mcf]..."
            "What would her expression be like? How much of me would she take before that pretty face of hers went askew?"
            "How deep would my cock need to reach for me to rend all thoughts from her head? How fast would I need to go before her eyes rolled back in her head?"
            scene w3_3170 with dissolve
            mina "Stop being meeeeean... ah, pleeeease?"
            scene w3_3171 with dissolve
            "The future was full of lewd possibilities."
            scene w3_3172 with dissolve
            "I nodded, signaling to her what was to come."
            scene w3_3173 with dissolve
            "Mina smiled back, signaling to me that she was ready."
        "Get vulgar with it.":

            mc "You want it?"
            scene mina_h_pussyr_a with dissolve
            show mina_h_pussyr with dissolve
            mina "Euug-!"
            "As the bottom of my shaft came in contact with her sweet parts, the breath Mina held in abruptly escaped her throat."
            mina "Hnngg... ehhh... I'm r-ready... ah..."
            "The tip of my cock agonizingly poked through the cleft of her sex."
            mc "Your little pussy is going to be a tight fit for my cock."
            mina "A-ahh...♥"
            mc "You think you can handle it?"
            mina "I m-mean, ha..."
            scene w3_3175 with dissolve
            play sound "sound effects/slap1.wav"
            scene w3_3176 with vpunch
            "*Fwap!*"
            mina "O-ohh-!"
            scene mina_h_pussyr_a with dissolve
            show mina_h_pussyr with dissolve
            mina "Hnnng... that's what it does... it's made to take.. a-ah~"
            mc "{b}What{/b} is it made to take?"
            mina "C-c'mon, [mcf]..."
            mc "What is your pussy made for, Mina?"
            mina "Ah... euuug..."
            "She looked at me with a complete understanding of what I was getting at."
            mina "It's made to take {i}cock{/i}."
            "Mina didn't dance around it quite as much as I had hoped."
            mc "I'm going to put it in now."
            scene w3_3170 with dissolve
            mina "Alright, but... b-be gentle, okay?"
            scene w3_3171 with dissolve
            "She asked with such a cute look..."
            scene w3_3170 with dissolve
            mina "Your thing is {i}huuuuuuuuge{/i}. Do it slowly, at least at first..."
            scene w3_3171 with dissolve
            "She said, perhaps purposefully inflating my ego for her cause."
            scene w3_3172 with dissolve
            mc "Ready?"
            scene w3_3174 with dissolve
            mina "R-ready..."

    scene w3_3177 with dissolve
    "......."
    "..."
    scene w3_3178 with dissolve
    mina "Hh-"
    scene w3_3179 with dissolve
    "Slowly, I slid the head of my penis into Mina's welcoming embrace."
    scene w3_3178 with dissolve
    mina "Hh-hat...!"
    scene w3_3179 with dissolve
    "I held myself in place, my eyes never leaving hers, letting her know I was intently aware of what she was feeling."
    scene w3_3178 with dissolve
    mina "Deeper..."
    scene w3_3180 with dissolve
    "Deeper I went, one-third of the way down my shaft."
    scene w3_3181 with dissolve
    mina "It's t-thick...♥"
    scene w3_3182 with dissolve
    "I stopped once more, holding for a second, enjoying the warmness of Mina's insides clinging sweetly to my shaft."
    scene w3_3181 with dissolve
    mina "You're pulling me apart, [mcf]..."
    scene w3_3183 with dissolve
    mina "Achk, h-hard...♥ You're so...!"
    scene w3_3184 with dissolve
    "Halfway."
    mina "..."
    "Mina kept her eyes glued to me, the longing expression on her face never wavering. A look that she was very intentionally making known."
    "{i}She was reassuring me that she wanted me.{/i}"
    scene w3_3183 with dissolve
    mina "{b}Deeper{/b}."
    play music "music/crazy.ogg"
    scene w3_3185 with vpunch
    mc "--!"
    "One final push, with more strength than I intended, emboldened by Mina's impassioned demand."
    mina "Mmhh, aaaaaaahh-♥♥♥♥♥"
    scene w3_3186 with dissolve
    mina "Y-you're in! F-finally...! Aaaah- {i}FUCK!{/i} Ha...!"
    "Instead of reeling back, Mina clung to me, keeping me buried at the base."
    scene w3_3187 with dissolve
    "An intense wave of pleasure washed over me and things quickly became hazy."
    scene w3_3188 with dissolve
    mina "You're in... all of you... ha... s-so much of you... ah...♥"
    scene w3_3187 with dissolve
    "Mina felt so good, her body was so soft, she smiled so lovelily..."
    scene w3_3188 with dissolve
    mina "D-don't move yet, okay...?"
    scene w3_3187 with dissolve
    "With the way she held me, I could feel her heartbeat."
    scene w3_3188 with dissolve
    mina "Haa..."
    scene w3_3187 with dissolve
    "I wanted to move, but at the same time, being joined like this... chest-to-chest... {b}felt so secure.{/b}"
    "Even in a situation like this, she had an uncanny knack for putting others at ease."
    scene w3_3189 with dissolve
    "Gently I laid her down on the table's surface, withdrawing a little and giving her a moment to adjust to my size."
    scene mina_h_tm1_a with dissolve
    "......"
    "..."
    "After a moment, she gave me a nod and..."
    scene mina_h_tm1_a with dissolve
    show mina_h_tm1 with dissolve
    "So it began, with me gently pushing into Mina's constraining depths."
    mina "Haa...♥"
    "Mina was no virgin, but there was a tempo to these things."
    mc "You alright?"
    mina "Y-yeeahh... you're... {b}heh...♥{/b}"
    "Pulling out from her grip took effort."
    mina "My heart jumped into my throat when you went all the way in..."
    "Pushing back into her hold took strength."
    mina "You're so big, hard, and thick...! God...!"
    "The table-fucked blonde's hold on me was incredible."
    mina "Y-yeah, I'm alright..."
    scene mina_h_tm2_a with dissolve
    show mina_h_tm2 with dissolve
    "Thankfully, Mina had a good sense of rhythm. She matched my pace and timing, joining with me at the height of every thrust."
    mina "I'm glad I'm doing this with {i}you{/i}, [mcf]."
    mina "Even now, you're being patient... ahh...♥"
    "Mina's usual exuberance carried on even here, with a tremendously playful smile plastered on her face."
    mc "It's just... you're so damn tight... ha, if I moved any faster than this, I would explode."
    mina "Ehh... ha...♥ Hehe... why do people ever do anything but {b}fuck{/b}?"
    scene mina_h_tm3_a with dissolve
    show mina_h_tm3 with dissolve
    "Her smile gave me a sense of overwhelming {i}togetherness{/i}, but it was also something I'd like to see messed up."
    mc "You're something else, you know that?"
    "It would be lovely to see that smile unfurl in pleasure."
    mct "(But, I guess you could say the same about me.)"
    mina "Hehe~"
    "....."
    "..."
    "Our chatter abated, and the conversation continued with our eyes."
    "She gifted me her rapt attention, expression brimming with eagerness and hunger."
    "Through a hazy stare, she told me she wanted more."
    "Her lips parted but carried no words - only breathy affirmations that conveyed to me {i}don't stop{/i}."
    scene mina_h_tm1_a with dissolve
    show mina_h_tm1 with dissolve
    "Every time I pushed {i}deep{/i} into her, there was a flicker of satisfaction that would fast die on the way back out."
    "It was a small drama, one that played out over and over in time with our rhythm, but each performance was as fresh as the last."
    "Each rendition of Mina's sultry expression aggravated my desire."
    "Each dive into Mina's lust-filled eyes propelled my hips forward with growing emotion. "
    "Every apsect of Mina's visage carried a mandate to leave her well and truly fucked."
    scene mina_h_tm3_a with dissolve
    show mina_h_tm3 with dissolve
    mc "Hnn, M-mina...! So, you wanted to hear a fantasy of mine?"
    mina "Of c-course! Tell me! Let's do it!"
    mc "You haven't heard it yet!"
    mina "I don't care! Let's do whatever it is!"
    mc "You're out of your mind!"
    mina "M-maybe...♥ I want to make this special for you, [mcf]!"
    "......"
    "..."
    "Mina, with the city as her backdrop, was like a dream."
    mc "The window!"
    scene mina_h_tm2_a with dissolve
    show mina_h_tm2 with dissolve
    mina "The window...? What about it?"
    mc "Doesn't it appeal to you?"
    mina "......"
    mina "..."
    mina "We have a good view of the city from here, don't we?"
    mc "Thirty-four floors, to be precise. I see you're thinking what I'm thinking."
    scene black with fade
    mina "Kiiiiinda?"

    if minaCleanStart == True:
        "It was a simple and innocuous choice, one fitting for the moment."
    else:
        "If she was honest about wanting to explore our fantasies together, I wanted to start with a simple and safe one."

    scene w3_3190 with fade
    mina "A-aahh...! C-cold~!"
    "I pressed Mina hard against the window pane to make my point."
    scene w3_3191 with dissolve
    mc "You know, I've lived my whole life and never really been that far from another person. I've never had a mile between me and any other human before."
    mc "Kinda fucking crazy when you really think about it..."
    scene w3_3190 with dissolve
    "Mina's response to that was to wiggle her ass. A {i}polite{/i} way of telling someone to get back to work if I've ever experienced one."
    scene mina_h_win1_a with dissolve
    show mina_h_win1 with dissolve
    mina "Hhha-♥"
    mc "You ever look up and imagine all the little dramas playing out in the buildings around you?"
    "Slowly, I picked up back where we left off, looking to set the scene."
    mc "Joyous celebrations, babies being born, dreams being fulfilled..."
    mina "Hnnng...♥ Ah, the angle you're pushh- w-woah...♥"
    mc "Spouses fighting, lovers quarreling, people having the worst days of their lives..."
    mina "Ha-♥ You c-can go faster if you want!"
    "I ignored her request."
    mc "You ever look up and imagine all that?"
    scene mina_h_win3_a with dissolve
    show mina_h_win3 with dissolve
    mina "H-haaat-♥ Hnng, mmmh-♥ F-faster!"
    mc "I do. There's so much happening all around us that it can be suffocating to think about."
    "I ignored her request a second time."
    mc "The city's teeming with life, but you tend to forget that once you're locked away behind some walls with some soundproofing."
    mina "Fhh, [mcf] faster!"
    mc "Isn't it hot sitting up high, peering down on all those meaningful moments?"
    mina "Hha, hhhaa I g-guess? The city looks nice from up here..."
    scene mina_h_win2_a with dissolve
    show mina_h_win2 with dissolve
    mc "Doesn't it turn you on to think about the people going about their daily lives as you tower above them, a dick buried in your twat?"
    mina "Mmmh, when you put it t-that way..."
    mc "None of that matters. None of {i}them{/o} matter."
    mina "Ha, hhh-♥"
    mc "There's just the sensation of being {b}above{/b} it all, getting fucked. Isn't it kind of a thrill?"
    mina "Y-yeeah! It feels gooood!"
    mc "It does for me too. It turns me on to imagine I'm lording above all that shit, balls deep in a woman of their fantasies."
    mina "Huuah, hhaaa...! W-w-heh?"

    menu:
        "Pick up the speed.(Dialouge/render changes only)":
            scene mina_h_win4_a with dissolve
            show mina_h_win4 with dissolve
            mc "God, I'm the luckiest man alive right now!"
            "To signify my feelings, I rolled my hips forward, driving my cock harder and faster into Mina's cunt."
            mina "Hwwwahh-♥"
            "The harder I pounded, the more she was fucked complacently into the window."
            mina "Gyyah... euhhh--♥ You're going so-"
            "Fast."
            mina "Yhhwe-♥ Hwwwuu-♥"
            "Fast and deep."
            mc "This good?"
            scene mina_h_win5_a with dissolve
            show mina_h_win5 with dissolve
            mina "Shh, y-yeah...♥ It f-feels g-good! Like r-really, {b}really{/b} g-good!"
            "Mina used her upper body to push back, but I had almost all the leverage from this position."
            mc "Take a look at the city, take a look at the streets... take a look at all the people...!"
            "I could lay into her pussy to my heart's content, taking in the lovely curve of Mina's back while basking in the view of the city."
            mc "They got no fucking idea we're screwing right above their heads."
            mina "Uunnggh- haa-!"
            mc "They got no idea I'm screwing the most beautiful woman they've never seen!"
            scene w3_3192 with dissolve
            mina "Ahh, haa..? Ehehe...♥ You weirdo!"
            scene w3_3193 with dissolve
            "Mina laughed, taking this relatively innocent fantasy in good stride."
        "\"Say my name, bitch.\"(w3MinaSayMyName = True)":

            $ w3MinaSayMyName = True
            scene mina_h_slap_a with dissolve
            show mina_h_slap with dissolve
            mc "It turns me on to imagine my name literally screamed into the high heavens!"
            mina "Yeeuuuah...?!"
            mc "Say my name!"
            "To further make my point, I slammed my cock harder and faster into Mina's cunt."
            mina "Hnnn, yyeee-♥ [mcf]!"
            "Each smack of her ass was well-received, Mina's bubble butt providing the perfect target."
            mc "Say my name, {b}bitch!{/b}"
            mina "Gyehh, [mcf]!"
            "Each smack yielded an eye-pleasurable jiggle that caused Mina's pussy to strangle my dick even harder."
            mc "Good girl!"
            mina "Eh, yyeeah, aaah...♥ [mcf]."
            mc "Good Mina!"
            scene w3_3192 with dissolve
            mina "Ehehe~♥"
            scene w3_3193 with dissolve
            "She giggled, none too disturbed by my sudden shift in attitude."
            scene w3_3192 with dissolve
            mina "Ah, heee-♥ [mcf]!"
            scene w3_3193 with dissolve
            "In fact, she sounded like she found this direction to be genuinely endearing."

    scene mina_h_win3_a with dissolve
    show mina_h_win3 with dissolve
    mina "Ah, hhaa... maybe we should try this on a rooftop sometime?! Wouldn't that be wild?"

    if minaCheat == True:
        mc "Is that on your list?"
        mina "N-nope! C-could be on {i}yours{/i} though!"
        mc "Hnngg, hauuch... no thanks! I'm afraid of heights!"
    else:
        mc "N-no thanks... I'm afraid of heights!"

    mina "Pffh, w-what? Hah-"
    scene mina_h_win5_a with dissolve
    show mina_h_win5 with dissolve
    mina "Yeeaahhuuuhh-♥ Ah, c-craaap-♥"
    "Mina's joy was so pervasive that I found myself smiling too."
    mina "Ah, you're hitting me in {i}all{/i} the r-right spots!"
    "Fucking her was unlike any other experience. It felt edifying and {i}wholesome{/i} of all things."

    if w3MinaSayMyName == True:
        mina "[mcf], [mcf], [mcf], [mcf], [mcf]!"
        "Even being pounded into the glass, she shined brilliantly..."
        mc "You slut!"
    else:
        mina "Hehe, you really think you're l-lucky?"
        "Even being pounded into the glass, she shined brilliantly..."
        mc "Let me prove it to you!"

    "I poured my focus into giving Mina my {b}all{/b}."
    mina "Fuh, hhaa-♥ [mcf]!"
    "By now, I had a pretty good idea of what angle of attack she found most gratifying."
    mina "Yyeh, haa... r-right there! Right there, you fhhweeuh-♥"
    "My cockhead dug into the outer wall of her vagina, following the bend of her pelvis, scrapping and gouging all the way."
    scene mina_h_win4_a with dissolve
    show mina_h_win4 with dissolve
    mc "Take it!"
    "I felt confident I could make her cum first."

    if w3MinaSayMyName == True:
        mc "Take it all, you bitch!"
    else:
        mc "Take it all!"

    "I wasn't anywhere near my limit and my recent experiences had given me plenty confidence in my stamina."
    mina "Y-yeahh, eeugh... g-give it to me-♥"
    "Sensing the change in focus, Mina did her best with what little leverage she could muster to pleasure me back."
    mina "Gnngh, hnnng-! G-give it all to me!"
    "That window of good humor had closed in favor of a concentrated feeling of lust."
    "Her giggles and sweet-natured cooing were now loud, vulgar grunts."
    mina "Guah, hhuugnhh, hnnn-! Give it to me, Daddy!"
    mct "(...ha, Daddy?)"
    scene mina_h_win5_a with dissolve
    show mina_h_win5 with dissolve

    if minaCheat == True:
        mct "(There it was again. Just like the first time we fooled around.)"
    else:
        mct "(...did Ian teach her that or is that all her, I wonder?)"

    mina "Ye, hha, fwhh- hehe~ fwuhh-♥"
    "I could tell from her body language she was getting close."
    mina "Gyhh, y-ye- ah, eeh?"
    "The way she babbled, the way her legs buckled, the way her hands fruitlessly tried to find a more secure hold on the glass."
    mina "Gyee, aaahhh.. eeeuugghh-"
    "Yeah, she was getting {i}damn{/i} close. Very--"
    scene w3_3194 with vpunch
    mina "Sh, wwwyyyaaaeehhhhhhh-♥♥♥♥"
    "Suddenly, her body went taut. Every muscle, including the one wrapped around my dick, froze up."
    mina "Ueehhhh, aaahh- hhhnnn-♥♥♥♥"
    "She cried... {i}howled{/i} in a beautifully filthy way as my momentum ground to a stop in opposition to Mina's unwavering tightness."
    scene mina_h_post1_a with dissolve
    show mina_h_post1 with dissolve
    mc "Gah, hhnn-!"
    mina "Ah, wwooahh.. s-shit.. d-dang... ahahaha... oh, w-wow... heh.."
    "Mina was ego-inducingly scatterbrained. Moments passed before... "
    mina "Haa... mmmh... why have you stopped? You still haven't cummed... hehh..."
    scene w3_3195 with dissolve

    if minaCleanStart == True:
        mc "Slow and steady..."
        scene w3_3196 with dissolve
        mina "Mmmhhh....?"
        scene w3_3197 with dissolve
        stop music fadeout 3.0
        mc "I paid a lot of money for this room. We're going to use it."
    else:
        mc "My goal isn't cumming, remember?"
        scene w3_3196 with dissolve
        mina "Mmmhhh....?"
        scene w3_3197 with dissolve
        stop music fadeout 3.0
        mc "You asked me to mess you up and there's still a lot to go."

    scene w3_3198 with dissolve
    mina "O-oh..."
    scene w3_3197 with dissolve
    mc "C'mon, let's try out the bed."
    scene black with fade
    "I still had a lot of gas in the tank, but even if I didn't..."
    play music "music/rockville.ogg"
    scene w3_3199 with sunshine
    "The way Mina's doe-like eyes teemed with desire was reason enough for me not to speed toward an orgasm."
    scene w3_3200 with dissolve
    mc "Mina..."
    scene w3_3201 with dissolve
    mina "Hehehe~"
    "In anticipation, she purred like a kitten."
    scene w3_3202 with dissolve
    mina "Mmmmm~"
    "Adding a touch of sensuality to the moment, Mina's tiny mouth ensnared my thumb, sucking on it desirously."
    scene w3_3203 with dissolve
    mc "Mina, Mina, Mina..."
    "I briefly considered giving her something {b}else{/b} to suck on, but my taste of Mina's lower mouth had been all too brief."

    menu:
        "Wordlessly take her.(Dialouge/render changes only)":
            "She watched me so attentively, so intently, that there was no need to explain what I wanted."
            scene w3_3204 with dissolve
            mina "........."
            scene w3_3205 with dissolve
            mina "......"
            scene w3_3206 with dissolve
            scene w3_3205 with dissolve
            mina "..."
            scene w3_3207 with dissolve
            scene w3_3205 with dissolve
            "She understood that I wanted to see her this time."
            scene w3_3208 with dissolve
            "To be face-to-face."
            scene w3_3209 with dissolve
            "She smiled and began to spread her legs. Inching them apart until..."
            scene w3_3210 with dissolve
            mina "Come on, [mcf]..."
            scene w3_3211 with dissolve
            "I didn't need a better invitation."
            scene black with fade
            mina "Gyeh- ahh.. just right into-"
            "--!"
            mina "Ww-wahha-♥"
        "You're her daddy.(w3MinaDaddy = True)":

            $ w3MinaDaddy = True
            scene w3_3212 with dissolve
            play sound "sound effects/slap1.wav"
            scene w3_3213 with hpunch
            "--!"
            mc "{b}Mina{/b}."
            scene w3_3214 with dissolve
            mina "Ah- ah... [mcf]..."
            scene w3_3215 with dissolve
            mc "Are you gonna be a slut for Daddy?"
            mina "A-ah! Whaaa-"
            scene w3_3216 with dissolve
            "If she had a predilection for this kind of play, might as well lean into it. Not like I wasn't into this shit, either."
            scene w3_3217 with dissolve
            scene w3_3216 with dissolve
            "In a deliberate effort, she kept eye contact with me, simply nodding and giving me approval at this direction."
            scene w3_3218 with dissolve
            mc "That's my baby girl."
            "I guess this really was a kink of hers."
            scene black with fade
            mina "Gyeh- ahh.. just right into-"
            "--!"
            mina "Ww-wahha-♥"
            mc "We're past warming up!"

    scene mina_h_mis2_a with cmet
    show mina_h_mis2 with dissolve
    "For the next leg of the evening, there was no need to build to tempo."
    mina "Ah, hhhnn-♥"
    "Mina's sex, while still nut-wrenchingly tight, had grown used to my size and shape."
    mc "Goddamn it, you feel amazing!"
    "Using her arms for leverage, I had no trouble slipping in and out of her at speed, carving out a long and deep path."
    mina "Euughh, hhhaak- {b}y-you t-toooo!{/b}"
    "Mina admirably did what she could to take an active part in our shared pleasure, using her legs to steady and guide my hips home, but I had the dominant position."
    "She could grind and writhe, but she had little recourse but to lie there, look up at me, and watch herself get fucked - all with an enamoring look on her face."
    mina "Whh, hhnn-♥ Sex with y-you was such a GOOD idea! Hehehe, ha-♥"
    "--but it wasn't like I had much choice either. I may have had a physical hold on her, but my head was preoccupied with Mina."
    scene mina_h_mis1_a with dissolve
    show mina_h_mis1 with dissolve

    if w3MinaDaddy == True:
        mc "You were BUILT for this, Mina."
        "What else could I do but spear her over and over and over again on my cock?"
        mc "Daddy's good little whore!"
        "What else could I do but marvel at Mina's perfect bust and its appetizingly engorged pink peaks?"
        mc "Daddy's perfect slut!"
        "No... I had little recourse of my own."
        mina "Whh, hhaa-♥ D-daddy! Ahhh...♥♥♥"
    else:
        mc "Ha! You took the -hnn- words RIGHT out of my mouth."
        mc "We should make this a regular thing, y-you know?"
        "What else would I do but spear her over and over and over again on my cock?"
        mina "Hnnhh- w-whenyouever you want, [mcf]."
        "What else could I do but marvel at Mina's perfect bust and its appetizingly engorged pink peaks?"
        mina "I'm yours... Ahh...♥"
        "No... I had little recourse of my own."
        mina "...you o-only have to ask~♥ Haaht, crapeeeuuguhh-♥"

    "Fuck and be fucked."
    "We had carved out, for only a painfully fleeting moment, a slice of meaning in this world."
    mina "Gehhuu, aahh-♥"
    "Meaning uncomplicated and lacking in nuance."
    "Meaning found in the most straightforward and essential human act."
    "Meaning at its most hedonistic and pure."

    if w3MinaDaddy == True:
        mina "Ghhu, hffhhuh- fuck me, Daddy!"
    else:
        mina "Ghhu, hffhhuh- fuck me, [mcf]!!"

    scene mina_h_mis2_a with dissolve
    show mina_h_mis2 with dissolve
    "In this brief moment, sex with Mina was the most obvious thing in the world. A cure-all for the soul."
    mc "Don't worry! I'm -hnnn- giving it my b-best!"
    "Oh, how easy it was to forget the messy events that led to this."
    "Oh, how quickly this charade would be over."
    mina "Gyahh, hhaa, wwh♥"
    "No... I had to make this last, as long as I could."
    "I would carve this experience into Mina's body to leave her no doubt about coming back for me."
    mina "Hnn, hwwwah, hhaaa♥♥"
    "There it was! That familiar feeling."
    mina "Ghh, hhnn, wwah, ewwuuuuhh♥♥♥"
    scene w3_3219 with dissolve
    "The tension..."
    scene w3_3220 with vpunch
    mina "Wwoohhh, ghh, www-hhhhnnnnn♥♥♥♥♥♥♥♥♥♥♥♥♥!"
    "The tension {b}broke.{/b}"
    scene w3_3221 with dissolve
    mina "Ehhhuuuhhh-♥"
    "Mina found herself descending the peak for the second time this evening."
    scene black with dissolve
    "I wasn't nearly finished."

    if w3MinaDaddy == True:
        mc "No time to rest, Babygirl."
    else:
        mc "No time to rest, beautiful."

    mina "Wha..? Whhhh-?!"
    scene mina_h_cow1_a with fade
    show mina_h_cow1 with dissolve
    mina "Gyy, hhhn- hhaaa-♥"
    "This time a well-fucked Mina was on top, but in her half-insensate state, she could only concede me the initiative."
    mina "Hnhh... n-no time out, aah-ah?"
    mc "Nope!"
    mina "Ehh.. ohh, h a- ohkkay-!"
    "She instinctually bucked and bounced, but it was up to me to do the lifting."
    mc "Haahh, thanks for being so understanding!"
    "Fortunately, Mina, contrary to all her bluster and immense personality, was a very light young lady."
    "Even in my fuck-focused state, prying Mina off my cock and dropping her back down was a trivial task."
    mina "Hheeh, hheeh-♥ You're very persuasive! Ahh-♥"
    "An immensely FUN and trivial task."
    mina "Ahh, vvheeeery-♥♥"
    "One with an immensely gratifying angle... {i}not that she had any bad ones.{/i}"
    mina "Persuusshhive-♥"
    "I could just dumbly watch her go up and down, up and down to my utmost satisfaction."

    if w3MinaDaddy == True:
        mc "If you say so, slut!"
    else:
        mc "Heh, if you say so!"

    "Up and down, sinking my fingertips into the pale flesh of her hefty mammaries."
    mina "Gyy, hhhn- hhhhn-♥ Hwwwhh-♥!"
    "Up and down, focusing on {i}the sensations{/i} as her lower body tried to milk me for all my pleasurable worth."
    mct "(Ahh... ha... Christ-!)"
    "{b}Riiiight{/b}, I've been so preoccupied with Mina's reactions that I forgot I was getting it as good as I was giving."
    mc "Ah, hhhhaa-"
    "My own moans unconsciously escaped my lips as my mind shifted awareness to the tingly feeling traveling up my spine."
    mina "Hehe- ah, hh--- y-you're feeling-? H-ha, {b}I'm--{/b}!"
    "{i}How could I not{/i}, I thought to myself, but it was a thought better served through action rather than voice."
    scene mina_h_cow2_a with dissolve
    show mina_h_cow2 with dissolve
    mina "Eehhh, hhhnn-♥"

    if w3MinaDaddy == True:
        mc "C'mon, shake it harder!"
        mina "Eeueuhhh- aaahh...! I a.. aaa--hhh-♥♥"
        mc "You can do it better than that!"
        mina "Waah, hhhnaa-♥♥♥ I'm c-close-!"
        "Once she starts, she just can't stop, huh?"
        mc "Shake it for Daddy, you bitch!"
        mina "I --aa, eeheeem- aahh..."
        mc "Come for me, Babygirl!"
    else:

        mc "C'mon... b-bounce! A-ah!"
        mina "Eeueuhhh- aaahh...! I a.. aaa--hhh-♥♥"
        mc "C-come on... you're aaahh... you- you feel amazing!!"
        mina "Waah, hhhnaa-♥♥♥ Hnggg, I-I'm close!"
        "Once she starts, she just can't stop, huh?"
        mc "Come on, do it, then!"
        mina "Wwwh, hhngg, wwaa--♥♥♥"
        mc "Come on... {i}come{/i} for me again-"

    scene w3_3222 with dissolve
    mina "I'm..."
    mina "I'm, I'm..."
    mina "I'm, I'm, I'm-!"
    $ renpy.music.set_volume(.2, 3, channel = "music")
    scene w3_3223 with vpunch
    mina "Euuugaaaaaaaaaaaaaaaaaaaghhhhhhhh-♥♥♥♥♥♥♥♥♥♥♥♥"
    "A warmness spread across my stomach..."
    mina "Wh, haa, hhnn-"
    scene w3_3224 with dissolve
    mina "Heeh, hhoo... oh... waahhh..."
    mina "Gaah, hehe, like... {b}fuck!{/b}"
    scene w3_3225 with dissolve
    mina "H-hey, uhh... waah..."
    mina "{b}Finish... go ahead... ahh... I want you to finish while fucking me... c-cum insiiide mee....♥♥♥♥♥ Pleeeeeease♥♥♥♥♥"
    scene w3_3226 with dissolve
    mina "I w-want to f-feel like I... ahhh...♥"
    mina "Make me feel-- aa-hhh...♥ Just... {b}ruin me{/b}, [mcf]."
    scene w3_3227 with dissolve
    mc "W-what...? Ahh... haa..."
    scene w3_3229 with dissolve
    mina "Make me forget I'm even a person, o-okay? It's..."

    if minaCleanStart == True:
        mina "...it's a fantasy of mine. {b}Destroy me.{/b}"
    else:
        mina "...c-consider it part of my list. {b}Destroy me.{/b}"
    scene w3_3228 with dissolve
    mc "......"
    scene w3_3227 with dissolve
    mc "...aaaaaah, shit. {b}You fucking got it!{/b}"
    scene black with fade
    mina "W-wahh, aaahhh...♥♥♥"
    mct "(How the fuck did I end up with the tame fantasy here?)"

    if w3MinaDaddy == True:
        mc "Get the fucking ass up!"
        play sound "sound effects/slap3.wav"
        "*Slap!*"
        mina "W-wwah, hhhngngggg..."
    else:
        mc "Point it this way!"
        mina "W-wah, ehh...?"
        mc "Face down, ass up!"

    play ambient "sound effects/fap.wav"
    "........."
    "......"
    "..."
    $ renpy.music.set_volume(1, 0, channel = "music")
    scene mina_h_pbone1_a with fade
    show mina_h_pbone1 with dissolve
    mc "F-fuuuuck!"
    "I lost it."
    mina "Guhh, hhhu, hee, hhhu-!"
    "I fucking lost it."
    mc "D-damn it, Mina... uggh... s-saying something like that♥"
    "It would be unfair to Mina's heartfelt and earnest request {i}not{/i} to fuck her like her only purpose was to wrench the semen from my fat and heavy balls."
    mc "In a voice like that, from a girl like you...?"
    "Did she have any idea what sort of power she wielded?"
    mina "Wwhh- hhhnn- wwwhhh-♥"
    "Did she know what sort of effect those words would have on a man?"

    if w3MinaDaddy == True:
        mc "Hnng, y-you filthy, beautiful bitch!"
    else:
        mc "Hnng, goddamn it!"

    mc "Of course, I'll ruin you!"
    "My instincts had taken over."
    mina "Guu, hhhnn- wwahhh-♥♥"
    "Instincts prone to sloppy, violent, impact-stricken sex."
    mina "Wwhhu, wwhhaa- hhaahhh-♥♥♥"
    "With a tight grip on Mina's hips, I did everything in my power to destroy not just her, but the both of us."
    mina "Whhh, gghhhu, iihhhz, uuoohhh-♥♥♥♥"
    "Destroy."
    "Destroy. Destroy."
    mc "Ah, fhhuuuck! Haaaa!"
    "Right now, {b}MY{/b} only purpose was to plug, stuff, and pull at Mina's fuck-ready insides."
    "{i}Gouge, scrape, prod, rub, stroke, swab, scratch.{/i}"
    mina "Ghhn, hhhuaa.. wwhahahaa-♥♥♥♥♥"
    "Right now, Mina had more sense in her pussy than she did in her head."
    "Destroy. Destroy. Destroy. Destroy."
    "Destroy. Destroy. Destroy. Destroy. Destroy. Destroy. Destroy. Destroy."
    mina "Whh, chhok, hhwwhh.. chhhum-♥♥♥♥♥♥"
    "All I could do was fuck, and all she could do was moan like a cock-stuffed bitch drunk on dick."
    mina "Whh, hhaa..!!"
    "Luckily, her lower mouth did all the talking required, inviting me, swallowing, and {b}consuming{/b} completely."
    mc "You want me to... Aahh... fine!"

    menu:
        "Destroy?(Dialouge/render changes only)":
            "...wait, it's not a question!"
        "Destroy!":
            mc "Take this, bitch!"

    scene mina_h_pbone2_a with dissolve
    show mina_h_pbone2
    mina "Gwwhhh... hnnggg... awww-!!!!"
    "As I brought my palm down on Mina's bouncing ass, the picture in my head was a wonderful dichotomy."
    mina "Ghhu, hhnngg, wwwahh- wwwhwhwhw-!!!!!"
    scene w3_2852 with pixellate
    "On one side was the Mina I knew as warm, caring, bright, bubbly... a source of affection..."
    scene mina_h_pbone2_a with pixellate
    show mina_h_pbone2
    mina "GGhhh, hhwwaa, wwwahh, hhehhh-"
    "On the other was the bleating fucktoy beneath me, a Mina consumed by a hedonistic state of bliss."
    mc "Gahh, {b}fhuuuuuuuuuuuuuuuuuuuuuuck!{/b}"
    "Neither was wrong. Neither was ugly."
    "We were two people letting out our frustrations... sharing and living out a fantasy... getting temporarily lost..."
    "Fuck, fuck, fuck, fuck, fuck, fuck...!"
    mc "You w-wonderful...!"
    "Take it, take it, take it, take it, take it, take it...!"
    mc "You lovely...!"
    "Fuck, damn, fuck, damn, fuck, damn...!"
    "As I felt my dick {b}boil{/i} over, as all feeling left my body... I could see it all."
    "Mina and someone who {i}resembled{/i} me, teetering on the edge of the track, about to take that final plummet..."
    mc "Mina... ahh... y-you..!"
    scene mina_h_pbone1_a with dissolve
    show mina_h_pbone1
    "In the last moments, that doomed soul called out..."

    menu:
        "\"I love you!\"(Dialouge/render changes only)":
            mc "Mina... I... I... {b}loooooooove you!{/b}"
        "\"Take it!\"":
            if w3MinaDaddy == True:
                mc "Take it, slut!"
            else:
                mc "T-take it!"

    stop ambient
    stop music
    play sound "sound effects/spurt.wav"
    scene w3_3230 with dissolve
    mc "Gyyh- asahhhh-♥♥♥♥♥"
    "Without even thinking about it, I gave Mina what she wanted."
    play ambient "sound effects/gulp2.wav"
    scene mina_h_pbone3_a with dissolve
    show mina_h_pbone3
    mc "Gyy, hhnhn-"
    "I buried myself entirely in Mina's embrace, shooting everything I had been working toward into Mina's womb."
    mina "Eehhhh.... hhaa.. chhum, hmmmh, mmuhuhh...♥♥♥"
    "I had given her my all."
    mc "Ghh, hhhaaaa..."
    "In the best possible way, like a pus-engorged abscess split asunder by its own putrid contents, I felt an exquisite sense of relief."
    stop ambient
    play sound "sound effects/thud-floor.mp3"
    scene w3_3231 with vpunch
    mc "Ughhh..."
    scene w3_3232 with dissolve
    mc "W-aah, uhh... that was... hnnngg..."
    scene w3_3233 with dissolve
    mina "W-woww... ahh..."
    play music "music/happy-clappy.ogg"
    scene w3_3234 with dissolve
    mina "I am so fhhhhuuuooool.... hehe, {size=-10}mmmhhh...{/size}"
    scene w3_3235 with dissolve
    "Even dissolved into one big pile of goop, Mina's voice hadn't lost its candor."
    scene w3_3236 with dissolve
    mina "........."
    mina "......"
    $ renpy.end_replay()
    scene w3_3237 with dissolve
    mina "...hey, [mcf]?"
    if not persistent.w3MinaHotelSex:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3MinaHotelSex = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    scene w3_3236 with dissolve
    mc "Y-yeah...?"
    scene w3_3237 with dissolve
    mina "I can't breathe."
    scene black with fade
    mc "Oh, I... yeeeeah, let me-"
    mina "{b}This{/b} is better~"
    scene w3_3239 with fade
    mina "Aaaaah... {i}big spoon secured{/i}."
    scene w3_3238 with dissolve
    "Mina simply held me for a little bit."
    "She spoke no words, but her affections were communicated all the same through touch."
    "How she clung to me filled me with an irrational peace of mind."
    "The way she ran her nose up and down my naked back made me feel, of all things, {b}present{/b} in the moment and acknowledged."
    scene w3_3239 with dissolve
    mina "{size=-10}Hmmm, mmhhh...{/size}"
    scene w3_3238 with dissolve
    "Even her sighs sounded like a lullaby to my ears and let me know that, on some level, she felt a measure of comfort from {i}my{/i} presence."
    scene w3_3240 with dissolve
    mc "I'm empty in the best possible way."
    scene w3_3239 with dissolve
    mina "Hehe~ It's a great feeling, isn't it?"
    scene w3_3240 with dissolve
    mc "Mmmmhhmmm."
    scene w3_3238 with dissolve
    "{i}To see and to be seen {b}was{/b} a wonderful feeling indeed.{/i}"
    scene w3_3239 with dissolve
    mina "Ha! Then again, I'm not {i}soooooo{/i} empty~"
    mina "I can feel it leaking out of me! I should probably get wash--"
    scene w3_3241 with dissolve
    mc "{b}No{/b}. Don't get up."
    stop music fadeout 3.0
    scene w3_3242 with dissolve
    mina "The sheets are going to get dirty. You wanna lie in your own filth?"
    scene w3_3243 with dissolve
    mc "Who cares. {i}This{/i} is too nice."
    scene w3_3242 with dissolve
    mina "Yeah, {b}it{/b} is..."
    scene w3_3244 with dissolve
    "......"
    "..."
    play music "music/inner-light.ogg"
    scene w3_3245 with dissolve
    mina "Hey [mcf]. When you think of yourself, do you feel like somebody, or do you feel like a nobody?"
    scene w3_3246 with dissolve
    "As she spoke, her hold on me grew more secure."
    scene w3_3247 with dissolve
    mc "That's out of nowhere."
    scene w3_3248 with dissolve
    mina "No, it's not. Don't guys get all introspective after they cum?"
    scene w3_3247 with dissolve
    mc "Yeah, well, you got me there."
    scene w3_3248 with dissolve
    mina "What even is that? Is it some kind of survival thing?"
    mina "Like, hey, you made a baby. So take stock, get your ducks in order?"
    scene w3_3247 with dissolve
    mc "Usually, it's just guilt over the fucked up thing you just masturbated to."
    scene w3_3245 with dissolve
    mina "Tell me about that later, but let's return to my original question..."
    scene w3_3249 with dissolve
    mina "Gun to your head, if you had to pick one or the other..."
    scene w3_3250 with fade
    mc "Right now? I'm feeling like somebody. What about you?"
    scene w3_3251 with dissolve
    "......"
    "..."
    scene w3_3252 with dissolve
    mina "I don't know. When things get quiet, my mind starts to wonder and wander."
    scene w3_3253 with dissolve
    mina "I know it's messed up, but all I can think of is that if you got something out of me, then I'm good. I put something into the world."
    scene w3_3250 with dissolve
    mc "I didn't {i}get{/i} something from you. We shared an afternoon."
    scene w3_3253 with dissolve
    mina "Sorry, I didn't mean it in a bad way."
    scene w3_3250 with dissolve
    mc "It's okay. I know you didn't."
    scene w3_3252 with dissolve
    mina "My dad once told me that if you give the world love, the world will provide you with love in return. It's not true, but I like to pretend it is."
    scene w3_3254 with dissolve
    mc "I can tell you try to live like it's true. Every part of you is so... {i}it must be exhausting{/i}."
    scene w3_3253 with dissolve
    mina "Sometimes I think giving other people love and kindness is like shouting into an {i}empty cave{/i}, and all you get reflected back is a dying echo of your voice that you can't even fucking stand."
    scene w3_3254 with dissolve
    mc "...how do you find the acoustics with me?"
    scene w3_3255 with dissolve
    mina "You haven't told me to just shut up and go to sleep."
    scene w3_3256 with dissolve
    mina "You have NO idea how much I appreciate that."
    scene w3_3257 with dissolve
    mc "...for what it's worth, my dad had a similar philosophy. He was a lawyer who helped people who couldn't help themselves."
    mc "He had a lot of love, and that love is reflected every time my mom speaks about him. It's reflected in the affection she gives me and it hasn't faded a single decibel."
    scene w3_3258 with dissolve
    mina "He sounds awesome."
    scene w3_3257 with dissolve
    mc "Your dad sounds pretty cool himself. I have a good feeling there's part of him in you as well."
    scene w3_3258 with dissolve
    mina "That's another thing I appreciate, [mcf]. You saying that."
    scene w3_3257 with dissolve
    mc "Well, I appreciate you letting me blow your back out."
    scene w3_3259 with dissolve
    mina "Pfffh- {b}ha!{/b} You just can't let a moment happen without making a joke, can you?"
    mc "Who says I'm joking? I appreciate it. It was very cool of you."
    mina "Shut up and go to bed."
    mc "Noooot sleepy~"
    stop music fadeout 3.0
    scene black with fade
    mina "I don't sound like that!"
    "........."
    "......"
    play sound "sound effects/shower.wav"
    "..."
    scene w3_3260 with wet
    "We laid around for another five or ten minutes before finally dredging ourselves out of bed."
    scene w3_3261 with dissolve
    "Mina had rebounded a lot quicker than I had, full of pep and giving credence to my suspicion that she might just be a succubus."
    stop sound
    play music "music/dog-park.ogg"
    scene w3_3262 with cmet
    mina "Mmmh, hmhhmmm~"
    scene w3_3263 with dissolve
    mina "Da da da da~ hmmmm~"
    mina "La, la, laaaa~ dadadada~"
    scene w3_3264 with dissolve
    mina "So... what kind of girl do you like, [mcf]? ~you can't say perky and blonde, either!"
    scene w3_3265 with dissolve
    mc "Like romantically? Put little thought into it."
    scene w3_3266 with dissolve
    mina "None whatsoever...?"
    scene w3_3267 with dissolve
    mina "Okay, say you go to a porn site. What are you searching for?"
    scene w3_3268 with dissolve
    mc "Those are two completely different things."
    scene w3_3269 with dissolve
    mina "Mmmh, hmm... ARE theeeeey...?"
    scene w3_3268 with dissolve
    mc "Well, not {i}completely{/i}, but... it's not like I search for say... {i}kind{/i}, {b}trustworthy{/b} blondes."
    scene w3_3270 with dissolve
    mina "So you {i}do{/i} know the kind of girl you like?"
    scene w3_3271 with dissolve
    mc "Would a vague answer like that satisfy you?"
    scene w3_3272 with dissolve
    mina "Not in the least!"
    scene w3_3268 with dissolve
    mc "I didn't think so."
    scene w3_3273 with dissolve
    mc "Well, what kind of man do you like? And don't say nerdy med students."
    scene w3_3274 with dissolve
    mina "I don't know either."
    scene w3_3275 with dissolve
    mc "No clue, eh? Okay then... say YOU go to a porn site..."
    scene w3_3276 with dissolve
    mina "Two dudes going at it! Hard, haha!"
    scene w3_3277 with dissolve
    mc "Sounds like you could always squeeze yourself into a throuple."
    scene w3_3278 with dissolve

    if w3MinaTransparent == True:
        mina "Like you and Hana, for example?"
        if hanaGF == True:
            scene w3_3279 with dissolve
            mc "..."
            scene w3_3280 with dissolve
            mina "You told me about it, remember?"
            scene w3_3279 with dissolve
            mc "I told you it was just a casual thing."
            scene w3_3280 with dissolve
            mina "So you did..."
        else:

            scene w3_3281 with dissolve
            mc "I told you it was just a casual thing."
            scene w3_3282 with dissolve
            mina "Hehe, casual's good~"
    else:

        mina "Any guys out there you want to sleep with so we can make that happen?"
        scene w3_3281 with dissolve
        mc "I-"
        scene w3_3282 with dissolve
        mina "Wait, don't answer that!"
        mc "I wasn't."
        mina "Hehe~"

    scene w3_3279 with dissolve
    mc "Soooooooo..."
    "......"
    scene w3_3283 with dissolve
    mc "...you watch a lot of porn, huh?"
    scene w3_3284 with dissolve
    mina "Is that... {i}weird{/i}?"
    scene w3_3285 with dissolve
    mc "It would be one of the more normal things about you. What's with that look?"
    scene w3_3286 with dissolve
    mina "Hmmmgg, that's the same thing as calling me weird, right?"
    scene w3_3287 with dissolve
    mc "I meant it as a compliment. Sure, you could fill in the blank and say the absence of normal is {i}weird{/i}, but there's also {b}exceptional{/b} or {b}unique{/b}."
    mc "...but the porn thing, that's pretty normal in itself."
    scene w3_3288 with dissolve
    mina "......"
    scene w3_3289 with dissolve
    mina "...Ian thought it was weird for a girl to look at porn."
    scene w3_3290 with dissolve
    mc "Heh, that is rich coming from a guy with his own homemade collection. Did he actually say as much?"
    scene w3_3291 with dissolve
    "That was, as usual for the pair, very bizarre."
    scene w3_3292 with dissolve
    mina "In so many different ways, over so many different things... it wasn't always direct, but I think he found a whole bunch of stuff about me off-putting."
    mina "{i}I learned to keep my thoughts to myself and just go along with whatever he wanted to do{/i}."
    scene w3_3293 with dissolve
    mc "Ah... {b}fuck Ian.{/b} Forget that shit."
    scene w3_3294 with dissolve
    mina "Heh, yeeeeeah. It seems obvious now, but it's funny how you don't realize how the {i}little{/i} things affect your self-esteem until you get some distance."
    scene w3_3295 with dissolve
    "......"
    "..."
    scene w3_3296 with dissolve
    mc "Do you know what might be fun?"
    scene w3_3297 with dissolve
    mina "...a game of Jenga?"
    scene w3_3296 with dissolve
    mc "{i}No{/i}. Let's go see what kind of boring porn they have on VOD and watch some together."
    scene w3_3298 with dissolve
    mina "We don't have to. I know what you're doing."
    scene w3_3299 with dissolve
    mc "What? There's nothing weird about a horny couple renting a hotel room and setting the mood with a little visual stimulation."
    mina "That seems a bit out of order."
    scene w3_3300 with dissolve
    mc "Does it? I don't know about you, but..."
    scene w3_3301 with dissolve
    play sound "sound effects/slap1.wav"
    scene w3_3302 with vpunch
    mina "O-oomf!"
    scene w3_3303 with dissolve
    mc "I'm still feeling pretty naughty."
    stop music fadeout 3.0
    mina "Hehe~ alright... it does sound pretty fun."
    scene black with fade
    mc "Good."

label w3MinaPornWatch:
    play music "music/select.ogg"
    scene w3_3304 with dissolve
    "We spent the next hour and a half watching some random run-of-the-mill feature, the type you'd expect to see available from a chain hotel."
    "It didn't {i}kick things off again{/i}, but it was fun in its own way. I hoped it might alleviate whatever dumb hangup Ian planted in her head."
    mct "(Hmm... she seems familiar...)"
    "It was more like one of those bad movie nights I used to have with Mom and Ian. We poked fun at the acting, sounds, and expressions the couple on screen made."
    scene w3_3305 with dissolve
    mina "What? You made a face just like that!"
    mc "Of course, I did! Everyone looks stupid when they're fucking!"
    mina "Hehe~ {b}I don't!{/b}"
    scene w3_3306 with dissolve
    "By the time it was over, we had spoken on a number of topics. One way or another, it always came back to sex."
    "From sexual politics to Mina's conservative upbringing and her mother's contradictory love of men. And why wouldn't it, when sitting butt naked, skin-to-skin on a hotel bed?"
    scene w3_3307 with dissolve
    mina "Yeeeeeah, Felicia said that isn't as fun as it sounds..."
    scene w3_3306 with dissolve
    "{i}...and why wouldn't it? My livelihood wholly revolved around sex."
    scene w3_3308 with dissolve
    mina "What about you? You have some, right?"
    scene w3_3309 with dissolve
    "We touched on her myriad fantasies before she turned the question back on me."
    scene w3_3310 with dissolve
    mc "Honestly, when you wanted to compare notes, I low-balled it with the window thing."
    scene w3_3308 with dissolve
    mina "Compared to what? Using the bathroom on my chest?"
    scene w3_3311 with dissolve
    "......"
    "..."
    scene w3_3312 with dissolve
    mina "Ahem, ahh... ah, {i}ew{/i}."
    mc "No, it's not that. Not necessarily..."
    scene w3_3313 with dissolve
    mina "Not necessarily?!"
    mc "My biggest fantasy... it's..."
    scene w3_3314 with dissolve
    "Mina was so good at putting a man to ease that I felt comfortable enough treading in deeper waters."
    scene w3_3315 with dissolve
    mc "My biggest fantasy is to {i}really{/i} let go."
    scene w3_3316 with dissolve
    mina "Let go of what?"
    scene w3_3315 with dissolve
    mc "...{b}everything{/b}. Not just my cares and worries, like a lot of people would mean, but my entire identity."
    mc "My memories, the love of the people in my life, {i}the love I feel in return{/i}, my purported morals, my past, my dreams, my ambitions--"
    scene w3_3317 with dissolve
    mina "--your doubts, fears, anxiety, the nagging voice in your head. {i}Everything{/i}. I got you."
    scene w3_3318 with dissolve
    mc "You understand, then?"
    scene w3_3317 with dissolve
    mina "All of it makes me feel uneasy too, but moving to California and reinventing yourself won't shut up the voice in your head."
    scene w3_3319 with dissolve
    mc "You've considered that, huh?"
    mina "Hasn't everyone dreamed of going to someplace no one knows you? {i}Heh{/i}, too scary!"
    mina "Besides, you can't unbuild yourself; you can only... redirect. {i}I think{/i}."
    scene w3_3306 with dissolve
    "......."
    "..."
    scene w3_3320 with dissolve
    mina "Ah, but what the hell do I know? What does any of this have to do with cumming?"
    scene w3_3321 with dissolve
    mc "I don't have any complex fantasies. All I want to do is to be mean."
    scene w3_3308 with dissolve
    mina "Name-calling and hair-pulling?"
    scene w3_3310 with dissolve
    mc "Not quite..."
    scene w3_3308 with dissolve
    mina "We could try S&M sometime if you want."
    scene w3_3321 with dissolve
    mc "That's a small part of it, but it's not exactly that..."
    scene w3_3322 with dissolve
    mina "Take your time. I won't judge you."
    scene w3_3323 with dissolve
    "......"
    "..."
    scene w3_3324 with dissolve
    mc "It's difficult to put into words. I want to capture a {i}feeling{/i} more than a specific act."
    scene w3_3323 with dissolve
    "Mina patiently waited for me to continue while I ordered my thoughts."
    scene w3_3324 with dissolve
    mc "There's a feeling of {i}revulsion{/i} that I want to turn inside out and direct at the world."
    scene w3_3325 with dissolve
    mina "Like how sometimes I get so disgusted with things that I just want to scream and let it all out?"
    mc "Exactly like that. {i}Too much like that{/i}."
    scene w3_3326 with fade
    mina "Oh, [mcf]... {b}every{/b} part of you is valid. There's not a thing wrong with wanting all your feelings seen and acknowledged."
    scene w3_3327 with dissolve
    mc "Is that what I want...? Ah, ha..."
    scene vic_fb1_a with pixellate
    show vic_fb1
    man "What are you?!"
    vic "A-ahh, hhnnggg-♥ I'm a stupid whore!"
    man "Do you like having sex for money?!"
    vic "Ahh, hhn-♥ Y-yees-♥"
    man "What's better, dick or money?!"
    vic "I, hhh- that's... ahh, hnggg... c-cccumming-"
    man "Haha, you bitch!"
    scene w3_3327 with pixellate
    mc "...sometimes I think all I want to do is find something holy and venerated and step on it until it's ugly, but that would just be a toddler having a temper tantrum."
    $ renpy.end_replay()
    scene w3_3328 with dissolve
    if not persistent.w3VicMidTierFBSex:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3VicMidTierFBSex = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    mina "Ah, [mcf]..."
    scene w3_3329 with dissolve

    if minaCleanStart == True:
        mina "I don't want to presume, but I enjoyed what we did today. I'd like to do it again... {i}many{/i} times, in fact."
        scene w3_3330 with dissolve
        mc "So did I. Ha, I'm glad I changed my mind about you."
        scene w3_3331 with dissolve
        mina "Don't be smug! I'm trying to say something serious!"
        scene w3_3329 with dissolve
        mina "What I mean is... there are things I want to experience, things you want to work through... what if we helped each other?"
        scene w3_3330 with dissolve
        mc "Well, I won't say no to continuing this sort of relationship, but that last part..."
    else:

        mina "I know I've already brought this up, but I mean it even more now. You're helping me with my stuff; what if I could be an out for your feelings as well?"
        scene w3_3330 with dissolve

    mc "Truthfully, it sounds scary."
    scene w3_3329 with dissolve
    mina "Well, heh...♥ You don't have to commit to anything concrete... just know that..."
    scene w3_3332 with dissolve
    mina "I'm pathetic and eager to please? {i}Hehe{/i}... sorry, I'm getting a little self-conscious here."
    scene w3_3329 with dissolve
    mina "...what I really want to say is I'd like to experience a {b}relationship{/b} where you don't have to measure out what you give and get."
    scene w3_3333 with dissolve

    if hanaGF == True:
        "In this moment, I couldn't help but think of the monogamy I promised Hana."
        mct "(Gah... why does life pile so many good things in my lap?)"
    else:
        "Life's really piling many good things in my lap lately, huh..."

    scene w3_3330 with dissolve
    mc "When you say relationship, do you mean...?"
    scene w3_3334 with dissolve
    mina "I'll be blunt. When I think of the future, I picture a lot of things, and one of those things is having someone to call {i}my{/i} own, but that's {i}the future{/i}."
    mina "I don't want to be one of those women who jump from relationship to relationship, never able to live for themselves. My mother is like that."
    scene w3_3335 with dissolve
    mc "She's on husband number four, right?"
    scene w3_3334 with dissolve
    mina "I know myself enough to see that's where I could head. I mean... even now, there's a voice in my head telling me that {i}I need someone{/i}, but..."
    scene w3_3336 with dissolve
    mina "I want to be a more self-reliant Mina and have the next someone come from the benefit of perspective."
    scene w3_3330 with dissolve
    mc "The fact that you can put it into words makes it seem like you're already pointed in that direction."
    scene w3_3329 with dissolve
    mina "Hehe~ I hope! And maybe one day, knowing myself... I {i}will{/i} want something from you. If that happens, I'll try not to be angry if you don't feel the same."
    scene w3_3330 with dissolve
    mc "You... {i}really{/i} make it easy for a guy."
    scene w3_3337 with dissolve
    mina "I'd ask the same of you... not that you ever would want something {b}more{/b}, right?"
    scene w3_3338 with dissolve
    "......"
    "..."
    scene w3_3339 with dissolve
    mina "Kidding! Kidding! Testing the waters! Kidding!"
    scene w3_3340 with dissolve
    "I couldn't help but share in her laugh."
    scene w3_3341 with dissolve
    mina "So... I can cross fucking in a hotel off my list."

    if minaCleanStart == True:
        scene w3_3342 with dissolve
        mc "You have a list?"
        scene w3_3343 with dissolve
        mina "That was, uh... what I wanted help with the other day."
        scene w3_3342 with dissolve
        mc "Oh, yeah. I forgot about that after you--"
        scene w3_3343 with dissolve
        mina "{b}Yeeeep.{/b}"
    else:
        scene w3_3342 with dissolve
        mc "That was an easy one."
        scene w3_3341 with dissolve
        mina "--and fun one to boot, hehe~"

    scene w3_3342 with dissolve
    mc "What else do you have on your list?"
    scene w3_3344 with dissolve
    mina "Hmmm, weeeeeell..."
    "Mina looked like she was giving it serious thought."
    scene w3_3345 with dissolve
    mc "Tell me the big ones."
    scene w3_3346 with dissolve
    mina "Something big? You didn't even give me anything concrete!"
    mc "What happened to not measuring things out? Besides..."
    scene w3_3347 with dissolve
    "*Chwup, fhwhup~*"
    mina "Ahh, hhnn- n-no f-fair...!"
    scene w3_3348 with dissolve
    mina "Hnnngg..."
    mc "C'mon, just a few immediate ones you feel like you're ready to try? We're talking about making them a reality, remember?"
    scene w3_3349 with dissolve
    mina "Ah, alright... in no order..."
    scene w3_3350 with dissolve
    mina "Sex outside."
    scene w3_3351 with dissolve
    mc "Doable."
    scene w3_3352 with dissolve
    "I knew I was capable of that thanks to Rosalind."
    scene w3_3350 with dissolve
    mina "I'd like to try being in the lead for once. Like {i}really{/i} in the lead."
    scene w3_3351 with dissolve
    mc "Very doable."
    scene w3_3353 with dissolve
    mina "Some costumes and roleplay would be fun."
    mc "Extremely doable, but isn't that your job?"
    mina "I should be good at it, right? It could double as practice!"
    scene w3_3354 with dissolve
    mc "What would you like to roleplay?"
    scene w3_3355 with dissolve
    mina "I... {b}don't know.{/b}"
    scene w3_3354 with dissolve
    mc "Ah, well... we can figure out the specifics later. Anything else?"

    if Mina_BiCurious >= 3:
        scene w3_3356 with dissolve
        mina "I want to... I want to... ah..."
        mina "I want to try having sex with a woman."
        scene w3_3357 with dissolve
        mc "Even if we limit it to someone we both know, that's also workable."
        scene w3_3355 with dissolve
        mina "...eh?! You think? You can't just ask someone, especially someone you know to--"
        scene w3_3354 with dissolve
        mc "Sure you can."

        if minaGym == True:
            mc "Veronica was super into you."
            scene w3_3358 with dissolve
            mina "She was?!"
            scene w3_3359 with dissolve
            mc "She stopped short of molesting you the day we joined her gym. How the hell could you not tell?"
            scene w3_3360 with dissolve
            mina "Ah, umm... {i}all girls school{/i}?"
            scene w3_3359 with dissolve
            mc "That's your excuse for everything, huh?"
            scene w3_3361 with dissolve
            mina "It's a good one!"

            if w3HanaDP >=4:
                scene w3_3357 with dissolve
                mc "We could also ask Hana. You two seemed friendly enough."
                scene w3_3356 with dissolve
                mina "Just because two women got along socially ONE time doesn't mean--"
                scene w3_3357 with dissolve
                mc "I'm just putting it out there as an option. Neither of us could go to a bar and pick up a third without embarrassing ourselves."

                if hanaGF == True:
                    mct "(Although, kinda weird fucking idea to bring up when I just promised her monogamy... yeeeah, that {b}could{/b} go south, but great things can't be done without risk.)"

                mc "You don't know her {i}that{/i} well, so if we could get her to agree, there is no chance of ruining a good thing."

                if w3MinaTransparent == True:
                    scene w3_3361 with dissolve
                    mina "Do you think she would be down?"
                    scene w3_3362 with dissolve
                else:
                    scene w3_3361 with dissolve
                    mina "Do you two have the kind of relationship where you could just ask-"
                    scene w3_3362 with dissolve
                    mc "Not exactly, but we could all get together and see how it goes."

                mc "You'll have to put in some work too. Try to be a little more seductive than you were with me."
                scene w3_3356 with dissolve
                mina "Ah, yy-- aahh...!"
                scene w3_3357 with dissolve
                mc "Sorry, it's just too fun - and hey, if you don't want to try either of those, there's always Felicia."
                scene w3_3363 with dissolve
                mina "Felicia?! I c--"
                scene w3_3364 with dissolve
                mc "You could, and she would. You know she's permanently down to fuck, but even if she wasn't, she'd probably even do it as a favor."
                scene w3_3360 with dissolve
                mina "I wouldn't want her to do it as a favor!"
                scene w3_3355 with dissolve
                mina "She's my only female friend. That sounds like a bad idea."
            else:

                scene w3_3357 with dissolve
                mc "We could also ask Felicia. If anyone would be amenable, it'd be here. You might even be most comfort--"
                scene w3_3363 with dissolve
                mina "A-ahh... you think? She's my only female friend... that sounds like a bad idea."
                scene w3_3364 with dissolve
                mc "You know she's permanently down to fuck, but she would probably do it as a favor."
                scene w3_3360 with dissolve
                mina "I wouldn't want her to do it as a favor!"
                scene w3_3359 with dissolve
                mc "I'm just saying it's an option. I don't think either of us could go to a bar and pick up a third without embarrassing ourselves--"


        elif w3HanaDP:
            scene w3_3357 with dissolve
            mc "You and Hana had some chemistry."
            scene w3_3356 with dissolve
            mina "Just because two women got along socially one time doesn't mean--"
            scene w3_3357 with dissolve
            mc "I'm just putting it out there as an option. Neither of us could go to a bar and pick up a third without embarrassing ourselves."

            if hanaGF == True:
                mct "(Although, kinda weird fucking idea to bring up when I just promised her monogamy... yeeeah, that {b}could{/b} go south, but great things can't be done without risk.)"

            mc "You don't know her {i}that{/i} well, so if we could get her to agree, there is no chance of ruining a good thing."

            if w3MinaTransparent == True:
                scene w3_3361 with dissolve
                mina "Do you think she would be down?"
                scene w3_3362 with dissolve
            else:
                scene w3_3358 with dissolve
                mina "Do you two have the kind of relationship where you could just ask-"
                scene w3_3359 with dissolve
                mc "Not exactly, but we could all get together and see how it goes."

            mc "You'll have to put in some work too. Try to be a little more seductive than you were with me."
            scene w3_3355 with dissolve
            mina "Ah, yy-- aahh...!"
            scene w3_3357 with dissolve
            mc "Sorry, it's just too fun - and hey, if you don't want to try either of those, there's always Felicia."
            scene w3_3363 with dissolve
            mina "Felicia?! I c--"
            scene w3_3364 with dissolve
            mc "You could, and she would. You know she's permanently down to fuck, but even if she wasn't, she'd probably even do it as a favor."
            scene w3_3360 with dissolve
            mina "I wouldn't want her to do it as a favor!"
            scene w3_3355 with dissolve
            mina "She's my only female friend. That sounds like a bad idea."
            scene w3_3354 with dissolve
            mc "You think? She's pretty fucking casual about--"
        else:

            scene w3_3357 with dissolve
            mc "Who would you be more comfortable with than Felicia? You know she's always down to--"
            scene w3_3363 with dissolve
            mina "Felicia? She's my only female friend. I couldn't. it'd be so--"
            scene w3_3364 with dissolve
            mc "Would it?"
            scene w3_3356 with dissolve
            mina "I, uhh... I don't know? It would be new territory for me."
            scene w3_3359 with dissolve
            mc "You know she'd be down, right?"
            scene w3_3360 with dissolve
            mina "Y-yeeah... {i}probably{/i}."
            scene w3_3357 with dissolve
            mc "She'd probably even do it as a favor."
            scene w3_3355 with dissolve
            mina "I don't want her to do it as a favor!"
            scene w3_3354 with dissolve
            mc "It could be a good chance for you two to grow closer."
            scene w3_3366 with dissolve
            mina "You just want to sleep with both of--"
            scene w3_3365 with dissolve
            mc "Hey, hey... this is your list. I'm just putting it out there as an option."
            mc "I don't think either of us could pick up a third at a bar without embarrassing ourselv--"
    else:

        scene w3_3356 with dissolve
        mina "I want to... I want to--"

    stop music
    play sound "sound effects/ringing-inbound.wav"
    scene w3_3367 with cmet
    scene w3_3368 with dissolve
    "*Ring, ring*"
    mc "Ah, hold that thought."
    scene black with fade
    mct "(I should've just let it go to--)"
    play sound "sound effects/phonemenu.wav"
    scene w3_3369 with dissolve
    "Unknown number. I usually wouldn't answer, but something in my mind {i}told{/i} me I should."
    scene w3_3370 with dissolve
    mc "Hello?"
    play music "music/bellissimo.ogg"
    scene w3_3371 with dissolve
    sophia "Hello, Mr. [mcl]. I didn't think we would speak again so soon."
    scene w3_3372 with dissolve
    mc "...you're the one who called me, Miss Lundgren."
    scene w3_3373 with dissolve
    sophia "It's not a social call. Well, not one on my behalf."
    sophia "How soon will you arrive home?"
    scene w3_3374 with dissolve
    mc "I don't know. I wasn't planning on it anytime-"
    scene w3_3375 with dissolve
    sophia "Mr. Van Doren has graciously found time in his schedule to educate you. He'll be here in one hour, {b}exactly.{/b}"
    scene w3_3376 with dissolve
    mc "What? You can't just--"
    scene w3_3375 with dissolve
    sophia "Please be here. It's to your benefit."
    play sound "sound effects/call-end.wav"
    scene w3_3377 with dissolve
    mc "Huh, wait- ah, shit."
    scene w3_3378 with dissolve
    mina "Something wrong?"
    mc "My neighbor had a pipe burst. I've got to-"
    scene w3_3379 with dissolve
    mina "Sure. No problem."
    mc "You're not mad I have to run off?"
    scene w3_3380 with dissolve
    mina "Why would I be? Saves me from having to awkwardly end our fun because I {i}really{/i} don't want to spend an entire night at a hotel without my stuff."
    scene w3_3381 with dissolve
    mc "Yeeeah, what would we have done? Get dinner and watch TV?"
    scene w3_3382 with dissolve
    mina "That wouldn't be so bad sometime, but not without access to my make up."
    scene w3_3381 with dissolve
    mc "...what were we talking about before, ah. Yeah."
    scene w3_3382 with dissolve
    mina "Call me tonight, okay?"
    scene w3_3383 with dissolve
    $ unread_mina = True
    $ history_mina = "After an afternoon tryst, Mina proposed helping me work through some of my own fantasies. It's a tempting offer... "
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    mc "Sure, will do."
    scene black with fade
    "Ah, goddamn it. I {b}hate{/b} rushing. What the hell does that old man even want."
    jump june15endrevise


label june15end:

    scene w3_3384 with curtains
    show screen textbox2 with dissolve
    "When I got back, I should've been more surprised at what I found, but honestly... part of me expected it."
    abel "Oh, good you're here."
    "Abel was sitting comfortably in a chair, a glass of tea in front of him, while Sophia idled in the kitchen."
    scene w3_3385 with dissolve
    abel "I feared you might stand me up like the ugly girl at a winter formal."
    scene w3_3386 with dissolve
    mc "You broke into my home?"
    scene w3_3387 with dissolve
    "A quick inspection of the room told me it was likely just us, although my mind doubled back and second-guessed the conspicuously suited man I had passed at the building's entrance."
    scene w3_3388 with dissolve
    abel "I did, although \"breaking in\" would be a generous term for the piddly security of this building."
    scene w3_3385 with dissolve
    abel "I do apologize about that, but I don't like visiting places that aren't verified by my staff."
    scene w3_3386 with dissolve
    mc "What kind of danger could you possibly expect in a pl--"
    scene w3_3389 with dissolve
    sophia "Look here."
    mc "What is...?"
    scene w3_3390 with dissolve
    sophia "It's a listening audio device that broadcasts sound above a specific decibel."
    mc "...I've been spied on?"
    sophia "I don't think so. This is the only one we found, likely forgotten after the others had been shoddily removed."
    scene w3_3391 with dissolve
    sophia "What's more, the battery likely ran out some time ago. This model can operate for 75 days in standby mode, so I suspect a previous tenant who had something to worry about."
    scene w3_3392 with dissolve
    abel "Point is, I only go places that are verified by my staff. Forgive the intrusion."
    scene w3_3393 with dissolve
    "......"
    "..."
    scene w3_3394 with dissolve
    mc "Why are you here?"
    scene w3_3395 with dissolve
    abel "Very respectably to the point. Good eye contact too."
    scene w3_3394 with dissolve
    mc "What is this, some kind of performance review?"
    scene w3_3395 with dissolve
    abel "Everything in life is performative, Mr. [mcl] - and every performance is judged."
    scene w3_3396 with dissolve
    mc "Like how you broke into my home? Is that supposed to imply something?"
    scene w3_3397 with dissolve
    abel "I hoped it might show how serious I am about this conversation."
    abel "I don't make house calls. {b}People come to me.{/b}"
    scene w3_3398 with dissolve
    abel "Sit down, please. It's rude to stand."
    scene w3_3399 with dissolve
    "Part of me wanted to desperately tell the old man to fuck off, but there was something about him that made refusing seem impossible."
    scene w3_3400 with fade
    "Whatever. {i}Let's talk{/i}."
    scene w3_3401 with dissolve
    mc "Why are you here?"
    scene w3_3402 with dissolve
    abel "Would you like Sophia to provide you some relief?"
    scene w3_3403 with dissolve
    mc "Why are you here?"
    scene w3_3404 with dissolve
    abel "The third time is less charming, but I understand your desire to cut to the heart of matters."
    scene w3_3405 with dissolve
    abel "I'm an overly familiar old man, but I do come bearing sound advice. I looked into you."
    scene w3_3406 with dissolve
    mc "You're not the first, unfortunately..."
    scene w3_3407 with dissolve
    abel "I am indeed the most thorough though, so I feel comfortable prescribing the following verdict."
    scene w3_3408 with dissolve
    abel "{i}There is nothing remotely remarkable about you.{/i} You are shockingly unexceptional."
    scene w3_3406 with dissolve
    mc "Thanks..."
    scene w3_3409 with dissolve
    abel "At first, I thought it would be appropriate to toy with you, just as he has seen fit to do with my Sophia, but your connection to Charles is tenuous at best."
    abel "And even if you were his protégé, I doubt he would mind me sniffing around. Undoubtedly, he would find it an interesting note in {i}his{/i} story."
    scene w3_3410 with dissolve
    mc "..."
    "What the fuck could I say to any of this? So I just kept my mouth shut and waited for him to further enlighten me."
    scene w3_3413 with dissolve
    abel "No, I'm here talking to you for a less petty purpose. How much do you know about the people who now surround you?"
    scene w3_3406 with dissolve
    mc "They're not the savory sort."
    scene w3_3407 with dissolve
    abel "No one of consequence ever is, but do you know the specifics?"
    scene w3_3406 with dissolve
    mc "Just what I could find on the internet."
    scene w3_3409 with dissolve
    abel "Ah, so nothing at all."
    abel "No one in this world {b}deserves{/b} a fair shake, despite what they tell you, but thankfully you fall within my providence. You see there are two types of people in this world..."
    scene w3_3411 with dissolve
    mc "There's probably a lot more than two..."
    scene w3_3412 with dissolve
    abel "Hush. There are those who think nothing of killing a spider in their own home. They simply can't be bothered to do otherwise."
    scene w3_3409 with dissolve
    abel "The other kind of person is the type who takes time to capture and release the spider safely, cognizant that a mere bug doesn't choose to encroach where it doesn't belong."
    scene w3_3408 with dissolve
    abel "Maybe I'm getting soft in my old age, but I'm here because you should be familiar with your environment. So you can have no one else to blame but yourself if you are dispossessed."
    scene w3_3414 with dissolve
    mc "{b}Please{/b}, educate me."
    scene w3_3415 with dissolve
    "What else could I say? Dr. Van Doren's motives aside, I wish he wasn't here, but it would be naïve to think I could make it through years at the Carnation Club without facing some obvious truths."
    mct "(That is... if he even tells me the truth. {i}Why the hell is he truly here{/i}?)"
    abel "Do you trust your bosses?"
    scene w3_3416 with dissolve
    mc "One's a gangster, one's a bomb-making hedonist, and one of them is Kathleen Pulman; I trust them to have their best interests at heart, but that is true of most employer-employee relationships isn't it?"
    scene w3_3414 with dissolve
    mc "Part of working for {i}anyone{/i} is becoming their best interest."
    scene w3_3415 with dissolve
    abel "I'm wondering what I'm even doing here."
    scene w3_3414 with dissolve
    mc "For the record, I don't trust you have good intentions either."
    scene w3_3415 with dissolve
    abel "Because of the present circumstances?"
    scene w3_3417 with dissolve
    mc "No. Because you're a head of a major pharmaceutical company, cavorting with pimps, refining a sex drug alongside your whore Nazi scientist."
    scene w3_3418 with dissolve
    sophia "Nazi?!"
    mc "No offense Sophia, but being blonde, sharply dressed in black, and testing drugs on people without their consent does conjure up a specific image."
    scene w3_3419 with dissolve
    abel "You're mad."
    scene w3_3420 with dissolve
    mc "You claim you're here to be candid? I'll be blunt too."
    scene w3_3421 with dissolve
    sophia "You have no idea who--"
    scene w3_3422 with dissolve
    abel "Pffh, hahaha! Hahahaha! I like you! I'm REALLY starting to think I've wasted my time."
    scene w3_3423 with dissolve
    mc "{b}Don't{/b}. Educate me about my environment and the people I work for."
    scene w3_3424 with dissolve
    abel "Okay, let's start with the gangster. You have a vague impression of his character, but you don't know his crimes do you?"
    scene w3_3425 with dissolve
    mc "No."
    scene w3_3426 with dissolve
    abel "It's so easy to get lulled into a sense of security when you're only exposed to a particular side of a person. Still, the man is an extortionist at heart."
    scene w3_3427 with dissolve
    abel "Loan sharking, protection rackets, insurance scams, gambling, prostitution. He's very much destroyed lives - not to mention he's killed people."
    scene w3_3429 with dissolve
    mc "...*ahem*, yeah?"
    scene w3_3430 with dissolve
    abel "Well, he's not a convicted murderer. He's a person of interest in four disappearances."
    scene w3_3431 with dissolve
    mc "That can mean a lot of things."
    scene w3_3430 with dissolve
    abel "{i}You want it to.{/i} And if he's not responsible, he's undoubtedly a factor in a number of suicides."
    scene w3_3427 with dissolve
    abel "Have you ever wondered if he knew your mother?"
    scene w3_3432 with dissolve
    mc "What?!"
    scene w3_3433 with dissolve
    abel "How many videos did she shoot? How big do you think the porn industry of Morehead Hills is?"
    scene w3_3434 with dissolve
    "......"
    "..."
    mct "(What the fuck, does everyone--)"
    scene w3_3435 with dissolve
    abel "It's better not to know, I suppose. I can tell you who HAS killed people."
    scene w3_3436 with dissolve
    mc "Warren?"
    scene w3_3437 with pixellate
    abel "For one... that man is a menace."
    abel "It takes a lot to get kicked out of the kind of mercenary company that would take a piece of trash like him, but he's pulled it off multiple times - for the same company, no less."
    abel "A by-product of being good at your job, but his \"Sandman\" moniker wasn't given to him because he excelled at fighting. {b}No{/b}, it has more to do with why he's currently a wanted man, living out of your club."
    scene w3_3438 with pixellate
    "......"
    "..."
    mct "(Holy shit, but I guess no fucking surprise there...)"
    scene w3_3439 with dissolve
    mc "You said for one? Who's the other?"
    scene w3_3438 with dissolve
    abel "Who do you suspect?"
    scene w3_3440 with dissolve
    mct "(Jacob...)"
    scene w3_3441 with pixellate
    abel "Warren's partner is more professional but a killer all the same. He got into trouble as a young man in Quebec that saw him flee the country."
    abel "After his time in the French Foreign Legion, he came to the States. Worked protection for various unsavory sorts."
    abel "Did other jobs too. The high-risk kind, the sort you contract out so it doesn't lead back to you."
    scene w3_3442 with pixellate
    abel "I don't think he took to it, considering he now guards a brothel. Still, it begs the question of what the man remains capable of."
    scene w3_3443 with dissolve
    mc "And Dr. Kohler?"
    scene w3_3442 with dissolve
    abel "He's everything you imagine him to be, but worse."
    abel "War profiteering, bribery, falsification of documents, state-sanctioned smuggling. He's done a lot for his country."
    scene w3_3444 with dissolve
    abel "A true American hero. A self-made man. {b}An irredeemable nihilist{/b}, of the lowest order - and that's before you even get into his hobbies..."
    scene w3_3443 with dissolve
    mc "Are you any better? You profit obscenely off the backs of sick people. {i}You lobby{/i}."
    scene w3_3445 with dissolve
    abel "I serve a purpose that will merit no appreciable distinction from the likes of you."
    scene w3_3446 with dissolve
    mc "{i}Riiiight{/i}... what about Kathleen? You neglected to mention her."
    scene w3_3447 with dissolve
    abel "She has Charles' nasty disposition but none of his accomplishments. As you noted, you can count on her to act in her own best interests. The only problem is I don't think she knows what that is."
    scene w3_3448 with dissolve
    mct "(He talks like he knows something...)"
    "It pisses me off."
    scene w3_3447 with dissolve
    abel "She's harmless."
    scene w3_3446 with dissolve
    mct "(I'm sure some people would disagree with that...)"
    scene w3_3449 with dissolve
    abel "You're young; you have your whole life ahead of you. You may even make something of yourself if you keep your eyes open."
    abel "Success is built upon and sustained by reading the wind and the changing tides. Nothing in this world lasts forever, from vaunted intuitions, to your favorite ice cream shop, and especially criminal enterprises."
    mc "Are you suggesting I should quit?"
    scene w3_3427 with dissolve
    abel "Not in the least! Quite the contrary, I believe you'd find quitting a more strenuous process. No, where you are is best."
    scene w3_3430 with dissolve
    abel "I'm suggesting you pay attention, so you don't get caught unaware."
    scene w3_3450 with dissolve
    mct "(He's DEFINITELY getting at something.)"
    scene w3_3451 with dissolve
    abel "If you ever find yourself in a bind, give Sophia a call. You should have her personal number now."
    play sound "sound effects/sms-chime.wav"
    scene w3_3452 with dissolve
    "Boop!"
    scene w3_3453 with dissolve
    mc "What kind of bind would I find myself in?"
    scene w3_3454 with dissolve
    abel "Perhaps the kind that would see your home bugged and surveilled. Do you know who lived here last?"
    scene w3_3453 with dissolve
    mc "I do..."
    scene w3_3454 with dissolve
    "Darius. The man who allegedly blackmailed Kathleen before running off."
    scene w3_3455 with dissolve
    abel "Do you know about him? Well, whatever he did, I would avoid making that same mistake."
    scene w3_3456 with dissolve
    mc "Be straight with me. You know something."
    scene w3_3457 with dissolve
    abel "I'm only making an inference, but it's entirely possible that the listening device has been here for years. I just wanted to underline my point."
    scene w3_3458 with dissolve
    sophia "It's a recent model. {b}A year old{/b}."
    scene w3_3459 with dissolve
    abel "Is it? That's good to know."
    abel "We shall take our leave now. Sorry for the intrusion."
    scene w3_3460 with dissolve
    mc "Wait... so let me get this straight."
    mc "An important man like you came here to give me vague advice out of the goodness of your heart, is that it?"
    scene w3_3461 with dissolve
    abel "[mcf]... let me ask you something... what could I {i}possibly{/i} get from a nobody like you?"
    abel "Think about it. Makes no sense."
    abel "This cost me nothing."
    scene w3_3462 with dissolve
    "......"
    "..."

    if w3SophiaPromoFinish == True:
        scene w3_3546 with dissolve
        sophia "Have a good afternoon, [mcf]."
    else:
        pass
    scene w3_3463 with dissolve
    "They showed themselves out just as they had let themselves in, leaving me confused."
    scene w3_3464 with dissolve
    "I hadn't learned anything I hadn't {i}known{i}. August was a piece of shit criminal, Chuck wasn't as I remembered him, and the two soldiers guarding the place had a body count."
    "None of that should surprise me, even if I tried not to think about it, but I felt disturbed and unsafe."
    scene w3_3465 with dissolve
    mct "(I mean, fuck... I'm just a pre-med student from the suburbs.)"
    mc "What the hell was the deal with that bug?"
    scene w3_3466 with dissolve
    "Was that {i}really{/i} the only one? Were there more? Did they plant it? Did they pretend it was here - no {i}why would they do that{/i}?"
    "It made no sense, but I knew the rest of my night would be spent researching how to detect listening devices. I wouldn't have peace of mind otherwise."
    mct "(Makes no sense, makes no sense...)"
    stop music fadeout 3.0
    scene black with fade
    "Dr. Van Doren's question repeated in my head."
    "What could he possibly get from a nobody like me?"
    mct "(God damn it, I don't like people coming and going as they please.)"
    play sound "sound effects/door-knock.wav"
    "*Knock, knock*"
    vic "[mcf]?"
    stop sound
    play music "music/night-on-the-docks-sax.ogg"
    $ date = "june15night"
    scene w3_3467 with wipeleft
    "What I did know is I didn't want to sleep in my apartment tonight. So tomorrow, I'd ensure I wasn't being spied on, but for now..."
    show june15night with squares
    mc "Heeeeeeey. Fancy seeing you here."
    "The comfort of home."
    scene w3_3468 with dissolve

    if w2ExEndingVictoria == True:
        vic "Twice in so few days? That's--"
    else:
        vic "Hey, hun! What are you doing here?"

    mc "Dropping in unannounced is a family trait."
    scene w3_3469 with dissolve
    vic "..."
    scene w3_3470 with dissolve
    mc "Are you busy? Want to watch some movies?"
    scene w3_3471 with dissolve
    vic "Are you ok- ah..."
    scene w3_3472 with dissolve
    vic "{i}Always{/i}."
    scene w3_3473 with dissolve
    "Don't ask."
    scene w3_3474 with dissolve
    mc "Hey, say..."
    scene w3_3475 with dissolve
    "Don't ask. Don't ask."
    scene w3_3474 with dissolve
    mc "Do you know a..."
    scene w3_3476 with dissolve
    "Don't ask. Don't ask. Don't ask. Don't ask."
    scene w3_3477 with dissolve
    mc "Do you know an August Byrnes?"
    scene w3_3478 with dissolve
    vic "Hmm...?"
    "WHY THE FUCK ARE YOU ASKING?!"
    scene w3_3479 with dissolve
    "......"
    "..."
    "IF SHE DOES, YOU JUST EXPOSED--"
    scene w3_3480 with dissolve
    vic "Is he a director? Has he done anything I've seen?"
    scene w3_3481 with dissolve
    vic "O-oh, wwhaaa...?!"
    "Oh, thank God."
    scene w3_3482 with dissolve
    "Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. Thank you. Thank you."
    scene w3_3483 with dissolve
    mc "I'm going to cook you dinner tonight."
    scene w3_3484 with dissolve
    vic "Ah, um... sure..."
    scene black with fade
    mc "What? Huh? This is all you have in the fridge? How are you staying healthy?!"
    "......"
    "..."
    jump june16start

label w3ExNoMinaFuckCall:
    $ w3Recollection = True
    "......"
    "..."
    "After everything, I found myself alone."
    "Not without accompaniment, but actually {i}alone{/i}."
    scene w3_3485 with circlewipe
    "Just me by my lonesome in a big dark room, not a single soul around, enjoying an afternoon matinée."
    scene w3_3486 with dissolve
    woman "It's coming! {b}Ruuuuuuun!{/b}"
    trailer "Coming this summer."
    mct "(Hmmm, Allison Smith...)"
    scene w3_3487 with dissolve
    mct "(What movie do I know her from...?)"
    trailer "Storms of Andromeda"
    mct "(Ah, hell. Who knows. This looks like shit, anyway.)"
    movieguy "...please put your phones away. Now, for the feature presentation."
    scene w3_3488 with dissolve
    mct "(Man, what a day already...)"
    mct "(The shoot was taxing. I should check in on the Carnations tomorrow, right?)"
    scene w3_3489 with dissolve
    mct "(Ah... what am I doing with my life? Why am I even watching this?)"
    scene w3_3490 with dissolve
    mct "(Hmmm. This kicks ass.)"
    play sound "sound effects/ringing-inbound.wav"
    scene w3_3491 with dissolve
    "*Ring, Ring*"
    mct "(Unknown number... well, I mean...)"
    mc "I'm the only one here."
    play sound "sound effects/phonemenu.wav"
    scene w3_3492 with dissolve
    mc "Hello?"
    play music "music/bellissimo.ogg"
    scene w3_3371 with dissolve
    sophia "Hello, Mr. [mcl]. I didn't think we would speak again so soon."
    scene w3_3372 with dissolve
    mc "...you're the one who called me, Miss Lundgren."
    scene w3_3373 with dissolve
    sophia "It's not a social call. Well, not one on my behalf."
    sophia "How soon will you arrive home?"
    scene w3_3374 with dissolve
    mc "I don't know. I wasn't planning on it anytime-"
    scene w3_3375 with dissolve
    sophia "Mr. Van Doren has graciously found time in his schedule to educate you. He'll be here in one hour, {b}exactly.{/b}"
    scene w3_3376 with dissolve
    mc "What? You can't just--"
    scene w3_3375 with dissolve
    sophia "Please be here. It's to your benefit."
    scene w3_3493 with dissolve
    mc "Huh, wait! Ah, s-shit!"
    mct "(After fucking with me, she thinks she can just--)"
    scene w3_3494 with dissolve
    mc "Ah, damn it."
    mct "(Damn it. Damn it. Damn it.)"
    mct "(Educate me? What the... ah...)"
    scene w3_3495 with dissolve
    "What other option do I have? I need to see what this crap is about."
    scene black with fade
    mct "(Whatever it is, it probably isn't good.)"
    "......."
    "......"
    "..."
    jump june15endrevise

label w3IanVisit:

    play music "music/hotshot-slow.ogg"
    scene w3_3496 with blinds
    grace "Is that all you have to say for yourself?"
    kil "It will do."
    scene w3_3497 with dissolve
    grace "........."
    grace "......"
    grace "..."
    kil "Stop breaking my balls, alright?!!"
    scene w3_3498 with dissolve
    grace "From where I'm standing, you still need to drop them."
    scene w3_3497 with dissolve
    kil "Ah, y-you- hhhnn- {b}d-damn it!{/b}"
    scene w3_3498 with dissolve
    grace "What?"
    scene w3_3497 with dissolve
    kil "*sigh* That was a good one."
    scene w3_3499 with dissolve
    grace "Thank you."
    "..."
    scene w3_3500 with dissolve
    grace "You don't return my calls, you miss your little cousin's graduation, your father's birthday party, and now you skip out on our anniversary party."
    grace "You've made it abundantly clear you don't want to be a part of this family."
    scene w3_3501 with dissolve
    kil "...have I? Then why are you here?"
    scene w3_3502 with dissolve
    grace "I can't accept that. Family's important, Ian."
    grace "Besides Charlie, I had no one. He raised and put me through school, where I met your father."
    scene w3_3503 with dissolve
    grace "Suddenly, I had a lot of family. You shouldn't throw that away just because of our disagreements."
    grace "Your cousin adores you; she has nothing to do with your perpetual temper tantrum."
    scene w3_3504 with dissolve
    kil "I was busy."
    scene w3_3505 with dissolve
    grace "Don't lie to me. Your father and I gave you everything you ever asked for. You never wanted for anything."
    scene w3_3506 with dissolve
    kil "There are some things I shouldn't have to ask for."
    scene w3_3507 with dissolve
    grace "I tried everything. When I thought I was smothering you, I gave you space. When that didn't work, I didn't know what the fuck to do."
    play sound "sound effects/ringing-inbound.wav"
    scene w3_3508 with dissolve
    "*Ring, ring*"
    stop music
    play sound "sound effects/phonemenu.wav"
    scene w3_3509 with dissolve
    kil "Yeah, Doc?"
    scene w3_3510 with dissolve

    if minaFlag == True:
        "After setting up the time and place with Mina, I had time to kill, so I thought I'd drop in on my hung-over and ailing friend."

        if minaCheat == True:
            "Whether it was some manifestation of guilt or if I was truly concerned, the irony of my visit wasn't lost on me."
    else:
        "With nothing better to do, I thought I'd drop in on my hung-over, ailing friend."

    scene w3_3509 with dissolve
    kil "Uh, huh. It's open. Just let yourself in."
    play sound "sound effects/phonemenu.wav"
    scene w3_3511 with dissolve
    "*Beep*"
    kil "That was [mcf], so let's finish this conversation never."
    scene w3_3512 with dissolve
    grace "I don't know what to do, but... just... {i}I love you, son.{/i}"
    grace "Time is more precious than you realize. I won't always be here. Ignoring your feelings today will just make you bitter tomorrow."
    scene black with fade
    kil "[mcf] will be here soon."
    grace "Yeah, I get the message."
    mc "Oh, uh... hello, Mrs. Beaufort. How are you?"
    grace "I'm good, [mcf]. I was just leaving."
    mc "Oh, well. It was nice to--"
    play music "music/hotshot.ogg"
    scene w3_3513 with dissolve
    kil "Thank God you showed up when you did! You cut her bitching short."
    mc "Glad to be of use."
    scene w3_3514 with dissolve
    kil "So what's up? Dropping by out of the blue isn't like you."
    mc "I just got off \"work.\" Wanted to come by and see how my sick little boy is doing."
    scene w3_3515 with dissolve
    kil "Yeah, yeah. Sorry. I just didn't feel like it, okay?"
    mc "You must have been really knocking them back last night if it put {b}you{/b} out of commission, huh?"
    scene w3_3516 with dissolve
    kil "What can I say? It was a special occasion."
    mc "Drowning your sorrows?"
    scene w3_3517 with dissolve
    kil "Not exactly, but... I don't know. It felt like a thing to do."
    kil "Even if I made my own bed, Mina is the longest relationship I have ever had."
    scene w3_3518 with dissolve
    kil "Honestly, I should've been drinking out of relief. Mina was a far too intense woman for me."
    scene w3_3519 with dissolve
    mc "Wasn't she more like a doormat?"
    scene w3_3520 with dissolve
    kil "In some ways, but she also put off this weird vibe. I don't know how to explain it. I could never get a solid read on her like I could other girls."
    scene w3_3519 with dissolve
    mc "What do you mean by that?"
    scene w3_3520 with dissolve
    kil "I've been wondering that myself."

    if ianIntrospect == True:
        kil "Like I'm the type of person who likes to test the limits of what I can get away with. I do it with my parents, I do it with my Uncle, and with the women I fuck. So naturally, I did it with the woman I..."
        scene w3_3521 with dissolve
        kil "I don't know. Typically when I piss someone off, I see {i}their{/i} shit."
        scene w3_3520 with dissolve
        kil "Their fucked up messes, what they {i}demanded{/i} of me, just stuff that made me feel good about twisting the knife."
        scene w3_3519 with dissolve
        mc "But with Mina?"
        scene w3_3522 with dissolve
        kil "Sometimes it felt like she was a mirror, right? Whenever I fucked up or made her jealous, it was like seeing what other people saw when they looked at me."
        scene w3_3524 with dissolve
        kil "For the first time, instead of testing other people's limits, I was seeing what I could get away with myself. Whenever she looked hurt, {i}I felt it{/i}."
        scene w3_3525 with dissolve
        kil "Don't just look at me like that. Does that make any fucked up sense?"
        scene w3_3523 with dissolve
        mc "Yeah, that's kinda messed up, dude - but I get it."
        scene w3_3522 with dissolve
        kil "You do?"
        scene w3_3523 with dissolve
        mc "Our views of ourselves are just unsubstantiated delusions until they meet opposition."
        scene w3_3529 with dissolve
        kil "Hell no, man. I live a dope life. I don't need some bitch to shatter that."
    else:
        scene w3_3519 with dissolve
        mc "...yeah?"
        scene w3_3521 with dissolve
        kil "I don't know, man. She's just not as stupid as she looks and I don't fucking get it."
        scene w3_3520 with dissolve
        kil "I woke up one night and she was just staring at me, lost in thought. Like the way Uncle sometimes gets when we play games."
        scene w3_3531 with dissolve
        mc "You sure she wasn't just 'mirin you, hot stuff?"
        scene w3_3526 with dissolve
        kil "God, don't say that word."
        scene w3_3527 with dissolve
        mc "What word?"
        scene w3_3526 with dissolve
        kil "That actually made my skin crawl."
        scene w3_3527 with dissolve
        mc "I mean, how could a girl not look? You're sooooo good-looking, Ian."
        scene w3_3526 with dissolve
        kil "Stop."
        scene w3_3527 with dissolve
        mc "God's gift to womankind."
        scene w3_3528 with dissolve
        kil "STOOOOOOOP. I'm not that kind of full of myself!"
        mc "Oh, you're not?"
        scene w3_3529 with dissolve
        kil "No! I'm a fucking gremlin with money and I know that, okay? A gremlin with a {b}dope life.{/b}"

    scene w3_3530 with dissolve
    mc "So you've said before."
    kil "How long are you staying? I got all day."

    if minaFlag == True:
        mc "I could fuck around for a couple of hours. Enough time to get a bite to eat and binge an episode or two of whatever shitty reality show we can find."
    else:
        mc "Let's kick it all day, then."

    kil "What a lucky week. You telling me I get some of my best friend's time two days in a row?"
    scene w3_3531 with dissolve
    mc "This is why Mina thought you wanted to fuck me, you know that?"
    scene w3_3532 with dissolve
    kil "Did she say that?!"
    scene w3_3531 with dissolve
    mc "She didn't need to. I could feel the jealousy in the air the day we met."
    scene w3_3532 with dissolve
    kil "Nah, dude. It doesn't come off like that. I don't have any positive male examples to gauge my tone against. That's all!"
    scene w3_3533 with dissolve
    "......"
    "..."
    scene w3_3534 with dissolve
    mck "Pfhh, hahaha!"
    kil "...who would top?"
    scene w3_3535 with dissolve
    mc "Is that a fucking question? If I asked you to, you'd spread it so wide that I could see what you had for lunch."
    scene w3_3536 with dissolve
    kil "Oh, fuck off, that's gross! Who's the gay one now?!"

    if minaCheat == True and Killian_Bromance >= 15:
        scene w3_3537 with dissolve
        "How could I laugh like this when I'm about to go see his ex after we..."
        mct "(Part of me wanted to tell him, but my sense of self-preservation prevented it. I didn't need to complicate my work life.)"
        mct "(Yeah, not afraid to rock the boat. Riiiiiight.)"

    scene w3_3535 with dissolve
    mc "The real question should be, \"who's your fucking daddy?\" You {i}definitely{/i} have those sorts of issues."
    scene black with fade
    kil "Uhhhhhhhhh! I can't even deny that, can I?"
    stop music fadeout 3.0
    if minaFlag == True:
        "So we shot the shit, ate, watched TV... all that junk. It was fun, but... {b}yeah.{/b}"
        "I did have to go see his ex-girlfriend."
        if minaCheat == True and hanaGF == True:
            jump w3MinaHanaGFHangStart
        elif minaCheat == True and hanaGF == False:
            jump w3MinaFullSpeedHangStart
        else:
            jump w3MinaPlatonicHangStart
    else:
        "So we shot the shit, ate, watched TV, played games, watched a movie..."
        "As time passed, the question of when to go home was answered for me."
        play ambient "sound effects/ringing-inbound.wav"
        scene w3_3538 with fade
        "*Ring, ring*"
        kil "Who is it?"
        mc "Unknown number."
        kil "Answer it."
        stop ambient
        play sound "sound effects/phonemenu.wav"
        scene w3_3539 with dissolve
        mc "Hello?"
        play music "music/bellissimo.ogg"
        scene w3_3371 with dissolve
        sophia "Hello, Mr. [mcl]. I didn't think we would speak again so soon."
        scene w3_3372 with dissolve
        mc "...you're the one who called me, Miss Lundgren."
        scene w3_3373 with dissolve
        sophia "It's not a social call. Well, not one on my behalf."
        sophia "How soon will you arrive home?"
        scene w3_3374 with dissolve
        mc "I don't know. I wasn't planning on it anytime-"
        scene w3_3375 with dissolve
        sophia "Mr. Van Doren has graciously found time in his schedule to educate you. He'll be here in one hour, {b}exactly.{/b}"
        scene w3_3376 with dissolve
        mc "What? You can't just--"
        scene w3_3375 with dissolve
        sophia "Please be here. It's to your benefit."
        scene w3_3540 with dissolve
        mc "Huh, wait! Ah, s-shit!"
        mct "(After fucking with me, she thinks she can just--)"
        scene w3_3541 with dissolve
        mc "Ah, damn it."
        scene w3_3542 with dissolve
        kil "What's wrong?"
        mct "(Damn it. Damn it. Damn it.)"
        mct "(Educate me? What the... ah...)"
        scene w3_3541 with dissolve
        mc "I'm going to have a house guest."
        scene w3_3543 with dissolve
        kil "Who?"
        scene w3_3544 with dissolve
        mc "Abel Van Doren."
        scene w3_3543 with dissolve
        kil "What the fuck? Why would he-"
        scene w3_3544 with dissolve
        mc "I've got no goddamn clue, man."
        scene w3_3543 with dissolve
        kil "I'll come with you."
        scene w3_3545 with dissolve
        mc "No, it's best you don't. I'll call you later about it, though."
        kil "...ah, alright. Nice hanging with you, bro."
        scene black with fade
        mc "You too, Ian."
        "........."
        "......"
        "..."
        jump june15endrevise
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
