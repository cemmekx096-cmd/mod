label June09Start:
    stop music
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionhana01 with blinds
    $ renpy.pause(6, hard=True)
    $ date = "june09day"
    play sound "sound effects/alarmclock-digital.wav"
    scene w2_1731 with sunshine
    show screen textbox2 with dissolve
    show screen qmenu with dissolve


    if met_abel == False:
        $ met_abel = True
    if not persistent.minaMCKissGallery:
        $ persistent.minaMCKissGallery = True

    mc "Hmm..."
    scene w2_1719 with dissolve
    play music "music/lobby-time.ogg"
    show june09day with squares
    if kat_polite == True:
        "Even after the veil of sleep had been lifted, last night's conversation with Mrs. Pulman remained at the forefront of my mind."
    else:
        "Even after the veil of sleep had been lifted, last night's conversation with Kathleen remained at the forefront of my mind."

    "The scope of my duties at the club was indeed truly open-ended."
    scene w2_1720 with dissolve
    "In a distant sense, the perverted mission I was assigned was exciting, but its actual execution was dread inducing."
    scene w2_1721 with dissolve
    mct "(I'm going to have to be smart about how we do this.)"
    scene w2_1722 with dissolve
    mc "*Yawn* Aaaaaugh...!"
    scene w2_1723 with dissolve
    mct "(A park, a gym, and Felicia's home...)"
    "If I want to get the shots without branding the girls as sex perverts, it'll all be about timing and finding the right location to go unnoticed."
    play sound "sound effects/thud-floor.mp3"
    scene w2_1724 with vpunch
    if w2KatSex == True:
        mct "(That fucking man-eater, I've never felt so drained...)"
    mc "......"
    mc "..."
    if w2KatSex == False:
        mct "(Maybe I might even enjoy this?)"
        "Not sure if I even want to know that about myself, but we will see..."
    scene w2_1725 with dissolve
    mc "Hana..."
    mct "(Wonder if she's still snoozing?)"
    scene w2_1726 with wipeleft
    "My new, abrupt house guest..."

    if w2HanaSex == True:
        "Despite all the bumping and grinding we did not two nights before, she had insisted on separate sleeping arrangements."
        scene w2_1727 with dissolve
        mct "(She said she didn't want to give the wrong impression after what we did.)"
    else:
        "Despite sharing a bed not two nights before, she had insisted on separate sleeping arrangements."
        scene w2_1727 with dissolve
        mct "(She said she didn't want to give the wrong impression.)"

    mct "(Women are funny.)"
    scene w2_1728 with dissolve
    hana "*snore* Schfwoo~"
    hana "Schfwoo~ Fhew~"
    scene w2_1729 with dissolve
    hana "Fhwooo~"
    scene w2_1730 with dissolve
    mc "Heh..."
    mct "(Adorable.)"
    scene w2_1732 with vpunch
    hana "*Sneeze* Achoo...!"
    scene w2_1733 with dissolve
    hana "Uh..."
    hana "Dammit, I was having a nice dream..."
    scene w2_1734 with dissolve
    hana "......"
    hana "..."
    hana "What are you looking at? Are you watching me sleep, weirdo?"
    scene w2_1735 with dissolve
    mc "You want some coffee?"
    scene w2_1734 with dissolve
    hana "...yes, please."
    scene w2_1736 with dissolve
    mc "Make us some while I'm in the shower, then."
    scene black with fade
    hana "You dick."
    play sound "sound effects/shower.wav"
    stop music fadeout 3.0
    "......"
    "..."
    stop sound
    play music "music/scissor-vision.ogg"
    scene w2_1737 with wet
    hana "Thanks... for letting me crash here last night."
    scene w2_1738 with dissolve
    mc "It's no problem. How long will I have the pleasure?"
    scene w2_1737 with dissolve
    hana "Mmmh... I don't know."
    scene w2_1739 with dissolve
    hana "Mom and I usually have a cold war after we get into it like we did last night. It could last a few days..."
    scene w2_1740 with dissolve
    mc "No worries, you can stay as long as you need. This place is too big for me, I'm more comfortable having someone to share it with."
    scene w2_1741 with dissolve
    hana "Ehe..."
    scene w2_1742 with dissolve
    "..."
    scene w2_1743 with dissolve
    hana "Thanks, [mcf]."
    scene w2_1744 with dissolve
    mc "If you don't mind me asking, what was it that you two got into it over?"
    scene w2_1745 with dissolve
    hana "Ah... it's {i}really{/i} fucking dumb."
    hana "Her memory isn't what it used to be, so whenever she misplaces something, she gets really agitated. It's easy to take it for granted, but you can imagine right?"
    scene w2_1746 with dissolve
    mc "I can."
    scene w2_1745 with dissolve
    hana "Well, for whatever reason, she thinks I'm hiding shit from her. I try to ignore it when she gets that way, and it's not like I don't understand delusions are part of her disease, but..."
    scene w2_1746 with dissolve
    mc "Everyone's got a tipping point."
    scene w2_1739 with dissolve
    hana "I think I may have too small of one sometimes."
    if trait_governor == True:
        $ Hana_Affection +=1
        scene w2_1740 with dissolve
        mc "I can relate."
        scene w2_1743 with dissolve
        hana "You can?"
        scene w2_1744 with dissolve
        mc "Uh huh, quite a bit."
        scene w2_1739 with dissolve
        hana "You know how much it sucks, then?"
        scene w2_1740 with dissolve
        mc "I do."
        scene w2_1739 with dissolve

    hana "It really, {i}really{/i} sucks."
    scene w2_1740 with dissolve
    mc "Don't beat yourself up over it. Your mom may be sick, but you're only human."
    scene w2_1742 with dissolve
    mc "Just cool off over the next however long and go from there."
    scene w2_1743 with dissolve
    hana "Yeah, you're right. What are you doing today?"
    hana "If you need to study, I'll get out of your hair."
    scene w2_1744 with dissolve
    mc "Ah, well... I think I've got to start working on some club business."
    mc "Don't ask about it, you don't want to know."
    scene w2_1747 with dissolve
    hana "My~ster~ious."
    scene w2_1744 with dissolve
    mc "What about you? You're welcome to veg out here if you want."
    scene w2_1743 with dissolve
    hana "Nah, I think I'll call an \"emergency band practice\". Work off some steam that way."
    scene w2_1748 with dissolve
    hana "Mind if I use your shower?"
    scene w2_1749 with dissolve
    mc "Think of this as your home."

    if w2HanaSex == True:
        scene w2_1750 with dissolve
        "With an enthusiastic heel turn, she extended her hips and..."
        scene w2_1751 with dissolve
        mc "--!"
        scene w2_1752 with dissolve
        hana "Will do."
        scene w2_1753 with dissolve
        "......"
        scene w2_1754 with dissolve
        "..."
        scene w2_1755 with dissolve
        mct "(...the wrong impression, was it?)"
    else:


        scene w2_1756 with dissolve
        hana "Thanks, [mcf]. You're a solid dude."
        scene w2_1757 with dissolve
        "......"
        scene w2_1758 with dissolve
        "..."
        scene w2_1755 with dissolve
        mct "(I am, ain't I?)"

    scene w2_1759 with dissolve
    if kat_polite == True:
        mct "(I should call Mrs. Pulman and see when she expects me to finish with her tasks.)"
    else:
        mct "(I should call Kathleen and see when she expects me to finish with her tasks.)"

    scene w2_1760 with dissolve
    "I probably only have a few days..."
    scene black with fade

    stop music fadeout 3.0
    play sound "sound effects/ringing-outbound.mp3"
    "*Ring... {w}ring... {w}...ring...*"
    stop sound
    play sound "sound effects/phonemenu.wav"
    scene w2_1761 with dissolve
    "*Click*"
    scene player-bedroom blur with dissolve
    show kat-call with dissolve

    if Kathleen_Trust >= 8:
        kat "[mcf]. Is this about your work for the week?"
    else:
        kat "Mr. [mcl]. Is this about your work for the week?"

    kat "I expected you to call, but this early? Very commendable. What an eager beaver."
    mc "I need to know when you expect the photos to be delivered."
    kat "The interview with Mr. Ford is set for Thursday. That's the time he's cleared in his busy schedule to speak with you."
    kat "All Mrs. Ford knows is she's entertaining a journalist that night. Keep it that way."
    mc "Felicia doesn't know a thing about this?"
    kat "No, but I wish I could see the look on her face when she opens the door."
    mc "Do you anticipate her reacting poorly?"
    kat "Poorly? I don't know. Shocked? Oh, yes."
    kat "For the other two, it doesn't matter the day you get it done as long as it's by Friday. Get the materials to me by then, please."
    "That gives me four days time then."
    mc "Understood."
    kat "I'll text you the location of the park and Mrs. Ford's penthouse. Do you have any questions?"
    mc "I know you said you'd leave it to my discretion, but how far are you really expecting me to go with this?"
    kat "Do what feels... {i}right{/i}. If you need to motivate them, explain to them that the girl with the \"best\" shoot will gain a leg up this weekend."
    mc "They will?"
    kat "Sure, why not. It'll be more fun that way."
    "Did she just... decide that?"
    mc "...alright, I'll get it done."
    "The capricious nature of the competition aside, and despite my mixed feelings, I knew what I had to do."

    if Kathleen_Trust >= 8:
        kat "I have confidence in you, [mcf]."
    else:
        kat "Don't let me down, Mr. [mcl]."

    kat "Ta-ta."
    play sound "sound effects/phonemenu.wav"
    "*Click*"
    scene w2_1762 with dissolve
    mct "(I said four days, but it's more like three...)"
    mct "(That means I can do... Rosalind or Veronica today and take care of the other tomorrow, a day before my appointed meeting with Felicia's husband.)"
    mct "(The question is, which one do I want to take care of first? I'll have to do both of course, but...)"
    hide screen textbox2 with dissolve

    menu:
        "Call Rosalind and tell her to meet you in the park.":
            $ w2RoseFirst = True

            play sound "sound effects/phonemenu.wav"
            scene w2_1763 with dissolve
            show screen textbox2 with dissolve
            "Beep!"
            play sound "sound effects/ringing-outbound.mp3"
            scene w2_1761 with dissolve
            "......"
            scene black with fade
            "..."
            jump w2RosalindParkStart
        "Call Veronica and tell her to expect you at the gym.":

            play sound "sound effects/phonemenu.wav"
            scene w2_1763 with dissolve
            show screen textbox2 with dissolve
            "Beep!"
            play sound "sound effects/ringing-outbound.mp3"
            scene w2_1761 with dissolve
            "......"
            "..."
            scene black with fade
            jump w2VeronicaGymStart



label w2RosalindParkStart:
    stop sound
    play ambient "sound effects/ringing-inbound.wav"
    scene w2_1764 with fade
    "*Ring, ring... {w}Ring, ring..."
    man "You're not going to answer it?"
    scene w2_1765 with dissolve
    rose "They will call back..."
    scene w2_1764 with dissolve
    man "If you're not going to answer it, I will."
    scene w2_1766 with dissolve
    rose "Uh..."
    scene w2_1767 with dissolve
    "..."
    scene w2_1768 with dissolve
    man "Too late."
    stop ambient
    play sound "sound effects/phonemenu.wav"
    scene w2_1769 with dissolve
    play music "music/leaving-home.ogg"
    man "Is that you, Rupert?"
    scene w2_1770 with dissolve
    "A man's deep voice, with the barest trace of a scouse accent, came unexpectedly from the other end of the line."
    scene w2_1769 with dissolve
    man "I'm in your home."
    scene w2_1770 with dissolve
    "It was a distinctly matter-of-fact, threatening tone."
    scene w2_1771 with dissolve
    mc "Is... this the right number? I'm looking for Rosalind."
    scene w2_1772 with dissolve
    man "...ah."
    man "The number read {i}Answer this{/i}. I just presumed you were her worthless husband."
    mct "(Worthless...?)"
    scene w2_1771 with dissolve
    mc "Who is this?!"
    scene w2_1773 with dissolve
    man "You didn't tell me you found a man."
    man "That makes things easier for all of us."
    scene w2_1774 with dissolve
    rose "He has nothing to do with this."
    scene w2_1775 with dissolve
    man "Shut the fuck up. I'll be the one to determine that."
    scene w2_1776 with dissolve
    man "Who are you?"
    scene w2_1777 with dissolve
    mc "[mcf]. Now, I asked you first."
    scene w2_1776 with dissolve
    olly "Well, [mcf], I'm Oliver. Olly to my friends."
    olly "How do you know Rosalind?"
    scene w2_1778 with dissolve
    "The conclusion had already formed in my head."
    scene w2_1779 with dissolve
    mc "...you're a loan shark?"
    if roseFlag == False:
        if kat_polite == True:
            "I recalled Rosalind's personalized file that Mrs. Pulman had me study in the interim between Veronica being chosen and the month of June."
        else:
            "I recalled Rosalind's personalized file that Kathleen had me study in the interim between Veronica being chosen and the month of June."
    scene w2_1778 with dissolve
    olly "Oh, good. Then you know her situation. What's your relationship with this sorry bitch?"
    scene w2_1781 with dissolve
    mc "I'm a friend. Put Rose on the phone, please."
    scene w2_1780 with dissolve
    olly "Did you know she owes me quite a bit of money? She's three weeks in delinquency from her last payment."
    scene w2_1781 with dissolve
    mc "Put Rose on the phone."
    scene w2_1776 with dissolve
    olly "Now, I try to be understanding, but she did marry that sack of shit who ran off."
    scene w2_1782 with dissolve
    olly "Unsecured loans are a tricky business, but luckily she's quite the looker, ain't she?"
    scene w2_1777 with dissolve
    mc "Put Rose on the phone, you fucker."
    scene w2_1783 with dissolve
    olly "Sheesh, fine! No need to repeat yourself, I was just going to say, if she has someone to lean on..."
    scene w2_1784 with dissolve
    rose "..."
    scene w2_1785 with dissolve
    olly "...she should probably make use of that shoulder before the month is up."
    scene w2_1786 with dissolve
    rose "*Gulp*"
    scene w2_1787 with dissolve
    olly "That should do as your reminder. I'll see myself out, luv."
    scene w2_1788 with dissolve
    olly "You have another week to get square with your missed payments, otherwise we'll have to look into alternative ways of paying."
    scene w2_1789 with dissolve
    rose "Hey, [mcf]. Sorry, but you caught me at a bad time..."
    mc "Are you okay?"
    scene w2_1790 with dissolve
    olly "Thanks for the tea."
    stop music fadeout 3.0
    scene w2_1791 with dissolve
    rose "Y-yes, I'm fine."
    scene w2_1792 with dissolve
    mc "That's the guy you owe money to? He hasn't hurt you, right?"
    scene w2_1791 with dissolve
    rose "N-no, he's just been..."
    scene w2_1793 with dissolve
    "Rose paused to carefully consider how to put it."
    play music "music/a-lost-map-of-a-heaven.ogg"
    scene w2_1791 with dissolve
    rose "Lurking around for the past week."
    scene w2_1792 with dissolve
    mc "What the hell does that mean?"
    scene w2_1791 with dissolve
    rose "Just stuff to remind me that I owe him. He likes to sit across the street so I see him when I go out."
    rose "Sometimes he knocks on the door and asks for a cup of tea..."
    scene w2_1792 with dissolve
    mc "You mean he's threatening you."
    scene w2_1791 with dissolve
    rose "Not exactly..."
    scene w2_1794 with dissolve
    rose "I mean, I don't like it or anything."
    rose "It's one thing when my daughter's not here, like today, but she's not dumb... she knows something is wrong."
    scene w2_1792 with dissolve
    mc "Not exactly? He's threatening you."
    scene w2_1793 with dissolve
    rose "..."
    scene w2_1796 with dissolve
    mc "Did I hear right? Did he say you only had a week to--"
    scene w2_1795 with dissolve
    rose "Why did you call?"
    scene w2_1796 with dissolve
    mc "Forget about that for a second, are you able--"
    scene w2_1795 with dissolve
    rose "Why did you call, Mr. [mcl]?"
    "There was a cold, unmistakable edge to her voice."
    "This was a topic she desperately wanted to run away from."
    scene w2_1796 with dissolve
    mc "...Mrs. Pulman wants us to have another photo shoot, but if this is a bad time or you're not in the moo--"
    scene w2_1797 with dissolve
    rose "No, this is a perfect time."
    rose "I'll do whatever is required of me."
    scene w2_1798 with dissolve
    mc "..."
    "From the sound of it, assuming she even wins, there's two weeks left in the exhibition and that bastard only gave her a week to pay back her missed installments."
    scene w2_1797 with dissolve
    rose "What do I need to do?"
    scene w2_1798 with dissolve
    mc "There's a park by your home. I want you to meet me there."
    scene w2_1800 with dissolve
    rose "...okay."
    rose "Anything else?"
    scene w2_1799 with dissolve

    if toughness >=20:
        mc "You need to wear something slutty."
    else:
        mc "You need to wear something revealing."

    scene w2_1801 with dissolve
    rose "......"
    scene w2_1800 with dissolve
    rose "...okay. I'll meet you there in an hour?"
    scene w2_1802 with dissolve
    mc "I'll see you then. Go-"
    stop music
    play sound "sound effects/phonemenu.wav"
    scene w2_1803 with dissolve
    "*Beep*"
    mc "Goodbye."
    scene w2_1762 with dissolve
    mc "..."
    mct "(Fuck me, is this something I should try to handle?)"
    "My job is to make sure she can get through the month, but what the hell could I even do here...?"

    if roseFlag == True and roseDealFullAcceptance == False:
        "It {b}felt{/b} like it was something I needed to take care of. If not because of my job, then because it was the right thing to do."
    if roseFlag == True and roseDealFullAcceptance == True:
        "It {b}felt{/b} like it was something I needed to take care of. If not because of my job, if not because it was the right thing to do, then because we had made a deal. She was mine for this month."

    scene w2_1804 with dissolve
    play sound "sound effects/thud-floor.mp3"
    scene w2_1805 with vpunch
    mct "(...the only way to help would be to give her money, right?)"
    mct "(Even with my new salary, I doubt I could afford that.)"

    if kat_polite == True:
        mct "(Do I bring this up to Mrs. Pulman? Maybe Dr. Chuck...?)"
    else:
        mct "(Do I bring this up to Kathleen? Maybe Dr. Chuck...?)"

    "First I need to find out what exactly three weeks of missed payment means, but before that..."
    scene w2_1806 with dissolve
    "I should get dressed."
    scene black with fade
    "........."
    "......"
    "..."
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionrosalind04 with blinds
    $ renpy.pause(6, hard=True)
    jump w2RosalindParkStartForReal


label w2RosalindParkStartForReal:
    if _in_replay:
        show transitionrosalind01 with cmet
        show screen textbox2 with dissolve
        "Please set [mcf]'s personality (toughness score) for this replay."
        hide screen textbox2 with dissolve
        menu:
            "Nice guy (Toughness: 0)":
                $ toughness = 0
            "Mischevious (Toughness: 18)":
                $ toughness = 18
            "Asshole (Toughness: 30)":
                $ toughness = 30
        show screen textbox2 with dissolve
        "Did [mcf] take advantage of Rosalind when they first met?"
        hide screen textbox2 with dissolve
        menu:
            "Yes.":
                $ roseTakeAdvantage = True
            "No.":
                pass
        show screen textbox2 with dissolve

    scene w2_1807 with blinds
    play ambient "sound effects/park.wav"
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    "Incognito."
    "Even if this wasn't my neck of the woods, I thought it'd be best to dress the part."
    "However, I think I made a mistake, because..."
    play music "music/sneaky-snitch.ogg"
    scene w2_1808 with vpunch
    "I look suspicious as fuck! I'm standing out even more!"
    scene w2_1809 with dissolve
    mct "(This camera isn't helping either!)"
    scene w2_1810 with dissolve
    mc "......"
    scene w2_1811 with dissolve
    mc "..."
    scene w2_1812 with vpunch
    mct "(I definitely look like I'm up to no good!)"
    scene black with fade
    mct "(Lose the mask, idiot.)"
    scene w2_1813 with cmet
    "Now... I'm less Unabomber and more just a guy in a hat."
    scene w2_1814 with dissolve
    "I hope."
    scene w2_1815 with dissolve
    mct "(Rosalind's running a little late...)"
    scene w2_1816 with dissolve
    mct "(Jeez, aren't those two embarrassed to do that in public...?)"
    scene w2_1817 with dissolve
    mc "Heh..."
    scene w2_1818 with dissolve
    mct "(She lives way closer than I do. Why is she taking so long...?)"
    scene w2_1819 with dissolve
    mct "(Is she having a hard time picking out what to wear? Come to think of it, maybe leaving it up to her on what to wear was a mistake...?)"
    scene w2_1820 with w12
    mc "You call this slutty?!"
    woman "{size=-10}[mcf].{/size=-10}"
    rose "I didn't know what you meant..."
    woman "[mcf]!"
    mc "..."
    scene w2_1821 with dissolve
    stop music
    woman "{size=+10}[mcf]...!{/size=+10}" with vpunch
    "Pulling me from my stupid little daydream was a woman's voice calling my name."
    scene w2_1822 with wipeleft
    "It was Rosalind."
    scene w2_1823 with dissolve
    rose "C-come here!"
    scene w2_1822 with dissolve
    "She timidly stood at the lip of a nearby tunnel, ushering me to come closer."
    scene black with fade
    mct "(How long...?)"
    play music "music/covert-affair.ogg"
    scene w2_1824 with dissolve
    mc "How long have you been here?"
    scene w2_1825 with dissolve
    rose "Um... just under ten minutes? Hehe..."
    scene w2_1824 with dissolve
    mc "Why did you wait so long?"
    scene w2_1826 with dissolve
    rose "I was waiting for that couple next to you to leave..."
    rose "The man lives on my street..."
    scene w2_1827 with dissolve
    mc "Oh... gotcha."
    scene w2_1828 with dissolve
    rose "...and that wasn't his wife."
    scene w2_1824 with dissolve
    mc "Hey, Rose... would you put your arms down a second?"
    scene w2_1826 with dissolve
    rose "Okay..."
    scene w2_1829 with dissolve
    "Rosalind had picked out an interesting-looking, snake-skinned mini dress."
    scene w2_1830 with dissolve
    mc "You had something like that in your wardrobe?"
    scene w2_1831 with dissolve
    rose "It's... fifteen years old."
    scene w2_1830 with dissolve
    mc "I'm surprised it still fits you. That's amazing, you must work really hard to stay in shape."
    scene w2_1832 with dissolve
    rose "..."
    scene w2_1833 with dissolve
    "She looked pretty self-conscious, not that I blamed her."
    "However, she also looked pretty. {b}Very{/b} pretty."
    hide screen textbox2 with dissolve

    menu:
        "Tell Rosalind her hair looks nice."(chg=[("rosalind_up", roseTakeAdvantage == False or roseTAapology == True)]):


            show screen textbox2 with dissolve
            "It wasn't just the dress either."
            mc "I like you with your hair down. You're always pretty, but for some reason it feels nostalgic."
            scene w2_1834 with dissolve
            rose "Nostalgic...? We've only known each other for a few weeks."
            scene w2_1835 with dissolve
            mc "Yeah, I guess you just remind me of someone. Either way, I like it."
            mc "You have beautiful curls."
            scene w2_1836 with dissolve
            rose "I wish I could say thanks, but considering the circumstance..."
            scene w2_1837 with dissolve
            mc "Hehe, yeah... it probably sounds hollow, huh?"

            if roseTakeAdvantage == False or roseTAapology == True:
                $ Rosalind_Affection += 1

                scene w2_1834 with dissolve
                rose "No, I'm sorry. I know you're just trying to make me comfortable."
                rose "You're a kind kid."
                scene w2_1835 with dissolve
                mct "(Kid...? A small, peculiarly stupid part of me resented the way she put that.)"
                scene w2_1834 with dissolve
                rose "Thanks for the compliment. Should we... move onto why I'm here?"
                scene w2_1835 with dissolve
            else:

                scene w2_1836 with dissolve
                "Should we... move onto why we're here?"
                scene w2_1837 with dissolve

            mc "Yeah, let's not waste any more time."


        "{color=#FF1493}[[Full Deal]{/color} Kiss her."(chg=["rosalind_passion_up"]) if roseDealFullAcceptance == True:
            $ Rosalind_Libido += 1

            show screen textbox2 with dissolve
            mc "Rosalind...?"
            scene w2_1835 with dissolve
            "She looked at me with upcast doe-like eyes full of nervous energy. It was the sort of look that reaffirmed my intention to kiss her even more."
            scene w2_1834 with dissolve
            rose "...yes?"
            scene w2_1838 with dissolve
            "With a sudden motion, I scooped her up in my arms. Her eyes widened in surprise."
            "I had fully accepted the terms of her deal."
            scene w2_1839 with dissolve
            rose "Mmh--!"
            "She belonged to me."
            scene rosaparkiss1_a with dissolve
            show rosaparkkiss1
            "She gave no resistance as my tongue pried open her lips and hurdled into the wet, warm hole in-between."
            rose "Aahh...mhh..."
            "Instead, she signaled her acceptance with a gentle contented hum."
            scene rosaparkiss2_a with dissolve
            show rosaparkkiss2
            "It wasn't long before her passivity turned into active participation, pressing her lips deeper into mine and forming a tight seal."
            "She felt heavy in my hands, like her entire body had gone slack and become dead weight..."
            mct "(Was I always this much of a fucking creep?)"
            scene w2_1840 with dissolve
            mc "*Smooch*"
            "When we parted, it was with a soft peck on the cheek and pleasant murmur."
            scene w2_1841 with dissolve
            "Our lips no longer touched, but our eyes were now locked."
            scene w2_1842 with dissolve
            rose "W-why..."
            scene w2_1843 with dissolve
            rose "That was embarrassing!"
            scene w2_1844 with dissolve
            mc "Worried someone might've seen?"
            scene w2_1843 with dissolve
            rose "Of course I am!"
            scene w2_1844 with dissolve
            mc "It didn't seem that way to me."
            scene w2_1843 with dissolve
            rose "Can we... move onto why I'm here, please?"
            scene w2_1845 with dissolve
            mc "Yeah, let's not waste any more time."
        "Move to the task at hand.":




            mc "Let's not waste any more time."
            scene w2_1834 with dissolve
            rose "I'd... really appreciate that."

    scene w2_1846 with dissolve
    mc "I want you to walk over to that bench and sit down. I'll follow you."
    scene w2_1847 with dissolve
    rose "You're not going to have me do anything too crazy out in the open, right?"
    scene w2_1848 with dissolve
    mc "Mrs. Pulman didn't give me explicit instructions, but you and I both can guess what she expects."
    scene w2_1849 with dissolve
    rose "..."
    "Trepidation was written plain on Rosalind's beautiful face."
    scene w2_1850 with dissolve
    rose "P-please, I..."
    scene w2_1851 with dissolve
    rose "Get whatever photos you need quickly then."
    scene w2_1852 with cmet
    play sound "sound effects/camera-phone-shutter.wav"
    "Like stepping foot off a diving board, Rosalind took the plunge and pushed herself forward at a hurried pace."
    scene w2_1853 with dissolve
    play sound "sound effects/camera-phone-shutter.wav"
    "Each step of her high heels made a sharp unwanted clack against the concrete pavement."
    scene w2_1854 with dissolve
    play sound "sound effects/camera-phone-shutter.wav"
    "It was like a foghorn in the night, but thankfully hardly anyone was around to take notice at this time of the day."
    scene w2_1855 with dissolve
    play sound "sound effects/camera-phone-shutter.wav"
    "Rosalind continued on without hesitation, looking straight ahead, until she arrived at where I told her to sit."
    scene w2_1856 with fade
    mc "So far, so good."
    scene w2_1857 with dissolve
    rose "I'm more uneasy about what's..."
    scene w2_1858 with dissolve
    woman "Oh! Is this a photo shoot?"
    "A woman crossed our path and stopped to ask a question. Her shrill voice caught Rosalind off guard, causing her to flinch in surprise."
    scene w2_1859 with dissolve
    mc "Ah..."
    mc "That's right. It's for a magazine."
    scene w2_1860 with dissolve
    woman "Oh, for real?! Which one?!"
    scene w2_1859 with dissolve
    mct "(Uh...)"

    if minaFlag == True:
        mc "Bandwagon magazine. Have you heard of it?"
        scene w2_1860 with dissolve
        woman "The fashion magazine?"
    else:
        mc "It's for a new fashion magazine..."
        mc "Spearhead! The first issue actually, you wouldn't have heard of it."
        scene w2_1860 with dissolve
        woman "A fashion magazine?"

    scene w2_1861 with dissolve
    woman "Is snake print coming back in style...?"
    "The woman gave my \"model\" a questionable look."
    scene w2_1862 with dissolve
    woman "Ehehe, it's what my mom used to wear."
    rose "..."
    scene w2_1863 with dissolve
    mc "Fashion is cyclical, you know."
    "I said that confidently, like I knew what the fuck I was talking about."
    scene w2_1864 with dissolve
    woman "Cool, yeah!"
    scene w2_1865 with dissolve

    if minaFlag == True:
        mc "Be sure to buy the next issue, okay?"
    else:
        mc "Be sure to buy the first issue if you see it, okay?"

    scene w2_1866 with dissolve
    woman "Hehe, yeah, I'll look for it!"
    woman "Good luck with your shoot!"
    "I guess I can see why Ian does this."
    scene w2_1867 with dissolve
    woman "Bye!"
    rose "Thanks..."
    scene w2_1868 with dissolve
    mc "..."
    rose "..."
    scene w2_1869 with dissolve
    rose "...fashion is cyclical?"
    scene w2_1870 with dissolve
    mc "I've heard that somewhere!"
    scene w2_1871 with dissolve
    rose "Eheh."
    scene w2_1872 with dissolve
    "Rosalind smiled for the first time since we met today."
    scene w2_1869 with dissolve
    rose "So, what's next?"
    scene w2_1870 with dissolve
    stop music fadeout 3.0
    mc "Actually, first, before we continue..."
    mc "I wanted to ask you something."
    scene w2_1869 with dissolve
    rose "Can't it wait until... after {i}this{/i} is finished?"
    scene w2_1873 with dissolve
    mc "No, actually. You being eager to get this over with as quickly as possible might be the only way I'll get you to answer my question."
    scene w2_1874 with dissolve
    play music "music/doll-dancing.ogg"
    "She looked at me dubiously, no doubt unsure where this was going."
    scene w2_1875 with dissolve
    rose "That sounds... mean of you."
    scene w2_1874 with dissolve
    mc "I know, but I am just trying to do my job here. Honestly."
    scene w2_1875 with dissolve
    rose "What's the question?"
    scene w2_1874 with dissolve
    mc "The loan shark that's been hassling you this week..."
    mc "How much do you owe? What are your terms?"
    scene w2_1877 with dissolve
    rose "Why the hell would you need to know that?"
    scene w2_1876 with dissolve
    mc "I heard him say you only had a week left before you had to find another way to pay."
    rose "..."
    mc "I mean, what does that mean? An insurance scam? Prostitution?"
    scene w2_1877 with dissolve
    rose "I don't know... but with the club, it's not like I'm not basically already a prostitute. So why do you care?"
    scene w2_1876 with dissolve
    mc "At the club, I can look after you."
    scene w2_1877 with dissolve
    rose "You believe that?"
    scene w2_1876 with dissolve
    mc "I want to."
    scene w2_1878 with dissolve
    mc "I don't know if I could do it otherwise."
    scene w2_1879 with dissolve
    rose "...you're a selfish kid, [mcf]."
    rose "In a nice way."
    scene w2_1878 with dissolve
    mc "So just tell me what I want to know."
    mc "The creep said you were three weeks behind in your payments?"
    scene w2_1875 with dissolve
    rose "I owe 23,000 dollars. I'm supposed to pay 225 dollars every three days for fifty-one installments, but any missed payment incurs an interest penalty of 2%% on the unpaid balance."
    rose "That works out to be 230 dollars, which means every payment I miss adds an extra one onto what I owe."
    scene w2_1877 with dissolve
    rose "At first I thought it was manageable, but with bills and two mortgages... you quickly find yourself sunk."
    scene w2_1876 with dissolve
    mc "So three weeks of missed payments... that's just a little over 3,100 dollars in payments and interest due."
    scene w2_1880 with dissolve
    mc "Hmm..."
    mct "(That's not an insurmountable number... not something I could personally take on even with my new wage at the club, but...)"
    scene w2_1881 with dissolve
    mc "I'll take care of it."
    scene w2_1882 with dissolve
    mct "(I {i}should{/i} have something like a discretionary fund or an expense account to deal with problems with the girls, right?)"
    mct "(Whatever. I'll make my case to the boss.)"
    rose "...?"
    scene w2_1883 with dissolve
    mc "I'll get the money you owe and get that asshole off your back. You won't have to worry about making payments until the exhibition is over."
    scene w2_1884 with dissolve
    "Rosalind gave me an odd look."
    scene w2_1885 with dissolve
    rose "W-what do you want in return...?"

    if roseFlag == True:
        scene w2_1884 with dissolve
        hide screen textbox2 with dissolve

        menu:
            "Tell her you're doing it as part of your deal."(chg=["rosalind_up"]):
                $ Rosalind_Affection += 1
                scene w2_1886 with dissolve
                show screen textbox2 with dissolve
                mc "Think of it as part of the terms of our deal. Not having that hanging over you should help you win the exhibition."

                if roseDealFullAcceptance == True:
                    scene w2_1887 with dissolve
                    mc "After all, what else could you give me? You already belong to me for the month, right?"
                    scene w2_1888 with dissolve
                    mc "Quid pro quo, right?"
                    scene w2_1889 with dissolve
                    rose "Right, but you haven't really... uh..."
                    scene w2_1888 with dissolve
                    mc "Taken advantage of our deal? There will be time for that."
                    scene w2_1890 with dissolve
                    mc "If it'll make you feel better, maybe I'll have you come by my place after this is finished."
                    scene w2_1891 with dissolve
                    rose "Only say that if you're serious..."
                else:


                    scene w2_1892 with dissolve
                    rose "...I guess that's true."
                    rose "You haven't really... at least not yet..."
                    scene w2_1893 with dissolve
                    mc "Taken advantage of our deal? Would it make you feel better if I did?"
                    scene w2_1894 with dissolve
                    rose "I don't know..."
            "Tell her you're doing it because it's your job.":




                scene w2_1886 with dissolve
                show screen textbox2 with dissolve
                mc "Looking out for you during this month is just part of my job. Don't think much else of it."
                scene w2_1885 with dissolve
                rose "...you haven't taken advantage of our deal."
                scene w2_1886 with dissolve
                mc "Worried I've changed my mind?"
                scene w2_1895 with dissolve
                rose "..."
                scene w2_1886 with dissolve

                if roseDealFullAcceptance == True:
                    mc "Would you feel better if I had you swing by my place after this?"
                else:
                    mc "Would you feel better if I did?"

                scene w2_1896 with dissolve
                mc "You're a funny woman Rose."
    else:


        scene w2_1886 with dissolve
        mc "Looking out for you during this month is just part of my job. Don't think much else of it."
        scene w2_1892 with dissolve
        rose "...thanks."


    stop music fadeout 3.0
    scene w2_1897 with dissolve
    mc "Now..."
    mc "Let's get back to the main event, eh?"
    scene w2_1898 with dissolve
    mc "It looks like you're starting to catch some attention."
    rose "Oh..."
    "A couple of college students had gathered nearby."
    scene w2_1899 with dissolve
    "Rosalind blushed intensely and put herself in a more guarded position."
    "It was funny to think that this was the same woman who was kowtowing at the club, but I understood well what the key difference in location made."

    if kat_polite == True:
        "Come to think of it, this was the kind of reaction that Mrs. Pulman was looking for..."
    else:
        "Come to think of it, this was the kind of reaction that Kathleen was looking for..."

    hide screen textbox2 with dissolve


    menu:
        "Grab a candid shot.":

            play music "music/covert-affair.ogg"
            scene w2_1900 with dissolve
            play sound "sound effects/camera-phone-shutter.wav"
            show screen textbox2 with flash
            "*Click*"
            scene w2_1901 with dissolve
            mc "You shouldn't feel apprehensive. That dress isn't too out there, relatively speaking..."
            scene w2_1922 with pixellate
            mct "(Moo.)"
            scene w2_1901 with pixellate
            mc "You look great."
            scene w2_1902 with dissolve
            rose "That's not really the issue..."
            scene w2_1903 with dissolve
            "The two college students remained nearby, speaking to one another but ever so occasionally stealing a peek in our direction."
            scene w2_1904 with dissolve
            "We were an odd pair for sure. Similar to the last lady, they were probably curious about what we were doing."
            play sound "sound effects/camera-phone-shutter.wav"
            "*Click*" with flash
            scene w2_1905 with dissolve
            rose "This is just because Mrs. Pulman said I have to do this."
            scene w2_1906 with dissolve
            mc "Of course it is. You have to do what you have to do."
            mc "We need to do a good job though. Can you lower your arms?"
            scene w2_1907 with dissolve
            rose "...okay."
            scene w2_1908 with dissolve
            mc "That wasn't so hard, was it?"
            play sound "sound effects/camera-phone-shutter.wav"
            "*Click*"
            "I tried to keep her attention on me and not the surroundings."
            scene w2_1909 with dissolve
            mc "Hm, a little more...?"
            scene w2_1910 with dissolve
            rose "...? Oh, okay..."
            scene w2_1911 with dissolve
            mc "Thank you, Rose. We'll get this over as quickly as possible."
            scene w2_1912 with dissolve
            play sound "sound effects/camera-phone-shutter.wav"
            "*Click*"
            scene w2_1913 with dissolve
            "Another photo; but all of this is pretty damn innocent so far. It's certainly not what the old woman is expecting."
            scene w2_1915 with dissolve
            rose "..."
            scene w2_1914 with dissolve
            rose "I'd like that."
            scene w2_1916 with dissolve
            mct "(They're not even trying to hide their interest in what we're doing anymore.)"
            "Hmm..."
            scene w2_1915 with dissolve
            "While their attention is on us, I could push this further. I bet the boss would be pleased with that direction."
            "Or... I could move this to the tunnel, where I could enjoy Rose's provocations more privately. She would likely appreciate that more."
            "Which direction do I want to take the shoot?"
            hide screen textbox2 with dissolve

            menu:
                "[mod_option] Both":
                    $ mod_week2_rose_park = True
                    $ w2RosalindParkTunnel = True
                    $ w2RoseShootPoints += 2
                    show screen textbox2 with dissolve
                    mct "(It might be embarrassing, but her humiliation here will pay off for her in the next exhibition.)"
                    mc "Spread your legs."
                    scene w2_1917 with dissolve
                    rose "Ah, wha...?"
                    scene w2_1918 with dissolve
                    "The switch from relative geniality to barking a command must've been stark. Her surprise was written on her face."
                    mc "Just let me have a lil' peek."
                    scene w2_1914 with dissolve
                    rose "O-okay..."
                    jump w2RosalindPark
                "Take this back to the tunnel.":

                    $ w2RosalindParkTunnel = True
                    show screen textbox2 with dissolve
                    mct "(Yeah, screw those weirdos.)"
                    mct "(The show is mine to enjoy alone.)"
                    jump w2RosalindTunnel
                "Stay in the park."(chg=["RoseShootPoints_up2"]):


                    $ w2RoseShootPoints += 2
                    show screen textbox2 with dissolve
                    mct "(It might be embarrassing, but her humiliation here will pay off for her in the next exhibition.)"
                    mc "Spread your legs."
                    scene w2_1917 with dissolve
                    rose "Ah, wha...?"
                    scene w2_1918 with dissolve
                    "The switch from relative geniality to barking a command must've been stark. Her surprise was written on her face."
                    mc "Just let me have a lil' peek."
                    scene w2_1914 with dissolve
                    rose "O-okay..."
                    jump w2RosalindPark
        "Tease her some first."(chg=["RoseShootPoints_up"]):




            $ w2RosalindTeased = True
            $ w2RoseShootPoints += 1

            play music "music/covert-affair.ogg"
            scene w2_1901 with dissolve
            show screen textbox2 with dissolve
            mc "What's with that look?"
            mc "An old woman like you is capturing the attention of men half your age. You should be happy."
            scene w2_1919 with dissolve
            "It was mean, but it was why we're here. To photograph Rosalind squirming."
            scene w2_1920 with dissolve
            play sound "sound effects/camera-phone-shutter.wav"
            "*Click*" with flash
            "...this was all to facilitate that, I told myself."
            scene w2_1902 with dissolve
            rose "That's..."
            scene w2_1903 with dissolve
            "The two college students remained nearby, speaking to one another but ever so occasionally stealing a peak in our direction."
            scene w2_1904 with dissolve
            "We were an odd pair for sure. Similar to the last lady, they were probably curious at what we were doing."
            play sound "sound effects/camera-phone-shutter.wav"
            "*Click*"
            scene w2_1905 with dissolve
            rose "Why would anyone be happy about that?"
            scene w2_1906 with dissolve
            mc "Are you actually trying to hide your huge tits? Yeah, right."
            mc "Put your arms down."
            scene w2_1904 with dissolve
            rose "Ah..."
            scene w2_1908 with dissolve
            rose "..."
            "She hesitated, but it wasn't for very long. Just long enough to make a perfunctory display of shame."
            scene w2_1909 with dissolve
            mc "Stick your chest out so I can get a good shot."
            scene w2_1921 with dissolve
            rose "..."
            scene w2_1910 with dissolve
            rose "Okay."
            play sound "sound effects/camera-phone-shutter.wav"
            scene w2_1911 with dissolve
            "*Click*"
            mc "Good girl."
            play sound "sound effects/camera-phone-shutter.wav"
            scene w2_1912 with dissolve
            "*Click*"
            mc "Do you not like having men's eyes on you?"
            scene w2_1914 with dissolve
            rose "Of course I don't..."
            scene w2_1915 with dissolve
            mc "I wonder..."
            scene w2_1916 with dissolve
            mct "(Heh, they're not even trying to hide their interest now.)"
            mct "(Did they hear what I've been saying?)"
            "Hmm..."
            scene w2_1915 with dissolve
            mc "Are you lying? I bet you're dripping wet right now."
            "I could push this further. I bet the boss would be pleased with that direction."
            "Or... I could move this to the tunnel, where I could enjoy Rose's provocations more privately. She would likely appreciate that more."
            "Which direction do I want to take the shoot?"
            hide screen textbox2 with dissolve

            menu:
                "[mod_option] Both":
                    $ mod_week2_rose_park = True
                    $ w2RosalindParkTunnel = True
                    $ w2RoseShootPoints += 2
                    show screen textbox2 with dissolve
                    mct "(It might be embarrassing, but her humiliation here will pay off for her in the next exhibition.)"
                    mc "Spread your legs."
                    scene w2_1917 with dissolve
                    rose "Ah, wha...?"
                    scene w2_1918 with dissolve
                    "The switch from relative geniality to barking a command must've been stark. Her surprise was written on her face."
                    mc "Just let me have a lil' peek."
                    scene w2_1914 with dissolve
                    rose "O-okay..."
                    jump w2RosalindPark
                "Take this to the tunnel.":
                    $ w2RosalindParkTunnel = True
                    show screen textbox2 with dissolve
                    mct "(Nah, fuck those pervs.)"
                    mct "(The show is mine to enjoy alone.)"
                    jump w2RosalindTunnel
                "Stay in the park."(chg=["RoseShootPoints_up"]):

                    $ w2RoseShootPoints += 1
                    show screen textbox2 with dissolve
                    mct "(Let's see how far I can take this.)"
                    scene w2_1918 with dissolve
                    mc "Spread your legs and we'll find out just how much of a horny bitch you are."
                    scene w2_1917 with dissolve
                    rose "*Gulp* D-do we have...?"
                    scene w2_1918 with dissolve
                    mc "This will pay off in the long run, trust me."
                    mct "(Mrs. Pulman did mention this will factor into this week's standings.)"
                    scene w2_1914 with dissolve
                    rose "O-okay..."
                    jump w2RosalindPark


label w2RosalindTunnel:

    scene w2_1923 with dissolve
    mc "It's getting pretty hot."
    mc "Let's find some place with better shade."
    scene w2_1924 with dissolve
    rose "...yeah, okay. I forgot to put sunscreen on today."
    scene w2_1925 with dissolve
    mc "Alley oop!"
    scene w2_1926 with dissolve
    mc "Let's try and make things a little more private."
    rose "...thanks, [mcf]."
    mc "Don't thank me yet."
    mc "We still have to meet Mrs. Pulman's expectations."
    scene black with fade
    rose "I'll take any small mercy."
    stop music fadeout 3.0
    scene w2_1927 with fade
    mc "There, out of sight."
    scene w2_1928 with dissolve
    rose "At least, until someone comes through here..."
    scene w2_1927 with dissolve
    mc "I'll keep a lookout. You just focus on looking like you're about to die of embarrassment."
    scene w2_1928 with dissolve
    rose "I don't think that will be too hard..."
    scene w2_1929 with dissolve
    mc "Strike a few basic poses for me, Rose."
    play music "music/burlesque-heartache.ogg"
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_1930 with flash
    "I had a general idea where I wanted to take this."
    "It's not like it was rocket science."
    mct "(Dr. Chuck would find that funny...)"
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_1931 with flash
    "Surprisingly, Rosalind wasn't as stiff as she was during the group photo shoot."
    "She adjusts to things quickly. Very, very quickly..."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_1932 with flash
    mct "(Perfect for the club. Did the boss know that from beginning?)"
    mct "(It's spooky the way she reads people...)"
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_1933 with flash
    rose "Is that enough...?"
    scene w2_1934 with dissolve
    mc "Yes, good."
    mc "Now I want you to feel yourself up over your clothes."
    scene w2_1935 with dissolve
    rose "Ah..."
    scene w2_1936 with dissolve
    rose "Can't we stop here...?"
    scene w2_1937 with dissolve
    mc "You think this would be enough to satisfy Mrs. Pulman?"
    scene w2_1938 with dissolve
    rose "No. Of course it wouldn't..."
    scene w2_1937 with dissolve
    mc "You're right it wouldn't."
    scene rosaparkrub1_a with dissolve
    show rosaparkrub1
    rose "Like this?"
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*" with flash
    mc "Make it more sexy."
    rose "I don't know how to do that."
    mc "Yes, you do. Don't forget I've seen what you can do."
    rose "..."
    scene rosaparkrub2_a with dissolve
    show rosaparkrub2
    rose "...is this more sexy?"
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*" with flash
    mc "Better, but it is a little cold."
    rose "Isn't that the point? To not be into it?"
    mc "You can look ashamed and horny at the same time."
    rose "I don't think that's going to happen in this sort of situation..."
    mct "(She says that, but I saw how she responded to having her breasts handled during the exhibition.)"
    "She's on a real thin trigger."
    mc "Are you certain of that?"
    scene w2_1939 with dissolve
    "She didn't answer."
    "Instead of simply moving on, I let the silence grow between us and let the moment build."
    "This would go smoother if she let go of her inhibitions a little."
    mc "Look me in the eyes, Rose."
    scene w2_1941 with dissolve
    mc "I know it's scary and I know you don't feel like you have any choice, but..."
    mc "This is also exciting, right? Anyone could walk by."
    scene w2_1940 with dissolve
    rose "N-no, it's not. It's just mortifying."
    scene w2_1941 with dissolve
    mc "It's a nice day out, isn't it? Divorce yourself from your daily life for the next few minutes."
    mc "Just forget all your stress and focus on my voice. Focus on touching yourself."
    scene rosaparkrub2_a with dissolve
    show rosaparkrub2
    mc "Just like you had me do when we worked together at the club. You remember that?"
    rose "Of course..."
    mc "The way you cradled me in your lap and had me suck on your tits..."
    mc "Think back. You tried to conceal it, but you were mortified then too. At the same time, part of you enjoyed it."
    rose "Not rea-"
    mc "Don't lie. You had an orgasm from just your breasts."
    mc "Be honest. Admit it."
    scene rosaparkrub3_a with dissolve
    show rosaparkrub3
    rose "......"
    mc "{b}Admit it{/b}."
    rose "...yes!"
    rose "P-part of me enjoyed holding you in my arms."
    mc "That wasn't the part you enjoyed."
    mc "{b}Get your breasts out{/b}."
    scene w2_1942 with dissolve
    "I raised my voice. Not so loud as to be overly conspicuous from outside the tunnel, but the reverb helped get my point across."
    scene w2_1943 with dissolve
    rose "Y-yes, sir!"
    scene w2RoseParkBoobBounce with dissolve
    "Without even thinking about it, without an ounce of hesitation, she did as I commanded her."
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*" with flash
    scene w2_1950 with dissolve
    rose "H-huh? I just..."
    scene w2_1951 with dissolve
    mc "Holding {b}me{/b} wasn't the part you enjoyed."
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*" with flash

    if w2RosalindTeased == True:
        mc "You liked having your fingers wrapped around my cock and my mouth locked around your lewd and sensitive cow tits."
    else:
        mc "You liked having your fingers wrapped around my cock and my mouth locked around your lewd and overly sensitive breasts."

    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*" with flash
    scene w2_1952 with dissolve
    rose "I.. y-yes! I g-guess..."
    scene w2_1951 with dissolve
    mc "You guess? You're really going to act like you don't remember it that well?"
    scene w2_1967 with dissolve
    mc "Recount it for me then. What was it like being up on that stage?"
    scene w2_1968 with dissolve
    rose "You would know. You were up there with me..."
    scene w2_1967 with dissolve
    mc "I want you to tell me."
    scene w2_1970 with dissolve
    rose "They..."
    rose "They looked like... bugs."
    scene w2_1969 with dissolve
    mc "Bugs? Who did?"
    scene w2_1970 with dissolve
    rose "The men in the audience. Their faces reminded me of bugs."
    scene w2_1969 with dissolve
    mc "Go on..."
    scene w2_1971 with dissolve
    rose "It was unnerving having all them looking up at me."

    if w1ExIntuitionGameWinnerRose == True:
        scene w2_1976 with dissolve
        mc "You got through it, though. You even won."
        scene w2_1972 with dissolve
        rose "I did."
        rose "...because I tuned everyone out and focused entirely on you at that time."
    else:
        scene w2_1967 with dissolve
        mc "You got through it, though."
        scene w2_1968 with dissolve
        rose "Uhuh... one game at a time."
        rose "I got through it by tuning everyone else out and just focusing on you for the first game."

    scene w2_1976 with dissolve
    mc "Am I really any better?"
    scene w2_1971 with dissolve
    rose "Maybe it's because you're so young?"
    if roseFlag == True:
        rose "Maybe it's because of what you promised me. Either way..."
    scene w2_1972 with dissolve
    rose "You don't scare me like others do at least."
    scene w2_1976 with dissolve
    mc "What else do you remember?"
    scene w2_1970 with dissolve
    rose "Honestly it's all a haze..."
    rose "A lot of you touching me and a lot of me touching you..."
    rose "The thing I remember the most is when Mrs. Pulman told us to stop."
    scene w2_1967 with dissolve
    mc "Really?"
    scene w2_1973 with dissolve
    rose "Yeah. There was a big feeling of relief and a lot of shame."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_1975 with flash
    "*Click*"
    scene w2_1974 with dissolve
    mct "(That's the expression that sick bitch is looking for.)"
    scene w2_1967 with dissolve
    mc "Kinda like when you come out of a test you know you did horrible on."
    scene w2_1972 with dissolve
    rose "Heh, I don't think it compares..."
    scene w2_1976 with dissolve
    mc "That's really all you remember?"
    scene w2_1970 with dissolve
    rose "I g-guess..."
    scene w2_1969 with dissolve
    hide screen textbox2 with dissolve
    $ mod_var = False
    menu:
        "[mod_option] Both":
            $ mod_var = True
            jump mod_RosalindTunnel_c_1
        "Physically help jog her memory."(chg=["rosalind_passion_up"]):
            label mod_RosalindTunnel_c_1:
            $ Rosalind_Libido += 1

            scene w2_1953 with dissolve
            show screen textbox2 with dissolve
            rose "What are you--"
            scene w2_1954 with dissolve
            mc "What does it look like?"
            "With a gentle shove, I pressed Rosalind's back against the cool tunnel wall."
            scene w2_1955 with dissolve
            mc "I'm going to help jog your memory of that night.."
            rose "...?"
            mc "Put your hands up."
            scene w2_1956 with dissolve
            "Once more, she did as I asked without any fuss. Her hands darted above her head in a flash, pushing out her chest and making an enticing display of titflesh."
            scene w2_1957 with dissolve
            mc "That didn't take much convincing."
            scene w2_1958 with dissolve
            rose "..."
            play sound "sound effects/camera-phone-shutter.wav"
            "*Click*" with flash
            scene w2_1959 with dissolve
            "One last shot before..."
            scene w2_1960 with dissolve
            rose "A-ah, you s-said you'd be on the lookout!"
            scene w2_1961 with dissolve
            mc "Hands. Up."
            scene w2_1962 with dissolve
            rose "..."
            scene w2_1963 with dissolve
            mc "Keep 'em up."
            scene rosaparksuck1_a with dissolve
            show rosaparksuck1
            rose "A-ah!"
            "\"What are you doing?\" was a very distant thought in the back of my head. It was so far away that it barely even registered."
            "Here I was sucking on Rosalind's tits in the middle of the day, the only thing keeping me from the broad daylight being a small brick tunnel that anyone could access at any moment."
            "Was this normal for me now?"
            rose "I'm f-feeling it already! You made your point, you can-"
            "Her voice came out like a squawk, much louder than she wanted. So loud that..."
            rose "You can s-stop no-!"
            scene w2_1964 with vpunch
            rose "Guh!"
            mc "Someone's going to hear you if you don't shut up, eh?"
            scene rosaparksuck1_a with dissolve
            show rosaparksuck1
            rose "*Whisper* Right! I need to be... ah!"
            "My logic reached her. She lowered her voice to a whisper, as I set hard at work at pleasuring Rosalind's voluptuous bust."
            "It's not like I could take my time here. My goal was to get her primed for the rest of the photos."
            mct "(...right?)"
            "Unlike before, it was my initiative. I sucked contentedly while nudging Rosalind's back into the wall."
            scene rosaparksuck2_a with dissolve
            show rosaparksuck2
            mc "*Fwhup, Chwup...!*"
            rose "So... rough..."
            mc "*Chwup... pheup...!*"
            rose "No, for real... you can stop..."
            scene w2_1965 with dissolve
            rose "Feel...!"
            "She guided my hand below her waist."
            scene w2_1966 with dissolve
            "She wasn't lying. Her panties were damp and warm."
            "If she wasn't already before, she was wet now."
            scene w2_1977 with dissolve
            "Her face told a similar story. It was now a potent mix of unease and sexual want."


            if roseFlag == True:

                "Her breathing had nearly slowed to a standstill..."
                mct "(Those lips...)"
                hide screen textbox2 with dissolve
                menu:
                    "Kiss her."(chg=["rosalind_passion_up"]):
                        $ Rosalind_Libido += 1
                        scene w2_1978 with dissolve
                        show screen textbox2 with dissolve
                        "*...smooch!*"
                        rose "...hmm?"
                        scene w2_1979 with dissolve
                        mc "Sorry, I couldn't resist. It was too tempting."
                        scene w2_1980 with dissolve
                        rose "S-stupid..."
                    "Job finished. Move on.":

                        show screen textbox2 with dissolve
                        "Time's a wasting. We should move on before anyone comes."
            else:
                "Time's a wasting. We should move on before anyone comes."

            scene w2_1981 with dissolve
            mc "Roll up your dress for me, I want to get a shot of your panties."
            scene w2_1982 with dissolve
            rose "O-okay..."
            scene w2_1983 with dissolve
            rose "......"
            scene w2_1984 with dissolve
            rose "...."
            scene w2_1985 with dissolve
            "After making sure the coast was clear, she did as I asked, pulling up her dress and revealing a thin and intricate-looking pair of black lace panties."
            scene w2_1986 with dissolve
            mc "You've got quite the wardrobe at home, huh?"
            play sound "sound effects/camera-phone-shutter.wav"
            "*Click*" with flash
            scene w2_1987 with dissolve
            if mod_var:
                $ mod_var = False
                jump mod_RosalindTunnel_c_2
            mc "Those are--"
        "Have her masturbate for you."(chg=["RoseShootPoints_up"]):



            $ w2RoseShootPoints += 1
            scene w2_1967 with dissolve
            show screen textbox2 with dissolve
            mc "How about we shift gears then."
            scene w2_1968 with dissolve
            rose "What do you mean...?"
            scene w2_1981 with dissolve
            mc "First, I want you to roll up your skirt. Do that for me, Rose."
            mc "Please."
            scene w2_1983 with dissolve
            rose "......"
            scene w2_1984 with dissolve
            rose "...."
            scene w2_1985 with dissolve
            "After making sure the coast was clear, she did as I asked, pulling up her dress and revealing a thin and intricate-looking pair of black lace panties."
            scene w2_1986 with dissolve
            mc "You've got quite the wardrobe at home, huh?"
            play sound "sound effects/camera-phone-shutter.wav"
            "*Click*" with flash
            label mod_RosalindTunnel_c_2:
            mc "Those are... great."
            scene w2_1987 with dissolve
            mc "They don't seem all that old. Not like the dress."
            scene w2_1989 with dissolve
            rose "...my husband got them for my birthday a few years ago."
            scene w2_1988 with dissolve
            mc "So he's the kind of prick who gets his wife lingerie for her birthday?"
            mc "Makes sense. What a selfish asshole."
            scene w2_1990 with dissolve
            rose "Terrible gifts were the least of his issues."
            play sound "sound effects/camera-phone-shutter.wav"
            scene w2_1991 with flash
            "*Click*"
            "Something about the conflicted look on her face... I had to steal a quick shot of it."
            scene w2_1993 with dissolve
            rose "You said \"first\". So what do you want me to do next?"
            scene w2_1992 with dissolve
            mc "Ah, right. Next I want you to touch yourself over your panties."
            scene rosaparkrub4_a with dissolve
            rose "...okay."
            play sound "sound effects/camera-phone-shutter.wav"
            "*Click*" with flash
            mc "Slowly rub yourself. Don't stop."
            rose "O-okay."
            scene rosaparkrub4_a with dissolve
            show rosaparkrub4
            "Obedient."
            play sound "sound effects/camera-phone-shutter.wav"
            "*Click*" with flash
            "That was a good way to describe Rosalind in this moment. Or perhaps more generously, she had a real knack for pushing past her discomfort."
            play sound "sound effects/camera-phone-shutter.wav"
            scene rosaparkrub5_a with flash
            show rosaparkrub5
            "*Click*"
            rose "A-are you paying attention? No one's coming, right?"
            mc "No, we're good."
            play sound "sound effects/camera-phone-shutter.wav"
            "*Click*"
            scene rosaparkrub4_a with dissolve
            show rosaparkrub4
            "Rosalind slid her delicate fingers across her slit, all the while I made sure to get as many good shots as possible."
            play sound "sound effects/camera-phone-shutter.wav"
            "*Click*"
            "It wasn't very hard for me to put aside my anxiety about this, was it?"
            "Once I had Rosalind in front of me, going along with things, I was quickly swept up by an intoxicating feeling."
            play sound "sound effects/camera-phone-shutter.wav"
            "*Click*"
            scene rosaparkrub5_a with dissolve
            show rosaparkrub5
            rose "D-don't you think you got enough pictures of that?"
            "The real answer was I could take a million pictures and still want to take more, but..."
            hide screen textbox2 with dissolve

            menu:
                "Have her pull aside her panties.":
                    show screen textbox2 with dissolve
                    mc "Almost. Pull aside your panties."
                    scene w2_1994 with dissolve
                    rose "...*sigh* Okay."
                    scene w2_1995 with dissolve
                    "*Click*"
                    "With a simple motion, she peeled back the slightly damp lingerie and exposed herself to the camera."
                    "It was a pretty sight by itself, but coupled with that complicated look on her face..."
                    scene w2_1996 with dissolve
                    "*Click*"
                    "Our patrons should find this satisfactory."
                    mc "Okay, next--"
                "Move onto something else.":


                    scene w2_1997 with dissolve
                    show screen textbox2 with dissolve
                    mc "Yeah, I think we should move on."
                    scene w2_1998 with dissolve
                    rose "What's next?"
                    scene w2_1997 with dissolve
                    mc "That's a good question..."
                    scene w2_1999 with dissolve
                    mct "(Should we move someplace else? We might be tempting fate by staying--)"



    stop music
    play sound "sound effects/soccer-bounce.wav"
    scene parkballbounceAZ
    show parkballbounce with dissolve
    mct "(Shit! Fuck!)"
    man "Nice kick, dumbass!"
    scene w2_2000 with vpunch
    mc "Shit, move...!"
    $ renpy.end_replay()
    if not persistent.roseW2ParkSceneGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.roseW2ParkSceneGallery = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    "......!"
    "...!"
    jump w2RosalindParkBathroom

label w2RosalindPark:

    scene w2_2001 with dissolve
    mc "Uncross your legs real quick."
    scene w2_1914 with dissolve
    rose "Uh, but..."
    scene w2_1915 with dissolve
    "She looked apprehensively at the curious college students that couldn't keep their eyes off of us."
    scene w2_2001 with dissolve
    "I gave her a nod to emphasize I knew the implication of what I was asking."
    mc "The audience you had last Saturday night was a lot worse, right? Don't think too hard about it."
    scene w2_2002 with dissolve
    "She paused and seemed to genuinely consider that perspective and with a smile..."
    scene w2_2003 with dissolve
    hide screen textbox2 with dissolve
    "Uncrossed her legs and revealed an eye-catching gap that exposed a dark pair of lace panties."
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*" with flash
    "I'm sure if they're not already looking, the sound of the mechanical shutter surely captured their attention."
    scene w2_2004 with dissolve
    ustud "What... you think..."
    ustud2 "shot...?"
    mc "(Heh, bingo.)"
    scene w2_2003 with dissolve
    "Rosalind was keenly aware of their glances and it showed on her face."
    scene w2_2005 with dissolve
    mc "Lean forward for me, please."
    scene w2_2006 with dissolve
    rose "Sure..."
    scene w2_2007 with dissolve
    "Catching on immediately, she bent forward and pretended to scratch her leg. Giving her plausible deniability, while anyone who was looking got a topside view of her breasts."
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*"
    "This was all well inside the realm of acceptability so far. Her attire was inappropriate for the setting, but we weren't doing anything criminal."
    scene w2_2008 with dissolve
    ustud2 "Let's... eat..."
    ustud "I... find... going on..."
    ustud2 "...starving!"
    scene w2_2009 with dissolve
    "Rosalind was being amenable, but where was the line?"
    "...and just how long are those two dweebs going to hover around?"
    scene w2_2010 with dissolve
    mc "You look like you need to stretch your arms a little."
    scene w2_2011 with dissolve
    rose "...hmm, yeah. I guess I do..."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_2012 with dissolve
    "*Click*"
    "Rosalind took a deep breath, leaned back, and threw out her chest in an exaggerated fashion that drew attention to her goods."
    scene w2_2013 with dissolve
    rose "Ayaaa...!"
    "She even yawned for added effect."
    scene w2_2014 with dissolve
    rose "Ah, thank god..."
    scene w2_2015 with dissolve
    "To my surprise, when I next looked, the boys were walking away."
    "Probably off to eat, if the bits I picked up from the conversation were to be believed."
    "In the end, they probably just thought Rosalind was a model."
    scene w2_2016 with dissolve
    mc "Heh. Looks like no one's looking now."
    scene w2_2017 with dissolve
    rose "There's still one person here..."
    scene w2_2018 with dissolve
    "Rosalind gestured to an old man sitting placidly on a bench."
    "For a second, I wondered if he was even alive. He sat motionless on the bench, head pointed straight ahead and eyes locked shut."
    "The only indication that he was indeed breathing, was a genial smile that stretched across his face. He was evidently content to bask in the warmth of the early midday sun."
    mct "(Hmm... if he's not looking...)"
    scene w2_2019 with dissolve
    "I gestured at my chest and pantomimed my expectations."
    mc "He's not looking."
    scene w2_2020 with dissolve
    rose "Uh... o-oh!"
    "The moment she caught on, her face turned a beet red!"
    scene w2_2021 with dissolve
    rose "There's no way... I c-couldn't!"
    mc "It's just us and that old man and he might be asleep. Mrs. Pulman isn't going to be happy with what we've got so far."
    scene w2_2022 with dissolve
    rose "I know..."
    scene w2_2023 with dissolve
    mc "Plus, I don't know in what way, but she told me these shoots will impact your standing in this week's exhibition."
    scene w2_2024 with dissolve
    rose "Wait, really?"
    rose "You should've told me that sooner..."
    scene w2_2025 with dissolve
    "That seemed to get the gears turning in her head."
    scene w2_2026 with dissolve
    rose "Ah... he really isn't looking, huh?"
    scene w2_2025 with dissolve
    mc "No, he's not, but someone might come any second."
    scene w2_2027 with dissolve
    rose "O-okay, just get the photo quick!"
    hide screen textbox2 with dissolve
    scene w2RoseParkBoobBounce2 with dissolve
    "Without another second of delay, the determined mother grabbed the top of her dress and give it a firm yank to expose herself."
    mct "(Ah... holy shit!)"
    "I had told her to do it, but that was just words. Now the feeling of being out in the open finally hit me."
    scene w2_2039 with dissolve
    rose "Hurry up!"
    scene w2_2038 with dissolve

    if toughness >= 22:
        mc "Sorry, I was just enjoying the view."
    else:
        mc "S-shit, right!"

    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*"
    mc "Cup them real quick."
    scene w2_2040 with dissolve
    rose "...fine."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_2041 with dissolve
    "*Click*"
    scene w2_2042 with dissolve
    rose "Ah..."
    scene w2_2043 with dissolve
    "The next pose she did out of her own initiative."
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*"
    "She was playing to win."
    mc "Okay that's enough."
    scene w2_2044 with dissolve
    show screen textbox2 with dissolve
    rose "Ohmygod...!"
    "As soon as she had made herself presentable, a petrified look had caught up with her and was making its home on her face."
    scene w2_2045 with dissolve
    rose "Oh... ha... jeez..."
    "She took a second to collect herself, before..."
    scene w2_2046 with dissolve
    rose "That's not enough, is it?"
    scene w2_2047 with dissolve
    "Taking the initiative once more."
    scene w2_2048 with dissolve
    rose "Quick!"
    mc "Yes, ma'am."
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*"
    scene w2_2049 with dissolve
    "The old man was still looking straight ahead."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_2050 with dissolve
    "Quickly, she rattled off a sequence of self-driven poses."
    "The next gave a clear shot of an expensive-looking piece of black lingerie."
    mct "(She has something like that in her wardrobe, huh?)"
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_2051 with dissolve
    mc "Good, good..."
    mc "I think this should be--"
    scene w2_2052 with dissolve
    rose "I... I think we need to do something more exciting. She really said this will affect this week's contest?"
    scene w2_2053 with dissolve
    mc "Something to that effect, yes."
    rose "...then I need to do something to stand out against the other Carnations."
    scene w2_2054 with dissolve
    rose "Follow me."
    scene w2_2055 with dissolve
    "She seems to have a concrete idea in mind. I could let her pull me along and see how this pans out."
    "If she's talking about standing out, it's probably a bold one."
    "However, I could...."
    hide screen textbox2 with dissolve
    menu:
        "Have her flirt with the old man.":

            scene w2_2056 with dissolve
            show screen textbox2 with dissolve
            mc "Why don't you go flirt with that old man a little bit?"
            scene w2_2057 with dissolve
            rose "W-what?! No way!"
            rose "I couldn't do that."
            scene w2_2058 with dissolve
            mc "Why not? He's probably harmless and you'll likely make his day."
            scene w2_2059 with dissolve
            rose "That's not the issue! It's too embarrassing!"
            rose "Besides, I don't know how to flirt."

            if roseSeduceFlag == True:
                scene w2_2060 with dissolve
                mc "That wasn't the case when you tried to seduce me."
                scene w2_2061 with dissolve
                rose "Eh...? That... I mean... You're a..."
                scene w2_2060 with dissolve
                mc "I'm a what?"
                scene w2_2061 with dissolve
                rose "You're just a kid."
                scene w2_2060 with dissolve
                mc "I'm twenty-two."
                scene w2_2061 with dissolve
                rose "You know what I mean."
                scene w2_2060 with dissolve
                mc "Don't you think you're taking me too lightly?"
                scene w2_2062 with dissolve
                rose "S-sorry, Mr. [mcl]."
                scene w2_2063 with dissolve
                mc "*Sigh* Anyway..."

            scene w2_2064 with dissolve
            mc "You're a beautiful woman and he's an old man. I don't think it'll be too hard to catch his interest."
            scene w2_2061 with dissolve
            rose "Like I said, it's embarrassing..."
            scene w2_2060 with dissolve
            mc "You just flashed me out in public. Striking up a conversation and touching an arm isn't nearly as extreme..."
            scene w2_2061 with dissolve
            rose "That was... no one was looking. He's going to think I'm a prostitute."
            scene w2_2062 with dissolve
            rose "I'm dressed like one..."
            rose "Can't we please just go somewhere more private?"
            scene w2_2063 with dissolve
            "She was giving me an unusual amount of pushback here. What do I say?"
            stop music fadeout 3.0
            hide screen textbox2 with dissolve

            menu:
                "Reason with her."(chg=["RoseShootPoints_up"]):
                    $ w2RoseShootPoints += 1
                    $ w2RosalindParkOldman = True
                    scene w2_2064 with dissolve
                    show screen textbox2 with dissolve
                    mc "Veronica and Felicia won't get a chance like this in their shoots."
                    scene w2_2065 with dissolve
                    rose "....ah."
                    scene w2_2066 with dissolve
                    rose "I'm being silly. What exactly would you have me do, though...?"
                    jump w2RosalindParkOldman
                "Agree to drop the idea.":


                    scene w2_2064 with dissolve
                    show screen textbox2 with dissolve
                    mc "Ah, fine. You're being unusually steadfast today. We'll do what you originally had in mind."
                    scene w2_2066 with dissolve
                    rose "Thank you."
                    scene w2_2067 with dissolve
                    mc "Lead the way."
                    $ renpy.end_replay()
                    if not persistent.roseW2ParkSceneGallery:
                        play sound "sound effects/notification.wav"
                        show memoryunlock with dissolve
                        $ renpy.pause(3, hard=True)
                        $ persistent.roseW2ParkSceneGallery = True
                        hide memoryunlock with dissolve
                        $ renpy.pause(0.5, hard=True)
                    show screen textbox2 with dissolve
                    scene w2_1926 with dissolve
                    "......"
                    if mod_week2_rose_park:
                        jump w2RosalindTunnel
                    "..."
                    jump w2RosalindParkBathroom
        "Let her lead the way.":

            scene w2_2064 with dissolve
            mc "You're being unusually tenacious. Lead the way."
            scene w2_2067 with dissolve
            "She gave me a nod in solidarity, before dragging me off toward the tunnel."
            scene w2_1926 with dissolve
            stop music fadeout 3.0
            $ renpy.end_replay()
            if not persistent.roseW2ParkSceneGallery:
                play sound "sound effects/notification.wav"
                show memoryunlock with dissolve
                $ renpy.pause(3, hard=True)
                $ persistent.roseW2ParkSceneGallery = True
                hide memoryunlock with dissolve
                $ renpy.pause(0.5, hard=True)
            show screen textbox2 with dissolve
            "......"
            if mod_week2_rose_park:
                jump w2RosalindTunnel
            "..."
            jump w2RosalindParkBathroom




label w2RosalindParkOldman:

    scene w2_2075 with dissolve
    mc "Nothing extreme. Go talk to the man, touch his arm, show some skin..."
    scene w2_2076 with dissolve
    rose "I can try."
    scene w2_2077 with dissolve
    mc "You can do it. I know you can."
    scene w2_2078 with dissolve
    mc "Here's the plan though. Since I have to get photos of it, I'm going to walk off, wait a few minutes, and find an inconspicuous spot off to the side to take them."
    mc "In five minutes, I want you to approach him and sit down. Hopefully he won't have left by then."
    scene w2_2076 with dissolve
    rose "I can... do that. I think."
    scene w2_2075 with dissolve
    mc "Hey, push comes to shove... you can just walk away if you need to."
    scene w2_2079 with dissolve
    "She gave me one last uneasy smile..."
    scene black with fade
    "......"
    "..."
    scene w2_2080 with bites
    "After getting in place, I waited and watched for Rosalind to approach."
    "The clanking of her heels were a dead giveaway of her approach, but still the man didn't stir."
    scene w2_2081 with fade
    play music "music/dog-park.ogg"
    rose "......"
    rose "..."
    scene w2_2082 with dissolve
    rose "Uh..."
    scene w2_2083 with dissolve
    om "It's a nice day."
    scene w2_2084 with dissolve
    rose "Wha- y-yeah it is, isn't it? Heh..."
    scene w2_2085 with dissolve
    om "......"
    scene w2_2086 with dissolve
    om "...did you just get off work?"
    scene w2_2087 with dissolve
    rose "No, not... really. Why do you ask?"
    scene w2_2088 with dissolve
    om "The way you're dressed. You look like you might've just left a cigar lounge."
    scene w2_2084 with dissolve
    rose "Those don't exist anymore, sir."
    scene w2_2083 with dissolve
    om "They don't? What happened to them?"
    scene w2_2090 with dissolve
    rose "The city did away with smoking indoors like a decade ago."
    scene w2_2089 with dissolve
    om "Is that right? How sad."
    scene w2_2090 with dissolve
    rose "Do you smoke?"
    scene w2_2091 with dissolve
    om "Me? No. That stuff will kill you!"
    scene w2_2092 with dissolve
    rose "Pfft, haha...! Was that sad look a joke then?"
    scene w2_2093 with dissolve
    om "No, of course not! I just think a man should have a say if people can smoke on his property."
    scene w2_2094 with dissolve
    rose "Hehehe...!"
    rose "You're funny..."
    scene w2_2095 with dissolve
    om "So if you're not off the clock, does that mean you're currently working?"
    scene w2_2096 with dissolve
    rose "...? O-oh! You mean, are you asking if I'm a..."
    scene w2_2095 with dissolve
    om "Working girl."
    scene w2_2097 with dissolve
    rose "No, of course no- ah, actually..."
    rose "I guess I kind of am, in some way. How did you know?"
    scene w2_2098 with dissolve
    om "A beautiful woman like you doesn't approach an old man like me for no reason."
    om "No offense, but uh... I'm a little too old for that sort of thing."
    scene w2_2099 with dissolve
    rose "You've got it all wrong. I really did just want to sit down."
    rose "It's a nice day."
    scene w2_2100 with dissolve
    om "It is, isn't it?"
    scene w2_2101 with dissolve
    om "..."
    rose "..."
    scene w2_2102 with dissolve
    om "A day like this is enough to forget your troubles, but you seem nervous. Are you okay?"
    scene w2_2103 with dissolve
    rose "Ah, that's a big question... but it's a simple answer. Life isn't going so great for me right now."
    scene w2_2102 with dissolve
    om "I'm sorry to hear that, Miss. If it's any comfort, I'm in the same boat."
    scene w2_2103 with dissolve
    rose "Really? What's wrong?"
    scene w2_2104 with dissolve
    om "What isn't wrong? I'm an old man. I'm told the perspective you gain as you grow old helps you accept the inevitable, but that's a load of crap."
    om "My body aches, my wife died last year, my list of friends grows shorter every year..."
    scene w2_2103 with dissolve
    rose "That doesn't give me any comfort. How long were you married?"
    scene w2_2102 with dissolve
    om "Fourty-three short years. That must seem like a lifetime to you. What are you, twenty-eight?"
    scene w2_2105 with dissolve
    rose "Oh, shut up! I thought you said you were too old for that sort of thing. Now, you're hitting on me."
    om "I'm not! That's a genuine guess."
    scene w2_2106 with dissolve
    rose "I'm thirty-six!"
    scene w2_2098 with dissolve
    om "Hehe, that doesn't seem too far off to me. I'm seventy-one."
    scene w2_2099 with dissolve
    rose "Seventy-one? You still got a lot of life left in you."
    scene w2_2100 with dissolve
    om "I hope so. I'd like to see my grandkids grow up before I die."
    scene w2_2099 with dissolve
    rose "You're a grandfather?"
    scene w2_2088 with dissolve
    om "All the comfort and happiness a child can bring, but with none of the fuss. They're the light of my life."
    om "Do you have any children?"
    scene w2_2090 with dissolve
    rose "I do. I have a daughter. What about you?"
    scene w2_2083 with dissolve
    om "How old is she?"
    scene w2_2090 with dissolve
    rose "Thirteen."
    scene w2_2089 with dissolve
    om "Difficult age."
    scene w2_2090 with dissolve
    rose "It's all a difficult age as far as I can tell, but it's..."
    rose "It's worth it."
    scene w2_2088 with dissolve
    om "Well said."
    scene w2_2107 with dissolve
    rose "..."
    scene w2_2102 with dissolve
    om "It's those kind of troubles, eh? Your mind went straight back to them with the mention of your daughter."
    scene w2_2103 with dissolve
    rose "Yeah, it is. Partly."
    scene w2_2104 with dissolve
    om "Do you want to go into details? I'm a good listener."
    scene w2_2103 with dissolve
    rose "The details are too complicated and embarrassing."
    scene w2_2102 with dissolve
    om "I understand. Still if I could hazard a guess, I think you'll be okay."
    scene w2_2103 with dissolve
    rose "Why would you say that?"
    scene w2_2108 with dissolve
    om "I can tell by your voice you clearly love your child. Whatever's going on between you and her and the outside world, you'll make it through."
    scene w2_2109 with dissolve
    rose "Love conquers all?"
    scene w2_2108 with dissolve
    om "Nah, that's trite nonsense cooked up by greeting card companies."
    scene w2_2109 with dissolve
    rose "I think that saying might go back further than that..."
    scene w2_2108 with dissolve
    om "That doesn't mattter. What I'm trying to say is, when your troubles are in your rearview mirror, the fondness you felt will be what you remember. You just have to persevere."
    scene w2_2110 with dissolve
    rose "......"
    scene w2_2111 with dissolve
    rose "..."
    scene w2_2112 with dissolve
    rose "Heh... do you normally dispense advice from this park bench?"
    scene w2_2113 with dissolve
    om "If you're inquiring about my office hours, you should seek out a professional quack."
    om "I'm just an old man warming his feet."
    scene w2_2114 with dissolve
    rose "..."
    scene w2_2115 with dissolve
    rose "I... I should go."
    scene w2_2116 with dissolve
    om "It was nice talking to you, Miss."
    scene w2_2117 with dissolve
    rose "My name's Rosalind."
    scene w2_2118 with dissolve
    om "It's nice talking to you, Rosalind."
    scene w2_2119 with dissolve
    rose "Hey, old man?"
    scene w2_2120 with dissolve
    scene w2_2121 with dissolve
    om "Yeah?"
    hide screen textbox2 with dissolve
    stop music
    play sound "sound effects/record-scratch.wav"
    scene w2_2122 with vpunch
    rose "Thanks for talking to me."
    om "G-gah! Wha...!"
    scene w2_2123 with cmet
    show screen textbox2 with dissolve
    play sound "sound effects/high-heel-footsteps-fast.wav"
    om "You tryin' to kill me?!"
    stop sound fadeout 2.0
    scene w2_2124 with dissolve
    om "Hehe..."
    om "It really is a nice summer day."
    scene w2_2125 with dissolve
    mct "(Ah, shit. I only got a few pictures, but damn...!)"
    mct "(I wasn't expecting her to do that.)"
    mct "(I should probably follow her.)"
    $ renpy.end_replay()
    if not persistent.roseW2ParkSceneGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.roseW2ParkSceneGallery = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    show screen textbox2 with dissolve
    "......"
    if mod_week2_rose_park:
        jump w2RosalindTunnel
    "..."
    jump w2RosalindParkBathroom

label w2RosalindParkBathroom:


    if _in_replay:
        show transitionrosalind02 with cmet
        show screen textbox2 with dissolve
        "Please set [mcf]'s personality (toughness score) for this replay."
        hide screen textbox2 with dissolve
        menu:
            "Nice guy (Toughness: 0)":
                $ toughness = 0
            "Mischevious (Toughness: 18)":
                $ toughness = 18
            "Asshole (Toughness: 30)":
                $ toughness = 30
        show screen textbox2 with dissolve
        "Did Rosalind talk to the man in the park?"
        hide screen textbox2 with dissolve
        menu:
            "Yes.":
                pass
            "No.":
                $ w2RosalindParkTunnel = True
                pass
        show screen textbox2 with dissolve

    if w2RosalindParkTunnel == True:
        play music "music/guiton-sketch.ogg"
        scene w2_2126 with sunshine
        mc "I think we're good, we can stop h-here--"
        rose "We're finishing the shoot in here!"
        stop ambient
        scene w2_2127 with blinds
        rose "Ha...! Fuck!"
        rose "That scared the SHIT out of me! Thank god there's no one in here."
        rose "I don't know if my heart could've taken it if I ran into a couple of guys peeing."
        scene w2_2128 with dissolve
        mc "Heh..."
        scene w2_2129 with dissolve
        rose "Haha...!"
        mc "Okay, I'll admit, that scared the shit out of me too. My chest is still pounding."
        rose "Hehehe...! Ah, I can't believe I just did something like that."
        scene w2_2130 with dissolve
        mc "Can't you?"
        rose "Heh. Yeah, you're right."
        scene w2_2131 with dissolve
        rose "This whole past month has been that feeling."
        scene w2_2132 with dissolve
        rose "*Sigh* What is happening to my life?"
        scene w2_2133 with dissolve
        "She took a brief moment to reflect, asking herself that question in an acerbically derisive way."
        scene w2_2134 with dissolve
        rose "Still, we've got a job to do."
        scene w2_2135 with dissolve
        mc "You don't think we got enough photos?"
        scene w2_2134 with dissolve
        rose "It can't hurt to take some more. I need to be better than Veronica and Felicia."
        scene w2_2135 with dissolve
        mc "You were just scared to death and now you're all business. You're remarkable at compartmentalizing."
        scene w2_2136 with dissolve
        rose "Yeah, okay. I'll add that to my résumé."
        scene w2_2135 with dissolve
        "A sudden shift in candor..."
        mc "Eye on the prize, huh? Yeah, we can take some photos in here if you want."
        scene w2_2137 with dissolve
        rose "More than that, I'm going to need your help."
    else:

        stop ambient fadeout 3.0
        play music "music/guiton-sketch.ogg"
        scene w2_2138 with sunshine
        mc "Where are we going? The bathroom...?"
        if w2RoseParkOldman == True:
            "After catching up to her, Rosalind forcefully grabbed me by the hand and marched me toward a nearby public restroom."
        else:
            "Along the way, Rosalind forcefully grabbed me by the hand and marched me like a child toward a nearby public restroom."
        rose "You and I can get \"bolder\" in here."
        mct "(Bolder? She really does have a plan...)"
        scene w2_2139 with blinds
        "Wasn't this supposed to be my show?"
        scene w2_2140 with dissolve
        rose "Good. No one's in here."
        scene w2_2141 with dissolve
        mc "What would you have done if there was?"
        scene w2_2142 with dissolve
        rose "Pretended to go, I guess."
        scene w2_2135 with dissolve
        "Rosalind suddenly had a peculiar nonchalance about her. All morning she had been timid, but now..."
        mc "What did you mean by bolder?"
        scene w2_2134 with dissolve
        rose "I meant we still have a job to do."
        scene w2_2135 with dissolve
        mc "You don't think we got enough photos?"
        if w2RoseParkOldman == True:
            scene w2_2131 with dissolve
            rose "No, that nice man didn't give you much did he?"
            scene w2_2135 with dissolve
            mc "No, I guess not."
            scene w2_2134 with dissolve
            rose "Exactly. We need to take some more photos"
        else:
            scene w2_2136 with dissolve
            rose "Of course we don't. But even if we did..."
            scene w2_2134 with dissolve
            rose "More can't hurt."

        rose "I need to be better than Veronica and Felicia."
        scene w2_2135 with dissolve
        mc "What did you have in mind?"
        scene w2_2137 with dissolve
        rose "Something I'll need your help with."


    scene w2_2143 with dissolve
    "With an abrupt shove, she scooted me deeper into the bathroom, toward the single stall."
    "I'd seen Rosalind's unceasing drive in action before, with the way she bore the brunt of the club's humiliations, but this was a whole other flavor."
    "She was being pushy and stealing the initiative."
    mc "What's the..."
    scene w2_2144 with dissolve
    play sound "sound effects/door-open.wav"
    "*Click*"
    play sound "sound effects/door-open.wav"
    "*Fwhlick* Click*"
    scene w2_2145 with dissolve
    mc "What's the plan...?"
    scene w2_2146 with dissolve
    rose "Be sure to take a lot of good pictures."
    scene w2_2145 with dissolve
    mc "Sure, but again, what's the--"
    scene w2_2147 with dissolve
    "Ignoring my question, Rosalind worked her panties past her plump hips and down her beautifully toned legs, before sitting down on the toilet."
    scene w2_2148 with dissolve
    rose "This is very, very embarrassing, but I need you to get some photos of me tinkling."
    scene w2_2149 with dissolve
    mc "That's your plan?"
    scene w2_2148 with dissolve
    rose "No, but I actually do have to go, so might as well make the most of it..."
    scene w2_2149 with dissolve
    mc "Shit, okay..."
    scene w2_2150 with dissolve
    play ambient "sound effects/urine-ground.wav"
    rose "Ah..."
    "After a moment to get things rolling, finally the telltale \"plap\" of urine hitting water filled the tiny room."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_2151 with flash
    "*Click*"
    "She looked truly shamed. THAT was what the old lady was looking for and Rosalind had found it herself."
    mc "It can't be that embarrassing, can it?"
    mct "(You jerked my dick in front of a crowd full of people, I mean...)"
    scene w2_2152 with dissolve
    rose "It is..."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_2151 with dissolve
    "*Click*"
    scene w2_2152 with dissolve
    rose "You want to try and see how it feels? You can go when I'm finished."
    scene w2_2153 with dissolve
    mc "I went before I left home..."
    scene w2_2154 with dissolve
    rose "Heh, that's what I thought."
    scene w2_2155 with dissolve
    stop ambient fadeout 3.0
    "Finally the sound trickled into nothing."
    scene w2_2147 with dissolve
    mc "So... what next?"
    rose "Sit down and get your penis out."
    mc "...eh?"
    scene w2_2156 with dissolve
    rose "Sit down and get your penis out, {b}please{/b}?"
    scene black with fade
    "A simple shrug was my answer to the resolute Rosalind."
    "I quickly kicked off my pants and did what I was bidden."
    scene w2_2157 with dissolve
    rose "It's half way there already..."
    scene w2_2158 with dissolve
    mc "Yeah. You want to work on the other half?"
    scene w2_2159 with dissolve
    rose "Picture."
    scene w2_2160 with dissolve
    "She peered at me with upcast, demanding eyes."
    scene w2_2161 with dissolve
    mct "(Right. This is work.)"
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*"
    scene w2_2162 with dissolve
    rose "Let's get you standing at full attention."
    scene w2_2163 with dissolve
    scene w2_2164 with dissolve
    scene w2_2165 with dissolve
    "In a smooth, business like motion she gobbled up my cock and took it deep into her mouth."
    "My glans slid pleasantly across her tongue into the deep recesses of her mouth, all the way until it brushed against her tonsils and uvula."
    "There she simply held it, allowing me to enjoy the warm comfort of her mouth while my cock engorged itself further with blood."
    mct "(I should get a picture.)"
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*"
    scene w2_2166 with dissolve
    rose "*Cough* Ack--ha...!"
    scene w2_2167 with dissolve
    scene w2_2168 with dissolve
    scene w2_2169 with dissolve
    rose "Ah!"
    scene w2_2170 with dissolve
    rose "Ack, sorry... I thought I could, but I'm still not used to taking it that deep."
    scene w2_2171 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Tell her she doesn't have to push herself."(chg=["rosalind_up"]):
            $ Rosalind_Affection += 1
            scene w2_2172 with dissolve
            show screen textbox2 with dissolve
            mc "You don't have to push yourself hard. We're just taking some photos here."
            scene w2_2173 with dissolve
            rose "I do. I absolutely do."
            rose "I appreciate your kindness, but... I've got to keep in the right mindset."
            scene w2_2172 with dissolve
            mc "Do as you wish then."
        "Tell her she'll be a pro by the end of this month.":


            scene w2_2172 with dissolve
            show screen textbox2 with dissolve
            mc "Heh, well you'll likely be a pro by the end of this month."
            scene w2_2173 with dissolve
            rose "Yeah, lucky me."
        "Tell her you don't mind a little gagging."(chg=["rosalind_passion_up"]):

            $ Rosalind_Libido += 1
            scene w2_2172 with dissolve
            show screen textbox2 with dissolve
            $ w2RoseGag = True
            mc "Don't worry. Some guys love a gag reflex."
            scene w2_2173 with dissolve
            rose "I'm not worried."


    scene w2_2174 with dissolve
    hide screen textbox2 with dissolve
    rose "You're good and hard now, right?"
    "I nodded."
    scene w2_2183 with dissolve
    rose "Picture."
    scene w2_2175 with dissolve
    "In an obscene gesture, she lightly wrapped her fingers around the circumference of my cock and nudged the head against her cheek in a humiliating gesture of mock supplication."
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*"
    mc "Is that all?"
    scene w2_2176 with dissolve
    scene w2_2177 with dissolve
    scene w2_2178 with dissolve
    "She gave me one hell of a sultry look before vigorously shaking her head no."
    scene w2_2179 with dissolve
    rose "Not until you give me what's in here and you get a photo."
    rose "Then we're done."
    scene w2_2180 with dissolve
    "Without waiting for me to reply, she wedged my cock deep into the valley of her gargantuan breasts."
    scene w2_2181 with dissolve
    mc "You're going to use those...?"
    if w1GonzoReward == True:
        mct "(Come to think of it, this is just the second time I've ever gotten a titjob before. The boss' \"reward\" was a bit overwhelming to properly enjoy it...)"
    else:
        mct "(Come to think of it, I've never gotten a titjob before. This is a first for me...)"
    scene w2_2182 with dissolve
    rose "I thought I'd give it a try."
    scene w2_2181 with dissolve
    mc "Carry on then."
    scene w2_2182 with dissolve
    rose "Sure, but you better remember to get some shots of this."
    hide screen textbox2 with dissolve
    scene toiletrosapai1_a with dissolve
    show toiletrosapai1
    "With no added fanfare, Rosalind pressed her tits tightly together and gently submerged my dick further into her cleavage."
    "I was amazed at how easily my cock fully disappeared into the pleasant expanse of the desperate mother's titflesh."
    "Instead of working my cock with the top and bottom of her breasts..."
    mc "It's like I'm penetrating your chest."
    rose "They do call it a..."
    scene toiletrosapai2_a with dissolve
    show toiletrosapai2
    "She paused for a moment, as if finding the words."
    rose "They do call it a \"titfuck\" right?"
    "The look on her face was cute, completely incongruent with the act she was performing."
    mc "You're really pushing yourself hard."
    rose "Picture."
    scene w2_2184 with dissolve
    mc "Right."
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*"
    mc "You really going to go all the way until I ejaculate?"
    scene toiletrosapai1_a with dissolve
    show toiletrosapai1
    rose "Yep. Like I said, I'm going to win this stupid game."
    rose "I shouldn't complain though, should I? These awful games of hers are how I'm going to dig myself out of the hole I'm in."
    "I was reminded of that bastard from earlier."
    mc "You don't feel like you're about to suffocate?"
    rose "Stop talking. Just focus on your part in this."
    rose "--cumming."
    scene toiletrosapai2_a with dissolve
    show toiletrosapai4
    "She was telling me to hurry, and to emphasize the point, she picked up the pace herself."
    "Pressing her breasts even tighter together in a vice-like squeeze and dragging the length of her mounds furiously across my cockflesh."
    if w1GonzoReward == True:
        mc "...ah! You know, you're pretty skilled at this."
        mct "(I can only imagine how much better it'd be with massage oils or a more comfortable setting...)"
        "You know, not a dirty bathroom..."
        mct "(I definitely want to try this again...)"
    else:
        mc "...ah! You know, whenever I saw this in a porno, I thought this was just one of those silly things they do for the sake of fantasy."
        mc "I didn't expect it to be this... effective."
        mct "(Imagine how much better it'd be with massage oils or a more comfortable setting.)"
        mct "(I definitely want to try this again...)"

    scene toiletrosapai3_a with dissolve
    show toiletrosapai3
    mc "Ah, ngh..."
    "A hushed, involuntary coo escaped my lips. Much to my surprise."
    "It did feel really, {b}really{/b} good. To the point that it seemed almost absurd how easily satisfied the male ego was."
    "{size=-10}*Plap* *Plap* *Plap*{/size=-10}"
    rose "You're starting to leak a little... it's getting pretty slick."
    rose "It's getting pretty easy to work with this giant thing."
    mc "Hehe..."
    "Truly, just how easily satisfied the male ego was."
    play sound "sound effects/door-open.wav"
    "*Creeeaaaak*"
    scene w2_2185 with dissolve
    mct "(Shit...!)"
    mct "(Someone just...!)"
    scene w2_2186 with wipeleft
    show screen textbox2 with dissolve
    "--!"
    om "*Whistle* And come tell me Seán O'Farrell where the gath'rin is to be?"
    scene w2_2187 with dissolve
    om "Hmm... hmm..."
    play sound "sound effects/zipper.wav"
    scene w2_2188 with dissolve
    om "One more word for signal token:- whistle out the marchin' tune"
    scene toiletrosapai2_a with dissolve
    show toiletrosapai4
    hide screen textbox2 with dissolve
    mct "(She didn't even fucking stop!)"
    "Rosalind persisted with her ministrations, not faltering even a moment, repeatedly burying my cock deep into her bust as the footsteps grew closer and the man presumably sidled up to the urinal."
    "The only way I could tell she was rattled was the glimmer of uneasiness in her eyes. Still..."
    mc "*Gulp*"
    "She continued."
    scene toiletrosapai3_a with dissolve
    show toiletrosapai3
    "{size=-10}*Plap* *Plap* *Plap*{/size=-10}"
    "It wasn't very loud, but the sound of my increasingly pre-cum lubricated cock sliding in between Rose's growingly damp cleavage startled me."
    "{size=-10}*Plap* *Plap* *Plap*{/size=-10}"
    "Every little noise the act produced sent my heart fluttering."
    mct "(Could whoever just walked in hear us...?)"
    om "Hmm... hmm..."
    scene w2_2189 with dissolve
    show screen textbox2 with dissolve
    play ambient "sound effects/urine-ground.wav"
    "No. If he could, he would have stopped his humming."
    om "Murmurs ran along the valleys like the banshee's lonely croon."
    stop ambient fadeout 3.0
    hide screen textbox2 with dissolve
    scene toiletrosapai2_a with dissolve
    show toiletrosapai2
    "Perhaps equally cognizant of the noise, Rosalind slowed the pace down to a crawl."
    "A torturous, agonizingly bitter crawl."
    "{size=-10}*Plap* *Plap* *Plap*{/size=-10}"
    mct "(Ah...!)"
    "I had to bite my lip not to audibly groan."
    "My stomach swelled with a sickly sweet feeling. What had been a persistently building pleasure had painfully dipped."
    "I was like a salivating dog who had a steak suddenly ripped from his maw and was forced to watch it cruelly dangle just out of reach."
    scene toiletrosapai1_a with dissolve
    show toiletrosapai1
    "{size=-10}*Plap* *Plap* *Plap*{/size=-10}"
    "Still, if you ignored the cloying desire..."
    "{size=-10}*Plap* *Plap* *Plap*{/size=-10}"
    "This was nice too in its own way."
    "Instead of the feeling of hot friction, it was now like my cock was being gently hugged."
    "Our flesh clung together in a sticky mixture of oozing ejaculate and bodily sweat."
    mct "(Mmh...!)"
    show screen textbox2 with dissolve
    scene w2_2190 with dissolve
    play ambient "sound effects/urine-ground.wav"
    "{size=-10}*Plap* *Plap* *Plap*{/size=-10}"
    mct "(How big is this asshole's bladder?!)"
    om "Hmm... hmm..."
    scene w2_2191 with dissolve
    stop ambient fadeout 2.0
    om "Tis the rising of the moon, tis the rising of the moon--"
    scene w2_2192 with dissolve
    play sound "sound effects/zipper.wav"
    "*Ziiiiiip*"
    mct "(Thank you! He's finished.)"
    scene w2_2193 with dissolve
    om "Yet, thank God, e'en still are beating hearts in--"
    scene w2_2194 with dissolve
    om "Hmm-oh?"
    scene w2_2195 with dissolve
    "The humming ceased and odd and alarming noise came from the lavatory lyricist."
    scene w2_2196 with dissolve
    om "...?"
    scene w2_2197 with dissolve
    om "Hehe! Sorry for the tune, buddy. I didn't think anyone was in here!"
    hide screen textbox2 with dissolve
    scene toiletrosapai2_a with dissolve
    show toiletrosapai2
    if toughness >= 20:
        mct "(This bitch! She's still going!)"
    else:
        mct "(She's still going!)"
    mc "Uh... that's okay! I was enjoying it. Was that a pub song? "
    scene w2_2199 with dissolve
    show screen textbox2 with dissolve
    om "It does get sung in pubs, but it's a little more than that..."
    scene w2_2198 with dissolve
    om "..."
    mc "Ahem... well, you've got a nice voice..."
    scene w2_2200 with dissolve
    om "Haha, thanks! I'll let you get back to your business in peace."
    scene w2_2201 with dissolve
    om "I'm not really one to strike up a conversation with a stranger in a bathroom. No offense."
    scene w2_2202 with dissolve
    om "Especially when it's such a nice day out."
    mc "Thanks, have a good one..."
    scene w2_2203 with dissolve
    om "In the bathroom...?"
    om "Ah, to be young again. Hehehe!"
    scene w2_2204 with dissolve
    rose "Ahahaha, he's gone..."

    if w2RosalindParkTunnel == True:
        rose "That's twice in one day I thought I was about to have a heart attack and die."
    else:
        rose "I thought I was going to have a heart attack and die."

    mc "You didn't stop... in fact, you're still go--"
    play ambient "sound effects/boobjob.wav"
    hide screen textbox2 with dissolve
    scene toiletrosapai3_a with dissolve
    show toiletrosapai3
    mc "Ngh--!"
    "*Plap* *Plap* *Plap*"
    "Rosalind picked up where she left off, precipitously pistoning my dick into her breasts like it was a vagina."
    rose "I couldn't let you go soft. I need you to finish."
    "*Plap* *Plap* *Plap*"
    mc "Ah...! Are you listening to yourself? You're crazy."
    rose "Crazy times make for crazy women..."
    scene toiletrosapai2_a with dissolve
    show toiletrosapai4
    "{size=+10}*Plap* *Plap* *Plap* *Plap* *Plap* *Plap*{/size=+10}"
    mc "F-fuck!"
    mct "(Am I imagining things or...)"
    "*Plap* *Plap* *Plap*"
    rose "This guy didn't seem to mind."
    mct "(...Did that situation get her fired up?)"
    rose "Picture."
    mc "Ha, okay..."
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*" with flash
    rose "Now, just focus on finishing, baby."
    scene toiletrosapai5_a with dissolve
    show toiletrosapai5
    mc "Mgnh..!"
    "{size=+10}*Plap* *Plap* *Plap* *Plap* *Plap* *Plap*{/size=+10}"
    "The moments leading up to my orgasm turned into an exhaustive sprint."
    "The noise my dick made while gliding through the determined mother's sea of boob flesh sounded less like a titfuck and more like full on copulation."
    "{size=+10}*Plap* *Plap* *Plap* *Plap* *Plap* *Plap*{/size=+10}"
    mc "Ah...! Ah...!"
    scene toiletrosapai2_a with dissolve
    show toiletrosapai6
    "If anyone walked in now, it'd be unmistakable what was happening."
    "{size=+10}*Plap* *Plap* *Plap* *Plap* *Plap* *Plap*{/size=+10}"
    rose "You can let it all go, [mcf]..."
    "Rosalind adopted the same soothing, motherly tone she did last exhibition."
    rose "Don't hold back."
    "It was an odd combo that simultaneously assuaged my mind and enflamed my libido. The way she could manipulate me..."
    scene toiletrosapai5_a with dissolve
    show toiletrosapai5
    "{size=+10}*Plap* *Plap* *Plap* *Plap* *Plap* *Plap*{/size=+10}"
    "Sometimes, it was hard to believe she wasn't a practiced whore."
    mc "D-damn it!"
    "It wasn't long before I felt the need to cum hit a blinding fever pitch."
    mc "I'm close... where should I--"
    rose "In my mouth! On my tongue!"
    mc "...eh? O-okay!"
    scene w2_2205 with dissolve
    stop ambient
    "In an instant, Rosalind switched modes. Prying my cock from the sloppy embrace of her busom and straight into the inferno of her mouth."
    "The moment I felt the underside of my dick touch her tongue..."
    stop music
    play sound "sound effects/spurt.wav"
    scene w2_2206 with vpunch
    mc "Ng--!"
    play sound "sound effects/spurt.wav"
    "I came. I came and I came." with vpunch
    play sound "sound effects/spurt.wav"
    rose "Mmmh...!" with vpunch
    scene w2_2207 with dissolve
    "As far as I could tell, Rosalind did her best to prevent it from going down her throat."
    "Of course, some inevitably did, but I could feel her use her tongue to the best of her ability to dam up her throat and catch the creamy load I was giving her."
    rose "Mmmh...! Mh....!"
    scene w2_2208 with dissolve
    play sound "sound effects/mouth-pop.wav"
    "*Plop*"
    rose "Mmmh..."
    "In contrast to her previous zeal, Rosalind looked uncomfortable. Slightly disgusted with the taste."
    scene w2_2209 with dissolve
    rose "Awahh...!"
    "In a lewd display, she opened her mouth and showed me the results of her handywork."
    rose "Ugh..."
    rose "Ugh... ewugg...."
    scene w2_2210 with dissolve
    rose "Phwfitcture!"
    scene w2_2209 with dissolve
    mc "Oh, fuck right!"
    "The feeling hadn't quite returned to my body, but I had gotten pretty used to this by now."
    "Hoisting up the camera, I readied it for one final picture."
    mc "Say cheese..."
    scene w2_2210 with dissolve
    rose "Fhwucvk owff...!"
    $ renpy.end_replay()
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_2209 with flash
    "*Click*"
    scene black with flash
    if not persistent.roseW2BoobjobSceneGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.roseW2BoobjobSceneGallery = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    show screen textbox2 with dissolve
    $ history_rosalind = "The screws are being tightened on Rosalind's debt situation. Since this potentially presents a problem for the exhibition, I may be able to persuade the powers to be to help."
    $ unread_rosalind = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    "........."
    "......"
    "..."
    scene w2_2211 with blinds
    play music "music/jazz-piano-bar.ogg"
    rose "Sorry if I got out of hand there."
    "After cleaning up, Rosalind changed into a set of clothes she had stashed in a purse for just the occasion."
    scene w2_2212 with dissolve
    mc "No, I get it. You want to win."
    mc "...not like I didn't enjoy it, either."
    scene w2_2213 with dissolve
    rose "Heh, yeah..."
    scene w2_2212 with dissolve
    mc "Still, I was surprised. You turned into a completely different person back there."
    scene w2_2214 with dissolve
    rose "You barely know me, [mcf]."
    scene w2_2215 with dissolve

    if w1RoseGonzo == True:
        mc "I know the embarrassing crap you were forced to spill to me during your interview."
        mc "Plus, I know what's in your file. You might be surprised at just how thorough Mrs. Pulman is in her background checks."
    else:
        mc "I know what's in your file and you might be surprised at just how thorough Mrs. Pulman is in her background checks."

    mc "She knows stuff about you that you've likely forgotten about."
    scene w2_2214 with dissolve
    rose "Oh, really? Like what?"
    scene w2_2215 with dissolve
    mc "...okay, I'm being hyperbolic."
    scene w2_2216 with dissolve
    mc "You're right. I don't know you very well outside of what brought you to the club."
    mc "Handing out tit fuckings in unisex bathrooms could very well be within your character."
    scene w2_2217 with dissolve
    rose "Pff, shut up!"
    rose "Don't say vulgar things like that in public, please."
    scene w2_2218 with dissolve
    rose "Haha...!"
    "She laughed, at her imagined joke."

    if roseFlag == True:
        scene w2_2219 with dissolve
        mc "Did you just reprimand me?"
        scene w2_2220 with dissolve
        rose "Yep. Am I not allowed to do that?"
        scene w2_2219 with dissolve
        mc "Well, you're almost as old as my mother."
        scene w2_2221 with dissolve
        rose "You want me to take that as an insult, but you like that about me."
        scene w2_2219 with dissolve
        mc "You can tell, huh?"
        scene w2_2220 with dissolve
        rose "I got the feeling. What with the way you acted when we screwed last week..."
        scene w2_2219 with dissolve
        mc "Who's being vulgar now?"
        scene w2_2220 with dissolve
        rose "Am I right or am I right?"
        scene w2_2219 with dissolve
        mc "Women's intuition, huh? Yeah, you're right."
        mc "I do like older women."
        scene w2_2221 with dissolve
        rose "Lucky for you that at your age, that's not a high bar. Most women are older women."
        scene w2_2219 with dissolve
        mc "It's not just your age that I like about you."
        scene w2_2227 with dissolve
        rose "Just so you know, I'm too frazzled from earlier to flirt back."
        scene w2_2223 with dissolve
        mc "You remind me of my own mother."
        scene w2_2224 with dissolve
        "Rosalind gave me a weird, funny look. Which was fair, I suppose..."
        scene w2_2222 with dissolve
        rose "I don't know how to take that, hun."
        scene w2_2225 with dissolve
        mc "It's not what you're thinking."

        if roseTakeAdvantage == False:
            mc "Remember how I told you I never wanted to trouble my mom again?"
            scene w2_2226 with dissolve
            rose "Hmm... oh yeah, the day we first met. You turned down my advances and we had a nice talk."
            scene w2_2222 with dissolve
            rose "I remember."

        scene w2_2223 with dissolve
        mc "Let's just say that for personal reasons, I sympathize with you going through hell for your kid's sake."
        scene w2_2222 with dissolve
        rose "Personal reasons?"
        scene w2_2225 with dissolve
        mc "Reasons that mean I'm going to provide and care for her until the day one of us dies."
        mc "So I have a lot of respect for you."
        scene w2_2227 with dissolve
        rose "[mcf]..."
        scene w2_2228 with dissolve
        rose "You're a sweet boy."
        scene w2_2229 with dissolve
        mc "I'm just running my mouth."
        scene w2_2230 with dissolve

        if roseTakeAdvantage == False:
            "Just like the day we first met, it was extremely easy to open up with her."
        else:
            "For some reason, it felt extremely easy to open up with her."

        scene w2_2231 with dissolve
        rose "You're a sweet boy, but it sounds like you've got some misguided ideas."
        scene w2_2230 with dissolve
        mc "Misguided...?"
        scene w2_2233 with dissolve
        rose "Just a guess, but I'm sure your mother would prefer you to live your own life."
        scene w2_2230 with dissolve
        mc "What she thinks doesn't really matter."
        mc "I'm going to do what I want and that's getting to the point in my life where I can look out for her."
        scene w2_2232 with dissolve
        rose "I take it all back. You're not so sweet, are you?"
        scene w2_2234 with dissolve
        rose "..."
        scene w2_2233 with dissolve
        rose "You should come back to my place and I'll make you lunch."
        scene w2_2230 with dissolve
        mc "Your place? What about your daughter?"
        scene w2_2233 with dissolve
        rose "I sent her off to a month-long summer camp yesterday."
        scene w2_2230 with dissolve
        mc "Isn't that expensive?"
        scene w2_2231 with dissolve
        rose "More than I can afford, but..."
        scene w2_2230 with dissolve
        mc "You want her gone while the exhibition is going on."
        scene w2_2231 with dissolve
        rose "Exactly... she's smart. She'll notice things are different."
        scene w2_2235 with dissolve
        rose "Instead of her mother lying to her, she'll instead make a nice memory."
        scene w2_2230 with dissolve
        mc "You don't have any other family?"
        scene w2_2231 with dissolve
        rose "None that I can or want to rely on."
        scene w2_2230 with dissolve
        mc "It sucks not having an extended family, huh?"
        scene w2_2231 with dissolve
        rose "It simplifies things. I was raised in a big family and dysfunctional doesn't quite cover it."
        scene w2_2230 with dissolve
        mc "All my extended family is on my dad's side."
        mc "They washed their hands clean of us after he died. So I have no frame of reference."
        scene w2_2236 with dissolve
        rose "..."
        scene w2_2235 with dissolve
        rose "If they're those kind of people, you dodged a bullet."
        scene w2_2234 with dissolve
        mc "Yeah, I suppose you're right."
        scene w2_2230 with dissolve
        mc "..."
        scene w2_2233 with dissolve
        rose "So... lunch?"
        scene w2_2230 with dissolve
        mc "Well, I did skip breakfast..."
        jump w2RosaFlag
    else:

        scene w2_2219 with dissolve
        mc "Heh. Yeah, we CERTAINLY didn't do anything vulgar today."
        scene w2_2220 with dissolve
        rose "Just two friends sitting on a bench in the park."
        scene w2_2237 with dissolve
        rose "Pftt, hehehe..."
        mc "Yeah, \"friends\"... ha!"
        scene w2_2234 with dissolve
        "......"
        scene w2_2230 with dissolve
        "..."
        scene w2_2231 with dissolve
        rose "You think I'll be able to go back to feeling normal after all this is over?"
        scene w2_2236 with dissolve
        mc "You might have a new normal, but... yeah I do."
        mct "(My mom did.)"
        scene w2_2233 with dissolve
        rose "I think so too. To be honest, I don't even feel like myself right now. Sometimes I get this weird feeling that I'm watching myself from up on high."
        scene w2_2230 with dissolve
        mc "I think that's called dissociation. It's a coping mechanism."
        scene w2_2231 with dissolve
        rose "Oh, Yeah? Guess it's good to have a word for it."
        scene w2_2235 with dissolve
        rose "I'm hoping that means this will all be behind me after the month is up."
        scene w2_2230 with dissolve
        mc "You're that confident about winning?"

        if roseSeduceFlag == True and roseFlag == False:
            scene w2_2231 with dissolve
            rose "Yes. Even without your help."

        scene w2_2233 with dissolve
        rose "I can't afford to think otherwise."
        scene w2_2230 with dissolve
        mc "Eyes on the prize?"
        scene w2_2232 with dissolve
        rose "Yep... Eyes. On. The. Prize."
        scene w2_2230 with dissolve
        rose "..."
        scene w2_2235 with dissolve
        rose "Ah, I should get home. I want to clean up and take a shower."
        rose "We're done here, right?"
        scene w2_2230 with dissolve
        mc "We are. I think Mrs. Pulman will be satisfied."
        mc "......"
        scene w2_2236 with dissolve
        rose "..."
        scene w2_2238 with dissolve
        rose "Heh, I'm going to go now."
        scene w2_2239 with dissolve
        mc "Be safe on the way home."
        scene w2_2240 with dissolve
        rose "I will."
        mc "..."
        scene w2_2241 with dissolve
        mct "(Oh, geez...)"
        mct "(Today was exciting.)"
        scene black with fade
        "......"
        "..."
        if date == "june09day":
            jump w2HanaNight1
        else:
            jump w2HanaNight2

label w2RosaFlag:


    if _in_replay:
        show transitionrosalind03 with cmet
        show screen textbox2 with dissolve
        "Did [mcf] take advantage of Rosalind when they first met?"
        hide screen textbox2 with dissolve
        menu:
            "Yes.":
                $ roseTakeAdvantage = True
            "No.":
                pass
        show screen textbox2 with dissolve

    scene w2_2233 with dissolve
    rose "Then eat with me. I'll fix you a home-cooked meal."
    scene black with fade
    stop music fadeout 3.0
    mc "Sure, I'd like that."
    "......"
    "..."
    play sound "sound effects/door-openclose.wav"
    scene w2_2242 with blinds
    "Along the way to Rosalind's home, I couldn't figure out for the life of me why she would voluntarily share a meal with me, especially after what we did in the park."
    "I had no pretense that she had any genuine affection or interest in me."
    scene w2_2243 with dissolve
    rose "The kitchen is in here."
    scene w2_2244 with dissolve
    rose "That's the living room. Make yourself comfortable."
    scene w2_2245 with dissolve
    rose "I'm going to go change."
    scene black with fade
    "So why, indeed...?"
    play ambient "sound effects/bacon-sizzle.wav"
    play music "music/helping-hands.ogg"
    scene w2_2246 with w20
    rose "Hmm hmm hmm..."
    rose "Now, I'm not the greatest cook, so don't set any high expectations for me."
    $ renpy.music.set_volume(.5, 1, channel = "ambient")
    scene w2_2247 with dissolve
    "That's why."
    scene w2_2248 with dissolve
    mc "I have this strange feeling that whatever you cook will be just fine..."
    scene w2_2247 with dissolve
    "Just a minute ago, she had walked in almost completely naked and carried on business as usual, asking if {i}this{/i} or {b}that{/b} suited my taste before beginning the prep work."
    "Doing so in a way that had a needlessly provocative flourish."
    "When she'd reach for something or another, she'd stick her ass out far more than was necessary."
    "When she'd bend over to grab a pan, she made sure to do it in a way that flashed her pussy."
    scene w2_2249 with dissolve
    "This was her being proactive on her half of our deal."
    scene w2_2250 with dissolve
    mc "This is a bit... much, don't you think?"
    scene w2_2252 with dissolve
    "At my comment the pleasant humming dwindled off into silence and her shoulders lost a bit of life."
    scene w2_2251 with dissolve
    rose "...do you not like forward women, Mr. [mcl]? Is that what you're trying to say?"
    scene w2_2252 with dissolve
    mc "No, that's not it... I can't knock you for your approach. The naked apron thing is A plus and you do look great."
    mc "Really, REALLY great."
    scene w2_2253 with dissolve
    rose "...that's a relief."
    rose "Despite all we have done, would you believe it was still difficult to parade myself out here dressed like this? It's kind of silly the way the mind works."
    scene w2_2254 with dissolve
    mc "It's just... don't you think you're trying a little {b}too{/b} hard?"

    if roseDealFullAcceptance == True:
        mc "It feels extreme, even to uphold your end of the deal. You don't have to take it this far."
    else:
        mc "You don't have to take it this far for me to uphold my end of the deal."

    scene w2_2251 with dissolve
    rose "Do you want me to put some clothes on, [mcf]? Is that it?"
    scene w2_2252 with dissolve
    mc "Ah... eheh..."
    mc "No."
    mc "{b}No{/b}, I don't."
    scene w2_2255 with dissolve
    "How could I not answer honestly in a situation like this?"
    scene w2_2256 with dissolve

    if roseDealFullAcceptance == True:
        mc "I'm just amazed at the faith you're putting in me."
    else:
        mc "The thing is you're putting a lot of faith in me. I'm still not sure how I can even help you."

    scene w2_2247 with dissolve
    rose "I know, but doing \"this\" doesn't cost me anything."
    mc "..."
    scene w2_2256 with dissolve
    mc "Carving out your own advantages. You're pretty ruthless for a housewife."
    scene w2_2257 with dissolve
    rose "This world is transactional. You've got to give to get, right?"
    scene w2_2247 with dissolve
    "Despite her cold, harsh words she said it with a warm smile. Like she accepted that truth, but wouldn't let it dim her spirit. It was..."
    mct "(Comforting.)"
    rose "Now... just sit back, enjoy your meal..."
    scene black with fade
    stop ambient fadeout 2.0
    stop music fadeout 2.0
    rose "...and the service."
    scene w2_2258 with dissolve
    play ambient "sound effects/fel2.wav"
    rose "*Smack* *Fwup* *Plop*"
    "What else would it be?"
    rose "*Fwuuuuuuuuch!*"
    scene w2_2259 with dissolve
    $ renpy.music.set_volume(1, 0, channel = "ambient")
    "As soon as she set the plate down, Rosalind had me undress and then got down on all fours and crawled under the table."
    rose "Fwup....! Mmh...!"
    stop ambient
    scene w2_2260 with dissolve
    rose "*Plop...!*"
    scene w2_2261 with dissolve
    rose "You should eat while the food is still hot."
    scene w2_2260 with dissolve
    scene w2_2259 with dissolve
    play ambient "sound effects/fel2.wav"
    rose "*G-guh! Guhk!*"
    mc "Ah!"
    $ renpy.music.set_volume(0.5, 1, channel = "ambient")
    scene w2_2262 with dissolve
    mc "Fuck..."
    "It had just been an hour since her previous service, but my dick was already standing at full, 100%% attention."
    $ renpy.music.set_volume(1, 1, channel = "ambient")
    scene w2_2263 with dissolve
    "It was heavy and bloated, forcing Rosalind's tongue to shape to its curves as it rested in her mouth."
    scene w2_2264 with dissolve
    rose "Guughk-!"
    scene w2_2263 with dissolve
    "She was making a deliberate show of holding it there, past the mouth of her gullet, ignoring her gag reflex and treating my ears to a wretched sequence of sputtering and choking as it tried to repel the foreign object."
    scene w2_2264 with dissolve
    rose "*Cough* *Gkh...!"
    if w2RoseGag == True:
        mct "(Don't tell me she took my comment about gagging to heart?)"
    scene rosahomedt_a with dissolve
    show rosahomedt
    rose "Mmmh...! *Chwup~!*"
    mc "Hot d-damn...!"

    if roseDealFullAcceptance == True:
        "I had fully agreed to let her be my slut for the month and she was making good on it."
        "Even if I wanted to turn her down, she seemed desperately dead set on doing this. I suspected it gave her a sense of control and the reassurance that I wouldn't absentmindedly renege on our deal."
    else:
        "I had previously told her I'd help without any strings attached and I truly meant it. I had felt that way, up to the certain point Rosalind had my cock in her mouth."
        "Not that I could deny her in the first place. Just like last time, she was desperately dead set on doing this and I suspected it gave her at least a small feeling of control."
        "She wanted to be on my mind, to be sure I wouldn't absentmindedly renege on our deal."

    stop ambient
    scene w2_2260 with dissolve
    rose "*Plop-!*"
    scene w2_2261 with dissolve
    rose "Eat, and then you can have dessert."
    scene w2_2265 with dissolve
    mc "Right, I should eat..."
    scene w2_2266 with dissolve
    "I ate it all, but I sure as shit didn't remember the taste for some reason."
    "Still, it might've been the best meal I had ever eaten in my entire life."
    scene black with fade
    mc "What was this about dessert...?"
    "......"
    "..."
    hide screen textbox2 with dissolve
    play music "music/ninja-tortoise.ogg"
    scene rosahometdog_a with cmet
    show rosahometdog
    "The part that came before this was all lost in a steamy flurry of hands and other body parts, mouths meeting nipples, teeth grazing skin, and hands tugging at clothes..."
    rose "[mcf]...! Ah...!"
    "Before I knew it, I was buck naked in Rosalind's kitchen, belly full of food and my balls careening violently against her quim as she bounced off my cock."
    rose "Finally...!"
    "If she wanted me to feel like a king, she'd succeeded with flying colors. She gave herself over completely to my hands."
    "Hands that held a firm grip on the wanton mother's swaying tits, while my lower half methodically plunged in and out of her cunt at a violently deep yet slow tempo."
    "*Clap...* *Clap...* *Clap...*"
    scene rosahometdog2_a with dissolve
    show rosahometdog2
    "Every biting thrust met a pillow soft landing from Rosalind's plump rump."
    rose "Ah! Gh! Ha...! That's it, baby!"
    "*Clap...** *Clap...* *Clap...* *Clap...*"
    "The sound of flesh on flesh and the shrill cries of copulation drowned out the dull electrical hum of the kitchen."
    rose "Eheh...! Grab me harder, [mcf]! Fuck me harder!"
    "The words were trite but the edge in her voice..."
    scene rosahometdog_a with dissolve
    show rosahometdog
    mc "Mmmh- y-you're actually into this?"
    "We had barely even started and Rosalind was crying out garishly for more."
    rose "Muhuh...! Y-es!"
    rose "W-why do you sound surprised? Ah-!"
    rose "I enjoyed it last time too! Don't you remember?"
    rose "Just, ah-! Look...! I took care of you today, so now you HAVE to take care of me. O-okay?!"
    mc "You have my help, you don't have to remind--"
    rose "I'm not talking about the competition! That's the l-last thing I want to think about right now! Ah~♥"
    rose "When I say \"take care of me\", I mean {b}fuck me{/b}!"
    rose "Fuck me like you own me! Fuck me like you hate me! Fuck me however you want!"
    rose "Just don't let my mind wander even a single minute!"
    scene rosahometdog2_a with dissolve
    show rosahometdog2
    mc "Ha! Is that why you fed me beforehand?! I'll fuck you all day if you want!"
    "I allowed myself to be taken in by her words. To my ears, they sounded genuine..."
    "What didn't when you were balls deep in a woman?"
    mc "R-rose!"
    "The word was surprisingly difficult to eek out under the sweltering pleasure and tight grip of Rosalind's lower mouth."
    mc "R-rose...!"
    rose "Ah-! Don't call my name! Ng-!"
    mc "Mmmhn, no...?"
    rose "Call me a slut! Call me a whore!"

    menu w2RosalindKitchenTone:
        "Play along and call her names."(chg=["rosalind_passion_up"]):
            $ Rosalind_Libido += 1
            $ w2RosaMean = True
            mc "You whore!"
            scene rosahometdog3_a with dissolve
            show rosahometdog3
            rose "Ah, t-thank you...! I know it's weird, but..."
            mc "Don't worry, you don't have to explain it to me."
            mc "Still, geez... You're thanking me for calling you a whore?"
            "It was sort of amusing, in its own twisted way."
            mc "You really are quite the dirty bitch! Do you like getting your hole plugged by a man young enough to be your own son?"
            rose "Yes! Keep plugging my pussy... please!"
            mc "You can do better than that, cunt. Say it like you mean it!"
            rose "Ah...! Ghe...! O-okay...!"
            rose "Please! Please, keep fucking my pussy! I NEED your cock plugging my fuck hole!"
            mc "Ah, you fucking hag! That's what I like to hear!"
            "Every piece of articulated abuse caused her hole to squeeze and cling to my cock tighter and tighter. It seemed Rosalind truly had a genuine appreciation for this sort of talk."
            "If this is what she liked, this is what she'll get the rest of the night."
            rose "Ah, f-fuck me like you mean it, [roseSN]."
            mct "(Shit, she remembered what I had her say at the exhibition. She's really...)"
            mc "You're something else, Rose."
            "An honest thought carelessly escaped my lips."
            rose "Ah! Ggh...!"
            "I didn't know how she could be so conscientious in a moment like this."




        "{color=#FF1493}[[Rosalind Libido]{/color} Play along with creativity and gusto."(chg=["rosalind_passion_up","rosalind_up"]) if w2RosaCreativeMenu == False:

            $ w2RosaCreativeMenu = True
            $ Rosalind_Libido += 1
            $ Rosalind_Affection += 1
            mc "Oh...? You fucking bitch!"
            mc "Isn't that one and the same?"
            rose "Mmmh...!"
            mc "Rosalind Carter and stupid whore... the two go hand in hand. When I say one, the other is implied!"
            rose "Mmmh...! Mmmh...! Ah...? W-what?"
            scene rosahometdog4_a with dissolve
            show rosahometdog4
            mc "You useless cum dump!"
            mc "Are you trying to pretend like they're two different things?"
            rose "N-no?"

            if Rosalind_Libido >= 5:
                $ w2RosaCreative = True
                mc "Apologize for being such a slutty mother!"
                rose "W-what?"
                mc "I said {b}apologize{/b} for being such a slutty mother!"
                rose "I'm s-sorry!"
                mc "For what?!"
                rose "I'm sorry for being a slutty mother!"
                mc "Who's a slutty mother?"
                rose "I am! I'm a slutty mother!"
                "The way her pussy clamped down on my dick as she accepted the verbal abuse reassured me I wasn't going too far here."
                "I wondered if she was always this slutty or if this week had kicked her {color=#FF1493}libido{/color=#FF1493} into overdrive."
                rose "I'm a slutty mother!"
                mc "That's not quite what I asked! Say it clearly and state your name!"
                rose "Ah-! Ah-! Ah! I--"
                rose "I, Rosalind Carter, -oooh!- am a slutty mother!"
                mc "Saying that so proudly while getting railed by my cock on the place where you have a family dinner. You really must be!"
                scene rosahometdog3_a with dissolve
                show rosahometdog3
                mc "You cow!"
                rose "Yes! Ah~♥"
                mc "You fat ass cow!"
                rose "Yes!"
                mc "YOU. {w}STUPID. {w}USELESS. FAT. ASS. {w}COW!"
                rose "Yes!"
                "Surprisingly, Rosalind didn't seem to mind the rhetorical cruelty. She even seemed to delight in it, much like I did."
                "It was all in a fucked up pursuit of getting our rocks off, of course."
                scene w2_2267 with pixellate
                vic "Gheh... fwh... c-cocks-!"
                cm "This stupid slut has fucking lost it! Haha! Is that all you can say?"
                vic "C-cocks...! Give me cocks!"
                scene rosahometdog3_a with pixellate
                show rosahometdog3
                "She wasn't stupid and I truly didn't believe she was a whore."
                "I didn't actually believe any of what I was asking Rosalind to say, but if she wanted me to call her dirty names, I'd do so happily and with genuine sadistic glee."
            else:

                rose "Ah-! N-no... not..."
                rose "A little less, p-please? That's..."
                "An uneasiness had brought her previous howling to a broken whisper. This sort of meanness was unappetizing for her."
                "No surprise, not everyone's as fucked up as me."
                scene rosahometdog_a with dissolve
                show rosahometdog
                mc "Sorry, that was too much. I don't, I'm..."
                "She needed me to help her forget about today; I should..."
                jump w2RosalindKitchenTone
        "Talk dirty, but don't degrade her."(chg=["rosalind_up"]):


            $ w2RosaKind = True
            $ Rosalind_Affection += 1
            scene rosahometdog4_a with dissolve
            show rosahometdog4
            mc "No... I won't let you get away from the fact that I'm fucking you, Rose."
            mc "I'm not screwing just some whore, I'm fucking you in your very own kitchen, sliding my cock in and out of your pussy while you cream yourself by shaking your beautiful ass."
            "If she wanted dirty, I'd make it dirty... but on my own terms."
            scene w2_2267 with pixellate
            vic "Gheh... fwh... c-cocks-!"
            cm "This stupid slut has fucking lost it! Haha! Is that all you can say?"
            vic "C-cocks...! Give me cocks!"
            scene rosahometdog3_a with pixellate
            show rosahometdog3
            "At this very moment at least, I didn't feel like degrading her."
            mc "Do you like taking the dick of a man young enough to be your son, {b}Rose{/b}?"
            rose "Yes, keep giving me that dick! Please!"
            mc "Good, because I love fucking you. Nothing beats your pussy!"
            mc "Not a single woman my age can compare."
            rose "Ah! Ah~♥ Liar! I'm just an old woman..."
            mc "Why would I be lying, Rose? How hard is my dick right now?"
            rose "H-hard!"
            mc "You can do better than that, Rose. Use your words."
            rose "Your cock is so {b}hard{/b} and {b}big!{/b}"
            rose "It's hitting me so deep!"
            mc "That's right. You're so beautiful that I'm hitting parts of you I didn't even know I could!"
            rose "Mmh..! [mcf]....♥ T-thank you! Keep plugging my cunt with your cock!"
            "It might not have been what she wanted exactly, but I could tell she was enjoying the dirty talk by the way her lower mouth clung sweetly to my pole."


    "So enamored with Rosalind's desire, I resolved to give her everything she wanted from this encounter."
    "If she wanted to forget all her troubles for an evening, I'd sure as hell oblige her."

    menu w2RosaIntensify:
        "Find a new angle of attack.":

            if w2RosaMean == True:
                mc "Brace yourself, slut. I'm going to fuck you as {b}deeply{/b} as you deserve!"
                scene rosahometlift_a with fade
                show rosahometlift
                "Giving Rosalind a quick heads up, I lifted her leg to find a new way to truly fuck the wanton mother like the bitch she is."
            if w2RosaCreative == True:
                mc "I hope your pussy is ready for what's next!"
                scene rosahometlift_a with fade
                show rosahometlift
                "Putting aside the fact I just delivered such a deeply ridiculous line with unmitigated gusto, I lifted Rosalind's leg to find a new angle of attack on her slathering cunt."
            if w2RosaKind == True:
                mc "Get ready, Rose. I'm going to fuck your pussy as {b}deep{/b} and hard as you want!"
                scene rosahometlift_a with fade
                show rosahometlift
                "Giving Rosalind a quick heads up, I lifted her leg and had her brace herself as I searched for a new avenue to pleasure the wailing, wanton mother's lovehole."

            "With an additional burst of fervor, I picked up speed, making a concerted effort to use the tip of my penis to gouge and scrape every nerve lining Rosalind's tunnel."
            rose "OoooOooh! Yhee-!"
            "The cacophonous wail it drew from Rosalind's rosy lips provided ample evidence that she had no qualms with this change of tempo and force."
            "*Clap...* *Clap...* *Clap...*"
            rose "Ha...!"
            "She was happy being putty in my hands, content to ride the wave of pleasure that every deep stab or shallow poke produced."
            "Likewise, I was happy to fill the void between her legs. To bury my cock to the base and delight in the way her insides fruitlessly tried to tighten and prevent its escape, only to be left barren once more as I easily withdrew from the sloppy hole."

            if w2RosaMean == True:
                mc "You like getting fucked like a proper bitch, Rose?"
                mc "You like how deep my dick is hitting your insides?"
                rose "Ah...! I do! I love it!"
                mc "Good! A slut like you deserves every inch, but only if you ask nicely!"
                rose "Mmmg....! Ah-! Huh? What?"
                mc "Ask me nicely to feed you lower mouth every inch of my cock!"
                "With Rosalind, it was so easy to lose myself and say such obnoxiously silly things. The crap that was coming out of my mouth..."
                rose "Please, give me... EVERY. FUCKING. INCH of your cock, sir!"

            if w2RosaCreative == True:
                mc "You know, you should thank me for fucking a past-her-prime whore like you. I'm really putting my back into this."
                rose "Thank you! Thank you for fucking me!"
                mc "Ha! It's hard work fucking a greedy cunt like yours!"
                rose "Thank you for fucking my greedy cunt, sir!"
                mc "That's more like it~"
                "With Rosalind, it was so easy to lose myself and say such obnoxiously silly things. The crap that was coming out of my mouth..."
                mc "That's more like it."

            if w2RosaKind == True:
                mc "How's this position working for you?"
                mc "You like how deep my dick is hitting your insides?"
                rose "Ah...! I love it - I'm loving every inch of it!"
                mc "Good. You'll get as much of it as you want."
                mc "No other thought will pass through your head other than taking dicks!"
                "With Rosalind, it was so easy to lose myself and say such obnoxiously silly things. The crap that was coming out of my mouth..."
                mc "I'm going to screw you so much that your pussy will remember the shape of my cock!"

            scene rosahometlift2_a with dissolve
            show rosahometlift2
            "I was happy. This was {i}fun{/i}."
            "{b}Freeing{/b}."
            "Rosalind would take anything I gave her, in exchange for something I didn't quite understand."

            if roseTakeAdvantage == True:
                rose "Ah... ha...! It's funny! To think, the first time we met, you apologized for what we did...!"
                mc "That's what led you to come to my apartment last week, am I wrong?"
                rose "-Ah! Y-you... realized that?"
                mc "You saw the signs of weakness and you did what you thought you had to...! I don't blame you."
                rose "That was part of it, but it was when you -ng!- a-asked me out that it clicked!"
                mc "I really did regret it, y'know...."
                rose "F-fuck....! That's why I like you, [mcf]!"

                if w2RosaMean == True:
                    mc "Ha! And I like how you move that fat ass of yours!"
                    mc "Now shut up and get fucked!"
                if w2RosaCreative == True:
                    mc "Ha! If I knew you were such a sex-starved hag, I wouldn't have!"
                    mc "Now shut up and get fucked!"
                if w2RosaKind == True:
                    mc "To be honest, I'd do it again! It was worth it to get to fuck you like this."
            else:


                rose "Ah... ha....! It's funny! You turned me down the first time we met and now...!"
                mc "That's what led you to come to my apartment last week, am I wrong?"
                rose "That was part of it, but it was when you -ng!- a-asked me out that it clicked!"
                rose "-Ah! Still, you... r-realized that?"
                mc "I had a feeling that it made me look like an easy target."
                rose "Don't put it that way...! You acted like a decent person that night! You left a strong impression...!"
                mc "Just for being decent?"
                rose "Sometimes \"just\" decent can make all the difference to a woman."
                rose "F-fuck...! Ah, fuck me! Are you a-angry that I tried to take advantage of your kindness?"
                mc "You saw an opening and took it...! I won't blame you for that."
                rose "Mmmh...! Thank you, [mcf]..."

                if w2RosaMean == True:
                    mc "Don't thank me yet, whore! I'm not done fucking you."
                if w2RosaCreative == True:
                    mc "Don't thank me yet! Save that for when I'm done fucking you!"
                if w2RosaKind == True:
                    mc "Don't thank me yet, Rose! I'm not done fucking you."

            scene rosahometlift_a with dissolve
            show rosahometlift
            "*Clap* *Clap *Clap*"
            "By this point Rosalind and I were working in perfect tandem, in sync with our movements and working together to fulfill each other's carnal needs."
            "She was giving as good as she got, throwing her ass back and meeting my thrusts with a well-timed precision that made sure I hit the deepest parts of her, grinding her hips in a way that wrung every ounce of pleasure from our joining."
            "*Clap* *Clap *Clap* *Clap* *Clap*"
            "She was making sure I tasted as much of her pussy as I possibly could."
            rose "Ha...! Ha...! How does this feel so good?! It's never..."
            "*Clap* *Clap *Clap* *Clap* *Clap* *Clap* *Clap*"
            mct "(Felt this good...?)"
            "Is that what people mean by sexual compatibility?"
            "*Clap* *Clap *Clap* *Clap* *Clap* *Clap* *Clap* *Clap* *Clap*"
            "Whatever you'd call it..."
            "*Clap* *Clap *Clap* *Clap* *Clap* *Clap* *Clap* *Clap* *Clap*"
            "It meant...."
            rose "Oh...! Oh...! Gh...!"

            "It meant we could selfishly indulge in each other's flesh without worry."
            scene w2_2269 with dissolve
            rose "Gegghhh...!"
            "So caught up in the act, my brain barely registered the feeling of the slutty mother erupting like a geyser and coating my thighs with her love juices."
            rose "Ghyhueeeeeeh! Heaaa..! Haaah!"
            "I might have not registered it at all if it wasn't for the piercing shriek and mind-blanking tightness that accompanied Rosalind's abrupt orgasm."
            scene rosahometlift2_a with dissolve
            show rosahometlift2
            rose "Ah...! Yeeeehs..."
            rose "Y-you're fhucking me through m-my...!"

            if w2RosaMean == True:
                mc "You think I'm going to slow down? A whore like you wouldn't be satisfied with that."
            if w2RosaCreative == True:
                mc "You think I would slow down just because you came? I've still got a load of jizz to give you."
            if w2RosaKind == True:
                mc "Slow down? I'm not going to be satisfied with you only having one!"

            scene w2_2268 with dissolve
            rose "Ah....! Gheeeee! Fwuwwwwaah! F-ffuuuuuck!"
            "Another orgasm."
            scene rosahometlift_a with dissolve
            show rosahometlift
            "It felt amazing to fuck her through her climax. The way her cunt clamped down made it difficult to escape her inner walls' sweet embrace and fight my way back into her."
            rose "Ah...! Ha...! A-another one....? It fheels wheiird...!"
            "In fact, the sensation was so delicious and heavenly and my legs burned fiercely from the exertion that I wanted to..."

            menu w2RosaEjaculate1:
                "Ejaculate.":


                    if w2RosaMean == True:
                        mc "C-cumming! Where do you want it, whore?"
                        rose "Inside! It's safe, you can do it inside!"
                        mc "Ask me for it, bitch!"
                        rose "Will you please give me your cum, [mcf]? Shoot it inside!"
                        mc "Ng...! Ha... have it your way!"
                        mc "T-take it!"

                    if w2RosaCreative == True:
                        mc "C-cumming! Beg me for it!"
                        rose "Ah, y-yes! Please! Give me your cum!"
                        mc "Where do you want it?"
                        rose "D-do it inside! It's safe!"
                        mc "You don't have to tell me twice...!"
                        mc "Have it your way, you slutty mother! Take it in your pussy!"

                    if w2RosaKind == True:
                        mc "C-cumming! Get ready!"
                        rose "Ah, y-yes! Do it, inside! It's safe...!"
                        rose "Give me your cum, [mcf]!"
                        mc "You don't have to tell me twice...!"
                        mc "T-take it!"

                    "With one last thrust, I hilted myself fully in Rosalind's spasming hole, propelled forward by the instinct to drive myself as deep as possible into the constricting passage and make a direct deposit of spunk in her ovaries."
                    "Every muscle of my body momentarily tensed up in preparation for my impending release, the fingers on my hands digging hard into the soft flesh of Rosalind's body and leaving a tangible mark of our copulation."
                    stop ambient
                    stop music
                    play sound "sound effects/spurt.wav"
                    scene w2_2274 with flash
                    mc "Gh, aaaah-!"
                    "An automatic, animal-like growl and then complete and utter sensory bliss."
                    rose "Ooooooh, oooooh!"
                    play sound "sound effects/spurt.wav"
                    scene w2_2275 with vpunch
                    "All tension in my body left me as I poured strand upon strand of semen into the wailing mother's accepting quim."
                    mc "--!"
                    "Her pussy was working hard to coax out every last spermatozoa waiting in my urethra."
                    scene w2_2276 with dissolve
                    mc "Oh, shit!"
                    "Before I regained my composure, I witlessly laxed my grip and sent Rosalind tumbling face first into the table."
                    play sound "sound effects/thud-floor.mp3"
                    scene w2_2277 with vpunch
                    "Thud!"
                    rose "Ha...! Ha...! That was...!"
                    "Thankfully, she seemed not to mind."
                    rose "That was... ah..."
                    scene black with fade
                    $ renpy.end_replay()
                    if not persistent.roseW2KitchenSceneGallery:
                        play sound "sound effects/notification.wav"
                        show memoryunlock with dissolve
                        $ renpy.pause(3, hard=True)
                        $ persistent.roseW2KitchenSceneGallery = True
                        hide memoryunlock with dissolve
                        $ renpy.pause(0.5, hard=True)
                    "......"
                    "..."
                    rose "H-how long until you can go again?"
                    jump w2RosalindConclusion


                "{color=#FF1493}[[Tireless]{/color} Resist the urge as long as you can."(chg=["rosalind_passion_up"]) if trait_tireless == True:
                    $ Rosalind_Libido += 1
                    "Not yet!"
                    stop ambient
                    scene w2_2278 with fade
                    rose "Eh, whaa....?"
                    "Resisting all instinct to fill the wanton mother's sloppy hole with my jizz, I dropped the insensate woman onto the table in front of us."
                    rose "When did I...?"
                    scene black with fade
                    "......"
                    "*Squick* *Squelch* *Sqewlch...!*"
                    rose "...geh! Ha...!"
                    jump w2RosalindTirelessFinish



                "{color=#696969}[[Tireless] Resist the urge as long as you can.{/color}" if trait_tireless == False:
                    jump w2RosaEjaculate1


        "{color=#FF1493}[[Strongman]{/color} Sweep Rosalind off her feet and onto your dick." if perk_strongman == True:

            stop ambient
            scene w2_2272 with fade
            rose "O-oh, what are you..."
            mc "Brace yourself."
            "With that simple, terse warning I abruptly dropped Rosalind onto my dick."
            scene w2_2273 with vpunch
            rose "Gggggeeeh-!"
            "The moment I did, the whole of my cock experienced a staggering, overwhelming tightness that threatened to make me cum right then and there."
            "Did she just..."
            rose "C-ccuuuming...?!" with flash
            "She did, holy shit!"
            play ambient "sound effects/boobjob-slow.wav"
            scene rosahometlift3_a with dissolve
            show rosahometlift3
            "With strenuous effort, I pulled my cock from the vice-like grip and began to fuck her in earnest."
            "I didn't want to let Rosalind have even a moment's rest. My goal was to drive her crazy."
            "It was difficult to move at first, but as her brief orgasm subsided, I fell into an earnest rhythm."
            rose "Ghwuah...?"

            if w2RosaKind == True:
                mc "You okay there?"
                rose "H-huh...? Y-yeah..."
                rose "I just wasn't expecting that."
                mc "Me either, you really surprised me. I almost came on the spot!"
            else:
                mc "Earth to Rose, do you hear me?"
                rose "Y-yeah..."
                rose "I j-just w-wasn't expecting that."
                mc "Good, then get it together. Don't just sit there."
                mc "Move your ass!"

            scene rosahometlift4_a with dissolve
            show rosahometlift4
            "Rosalind gripped me tightly, holding on as if for dear life."
            "A fact that I appreciated, as I focused on holding her body steady so my lower half could gouge and scrape every delicious inch of Rosalind's inner walls."
            "The position was putting a strain on my body, but it was worth it to literally have the slutty mother in the palm of my hands."
            rose "Gheeeaaauuh...!"
            "A little soreness in the morning would be a small price to pay for the precious sound of Rosalind howling like a bitch in heat."
            rose "Ah-! Yesh...! You're... hwitting meh soh, deeeep...!"
            scene rosahometlift3_a with dissolve
            show rosahometlift3

            if w2RosaKind == True:
                mc "I know. You taste wonderful, Rose."
                mc "How are you liking the taste of my dick?"
                rose "L-lihk eeet...!"
                mc "You like it? That makes me happy."
            else:
                mc "I know. It's what you wanted, right?"
                mc "To be handled like a sex toy?"
                rose "Yesh...!"
                mc "Heh, is that all you can say?"

            "*Squick* *Squelch* *Sqewlch...!*"

            if roseTakeAdvantage == True:
                rose "Ah... ha...! It's funny! To think, the first time we met, you apologized for what we did...!"
                mc "That's what led you to come to my apartment last week, am I wrong?"
                rose "-Ah! Y-yooooou... realized that?"
                mc "You saw the signs of weakness and you did what you thought you had to...! I don't blame you."
                rose "That was paaaaaart of it, but it was when you -ng!- a-asked me out that it clicked!"
                mc "I really did regret it, y'know...."
                rose "F-fuck....! That's why I like you, [mcf]!"

                if w2RosaMean == True:
                    mc "Ha! And I like how you use that fat ass of yours!"
                    mc "Now shut up and get fucked!"
                if w2RosaCreative == True:
                    mc "Ha! If I knew you were such a sex-starved hag, I wouldn't have!"
                    mc "Now shut up and get fucked!"
                if w2RosaKind == True:
                    mc "To be honest, I'd do it again! It was worth it to get to fuck you like this."
            else:


                rose "Ah... ha....! It's funny! You turned me down the first time we met and now...!"
                mc "That's what led you to come to my apartment last week, am I wrong?"
                rose "That was part of it, but it was when you -ng!- a-asked me out that it clicked!"
                rose "-Ah! Still, you... r-realized that?"
                mc "I had a feeling that it made me look like an easy target."
                rose "D-don't put it that way...! You acted like a decent person that night! You left a stroooong impression...!"
                mc "Just for being decent?"
                rose "Sometimes \"just\" decent can make... -ah!- c-can make ALL the difference to a woman, ooooh!"
                rose "F-fuck...! Ah, fuck me! Are you a-angry that I tried to take advantage of your kindness?"
                mc "You saw an opening and took it...! I won't blame you for that."
                rose "Mmmh...! Thank you, [mcf]..."

                if w2RosaMean == True:
                    mc "Don't thank me yet, whore! I'm not done fucking you."
                if w2RosaCreative == True:
                    mc "Don't thank me yet! Save that for when I'm done fucking you!"
                if w2RosaKind == True:
                    mc "Don't thank me yet, Rose! We're not finished yet."


            mct "(Man, what I wouldn't give to see this from the outside...!)"
            mct "(She's like a waterfall. I can feel her juices dripping down my leg!)"
            "*Squick* *Smack...!* *Squelch* *Clap* *Sqewlch...!*"
            scene w2_2271 with vpunch
            rose "Ooooh, oooh...! Gyeh...!"
            scene w2_2270 with dissolve
            mc "Another one?"
            "Another climax threatened to send me dickhead first to my own end."
            rose "Geheh..."
            mc "You're on a short trigger."
            scene rosahometlift4_a with dissolve
            show rosahometlift4
            mc "{b}Good{/b}!"

            if w2RosaKind == True:
                mc "I wonder just how many times you'll cum before the evening's over."
            else:
                mc "I wonder just how many times you'll cream yourself before I pack your womb with my jizz?"

            rose "Eyeh... w-why...? It's still...!"
            "While her body shook and quivered from her last climax, I didn't dare stop."
            "I kept hammering into her convulsing hole over and over and over, parting the swollen lips of her lower mouth with a stringent and powerful rhythm."
            "*Squick* *Squelch* *Sqewlch...!*"
            rose "Ohwhff... owff... ng..."
            "*Squick* *Smack...!* *Squelch* *Clap* *Sqewlch...!*"
            rose "Ehyee..."
            "Every upward thrust had Rosalind sounding like a cheap, chewed up squeak toy."

            scene rosahometlift3_a with dissolve
            show rosahometlift3
            "This position meant I was doing the bulk of the work. All Rosalind really had the leverage to accomplish was to grind and press herself deeper into me every time my cock rose up to hit the deepest parts of her."
            "Which provided its own thrill in and of itself, but I was feeling the strain from holding the sex-starved mother up for so long."
            "A soreness had crept up my back and my legs were beginning to tremble from holding this pose for so long."
            "*Squick* *Squelch* *Sqewlch...!*"
            "My body was telling me to hurry and end this and the growing tightness in my testicles couldn't argue back."
            "*Squick* *Smack...!* *Squelch* *Clap* *Sqewlch...!*"
            "The desire to ejaculate and flood Rosalind's lower mouth with seed grew and grew, until..."

            menu w2RosaEjaculate2:
                "Give into the urge.":


                    if w2RosaMean == True:
                        mc "I'm about to blow. Where do you want it, whore?"
                        rose "Eh... ah... you... ha... c-can..."
                        "Drunk on dick, Rosalind struggled to get the words out of her mouth."
                        rose "Ah... ah...! You c-can...!"
                        mc "You want me to pick?"
                        rose "In-in--"
                        mc "Tell me!"
                        rose "{size=+10}[mcf]Insiiiiiiide!{size=+10}"
                        rose "It's safe, you can do it inside!"
                        mc "Then take it, you bitch!"


                    if w2RosaCreative == True:
                        mc "I'm about to pop. Where do you want my load, hag?"
                        rose "Eh... ah... you... ha... c-can..."
                        "Drunk on dick, Rosalind struggled to get the words out of her mouth."
                        rose "Ah... ah...! You c-can...!"
                        mc "Time's ticking!"
                        rose "In-in--"
                        mc "Spit it out!"
                        rose "{size=+10}[mcf]Insiiiiiiide!{size=+10}"
                        rose "It's safe, you can do it inside!"
                        mc "You got it! Take it, you slutty mother!"

                    if w2RosaKind == True:
                        mc "I'm about to cum. Where do you want it, Rose?"
                        rose "Eh... ah... you... ha... c-can..."
                        "Drunk on dick, Rosalind struggled to get the words out of her mouth."
                        rose "Ah... ah...! You c-can...!"
                        mc "Should I pull out?"
                        rose "In-in--"
                        mc "T-time's a bit tight here!"
                        rose "{size=+10}[mcf]Insiiiiiiide!{size=+10}"
                        rose "It's safe, you can do it inside!"
                        mct "(I was hoping you'd say that...!)"

                    "Having finally received a clear answer, I buried myself deep into Rosalind's quim - as far as I could humanly go, driven by the instinct to inseminate and color her insides white."
                    "I felt all sensation leave my legs as my body tensed up in preparation for my near immediate climax."
                    "My fingers sunk deep into the pliant, plump flesh of Rosalind's inner thighs as my hands squeezed her tight to make sure I had a proper hold on her."
                    stop ambient
                    stop music
                    scene w2_2279 with flash
                    play sound "sound effects/spurt.wav"
                    mc "Gh, aaaah-!"
                    "An automatic, animal-like growl and then complete and utter sensory bliss."
                    play sound "sound effects/spurt.wav"
                    rose "Ooooooh, oooooh!" with vpunch
                    scene w2_2280 with dissolve
                    "All tension in my body left me as I pushed rope upon rope of burning hot jizz through my urethra."
                    mc "--!"
                    scene w2_2281 with dissolve
                    mc "O-oh, shit!"
                    "Before I regained my composure, I witlessly laxed my grip and sent Rosalind tumbling face first into the table."
                    play sound "sound effects/thud-floor.mp3"
                    scene w2_2277 with vpunch
                    "Thud!"
                    rose "Ha...! Ha...! That was...!"
                    "Thankfully, she seemed not to mind."
                    rose "That was... ah..."
                    scene black with fade
                    $ renpy.end_replay()
                    if not persistent.roseW2KitchenSceneGallery:
                        play sound "sound effects/notification.wav"
                        show memoryunlock with dissolve
                        $ renpy.pause(3, hard=True)
                        $ persistent.roseW2KitchenSceneGallery = True
                        hide memoryunlock with dissolve
                        $ renpy.pause(0.5, hard=True)
                    "......"
                    "..."
                    rose "H-how long until you can go again?"
                    jump w2RosalindConclusion


                "{color=#FF1493}[[Tireless]{/color} Resist the urge as long as you can."(chg=["rosalind_passion_up"]) if trait_tireless == True:
                    $ Rosalind_Libido += 1
                    "Not yet!"
                    stop ambient
                    scene w2_2278 with fade
                    rose "Eh, whaa....?"
                    "Resisting all instinct to fill the wanton mother's sloppy hole with my jizz, I dropped the insensate woman onto the table in front of us."
                    rose "Eye... wh-what...? When did...?"
                    scene black with fade
                    "......"
                    "*Squick* *Squelch* *Sqewlch...!*"
                    rose "...geh! Ha...!"
                    jump w2RosalindTirelessFinish

                "{color=#696969}[[Tireless] Resist the urge as long as you can.{/color}" if trait_tireless == False:
                    jump w2RosaEjaculate2

        "{color=#696969}[[Strongman] Sweep Rosalind off her feet and onto your dick.{/color}" if perk_strongman == False:
            jump w2RosaIntensify




label w2RosalindTirelessFinish:

    play ambient "sound effects/boobjob-slow.wav"
    scene rosahometlay_a with dissolve
    show rosahometlay
    "I don't know how much time had passed. Not even ten minutes maybe, but it felt like longer."
    "After placing Rosalind in a more tenable position, I mustered my strength and got busy truly and wholeheartedly {b}plowing{/b} the half sensate mother."
    rose "Geh... wha... ha...!"
    "I no longer had the mental wherewithal to indulge in the dirty talk like Rosalind wanted, nor did she seem to be in a state to gleefully receive it."
    "Instead, all my diminishing focus went into pushing my cock in and out of Rosalind's embrace."
    mc "Eugh...! Eugh...!"
    mct "(Fucking a woman like Rosalind is hard work...!)"
    "*Squick* *Smack...!* *Squelch* *Clap* *Sqewlch...!*"
    mct "(She just accepts everything you throw at her and keeps on trucking.)"
    mc "Ha...! Ha...!"
    mct "(I don't think I could ever get sick of {i}this{/i}.)"
    mc "H-hey, ng-! Rose... are you okay down there?"
    rose "Ahmm... yee-yeeesh...! K-keep...!"
    "Drunk on dick, Rosalind struggled to get the words out of her mouth."
    rose "Keep going! Eheeyee...♥ F-fill meeee up!"
    rose "Keep gooing until yeeou fwhill me oop...! Ets Saaahf...!♥"

    if w2RosaMean == True:
        mc "You... ng-! Don't have to tell me that..."
        scene rosahometlay2_a with dissolve
        show rosahometlay2
        mc "I was going to anyway, slut!"
        rose "Ehyee...! Yes...!"
        mc "What's inside you?"
        rose "Dick!"
        mc "Whose dick?"
        rose "Y-yooours! [mcf]'s dehk..!"
    if w2RosaCreative == True:
        mc "Oh? Where did you want it?"
        rose "Enshiiiide...!"
        mc "Inside?"
        rose "Yesh! F-fill meeee up!"
        mc "Use your words!"
        rose "C-cum inside me, [mcf]! I want it inside...!"
        scene rosahometlay2_a with dissolve
        show rosahometlay2
        mc "You got it. Get ready to take my load, you slutty mother!"

    if w2RosaKind == True:
        mc "Music to my ears, Rose. If that's what you want..."
        scene rosahometlay2_a with dissolve
        show rosahometlay2
        mc "Ah...! I'm happy to oblige!"
        mc "Just relax. I'll give you what you want."
        rose "Ehe...♥"
        mc "I'll fuck every thought out of your head and replace it with sex."
        rose "T-thawnk... y-youuh...!"

    "Honestly, I was ready too. I had been for awhile."
    "My whole being was telling me to cum and I no longer had the spirit to resist."
    "*Squick* *Squelch* *Sqewlch...!*"
    "Throwing my back into it, I sped toward that conclusion."
    "*Squick* *Smack...!* *Squelch* *Clap* *Sqewlch...!*"
    "With one last thrust, I hilted myself fully in Rosalind's spasming hole, propelled forward by the instinct to drive myself as deep as possible into the constricting passage and make a direct deposit of spunk in her ovaries."
    "Every muscle of my body momentarily tensed up in preparation for my impending release, the fingers on my hands digging hard into the soft flesh of Rosalind's body, leaving a tangible mark of our copulation."
    "I felt all sensation leave my legs as my body tensed up in preparation for my near immediate climax. Then...!"
    stop ambient
    stop music
    play sound "sound effects/spurt.wav"
    scene w2_2282 with flash
    mc "Gh, aaaah-!"
    play sound "sound effects/spurt.wav"
    "White. Blinding white, as thick strands of cum made their way up and out my urethra and painted Rosalind's insides." with hpunch
    rose "Ooooooh, oooooh!"
    scene w2_2283 with hpunch
    play sound "sound effects/spurt.wav"
    "The sensation of being filled with warm goo must've been the final push she needed for one last climax. Her cunt greedily seized ahold of my dick, coaxing out every last drop of cum."
    "Then a feeling of dizzyness..."
    "Lightheadedness..."
    "and then..."
    scene black with fade
    play sound "sound effects/thud-floor.mp3"
    "*Thump.*"
    "I tumbled back onto the floor."
    mc "Ugh..."
    rose "[mcf]...!"
    scene w2_2284 with dissolve
    mc "Sorry..."
    scene w2_2285 with dissolve
    "When I regained my senses, Rosalind stood over me with a concerned expression, an affectionate hand on my body."
    "For the state she was in just a second ago, she had come to her senses surprisingly quick."
    mc "Just lost my balance there for a second..."
    scene w2_2286 with dissolve
    rose "Geez, you scared me..."
    rose "Next round, I should probably be on top."
    scene black with fade
    "Next... {w}round?"
    $ renpy.end_replay()
    "......"
    if not persistent.roseW2KitchenSceneGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.roseW2KitchenSceneGallery = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    "..."

    jump w2RosalindConclusion



label w2RosalindConclusion:

    $ renpy.music.set_volume(1, 0, channel = "ambient")
    "She was either incorrigible or simply trying to tame me through my cock. Either way..."
    scene w2_2287 with circlewipe
    "Along the way to wash up, we did it one more time in the living room."
    play sound "sound effects/shower.wav"
    scene w2_2288 with ccirclewipe
    "Then we made another mess in the shower."
    stop sound fadeout 2.0
    scene w2_2289 with bites
    play music "music/jazz-piano-bar.ogg"
    "Then once more in her bedroom, on the way back."
    rose "La da la... lada... ladalaa..."
    mc "*Afewh...* *Zheeee...*"
    rose "Freedom is just another word for nothing left to lose."
    mc "*Fweeooh*"
    rose "And feeling good was easy, Lord, when he sang the blues..."
    mct "(Ah...)"
    rose "Hmmm hmmm, la da la..."
    scene w2_2290 with dissolve
    mc "You have a nice singing voice, Rose."
    scene w2_2291 with dissolve
    rose "Heh, you fell asleep on me."
    scene w2_2290 with dissolve
    mc "How long was I out?"
    scene w2_2291 with dissolve
    rose "Oh, I don't know. Twenty minutes maybe...?"
    rose "I didn't want to disturb you. You looked so peaceful."
    scene w2_2290 with dissolve
    mc "You wore me out."
    scene w2_2291 with dissolve
    rose "I asked for too much today, didn't I?"
    rose "Thank you, [mcf]. For indulging me."
    scene w2_2292 with dissolve
    mc "Uh..."
    mct "(When she puts it like that, I feel...)"
    scene w2_2293 with dissolve
    mc "Well, we both enjoyed ourselves...."
    scene w2_2294 with dissolve
    rose "Aaaah.... "
    scene w2_2295 with dissolve
    "Rosalind let out a deep, contented sigh."
    "She was so warm and this felt so nice..."
    "I wanted to go right back to sleep."
    scene w2_2294 with dissolve
    rose "You did a great job today, hun."
    scene w2_2295 with dissolve
    mc "..."
    mct "(Shouldn't I be the one saying that?)"
    scene w2_2293 with dissolve
    mc "Aaaah..."
    scene w2_2295 with dissolve
    "I too, sighed contentedly. Right into Rosalind's inviting busom."
    scene w2_2293 with dissolve
    mc "I hope you got what you wanted out of that and I hope that I can fulfill my side of our arrang--"
    scene w2_2296 with dissolve
    rose "Don't worry your pretty little head about it."
    scene w2_2297 with dissolve
    "She pulled me tighter into her gentle embrace."
    scene w2_2298 with dissolve
    rose "Hmmm hmmm, la da la..."
    "...and began to hum once more in a soothing tone."
    rose "La dala... la da la..."
    "Normally my impression of her was of a stressed out dog, trembling in the rain. So for her to be feeling relaxed enough to shut her eyes and sing..."
    hide screen textbox2 with dissolve
    "It felt nice to catch a glimpse of this side of her."
    "The side that felt reassuring and was brimming with encouragement. A side that wasn't beaten down by the stress of the world."
    "I wanted to see more of it, in lights other than the bleariness of post-coital bliss."
    scene w2_2290 with dissolve
    mc "Hey, Rose..."
    scene w2_2291 with dissolve
    rose "Yeah, hun?"
    scene w2_2290 with dissolve
    mc "Could you... sing that whole song to me, from the top?"
    mc "I enjoy hearing your voice."
    scene w2_2299 with dissolve
    rose "When you put it so bluntly, it's embarrassing you know."
    rose "Now I'm feeling self-conscious."
    scene w2_2300 with dissolve
    mc "Please, would you do it for me?"
    scene w2_2301 with dissolve
    rose "..."
    scene w2_2291 with dissolve
    rose "Of course, [mcf]. I'd be happy to."
    scene w2_2302 with dissolve
    rose "Busted flat in Baton Rouge, waitin' for a train~"
    mct "(Mmh...)"
    rose "When I's feelin' near as faded as my jeans~"
    scene w2_2303 with dissolve
    "As soon as she begun in earnest, the drowsiness that had a hold of me became more pronounced."
    rose "Bobby thumbed a diesel down just before it rained~"
    stop music fadeout 3.0
    "I felt myself slipping."
    rose "And rode us all the way into New Orleans~"
    scene black with fade
    "Slipping to more nostalgic days."
    scene w2_2304 with pixellate
    play music "music/ill-remember-you.ogg"
    vic "Suzanne takes you down to her place near the river~"
    vic "You can hear the boats go by, you can spend the night beside her~"
    vic "And you know that she's half-crazy but that's why you want to be there~"
    scene w2_2305 with dissolve
    vic "And she feeds you tea and oranges that come all the way from China~"
    vic "And just when you mean to tell her that you have no love to give her~"
    scene w2_2306 with dissolve
    vic "Then she gets you on her wavelength~"
    vic "And she lets the river answer that you've always been her lover~"
    scene black with fade
    stop music fadeout 3.0
    "......"
    "..."

    if date == "june09day":
        jump w2HanaNight1
    else:
        jump w2HanaNight2



label w2VeronicaGymStart:
    stop sound
    play music "music/doll-dancing.ogg"
    scene w2_2307 with dissolve

    if date == "june09day":
        ver "...listen, there's no need to get... there's no need to get mean about it."
    else:
        ver "...listen, there's no need to get... there's no need to get mean about it. I told you yesterday!"

    ver "I had the courtesy to RSVP no, I don't owe you an explanation beyond that."
    play ambient "sound effects/call-waiting.wav"
    scene w2_2308 with dissolve
    ver "...Ah!"
    ver "{size=-10}Thank go--{/size=-10}"
    scene w2_2307 with dissolve
    stop ambient
    ver "No, I am happy for you! I just--"
    scene w2_1778 with dissolve
    mct "(Is she not going to pick up? I guess I could just go down there if I had to.)"
    mct "(It's where she lives anyway.)"
    if date == "june09day":
        mct "(Or I could call Rosalind, I guess...)"
    scene w2_2309 with vpunch
    ver "Jesus! Why do you want to open old wounds?"
    scene w2_2310 with dissolve
    ver "Listen...! I've got an important call on the other line and, truthfully, I don't really want to discuss this any further with you."
    scene w2_2311 with dissolve
    ver "I'm not coming. That's the bottom line, I'm... I'm sorry. I hope everything works out the best for you."
    play sound "sound effects/phonemenu.wav"
    scene w2_2312 with dissolve
    ver "What do you want?"
    scene w2_2313 with dissolve
    "The voice on the other end sounded a lot more annoyed than I expected, which was saying something considering the speaker."
    scene w2_1772 with dissolve
    "I feared this would be a portent of things to come, if this was how she answered a mere phone call."
    hide screen textbox2 with dissolve

    menu:
        "Move onto the business at hand.":

            scene w2_1779 with dissolve
            show screen textbox2 with dissolve
            mc "I have club business with you."
            mc "Business that has to be taken care of in the near immediate future. Are you in a position to talk?"
            scene w2_1778 with dissolve
            ver "...yeah, I am. I guess."
            ver "What kind of business?"
        "Ask if everything is okay."(chg=["veronica_up"]):


            $ Veronica_Affection +=1
            scene w2_1771 with dissolve
            show screen textbox2 with dissolve
            mc "You sound upset, is everything okay?"
            scene w2_1772 with dissolve
            ver "Oh yeah, just peachy. Taking a phone call from my pimp."
            scene w2_2313 with dissolve
            mc "I guess that's a strong \"no\" then."
            scene w2_2314 with dissolve
            ver "..."
            scene w2_2323 with dissolve
            ver "Yeah, I'm sorry. I'm not in a good mood right now, but I shouldn't take it out on you."
            ver "It does neither of us any good."
            scene w2_2324 with dissolve
            mc "Do you want to talk abou--"
            scene w2_2317 with dissolve
            ver "No. The one thing I DEFINITELY don't want to do is spill my guts."
            scene w2_2321 with dissolve
            mc "Hehe, yeah. I expected as much, but I thought I'd ask."
            scene w2_2322 with dissolve
            ver "Moving on... I'm guessing you have something to tell me?"
        "Tell her to tone it down."(chg=["veronica_up"]):


            $ Veronica_Affection +=1
            scene w2_1781 with dissolve
            show screen textbox2 with dissolve
            mc "Do you always answer the phone like a moody teenager or should I feel special?"
            scene w2_1780 with dissolve
            ver "Don't start with me. I'm not in the mood."

            if w1VeroGonzo == True or mod_week1_interview:
                scene w2_1781 with dissolve
                mc "I can tell, but in your own words from last week..."
                ver "Now I've had time to compartmentalize what I have to do. No point in making a thing like this difficult, is there?"
                scene w2_1780 with dissolve
                ver "...ah, whatever. Let's start over from the top then."
            else:
                scene w2_1781 with dissolve
                mc "I know, but there's no need to let that affect our working relationship. A little civility goes a long way."
                scene w2_1780 with dissolve
                ver "Civil...? Ha! That's a funny word for our dynamic, but let's start over from the top then."

            scene w2_2319 with dissolve
            ver "*Breeeng, beeeeng*"
            "Veronica crudely imitated the sound of a rotary telephone."
            scene w2_2320 with dissolve
            ver "Hello, sir. How can I help you?"
            scene w2_2318 with dissolve
            mc "I'm not telling you to kiss my ass, I was just saying--"
            scene w2_2316 with dissolve
            ver "Stop being a giant bitch?"
            scene w2_2318 with dissolve
            mc "...I was just saying, let's get along."
            scene w2_2316 with dissolve
            ver "Get along? Yeah... ok. I can do that."
            scene w2_2313 with dissolve
            mc "You can keep up the \"sir\" part if you really want to though. I don't mind."
            scene w2_2309 with dissolve
            ver "The funny thing about that is I've really got no clue if you're joking or not."
            scene w2_2321 with dissolve
            mc "Take it either way."
            scene w2_2322 with dissolve
            ver "Now... Why did you call, {b}sir{/b}?"


    scene w2_1779 with dissolve
    mc "The mission Mrs. Pulman mentioned Monday, you remember it?"
    scene w2_1778 with dissolve
    ver "Yeah, it was vague as hell, which worries the shit out of me. Probably part of that bitch's plan."
    scene w2_1779 with dissolve
    mc "The mission for you is an impromptu photo shoot at your gym."
    scene w2_2309 with dissolve
    ver "A photo shoot?"
    scene w2_2314 with dissolve
    mc "You know damn well what that means."
    scene w2_2315 with dissolve
    ver "...ah, fuck. I do."
    ver "...and we're doing THAT today?"
    scene w2_2314 with dissolve
    mc "You got it. You and I are going to take some pictures. Are you free?"
    scene w2_2309 with dissolve
    ver "As free as I'll ever be, I guess..."
    scene w2_2317 with dissolve
    ver "The thing is, I can't exactly close my doors. I have regulars who--"
    scene w2_2318 with dissolve
    mc "I think Mrs. Pulman expects the place to be open when we take it."
    mct "(Not that I was sure she'd know...)"
    scene w2_2309 with dissolve
    ver "On the plus side, that replaces my first concern. On the other hand, it's replaced with an even worse one."
    scene w2_2317 with dissolve
    ver "I can't just prance around my gym naked, you know that?"
    scene w2_1771 with dissolve
    mc "I know. We'll be careful, I promise. I'm not intending either of us to be branded as weirdo sex perverts."
    scene w2_1779 with dissolve
    mc "If anyone asks why there's a man with a camera around, just explain to them that I'm there to photograph a former Olympian."
    mc "The more risque business, we'll try and snag all incognito like."
    scene w2_1778 with dissolve
    ver "*sigh* I don't know about this, errand boy."
    scene w2_1779 with dissolve
    mc "If it helps, I'm told it's tied to your performance this weekend."
    scene w2_2323 with dissolve
    ver "That means...?"
    scene w2_2324 with dissolve
    mc "The boss was pretty vague about it. Just that there will be a ranking based off each of the shoots."
    scene w2_2312 with dissolve
    ver "She loves turning everything into a stupid game, doesn't she?"
    scene w2_2313 with dissolve
    mc "That is what this whole month ultimately is."
    scene w2_2315 with dissolve
    ver "*Sigh* If that's what the old bitch wants, fine! However, what I say goes today."
    scene w2_2317 with dissolve
    ver "I'm not doing anything that'll jeopardize my reputation."
    scene w2_2318 with dissolve
    mc "That's reasonable. We'll take some photos and see what we can get away with."
    mc "Worst comes to worst, the old lady will have to be satisfied with what she gets. Does that sound good?"
    scene w2_2316 with dissolve
    ver "...yes, I suppose it does."
    scene w2_1778 with dissolve

    if minaGym == True:
        ver "I've got a personal training session in an hour, so be here in two."
    else:
        ver "I'll be here all day. You can come down whenever you want."

    scene w2_1779 with dissolve
    mc "By the way, workout clothes get pretty skimpy, right?"
    mc "Make sure that's the case today--"
    play sound "sound effects/phonemenu.wav"
    stop music
    scene w2_1762 with dissolve
    "*Beep*"
    "Without so much as a goodbye, Veronica disconnected from our brief call."
    "When you got down to brass tacks, I wasn't sure how exactly this was going to go."
    scene w2_2325 with dissolve

    if date == "june09day":
        "For Rosalind's shoot tomorrow, we'll have a lot of space to work with. But an indoor gym..."
    else:
        "In Rosalind's case, we had a lot of space to work with in a park. But an indoor gym..."

    "This one will have to be played by ear."
    scene black with fade
    "......"
    "..."
    if minaGym == True:
        jump w2VeronicaGymMinaIntro
    else:
        jump w2VeronicaGymIntro

label w2VeronicaGymMinaIntro:

    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionveronica04 with blinds
    $ renpy.pause(6, hard=True)

    scene w2_2326 with blinds
    show screen qmenu with dissolve
    show screen textbox2 with dissolve
    "A couple of hours later, I was nearing the gym."
    mina "Nine....!"
    play music "music/ukulele-fun.ogg"
    scene w2_2327 with cmet
    mina "Eeeehh, ten...!"
    play sound "sound effects/thud-floor.mp3"
    scene w2_2328 with vpunch
    ver "You've got one more set."
    scene w2_2329 with dissolve
    mina "Aaaah, I'm pooped! I don't know if I can do any more."
    scene w2_2328 with dissolve
    ver "You have another set in you. I know you do."
    ver "You said the same thing in our first session, but it was a whole set earlier."
    scene w2_2329 with dissolve
    mina "Did I...?"
    scene w2_2328 with dissolve
    ver "You did. You've already made progress. So keep at it a little longer."
    ver "One more set. Ten reps, ten seconds each."
    scene w2_2330 with dissolve
    ver "Do it for me? Please?"
    scene w2_2331 with dissolve
    mina "Hehe, yeah... I can do one more set!"
    scene w2_2332 with dissolve
    mina "Ah, my thighs...!"
    scene w2_2333 with dissolve
    ver "Watch your posture. If you don't do it right, you won't get the full benefit of the exercise. We only have so many waking hours. It's important you squeeze every last drop out of them."
    ver "No sense in wasting time, right Mina?"
    scene w2_2334 with dissolve
    mina "Right, Coach!"
    scene w2_2335 with dissolve
    ver "I don't know why you insist on calling me that. Veronica is fine. Or even just Vera."
    scene w2_2336 with dissolve
    mina "I don't know... it just seems fitting to me. Do you mind?"
    scene w2_2335 with dissolve
    ver "No, you can call me what you want."
    scene w2_2336 with dissolve
    mina "Good, because I'm quite fond of it for some reason!"
    scene w2_2337 with dissolve
    ver "You're sort of weird, aren't you?"
    scene w2_2338 with dissolve
    mina "Eheh, I'm weird?"
    scene w2_2337 with dissolve
    ver "Not in a bad way. I'm pretty weird too."
    scene w2_2338 with dissolve
    mina "If you're weird, then I'm happy to be included in that."
    scene w2_2339 with dissolve
    ver "..."
    scene w2_2340 with dissolve
    mina "So, what's this supposed to strengthen again?"
    scene w2_2341 with dissolve
    ver "This one also improves your pelvic floor muscles."
    scene w2_2342 with dissolve
    mina "W-wait, kegels?"
    scene w2_2343 with dissolve
    ver "That's right."
    scene w2_2342 with dissolve
    mina "Isn't that... {i}for sex{/i}? There was an article about it in a magazine I modeled for one time..."
    scene w2_2344 with dissolve
    ver "It also helps with incontinence, but... yeah. It can improve your sexual health too."
    ver "That's just an added benefit. Stretching is an important part of any post workout routine."
    scene w2_2338 with dissolve
    mina "How does it... how does it improve your sexual health?"
    scene w2_2345 with dissolve
    ver "Curious about that?"
    scene w2_2339 with dissolve
    mina "Maybe a little..."
    scene w2_2344 with dissolve
    ver "Well... for one, it can make it easier to orgasm."
    scene w2_2338 with dissolve
    mina "Really?! It can do something like that?!"
    scene w2_2346 with dissolve
    ver "Ummhmm. It increases blood flow to your vagina, which makes it easier to get aroused."
    ver "It can also let you learn to better control your muscles down there, which can make things more {i}\"fun\"{/i} for you and your partner."
    scene w2_2347 with dissolve
    mina "Control down there?"
    ver "Yeah, think about how you flex your muscles when you want to pee. With enough kegels..."
    scene w2_2348 with dissolve
    ver "You might even be able to {i}grip{/i} things."
    scene w2_2349 with dissolve
    mina "Things...? O-oh! You mean..."
    scene w2_2350 with dissolve
    ver "Yeah, more fun for you and your partner."
    scene w2_2351 with dissolve
    mina "Hehe, that's amazing! Isn't exercise great?"
    scene w2_2352 with dissolve
    ver "Exercise is the most important investment you'll ever make in yourself. A healthy body extends to all aspects of your life."
    scene w2_2353 with dissolve
    ver "It strengthens you physically and helps you live a longer life, but it's also a mental thing. You form good habits, you build a good work ethic..."
    scene w2_2352 with dissolve
    ver "If you let it, it'll extend to all facets of your life. Work and personal life included."
    scene w2_2339 with dissolve
    mina "You know, you kinda sound like this is your job!"
    scene w2_2354 with dissolve
    ver "No shit?"
    scene black with fade
    $ renpy.music.set_volume(.1, 2, channel = "music")
    mc "Hmmm..."
    play sound "sound effects/locker-close.wav"
    scene w2_2355 with w20
    "*Clank*"
    "I wasn't expecting to see Mina here, but I DID get her to sign up last week."
    scene w2_2356 with dissolve
    mct "(She must be that appointment Veronica mentioned on the phone, which hopefully means she'll be leaving soon.)"
    mct "(I should leave the camera in my locker. She'd most likely ask about it...)"
    "On the plus side, it's not really that busy. So, that's good."
    "That'll make it easier to get the sort of shots Mrs. Pulman expects."
    scene w2_2357 with dissolve
    mct "(Hmm...)"
    scene w2_2358 with dissolve
    "This place is huge."
    "Really, {i}really{/i} huge, with a ton of facilities."
    "The overhead for this place must be massive. I'm surprised Samson even had to do anything."

    if VeroFlag == True:
        mct "(I should probe Veronica later and get some details about their relationship.)"
    else:
        mct "(I'm staying out of it, but still...)"

    mct "(That bastard...)"
    scene w2_2359 with dissolve
    "That's not important right now, though."
    scene black with fade
    mct "(Let's go say hello.)"
    $ renpy.music.set_volume(1, 2, channel = "music")
    scene w2_2360 with circlewipe
    ver "Good hustle today."
    scene w2_2361 with dissolve
    mina "Thanks, Coach!"
    scene w2_2362 with dissolve
    ver "It makes sense you're a model. You're pretty fit already."
    scene w2_2363 with dissolve
    mina "What's it been...? I've worked out regularly for a few years now."
    scene w2_2362 with dissolve
    ver "What made you switch gyms?"
    scene w2_2364 with dissolve
    mina "My last place sucked. Their facilities were always out of order, it was pretty dirty, and the membership was largely men who couldn't keep their eyes to themselves."
    mina "I mean.. I don't mind a glance, it's part of looking good, but don't stare a hole in a girl."
    scene w2_2365 with dissolve
    ver "You don't have to worry about that here. I don't let anyone join who's not serious."
    scene w2_2366 with dissolve
    mina "Hehe, don't think I forgot your speech last week. You put [mcf] and I through the wringer."
    scene w2_2367 with dissolve
    ver "[mcf]..."
    ver "How well do you know that kid?"
    scene w2_2368 with dissolve
    mina "I've only known him for about a month, but..."
    mina "He's great. He's been helping me with my acting."
    mina "Why do you ask?"
    scene w2_2369 with dissolve
    ver "I was just curious. I like to get to know anyone who becomes a member here."
    scene w2_2370 with dissolve
    mina "Anyway, I'm really happy I found this place! You're tougher than my last trainer, but I look up to you."
    mina "I get to brag I'm being trained by a silver medalist! That's cool! SO cool!"
    scene w2_2371 with dissolve
    ver "Ah, well... that's in the past."
    scene w2_2369 with dissolve
    ver "I prefer to look forward. I know my share of athletes that get caught up in reliving past glories."
    ver "They stop pushing themselves and become complacent. Don't get me wrong, I'm proud of my accomplishment, but I'd just as soon not have done them if it means becoming stagnant as a person."
    scene w2_2372 with dissolve
    mina "Yep! I'm very glad to have found this gym."
    ver "Thanks..."
    scene w2_2373 with dissolve
    ver "Speak of the devil..."
    mina "Oh...!"
    scene w2_2374 with dissolve
    mina "[mcf]...!"
    "Just as soon as I entered, Mina gave me an emphatic and warm greeting, the sort that said she was excited to see me. The kind that made you feel unequivocally welcome."
    "Truly a talent of hers."
    mc "Hey!"
    scene w2_2375 with hpunch
    mc "How's it going?"
    mina "Tired, but happy to see you!"
    mina "It feels like it's been forever!"
    mc "What are you talking about?"
    scene w2_2376 with dissolve

    if date == "june09day":
        mc "I just saw you yesterday."
    else:
        mc "I saw you like a day and a half ago."

    mina "So? Still feels like a long time to me!"
    "{b}Truly{/b} a talent of hers."
    mina "Ehehe..."
    scene w2_2377 with dissolve
    mc "How are you?"
    scene w2_2378 with dissolve
    ver "Could be better. Could be worse."
    ver "I'm happy to see my two most recent members take their health seriously."
    scene w2_2379 with dissolve
    mina "You're here to work out?"
    scene w2_2380 with dissolve
    ver "Why else would he be here?"
    "Veronica gave me a knowing, painfully ironic look."
    scene w2_2377 with dissolve
    mc "Ah, yep. Thought I'd make full use of the free time I had on my hands and get a workout in."
    scene w2_2378 with dissolve
    ver "That's admirable. Making full use of your free time."
    scene w2_2381 with dissolve
    mc "Is it...? I just get antsy sitting on my hands."
    scene w2_2378 with dissolve
    ver "Oh yeah, plenty people are just content sitting around and doing nothing when they're not working."
    scene w2_2382 with dissolve
    ver "There's a serious health epidemic in this country. It's a good thing you're {b}here to work out{/b}."
    scene w2_2383 with dissolve
    ver "Why don't you get started, then? I've got to type up and print out some benchmarks for Mina. As well as go over a few things."
    ver "That'll take some time so..."
    scene w2_2384 with dissolve
    ver "Make full use of it."
    scene black with fade
    stop music fadeout 3.0
    mc "Sure, that is WHY I'm here..."
    "......"
    "..."
    scene w2_2385 with fade
    "Thirty-five minutes later..."
    mc "Ha... Ha..."
    "To keep up appearances with Mina, I had earnestly thrown myself into a workout, which is probably what Veronica was counting on."
    mct "(Veronica's being slow on purpose, isn't she?)"
    scene w2_2386 with dissolve
    mct "(Well, on the plus side...)"
    "The place has thinned out even more."
    scene w2_2387 with dissolve
    play music "music/cold-sober.ogg"
    ver "Hard at work?"
    "While I was lost in thought, Veronica had appeared next to me with a triumphant look on her face."
    scene w2_2388 with dissolve
    mc "You look pretty pleased with yourself."
    scene w2_2389 with dissolve
    ver "What can I say? I make my own fun."
    ver "If you're going to take lewd photos of me soon, I might as well bust your ass beforehand."
    scene w2_2390 with dissolve
    ver "Not quite equitable, but I'll take what I can get. If you're mad about it..."
    scene w2_2412 with dissolve
    "Veronica quickly closed the gap between us, with a perplexingly fierce and sly look on her face."
    scene w2_2411 with dissolve
    ver "If you're mad about it, you can get payback for it later."
    scene w2_2391 with dissolve
    mc "You mean during the photo shoot?"
    scene w2_2392 with dissolve
    ver "Well, we should do our best..."
    scene w2_2393 with dissolve
    "{i}Right{/i}. Her performance is tied to this."
    scene w2_2391 with dissolve
    mc "I'm not mad. I do pay dues here. I should use the place."
    mc "Did Mina leave?"
    scene w2_2390 with dissolve
    ver "She had to rush off somewhere, but she told me to tell you good-bye."
    scene w2_2392 with dissolve
    ver "There was A LOT more energy behind it, but you're not getting that from me."
    scene w2_2391 with dissolve
    mc "I can imagine."
    scene w2_2390 with dissolve
    ver "She actually yakked quite a bit about you after we parted. For some reason, I think she may genuinely like you."
    scene w2_2413 with dissolve
    mc "Maybe she's a good judge of character."
    scene w2_2392 with dissolve
    ver "At the age of nineteen? That's highly unlikely."
    scene w2_2393 with dissolve
    "Actually, I couldn't argue with that, considering the disrespect she puts up with from Ian."
    scene w2_2394 with dissolve
    mc "...hmm."
    mc "What about Samson?"
    scene w2_2395 with dissolve
    ver "What about that bastard?"
    scene w2_2396 with dissolve
    mc "Were you a good judge of his character?"
    scene w2_2397 with dissolve

    if VeroFlag == True:
        "I wanted to get her take on the washed-up actor."
    else:
        "Even if I wasn't going to get involved with Veronica's problem, I was still a little curious."

    scene w2_2395 with dissolve
    ver "Are you implying something?"
    scene w2_2396 with dissolve
    mc "No, I was just wondering what your initial impressions of the man were. You did enter a business relationship with him. His face is plastered all over your walls."
    scene w2_2398 with dissolve
    mc "Surprised you still have those up, actually..."
    scene w2_2399 with dissolve
    ver "Ack, don't fucking mention that! I'd rip them down, but I'd be in breach of our contract if I did."
    scene w2_2396 with dissolve
    mc "So, what did you first think of him? You know, before you had knowledge of the Carnation Club."
    scene w2_2395 with dissolve
    ver "What did I think? I thought he was an asshole. Just a {b}normal{/b}, run-of-the-mill narcissistic asshole."
    ver "Not exactly unheard of in the bodybuilder world. I'm used to dealing with them."
    scene w2_2396 with dissolve
    mc "Run-of-the-mill?"
    scene w2_2395 with dissolve
    ver "Yeah. Really into himself. The kind who doesn't really listen and is instead just waiting for his turn to talk."
    ver "The type of man who always makes the conversation about himself, no matter what the topic is. Annoying, but harmless..."
    scene w2_2399 with dissolve
    ver "{b}Seemingly{/b} harmless, at least. Obviously my opinion has shifted on that predatory bastard."
    scene w2_2396 with dissolve
    mc "How did you first meet him?"
    scene w2_2400 with dissolve
    ver "Why the hell do you care? You're asking a lot of questions."

    if VeroFlag == True:
        scene w2_2398 with dissolve
        mc "To be honest, I'm curious. I don't like the asshole either and quite frankly..."
        mc "I think he may have done something to hasten the situation you're in."
        scene w2_2397 with dissolve
        "I KNEW he did, but saying as much would be overplaying my hand. If she reacted poorly, it could make my position at the club tenuous."
        scene w2_2401 with dissolve
        mc "You don't think it's coincidental that the man you're in a business relationship with just happened to have a convenient out for you?"
        scene w2_2402 with dissolve
        ver "Don't think I haven't made a connection there errand boy, but my financial troubles with this place largely predate meeting him."
        scene w2_2403 with dissolve
        ver "It's more likely he just saw an opportunity when we first met and inserted himself in the situation. All he had to do was wait and dangle the club in front of me."
        scene w2_2401 with dissolve
        "That would make sense. If what she's saying is true, why would Samson do anything when he didn't have to?"
        mct "(Except he point-blank admitted to having a hand in it. Was he lying to impress the other patrons?)"
        scene w2_2875 with dissolve
        "In Lucy's case, that slimy bastard Isaak just had to wait like a trapdoor spider and let the women come to him. Every year, a new batch of students with hopeful mothers."
        scene w2_2876 with dissolve
        "You would think the same would be true of Samson's sponsorship of Veronica. A famous bodybuilder like him must get a lot of business inquiries. He would just have to wait for someone perfect to fall into his lap."
        scene w2_2877 with dissolve
        "...but how many gym owners are even women? On top of that, how many are beautiful and fierce like Veronica, the type that would be fun to break down and humiliate?"
        mct "(No. He wasn't lying. He definitely had a hand in it and I'm going to root out what he did.)"
        scene w2_2401 with pixellate
        mc "Still, how did you two meet?"
        scene w2_2402 with dissolve
        ver "At an industry show for gym equipment he was promoting."
        ver "I approached him, we got some drinks. I got drunk and a little too loose-lipped with my troubles..."
        ver "Eventually the topic of using a spokesperson to drum up business was broached."
        scene w2_2401 with dissolve
        mc "By you or him?"
        scene w2_2403 with dissolve
        ver "Uh... I don't remember, but I can see what you're getting at. It's not like he came cheap, but hiring him was actually successful. It got memberships up."
        scene w2_2402 with dissolve
        ver "Trust me, I've mulled this over a thousand times. It's a natural conclusion to reach for, but there's no way he's responsible for the money this place is hemorrhaging."
        scene w2_2404 with dissolve
        ver "I'm just a bitch with a bad business sense. I wish I could put the blame on someone else."
        scene w2_2405 with dissolve
        "Veronica looked utterly ripped open for the briefest moment, guts laid bare."
        "I was still certain he did something, but..."
        scene w2_2406 with dissolve
        mc "Sorry, it was just a random thought I had."
        scene w2_2407 with dissolve
        ver "No it's okay. For someone whose paycheck depends on exploiting me, you sounded genuinely concerned."
        ver "So, thanks. I guess."
        scene w2_2401 with dissolve
        mc "I don't like the idea of people's dreams being fucked with."
        scene w2_2408 with dissolve
        ver "..."
        scene w2_2407 with dissolve
        ver "So, just a half an hour workout today? You wanna go for an hour?"
        scene w2_2408 with dissolve
        mc "VERY funny. I'm going to go get my camera."
        mc "We'll see about that payback."
        scene black with fade
        stop music fadeout 3.0
        "......"
        "..."
        jump w2VeronicaGymphotoshoot
    else:

        scene w2_2398 with dissolve
        mc "Ah, yeah. You're right. It's none of my business."
        scene w2_2397 with dissolve
        "I'm staying out of it."
        scene w2_2409 with dissolve
        ver "..."
        scene w2_2395 with dissolve
        ver "Just a half an hour workout today? You wanna go for an hour?"
        scene w2_2410 with dissolve
        mc "VERY funny. I'm going to go get my camera."
        mc "We'll see about that payback."
        scene black with fade
        stop music fadeout 3.0
        "......"
        "..."
        jump w2VeronicaGymphotoshoot


label w2VeronicaGymIntro:

    scene w2_2414 with blinds
    show screen qmenu with dissolve
    show screen textbox2 with dissolve
    "A couple of hours later, I was nearing the gym."
    scene w2_2415 with dissolve
    mct "(Hmmm, where is she...?)"
    woman "*{size=-10}Grunts* Ah...!{/size=-10}"
    scene w2_2416 with dissolve
    mct "(Maybe I should give her a call?)"
    woman "{size=-5}*Grunts* Fweeeh!{/size=-10}"
    scene w2_2417 with dissolve
    mc "There she is..."
    play music "music/jack-the-lumberer.ogg"
    hide screen textbox2 with dissolve
    scene veroglift1_a with dissolve
    show veroglift1
    $ renpy.pause(7.5, hard=True)
    scene veroglift2_a with dissolve
    show veroglift2
    show screen textbox2 with dissolve
    "Veronica was off to the side, doing one bicep curl after another."
    "One..."
    "Two..."
    "Three..."
    "She not only made it look effortless, but she made it look good."
    "A couple of the gym rats must've thought so too, as they put a pin in their own routine and gathered nearby to watch the Amazon work."
    "Her biceps bulged and her body glistened with an attractive veneer of sweat."
    "At the peak of every arc, the curl bar would brush past the obstacle of the Amazon's prodigious bust, resulting in a pleasantly repetitive jiggle that showed no signs of slowing down."
    scene veroglift3_a with dissolve
    show veroglift3
    ver "[mcf]. Ah, there you are."
    "She addressed me with no signs of stopping."
    ver "I had some free time waiting for you, so I thought I'd let off some steam."
    "I was reminded of how on edge she sounded on the phone earlier. Did something happen?"
    mc "This is how you decompress?"
    ver "Of course. Just one of the many, many benefits of exercise."
    mc "Yeah, but it's also like your job."
    ver "I have the fortune of doing what I love."
    scene w2_2418 with dissolve
    ver "Plus, it's not like it's the only way I relieve stress. If you know what I mean..."
    play sound "sound effects/thud-heavy.wav"
    scene w2_2419 with vpunch
    "Veronica shot me a lecherous grin, smiling ear to ear with her insinuation."
    scene w2_2420 with dissolve
    ver "...and I think you do."
    scene w2_2421 with dissolve
    "Asked and answered her own question. For most people, that would come off as obnoxious, but not her."
    scene w2_2422 with dissolve
    ver "What do you do for fun, errand boy?"
    scene w2_2421 with dissolve
    mc "Woah, are you actually asking me a personal question?"
    scene w2_2422 with dissolve
    ver "...yes?"
    scene w2_2421 with dissolve
    mc "Hmm, well I..."
    hide screen textbox2 with dissolve

    menu:
        "Tell her you like to study"(chg=["veronica_up"]):
            $ Veronica_Affection +=1
            scene w2_2423 with dissolve
            show screen textbox2 with dissolve
            mc "I like to brush up on past material for tests, I guess."
            scene w2_2429 with dissolve
            ver "You mean you study? I meant what do you do to relax."
            scene w2_2423 with dissolve
            mc "Study and review. It makes me feel better."
            scene w2_2425 with dissolve
            ver "You study to.... relax?"
            scene w2_2424 with dissolve
            mc "That probably sounds weird, but look at it this way: I've got a goal."
            scene w2_2426 with dissolve
            ver "I remember. You want to be a doctor."
            scene w2_2423 with dissolve
            mc "I haven't reached it yet and every second I spend sitting on my hands is just added inertia dragging me down."
            scene w2_2425 with dissolve
            ver "That sounds unhealthy. Rest is an important part of learning, just as it is with exercise."
            scene w2_2423 with dissolve
            mc "I recognize that, but it's not like I'm going one hundred percent all the time. It's not like I don't ever veg out either."
            scene w2_2424 with dissolve
            mc "But on the whole, I just find that keeping busy helps me feel comfortable. Prevents me from feeling restless."
            scene w2_2429 with dissolve
            ver "...hmm, you said it probably sounded weird, but I get it. The desire to keep moving."
            scene w2_2427 with dissolve
            ver "Speaking from experience, it has its ups and downs."
            scene w2_2423 with dissolve
            mc "Are you giving me advice?"
            scene w2_2429 with dissolve
            ver "Don't read anything into it, errand boy. Force of habit from my job, I guess."
            scene w2_2423 with dissolve
            mc "No, too late. I'm going to chalk it up to you and I developing a rapport."
            scene w2_2428 with dissolve
            ver "Oh, if that's the case... do you want to join me?"
        "Tell her you like to watch movies.":

            scene w2_2423 with dissolve
            show screen textbox2 with dissolve
            mc "When I'm not studying, I guess I watch a lot of movies."
            scene w2_2425 with dissolve
            ver "Really? That's kinda... basic, don't you think?"
            scene w2_2423 with dissolve
            mc "I wasn't trying to impress you."
            scene w2_2426 with dissolve
            ver "Oh, I didn't mean to sound like a bitch, but it's like saying you like music, right?"
            scene w2_2427 with dissolve
            ver "Doesn't everyone?"
            scene w2_2423 with dissolve
            mc "Sure, everyone likes movies and music, but for most people it's a matter of function."
            scene w2_2424 with dissolve
            mc "You watch something to turn your brain off for a couple of hours and then rarely think about it again."
            scene w2_2423 with dissolve
            mc "Same with music. Everyone {i}likes{/i} music, but then you can be {b}into{/b} music."
            scene w2_2426 with dissolve
            ver "So you think about movies a lot then?"
            scene w2_2423 with dissolve
            mc "Ah, well... not as much as some people I know. My mom is more of the cinema is art type, I just really like to watch things explode and see poorly shot dummies fall off of buildings."
            scene w2_2425 with dissolve
            ver "Sorry, I guess. I didn't mean to belittle your interests."
            scene w2_2424 with dissolve
            mc "Nah, I'm actually pretty psyched you asked. I didn't really expect any sort of personal question coming from you."
            scene w2_2429 with dissolve
            ver "Are you implying something?"
            scene w2_2423 with dissolve
            mc "No, not at all! I'll just chalk it up to you and I building a rapport."
            scene w2_2428 with dissolve
            ver "Is that what you think we're doing? In that case, would you like to join me right now?"


    scene w2_2423 with dissolve
    if perk_strongman == True:
        mc "Doing bicep curls? Fat chance. I haven't done any weight training since high school."
    else:
        mc "Doing what you're doing? You're making fun of me."

    scene w2_2427 with dissolve
    ver "No. Just get a workout in, before our \"business\" today."
    scene w2_2429 with dissolve
    ver "You are a member of this gym. You promised you'd be serious about it. Was that just bullshit?"
    scene w2_2430 with dissolve
    mc "Hmm..."

    if kat_polite == True:
        mct "(Should I get a work out in? There's Mrs. Pulman's twisted mission, but...)"
    else:
        mct "(Should I get a work out in? There's Kathleen's twisted mission, but...)"

    mct "(What else am I doing today?)"
    scene w2_2423 with dissolve
    mc "Why not?"
    scene w2_2431 with dissolve
    ver "Good. Then you and I can be {b}partners{/b} today."
    scene w2_2432 with dissolve
    "Her lips furled into a foreboding, ominous grin as she spoke the otherwise innocuous words."

    if kat_polite == True:
        "At that moment, she sounded evil. As evil as Mrs. Pulman."
    else:
        "At that moment, she sounded evil. As evil as Kathleen."

    mc "I will..."
    scene black with fade
    $ renpy.music.set_volume(.1, 2, channel = "music")
    mc "I'll go get dressed."
    play sound "sound effects/locker-close.wav"
    "*Clank*"
    scene w2_2355 with w20
    mct "(You know...)"
    scene w2_2356 with dissolve
    "A workout really wouldn't be so bad, plus if I kill some time, the place might thin out some more."
    "That'll make it easier to get the shots Mrs. Pulman expects, without branding either of us as criminals."
    scene w2_2357 with dissolve
    mct "(Hmm...)"
    scene w2_2358 with dissolve
    "This place is huge."
    "Really, {i}really{/i} huge, with a ton of facilities."
    "The overhead for this place must be massive. I'm surprised Samson even had to do anything."

    if VeroFlag == True:
        mct "(I should probe Veronica later and get some details about their relationship.)"
    else:
        mct "(I'm staying out of it, but still...)"

    mct "(That bastard...)"
    scene w2_2359 with dissolve
    "That's not important right now, though."
    scene black with fade
    $ renpy.music.set_volume(1, 2, channel = "music")
    mct "(Let's go break a sweat.)"
    scene w2_2433 with dissolve
    "The workout proceeded as normal, relatively speaking."
    scene w2_2434 with cmet
    "First, Veronica helped me stretch with a more hands-on approach."
    "The ease and strict professionalism she did it with made me feel oddly self-conscious, given what would come later."

    if date == "june09day":
        "My mind was preoccupied with all the lewd potentiality of Mrs. Pulman's appointed task."
    else:
        "If it turns out even just a fraction like Rosalind's photo shoot..."

    scene w2_2435 with wipeleft
    "Thankfully I didn't have too much time to think about it."
    "I could tell she was taking it easy for my sake, but even still."
    scene w2_2436 with wiperight
    "It was hard, tough work."
    "The Amazon's pace was relentless."
    scene w2_2437 with wipeup
    "Regret would've been the word foremost in my mind if my mind wasn't so utterly preoccupied with keeping up."
    "In its own way, this was sort of fun."
    scene w2_2438 with circlewipe
    "I had no mental room to think and all the daily stress simply faded into the background."
    "Put on pause, to be picked back up by a less tired and more rejuvenated [mcf]."
    scene w2_2439 with dissolve
    ver "You're doing pretty good, errand boy."
    scene w2_2440 with dissolve
    mc "Ah... ha... am I?"
    scene w2_2439 with dissolve
    ver "You haven't stopped or bitched any."
    scene w2_2440 with dissolve
    mc "That's the bar?"
    scene w2_2439 with dissolve
    ver "That's a pretty high bar."
    scene w2_2441 with dissolve
    "The faint words of praise, coming from her, felt good. Probably because she was always such a hardass."
    "Then it hit me. I didn't really know her in any other context other than the club, it's kind of shitty to assume she's always antagonistic..."
    scene w2_2442 with dissolve
    mc "Hmm..."
    scene w2_2443 with dissolve
    mct "(Damn, her form's impeccable. Like an unbending oak.)"
    scene w2_2444 with dissolve
    ver "Eh, what is it? Why are you looking at me--"
    mc "Praise me more."
    scene w2_2445 with dissolve
    ver "Shut up! Just focus on doing thirty push ups."
    scene w2_2439 with dissolve
    mc "......"
    scene w2_2440 with dissolve
    mc "..."
    scene w2_2439 with dissolve
    mc "...ah, shit. What number was I at?"
    scene w2_2446 with dissolve
    ver "Pfft--"
    "She did her best to conceal it, but I could hear her snickering all the same."
    scene w2_2439 with dissolve
    mc "Was it seventeen?"
    ver "If you can't remember, best to just start over then."
    scene w2_2440 with dissolve
    mc "I'm not starting over!"
    "It was a nice atmosphere, but one looming fact would soon change it."
    "Soon we'd be in the middle of club business and any semblance of friendliness between us would be violently dashed and skewered."
    scene black with fade
    stop music fadeout 3.0
    "It was a thought that both excited me and made me a little sad."
    scene w2_2447 with dissolve
    ver "Heh! Ah, that was fun. You wanted more praise?"
    ver "Well, you really kept up! Good job!"
    mc "Ah... ha... ha... *huff*..."
    scene w2_2448 with dissolve
    play music "music/cold-sober.ogg"
    mc "You're in pretty good spirits, all things considering."
    scene w2_2449 with dissolve
    ver "All things considering...? Oh! Well, if you're going to take lewd photos of me soon..."
    scene w2_2450 with dissolve
    ver "It was fun having you break a sweat beforehand."
    scene w2_2449 with dissolve
    ver "Not quite equitable, but I'll take what I can get."
    scene w2_2451 with dissolve
    "Veronica quickly closed the gap between us, with a perplexingly fierce and sly look on her face."
    scene w2_2452 with dissolve
    ver "You'll have your own fun later, right?"
    scene w2_2453 with dissolve
    mc "You mean during the photo shoot? It's \"work\" for both of us."
    scene w2_2452 with dissolve
    ver "Uh huh, and you don't enjoy it?"
    scene w2_2453 with dissolve
    mc "It has its perks."
    scene w2_2454 with dissolve
    ver "Well, either way, we should do our best."
    scene w2_2455 with dissolve
    "{i}Right{/i}. Her performance is tied to this."
    mc "...hmm."
    scene w2_2394 with dissolve
    "One of the many posters of Samson littering the gym walls caught my eyes."
    mc "Can I ask you something?"
    scene w2_2456 with dissolve
    ver "Depends on the something."
    scene w2_2457 with dissolve
    mc "How well do you know Samson?"
    scene w2_2458 with dissolve

    if VeroFlag == True:
        "I wanted to get her take on the washed-up actor."
    else:
        "Even if I wasn't going to get involved with Veronica's problem, I was still a little curious."

    scene w2_2456 with dissolve
    ver "Why do you want to know about that bastard?"
    scene w2_2459 with dissolve
    mc "I was just wondering what your initial impressions of the man were. You did enter a business relationship with him. His face is plastered all over your walls."
    mc "Surprised you still have those up, actually..."
    scene w2_2460 with dissolve
    ver "Ack, don't fucking mention that! I'd rip them down, but I'd be in breach of our contract if I did."
    scene w2_2457 with dissolve
    mc "So, what did you first think of him? You know, before you had knowledge of the Carnation Club."
    scene w2_2456 with dissolve
    ver "What did I think? I thought he was an asshole. Just a {b}normal{/b}, run-of-the-mill narcissistic asshole."
    ver "Not exactly unheard of in the bodybuilder world. I'm used to dealing with them."
    scene w2_2457 with dissolve
    mc "Run-of-the-mill?"
    scene w2_2456 with dissolve
    ver "Yeah. Really into himself. The kind who doesn't really listen and is instead just waiting for his turn to talk."
    scene w2_2461 with dissolve
    ver "The type of man who always makes the conversation about himself, no matter what the topic is. Annoying, but harmless..."
    scene w2_2456 with dissolve
    ver "{b}Seemingly{/b} harmless, at least. Obviously my opinion has shifted on that predatory asshole."
    scene w2_2457 with dissolve
    mc "How did you first meet him?"
    scene w2_2461 with dissolve
    ver "Why the hell do you care? You're asking a lot of questions."

    if VeroFlag == True:
        scene w2_2459 with dissolve
        mc "To be honest, I'm curious. I don't like the asshole either and quite frankly..."
        scene w2_2457 with dissolve
        mc "I think he may have done something to hasten the situation you're in."
        scene w2_2458 with dissolve
        "I KNEW he did, but saying as much would be overplaying my hand. If she reacted poorly, it could make my position at the club tenuous."
        scene w2_2462 with dissolve
        mc "You don't think it's coincidental that the man you're in a business relationship with just happened to have a convenient out for you?"
        scene w2_2464 with dissolve
        ver "Don't think I haven't made a connection there, errand boy. That's why I called him a predatory asshole, but my financial troubles with this place largely predate meeting him."
        scene w2_2463 with dissolve
        ver "It's more likely he just saw an opportunity when we first met and inserted himself in the situation. All he had to do was wait and dangle the club in front of me."
        scene w2_2462 with dissolve
        "That would make sense. If what she's saying is true, why would Samson do anything when he didn't have to?"
        mct "(Except he point-blank admitted to having a hand in it. Was he lying to impress the other patrons?)"
        "In Lucy's case, that slimy bastard Isaak just had to wait like a trapdoor spider and let the women come to him. Every year, a new batch of students with hopeful mothers."
        "You would think the same would be true of Samson's sponsorship of Veronica. A famous bodybuilder like him must get a lot of business inquiries. He would just have to wait for someone perfect to fall into his lap."
        "...but how many gym owners are even women? On top of that, how many are beautiful and fierce like Veronica, the type that would be fun to break down and humiliate?"
        mct "(No. He wasn't lying. He definitely had a hand in it and I'm going to root out what he did.)"
        mc "Still, how did you two meet?"
        scene w2_2463 with dissolve
        ver "At an industry show for gym equipment he was promoting."
        ver "I approached him, we got some drinks. I got drunk and a little too loose lipped with my troubles..."
        ver "Eventually the topic of using a spokesperson to drum up business was broached."
        scene w2_2462 with dissolve
        mc "By you or him?"
        scene w2_2464 with dissolve
        ver "Uh... I don't remember, but I can see what you're getting at. It's not like he came cheap, but hiring him was actually successful. It got memberships up."
        ver "Trust me, I've mulled this over a thousand times. It's a natural conclusion to reach for, but there's no way he's responsible for the money this place is hemorrhaging."
        scene w2_2465 with dissolve
        ver "I'm just a bitch with a bad business sense. I wish I could put the blame on someone else."
        scene w2_2466 with dissolve
        "Veronica looked utterly ripped open for the briefest moment, guts laid bare."
        "I was still certain he did something, but..."
        scene w2_2467 with dissolve
        mc "Sorry, it was just a random thought I had."
        scene w2_2469 with dissolve
        ver "No it's okay. For someone whose paycheck depends on exploiting me, you sounded genuinely concerned."
        scene w2_2463 with dissolve
        ver "So, thanks. I guess."
        scene w2_2462 with dissolve
        mc "I don't like the idea of people's dreams being fucked with."
        scene w2_2468 with dissolve
        ver "..."
        scene w2_2469 with dissolve
        ver "So, the second half of our workout..."
        scene w2_2468 with dissolve
        mc "VERY funny. I'm going to go get my camera."
        mc "We'll see about that \"fun\"..."
        scene black with fade
        stop music fadeout 3.0
        "......"
        "..."
        jump w2VeronicaGymphotoshoot
    else:

        scene w2_2459 with dissolve
        mc "Ah, yeah. You're right. It's none of my business."
        scene w2_2458 with dissolve
        "I'm staying out of it."
        scene w2_2470 with dissolve
        ver "..."
        scene w2_2456 with dissolve
        ver "So, the second half of our workout..."
        scene w2_2471 with dissolve
        mc "VERY funny. I'm going to go get my camera."
        mc "We'll see about that \"fun\"..."
        scene black with fade
        stop music fadeout 3.0
        "......"
        "..."
        jump w2VeronicaGymphotoshoot


label w2VeronicaGymphotoshoot:

    if _in_replay:
        show transitionveronica03 with cmet
        show screen textbox2 with dissolve
        "Please set [mcf]'s personality (toughness score) for this replay."
        hide screen textbox2 with dissolve
        menu:
            "Nice guy (Toughness: 0)":
                $ toughness = 0
            "Mischevious (Toughness: 18)":
                $ toughness = 18
            "Asshole (Toughness: 30)":
                $ toughness = 30
        show screen textbox2 with dissolve


    play music "music/jazz-apricot.ogg"
    scene w2_2472 with blinds
    "When I got back from the locker room, I found Veronica at the end of the hall."
    scene w2_2473 with dissolve
    mc "Hey, what are you doing?"
    scene w2_2474 with dissolve
    ver "Last guy left, so I saw an opportunity to close down before anyone else got here. Just need to send out a text..."
    scene w2_2473 with dissolve
    mc "I thought we decided we needed to leave it open. Mrs. Pul--"
    scene w2_2475 with dissolve
    ver "That's what you and that old bitch decided, not me."
    scene w2_2476 with dissolve
    "Veronica said it firmly, without any room to question."
    mc "..."
    scene w2_2477 with dissolve
    mc "I understand."
    scene w2_2478 with dissolve
    ver "Listen... it's just too risky for me, okay? I'm in this whole fucked-up thing to save {i}this{/i} business."
    scene w2_2479 with dissolve
    ver "I'm not going to do anything that will harm it, like getting caught being photographed with my pants down."
    scene w2_2480 with dissolve
    mc "I get that. I really do."
    "It's not like I could force her one way or another, plus knowing the place is closed takes a ton of stress off me too."
    scene w2_2482 with dissolve
    ver "Your boss won't be able to tell whether the place is open or closed from just a photograph either."
    scene w2_2480 with dissolve
    mc "That is also LIKELY true."
    scene w2_2482 with dissolve
    ver "You wouldn't tell her, right?"
    scene w2_2480 with dissolve
    mc "No. Why would I?"
    scene w2_2482 with dissolve
    ver "Well, I sure as shit won't either."
    scene w2_2480 with dissolve
    mc "If this is what it takes for you to do it..."
    scene w2_2482 with dissolve
    ver "It is."
    scene w2_2481 with dissolve
    mc "Alright, then. Guess we have the place to ourselves."
    scene w2_2482 with dissolve
    ver "Don't worry. We'll both do our jobs."
    scene w2_2483 with dissolve
    ver "We'll get some photos. We'll get some good photos. Hell, this place being closed..."
    ver "We can even get some GREAT photos."
    scene w2_2484 with dissolve
    mc "You have something in mind?"
    scene w2_2485 with dissolve
    "It sounded like she had a game plan, which felt oddly just like her."
    scene w2_2486 with dissolve
    ver "Wait here."
    "With that, Veronica brushed past me and moved deeper into the gym."
    scene w2_2487 with dissolve
    "Disappearing into parts unknown."
    scene black with fade
    "......"
    "..."
    scene w2_2488 with dissolve
    "After the Amazon's footsteps had receded into the recesses of the building, the whole place fell into an eerie quiet."
    mct "(What could she possibly be retrieving?)"
    "A couple of minutes later..."
    scene w2_2489 with dissolve
    ver "Sorry, it took me a minute to find it and dig it out."
    "In her hand was a small strip of black leather, in the familiar shape of a..."
    scene w2_2490 with dissolve
    mc "Is that a... pet collar?"
    scene w2_2491 with dissolve
    ver "Eh... something like that. It's for humans. Part of my \"personal\" collection."
    scene w2_2492 with dissolve
    mc "Personal... oh!"
    "The tawdry conclusion came as a bit of a surprise."
    mc "I didn't realize you were into things like that."
    scene w2_2493 with dissolve
    ver "Pick your jaw up off the floor. I haven't ever worn it myself."
    scene w2_2494 with dissolve
    mc "Then who..."
    scene w2_2493 with dissolve
    ver "My ex-wife. She was into that kind of thing."
    scene w2_2495 with dissolve
    ver "It turned out I was too. Got used to it fast, so much so that now when I take home cute lays from the bar, I still like to make use of it."
    "There was something about that casual admission that was crazy hot."
    scene w2_2494 with dissolve
    mc "Is that so?"
    scene w2_2496 with dissolve
    ver "Yeah, I wonder how you'd look on a leash."
    scene w2_2497 with dissolve
    mc "That's not why you got it, right?"
    scene w2_2498 with dissolve
    ver "No, obviously not. You're behind the camera. It's for..."
    scene w2_2499 with dissolve
    "A slight blotch of red colored her pale cheeks."
    scene w2_2500 with dissolve
    ver "It's for me. I'll be the pet today."
    scene w2_2501 with dissolve
    "......"
    "..."
    mc "--!" with vpunch
    "The cute way she said the incongruous words sent my stomach fluttering. Suddenly, I was a lot more stoked about her unilateral decision to shut the place down."
    scene w2_2502 with dissolve
    mc "You're really serious about this shoot."
    scene w2_2503 with dissolve
    ver "Not really."
    scene w2_2504 with dissolve
    mc "My impression of you is of someone who's resisting the exhibition every step of the way."
    scene w2_2505 with dissolve
    ver "Well, it's a tricky balance of telling that cunt to eat it and doing what's necessary. One's more fun than the other."
    ver "Don't get me wrong. I'm going to ultimately win on my own terms."
    scene w2_2504 with dissolve
    mc "That's important to you?"
    scene w2_2506 with dissolve
    ver "Life's about pretending there's dignity, especially where there is none."
    scene w2_2507 with dissolve
    mc "Dignity is a funny word for these circumstances."
    scene w2_2508 with dissolve
    ver "The collar's my idea, isn't it? Those skeevy old fucks will eat it up."
    scene w2_2510 with dissolve
    "The difference of being told to do something or choosing it... is she a teenager?"
    "It seemed like such a childish distinction for the situation, but for Veronica, it was evidently an important one."
    scene w2_2507 with dissolve
    mc "Alright, if you want to \"win on your own terms\"... you can be the pet."
    scene w2_2509 with dissolve
    mc "Just don't be mad if I inadvertently treat you like one for the sake of the photo shoot."
    scene w2_2511 with dissolve
    ver "Whatever helps you take the best photos. I don't think you've got much fang, anyway."
    scene w2_2509 with dissolve
    mct "(Is that so...?)"
    hide screen textbox2 with dissolve

    menu:
        "Keep it friendly and business like. Help her put on the collar."(chg=["veronica_up"]):
            $ Veronica_Affection += 1
            scene w2_2512 with dissolve
            show screen textbox2 with dissolve
            mc "Let me help you put that on then."
            ver "You want to be the one to put it on me, eh...?"
            mc "I'm just offering a hand."
            scene w2_2513 with dissolve
            ver "Well then, I'll take it."
            ver "Securing it is a cinch, but adjusting the size by yourself is a little tricky."
            scene w2_2514 with dissolve
            "Taking the collar from her, Veronica turned around and offered me her beautiful neckline."
            ver "Do you need me to hunch down? I know I'm pretty tall..."
            scene w2_2515 with dissolve
            mc "No need. You're just the right height."

            scene w2_2516 with dissolve:
                subpixel True
                yalign 1.0
                xalign 0.6
                linear 4 yalign 0.15

            "Getting in close made me more acutely aware of Veronica's feminine form."
            scene w2_2517 with dissolve
            "The alluring divot in her lower back, its eye-catching curve, and the flawlessly freckled skin still slightly damp with perspiration."
            "It was all in contrast to her wide back and broad shoulders. In a hopelessly dumb and illogical animal-like way, just being this close to the towering woman was oddly comforting."
            scene w2_2518 with dissolve
            ver "What are you waiting for? An explanation on how buckles work?"
            scene w2_2519 with dissolve
            hide screen textbox2 with dissolve

            menu:
                "Tell her you were just admiring her backside."(chg=[("veronica_up", Veronica_Affection >= 10), ("veronica_down", Veronica_Affection < 10)]):
                    scene w2_2520 with dissolve
                    show screen textbox2 with dissolve
                    mc "Sorry, I was just admiring the view from behind."
                    if Veronica_Affection >=10:
                        $ Veronica_Affection += 1
                        scene w2_2521 with dissolve
                        ver "You were, you little pervert?"
                        scene w2_2520 with dissolve
                        mc "Yeah, you take care of yourself. I hope you don't mind."
                        scene w2_2521 with dissolve
                        ver "I'm used to people looking. It comes with my profession."
                        scene w2_2520 with dissolve
                        mc "You do take care of yourself. I like how big and wide your shoulders are."
                        scene w2_2522 with dissolve
                        ver "W-what? That's weird!"
                        scene w2_2523 with dissolve
                        mc "Sorry."
                        scene w2_2524 with dissolve
                        ver "Jeez, that's a fucking new one. Just put the collar on, will you?"
                        "Despite the harsh language, her tone sounded surprisingly subdued."
                        scene w2_2525 with dissolve
                        mc "Heh, sorry..."
                        ver "Stop apologizing. It's okay."
                        ver "You'll have plenty of time to admire me in today's shoot, [mcf]."
                        scene black with fade
                        "With care, I fastened the collar around Veronica's neck. Making sure it was secure, but not too tight."
                    else:

                        $ Veronica_Affection -= 1
                        scene w2_2521 with dissolve
                        show screen textbox2 with dissolve
                        ver "Whatever. We've got a job to do. Just hurry up and put it on."
                        "Of course, Veronica flat out rejected my creepy comment."
                        scene w2_2526 with dissolve
                        mc "Sorry."
                        ver "It's fine. You'll have a lot of time to admire me in today's shoot, errand boy."
                        scene black with fade
                        "With care, I fastened the collar around Veronica's neck. Making sure it was secure and maybe just a tad too tight."
                "Don't say anything at all.":


                    scene w2_2526 with dissolve
                    show screen textbox2 with dissolve
                    mc "Sorry. Was lost in thought."
                    ver "That's okay, but try to focus. We have a job to do."
                    scene black with fade
                    "With care, I fastened the collar around Veronica's neck. Making sure it was secure, but not too tight."
        "Order her to her knees and collar the oversized bitch. [mod_chat]":


            $ w2VeronicaDog = True
            show screen textbox2 with dissolve
            "There was something about her statement that rubbed me the wrong way and made me want to test the waters."
            mc "Whatever helps me take the best photos? Those are your words?"
            scene w2_2527 with dissolve
            ver "Don't let it be said you have poor listening comprehension."
            scene w2_2528 with dissolve
            "Veronica gave me a funny look. There wasn't even really an uneasiness in her eyes, much less trepidation."
            "It was more in the ballpark of curious and trying, like she was trying to size up the intentions of a disobedient toddler."
            mct "(It REALLY makes me want to test the waters.)"
            scene w2_2529 with dissolve
            mc "Get down on the floor like a good doggy and let me collar you then."
            scene w2_2530 with dissolve
            ver "You want to put it on me, eh?"
            ver "Well, I don't mind I guess. Securing it is a cinch, but adjusting the size is pretty--"
            scene w2_2531 with dissolve
            mc "Down."
            scene w2_2532 with dissolve
            "I spoke to her like a dog and she persisted with that same curious expression."
            scene w2_2533 with dissolve
            "Then she smiled, incredulously so."
            scene w2_2534 with dissolve
            "The Amazon got down on her knees, amused and indulging me."
            scene w2_2535 with dissolve
            "It was a bit of a rush seeing her like that, but even from her new position, it was like she was looking down on me."
            "A thought that made me want to push it further..."
            hide screen textbox2 with dissolve

            menu:
                "Tell her to get down on all fours."(chg=[("veronica_passion_up", Veronica_Affection >=13 or Veronica_Horniness >=6), ("veronica_down", Veronica_Affection < 13 and Veronica_Horniness < 6)]):
                    scene w2_2536 with dissolve
                    show screen textbox2 with dissolve
                    mc "I said like a good {b}doggy{/b}. {b}Hands and knees{/b}."
                    scene w2_2537 with dissolve
                    ver "...we're not even taking photos yet, {b}errand boy{/b}. Don't be ridiculous."
                    scene w2_2536 with dissolve
                    mc "It's important we set the tone."
                    scene w2_2538 with dissolve
                    ver "That's what this is? Setting the tone?"
                    ver "It's not some pathetic power trip?"
                    scene w2_2536 with dissolve
                    mc "Eh? Maybe it is, but can you blame me for taking advantage?"
                    mc "In this sort of situation, with a woman as stunning as you playing the pet? Wouldn't you act the same in my shoes?"
                    scene w2_2539 with dissolve
                    ver "..."

                    if kat_polite == True:
                        "Veronica glared at me defiantly, but I knew I was right. By her own admission she had a dominant streak, one I'd seen firsthand during her treatment of Mrs. Pulman."
                    else:
                        "Veronica glared at me defiantly, but I knew I was right. By her own admission she had a dominant streak, one I'd seen firsthand during her treatment of Kathleen."

                    if Veronica_Affection >=13 or Veronica_Horniness >=6:
                        $ Veronica_Horniness +=1
                        scene w2_2537 with dissolve
                        ver "What kind of ass backwards appeal is that, [mcf]?"
                        ver "Are you listening to yourself?"
                        scene w2_2536 with dissolve
                        mc "Am I wrong?"
                        scene w2_2540 with dissolve
                        ver "...no, if I was in your situation I might have fun with it too."
                        scene w2_2541 with fade
                        "To my surprise, Veronica got down on all fours like a dog."
                        scene w2_2542 with dissolve
                        ver "By all means have your power trip."
                        scene w2_2541 with dissolve
                        "Back arched, and ass pointed in the air like a bitch in heat."
                        scene w2_2543 with dissolve
                        mc "Good girl."
                        "For emphasis, I patted her head lovingly just like a pet."
                        scene w2_2542 with dissolve
                        ver "Don't be surprised if I bite you."
                        scene w2_2544 with dissolve
                        "The scary thing was, I had doubts she was speaking in metaphors."
                        "She might literally bite me."
                        mc "We'll see, I guess."
                        scene black with fade
                        "Without any ceremony, I affixed the collar around the Amazon's neck. Making sure it was appropriately snug for her new position as a pet."
                    else:
                        $ Veronica_Affection -= 1
                        scene w2_2537 with dissolve
                        ver "What kind of ass backwards appeal is that, errand boy? Are you listening to yourself?"
                        scene w2_2536 with dissolve
                        mc "Am I wrong?"
                        scene w2_2538 with dissolve
                        ver "...no, if I was in your situation I might have fun with it too, but that doesn't mean I'll be going along with all your degrading ideas. Especially when you're not even taking pictures."
                        ver "Context is key."
                        scene w2_2539 with dissolve
                        "Veronica looked unmovable on this."
                        scene w2_2545 with dissolve
                        mc "I guess I asked too much."
                        scene w2_2546 with dissolve
                        ver "So you think I'm stunning, do you?"
                        scene w2_2545 with dissolve
                        mc "That's what I said."
                        scene black with fade
                        "With a gentle and firm touch, I fastened the leather collar securely around the Amazon's neck. Making sure it was nice and snug, with the appropriate give for a pet."
                "Put the collar on her.":

                    scene w2_2545 with dissolve
                    show screen textbox2 with dissolve
                    mc "Thank you for your indulgence, Veronica."
                    mc "I just wanted to set the tone a little."
                    scene w2_2548 with dissolve
                    ver "Whatever, I did say you could treat me like a pet."
                    scene w2_2547 with dissolve
                    ver "I don't think I could ever get used to this. My ex must've had some screws loose."
                    scene w2_2545 with dissolve
                    mc "Don't say that. Wouldn't it be nice to be pampered and taken care of like a pet?"
                    scene w2_2547 with dissolve
                    ver "Sounds like a nightmare."
                    scene w2_2545 with dissolve
                    mc "I'm glad you feel that way."
                    scene w2_2548 with dissolve
                    ver "Why?"
                    scene w2_2549 with dissolve
                    mc "It makes collaring you all the more fun."
                    scene black with fade
                    "With a gentle and firm touch, I fastened the leather collar securely around the Amazon's neck. Making sure it was nice and snug, with the appropriate give for a pet."

    scene w2_2550 with dissolve
    ver "Well, there you go. I'm collared, just like a pet."
    if w2VeronicaDog == True:
        ver "...and you had your fun doing it."
        scene w2_2551 with dissolve
        mc "Sorry, it comes over me sometimes."
        scene w2_2552 with dissolve
        ver "I actually get it. It is my collar after all."
        ver "I got a little bossy too whenever my ex-wife would wear it."
    else:
        scene w2_2551 with dissolve
        mc "How does it feel?"
        scene w2_2552 with dissolve
        ver "I like being on the other side of the collar."
        scene w2_2551 with dissolve
        mc "That so?"
        scene w2_2552 with dissolve
        ver "Uh huh, bossing around people is a lot more fun."

    scene w2_2553 with dissolve
    ver "Hmm..."
    scene w2_2550 with dissolve
    ver "What say we get this over with, boss?"
    stop music fadeout 3.0
    scene black with fade
    "That sounded fine with me."
    play music "music/dancebroom-riddim.ogg"
    scene w2_2554 with circlewipe
    "...and things got rolling pretty nicely as soon as we re-entered the gym proper."
    "Veronica slid off her gym shorts and revealed what was underneath: a tight, form-fitting pair of racing briefs that nicely emphasized her sculpted derrière."
    scene w2_2555 with dissolve
    ver "What are you waiting for?"
    scene w2_2554 with dissolve
    "Hunched over with her ass sticking out, she looked back at me in just the {i}perfect{/i} way. So perfect that..."
    scene w2_2556 with dissolve
    mc "Oh, right..."
    "The shoot had begun."
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*" with flash
    "I remembered what we were doing."
    scene w2_2557 with dissolve
    ver "I'll trust you to get my good side."
    "The Amazon advanced further into the gym, with a deliberate sashay that made her aforementioned derrière that much more tantalizing."
    scene w2_2558 with dissolve
    ver "What's our game plan?"
    scene w2_2559 with dissolve
    mc "The plan? Well..."

    if date == "june09day":
        mc "As you know, the gist of this whole shoot is embarrassing you. Painfully so."
    else:
        scene w2_2573 with pixellate
        "With Rosalind, we took some more basic, preliminary shots before moving onto a more \"bold\" direction."
        scene w2_2574 with dissolve
        "Although I doubt Veronica and I will end up like that..."
        scene w2_2559 with pixellate
        mc "As you know, the gist of this whole shoot is embarrassing you. Painfully so."


    scene w2_2560 with dissolve
    ver "We should build up to that though, right? Get some shots of me working out, wearing THIS, prancing about the gym like it's still open."
    scene w2_2559 with dissolve
    mc "That would be a good place to start."
    scene w2_2561 with dissolve

    if minaGym == True:
        "She definitely had a mind for this, which was no surprise given how shamelessly she flirted with Mina the first time they met. She was practically a dirty old man."
    else:
        "She definitely had a mind for this, much more than she lets on."

    scene w2_2562 with dissolve
    ver "Then I'll just do some shit and you can follow me around. That sound good?"
    mc "Works for me. I'm a little interested in seeing what you come up with on your own."
    ver "Oh, are you?"
    scene w2_2563 with dissolve
    mc "I figure you have a knack for this."
    ver "Based on what, exactly?"
    mc "Just my intuition."
    scene w2_2564 with dissolve
    ver "I'm not so sure how I should feel about that."
    scene w2_2565 with dissolve
    mc "You could take it as a compliment. You're a confident woman and you're comfortable in your body."
    mc "You know how to strike an attractive pose."
    scene w2_2566 with dissolve
    ver "Like this?"
    scene w2_2567 with dissolve
    "In a sudden display of flexibility, Veronica slowly lifted and fully extended her left leg, hooking her foot on the frame of the chest press station and using her upper body to brace herself against the machine."
    mc "Ah..."
    "The result of the impromptu pose was three-fold: a tightened core that accentuated her abs and put both her long tree trunk-like legs and large bust on magnificent display."
    mc "I think..."
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*" with flash
    mc "I think my intuition was correct. Hold that pose, I'm going to get some shots."
    scene w2_2568 with dissolve
    "One portion of her body after the next, I trained the camera on Veronica's chiseled form in search of all her best angles."
    "First, I took pictures of her leg. Working my way up from her bulging calves to her thighs."
    scene w2_2569 with dissolve
    "Onto the crotch, where the eye could easily trace the outline of her vulva through the fabric of her racing briefs."
    scene w2_2570 with dissolve
    "Then I panned up the Amazon's tummy, taking shots of her hard won abs and working my way further up top."
    scene w2_2571 with dissolve
    "To her bust."
    scene w2_2572 with dissolve
    "Even her armpit. I left no stone uncovered."
    scene w2_2575 with dissolve
    ver "Don't you think you've got enough."
    scene w2_2576 with dissolve
    mc "I do now."
    scene w2_2577 with dissolve
    ver "Good."
    ver "It was like you were fucking me with the camera."
    scene w2_2578 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Share your (positive) honest thoughts"(chg=["veronica_up"]):
            $ Veronica_Affection +=1
            scene w2_2579 with dissolve
            show screen textbox2 with dissolve
            mc "Sorry, it's just you're a work of sculpted art."

            if Veronica_Affection >=11:
                scene w2_2580 with dissolve
                ver "Jeez, how can you say that kind of shit with a straight face?"
                scene w2_2581 with dissolve
                mc "I do it one syllable at a time."
                scene w2_2580 with dissolve
                ver "Dork."
                scene w2_2582 with dissolve
                "She seemed to take the compliment in stride."
            else:
                scene w2_2583 with dissolve
                ver "That's a pretty lame line."
                scene w2_2584 with dissolve
                mc "I'm not feeding you a line. Why would I, considering the nature of our relationship? I genuinely mean it."
                scene w2_2600 with dissolve
                ver "Keep it to yourself then."
                scene w2_2601 with dissolve
                "She seemed to take it more genuinely than she let on, or so my male lizard brain thought."
        "Keep the compliment to yourself.":

            scene w2_2579 with dissolve
            show screen textbox2 with dissolve
            mc "That's... sort of the point here, yeah?"
            scene w2_2585 with dissolve
            ver "Eh, I guess you've got a point there."
            ver "I can't help it if you like what you see."
            scene w2_2586 with dissolve
            mc "You can be preeeetty full of yourself when you want to be."

    scene w2_2587 with dissolve
    ver "Hmmm, I got some ideas for some more stretches."
    scene w2_2588 with dissolve
    mc "You lead and I follow."
    scene w2_2589 with dissolve
    ver "Ha, I know you will."
    scene w2_2590 with dissolve
    mc "Just make sure to shake your ass on the way."
    scene black with fade
    "Next in yet another strenuous display of unnatural flexibility for a woman of her size..."
    scene w2_2591 with cmet
    mct "(Damn!)"
    "Veronica got down on the ground, and supporting her upper body with her arms, almost fully splayed her legs out between two weight benches."
    "With the angle I was at, it put her crotch on full display. At least it would be, if it wasn't for that thin, damnable piece of fabric covering her womanly bits."
    scene w2_2593 with dissolve
    ver "Hurry up and take the shot."
    scene w2_2594 with dissolve
    mc "Right, okay!"
    scene w2_2595 with dissolve
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*" with flash
    mc "Nice pose."

    if date == "june09day":
        scene w2_2594 with dissolve
        mc "I doubt Rosalind or Felicia could even come close to a pose like that."
        scene w2_2592 with dissolve
        mct "(Although, I'd like to see them try...)"
        scene w2_2593 with dissolve
        ver "I think you might be underestimating Blondie a tad. I've seen her type in the gym; rich women like her can't afford to let themselves go."
        ver "...you know, so they don't get replaced like an old car."
    else:
        scene w2_2594 with dissolve
        mc "Let's just say Rosalind didn't have your flexibility in her shoot yesterday. I doubt she could've come close to striking a pose like that."
        scene w2_2592 with dissolve
        mct "(Although, I would've liked to see her try...)"
        scene w2_2593 with dissolve
        ver "Oh? Who do you think will have the better shoot?"
        scene w2_2594 with dissolve
        mc "Only time will tell."
        scene w2_2596 with dissolve
        ver "Aw, come on..."

    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_2599 with dissolve
    "*Click*"
    ver "Come on now, though... \"nice\"? How bland."
    mc "What? You'd prefer me to be vulgar?"
    scene w2_2596 with dissolve
    ver "No, of course not. Just an observation... it seemed oddly sterile."
    scene w2_2594 with dissolve
    mc "Fishing for a compliment?"
    scene w2_2596 with dissolve
    ver "Hell no."
    scene w2_2597 with dissolve
    mc "How would you have preferred I put it? Should I have said it \"looks like you're warmly welcoming a lover\" or..."
    play sound "sound effects/thud-floor.mp3"
    scene w2_2598 with vpunch
    ver "Ugh, no. Shut up."
    ver "That's awful."
    scene black with fade
    mc "I thought so."
    scene w2_2602 with dissolve
    ver "Now I'm afraid to ask your thoughts on this."
    scene w2_2603 with dissolve
    mc "It's... not as flashy as the first two."
    scene w2_2602 with dissolve
    ver "No...?"
    scene w2_2604 with dissolve
    ver "Better?"
    scene w2_2605 with dissolve
    mc "Yeah, that's better, but you should look more embarrassed."
    scene w2_2606 with dissolve
    ver "That ship has already sailed."
    scene w2_2607 with dissolve
    mc "I don't mean between us. This place is still open, remember?"
    scene w2_2608 with dissolve
    ver "Ah..."
    scene w2_2609 with dissolve
    ver "..."
    scene w2_2610 with dissolve
    "After taking a moment to collect herself, the Amazon put on her best worn bashful expression and looked away from the camera's eye."
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*" with flash
    mc "You're a born actress, Veronica."
    scene w2_2611 with dissolve
    ver "Really?"
    scene w2_2612 with dissolve

    if minaGym == True:
        mc "Yeah, you give Mina a run for her money."
        scene w2_2613 with dissolve
        ver "I doubt it. I can tell; that girl is good at faking things."
    else:
        mc "Better than me."
        scene w2_2615 with dissolve
        ver "I have a feeling that's not a high bar to clear."

    scene w2_2614 with dissolve
    "Not that I would draw attention to it, but I was a little surprised at how easily Veronica and I were carrying on."
    scene w2_2616 with dissolve
    mc "..."
    scene w2_2615 with dissolve
    ver "Why are you looking at me like that?"
    scene w2_2616 with dissolve
    mc "Nothing."
    scene w2_2617 with dissolve
    ver "...? Oh."
    scene w2_2618 with dissolve
    "As if suddenly remembering her chest was exposed, she quickly tugged her spandex top back down over her barely containable chest."
    ver "That's what you were looking at."
    scene black with fade
    "That surprisingly wasn't the case, but I didn't feel like denying it."
    scene w2_2619 with circlewipe
    "For the next pose, once again she positioned herself between the weight benches, this time in a way that is a little difficult to articulate."
    scene w2_2620 with dissolve
    ver "This one's a little more dynamic than the last."
    scene w2_2619 with dissolve
    "It looked like a cheetah in mid-sprint."
    mct "(Man...)"
    "If this sequence of poses had me wondering ANYTHING all, it'd be..."
    scene w2_2621 with dissolve
    "How difficult would it be to screw in that position?"
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*" with flash
    scene w2_2622 with dissolve
    mc "Well, it's... {i}extraordinarily nice{/i}."
    scene w2_2623 with dissolve
    ver "Extraord--"
    ver "Aha...! Don't make me laugh. I'm liable to fall on my face."
    scene w2_2624 with dissolve
    mc "Hmmm..."
    scene w2_2625 with dissolve
    mc "Speaking of faces..."
    "Positioning myself at her head to take another photo, it dawned on me that something was missing."
    mc "It could do with..."
    "What would make the next few shots better? No surprise, it was..."
    scene w2VeronicaGymBoobReveal with dissolve
    "Tits."
    "In a smooth motion, I managed to grab the band on the underside of the balancing woman's top, and with a strong tug, freed her freckled breasts from their spandex prison."
    scene w2_2630 with dissolve
    mc "Sorry. You weren't in a position to do it yourself."
    "The way they spilled out was nothing short of idyllic."
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*"
    scene w2_2631 with dissolve
    ver "Yeah, yeah... a warning would've been nice, you could've knocked me over."
    scene w2_2634 with dissolve
    mc "There wasn't any danger of that. Your limbs are like the roots of a tree."
    scene w2_2631 with dissolve
    ver "That's..."
    scene w2_2633 with dissolve
    "For a brief second, Veronica was speechless for once."
    scene w2_2632 with dissolve
    ver "Never heard that one before."
    scene w2_2630 with dissolve
    "Just a second, though."
    "Enough for a quick and titillating thought to cross my mind."
    hide screen textbox2 with dissolve

    menu:
        "Tell her to stick out her tongue."(chg=["VeronicaShootPoints_up"]):
            $ w2VeroShootPoints += 1
            show screen textbox2 with dissolve
            mc "I want to get one last shot in this position and I need you to do {i}one{/i} last thing..."
            scene w2_2635 with dissolve
            ver "I--"
            scene w2_2631 with dissolve
            ver "What?"
            scene w2_2634 with dissolve
            mc "Nothing too difficult, just..."

            if w2VeronicaDog == True:
                mc "Stick your tongue out like a bitch in heat."
            else:
                mc "Stick your tongue out, like a dog."

            scene w2_2635 with dissolve
            ver "...right, the pet angle."
            scene w2_2634 with dissolve
            "Instead of fighting it. She understood."
            scene w2_2636 with dissolve
            "..."
            scene w2_2637 with dissolve
            ver "Ah...."
            "She looked directly into the camera's eye and hit me with the lewdest look she could summon - and boy, did it pass all muster for the term."
            play sound "sound effects/camera-phone-shutter.wav"
            "Quickly, I got the shot I was looking for, because..."
            mct "(All of {b}this{/b} and a simple look was the thing that finally did it, huh?)"
            "No hiding it. A half-hard erection strained against my gym shorts."
            scene w2_2639 with dissolve
            ver "..."
            scene w2_2640 with dissolve
            ver "Looks like your lil' fellow has finally woken up."
            scene w2_2642 with dissolve
            mc "How could it not?"
            scene w2_2641 with dissolve
            ver "To be honest, I was starting to get a little worried that the shoot was boring."
            ver "Not as lively as it was a few days ago."
            scene w2_2642 with dissolve
            mc "You took note?"
            scene w2_2640 with dissolve
            ver "Hmmpfh."
            scene w2_2641 with dissolve
            ver "How could I not?"
        "Move on.":


            show screen textbox2 with dissolve
            "Nah, not really feeling it. I'll just get the rest of the shots quick."

    stop music fadeout 3.0
    scene black with fade
    "Like with the first pose, I took my time getting the rest of shots."
    "By the end, I had gotten familiar with every impressive inch of Veronica's sculpted form."
    play music "music/i-knew-a-guy.ogg"
    scene w2_2651 with circlewipe
    mc "That should do us for the basic stuff."
    scene w2_2652 with dissolve
    ver "Oh, yeah... now we move onto more..."
    ver "{b}More{/b}."
    scene w2_2651 with dissolve
    mc "Mrs. Pulman probably won't accept anything short of debauched."
    scene w2_2653 with dissolve
    ver "That's pretty much a matter of fact with that mean bitch."
    scene w2_2654 with dissolve
    ver "..."
    scene w2_2655 with dissolve
    "An unsettling quiet fell over the room as Veronica panned her eyeline across the gym."
    "......"
    "..."
    scene w2_2656 with dissolve

    if Veronica_Affection >= 13:
        ver "We've got to give it our all here, [mcf]."
    else:
        ver "We've got to give it our all here, errand boy."

    if w2VeronicaDog == True:
        scene w2_2657 with dissolve
        mc "I'll... give as much as you want. Keep that in mind."
        mc "Careful what you wish for, right?"
        scene w2_2658 with dissolve
        ver "Heh, yeah..."
    else:
        scene w2_2657 with dissolve
        mc "That mostly depends on you, but I'll give as much as you ask of me."
        scene w2_2658 with dissolve
        ver "I'd appreciate it."

    scene w2_2659 with dissolve
    "I think it dawned on her what she was asking for."
    scene w2_2660 with dissolve
    mc "Follow me, then."
    mc "We need a change of scenery."
    scene black with fade
    "On the way into the locker room, I made certain to snag a photograph of Veronica in front of the \"Men Only\" sign."
    scene w2_2661 with fade
    ver "What are we going to do in here?"
    scene w2_2662 with dissolve
    mc "If you want to have the best photo session of the three, we've got to escalate things."
    scene w2_2661 with dissolve
    ver "We already covered that part. I mean why here?"
    scene w2_2663 with dissolve
    mc "Oh, ah... well..."
    scene w2_2662 with dissolve
    mc "In theory, this place is still open, so we can't just do the heavy duty stuff on the gym floor."
    scene w2_2661 with dissolve
    ver "That makes sense."
    scene w2_2662 with dissolve
    mc "Plus, making it look all incognito-like will add to the eroticism of the photos."
    scene w2_2664 with dissolve
    ver "Well thought-out, as expected of a pervert."
    scene w2_2665 with dissolve
    mc "The pet collar was yours, remember?"
    scene w2_2666 with dissolve
    ver "Fine, we're both perverts then."
    scene w2_2667 with dissolve
    mc "That works for me."
    scene w2_2664 with dissolve
    ver "What do you have in mind for the rest of the shoot, pervert?"
    scene w2_2668 with dissolve
    mc "You're the one who brought in the pet play dynamic, so we'll go with that."
    scene w2_2669 with dissolve
    ver "I had a feeling that'd be the case, but more specifically...?"
    scene w2_2670 with dissolve
    mc "More specifically, eh?"
    scene w2_2671 with dissolve
    "If I wanted to make this good and thematic, the photos will need to depict Veronica as less than human."

    if w2VeronicaDog == True:
        "I had already gotten a taste for treating the large woman like a dog."
        scene w2_2672 with dissolve
        mc "First things first, {b}bitches{/b} don't wear clothes."
        scene w2_2673 with dissolve
        "Veronica ever-so-slightly tensed up at my choice of words."
        scene w2_2674 with dissolve
        ver "Bi--"
        ver "Nggh. Is that your way of asking me to undress?"

        if toughness >= 22:
            scene w2_2673 with dissolve
            mc "I'm {b}telling{/b} you to take your clothes off for the camera."
            scene w2_2674 with dissolve
            ver "Telling me...? You little sh-"
        else:
            scene w2_2673 with dissolve
            mc "I'm asking you to take your clothes off {b}for the camera{/b}."
            scene w2_2674 with dissolve
            ver "That's not quite how you put it, you lil' sh-"

        scene w2_2675 with dissolve
        "Before she could complete the last utterance, Veronica cut herself off with a long and exaggeratingly drawn out sigh."
        scene w2_2676 with dissolve
        ver "Ah, no damn sense dragging this out. This is what I'm here to do, even if you're enjoying it a bit too much."
    else:

        "How would I approach doing something like that? Especially getting her to FULLY go along with it..."
        scene w2_2672 with dissolve
        mc "First things first..."
        scene w2_2677 with dissolve
        ver "..."
        mc "You should undress. Pets don't wear clothes, right?"
        scene w2_2678 with dissolve
        ver "{b}No{/b}, they don't. Simple enough place to start I suppose."

    scene w2_2679 with dissolve
    "Acknowledging what she needed to do, Veronica reached for her racing briefs and hooked her fingers into the elastic band."
    scene w2_2680 with dissolve
    "Before matter-of-factly removing them like one would do before stepping into the shower."
    scene w2_2681 with dissolve
    "Before I could fully take in the sight of a woman wearing nothing but a sports bra, her hands found a new direction."
    scene w2_2682 with dissolve
    "Like before, she made short work in discarding her top and stood before me in her fully magnificent buff."
    scene w2_2683 with dissolve
    ver "There. As God made me -- well, I had a pretty big hand in it too, but you know what I mean."
    scene w2_2684 with dissolve
    mc "You'll never run short of ego, will you?"
    scene w2_2685 with dissolve

    if Veronica_Affection >= 13:
        ver "It's not ego, it's confidence, [mcf]."
    else:
        ver "It's not ego, it's confidence, errand boy."

    scene w2_2686 with dissolve
    ver "Make no mistake, it's an important distinction."
    hide screen textbox2 with dissolve
    scene w2_2687 with dissolve
    "The way she aimed and pointed her chest toward me like a pair of missiles made it difficult to argue semantics."
    mc "You'll never run out of confidence, will you?"
    scene w2_2688 with dissolve
    ver "Hell no."
    scene w2_2687 with dissolve
    "To think this confident woman is about to parade around here like a pet..."

    menu:
        "Try and warm Veronica up before the rest of the photo shoot."(chg=["veronica_passion_up2","veronica_up","VeronicaShootPoints_up"]):
            $ w2VeronicaHeated = True
            $ Veronica_Horniness += 2
            $ Veronica_Affection += 1
            $ w2VeroShootPoints += 1
            "However, all things in their own time. Before we got to that, a little preparation was in order. "
            mc "You're not feeling it yet, are you?"
            scene w2_2689 with dissolve
            ver "...feeling it? You mean am I turned on?"
            scene w2_2688 with dissolve
            ver "Of course I'm not."
            scene w2_2687 with dissolve
            mc "Do you want to be?"
            scene w2_2688 with dissolve
            ver "I don't think that's going to happen, under these circumstances."
            scene w2_2687 with dissolve
            mc "Arousal is as much a physical thing as it is a mental one."
            mc "I just think being gassed up and visibly aroused will make for a more exciting shoot. In your own words, we should do our best."
            scene w2_2690 with dissolve
            show screen textbox2 with dissolve
            ver "Are you saying you could possibly make me swoon in this asinine scenario?"
            scene w2_2693 with dissolve
            mc "I'm not necessarily suggesting that, but if you recall how last Saturday went..."
            mc "You got pretty into it."
            scene w2_2692 with dissolve
            ver "..."
            "There was one thing I suspected about the woman in front of me that was true of most people. She was at her most comfortable, and thus at her most manageable, when she {i}felt{/i} in control."
            scene w2_2693 with dissolve
            mc "The ball is entirely in your court here, Veronica."
            mc "We can do it on your terms."
            scene w2_2690 with dissolve
            ver "My terms...?"
            scene w2_2693 with dissolve
            mc "Whatever would most comfortably get you in the mood."
            scene w2_2694 with dissolve
            ver "This is absurd."
            scene w2_2695 with dissolve
            mc "Should we just move on, then?"
            scene w2_2696 with dissolve
            ver "..."
            scene w2_2697 with dissolve
            ver "...it's my ears."
            scene w2_2696 with dissolve
            "Out from the corner of her eye, she gauged my uncomprehending expression."
            scene w2_2697 with dissolve
            ver "My ears are... {i}especially{/i} sensitive, but since I'm usually the one leading, I rarely..."
            scene w2_2698 with dissolve
            ver "I rarely..."
            stop music fadeout 3.0
            scene w2_2699 with dissolve
            mc "Got it."
            "With that adorable request, I felt the scales of power re-align to a slightly more equitable balance."
            scene w2_2700 with dissolve
            "For now though, I would put aside those thoughts and focus entirely on Veronica."
            scene w2_2701 with dissolve
            mc "Just a heads up, I'm not going to half-ass this."
            scene w2_2702 with dissolve
            "She didn't speak, but she looked unconvinced. That would work in my favor."
            scene w2_2703 with dissolve
            mc "Leave it to me."
            play music "music/soft-feeling.ogg"
            scene w2_2704 with dissolve
            "My plan of attack was from behind, but before that, I wanted to steal a taste for myself."
            scene w2_2705 with dissolve
            "I made my way down Veronica's torso, admiring and kissing her chiseled abs."
            ver "T-that tickles..."
            scene w2_2707 with dissolve
            "Feeling a little more carnivorous, I sunk my tongue into their sinuous recesses, probing the border of her abdominal muscle."
            scene w2_2706 with dissolve
            "Her skin tasted unsurprisingly salty on my tongue, a palatable reminder of Veronica's daily labor in the gym."
            hide screen textbox2 with dissolve
            scene w2_2708 with dissolve
            ver "That's the wrong direction..."
            scene w2_2709 with dissolve
            mc "Patience. I'm getting there."
            scene w2_2710 with dissolve
            ver "Oh!"
            "Again, just for a moment, I returned to the Amazon's delectable tummy by plunging my tongue into her navel."
            ver "That really tickles!"
            scene w2_2711 with dissolve
            mc "Turn around for me."
            scene w2_2712 with fade
            "Without any fuss, she did as I asked. Turning on the ball of her heels, she placed her sizable, yet trim ass directly in front of my face."
            mct "(If she wanted, she could use this thing to kill a man.)"
            scene w2_2713 with dissolve
            "This time, I went in reverse."
            scene w2_2714 with dissolve
            "Trailing up from her buttocks to the small of her back."
            scene w2_2715 with dissolve
            "Past her clavicle and wide shoulders until I was standing up straight, my body eagerly pressed into Veronica's and my breath tickling the nape of her neck."
            "I so very much wanted to reach from behind and man handle the redhead's tits, but this was on her terms."
            scene w2_2716 with dissolve
            ver "Just so you know, this is more creepy than sexy."
            scene w2_2717 with dissolve
            mc "Patience."
            scene w2_2718 with dissolve
            mc "Just how sensitive are you here?"
            scene w2_2719 with dissolve
            ver "{b}S-sensitive{/b}."
            scene w2_2720 with dissolve
            "Must be. My breathe on her earlobe as I spoke caused her to physically shudder."

            if w1GonzoReward == True:
                scene w2_2718 with dissolve
                mc "Me too, actually."
                scene w2_2725 with pixellate
                if kat_polite == True:
                    "If Mrs. Pulman's little lesson about erogenous zones were any indication."
                else:
                    "If Kathleen's little lesson about erogenous zones were any indication."

                scene w2_2720 with pixellate
                "Either from embarrassment or arousal, her ears were already looking flush."
            else:

                "Either from embarrassment or arousal, her ears were already looking flush."

            scene w2_2718 with dissolve
            mc "I'll begin then."
            scene w2_2721 with dissolve
            "Starting with the lobe, I ran my tongue up the length of the Amazon's ear, pressing firm and conforming to its intricate bends and folds."
            "Admittedly, this was a new one for me. I'd never set out to molest a gal's ear before. However, I was feeling up to the challenge."
            ver "Mmmph!"
            "She let out a small, pleasurable coo."
            scene w2_2722 with dissolve
            ver "A-ah!"
            "It didn't take long for Veronica to vocalize what she was feeling, even if it was just ever so slight."
            mct "(This is going to be fun.)"
            scene verogear1_a with dissolve
            show verogear1
            "At first, I went with a more reserved approach: sliding and scraping my tongue against the woman's outer ear, bending and prodding the cartilage with firm licks."
            "Taking in and learning its fine contours."
            "The Helix, the scapha..."
            "The antihelix and antihelix fold..."
            scene verogear2_a with dissolve
            show verogear2
            "Oddly enough, in the process of making the redhead squirm, a checklist formed in my head and I began to mentally review what I had learned about the anatomy of the human ear in my studies."
            "The antitragus and lobule..."
            "Very gently, I took the fleshy lower protrusion of her ear in my mouth and nibbled and coaxed it with my tongue."
            ver "Mmmh!"
            "Occasionally, Veronica's body would involuntarily twitch and jerk and I would have to reaffirm my grip on her body."
            scene verogear1_a with dissolve
            show verogear1
            "I held onto her tight, worried she might wiggle away."
            ver "That... that feels good..."
            "It's not like the simple act was anything to be proud of, this was mostly her, but I still felt a bizarre sense of accomplishment from her words."
            ver "Feels really, really good..."
            "Next I worked my way to the inner cone of her ear."
            "The fossa... a depression in the fork of the antihelix."
            "The concha... the hallow next to the ear canal."
            scene verogear2_a with dissolve
            show verogear2
            "Licking and licking and licking, probing all the little divots that help funnel and process sound."
            "Next I wormed my wet, warm, wriggly appendage into her ear canal - {i}the external auditory meatus{/i} - teasing and probing to my heart's content."
            ver "Ah, d-damn...! That...!"
            "That one REALLY got a response."
            ver "Keep going!"
            "That I did. It tasted unusual, but no less so than eating her out."
            ver "Keep-!"
            scene w2_2723 with dissolve
            mc "Sssh!"
            "With the desire to have complete control over the towering woman, I covered her mouth with the palm of my hand."
            ver "Mppph..!"
            scene w2_2724 with dissolve
            mc "Sssh!"
            "The warm air blowing through my pursed lips had the intended pleasurable effect."
            ver "Mppph..!"
            scene verogear3_a with dissolve
            show verogear3
            ver "Mmmmmh...! "
            "Once more, I thrust my tongue back in. Eager to have Veronica resume her squirming."
            ver "Mmmmmh...! "
            "This time, I took a carte blanche approach and threw all exploratory pretense out the window."
            ver "Mmmmmmmmmhhhh.....!"
            "I drove my tongue as deep as it could humanly fit and shook the tip as violently as I could muster."
            "As far as I was concerned, her ear was now a pussy and I was going to do my damnedest to pleasure it like one."
            ver "Mmfwhhooock!"
            scene verogear4_a with dissolve
            show verogear4
            "Veronica wasn't alone in feeling this."
            "The feeling of giving the headstrong woman pleasure and having her melt in my hands had me painfully hard right now."
            "On instinct, I found my lower half doing its own bit of writhing. Pressing my covered crotch hard into Veronica's naked ass and dully gyrating to the Amazon's own subconscious motions."
            scene verogear3_a with dissolve
            show verogear3
            "So much sexual urge was welling up in me, but I held it back. The point of this was to get her jazzed up, not for me to get off."
            mct "(It's not like I'm undersexed. I can control myself.)"
            ver "Mmmfpg...! Mhaa!"
            "In time, something strange happened. My arms began to feel... heavy?"
            "That's right. Veronica wasn't quite supporting her weight anymore. Her body had gone slack."
            "Leaving me to..."
            scene black with fade
            "Take it to the ground."
            scene verogear5_a with fade
            show verogear5
            "She didn't fight it as I guided her to the floor. She was lost in her own pleasure-drenched world."
            "Not once did I stop my assault on her ear. Once the problem of gravity had been taken care of, all that was on my mind was that singular task."
            "I was going to thoroughly violate her ear and that I did."
            "Over the next few minutes, I had my way with her and Veronica openly accepted."
            "To no surprise, eventually Veronica's hand found its way to her vagina."
            "She didn't take the plunge, though. Instead she used her long fingers to gently caress and gently tease apart her labia."
            ver "[mcf]..."
            ver "Y-you're doing a good job..."
            "Her voice was low and believably sultry..."
            "I had achieved what we had set out to do, but neither of us showed any signs of stopping."
            mct "(We should stop though.)"
            scene w2_2736 with dissolve
            stop music fadeout 3.0
            ver "H-huh...?"
            "It felt weird to let go of her. I had been clinging to her so tightly that the absense of human warmth felt stark against the cool locker room air."
            scene w2_2726 with dissolve
            show screen textbox2 with dissolve
            mc "You feeling it now?"
            scene w2_2727 with dissolve
            "She didn't speak. Instead she strongly pressed her back into my chest, like a passing house cat marking its territory."
            scene w2_2728 with dissolve
            ver "Ah, fuck..."
            scene w2_2729 with dissolve
            "The eyes that looked up at me, no matter how mollified, was still unmistakably Veronica."
            scene w2_2728 with dissolve
            ver "I don't..."
            scene w2_2729 with dissolve
            "She was in no way simpering."
            scene w2_2728 with dissolve
            ver "I don't think this was such a good idea. Now I'm too wound up."
            scene w2_2730 with dissolve
            mc "No, this next part is going to be all the better for it."
            scene w2_2728 with dissolve
            ver "The next part..."
            scene black with fade
            if w2VeronicaDog == True:
                mc "On your knees, bitch."
            else:
                mc "On your knees, pet."
        "Just move onto the photo shoot.":

            show screen textbox2 with dissolve
            "Whether I wanted to get to that part quicker or if I just wanted to get this other with, I couldn't quite distinguish."
            "It may have been a bit of both. Either way, this shoot was about shame. If she's aroused or not doesn't play into it."
            mc "Then why don't you confidently get down on your knees and we'll begin, pet."
            scene w2_2731 with dissolve
            stop music fadeout 3.0
            ver "...let's get it over with."
            scene w2_2732 with dissolve
            "...is all the Amazon said as she sunk beneath my eyeline and onto the cold, hard locker room floor."
            scene w2_2733 with dissolve
            ver "Even though this was partially my plan, that smug look on your face is irritating."
            scene w2_2734 with dissolve
            mct "(Heh. She better get used to it.)"


    scene w2_2735 with dissolve
    play music "music/devious-little-smile.ogg"
    mc "I hope you like walkies."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_2737 with flash
    "*Click*"
    "Not giving her a chance to glibly respond, I launched into the photo shoot."
    scene w2_2738 with dissolve
    mc "Put your hands up, like a set of paws."
    scene w2_2739 with dissolve
    ver "Meow?"
    scene w2_2740 with dissolve
    mc "You're covering your breasts."
    scene w2_2741 with dissolve
    ver "That better you tit fiend?"
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_2742 with flash
    "*Click*"
    mc "I'm not so limited. I have a lot of preoccupations when it comes to a woman's body."
    scene w2_2743 with dissolve
    ver "Could've fooled me with the way you attacked poor Rosie's breasts last Saturday."
    scene w2_2744 with dissolve
    mc "I was just... following her lead."
    scene w2_2745 with dissolve
    ver "Yeah, sure you were. If it were me, I'd just own up to it."
    scene w2_2744 with dissolve
    mc "To being a tit fiend?"
    scene w2_2746 with dissolve
    ver "Yeah! Next to an Adonis belt, a woman's breasts are my favorite part of the human body."
    scene w2_2747 with dissolve
    mc "Adonis belt?"
    scene w2_2748 with dissolve
    ver "Uh... it's like..."
    ver "Y'know, when you see a man or woman with a v-line running from their hips to their pelvis?"
    mc "I think I'm picturing it."
    ver "Well, when your body fat is low enough that you can see the separation between your obliques and your hip flexors, it's called an adonis belt. It's quite sought after in the world of fitness."
    scene w2_2749 with dissolve
    mc "I see..."
    "Her description was painfully unsexy."
    scene w2_2750 with dissolve
    mc "Say no more, tit fiend."
    scene w2_2751 with dissolve
    mc "What's with the sharing?"
    scene w2_2752 with dissolve
    ver "I don't know. I guess I'm just making conversation to take my mind off the hard tile floor."
    scene w2_2753 with dissolve
    "So it was an extremely indirect way of telling me to hurry up..."
    scene w2_2751 with dissolve
    mc "Message received."
    scene w2_2754 with dissolve

    if w2VeronicaDog == True:
        mc "Get on all fours, like a dog."
    else:
        mc "Lean forward for me and place your hands flat on the floor."

    scene w2_2755 with dissolve
    ver "I can see where this is going..."
    scene w2_2756 with dissolve
    ver "You planning on giving me a \"bone\" next?"
    scene w2_2757 with dissolve
    mc "Do you want one?"
    scene w2_2756 with dissolve
    ver "What do--"
    scene w2_2757 with dissolve
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*"

    if w2VeronicaDog == True:
        mc "I wonder if you know any tricks. Can you roll over for me, girl?"
    else:
        mc "Roll over."

    scene w2_2758 with dissolve
    ver "Onto my back?"
    scene w2_2759 with dissolve
    "I gave a simple nod to confirm my intentions."

    if w2VeronicaHeated == True:
        "The annoyed look I was expecting from her didn't quite have its normal edge."
        scene w2_2760 with dissolve
        ver "I'm glad I mopped the floor today."
        scene w2_2761 with dissolve
        "In place of simply rolling over in supplication like an animal would, Veronica added her own erotic flourish to the mixture."
        play sound "sound effects/camera-phone-shutter.wav"
        "*Click*"
        "She pushed her breasts together in a camera-pleasing way."
        mc "The men at the club are going to think you're into this."
        "There was not an ounce of embarrassment or shame seen on her face."
        scene w2_2762 with dissolve

        if Veronica_Affection >=13:
            ver "... and whose tongue is at fault for that, [mcf]?"
        else:
            ver "...and whose tongue is at fault for that, errand boy?"

        scene w2_2764 with dissolve
        "If I wanted her to display genuine shame for the camera, I'd have to take it further."
    else:


        "Veronica looked up at me coldly, but was quick to play along with the role she had committed herself to."
        scene w2_2760 with dissolve
        ver "I'm glad I mopped the floor today..."
        scene w2_2763 with dissolve
        "She let herself slump to her side, before rolling over onto her back and hiking her knees in the air."
        mct "(Not quite the picture-perfect pooch, but...)"
        play sound "sound effects/camera-phone-shutter.wav"
        "*Click*"
        "But nonetheless a nice, supplicant display for the camera."
        scene w2_2764 with dissolve
        "However, if I wanted her to display genuine shame for the camera, I'd have to take it further."

    if w2VeronicaDog == True:
        scene w2_2765 with dissolve
        mc "We're going on a small walk to the showers."
        scene w2_2766 with dissolve
        ver "By walk you mean you want me to crawl there, on my hands and knees?"
        scene w2_2765 with dissolve
        mc "You catch on quick."
    else:


        scene w2_2765 with dissolve
        mc "Next I'm going to ask you to walk over to the showers."
        scene w2_2766 with dissolve
        ver "By walk you mean you want me to crawl there, on my hands and knees?"
        scene w2_2765 with dissolve
        mc "You read my mind."


    scene w2_2767 with dissolve
    ver "I mean... how else would a \"bitch\" get around?"
    "I hesitated to call this being on board, but I was happy she wasn't putting up any fuss."

    if Veronica_Affection >=13:
        ver "Keep up, [mcf]."
    else:
        ver "Keep up, errand boy."

    scene w2_2768 with dissolve
    "In way of warning, Veronica methodically began her advance toward the shower area."
    "Thankfully, she wasn't in any rush. It was one hand at a time, one knee at a time - which gave me plenty of time to secure all the quality shots I wanted."
    scene w2_2769 with dissolve
    "The natural locomotion of the position was erotic on its own, but Veronica imbued every deliberate step forward with her patent-pending, hypnotizing sway that she readily deployed at moments like this."

    if w2VeronicaHeated == True:
        "For the benefit of the camera, she'd look back now and then, ever so inconspicuously with eyes rich with need."
        scene w2_2770 with dissolve
        "It was hot and I very much hoped the camera was picking up on even a fifth of that."
    else:
        "Every now and then, Veronica would look back and up at the camera in a naturally inconspicuous way. Giving me a good opportunity to snag a photo of her face without any sense of artifice."
        scene w2_2770 with dissolve
        "She had a talent for being photographed."

    mct "(All that's missing was a leash...)"
    scene w2_2771 with dissolve

    if w2VeronicaDog == True:
        mc "Heel, girl."
    else:
        mc "You can stop here."

    scene w2_2772 with dissolve
    "She had given me a lot in a short distance, but now it was time to up the ante."
    "As indomitable as her spirit is, Veronica was a prideful woman and the other side of pride is shame."
    scene w2_2773 with dissolve
    "The greater the pride, the greater the capacity for shame."
    hide screen textbox2 with dissolve

    menu:
        "Have Veronica urinate like a dog."(chg=["VeronicaShootPoints_up"]):
            $ w2VeroShootPoints += 1
            show screen textbox2 with dissolve
            if kat_polite == True:
                "She may have been able to stoically endure Mrs. Pulman's challenges up to this point, but there is a difference between having something done to you and doing it yourself."
            else:
                "She may have been able to stoically endure Kathleen's challenges up to this point, but there is a difference between having something done to you and doing it yourself."

            "Now, there will always be those who'll refuse to take ownership of their actions no matter the circumstance, but Veronica..."
            mc "How long has it been since you last used the restroom?"
            "Veronica wasn't one of those people. She was a self-determined and disciplined woman, qualities which naturally produced a strong sense of personal accountability."
            scene w2_2774 with dissolve
            ver "A few hours I guess. Why?"
            scene w2_2773 with dissolve
            mc "Do you need a bathroom break?"
            scene w2_2774 with dissolve
            ver "...I can hold it."
            scene w2_2773 with dissolve
            mc "Why, when you don't have to? You can go right here."
            scene w2_2775 with dissolve
            ver "You're out of your mind if you think I'm pissing on my floor."
            scene w2_2773 with dissolve
            mc "I don't think the mess is really your issue."

            if w1ExVeroPissedOn == True:
                scene w2_2775 with dissolve
                ver "Of course it isn't. I'd ask if you knew how embarrassing it is to piss in front of someone, but as I recall..."
                scene w2_2776 with dissolve
                ver "{b}You fucking peed on me last Saturday{/b}."
                scene w2_2777 with dissolve
                mc "Heh... uh, sorry about that."
                "There was no way she was forgetting about that, huh?"
                scene w2_2775 with dissolve
                ver "You're sorry? You're fucking sorry?"
                scene w2_2777 with dissolve
                mc "I... got caught up in the moment?"
                scene w2_2776 with dissolve
                ver "That's the worst excuse I've ever heard."
                scene w2_2777 with dissolve
                mc "I'm afraid that's the only one I've got."
                ver "......"
                scene w2_2775 with dissolve
                ver "...bah! That's not important anymore. I'm not-- "
            else:

                scene w2_2775 with dissolve
                ver "Of course it isn't. The issue is that it's fucking disgusting. I'm not--"

            scene w2_2779 with dissolve
            mc "Veronica..."
            scene w2_2780 with dissolve
            ver "..."
            hide screen textbox2 with dissolve

            menu:
                "Be nice. Reassure her."(chg=["veronica_up"]):
                    $ Veronica_Affection += 1
                    scene w2_2792 with dissolve
                    show screen textbox2 with dissolve
                    mc "You can do it."
                    scene w2_2793 with dissolve
                    ver "The fuck is that, the world's worst pep talk?"
                    scene w2_2794 with dissolve
                    mc "Good. Fast. Easy."
                    ver "What?"
                    $ renpy.music.set_volume(.3, 2, channel = "music")
                    scene w2_2802 with pixellate
                    mc "There's gotta be a better way to make money, right?"
                    scene w2_2803 with dissolve
                    ver "Good. Fast. Easy."
                    scene w2_2804 with dissolve
                    mc "...huh?"
                    scene w2_2803 with dissolve
                    ver "Good, fast, and easy. You can only pick two and I'm past {i}good{/i} and {i}easy{/i}."
                    scene w2_2804 with dissolve
                    mc "I'm not following..."
                    scene w2_2805 with dissolve
                    ver "This is the {i}good{/i} and {i}fast{/i} solution to my problem."
                    scene w2_2806 with dissolve
                    mc "Good? This is the {i}good{/i} in your book?"
                    scene w2_2805 with dissolve
                    ver "It's {i}good{/i} because all I have to do is put up with one shitty month, and after I win, I'll be able to buy some time and get my creditors off my back without digging myself deeper in the hole. It's the most direct, effective solution."
                    $ renpy.music.set_volume(1, 2, channel = "music")
                    scene w2_2786 with pixellate
                    mc "Those were your words to me when I asked why you joined the competition."
                    mc "I didn't really agree with them, but I admired your pragmatism."
                    scene w2_2785 with dissolve
                    ver "Fuck, you remembered that conversation and are actually using it against me?"
                    scene w2_2786 with dissolve
                    mc "I did and I am."
                    scene w2_2785 with dissolve
                    ver "I feel sorry for whoever you trick into marrying you."
                    scene w2_2786 with dissolve
                    mc "You see what I'm getting at though?"
                    scene w2_2785 with dissolve
                    ver "That I've made my own bed and now I've got to lie in it?"
                    scene w2_2786 with dissolve
                    mc "Well, you could actually say fuck this bed and walk away if you wanted."
                    scene w2_2785 with dissolve
                    ver "I {b}chose{/b} good and fast."
                    scene w2_2792 with dissolve
                    mc "You've already put up with much worse than tinkling in the shower. You're strong."
                    mc "Besides..."
                    scene w2_2807 with pixellate
                    ver "It's just sex work, isn't it? You're overselling it."
                    scene w2_2795 with pixellate
                    mc "It's just sex work, remember? You're overselling it."
                    "I pitched my voice lower to mimic Veronica's typical, orotund brand of derision."
                    scene w2_2796 with dissolve
                    ver "...? Is that supposed to be...?"
                    scene w2_2797 with dissolve
                    ver "Oh!"
                    stop music
                    play sound "sound effects/record-scratch.wav"
                    scene w2_2798 with dissolve
                    "To my complete shock, the towering Amazon suddenly keeled over in a violent burst of laughter."
                    play music "music/swagger.ogg"
                    ver "Ahahahaha...!"
                    scene w2_2799 with dissolve
                    with vpunch
                    ver "O-oh, man! Baah! Aaah!"
                    ver "Ah! You're fucking adorable?"
                    scene w2_2800 with wipeleft
                    mct "(...adorable?)"
                    ver "Mah! Aha, oh...!"
                    scene w2_2799 with dissolve
                    mc "Are you... okay?"
                    ver "Fahaha, ah! Oh! Y-yes!"
                    ver "Just give me a second!"
                    scene black with fade
                    stop music fadeout 3.0
                    "This continued on for an unbelievable minute."
                    "I didn't know what she thought was so funny, but it seemed to convince her, as her words to me were..."
                    scene w2_2801 with dissolve
                    ver "I was a fucking idiot to say that, huh?"
                    ver "What the hell do I know about any of this?"
                    scene black with fade
                    ver "Well, let's get to pissing on the floor, you disgusting perv."
                    "......"
                    "..."
                "Be mean and use a little push and pull to convince her.":


                    $ w2VeronicaMean = True

                    show screen textbox2 with dissolve
                    mc "That's the mentality of a human being and for the purpose of our shoot, you're not a human being."

                    if kat_polite == True:
                        "With Mrs. Pulman in my mind's eye, I did my best to spew her brand of venom."
                    else:
                        "With Kathleen in my mind's eye, I did my best to spew her brand of venom."

                    scene w2_2779 with dissolve
                    mc "You're a dirty bitch and dirty bitches don't care where they pee, do they?"
                    scene w2_2781 with dissolve
                    "Honestly, I was surprised she didn't punch me in that face then and there."
                    "Hell, she didn't even {b}look{/b} like she wanted to kill me. Instead she stared at me unflinchingly, unperturbed and impossible to read."
                    scene w2_2782 with dissolve
                    ver "They do if they're potty trained."
                    scene w2_2783 with dissolve
                    "An uneasy joke that betrayed what she was feeling. Time to switch gears and go in for the kill."
                    scene w2_2784 with dissolve
                    mc "I'm not Mrs. Pulman, Veronica. I'm not under the delusion that I can bend you to my will. You're your own woman."
                    scene w2_2785 with dissolve
                    ver "Fuck, you know how patronizing it is to hear a man say that?"
                    scene w2_2786 with dissolve
                    mc "In truth, I'm actually a little afraid of you. You sure as hell throw a mean right elbow."
                    scene w2_2785 with dissolve
                    ver "Ugh. Don't remind me of that slimy bastard putting his hands on me and what..."
                    scene w2_2787 with dissolve
                    ver "Came afterwards."
                    scene w2_2788 with dissolve
                    mc "All I'll say is that this week is about shame and the look on your face right now is... perfect."
                    ver "It is...?"
                    play sound "sound effects/camera-phone-shutter.wav"
                    "*Click*" with flash
                    "All I did was smile, hoping the word and its implications would hang in her mind."
                    ver "Perfect...?"
                    scene w2_2782 with dissolve
                    ver "Ha, it's fucked up, but it's true."
                    scene w2_2784 with dissolve
                    mc "Listen to me over the next measly half hour and we'll impress that old hag. I promise."
                    mc "However, I can't guarantee you'll have the winning photo shoot. That part is on you. Will you..."
                    scene w2_2789 with dissolve
                    ver "..gh!"
                    "The moment I grabbed her hair, the look that flashed across Veronica's face chilled my blood, but I kept my grip on the fiery strands of her gorgeous red hair."
                    scene w2_2790 with dissolve
                    mc "Will you forgive me for grabbing your hair like that and {b}choose{/b} to work with me for just thirty minutes? Put aside Veronica and play a part - not for me, but for--"
                    scene w2_2791 with dissolve
                    ver "Oh, shut up. Stop your blathering. I get the point."
                    ver "I'll do it. I'll play the part of the obedient dog, you just make sure everything you take is fire."
                    scene black with fade
                    play sound "sound effects/camera-phone-shutter.wav"
                    "*Click*"
                    mc "Thank you."
                    "......"
                    "..."

            play music "music/hypnosis.ogg"
            scene w2_2808 with fade
            "After some convincing, Veronica sluggishly crawled onto the shower tile and languished there awaiting my signal."
            "Apropos of the situation, she had the body language of a wet dog - droopy, deeply uncomfortable, and resigned to her fate."
            scene w2_2809 with dissolve
            mc "I'm ready when you are."
            scene w2_2810 with dissolve
            ver "You just want me to...?"
            scene w2_2809 with dissolve
            mc "Lift your leg like a dog and go."
            scene w2_2811 with dissolve
            "Veronica took a moment to think, before awkwardly lifting her right leg."
            "It, of course, was an unnatural pose for a human being and the uneasiness in her expression said as much."
            scene w2_2812 with dissolve
            mc "Whenever you want."
            scene w2_2813 with dissolve
            ver "Give me a second! It's coming!"
            ver "I'm feeling a little pee shy right now..."
            scene w2_2814 with dissolve
            "Veronica's face was a deep shade of crimson. More than I'd ever seen before."
            "In theory I thought this would work, but seeing the results was another thing. She'd never came close to looking like this in her audition or last week's exhibition, but here she was thoroughly disarmed."

            if toughness <=15:
                "Part of me even felt a little bad that this was my idea."

            play ambient "sound effects/urine-ground.wav"
            scene w2_2815 with dissolve
            ver "...ahh."
            "Finally, in a sight to behold, the proud woman began to urinate under the scrutiny of the camera's eye."
            scene w2_2816 with dissolve
            "It started out a mere trickle, before gaining momentum into a full blown stream."

            if date == "june09day":
                mct "(Come to think of it, I've never seen a woman pee before...)"
            else:
                "For the second time in two days, I was watching a woman pee..."

            play sound "sound effects/camera-phone-shutter.wav"
            "*Click*" with flash
            "Like a pervert, my eyes were glued to Veronica's sex, intensely fascinated with the sight in front of me - with the Amazon's burning embarrassment and the sheer eroticism of the act."
            "Veronica kept her eyes welded tight, as if trying to distance herself from the shameful act."
            mc "This is going to be a hit with the patrons, I'm sure of it."
            scene w2_2817 with dissolve
            ver "Goody goody..."
            "As I suspected, that inane assurance didn't help any. It probably just made things worse..."
            "In contrast to how long it took for it to finally start, Veronica's show of \"public\" urination abruptly petered out to an end."
            stop ambient
            scene w2_2818 with dissolve
            ver "You..."
            scene w2_2820 with dissolve
            ver "You get all that, errand boy?! You get all the shots you needed?"
            scene w2_2819 with dissolve

            if w2VeronicaMean == True:
                mc "I did and it was great. You looked absolutely ashamed."
                mc "You want to see?"
                scene w2_2820 with dissolve
                ver "No! Of course I don't, you dweeb."
            else:
                mc "I did. I know that was tough for you, but it's the path forward."
                mc "Curious about how it looked? You want to see?"
                scene w2_2820 with dissolve
                ver "Is that another one of your jokes?"
                scene w2_2819 with dissolve
                mc "Well, you laughed so hard last time I guess I got a little full of myself..."

            scene black with fade
            ver "So, what's next?"
        "Use intimacy to make her squirm."(chg=[("veronica_passion_up2", Veronica_Affection >= 11 or Veronica_Horniness >= 6), ("veronica_passion_up", Veronica_Affection < 11 and Veronica_Horniness < 6)]):

            $ w2VeronicaSquirm = True
            $ Veronica_Horniness += 1

            show screen textbox2 with dissolve
            "Up to this point, Veronica had boldly endured everything the club had thrown at her. It hadn't been pretty, but she's faced her challenges with relative stoicism."
            "If she was undaunted by a room full of perverts, what hope was there for me to embarrass her when it was just the two of us?"
            "However, therein lied my answer: {b}it was just the two of us{/b}."
            mc "Hey, Veronica..."
            "The atmosphere of the club was the furthest away from intimate. It was a whole other world, outlandish and borderline surreal. Speaking from personal experience, underneath the hot lights of the stage and the leering gazes, it was easy to lose yourself in the moment."
            mc "Why don't you spread your legs for me right now?"
            scene w2_2778 with dissolve
            "This wasn't that. This was two people. Veronica, proprietor and Olympian, and me... the errand boy."
            scene w2_2774 with dissolve
            ver "Okay...?"
            scene w2_2821 with dissolve
            hide screen textbox2 with dissolve
            "If I wanted to make her squirm for the camera, I didn't need to be extreme. I simply needed to slow things down and bring it down to a personal level."
            scene w2_2822 with dissolve
            "........."
            scene w2_2823 with dissolve
            "......"
            scene w2_2824 with dissolve
            "..."
            scene w2_2825 with dissolve
            ver "What the hell are you doing? Aren't you going to snap a picture?"
            scene w2_2826 with dissolve
            mc "Ah, sorry."
            play sound "sound effects/camera-phone-shutter.wav"
            scene w2_2827 with flash
            "*Click*"
            scene w2_2828 with dissolve
            mc "Sorry, got a bit distracted admiring the body of a medal-winning Olympian."
            scene w2_2829 with dissolve
            hide screen textbox2 with dissolve
            ver "Don't give me that! You were just face deep in my cunt last Saturday."
            ver "Not to mention all the other times you've seen me naked."
            scene w2_2830 with dissolve
            mc "Do you tire of seeing the sunrise?"
            "It took strength to deliver that corny line so even-handedly, but I did it."
            scene w2_2831 with dissolve
            ver "Oh, just kill me..."
            "If it was physically possible, her eyes would've violently rolled to the back of her head."
            scene w2_2830 with dissolve

            if toughness >=21:
                mc "Now touch yourself."
            else:
                mc "Next, I want you to rub yourself."

            scene w2_2832 with dissolve
            show screen textbox2 with dissolve
            "She wasted no time in drawing her hand to her quim."
            scene w2_2834 with dissolve
            mc "When was the last time you masturbated?"
            scene w2_2835 with dissolve
            ver "...?"
            scene w2_2836 with dissolve
            mc "Just tell me. There's a purpose."
            scene w2_2833 with dissolve
            ver "I guess... yesterday?"
            scene w2_2834 with dissolve
            mc "You guess?"
            scene w2_2833 with dissolve
            ver "No, it was this morning..."
            scene w2_2834 with dissolve
            mc "Really now? Do you do it every day?"
            scene w2_2837 with dissolve
            ver "It's become... more frequent."
            scene w2_2838 with dissolve
            mc "Do you watch porn while you do it?"
            scene w2_2837 with dissolve
            ver "No - what's with these questions?"
            scene w2_2838 with dissolve
            mc "What do you think about?"
            scene w2_2839 with dissolve
            "Veronica looked at me like she was trying to figure me out."
            scene w2_2840 with dissolve
            ver "I think about a ton of different things..."
            scene w2_2841 with dissolve
            mc "Be specific."
            scene w2_2842 with dissolve
            ver "Lately I've been thinking about when I put that old bitch in her place. Fuck, that was hot..."
            scene w2_2843 with dissolve
            mc "You actually think about that night?"
            scene w2_2845 with dissolve
            ver "Hell, yeah. Well... that part of it. She's repulsive and a piece of crap, but that's what made her humiliation so fun."
            scene w2_2844 with dissolve
            mc "That's a pretty dangerous way to play the game, considering she's the one that decides the results."
            scene w2_2845 with dissolve
            ver "Maybe it is, but... I think she likes the dynamic it brings. Makes me a bigger target, but it makes her little circus more dramatic - and that's all she cares about."
            scene w2_2844 with dissolve
            mct "(Is she saying... she antagonizes Mrs. Pulman not only out of contempt or anger, but... on purpose?)"
            scene w2_2842 with dissolve
            ver "Did you enjoy watching that bitch get taken down a peg?"
            scene w2_2843 with dissolve
            hide screen textbox2 with dissolve

            menu:
                "Tell her you honestly did":
                    show screen textbox2 with dissolve
                    "No harm in being honest."
                    mc "Heh, hands down, it was the best part of the night."
                    scene w2_2845 with dissolve
                    ver "I hope I get the chance to turn the tables again. I wish more of those freaks got to see their queen bitch cream herself from having her fat, old ass spanked."
                    scene w2_2844 with dissolve
                    mc "You sound like her."
                    scene w2_2842 with dissolve
                    ver "It's a little different. It's not like I'm talking about punishing poor ol' Rosie."
                    scene w2_2843 with dissolve
                    "The smile on her face suggested to me she might also like to do that..."
                "Tell her she went too easy on her.":

                    show screen textbox2 with dissolve
                    mc "I would've pushed her even harder. You took it easy on her."
                    scene w2_2840 with dissolve
                    ver "Nah, that woman's straight as an arrow. It wasn't just about roughing her up, I had to make her cum remember?"
                    scene w2_2844 with dissolve
                    mc "Right, yeah..."
                    scene w2_2845 with dissolve
                    ver "I pretty much fucking threaded the needle there."
                "Tell her that whole night runs together in your head.":


                    show screen textbox2 with dissolve
                    mc "That whole night is one big blur to me. It all runs together."
                    scene w2_2844 with dissolve
                    "That wasn't entirely true, I remembered certain parts of it in vivid details, but..."
                    "Even though it was just a few weeks ago, it felt like a lifetime. So much had happened since in my normally slow and uneventful life."
                    "I knew I felt something, but I couldn't remember if it was repulsion or arousal..."

            scene w2_2846 with dissolve
            mc "Anything else?"
            ver "Hmm...?"
            mc "What else do you think about when you touch yourself?"
            ver "What else..."
            scene w2_2847 with dissolve
            "She looked at me dubiously as if weighing exactly what she wanted to divulge."

            if Veronica_Affection >= 11 or Veronica_Horniness >= 7:
                $ Veronica_Horniness += 1
                scene w2_2848 with dissolve
                ver "This morning I thought about when you ate me out."
                scene w2_2849 with dissolve
                "That was... surprising."
                scene w2_2850 with dissolve
                mc "Really?"
                scene w2_2849 with dissolve
                "I could feel the pure smugness creep across my face with her admission."
                scene w2_2848 with dissolve
                ver "That's right. What do you think about that, errand boy?"
                scene w2_2850 with dissolve
                mc "I'm surprised you're telling me that... why are you?"
                scene w2_2848 with dissolve
                ver "Because... I know what you're trying to do here. It's a good plan."
                ver "Go ahead, take it."
                scene w2_2851 with dissolve
                "She admitted something embarrassing, on purpose."
                play sound "sound effects/camera-phone-shutter.wav"
                "*Click*" with flash
                mc "Beautiful."
                scene w2_2848 with dissolve
                ver "What do you want me to do next?"
            else:

                scene w2_2845 with dissolve
                ver "I know what you're trying to do. You're trying to embarrass me."
                scene w2_2844 with dissolve
                mc "Guilty as charged. Are you going to answer the question then?"
                scene w2_2840 with dissolve
                ver "Hmm... well, I mean... there's all sorts of things. I have a pretty active imagination."
                scene w2_2841 with dissolve
                mc "What did you think about this morning?"

                if minaGym == True:
                    scene w2_2840 with dissolve
                    ver "Blondie."
                    scene w2_2841 with dissolve
                    mc "You mean Felicia?"
                    scene w2_2840 with dissolve
                    ver "No. Mina."
                    "...heh, yeah. That makes sense."
                    "I couldn't fault her for that."
                else:
                    scene w2_2845 with dissolve
                    ver "Oh, you know. Odds and ends. Recollections and past feelings."
                    scene w2_2844 with dissolve
                    mc "Really? You can do that?"
                    scene w2_2845 with dissolve
                    ver "Oh yeah. When it comes to arousal, women aren't as visual as men."

                "Unfortunately, that admission didn't seem to bother the Amazon."
                scene w2_2852 with dissolve
                mc "Can't you give me..."
                scene w2_2853 with dissolve
                ver "What are you talking about?"
                ver "I'm knuckle deep in my snatch here, it IS embarrassing. DO you think I'm a robot?"
                play sound "sound effects/camera-phone-shutter.wav"
                scene w2_2854 with dissolve
                "*Click*"
                "That's it. That's the look."
                mc "You hide it pretty well."
                scene w2_2848 with dissolve
                ver "I know. So... what do you want me to do next?"

    scene w2_2855 with dissolve
    mc "Hmm..."
    scene w2_2856 with dissolve
    mc "Crawl."
    scene w2_2857 with dissolve
    ver "Again?"
    scene w2_2856 with dissolve
    mc "Crawl to me."
    scene w2_2856 with dissolve
    ver "..."
    scene w2_2858 with dissolve
    ver "Oooookay."
    scene w2_2859 with dissolve
    "With a slight shrug, she got down on all fours and closed the short distance between us."
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*"
    scene w2_2860 with dissolve
    ver "Now what?"
    scene w2_2859 with dissolve
    mc "Now I want you to... lick me."
    scene w2_2862 with dissolve
    ver "Where?"
    scene w2_2861 with dissolve
    mc "Nothing obscene, just..."
    scene w2_2863 with dissolve

    if w2VeronicaDog == True:
        mc "Lick me like an affectionate puppy."
    else:
        mc "My leg. Like a dog would."

    scene w2_2864 with dissolve
    "Instead of grumbling, Veronica lowered her neck, brought her lips to my shin, and..."
    "And..."
    "AAAAND...."
    scene w2_2865 with dissolve
    "Gave my leg a short, cute, tiny tickle that only remotely resembled a lick."
    scene w2_2866 with dissolve

    if w2VeronicaDog == True:
        mc "Come on, you can do better than that."
    else:
        mc "Put a little more heart into it, please."

    ver "Mmmmph..."
    scene w2_2867 with dissolve
    hide screen textbox2 with dissolve
    "A little more begrudgement begat a more exploratory lick."
    scene w2_2868 with dissolve
    play sound "sound effects/camera-phone-shutter.wav"
    "While she worked her way up and down my shin, I made sure to take as many pictures as I could."
    scene w2_2869 with dissolve
    "Most would be trash, but a few were guaranteed to be keepers."

    if w2VeronicaHeated == True:
        "She proved to be shockingly dutiful in her treatment."
        scene w2_2870 with dissolve
        "The next thing that happened came out of left field."
        "Veronica brought her face low to the ground in a face down, ass up position and hovered her head above my shoe."
        scene w2_2871 with dissolve
        "Next she looked up at me with the most sex-oozing glare I could ever picture, full of devious intent and willful submission."
        play sound "sound effects/camera-phone-shutter.wav"
        scene w2_2872 with dissolve
        "*Click*"
        mct "(Ha...!)"
        "She kissed the tip of my sneakers without a trace of hesitation. Entirely of her own volition."
    else:

        "She proved competent and unflinching when it came to the task."

    scene w2_2873 with dissolve
    ver "You get some good shots?"
    scene w2_2874 with dissolve
    "I simply nodded."
    stop music fadeout 3.0
    scene black with fade
    show screen textbox2 with dissolve
    ver "Good. What next?"
    scene w2_2879 with dissolve
    mc "We need something more substantial."
    ver "\"Substantial\", huh?"
    scene w2_2880 with dissolve
    "She looked like she had an idea."
    scene w2_2881 with dissolve
    mc "What is it?"
    scene w2_2882 with dissolve
    ver "I do have some toys here."
    scene w2_2883 with dissolve
    "I must have looked at her quizzically, because she answered what I was thinking."
    scene w2_2884 with dissolve
    ver "I live here, remember? Where else would I keep them? A girl has needs."
    scene w2_2885 with dissolve
    mc "You want to use them?"
    "She's had a large amount of control over the day's proceedings, which for some reason, felt ungratifying."
    scene w2_2886 with dissolve
    ver "You got something else in mind?"
    scene w2_2885 with dissolve
    mc "No. Go get your toys."
    scene w2_2887 with dissolve

    if Veronica_Affection >= 13:
        ver "Be right back, [mcf]."
    else:
        ver "Be right back, errand boy."

    scene black with fade
    "......"
    "..."
    "Veronica wasted no time as soon as she got back."
    scene w2_2888 with dissolve
    play sound "sound effects/vib-start.wav"
    "The massager whirled to life, the walls of the near-empty locker room carrying the soft drone of its motor with a blaring clarity."
    scene w2_2889 with dissolve
    stop sound fadeout 2.0
    $ renpy.music.set_volume(.2, 0, channel = "ambient")
    play ambient "sound effects/vib-ongoing.wav"
    "A blaring clarity that dulled as she pressed the head of the wand against her vulva."
    ver "Ah..."
    play music "music/hypnosis.ogg"
    scene verog_d01_a with dissolve
    hide screen textbox2 with dissolve
    "The moment the tool touched her sex, a quiet moan left her lips."
    mc "You're feeling it that fast?"
    ver "Shut up. Do your job."
    scene verog_d01_a with dissolve
    show verog_d01
    mct "(My job...)"
    "This has yet to feel like one."
    "All the while I paused to consider my position, Veronica had fully and shamelessly set on the task of pleasuring herself, running the massager down the length of her labia and coaxing her sweet spot from its hood."
    "Of course, I had taken a couple of pictures in the meantime, but I wasn't close to being done."
    "Veronica was at the helm of this ship and she knew these waters well. Given enough time, the camera's eye would catch even more lovely and debauched expressions."
    mc "I want you to keep going. Keep pleasuring yourself, as if I'm not even here."
    ver "Mmh..."
    scene w2_2890 with dissolve
    "She pressed the tool firmly into her crotch before I could even finish my words, causing the flexible rubber head of the wand to crane and conform to the contours of her sex."
    ver "...alright."
    scene verog_d02_a with dissolve
    show verog_d02
    mct "(...did I even have to tell her?)"
    ver "A~ha..."
    "Taking \"pretending I'm not here\" to heart, Veronica relaxed her neck and tightly shut her eyes."
    ver "Aha, aha..."
    "It shouldn't take long before her normally even-keeled expression is gnarled by physical indulgence and I would get the shots that I was looking for."
    "I enjoyed the show for a few minutes, watching the Amazon work her lower mouth with relentless repetition. "
    scene verog_d01_a with dissolve
    show verog_d01
    "Veronica's wrist never seemed to tire or falter from pleasure, she just continued to press the massager into her genitalia, using a soft rocking motion to tease and stimulate her now erect pink nub."
    ver "Aha, aha, aha..."
    "She was lost in her own little world, freely letting faint moans escape her throat without any care for my presence."
    "That, the dull buzz of the messager, and the sporadic click of the camera's shutter was all that filled the room."
    scene verog_d02_a with dissolve
    show verog_d02
    "......"
    "..."
    ver "Ha... ha...! Come to think of it, I've never masturbated in front of another person before. Not my wife, not a f-fling...!"
    mc "Why would you, when there's better things you can be doing with them? Are you suddenly feeling self-conscious?"
    ver "Not so suddenly..."
    "Even while she spoke, she didn't miss a beat. Her hand never ceased."
    scene w2_2891 with dissolve
    ver "Ah, f-fuck...!"
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*"
    "That was the look I was searching for. A surge of pleasure racked Veronica's body, causing her face to morph into something unkempt and erotic."
    scene w2_2892 with dissolve
    ver "Mmh...!"
    mc "Don't stop!"
    "Caught up in the moment, wanting her to go even further, I involuntarily barked out a command."
    mct "(Again, not that I had to tell her...)"
    hide screen textbox2 with dissolve
    scene verog_d03_a with dissolve
    show verog_d03
    "Her free hand found its way to her breasts, roughly cupping it while her other kept on task by increasing the tempo."
    "Her eyes grew progressively more unfocused. Her soft pink tongue peeked out of her mouth and the corner of her lip furled in concentration."

    if w2VeronicaHeated == True:
        "If going hands-on with Veronica before the shoot hadn't already stoked my desire, this wanton show would have done the job."
    else:
        "Everything leading up to this in the shoot was hot, but with this particular moment, the flame of desire was fully ignited in me."

    "I was rock fucking hard."
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*" with flash
    "Her lower body swayed as if to meet the mounting bliss half-way, working in tandem with her hand to climb the peaks of pleasure."
    ver "Mmmhhaa...!"
    "Her moans went from faint and intermittent to lusty and sharp."
    ver "Mmmh, ah~ ah...!"
    "I wanted to ask if she was faking, but with just me and her, she had no reason to in this situation."
    mct "(So she's a screamer...)"
    mct "(She is intense, no surprise it extends even to the bedroom...)"
    $ renpy.music.set_volume(.5, 1.5, channel = "music")
    scene w2_2909 with pixellate
    "......"
    scene w2_2910 with vpunch
    "..."
    mct "(Then again, I guess I learned that from when she almost popped my head like a melon...)"
    $ renpy.music.set_volume(1, 2, channel = "music")
    scene verog_d04_a with pixellate
    show verog_d04
    ver "Mfffh...!"
    "She must have shared in my thoughts, as her hand moved from her breast and up to her mouth in an attempt to squash her self-indulgent moans."
    ver "Mffhha... mhaa....!"
    mct "(Seems like a waste this isn't a video...)"

    if kat_polite == True:
        mct "(I bet Mrs. Pulman would love to hear this.)"
    else:
        mct "(I bet Kathleen would love to hear this.)"

    mct "(Veronica might have taken best shoot from her cries alone if that was the case.)"
    play sound "sound effects/camera-phone-shutter.wav"
    "*Click*"
    ver "Mmmf! Ah~hhha...~"
    "Whether it was intentional or not, she was putting on quite the show."
    "Her whole body became part of the act and the way she half-heartedly covered her mouth was uncharacteristically cute."
    "While I was enjoying the sight and sounds, my eyes wondered over to the pink dildo that Veronica had scrounged up alongside the massager."
    ver "Mmh...! Mh...!"
    "It was simply laying to her side, lonely and unused, and the Amazon's mouth was looking conspicuously unoccupied apart from the stifled moans being pried from her lips."
    scene w2_2893 with dissolve
    "It gave me an idea."
    hide screen textbox2 with dissolve
    menu:
        "Use the dildo to plug that hole.":
            "Seeing as she went to the trouble of retrieving it, it would be a shame not to make use of it, even if it wasn't for its intended use."
            scene w2_2894 with dissolve
            ver "Ah~hammf..."
            mct "(This should make for a nice final flourish, I think.)"
            scene w2_2895 with dissolve
            ver "MffHa... ha....!"
            scene w2_2896 with dissolve
            mc "Veronica..."
            ver "Ah..! Mmmf..!"
            mc "Veronica!"
            scene w2_2897 with dissolve
            ver "Ah...? W-what?"
            mc "Open your mouth."
            scene w2_2898 with dissolve
            "She gave me a long look, before her eyes fixated on the pink toy in my hand and came to an understanding."
            scene w2_2899 with dissolve
            ver "Ohhwkay~"
            "Given the situation, she was being compliant."
            if toughness >=20:
                mc "Let's see how much you can take."
            else:
                mc "Let me know if I go too deep."
            scene w2_2900 with dissolve
            "Slowly, I worked the fake cock past the Amazon's parted lips."
            scene w2_2901 with dissolve
            "Veronica's mouth openly accepted the foreign invader as it gently worked its way past her tongue."
            ver "Gwuh..."
            scene w2_2902 with dissolve
            "Until the gratuitously pink phallic toy was close to knocking against the back of her throat."
            ver "Mmhw..."
            play sound "sound effects/camera-phone-shutter.wav"
            "*Click*" with flash
            scene w2_2903 with dissolve
            "Her dumb expression was pure gold for the camera, and at the same time, she never ceased working toward her own gratification."
            mct "(Hmm...)"
            "I do have room to work the dildo down a little further. The angle might make it a tad unpleasant for Veronica, though..."
            hide screen textbox2 with dissolve

            menu:
                "Deep throat this bitch"(chg=["VeronicaShootPoints_up"]):
                    $ w2VeroShootPoints +=1
                    "...yes, I would VERY much like to see just how far she can take it."
                    scene w2_2904 with vpunch
                    ver "*Cough...!* Hwack...! Kha...!"
                    "Slowly but firmly, the toy touched the back of the Amazon's throat, causing her to momentarily sputter."
                    play sound "sound effects/camera-phone-shutter.wav"
                    scene w2_2905 with vpunch
                    "*Click*"
                    ver "*Cough...!* Kha...! Ha...! Heah..."
                    scene w2_2906 with dissolve
                    "I held it there, going no further for maybe a dozen seconds, to allow her time to adjust to its occupancy. Amazingly, she didn't try rebuff any further advance."
                    mc "I'm going all the way to the base now. Are you ready?"
                    ver "Gwhooo whetehvar...!"
                    scene w2_2907 with vpunch
                    "Bending the toy so that it would snake down her throat, I made the final push for complete 100 percent deepthroat."
                    ver "*Cough!* Fhwe...! Khak...!"
                    scene w2_2908 with dissolve
                    mc "Breathe through your nose."
                    ver "Guhh... *Cough!* Kha... euch..."

                    if toughness >=20:
                        mc "You doing alright? You okay?"
                    else:
                        mc "You okay? You want me to take it...?"

                    scene w2_2911 with dissolve
                    ver "*Cough* Ghuhh..."
                    "Rather than answer me..."
                    scene w2_2908 with dissolve
                    ver "Ah... mmh....ghwwa..."
                    "Her coughing rescinded and was replaced by the previous sounds of self-debasement."
                    scene w2_2911 with dissolve
                    ver "Ah...!"
                    "The pleasure from the massager had won out over her discomfort..."
                    scene w2_2912 with dissolve
                    play sound "sound effects/camera-phone-shutter.wav"
                    "*Click*"
                    mc "I'll let you hold it yourself, I'm going to get some final pictures."
                "This is far enough, focus on getting the final shots.":





                    scene w2_2913 with dissolve
                    mc "You doing alright? You okay?"
                    scene w2_2911 with dissolve
                    ver "Ahwhuh...! *Cough!* Hwahk..."
                    "My question prompted an involuntarily nod, causing the toy to scrape against the back of her throat and making the Amazon momentarily sputter."
                    mc "Heh, sorry for asking..."
                    scene w2_2912 with dissolve
                    play sound "sound effects/camera-phone-shutter.wav"
                    "*Click*"
                    mc "I'll let you hold it yourself, I'm going to get some final pictures."

            scene verog_d05_a with dissolve
            show verog_d05
            "Positioning myself back at the foot of the bench, I got the last handful of shots while Veronica carried on -- a silicone dick hanging out of her mouth and a gray massager snuggled against her twat."
            "A far cry from the woman in the posters adorning the gym, but oddly enough in a fucked-up way, a formidable image in its own right."
            "After securing the final photos, I let the thing carry on more than necessary."
            "Veronica was off in her own little world and I didn't mind idly standing by and watching."
            scene black with fade
            "Still, all good things must come to an end."
            scene w2_2925 with fade
            mc "Hmmm... that's enough."
        "Use your own personal tool for the deed."(chg=["veronica_down","veronica_passion_up"]):


            $ w2VeronicaTBag = True
            $ Veronica_Horniness +=1
            $ Veronica_Affection -= 1
            "While the obnoxiously pink fake cock would've been fun to use, it also planted another idea in my head."
            scene w2_2914 with dissolve
            mc "Veronica..."
            ver "Ah..! Mmmf..!"
            scene w2_2896 with dissolve
            mc "Veronica...!"
            scene w2_2897 with dissolve
            ver "Ah...? W-what?"
            scene w2_2915 with dissolve
            mc "I'm going to do something you're not going to be happy with, but you'll trust me right?"
            mc "It's all for making those perverted bastards happy."
            scene w2_2897 with dissolve
            ver "Mffh... ha... ah? Eh..."
            ver "W-whatever, just do what you're thinking."
            scene w2_2915 with dissolve
            "Not for a second while processing my request did she slow down working her lower mouth."

            if toughness >=22:
                mct "(What a horny bitch.)"
            else:
                mct "(She's really, REALLY feeling it.)"

            scene black with fade
            "She watched me undress with clouded, half-lidded eyes, but she didn't stop me."
            scene w2_2916 with dissolve
            ver "Ah... what are you..."
            play sound "sound effects/slap1.wav"
            scene w2_2917 with vpunch
            "*Plop*"
            "My answer came when I shadowed Veronica's cute button nose with my erect dick and blanketed her forehead with my heavy balls."
            scene w2_2918 with dissolve
            ver "Gh...!"
            "The warmth of Veronica's face felt heavenly to the underside of my dick."
            mc "Trust me, the old lady will eat this up."
            play sound "sound effects/camera-phone-shutter.wav"
            "*Click*"
            scene verog_d06_a with dissolve
            show verog_d06
            "--it also came with the added bonus of me enjoying the dominant, humiliating position I was holding over her."
            mc "Don't worry about what I'm doing up here, just keep doing what you're doing."

            if w2VeronicaDog == True or w2VeronicaMean == True:
                mc "... yeah, just keep masturbating while you've got my balls on your forehead, bitch."
                "The position DEFINITELY went to my head."
                mc "That's all you need to worry about."
            else:
                mc "Just keep doing what you're doing."

            ver "Ah... mmh....ghwwa..."
            "Shockingly, she did just that. She didn't scoff, crack or joke, or rebuff me: she simply returned to her self-indulgence with nary a peep."
            ver "Ah... fhwa..."
            scene verog_d07_a with dissolve
            show verog_d07
            play sound "sound effects/camera-phone-shutter.wav"
            "*Click*"
            mct "(Come to think of it, I haven't showered since I worked out...)"
            "Somehow, that made the whole thing better in my perverted mind."

            menu:
                "Humiliate her further"(chg=["VeronicaShootPoints_up"]):
                    $ w2VeroShootPoints +=1
                    scene w2_2919 with dissolve
                    mc "You like the smell of sweaty balls?"
                    mc "You haven't slowed down."
                    scene w2_2920 with dissolve
                    ver "Ah...! Ah..! Sh-shut..."
                    scene w2_2919 with dissolve
                    ver "Mmhh..."
                    play sound "sound effects/camera-phone-shutter.wav"
                    "*Click*"
                    mc "You can't really pretend otherwise in this situation."
                    scene w2_2920 with dissolve
                    ver "Shut up, it's f-for the shoot--"
                    scene w2_2921 with dissolve
                    play sound "sound effects/slap2.wav"
                    scene w2_2922 with vpunch
                    "*Smack*"
                    mc "Get a good whiff of it, cunt."
                    scene w2_2919 with dissolve
                    ver "Mfg... ha..."
                    "All the while, the massager remained snugly hugging her twat."
                    mc "Not just that, give it a little lick -- for the camera, of course."
                    scene w2_2920 with dissolve
                    ver "Ah... you fucking.."
                    scene w2_2921 with dissolve
                    play sound "sound effects/slap2.wav"
                    scene w2_2922 with vpunch
                    "*Smack*"
                    scene w2_2923 with dissolve
                    mc "I said LICK the underside of my shaft, bitch."
                    scene w2_2920 with dissolve
                    ver "Ah... whatever."
                    scene w2_2924 with dissolve
                    ver "Mfwww..."
                    play sound "sound effects/camera-phone-shutter.wav"
                    "*Click*"
                    "Instead of wasting her breath, she relented to my request, gingerly running the underside of her tongue across the bottom of my shaft."
                    scene w2_2919 with dissolve
                    "It was quick, so quick that I almost missed it, but I got the shot."
                    scene verog_d07_a with dissolve
                    show verog_d07
                    "I wasn't going to push my luck trying to get anything else out of her."
                "Don't make this anymore unpleasant for Veronica.":


                    "No, this is enough. Even if the primary purpose is taking a bunch of depraved photos, I'm also already taking advantage here."

            "After securing the final photos, I let the thing carry on more than necessary."
            "Veronica was off in her own little world and I didn't mind idly standing by and enjoying the sensation of her hot breath tickling my junk."
            "A far cry from the woman in the posters adorning the gym, but oddly enough in a fucked-up way, a formidable image in its own right."
            scene black with fade
            "Veronica continued on for a little bit after I slinked away to get dressed, but eventually all good things must come to an end."
            scene w2_2926 with fade
            mc "Hmmm... that's enough."

    stop music fadeout 3.0
    ver "Mmmfh... ha... ha...!"
    scene w2_2927 with dissolve
    mc "Veronica, that's enough. You can stop."
    ver "H-huh...? What...?"
    play music "music/devious-little-smile.ogg"
    mc "I've got all the shots I need. You can stop."
    scene w2_2928 with dissolve
    "A striking look of disappointment wore plain as day on her face and her hand conspicuously kept moving."
    ver "Are you sure? I'm al-almost..."
    ver "Almost..."
    mc "The shoot's over. You can stop--"
    ver "Almost... almost... ah, fuck!"
    $ renpy.music.set_volume(1, 0, channel = "ambient")
    scene w2_2929 with dissolve
    "As if coming to her senses, the Amazon angrily sprang up."
    scene w2_2930 with dissolve
    scene w2_2931 with vpunch
    play sound "sound effects/thud-floor.mp3"
    stop ambient
    ver "God damn it!"
    "It was quite the loud impact given how big and empty the locker room was."
    scene w2_2932 with dissolve
    mc "...uh, you should treat your precious things better..."
    scene w2_2933 with dissolve
    ver "{b}Shut up{/b}. Shut up, shut up, {b}shut up{/b}!"
    scene w2_2934 with dissolve
    "Veronica looked confuddled, an extreme look of frustration -with a hint of shame- on her face."
    "Her eyes were pointing my way, but they weren't looking at me."
    "She was looking past me, the walls, past the city itself."
    ver "......"
    ver "..."
    scene w2_2935 with dissolve
    show screen textbox2 with dissolve
    "Abruptly, she stood up and came face to face with me."
    "Her agitation was concerning enough when it was undirected and aloof, but now that it was pointed at me..."
    scene w2_2936 with dissolve
    if not persistent.veroW2GymSceneGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.veroW2GymSceneGallery = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    "......"
    "..."
    "I felt a genuine unease."
    $ renpy.end_replay()

    if Veronica_Affection >=10 and w2VeronicaHeated == True or Veronica_Horniness >=8:
        scene w2_2937 with dissolve
        ver "Damn it, it wasn't... I'm so..."
        jump w2VeronicaphotoshootExtended
    else:
        stop music
        scene w2_2939 with dissolve
        ver "I can't believe I even considered that..."
        scene w2_2940 with dissolve
        mc "Considered what?"
        scene w2_2939 with dissolve
        ver "Don't worry about it. We're done here, I guess?"
        scene w2_2940 with dissolve
        mc "Yeah... that was an interesting set."
        scene w2_2943 with dissolve
        ver "Then I'm going to go de-stress in the sauna for a bit. Let yourself out, I'm kinda sick of looking at you."

        if VeroFlag == True:
            scene w2_2944 with dissolve
            mc "Heh, you say that, but..."

            "I wanted to talk with Veronica more and try to figure out just how Samson figured into her business."
            ver "...but?"
            scene w2_2944 with dissolve
            mc "Mind if I join you for a soak?"
            scene w2_2945 with dissolve
            ver "..."
            scene w2_2944 with dissolve
            mc "The place is closed and it's not like we haven't seen each other--"
            scene w2_2946 with dissolve
            ver "Stop talking. Just..."
            ver "Just... ah, just give me a second to fire it up."
            scene w2_2947 with dissolve
            mc "Hehe, thanks! If you're still sick of me, I can sit in the corner or something."
            scene black with fade
            jump w2VeronicaFlag
        else:
            scene w2_2945 with dissolve
            "Seeing no reason to stick around, and not wanting to piss her off more than she already seemed to be, I thought that wasn't a bad idea."
            scene w2_2944 with dissolve
            mc "Enjoy your soak."
            scene w2_2948 with dissolve
            ver "Pssh, yeah."
            scene w2_2949 with dissolve
            ver "Fuck, is it broken?!"
            scene black with fade
            "Yeah, just gonna \"de-stress in the sauna\", huh?"
            "......"
            "..."
            mc "Have fun."

            if date == "june09day":
                jump w2HanaNight1
            else:
                jump w2HanaNight2


label w2VeronicaphotoshootExtended:

    if _in_replay:
        show transitionveronica02 with cmet
        show screen textbox2 with dissolve
        "Please set [mcf]'s personality (toughness score) for this replay."
        hide screen textbox2 with dissolve
        menu:
            "Nice guy (Toughness: 0)":
                $ toughness = 0
            "Mischevious (Toughness: 18)":
                $ toughness = 18
            "Asshole (Toughness: 30)":
                $ toughness = 30
        show screen textbox2 with dissolve


    scene w2_2938 with dissolve
    mc "You're what?"
    scene w2_2940 with dissolve
    "Once again, the towering woman narrowed her focus on me."
    scene w2_2942 with dissolve
    "Her face was sullen and apprehensive, like a prisoner on her way to execution."
    scene w2_2939 with dissolve
    ver "Ugh..."
    scene w2_2940 with dissolve
    "Her stare bore a hole right through me, while seemingly weighing something tumultuous in her head."
    scene w2_2941 with dissolve
    ver "I can't believe I'm going to do this."
    mc "Do wha--"
    play sound "sound effects/thud-floor.mp3"
    scene w2_2950 with hpunch
    mc "Eheh?"
    scene w2_2951 with dissolve
    "A strong push had me pinned against the wall."
    scene w2_2952 with dissolve

    if Veronica_Affection >=13:
        ver "That wasn't satisfying for you either, was it [mcf]?"
    else:
        ver "That wasn't satisfying for you either, was it errand boy?"

    scene w2_2951 with dissolve
    "I knew what she was getting at, yet I still asked smugly."
    scene w2_2953 with dissolve
    mc "What do you possibly mean?"
    scene w2_2954 with dissolve
    ver "Don't make this more painful than it already is for me."

    if w2VeronicaTBag == True:
        ver "You just spent five minutes with your disgusting cock sitting on my face. I could see how big and hard you were during that pet play shit too."
    else:
        ver "I could see how big and hard you were during all that pet play shit."

    scene w2_2953 with dissolve
    mc "Yeah, and...?"
    scene w2_2955 with dissolve
    ver "I don't know why, but this past week I've been especially... ah..."
    scene w2_2957 with dissolve
    "She trailed off almost with a plaintive whimper."
    scene w2_2956 with dissolve
    ver "It's... it's fucking torture to just stop like that, okay?!"
    scene w2_2958 with dissolve
    mc "I know I said stop, but you could've finished if you wanted."
    ver "I'm past that satisfying me, I need--"
    ver "Ah, ugh! Listen... I'll scratch your back, if you scratch mine."
    "Despite her cute consternation, she succeeded in mustering her typical brand of bluntness."
    scene w2_2959 with dissolve
    ver "This is a one-time offer."
    scene w2_2960 with dissolve
    "I never anticipated Veronica sticking her neck out like this, she must be really pent up."
    scene w2_2961 with dissolve
    mc "So you want to do a little quid pro quo?"
    scene w2_2959 with dissolve
    ver "I don't know what the hell that means."
    scene w2_2961 with dissolve
    mc "It's Latin for--"
    scene w2_2962 with dissolve
    ver "Can it. Just give me your answer, before I die of humiliation."
    hide screen textbox2 with dissolve
    scene w2_2960 with dissolve

    menu:
        "Scratch Veronica's back."(chg=["veronica_passion_up2","veronica_up3"]):
            $ w2VeronicaScratch = True
            $ Veronica_Affection += 3
            $ Veronica_Horniness += 2
            scene w2_2961 with dissolve
            show screen textbox2 with dissolve
            mc "Seems like a big itch, but I'll try my best."
        "Turn her offer of satisfaction down.":

            scene w2_2963 with dissolve
            show screen textbox2 with dissolve
            stop music fadeout 3.0
            mc "I..."
            mc "I don't think you broke your massager. I think that would be a better alternative than what I could provide you."
            scene w2_2964 with dissolve
            "I did my best to look conciliatory."
            ver "..."
            scene w2_2965 with dissolve
            ver "Fuck. I can't believe I even considered that."
            scene w2_2966 with dissolve
            mc "Things did get pretty heated there, plus you didn't get a chance to finish."
            scene w2_2965 with dissolve
            "I tried to sound understanding without it being too embarrassing for her."

            if VeroFlag == True:
                scene w2_2968 with dissolve
                ver "*Sigh* I think I'm just going to de-stress in the sauna. You want to join?"
                scene w2_2967 with dissolve
                "To my shock, she extended an unexpected invitation my way."
                mc "Actually..."

                "I did want to talk with Veronica more and try to figure out just how Samson figured into her business."
                scene w2_2967 with dissolve
                mc "You're asking me to sit in the sauna with you?"
                scene w2_2968 with dissolve
                ver "It's dangerous to soak alone. I could pass out and no one would know."
                scene w2_2967 with dissolve
                mc "I'm just giving you a hard time. I don't need convincing."
                scene w2_2968 with dissolve
                ver "Give me a sec then, it takes a minute to fire up."
                scene black with fade
                "......"
                "..."
                jump w2VeronicaFlag
            else:
                scene w2_2968 with dissolve
                ver "Actually, I'm just going to go de-stress in the sauna for a bit. Let yourself out, will ya? I'm too embarrassed to look at you."
                scene w2_2967 with dissolve
                "Seeing no reason to stick around, I thought that wasn't a bad idea."
                mc "Enjoy your soak."
                scene w2_2948 with dissolve
                ver "Pssh, yeah."
                scene w2_2949 with dissolve
                ver "Fuck, is it broken?!"
                scene black with fade
                "Yeah, just gonna \"de-stress in the sauna\", huh?"
                "......"
                "..."
                mc "Have fun."

                if date == "june09day":
                    jump w2HanaNight1
                else:
                    jump w2HanaNight2

    scene w2_2969 with dissolve
    ver "Ha. Just shut up."
    scene w2_2970 with dissolve
    "........."
    scene w2_2971 with dissolve
    "......"
    scene w2_2972 with dissolve
    "..."
    scene w2_2973 with dissolve
    mc "Uh, how should we do this?"
    scene w2_2974 with dissolve
    ver "Last Saturday..."
    ver "Is {i}ninty-nine percent{/i} the reason I even considered this."
    scene verog_tt_a with dissolve
    show verog_tt
    mc "Hmmm, I don't know..."
    mc "I think I have other things I'd rather do with my mouth."
    ver "Then wha--"
    mc "Two things actually. One right now and the other for when you're satisfied.."
    ver "Confi--"
    scene w2_2975 with vpunch
    ver "Ah...!"
    mc "Egotistical."
    "Her nipples were still sensitive from earlier. I would use that."
    scene w2_2976 with dissolve
    "I got down on my knees in front of her on the cold, hard floor."
    scene w2_2977 with dissolve
    hide screen textbox2 with dissolve
    "The position immediately gave me an appreciation for what I just put Veronica through."
    mc "You mind if I begin?"
    "Like this, Veronica towered over me. Even more than usual."
    ver "..."
    "It added an exciting edge to the situation."
    scene w2_2978 with dissolve
    ver "Hurry up."
    scene verog_tt2_a with dissolve
    show verog_tt2
    "My plan was to use my fingers, but first I wanted to take a taste for myself."
    ver "~!"
    "I latched onto to the tip of her breast, savoring the feeling of having the whole of her pebble-like areola between my lips."
    "Lightly I held her nipple in place with my teeth, while I used the tip of my tongue to tease the engorged nub and coat it with saliva."
    ver "Damn it, even this feels good..."
    scene verog_tt3_a with dissolve
    show verog_tt3
    "Making it feel even better was my goal, so I brought my hand up to her lower entrance and started to lightly rub the outer folds of her labia."
    ver "Ha... ~ah..."
    "No penetration. Not yet."
    ver "That..."
    "I wanted to tease the overwrought woman a little."
    "The tip of my finger found its way to her clit, still peeking out from its hood thanks to Veronica's earlier masturbation."
    ver "Mma...!"
    "The way this small little nub gave me control over Veronica's body felt like magic."
    ver "Ah, fhu..."
    "Simply rubbing it wrenched all sorts of funny sounds from the Amazon's vocal cords."
    "Next was..."
    stop music
    scene w2_2979 with vpunch
    ver "Mhuhm..!"
    play music "music/guiton-sketch.ogg"
    scene verog_tt4_a with dissolve
    show verog_tt4
    "I sunk two fingers knuckle deep inside the Amazon and got to work."
    "Her cunt greedily accepted them."
    "*Schlick... schlick...*"
    "My digits steadily worked their way in and out with absolutely no effort, her insides already well-lubricated and primed to go."
    ver "Mmmh...!"
    "Likewise, I worked her teat with a similar low, but unremitting intensity, wanting to take my time in escalating things."
    ver "Mmmh...! {b}Mmmh...!{/b}"
    "The proof that the joint attack was effective lay in the sweet moans it wrested out of Veronica, growing in volume and frequency that matched my own rising roughness."
    "Try as she might to keep a lid on it and keep me from that satisfaction."
    scene verog_tt5_a with dissolve
    show verog_tt5
    ver "Is this how you got this job? Working that old bitch like this?"
    "I ignored the question, not wanting to stop my attack on her breast, but Veronica carried on."
    ver "Come on, tell me."
    scene w2_2980 with dissolve
    mc "Does the thought of that turn you on?"
    scene w2_2981 with dissolve
    ver "Of course not."
    scene w2_2980 with dissolve
    mc "Liar."

    if w2VeronicaSquirm == True:
        "I knew that to be the case, she had admitted to masturbating to what she did to Mrs. Pulman after all."

    scene w2_2982 with dissolve
    ver "I was just curious how a dweeb like you got a job like this."
    mct "(You want to play it like that, huh?)"
    scene w2_2980 with dissolve

    if toughness >=21:
        mc "Just go back to moaning, you bitch."
    else:
        mc "Okay then..."

    $ renpy.music.set_volume(.5, 1, channel = "ambient")
    play ambient "sound effects/boobjob.wav"
    scene verog_mt1_a with dissolve
    show verog_mt1
    ver "O-oh!"
    "With added vigor, I was finished talking and set to task with the goal of turning Veronica into an insensate, quivering puddle of sex."
    ver "Ghh-, oh-, fhu~"
    "Long and deep strokes, hammering away consistently at her cunt."
    ver "Ah... ah... why am I letting you..."
    scene w2_2983 with dissolve
    ver "Why am I letting you..."
    mc "You know why."
    scene w2_2984 with dissolve
    ver "Mmmh...!"
    mc "It feels good."
    scene verog_mt2_a with dissolve
    show verog_mt2
    ver "Fwhu, you-"
    "Whether through instinct or need, Veronica pulled me closer and slammed my face square into her bosom."
    mc "Just drop the pretense and enjoy yourself."
    "*Schlick..! *Fwhip..!* *Sckhlick..!*"
    ver "Mmmh, ha...!"
    "*Schlick! *Schlick...!*"
    "Honestly, this was more her than me. She was so pent up that any warm touch would probably set her off."
    "Her cunt was doing its best to receive me, offering no resistance and clinging to my fingers like they were a cock about to deposit a fat load of jizz."
    "The way she firmly cradled my head, holding it to her chest like a lover added to my excitement."
    "I was going to push this fiery and crass woman to the edge and physically feel, skin-to-skin, the effects cumming her brains out had on her body."
    scene verog_mt1_a with dissolve
    show verog_mt1
    "*Schlick..! *Fwhip..!* *Sckhlick..!*"
    mc "Down here is very agreeable... it's a pretty big contrast to your normal attitude."
    mc "Are you normally this horny?"
    ver "Ah... I got a big sex drive, okay? This past month though..."
    scene verog_mt3_a with dissolve
    show verog_mt3
    ver "Fuck! It's like it's been kicked into overdrive~"
    ver "Mmha...!"
    mc "Really...?"
    mc "You're a perverted woman deep down, aren't you?"
    ver "Fuck you, it sure as shit has nothing to do with the club! It's just..."
    ver "Ah, s-shut up and let me cum in peace, you dumbass."
    scene verog_mt2_a with dissolve
    show verog_mt2
    if w2VeronicaMean == True or w2VeronicaDog == True:
        mc "Don't let me stop you, bitch. Go ahead!"
    else:
        mc "Don't let me stop you!"

    "*Schlick..! *Fwhip..!* *Sckhlick..!*"
    ver "Oooh... ah... ah... ah..."
    "*Schlick! *Schlick...!*"
    "Her grip on my shoulder tightened, achingly as she hugged me even closer."
    ver "Ah... ah... ah...!"
    "Erratic bursts of hot air pelted my forehead and her moans were delivered straight into my ear at an expeditious rate."
    "*Schlick..! *Fwhip..!* *Sckhlick..!*"
    "My right hand was absolutely splattered and coated in her juices, the reward of a vigorous and unrelenting finger fucking."
    "*Schlick! *Schlick...!*"
    "The ball of my wrist positively ached..."
    "The tips of her fingers dug painfully deep into the flesh of my back..."
    ver "Mmh, ssh-shi...!"
    scene w2_2985 with hpunch
    mc "Ugh!"
    "With a great surge of violence and shocking strength, Veronica squeezed the ever-loving shit out of me."
    scene w2_2986 with flash
    $ renpy.music.set_volume(.1, 1, channel = "ambient")
    "So did her lower half, clenching hard around my finger like a vice as a copious amount of femcum spurted from the plugged hole."
    ver "Ghe...!"
    $ renpy.music.set_volume(.5, 1, channel = "ambient")
    scene verog_mt4_a with dissolve
    show verog_mt4
    "*Schlick..! *Fwhip..!* *Sckhlick..!*"
    ver "Ghehehyeee~"
    "*Schlick! *Schlick...!*"
    "Despite her death grip on me, rendering me almost unable to breathe, and despite her clear satisfaction, my right hand didn't cease."
    ver "Ohssshit.. ghh..."
    "*Schlick..! *Fwhip..!* *Sckhlick..!*"
    "*Schlick..! *Fwhip..!* *Sckhlick..!* *Schlick! *Schlick...!*"
    scene w2_2987 with flash
    $ renpy.music.set_volume(.1, 1, channel = "ambient")
    "More."
    scene w2_2986 with flash
    "More and more..."
    scene w2_2987 with dissolve
    mc "Fuck, that's a lot!"
    scene verog_mt5_a with dissolve
    show verog_mt5
    "Her last orgasm freed me from her crushing hold, her arms falling limply to the side."
    ver "Ghe.. .heh... ahaeheh..."
    "*Schlick..! *Fwhip..!* *Sckhlick..!* *Schlick! *Schlick...!*"
    ver "Ah... ah..."
    "*Schlick..! *Fwhip..!* *Sckhlick..!*"
    ver "Ha..."
    "*Schlick...*"
    stop ambient
    stop music fadeout 3.0
    $ renpy.music.set_volume(1, 1, channel = "ambient")
    scene verog_mt5_a with dissolve
    ver "Fuck."
    scene w2_2988 with dissolve
    "As soon as the fervor died, so did the strength in her legs."
    ver "Ha... damn it, [mcf]. That was..."
    ver "Fuck."
    "Having her like this, so close and so helpless, reminded me of the {b}second{/b} thing I had wanted to do with my mouth..."
    play music "music/soft-feeling.ogg"
    scene w2_2989 with dissolve
    ver "Mmphf?!"
    "Before she could see it coming, I planted a surprise kiss on her lips. It felt like I was grabbing the tiger by its tail."
    "As much as she could physically muster in her state, her body physically tensed up in a flash of bewilderment."
    scene verog_kiss1_a with dissolve
    show verog_kiss1
    "Only a flash though, as she quickly receded back into her post-orgasm fog and accepted my haphazard advance."
    ver "Mmmh...."
    "My tongue found easy passage into her mouth and was soon mingling with her own."
    "Her lips are so soft..."
    ver "Mmmh... mhhh..."
    scene verog_kiss2_a with dissolve
    show verog_kiss2
    "To my utter disbelief, cooing softly, she absentmindedly returned the kiss. Not vigorously, or even tenderly... it was more like soft, instinctive acceptance."
    "*Chup~ fwhup~*"
    ver "Emmm~hum...."
    "......."
    "..."
    scene w2_2990 with dissolve
    ver "...eeuh?"
    stop music
    scene w2_2991 with hpunch
    "Unfortunately, it was all too brief. Mustering her strength, Veronica came to her sense and parted our kiss with a light shove."
    ver "Fucker."
    ver "I didn't say you could do that."
    scene w2_2992 with dissolve
    "Despite her words, she didn't seem too angry about it."
    scene w2_2993 with dissolve
    ver "So I guess it's yo--"
    scene w2_2994 with dissolve
    mc "It's my turn?"
    scene w2_2995 with dissolve
    ver "...eager, aren't you?"
    scene w2_2994 with dissolve
    mc "You have no idea how turned on I am right now."
    scene w2_2995 with dissolve
    ver "Actually, I do."
    ver "Now..."

    $ renpy.end_replay()
    if not persistent.veroW2ScratchGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.veroW2ScratchGallery = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)


label w2VeronicaEdwinScratch:

    if _in_replay:
        show transitionveronica04 with cmet
        show screen textbox2 with dissolve
        "Please set [mcf]'s personality (toughness score) for this replay."
        hide screen textbox2 with dissolve
        menu:
            "Nice guy (Toughness: 0)":
                $ toughness = 0
            "Mischevious (Toughness: 18)":
                $ toughness = 18
            "Asshole (Toughness: 30)":
                $ toughness = 30

        show screen textbox2 with dissolve
        "Did you urinate on Veronica during the Week 1 exhibition?"
        hide screen textbox2 with dissolve

        menu:
            "Yes, I peed on her.":
                $ w1ExVeroPissedOn = True
            "No, that's disgusting!.":
                pass

        show screen textbox2 with dissolve
        "Did you talk to Veronica harshly during the photo shoot?"
        hide screen textbox2 with dissolve

        menu:
            "Yes. Who's a good doggy?":
                $ w2VeronicaMean = True
                $ w2VeronicaDog = True
            "No.":
                pass

        show screen textbox2 with dissolve

    scene black with fade
    ver "A deal is a deal."
    scene w2_2996 with dissolve
    play music "music/sneaky-snitch.ogg"
    mc "Here?"
    ver "You're going to make a mess."
    scene w2_2997 with dissolve
    ver "I just mopped."
    scene w2_2998 with dissolve
    "With an almost alarmingly firm grip, the red-headed woman wrapped her hand tightly around my stiffened cock."
    scene w2_2997 with dissolve
    ver "Shit, what should I do with this?"
    scene w2_2999 with dissolve
    "Slowly she worked her palm down the length of my shaft to the base."
    mc "You play both sides, right? You should have a pretty good idea. "
    scene w2_3000 with dissolve
    "The term \"withering glare\" took on a colorful new meaning."
    scene w2_3001 with dissolve
    ver "I'm usually not staring down the business end."
    scene verog_lick_a with dissolve
    show verog_lick
    "*Chwulp*"
    "With that as a lead in, Veronica tested the waters, giving the head of my cock a series of exploratory licks."
    "*Fwulp*"
    "Her tongue, as warm and soft as it was, ineptly prodded the underside of my glans."
    "It was..."
    mct "(Not very stimulating.)"
    "Patiently, I waited, hoping this was a prelude to something more satisfying, but..."
    "*Chwulp*"
    "*Fwulp*"
    "It was more of the same woeful teasing."
    mc "Veronica, this is nice and all, but..."

    if w2VeronicaMean == True or w2VeronicaDog == True:
        mc "You shouldn't play with your food. I'm dying here."
    else:
        mc "I'm dying here. How about something else?"

    scene w2_3003 with dissolve
    ver "Hmmm, yeah..."
    scene w2_3002 with dissolve
    "Veronica looked at a bona fide loss."
    scene w2_3003 with dissolve
    ver "Well, you want to be the one to do it?"
    scene w2_3002 with dissolve
    mc "You want me to lead?"
    scene w2_3003 with dissolve
    ver "I don't care. Whatever is quickest."
    scene w2_3002 with dissolve
    "Her business-like demeanor was patently unsexy and wasn't helping things."
    scene w2_3004 with dissolve
    "Part of me wanted to insist she put forth at least a modicum of effort."
    "Then again, having control over the imposing woman would be thrilling in its own right."
    stop music fadeout 3.0
    hide screen textbox2 with dissolve

    menu:
        "Insist that she does the work.":

            $ w2VeronicaTop = True
            mc "C'mon, it's not brain surgery. It's not like I half-assed it."
            scene w2_3002 with dissolve
            mc "Fulfill your side of the bargain. Treat me however you want. Just make it fun."
            scene w2_3003 with dissolve
            ver "Really?"
            scene w2_3002 with dissolve
            mc "Really."
            scene w2_3005 with dissolve
            ver "I can do whatever I want?"
            scene w2_3004 with dissolve
            mc "I'm just asking you to put your back into it."
            scene w2_3005 with dissolve

            if Veronica_Affection >= 13:
                ver "Careful with your phrasing, [mcf]!"
            else:
                ver "Careful with your phrasing, errand boy!"

            scene black with fade
            mc "H-huh?"
            scene w2_3006 with cmet
            play music "music/ninja-tortoise.ogg"
            "Next thing I knew, I was hoisted off the ground and in the Amazon's arms."
            mc "What are you--"
            play sound "sound effects/thud-floor.mp3"
            scene w2_3007 with vpunch
            "The next {b}next{/b} thing, I was flat on my back with Veronica looming over me like a giant."
            scene w2_3008 with dissolve
            mct "(Did she just... lick her chops?)"
            scene w2_3009 with dissolve
            ver "What am I doing? It sounded like a challenge. If you want me to put my back into it, I will."
            ver "Just know, you've revoked your right to complain."
            scene w2_3008 with dissolve
            mc "Complain?"
            "If anything, her change in demeanor was refreshing."
            mc "I like the view so far."
            scene w2_3009 with dissolve
            ver "Give me your legs."
            scene black with fade
            "I had every intention of complying, but she beat me to the punch, roughly grabbing my legs and lifting my hips up in the air."
            scene w2_3011 with dissolve
            mc "...this is new, it's like I'm the woman."
            scene w2_3010 with dissolve
            "Veronica had full leverage over me. I was at her mercy."
            scene w2_3012 with dissolve
            ver "You look good on your back, slut."
            scene w2_3011 with dissolve
            mc "This is cool and all, but what can you do in a position like this?"
            scene w2_3010 with dissolve
            "Like this, my dick was pointed toward me, dangling preciously under the weight of gravity and the small shifts in Veronica's body weight."
            scene w2_3012 with dissolve
            ver "For a pervert, you lack imagination."
            scene w2_3010 with dissolve
            "On the plus side, the feeling of the Amazon's right breast resting heavily on my balls was nice."
            "It felt warm and the way her pointed nipple tickled the underside of my scrotum was pleasant in its own small way."
            scene w2_3013 with dissolve
            ver "Like this, I can watch all the little twisted expressions your face is about to make."
            scene w2_3014 with dissolve
            "With the added provocation, Veronica grabbed a hold of my cock, firmly holding it in place."
            mc "A handjob?"
            scene w2_3013 with dissolve
            ver "Don't sound so disappointed. You used your hand, didn't you? A deal is a deal and fair is fair."
            scene w2_3015 with dissolve
            ver "Besides..."
            scene w2_3016 with dissolve
            "Veronica smirked, looking down on me directly into my eyes. She had complete control of the situation."
            scene w2_3015 with dissolve
            ver "I promise, you've never experienced a hand job like this."
            scene verog_fd1_a with dissolve
            show verog_fd1
            "She paused for a moment to let that vow hang fat in my mind, before smoothly working my dick with the rough surface of her overworked hands."
            "That in itself was new. She had the hands of a woman who used hers for a living and the grip to match."
            "The hands of an Olympian shot putter was jerking my dirty, sweaty cock."
            scene verog_fd2_a with dissolve
            show verog_fd2
            ver "What's with that dumb look on your face? You're not already about to blow, are you?"
            mc "No. I'm just enjoying this scenario."
            "She was working my cock at an unyielding, slowly building pace."
            ver "That much is obvious. You've got your legs wrapped around me like a greedy whore."
            ver "Tell me, [mcf], do you like being on your back?"
            mc "I like seeing you on top."
            scene w2_3017 with dissolve

            if w2VeronicaDog == True or w2VeronicaMean == True:
                ver "Ha! Could've fooled me with the way you acted earlier, but a good answer nonetheless."
            else:
                ver "Ha! That's a good answer, pervert."

            ver "You know, for a piece of trash, you're not so bad like this. You make all sorts of cute faces."
            scene w2_3018 with dissolve
            mc "Mm-ah, y-you're the one who voluntarily stepped into the garbage bin."
            scene verog_fd3_a with dissolve
            show verog_fd3
            ver "Don't. I. Know it."
            "Her pace turned more aggressive and she jerked my cock even faster, sending a stronger message to my brain and spinal cord that it was time to reproduce."
            mc "Ah, that- mmh...!"
            ver "Don't hold it. Let me hear you whimper like an animal."
            "I could tell by the look in her eyes that she was enjoying this. The change in attitude made me happy."
            "It made me want to indulge her, but..."
            scene verog_fd4_a with dissolve
            show verog_fd4

            menu:
                "Shamelessly moan for the woman."(chg=["veronica_passion_up","veronica_up"]):
                    $ w2VeronicaShameless = True
                    $ Veronica_Horniness += 1
                    $ Veronica_Affection += 1
                    mc "Mmha, ah... that's a little...."
                    "It made me want to indulge her, but it was still embarrassing."
                    ver "Don't think. Just do it."
                    ver "{b}Moan, you bastard.{/b}"
                    mc "Ah, f-fuck..."
                    mc "O-oh...!"
                    "She was going to drag those sounds out of me whether I liked it or not, so I might as well let loose a little."
                    ver "That's it. Louder, you fucking slut."
                    mc "Mmh--oh-oh?"
                    "Self-consciously, I found myself gauging the Amazon's reaction, looking for her approval in a bid to make me not feel like a weirdo."
                    "The smile on her face told me to continue."
                    mc "D-don't stop..."
                    ver "Does it feel good?"
                    mc "Yes!"
                    ver "I bet it does, me milking you like a bull."
                    mc "Mmh, oh!"
                    ver "That's what I love to hear. What's with men and trying to hold it in during sex?"
                    mc "Oh, ah~ I don't--"
                    ver "A guy moaning is so fucking hot."
                    ver "Afraid of sounding like a woman? Afraid of sounding stupid? Dumb bravado is what it is."
                    mc "Ng, y-yeah, I guess."
                    ver "You don't really give a shit, do you? You're just putty in my fucking hands. All you care about is cumming~"
                "Turn the attention to her own arousal.":


                    show screen textbox2 with dissolve
                    mc "Y-yeah it feels good, but..."
                    "It made me want to indulge her, but that didn't mean I was going to give her what she wanted. Even flat on my back with Veronica mounting me like a woman, I had my pride as a man."
                    mc "I'm not the only one who's enjoying myself."
                    mc "Poor Veronica. Getting turned on again so soon. It must be tough being such a horny bitch."
                    ver "Yeah, I'm getting turned on again. So what? Despite your looks, you've got a big cock and you're singing just like a songbird."
                    ver "Just the way I like my horny mutts."
                    mc "You like big cocks?"
                    ver "Surprised?"
                    mc "Ah-ah, a little!"
                    ver "That! More of that! Sing for me, dog."
                    mc "Ngh-! I don't think...!"
                    ver "You're already moaning. Stop thinking and just give in. I didn't fucking shy away from it when you were finger-deep in my cunt, did I?"
                    mc "N-no...!"
                    ver "What's with men and trying to hold it in during sex?"
                    ver "Afraid of sounding like a woman? Afraid of sounding stupid?"
                    mc "No, I just like seeing you work for it. Builds character~"
                    ver "Oh, you want me to work for it?"

            scene verog_fd5_a with dissolve
            show verog_fd5
            hide screen textbox2 with dissolve
            mc "Oh, oh--!"
            "Veronica launched into a blistering pace, faster than my dick had ever been jerked."

            if w2VeronicaShameless == True:
                mc "Fuck, that's i-intense!"
            else:
                ver "How's this for working for it? Let it out. Let all your pathetic mewling out!"


            "To my surprise, the increased friction wasn't painful. It was mind-melting."
            "Veronica was well aware of the generous amount of pre-cum that had dribbled down my shaft and coated it in a nice sheen."
            ver "Ha! You trying to crush me?"
            ver "You just clamped down tight!"

            if w2VeronicaShameless == True:
                mc "Oh! Nguah!"
                ver "Good, good..."
            else:
                ver "At least your body is honest!"

            "Despite how new and weird this was... this was honestly pretty fun."
            "The club had given me an opportunity to indulge my sadistic side, but being on the other side wasn't without its thrill."
            scene verog_fd3_a with dissolve
            show verog_fd3
            ver "Huh? You're smiling?"
            mc "Ah... fuck, I was..."
            mc "I was just thinking..."
            ver "Spit it out."
            mc "I was just thinking... you're pretty fun in the sack."
            ver "Ha! You haven't seen me in the sack."
            ver "Now..."
            scene verog_fd4_a with dissolve
            show verog_fd4
            ver "Stop thinking about stupid things and cum for me."
            "*Fwhick...! Fwap...! ...Fwahp!*"
            ver "I know you're close!"
            "Veronica went in for the coup de grâce, hand rigidly bolted to my cock and speeding even further beyond."
            "*Fap* *Fwhap!* *Fhap..!*"
            "The view in front of me steadily lost focus, the edges of Veronica's muscular form bleeding into the vast whiteness of the ceiling."
            mc "Ghoo-"
            "*Fwhick...! Fwap...! ...Fwahp!*"
            ver "You close?"
            mc "Yeah, I'm about to--"
            mct "(Ah, wait a minute...)"
            "As I neared peak excitement, a thought crossed my mind..."
            "I was directly looking down the business end of my dick."
            scene white with fade
            "I felt good."
            "I felt my balls contract, as they pushed out sperm to my prostate."
            "My body went rigidly tense..."
            "Everything felt so, so good..."
            scene w2_3019 with dissolve
            play sound "sound effects/spurt.wav"


            menu:
                "Fuck yeah!"(chg=["veronica_passion_up2"]):
                    $ Veronica_Horniness += 2
                    $ w2EdwinFacial = True
                    scene w2_3020 with dissolve
                    mc "F-fhuck!"
                    scene w2_3021 with dissolve
                    "My brain was filled with absolutely nothing as I ejaculated {b}hard{/b}. I was so pent up and Veronica had milked me for all I'm worth..."
                    scene w2_3022 with dissolve
                    play sound "sound effects/spurt.wav"
                    mc "Ah!"
                    play sound "sound effects/spurt.wav"
                    "I didn't care as rope after rope of my own cum showered down on me."
                    "......"
                    "..."
                    scene w2_3023 with dissolve
                    mc "Ha... I... ah..."
                    scene w2_3025 with dissolve
                    "As I came back to my senses, I noticed Veronica had a peculiar look in her eye."
                    scene w2_3024 with dissolve
                    ver "Fuck, that's so..."
                    scene w2_3025 with dissolve
                    "The hungry, unmistakable look of arousal."
                    scene w2_3024 with dissolve
                    ver "Hot."
                    scene w2_3026 with dissolve
                    "In an instant, Veronica was on me like a lion. Breasts pleasantly pressed into my own chest."
                    scene w2_3027 with dissolve
                    mc "Ah.."
                    scene w2_3028 with dissolve
                    mc "What are you doing?"
                    scene w2_3029 with dissolve
                    ver "This is a first..."
                    scene w2_3030 with dissolve
                    mc "Oh!"
                    "My body was still on edge from my orgasm, the simple act of Veronica licking my nipple felt good."
                    scene w2_3031 with dissolve
                    ver "I've never seen a man covered in his own cum before..."
                    ver "Fuck."
                    ver "That's hot..."
                    stop music fadeout 3.0
                    scene w2_3032 with dissolve
                    mc "Ah...?"
                    stop music fadeout 3.0
                    scene w2_3033 with dissolve
                    mc "Haha...! Ah...!"
                    mc "Jeez... aha...!"
                    mc "You're weird!"
                    scene w2_3034 with dissolve
                    "As I laughed, Veronica's smile was surprisingly soft."

                    if prVero_Facial == True:
                        scene w2_3035 with dissolve
                        ver "I guess I'll consider us even for what you did to me the first time we met."
                        scene w2_3034 with dissolve

                    $ renpy.end_replay()
                    if not persistent.veroW2MCScratchGallery:
                        play sound "sound effects/notification.wav"
                        show memoryunlock with dissolve
                        $ renpy.pause(3, hard=True)
                        $ persistent.veroW2MCScratchGallery = True
                        hide memoryunlock with dissolve
                        $ renpy.pause(0.5, hard=True)

                    "......"
                    scene black with fade
                    "..."
                    if VeroFlag == True:
                        jump w2VeronicaFlag
                    else:
                        "That was how the evening ended. After cleaning up, we went our separate ways."

                        if date == "june09day":
                            jump w2HanaNight1
                        else:
                            jump w2HanaNight2
                "Crap!"(chg=[("veronica_passion_up", prVero_Facial == True), ("veronica_passion_down", prVero_Facial == False)]):


                    scene w2_3020 with dissolve
                    mct "(Dodge)!"
                    play sound "sound effects/spurt.wav"
                    scene w2_3036 with dissolve
                    "The first rope of jizz spiraled past my head with minimal splash damage."

                    if prVero_Facial == True:
                        $ w2EdwinFacial = True
                        $ Veronica_Horniness += 1
                        "But..."
                        play sound "sound effects/spurt.wav"
                        scene w2_3037 with dissolve
                        "The second..."
                        ver "No dodging, slut!"
                        play sound "sound effects/spurt.wav"
                        scene w2_3038 with dissolve
                        "With a twisted smile, Veronica re-angled my cock back in the direction of my face."
                        scene w2_3039 with dissolve
                        mc "Ng-oh!"
                        "Direct hit."
                        scene w2_3040 with dissolve
                        play sound "sound effects/spurt.wav"
                        mc "Ah..."
                        "......"
                        "..."
                        scene w2_3041 with dissolve
                        "When everything was said and done, I found myself covered in my own spunk."
                        "That was... new."
                        scene w2_3017 with dissolve
                        ver "Ha...! Looks good on you!"
                        scene w2_3018 with dissolve
                        mc "You did that on purpose."
                        ver "Maybe. Let's call us almost even for when you hosed me down the first time we met."
                        scene w2_3018 with dissolve
                        mc "Ha...!"
                        mct "(With all the perverted shit that's been going on, I'd forgotten about that...)"
                        mc "Just almost?"
                    else:

                        $ Veronica_Horniness -= 1
                        play sound "sound effects/spurt.wav"
                        scene w2_3042 with dissolve
                        "So did the second."
                        play sound "sound effects/spurt.wav"
                        scene w2_3043 with dissolve
                        "And the third."
                        play sound "sound effects/spurt.wav"
                        scene w2_3045 with dissolve
                        "By the end of it, there was a smattering of spunk reeking next to my head."
                        "The stench was unpleasant, but at least I wasn't covered in it."
                        scene w2_3044 with dissolve
                        mct "(Quick thinking)"
                        scene w2_3046 with dissolve
                        "When my attention was refocused on Veronica, she had a sour look on her face."
                        mc "What's with that look?"
                        scene w2_3047 with dissolve
                        ver "I just wanted to see... ah, forget it."

                    scene black with fade
                    stop music fadeout 3.0
                    $ renpy.end_replay()
                    if not persistent.veroW2MCScratchGallery:
                        play sound "sound effects/notification.wav"
                        show memoryunlock with dissolve
                        $ renpy.pause(3, hard=True)
                        $ persistent.veroW2MCScratchGallery = True
                        hide memoryunlock with dissolve
                        $ renpy.pause(0.5, hard=True)
                    "......"
                    "...."


                    if VeroFlag == True:
                        jump w2VeronicaFlag
                    else:
                        "That was how the evening ended. After cleaning up, we went our separate ways."

                        if date == "june09day":
                            jump w2HanaNight1
                        else:
                            jump w2HanaNight2
        "Take charge.":



            "Staring down at Veronica made the decision for me."
            "Those big green eyes, that cute button nose, and that profanity-spewing cock holster she called a mouth..."
            "I wanted to mess them up."
            mc "Whatever is quickest?"
            scene w2_3005 with dissolve
            ver "Y--"
            play music "music/hypnosis.ogg"
            play sound "sound effects/slap1.wav"
            scene w2_3048 with vpunch
            "*Slap*"
            mc "Sure. You suck at giving blowjobs, but I'll show you how it's done."
            scene w2_3049 with dissolve

            if Veronica_Affection >= 13:
                ver "You an expert at sucking cock, [mcf]?"
            else:
                ver "You an expert at sucking cock, errand boy?"

            scene w2_3050 with dissolve
            mc "Ha!"
            scene verog_prebj_a with dissolve
            show verog_prebj
            mc "I walked right into that one, I guess."
            ver "What are you doing?"
            mc "What does it look like?"
            ver "You're jerking your disgusting cock inches from my nose."
            ver "Slowly."
            ver "Like a weirdo."
            mc "I'm just making sure I'm at 100 percent."
            "Actually, I was taking my time and enjoying the sight of Veronica beneath my cock."
            "I was so turned on that I knew I wouldn't last very long if I just crammed my cock down the Amazon's throat and I wanted to enjoy myself."

            if toughness >= 17:
                mc "Open your mouth and stick out your tongue."
            else:
                mc "Open your mouth and stick out your tongue, please."

            scene w2_3051 with dissolve
            ver "Ahh~"
            mc "Stick it out more."
            scene w2_3052 with dissolve
            ver "Ahhhhh--"
            scene verog_prebj2_a with dissolve
            show verog_prebj2
            mc "--hhho!"
            "I found her parted lips made a soft, mighty fine bed for my cock."
            "Her warm, moist tongue felt pleasant to the underside of my shaft and the way her hot breath hit the opening of my urethra made me shudder."
            mc "Mmmh...!"
            "Somehow, this was more thrilling than Veronica's earlier attempt at a blowjob."
            scene w2_3053 with dissolve
            mc "I'm putting it in now."
            scene w2_3054 with dissolve
            "With that little heads up, I began to inch my dick inside of Veronica's waiting mouth."
            "Past the tip of her tongue."
            scene w2_3055 with dissolve
            "The arch of her tongue..."
            scene w2_3056 with dissolve
            "...just stopping short of knocking on her tonsils."
            "Meanwhile, she kept her eyes open, practically growing cross-eyed as she kept them firmly locked on the thing threatening to invade her throat."
            mct "(Fuck...)"
            "I wanted to cum just from that look alone."
            mc "You doing alright?"
            scene w2_3057 with dissolve
            "......"
            "..."
            "I took the growing silence as a yes and continued."
            mc "Put your hands on your knees and brace yourself. You'll be more comfortable that way."
            scene w2_3058 with dissolve
            "The action had the agreeable upside of pushing my cock even deeper into the Amazon's mouth."
            scene w2_3059 with dissolve
            mc "Let me know if it's too much."
            ver "..."
            scene verog_bj1_a with dissolve
            show verog_bj1
            "Taking it gently, I used my hands and hips in tandem, guiding Veronica's head down the length of my shaft."
            "I didn't dare take it further than half way - at least, not yet. I felt like this was already pushing it for what Veronica would allow me to do for our arrangement."
            "*Chup...*"
            "Just looking down at the muscular woman and seeing her lips sheathed around my cock made up for the lack of intensity."
            "*Chup, chwup...*"
            mc "That's right, nice and steady..."

            if w2VeronicaMean == True:
                mc "Suck my cock, bitch."
            else:
                mc "Suck my cock."

            mc "Just like that."
            "I didn't dream she was getting anything out of my verbal \"encouragement.\" I was speaking purely for my benefit."
            mc "Ah..."
            "*Chup, chwup, fhwup...*"
            scene verog_bj2_a with dissolve
            show verog_bj2
            "Veronica was handling things easily. Serenely."
            "She was even putting in effort on her end, in a far more supplicant display than I would expect."

            if w1GonzoReward == True:
                "It was amateurish, at least in comparison to my education with Harper and Dalia, but there was something more satisfying about this."

            "She pursed her lips to form a better seal around my cock and used her tongue to catch and hook underneath my frenulum on my back strokes."

            if w1GonzoReward == False:
                "There was something satisfying about knowing she was at least putting forth a humble effort."

            mc "Ah..."
            "*Chup, fhqup... chwup...*"
            scene verog_bj1_a with dissolve
            show verog_bj1
            mc "Mgh, ah...!"

            menu:
                "Tell her she is doing great.":
                    mc "Even in a position like this... you look..."
                    "*Chup...*"
                    mc "You're doing a damn good job."
                    "*Chup, chwup...*"
                    mc "You look so hot right now."
                    "*Chup, chwup, fhwup...*"
                    mc "F-fuck..."
                    mc "I'm... I'm going to speed up now, okay?"
                "Throw in some taunting.":

                    mc "How's my sweaty dick taste?"
                    "*Chup...*"
                    mc "This is a pretty good look for you, you know that?"
                    "*Chup, chwup...*"
                    mc "On your fucking knees, sucking a fat cock."
                    "*Chup, chwup, fhwup...*"
                    mc "Ha! I bet you're regretting the workout I did."
                    ver "Ghuh...!"
                    "*Chup, chwup, fhwup... fwip!*"
                    mc "A-ah! J-just a heads up... I'm going to go faster now."

            play ambient "sound effects/fel2.wav"
            scene verog_bj3_a with dissolve
            show verog_bj3
            "*CHUP, CHWUP, FWHUP, THURP...!*"
            "Deeper and with a more satisfying speed..."
            "*CHUP, CHWUP, FWHUP!*"
            "I knew Veronica could take it and the expression on her cock-stuffed face didn't contradict otherwise."
            mc "Ah... this is..."
            "I was starting to think my goal of turning her face into a sexy mess was untenable."
            mct "(...I guess we'll have to see about that.)"
            mc "Hey, stop me if I'm too..."
            scene verog_bj4_a with dissolve
            show verog_bj4
            ver "G-guh!"
            mc "...rough!"
            ver "*GLUG... GLUG... GLUG... GLUG... GLUG...!"
            "With a rough grip on her hair, I guided her head frantically up and down my cock, using her face like a sex toy."
            ver "*GLUG... GLUG... GLUG... GLUG... GLUG...!"
            "Easing into things was the play. Her face looked more uncomfortable, but she accepted the new pace as readily as last time."
            mct "(F-fuck...!)"
            "That's the look!"
            ver "*GLUG... GLUG... GLUG... GLUG... GLUG...!"
            "That's the fucking look!"
            mct "(I've got a silver medalist bombshell inhaling my cock.)"
            "A fucked-up thought crossed my mind..."
            ver "*GLUG... GLUG... GLUG... GLUG... GLUG...!"
            "I had Samson to thank for this."
            if VeroFlag == True:
                "The thought didn't sit right with me. In fact, it disgusted me."
                "But still..."

            if toughness >=21:
                mc "Ah, you bitch!"

            mc "Here it comes!"

            menu:
                "Ride her face and cum down her throat.":

                    scene w2_3060 with vpunch
                    mc "--!"
                    ver "Cghuhh...!"
                    "With as much strength as a man could muster in the throes of an orgasm, I crammed my dick as far back as I could."
                    stop ambient
                    play sound "sound effects/spurt.wav"
                    with flash
                    scene w2_3061 with dissolve
                    mc "O-oh!"
                    "That burst of energy evaporated as quickly as it took me, my legs giving out and sending the two of us to the floor."
                    play sound "sound effects/thud-floor.mp3"
                    scene w2_3062 with fade
                    "Amazingly, I was still lodged in her throat."
                    mc "Eugh!"
                    play sound "sound effects/spurt.wav"
                    with flash
                    play ambient "sound effects/fel2.wav"
                    scene verog_bj5_a with dissolve
                    show verog_bj5
                    "I wasn't finished cumming. This whole evening had me primed to pump an ungodly amount of semen down her gullet and that's what I was going to do."
                    "I held her head in this new position, rocking my hips like I was trying to breed her face."
                    play sound "sound effects/spurt.wav"
                    with flash
                    mc "Take it. T-take it all...!"
                    ver "Chuuu...!"
                    play sound "sound effects/spurt.wav"
                    ver "Gwwh...! *Glug... Glug... glug...*"
                    mc "Uh..."
                    stop ambient
                    stop music
                    play sound "sound effects/thud-floor.mp3"
                    scene w2_3063 with vpunch
                    mc "F-fuck..."
                    mct "(Oh crap, I hope I didn't take it too far...)"
                    ver "Ewh...euch... ha..."
                    scene w2_3064 with fade
                    mc "Sorry, I may have overdone it..."
                    ver "N-no... ah..."
                    "She struggled to get the words out from her cock-induced dyspnea."
                    ver "We had... a deal... and I said..."
                    ver "Whatever's quickest... but..."
                    scene w2_3065 with dissolve
                    ver "Fuck, were you trying to kill me? Even with the warning..."
                    ver "That was too much you freak of nature!"
                "Look her in the eye and paint her white."(chg=["veronica_passion_up"]):


                    $ Veronica_Horniness += 1
                    stop ambient
                    scene w2_3066 with dissolve
                    "Fighting back my instinct to cum in a wet and warm hole, I retreated from Veronica's plush mouth and leveled my cock before her nose."
                    mc "L-look up at me!"
                    ver "H-huh...?"
                    "Still in a cock daze, she had yet to process the abrupt development."
                    scene w2_3067 with dissolve
                    mc "I said look me in the fucking eyes...!"
                    ver "Uh, okay..."
                    scene w2_3068 with dissolve
                    "Veronica complied, turning her clouded gaze up at me while I peered down into her bespeckled eyes."
                    ver "I'm going to shower after this, but don't get it in my fucking hair, okay?"
                    scene verog_eyes1_a with dissolve
                    show verog_eyes1
                    "*Fap, fwhap... fhwaap...!*"
                    "So wrapped up in the sight beneath me, my lone answer to her concern was the sodden-sounding staccato of me furiously beating my dick like it was a wet towel."
                    "Her deep green orbs were mystifying. I couldn't read what she was feeling in the least."
                    "All I knew was what I was feeling at the moment. The excitement of having a beautiful woman at my feet, the immoderate drive to hose her down with my jizz, and the impending sense of satisfaction of knowing that was indeed soon to come."
                    mc "Ah... fuck..."
                    mc "You're so..."
                    "The time we spent locking eyes was so very brief, but it felt immense."
                    "*Fap, fwhap... fhwaap...!*"
                    "They had stolen my focus. It was like the dynamic had suddenly switched. Like she was in control."
                    ver "You've got such a stupid look on your face right now. It's actually..."
                    ver "Kinda hot."
                    scene verog_eyes2_a with dissolve
                    show verog_eyes2
                    ver "Hey, [mcf]...."
                    "*Fap, fap, fap...!*"
                    ver "Cum on my chest."
                    ver "Look me in the eye, say my name, and {b}cum on my tits{/b}."
                    mc "Say your...?"
                    ver "Yeah. I want you to say my name while you're gasping like a dumb animal."
                    ver "You can do that right?"
                    mc "Ha!"
                    "Finally, I could pick up on what she was feeling. She was suddenly..."
                    mc "Veronica..."
                    "Feeling it."
                    mc "Veronica... I'm about to..."
                    ver "Do it!"
                    mc "--!"
                    play sound "sound effects/spurt.wav"
                    scene w2_3069 with flash
                    mc "Veronica....!"
                    "Fat ropes of spunk exploded from my urethra one after another."
                    "Layering on top of each other, coating her freckled breasts in white."
                    play sound "sound effects/spurt.wav"
                    scene w2_3070 with dissolve
                    "Some even managed to reach her face and drip down her chin."
                    "By the time my orgasm subsided..."
                    stop music fadeout 3.0
                    scene w2_3071 with dissolve
                    "I was weak in the legs."
                    mc "Ah, thanks..."
                    ver "Jeez, that good huh?"
                    ver "What the fuck is with this amount by the way? I mean, holy shit!"



            scene black with fade
            ver "Go get the camera! We can use this!"

            $ renpy.end_replay()
            if not persistent.veroW2MCScratchGallery:
                play sound "sound effects/notification.wav"
                show memoryunlock with dissolve
                $ renpy.pause(3, hard=True)
                $ persistent.veroW2MCScratchGallery = True
                hide memoryunlock with dissolve
                $ renpy.pause(0.5, hard=True)

            mc "Yeah, okay... just give me a second to catch my..."
            ver "Hurry, this shit is disgusting."
            "......"
            "..."
            mct "(Every part of the buffalo, I suppose.)"

            if VeroFlag == True:
                jump w2VeronicaFlag
            else:
                "That was how the evening ended. After cleaning up, we went our separate ways."

                if date == "june09day":
                    jump w2HanaNight1
                else:
                    jump w2HanaNight2


label w2VeronicaFlag:

    play music "music/jazz-piano-bar.ogg"
    scene w2_3072 with w12
    show screen textbox2 with dissolve
    mc "You sure this is okay?"
    mc "Keeping this place closed longer than you have to?"
    scene w2_3073 with dissolve
    mct "(Considering how in the red it is, I mean...)"
    scene w2_3074 with dissolve
    ver "An extra thirty minutes won't hurt."
    ver "At least, not in the long run. Not like people are clamoring to get in."
    scene w2_3072 with dissolve
    mc "The overhead on this place must be killer."
    scene w2_3081 with dissolve
    ver "Honestly, I've bitten off more than I can chew here. It would've been better to start from the ground up."
    scene w2_3076 with dissolve
    mc "What do you mean?"
    scene w2_3075 with dissolve
    ver "This gym... it originally belonged to my trainer and coach. He was a nice guy, but a miserable bastard."
    scene w2_3078 with dissolve
    ver "He didn't have much in the way of family and the little he did had nothing to do with him, so when he got sick, I took over his lease and he sold me this place on the cheap."
    scene w2_3077 with dissolve
    mc "How was the business back then?"
    scene w2_3079 with dissolve
    ver "Not very good... this place was NEVER busy, which was what I liked about working out here, but that stupidly didn't even cross my mind even when I took over his obligations."
    scene w2_3078 with dissolve
    ver "I was just happy my dream of starting a gym was getting off the ground."
    scene w2_3077 with dissolve
    mc "So this place doing crappy isn't your doing?"
    scene w2_3075 with dissolve
    ver "Oh, no. I've helped. Making it worse."
    ver "It was stupid of me to think I could run a gym just because I liked working out."
    scene w2_3076 with dissolve
    mc "Not stupid, but maybe naive."
    scene w2_3081 with dissolve
    ver "Same thing."
    scene w2_3080 with dissolve
    mc "What kind of problems does this place have? Specifically I mean."
    scene w2_3074 with dissolve
    ver "No point in going into detail. We don't have the time and I'm jabbering way too much about this place already."
    scene w2_3082 with dissolve
    mc "It's fine. What else would we talk about?"

    if w2VeronicaScratch == True and w2VeronicaTop == False:
        mc "The club? Me cramming my dick down your throat just now? Should we just sit in painful silence?"
    elif w2VeronicaScratch == True and w2VeronicaTop == True and w2EdwinFacial == True:
        mc "The Club? You hosing me down in my own jizz just now? Should we just sit in painful silence?"
    elif w2VeronicaScratch == True and w2VeronicaTop == True and w2EdwinFacial == False:
        mc "The Club? You almost hosing me down in my own jizz just now? Should we just sit in painful silence?"
    else:
        mc "The club? You parading around here like a dog? Should we just sit in painful silence?"


    scene w2_3083 with dissolve
    ver "Well, how about we talk about you?"
    scene w2_3084 with dissolve
    mc "You don't care about that."
    scene w2_3083 with dissolve
    ver "True. Very true, but it's something."
    scene w2_3088 with dissolve
    ver "I mean a kid your age working where you do is extremely fucked. What's the deal with that?"
    scene w2_3089 with dissolve
    mc "That's not interesting either. It's good money that'll pay for college."
    scene w2_3087 with dissolve
    mc "In a way, we aren't so different. Well, besides me not facing the impending threat of being dicked down..."
    scene w2_3085 with dissolve
    ver "Pft, ha!"
    ver "It comes down to money don't it? But it's not like you're not enjoying the {i}perks{/i}."
    ver "Don't deny it."
    scene w2_3086 with dissolve
    mc "Heh, well... what feels good and what's conscionable are sometimes an entirely separate matter."

    if w2VeronicaScratch == True:
        mc "Case in point, what you just did with me."
        scene w2_3085 with dissolve
        ver "Ah, fuck you. So that's it in a nutshell?"
    else:
        scene w2_3085 with dissolve
        ver "That's it in a nutshell?"

    scene w2_3087 with dissolve
    mc "Yeah, I told you it's not that interesting."
    scene w2_3090 with dissolve
    ver "Actually... more interesting than most, kid."
    scene w2_3082 with dissolve
    mc "So, what kind of problems does this place face?"
    scene w2_3083 with dissolve
    ver "Eh? You're back on that again?"
    scene w2_3084 with dissolve
    mc "I'm curious.."
    scene w2_3079 with dissolve
    ver "You want to be here all day?"
    scene w2_3077 with dissolve
    mc "C'mon, just tell me a {i}little{/i} about it."
    scene w2_3075 with dissolve
    ver "Where to start? The location ain't so great, not that many people come in and only a fraction become dues-paying members, and the customers I do have aren't renewing their memberships."
    ver "The overhead is high, I have ongoing obligations on some of the older equipment from the previous owner, and I have this leasing nightmare on some newer stuff..."
    scene w2_3077 with dissolve
    mc "Tell me about that?"
    scene w2_3078 with dissolve
    ver "There was something called an {i}evergreen{/i} clause in my contract with the leasing company."
    ver "Basically, failing to notify them within ninety days of the buyout of the lease allowed them to renew the contract for another year. It's basically a fucking scam."
    scene w2_3089 with dissolve
    mc "That's not illegal?"
    scene w2_3088 with dissolve
    ver "Nope."
    mct "(Hmm...)"
    scene w2_3087 with dissolve
    mc "Go on."
    scene w2_3091 with dissolve
    ver "Well, I had to replace the air conditioner last year, which was expensive as fuck."
    ver "I paid that geriatric asshole a tidy sum in promotional fees."
    ver "Utilities keep going up, I had to bring a couple of things up to code after an unexpected inspection, just... you know, a bunch of shit."
    scene w2_3092 with dissolve
    mct "(She has so many problems that even if Samson could take credit for a few of them and it could be fixed, magically somehow...)"
    "Which was a big if..."
    mct "(She'd still be fucked, right?)"
    scene w2_3091 with dissolve
    ver "I'm... going to stop there."
    scene w2_3093 with dissolve
    mc "Can the money you win for the club really fix all that?"
    scene w2_3091 with dissolve
    ver "No, it's just a stopgap."
    scene w2_3093 with dissolve
    mc "So patching up an already sinking ship...?"
    scene w2_3094 with dissolve
    ver "*Sigh* I'm..."
    ver "It sounds like I'm an idiot, but I've..."
    ver "I have learned a lot though. Through classes and just by doing... I like to think if I can get out from under this... I could..."
    scene w2_3095 with dissolve
    ver "Make a better go of it."
    scene w2_3096 with dissolve
    mc "..."
    "Veronica put on a big smile. I had no idea if it was merely masking her hopelessness or if her spirit was truly that indomitable, but..."
    "Either way, I felt for her."
    hide screen textbox2 with dissolve

    menu:
        "Encourage her."(chg=["veronica_up2"]):
            $ Veronica_Affection +=2
            scene w2_3097 with dissolve
            show screen textbox2 with dissolve
            mc "No matter what happens, I think you'll be okay."
            mc "A woman like you will find a way to land on her feet, even if it's on a new path."
            scene w2_3098 with dissolve
            ver "Get the fuck out of here. You don't know me."
            scene w2_3099 with dissolve
            mc "That's why you should put stock into what I just said. It's not just words said to comfort a friend."
            mc "It's a careful observation made about a stranger."
            scene w2_3100 with dissolve
            ver "..."
            "A smile, but this time different."
            scene w2_3098 with dissolve
            ver "I'm getting lightheaded. Let's get out of here."
        "Suggest we get out of here.":

            scene w2_3097 with dissolve
            show screen textbox2 with dissolve
            mc "I think we've been in here long enough."
            scene w2_3101 with dissolve
            ver "Ha, pussy! It hasn't been ten minutes!"

    scene w2_3102 with dissolve
    ver "Hey, [mcf]."
    scene w2_3103 with dissolve
    mc "Yeah?"
    scene w2_3104 with dissolve
    ver "Getting that shit off my chest was nice. I don't really have anyone to bitch to anymore since my divorce."
    scene w2_3103 with dissolve
    mc "It's part of my job."
    scene w2_3105 with dissolve
    ver "You say that, but I don't think you believe that."
    scene w2_3106 with dissolve
    ver "Hmpfh"
    stop music fadeout 3.0
    "......"
    scene black with fade
    $ history_veronica = "Chatting with Veronica revealed a myriad of issues plaguing her gym, but nothing concrete that pointed to sabotage. The situation seems hopeless to me, but I'm still resolved to help."
    $ unread_veronica = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    "..."
    mct "(Maybe I should ask Samson directly? That bastard is so guileless that wringing out specifics from him shouldn't be too hard.)"

    if date == "june09day":
        jump w2HanaNight1
    else:
        jump w2HanaNight2

label w2HanaNight1:

    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionhana02 with blinds
    $ renpy.pause(6, hard=True)
    $ date = "june09night"
    play sound "sound effects/door-open.wav"

    if w2RoseFirst == True:
        scene w2_3107 with blinds
        show screen textbox2 with dissolve
        show screen qmenu with dissolve
        "As soon as I cracked the door to my apartment, a peculiar smell rushed to greet me."
        "The heady scent of oregano and melted cheese, mingled with smoky odor of burnt food."
        "It seems that Hana had..."
        play music "music/i-knew-a-guy.ogg"
        scene w2_3108 with dissolve
        show june09night with squares
        "Ordered a pizza."
        hana "'Ey, yo. Good timing. You probably saw the pizza guy on his way out."
        scene w2_3109 with dissolve
        mc "What's..."
        mc "You cooked as well?"
        hana "Oh, that? I wanted to cook you dinner tonight as way of a proper thanks for letting me crash here."
    else:

        scene w2_3110 with blinds
        show screen textbox2 with dissolve
        show screen qmenu with dissolve
        "As soon as I cracked the door to my apartment, a peculiar smell rushed to greet me."
        "The heady scent of oregano and melted cheese, mingled with smoky odor of burnt food."
        "It seems that Hana had..."
        play music "music/i-knew-a-guy.ogg"
        scene w2_3111 with dissolve
        show june09night with squares
        "Ordered a pizza."
        hana "'Ey, yo. Good timing. You probably saw the pizza guy on his way out."
        scene w2_3112 with dissolve
        mc "What's..."
        mc "You cooked as well?"
        hana "Oh, that? I wanted to cook you dinner tonight as way of a proper thanks for letting me crash here."

    scene w2_3113 with dissolve
    hana "You made it look so easy the other night..."
    scene w2_3114 with dissolve
    "That explains the burning smell."
    mc "I thought we were past {i}thank yous{/i} as of this morning."
    scene w2_3115 with dissolve
    hana "Heheh, well a girl's got to eat. Might as well make it a 2-for-1 and score some brownie points."
    scene w2_3116 with dissolve
    hana "I didn't know what kind of pizza you liked, so I just played it safe and got pepperoni."
    scene w2_3117 with dissolve
    mc "That's fine. Pepperoni suits a boring asshole like me just fine."
    "Pizza topping off a day of debauchery..."
    mct "(Not bad.)"
    scene w2_3118 with dissolve
    hana "So what did you do today? You said business, right?"
    scene w2_3119 with dissolve
    mc "Yeah, it ate up my whole afternoon."

    if w2RoseFirst == True:
        mc "I met with Rosalind for an... \"extracurricular\" photo shoot in the park."
        scene w2_3118 with dissolve
        hana "That's the extra MILFy one, right?"
        scene w2_3119 with dissolve
        mc "Ha, that's one way to describe her."
    else:

        mc "I met with Veronica for an... \"extracurricular\" photo shoot at her gym."
        scene w2_3118 with dissolve
        hana "That's the beefy one, right?"
        scene w2_3119 with dissolve
        mc "That's one way to put it."

    scene w2_3120 with dissolve
    hana "I can only imagine how that shit went."
    scene w2_3119 with dissolve
    mc "You don't want to hear about it. It'll just ruin your mood before dinner."
    scene w2_3120 with dissolve
    hana "Yeah, I'll thank you for sparing me the details."
    scene w2_3121 with dissolve
    hana "Now--!"
    hana "Grab a slice!"
    scene w2_3122 with dissolve
    mc "Let me get changed into something more comfortable first."
    scene black with fade
    "Over pizza, I put on a movie in the background while, among other topics, Hana regaled me with how her practice went."
    scene w2_3123 with fade
    mc "He really did that?"
    scene w2_3124 with dissolve
    hana "Yuuuup!"
    scene w2_3123 with dissolve

    if hanaFlag == True:
        mc "Spider... isn't too bright, is he?"
    else:
        mc "That guy doesn't sound very bright."

    scene w2_3125 with dissolve
    hana "Haha... no, he's a pretty dim bulb. I would question what Jerrica sees in him, but he's got a big cock and she tells me he knows how to use it."
    hana "Oh, and he's like \"extremely thoughtful, kind, and funny\", but I'm pretty sure it's the fact he's the only guy she's ever dated."
    scene w2_3126 with dissolve
    mc "That's sweet. Every love is unique."
    scene w2_3127 with dissolve
    hana "It is, isn't it?"
    hana "I hope they never split. Not just because of the band, but because the world would be a lot better place if more people had what they have."
    hana "Even if it is so bewildering."
    scene w2_3128 with dissolve
    "The two of us shared a comfortable silence, before she brought things back to life."
    scene w2_3129 with dissolve
    hana "You already finished? That was like half a pizza! How the fuck are you so skinny?"
    scene w2_3126 with dissolve
    mc "I normally don't eat that much, actually... but this past week my appetite's been humongous."
    scene w2_3130 with dissolve
    hana "And what's got you so insatiable this week?"
    scene w2_3131 with dissolve
    mc "Uh... working for Mrs. Pulman really takes it out of you."
    "I didn't want to bring it back around to this topic, but she did inadvertently ask."
    scene w2_3132 with dissolve
    hana "...oh, jeeeeeez!"
    scene w2_3133 with dissolve
    mc "Pft--!"
    hana "Mhaha..!"
    "We joined together in a brief, but hearty laugh at the absurdity of the situation."

    if hanaFlag == True and w2HanaSex == True:
        scene w2_3134 with dissolve
        hana "Ah..."
        scene w2_3135 with dissolve
        mc "......"
        hana "..."
        scene w2_3136 with dissolve
        hana "Sorry."
        scene w2_3138 with dissolve
        mc "For what?"
        scene w2_3136 with dissolve
        hana "If you didn't notice, then forget I said anything."
        scene w2_3137 with dissolve
        mct "(Did she mean the way she touched me just now?)"
        mct "(Why would she apologize for that?)"
    else:

        hana "Aha..."

    scene w2_3139 with dissolve
    hana "I'm going to go shower. Beating the hell out of a drum kit really works up a sweat."
    hana "I probably stink right?"
    scene w2_3140 with dissolve
    mc "No, but that might be because of the food you burned."
    scene w2_3141 with dissolve
    hana "Ha, fuck you!"

    scene black with fade
    "After her shower, she rejoined me for the movie."

    if hanaFlag == True and w2HanaSex == True:
        scene w2_3148 with w20
        mc "I love this part."
        hana "Is it all the half-naked dancers?"
        mc "No! It's... a catchy song."
        scene w2_3149 with dissolve
        scene w2_3150 with dissolve
        scene w2_3149 with dissolve
        "......"
        scene w2_3151 with dissolve
        "..."
        scene w2_3152 with dissolve
        hana "This movie is... surprisingly tragic."
        scene w2_3153 with dissolve
        mc "You could say Gideon brought it on himself."
        scene w2_3154 with dissolve
        hana "That doesn't make it any less sad."
        scene w2_3155 with dissolve
        mc "No, it doesn't..."
        scene w2_3156 with dissolve
        "......"
        "..."
    else:

        scene w2_3142 with w20
        mc "I love this part."
        hana "Is it all the half-naked dancers?"
        mc "No! It's... a catchy song."
        scene w2_3143 with dissolve
        scene w2_3144 with dissolve
        scene w2_3143 with dissolve
        "......"
        scene w2_3145 with dissolve
        "..."
        scene w2_3146 with dissolve
        hana "This movie is... surprisingly tragic."
        scene w2_3147 with dissolve
        mc "You could say Gideon brought it on himself."
        scene w2_3146 with dissolve
        hana "That doesn't make it any less sad."
        scene w2_3147 with dissolve
        mc "No, it doesn't..."
        scene w2_3145 with dissolve
        "......"
        "..."

    scene black with fade
    hana "Not my usual thing, but that was pretty good!"
    hana "Oh, you're already turning in?"
    stop music fadeout 2.0
    "......"
    "..."
    jump w2HanaMorning2

label w2HanaMorning2:

    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionhana03 with blinds
    $ renpy.pause(6, hard=True)
    $ date = "june10day"
    scene black with blinds
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    "Giggling."
    scene w2_3157 with circlewipe
    "Sweet and nostalgic giggling."
    play music "music/crinoline-dreams.ogg"
    scene w2_3158 with dissolve
    show june10day with squares
    "Familiar, warm, and comforting."
    "The next morning, I awoke with a smile on my face."
    $ renpy.music.set_volume(.1, 1, channel = "music")
    scene w2_3159 with dissolve
    play sound "sound effects/horror.wav"
    mct "(Wait...)"
    scene w2_3160 with fade
    "Not just familiar."
    scene w2_3161 with dissolve
    "{b}Familial{/b} laughter."
    "Talking to..."
    scene w2_3162 with wipeleft
    hana "Hey! Speak of the devil!"
    hana "He's finally up!"
    scene w2_3163 with dissolve
    mc "Morning..."
    scene w2_3164 with dissolve
    vic "We were just talking about you."
    vic "Have some coffee with Hana and me, hun."
    scene w2_3165 with dissolve
    "The way she emphasized her name in an overly well-acquainted way..."
    scene w2_3163 with dissolve
    mc "One sec."
    scene w2_3165 with dissolve
    stop sound
    play sound "sound effects/string-break.wav"
    $ renpy.music.set_volume(1, 3, channel = "music")
    "Felt like someone breaking a violin string."
    scene black with fade
    mc "Uh... just how long..."
    scene w2_3166 with cmet
    mc "How long have you been here?"
    scene w2_3168 with dissolve
    vic "Oh, only about ten minutes or so?"
    scene w2_3169 with dissolve
    hana "Long enough for me to change and for your mom to fix us a cup of coffee."
    scene w2_3167 with dissolve
    "Ten minutes: not very long in the scheme of things, but long enough for my mother to draw her own conclusions."

    if hanaFlag == True and w2HanaSex == True:
        scene w2_3170 with dissolve
        vic "Got to be honest, [mcf]... I wasn't expecting to find a woman in your apartment, let alone one prancing about half-naked."
        scene w2_3172 with pixellate
        mc "Naked...?"
        hana "Just... what I sleep in."
    else:

        scene w2_3171 with pixellate
        vic "Got to be honest, [mcf]... I wasn't expecting to find a woman in your apartment."

    mc "Thanks for your vote of confidence, Mother."
    scene w2_3173 with pixellate
    vic "You never mentioned to me about having a {i}lady friend{/i}."
    scene w2_3174 with dissolve
    vic "I guess I did all that worrying about you for nothing."
    scene w2_3175 with dissolve
    mc "You've got the wrong idea, she's not..."
    stop music fadeout 5.0
    scene w2_3176 with dissolve
    hana "The wrong idea? That's not what you told me on your birthday..."
    scene w2_3177 with dissolve
    vic "Oh, no... did I misunderstand?"
    vic "Is this one of those \"pump and dump\" sit--"
    scene w2_3178 with dissolve
    hana "Pfffft...!"
    "Before she could even get the words out, they both cracked up."
    play music "music/sugar-zone.ogg"
    scene w2_3179 with vpunch
    vic "Pfhahaha...!!"
    scene w2_3180 with dissolve
    mc "......"
    mc "..."
    scene w2_3181 with dissolve
    mc "...already both screwing with me, huh?"
    scene w2_3182 with dissolve
    vic "Sorry! Couldn't resist!"
    scene w2_3183 with dissolve
    vic "Hana already told me about her having a fight with her mother and needing a place to stay."
    vic "Still, a mother can hope a supportive hand might lead to..."
    scene w2_3184 with dissolve
    vic "Oops! I'll stop there. Wishful thinking."
    scene w2_3185 with dissolve
    mc "She's a friend and coworker."
    scene w2_3186 with dissolve
    vic "I know."
    scene w2_3185 with dissolve
    mc "You guys talked about work?"
    scene w2_3174 with dissolve
    vic "In passing. She was as vague about the place as you are."
    scene w2_3187 with dissolve
    vic "Men's club, huh? Makes sense they'd keep a pretty little thing like Hana around."
    scene w2_3188 with dissolve
    hana "Ah, stop..."
    scene w2_3189 with dissolve
    vic "I can only imagine what you put up with in an environment like that."
    scene w2_3185 with dissolve
    mc "Everyone there's a gentleman."
    scene w2_3186 with dissolve
    vic "{b}Yeah{/b}, I know how gentlemen are."
    scene w2_3190 with dissolve
    vic "Just saying: don't let anyone get handsy with you just because you're a waitress. A job isn't worth that."
    scene w2_3191 with dissolve
    mc "You're making a big assumption. It's a nice place."
    "It was genuinely difficult to keep a straight face while spouting that bald-faced lie."
    scene w2_3192 with dissolve
    vic "Maybe. I hope I am, but you're also a guy, hun."
    scene w2_3193 with dissolve
    hana "No need to worry, Mrs. [mcl]. I can take care of myself."
    scene w2_3194 with dissolve
    vic "Vicky is fine."

    if w1ExHarrassmentRepeat == True:
        scene w2_3195 with dissolve
        hana "Plus, I did have a tiny bit of trouble with a drunk member the other night, but [mcf] swiftly gave me a hand."
        vic "He did?"
        scene w2_3196 with dissolve
        vic "That sounds just like [mcf]."
        vic "That's one of the things I'm most proud about. He was always quick to stand up for his friends."
        scene w2_3197 with dissolve
        mc "I think you may be looking back with rose-tinted glasses, Mom..."
        scene w2_3198 with dissolve
        vic "No. It's the advantage of hindsight, of knowing the man you've become."
        hana "Yeesh..."
        mc "Ah..."
        "Her look left no room for refusal."
        scene w2_3175 with dissolve
        mc "So, what are you doing here so early in the morning?"
        "...so I moved the conversation away from me."
    else:
        scene w2_3191 with dissolve
        mc "So, what are you doing here so early in the morning?"

    stop music fadeout 3.0
    scene w2_3199 with dissolve
    vic "I found something I thought was lost while going through some old boxes and I wanted to show it to you."
    mc "There was no need to make the trip over here. I could've met you at the house..."
    scene w2_3200 with dissolve
    vic "I also just felt like seeing my son right then and now."
    scene w2_3201 with dissolve
    vic "This belonged to your father."
    mc "What is it?"
    play music "music/inner-light.ogg"
    scene w2_3202 with fade
    vic "It was a gift from his old boss at the charity, for graduating law school."
    "Mom never really talked much about my dad. A little more as time went on, but..."
    vic "Put it on."
    mc "Okay."
    scene black with fade
    "Before putting it on, I closely examined it. It had a nice weight to it."
    "On the inside was an engraving. Small and hard to read."
    "The number of words must've meant it cost a fortune."
    scene w2_3203 with dissolve
    mc "I can't read it. What does it say?"
    scene w2_3204 with dissolve
    vic "Doing nothing for others is the undoing of ourselves."
    scene w2_3203 with dissolve
    mc "Huh... weird thing to put on a watch."
    scene w2_3205 with fade
    "Thankfully, the band ended up not needing any adjustment. It fit snugly around my wrist."
    scene w2_3206 with dissolve
    vic "Oh..."
    scene w2_3207 with dissolve
    vic "Hold out your wrist, hun."
    scene w2_3208 with dissolve
    vic "That takes me back. You remind me so much of your father."
    vic "I want you to have it, [mcf]. As a keepsake."
    scene w2_3209 with dissolve
    mc "Are you sure? Wouldn't you rather have it?"
    scene w2_3210 with dissolve
    vic "No. It's yours."
    vic "He wore it every single day to work."
    scene w2_3211 with dissolve
    mc "Thanks, Mom."
    "I hadn't ever really thought about it, but I guess I didn't really have anything valuable to call a memento of his."
    mc "You just found it in a box?"
    vic "Yeah, it's the funniest thing. I thought it was lost somewhere between the accident and after the hospital."
    vic "Everything immediately after that day was such a daze, I must've forgotten I put it away for safekeeping."
    mc "I can imagine..."
    scene w2_3212 with dissolve
    mc "I promise to keep it safe then."
    scene w2_3213 with dissolve
    vic "..."
    scene w2_3214 with dissolve
    vic "Come here, Hana!"
    scene w2_3215 with dissolve
    hana "...why?"
    scene w2_3216 with dissolve
    vic "Don't talk back. Just get your cute butt here."
    scene w2_3217 with dissolve
    hana "Mmmh... okay..."
    scene w2_3218 with dissolve
    hana "What do you--"
    scene w2_3219 with dissolve
    vic "Heh, you're soft."
    hana "I... w-what..."
    scene w2_3220 with dissolve
    vic "This is better than just awkwardly standing there while [mcf] and I prattle on, right?"
    vic "A nice... big... warm hug."
    hana "I'm not really a hugger..."
    scene w2_3221 with dissolve
    vic "Oh, honey. I don't give a crap."
    vic "Just... think of England."
    hana "Think of...? What the f-"
    scene w2_3222 with dissolve
    mc "Eh, it's best to just listen to her."
    mc "It'll be over soon..."
    stop music fadeout 3.0
    scene black with fade
    "......"
    "..."
    hana "What the fuck, your mom is..."
    scene w2_3223 with dissolve
    hana "Exhausting, but pretty fucking cool."
    "Mom stayed another twenty minutes or so, mostly ignoring me and chatting Hana's ear off."
    scene w2_3224 with dissolve
    mc "She was just high on the discovery of finding someone of the opposite sex here."
    scene w2_3225 with dissolve
    hana "Ha! Even your mom thinks you're a loser!"
    scene w2_3226 with dissolve
    mc "Nuh-uh, I'll have you know..."
    scene w2_3227 with dissolve
    mc "My mom thinks I'm real cool."
    hana "Pfft-!"
    scene w2_3228 with dissolve
    hana "Don't make me laugh, this has been too much warmth for one day!"
    hana "...ah! I'm going to need to see my own mother soon to balance shit out."
    scene w2_3229 with dissolve
    mc "What are you doing today? More practice?"
    scene w2_3230 with dissolve
    hana "Dunno. Mrs. Pulman wanted to talk to me."
    scene w2_3229 with dissolve
    mc "Really? Is that normal?"
    scene w2_3230 with dissolve
    hana "Not at fucking all."
    scene w2_3229 with dissolve
    mc "You going?"
    scene w2_3231 with dissolve
    hana "Yeah, I'll humor the old bitch. If I don't, she'll just corner me at the club about it this Saturday anyway."
    hana "Might as well go while I still have an exit strategy."
    scene w2_3229 with dissolve
    mc "Smart."
    scene w2_3230 with dissolve
    hana "What about you? More club stuff?"
    scene w2_3229 with dissolve
    mc "More club stuff."
    scene w2_3231 with dissolve
    hana "*sigh* I like you better when there isn't more \"club stuff\" you know, but... I'm glad we're in this together."
    scene w2_3229 with dissolve
    mc "We in a foxhole or something?"
    scene w2_3232 with dissolve
    hana "Heh. Sort of."
    scene black with fade
    "......"
    "..."
    play sound "sound effects/phonemenu.wav"
    scene w2_1763 with dissolve
    show screen textbox2 with dissolve
    "Beep!"
    play sound "sound effects/ringing-outbound.mp3"
    scene w2_1761 with dissolve
    "......"
    scene black with fade
    "..."

    if w2RoseFirst:
        jump w2VeronicaGymStart
    else:
        jump w2RosalindParkStart


label w2HanaNight2:


    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionhousegirls with blinds
    $ renpy.pause(6, hard=True)
    $ date = "june10night"
    scene w2_3233 with blinds
    show screen textbox2 with dissolve
    show screen qmenu with dissolve

    if w2RoseFirst == True:
        "After getting home from the gym, my new housemate was nowhere to be found."
    else:
        "After leaving Rose, my new housemate was nowhere to be found."

    "So I simply had a small meal, vegged out on the couch, and accidently had myself a nice catnap."
    "I must've needed it after all the day's activity."
    mc "Hmm..."
    "........."
    "......"
    play sound "sound effects/door-openclose.wav"
    scene w2_3234 with dissolve
    mc "...?"
    scene w2_3235 with dissolve
    play music "music/modern-situations.ogg"
    scene w2_3236 with vpunch
    mc "O-ohmf?!"
    "The air suddenly vacated my lungs as an admittedly nice, but unexpectedly heavy ass landed square on my diaphragm."
    scene w2_3237 with dissolve
    hana "*Huff* Humhhh...!"
    scene w2_3238 with dissolve
    hana "Hey, [mcf]..."
    scene w2_3239 with dissolve
    mc "Hey, Hana..."
    scene w2_3240 with dissolve
    "She sounded more deflated than I was feeling."
    scene w2_3241 with dissolve
    mc "You pick that up on the way home? We've got a couple of bottles here."
    hana "I know, but I didn't want to presume and be a bad house guest."
    mc "That's okay, I didn't pay for any of the booze here. Your father did, I gue--"
    scene w2_3242 with hpunch
    hana "Don't mention that fucking deadbeat right now, okay? Please?"
    scene w2_3243 with dissolve
    mc "Okay... then I'll ask a dumb question. How did your day go?"
    scene w2_3244 with dissolve
    "She shook the bottle for emphasis."
    scene w2_3245 with dissolve
    mc "Aha... that bad?"
    mc "Do you want to talk about it?"
    scene w2_3246 with dissolve
    hana "No."
    scene w2_3247 with dissolve
    "Just no."
    scene w2_3248 with dissolve
    hana "You know, on the way home this seemed like a good idea, but..."
    scene w2_3249 with dissolve
    scene w2_3250 with dissolve
    play sound "sound effects/ice-glass.wav"
    hana "What a waste of money."
    scene w2_3251 with dissolve
    hana "How did \"work\" go today?"
    scene w2_3252 with dissolve

    if w2RoseFirst == True:
        mc "I... paraded a tall, muscular red-headed woman around like a dog."
    else:
        mc "I... took lewd, exhibitionistic pictures in a park of a woman old enough to be my mother."

    mc "So... just a normal day?"
    scene w2_3253 with dissolve
    hana "Ha...!"
    hana "That's so..."
    mc "Awesome?"
    hana "Funny."
    scene w2_3254 with dissolve
    hana "Don't try and finish my sentences, dork."
    scene w2_3255 with dissolve
    mc "You're pretty heavy you know."
    scene w2_3254 with dissolve
    hana "It's all this tit and ass. You complainin'?"
    scene w2_3256 with dissolve
    mc "No."
    "Just no."

    if hanaFlag == True:
        scene w2_3257 with fade
        hana "You mind?"
        mc "No."
        hana "Sorry to impose..."
        scene w2_3258 with dissolve
        mc "You sure you don't want to talk about it?"
        hana "In the morning. After I've made my decision on my own."
        hana "I already know what your advice would be."
        scene w2_3259 with dissolve
        mc "How do you know that?"
        scene w2_3260 with dissolve
        hana "Because you and I met, and no one twisted your arm."
        hana "You greedy fucker."
        scene w2_3261 with dissolve
        mc "Woah, woah, woah!"
        scene w2_3262 with dissolve
        hana "Sorry."
        hana "I don't mean that."
        scene w2_3263 with dissolve
        mc "Yeah, I get it."
        scene w2_3262 with dissolve
        hana "You do?"
        "This was about her meeting with Mrs. Pulman."
        "I knew well enough not to try and pry any further."
        scene w2_3264 with dissolve
        hana "Thank you."
        scene black with fade
        "For a half an hour, we laid chest-to-chest, with nothing spoken. The only thing filling the silence of my apartment being the hum of the refrigerator and the sound of our breathing."
        "Whether it was her intention or not..."
        scene w2_3265 with dissolve
        "Hana drifted off to sleep."
        mct "(Shit, my arm is falling asleep...)"
        hide screen textbox2 with dissolve

        menu:
            "Cling to Hana and sleep here."(chg=["hana_up", "maid"]):
                $ Hana_Affection +=1
                show screen textbox2 with dissolve
                "My comfort be damned, I didn't want to disturb her."
                scene w2_3266 with dissolve
                "Instead, I wrapped an arm around her and pulled her closer."
                hana "Mmmh..."
                "The action wrenched a soft, pleasant murmur from the sleeping beauty."
                "I internally chuckled at myself for even considering this the \"uncomfortable\" choice."
                scene black with fade
                stop music fadeout 3.0
                mct "(I hope Mom doesn't pop in tomorrow.)"
                "......"
                "..."

                if w2HanaSex == True:
                    $ w2HanaHump = True
                    jump w2HanaDream
                else:
                    jump w2HanaMorning3
            "Carry Hana to your bed.":



                show screen textbox2 with dissolve
                "I'll take the couch tonight."
                scene w2_3267 with dissolve
                "Hana could use the extra comfort."
                scene w2_3268 with dissolve
                "Although, she stirred, she surprisingly didn't wake."
                "All the way up, she just tightly clung to me."
                scene w2_3269 with dissolve
                mc "There, there..."
                scene w2_3270 with dissolve
                hana "Heh. Never been princess carried before."
                hana "You don't mind...?"
                scene w2_3269 with dissolve
                mc "No, take it tonight."
                scene black with fade
                hana "I won't argue."
                stop music fadeout 3.0
                "......"
                "..."
                jump w2HanaMorning3
    else:


        scene w2_3271 with dissolve
        hana "*Sigh* ..."
        scene w2_3272 with dissolve
        mc "Lot on your mind, clearly. You sure you don't want to talk about it?"
        scene w2_3273 with dissolve
        hana "No, it's something I want to settle without your input."
        scene w2_3274 with dissolve
        "The was a weird emphasis on the {b}my{/b} input."
        scene w2_3273 with dissolve
        hana "I know what your advice would be."
        scene w2_3274 with dissolve
        "To my chagrin, she certainly sounded sure of that."
        scene w2_3275 with dissolve
        mc "Okay, then. Take my bed tonight."
        mc "I'll sleep here."
        scene w2_3273 with dissolve
        hana "I don't wan--"
        scene w2_3276 with dissolve
        mc "Just do it, you mopey sad sack. You sound like you need the extra comfort."
        scene w2_3277 with dissolve
        hana "Ha! Okay, I won't be told three times."
        scene w2_3278 with dissolve
        hana "Thanks, [mcf]."
        mc "Sure, just let me know when you \"settle\" whatever it is."
        hana "I'll tell you about it in the morning."
        scene black with fade
        "With that, after Hana had changed and brushed her own teeth and things quieted down, I decided to just resume my nap right then and there."
        hana "Good night, [mcf]."
        mc "Good night."
        "......"
        "..."
        jump w2HanaMorning3

label w2HanaDream:

    play music "music/landing.ogg"
    scene w2_3360 with w13
    "*Schlick...!* *Fwhip...!* *Fhuhp..!*"
    hana "Ah...! Y-you're so..."
    scene dream1_a with dissolve
    show dream1
    hana "How are y-you so good at this, Rosie..."
    "*Schlick...!* *Fwhip...!* *Fhuhp..!*"
    scene dream2_a with dissolve
    show dream2
    ver "Mmmh..."
    hana "I feel like I'm being ripped apart!"
    ver "Ah... y-you've got to be ready for what's n-next..."
    chuck "Isn't this a blast from the past, lad?"
    scene w2_3361 with w24
    chuck "Long time no see, Dr. [mcl]."
    scene w2_3362 with dissolve
    chuck "Oh... you don't mind if I call you lad, do you? For old time's sake?"
    chuck "You've been so busy that you haven't had time to make it down to the club, but a man..."
    scene dream3_a with dissolve
    show dream3
    chuck "A man's appetite grows proportional to the food he's accustomed to."
    ver "See H-hana, the doctor is here for you."
    hana "A-ah!"
    "*Schlick...!* *Fwhip...!* *Fhuhp..!*"
    scene dream4_a with dissolve
    show dream4
    hana "I'm already ready!"
    "*Schlick...!* *Fwhip...!* *Fhuhp..!*"
    hana "I'm r-ready for..."
    ver "Don't rush this! You have all night with him."
    "*Schlick...!* *Fwhip...!* *Fhuhp..!*"
    hana "But I'm--ghhhfuchk!"
    chuck "Isn't it a beautiful sight, lad?"
    scene w2_3363 with w20
    chuck "You grow old and ugly, but the flowers at the club remain lovely and unwilting."
    chuck "Ha! Can you believe I almost picked botany as the focus of my studies..."
    scene w2_3364 with fade
    chuck "Yet, I still ended up with a garden of my own."
    chuck "Kinda funny!"
    scene w2_3365 with fade
    chuck "I'm sorry about your mother, by the way."
    chuck "I took the loss of my own hard too, but I hope this is a solace to you."
    scene w2_3366 with fade
    chuck "It may not feel like it some times, but she would've been proud."
    scene w2_3367 with w22
    chuck "She would've been proud of the man you've become."
    scene w2_3368 with dissolve
    hana "Hey, new guy."
    scene w2_3369 with vpunch
    hana "All this just to get laid?"
    hana "You fucking animal."
    scene w2_3370 with dissolve
    hana "{size=-15}Eh, eh...?{/size=-15}"
    hana "{size=-10}[mcf]...?{/size=-10}"
    scene w2_3371 with dissolve
    scene black with vpunch
    stop music fadeout 3.0
    mc "Ah...?"
    hana "[mcf]."
    "I woke up, pulled from my dream by Hana's lulling voice."
    $ renpy.end_replay()
    mct "(How long had I been asleep?)"

    if not persistent.hanaW2Dream:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.hanaW2Dream = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)

label w2HanaDryHump:

    scene w2_3372 with w12
    hana "You're tossing about."
    scene w2_3373 with dissolve
    mc "Sorry, I had a weird dream."
    play music "music/modern-situations.ogg"
    scene w2_3374 with dissolve
    hana "Oh?"
    hana "Weird, was it...?"
    hana "Your cock is hard."
    scene w2_3375 with dissolve
    mc "So it is..."
    scene w2_3374 with dissolve
    hana "...and it's pressing against me."
    scene w2_3375 with dissolve
    mc "That's bound to happen when--"
    scene w2_3376 with dissolve
    "I was cut off by a finger directing that I stop talking."
    hana "I don't mind."
    scene hanan_grind1_a with dissolve
    "As if to emphasize her point, she pressed her lower half into mine and left it there."
    "......"
    show hanan_grind1
    "..."
    "No words were said."
    "Breast-to-breast, we let the quickened rise and fall of our chests do the talking."
    "......"
    "..."
    "No words were further said still."
    "Crotch-to-crotch, the gentle sway of Hana's hips revealed to me everything that needed to be known at this junction."
    "Nothing concrete needed to be understood, just the short-lived burning flame of desire, needing to be snuffed out before it reached a bone-blackening pitch."
    scene hanan_grind2_a with dissolve
    show hanan_grind2
    "......"
    "..."
    "{i}Keep quiet, [mcf]{/i}."
    "That was the look."
    "I can do that."
    scene w2_3377 with dissolve
    hana "Put your hands on my ass."
    scene hanan_grind2_a with dissolve
    "I can do that too."
    scene hanan_grind3_a with dissolve
    show hanan_grind3
    "Eyes still half-lidded from sleep, I was happy to just go along with the flow and see where the rocker girl would lead this."
    "I would think this a continuation of a dream if not for the itchy, clawing sensation of Hana's tight denim pants rubbing against my cock assuring me this was indeed a physical reality."
    hana "Slap my butt."
    scene w2_3378 with dissolve
    "Yeah... Hana's large and rapturously soft ass..."
    "I could give it a slap."
    scene w2_3379 with dissolve
    play sound "sound effects/slap3.wav"
    scene w2_3380 with vpunch
    "*Smack*"
    scene hanan_grind4_a with dissolve
    show hanan_grind4
    hana "--!"
    "The result was a supercharged Hana, pistoning her hips even faster like a proper fucking."
    "This whole exercise was quite the literal and figurative cock tease. Dry humping would most certainly not get me there, not after what I had experienced thanks to the club."
    "Surprisingly, rather than frustration, I felt contentment. Hana rubbing herself against me like an awkward virgin was a satisfaction in and of itself."
    "It seemed to be enough for Hana, however, who soon clung tightly to me like a genuine lover as I bent my legs and lifted her up to give her more depth to her thrusts."
    "In contrast to the pleasant feeling of her soft breasts resting on my chest, her lower half took me on a rough, turbulent, and moderately uncomfortable ride."
    scene hanan_grind5_a with dissolve
    show hanan_grind5
    "Uncomfortable, but... enjoyable all the same."
    "Like a rollercoaster."
    hana "Kah...!"
    "A lone, hack-like cry of pleasure would be all I would extract from her, as she tightened her chest and refused to let anything else escape."
    hide screen textbox2 with dissolve

    menu:
        "Hug Hana tighter":
            scene hanan_grind6_a with dissolve
            show hanan_grind6
            show screen textbox2 with dissolve
            "Meeting her fervor halfway, I pulled her even deeper into the embrace, pressing her body as deep into mine as was humanly possible."
            "The tips of her jet-black fingernails dug deep into my shoulder blades, ten little pin pricks that completely cleansed any lingering sleepiness from my eyes."
            "Deeper and deeper, until she had her claws in me like a cat unwilling to let go."
            "Deeper still and..."
            scene w2_3381 with dissolve
            "Hana tensed up and her body went rigid, all air vacating her lungs as a jolt of ecstasy had her momentarily forget to breath."
            "......"
            "..."
        "Grab her breasts":

            scene hanan_grind7_a with dissolve
            show hanan_grind7
            show screen textbox2 with dissolve
            "Unable to resist the temptation that was in front of my face, I mustered my strength and lifted the would-be rock star up."
            "My fingers found purchase in the underside of Hana's breasts, my tips sinking deep into their seemingly endless volume."
            "They would've sunk deeper still, had it not been for the layers of clothing that tautly hugged her chest."
            "The frustration of not touching Hana's warm flesh and a caveman-like impulse to rip apart the sheer fabric and expose the treasure underneath almost got the better of me."
            "Fortunately, I reeled that explosive impulse in."
            mct "(She probably would be fucking pissed...)"
            scene w2_3382 with dissolve
            "Suddenly, Hana tensed up and her body went rigid, her head knocked back, and all air vacating her lungs as a jolt of ecstasy had her momentarily forget to breath."
            "......"
            "..."

    scene w2_3383 with vpunch
    "Just as abruptly it began, it also ended."
    "All tension left her and her body became jello in my arms."
    scene w2_3384 with dissolve
    hana "Ha..."
    hana "That was..."

    "Now, she snuggled up in a different way. A more comfortable way."
    "My cock was still painfully erect, but I still didn't say anything. It didn't feel like I should."
    "I just held her in silence and after some time..."
    hana "Zhhuu..."
    "Hana was asleep."
    scene black with fade
    "It was like a shared dream."
    $ renpy.end_replay()

    if not persistent.hanaW2DryHump:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.hanaW2DryHump = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)

label w2HanaMorning3:

    stop music
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionkathleen02 with blinds
    $ renpy.pause(6, hard=True)
    $ date = "june11day"

    scene w2_3279 with fade
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    mct "(Mhh...)"
    scene w2_3280 with dissolve
    "The light pouring into the room told me it was still early. Everything was bathed in a nice, dream-like hue of orange and red."
    scene w2_3279 with dissolve
    mct "(This couch sleeps pretty good...)"
    "I didn't really want to move, but I could hear signs of life in the apartment."
    scene w2_3280 with dissolve
    "Feet shuffling about, a faucet, the sound of... clanking glass?"
    scene w2_3281 with dissolve
    mc "Changed your mind about that drink, huh?"
    play music "music/that-one-bar-scene.ogg"
    scene w2_3282 with dissolve
    hana "That was when I had some head scratching to do, but now that I've made my decision..."
    scene w2_3283 with dissolve
    hana "I could use one."
    scene w2_3284 with dissolve
    "*Glug glug glug...*"
    scene w2_3285 with dissolve
    hana "Sorry to wake you, by the way."
    mc "You didn't disturb me."
    scene w2_3286 with dissolve
    hana "Good."
    scene w2_3287 with dissolve
    "She looked really good in this light."
    scene w2_3288 with dissolve
    mc "I'm on pins and needles wanting to find out what Mrs. Pulman talked to you about."
    scene w2_3289 with dissolve
    hana "You figured that out?"
    scene w2_3288 with dissolve
    mc "It doesn't take a detective to venture that guess -- you told me you were meeting her, remember?"
    scene w2_3286 with dissolve
    hana "Oh yeah. Ha! Guess you're not a mind reader."
    scene w2_3290 with dissolve
    mc "Did you think that was a real possibility?"
    scene w2_3291 with dissolve
    hana "Heh, no... I just forgot."
    hana "I did tell you I'd explain it in the morning."
    scene w2_3290 with dissolve
    mc "I'm not going to hold you to that, but I would like to hear it."
    scene w2_3321 with dissolve
    hana "Ah... so what she wanted was..."
    scene w2_3288 with dissolve
    mc "Is it complicated to explain?"
    scene w2_3321 with dissolve
    hana "Saying it aloud makes it feel real."
    scene w2_3288 with dissolve
    mc "If you want, start from the beginning."
    scene w2_3292 with dissolve
    hana "..."
    scene w2_3293 with dissolve
    hana "As you know, Mrs. Pulman asked me to meet with her, which is pretty unusual."
    hana "She flatters me from time to time, but she's never really {i}talked{/i} to me before."
    stop music fadeout 3.0
    scene w2_3288 with dissolve
    mc "Where did she ask to meet?"
    scene w2_3289 with dissolve
    hana "The club."
    play music "music/doll-dancing.ogg"
    scene w2_3294 with pixellate
    hana "What the fuck is this?"
    scene w2_3295 with dissolve
    kat "I need your opinion."
    scene w2_3296 with dissolve
    hana "...what could you POSSIBLY need my opinion about?"
    scene w2_3295 with dissolve
    kat "You know Mr. Travis, one of our patrons."
    scene w2_3294 with dissolve
    hana "What about him?"
    scene w2_3297 with dissolve
    kat "You seemed well acquainted with him."
    kat "You chatted with him for over twenty minutes last October. Quite the record, for you."
    scene w2_3298 with dissolve
    hana "Well acquainted? Bleugh, don't make me puke. The guy's a disgusting pig, but he manages a few interesting acts."
    hana "Shooting the shit with him was {i}marginally{/i} better than just standing there bored out of my mind watching old men pathetically try their best to orgasm."
    scene w2_3299 with dissolve
    kat "So... {b}colorful{/b}."
    scene w2_3297 with dissolve
    kat "Still you know the man's world better than I."
    scene w2_3300 with dissolve
    hana "I guess..."
    scene w2_3297 with dissolve
    kat "He's got an act that's playing a week-long homecoming show in the city, something Oath."
    scene w2_3300 with dissolve
    hana "Vulgar Oath."
    scene w2_3301 with dissolve
    kat "That's it!"
    scene w2_3303 with dissolve
    hana "They suck."
    scene w2_3302 with dissolve
    kat "I wasn't really looking for an assessment of their musical prowess, Miss Rhodes."
    scene w2_3303 with dissolve
    hana "I didn't figure, {b}Mrs. Pulman{/b}. What do you want?"
    scene w2_3302 with dissolve
    kat "As I understand it, the lead singer of Vulgar {i}Oats{/i} gets himself in a bit of trouble whenever he's in one city for more than a few days."
    kat "He falls in love with any half-bit floozy that gets their claws in him, which makes things problematic for Mr. Travis and the rest of the band."
    scene w2_3303 with dissolve
    hana "Okay..."
    scene w2_3304 with dissolve
    kat "That's where Andrea or Mercedes will come in. Mr. Travis had the idea of making a preemptive attack."
    kat "Have one of our girls get their claws in him and painlessly release him when the time comes. No fuss."
    scene w2_3305 with dissolve
    hana "Hot damn, that's so stupid."
    kat "I agree, but what I wanted your opinion on is..."
    scene w2_3306 with dissolve
    kat "Which woman here is more suited to entertain an immature, immensely moronic pretty boy who has never been told no in his life?"
    scene w2_3307 with dissolve
    hana "Come on, you want my opinion on this crap? That's what I drove down here for?"
    scene w2_3306 with dissolve
    kat "Humor me, Miss Rhodes. Please."
    kat "You know both the girls rather well."
    kat "You know the scene and the type of man the singer is."
    scene w2_3308 with dissolve
    hana "*Sigh* Couldn't you have done this over the phone?"
    hana "Uh..."
    scene w2_3309 with dissolve
    hana "........."
    scene w2_3310 with dissolve
    hana "......"
    scene w2_3311 with dissolve
    hana "..."
    scene w2_3312 with dissolve
    hana "Mercedes..."
    scene w2_3313 with dissolve
    hana "Wearing that."
    scene w2_3314 with dissolve
    kat "Excellent! That was easy enough!"
    scene w2_3315 with dissolve
    kat "You girls can go home now."
    scene w2_3316 with dissolve
    hana "Is that it?"
    scene w2_3317 with dissolve
    kat "Not quite, dear. Come up and have a drink with me in my office."
    $ renpy.music.set_volume(.2, 1, channel = "music")
    scene w2_3318 with pixellate
    mc "She wanted your opinion on which girl to send?"
    scene w2_3319 with dissolve
    hana "Oh, that was just the bullshit preamble to what she really wanted to talk about."
    scene w2_3318 with dissolve
    mc "That sounds like her."
    scene w2_3320 with dissolve
    "I've had my own taste of her meandering brand of slowly getting to the point."
    scene w2_3318 with dissolve
    mc "What did she really want to talk about?"
    scene w2_3319 with dissolve
    hana "Well, we went up to her office and had a drink. Dumb, bullshit chit chat until she finally dropped the bomb on me."
    $ renpy.music.set_volume(1, 1, channel = "music")
    scene w2_3322 with pixellate
    kat "You should accept your father's offer. You have a better mind for it than you give yourself credit for."
    scene w2_3324 with dissolve
    hana "...you know about {i}that{/i}?"
    scene w2_3322 with dissolve
    kat "Of course I do. He discussed it with Charles and I."
    scene w2_3324 with dissolve
    hana "I have no intention of having more to do with this place than I have to."
    scene w2_3323 with dissolve
    kat "You're a bitterly stubborn girl. It's a good trait to have in some circumstances, but in others... you're simply going to end up shooting yourself in the foot if you don't curtail the obstinacy."
    scene w2_3322 with dissolve
    kat "You already profit off this place, the only difference is the purse strings will belong to you."
    scene w2_3325 with dissolve
    hana "You can stop there. I don't give a shit about what my father wants. This place disturbs me."
    scene w2_3322 with dissolve
    kat "It's a matter of morals, is it? Do you have something against sex work?"
    scene w2_3324 with dissolve
    hana "No. I'm perfectly okay with the concept. What I have an issue with is pimps."
    scene w2_3322 with dissolve
    kat "You think the world can get by without managers?"
    scene w2_3324 with dissolve
    hana "I think it could get by without {b}pimps{/b}."
    scene w2_3327 with dissolve
    kat "Think about it. The women who work here have already proven unable to manage themselves. What we provide them is a steady hand."
    scene w2_3326 with dissolve
    hana "You mean you line your pockets with their misery. The women here are desperate and you take advantage of that."
    scene w2_3323 with dissolve
    kat "There are plenty of menial jobs out there that people only do out of desperation."
    scene w2_3329 with dissolve
    hana "The difference is no one's terrified of working fast food."
    scene w2_3328 with dissolve
    kat "Terrified? The girls aren't--"
    scene w2_3329 with dissolve
    hana "Don't bullshit me. The girls are afraid of my dad and they're afraid of you and that huge asshole that follows you around."
    scene w2_3330 with dissolve
    hana "...and for whatever reason, Dalia is {b}especially{/b} afraid of Chuck."
    scene w2_3331 with dissolve
    kat "Oh, sweet, naive Hana..."
    scene w2_3332 with dissolve
    kat "The world isn't kind and this is a business that requires order."
    kat "If not here, they'd have more dire things to be afraid of. You say you have an issue with pimps, but if the alternative was them sinking deeper into their addictions or financial ruin, is this place not the better choice?"
    scene w2_3331 with dissolve
    kat "At least with the club, their lives are slowly being put back on track."
    scene w2_3333 with dissolve
    hana "Holy shit. Do you even hear yourself? Do you actually buy into that festering, fly-infested bullshit?"
    hana "They had a way to get their lives back on track, but you used your sister's charity as a door to exploit them. "
    scene w2_3334 with dissolve
    kat "......"
    hana "..."
    scene w2_3335 with dissolve
    kat "Let's get real for a second, then."
    kat "Your biggest issue with this place isn't the morality of it all. It's your father."
    scene w2_3336 with dissolve
    hana "I've got more than one bone to pick."
    scene w2_3337 with dissolve
    kat "Yes, but the main one is: you're a strong-willed woman and you resent being forced into things."
    scene w2_3336 with dissolve
    hana "No shit."
    scene w2_3338 with dissolve
    kat "Your mother needs care, but she likely has years left, doesn't she?"
    kat "He won't bend on his stipulations. You'll be here awhile, even if you're just waiting for her to pass on."
    scene w2_3339 with dissolve
    hana "..."
    scene w2_3338 with dissolve
    kat "You should take him up on his offer."
    scene w2_3340 with dissolve
    kat "For whatever reason, that man is dead set on kindling a father-daughter relationship with you. You should take advantage of that."
    kat "Show an interest in the business like he asked. Then take the half of the equity he's offering you now and the other half when he retires."
    scene w2_3338 with dissolve
    kat "Instead of being pulled along, go with a flow until you're in a suitable position to redirect. Get your own say in things."
    scene w2_3341 with dissolve
    kat "Do some good instead of throwing tantrums like a {b}petulant child{/b}."
    scene w2_3342 with dissolve
    hana "...gh. The mask is coming off now, isn't it bitch?"
    scene w2_3343 with dissolve
    kat "Don't take it that way, Miss Rhodes. I really do like you. You're a strong woman, especially for your age. You just resent that I'm right about your situation."
    scene w2_3332 with dissolve
    kat "Your father has an old school way of doing things, but he'll be pliable to suggestion with you on board. Things can change around here. Become more velvet glove, than iron fist."
    kat "Quite frankly, I don't really care what motivates the girls as long as they perform."
    scene w2_3333 with dissolve
    hana "Bullshit. I won't get a say, the old man will just be jerking me around a different way."
    scene w2_3331 with dissolve
    kat "Oh, child. Even just half of his share of the business is larger than mine."
    scene w2_3343 with dissolve
    kat "I guarantee you, you'll have sway, especially with me backing you."
    hana "..."
    scene w2_3344 with dissolve
    kat "Plus, when he does retire and you assume August's full side of the business, if this place still remains unpalatable to you..."
    scene w2_3345 with dissolve
    kat "Spit on his legacy. Wash your hands of the place."
    kat "Sell it to me and set you, your mother, and anyone you wish up for life. I hear your best friend lives out of a van?"
    scene w2_3346 with dissolve
    hana "..."
    scene w2_3345 with dissolve
    kat "Think it over, dear."
    scene w2_3347 with pixellate
    hana "I know the bitch is just counting on me selling it to her, but fuck me...!"
    stop music fadeout 3.0
    hana "She's right."
    scene w2_3348 with dissolve
    mc "Huh, holy shit..."
    mc "So when you say you reached a decision, what you really mean is..."
    mc "I should be calling you boss from now on?"
    play music "music/that-one-bar-scene.ogg"
    scene w2_3349 with dissolve
    hana "Please, no!"
    scene w2_3350 with dissolve
    hana "I don't have it yet, anyway. The old man's condition for half of his shares is that I show an active interest in learning the business."
    scene w2_3351 with dissolve
    mc "And that's what you're going to do? \"Learn\" the business, whatever that means?"
    scene w2_3350 with dissolve
    hana "Yep. That's what I'm going to do."
    scene w2_3352 with dissolve
    mc "Hmm..."
    "Retain her ownership or sell it to Mrs. Pulman; Hana is set if she agrees to this. Yet she seems so..."
    scene w2_3351 with dissolve
    mc "You afraid?"
    scene w2_3353 with dissolve
    hana "Yeah, but I don't understand it."
    scene w2_3354 with dissolve
    mc "I sympathize. In my case, I was afraid I might learn some nasty truths about myself."
    mc "In your case, you were previously forced into this by your dad. It was easier to rationalize your role in the club."
    mc "Now you're making an active choice and that's scary."
    scene w2_3355 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Emphasize her good qualities.":
            scene w2_3356 with dissolve
            show screen textbox2 with dissolve
            mc "Luckily for you, you're a good person. That place won't change you."
            mc "...but maybe you could change it just a little?"
            scene w2_3357 with dissolve
            hana "You're crazy if you think that's actually possible."
            scene w2_3356 with dissolve
            mc "It's at least worth trying, right? Maybe you could start small."
            scene w2_3357 with dissolve
            hana "Maybe..."
        "Emphasize the importance of the money."(chg=["hana_anger_up"]):


            $ Hana_Anger += 1
            scene w2_3358 with dissolve
            show screen textbox2 with dissolve
            mc "Just think of what you can do with that money once you get out from underneath your father's thumb."
            scene w2_3359 with dissolve
            hana "Is that what keeps you going?"
            scene w2_3358 with dissolve
            mc "I'm not ashamed to admit that. I want to help my mom with her retirement and the first step there is getting a good job."
            scene w2_3356 with dissolve
            mc "Besides, if you do sell it, that'll be a nice fuck you to your father won't it?"
            scene w2_3357 with dissolve
            hana "It would be..."

    scene w2_3356 with dissolve
    mc "Either way, I'll be there every step of the way with you as a friend."
    mc "I can't quit either, anyway."
    scene w2_3357 with dissolve
    hana "You could, but..."
    scene w2_3385 with dissolve
    hana "I kinda don't want you to if I'm going balls deep on the place."
    scene w2_3386 with dissolve
    "We shared a look and for the first time since I woke up, my mind let me be keenly aware of a particular detail."
    scene w2_3351 with dissolve
    mc "By the way, not that I mind, but..."
    scene w2_3387 with dissolve
    mc "You sure it's okay to be sitting there dressed like that?!"
    scene w2_3388 with dissolve
    hana "Oh? Wha...?"
    hana "Give me a break. I slept in my clothes last night."

label w2HanaMCKiss:
    if _in_replay:
        show screen textbox2 with dissolve
    if hanaFlag == True:
        scene w2_3389 with dissolve
        mc "I'm the one who {b}needs{/b} a break! You're taking me too lightly as a man."
        scene w2_3390 with dissolve
        hana "Am I?"
        scene w2_3391 with dissolve
        mc "Yeah, {b}waaaay{/b} too lightly. The close proximity, the clothes, and not to mention..."

        if w2HanaHump == True and w2HanaSex == True:
            mc "Whatever the hell came over you this morning when you were so damn thirsty that you dry humped yourself into a coma."
            scene w2_3392 with dissolve
            hana "Heh... uh..."
            hana "I..."
            scene w2_3393 with dissolve
            hana "Can't blame the booze, can I?"
            hana "I hear you. If having a cute, young half-naked woman in your apartment is really such a problem..."
            scene w2_3394 with dissolve
            hana "I'll go get dressed."
            hana "Wouldn't want you to feel that I'm taking you too lightly as a ma--"
            scene w2_3395 with dissolve
            stop music fadeout 2.0
            mc "That wasn't what I was getting at."
            hana "Wh-"
            play music "music/everything-you-wanted.ogg"
            scene w2_3396 with vpunch
            mc "I'm just letting you know that I'm beginning to feel... {b}frustrated{/b}."
            scene w2_3397 with dissolve
            hana "Frustrated? Because of lil' ol' {i}me{/i}?"
            hana "Oh, golly. That wasn't my intention."
            hana "I wouldn't want you to feel like I just used you like a toy. What should I do to help cool things down??"
            scene w2_3398 with dissolve
            hana "Mmh..."
            "The look Hana gave me was pure combustion, that..."
            scene w2_3399 with wipeleft
            hana "Mmmh...!"
            "Spurred me into action."
            scene hanahome_kiss1_a with dissolve
            show hanahome_kiss1
            "...although I'm not so sure that I pulled her into the kiss as much as she met me half way."
            "*Chwup, fwhup...!*"
            scene w2_3400 with dissolve
            "It was a painfully short embrace."
            scene w2_3401 with dissolve
            hana "You think it's a good idea to just kiss your boss like that?"
            scene w2_3402 with dissolve
            mc "I thought you didn't want me to call you that."
            scene w2_3401 with dissolve
            hana "Well..."
            scene w2_3402 with dissolve
            mc "You're going to use it whenever it suits you, aren't you?"
            scene hanahome_kiss1_a with dissolve
            show hanahome_kiss1
            "*Chwup, chwup...!"
            "This time it was all her."
            "Fwhup...! Cwhup...!"
            scene w2_3401 with dissolve
            hana "What were you saying?"
            scene w2_3402 with dissolve
            mc "I..."
            mc "Nothing important."
            scene w2_3403 with dissolve
            hana "You're too damn cute, for a dweeb."
            scene w2_3404 with dissolve
            mc "You got to work on your pillow talk."
            scene w2_3403 with dissolve
            hana "Don't presume we're going to find our way to any pillows."
            scene w2_3405 with dissolve
            hana "Mhmh, oh!"
            scene w2_3406 with dissolve
            "*Chwup, chwup...!"
            scene hanahome_kiss2_a with dissolve
            show hanahome_kiss2
            "With one deft movement, I hiked the rag she was using as a shirt up and brought my mouth to the tip of her exposed breast."
            "*Chwup, fwhup, fhup...!"
            scene w2_3407 with dissolve
            mc "What were you saying?"
            hana "I..."
            scene hanahome_kiss2_a with dissolve
            show hanahome_kiss2
            hana "Oh, oh...!"
            hana "I was just..."
            "*Chwup, fwhup, fhup...!"
            hana "R-running my mouth like an idiot..."
            scene w2_3408 with dissolve
            hana "You..."
            hana "You really shouldn't leave it unoccupied."
            scene hanahome_kiss3_a with dissolve
            show hanahome_kiss3
            "It was the strongest kiss yet. We locked lips in the truest, inescapable sense of the word."
            hana "Mmmh..."
            "Hana held me in place by my neck, jamming her tongue in my mouth with a charmingly inexperienced zeal."
            scene w2_3409 with dissolve
            hana "[mcf]..."
            "She looked like she did earlier, but this time it was like she was waiting for me to make the next move."
            scene w2_3410 with dissolve
            hana "--!"
            scene w2_3411 with dissolve
            mc "Can I?"
            scene w2_3412 with dissolve
            hana "...let me clean up first?"
            scene w2_3413 with dissolve
            hana "It's been an embarrassingly long time and I want to feel, uh... you know."
            hana "My best?"
            scene w2_3414 with dissolve
            "Stop and go is awfully frustrating, but..."
            scene w2_3415 with dissolve
            mc "You're the boss."
            scene w2_3416 with dissolve
            if not persistent.hanaMCKiss:
                play sound "sound effects/notification.wav"
                show memoryunlock with dissolve
                $ renpy.pause(3, hard=True)
                $ persistent.hanaMCKiss = True
                hide memoryunlock with dissolve
                $ renpy.pause(0.5, hard=True)
            hana "Thanks, [mcf]..."
            $ renpy.end_replay()
            scene black with fade
            stop music fadeout 3.0
            $ history_hana = "After inexplicably dry humping me in the middle of the night, Hana revealed something extremely interesting: she stands to inherit a significant portion of the Carnation Club."
            $ unread_hana = True
            play sound "sound effects/notification.wav"
            show bioupdate with dissolve
            "..."

        if w2HanaSex == True and w2HanaHump == False:
            mc "Still, I am a man..."
            scene w2_3393 with dissolve
            hana "Ha! You better not look at me that way."
            scene w2_3394 with dissolve
            hana "I'm your future boss, idiot."
            scene w2_3417 with dissolve
            mc "I thought you didn't want me to call you that."
            scene w2_3418 with dissolve
            hana "That's right, but I can call myself that if I want."
            hana "You mind if I use the bathroom first?"
            scene w2_3417 with dissolve
            mc "You're the boss."
            scene w2_3419 with dissolve
            hana "You know, I could just come around on this."
            scene w2_3420 with dissolve
            mc "I have a feeling you're not going to hate everything about your decision."
            scene w2_3421 with dissolve
            mct "(Ian's going to have a fuckin' aneurysm.)"
            scene black with fade
            stop music fadeout 3.0
            $ history_hana = "Hana revealed something extremely interesting: she stands to inherent a significant portion of the Carnation Club."
            $ unread_hana = True
            play sound "sound effects/notification.wav"
            show bioupdate with dissolve
            "..."


        if w2HanaSex == False and w2HanaHump == True:
            mc "The offer you made last Sunday."
            scene w2_3393 with dissolve
            hana "Oh? You regretting it?"
            mc "No, but..."
            scene w2_3394 with dissolve
            hana "Heh. I don't feel so bad about you rebuffing my advances now at least."
            hana "Nice to know you see me that way."
            scene w2_3417 with dissolve
            mc "Do you actually care about that?"
            scene w2_3418 with dissolve
            hana "Even a gal like me has her pride."
            scene w2_3417 with dissolve
            mc "......"
            hana "..."
            scene w2_3418 with dissolve
            hana "It'd be inappropriate now that I'm your future boss."
            scene w2_3417 with dissolve
            mc "Oh, shut up! You're going to use that whenever it's convenient."
            scene w2_3419 with dissolve
            hana "Yup!"
            scene w2_3420 with dissolve
            mc "Where are you going?"
            hana "Ladies' room. To get changed."
            hana "Feel free to take one last look."
            scene w2_3421 with dissolve
            mc "Ha!"
            mct "(She sure let that go to her head.)"
            scene black with fade
            stop music fadeout 3.0
            $ history_hana = "Hana revealed something extremely interesting: she stands to inherent a significant portion of the Carnation Club."
            $ unread_hana = True
            play sound "sound effects/notification.wav"
            show bioupdate with dissolve
            "..."
    else:

        mc "Still, I am a man..."
        scene w2_3393 with dissolve
        hana "Ha! You better not look at me that way."
        scene w2_3394 with dissolve
        hana "I'm your future boss, idiot."
        scene w2_3417 with dissolve
        mc "I thought you didn't want me to call you that."
        scene w2_3418 with dissolve
        hana "That's right, but I can call myself that if I want."
        hana "You mind if I use the bathroom first?"
        scene w2_3417 with dissolve
        mc "You're the boss."
        scene w2_3419 with dissolve
        hana "You know, I could just come around on this."
        scene w2_3420 with dissolve
        mc "I have a feeling you're not going to hate everything about your decision."
        scene w2_3421 with dissolve
        mct "(Ian's going to have a fuckin' aneurysm.)"
        scene black with fade
        stop music fadeout 3.0
        $ history_hana = "Hana revealed something extremely interesting: she stands to inherent a significant portion of the Carnation Club."
        $ unread_hana = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve
        "..."

    scene w2_3422 with fade
    play music "music/sneaky-snitch.ogg"
    "Faced with the prospect of killing time while Hana was in the shower, I did what anyone in my situation would do."
    if w2HanaSex == True:
        scene w2_3423 with dissolve
        mc "Nice."
        "No harm in keeping the fire going, right...?"
    else:
        scene w2_3424 with dissolve
        mc "Cute..."
        mct "(Wonder what August's policy on pets is...)"

    play ambient "sound effects/ringing-inbound.wav"
    scene w2_3425 with dissolve
    "*Ring, ring*"
    "A face I didn't expect replaced the \"content\" that was previously occupying my screen."
    mct "(Felicia...)"
    mct "(Oh yeah...)"
    "I was so preoccupied with Hana's company that I forgot to feel anxious about my preposterous \"interview\" with her husband. That said..."

    if kat_polite == True:
        mct "(Mrs. Pulman was keeping her in the dark about today. What could she want?)"
    else:
        mct "(Kathleen was keeping her in the dark about today. What could she want?)"

    stop ambient
    scene w2_3426 with dissolve
    mc "Hello? Felicia?"
    scene w2_3427 with dissolve
    fel "[mcf]. Is this a bad time?"

    if w2HanaSex == True:
        scene w2_3426 with dissolve
        mc "You could call it a bad--"
        scene w2_3427 with dissolve
        fel "Well, tough titties. It is for Mina too."
    else:

        scene w2_3426 with dissolve
        mc "Not really."
        scene w2_3427 with dissolve
        fel "Good, because it is for Mina."

    scene w2_3428 with dissolve
    mc "What's wrong with Mina?"
    scene w2_3429 with dissolve
    fel "She's... well..."
    scene w2_3430 with vpunch
    play sound "sound effects/metal-drop.wav"
    fel "--!"
    fel "H-hey! That's not quite what I meant when I said get angry, not sad!"
    scene w2_3431 with dissolve
    mc "What's...?"
    scene w2_3432 with dissolve
    fel "Listen, [mcf]. Could you do me a favor?"
    fel "I could use a lil' assist in playing emotional pick up for our mutual spritely, bottle rocket of a friend."
    fel "Could come over to Mina's? The sooner the better."

    if w2HanaSex == True:
        scene w2_3433 with dissolve
        mct "(Ah, fuck)..."
        scene w2_3434 with dissolve
        mc "I was in the middle of..."
        scene w2_3433 with dissolve
        fel "Please?"
        mct "(Getting some.)"
        scene w2_3426 with dissolve
        mc "Yeah, of course I will."
    else:
        scene w2_3426 with dissolve
        mc "Yeah, I'm free today until my... thing."
        scene w2_3427 with dissolve
        mct "(With you.)"

    scene w2_3435 with dissolve
    fel "Great! Oh my god, thank you! Do you know the address?"

    if minaFlag == True:
        scene w2_3436 with dissolve
        mc "Yeah, I've been there."
        scene w2_3437 with dissolve
        fel "Good, because I suck at directions."
    else:
        scene w2_3436 with dissolve
        mc "No."
        scene w2_3438 with dissolve
        fel "Alright... uh... let's see I suck at directions... do you know where..."
        scene w2_3436 with dissolve
        mc "I'll just plug it into the internet."
        scene w2_3437 with dissolve
        fel "Great, I'll find a piece of mail and text it to you."

    play sound "sound effects/phonemenu.wav"
    stop music
    scene w2_3439 with dissolve
    fel "See you soon!"
    scene w2_3440 with dissolve
    "Without so much of a goodbye, Felicia hung up."
    mc "Shit..."
    mct "(I hope everything is okay.)"

    if w2HanaSex == True:
        play sound "sound effects/door-slide.wav"
        scene w2_3441 with dissolve
        "The sound of the bathroom door opening. Hana had finished cleaning up."
        scene w2_3442 with dissolve
        mct "(Hopefully she'll under--)"
        play music "music/take-the-lead.ogg"
        scene w2_3443 with dissolve:
            subpixel True
            yalign 1.0
            xalign 0.6
            linear 6 yalign 0.25
        mc "Holy shit."
        "When she said she wanted to look her best..."
        mc "Holy. {b}SHIT{/b}."
        scene w2_3444 with dissolve
        hana "That's... uh..."
        scene w2_3445 with dissolve
        hana "The reaction I was hoping for."
        scene w2_3446 with dissolve
        mct "(I know I thought I hoped Mina was okay, but...)"
        "This better be serious."
        mc "You look great."
        scene w2_3447 with dissolve
        hana "No shit."
        scene w2_3448 with dissolve
        mc "You look great, but..."
        scene w2_3449 with dissolve
        hana "...but full stop, I just look great?"
        scene w2_3450 with dissolve
        hana "This isn't the \"but\" kind of situation."
        scene w2_3451 with dissolve
        mc "You look great, but I'm going to have to blue ball both of us."
        mc "Can I take a rain check on..."
        scene w2_3452 with dissolve
        mc "THAT."
        scene w2_3453 with dissolve
        hana "Explain."
        scene w2_3454 with dissolve
        hana "THIS is pretty embarassing, so it better be good."
        scene w2_3455 with dissolve
        mc "Mina's having a really bad time right now. I think Ian--"
        scene w2_3456 with dissolve
        hana "Say no more."
        scene w2_3457 with dissolve
        hana "I like twintails. She's awesome."
        hana "I'll drive you."
        scene w2_3458 with dissolve
        hana "Just let me..."
        stop music fadeout 3.0
        scene black with fade
        hana "Get dressed."
        "Damn it."
        "......"
        "..."
    else:
        scene w2_3459 with dissolve
        mc "Hey, could you give me a ride?"
        scene w2_3460 with dissolve
        hana "Yeah, sure. Not like I can refuse my gracious host. Where to?"
        scene w2_3459 with dissolve
        mc "Mina's having a really bad time. I think Ian--"
        scene w2_3461 with dissolve
        hana "Say no more."
        scene w2_3462 with dissolve
        hana "I like twintails. She's awesome. Let's go."
        "......"
        "..."

label w2MinaStart:
    if _in_replay:
        show screen textbox2 with dissolve
    play sound "sound effects/door-knock.wav"
    "*Knock, Knock*"
    stop sound
    scene w2_3463 with cmet
    play music "music/Moonlight-Sonata.ogg"
    fel "Thanks for coming."
    mc "It sounded serious."
    scene w2_3464 with dissolve
    fel "No, {b}really{/b}. Thanks."
    fel "Our girl doesn't have a lot of friends in the first place. You and I are the only ones close to the situation and I unfortunately can't stay as long as I should."
    scene w2_3465 with dissolve
    mc "You're leaving?"
    scene w2_3464 with dissolve
    fel "Don't give me that look. I'm not pawning her off on you or anything like that."
    scene w2_3466 with dissolve
    fel "I've got an annoying {i}thing{/i} tonight that I'm obligated to play homemaker for. Whole nine yards: doll myself up, oversee the dinner plans, psych myself up into pretending that I give a crap."
    scene w2_3467 with dissolve
    fel "Basic gold digger stuff."
    scene w2_3468 with dissolve

    if kat_polite == True:
        "Part of me wanted to give Felicia a heads up and ruin Mrs. Pulman's surprise, so she wouldn't be caught unaware, but this wasn't exactly the time and place to comfortably get into it."
    else:
        "Part of me wanted to give Felicia a heads up and ruin Kathleen's surprise, so she wouldn't be caught unaware, but this wasn't exactly the time and place to comfortably get into it."

    scene w2_3469 with dissolve
    mc "\"Basic\"? You should write a memoir. Okay, I get it."
    scene w2_3470 with dissolve
    mc "Where's Mina?"
    scene w2_3471 with dissolve
    fel "The princess is in her room."
    scene w2_3472 with dissolve
    mc "Sulking?"
    scene w2_3473 with dissolve
    fel "I think she's getting dressed. She got pretty miffed when I told her I called you."
    fel "I think she was worried about looking anything less than prim and proper."
    scene w2_3474 with dissolve
    fel "Which I get wanting to look good, but sometimes it's more advantageous to let a man see you with your nose runny and your hair down."
    scene w2_3472 with dissolve
    mc "Basic gold digger stuff?"
    scene w2_3471 with dissolve
    fel "Sorry, I can't turn it off. I'm not good at touchy-feely stuff, which is actually another reason I called you..."
    scene w2_3473 with dissolve
    fel "If I could stay, I'd fill her head with all sorts of bad advice. She doesn't need my warped view on things."
    scene w2_3472 with dissolve
    "Felicia clearly cared, but she was smart enough to recognize her limitations."
    mc "So, what's the situation?"
    scene w2_3471 with dissolve
    fel "What's the situation?"
    scene w2_3474 with dissolve
    fel "You have three guesses, but you only need one, stud."
    scene w2_3472 with dissolve
    mc "What did he do?"
    scene w2_3471 with dissolve
    fel "He {b}did{/b} a couple of \"things\", but it's better that I show you rather than explain."
    scene w2_3472 with dissolve
    mc "{b}Show{/b} me?"
    scene w2_3475 with dissolve
    fel "Uh huh. Nice of a man to video tape his fuck ups and leave it lying around to be found by his sweet, undeserving girlfriend."
    mc "Oh, no..."
    scene w2_3476 with dissolve
    fel "Oh, yeah. {b}Real{/b} considerate."
    fel "So, Mina found a random USB. I don't know why she decided to peek at what was on it, but..."
    scene ian_3some_a with pixellate
    show ian_3some
    hide screen textbox2 with dissolve
    alice "Oh, K-Killian...! This is t-too..."
    "Within the first second of the video, I instantly understood the entire situation."
    kil "No, no, no. {b}Mr. Beaufort{/b}, bitch."
    kil "Don't forget who you work for just because I was nice enough to clean out the cobwebs down there."
    "For Mina, it may have been one thing to know that Ian was sneaking around, but being faced with evidence..."
    alice "A-ah, y-you used to be s-so...!"
    "Not just any evidence at that, either. This wasn't just a damning text message or another woman's clothes carelessly forgotten, but video of her boyfriend balls deep in his menopausal housemaid."
    kil "Sweet? Bullshit. I've always wanted to fuck this fat ass--"
    scene w2_3477 with dissolve
    if not persistent.w2IanMaid3some:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w2IanMaid3some = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    show screen textbox2 with dissolve
    mc "Fuck."
    fel "You can say that again. You get the idea?"
    mc "Yeah, turn it off."
    $ renpy.end_replay()
    scene w2_3478 with dissolve
    mc "Uh... okay, I get why you called me here, but what am I going to do? I won't be much help, we haven't known each other for very long."
    scene w2_3479 with dissolve
    fel "Making sure she doesn't break all her glassware would be a good start. She's trending toward pissed more than anything else."
    scene w2_3480 with dissolve
    mc "...you sure she'll be comfortable with me here? The asshole is my close friend, remember?"
    stop music
    scene w2_3481 with dissolve
    mina "These walls are pretty thin, y'know."
    scene w2_3482 with dissolve
    mc "......"
    play music "music/called-upon.ogg"
    scene w2_3483 with dissolve
    mc "...hey."
    scene w2_3484 with dissolve
    mina "Hey, [mcf]."
    scene w2_3485 with dissolve
    mc "I guess you can answer my question then."
    scene w2_3486 with dissolve
    mina "Am I comfortable with you here? That depends. Did you know?"
    hide screen textbox2 with dissolve
    scene w2_3504 with dissolve

    menu w2MinaQuestion:
        "Tell the truth."(chg=["mina_up"]):
            $ Mina_Affection += 1
            scene w2_3487 with dissolve
            if w2MinaIanCover == True:
                scene w2_3487 with dissolve
                show screen textbox2 with dissolve
                mc "Sorry. I don't know why I tried to cover for him just now."
                scene w2_3497 with dissolve
                mina "I get it. I'm a child of divorce."
                mina "Avoid conflict, right?"
                scene w2_3498 with dissolve
                "I marveled how Mina managed to retain her sense of empathy even in a situation like this."
                scene w2_3499 with dissolve
                mc "Ah, maybe... I did know, though. He's not very \"secretive\" about it."
                mc "Sorry."
                scene w2_3489 with dissolve
                mina "Don't be. I knew too, in my own way. It's not like I can be angry at you when I was doing a bang up job making a fool of myself all on my own."
                scene w2_3490 with dissolve
                mina "If you want, I'd love for you to keep me company, [mcf]."
            else:

                scene w2_3487 with dissolve
                show screen textbox2 with dissolve
                mc "Yes, I did."
                mc "...sorry."
                scene w2_3488 with dissolve
                mina "Don't be. I knew in my own way and I didn't do anything about it. It's not like I can be angry at you when I was doing a bang up job making a fool of myself all on my own."
                scene w2_3489 with dissolve
                mina "Thanks for not lying about it right now, [mcf]."
                scene w2_3490 with dissolve
                mina "If you want, I'd love for you to keep me company."

        "Lie for Ian."(chg=["killian_up2","mina_down2"]) if w2MinaIanCover == False:
            $ Killian_Bromance += 2
            $ Mina_Affection -= 2
            $ w2MinaIanCover = True
            scene w2_3487 with dissolve
            show screen textbox2 with dissolve
            mc "Have you talked to him about it?"
            mc "Maybe the video's old? He's always liked to... film things."
            scene w2_3500 with dissolve
            mina "...it's not old. He was chatting with that purple haired {b}slut{/b} a few weeks ago at {i}Circus{/i} when me, you, and Felicia were there."
            scene w2_3501 with dissolve
            "Mina looked at me odd, as if she fully understood my deflection wasn't done out of a genuine interest of giving the benefit of the doubt."
            scene w2_3502 with dissolve
            "She looked vaguely hurt. How do I answer her original question?"
            hide screen textbox2 with dissolve
            jump w2MinaQuestion
        "Lie about your knowledge, tactfully."(chg=[("mina_down", w2MinaIanCover == True)]):


            scene w2_3487 with dissolve
            if w2MinaIanCover == True:
                $ Mina_Affection -= 1
                scene w2_3487 with dissolve
                show screen textbox2 with dissolve
                mc "I didn't know explicitly, but Ian's not exactly the monogamous type and he's not good at hiding things."
                scene w2_3502 with dissolve
                mina "..."
                "I could tell she didn't quite buy it."
            else:
                scene w2_3487 with dissolve
                show screen textbox2 with dissolve
                mc "Not explicitly, but..."
                mc "Well, I know Ian's not exactly the monogamous type."

            scene w2_3503 with dissolve
            mina "..."
            scene w2_3489 with dissolve
            mina "Yeah... I didn't know for sure either, but I... {i}knew{/i}."
            scene w2_3490 with dissolve
            mina "If you want, I wouldn't mind some company, [mcf]."

    scene w2_3491 with dissolve
    mina "As a friend though. I don't need a babysitter."
    fel "Oh, hun... that's not what this..."
    scene w2_3492 with dissolve
    fel "I mean..."
    fel "Yeah, you would see it that way."
    scene w2_3493 with dissolve
    mina "I appreciate the thought."
    scene w2_3494 with dissolve
    mc "No worries. I had enough babysitting at my last job."
    scene w2_3495 with dissolve
    mina "Good!"
    mina "Because, instead of that..."
    stop music
    play sound "sound effects/surprise.wav"
    scene w2_3496 with w19
    mina "I need to know: either of you want to star in a video?"
    jump w2MinaRevealContinued
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
