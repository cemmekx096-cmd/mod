label June13Start:
    if met_sophia == False:
        $ met_sophia = True

    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transition_carnations with blinds
    $ renpy.pause(6, hard=True)
    $ date = "june13day"
    $ renpy.music.set_volume(.2, 0, channel = "ambient")
    play ambient "sound effects/chatter-low.wav"
    scene w2_5689 with fade
    show screen qmenu with dissolve
    ver "--don't you think it's wildly unfair only one of us is compensated?"
    scene w2_5690 with dissolve
    rose "Isn't that the point? They're paying to see our desperation."
    scene w2_5691 with dissolve
    show screen textbox2 with dissolve
    ver "{i}Our{/i} desperation...?"
    scene w2_5692 with dissolve
    fel "...don't look at me, bitch. You agreed to the terms."
    scene w2_5693 with dissolve
    ver "I did, but all I'm saying is, if we really help bring in as much money as [mcf] says... don't you think we have a hefty fucking bargaining chip?"
    ver "We could threaten not to perform to--"
    scene w2_5694 with dissolve
    fel "Let me stop you there. That's a bad idea - {b}a really stupid and bad idea{/b}."
    scene w2_5695 with dissolve
    rose "Yeah, I agree with Felicia, I don't want to jeopardize my chances of clearing my debt. Besides, I don't think we have as much negotiating power as you think..."
    scene w2_5696 with dissolve
    ver "Don't we?"
    play sound "sound effects/ice-glass.wav"
    scene w2_5697 with dissolve
    "*Clank*"
    scene w2_5698 with dissolve
    fel "You're not as dumb as you look, right? Don't you have a read on the kind of place it is?"
    fel "The kind of people who run the place? The kind of people who are paying to watch?"
    scene w2_5699 with dissolve
    ver "Yeah, they're rich assholes, which means they can afford to--"
    scene w2_5700 with dissolve
    fel "They're not the kind of people you jerk around. Christ, imagine agreeing to participate without understanding that."
    stop ambient fadeout 3.0
    scene w2_5701 with dissolve
    ver "You can only say that because of the stupid-ass reason you--!"
    play music "music/jazz-apricot.ogg"
    scene w2_5702 with dissolve
    show june13day with squares
    mc "Sorry I'm late. I wasn't expecting you to change where we ate..."
    ver "--ah, herm..."
    scene w2_5703 with dissolve
    $ renpy.music.set_volume(1, 0, channel = "ambient")
    ver "Well... you did say you wanted to treat us."
    scene w2_5704 with dissolve
    ver "...and after all the parading you had us do this week, I wouldn't call that crappy diner a treat. This place isn't too expensive for you, right?"
    mc "I wasn't complaining. At the very least, you guys do deserve a good hot meal before tonight."
    scene w2_5705 with dissolve
    mc "What were you three talking about when I came in? It looked anima--"
    scene w2_5706 with dissolve
    carnations "{b}Nothing{/b}."
    scene w2_5707 with dissolve
    mc "I see..."
    mct "(...not suspicious in the least.)"
    scene w2_5708 with dissolve
    mc "Fine, keep your secrets."
    scene w2_5709 with dissolve
    rose "It was just girl talk--"
    scene w2_5710 with dissolve
    fel "...{b}Carnation{/b} talk. Strategizing, I guess."
    scene w2_5711 with dissolve
    mc "Hmm, well I'm glad. That's better than being sick with worry."
    mc "How are you each doing today?"
    scene w2_5712 with dissolve
    rose "Alright--"
    ver "As good as can be expect--"
    scene w2_5713 with dissolve
    fel "Looking forward to tonight."
    scene w2_5714 with dissolve
    ver "Looking for--?"
    scene w2_5715 with dissolve
    rose "... er, how are you, [mcf]?"
    scene w2_5716 with dissolve
    mc "I'm both alright and as good as can be expected."
    mc "I mainly can't believe it's only been a week. These past seven days felt much longer."
    mct "({b}So, so much longer.{/b})"
    scene w2_5717 with dissolve
    rose "Tell me about it..."
    fel "I wonder what Kat's got cooked up."
    ver "Yeah, {i}humiliation{/i}... it's a pretty open-ended shitshow, huh?"
    scene w2_5718 with dissolve
    mc "Do you guys actually want to think about that before we eat?"
    rose "There's no running away from it."
    ver "Rose is right. It's better to mentally steel yourself."
    scene w2_5719 with dissolve
    rose "You don't have any clue about what we can expect do you?"
    mc "Same answer as last week: I'm equally in the dark as you."
    scene w2_5720 with dissolve
    fel "Heh. Maybe she'll have us crawl around on all fours like an animal?"
    "Felicia shot Veronica a knowing look. The conversation they had before I arrived was evidently quite open..."
    scene w2_5721 with dissolve
    ver "Shut it, pig."
    mct "(I guess, in a way, they're starting to have a fucked-up sense of camaraderie...)"
    scene w2_5722 with dissolve
    rose "I doubt it will be that basic..."
    scene w2_5723 with dissolve
    fel "If you think about it, for most people, just having sex in front of a crowd is humiliating in and of itself. Yet, that's the baseline here..."
    fel "I reckon she'll get pretty damn personal with it."
    scene w2_5724 with dissolve
    mc "This is a {b}show{/b} foremost, with an audience and all that jazz. It'll be something the club patrons will easily understand and want to see."
    scene w2_5725 with dissolve
    ver "Oh! The whole thing would be a flop if that old bitch didn't get the reaction she wanted out of us, wouldn't it?"
    rose "I want to win, Veronica, not screw with that woman's twisted fun."
    scene w2_5726 with dissolve
    ver "I know, but it's stimulating to imagine."
    mct "(Anyone overhearing this conversation must be confused as fuck right now...)"
    scene w2_5727 with dissolve
    "Well, the four of us are an odd combination to begin with."
    scene w2_5728 with dissolve
    waitress "You ready to order?"
    fel "Yep!"
    scene black with fade
    stop music fadeout 3.0
    waitress "What are you having?"
    "So we did indeed have what I hoped: a nice, hot meal before tonight."
    "......"
    "..."
    play music "music/thief-in-the-night.ogg"
    scene w2_5729 with circlewipe
    ver "Ah, I'm stuffed...!"
    rose "I don't think it was such a good idea to eat that much. Especially before..."
    scene w2_5730 with dissolve
    fel "Before our \"workout\" tonight, you mean?"
    scene w2_5731 with dissolve
    rose "Y-yeah..."
    scene w2_5732 with dissolve
    fel "Well, some men love to see a girl fighting back her lunch, y'know?"
    scene w2_5733 with dissolve
    rose "Geh, gross."
    scene w2_5734 with dissolve
    fel "Let me out. I'm going to go smoke."
    scene w2_5735 with dissolve
    fel "Any of you want to join me?"
    rose "No thanks, I don't smoke."
    mc "Me either."
    scene w2_5736 with dissolve
    fel "What about you, Red?"
    scene w2_5737 with dissolve
    ver "That's a joke, right? You think I'd poison my body like that?"
    scene w2_5738 with dissolve
    fel "I figured maybe you'd like some fresh air?"
    scene w2_5739 with dissolve
    ver "The air in here suits me fine."
    scene w2_5740 with dissolve
    fel "...s'alright."
    scene w2_5741 with dissolve
    ver "......"
    rose "..."
    scene w2_5742 with dissolve
    ver "So... how's your daughter doing, Rose?"
    scene w2_5743 with dissolve
    rose "I actually sent her to this nice summer camp."
    scene w2_5742 with dissolve
    ver "Yeah, because of...?"
    scene w2_5743 with dissolve
    rose "Uh huh. She doesn't need to see [mcf] coming or going and I don't need to fake my moods or hide where I go every Saturday."
    scene w2_5742 with dissolve
    ver "That's... smart and reasonable."
    scene w2_5744 with dissolve
    rose "It's sucky is what it is. I'm not lying, but... I hate feeling like I'm hiding things from my daughter."
    scene w2_5745 with dissolve
    mc "That's part of being a parent, right? Children don't really understand adult problems sometimes, nor should they."
    scene w2_5746 with dissolve
    ver "What would you know about that?"
    scene w2_5747 with dissolve
    mc "Conjecture, I guess."
    scene w2_5748 with dissolve
    rose "...[mcf]'s right, but it still sucks."
    rose "She's old enough to understand her father is... well, you know. The specifics though..."
    scene w2_5749 with dissolve
    ver "That's some real shit."
    scene w2_5750 with dissolve
    rose "Heh...! You have a talent for not knowing how to put things, Veronica."
    scene w2_5751 with dissolve
    ver "Ah... well..."
    scene w2_5752 with dissolve
    ver "I hope your daughter has a good time."
    scene w2_5753 with dissolve
    rose "Me too, despite whatever happens at the end of this month..."
    scene w2_5754 with dissolve
    ver "Yeah..."
    scene w2_5755 with dissolve
    rose "Excuse me... nature calls."
    scene w2_5756 with dissolve
    "Rosalind zipped away from the table, leaving me and the statuesque redhead awkwardly alone."
    scene w2_5757 with dissolve
    mc "I'm glad you picked this place, it's pretty ni--"
    scene w2_5758 with dissolve
    ver "Rose has a lot riding on her shoulders, huh?"
    scene w2_5759 with dissolve
    mc "You all do."
    scene w2_5764 with dissolve
    ver "Not in the same way."
    scene w2_5763 with dissolve
    mc "You having doubts?"
    scene w2_5764 with dissolve
    ver "No, it's just... she must look at me the same way I look at Blondie."
    scene w2_5762 with dissolve
    mct "(Does that bother her...?)"
    "All she was saying was true, but..."
    hide screen textbox2 with dissolve

    menu:
        "Agree with her."(chg=["tough_up"]):
            $ toughness +=1
            scene w2_5763 with dissolve
            show screen textbox2 with dissolve
            mc "Well, you're not wrong. Her situation is pretty fucked."
            scene w2_5761 with dissolve
            "No sense in sugar-coating what she already realizes."
            scene w2_5759 with dissolve
            mc "That gym may be a dream of yours, but she has her whole livelihood and a child to worry about."
            scene w2_5761 with dissolve
            ver "......"
            ver "..."
        "Offer some validation."(chg=["veronica_up"]):

            $ Veronica_Affection += 1
            scene w2_5763 with dissolve
            show screen textbox2 with dissolve
            mc "Well, everyone's got problems and they all seem more important to the one who shoulders them."
            mc "You're fighting for your livelihood too, right?"
            scene w2_5760 with dissolve
            ver "I am, but... I mean..."
            ver "It doesn't mean I don't feel sorry for her. What's worse...?"

    scene w2_5765 with dissolve
    ver "I still want to win. So very, {i}very{/i} badly."
    ver "I refuse to be a {b}loser{/b}."
    scene w2_5761 with dissolve
    "The emphasis on that last word made it sound vulgar. "
    scene w2_5760 with dissolve
    ver "...and I kinda fuckin' hate that I feel that way."
    scene w2_5761 with dissolve
    "Veronica overwrought with guilt was a look I was unfamiliar with."
    scene w2_5766 with dissolve
    fel "This damn city, I swear...!"
    scene w2_5767 with dissolve
    mc "That was fast."
    scene w2_5768 with dissolve
    fel "Some ass got on me for smoking in front of the building."
    fel "Where do they expect me to do it, in the middle of the street?"
    scene w2_5769 with dissolve
    ver "You should seriously consider quitting."
    scene w2_5770 with dissolve
    fel "That your advice as a professional?"
    scene w2_5769 with dissolve
    ver "That's just common sense. It's a filthy, harmful habit."
    scene w2_5771 with dissolve
    fel "Eh. I only do it after a big meal or a \"good\" time."
    scene w2_5772 with dissolve
    fel "Speaking of bad habits... I think I have room for dessert. Maybe a hot fudge brownie with ice cream..."
    scene w2_5773 with dissolve
    ver "Don't you watch what you eat? I mean, I know you do just by looking at you..."
    scene w2_5774 with dissolve
    fel "Doesn't hurt to splurge once in a while. Today I'm not going to think about a damn thing, but enjoying myself."
    scene w2_5775 with dissolve
    fel "Waitress!"

    if kat_polite == True:
        "I had gradually come to understand the most important quality Mrs. Pulman looked for in a Carnation."
    else:
        "I had gradually come to understand the most important quality Kathleen looked for in a Carnation."

    stop music fadeout 3.0
    scene black with fade
    "Single-mindedness - each and every one of them."
    "......"
    "..."
    play music "music/devious-little-smile.ogg"
    scene w2_5776 with blinds
    mc "You didn't have to volunteer to give me a ride."
    rose "I know, but anything to eat up the time between now and tonight I guess. What am I going to do, go home and watch TV? Too many butterflies to just sit on my keister."
    mc "It's just a ten-minute drive. You'll still have a lot of time on your hands."
    scene w2_5777 with dissolve
    rose "Well, I also wanted to speak to you."
    mc "Privately? About what?"
    rose "About Oliver and your help."

    if rosalindFelSolution == True:
        scene w2_5778 with dissolve
        mc "He's not still hassling you, is he? I transferred the money this morning."
        scene w2_5779 with dissolve
        rose "No, he... he was very surprised to receive it. He had a lot of questions, but I didn't explain it to him."
        scene w2_5778 with dissolve
        mc "That's good news, so what's there to talk about then?"
        scene w2_5782 with dissolve
        rose "I know you say it's part of your job, but I wanted to thank you in person for getting me the money. I said it on the phone, but, well..."
        scene w2_5780 with dissolve
        rose "...gratitude should be shown face-to-face. That's one of the very few things my mother taught me that I still agree with."
        scene w2_5784 with dissolve
        mc "You're welcome, Rose."
        mct "(I didn't really do anything and it's not like it's my money...)"
        scene w2_5781 with dissolve
        rose "I should've thanked Felicia for the money as well, like you told me to, but I couldn't bring myself to do it."
        scene w2_5783 with dissolve
        mc "Is it because of Veronica being there?"
        scene w2_5789 with dissolve
        rose "Partly, but I also just can't understand why she would help me. What is she trying to pull, [mcf]?"
        scene w2_5790 with dissolve
        mc "I wouldn't read too much into it. She wears clothes that cost more than what she gave you."
        mc "Heh. Doesn't that just boil your blood?"
        scene w2_5781 with dissolve
        rose "When you put it that way, it does sort of tee me off. Still..."
        scene w2_5783 with dissolve
        mc "Seriously though, she's capricious and she did it for me as a favor. She isn't trying to pull wool over your eyes."
        mc "I mean I probably could've got the club to pay it, but accepting a handout from an overprivileged whacko seemed like the most painless solution for you. Am I wrong?"
        scene w2_5785 with dissolve
        rose "...mmmh, but I still feel like that bitch is trying to mind game me."
        scene w2_5786 with dissolve
        mc "Ha! I'll be damned!"
        scene w2_5781 with dissolve
        rose "...what?"
        scene w2_5783 with dissolve
        "Naturally, Rosalind was suspicious of her opponent. I might be too if I were in her position, but I knew for a fact what motivated her generosity."
        mc "I've never heard you so catty before."
        scene w2_5786 with dissolve
        mct "(What I was suspicious of was what Felicia was angling for by paying me for my company.)"
        mc "Seriously. Don't overthink it."
        scene w2_5787 with dissolve
        rose "How could I not?"
        scene w2_5788 with dissolve
        mc "Understanding that woman is an exercise in futility. She's a black hole of common sense."
        mc "So, just thank her if you want, but honestly I don't think she expects you to."
        scene w2_5793 with dissolve
        rose "No... I should. It's the right thing to do."
        scene w2_5795 with dissolve
        mc "The \"right thing\", huh?"
        scene w2_5794 with dissolve
        "That was a funny thing to be worried about while prostituting yourself in a bizarre series of sex games."

    if rosalindKatSolution == True:
        scene w2_5778 with dissolve
        mc "He's not still hassling you, is he?"
        scene w2_5782 with dissolve
        rose "No, Mrs. Pulman transferred the money directly into my bank account last night, which I then used to pay off the interest this morning. Oliver was surprised to receive it."
        scene w2_5779 with dissolve
        rose "He had a lot of questions, but none that I cared to answer."
        scene w2_5778 with dissolve
        mc "If it's settled, then what is there to talk about?"
        scene w2_5789 with dissolve
        rose "I guess I should say thank you in person for getting me the money, even if you say it's part of your job."
        scene w2_5779 with dissolve
        rose "...and gratitude should be shown face-to-face. That's one of the very few things my mother taught me that I still agree with."
        scene w2_5778 with dissolve
        mc "It didn't exactly come without strings, Rose. You {b}shouldn't{/b} thank me."
        mct "(Not in the least...)"
        scene w2_5781 with dissolve
        rose "I know, but it keeps the motor running, right?"
        scene w2_5778 with dissolve
        "It was a sad thought that she might clear her debt, but not escape that place, but what can I do?"
        mct "(She agreed to it.)"
        mc "Do you know what you'll have to do to pay it back or for how long you'll have to do it?"
        scene w2_5785 with dissolve
        rose "Mrs. Pulman said we'll talk about it at the end of the month, but you and I both know what she expects."
        scene w2_5783 with dissolve
        "Yeah, of course I knew. The first part of my question was a formality. It was the latter part I was actually curious about."
        scene w2_5782 with dissolve
        rose "I thought maybe I could start working it off this month, while I have all this free time, but she said Carnations aren't on the \"ordinary\" menu - whatever the hell that means."
        scene w2_5783 with dissolve
        "A house girl probably pulls in $5000 in a few nights, but I imagine it wouldn't be that simple of a transaction."
        mc "If I had to guess, I think she's worried the allure of her show would be compromised if you started boning old fucks not even halfway through the month."
        mc "Plus, you'll be more valuable as a prostitute AFTER the Exhibition is over."
        scene w2_5785 with dissolve
        rose "Huh, prostitute...?"
        scene w2_5786 with dissolve
        mc "You did say you and I both know what she expects, right?"
        scene w2_5785 with dissolve
        rose "Yeah, but just speaking the word aloud makes it..."
        scene w2_5796 with dissolve
        rose "It makes me want to puke."


    if rosalindKatSolutionFree == True:
        scene w2_5778 with dissolve
        mc "He's not still hassling you, is he?"
        scene w2_5779 with dissolve
        rose "No, Mrs. Pulman transferred the money directly into my bank account last night, which I then used to pay off my interest this morning. Oliver was surprised to receive it."
        rose "He had a lot of questions, but none of them I cared to answer."
        scene w2_5778 with dissolve
        mc "If it's settled, what is there to talk about?"
        scene w2_5782 with dissolve
        rose "I know you say it's part of your job, but I wanted to thank you in person. I said it on the phone, but, well..."
        scene w2_5780 with dissolve
        rose "...gratitude should be shown face-to-face. That's one of the very few things my mother taught me that I still agree with."
        scene w2_5784 with dissolve
        mc "You're welcome, Rose."
        mct "(It wasn't like it was my money. I just asked someone else to foot the bill...)"
        mc "So you're squared away until after the Exhibition ends, correct?"
        scene w2_5780 with dissolve
        rose "Yeah. With any luck, I won't see that bastard's face for the rest of the month."
        scene w2_5782 with dissolve
        rose "With even more luck, I'll only see him one more time..."
        scene w2_5778 with dissolve
        mc "How did your husband meet that bottom feeder?"
        scene w2_5781 with dissolve
        rose "How does anyone meet a loan shark? I honestly don't know, but he did."
        rose "He liked to gamble and he always had some big idea to make money. He was ambitious, but he didn't have the talent or means."
        scene w2_5785 with dissolve
        rose "*Scoff* Bastard..."
        scene w2_5786 with dissolve
        mc "Sorry for asking."
        scene w2_5781 with dissolve
        rose "No, it's fine. It's just funny how people say, \"he's not the man I married\". Me? I think he was always that way; it just took a long time for the picture to develop."
        scene w2_5783 with dissolve
        mc "You... never know what kind of person you're dealing with or who you're looking at until circumstances unveil another piece of the puzzle."
        mc "Sometimes it takes a whole lifetime to learn an uncomfortable truth about yourself or those you love."
        scene w2_5791 with dissolve
        rose "...half a lifetime? You're in your early twenties, kid."
        scene w2_5792 with dissolve
        mc "That I am. I got a whole lot left to learn about myself."
        scene w2_5781 with dissolve
        rose "Heh, you're right, though..."
        rose "Never in my life would I have imagined I'd have what it took to be a..."
        scene w2_5786 with dissolve
        "She paused, as if hoping the uncomfortable word would speak itself."
        scene w2_5785 with dissolve
        rose "I would have never imagined I'd have what it takes to be a {b}prostitute{/b}."
        scene w2_5786 with dissolve
        mc "Technically, you haven't been paid for anything yet, right? It's only if you win..."
        scene w2_5796 with dissolve
        rose "Ha... that's an even more depressing thought!"

    if rosalindAugSolution == True:
        scene w2_5778 with dissolve
        mc "He's not still hassling you, is he?"
        scene w2_5789 with dissolve
        rose "I don't know. He didn't drop by this morning... which is unusual. I figured it had something to do with the club paying what I owed?"
        scene w2_5790 with dissolve
        mc "Something like that."
        "More specifically, didn't pay anything. He said he'd simply ask her loan shark to back off, but there was no point in clarifying that distinction."
        mc "Mr. Byrnes said he'd take care of it directly."
        scene w2_5789 with dissolve
        rose "I see..."
        scene w2_5778 with dissolve
        mc "Is that what you wanted to talk about?"
        scene w2_5782 with dissolve
        rose "Partly, but I also wanted to express my gratitude face-to-face. I said it on the phone, but, well..."
        scene w2_5780 with dissolve
        rose "...gratitude should be shown face-to-face. That's one of the very few things my mother taught me that I still agree with."
        scene w2_5784 with dissolve
        mc "You're welcome, Rose."
        mct "(I didn't really do anything. Just talked to someone...)"
        mc "You should be squared away until after the Exhibition ends I think."
        scene w2_5780 with dissolve
        rose "With any luck, I won't see that bastard's face for the rest of the month."
        scene w2_5782 with dissolve
        rose "With even more luck, I'll only see it one more time..."
        scene w2_5778 with dissolve
        mc "How did your husband meet that bottom feeder?"
        scene w2_5781 with dissolve
        rose "How does anyone meet a money lender? I honestly don't know, but he did."
        rose "He liked to gamble and he always had some big idea to make money. He was ambitious, but he didn't have the talent or means."
        scene w2_5785 with dissolve
        rose "*Scoff* Bastard..."
        scene w2_5786 with dissolve
        mc "Sorry for asking."
        scene w2_5781 with dissolve
        rose "No, it's fine. It's just funny how people say, \"he's not the man I married\". Me? I think he was always that way it just took a long time for the picture to develop."
        scene w2_5783 with dissolve
        mc "You... never know what kind of person you're dealing with or who you're looking at until circumstances unveil another piece of the puzzle."
        mc "Sometimes it takes a whole lifetime to learn an uncomfortable truth about yourself or those you love."
        scene w2_5791 with dissolve
        rose "...half a lifetime? You're in your early twenties, kid."
        scene w2_5792 with dissolve
        mc "That I am. I got a whole lot left to learn about myself."
        scene w2_5781 with dissolve
        rose "Heh, you're right, though..."
        rose "Never in my life would I have imagined I'd have what it took to be a..."
        scene w2_5786 with dissolve
        "She paused, as if hoping the uncomfortable word would speak itself."
        scene w2_5785 with dissolve
        rose "I would have never imagined I'd have what it takes to be a {b}prostitute{/b}."
        scene w2_5786 with dissolve
        mc "Technically, you haven't been paid for anything yet."
        scene w2_5796 with dissolve
        rose "Ha... that's an even more depressing thought!"

    if rosalindKilSolution == True:
        scene w2_5778 with dissolve
        mc "Ah, right... I should tell Ian you agreed and get him to send you the money."
        scene w2_5779 with dissolve
        rose "No need. He already did."
        scene w2_5778 with dissolve
        mc "Really? I figured he would forget about it just as soon as he walked out of the dressing room."
        scene w2_5781 with dissolve
        rose "Dressing room?"
        scene w2_5778 with dissolve
        mc "Ah, um... nevermind that, just an {b}unusual{/b} arena for a game of Go. So you're squared away with that bottom feeder?"
        scene w2_5789 with dissolve
        rose "I am. Mr. Beaufort got in touch last night and wired me the money... he sounded excited."
        scene w2_5790 with dissolve
        mc "Yeah, he's uh... weird like that."
        scene w2_5781 with dissolve
        rose "Oliver was surprised to receive it. Had a lot of questions, but none that I answered."
        scene w2_5778 with dissolve
        mc "If that's taken care of, what did you want to talk about then?"
        scene w2_5782 with dissolve
        rose "I know you say it's part of your job, but I wanted to thank you in person. I said it on the phone, but, well..."
        scene w2_5779 with dissolve
        rose "...gratitude should be shown face-to-face. That's one of the very few things my mother taught me that I still agree with."
        scene w2_5778 with dissolve
        mc "You're welcome, Rose."
        mct "(Thanking me for an impending spit-roast, that's a new one...)"
        mc "Although, you really don't need to, considering the strings attached..."
        mc "For the record, the whole threesome thing wasn't my idea - not that I'm opposed, but--"
        scene w2_5781 with dissolve
        rose "Quite frankly. [mcf], I don't really give a crap whose idea it was. It's a better going rate than I'm currently getting, y'know?"
        scene w2_5778 with dissolve
        mc "You're not actually being paid anything as of yet."
        scene w2_5785 with dissolve
        rose "Yeah... that was the depressing point I'm trying to make."
        rose "I'm a prostitute that hasn't been paid."
        scene w2_5786 with dissolve
        mc "Yeah, it's not really a system in your favor. You girls should form a union."
        scene w2_5782 with dissolve
        rose "Funny you should say that..."
        scene w2_5778 with dissolve
        mc "What?"
        scene w2_5781 with dissolve
        rose "Uh, nothing... Veronica made the same joke."
        scene w2_5790 with dissolve
        "......"
        scene w2_5792 with dissolve
        "..."
        scene w2_5791 with dissolve
        rose "{b}For the record{/b}, it wasn't your idea, but you're also going along with it."
        scene w2_5792 with dissolve
        mc "Hey! It was his only condition and I wanted to help you..."
        "Her smug smile told me she saw right through me."
        scene w2_5797 with dissolve
        rose "Pft-!"
        mc "Okay, fine. It wasn't a hard sell."

    "......"
    "...."
    scene w2_5798 with dissolve
    rose "Should we get going...?"
    scene w2_5795 with dissolve
    mc "In a hurry to sit on your \"keister\", are you?"
    scene w2_5796 with dissolve
    rose "Don't joke. I don't know what to do with my time anymore. It's like I'm in a weird liminal state this month."
    scene w2_5794 with dissolve
    hide screen textbox2 with dissolve

    if roseFlag == True:
        $ mod_var = False
        mct "(Well, if she's looking for things to do...)"
        menu w2PreExhibitionSplit:
            "[mod_option] Both" if Rosalind_Affection >= 25 and roseDealFullAcceptance:
                $ Rosalind_Affection += 3
                $ mod_var = True
                $ w2RoseMomMet = True
                jump mod_w2PreExhibitionSplit_1
            "{color=#696969}[mod_option] Both (requires: accepted Full deal and Rose affecttion 25 or more{/color}" if Rosalind_Affection <= 24 or not roseDealFullAcceptance:
                jump w2PreExhibitionSplit
            "{color=#FF1493}[[Affection]{/color} Kill some time together at your apartment.(if rosalind affection>=25)"(chg=["rosalind_up3"]) if Rosalind_Affection >= 25:
                $ Rosalind_Affection += 3
                $ w2RoseMomMet = True
                label mod_w2PreExhibitionSplit_2:
                scene w2_5800 with dissolve
                show screen textbox2 with dissolve
                mc "If you're just sitting on your hands with nothing to do, then why don't we kill time together?"
                scene w2_5801 with dissolve
                mc "Come back to my place and we'll watch a movie."
                scene w2_5802 with dissolve
                rose "[mcf]... if you want to screw, you can just say it. You don't need a pretense."
                scene w2_5803 with dissolve
                "The offer had me take stock of her body, my eyes flicking all the way down her tightly packed sweater puppies and stopping at her long, bare legs."
                "It was an appetizing thought, but..."
                scene w2_5801 with dissolve
                mc "I don't think that's wise. You should save your energy for tonight."

                if kat_polite == True:
                    "Honestly, the same advice applies to me if Mrs. Pulman has me take the stage again..."
                else:
                    "Honestly, the same advice applies to me if Kathleen has me take the stage again..."

                mct "(...wait, am I just like a discount Carnation?)"
                scene w2_5802 with dissolve
                rose "So... you mean {i}actually{/i} watch a movie then? You just want to hang out with a thirty-six year old woman?"
                scene w2_5801 with dissolve
                mc "I was just going to go home and nap otherwise. You're the one talking about how you have nothing to do."
                scene w2_5804 with dissolve
                "She looked at me like I was strange."
                scene w2_5805 with dissolve
                mc "C'mon, it'll occupy your mind for a couple of hours."
                scene w2_5806 with dissolve
                rose "Okay, but can we do something other than watch a movie? Sitting and staring at a screen will just fill my head with other unwanted thoughts."
                scene w2_5801 with dissolve
                mc "Alright, then. I'm sure we can figure something for two people to do that's not watching a movie or sex."
                stop music fadeout 3.0
                scene black with fade
                "......"
                "..."
                jump w2PreExhibitionRose


            "{color=#FF1493}[[Full Deal]{/color} ??????" if roseDealFullAcceptance == True:
                label mod_w2PreExhibitionSplit_1:
                scene w2_5939 with dissolve
                show screen textbox2 with dissolve
                mc "If you're so bored..."
                scene w2_5940 with dissolve
                "My eyes flickered down her body, starting from her luscious lips and tracking all the way down her smooth bare legs."
                scene w2_5939 with dissolve
                mc "We could find something that will eat up your time."
                scene w2_5941 with dissolve
                "I could tell by the way she blushed that my pervy expression hadn't gone unnoticed."
                scene w2_5942 with dissolve
                rose "You want to... screw, then?"
                scene w2_5941 with dissolve
                "The way she carefully picked out what word to use was cute."
                scene w2_5943 with dissolve
                mc "We shouldn't. It's going to be a long night and you should conserve your energy."
                scene w2_5941 with dissolve
                mct "(Gee, what a good employee I am...)"
                scene w2_5942 with dissolve
                rose "Then what's with {i}that{/i} look?"
                scene w2_5944 with dissolve
                "{i}That look{/i} was..."
                scene w2_5945 with dissolve
                "It was hard to reconcile wanting the best for Rosalind with the black desire that bubbled its way to the surface when I thought about her willingness to do whatever I wanted."
                "One moment we were talking about easing her burdens and the next my hand lecherously drew up her dress, finding perch on her hip."
                "{b}That look{/b} was everything I wanted to do despite myself."
                scene w2_5946 with dissolve
                mc "I don't know. I'm thinking..."
                scene w2_5947 with dissolve
                rose "About what?"
                scene w2_5946 with dissolve
                mc "About why I'm grabbing you like this all of a sudden, even though we aren't going to do anything."
                scene w2_5948 with dissolve
                rose "Oh..."
                "Naturally, she didn't have a response to my bizarre answer."
                scene w2_5949 with dissolve
                rose "I mean... I don't mind."
                scene w2_5950 with dissolve
                mc "Is that all it takes? Is the knowledge you won't push me away all it takes to turn me into a hypocrite?"
                scene w2_5951 with dissolve
                "Her big blue eyes affixed me with a steely unflinching gaze."
                scene w2_5952 with dissolve
                rose "A principled man would be of no help to me, [mcf]."
                scene w2_5953 with dissolve
                mc "You...!"
                scene w2_5954 with dissolve
                "She didn't try to pretend I wasn't scum, like I secretly hoped."
                mct "(It wasn't her job to make me feel any less like a piece of crap.)"
                hide screen textbox2 with dissolve

                menu:
                    "Maybe you should have her take you home.":
                        scene w2_6013 with dissolve
                        show screen textbox2 with dissolve
                        mc "Ha, you're right. Let's go and get some rest."
                        rose "...you're not mad, are you? I didn't mean to imply you were--"
                        scene w2_6014 with dissolve
                        mc "Quite the contrary, I'm grateful for the reality check."
                        "I smiled reassuringly, as to not erroneously worry Rosalind that our deal might be in jeopardy over a spat of cognitive dissonance on my part."
                        scene w2_6015 with dissolve
                        rose "...seriously, put your hand back where it was. I was just being... uh, glib?"
                        scene w2_6016 with dissolve
                        mc "Let's just think about tonight, Rose. You've got to not only survive, but win."
                        mc "{b}You're going to win{/b}."
                        scene w2_6017 with dissolve
                        rose "...damn it, you're so weird. One moment you're like a lecherous old man and the next you're like... {b}this{/b}?"
                        scene w2_6018 with dissolve
                        mc "I mean, I've got to figure out how I might help you, right? There's two sides to this."
                        mc "Or would you prefer... \"I'll fuck your brains out some other time, whore\" to make you more comfortable?"
                        scene w2_6019 with dissolve
                        rose "Heh, you know what's fucked up? The latter is actually more reassuring to me."
                        scene black with fade
                        if mod_var:
                            $ mod_var = False
                            m_dev "Mod Option jump to other choice"
                            jump mod_w2PreExhibitionSplit_2
                        rose "Fine. Go take your nap."
                        "......"
                        "..."
                        stop music fadeout 3.0
                        jump w2PreExhibitionSolo
                    "Show her a glimpse of your true colors."(chg=["rosalind_down2","rosalind_passion_up"]):

                        $ Rosalind_Affection -= 2
                        $ Rosalind_Libido += 1
                        stop music fadeout 2.0
                        scene w2_5953 with dissolve
                        mc "So that's what you've been counting on from the very beginning? Me being an asshole?"
                        scene w2_5952 with dissolve
                        rose "I wouldn't put it that way... you're just young."
                        rose "Still, you haven't actually called on me to uh... {i}pleasure you{/i} yet. Seriously, think of me as a sex toy... just keep your side of the--"
                        play music "music/leaving-home.ogg"
                        scene w2_5955 with dissolve
                        rose "Ah--! W-what...?"
                        mc "...what I want?"
                        mc "Grabbing your throat like this..."
                        scene w2_5956 with dissolve
                        rose "Mmmh...!"
                        scene w2_5957 with dissolve
                        mct "(Was just the tip of the iceberg.)"
                        scene w2_5956 with dissolve
                        "When I roughly pressed my lips to hers, she {b}embraced me{/b}. It was frustrating that even now she didn't react the way I hoped."
                        scene w2_5959 with dissolve
                        rose "You... can squeeze harder if you'd like."
                        scene w2_5958 with dissolve
                        "Her reaction was unexpected, but what expectations did I have from grabbing her like this?"
                        scene w2_5959 with dissolve
                        rose "If you want to get rough, I'll welcome it. Just remember: {b}help me{/b}. None of this half-assed crap of \"doing what you can\", either. Find a damn way to help me win."
                        scene w2_5958 with dissolve
                        "......"
                        "..."

                        menu:
                            "Finally, have her take you home."(chg=["rosalind_up"]):
                                $ Rosalind_Affection += 1
                                stop music fadeout 3.0
                                scene w2_6020 with dissolve
                                show screen textbox2 with dissolve
                                mc "Ah, fuck..."
                                rose "W-what's the matter? I didn't mean to say anything wrong?"
                                scene w2_6021 with dissolve
                                mc "That's the first thought on your mind, huh? You're a fucking machine, Rose."
                                mc "Suppose you got to be."
                                scene w2_6013 with dissolve
                                rose "I don't know how to take that."
                                mc "Let's go home and get some rest."
                                rose "Eh, but you were just...?"
                                scene w2_6022 with dissolve
                                rose "I don't mind you putting your hand on my throat, hun. It just adds a little spice, right? I know you would never take it too--"
                                scene w2_6023 with dissolve
                                mc "You don't know shit, Rose. You've got a lot of assumptions that I hope are true."
                                scene w2_6024 with dissolve
                                rose "Jeez, you're weirdly temperamental. Really, I'm sorry if I did anything wrong. I was just being glib."
                                scene w2_6025 with dissolve
                                mc "Don't worry about crap that doesn't matter."
                                "I smiled reassuringly, so not to worry Rosalind that our deal might be in jeopardy over a spat of cognitive dissonance on my part."
                                mc "Focus on winning tonight and I'll focus on my end of our arrangement. That's my request for you, okay?"
                                scene w2_6026 with dissolve
                                rose "...ah, you really are so weird."
                                scene w2_6027 with dissolve
                                mc "Would a \"I'll fuck you later\" make you feel better?"
                                scene w2_6028 with dissolve
                                rose "You know what?"
                                scene black with fade
                                rose "It just might."
                                if mod_var:
                                    $ mod_var = False
                                    m_dev "Mod Option jump to other choice"
                                    jump mod_w2PreExhibitionSplit_2
                                "......"
                                "..."
                                jump w2PreExhibitionSolo
                            "Fully commit."(chg=["rosalind_passion_up2"]):


                                $ Rosalind_Libido += 2
                                $ w2RosalindPhoto = True
                                jump w2RoseSpank
            "Just get a ride home and decompress by yourself.":


                show screen textbox2 with dissolve
                scene w2_5795 with dissolve
                mc "Yeah, let's go. I want to squeeze in a nap before tonight."
                scene w2_5796 with dissolve
                rose "*Sigh* If only I could will my body to sleep..."
                scene w2_5800 with dissolve
                mc "Not much for naps?"
                scene w2_5802 with dissolve
                rose "I've been... having a little trouble sleeping recently."
                scene w2_5801 with dissolve
                mc "That's not good. You need all the rest you can get."
                scene w2_5803 with dissolve
                "That was true. There were still two more weeks to go after tonight."
                scene w2_5997 with dissolve
                rose "It's not a worrying amount. I'm just a little tired during the day."
                scene w2_5805 with dissolve
                mc "I guess it {b}would{/b} be abnormal if you were sleeping like a baby..."
                scene w2_5998 with dissolve
                rose "Talk in the car?"
                scene w2_5999 with dissolve
                "As we moved to go, my eyes flickered down her body one last time, starting from her luscious lips and going all the way down her long, bare legs. My gaze didn't go unnoticed..."
                scene w2_6000 with dissolve
                rose "I know that look."
                rose "You want me... to take care of you?"
                scene w2_6001 with dissolve
                mc "No, it's not the time or place for that. We should save our energy for tonight."
                scene w2_6029 with dissolve
                rose "You sure?"
                scene w2_6030 with dissolve
                mc "You got to stop worrying I'm going to renege on our deal, Rosalind. I'll look for ways I can help you even if you don't blow me in a parking lot."
                scene w2_6031 with dissolve
                rose "I would never do something so outrageous. I would blow you back at your place."
                mct "(Glad to see she had a sense of humor about this.)"
                scene w2_6032 with dissolve
                mc "Just focus on tonight. You've got to not only survive, but win."
                stop music fadeout 3.0
                scene black with fade
                mc "{b}You've got to win{/b}."
                "......."
                "..."
                jump w2PreExhibitionSolo



            "{color=#696969}[[Affection] Kill some time together at your apartment.{/color}" if Rosalind_Affection <= 24:
                jump w2PreExhibitionSplit

            "{color=#696969}[[Full Deal] ??????{/color}" if roseDealFullAcceptance == False:
                jump w2PreExhibitionSplit
    else:

        scene w2_5795 with dissolve
        mc "Yeah, let's go. I want to squeeze in a nap before tonight."
        scene w2_5796 with dissolve
        rose "*Sigh* If only I could will my body to sleep..."
        scene w2_5800 with dissolve
        mc "Not much for naps?"
        scene w2_5802 with dissolve
        rose "I've been... having a little trouble sleeping recently."
        scene w2_5801 with dissolve
        mc "That's not good. You need all the rest you can get."
        scene w2_5803 with dissolve
        "That was true. There were still two more weeks to go after tonight."
        scene w2_5997 with dissolve
        rose "It's not a worrying amount. I'm just a little tired during the day."
        scene w2_5805 with dissolve
        mc "I guess it {b}would{/b} be abnormal if you were sleeping like a baby..."
        scene w2_5998 with dissolve
        rose "Talk in the car?"
        scene black with fade
        mc "Yeah, let's go."
        "......"
        "..."
        jump w2PreExhibitionSolo


label w2RoseSpank:

    if _in_replay:
        play music "music/leaving-home.ogg"

    "To back down now would be...."
    scene w2_5960 with dissolve
    mc "Turn around and put your hands on the car."
    "{b}Absurd{/b}."
    scene w2_5961 with dissolve
    "This world exacts a toll on men and women like Rosalind. Just like the men who took from my mother, I would greedily take from the woman in front of me with the full promise of rectification."
    scene w2_5962 with dissolve
    rose "Here? Let's go to your place..."
    scene w2_5960 with dissolve
    mc "I'll find a way to help you. No matter what."
    scene w2_5961 with dissolve
    rose "..."
    scene w2_5963 with dissolve
    scene w2_5964 with dissolve
    scene w2_5963 with dissolve
    "Her debts would be cleared one way or another. She would win this exhibition or I'd elsewise find the means."
    scene w2_5962 with dissolve
    rose "Alright..."
    scene w2_5963 with dissolve
    "Rosalind just wanted a normal life with her daughter. She was a nice woman who deserved help."
    scene w2_5965 with dissolve
    mc "Fuck, you're such a stupid bitch."
    scene w2_5966 with dissolve
    mc "Put your hands on the car."
    scene w2_5967 with dissolve
    "She did as I asked and then some, sticking out her fat ass for my benefit. She might not be certain of what I was about to do, but she made a safe assumption..."
    scene w2_5968 with dissolve
    rose "No one can see us, right?"
    scene w2_5969 with dissolve
    mc "Who knows? There's so many windows."
    scene w2_5967 with dissolve
    mct "(This parking lot was pretty private, and I had a good view of the street from here, but I would need to be quick...)"
    scene w2_5968 with dissolve
    rose "W-what are you going to do?"
    scene w2_5970 with dissolve
    mc "Who knows..."
    play sound "sound effects/slap3.wav"
    scene w2_5971 with vpunch
    "*Smack!*"
    rose "Ooomfh...!"
    scene w2_5970 with dissolve
    mc "You better keep it down if you don't want to draw anyone's attention."
    play sound "sound effects/slap2.wav"
    scene w2_5972 with vpunch
    "*Smack!*"
    rose "Mmmh...!"
    scene w2_5970 with dissolve
    mct "(What was I doing here? My disposition had flipped so quickly...)"
    scene rosap_slap_a with dissolve
    show rosap_slap with dissolve
    "*Smack!*"
    rose "Ngh-!"
    mc "You fucking cow..."
    mct "(Was I just an animal, who at the first taste of blood, leaped into action?)"
    show rosap_slap with dissolve
    "*Smack!*"
    rose "Bwah-!"
    scene w2_5992 with dissolve
    mc "You're getting your ass spanked by a college student in a parking lot, what the hell is wrong with you?"
    mc "Don't you feel any shame?"
    scene w2_5993 with dissolve
    mct "(...or me, for that matter.)"
    scene w2_5994 with dissolve
    rose "I'm just doing what I have to do..."
    scene w2_5992 with dissolve
    mc "Bullshit."
    scene w2_5993 with dissolve
    mct "(So, she'd accept my crueler impulses as part of the deal? {b}Great{/b}.)"
    scene rosap_slap_a with dissolve
    show rosap_slap with dissolve
    mc "You're just doing what you have to do. What are you, a cockroach?"
    "I'd gladly have a field day with it."
    show rosap_slap with dissolve
    rose "Mffwh...!"
    show rosap_slap with dissolve
    mc "Truth is, those are just words to make you feel better."
    show rosap_slap with dissolve
    mc "The reality is you're just a lousy, {b}scheming{/b} bitch mistaking getting eaten whole for pragmatism."
    scene w2_5976 with dissolve
    mc "Where's your fucking pride as a woman?"
    rose "It's cause I'm just a stupid w-whore--"
    scene rosap_slap_a with dissolve
    show rosap_slap with dissolve
    show rosap_slap
    show rosap_slap
    rose "Ack!"
    mc "Eh? You think that's what I want to hear?"
    mc "You think I want worthless lip service from you?"
    show rosap_slap with dissolve
    mc "Don't bullshit me."
    mc "{b}You{/b} don't believe you're a whore. {b}I{/b} don't believe you're a whore."
    scene w2_5976 with dissolve
    mc "You may be a lousy, scheming bitch, but I don't see a whore. I see a strong woman."
    rose "Haaa... ha, [mc]--"
    scene rosap_slap_a with dissolve
    show rosap_slap with dissolve
    rose "Gaht...!"
    mc "That's what makes bending you over in a parking lot like this so damn fun!"
    scene w2_5995 with dissolve
    "Her pale, expansive ass had turned a beautiful shade of red with every wallop."
    mct "(If only I wasn't worried about how public this was. Getting arrested here... fuck, I'd be in deep shit for ruining tonight's exhibition.)"
    "I needed to reel my ugly side in, but this incredible feeling spreading through my body..."

    if w2HarpRainCheck == True:

        if kat_polite == True:
            "It was more enticing than what Mrs. Pulman's birthday offering."
        else:
            "It was more enticing than what Kathleen's birthday offering."
    else:
        if kat_polite == True:
            "It was far more exciting than Mrs. Pulman's birthday gift."
        else:
            "It was far more exciting than Kathleen's birthday gift."

    rose "A-are we finished?"
    mc "Almost, but you're looking sloppy. Straighten out your posture and brace yourself."
    scene w2_5996 with dissolve
    mc "These will be the last strikes."
    rose "Ha... I'm ready."
    scene rosap_slap_a with dissolve
    show rosap_slap with dissolve
    rose "Tskchh...!"
    mc "Good girl."
    show rosap_slap with dissolve
    mc "You're a strong woman, right?"
    rose "..."
    show rosap_slap with dissolve
    mc "Say it."
    rose "I'm a strong--"
    show rosap_slap with dissolve
    rose "--aahwoman!"
    show rosap_slaploop with dissolve
    "*Smack!*"
    mc "That's right, you lousy bitch!"
    "*Smack!* *Smack!*"
    mc "Don't forget it!"
    "*Smack!* *Smack!* *Smack!*"
    mc "That's why you can handle anything I throw at you!"
    "*Smack!* *Smack!* *Smack!* *Smack!*"
    mc "That's why you're going to win the exhibition!"
    scene w2_5977 with vpunch
    with flash
    rose "Ggg-----!"
    scene w2_5978 with dissolve
    rose "Ch-chwrap...!"
    scene w2_5979 with dissolve
    mc "You fucking disgust me."
    scene w2_5980 with dissolve
    "That wasn't really true, but..."
    scene w2_5981 with dissolve
    rose "Ack... that smarts, y-you really...!"
    scene w2_5982 with dissolve
    "I loved saying it."
    scene w2_5983 with dissolve
    rose "Ha... you really like this sort of thing, huh?"
    scene w2_5984 with dissolve
    "She just softly smiled."
    scene w2_5985 with dissolve
    mc "That's all you have to say? Aren't you even phased in the least?"
    scene w2_5986 with dissolve
    rose "Honestly...?"
    rose "I wasn't a fan of how public that was, but I've done worse this week. It was also uncomfortable and painful..."
    scene w2_5985 with dissolve
    mc "Then why are you smiling?"
    scene w2_5987 with dissolve
    rose "Who knows?"
    "Rosalind gently grabbed my hand, holding onto it as if it were dear."
    scene w2_5988 with dissolve
    rose "So, this is what you want?"
    rose "You want to choke and whip me?"
    scene w2_5989 with dissolve
    mc "Yes."
    scene w2_5988 with dissolve
    rose "You want to tie me up?"
    scene w2_5989 with dissolve
    mc "Yes, and more."
    scene w2_5990 with dissolve

    if kat_polite == True:
        "Mrs. Pulman had promised me the club would be a place where I could live out my desires, but playing with a woman like Rosalind was more appealing than a practiced whore."
    else:
        "Kathleen had promised me the club would be a place where I could live out my desires, but playing with a woman like Rosalind was more appealing than a practiced whore."

    scene w2_5991 with dissolve
    rose "*gulp* Okay then."
    scene w2_5988 with dissolve
    rose "For the next two weeks, {b}I'm yours{b} to do what you want with."
    scene w2_5990 with dissolve
    "The way she looked me in the eyes as she said it..."
    scene w2_5985 with dissolve
    show screen textbox2 with dissolve
    mc "...you bitch. That was already our deal."
    "My current life was one filled with dangerous women, but for me Rosalind was the most hazardous of them all."
    $ renpy.end_replay()
    scene black with fade
    stop music fadeout 3.0
    mc "Don't think I'm done with you today. When you get home, I have something for you to do."
    "......"
    "..."
    if not persistent.roseW2Spank:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.roseW2Spank = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    if mod_var:
        $ mod_var = False
        m_dev "Mod Option jump to other choice"
        jump mod_w2PreExhibitionSplit_2
    jump w2PreExhibitionSolo



label w2PreExhibitionRose:

    scene w2_5807 with circlewipe
    mc "C'mon, think of something else..."
    rose "That's not for show, is it?"
    mc "It's just... {i}I'm not very good{/i}."
    scene w2_5808 with dissolve
    rose "I don't mind. Just play me something while I brew us some tea."
    scene w2_5809 with dissolve
    mc "I can count the number of songs I know on both hands--"
    rose "You only need to know one, hun."
    scene w2_5810 with dissolve
    "She gave no quarter."
    mc "...*sigh*"
    scene w2_5811 with dissolve
    mct "(It's been a few years...)"
    scene w2_5812 with dissolve
    mct "(...but I guess what's the embarrassment of playing a song poorly compared to what I've seen of Rosalind?)"
    scene w2_5813 with dissolve
    "Sitting myself down in front of the keyboard, I rummaged through my unreliable memory in search of a song to play."
    "Even though there weren't many to pick from, I still couldn't decide. Nothing seemed..."
    scene w2_5814 with dissolve
    "......"
    "..."
    scene w2_5815 with dissolve
    mc "Ah...! Okay, I got it."
    "I settled on the one melody I knew the best."
    play music "music/ill-remember-you.ogg"
    scene w2_5816 with dissolve
    "*Da...da...da...da~*"
    "Thinking about how to play would only hobble what would already be a sloppy rendition, so I just got started."
    scene w2_5817 with dissolve
    rose "...hmm?"
    "My fingers were uncooperative and I was playing predominantly off-key, but there was a warm and fuzzy hit of dopamine and nostalgia to my clumsy fingering."
    "*Da...da...da...da~*"
    scene w2_5818 with dissolve
    rose "What is...?"
    rose "It's.. da, da... buh-built..."
    scene w2_5819 with dissolve
    rose "Oh...!"
    scene w2_5820 with dissolve
    rose "You built your tower strong and tall~"
    "Rosalind's delightful, singsong voice carried from the kitchen as she recalled the lyrics."
    rose "Can't you see it's got to fall~"
    "*Da...da...da...da~*"
    scene w2_5821 with dissolve
    rose "{b}That{/b} is a surprising choice."
    scene w2_5823 with dissolve
    mc "It was my dad's favorite song. My mom played it all the time when she was teaching me how to play. "
    scene w2_5822 with dissolve
    rose "That's nice. You play it well."
    scene w2_5823 with dissolve
    mc "No, I don't... not in the least. Honestly, it was an annoyance back then, but now I wish I took learning the piano more seriously."
    scene w2_5822 with dissolve
    rose "...because it would came in handy for when old women ask you to play?"
    scene w2_5824 with dissolve
    mc "Yeah, I hear ragtime is a real panty dropper amongst certain demographics."
    "*Da...da...da...da~*"
    scene w2_5825 with dissolve
    mc "You know, you're standing in the very apartment you tried to seduce me in a week and a half ago."
    scene w2_5826 with dissolve
    rose "...what's your point?"
    scene w2_5827 with dissolve
    mc "That you don't think of yourself as an old woman and neither do I."
    scene w2_5828 with dissolve
    rose "...it's not polite to bring up ancient history, [mcf]."
    scene w2_5831 with dissolve
    mc "Mmmh... hmmm, hmm~ my bad. It wasn't my intention to be rude."
    scene w2_5816 with dissolve
    rose "No, really. Why do you regret it?"
    scene w2_5831 with dissolve
    mc "My mom loved teaching me, but she eventually gave up on it."
    scene w2_5830 with dissolve
    mc "It would've been nice to have been able to look back on more memories."
    scene pr1195 with pixellate
    mc "Hmmm~"
    mc "Hmm~ hmmm~"
    scene w2_5816 with pixellate
    rose "You could still improve and she could still help you, right?"
    scene w2_5831 with dissolve
    mc "I suppose, but that's a lot of time and hard work. I have other things now..."
    scene w2_5816 with dissolve
    rose "School?"
    scene w2_5831 with dissolve
    mc "School and the... {b}club{/b}. Although, I'm not sure how much time the latter will eat up once the Exhibition is over."
    scene w2_5832 with dissolve
    rose "... hmm, my daughter wants to be a veterinarian."
    scene w2_5833 with dissolve
    mc "Oh yeah? She loves animals, huh?"
    scene w2_5832 with dissolve
    rose "What kid doesn't?"
    scene w2_5833 with dissolve
    mc "I hear vet school is more difficult to get into than med school."
    scene w2_5832 with dissolve
    rose "Really? That's surprising."
    scene w2_5833 with dissolve
    mc "It's just something I read. It's because there's fewer of them, which makes it more competitive."
    mc "How does she do in school?"
    scene w2_5834 with dissolve
    rose "She does wonderful. Honor roll - makes me so damn proud."
    scene w2_5835 with dissolve
    rose "She loves learning. I don't know where it comes from though. I wasn't very good at school and neither was Rupert - uh, that's her father."
    scene w2_5836 with dissolve
    mct "(Rupert, huh...?)"
    mc "Fitting name for an asshole..."
    scene w2_5837 with dissolve
    mc "Oooh...?"
    scene w2_5838 with dissolve
    "Rosalind's hands unexpectedly gripped my shoulders."
    scene w2_5839 with dissolve
    rose "Keep playing. The water is still boiling."
    scene w2_5837 with dissolve
    mc "Alright..."
    scene w2_5838 with dissolve
    "I wasn't playing all that much better. Every few keys I missed my mark and split the melody apart with discordant noise."
    scene w2_5839 with dissolve
    rose "Nora is a bright girl. Whatever she sets her mind to, she'll achieve."
    scene w2_5838 with dissolve
    "Still, I persisted in playing."
    scene w2_5840 with dissolve
    rose "I just can't allow her parents' mistakes to drag her down."
    "She laid it on thick, undoubtedly impressing upon our arrangement."
    scene w2_5841 with dissolve
    rose "Mm_____~ mm____~ Hey, da, da, da~"
    rose "You close your eyes and speak to me~ Of faith and love and destiny..."
    scene w2_5840 with dissolve
    "She sang with a lilted voice, tickling my brain and bringing me back to earlier this week."
    rose "As distant as eternity~ From truth and understanding..."
    scene w2_5842 with dissolve
    mc "You have a pretty voice. You ever sing before?"
    rose "Girls' choir from middle to the end of high school."
    "I see..."
    scene w2_5841 with dissolve
    rose "The wind blows cold outside your door~"
    scene w2_5840 with dissolve
    "My music was a poor accompaniment to her singing, but I didn't feel too bad about it."
    scene w2_5843 with dissolve
    "This was... {b}nice{/b}."
    stop music fadeout 3.0
    play sound "sound effects/teakettle.wav"
    scene black with fade
    "*Wheeeeeeeeee!*"
    rose "Oh, my! There's the kettle!"
    stop sound fadeout 3.0
    "......"
    "..."
    play music "music/dog-park.ogg"
    scene w2_5844 with fade
    "What was most surprising is how long we talked - four cups of tea, spread across an hour, just chit-chatting about this and that."

    if roseTakeAdvantage == False:
        "I hadn't spoken with Rosalind that freely since the night we first met and she offered me her lap as a pillow."

    "In theory it was weird talking to a Carnation for so long about anything other than the club or sex, but it didn't really feel that unnatural."
    rose "Yeah... it was a \"everything is shameful\" household."
    scene w2_5845 with dissolve
    "I got lost in her gentle charms."
    scene w2_5846 with dissolve
    rose "My mother is a nice woman when you need a hot meal after a neighbor dies, but I was happy to go off to college."
    scene w2_5847 with dissolve
    mc "What did you study?"
    scene w2_5846 with dissolve
    rose "Business... well, mainly things related to clerking and being an administrative assistant."
    scene w2_5848 with dissolve
    rose "That's my day job, so to speak. Or it was... I'm taking a leave right now."
    scene w2_5849 with dissolve
    "......"
    "..."
    scene w2_5850 with dissolve
    rose "Heh...! The tea was pretty awful, wasn't it?"
    scene w2_5851 with dissolve
    mc "Ha! I've been wanting to say that for the past hour. It was here when I moved in a few weeks ago, so I can't vouch for the source."
    scene w2_5850 with dissolve
    rose "Then why did we drink eight cups of it between the two of us?"
    scene w2_5851 with dissolve
    mc "You tell me. You kept refilling my cup. I was just being polite."
    scene w2_5850 with dissolve
    rose "You looked like you were enjoying it, so I just kept going!"
    scene w2_5852 with dissolve
    mc "The company made up for it. I'm glad you came up with me. It's been a nice change of pace from the rest of the week."
    scene w2_5853 with dissolve
    rose "Me too, I would've just gone home, and had better tea mind you, but I would have just sat in silent contemplation until it was time to get dressed and leave."
    rose "That's... sort of what I do in the evenings now."
    scene w2_5854 with dissolve
    "A leave from her job, her daughter at summer camp, the Exhibition looming over her... it painted a depressing picture."
    scene w2_5855 with dissolve
    mc "You make sitting around sound exhausting."
    scene w2_5853 with dissolve
    rose "Oh, {b}it is{/b}. So, yeah... I would say I have enjoyed the company as well."
    stop music fadeout 3.0
    play sound "sound effects/door-open.wav"
    scene w2_5856 with dissolve
    "*Click*"
    vic "You should try knocking first, you never know..."
    kil "It's fiiiiine! [mcf], if you're home, we're coming in--!"
    scene w2_5857 with dissolve
    "Well, {b}fuck me.{/b}"
    "Standing in my apartment was my mother and lifelong friend. An everyday, innocuous set of visitors for a bright weekend afternoon."
    "The singular problem was..."
    play music "music/swagger.ogg"
    scene w2_5858 with dissolve
    vic "Oh! You have company!"
    "I would now have to lie to my dear mother about who this leggy, older woman sitting across from me at the kitchen table was."
    scene w2_5859 with dissolve
    vic "Sorry! We should've called first!"
    scene w2_5860 with dissolve
    "Her smile told me that she was, in fact, not sorry."
    scene w2_5859 with dissolve
    vic "I should've {i}definitely{/i} called first..."
    scene w2_5861 with dissolve
    mc "...eheh, and why didn't you?"
    scene w2_5862 with dissolve
    vic "Well, since you couldn't get lunch with me today because you had already made plans with some \"college friends\", I invited Ian so we could catch up..."
    mct "(Yeah, okay, that part was nice and normal, but...)"
    scene w2_5863 with dissolve
    vic "...and then, since I know you love Bake n' Take, I wanted to leave the leftovers in your fridge. In case you weren't home, Ian told me he had a key..."
    scene w2_5864 with dissolve
    mc "I see... well, I did meet my friends a couple of hours ago and then--"
    scene w2_5866 with dissolve
    vic "...and if you were home, I {b}certainly{/b} wasn't expecting to disturb you while you were in the {i}middle of something{/i}."
    scene w2_5865 with dissolve
    "Her look told me that she was, in fact, pleased with the discovery."
    scene w2_5866 with dissolve
    vic "If we're interrupting {i}something{/i}, we'll--"
    scene w2_5867 with dissolve
    mc "Don't look so excited, okay?"
    mc "This is Rosalind and she's {b}a friend{/b}."
    scene w2_5868 with dissolve
    rose "Hello..."
    scene w2_5869 with dissolve
    vic "A friend, huh? Just like that Hana girl?"
    vic "I've never known you to have that many friends, [mcf]. I'm glad my son's becoming popular."
    scene w2_5870 with dissolve
    mct "(This is twice in the same week...)"
    "The way she was so damn sure of the situation made me want to do some teasing of my own. Then again, the actual truth of our relationship wasn't outside the ballpark of what she was imagining either..."
    hide screen textbox2 with dissolve

    menu:
        "Suppress that urge.":
            scene w2_5871 with dissolve
            show screen textbox2 with dissolve
            mc "She's the mother of one of my former students."
            vic "The m-mother--"
            scene w2_5872 with dissolve
            vic "Ah... you don't have to explain. You're an adult."
            scene w2_5873 with dissolve
            "She didn't believe me, which was pretty astute of her, considering it {i}was{/i} a lie."
            scene w2_5874 with dissolve
            mc "I feel like I do when there's an obvious misunderstanding and you make a game out of giving me a hard time."
            mc "We ran into each other at the nearby park and we were having some tea while she told me about how her daughter was doing in school."
        "Call your mom's bluff and pull Rosalind close.":


            scene w2_5875 with dissolve
            show screen textbox2 with dissolve
            mc "Well, you have been telling me to get my nose out of the books and enjoy my youth, right?"
            rose "Uh-huh...?"
            vic "Those were more or less my words, yes..."
            scene w2_5876 with dissolve
            mc "This is Rosalind, I met her at a bar a few hours earlier while day drinking. We hit it off pretty well."
            mc "I think you might've gone to school together?"
            rose "School...? Eh? Oh, uh... i-it's nice to..."
            scene w2_5877 with dissolve
            vic "......"
            scene w2_5878 with dissolve
            vic "...bah, you have the worst poker face, [mcf]. She really is just a friend, huh?"
            scene w2_5879 with dissolve
            mc "That's what I was trying to tell you. She's the mother of one of my former students."
            mc "We ran into each other at the nearby park and we were having some tea while she told me about how her daughter was doing in school."

    scene w2_5880 with dissolve
    vic "Ah! One of the kids you tutored...?"
    scene w2_5881 with dissolve
    "She didn't look like she quite bought it, but she wasn't really in a position to question my story."
    stop music fadeout 3.0
    scene w2_5880 with dissolve
    vic "...hello, Rosalind. I'm Victoria, [mcf]'s mother."
    scene w2_5882 with dissolve
    rose "Your son was a very capable tutor."
    scene w2_5883 with dissolve
    vic "Aha~ yes! I've heard people say that."
    vic "He always did well in his studies."
    scene w2_5884 with dissolve
    mc "I was basically just a glorified proctor..."
    scene w2_5883 with dissolve
    vic "I apologize if I embarrassed you just now while teasing my son. I like to seize the opportunity when it presents itself."
    scene w2_5885 with dissolve
    rose "You two really have an interesting sense of humor."
    scene w2_5886 with dissolve
    kil "That's one way to put it..."
    play music "music/crinoline-dreams.ogg"
    scene w2_5887 with dissolve
    mc "...and this is Killian, a friend of mine."
    scene w2_5888 with dissolve
    kil "Have we met before? You look familiar..."
    scene w2_5889 with dissolve
    mct "(That...!)"
    scene w2_5890 with dissolve
    rose "I don't think so... I'm pretty good with faces."
    "If I could right now, I would kick him in the shin."
    rose "I would definitely remember a face like yours."
    scene w2_5891 with dissolve
    mc "Punchable, you mean?"
    scene w2_5892 with dissolve
    vic "He means pinchable."
    kil "Stop, I'm not a kid anymore..."
    "Seeing Ian recoil from my mother's affection, like an embarrassed child, brought a smile to my face."
    scene w2_5893 with dissolve
    vic "Really? That must make me old now..."
    kil "W-what? I didn't say that...!"
    scene w2_5894 with dissolve
    vic "Heh~ ah, Ian..."
    mct "(...you're so easy.)"
    scene w2_5895 with dissolve
    vic "{b}Well...{/b}, I'm going to put this in the fridge and get out of your hair."
    mc "You really don't have to go. We were finished with our--"
    rose "He's right, I was just leaving."
    scene w2_5896 with dissolve
    vic "No, I really did just intend to drop this off. I've got some copy I need to edit at home."
    vic "In the future, I'll call ahead."
    scene w2_5897 with dissolve
    mc "It's really not a big deal, Mom."
    scene w2_5896 with dissolve
    vic "Yeah, yeah... I know you feel that way, but a phone call won't hurt either of us!"
    scene w2_5898 with dissolve
    vic "You're a man. It's not appropriate for me to drop in unannounced."
    scene w2_5899 with dissolve
    mc "You should learn from her example."
    kil "Eh? You love it when I drop by."
    scene w2_5900 with dissolve
    rose "It was nice to meet you, Victoria."
    vic "Likewise."
    scene black with fade
    stop music fadeout 3.0
    vic "Enjoy the pizza. I asked them to put extra feta on it like you like."
    mc "Thanks, Mom."
    "......"
    "..."
    scene w2_5901 with wipeleft
    mc "...you look familiar?"
    scene w2_5902 with dissolve
    kil "Ow! It was just an inside joke!"
    "Ian had stuck around after my mom left, under the technically true umbrella of us both having work in a few hours."
    scene w2_5903 with dissolve
    kil "It's not like Vicky could've figured anything out from that!"
    scene w2_5904 with dissolve
    rose "That was..."
    scene w2_5905 with dissolve
    rose "Your mother seems like a nice woman, [mcf]."
    kil "Yeah! Not many mothers would give out mental high fives over their son getting laid!"
    scene w2_5906 with dissolve
    mc "We actually weren't screwing around, asshole."
    kil "No joke? If you're not fucking, then what the hell is she doing here?"
    scene w2_5907 with dissolve
    rose "Ack, he's right... what AM I doing here?"
    mc "We were having not-so-good tea..."
    scene w2_5908 with dissolve
    rose "Heh, I know, and I did enjoy it... but in a few hours things will be very different. It makes all of this seem so..."
    scene w2_5909 with dissolve
    kil "Stupid?"
    rose "...inappropriate."
    scene w2_5910 with dissolve
    "She was right. This was more or less just a diversion from reality. She and I weren't friends."
    "I was part of the machine that was exploiting her misfortune and she was indulging me out of necessity."

    if rosalindKilSolution == True:
        $ w2ThreesomeTopicBreached = True
        scene w2_5911 with dissolve
        play music "music/as-i-figure.ogg"
        kil "You know, Rose...."
        scene w2_5912 with dissolve
        kil "Since you're being inappropriate and all three of us are here..."
        rose "Ah...!"
        "Ian slithered up to Rosalind like a snake, running his hand down her lower back and grabbing a generous portion of her ass."
        scene w2_5913 with dissolve
        kil "We could fulfill that little transaction we made."
        scene w2_5914 with dissolve
        "The at-hunt playboy tossed a sordid smile my way."
        scene w2_5915 with dissolve
        rose "Ah, w-well if that's... ah..."
        scene w2_5916 with dissolve
        mc "{b}Not today{/b}."
        kil "Ah, c'mon why. This is the perfect time--"
        scene w2_5917 with dissolve
        mc "She has \"work\" in a few hours."
        scene w2_5918 with dissolve
        kil "You sound like August!"
        mc "..."
        scene w2_5919 with dissolve
        kil "Okay, okay, I get it! You take everything you do seriously!"
        rose "Heh, you two are funny."
        scene w2_5920 with dissolve
        kil "See? She likes us."
        scene w2_5921 with dissolve
        mc "You have a big night ahead of you. I'll see you later?"
        scene w2_5922 with dissolve
        rose "Thank you for the crappy tea, Mr. [mcl]."
        scene black with fade
        stop music fadeout 3.0
        "With a way-too-polite exit, the motherly woman left Ian and me alone."
    else:
        scene w2_5908 with dissolve
        rose "I should go."
        scene w2_5923 with dissolve
        kil "Yeah, that would be wise."
        scene w2_5924 with dissolve
        rose "Thank you for the crappy tea, Mr. [mcl]."
        mc "Yeah, I guess you do have a big night ahead of you. I'll see you later."
        scene w2_5925 with dissolve
        rose "There's no doubt about that is there?"
        scene black with fade
        stop music fadeout 3.0
        "With a way-too-polite exit, the motherly woman left Ian and me alone."

    play music "music/cold-sober.ogg"
    scene w2_5926 with dissolve
    mct "(...and then there were two.)"
    scene w2_5927 with dissolve
    kil "You guys really weren't screwing around?"
    scene w2_5928 with dissolve
    mc "We were just talking."
    scene w2_5929 with dissolve
    kil "Ha! \"Just\" talking? You gotta be careful man."
    scene w2_5928 with dissolve
    mc "Careful about what?"
    scene w2_5927 with dissolve
    kil "Those snakes will take advantage of you."
    scene w2_5928 with dissolve
    mc "{i}She'll{/i} take advantage of {i}me{/i}? Don't you think the shoe is on the other foot here?"
    scene w2_5927 with dissolve
    kil "It goes both ways. I'm just saying, don't go catching feelings for a whore."
    scene w2_5929 with dissolve
    kil "You should be careful. You don't know the way the world works yet."
    scene w2_5930 with dissolve
    mc "You--"
    scene w2_5931 with dissolve
    "There was a lot to unpack in his words, one of which was an infuriating assumption about what I was feeling, but most of all..."
    scene w2_5930 with dissolve
    mc "{i}I{/i} don't know the way the world works?"
    mc "I'm not the one who spent his summers in his family's {b}third{/b} home. I'm not the one whose parents foot every single--"
    scene w2_5932 with dissolve
    kil "Slow down. You really want to take it that direction, considering my uncle is the one footing your college and living expenses for you doing jack shit all for work?"
    kil "I'm just trying to look out for you, bro. Those bitches will try and worm their way into your life and squeeze out any advantage they can get."
    scene w2_5933 with dissolve
    mc "......"
    scene w2_5934 with dissolve
    mc "...you've got such a warped view of women."
    scene w2_5935 with dissolve
    kil "No, I've got a warped view of people. {b}We're all scum{/b}."
    scene w2_5937 with dissolve
    kil "That's why there's nothing wrong with you squeezing back and fucking their brains out. Just don't go making friends with them?"
    scene w2_5936 with dissolve
    mc "Just a few weeks ago you told me to look out for them and make sure the Carnations were safe."
    scene w2_5937 with dissolve
    kil "You don't need to be their friend to do that, numb nuts. I feel sorry for most of those girls, but just because they're pitiable doesn't mean they won't hesitate to manipulate the shit out of you."
    scene w2_5933 with dissolve
    "I didn't really buy into what he was advising, but I couldn't refute it. Rosalind and I did make an arrangement..."
    scene w2_5934 with dissolve
    mc "Yeah, thanks for the rotten advice, Dad."
    scene w2_5935 with dissolve
    kil "Heh! No problem! So, you want to play a game?"
    scene w2_5936 with dissolve
    mc "Nah, I think I'm going to get an hour of shut-eye in before tonight."
    scene w2_5938 with dissolve
    kil "Good idea. Fill up the gas tank!"
    kil "We're going to need every ounce we can get!"
    stop music fadeout 3.0
    scene black with fade
    "......"
    "..."
    if w2RosalindPhoto == True:
        stop music fadeout 3.0
        play sound "sound effects/sms-chime.wav"
        "*Chirp, chirp.*"
        scene w2_6063 with dissolve
        mct "(Ah, that must be Rosalind with the \"homework\" I assigned.)"
        "One photo to please me, of her choosing, with the caveat that she would be punished if it wasn't to my tastes. Emboldened by her willingness to be manhandled, I was leaning hard into our new dynamic."
        mct "(Of course, it wasn't going to please me.)"
        play music "music/leaving-home.ogg"
        scene w2_6064 with dissolve
        "It could be the hottest thing I'd ever seen and I'd tell her it's trash."
        mct "(Now, let's see...)"

        scene player-livingroom blur with dissolve
        hide screen textbox2 with dissolve
        call phone_start_rose from _call_phone_start_rose_mod
        call message_start ("Rosalind", "I didn't really know what to do, it's not like I have a lot of weird objects just lying around the house...") from _call_message_start_24_mod
        call reply_message ("You had awhile to come up with something. Show me.") from _call_reply_message_28_mod
        call message_img ("Rosalind", "This was kind of gross, tbh...", "rosalind04") from _call_message_img_5_mod
        call phone_end_rose from _call_phone_end_rose_mod

        scene w2_6012 with pixellate
        mct "(Eh? That's a huge-ass sausage! Who has something like that in their fridge?)"
        "It was cute imagining Rosalind racking her brain trying to come up with ideas and arriving at that."
        scene w2_6065 with dissolve
        mct "(Heh, she's amazing...)"

        scene player-livingroom blur with dissolve
        hide screen textbox2 with dissolve
        call phone_start_rose from _call_phone_start_rose_1_mod
        call message_img ("Rosalind", "This was kind of gross, tbh...", "rosalind04") from _call_message_img_6_mod
        call reply_message ("Seriously, that's all you could come up with in that time? You worthless cow.") from _call_reply_message_29_mod
        call message ("Rosalind", "I'm sorry. I did my best...") from _call_message_75_mod
        call reply_message ("Not yet you're not, but you will be sorry later this week. Expect it.") from _call_reply_message_30_mod
        call phone_end_rose from _call_phone_end_rose_1_mod
        scene w2_6066 with dissolve
        show screen textbox2 with dissolve
        if not persistent.roseW2Sausage:
            play sound "sound effects/notification.wav"
            show memoryunlock with dissolve
            $ renpy.pause(3, hard=True)
            $ persistent.roseW2Sausage = True
            hide memoryunlock with dissolve
            $ renpy.pause(0.5, hard=True)
    jump w2PreExhibitionStart


label w2PreExhibitionSolo:
    "A glass of hot chocolate and a half an hour later, a strange thought occupied my mind as I drifted off to sleep..."
    mct "(I've never had trouble sleeping, have I?)"
    play music "music/crinoline-dreams.ogg"
    scene w2_6002 with circlewipe
    mc "Ah, Mom...?"
    scene w2_6003 with dissolve
    vic "Hi, hun."
    scene w2_6002 with dissolve
    mc "What are you doing here?"
    scene w2_6003 with dissolve
    vic "Since you couldn't make it to lunch, I just wanted to drop off some leftover pizza. Ian and I went to {i}Bake and Take{/i}."
    scene w2_6002 with dissolve
    mc "Extra feta?"
    scene w2_6003 with dissolve
    vic "Uh-huh, extra feta. Just how you like it."
    scene w2_6005 with dissolve
    mc "Thanks. You're the best."
    scene w2_6004 with dissolve
    vic "Not really."
    scene w2_6005 with dissolve
    mc "How'd you get in?"
    scene w2_6004 with dissolve
    vic "Ian had a key."
    scene w2_6005 with dissolve
    mc "Right, yeah..."
    scene w2_6006 with dissolve
    mct "(At least he's not using it as a fuckpad for a drunken tryst this time...)"
    scene w2_6007 with dissolve
    kil "'Sup, bud."
    scene w2_6008 with dissolve
    mc "*yawwwwwwwn* Hey."
    scene w2_6009 with dissolve
    kil "I didn't even know you had college friends."
    "That was... true. I didn't like lying, but what could I do?"
    scene w2_6010 with dissolve
    mc "What are you talking about? I'm a well-liked guy."
    scene w2_6011 with dissolve
    vk "..."
    mc "Don't share a look like you don't know what I'm talking about!"
    scene w2_6033 with dissolve
    vic "Pfft- sorry. You're pretty likable, if I do say so myself, but uh..."
    kil "You're not the warmest, most approachable dude, dude."
    scene w2_6034 with dissolve
    mc "I don't appreciate you guys ganging up on me, especially when it's with something as unimportant as the truth."
    scene w2_6035 with dissolve
    vic "I think you used that line before, hun."
    scene w2_6036 with dissolve
    kil "He tried to pull that Pontius Pilate shit all the time when he got into trouble, remember?"
    scene w2_6037 with dissolve
    vic "Ah, hehe... yeah, his whole \"moral subjectivism\" phase in middle school. That was annoying."
    scene w2_6038 with dissolve
    mc "I think I'm most shocked you know who Pontius Pilate is."
    scene w2_6039 with dissolve
    kil "Some sort of car?"
    scene w2_6040 with dissolve
    vic "So, what are you doing today, [mcf]?"
    scene w2_6041 with dissolve
    mc "Uh..."
    scene w2_6042 with dissolve
    vic "Great. {b}Now you two{/b} are sharing a look."
    scene w2_6043 with dissolve
    vic "It must be something... \"fun\" then?"
    scene w2_6044 with dissolve
    kil "No, we just have..."
    scene w2_6045 with dissolve
    mc "We both have work tonight at Dr. Chuck's lounge."
    "To my knowledge, Ian had never lied to my mother. When we were kids, he was always the weak link in our schemes, quick to crack from the very first question."
    scene w2_6046 with dissolve
    vic "Oh, yeah?"
    scene w2_6047 with dissolve
    "Not that I thought that would be true now, he's an adult ass-man after all, but let's not take any chances."
    mc "Yep, gotta be there in a few hours."
    scene w2_6043 with dissolve
    vic "You two REALLY aren't doing anything shady, right?"
    scene w2_6047 with dissolve
    mc "Why do you keep asking that?"
    scene w2_6046 with dissolve
    vic "I mean this is a REALLY expensive apartment..."
    scene w2_6048 with dissolve
    kil "My uncle's got a lot of real estate. The place was just sitting unused until he can sell it for a profit."
    scene w2_6049 with dissolve
    mc "That's what I told her."
    scene w2_6050 with dissolve
    vic "Sorry. I don't mean to accuse you boys of anything, I'm just a worrywart."
    vic "This feeling I've got is probably just gas."
    "It was actually unnatural how her intuition was always spot on."
    scene w2_6051 with dissolve
    kil "You don't have to worry about [mcf] getting himself into any trouble!"
    kil "I'm looking out for him, just like I did when I was a kid."
    scene w2_6052 with dissolve
    vic "You went along with anything [mcf] wanted..."
    vic "I'm glad you got a lot more backbone now, though."

    if w2RosalindPhoto == True:
        jump w2RosalindSelfie
    else:
        scene w2_6053 with dissolve
        kil "You have no idea, woman."
        scene w2_6054 with dissolve
        vic "Pfft..."
        mc "That your best impression of what a man sounds like?"
        scene w2_6055 with dissolve
        kil "...ngh! Y'know, I don't appreciate you guys ganging up on me with something as inconvenient as the truth."
        scene w2_6056 with dissolve
        vic "Smooth! Personally, I thought you sounded really cool."
        scene w2_6057 with dissolve
        vic "Anyway, before I go home to get some work done, I wanted to ask if you guys wanted to have dinner sometime this week?"
        scene w2_6058 with dissolve
        kil "Just the three of us?"
        scene w2_6059 with dissolve
        vic "Sure, or... you have a girlfriend, don't you Ian? You're welcome to bring her along."
        vic "Maybe [mcf] could bring that nice Hana girl with him?"
        scene w2_6060 with dissolve
        mck "Uh..."
        "Between everything going on with Mina and Ian, and with Hana sharing our vocation, that didn't sound like a good idea..."
        mc "Like a home-cooked meal? Like one that {b}you{/b} cooked?"
        scene w2_6061 with dissolve
        vic "Hey, I cooked for you a few weeks ago!"
        scene w2_6062 with dissolve
        mc "That was just for the two of us, though..."
        kil "I'm sure we can swing something sometime at some point."
        vic "Yeah, well, just let me know..."
        scene black with fade
        vic "Anyway, I need to head home. The bills don't pay themselves."
        "......"
        "..."
        jump w2PreExhibitionSoloWarning

label w2RosalindSelfie:
    stop music fadeout 3.0
    play sound "sound effects/sms-chime.wav"
    "*Chirp, chirp.*"
    scene w2_6063 with dissolve
    mct "(Ah, that must be Rosalind with the \"homework\" I assigned.)"
    "One photo to please me, of her choosing, with the caveat that she would be punished if it wasn't to my tastes. Emboldened by her willingness to be manhandled, I was leaning hard into our new dynamic."
    mct "(Of course, it wasn't going to please me.)"
    play music "music/leaving-home.ogg"
    scene w2_6064 with dissolve
    "It could be the hottest thing I'd ever seen and I'd tell her it's trash."
    mct "(Now, let's see...)"

    scene player-livingroom blur with dissolve
    hide screen textbox2 with dissolve
    call phone_start_rose from _call_phone_start_rose
    call message_start ("Rosalind", "I didn't really know what to do, it's not like I have a lot of weird objects just lying around the house...") from _call_message_start_24
    call reply_message ("You had awhile to come up with something. Show me.") from _call_reply_message_28
    call message_img ("Rosalind", "This was kind of gross, tbh...", "rosalind04") from _call_message_img_5
    call phone_end_rose from _call_phone_end_rose

    scene w2_6012 with pixellate
    mct "(Eh? That's a huge-ass sausage! Who has something like that in their fridge?)"
    "It was cute imagining Rosalind racking her brain trying to come up with ideas and arriving at that."
    scene w2_6065 with dissolve
    mct "(Heh, she's amazing...)"

    scene player-livingroom blur with dissolve
    hide screen textbox2 with dissolve
    call phone_start_rose from _call_phone_start_rose_1
    call message_img ("Rosalind", "This was kind of gross, tbh...", "rosalind04") from _call_message_img_6
    call reply_message ("Seriously, that's all you could come up with in that time? You worthless cow.") from _call_reply_message_29
    call message ("Rosalind", "I'm sorry. I did my best...") from _call_message_75
    call reply_message ("Not yet you're not, but you will be sorry later this week. Expect it.") from _call_reply_message_30
    call phone_end_rose from _call_phone_end_rose_1
    scene w2_6066 with dissolve
    show screen textbox2 with dissolve
    mct "(I love this woman. She's so much fun.)"
    vic "[mcf], did you hear what I said?"
    stop music fadeout 3.0
    scene w2_6067 with dissolve
    mc "No, sorry... I was distracted by a message."
    scene w2_6068 with dissolve
    mc "What were you saying?"
    play music "music/crinoline-dreams.ogg"
    scene w2_6059 with dissolve
    vic "Why don't the three of us have dinner together sometime this week?"
    vic "...or, you have a girlfriend don't you Ian? Why don't you bring her as well? [mcf] could invite that Hana girl."
    scene w2_6060 with dissolve
    mck "Uh..."
    "Between everything going on with Mina and Ian, and with Hana sharing our vocation, that didn't sound like a good idea..."
    mc "Like a home-cooked meal? Like one that {b}you{/b} cooked?"
    scene w2_6061 with dissolve
    vic "Hey, I cooked for you a few weeks ago!"
    scene w2_6062 with dissolve
    mc "That was just for the two of us, though..."
    kil "I'm sure we can swing something at some point."
    vic "Yeah, well, just let me know..."
    $ renpy.end_replay()
    scene black with fade
    stop music fadeout 3.0
    vic "Anyway, I need to head home. The bills don't pay themselves. I've got some copy that needs editing at home."
    if not persistent.roseW2Sausage:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.roseW2Sausage = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    "......"
    "..."
    jump w2PreExhibitionSoloWarning



label w2PreExhibitionSoloWarning:

    play music "music/cold-sober.ogg"
    scene w2_6069 with dissolve
    kil "College friends, huh?"
    scene w2_6077 with dissolve
    kil "What were you really doing? Got a side piece or something?"
    scene w2_6070 with dissolve
    mc "No, I grabbed lunch with the Carnations."
    scene w2_6071 with dissolve
    kil "...uh, why?"
    scene w2_6070 with dissolve
    mc "What do you mean, why? It's my job."
    scene w2_6071 with dissolve
    kil "Your job is not to be buddy buddy with them, bud."
    scene w2_6070 with dissolve
    mc "I'm just trying to keep morale up and to make sure they don't have any problems that'll impede their performance."
    scene w2_6071 with dissolve
    kil "If you say so. Just don't be a sucker, man. You gotta be careful around the staff."
    scene w2_6070 with dissolve
    mc "Careful about what?"
    scene w2_6071 with dissolve
    kil "Those whores will look for any advantage they can get, and I know you're not as callous as you pretend to be."
    scene w2_6072 with dissolve
    kil "Once that happens, you're fucked. Things won't end how you expect them to."
    scene w2_6070 with dissolve
    mc "Speaking from experience, Romeo?"
    scene w2_6071 with dissolve
    kil "{b}No{/b}. Darius did though. He fell in love with one of the girls and it tore him up inside."
    scene w2_6072 with dissolve
    kil "I think that's why he eventually split."
    scene w2_6074 with dissolve
    mc "Ah, huh... I see..."
    mct "(...right, he doesn't know about the blackmail.)"
    scene w2_6069 with dissolve
    kil "Anyway, I'm just trying to look out for you, bro. Those bitches will try and worm their way into your life and squeeze out any advantage they can get."
    scene w2_6074 with dissolve
    mc "......"
    scene w2_6075 with dissolve
    mc "...you've got such an infuriating view of women, Ian."
    scene w2_6073 with dissolve
    kil "No, I've got a warped view of people. {b}We're all scum{/b}."
    kil "That's why there's nothing wrong with you squeezing back and fucking their brains out. Just don't get too chummy with 'em, yeah?"
    scene w2_6070 with dissolve
    mc "You know, just a few weeks ago you told me to look out for them and make sure the Carnations were safe."
    scene w2_6071 with dissolve
    kil "You don't need to be their friend to do that, numb nuts. I feel sorry for most of those girls, but just because they're pitiable doesn't mean they won't hesitate to manipulate the shit out of you."
    scene w2_6075 with dissolve
    mc "Yeah, thanks for the rotten advice, Dad."
    scene w2_6077 with dissolve
    kil "Heh! No problem! So, you want to play a game? We still got some time before we need to head out."
    scene w2_6076 with dissolve
    mc "I think I'm going to get a slice of that pizza you guys brought, get cleaned up, and then get changed into our uniform."
    mc "You can entertain yourself without making a mess, right?"
    stop music fadeout 3.0
    scene black with fade
    kil "Hehe, we'll see!"
    "......"
    "..."
    jump w2PreExhibitionStart

label w2PreExhibitionStart:
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transition_housegirls2 with blinds
    $ renpy.pause(6, hard=True)
    play music "music/george-street-shuffle.ogg"
    scene w2_6078 with blinds
    show screen qmenu with dissolve
    "That evening, Ian and I arrived on time."
    "I saw no sense in us being early. The night would be long enough as is and, quite frankly, I didn't want to put in overtime rubbing elbows with the club's clientele."
    "...a thought whose increasing hypocrisy wasn't lost on me."
    scene w2_6079 with dissolve
    kil "Pheeeeeew!"
    kil "I'll give the old lady credit where credit is due."
    kil "She knows how to put a costume together."
    hide screen textbox2 with dissolve
    scene w2_6080 with dissolve
    mc "No kidding..."
    "The fact that Jacob was unerringly looking her in the eyes was an admirable show of willpower."
    jacob "Call it a favor. Have them dock my pay if they must, just give her an extra day to--"
    scene w2_6081 with dissolve
    mc "Hey, Jacob."
    jacob "..."
    scene w2_6082 with dissolve
    jacob "Ah, you two are finally here. The Little Miss isn't with you?"
    scene w2_6083 with dissolve
    mc "Should she be?"
    scene w2_6084 with dissolve
    jacob "I was told to direct you to Mr. Byrnes' office when the three of you got here."
    scene w2_6085 with dissolve
    mc "I... actually don't know where that is."
    kil "I'll take us there."
    scene w2_6086 with dissolve
    dal "Hey, Mr. [mcl]..."
    "Dalia looked at me uncertainly."
    dal "Is it true Hana's gonna be an owner?"
    scene w2_6087 with dissolve
    mc "I don't think anything's official yet, but... she's open to it."
    mc "Why do you ask?"
    scene w2_6088 with dissolve
    dal "It's a big topic among the girls. She's pretty popular."
    scene w2_6089 with dissolve
    kil "Bah!"
    mc "...well, she's agreed to take a bigger interest."
    scene w2_6090 with dissolve
    dal "Hmm..."
    scene w2_6091 with dissolve
    jacob "Best not get your hopes up, Dal."
    scene w2_6092 with dissolve
    dal "It's the girls I'm worried about."
    scene w2_6093 with dissolve
    kil "C'mon, doc. We shouldn't keep August waiting."
    mc "See you two later tonight I guess."
    scene w2_6094 with dissolve
    dal "I'm really sorry I can't do anything about Emma."
    scene w2_6095 with dissolve
    jacob "*sigh* I know your hands are tied. I don't blame you."
    stop music fadeout 3.0
    scene black with fade
    "Ian led the way to Mr. Byrnes' office."
    aug "Come in!"
    play sound "sound effects/door-openclose.wav"
    play music "music/covert-affair.ogg"
    scene w2_6096 with blinds
    show screen textbox2 with dissolve
    aug "Get your asses over here! Now, we're just waiting on Hana and Chuck."
    "The old man greeted us with a smile and waved us over."
    scene w2_6097 with dissolve

    if kat_polite == True:
        "Mrs. Pulman, on the flip side, was looking unusually unhappy and staying conspicuously silent."
    else:
        "Kathleen, on the flip side, was looking unusually unhappy and staying conspicuously silent."

    scene w2_6098 with dissolve
    kat "Hello, [mcf]."
    scene w2_6099 with dissolve
    scene w2_6100 with dissolve
    scene w2_6099 with dissolve
    "I returned her simple greeting with a nod."

    if w2KatSex == True:
        scene w2_6102 with dissolve
        kat "Excited for tonight?"
        scene w2_6103 with dissolve
        "The question was accompanied by the old woman's hand not-so-subtly massaging my inner thigh."
        scene w2_6104 with dissolve
        scene w2_6103 with dissolve
        "Once more, I nodded. After what we did on my birthday, I couldn't feign otherwise."
        scene w2_6102 with dissolve
        kat "You did wonderfully last week. I expect tonight is going to be quite the show."
        scene w2_6118 with dissolve
        aug "...that's true. At your age, I would've had trouble getting it up in those circumstances."
    else:

        scene w2_6098 with dissolve
        kat "Excited for tonight?"
        scene w2_6101 with dissolve
        mc "Mildly anxious might be a better way of describing it."
        scene w2_6098 with dissolve
        kat "You did wonderfully last week."
        scene w2_6105 with dissolve
        aug "That's true, at your age I would've had trouble getting it up in those circumstances."

    scene w2_6106 with dissolve
    kat "At your age now, isn't that doubly true, Augy?"
    scene w2_6107 with dissolve
    aug "Ha! I still fuck like I'm in my 20s, you peach."
    scene w2_6108 with dissolve
    kat "Hmpfh, charming."
    scene w2_6109 with dissolve
    kil "Right, sooooo.... what are we doing here?"
    scene w2_6110 with dissolve
    aug "Having a drink to celebrate my daughter coming around on this place."
    scene w2_6111 with dissolve
    "I didn't know if Hana would really be in a drinking mood, but I wasn't going to suggest as much to August."
    "He looked {i}very{/i} happy."
    scene w2_6109 with dissolve
    kil "Eh? She came around on the money."
    scene w2_6112 with dissolve
    aug "That's one and the same for me. This place IS money."
    scene w2_6113 with dissolve
    show screen textbox2 with dissolve
    aug "Only those among us who have never needed it can say otherwise."
    scene w2_6114 with dissolve
    kat "Come now, you don't shy away from the perks of this place. Not to mention Charles..."
    kat "Well, all three of us love the work in our own ways, don't we?"
    scene w2_6113 with dissolve
    aug "I should stop worrying about ever-increasing, needless extravagance then?"
    scene w2_6115 with dissolve
    kil "Mommy and Daddy shouldn't argue in front of the kids."
    scene w2_6114 with dissolve
    kat "Ian's right. We should table our earlier discussion."
    kat "We're here to celebrate our impending new partnership."
    scene w2_6113 with dissolve
    aug "Ha! Alright, yeah!"
    aug "We should enjoy the days we have left, right?"
    play sound "sound effects/door-openclose.wav"
    scene w2_6116 with dissolve
    kat "Mmhh--"
    play music "music/that-one-bar-scene.ogg"
    scene w2_6117 with dissolve
    chuck "Look at the beautiful mouse I found wandering the hallway."
    scene w2_6119 with dissolve
    hana "What's all this? We having a party?"
    scene w2_6120 with dissolve
    aug "The three of us thought we'd share a drink, dear. As peers."
    "Peers was a loaded word, one I thought would make her flinch, but..."
    scene w2_6121 with dissolve
    hana "Oh, is that it? Should I pour?"
    hana "Can't escape filling the glasses of old men, I guess."
    scene w2_6122 with dissolve
    "She rolled with it, seemingly unphased."
    scene w2_6123 with dissolve
    chuck "Baha, nonsense, lass. I'll get it."
    scene w2_6124 with dissolve
    kil "By the way, what are [mcf] and I doing here?"
    scene w2_6125 with dissolve
    aug "Why wouldn't you two be here? We're all family here."
    scene w2_6126 with dissolve
    kil "Family, huh?"
    scene w2_6127 with dissolve
    hana "Yeah, let's get along, little brother."
    scene w2_6128 with dissolve
    kil "Ha, sure thing."
    stop music fadeout 2.0
    scene black with fade
    aug "To my daughter and all our futures together."
    play sound "sound effects/ice-glass.wav"
    scene w2_6129 with fade
    "*Clink*"
    scene w2_6130 with dissolve
    "*Glug* *Glug* *Glug*"
    scene w2_6131 with dissolve
    mc "Ffhaaa....!"
    mct "(I'm developing a taste for this...)"
    scene w2_6132 with dissolve
    chuck "You always did keep it to a few words."
    scene w2_6133 with dissolve
    aug "You talk too much, Charles."
    scene w2_6134 with dissolve
    hana "That it?"
    play music "music/as-i-figure.ogg"
    scene w2_6135 with dissolve
    aug "Pretty much. You don't need to hear from me what it means to have a stake in this place."
    aug "I know it may not seem like it considering how high up and secluded we are, but this is a criminal enterprise."
    scene w2_6136 with dissolve
    kat "Don't be so dramatic, Augy."
    scene w2_6137 with dissolve
    aug "Kathy doesn't like when I use that word to describe her, but it's true."
    aug "We're all criminals. No moral judgement, but that's just a simple fact. Doesn't mean you can't be decent, but..."
    scene w2_6138 with dissolve
    aug "This isn't a soft business, Hana. It'll take time for a kind girl like you to become acclimated to the realities and pitfalls."
    scene w2_6139 with dissolve
    hana "I know that old man, but I'll eventually get a say in things, right?"
    scene w2_6140 with dissolve
    chuck "Of course you will, lass. You'll have your say, just as any of us has."
    scene w2_6141 with dissolve
    aug "You can always speak your mind, but first you need to learn how things work."
    scene w2_6142 with dissolve
    kat "Why wait? A good idea is a good idea, and I'm certain Hana has a few of those in her."
    scene w2_6143 with dissolve
    aug "We'll take it one day at a time. For tonight, she gets to know our customers in a different light and sit in on your little game."
    scene w2_6144 with dissolve
    kat "She'll do more than just sit."
    aug "Oh? What are you talking about, Kathy?"
    kat "I'm going to have her help judge tonight's performances."
    scene w2_6145 with dissolve
    hana "Judge? What the hell is there to judge? It's all just a pony show."
    scene w2_6146 with dissolve
    kat "Now, now dear... don't think of your role tonight as frivolous."
    kat "{b}Our{/b} Carnations are going to work hard tonight, their hopes and dreams hanging in the balance. You should take your role seriously."
    scene w2_6147 with dissolve
    hana "You gotta be..."
    "That last bit of information had Hana looking totally dejected."
    hana "I shouldn't be..."
    scene w2_6148 with dissolve
    chuck "Having her judge is a good idea. Our friends just know her as a serving girl, but putting her front-and-center tonight will cause them to remember her. The sooner the better if she does actually become a face for our club."
    aug "You're not wrong. She should experience what it's like to be responsible for another person's livelihood."
    scene w2_6149 with dissolve
    "Seeing Hana unhappily surrounded on all sides, made me want to...."
    scene w2_6150 with dissolve
    "{i}Yoink{/i}."
    mc "Don't you think you should ask Hana if she's okay with judging?"
    scene w2_6151 with dissolve
    chuck "........."
    scene w2_6152 with dissolve
    kat "......"
    scene w2_6153 with dissolve
    aug "..."
    scene w2_6154 with dissolve
    chuck "No one's forcing the lass into anything. Would you please help Kat tonight, Hana?"
    scene w2_6155 with dissolve
    "She looked at me with a resigned smile."
    scene w2_6156 with dissolve
    hana "...yeah."
    scene w2_6157 with dissolve
    hana "I did say I'd take a bigger interest in this place."
    scene w2_6158 with dissolve
    "Whether she ends up making changes for the better or just cashes out once she's got her share, this was her choice."
    scene w2_6159 with dissolve
    mct "(Just like me.)"
    scene w2_6160 with dissolve
    hana "I still think it's bullshit, but yeah, I'll \"judge\", whatever that means."
    scene w2_6161 with dissolve
    kat "Good! Good! Good!"
    scene w2_6162 with dissolve
    kil "What about us? You have anything for [mcf] and me to do?"
    scene w2_6163 with dissolve
    kat "Hmm, Ian, you can do your usual mingling or whatever it is you do."
    kat "[mcf] should work the crowd as well, but I want him to enjoy tonight to the fullest. Experience it from the perspective of a patron."
    scene w2_6164 with dissolve
    mc "I don't have a clue what that means."
    scene w2_6165 with dissolve
    kat "Enjoy our facilities, sample the girls, and be friendly with our guests. Most of it is what you'd do normally, but I want you to give me your opinion on it later next week."
    kat "What was lacking, what you found excellent, any ways we might improve our customer service? Give me your unique perspective."
    scene w2_6164 with dissolve
    mc "...okay, I can do that."
    "Sounded like she just wanted me to walk around."
    scene w2_6165 with dissolve
    kat "Good, then you two can get out of here and go socialize."
    scene w2_6166 with dissolve
    kil "Fine by me. Thanks for the drink."
    scene w2_6167 with dissolve
    hana "Hey, [mcf]... before you go..."
    mc "Yeah?"
    scene w2_6168 with dissolve
    hana "{b}Thanks{/b}."
    scene w2_6169 with dissolve
    mc "For what?"
    scene w2_6168 with dissolve
    hana "You know..."
    scene w2_6169 with dissolve
    "I did know."
    scene black with fade
    stop music fadeout 3.0
    mct "(Enjoy the pre-festivities as a patron, huh?)"
    "......"
    "..."
    jump w2ExHallway





screen w2ExNavMenu:
    if w2ExTimeBlock == "A":
        imagemap:
            idle "gui/screens/imagemaps/w2ExNavMenu1_idle.png"
            hover "gui/screens/imagemaps/w2ExNavMenu1_hover.png"
            ground "gui/screens/imagemaps/w2ExNavMenu1_ground.png"

            hotspot (321,85,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2ExAugustOffice")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            hotspot (736,56,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2ExBar")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            hotspot (311,367,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2ExSecurityRoom")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            hotspot (777,367,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2ExHallway")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            hotspot (10, 22, 180, 180) action [Play("menu_click","sound effects/page-turn.wav"), Return()] hovered [ Play ("hover_extra", "sound effects/click.wav") ]

    if w2ExTimeBlock == "B":
        imagemap:
            if w2ExSexRoomUnlock == True:
                idle "gui/screens/imagemaps/w2ExNavMenu3_idle.png"
                hover "gui/screens/imagemaps/w2ExNavMenu3_hover.png"
                ground "gui/screens/imagemaps/w2ExNavMenu3_ground.png"
            else:
                idle "gui/screens/imagemaps/w2ExNavMenu2_idle.png"
                hover "gui/screens/imagemaps/w2ExNavMenu2_hover.png"
                ground "gui/screens/imagemaps/w2ExNavMenu2_ground.png"

            hotspot (321,85,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2ExAugustOffice")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            hotspot (736,56,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2ExBar")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            hotspot (311,367,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2ExSecurityRoom")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            hotspot (777,367,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2ExHallway")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            if w2ExSexRoomUnlock == True:
                hotspot (1237,367,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2ExLezB")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            hotspot (311,668,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2ExVelvetRoom")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            hotspot (777,668,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2ExVIPLounge")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            hotspot (1238,668,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2ExVincenzoB")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            hotspot (10, 22, 180, 180) action [Play("menu_click","sound effects/page-turn.wav"), Return()] hovered [ Play ("hover_extra", "sound effects/click.wav") ]


label w2ExNavMenu:
    call screen w2ExNavMenu with pixellate




screen w2ExAugustOffice:

    imagemap:

        imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w2ExNavMenu")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]

        if w2ExTimeBlock == "A":

            idle "gui/screens/imagemaps/w2ExAugOfficeA_idle.png"
            hover "gui/screens/imagemaps/w2ExAugOfficeA_hover.png"
            ground "gui/screens/imagemaps/w2ExAugOfficeA_ground.png"
            hotspot (5,430,1200,800) action Jump("w2ExAugustA")

        if w2ExTimeBlock == "B":
            idle "gui/screens/imagemaps/w2ExAugOfficeB_idle.png"
            hover "gui/screens/imagemaps/w2ExAugOfficeB_hover.png"
            ground "gui/screens/imagemaps/w2ExAugOfficeB_ground.png"
            hotspot (1306,306,600,600) action Jump("w2ExAugustB")

label w2ExAugustOffice:
    show black
    $ renpy.music.play("music/study-and-relax.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w2ExAugustOffice with fade


label w2ExAugustA:

    if w2ExAugustARepeat == False:
        $ w2ExAugustARepeat = True

        scene w2_6170 with dissolve
        "Looks like the owners plan to keep Hana snared for longer still. Seeing her uncomfortably caught between the three of them was a pitiable sight, but there wasn't much I could do for her right now."
        "I should go kill time like I've been directed."
    else:
        scene w2_6171 with dissolve
        "I should go kill time like I've been directed."

    jump w2ExAugustOffice



label w2ExAugustB:

    if w2ExAugustBRepeat == False:
        $ w2ExAugustBRepeat = True

        scene w2_6172 with dissolve
        aug "What are you doing creeping around up here? You should be downstairs, enjoying yourself."
        scene w2_6173 with dissolve
        mc "I could say the same of you."
        scene w2_6174 with dissolve
        aug "I've had a lifetime of \"enjoying myself\", kid. Not that I think I'm old, but... I've learned to appreciate time by myself on nights like this."
        scene w2_6173 with dissolve
        mc "You mean exhibition nights?"
        scene w2_6172 with dissolve
        aug "No, I don't mean Kathy's dumb shows."
        scene w2_6173 with dissolve
        mc "... what then?"
        scene w2_6174 with dissolve
        aug "I just like to have some time to myself when I think I've gotten what I wanted."
        scene w2_6175 with dissolve
        mc "I should leave then."
        scene w2_6176 with dissolve
        aug "No, sit down. Let's chat. I'm not going to kick you out."
        scene w2_6177 with dissolve
        mc "...alright."
        stop music fadeout 3.0
        scene w2_6178 with dissolve
        aug "By the way, I know I asked you how you liked working here, but how do you like working with Kathy specifically?"
        scene w2_6179 with dissolve
        "He looked as if he was measuring me."

        if Kathleen_Trust >= 11:
            scene w2_6180 with dissolve
            mc "I've got no complaints. She's pretty straightforward and honest with her expectations."
            scene w2_6181 with dissolve
            aug "Is that right?"
        else:
            scene w2_6180 with dissolve
            mc "Just fine, I guess..."
            scene w2_6182 with dissolve
            aug "Just \"fine\", eh...?"

        scene w2_6183 with dissolve
        "......"
        scene w2_6184 with dissolve
        "..."
        mc "So you're up here, drinking alone, and thinking?"
        scene w2_6185 with dissolve
        aug "You make it sound awfully sad."
        scene w2_6184 with dissolve
        mc "No, I actually get it."
        scene w2_6186 with dissolve
        aug "Do you now?"
        scene w2_6187 with dissolve
        mc "It's like mental housekeeping. It's useful to sort your head out and put things in order."
        mc "If you're thorough about it, then you won't be surprised by your feelings. You're... thinking about Hana, right?"
        scene w2_6188 with dissolve
        aug "...ha."
        play music "music/crinoline-dreams.ogg"
        scene w2_6189 with dissolve
        aug "More and more these days. How'd you guess?"
        scene w2_6190 with dissolve
        mc "You told me as much. You {i}think{/i} you've gotten what you wanted, yeah?"
        scene w2_6191 with dissolve
        aug "I've found that getting what you want often leaves you unsatisfied if you just let your perceived successes fly by you without a second thought."
        aug "How much do you know about Hana's situation?"
        scene w2_6190 with dissolve
        mc "She's told me the rub of it, but you already knew that I think."
        scene w2_6191 with dissolve
        aug "I inferred as much from our conversation yesterday, but I wasn't sure."
        scene w2_6190 with dissolve
        aug "I bet the truth hasn't really painted me in a good light, huh?"
        mc "No one in this building is at risk of sainthood."
        scene w2_6192 with dissolve
        aug "Fwahaha, so true!"
        scene w2_6193 with dissolve
        aug "*Glug, glug, glug!*"
        scene w2_6194 with dissolve
        aug "More than a year ago, I set my daughter on the path of a criminal by leveraging her sick mother's illness against her."
        aug "Today she took another step down that path and thus I'm reflecting on my choices."
        scene w2_6195 with dissolve
        mc "I see. Are you happy with them?"
        scene w2_6196 with dissolve
        aug "Don't just come out and ask someone that, you jackass!"
        mc "Ha, sorry!"
        scene w2_6197 with dissolve
        aug "S'alright. I was begging the question."
        aug "Time will tell... ah fuck I'm dry."
        scene w2_6198 with dissolve
        aug "Pour your boss a drink, you lazy asshole!"
        scene black with fade
        mc "Aha, right away, sir!"
        "I shared a drink with the old man before politely excusing myself."
        "I think he appreciated me beating a retreat."
    else:


        scene w2_6199 with dissolve
        "I should give the man time alone with his thoughts."

    jump w2ExAugustOffice





screen w2ExBar:

    imagemap:

        imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w2ExNavMenu")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]

        if w2ExTimeBlock == "A":

            idle "gui/screens/imagemaps/w2ExBarA_idle.png"
            hover "gui/screens/imagemaps/w2ExBarA_hover.png"
            ground "gui/screens/imagemaps/w2ExBarA_ground.png"
            hotspot (161,275,200,600) action Jump("w2ExYooriA")
            hotspot (1594,412,600,250) action Jump("w2ExIsaakA")
            hotspot (440,230,400,800) action Jump("w2ExDaliaA")
            hotspot (840,161,600,400) action Jump("w2ExVeronicaMingleA")
            hotspot (1303,299,250,300) action Jump("w2ExSamsonA")

        if w2ExTimeBlock == "B":
            idle "gui/screens/imagemaps/w2ExBarB_idle.png"
            hover "gui/screens/imagemaps/w2ExBarB_hover.png"
            ground "gui/screens/imagemaps/w2ExBarB_ground.png"
            if w2ExYooriBRepeat == False:
                hotspot (1251,378,450,600) action Jump("w2ExYooriB")
            else:
                hotspot (154,265,200,600) action Jump("w2ExYooriB")

label w2ExBar:
    show black
    $ renpy.music.play("music/jazz-apricot.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w2ExBar with fade


label w2ExYooriA:

    if w2ExYooriARepeat == False:
        $ w2ExYooriARepeat = True
        scene w2_6200 with dissolve
        "It didn't occur to me, but..."
        scene w2_6201 with dissolve
        pp "What can I get you, sir?"
        scene w2_6202 with dissolve
        "I guess Hana would indeed need a replacement behind the bar."
        scene w2_6203 with dissolve
        mc "Hey, we haven't been introduced. I'm [mcf]."
        scene w2_6201 with dissolve
        yoori "Yoo-ri."
        scene w2_6204 with dissolve
        mc "They're asking a pregnant lady to tend the bar?"
        scene w2_6205 with dissolve
        yoori "I believe that was Mr. Byrnes' idea of a joke. Don't worry, I'm not drinking."
        scene w2_6204 with dissolve
        mc "He's an odd man..."
        scene w2_6206 with dissolve
        yoori "I'm not at liberty to agree."
        scene w2_6204 with dissolve
        "Short and to the point, she was a cautious one."
        scene w2_6207 with dissolve
        yoori "What can I get you, Mr. [mcl]?"
        scene w2_6204 with dissolve
        mc "Nothing. I'm just loitering."
        "......"
        "..."
        mc "Ah, well... goodbye, Yoo-ri."
        scene w2_6205 with dissolve
        yoori "Goodbye, sir."
    else:

        scene w2_6208 with dissolve
        "I don't feel like getting tipsy, so I really have no business with the expectant bartender. I should go kill time another way."

    jump w2ExBar

label w2ExIsaakA:

    if w2ExIsaakARepeat == False:
        $ w2ExIsaakARepeat = True

        scene w2_6209 with dissolve
        "In the corner, like a rat, sat Isaak."
        scene w2_6210 with dissolve
        isak "That's right, get a good feel of my junk. That's gonna be splitting open your fat ass later."
        scene w2_6209 with dissolve
        "He would've been utterly missable if not for the jiggle of Lucy's fat tits as she massaged the man's putrid-looking cock."
        scene w2_6210 with dissolve
        isak "Aren't you excited, Mrs. Long?"
        scene w2_6209 with dissolve
        "Lucy quietly acquiesced to the man's verbal abuse, a distant look on her face."
        scene w2_6211 with dissolve
        isak "Bah! That's the same expression as yesterday!"
        isak "You think you can treat me coldly just because we were at work?"
        scene w2_6212 with dissolve
        lucy "You don't get to touch me whenever you please, especially not at the Academy, Isaak."
        scene w2_6213 with dissolve
        isak "{b}Don't I{/b}? Don't you know your place yet?"
        lucy "...I'm well aware of what I agreed to."
        scene w2_6214 with dissolve
        isak "I don't know why you're so full of yourself. You've always been a prostitute, it just took awhile for your lifestyle to finally catch up to your diseased mentality."
        scene w2_6215 with dissolve
        lucy "T-that isn't true..."
        scene w2_6216 with dissolve
        isak "Honestly, I can't wait to look your husband in the eye at the next Christmas party, with the knowledge that his lovely wife is just a dime-a-dozen bitch."
        "The man's words irked me, but it's not like I could pull Lucy away from him. This was what she signed up for. Plus..."
        "I definitely wasn't going over there to say hello."
    else:
        scene w2_6217 with dissolve
        isak "What are you waiting for? Why don't you give it a kiss?"
        "I'll leave them to it."

    jump w2ExBar



label w2ExDaliaA:
    if w2ExDaliaARepeat == False:
        $ w2ExDaliaARepeat = True

        scene w2_6218 with dissolve
        "At the bar's side stood Dalia, badgering the same man she was domineering the previous week."
        dal "You brought all the things I asked you to, right Andrew?"
        "Her palm sat flat on the man's bald head, as if ruffling his nonexistent hair, while she cowed him with a well-practiced stern look."
        scene w2_6219 with dissolve
        drew "I did..."
        dal "...and the money too?"
        drew "Y-yeah..."
        scene w2_6220 with dissolve
        dal "You know that's all I see in you, right?"
        drew "I very much do..."
        scene w2_6221 with dissolve
        "Fascinated by their odd dynamic, I let my attention linger too long on the pair."
        scene w2_6222 with dissolve
        dal "Mr. [mcl]. Have you met Andrew?"
        scene w2_6223 with dissolve
        mc "We didn't get the chance to speak last week."
        scene w2_6224 with dissolve
        "The man seemed so diminutive next to Dalia, yet... "
        scene w2_6225 with dissolve
        dal "Introduce yourself, Andrew."
        scene w2_6226 with dissolve
        drew "It's good to meet, you Mr..."
        "His body language shifted on a dime. He stood tall and spoke clearly, proffering his hand like he had no doubt done thousands of times."
        scene w2_6227 with dissolve
        mc "[mcf]."
        scene w2_6228 with dissolve
        drew "It's good to meet you, Mr. [mcf]. I'm Andrew Reeves, the Ambassador of New Zealand to the United States."
        scene w2_6227 with dissolve
        mc "Ha... really..."
        mct "(An ambassador?)"
        scene w2_6229 with dissolve
        mc "Well, I... I hope tonight will further the relations of our two countries."
        mct "(Smooth, [mcf]..)"
        scene w2_6230 with dissolve
        drew "Ah, you can be very damn sure of that!"
        scene w2_6231 with dissolve
        drew "I was very lucky my schedule permits me to--"
        scene w2_6232 with dissolve
        dal "Andrew?"
        scene w2_6233 with dissolve
        drew "Ah, y-yes, Dalia?"
        "The man's posture changed on a dime once again."
        scene w2_6234 with dissolve
        dal "Now that you've been introduced, let's return to our previous topic."
        "Dalia shot me a look like she wanted me to go, which I was more than happy to."
        scene w2_6235 with dissolve
        drew "Well y-yeah, I carried the {i}ribbed{/i} one with me all day and I have your..."
        scene black with fade
        "This didn't seem like my sort of conversation."
    else:

        scene w2_6219 with dissolve
        mct "Let's leave the distinct pair to themselves for now."

    jump w2ExBar

label w2ExVeronicaMingleA:

    if w2ExVeronicaMingleARepeat == False:
        $ w2ExVeronicaMingleARepeat = True

        stop music fadeout 3.0
        scene w2_6291 with dissolve
        "In the far back, standing in the center of a ring of sitting patrons and their companions, stood Veronica clothed in her exhibition battle garb."
        "That is to say, her ridiculously pink princess lingerie."
        ver "Yeah, that's real commendable, you porcupine."
        mct "(...honestly, she was kinda making it work for her.)"
        jim "That's a new one."

        if w2ExRosalindMingleARepeat == True or w2ExFeliciaMingleARepeat == True:
            mct "(Looks like she had gathered quite the crowd, just like with Felicia and Rosalind.)"
        else:
            if kat_polite == True:
                mct "(I guess Mrs. Pulman has the Carnations out on the floor tonight, like actors in a stage play greeting their \"adoring\" audience.)"

        "I briefly considered not going over."
        "......"
        "..."
        mct "(Damn it, here I go.)"
        play music "music/cold-sober.ogg"
        scene w2_6292 with dissolve
        mc "Good afternoon, everyone."
        jim "Ah, it's you. Kathy's boy... [mcf]."
        "Our city's Chief of Police casually addressed me in return."
        scene w2_6293 with dissolve
        mc "I'm glad you remembered my name, Mr. O'Doherty. We only spoke briefly last week."
        scene w2_6294 with dissolve
        jim "You think I'd have trouble remembering a measly fuckin' name or something?"
        scene w2_6295 with dissolve
        shel "Come now, [mcf] didn't imply anything like that. He just means you're a small, conceited bastard."
        scene w2_6296 with dissolve
        mc "I didn't mean that either..."
        jim "Oh, yeah, and you're a real man of the people, right?"
        scene w2_6297 with dissolve
        vinc "...it's not hard to remember after you performed marvelously on stage last week."
        mc "I didn't really do much."
        scene w2_6298 with dissolve
        mc "It was the girls who did all the hard work. All I did was sit, stand, or lie down."
        scene w2_6299 with dissolve
        ver "Don't be so modest. The way you clung to Rosie's tit like a widdle baby was very moving."
        scene w2_6300 with dissolve
        "Veronica's calloused hands pushed down on my neck, as she brought herself back into the conversation."
        scene w2_6301 with dissolve
        mc "Again, I didn't really do all that much... besides going muff-diving and getting you to squirt everywhere."
        scene w2_6302 with dissolve
        jim "Ba, ha!"
        "She was forcing her character a bit, but I might as well play into my charge's hand."
        scene w2_6303 with dissolve
        vinc "Me? I would've been paralyzed with stage fright."
        scene w2_6304 with dissolve
        andrea "Stage fright? But you performed for over a thousand people last month, Enzo. What's half a dozen people compared to that?"
        scene w2_6305 with dissolve
        vinc "Heh, there's performances and then there's {i}performing{/i}. I know you're well aware of that difference, sweat pea. I watched your videos."
        scene w2_6306 with dissolve
        andrea "O-oh...? You did? Those old things?"
        scene w2_6307 with dissolve
        shel "Have you seen Emma around, [mcf]?"
        scene w2_6308 with dissolve
        mc "No, Mr. Shelby, I haven't."
        scene w2_6309 with dissolve
        "I recalled Hana's warning. This was the congressman that choked out Harper."
        scene w2_6308 with dissolve
        mc "I'll inquire about her for you."
        scene w2_6309 with dissolve
        "--I sure as shit wouldn't."
        scene w2_6310 with dissolve
        shel "I'd appreciate it. Next to Cassandra here, none of the other girls have as good of a ground game. She's got a... wiry build."
        scene w2_6311 with dissolve
        cass "Yeah... she can really whip her arms..."
        ver "{size=-10}Fuckin' weirdos...{/size=-10}"
        scene w2_6312 with dissolve
        shel "You were the one behind the camera for this beautiful creature's photoshoot this week, yes?"
        scene w2_6313 with dissolve
        jim "Beautiful? This bitch has spent the last five minutes insulting us."
        scene w2_6314 with dissolve
        mc "... I did. For each of the Carnations to be exact."
        scene w2_6315 with dissolve
        vinc "That was quite the package Kathleen sent us. Every single printed photo."
        scene w2_6316 with dissolve
        ver "You all got copies of that? Physical copies of... *ahem* my modeling?"
        scene w2_6317 with dissolve
        jim "What, you stupid or something? What did you think Kathy was going to do with the photos?"
        scene w2_6318 with dissolve
        jim "Say, want to come over here and earn my copy back by draining my nuts?"
        scene w2_6319 with dissolve
        ver "I'd rather bite off my fucking tongue, you sack of shit."
        scene w2_6320 with dissolve
        madi "There's no need for that bitch when I'm here, baby."
        scene w2_6321 with dissolve
        jim "Did I say you could touch me?"
        scene w2_6322 with dissolve
        madi "Ah-!"
        scene w2_6323 with dissolve
        shel "Point is, those photos were splendid work."
        scene w2_6324 with dissolve
        mc "If it turned out great, it was all because of the model."
        scene w2_6325 with dissolve
        ver "Yeah, and which shoot did you like best, congressman?"
        scene w2_6326 with dissolve
        shel "Of course, I voted for you, dear. Your legs are the size of my fucking head."
        scene w2_6327 with dissolve
        ver "...hmpfh."
        shel "I dream of what you'll do with them."
        scene w2_6328 with dissolve
        mc "... so, are you gentleman finding everything to your satisfaction tonight?"
        "I came back around to the reason I approached in the first place, to perfunctorily perform my role as a representative of the club."
        scene w2_6329 with dissolve
        shel "Yes, except for that one refusing to sit with us."
        scene w2_6330 with dissolve
        ver "I prefer to stand and you prefer the view, don't you?"
        "It seemed Veronica had her own unique spin on socializing."
        scene w2_6331 with dissolve
        vinc "Haaa! It's like looking at Brünnhilde made flesh."
        andrea "Uh, who?"
        scene w2_6332 with dissolve
        vinc "A queen who resided over the sea, whose like no one knew of anywhere."
        vinc "She was exceedingly beautiful and great in physical strength."
        scene w2_6333 with dissolve
        andrea "A-ah...!"
        vinc "She shot the shaft with the bold knights - love was the prize."
        andrea "O-oh, Vincenzo...!"
        scene w2_6334 with dissolve
        ver "...oooookay."
        scene w2_6335 with dissolve
        ver "Please for the love of everything beneath the sky, {b}shoot me dead{/b}."
        scene w2_6336 with dissolve
        mc "I'm afraid I can't help you there, Brünnhilde. The powers that be would frown on your untimely demise."
        scene w2_6337 with dissolve
        mc "Hang in there."
        ver "Fuck..."
        scene w2_6338 with dissolve
        mc "Besides the seating arrangements, is everything good?"
        scene w2_6339 with dissolve
        shel "You can tell Kathleen that the club's service is exemplary, as usual."
        scene w2_6338 with dissolve
        mc "I'll pass that along."
        scene black with fade

        mc "...well, then, I will excuse myself."
        "I didn't want to take a squat either, to be frank."
    else:

        scene w2_6291 with dissolve
        mct "(I've already done my \"hello\"s and \"how-are-you\"s over there. I should mingle elsewhere.)"

    jump w2ExBar


label w2ExSamsonA:

    if w2ExSamsonARepeat == False:

        scene w2_6236 with dissolve
        "Over on the red couch, saddled up next to Harper and Nicolette, was Samson. He really did have a type."
        "With how relentless the man is, I might get pulled into something time-consuming. Should I go over there now?"
        hide screen textbox2 with dissolve

        menu:
            "Go over and say hello.":
                $ w2ExSamsonARepeat = True
                $ w2ExTimeBlock = "B"
                show screen textbox2 with dissolve
                if VeroFlag == True:
                    mct "(Well, I do need to be friendly if I hope to get any more information out of him regarding how he sabotaged Veronica.)"
                else:
                    mct "(Hey, being friendly is my job, right?)"

                scene w2_6237 with dissolve
                sam "Heya, kid."
                mc "You're a greedy man, aren't you Mr. Garcia?"
                sam "Oh, you mean...?"
                scene w2_6238 with dissolve
                sam "Bahahaha, damn straight I am! If I could I'd have them all to myself!"
                scene w2_6239 with dissolve
                "I shot Harper what I hoped was a sympathetic look, as the boisterous man shouted with zero regard for the girls' ears."
                scene w2_6240 with dissolve
                mc "Wouldn't we all?"
                scene w2_6239 with dissolve
                "It was just the beginning of the night and he looked moderately intoxicated..."

                if VeroFlag == True:
                    mct "(Maybe I could use that to my advantage?)"
                    "I didn't know what I would do with the information I sought, or how that might help Veronica, but the first step was obtaining it."

                scene w2_6241 with dissolve
                sam "Indeed! Although..."
                scene w2_6242 with dissolve
                "Samson's eyes unsubtly drifted to where Veronica stood."
                sam "Difficult women that make you work for it carry their own unique brand of flavor."
                mc "Right, yeah..."
                mct "(Is that what you call sabotaging a person's livelihood?)"
                stop music fadeout 3.0
                hide screen textbox2 with dissolve
                scene w2_6243 with dissolve
                sam "Want to sit down and join me? Greedy as I am, I do know how to share--"
                play sound "sound effects/thud-floor.mp3"
                scene w2_6244 with vpunch
                "*Thud*"
                scene w2_6245 with dissolve
                isak "No need to get up. Crawl and get me a drink, will you? And be sure to come back with a smile, too."
                scene w2_6246 with dissolve
                "I didn't see it, but I could make a pretty good guess how Lucy wound up on the bar room floor."
                lucy "I--!"
                scene w2_6247 with dissolve
                lucy "Yes, sir."
                scene w2_6248 with dissolve
                isak "Aha, that's a nice change of tone."
                scene w2_6249 with dissolve
                harp "How about I get you that drink instead? Lucy is very inexperienced, Mr. Miller."
                scene w2_6250 with dissolve
                "Having pulled herself away from the greedy bodybuilder's grasp, Harper inserted herself between the pair."
                harp "I'll treat you much better than she can."
                scene w2_6251 with dissolve
                show screen textbox2 with dissolve
                isak "No thanks, I'm actually quite happy to teach her."
                scene w2_6252 with dissolve
                harp "No, really, I'll do any--"
                scene w2_6253 with dissolve
                isak "You're too skanky for my tastes."
                play music "music/jack-the-lumberer.ogg"
                scene w2_6255 with dissolve
                dal "Lucy!"
                dal "You're \"ornament\"-duty tonight! Chelsea called out last minute."
                harp "{size=-10}Chelsea...?{/size=-10}"
                "There was no Chelsea on the staff. Even if Isaak didn't know that, the timing made it an obvious lie."
                dal "You know how finicky Mrs. Pulman is with her arrangements. Will you take her to the Velvet Room to get strapped in, Harper?"
                scene w2_6256 with dissolve
                dal "I'm so sorry, Mr. Miller. Why don't you join us for that drink?"
                isak "Just--"
                "Just as Isaak started to interject and raise an issue..."
                scene w2_6257 with dissolve
                ver "You like pushing women to the ground, do you?"
                scene w2_6258 with dissolve
                "Face-to-face, Isaak looked extremely small next to the towering woman."
                scene w2_6259 with dissolve
                isak "I, y-you, what--"
                scene w2_6260 with dissolve
                ver "What are you, a damn fish?"
                scene w2_6259 with dissolve
                isak "Y-you--"
                scene w2_6260 with dissolve
                ver "Before you start with that \"watch how you speak to me\" bullshit, I'll remind you that I don't work here, pipsqueak."
                ver "I'm free to call a pathetic, balding loser for what he is, and you are a {b}very{b} pathetic, fat, balding, limp-dicked loser."
                scene w2_6261 with dissolve
                sam "Bahaha, oh come on Veronica, don't bully the little guy."
                scene w2_6262 with dissolve
                ver "Don't think I didn't see you impotently jerk that small dick of yours while I was on stage a few weeks ago. Or, actually..."
                scene w2_6263 with dissolve
                ver "Ha, maybe I didn't see it?"
                "Veronica's intrusion was just what was needed to allow Harper and Lucy to exit the bar without further protest."
                scene w2_6264 with dissolve
                isak "...you're {i}funny{/i}, I'll give you that."
                "Despite being clearly flustered, he tried to coolly play it off."
                isak "It'll be amusing to see that smirk wiped off your face."
                scene w2_6265 with dissolve
                ver "Bah, why the hell do all you jackasses say the same thing?"
                scene w2_6266 with dissolve
                "With Lucy gone, Veronica beat a prudent retreat."
                scene w2_6267 with dissolve
                ver "This shithead spewed the same garbage."
                "If she had made a calculated performance just now, the smiling faces in the back told me she had succeeded. Everyone but Isaak seemed genuinely amused by her tenacity."
                scene w2_6268 with dissolve
                ver "{size=-10}He wants to wrestle me. Like, what the fuck?{/size=-10}"
                stop music fadeout 3.0
                scene w2_6269 with dissolve
                sam "Ha, he slinked off! God I love that woman!"
                "Veronica aside, I was starting to have an understanding of the dynamic between the house girls."
                play music "music/jazz-apricot.ogg"
                scene w2_6270 with dissolve
                mc "I don't think she feels the same."
                "Harper didn't hesitate to jump in and Dalia covered their retreat."
                scene w2_6271 with dissolve
                sam "I wouldn't want her to. She's playing a once-in-a-lifetime part that has been tailored for her."
                scene w2_6272 with dissolve
                "Samson sounded proud, no doubt imagining himself the writer of that role in his cinematically-chosen metaphor."

                if VeroFlag == True:
                    mct "(Now's the time.)"
                    "If I wanted to get to the bottom of Samson's responsibility in the decline of Veronica's gym, this was the opportunity."
                    scene w2_6273 with dissolve
                    mc "Hey, Mr. Garcia..."
                    "The aging movie star was half-drunk and high on his \"muse's\" fiery display of grit. I was confident he'd spill the beans with the right push."
                    mc "Why don't you go and get another drink and then you and I can hit the sauna?"
                    scene w2_6274 with dissolve
                    sam "What, just you and me? No thanks, kid. I don't swing that way anymore."
                    scene w2_6275 with dissolve
                    mc "No, you idiot. Bring your lady friend."
                    mc "We'll kick back and enjoy ourselves."
                    scene w2_6276 with dissolve
                    sam "Alright, sure, but you gotta tell me how you managed to put a collar on that bitch over there without losing any fingers, deal?"
                    scene black with fade
                    mc "It's a deal."
                    scene w2_6277 with fade
                    "Like I hoped, Samson made his way to the bar first."
                    mct "(The more liquored up, the better.)"
                    scene w2_6278 with dissolve
                    dal "Let me accompany you, Mr. [mcl]. It's not right for you to be unattended."
                    dal "Don't want to be a third wheel, do you?"
                    scene w2_6279 with dissolve
                    mc "That's alright, the night's not really about my pl--"
                    scene w2_6280 with dissolve
                    dal "Please?"
                    "Dalia leaned in and spoke in a whisper just for me."
                    scene w2_6281 with dissolve
                    dal "I want to keep an eye on Nico, alright?"
                    scene w2_6282 with dissolve
                    dal "It's her first night. I'm worried she might have jumped into the deep end too soon."
                    "She looked anxious, but there was a genuine concern in her voice."
                    mc "...yeah, sure, come with. I'm not going to turn down your lovely company."
                    "I brought our conversation back to a normal volume."
                    scene w2_6283 with dissolve
                    mc "What about him?"
                    scene w2_6284 with dissolve
                    dal "Andrew? Who cares?"
                    scene w2_6285 with dissolve
                    dal "Quite frankly, I'm getting sick of toying with him."
                    dal "He's painfully boring."
                    scene w2_6286 with dissolve
                    "Her \"toy\" looked down in shame, but from where I stood, I could see a smile forming on his lips."
                    scene black with fade
                    stop music fadeout 3.0
                    "After encouraging and sharing one more drink with Samson, the four of us - Dalia, Nicolette, and myself included - made our way to the building's sauna."
                    jump w2ExSauna
                else:

                    scene w2_6287 with dissolve
                    sam "Want to sit down?"
                    scene w2_6288 with dissolve
                    "I weighed my options..."
                    scene w2_6289 with dissolve
                    mc "Sure thing."
                    "Samson was the more manageable of the groups."
                    scene w2_6290 with dissolve
                    mc "I've been told to kill some time."
                    scene black with fade
                    "So we did. I listened to the has-been yak, avoided drinking, and made one-sided small-talk with Nicolette until I couldn't stand it anymore and excused myself."
                    "......"
                    "..."
                    jump w2ExVeronicaHanaB
            "Go mingle elsewhere first.":


                show screen textbox2 with dissolve
                mct "I'll look around the upper floors some more first."
                jump w2ExBar




label w2ExYooriB:

    if w2ExYooriBRepeat == False:
        $ w2ExYooriBRepeat = True
        scene w2_6340 with dissolve
        "Coming back to the bar, I found it much, much, much less packed. Guess everyone migrated downstairs for the most part."
        "All except for the pregnant bartender, currently taking a load off on one of the club's big red sofas."
        scene w2_6341 with dissolve
        yoori "O-oh!"
        yoori "Uh... I was just..."
        scene w2_6342 with dissolve
        yoori "No one was here, so..."
        scene w2_6343 with dissolve
        mc "Relax, don't get up."
        scene w2_6344 with dissolve
        yoori "I know I shouldn't be, it's just--"
        scene w2_6345 with dissolve
        mc "{b}Seriously{/b}. I'm just killing time."
        mc "I'm not here to bust your ovaries over you resting your back."
        scene w2_6344 with dissolve
        yoori "... so you don't want a drink or anything extra?"
        scene w2_6345 with dissolve
        mc "What, are you on tap too -- ah, don't answer that."
        mc "No, I don't want a drink. I'm just sticking my head in."
        scene w2_6344 with dissolve
        yoori "...and you're not gonna report this to Mr. Byrnes?"
        scene w2_6346 with dissolve
        mc "What would I report, exactly?"
        scene w2_6347 with dissolve
        yoori "That I was..."
        mc "Lying down on the job?"
        scene w2_6348 with dissolve
        yoori "Heh, that's a funny thing to say about a prostitute."
        mc "In that case, my silence is dependent on one thing."
        scene w2_6349 with dissolve
        yoori "...on what?"
        mc "You not reporting me for slacking off either."
        scene w2_6350 with dissolve
        yoori "Ah...?"
        scene w2_6351 with dissolve
        yoori "...it's a deal!"
        scene w2_6352 with dissolve
        mc "... so like what are you, seven months along?"
        scene w2_6353 with dissolve
        yoori "That's right. Halfway to eight."
        scene w2_6354 with dissolve
        "......"
        "..."
        scene w2_6355 with dissolve
        mc "...and they still got you working, huh?"
        scene w2_6356 with dissolve
        yoori "There's a... {i}call{/i} for that sort of thing. It limits my client pool, but it's a {i}premium{/i} service."
        scene w2_6355 with dissolve
        mc "I've been filled in on that a little actually."
        scene w2_6356 with dissolve
        yoori "I think Mr. Byrnes is taking pity on me by assigning me here tonight."
        scene w2_6355 with dissolve
        mc "You think? I guess pouring drinks is a pretty comfy gig compared to the other alternative."
        scene w2_6356 with dissolve
        yoori "Yeah, dunno why, but he's been in a more pleasant mood this week."
        scene w2_6357 with dissolve
        yoori "He even asked me how the baby was doing."
        "That seemed like a pretty low bar."
        scene w2_6358 with dissolve
        yoori "...you're, uh... Ian's friend too, right?"
        scene w2_6359 with dissolve
        mc "Too? I thought I was his only friend."
        scene w2_6360 with dissolve
        yoori "You don't know Darius?"
        scene w2_6359 with dissolve
        mc "No, I've only heard of him, and it mostly was about him running off."
        mc "What was he like?"
        scene w2_6358 with dissolve
        yoori "He was..."
        "She hesitated, cautious of putting the truth plainly."
        scene w2_6361 with dissolve
        yoori "He was what you'd expect from a man his age, I guess -- working in a place like this I mean. He was wild and a bit full of himself."
        scene w2_6360 with dissolve
        yoori "He wasn't as bad as he could've been. Isla had a real big soft spot for him and he got better over time."
        scene w2_6359 with dissolve
        mc "Is Isla one of the girls?"
        scene w2_6360 with dissolve
        yoori "Former. She left about a month or so before Darius did."
        scene w2_6361 with dissolve
        yoori "She had worked here for two years. I guess her account was settled."
        scene w2_6359 with dissolve
        mc "I see..."
        scene w2_6363 with dissolve
        yoori "{b}You{/b} seem pretty decent so far, [mcf]."
        scene w2_6362 with dissolve
        mc "I do? We've only exchanged a few words."
        scene w2_6364 with dissolve
        yoori "Uh huh. Whores have a sixth sense about people. You're decent."
        scene w2_6363 with dissolve
        yoori "Plus, you're sitting here and having a normalish conversation with me."
        scene w2_6362 with dissolve
        "The bar now felt like it was touching the floor."
        scene w2_6366 with dissolve
        yoori "It's kinda cute how you're sitting at a polite, respectful distance."
        scene w2_6367 with dissolve
        mc "I'm not a customer. You can cut the bullshit."
        scene w2_6368 with dissolve
        yoori "Hmpfh. What an insensitive thing to say to a woman."
        scene w2_6363 with dissolve
        yoori "You should ask me to teach you the intricacies of a woman's heart sometime. I'm a pretty good teacher if I say so myself."
        scene w2_6364 with dissolve
        yoori "Despite how I look, I was the club's top earner."
        scene w2_6362 with dissolve
        "Ian's words of caution appropriately came to mind."
        mc "I should get back to work. Those old farts aren't gonna kiss their own asses."
        scene w2_6365 with dissolve
        yoori "Mmh, ignored!"
        scene black with fade
        "Again... Ian's words of caution came to mind."
        yoori "Thanks for talking with me, [mcf]."
        jump w2ExBar
    else:

        scene w2_6208 with dissolve
        "It was nice being away from the building's bustle, but I should check in on some other places."
        jump w2ExBar




screen w2ExSecurityRoom:

    imagemap:

        imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w2ExNavMenu")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]

        if w2ExTimeBlock == "A":

            idle "gui/screens/imagemaps/w2ExSecurityRoomA_idle.png"
            hover "gui/screens/imagemaps/w2ExSecurityRoomA_hover.png"
            ground "gui/screens/imagemaps/w2ExSecurityRoomA_ground.png"
            hotspot (801,383,600,600) action Jump("w2ExWarrenA")

        if w2ExTimeBlock == "B":
            idle "gui/screens/imagemaps/w2ExSecurityRoomB_idle.png"
            hover "gui/screens/imagemaps/w2ExSecurityRoomB_hover.png"
            ground "gui/screens/imagemaps/w2ExSecurityRoomB_ground.png"
            hotspot (600,383,600,600) action Jump("w2ExJacobB")


label w2ExSecurityRoom:
    show black
    $ renpy.music.play("music/i-knew-a-guy.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    if w2ExWarrenARepeat == True and w2ExTimeBlock == "A":
        call screen w2ExSecurityRoom with fade
    elif w2ExWarrenARepeat == False and w2ExTimeBlock == "A":
        jump w2ExWarrenA
    else:
        call screen w2ExSecurityRoom with fade




label w2ExWarrenA:

    if w2ExWarrenARepeat == False:
        $ w2ExWarrenARepeat = True

        scene w2_6370 with dissolve
        war "What do you want, kid?"
        scene w2_6369 with dissolve
        "The moment I peaked into the security room, the faint conversation I had heard from behind the door immediately ceased and two sets of harsh eyes fell upon me."
        mc "Sorry for disturbing you. I was just poking my head in to say hello."
        scene w2_6370 with dissolve
        war "You takin' a tour? That's a bad habit for around here."
        scene w2_6371 with dissolve
        jiji "You should be more cordial with the men you work with."
        scene w2_6372 with dissolve
        war "Hey, I'm fuckin' friendly okay? That was just some helpful advice."
        scene w2_6373 with dissolve
        jiji "Nice night, isn't it, [mcf]?"
        scene w2_6369 with dissolve
        mc "It's a tad humid."
        scene w2_6374 with dissolve
        mc "How do you do, Mr. Jameson? Are all your needs being taken care of?"
        scene w2_6375 with dissolve
        "Annoyed by Warren's standoffishness, I pushed into the room and did my job."
        scene w2_6376 with dissolve
        jiji "Not yet."
        scene w2_6377 with dissolve
        jiji "I should find myself some more fetching company."
        scene w2_6378 with dissolve
        war "Then why are you botherin' me, old man? Go find a girl and underwhelm her."
        scene w2_6379 with dissolve
        mc "I think you hurt his feelings, sir."
        scene w2_6380 with dissolve
        jiji "Unlikely. All {i}Sandman{/i} knows how to do is breathe, shit, eat, fight, and {b}fuck{/b}."
        scene w2_6381 with dissolve
        war "Hey!"
        scene w2_6382 with dissolve
        war "I'm workin' on a journal of poetry. Wanna see it?"
        scene w2_6383 with dissolve
        jiji "Actually, I'm leaving. Nice catching up with you, Al."
        scene black with fade
        war "Have a good time, sir."
        scene w2_6389 with dissolve
        "Leaving just the two of us alone, Warren suddenly felt more intimidating."
        scene w2_6390 with dissolve
        war "You sure like it in here, don't you kid?"
        scene w2_6391 with dissolve
        mc "What are you implying?"
        scene w2_6392 with dissolve
        war "Someone accessed the feed yesterday. You."
        scene w2_6393 with dissolve
        mc "I was looking for Dr. Chuck."
        scene w2_6394 with dissolve
        war "You ever heard of a phone?"
        scene w2_6393 with dissolve
        mc "Should I not have done that?"
        scene w2_6394 with dissolve
        war "No, it's fine. So long as you..."
        scene w2_6395 with dissolve
        war "...didn't see anything you shouldn't have."
        scene w2_6396 with dissolve
        mc "What could I possibly see that's worse than the illegal prostitution and weird, disturbing fetishes?"
        scene w2_6397 with dissolve
        war "Hmmm... ha! I'm just busting your balls. Feel free to pop in and people watch all you want."
        war "Mi casa es tu casa, eh?"
        scene w2_6398 with dissolve
        "If that was the case, why even bring it up? I have a feeling that he just wanted me to know he knew."
        scene w2_6399 with dissolve
        mc "I wasn't people watch--"
        scene w2_6400 with dissolve
        war "Then, you ever heard of a phone?"
        scene w2_6401 with dissolve
        mc "Ah, fuck. You got a point. Fair enough."
        mct "(That was the more fun way of doing it, wasn't it?)"
        scene black with fade
        war "Do \"pop\" your head in again, kid. I gotta learn to be more cordial, I guess."
    else:

        scene w2_6388 with dissolve
        mct "(That's enough Warren for one evening. The guy gives me the heebie jeebies.)"

    jump w2ExSecurityRoom



    label w2ExJacobB:

        if w2ExJacobBRepeat == False:
            $ w2ExJacobBRepeat = True
            scene w2_6738 with fade
            if w2ExWarrenARepeat == True:
                "Despite Warren's vague suspicion, or maybe because of it, I once again stuck my head into the security room."
                "I just couldn't help myself."
            else:
                "I decided to poke my head in the security room."

            scene w2_6739 with dissolve
            mc "Hey Jacob. You're posted up here now, huh?"
            scene w2_6740 with dissolve
            jacob "Yup. Just watching the feeds."
            scene w2_6741 with dissolve
            mc "Looks more like you're reading."

            if w2ExVincenzoB1 == False and w2ExVincenzoB2 == False:
                $ w2ExVincenzoB1 = True
                scene w2_6745 with dissolve
                "Click"
                scene w2_6742 with dissolve
                jacob "Well, a little Dostoyevsky helps to mercifully distract from Vincenzo's jiggling fat rolls as he rolls the dice on dying of a heart attack."
                mct "(Note to self... avoid the pool.)"
                mc "You make a persuasive case for literacy."

            elif w2ExVincenzoB1 == True and w2ExVincenzoB2 == False:
                $ w2ExVincenzoB2 = True
                scene w2_6746 with dissolve
                "Click"
                scene w2_6743 with dissolve
                jacob "Well, a little Dostoyevsky helps to mercifully distract from Vincenzo's jiggling fat rolls as he rolls the dice on dying of a heart attack."
                mct "(He brought another girl into the mix? Damn, dude's a machine...)"
                mc "You make a persuasive case for literacy."

            elif w2ExVincenzoB1 == True and w2ExVincenzoB2 == True:
                scene w2_6747 with dissolve
                "Click"
                scene w2_6744 with dissolve
                jacob "Well, a little Dostoyevsky helps to mercifully distract from Vincenzo's jiggling fat rolls as he rolls the dice on dying of a heart attack."
                mct "(He's taking a lap after all that?!)"
                mc "You make a persuasive case for literacy."

            scene w2_6748 with dissolve
            jacob "You need something?"

            if w2ExSearch == True:
                $ w2ExSexRoomUnlock = True
                scene w2_6749 with dissolve
                mc "You have any idea where Harper and maybe Lucy are?"
                scene w2_6751 with dissolve
                jacob "...?"
                scene w2_6752 with dissolve
                mc "Dalia's asking."
                scene w2_6753 with dissolve
                jacob "Rockstar room."
                scene w2_6754 with dissolve
                jacob "I'm keeping the feed off, out of respect."
                scene w2_6755 with dissolve
                mc "Thanks, Jacob."
                jacob "Sure, no problem. Just remember to knock first."
            else:
                scene w2_6749 with dissolve
                mc "Nope, just checking in."
                mc "...and I've checked. See you around."
                scene w2_6750 with dissolve
                jacob "See you around, [mcf]."

            jump w2ExSecurityRoom

        if w2ExJacobBRepeat == True:
            scene w2_6738 with fade
            "Let's not disturb Jacob's Russian-lit time anymore, eh?"
            jump w2ExSecurityRoom








screen w2ExHallway:

    imagemap:

        imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w2ExNavMenu")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]

        if w2ExTimeBlock == "A":


            idle "gui/screens/imagemaps/w2ExHallwayA1_idle.png"
            hover "gui/screens/imagemaps/w2ExHallwayA_hover.png"
            if w2ExRosalindMingleARepeat == False:
                ground "gui/screens/imagemaps/w2ExHallwayA1_ground.png"
                hotspot (1408,341,600,600) action Jump("w2ExRosalindMingleA")
            else:
                ground "gui/screens/imagemaps/w2ExHallwayA2_ground.png"


            hotspot (801,383,600,600) action Jump("w2ExJacobA")
            hotspot (61,375,600,600) action Jump("w2ExFeliciaMingleA")

        if w2ExTimeBlock == "B":
            idle "gui/screens/imagemaps/w1ExHallwayB_ground.png"
            hover "gui/screens/imagemaps/w1ExHallwayB_ground.png"
            ground "gui/screens/imagemaps/w1ExHallwayB_ground.png"




label w2ExHallway:
    show black
    $ renpy.music.play("music/cello-suite-No-1-G-Major-Prelude.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w2ExHallway with fade




label w2ExJacobA:

    if w2ExJacobARepeat == False:
        $ w2ExJacobARepeat = True

        scene w2_6402 with dissolve
        jacob "You finished with the powers-that-be?"
        scene w2_6403 with dissolve
        mc "Yeah, thankfully that didn't take too long. Things seemed pretty weird between Mrs. Pulman and Mr. Byrnes."
        scene w2_6402 with dissolve
        jacob "I don't know anything about that. They usually stay out of each other's way."
        scene w2_6403 with dissolve
        mc "Want to take a stab at why that might be?"
        "It couldn't hurt for me to get a sense of the internal politics of this place."
        scene w2_6404 with dissolve
        jacob "Sometimes in life, the less you understand, the better. In this case..."
        scene w2_6405 with dissolve
        jacob "I dunno. They're friendly enough, but I wouldn't say they jibe."
        scene w2_6406 with dissolve
        jacob "They're from different backgrounds, you get it? Dr. Kohler is what bridges the two."
        scene w2_6407 with dissolve
        mc "They both enjoy the \"work\" though, right? That's something."
        scene w2_6408 with dissolve
        jacob "Maybe they all do have the same glitch in their software, but beats me."
        scene w2_6409 with dissolve
        mc "Hmmm....?"
        scene w2_6408 with dissolve
        jacob "Yeah, what is it?"
        scene w2_6410 with dissolve
        mc "How'd you end up working here, Jacob?"
        scene w2_6408 with dissolve
        jacob "Same as you, [mcf]."
        scene w2_6407 with dissolve
        mc "You mean you knew somebody?"
        scene w2_6406 with dissolve
        jacob "Yeah, {b}I knew somebody{/b}. After coming back from overseas I did odd jobs here and there. Nothing I'm proud of, but nothing I'm ashamed of either."
        scene w2_6408 with dissolve
        jacob "I worked with somebody who knew Mr. Byrnes. We met one day and he made me an offer. He thought I was funny."
        scene w2_6410 with dissolve
        mc "Tell me a joke."
        scene w2_6411 with dissolve
        jacob "Knock, knock."
        scene w2_6412 with dissolve
        mc "Who's there?"
        scene w2_6413 with dissolve
        jacob "Fuck you."
        scene w2_6409 with dissolve
        mc "I'll have to remember that one."
        "......"
        "..."
        scene w2_6402 with dissolve
        jacob "...say, can I ask you a favor?"
        scene w2_6403 with dissolve
        mc "Sure, what is it?"
        scene w2_6402 with dissolve
        jacob "One of the girls - Emma - is having a rough n' tumble sort of week. She got bad news about her dad and then -- ah, well, would you mind looking out for her tonight?"
        scene w2_6403 with dissolve
        mc "It's a big place with a lot of private rooms. That's next to impossible."
        scene w2_6404 with dissolve
        jacob "Yeah, fuck I know, but..."
        scene w2_6414 with dissolve
        jacob "I'm worried about her up here."
        scene w2_6415 with dissolve
        jacob "She's tough-as-nails, more than I am, but we're talking about going ten rounds of boxing here."
        scene w2_6416 with dissolve
        jacob "Sometimes you eat a glancing blow and your legs turn to jelly."
        scene w2_6417 with dissolve
        "This wasn't necessarily my job, but on the face of it, what he was asking didn't really require me to do much beyond keep an eye out. Conversely..."
        mct "(I could also take it a step further for Jacob. I was told to act like a patron of the club tonight. I could use that to my advantage...)"
        hide screen textbox2 with dissolve

        menu:
            "Take it further and use your position to help Jacob out."(chg=["jacob_up"]):
                $ Jacob_Friendship += 1
                $ w2ExEmmaFavor = "promised"

                scene w2_6410 with dissolve
                show screen textbox2 with dissolve
                mc "I'll do you one better. If I see her, I'll give her the night off."
                scene w2_6408 with dissolve
                jacob "I've already asked Dalia about that. That's a no-go."
                scene w2_6407 with dissolve
                mc "You were talking about sending her home, but there's more creative ways of giving her some \"R 'n R.\""
                scene w2_6405 with dissolve
                jacob "... yeah? I wouldn't want either of you to get into trouble."
                scene w2_6384 with dissolve
                mc "It should be fine - for her definitely and for me probably. Don't worry!"
                scene w2_6385 with dissolve
                jacob "...I'll owe you one, then?"
                scene w2_6386 with dissolve
                mc "Sure. Maybe you'll have a better joke for me next time?"
                mc "No promises, however. I don't think there's much I can do if she's snatch deep on some rich creep's junk, but I will try."
                scene w2_6385 with dissolve
            "Agree to his simple favor.":

                $ w2ExEmmaFavor = "watched"
                scene w2_6407 with dissolve
                show screen textbox2 with dissolve
                mc "It's not much, but yeah, I'll keep my eyes and ears open."
                scene w2_6408 with dissolve

        jacob "Colorful... but, thanks, man. I appreciate it."
        scene black with fade
        mc "See you around, Jacob."
    else:

        scene w2_6387 with dissolve
        mct "(I should let the man do his job... of standing around.)"

    jump w2ExHallway

label w2ExRosalindMingleA:
    $ w2ExRosalindMingleARepeat = True

    if _in_replay:
        play music "music/cello-suite-No-1-G-Major-Prelude.ogg"
        show screen textbox2 with dissolve

    scene w2_6418 with dissolve
    "Off to the side, not hogging as much attention as Felicia, was Rosalind."
    mihir "So few sexual partners, really?"
    rose "Heh, well, I married in college so..."
    mihir "You're quite the bold woman, Mrs. Carter."
    scene w2_6420 with dissolve
    rose "Please, just call me Rose. Carter is my married name and... ah..."
    scene w2_6421 with dissolve
    tom "Are you currently lactating, Rose?"
    scene w2_6422 with dissolve
    rose "N-no, my daughter's twelve. It's been a long--"
    scene w2_6423 with dissolve
    tom "That's alright. All it would take is the right stimulation to get you flowing again."
    tom "I'd like to see that. You have very enticing breasts, Rose."
    scene w2_6424 with dissolve
    rose "Oh, um... t-thank you, Mr...?"
    scene w2_6425 with dissolve
    mc "Mr. Thomas Blake."
    rose "Ah, [mcf]...!"
    "She looked happy to see a familiar face, even if it was mine."

    if w1ExGame2LoserRose == True:
        scene w2_6426 with dissolve
        tom "I'm a little hurt you don't remember me. We met face-to-face last week during the last game."
        rose "O-oh... right you were..."
        scene w2_6444 with pixellate
        tom "I'm so glad I got to be first to soil those beautiful breasts of yours..."
        scene w2_6427 with pixellate
        rose "So we did, Mr. Blake."
        scene w2_6428 with dissolve
    else:
        scene w2_6428 with dissolve
        tom "That's right, I wanted to speak with you personally last week, but I never got the chance."

    tom "I'll have you know, I'm pulling for you to win this year."
    scene w2_6429 with dissolve
    rose "Thank you..."
    scene w2_6430 with dissolve
    mihir "We haven't met."
    scene w2_6431 with dissolve
    mc "No, we didn't get a chance last week, Mr. Chatterjee."
    scene w2_6432 with dissolve
    mihir "I see you've taken care to learn everyone's name."
    scene w2_6433 with dissolve
    "That was true. After last week, I made sure I was well-acquainted with the club's members."
    scene w2_6434 with dissolve
    mc "Of course."
    scene w2_6433 with dissolve
    "Mihir Chatterjee was the Dean of Allerton University."
    scene w2_6434 with dissolve
    mc "It's part of the job. I'm at your service."
    scene w2_6433 with dissolve
    "Where St. Ives Academy was the premier institution for secondary education in the tri-state area, Allerton likewise shared that same sterling reputation as a university. The parents of students I tutored to get into the first, often had their eyes set on Allerton in the horizon."
    scene w2_6432 with dissolve
    mihir "There's no need to suck up so hard, sir."
    scene w2_6433 with dissolve
    "The fact that the club had their claws in both places, represented by Isaak and Mihir respectively, was quite telling."
    scene w2_6435 with dissolve
    mihir "Thomas and I aren't like Mr. Wong over there. We have nothing to prove."
    scene w2_6436 with dissolve
    mc "I get it. I'd hate that too if I were you."
    scene w2_6437 with dissolve
    mc "I still haven't gotten acquainted with everyone's... *ahem* {i}preferences{/i}."
    scene w2_6438 with dissolve
    rose "Mrs. Pulman encouraged us to mingle with the guests, but she was very explicit that we weren't allowed to be touched."
    scene w2_6439 with dissolve
    tom "Ah... that's... unfortunate, but I understand. I hope you'll forgive the impropriety. It's just..."
    scene w2_6440 with dissolve
    rose "I have very enticing breasts?"
    scene w2_6441 with dissolve
    tom "You stole the words from my mouth."
    scene w2_6442 with dissolve
    mct "(He's not allowed to touch, eh...?)"
    hide screen textbox2 with dissolve

    menu:
        "Demonstrate Rosalind's sensitivity in the customer's stead."(chg=[("rosalind_passion_up", roseFlag == False), ("rosalind_passion_up2", roseFlag and Rosalind_Affection < 25), ("rosalind_passion_up3", roseFlag and Rosalind_Affection >= 25), ("kathleen_trust_up", roseFlag and Rosalind_Affection >= 25)]):
            $ Rosalind_Libido += 1
            $ w2ExRosalindKissDemo = True
            stop music fadeout 3.0
            scene w2_6443 with dissolve
            mc "Am I allowed to touch?"
            rose "Umm... she didn't say..."
            play music "music/helping-hands.ogg"
            scene rosa_e2_tw1_a with dissolve
            show rosa_e2_tw1
            tom "Oh...?!"
            rose "What are you...?"
            "Slinking behind Rose, I scooped up a handful of titflesh and began to knead it in an exaggerated fashion."
            mc "Allow me to put on a demonstration for the two of you, Mr. Blake."
            rose "A demonstration? What could you--"
            mc "Looking is fine right? Let's give our esteemed guests a good view of what it looks like when your cow tits are poked and prodded."
            "I wasn't sure if I was acting out of an impulse to lord the perks of my position over the tackily-dressed man or if I simply did it out of a desire to provide good \"service\"..."
            mc "You know... let them hear what sounds you make when they're groped and teased."
            mct "(Okay, I knew the answer to that as clear as day.)"
            rose "A-aht... I guess... Mrs. Pulman didn't say anything against l-looking..."
            "It was absolutely, without a doubt, the first one. It was fun to show off like Rosalind belonged to me, even if that wasn't true."
            mihir "This is rather unorthodox."
            scene rosa_e2_tw2_a with dissolve
            show rosa_e2_tw2
            mc "Note how large and {b}pliable{/b} they are. Heavy too."
            mc "The right kind of hefty. Comforting, warm, and safe. Like a blanket, {b}safe{/b}."
            mc "Inviting, like a mother's bosom."
            "I chose my words deliberately, ones fit for a lactation maniac like Thomas."
            mihir "Hmmpfh. Very nice."
            tom "You're teasing me, Mr. [mcl]."
            mc "Not true. I just wanted to give you a demonstration."
            rose "Ah, mmnfh...!"
            mc "They're so damn sensitive. She's too easy, right?"
            tom "No, she's perfect."
            mc "I think so too, Mr. Blake. She's got the finest rack out of all the Carnations, doesn't she?"

            if roseFlag == True:
                $ Rosalind_Libido += 1
                scene rosa_e2_tw3_a with dissolve
                show rosa_e2_tw3
                rose "Wahhaaaa, s-shoot... why..."
                "*Chup, fwhup~*"
                "Without really thinking about it, I planted a series of small kisses in quick succession on her cheek."
                "*Fwup, chwup, thwup...!*"
                rose "Aaaht, t-tickles...!"
                "My fingertips teased her areola, coaxing the pale pink protuberance to a fine point, and then brushed its outer edges with rough precision."
                "With any luck, the way I was grabbing her from behind would remind her of not long ago, when we fucked in her kitchen and desperately clung to one another in a bid for pleasure."
                rose "Mffaaah~"
                tom "She has a lovely voice."
                mihir "We heard it last week, Tom."
                tom "Yeah, but not this close... {b}so lovely...{/b}."

                if Rosalind_Affection >= 25:
                    $ Rosalind_Libido += 1
                    $ Kathleen_Trust += 1
                    "What started out as something exhibitory, brought out by my twisted desire to tease Rosalind for a viewing audience, had inadvertently consumed my own passion."
                    "I was no longer hearing the peanut gallery. I had no clue what Thomas' dumb expression might be right now."
                    "Instead, I became focused entirely on Rosalind. My cock pressed hard into the mother's cow-print covered ass, the gentle sway of her body sending waves of pleasure down my legs."
                    rose "Nehhh...! I t-think--"
                    scene w2_6464 with dissolve
                    rose "Aht...!"
                    tom "Marvelous!"
                    scene rosa_e2_tw4_a with dissolve
                    show rosa_e2_tw4
                    "*Chup, fwhup~*"
                    mc "You think they got the point?"
                    rose "Sfhtt... n-no? I mean... y-yes?"
                    "*Fwup, chwup, thwup...!*"
                    mc "Which is it?"
                    rose "Mmhhh...! Ahhh, [mcf]..."
                    rose "Mmmh..."

                    if Rosalind_Affection >= 30 or Rosalind_Libido >= 12:
                        $ Rosalind_Libido += 1
                        mc "Don't be afraid to really let them hear you--"
                        scene w2_6465 with dissolve
                        mct "(Oh!)"
                        "Of her volition, to my surprise in the fog of lust, Rosalind cocked her neck and planted a kiss on my lips."
                        "A nice, passionate kiss. More lip and less tongue, but nonetheless like a lover."
                        rose "Mmmh...."
                        "I didn't expect her to take my words so seriously."
                        scene rosa_e2_tw4_a with dissolve
                        show rosa_e2_tw4
                        rose "H-haat..."
                        "It was, as usual, all too brief."
                    else:
                        mc "Don't hold back. Don't be afraid to let them hear you moan."
                        rose "Hnng, haaa...!"

                    rose "...h-how did this suddenly happen?"
                    rose "I was just... ha, answering... q-questions..."
                    stop music fadeout 3.0
                    scene w2_6466 with dissolve
                    mc "...ah, ha... um, so..."
                    "Abruptly, I pulled away."
                    scene w2_6467 with dissolve
                    mc "...I hope you voted her as having the best photoshoot this week."
                    scene w2_6468 with dissolve
                    rose "Ha... ha..."
                    "Marketing Rose like she was a product was a specific sort of thrill, but I was becoming drunk on lust by this point, and taking it any further would have me needing release."
                    mihir "I believe we both did."
                    scene w2_6469 with dissolve
                    rose "A-ah..! O...oh? Ah..."
                    scene w2_6470 with dissolve
                    rose "T-thank you, both."
                    scene w2_6471 with dissolve
                    tom "Certainly."
                    scene w2_6472 with dissolve
                    play music "music/cello-suite-No-1-G-Major-Prelude.ogg"
                    show screen textbox2 with dissolve
                    tom "Ha! ...and thanks for the \"demonstration\" you jerk-bastard."
                    mc "It was my pleasure."
                    scene w2_6473 with dissolve
                    mihir "I can see why Mrs. Pulman has you working here. You two work well together."
                    mc "You think, ah?"
                    mihir "Truly."
                else:


                    play music "music/cello-suite-No-1-G-Major-Prelude.ogg"
                    scene w2_6474 with dissolve
                    show screen textbox2 with dissolve
                    mc "I hope you voted her as having the best photoshoot this week."
                    "Abruptly, I pulled away."
                    scene w2_6475 with dissolve
                    rose "Ha... ha..."
                    "Marketing Rose like she was a product was a specific sort of thrill, but I had more than my fill. I was getting turned on by this point, and I didn't exactly want to deal with an erection right now."
                    mihir "I believe we both did."
                    scene w2_6476 with dissolve
                    rose "A-ah..! T-thank you, both."
                    tom "Certainly."
                    scene w2_6477 with dissolve
                    tom "Ha! ...and thanks for the \"demonstration\" you jerk-bastard."
                    mc "It was my pleasure."
            else:


                play music "music/cello-suite-No-1-G-Major-Prelude.ogg"
                scene w2_6478 with dissolve
                show screen textbox2 with dissolve
                mc "I hope you voted her as having the best photoshoot this week."
                "Abruptly, I pulled away."
                scene w2_6479 with dissolve
                rose "Ha... ha..."
                "Marketing Rose like she was a product was a specific sort of thrill, but I had my fill. The longer it went on, the more I risked getting turned on myself."
                mihir "I believe we both did."
                scene w2_6480 with dissolve
                rose "A-ah..! T-thank you, both."
                tom "Certainly."
                scene w2_6481 with dissolve
                tom "Ha! ...and thanks for the \"demonstration\" you jerk-bastard."
                mc "It was my pleasure."

            $ renpy.end_replay()
            scene w2_6445 with dissolve
            if not persistent.roseW2Sgrope:
                play sound "sound effects/notification.wav"
                show memoryunlock with dissolve
                $ renpy.pause(3, hard=True)
                $ persistent.roseW2Sgrope = True
                hide memoryunlock with dissolve
                $ renpy.pause(0.5, hard=True)

            mihir "Say, Thomas, would you like to join me downstairs, in the Velvet Room? Kathleen mentioned featuring entertainment there tonight."
            scene w2_6446 with dissolve
            tom "Ah... it is a shame to say goodbye, but the longer I stay, the stronger my longing will be."
            scene w2_6447 with dissolve
            tom "Excuse me, Rose."
            scene w2_6448 with dissolve
            rose "It was... \"nice\" meeting you, Mr. Blake. Mr. Chatterjee."
            scene w2_6449 with dissolve
            "......"
            scene w2_6450 with dissolve
            "..."
            scene w2_6482 with dissolve
            rose "They voted for me!"
            rose "Yes!"
            scene w2_6483 with dissolve
            mc "That's a cute reaction, considering the subject..."
            scene w2_6484 with dissolve
            rose "I'm glad you came over, [mcf]."
            scene w2_6483 with dissolve
            mc "You are? Even after I...?"
            scene w2_6484 with dissolve
            rose "I am."
        "Keep your hands to yourself.":

            show screen textbox2 with dissolve
            "I decided to let the dirty idea remain just that. A dirty idea."
            $ renpy.end_replay()
            scene w2_6445 with dissolve
            mihir "Mmh, hmpfh. Would you... care to join me downstairs, Thomas?"
            mihir "I hear there's some entertainment provided in the Velvet Room."
            scene w2_6446 with dissolve
            tom "Ah... it is a shame to say goodbye, but the longer I stay, the stronger my longing will be."
            scene w2_6447 with dissolve
            tom "Excuse me, Rose."
            scene w2_6448 with dissolve
            rose "It was... \"nice\" meeting you, Mr. Blake. Mr. Chatterjee."
            scene w2_6449 with dissolve
            "......"
            scene w2_6450 with dissolve
            "..."
            scene w2_6485 with dissolve
            rose "*Sigh* I'm glad you came over."
            scene w2_6486 with dissolve
            mc "You are?"


    scene w2_6485 with dissolve
    rose "It's weird, but being asked to talk with these men puts me more in a tizzy than being on stage."
    scene w2_6486 with dissolve
    mc "You rather get your ass blasted in front of a crowd than do a little bit of talking?"
    scene w2_6487 with dissolve
    rose "I'm not saying that! It's just, well..."

    if w2ExRosalindKissDemo == True:
        scene w2_6488 with dissolve
        rose "All I'm sayin' is that was more enjoyable than having to pretend I was interested in those men's questions..."
        scene w2_6489 with dissolve
        rose "Take that as you will."

    scene w2_6490 with dissolve
    "......"
    "..."
    scene w2_6486 with dissolve

    if kat_polite == True:
        mc "So Mrs. Pulman has you working the floor, huh?"
    else:
        mc "So Kathleen has you working the floor, huh?"

    scene w2_6491 with dissolve
    rose "Only for a little bit, before everyone moves downstairs."
    scene w2_6486 with dissolve
    mc "Makes sense. Last week she waited for the introductions, but now she wants you to win over some fans I take it."
    scene w2_6492 with dissolve
    rose "That's... ridiculous."
    "I didn't say anything else, but I agreed."
    scene w2_6493 with dissolve
    rose "Well, I'm going to go find someplace quiet, where hopefully I'll attract less attention..."
    scene w2_6494 with dissolve
    mc "I don't think that's likely, but good luck."
    scene w2_6493 with dissolve

    if roseFlag == True:
        rose "See you later, [mcf]."
    else:
        rose "See you later, Mr. [mcl]."

    scene w2_6494 with dissolve
    mc "Bye, Rose."
    jump w2ExHallway



label w2ExFeliciaMingleA:

    if w2ExFeliciaMingleARepeat == False:
        $ w2ExFeliciaMingleARepeat = True

        stop music fadeout 3.0
        scene w2_6451 with dissolve
        frank "Hey, [mcf]! Get your big-dick-having ass over here!"
        mc "Ummm, excuse me?"
        "I was waved over in a concerning, overly-familiar way."
        play music "music/plans-in-motion.ogg"
        scene w2_6452 with dissolve
        mc "...how can I help you Mr. Grenier?"

        if w2ExRosalindMingleARepeat == False:
            mct "(I guess the old woman has them out socializing during the pre-game.)"

            "Looks like Felicia is fairing better than Rosalind over there."

        scene w2_6453 with dissolve
        fel "Hiya stud."
        scene w2_6454 with dissolve
        frank "I need your help settling something between Waylon and me."
        mc "What are you....?"
        scene w2_6455 with dissolve
        frank "Whip your cock out real quick, would 'ya?"
        scene w2_6456 with dissolve
        "......."
        "..."
        scene w2_6457 with vpunch
        mc "...no?!"
        scene w2_6458 with dissolve
        eric "Come on, it's not what you think. We just want to see it up close to settle a wager."
        scene w2_6459 with dissolve
        mc "...do you think that {i}actually{/i} adds context to your request, Mr. Waylon?"
        scene w2_6460 with dissolve
        frank "It's not like we haven't seen it before."
        scene w2_6461 with dissolve
        cel "I haven't."
        merc "Neither have I, actually."

        if w1GonzoReward == True or w2HarpRainCheck == False:
            merc "Harper said you were packing, though. I kinda want to see it myself."

        scene w2_6462 with dissolve
        fel "It's, um..."
        scene w2_6463 with dissolve
        fel "...this big?"
        scene w2_6495 with dissolve
        eric "See? Looks like I was right."
        frank "Nothing's been proven yet, you git."
        scene w2_6496 with dissolve
        mc "I'm sorry, what are you trying to prove?"
        scene w2_6497 with dissolve
        frank "Waylon here thinks you got a bigger cock than I do and I want to prove this one way or the other."
        scene w2_6496 with dissolve
        mc "Is that right..."
        scene w2_6498 with dissolve
        fel "They've been talking about this since you walked in the room..."
        fel "Will you please settle this? I'm trying to make an impression here and all they want to do is talk about your cock."
        scene w2_6499 with dissolve
        frank "C'mon, what do you say? Let's prove who's got the mightier cock!"
        scene w2_6500 with dissolve
        frank "It's good to know the pecking order!"
        scene w2_6501 with dissolve
        merc "The {i}pecker{/i} order!"
        scene w2_6502 with dissolve
        "......"
        "..."
        scene w2_6503 with dissolve
        mc "I, uh... gah--"
        hide screen textbox2 with dissolve

        menu:
            "Be proud of your junk, take it out!"(chg=["felicia_up2"]):
                $ w2ExWhippedOut = True
                $ Felicia_Affection += 2

                stop music fadeout 2.0
                "It was a bizarre situation, but I learned last week on stage that I'm not exactly cock-shy."
                mct "(Was doing stupid shit like this part of my job schmoozing these pricks?)"
                play music "music/rifts-for-days.ogg"
                scene w2_6504 with dissolve
                mc "Alright, alright... stand back. Make room."
                "Whatever."
                scene w2_6505 with dissolve
                mc "No matter the outcome, you promise not to bear a vendetta against me, right?"
                scene w2_6506 with dissolve
                frank "On my honor as a gentleman."
                scene w2_6505 with dissolve
                mc "...{b}do{/b} you consider yourself a gentleman, Mr. Grenier?"
                scene w2_6507 with dissolve
                eric "Bah! Ha!"
                frank "Oh, you cocky son of a bitch! You sound like Kristoff."
                play sound "sound effects/zipper.wav"
                scene black with fade
                "*Ziiiiiiiip*"
                scene w2_6508 with dissolve
                mc "*Sigh* Well... here it is."
                scene w2_6509 with dissolve
                frank "Hmm..."
                scene w2_6510 with dissolve
                eric "He's got you beat, asshole."
                scene w2_6511 with dissolve
                frank "We don't know that. He's flaccid."
                frank "He could be ALL show, y'know..."
                scene w2_6512 with dissolve
                merc "I think you have him beat, hun."
                scene w2_6513 with dissolve
                frank "Yeah? You think so? I thought so myself, but..."
                frank "I can't be certain. Go wake him up, will 'ya?"
                scene w2_6514 with dissolve
                merc "Sure thing."
                scene w2_6515 with dissolve
                merc "Excuse me, Mr. [mcl]..."
                "I had already gone along with this absurd situation, swatting the busty woman's hand away would just be meaningless grandstanding."
                scene w2_6516 with dissolve
                mc "Go ahead."
                scene e2_mercf_a with dissolve
                show e2_mercf
                "The call girl's fingers gently coiled around my manhood, while her lotion-smooth palm gently caressed my shaft."
                "......"
                "..."
                "For a dozen seconds she worked my flaccid cock to no avail. I stayed soft in her hands, but she continued undaunted, an impatient look in her eye."
                "It was no use. I had thought it was no big deal, but on stage I had some distance. Having these old fucks just a few feet away really put a damper on my vitality..."
                "......"
                "..."
                scene w2_6517 with dissolve
                mc "Sorry, it's no good. Maybe if..."
                scene w2_6518 with dissolve
                merc "That's okay, hun. I'll use my--"
                stop music fadeout 3.0
                scene w2_6519 with dissolve
                fel "I'll do it."

                if feliciaSugarBaby == True:
                    "My would-be sugar mama stepped between Mercedes and me, creating some distance."
                    scene w2_6520 with dissolve
                    fel "I think I got a pretty good handle on [mcf]'s little guy."
                    scene w2_6521 with dissolve

                elif feliciaFlag == True:
                    "Felicia stepped between Mercedes and me, creating some distance."
                    scene w2_6520 with dissolve
                    fel "I think I got a pretty good handle on [mcf]'s little guy."
                    scene w2_6521 with dissolve
                else:
                    scene w2_6520 with dissolve
                    fel "You don't mind me giving it a try, do you Mr. [mcl]?"
                    scene w2_6521 with dissolve
                    "I shook my head no."

                eric "This should be interesting."
                scene w2_6522 with dissolve
                "Instead of grabbing my cock, Felicia took her time, placing an affectionate hand on my chest and turning a needy eye up into my own."
                play music "music/dancebroom-riddim.ogg"
                scene fel_e2_stare_a with dissolve
                show fel_e2_stare
                eric "What are you waiting for, an invitation?"
                "Felicia ignored the man and remained fixated on me."
                fel "Hmm..."
                "Her hand played along my chest, her claw-like hand tickling my breast even through the fabric of my shirt."
                "The pattern she drew sent chills up my spine, like she was scratching an itch I didn't know I had."
                scene w2_6523 with dissolve
                "All the while, she wordlessly bewitched me with her eyes. Every breathy exhale, fluttering lash, and lip bite magically creating a feeling of anticipation in my chest."
                "She would look like she wanted to say something, but on the cusp of it coming out, she would force it back down much to my frustration."
                scene fel_e2_stare_a with dissolve
                show fel_e2_stare
                "Instead, her hand drew up my breast, fingertips circling my nipple and coaxing it to a fine point."
                mct "(What did she want to say? What was she going to say?)"
                "By this point I had forgotten all about Frank and Eric."
                "I had forgotten about Mercedes and Celine."

                if w2ExRosalindMingleARepeat == True:
                    "I had forgotten about Rosalind, who was off to the side, whose attention could very well be focused on me right now."

                fel "Mmmh...?"
                "She started, but again stopped."
                mct "(Say something!)"
                scene w2_6524 with dissolve
                fel "Mmmh, get hard for me baby."
                scene w2_6525 with dissolve
                "To my amazement, that was all it took. My cock was standing proud."
                "Perhaps it had slowly gotten that way while Felicia teased me, but the first I became aware of it was the moment she broke her spell."
                scene w2_6526 with dissolve
                fel "Looks like [mcf] still had a little bit to show after all. You want to take yours out and compare, Frank?"
                stop music
                play sound "sound effects/record-scratch.wav"
                scene w2_6527 with dissolve
                frank "...I decline. I gotta be honest, I knew he had me beat the moment he pulled it out."
                frank "I just wanted to see how far he was willing to take it."
                scene w2_6528 with dissolve
                "......."
                "..."
                play sound "sound effects/zipper.wav"
                scene black with fade
                "*Ziiiiiiip*"
                $ renpy.end_replay()
                play music "music/cello-suite-No-1-G-Major-Prelude.ogg"
                scene w2_6529 with fade
                show screen textbox2 with dissolve
                mc "*Sigh* I'm glad to be of entertainment."
                frank "C'mon, don't be cross, [mcf]. We got to know each other better is all!"
                scene w2_6530 with dissolve
                eric "...and I feel like I got five grand richer."
                frank "Still, that was fuckin' impressive! She didn't even touch your cock!"
                scene w2_6531 with dissolve
                frank "I thought you were better than that. Hell, I know you're better than that."
                scene w2_6532 with dissolve
                eric "Have you ever tried tantric sex?"
                scene w2_6533 with dissolve
                fel "No, what's the fun in that? The point of sex is to cum."
                scene w2_6532 with dissolve
                eric "That's surprising, you seem like..."
                "Frank and Eric began a round of twenty questions with Felicia, asking her all about her life. Where she was born, what she liked doing, and much more dirty ones too."
                "She lied often, but that wasn't here or there, but with a slowly softening half-chub in my pants, this was my chance to slip away unceremoniously."
                scene black with fade
                if not persistent.felW2grope:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.felW2grope = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)

                "Silver lining of me feeling like an idiot, at least Felicia seemed to have made a favorable impression."
            "This is fucking weird. No thanks."(chg=["tough_up2"]):


                $ toughness += 2
                stop music
                play sound "sound effects/record-scratch.wav"
                scene w2_6534 with dissolve
                show screen textbox2 with dissolve
                mc "I'm not taking my cock out just to settle a bet."
                frank "......"
                play music "music/cello-suite-No-1-G-Major-Prelude.ogg"
                scene w2_6535 with hpunch
                "The bald man gave me a hearty slap on the back."
                frank "...ha, it's good you have some self-respect!"
                mc "You weren't giving me any credit, huh?"
                $ renpy.end_replay()
                scene w2_6536 with dissolve
                frank "Guess our bet is a wash, Eric."
                eric "Bah, I would've won."
                frank "Fat chance, I've got the biggest cock in this place. Where were we before we got distracted?"
                scene w2_6537 with dissolve
                eric "We were... right."
                scene w2_6538 with dissolve
                eric "How often do you and your husband fuck?"
                fel "What kind of question is that?"
                scene black with fade
                "Frank and Eric began a round of 20 questions with Felicia, asking her all about her life. Where she was born, what she liked doing, and much more dirty ones too."
                "I saw this as the opportunity to unceremoniously slip away from the dick-curious pair."
    else:

        if w2ExWhippedOut == True:
            scene w2_6539 with dissolve
            "I think I've embarrassed myself enough, thank you very much."
            "...At least until the exhibition begins. Let's find something else to do."
        else:
            scene w2_6539 with dissolve
            "I don't think I want to go back over there. Let's find something else to do."

    jump w2ExHallway



label w2ExVeronicaHanaB:

    play music "music/cold-sober.ogg"

    if VeroFlag == True:
        scene w2_6629 with blinds
        "After getting dressed, I split up from Samson. I had gotten what I wanted out of the oaf, but I still had no idea how I might help Veronica get her business back on track."
        "I should've known when I impulsively decided to look into Veronica's manufactured hardship that it wouldn't be something a student could easily unravel..."
        mct "(Speak of the devil...)"
    else:


        scene w2_6629 with blinds
        "After whiling away my time in the bar, balancing making myself a known quantity as per Mrs. Pulman's instructions with staying at the periphery of the conversations, people gradually moved downstairs."
        "I took my time, but eventually I found myself making that same migration. Along the way..."


    scene w2_6630 with dissolve
    "In the hallway stood Hana and Veronica - the odd pair having a seemingly low-key conversation."

    scene w2_6631 with dissolve
    mc "I see you BOTH escaped."
    scene w2_6632 with dissolve

    if VeroFlag == True:
        ver "{b}Thankfully{/b}. Everyone moved downstairs and now that old bitch wants us elsewhere."
    else:
        ver "Yeah, I'm done socializing with those parasites for now. Thankfully that old cunt wants us elsewhere."

    scene w2_6633 with dissolve
    mc "What is she having you do now? You're already..."
    scene w2_6634 with dissolve
    mc "...{b}dressed{/b}."
    scene w2_6635 with dissolve
    ver "Beats me. Guess we're on stand-by for tonight."
    scene w2_6636 with dissolve
    mc "What about you? What's the old lady got you doing?"
    scene w2_6637 with dissolve
    hana "Sitting on my hands, but I wanted to..."
    hana "I wanted to meet the girls."
    scene w2_6636 with dissolve
    mc "You've never spoken with any of them before?"
    scene w2_6637 with dissolve
    hana "No... never saw the point, but since I'm going to be..."
    scene w2_6638 with dissolve
    hana "Well, Veronica's the first I ran into."
    scene w2_6639 with dissolve
    ver "Actually..."
    scene w2_6640 with dissolve
    ver "I'm still not sure who you are, cutie. You're the bartender, right?"
    scene w2_6641 with dissolve
    hana "Actually, as of tonight, I'm not sure what I am. At the very least, I'm August's daughter."
    hana "Please don't hold that against me."
    scene w2_6642 with dissolve
    ver "...who's August?"
    scene w2_6643 with dissolve
    mc "Ha!"
    hana "He's the old fuck with the gaudy suits, glasses, and slicked-back hair."
    scene w2_6644 with dissolve
    ver "Ah, {b}him{/b}..."
    scene w2_6645 with dissolve
    "Veronica eyed the rocker girl with apparent suspicion."
    scene w2_6644 with dissolve
    ver "Your pops has you working at a whore-house?"
    scene w2_6646 with dissolve
    hana "It's complicated, but yeah."
    scene w2_6644 with dissolve
    ver "If you don't mind me saying, that's real fucked up."
    scene w2_6646 with dissolve
    hana "You're singing to the choir."
    scene w2_6645 with dissolve
    ver "..."
    "As friendly as Hana tried to sound, Veronica didn't look like she knew what to make of her."
    scene w2_6647 with dissolve
    hana "Soooooooo.... I guess that's it... just wanted to say hello..."
    ver "...?"
    scene w2_6648 with dissolve
    ver "Ha!"
    "Veronica's standoffishness gave way to relief, much to Hana's surprise."
    ver "You look out of place, y'know?"
    scene w2_6649 with dissolve
    hana "More than that dweeb?"
    scene w2_6650 with dissolve
    ver "Way more than him."
    "I think I preferred Hana's assessment of my character over Veronica's. The way the Amazon was looking at me right now was too... {i}cutting{/i}."
    scene w2_6651 with dissolve
    mc "Oh...! I wanted to say: nice one in the bar earlier. You made that worm look small."
    scene w2_6652 with dissolve
    hana "What happened?"
    mc "She stepped in on a house girl's behalf."
    scene w2_6653 with dissolve
    ver "Eh? I didn't do it for that poor woman."
    ver "In fact, I probably made things indirectly worse for her."
    scene w2_6654 with dissolve
    mc "You think?"
    scene w2_6653 with dissolve
    ver "He's just going to be angrier with her in the long run and next time she'll be short on convenient excuses."
    scene w2_6654 with dissolve
    mc "Then why'd you step in like that?"
    scene w2_6653 with dissolve
    ver "...because I'm an impulsive, self-aggrandizing cunt?"
    scene w2_6654 with dissolve
    mc "Is that you bashful about doing something nice?"
    scene w2_6655 with dissolve
    ver "...it's not like my feet moved on their own. Those men I was talking with didn't respect that baldy, you understand?"
    ver "I could tell by their body language and the way they spoke, so..."
    scene w2_6656 with dissolve
    ver "I guess I made a positive impression while doing what the hell I wanted?"
    scene w2_6657 with dissolve
    mc "Give yourself more credit."
    scene w2_6658 with dissolve
    ver "I should go. Maybe I'll see you around, Hana?"
    hana "Oh... you will."
    stop music fadeout 3.0
    scene black with fade
    "With a half-assed wave, Veronica departed, leaving me alone in familiar company."
    scene w2_6659 with dissolve
    hana "Why is she here?"
    scene w2_6660 with dissolve
    mc "You didn't see that part last week, huh?"

    if kat_polite == True:
        mc "Mrs. Pulman made a big show about it."
    else:
        mc "Kathleen made a big show about it."

    scene w2_6661 with dissolve
    hana "No, I popped in while you were face deep in her--"
    scene w2_6662 with dissolve
    mc "I remember!"
    scene w2_6663 with dissolve
    mc "Considering you're judging the show tonight, do you really want to know?"
    scene w2_6664 with dissolve
    hana "...ah, I--"
    scene w2_6665 with dissolve
    hana "You're right. Tell me afterwards, okay?"
    scene w2_6666 with dissolve
    mc "Sure. Try not to think about things too much tonight, okay?"
    scene w2_6665 with dissolve
    hana "Is that how you manage it?"
    scene w2_6667 with dissolve
    "I didn't answer that question."
    scene w2_6668 with dissolve
    mc "If you can't manage that, just remember you'll have a friend by your side tonight. I mean..."
    scene w2_6669 with dissolve
    mc "...I mean... ah, you might not like what I'm asked to do during the exhibition, but--"
    scene w2_6670 with dissolve
    hana "I'll get over it."
    mc "Where you going next?"
    scene w2_6671 with dissolve
    hana "I'm going to go find the other two and do that same awkward dance. You?"
    scene w2_6672 with dissolve
    mc "Heading downstairs. Seems that's where the \"fun\" is."
    scene w2_6673 with dissolve
    hana "I guess that's a good \"good-fucking-bye\" as any."
    scene black with fade
    mc "Good-fucking-bye, Hana."

    if jacobHarpVouch or w2HarpRainCheck or VeroFlag == True:
        $ w2ExSearch = True
        scene w2_6726 with fade
        play music "music/cello-suite-No-1-G-Major-Prelude.ogg"
        dal "Mr. [mcl]?"
        scene w2_6727 with dissolve

        if VeroFlag == True:
            "I turned around to find myself greeted by the woman I had just brutishly blown my wad in."
            scene w2_6728 with dissolve
            mc "Ah, Dalia..."
            scene w2_6727 with dissolve
            "My lack of self-consciousness about it almost made me feel self-conscious. This was my life now."
            scene w2_6729 with dissolve
            mc "I didn't expect to see you again so soon. Sorry if I got a bit too rough back there, I was..."
            scene w2_6730 with dissolve
            dal "Do not worry about it. It's none of my business why you were humoring Samson or what you talked about."
            scene w2_6728 with dissolve

        mc "How can I help you, Dalia?"
        scene w2_6731 with dissolve
        dal "If you see Harper and Lucy, would you please tell them to stop fucking around?"
        scene w2_6732 with dissolve
        mc "Fucking around...?"
        scene w2_6731 with dissolve
        dal "It's just a strong suspicion I have. Harper's smart, and the most professional girl I have, but with Nicolette taking up Samson's attention... ah, well..."
        scene w2_6732 with dissolve
        mc "While the cat's away?"
        scene w2_6731 with dissolve
        dal "Keep this between us?"
        scene w2_6732 with dissolve
        mc "Alright. If I see them, I'll pass along the message."
        scene w2_6733 with dissolve
        dal "I'd honestly prefer you put the fear of God into them as part of the management staff, but if you just want to simply \"pass it along\", then I would appreciate that all the same."
        scene w2_6734 with dissolve
        mc "...ah."
        "Her choice of words was interesting."
        scene w2_6735 with dissolve
        dal "You seem alright so far, so I'm sticking my neck out a little by asking for your help with this instead of just reporting it to Mr. Byrnes."
        dal "I've got nine other girls besides them to go watch out for, you understand?"
        scene black with fade
        "I understood."

    jump w2ExHallway



label w2ExSauna:

    mc "Mmmhh...! You... don't have to do that, Dalia."
    dal "If I don't, I have no purpose for being here. Do you catch my meaning?"
    play music "music/devious-little-smile.ogg"
    scene w2_6540 with wet
    mc "Ah... well, it does feel good..."
    hide screen textbox2 with dissolve
    scene w2_6541 with dissolve
    "Dalia helped me undress myself better than even I could've. Now, we were just waiting for Samson and Nicolette to join us."
    scene w2_6542 with dissolve

    if w2HarpRainCheck == True:
        dal "You're not afraid of the girls, are you?"
        scene w2_6541 with dissolve
        "In the meantime, she diligently started on giving me a massage - a prelude for things to come most likely."
        scene w2_6543 with dissolve
        mc "What do you mean by that?"
        scene w2_6544 with dissolve
        dal "Mrs. Pulman offered Harper up to you on a stick and you turned her down."
    else:

        dal "Besides, I know you're not one to turn down a good time."
        scene w2_6541 with dissolve
        "In the meantime, she diligently started on giving me a massage - a prelude for things to come most likely."
        scene w2_6543 with dissolve
        mc "What do you mean by that?"
        scene w2_6544 with dissolve
        dal "What you, Mrs. Pulman, and Harper did."

    scene w2_6543 with dissolve
    mc "Oh, that..."
    mc "You know about that, huh?"
    scene w2_6542 with dissolve
    dal "Of course. I know everything each girl does and what she... {i}endures{/i}."
    scene w2_6544 with dissolve
    dal "For one, it's my job. For another, the girls share field notes with each other."
    scene w2_6545 with dissolve
    mc "You mean gossip?"
    scene w2_6544 with dissolve
    dal "No, {b}educational{/b} notes."
    dal "Things like... what to expect from a client, how they treated her, what they ask for... it keeps them sharp, you understand?"
    scene w2_6543 with dissolve
    mc "To know how to best serve the customer?"
    scene w2_6542 with dissolve
    dal "It keeps them from getting into trouble, and more importantly, it keeps them safe."
    scene w2_6543 with dissolve
    mc "That makes sense..."
    scene w2_6545 with dissolve
    mc "So, who are the most problematic customers? The ones the girls need to be safe around?"
    "I figured that would be useful knowledge."
    scene w2_6544 with dissolve
    dal "I'm gonna need you to rephrase that question. I can't answer that, as none of our esteemed patrons are problematic."
    scene w2_6541 with dissolve
    "As always, Dalia was careful. That was true when we first met and that seemed doubly true now."
    scene w2_6543 with dissolve
    mc "Come on, you can speak frankly. I'm on your side of the glass."
    scene w2_6542 with dissolve
    dal "Are you? You think that? Well, it doesn't matter."
    scene w2_6544 with dissolve
    dal "None of our customers are anything but beacons of excellence that we strive to pleasure."
    scene w2_6545 with dissolve
    mc "*sigh* Ah, jeez... alright, then..."
    scene w2_6546 with dissolve
    mc "What customers have \"unique temperaments or requests that present unique challenges\" for our employees?"
    mc "See? Just an innocent, professional question from management."
    scene w2_6544 with dissolve
    dal "Thank you, [mcf]."
    scene w2_6547 with dissolve
    dal "Hmm..."
    scene e2_dalia_rub_a with dissolve
    show e2_dalia_rub

    "Looking like she was seriously considering my question, Dalia's hand still found its way to my crotch like it had a mind of its own."

    if w2ExWhippedOut == True and w2ExRosalindKissDemo == True:
        "Maybe I still had gas in the tank from my little adventure with Felicia and Rosalind, but I found myself quickly growing hard from her touch."
        "Maybe Dalia was just that damn good..."

    if w2ExWhippedOut == True and w2ExRosalindKissDemo == False:
        "Maybe I still had gas in the tank from Felicia's \"help\", but I found myself quickly growing hard from her touch."
        "Maybe Dalia was just that damn good..."

    if w2ExWhippedOut == False and w2ExRosalindKissDemo == True:
        "Maybe I still had gas in the tank from my diversion in the hallway with Rosalind, but I found myself quickly growing hard from her touch."
        "Maybe Dalia was just that damn good..."

    if w2ExWhippedOut == False and w2ExRosalindKissDemo == False:
        "Dalia's skill was on full display. I found myself quickly growing hard from her touch."

    scene w2_6548 with dissolve
    dal "You never know who you're going to catch on a bad day, but Mr. Shelby works our girls pretty hard."
    dal "The stuff he's into wears at you, but he's predictable - he likes to make the girls fight and the loser... the loser takes the brunt of {i}passions{/i}."
    scene w2_6549 with dissolve
    mc "He makes them fight?"
    scene w2_6550 with dissolve
    dal "Eh... it's more like wrestle? Chokeholds, rolling around, hair pulling.... no striking, thankfully."
    scene w2_6551 with dissolve
    mc "Oh, jeez. That's fucking weird. Anyone who's unpredictable?"
    scene w2_6550 with dissolve
    dal "A few, Mr. O'Doherty has a temper for example, but not in the way Mr. Grenier does..."
    scene w2_6549 with dissolve
    mc "What's his deal?"
    scene w2_6550 with dissolve
    dal "Nothing too weird, sexually speaking, but he has a hair-trigger. One time he got so mad at Serena for not responding to a question that he whipped her with a belt until her back was bloody and then used a beer bottle to..."
    scene w2_6552 with dissolve
    dal "...doesn't matter, the details aren't important - point is, she had to take a month off after that. That's why the girls {b}talk{/b}."
    scene w2_6553 with dissolve
    mc "Jesus {b}FUCK{/b}, that's..."
    "Guzzling goblets of cum and Mrs. Pulman's humiliation games aside, that was a whole other level! That's..."
    mc "Why would Mr. Byrnes and Dr. Chuck still let the girls serve him?! Why is he even allowed in the building?!"
    scene w2_6554 with dissolve
    dal "Why...? [mcf]... you..."
    scene w2_6555 with dissolve
    dal "Heh, some of the girls don't think you'll last long here."
    scene w2_6556 with dissolve
    "......"
    scene w2_6557 with dissolve
    mc "...they know about it, right? Dr. Chuck knows about it?"
    scene w2_6555 with dissolve
    dal "Oh, dear... of course."
    scene w2_6557 with dissolve
    mc "Damn it..."
    scene w2_6558 with dissolve
    mc "I'm serious, like... ah, {b}damn{/b}."
    scene w2_6559 with dissolve
    dal "Don't dwell on it, kid."
    "Her voice softened and for once I finally heard her speak without pretense."
    scene w2_6560 with dissolve
    dal "Just... clear your head."
    scene w2_6561 with dissolve
    "At this moment, I understood why Dalia was queen bee amongst the girls. Normally so skittish and stressed-looking, but when she had to turn it on, she really knew how to turn it on."
    scene w2_6560 with dissolve
    dal "Focus on the perks of the job and let me take care of you."
    scene w2_6561 with dissolve
    "Her eyes, her lips, all of her features suddenly seemed very striking... if I wasn't careful, I might just lose track of why I'm here in the first place."
    scene w2_6562 with dissolve
    mc "I'm on the jo--"
    scene w2_6563 with dissolve
    sam "Sorry to keep you waiting -- ah, ha!"
    scene w2_6564 with dissolve
    sam "I see you have already gotten started, you son of a bitch!"
    stop music fadeout 3.0
    scene black with fade
    sam "Time to break in the new girl!"
    play music "music/as-i-figure.ogg"
    scene e2_dalia_nut_a with dissolve
    show e2_dalia_nut
    dal "*Chup, fwhup... khup...!* Mmmhhh.... *pop*"
    "The moment Samson sat down, Dalia wasted no time crawling between my legs and getting to work."
    "Not that I necessarily even wanted to, but refusing the service would've run contrary to my goal of getting Samson to let his guard down. I needed to be one of the boys..."
    dal "*Chhupp~ phwup!* Gghhmmm~"
    "Again, not that I was complaining."
    "With the utmost care, she began with my testes, alternately taking each one between her plush lips and using her tongue like a brush to coat them in saliva."
    dal "*Suuuuck!* Haaa...!"
    "My dick was already heavy and painfully bloated, Dalia used even her hot, breathy sighs to tickle my scrotum and pleasure the underside of my dick."
    scene w2_6565 with dissolve
    sam "This one has a pretty cute face, Dalia. Not to mention her eyes..."
    scene w2_6566 with dissolve
    dal "*Chup, fwup...!* Ffhhhaww~"
    scene w2_6567 with dissolve
    sam "There's a lot of fire behind them. I like that."
    scene w2_6568 with dissolve
    nico "Thanks...?"
    scene w2_6569 with dissolve
    "For the first time this evening, I heard Nicolette speak."
    scene w2_6568 with dissolve
    nico "Should I begin or are you just going to look at me?"
    scene w2_6570 with dissolve
    sam "Go ahead, slut. I want to feel your fucking tonsils!"
    scene w2_6571 with dissolve
    $ renpy.pause(0.5, hard=True)
    scene w2_6572 with vpunch
    "In one dramatic, unbroken motion Samson penetrated her mouth like a cunt, hilting himself to the base and very much knocking against the back of the beleagured redhead's throat."
    "......"
    "..."
    scene w2_6573 with dissolve
    sam "Ha! Very good!"
    scene w2_6572 with dissolve
    "Nico didn't choke or sputter at the sudden intrusion, not in the least. She rolled with the punches, taking the man's sizable cock down her throat like a cock-sucking champion."
    scene w2_6574 with dissolve
    nico "G-ghuh...!"
    sam "I'm impressed."
    sam "I don't expect you to be skilled as Harper, but you got promise. Show me what you got..."
    scene w2_6575 with dissolve
    "Relaxing his posture, Samson gave up the reins and left the trim woman to her own devices."
    scene w2_6576 with dissolve
    dal "Chup... chuwp! Ah...mhh, haat!"
    nico "*Fwup, suuuuck!* Haa...!"
    sam "Come to think of it kid, this is where we first met. You swallowed cigar smoke like it was food."
    scene e2_dalia_lick_a with dissolve
    show e2_dalia_lick
    dal "*Slurp, lchhk..!* Mmmh..."
    "The skilled prostitute had shifted her attention to my shaft, leaving my balls glistening with spit and missing the warmth of her mouth."
    mc "That's right. That was the first and last time I smoked one."
    mc "Too bad we don't have one right now, eh?"
    "To the contrary, I was grateful, but I lied through my teeth."
    scene w2_6577 with dissolve
    mct "(Gh-! Shit, she's good!)"
    sam "Ha ha, I should've thought to bring some!"
    scene e2_dalia_nico_bj1_a with dissolve
    show e2_dalia_nico_bj1
    "*Chwup, fhuwp, suuuuck, kwhup, sluuurp...!*"
    "The pair of whores worked independently from one another, but the sound of their individual efforts coalesced into a vividly lewd cacophony that reverberated off the sauna walls."
    "*Chhwwppp, fggghhh, squeeelch~* *{b}Pop{/b}!*"
    "As the pleasure mounted, I asked myself..."
    mct "(How am I going to pose the questions I needed to ask?)"
    sam "Is this the life or is this the life?"
    "I doubted the giant man would be overly secretive and defensive about the broader details. Samson did proudly announce his wrongdoing openly last week, but the specifics..."
    scene e2_dalia_nico_bj2_a with dissolve
    show e2_dalia_nico_bj2
    dal "Mmmffhhh *squelch...!*"
    mc "It sure is..."
    mct "(I can't be direct about it. I need to not seem like I'm prying.)"
    "Hopefully the alcohol has him loose lipped and I just need to point him in the right direction."
    scene w2_6578 with dissolve
    "First, I need to work on our rapport."

    menu:
        "Connect on a base level. Ask him how Nicolette is performing.":
            scene w2_6579 with dissolve
            mc "How's the new bitch's mouth?"
            scene w2_6578 with dissolve
            "I purposefully asked in the most vulgar way I could think."
            sam "Ah, you know... pretty good, I guess."
            scene w2_6581 with dissolve
            mc "You, ahnng--"
            "The way Dalia's tongue ran over my cum slit caused my body to suddenly jerk."
            scene w2_6580 with dissolve
            mc "You guess?"
            scene w2_6582 with dissolve
            sam "Well, she seems like she had her share of experience throating a chode, but it's a competitive field around here."
            scene w2_6583 with dissolve
            sam "You can't swing a dead cat in the club without hitting a prize-winner cocksucker. How about you? Is Dalia as good as she acts like she is?"
            scene w2_6584 with dissolve
            mc "Ah-- ah, ha, you haven't tried this slut before?"
            scene w2_6585 with dissolve
            sam "Nah, she hangs around the more well-to-do members. Never seen the Empress Whore slum it with a pleb like myself."
            scene w2_6587 with dissolve
            sam "Surprised she even came along..."
            scene e2_dalia_nico_bj3_a with dissolve
            show e2_dalia_nico_bj3
            mc "Don't be absurd. You, a pleb?"
            "I tried my best to sound like I was genuinely shocked that a dried-up actor wasn't treated the same as the CEO of an international pharmaceutical company."
            mc "I thought this was a \"fraternity\" - that everyone was..."
            "The constricting softness of Dalia's throat had me temporarily lose my train of thought."
            mc "Ah...!"
            mc "...I thought that everyone was equal brothers around here."
            sam "Ha, you thought wrong, kid! You put any two shitheads together and {b}poof{/b}! You got a hierarchy on your hands."
            scene e2_dalia_nico_bj1_a with dissolve
            show e2_dalia_nico_bj1
            sam "I guess God thought it was funny to make us all unequal, unsatisfied, and greedy - not that I'm complaining."
            mc "You're not? H-ha, it kind of sounds like it."
            sam "Nah, I'm a realist. Inequality is why this whore is polishing my knob right now."
            "His self-awareness caught me off-guard, but it was a reminder not to underestimate the man. He was a predator all the same."
            sam "You don't need to be king of the jungle to get fed and fat!"
            scene e2_dalia_nico_bj2_a with dissolve
            show e2_dalia_nico_bj2
            "Regarding him as some big, loud-mouthed dope would be to my detriment tonight."
            sam "Ha! Playing the jester honestly isn't so bad."
        "Get him talking about himself and his life's successes."(chg=["sam_up"]):

            $ Sam_Friendship += 1
            scene w2_6580 with dissolve
            mc "You'd know something about that, wouldn't you?"
            scene w2_6578 with dissolve
            sam "What are you sayin'?"
            scene w2_6579 with dissolve
            mc "You've lived a hell of a life. Seen both sides of the curtain - poverty and success."
            scene w2_6581 with dissolve
            mc "You iim-- ng, aah..."
            "The way Dalia's tongue ran over my cum slit caused my body to jerk."
            scene w2_6580 with dissolve
            mc "You immigrated when you were a young boy, g-got--"
            scene w2_6587 with dissolve
            sam "Christ, you read my wikipedia article?"
            scene w2_6584 with dissolve
            mc "No, I... I just admire your tenacity, truly. Not everyone could do what you did."
            scene w2_6588 with dissolve
            sam "Huh..."
            "The bodybuilder looked temporarily flabbergasted."
            mc "What is it?"
            scene w2_6585 with dissolve
            sam "Around here, no one ever asks me about that shit. They always want to hear about those shitty movies I was--"
            scene e2_dalia_nico_bj3_a with dissolve
            show e2_dalia_nico_bj3
            mc "Hey, those are cinema! If only we all could execute our big ideas - explosions, action, car chases - see it come to life on a screen. Even if the end result isn't perfect, it's..."
            "The constricting softness of Dalia's throat had me temporarily lose my train of thought."
            mc "Ah...!"
            mc "...{b}m-magic!{/b}"
            sam "Gahaha, what kind of horse shit is that? Magic?"
            sam "Like we're at the happiest place on earth?"
            scene w2_6589 with dissolve
            mc "Aren't we?"
            sam "Gahahaha, good point!"
            scene e2_dalia_nico_bj1_a with dissolve
            show e2_dalia_nico_bj1
            sam "Don't misunderstand, I'm proud of my movie career, but it's all anyone ever wants to hear about."
            sam "No one outside of the sport gives a crap about body building or my accomplishments there. No one cares that I didn't even speak a lick of English when I got here."
            mc "That's right. You learned English as your second language."
            sam "Ha! I don't speak Spanish so well anymore, kid."
            mc "Still..."
            scene e2_dalia_nico_bj2_a with dissolve
            show e2_dalia_nico_bj2
            sam "{b}Still{/b}. I built myself up from nothing, accomplished great feats, and demolished the piss-poor expectations my abuelo had for me."
            sam "Now... now I can take it easy playing the jester, growing fat on table scraps."

    mc "Jester...?"
    mct "(Yep, he holds his liquor well, but he's definitely intoxicated.)"
    sam "Five thousand years ago you better fucking believe I would've been a warrior-king! I would've had--"
    scene w2_6590 with dissolve
    scene w2_6591 with dissolve
    sam "Less cheek, more throat bitch!"
    scene w2_6592 with dissolve
    dal "Ah..."
    scene w2_6593 with dissolve
    sam "...where was I?"
    scene e2_dalia_nico_bj1_a with dissolve
    show e2_dalia_nico_bj1
    mc "You were telling me about how you would've conquered the world."
    sam "I was? That's embarrassing. Don't listen to me, kid."
    sam "I'm full of crap - {b}now, lemme ask you something...{/b}"
    mc "What do you want to know?"
    sam "Veronica..."
    scene e2_dalia_nico_bj2_a with dissolve
    show e2_dalia_nico_bj2
    "Just my luck; I was hoping he'd bring her up under his own volition."
    mc "...how did I get her to crawl around like a dog?"
    sam "Exactly! You read my mind!"
    mct "(You told me you wanted to know that earlier, you moron...)"
    sam "When I saw those photos, I just about made a mess of my pants. I couldn't believe it."
    scene e2_dalia_nico_bj3_a with dissolve
    show e2_dalia_nico_bj3
    sam "Even now, just looking at you... I want to strangle you out of envy."
    mc "I'd prefer if you didn't..."
    sam "Then tell me! How the hell did you pull that off?"
    mc "It was her idea."
    scene w2_6594 with dissolve
    sam "W-whaa...? S-seriously?!"
    scene w2_6595 with dissolve
    sam "I can't believe my ears! That fucking bitch! I'm going--"
    sam "I'm going....!"
    play sound "sound effects/spurt.wav"
    scene w2_6596 with vpunch
    sam "Gwwwwwaaaaaaaaa, {b}c-cuuuuuuuuum!{/b}"
    nico "Gh-?!"
    play ambient "sound effects/gulp.wav"
    scene e2_nico_gulp_a with dissolve
    show e2_nico_gulp
    "With a frightening, bestial roar the man easily took control of Nicolette's face and unexpectedly buried his cock fully down."
    nico "*Glug, glug, guulp, ghh*! Gaah, ghhkk...!"
    "The redheaded prostitute's only choice was to swallow Samson's cum, and from the sound of her vigorous gulping, her work was cut out for her."
    nico "Ghh...!"
    sam "Ah, you f-fuckin' worthless...! Don't you dare spill a drop...!"
    stop ambient
    scene w2_6597 with dissolve
    sam "{b}Show me{/b}."
    scene w2_6598 with dissolve
    nico "Ah~"
    "Nico obediently stuck out her tongue, showing Samson that she did indeed not spill a drop."
    sam "Ha, good girl."
    scene w2_6599 with dissolve
    sam "What's the matter, Dalia? Can't keep up with the young blood? Bahaha!"
    mct "(Fuck I need to...huh?)"
    "The absence of Dalia sucking my dick did not pass without notice..."
    scene w2_6600 with dissolve
    mc "What are you...?"
    scene w2_6601 with dissolve
    dal "Allow me to take an alternative approach more aligned with {b}your stamina{/b}, Mr. [mcl]."
    "She obscured her retort to the brutish man with feigned reverence toward me."
    dal "A more {i}direct{/i} approach."
    scene w2_6602 with dissolve
    mc "...go ahead."
    "I almost said please. I didn't care how she got me there, I was starting to feel the ache of blue balls setting in from the sudden drought of Dalia's expert mouth-milking."
    scene black with fade
    "With the precision of a computer-guided missile, Dalia backed her fat ass up and..."
    scene w2_6603 with cmet
    dal "A-ah, haa...!"
    "...and without a moment's hesitation, buried me balls deep in her cunt."
    mc "Gh, ghah...!"
    "She wasn't dry, but she also wasn't nearly turned on enough for our coupling to be smooth. The rough friction as her haunches brought Dalia's weight down on my cock ignited a chain reaction of pleasure that crept up my spine and fried my brain with a white flash of ecstasy. "
    mc "F-fhuuck me...!"
    scene w2_6604 with dissolve
    dal "Ha... that's..."
    dal "That's the idea, sir."
    scene e2_dalia_ride_a with dissolve
    show e2_dalia_ride
    "Dalia started off gently, rocking her hips in time with a slow and deliberate rhythm."
    sam "Huh..."
    "Her soft insides squeezed me tightly, and whenever she pried us apart, clung to my shaft and tried to suck me back in."
    sam "That looks nice."
    sam "You don't think I'm finished, do you slut? I can go all night."
    nico "...of course."
    scene w2_6605 with dissolve
    "The fledgling prostitute similarly positioned herself, facing away from Samson."
    nico "Like this?"
    scene w2_6606 with dissolve
    sam "What do you think -- now, where were we [mcf]?"
    scene e2_dalia_nico_ride1_a with dissolve
    show e2_dalia_nic_ride1
    mc "Uh, the... well... ah..."
    "With a beautiful woman riding my cock, my recollection came slowly."
    mc "...the collar was Veronica's idea. She told me she used it on her ex-wife in the bedroom."
    sam "Really? Makes sense, I guess."
    mc "You knew her?"
    sam "I met her once or twice. They were married when she first bought my likeness for promotion."
    mc "What was Veronica's wife like?"
    sam "You're asking cause you're curious about what kind of woman that fiery bitch would get hitched to? Turns out, no one exciting."
    "While we chattered, Dalia was putting her prowess on display, using her inner thighs to keep me steady and locked down how she wanted me."
    sam "I think she worked at an animal shelter. She was a scant little thing. Quiet as a mouse. Didn't make much in the way of an impression."
    sam "It doesn't surprise me to hear she had a submissive streak. Her name was... uh... it's on the tip of my tongue -- Liliana!"
    scene e2_dalia_ride2_a with dissolve
    show e2_dalia_ride2
    mct "(That matched the name in Veronica's dossier...)"
    mc "Do you... ah..."
    "It was gradually growing easier to push inside her, but the way she had me pinned consigned her with the bulk of the work."
    mc "...do you know why they split?"
    "Dalia, meanwhile, had upped her tempo in accordance to the new ease in which she impaled herself."
    sam "I'm not their marriage counselor, kid. Maybe--"
    scene e2_nico_ride_a with dissolve
    show e2_nico_ride
    nico "Eeegh... ha!"
    sam "...maybe one of them stepped out or maybe it was money issues. What else is there?"
    "What else? A lot of things, but the most troublesome thought was it being the result of Veronica's failing business."
    mct "(Which would mean...)"
    scene w2_6607 with hpunch
    sam "C'mon, move your ass faster!"
    scene e2_dalia_nico_ride2_a with dissolve
    show e2_dalia_nic_ride2
    "Speculating right now wasn't only pointless, but it was also difficult. My mind was at odds with my body, pleasured as I was by Dalia's rocking and writhing."
    sam "That's more like it."
    "Unlike me, Samson looked almost unaffected and bored by this scenario."
    mc "Ee-- you..."
    mct "(Damn it, it's hot in here...)"
    mc "...y-you've known Veronica for a while, I take it?"
    sam "About ten years or so?"
    mc "...a whole decade? That long?"
    "Veronica had told me they met at some gym equipment convention, AFTER her financial troubles..."
    sam "{b}Known of her{/b}, at least. You might say I'm a \"longtime fan\", going all the way back to when she competed in shot put at the collegiate level."
    "The possible implication of that statement was unsettling."
    mc "You're an avid shot put watcher then?"
    sam "Oh, God no. Who the fuck wants to watch someone throw a ball down an empty field?"
    sam "I knew her coach is all, the dumb thieving bastard."
    mc "Wait, the coach who sold her the--"
    sam "So, you fuck her yet?"
    "Frustratingly, right when I thought I might be getting somewhere, Samson changed the topic."

    if w2VeronicaScratch == True:
        mc "Veronica? Uh... no."
        "Well, there was her \"stress relief\" earlier this week at her gym, but I wanted to avoid any potential envy-induced strangling."
    else:
        mc "Veronica? Not yet."

    scene w2_6608 with dissolve
    sam "You telling me you had her down on all fours with her coochie hanging out and you didn't try anything?"
    scene w2_6609 with dissolve
    mc "Don't look at me so incredulously, I was only there to take pictures. Even if I tried, she wouldn't have let me."
    scene w2_6608 with dissolve
    sam "Pssh, but you didn't try. You call yourself a man?"
    scene w2_6609 with dissolve
    mc "You remember when she made your nose less ugly, asshole?"
    scene w2_6608 with dissolve
    sam "Bah, {b}you pussy bitch!{/b}"
    scene w2_6610 with dissolve
    mc "......"
    sam "..."
    scene w2_6611 with dissolve
    "Samson found our little exchange amusing and I feigned a chuckle to match his."
    sam "Ha, I like you [mcf]. I like you a lot."
    mc "Thanks, you're better company than some of the other stuffy fuckers around here."
    scene e2_dalia_nico_ride2_a with dissolve
    show e2_dalia_nic_ride2
    sam "No matter. You'll fuck her sooner or later, knowing how Kathy's games go."
    mc "Jealous?"
    sam "Absolutely. Considering all I went through to get her here, it'll pain me to see another man get there before me, but..."
    "Bingo! He brought the conversation back where I wanted it."
    sam "...but tricking her out like this is fun enough to make up for it."
    "The vindictive tone in his voice piqued my curiosity, but I refrained from asking the obvious question. Rather than being direct..."
    mc "I-- ng, s-shit...!"
    "The animal need to dump my load in Dalia's cunt and the heat from the sauna made finding the right words an arduous task. More and more of my thoughts were turning to my lower half."
    mct "({b}I needed to finish!{/b})"
    stop music fadeout 3.0
    scene w2_6612 with dissolve
    dal "Wha...?"
    "Grabbing my companion's flank, I literally took things into my own hands and forced Dalia to a halt, fully sheathing myself in the warm embrace of her quim."
    "I needed to finish quickly and I was going to impress the dumb old bastard while I was at it."
    dal "Is something the--"
    play music "music/time-piece.ogg"
    play ambient "sound effects/fap.wav"
    scene e2_dalia_ride3_a with dissolve
    show e2_dalia_ride3
    dal "G-geh?!"
    "In a bid to outrace the heat and pleasure gnawing at my mind, I marshalled every ounce of my remaining stamina and hurled myself towards an expeditious orgasm."
    dal "A-hah, oh, s-shit...!"
    mc "Gh... sorry, but you were taking too damn long!"
    "Using my leverage on Dalia's body, I repeatedly and forcibly pried and impaled the busty whore on every inch of jackhammering cock."
    sam "You showin' off, kid?"
    dal "F-fuckk...ah! It's too hot to be doing--"
    mc "Exactly, which is why...!"
    "For the moment, I erased the idiot to my right from my mind. I turned my thoughts away from Veronica's situation and focused wholly on railing the bitch in my lap without mercy."
    dal "Gwaaah...!"
    "Sweat trickled heavily down my brow, stinging my eyes and obscuring my vision."
    mc "Neeug...!"
    "An intense, growingly pervasive parchedness plagued my body."
    mct "(Fuck! Good thing I had a nap before coming here!)"
    "My hips and arms began to ache."
    dal "Geeh-"
    "*Twap, thwap, fhwap~!!!!*"
    "The sound of our abject copulation dwarfed the fuck-sounds from the pair next to me, and all that entered my ears was the ear-candy of Dalia's fat ass smashing against my pelvis."
    mct "(S-shit...!)"
    "It was like I could feel the life being sapped from my body, but my sense of preservation had been overwritten by another base urge."
    dal "W--wah... ghh...! Y-you're f-fhucking me so-soohhhh, gghhh-!"
    "Dalia reflexively tried to encourage me with honeyed words, but practiced as she was, it came out a garbled mess of fuck-drunk nonsense."
    dal "Gahhhhhh, good, j-jhoor...!"
    scene w2_6613 with flash
    dal "Ghyeh-!"
    "Her cunt tightened suddenly and violently, even more greatly molding to the shape of my cock as if it was assuming ownership of the tool."
    dal "Shhh---!"
    scene e2_dalia_ride4_a with dissolve
    show e2_dalia_ride4
    dal "Ehhh...~! Heeeeeeehhh....!"
    mc "Fuck, fuck, fuck, fuck, fuck...!"
    mc "(Come on, come on, come on...!)"
    "I was almost there."
    dal "Haa, eeh...!"
    "I was losing feeling in my limbs and my balls began to tighten."
    dal "Ooohh... g-go ahead...!"
    "Soon I'd be pushing a pressurized jet of white through a pin point and flooding Dalia's womb with my jizz...!"
    dal "Give me..."
    "Soon I'd...!"
    stop ambient
    stop music
    play sound "sound effects/spurt.wav"
    scene w2_6614 with flash
    mc "Geeeeeeh!"
    "With a sound not too unlike Samson's own earlier roar, I gave Dalia everything I had, packing my semen down as deep as I could as I continued to piston my hips."
    mc "Ha... haa...!"
    scene w2_6886 with flash
    play sound "sound effects/spurt.wav"
    with flash
    "My dick scooped out and continuously recoated her inner walls in my spunk, until every part of her insides was dyed in my color."
    mc "Gh, so...!"
    scene black with fade
    "For a brief moment, I think I blacked out."
    "My thoughts gradually came back to me and I was more acutely aware of my battered lower half."
    mct "(So... thirsty...)"
    mc "Where were we...?"
    play sound "sound effects/thud-floor.mp3"
    scene w2_6615 with fade
    "With the last of my strength, I gently guided Dalia off my overwrought cock."
    mc "I think..."
    play music "music/as-i-figure.ogg"
    scene w2_6616 with dissolve
    mc "You were saying you went through a lot to get Veronica participating in the exhibition?"
    scene w2_6617 with dissolve
    sam "......"
    nico "..."
    scene w2_6618 with dissolve
    sam "...heh, yeah. Tripping that bitch up was a long time in the making."
    mc "A decade in the making?"
    scene e2_nico_ride2_a with dissolve
    show e2_nico_ride2
    sam "No way! That'd be weird, right? You tryin' to paint me as some sort of obsessive stalker?"
    sam "Since I joined the club five years ago, I've tagged more than half-a-dozen women to potentially recruit, but Veronica is actually the second one to pay out."
    sam "In this case, I just made a Hail Mary when Danny took ill and was looking to offload some of his assets."
    mc "Danny is...?"
    sam "The bitch's old training coach."
    "So Samson's meddling predated Veronica buying the gym...?"
    mc "Ha... impressive. {b}Very{/b} impressive."
    sam "Maybe. It took luck to get her to this point, but when your whole life is lucky, that's a goddamn skill and you should give yourself credit for it."
    mc "So you used your foreknowledge of the sale to stack the deck in your favor from the very onset?"
    sam "Not just that. I was the one who convinced that old shit-stain to sell it to her in the first place. She was interested, but he was opposed to saddling his protégé with that dud of a place."
    mc "You convinced him?"
    sam "A sick man with debts is easily persuaded. That was just the start of it though."
    sam "I even got him to chain her down by having Danny point her in the direction of a buddy of mine's leasing company. There's also the matter with her rental agreement, but..."
    scene w2_6619 with dissolve
    mct "(Holy shit... he got her own coach to set her up like that...? That's...)"
    "That's the kind of shit that ruins your ability to ever trust another human being, isn't it?"
    sam "Ultimately, though..."
    "The man gestured wildly and puffed his chest out proudly."
    scene w2_6620 with dissolve
    mc "...ultimately, what?"
    scene w2_6619 with dissolve
    sam "Ultimately--"
    play sound "sound effects/spurt.wav"
    scene w2_6621 with dissolve
    sam "Arg, shit! W-whore...!"
    play sound "sound effects/spurt.wav"
    "Samson abruptly climaxed, but neither of us paid it any heed."
    scene w2_6622 with dissolve
    sam "None of that would've mattered if she just walked away."
    play sound "sound effects/thud-heavy.wav"
    scene w2_6623 with vpunch
    "*Thud!*"
    sam "That's what I'm most proud of."
    scene w2_6624 with dissolve
    sam "She could've eaten the loss and taken her lumps as a learning experience, but I knew she wouldn't because I was certain of the kind of woman she is."
    sam "That pig-bitch is too damn proud."
    scene w2_6625 with dissolve
    mc "Is her coach still alive?"
    scene w2_6626 with dissolve
    sam "Funny how that works. He was given six months to live and he's still walking around a few years later."
    sam "The shameful bastard didn't even have the decency to kick it."
    scene w2_6627 with dissolve
    stop music fadeout 3.0
    show screen textbox2 with dissolve
    "Samson's information didn't change anything. It didn't offer anything {b}actionable{/b}..."
    "All it did was shine light on a greater, more sickening duplicity."
    sam "Anyway, I think I'm about to have a heat stroke, eh? Let's get out of here."
    scene w2_6628 with dissolve
    mc "Ah, yeah..."
    scene black with fade
    mc "Good idea, {size=-10}you slimy fuck.{/size=-10}"
    $ renpy.end_replay()
    if not persistent.daliaW2Sauna:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.daliaW2Sauna = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)

    "......"
    "..."
    jump w2ExVeronicaHanaB




screen w2ExVIPLounge:

    imagemap:

        imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w2ExNavMenu")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]


        if w2ExEmmaFavor == "fulfilled":
            idle "gui/screens/imagemaps/w2ExLoungeB2_idle.png"
            hover "gui/screens/imagemaps/w2ExLoungeB2_hover.png"
            ground "gui/screens/imagemaps/w2ExLoungeB2_ground.png"
            hotspot (154,213,600,600) action Jump("w2ExIanAbelSophiaB")
            hotspot (1045,398,600,600) action Jump("w2ExChuckB")

        else:
            idle "gui/screens/imagemaps/w2ExLoungeB1_idle.png"
            hover "gui/screens/imagemaps/w2ExLoungeB1_hover.png"
            ground "gui/screens/imagemaps/w2ExLoungeB1_ground.png"
            hotspot (154,213,600,600) action Jump("w2ExIanAbelSophiaB")
            hotspot (1045,398,600,600) action Jump("w2ExChuckB")



label w2ExVIPLounge:
    show black
    $ renpy.music.play("music/i-knew-a-guy.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w2ExVIPLounge with fade


label w2ExChuckB:

    if w2ExChuckBRepeat == False:
        $ w2ExChuckBRepeat = True

        scene w2_6674 with dissolve
        "Off by himself, in the nearly empty lounge, sat Dr. Chuck ruminating intently over the end-state of a chess board."
        "The frustrated look on my former mentor's face said it all in terms of who won."
        scene w2_6675 with dissolve
        "His opponent was an amazing woman..."
        scene w2_6676 with dissolve
        mc "Was it close?"
        scene w2_6677 with dissolve
        "......"
        "..."
        scene w2_6678 with dissolve
        chuck "...not at all, lad."
        scene w2_6679 with dissolve
        kil "He got his asshole turned inside out."
        mc "Ah..."
        abel "Come sit down and have a drink, [mcf]."
        scene w2_6680 with dissolve
        "Ha... there was no way I was getting through the night dry, I guess."
        chuck "Mmh..."
    else:

        scene w2_6674 with dissolve
        mct "(I should leave him to his thoughts.)"

    jump w2ExVIPLounge


label w2ExIanAbelSophiaB:

    if w2ExIanAbelSophiaBRepeat == False:
        $ w2ExIanAbelSophiaBRepeat = True
        scene w2_6681 with dissolve
        if w2ExChuckBRepeat == True:
            "Doing as I was bid, I left Dr. Chuck to his own devices and decided to join my bartender friend, Dr. Abel, and his dutiful attendant at the bar."
        else:
            $ w2ExChuckBRepeat = True
            "The lounge was practically empty, save for a few people, and I naturally headed toward the bar where Ian was apparently playing bartender."

        mc "You know how to mix drinks?"
        scene w2_6682 with dissolve
        kil "Not at fucking all. Luckily, most everyone drinks it straight here."
        scene w2_6683 with dissolve
        mc "I'll take a Ramos Gin Fi--"
        kil "Denied. You'll take a whiskey."
        scene w2_6684 with dissolve
        abel "Some bartender he is."
        kil "Well, this is August's post. I'm just fillin' in."
        abel "It's nice to see you yet again, [mcf]."
        scene w2_6685 with dissolve
        abel "Sophia?"
        sophia "Excuse me."
        scene w2_6686 with dissolve
        "Before I could refuse, the beautiful doctor had switched targets at her benefactor's behest."
        scene w2_6687 with dissolve
        sophia "I'm not very good at this, but I hope my meager skills can bring you a modicum of comfort, sir."
        mc "A-ah...!"
        mct "(This wasn't very good?!)"
        scene w2_6688 with dissolve

        if VeroFlag == True:
            "I could feel my weariness from my sauna excursion disappear with the delicate workmanship of the blonde's fingers."
        else:
            "Quite frankly, this felt fucking amazing."

        scene w2_6689 with dissolve
        mc "How are... you tonight, Dr. Lundgren?"
        scene w2_6690 with dissolve
        sophia "There's no Dr. Lundgren here. Please, just ignore me."
        scene w2_6691 with dissolve
        mc "Oooohkay..."
        scene w2_6692 with dissolve
        mc "...how are you tonight, Dr. Van Doren?"
        scene w2_6693 with dissolve
        abel "Availing myself to the club's whiskey and enjoying the company of this fine gentleman."
        abel "Your nephew is an interesting fellow, Charles."
        scene w2_6694 with dissolve
        chuck "...hm?"
        chuck "Yeah, 'course he is..."
        scene w2_6695 with dissolve
        abel "Oh, he answered?"
        abel "He must have finally wrapped his head around the gap between him and my protégé."
        scene w2_6696 with dissolve
        chuck "She's brilliant alright - more brilliant than you, Abel - and I'm not just talkin' about chess either."
        scene w2_6697 with dissolve
        abel "She certainly is."
        scene w2_6698 with dissolve
        "The man wryly smiled before taking a swig of his drink."
        scene w2_6699 with dissolve
        abel "Do you desire her? Just say the word and I'll give her to you for an entire week."
        "If Dr. Van Doren's outrageous offer bothered her, it didn't manifest in her hands. Sophia never slowed or faltered in her technique."
        scene w2_6700 with dissolve
        chuck "You insult me."
        scene w2_6701 with dissolve
        abel "That wasn't my intention at all, Dr. Kohler."
        abel "It's the whiskey talking, you see."
        mct "(...they both were insane.)"
        scene w2_6702 with dissolve
        "The pair's odd exchange knocked all conversational momentum out of the room."
        kil "Ah, so yeeeeeah, anyway..."

        if w2ExEmmaFavor == "promised":
            "Sitting here, Jacob's favor regarding his prostitute friend came to mind. I was considering sticking my own neck out to help, but it occurred to me both my lifelong friend and my old mentor had more well-protected throats."
            "The question is, which avenue do I wish to take?"
            hide screen textbox2 with dissolve

            menu:
                "Get Ian's help on the down low. Have him \"occupy\" Emma's time."(chg=["jacob_up","killian_up"]):
                    $ Jacob_Friendship +=1
                    $ Killian_Bromance += 1
                    $ w2ExEmmaFavor = "fulfilled"
                    $ w2ExEmmaFavorIan = True
                    scene w2_6703 with dissolve
                    show screen textbox2 with dissolve
                    mc "Can I talk to you for a second?"
                    kil "Oh...?"
                    scene w2_6704 with dissolve
                    mc "Excuse me, Dr. Lundgren."
                    scene w2_6705 with dissolve
                    mc "Can I ask you a favor?"
                    scene w2_6706 with dissolve
                    kil "Abso-fucking-lutely, man. Just say it."
                    scene w2_6705 with dissolve
                    mc "Jacob is concerned about one of the girls --"
                    scene w2_6707 with dissolve
                    kil "{b}Emma{/b}."
                    scene w2_6708 with dissolve
                    "Naturally, Ian was more attuned to the personal dynamics of this place than I was and instantly grasped the situation."
                    scene w2_6705 with dissolve
                    mc "Yeah, he's concerned about her. He wanted me to watch over her tonight, but I was thinking we might do him one better."
                    scene w2_6707 with dissolve
                    kil "What are you thinking?"
                    scene w2_6705 with dissolve
                    mc "You're allowed to enjoy yourself, right? Are you free to use the girls' services on exhibition nights?"
                    scene w2_6709 with dissolve
                    kil "In theory, it's cool. You want me to...?"
                    scene w2_6705 with dissolve
                    mc "Go find Emma and spend some time with her, before and after the show."
                    scene w2_6709 with dissolve
                    kil "...don't bone her, right?"
                    scene w2_6705 with dissolve
                    mc "...preferably not. It would run contrary to--"
                    scene w2_6706 with dissolve
                    kil "Yeah, that's what I thought. Just checking!"
                    scene w2_6710 with dissolve
                    kil "Uncle! I'm going to go have some fun, you don't mind watching the bar, right?"
                    scene w2_6711 with dissolve
                    chuck "...oh? Yeah, sure. Kathy's got everyone in the Velvet Room anyway."
                    scene w2_6710 with dissolve
                    kil "Thanks!"
                    scene w2_6709 with dissolve
                    kil "Before and after, eh?"
                    scene w2_6705 with dissolve
                    mc "I'll owe you one."
                    scene w2_6706 with dissolve
                    kil "Don't worry, I don't keep tally."
                    scene w2_6705 with dissolve
                    mc "By the way..."
                    scene w2_6707 with dissolve
                    kil "Yeah?"
                    scene w2_6705 with dissolve
                    mc "Does Jacob look out for all the girls like this or is there something about this one in particular?"
                    scene w2_6707 with dissolve
                    kil "Yes and {b}yes{/b}."
                    scene black with fade
                    "Wrapping up our conversation, Ian jaunted out of the bar, presumably to find Emma."
                    "Naively, I felt a little good about myself."
                    jump w2ExVIPLounge
                "Take a lark on a more direct approach. Ask Dr. Chuck to excuse Emma for the rest of the night."(chg=["jacob_up2","august_down2","chuck_up"]):

                    $ Jacob_Friendship +=2
                    $ August_Friendship -=2
                    $ Chuck_Friendship += 1
                    $ w2ExEmmaFavor = "fulfilled"
                    $ w2ExEmmaFavorChuck = True
                    scene w2_6704 with dissolve
                    show screen textbox2 with dissolve
                    mc "Excuse me, Dr. Lundgren."
                    scene w2_6712 with dissolve
                    mc "Can I ask you a personal favor, Dr. Chuck?"
                    scene w2_6713 with dissolve
                    "I wasn't sure this would work, but I was confident enough in our personal history to ask."
                    scene w2_6714 with dissolve
                    chuck "I'm beginning to think favors are what I'm here for..."
                    scene w2_6715 with dissolve
                    "It was just a glance, but he was definitely directing that toward Ian."
                    scene w2_6716 with dissolve
                    mc "Is asking for one while you're licking your wounds a poor choice in timing?"
                    scene w2_6717 with dissolve
                    chuck "You cheeky dickhead! {b}Ask{/b}."
                    scene w2_6716 with dissolve
                    mc "Can you give Emma the night off?"
                    scene w2_6718 with dissolve
                    chuck "Who?"
                    scene w2_6716 with dissolve
                    mc "...she's one of the girls."
                    scene w2_6718 with dissolve
                    chuck "Ah. Can't the bitch ask herself?"
                    scene w2_6716 with dissolve
                    mc "She didn't put me up to it."
                    scene w2_6719 with dissolve
                    chuck "Is that right?"
                    "Dr. Chuck looked like he was trying to unravel the truth with his eyes."
                    scene w2_6720 with dissolve

                    if w1ExDickhead == True:
                        mc "I've barely said a few words to her."
                    else:
                        mc "I've never even spoken with her."

                    scene w2_6718 with dissolve
                    chuck "Alright, I believe you, but then why are you asking?"
                    scene w2_6716 with dissolve
                    mc "I heard through the grapevine that her father's sick."
                    scene w2_6715 with dissolve
                    "I decided to leave Jacob's name out of it."

                    if w2TIWarrenDaliaRepeat:
                        scene w2_6716 with dissolve
                        mc "{b}Plus{/b}, there was that business with Warren recently."
                        scene w2_6715 with dissolve
                        "Putting two-and-two together, I recalled the tail-end of the conversation I heard between Dalia and Warren yesterday."
                        scene w2_6718 with dissolve
                        chuck "Ah, yeah... I heard about that..."
                        chuck "That moron only knows how to break things."

                    scene w2_6716 with dissolve
                    mc "This is all just a personal observation."
                    scene w2_6721 with dissolve
                    chuck "Okay, sure, but why do you give a damn about one of the wh--"
                    scene w2_6722 with dissolve
                    "He stopped himself. I guess in some ways he still wasn't letting go of the kind façade from my memories."
                    scene w2_6721 with dissolve
                    chuck "What I mean is, you've only been here a month, don't you think you shouldn't meddle in staffing decisions?"
                    scene w2_6716 with dissolve
                    mc "Not meddling, just asking my old mentor and physics club advisor."
                    scene w2_6718 with dissolve
                    chuck "...is this important to you?"
                    scene w2_6716 with dissolve
                    mc "Yes, it helps me be comfortable with this place."
                    scene w2_6723 with dissolve
                    chuck "...s'alright. That's all I need to hear."
                    scene w2_6724 with dissolve
                    "The way he smiled almost tricked me into believing that façade again."
                    scene w2_6721 with dissolve
                    chuck "August might be annoyed, but we got more holes than poles on nights like this. Emma or whatever her name is can go home."
                    scene w2_6725 with dissolve

                    if chuck_uncle == True:
                        mc "Thanks, Uncle Chuck."
                    else:
                        mc "Thank you, \"Uncle\" Chuck."

                    chuck "Don't mention it."
                    scene w2_6714 with dissolve
                    chuck "That's what I'm here for."
                    scene black with fade
                    chuck "Ian... find the girl and send her home. I'll watch over the bar."
                    "Naively, I felt a little good about myself."
                    jump w2ExVIPLounge
                "Don't ask.":

                    show screen textbox2 with dissolve
                    mct "(Nah, I won't involve either of them in this. I volunteered {b}myself{/b}, after all.)"

        scene black with fade
        "I spent time talking and enjoying my drink, but excused myself when I found the chance."
        jump w2ExVIPLounge

    if w2ExIanAbelSophiaBRepeat == True:
        if w2ExEmmaFavor == "fulfilled":
            scene w2_6888 with dissolve
            "I've already chatted with the odd pair."
            jump w2ExVIPLounge
        else:
            scene w2_6887 with dissolve
            "I've already killed enough time here."
            jump w2ExVIPLounge





label w2ExVincenzoB:
    stop music fadeout 2.0
    if w2ExVincenzoB1 == False and w2ExVincenzoB2 == False:
        $ w2ExVincenzoB1 = True

        scene black with fade

        if hanaFlag == True:
            "Working my way through the lower levels of the Club, I passed by the pool we used the night of Hana's concert. The sound of copulation got the better of my curiosity."
        else:
            "Working my way through the lower levels of the club, I passed by an indoor pool, where the sound of copulation got the better of my curiosity."

        mct "(Just a quick peek.)"
        scene w2_6736 with fade
        play ambient "sound effects/fap.wav"
        cel "Ah, again...?"
        vinc "You think I'd be satisfied just going once, my dear?"
        cel "A-ah...! Fhh...!"
        vinc "Don't sound so surprised, my dear! I won't be finished with just two!"
        scene black with fade
        stop ambient fadeout 2.0
        "Curiosity, like a flame, will sometimes burn you."
        jump w2ExNavMenu


    if w2ExVincenzoB1 == True and w2ExVincenzoB2 == False:
        $ w2ExVincenzoB2 = True
        scene black with fade
        "Fifteen minutes later, while passing through, the noise still persisted..."
        mct "(He couldn't still be...)"
        scene w2_6737 with fade
        play ambient "sound effects/fap.wav"
        mct "(Another one?!)"
        madi "Nngg...! S... sir, don't you think you've eaten enough?"
        "Off on the sidelines utterly wrecked, was one of the house girls. In the fat man's paws was a new girl."
        vinc "I've only just begun to whet my appetite, slut!"
        madi "Ghhh... I got to be at the Vee---"
        scene black with fade
        stop ambient fadeout 2.0
        "Disgusting, but... impressive."
        "Very impressive."
        jump w2ExNavMenu

    if w2ExVincenzoB1 == True and w2ExVincenzoB2 == True:
        scene black with fade
        "That's enough spying for one day..."
        jump w2ExNavMenu




label w2ExLezB:

    stop music fadeout 3.0
    $ w2ExSexRoomUnlock = False
    $ w2ExLezSeen = True

    scene w2_6756 with fade
    if hanaFlag == True:
        "Slowly, I made my way down to the very same room Hana and I had our \"heart-to-heart\" in not long ago."
    else:
        "Slowly, I made my down to the gaudy room displayed on the security room monitor."

    scene w2_6757 with dissolve
    "I was fairly certain that dealing with the house girls fell outside the scope of my job description, but I preferred the comfort of a concrete goal with a clear end to my other tasks for the night."
    mc "...Jacob said to knock first, eh?"
    scene w2_6758 with dissolve
    mc "Oh!"
    play music "music/devious-little-smile.ogg"
    scene e2_lhl_1_a with dissolve
    show e2_lhl_1
    "In the time it took me to venture from Jacob's post down to where Harper and Lucy were having a private conversation, the pair had moved off the bed and were now..."
    mct "(So it's like that...)"
    "Chest-to-bountiful-chest, Harper had locked the school teacher in the passionate embrace of a lover's kiss."
    "The sight had me transfixed, in part from the polite reticence to intrude on the couple's private moment and more aptly because of the sordid peep-show I was now stealing."
    "Their entwining bodies, I thought, made for a novel sight."
    "Inside this building, {b}this{/b} was a rare glimpse of lust and affection absent of performative pretense."
    "This exchange didn't have a price tag on it. Ostensibly..."
    mct "(They're doing this because they both want to...?)"
    "The cynical part of me imagined some quid-pro-quo, a deal brokered by the new girl for her senior's protection - that was just my twisted imagination though, the truth wasn't graspable behind this glass window."
    mct "(I wonder who made the move on who... gotta have been Harper right?)"
    mct "(Whatever the case...)"
    scene w2_6759 with dissolve
    "Neither woman knew I was here, privy to their private moment."
    scene w2_6760 with dissolve
    mct "({b}Shit{/b}.)"
    "I felt dirty for looking and more than a little guilty for intruding on their privacy."
    "The civilized part of me now wished that I had stayed out of it, that I had turned Dalia's request down and told her to do her own damn job herself."
    scene w2_6761 with dissolve
    "The uncivilized part..."
    mct "(Just one more quick peek...)"
    scene w2_6762 with dissolve
    mc "Woah..."
    scene e2_lhl_2_a with dissolve
    show e2_lhl_2
    "Harper had changed her mode of attack, her tongue venturing down to Lucy's left breast and bringing the woman to her knees."
    "This new approach left Harper's hands free to dole out even greater attention, one hand prodding Lucy's mouth-free breast and the other snaking a thumb into the submissive teacher's gaping mouth-hole."
    "The way Lucy absent-mindedly sucked on the intruding digit kindled my own lust and began to supercede my purpose for being here..."
    mct "(Fuck me, I need to...)"
    scene w2_6763 with dissolve
    hide screen textbox2 with dissolve

    menu w2ExLezBVouyer:
        "{color=#FF1493}[[Voyeur]{/color} Let them finish while enjoying the view." if history_voyeur == True:
            pass
        "Awkwardly interrupt and gently remind the girls they're on the clock."(chg=["tough_down"]):
            $ toughness -= 1
            stop music fadeout 3.0
            show screen textbox2 with dissolve
            "It would be best to step in before things got too heated."
            "Dalia said she'd prefer me to approach it like management, but..."
            play sound "sound effects/door-knock.wav"
            scene w2_6764 with dissolve
            "*Knock, knock*"
            "Laying it on thick after beaver damming them would be a peak dick-head move."
            stop sound
            $ renpy.end_replay()
            scene w2_6765 with dissolve
            mc "Girls! It's [mcf]!"
            scene w2_6766 with dissolve
            "........."
            "......"
            "..."
            "For what felt like eternity, I stood there in silence."
            mct "(Are they pretending like they're not..?)"
            "Just as I was contemplating opening the door myself..."
            scene w2_6767 with dissolve
            harp "..."
            play music "music/thief-in-the-night.ogg"
            scene w2_6768 with dissolve
            harp "I--! You need something, Mr. [mcl]?"
            scene w2_6769 with dissolve
            mc "What were you two doing in there?"
            scene w2_6770 with dissolve
            harp "Lucy needed some time after that ba-- I mean, Mr. Miller hit her."
            harp "I was just--"
            scene w2_6771 with dissolve
            mc "...being a good friend?"
            scene w2_6772 with dissolve
            harp "Ah..."
            "She knew I knew."
            mc "Aren't you two on the clock?"
            harp "I..."
            scene w2_6773 with dissolve
            harp "It won't happen again."
            scene w2_6774 with dissolve
            "Harper shifted her body language to something more cold and familiar."
            scene w2_6773 with dissolve
            harp "How did you know that...?"
            scene w2_6775 with dissolve
            mc "Dalia suspected you might be enjoying a bit of respite while Nicolette was capturing Samson's attention."
            scene w2_6776 with dissolve
            "......"
            "..."
            scene w2_6777 with dissolve
            harp "Ah, Dalia sent you!"
            mc "Bingo."
            mc "She just wants you to keep your wits about you. Your absence might be noted, y'know?"
            scene w2_6778 with dissolve
            harp "Heh, that clever bitch."
            scene w2_6779 with dissolve
            "The pair shared a look whose meaning I was nonprivy to."
            scene w2_6780 with dissolve
            lucy "Did you see us, umm...?"
            scene w2_6781 with dissolve
            harp "Aht! Leave it at that."
            harp "Remember what I taught you. Gotta know when you're ahead, Luce."
            scene w2_6782 with dissolve
            lucy "R-right."
            scene w2_6783 with dissolve
            harp "We should get back out there."
            mc "You really should. Just try and entertain the guests somewhere Isaak isn't, yeah?"
            "Lucy's humiliation kowtowing to a man she has to see every workday was a bad recipe after all. She chose to be here, but I still felt a little sorry for her in that regard."
            scene w2_6784 with dissolve
            harp "Hey, Luce..."
            "The pair passed me by, on to who knows where to do who knows what obscene acts."
            scene w2_6785 with dissolve
            harp "Always do what Dalia says. That's the biggest rule to remember if you want to succeed here."
            harp "She'll keep you whole."
            lucy "I'll remember."
            scene w2_6786 with dissolve
            harp "She asked you to do this for her?"
            mc "That's what I said."
            scene w2_6787 with dissolve
            harp "Hmm, interesting..."
            scene w2_6788 with dissolve
            mc "She said she didn't want to take it to Mr. Byrnes."
            scene w2_6789 with dissolve
            lucy "Would she have done that?"
            scene w2_6790 with dissolve
            harp "Not a chance. That's why you always have to listen to her."
            scene black with fade
            stop music fadeout 3.0
            harp "I've still got a lot to teach you about this place."
            jump w2ExNavMenu
        "Put your boss hat on and firmly remind them they have a job to do."(chg=["tough_up"]):



            $ toughness += 1
            stop music fadeout 3.0
            show screen textbox2 with dissolve
            "It would be best to step in before things got too heated."
            "Dalia said she preferred if I did things sternly, well..."
            scene w2_6791 with dissolve
            "...I don't think I have that kind of vibe, but I can try."
            $ renpy.end_replay()
            scene e2_lhl_3_a with dissolve
            show e2_lhl_3
            lucy "A-ah, ohhh, H-harp...!"
            "They hadn't noticed me."
            "Harper was now knuckle deep in Lucy's cunt, working diligently to pry dirty sounds from the raven-haired MILF's dumbly-parted lips."
            "*Chuwp, fwhlup, ch!"
            lucy "Yhgnnn...! Ah--"
            play music "music/cold-sober.ogg"
            scene w2_6792 with dissolve
            mc "*Ahem!*"
            mc "{b}I was ordered to look for you two{/b}, but I didn't expect..."
            "Leaving it vague like that, they would naturally assume it was under the direction of one of the owners."
            scene w2_6793 with dissolve
            mc "Well, you gals seem close."
            harp "Ah, ah... [mcf]...! I mean Mr. [mcl], haven't..."
            mc "It must be nice fucking around while all your other co-workers pick up the slack, eh?"
            scene w2_6794 with dissolve
            harp "......"
            lucy "..."
            "Caught abruptly and totally off guard, the two looked deeply embarrassed and unable to mount a defense."
            "Instead, they remained before me on their knees, Harper looking like a trapped animal while Lucy..."
            scene w2_6795 with dissolve
            mc "Kinda silly to try and maintain your modesty considering your work uniform, Lucy."
            scene w2_6796 with dissolve
            lucy "Ah... yeah..."
            lucy "Reflex I guess..."
            "It was nice to know she hadn't burned out her sense of shame, yet."
            scene w2_6797 with dissolve
            mc "So you two thought you'd enjoy yourself while Mr. Garcia shoves his fat cock down Nicolette's throat?"
            scene w2_6798 with dissolve
            harp "It's not like that."
            scene w2_6799 with dissolve
            "As expected, Harper came to her senses much faster than her less experienced co-worker."
            scene w2_6800 with dissolve
            harp "Lucy needed some time after that bastard hit her and..."
            scene w2_6798 with dissolve
            harp "Ah, fuck. Haven't you ever heard of knocking?"
            scene w2_6799 with dissolve
            "In light of being discovered plumbing the depths of Lucy's cunt, she realized immediately how flimsy an explanation that was."
            scene w2_6801 with dissolve
            lucy "It's my fault Harper's here in the first place, she was just--"
            scene w2_6802 with dissolve
            harp "Shut up, {b}you idiot{/b}. I'm the one who should know better."
            scene w2_6798 with dissolve
            harp "--level with me, are you going to tell August about this?"
            scene w2_6797 with dissolve
            mc "...get off your knees and stand up."
            "I purposefully ignored her question."
            scene w2_6803 with dissolve
            mc "You too."
            scene w2_6804 with dissolve
            mc "Good. Now I feel like I'm talking to a pair of adults."
            mc "What would happen if it was Warren who caught you two?"
            scene w2_6805 with dissolve
            harp "{b}Jacob's{/b} watching the cameras."
            scene w2_6804 with dissolve
            "So she knew and counted on that? I knew she wasn't stupid."
            mc "That's beside the point, stupid. What if Samson, Isaak, or someone else went looking for you two?"
            mc "Your absence might be noticed. Maybe even by Mr. Byrnes."
            scene w2_6806 with dissolve
            harp "Wait I thought he--"
            scene w2_6807 with dissolve
            mc "Seriously, how fucking dumb do you have to be to be lectured by a kid who's only been here for a few weeks?"
            scene w2_6808 with dissolve
            harp "...hmmgg!"
            scene w2_6809 with dissolve
            harp "Are you trying to squeeze a \"favor\" from us?"
            scene w2_6810 with dissolve
            mc "Why would you think that?"
            scene w2_6809 with dissolve
            harp "Why else would you just waltz in here and grill us?"
            scene w2_6810 with dissolve
            mc "Dalia sent me."
            scene w2_6811 with dissolve
            harp "...oh."
            mc "She's got her hands full tonight managing the other girls and you're adding to her problems, so get your shit together."
            scene w2_6812 with dissolve
            harp "...ha, she amazes me. Goddamn psychic bitch."
            scene w2_6813 with dissolve
            harp "Always do what Dalia says. That's the biggest rule to remember if you want to succeed here."
            harp "She'll keep you... whole."
            scene w2_6814 with dissolve
            lucy "Got it..."
            scene w2_6815 with dissolve
            harp "...she used you as messenger, huh?"
            scene w2_6816 with dissolve
            mc "She brought a problem she had to me, {b}to deal with{/b}."
            mc "...I felt a little silly."
            scene w2_6815 with dissolve
            harp "Well, {b}don't.{/b}"
            harp "You played the part well, bossman."
            scene w2_6817 with dissolve
            harp "Come on."
            scene black with fade
            stop music fadeout 2.0
            harp "I'll teach you more later."
            jump w2ExNavMenu

        "{color=#696969}[[Voyeur] Let them finish while enjoying the view.{/color}." if history_voyeur == False:
            jump w2ExLezBVouyer



    "I desired to see more. My curiosity, or rather my perversion, was just too strong."
    scene w2_6818 with dissolve
    "I wanted to see what it was like to see two women fuck without an audience."
    "I wanted to {i}hear{/i} them..."
    scene e2_lhl_2_a with dissolve
    show e2_lhl_2
    "With a careful push, I moved the door ajar, just enough for any lewd noise to escape the soundproofing."
    lucy "Oh-, nghh... Harp... don't... we should..."
    "Harper was still focusing on the busty woman's chest, running her pink teat between her fingers and delivering a potent tongue lashing to the other."
    lucy "Mmfhh, wheeshould~"
    "Lucy's words came out in a torrid mess, every syllable fighting the thumb obstructing her mouth."
    lucy "Ah...!"
    "*Chwup, fwhup... thwup!*"
    lucy "We--shhhould...! Weshhh...."
    lucy "Weshoudlhg--ggoohhabbk?"
    scene w2_6819 with dissolve
    harp "Say again?"
    lucy "We should..."
    lucy "...I mean... i-is this okay?"
    scene w2_6820 with dissolve
    harp "Is what okay?"
    harp "Do you mean what you and I are currently doing?"
    scene w2_6821 with dissolve
    lucy "Yes... I-I mean, no -- I mean...! Shouldn't we be upstairs--"
    scene w2_6822 with dissolve
    harp "Should I stop then?"
    scene w2_6823 with dissolve
    lucy "I..."
    scene w2_6824 with dissolve
    harp "We {b}can{/b} stop."
    scene w2_6825 with dissolve
    lucy "I-I, uh... prefer it up here. Away from..."
    scene w2_6824 with dissolve
    harp "Don't you like what I'm doing as well?"
    scene w2_6825 with dissolve
    lucy "...I'm a--"
    scene w2_6826 with dissolve
    lucy "O-ohh....!"
    harp "I may be better with pleasing a man, but I honestly don't think I'm too shabby at..."
    scene w2_6827 with dissolve
    lucy "A-aahh!"
    "Harper's fingers sunk deep into the babbling school teacher's snatch, skewering her words into a shrill cry."
    lucy "Ha... ha... I'm a married woman... I prefer..."
    scene w2_6828 with dissolve
    harp "I'll stop then."
    scene w2_6829 with dissolve
    lucy "W-wait...! I didn't... I..."
    scene w2_6830 with dissolve
    "Harper had the confused woman dancing on a marionette string."
    scene w2_6831 with dissolve
    harp "I want to hear you say it then. {b}Ask me to continue{/b}."
    scene w2_6832 with dissolve
    lucy "...*gulp* I would like you to... I would..."
    lucy "I {i}want{/i} you to continue, Harper."
    scene w2_6833 with dissolve
    lucy "{size=-10}P-please...{/size=-10}"
    scene w2_6834 with dissolve
    harp "Thank you, Lucy."
    lucy "Don't look so pleased miss--"
    scene e2_lhl_3_a with dissolve
    show e2_lhl_3
    lucy "Nnhh-- eeeeey...!"
    "With renewed vigor from her partner's lusty affirmation, Harper sunk her fingers knuckle-deep into the curvy woman's cunt and resumed gobbling tit."
    mct "(She's quite good at multitasking...)"
    scene e2_lhl_3a_a with dissolve
    show e2_lhl_3a
    "Harper's plush lips formed a perfect seal around the teacher's nipple, and I could imagine her small tongue enveloping its burgeoning point, prodding it with pen-like flourishes."
    "*Chwup, fhwup...!*"
    "Even from this far back, hidden behind the wide door, the resulting sound was clear as day."
    "*Chwup, khwuuup, gwhupp...!*"
    "Rather than lewd, it was ravenous."
    "It was the sound of a starving beast picking its prey to the bone, desperate for every scrap of succor."
    scene w2_6835 with dissolve
    lucy "Hnnngg-!"
    lucy "You're iin-inn-incorrigible...!"
    "Lucy was wildly receptive to the seasoned prostitute's touch, voice shrill and drenched in pleasure."
    lucy "H-hhhyyy..."
    scene w2_6836 with dissolve
    harp "Incorrigible! Now that's a word fit for an English teacher, but..."
    harp "What about you, beautiful? You're sucking on my fingers SO. DAMN. HARD. right now."
    scene e2_lhl_3b_a with dissolve
    show e2_lhl_3b
    lucy "Ahhh...!"
    "Harper's words coincided with a pitch in intensity, her slender fingers gouging Lucy's sex with dramatic abandon."
    lucy "Nnhhh...ahhh!"
    "My mind filled in what I couldn't see, painting a vivid picture of Harper's fingerly love."
    "Of Lucy's insides being nearly pulled out, clinging desperately to her lover's unremitting penetration."
    "Harper's fingers gliding effortlessly, slathered in the school teacher's juices, made a beautiful sound that failed to reach my ears."
    scene e2_lhl_3_a with dissolve
    show e2_lhl_3
    "That was, of course, just my mind's eye. Were I to make out what I could see, it would be two women seizing a moment of pleasure and leaving the world behind..."
    mct "(...and Dalia wanted me to send them back?)"
    "*Chwup, fhwup...!*"
    "I would, of course. I'd pass them her message, like a good boy, but I wouldn't rob them of what was going on in front of me."
    "*Chwup, khwuuup, gwhupp...!*"
    lucy "Mmmhhh...! Ghaaak...! I'm... getting..."
    lucy "GGhh...! Ha... nnhyyyeees, I'm--"
    scene w2_6837 with dissolve
    harp "Not yet."
    lucy "H-huhh...?"
    harp "{b}Lie down{/b}."
    "Harper's voice, with an unusually commanding edge, carried loud and clear to my ears."
    scene w2_6838 with dissolve
    lucy "...ah, but..."
    "It was so potent I almost did as she asked..."
    scene w2_6839 with dissolve
    harp "{b}Trust me{/b}."
    scene w2_6840 with dissolve
    scene w2_6841 with dissolve
    scene w2_6840 with dissolve
    "Lucy just meekly nodded, giving herself over to Harper's care."
    scene w2_6842 with dissolve
    harp "G-gah, that look! You don't know how lucky you're making me feel."
    scene w2_6843 with dissolve
    lucy "Mmhh-!"
    "More than a kiss, it was a declaration."
    scene w2_6844 with dissolve
    lucy "{b}Oh!{/b}"
    scene w2_6845 with dissolve
    lucy "Ooofh!"
    "With surprising violence, Harper pushed Lucy onto her back."
    scene w2_6846 with dissolve
    harp "I'm going to take you to even greater highs."
    scene w2_6847 with dissolve
    "Harper sternly peered down at the raven-haired woman's soft body."
    "She wandered over all the generous curves, her cute paunch, and grabbable love handles..."
    scene w2_6848 with dissolve
    harp "Show me..."
    scene w2_6849 with dissolve
    lucy "...what?"
    scene w2_6847 with dissolve
    "Harper didn't answer her."
    scene w2_6850 with dissolve
    lucy "Okay..."
    scene w2_6851 with dissolve
    "Obediently, Lucy spread her legs, revealing herself plain as day to her lover."
    "What I wouldn't give to be inside Harper's head right now, to have a front row seat to the show..."
    "........."
    "......"
    "..."
    "Harper just stared, a smile on her face..."
    scene w2_6852 with dissolve
    lucy "S-say something...!"
    stop music
    play sound "sound effects/thud-floor.mp3"
    scene w2_6853 with vpunch
    lucy "Ooooh-!"
    "Almost in exaggeration, Harper pounced on the embarrassed woman like she was prey, diving head first into her soft body."
    scene w2_6854 with dissolve
    harp "Let's continue."
    lucy "Ha... you're so..."
    play music "music/too-cool.ogg"
    scene e2_lhl_4_a with dissolve
    show e2_lhl_4
    "*Slurp, fwhiiip, chwup...!*"
    "Harper slinked down, face-to-face with her partner's lady parts, and began the dutiful task of elevating the needy teacher to the previously promised greater height of pleasure."
    lucy "Haaaaaeeuugh....!"
    "Harper took it slowly. Deliberately."
    "*Chwu, fwhip, sluurrp!*"
    "Her tongue scraped Lucy's slit, parting her lips and inching toward Lucy's exposed pleasure buzzer."
    lucy "Ah, ha.... gyaah... feels..."
    "Lucy, unafraid to let her voice out, started with a shrill cry."
    lucy "F-feels... good... ah..."
    scene e2_lhl_4a_a with dissolve
    show e2_lhl_4a
    "Harper's tongue just continued, with purpose, as if worshiping the school teacher's lower mouth."
    "She never slowed. She never stopped to take a breath."
    "She never got ahead of herself and sped on in excitement."
    "Instead, she used her tongue to cradle Lucy's clit, gently enveloping and savoring it with care."
    "Loving it."
    lucy "Oh... ohhhh..."
    "{b}Teasing{/b} it."
    lucy "HAaAaat, that's the sp-spo-spohtt...!"
    scene e2_lhl_4_a with dissolve
    show e2_lhl_4
    "In no time flat, Harper had the scholarly slut sounding like an idiot, calling out undaunted, safe in the knowledge that..."
    mct "(That no one but Harper could hear her...)"
    scene w2_6855 with dissolve
    "The thought flooded me with a perverted rush. The same I used to get peeping on the neighborhood moms."
    "In the absence of a conscience, I had always hoped a measure of self-awareness and the goal of living a respectable life would keep me from the impulses of my youth."
    mc "......"
    mc "..."
    scene w2_6856 with dissolve
    lucy "Oo-ooohh, OOoohhhhahhyyy....!"
    scene w2_6857 with dissolve
    mc "Hmpfh."
    scene e2_lhl_5_a with dissolve
    show e2_lhl_5
    "When I looked back, Harper had changed positions, moving atop the busty woman and writhing carnally."
    lucy "Mmhhh...! Haa....!"
    scene e2_lhl_5a_a with dissolve
    show e2_lhl_5a
    "Their chests were pressed together in a beautiful mish-mash of tit flesh."
    "Harper's nipples, erected to a point, painstakingly clashed with her lover's own chest."
    harp "Ah, c-come on...."
    harp "Move your hips more..."
    "Unlike before, Harper's own pleasure was written plain-as-day on her face."
    harp "I've taught you better than this, right?"
    harp "Move 'em like I'm paying you!"
    scene e2_lhl_5_a with dissolve
    show e2_lhl_5
    lucy "Mmmmggg...! Ah...! I aaaaaam...."
    "Lucy's voice came out in a plaintive, girly whine unfitting of her mature demeanor."
    harp "No you're not... ah, fuck me like I'm a client...!"
    "The neediness in Harper's own voice was palpable."
    harp "Like... ah... fuck me like you're in a hurry to get rid of me..."
    scene e2_lhl_5b_a with dissolve
    show e2_lhl_5b
    lucy "Ah...!"
    "Pinned down as she was, Lucy did her best to aid in the friction."
    lucy "I... I am...! I've just never done this before...!"
    "Every time Harper would push into her, grinding their sweet spots together, Lucy pushed back."
    lucy "L-like this...?"
    harp "Uh-huh... ah... that's the way, Lucy..."
    harp "That's the way, sweetheart!"
    lucy "Guhh...!"
    scene w2_6858 with dissolve
    lucy "Ugh... w-hy am, achk, why... why am I so horny tonight? Even after that bastard... ah..."
    scene w2_6859 with dissolve
    harp "Don't think about that creep. Just focus..."
    scene w2_6860 with dissolve
    lucy "Ah..."
    harp "Just focus on this here, right now....!"
    lucy "Ha, y-you're right, Harper...."
    scene e2_lhl_5_a with dissolve
    show e2_lhl_5
    harp "Let's just make each other feel good!"
    lucy "O-ohhhhy...!"
    "The pair humped each other with great fervor, mashing their hips together as if fighting for their life."
    "It wasn't the hardest fucking, but it was as passionate and desperate of one as I'd ever seen."
    lucy "Are... are you feeling good too?"
    "She asked with a genuine measure of concern in her voice, notable even through the libidinous overtone."
    harp "Haat, y-yeah..."
    harp "You're... doing... great...! Ngh...!"
    lucy "Ha... ha... I'm g-glad..."
    lucy "T-thanks for... thanks for... helping me these last few weeks..."
    harp "Save the mushy stuff until a-after...! Right now...!"
    harp "{b}Right now just be my dirty, filthy bitch{/b}."
    lucy "Ha... ha.... o-kay..."
    scene e2_lhl_5a_a with dissolve
    show e2_lhl_5a
    lucy "{b}F-fuck me{/b}, Harper."
    "Emboldened by her lover's request, Lucy called out without abandon."
    lucy "Fuck me, {b}please{/b}, baby....!"
    harp "Ah, that's it... beautiful...! Say my name...!"
    lucy "H-harper...!"
    lucy "Ah...ah, H-harper...!"
    harp "S-shit, Luce...! You're..."
    lucy "I'm your bitch! Your filthy bitch!"
    scene e2_lhl_5b_a with dissolve
    show e2_lhl_5b
    harp "Ahccckk...! I'll always...! I'll have your back, you know that?"
    lucy "I k-know...! S-so please... {b}please{/b} keep teaching me...!"
    lucy "I... I..."
    harp "What is it?"
    lucy "I'm going to... I'm there... I'm... Oooooohhhhh...!"
    scene w2_6861 with dissolve
    lucy "Oofofhhh...ssssshhhhhhh--!"
    "Throwing her head back, she came."
    "Her hips stopped all movement, she clung desperately to her partner, and she came."
    "The thump as she violently and involuntarily knocked the back of her head against the carpet could be heard from even here."
    scene w2_6862 with dissolve
    lucy "Ah.... eyee..."
    harp "You okay?"
    lucy "Y-yeah... I'm... ah... haa..."
    "......"
    "..."
    "The two held each other for a minute, and just when I thought I should step away..."
    scene w2_6863 with dissolve
    harp "Sorry, Lucy... hope you don't mind, but..."
    lucy "Huh...?"
    scene w2_6864 with dissolve
    lucy "Mmmnfh...?!"
    "Harper abruptly shoved her cunt in Lucy's face, pressing her vulva firmly into the absent-focused teacher's nose."
    harp "I'm still not satisfied...! Bear with me, please!"
    scene e2_lhl_6_a with dissolve
    show e2_lhl_6
    lucy "Mhhff...! Mmhh...!"
    "Lucy could only grunt in acceptance and do her best as Harper began to ride her face into the dirt."
    mct "(Man, they are REALLY going at it...)"
    harp "Haaa...!"
    harp "Hang in there, beautiful... I'm just..."
    "Harper's hips moved in a rhythm like she was riding a cock, rocking back and forth over Lucy's mouth and nose, giving her mere moments to suck down another breath."
    harp "Ah, haaat... yeah, that's right... use your tongue... eat my cunt..."
    lucy "Mmmfh... mfhhhhh... mmmmhhh...!"
    "From the looks of it, Lucy was adjusting to the rough treatment, but her face was still mashed deeply in another person's sex."
    lucy "Mmmmmh...!!!!"
    "Harper was quickly being pulled into her own little world, one where she was solely focused on her pleasure."
    scene e2_lhl_6a_a with dissolve
    show e2_lhl_6a
    harp "Ah... ah-ha, ha...!"
    "The selfish change in tone kindled an even stronger fire in me, as my eyes were drawn to the way her chest hypnotically bounced while using the half-sensate woman's face."
    harp "Shh, yeeah... that's...!"
    "To end the discomfort as soon as possible for her lover, it was fast and frenzied as it needed to be."
    lucy "Bummfhh!"
    "Harper raced toward her own climax. Intentional or not, her rough treatment was in its own way a form of diligence."
    harp "C'mon, suck me harder! Ah...!"
    lucy "Bufu!"
    "*Fwhup, chkwwup... shhkklup...!!!!*"
    harp "Oooooh, ha-- g-good girl...!"
    "*Chwup, fhhhhhuuuuup!*"
    harp "I didn't expect you to..."
    harp "G-goood giiiiirl! Ah.. haaaa, haat...!"
    scene w2_6865 with dissolve
    harp "{b}Gaaaaaaaaaah....!{/b}"
    scene w2_6866 with dissolve
    "With a satisfied cry, Harper let loose on her poor lover's face, gushing profusely all over the submissive teacher's face."
    harp "Shheee.... ah..."
    lucy "Guhh, gffulll....!"
    "Harper made no attempt to stop it either. In fact..."
    scene w2_6867 with dissolve
    harp "Ha... drink it...!"
    lucy "Guhlugh... ghuuu... bufu... mmfh...!"
    "She was relishing her position of control."
    mct "(I can only imagine how rare those moments are for her...)"
    harp "Ah... ah, shoot, Lucy..."
    stop music fadeout 2.0
    scene w2_6868 with dissolve
    harp "Hehe, I made a mess of you..."
    lucy "Haa... haa.... ah..."
    scene w2_6869 with fade
    harp "Thanks, beautiful. From the bottom of my heart."
    scene w2_6870 with dissolve
    lucy "Haa... I've never done..."
    scene black with fade
    harp "You've already said that."
    "......"
    if not persistent.harperlucyW2Lez:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.harperlucyW2Lez = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    "..."
    $ renpy.end_replay()
    scene w2_6871 with circlewipe
    show screen textbox2 with dissolve
    "I waited ten minutes for the pair to collect themselves."
    "I considered barging in and using the opportunity of them being caught red-handed to make Dalia's point, but..."
    scene w2_6872 with dissolve
    "*Squeeeeeek*"
    "I didn't want to ruin their moment."
    mct "(There they come.)"
    scene w2_6873 with dissolve
    mc "Hey!"
    harp "O-oh...! Uh... [mcf]!"
    harp "What are you, uh..."
    scene w2_6874 with dissolve
    mc "Dalia sent me to find you two. She suspected you two might be goofing off or something..."
    scene w2_6875 with dissolve
    harp "Ah, that..."
    scene w2_6876 with dissolve
    lucy "She was helping me get my head straight. Being around that man... I'm still..."
    lucy "I'm still new at this."
    scene w2_6877 with dissolve
    mct "(Getting your head straight, eh?)"
    scene w2_6878 with dissolve
    mc "Understandable, I'm not here to bust your ass. Just doing as I'm asked."
    mc "Since your head is now straight, you should get back out on the floor. She doesn't want Mr. Byrnes to notice."
    scene w2_6879 with dissolve
    harp "Ha, right..."
    harp "Be sure to apologize and thank Dalia later, okay?"
    scene w2_6880 with dissolve
    lucy "I will!"
    scene w2_6881 with dissolve
    harp "Without her, we'd be a lot worse off."
    scene w2_6882 with dissolve
    harp "How'd you find us...?"
    scene w2_6883 with dissolve
    "Harper looked at me suspiciously, worried I might know."
    scene w2_6884 with dissolve
    mc "Jacob pointed me this way. Told me to knock since you guys were having a private conversation."
    mc "Trust Jacob to be a decent guy, am I right?"
    scene w2_6885 with dissolve
    harp "Yeah. He's the best."
    scene black with fade
    "Ultimately, I didn't make a production of it and all three of us went along our way."
    jump w2ExNavMenu





screen w2ExVelvetRoom:

    imagemap:

        imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w2ExNavMenu")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]



        idle "gui/screens/imagemaps/w2ExVelvetRoom_idle.png"
        hover "gui/screens/imagemaps/w2ExVelvetRoom_hover.png"
        ground "gui/screens/imagemaps/w2ExVelvetRoom_ground.png"
        hotspot (0,390,600,600) action Jump("w2ExMercedesB")
        hotspot (378,565,480,600) action Jump("w2ExDaliaB")
        hotspot (490,260,600,300) action Jump("w2ExFreeRoamEnd")
        hotspot (1141,223,600,600) action Jump("w2ExEmmaB")
        hotspot (1601,216,600,600) action Jump("w2ExWarrenB")
        hotspot (1340,433,600,600) action Jump("w2ExNicoB")


label w2ExVelvetRoom:
    show black
    $ renpy.music.play("music/landing.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w2ExVelvetRoom with fade



label w2ExDaliaB:

    if w2ExDaliaBRepeat == False:
        $ w2ExDaliaBRepeat = True

        scene w2_6889 with dissolve
        "Off in the corner was Dalia, having once more joined up with her adoring patron."
        "He was..."

        if VeroFlag == True:
            mct "(I sure hope Dalia cleaned herself out after our tryst in the sauna, otherwise...)"
            scene w2_6890 with dissolve
            dal "You can do better, Andrew."
            mct "(Gross. Let's not think about it.)"
            scene w2_6891 with dissolve
            mct "(Oh..?)"
            "She's looking right at me."
            "Through chance, our eyes met and I reflexively gave a curt wave to the preoccupied prostitute."
            scene w2_6892 with dissolve
            scene w2_6891 with dissolve
            "She gave a slight nod, acknowledging me."
            "Out of context, she looked kinda cool..."
            jump w2ExVelvetRoom
        else:

            "He was on his knees, servicing her. Compared to the other girls..."
            scene w2_6893 with dissolve
            "She had it made."
            scene w2_6890 with dissolve
            dal "{b}Do better{/b}, Andrew."

            if jacobHarpVouch or w2HarpRainCheck:
                scene w2_6891 with dissolve
                mct "(Oh..?)"
                "She's looking right at me."
                "Through chance, our eyes met and I reflexively gave a curt wave to the preoccupied prostitute."
                scene w2_6892 with dissolve
                scene w2_6891 with dissolve
                "She gave a slight nod, acknowledging me."
                "Out of context, she looked kinda cool..."
                jump w2ExVelvetRoom
            else:
                jump w2ExVelvetRoom
    else:


        scene w2_6889 with dissolve
        mct "(He's still at it...)"
        jump w2ExVelvetRoom

label w2ExWarrenB:

    if w2ExWarrenBRepeat == False:
        $ w2ExWarrenBRepeat = True

        scene w2_6894 with dissolve
        "Out of the way stood Warren, presumably standing guard. Now, what he was warding against I couldn't imagine, but..."

        scene w2_6895 with dissolve
        if w2ExEmmaBRepeat == True:
            "Currently, he was eyeballing Emma something fierce."
        else:
            "Currently, he was eyeballing one of the house girls something fierce."

        "His vacant, hungry expression gave me the creeps and..."
        scene w2_6896 with dissolve
        "I wasn't the only one who noticed."
        scene w2_6897 with dissolve
        war "Heh..."
        scene w2_6898 with dissolve
        "....."
        "..."
        scene w2_6894 with dissolve
        "I should quit staring at the man."
    else:
        scene w2_6894 with dissolve
        "Yep, he's still leering..."

        if w2TIWarrenDaliaRepeat == True:
            mct "(That prick.)"

    jump w2ExVelvetRoom

label w2ExEmmaB:
    if w2ExEmmaBRepeat == False:

        scene w2_6899 with dissolve
        if w2ExEmmaFavor == "unknown":

            if w2ExRosalindMingleARepeat == True:
                "Looks like that bizarre pair is still together, enjoying the... {i}art{/i}."
            else:
                "Two familiar faces were standing idly by, enjoyin the evening's... {i}art{/i}"

            "No point in approaching them."
            jump w2ExVelvetRoom
        else:

            $ w2ExEmmaBRepeat = True

            if w2ExRosalindMingleARepeat == True:
                "It seemed Mihir and his tit-fiend compeer made it down here just fine."
            else:
                "Two familiar faces were standing idly by, enjoying the evening's... {i}art{/i}"

            "Next to them was a face I recognized, but hadn't seen tonight."

            scene w2_6900 with dissolve
            if w2ExEmmaFavor == "fulfilled":
                "It was Emma. The house girl Jacob had asked me to watch out for and had done a good job of making herself scarce."
                "It seems Ian hadn't been by yet to retrieve her."
            if w2ExEmmaFavor == "promised":
                "It was Emma. The house girl Jacob had asked me to watch out for and the one I promised to try and score a night off for."
                "From what I gathered, she had done a good job at making herself scarce, but here she stood in the thick of things."
            if w2ExEmmaFavor == "watched":
                "It was Emma. The house girl Jacob had asked me to watch out for and had done a good job making herself scarce."

            scene w2_6901 with dissolve
            mc "Hello, gentlemen."

            if w2ExRosalindMingleARepeat == True:
                scene w2_6902 with dissolve
                mihir "Hello again, sir."
                "Mihir formally greeted me and Thomas gave an affirming nod, understandably more preoccupied with the immobile girl."
            else:
                scene w2_6902 with dissolve
                mihir "Hello. We haven't met."
                scene w2_6903 with dissolve
                mc "No, we didn't get a chance last week, Mr. Chatterjee."
                scene w2_6904 with dissolve
                mihir "I see you've taken care to learn everyone's name."
                "That was true. After last week, I made sure I was well-acquainted with the club's members."
                scene w2_6903 with dissolve
                mc "It seemed like a prudent thing to do, given my job."

            scene w2_6905 with dissolve
            mc "Hello to you as well, Emma."
            scene w2_6906 with dissolve
            emma "Ah, good evening Mr. [mcl]."
            "She awkwardly stared at me, startled by me addressing her by name and unsure of what else to say."
            scene w2_6907 with dissolve
            mc "How are you doing this evening?"
            emma "...h-huh?"
            "She didn't expect that one either."
            scene w2_6908 with dissolve
            mc "Jacob mentioned, out of concern, that you were having some family problems."

            if w2ExEmmaFavor == "promised":
                if kat_polite == True:
                    "Since Mrs. Pulman told me to enjoy the night as if I was a patron, my plan was to bend the rules a smidge and send her off to one of the rooms to \"wait for me\", but I would need to wait for when she was otherwise disengaged."
                else:
                    "Since Kathleen told me to enjoy the night as if I was a patron, my plan was to bend the rules a smidge and send her off to one of the rooms to \"wait for me\", but I would need to wait for when she was otherwise disengaged."

                "Until then, I just wanted to speak with her."

            scene w2_6909 with dissolve
            emma "Oh... he did? He really shouldn't... ah..."
            scene w2_6910 with dissolve
            "The poor woman had an unseemly amount of bruising on her torso..."
            scene w2_6909 with dissolve
            emma "I'm fine. Nothing the other girls haven't faced."
            scene w2_6910 with dissolve
            "That was most certainly a lie. She looked unnaturally pale, with bags noticeable under her eyes even through her caked on makeup."
            scene w2_6911 with dissolve
            mc "Sorry, we don't really know each other, but I thought I'd ask."
            "Try as she might to hide it, the woman that stood in front of me had the body language of a perpetually frightened guinea pig."
            scene w2_6909 with dissolve
            emma "No, thank you for asking... I just... Jacob shouldn't have said anything."
            scene w2_6912 with dissolve
            mc "He was concerned and just--"
            "Emma flinched from my touch."
            scene w2_6911 with dissolve
            mc "Ah..."
            mc "Don't be mad at him. He just asked me to keep an eye out for you because he's concerned."
            scene w2_6909 with dissolve
            emma "Ha... I'm..."
            scene w2_6913 with dissolve
            emma "You don't need to, I'm okay."
            scene w2_6914 with dissolve
            emma "I'm going to... uh... well, thanks."
            scene w2_6915 with dissolve
            "Pulling away from me, she rejoined the two men she was shadowing."

            if w2ExEmmaFavor == "fulfilled.":
                "Hopefully Ian would be here soon."
            if w2ExEmmaFavor == "promised":
                "Hopefully I'll get the chance to send her off soon."

            jump w2ExVelvetRoom
    else:

        scene w2_6899 with dissolve
        "Emma was still hanging around Mihir and Thomas, doing her best to look occupied despite their clear lack of interest in her."
        jump w2ExVelvetRoom

label w2ExNicoB:

    if w2ExNicoBRepeat == False:
        $ w2ExNicoBRepeat = True

        scene w2_6916 with dissolve
        nico "Gh... haa....! Mr. Wayyyyylon...!"
        eric "Ah... shit. This new girl tastes so fucking bland, Sammy!"
        scene w2_6917 with dissolve
        eric "*Glug... glug... glug...!"
        scene w2_6918 with dissolve
        eric "You want some?"
        nico "S-sure..."
        scene w2_6919 with dissolve
        eric "Good. Maybe it'll loosen you up!"
        nico "Gehh...!"
        play ambient "sound effects/gulp.wav"
        scene w2_6920 with dissolve
        sam "Sheesh man, you're never happy with any of the girls. Do you even like women?"
        eric "Fuck you, you dried up steroid-jockey. It's not my fault this place is full of dirty whores."
        sam "...you're in a brothel, you know that, right?"
        stop ambient
        scene w2_6921 with dissolve
        "......"
        "..."
        if VeroFlag == True:
            "Even after serving Samson..."

        "Poor Nicolette was truly being put through the wringer tonight."
        jump w2ExVelvetRoom
    else:

        scene w2_6922 with dissolve
        sam "Holy shit. Hurry up, Eric."
        sam "I want a turn."
        "Seems her night was just beginning."
        jump w2ExVelvetRoom

label w2ExMercedesB:

    if w2ExMercedesBRepeat == False:
        $ w2ExMercedesBRepeat = True

        scene w2_6923 with dissolve
        if w2ExEmmaBRepeat == True:
            "Yet another piece of human art, although the two men standing in front of this one didn't seem as interested."
        else:
            "One of the house girls was put on display, strapped into some sort of device. The two men in front of her didn't seem all that interested though."
    else:

        scene w2_6924 with dissolve
        "They look to be having a pretty lively conversation..."


    jump w2ExVelvetRoom

label w2ExFreeRoamEnd:

    if w2ExKathleenBRepeat == False:
        $ w2ExKathleenBRepeat = True
        scene w2_6925 with dissolve
        if kat_polite == True:
            mct "(There's Mrs. Pulman and...)"
        else:
            mct "(There's Kathleen and...)"

        "An ugly, fat, naked old man."

        scene w2_6926 with dissolve
        "If I go over there right now, I may just get pulled into something for the rest of the night."
        hide screen textbox2 with dissolve

        menu:
            "Go over there.":
                jump w2ExKathleenB
            "Kill time some other ways first":

                show screen textbox2 with dissolve
                mct "(I'll go have a peek elsewhere first.)"
                jump w2ExVelvetRoom
    else:

        scene w2_6925 with dissolve
        "Should I go over there finally?"
        hide screen textbox2 with dissolve

        menu:
            "Go speak with Mrs. Pulman.":
                jump w2ExKathleenB
            "Kill time some other ways first.":

                show screen textbox2 with dissolve
                mct "(I'll go have a peek elsewhere first.)"
                jump w2ExVelvetRoom

label w2ExKathleenB:

    stop music fadeout 3.0
    scene w2_6927 with dissolve
    show screen textbox2 with dissolve
    kat "Mr. [mcl]. I'm glad you found your way here."
    scene w2_6928 with dissolve
    kat "Sit down, won't you?"
    shel "Plenty of room."
    scene w2_6929 with dissolve
    "...the only seat being next to the naked congressman currently getting blown."
    scene w2_6930 with dissolve
    mc "Thank you."
    "I left as much \"polite\" space between us as physically possible."
    play music "music/cello-suite-No-1-G-Major-Prelude.ogg"
    scene w2_6931 with dissolve
    kat "Have you been enjoying yourself like I asked?"
    scene w2_6932 with dissolve
    mc "I've... mingled. {b}Observed{/b}."
    scene w2_6933 with dissolve
    kat "Just \"mingled\"...? That won't do."
    scene w2_6934 with dissolve
    kat "Andrea, see that [mcf] doesn't get cold."
    scene w2_6935 with dissolve
    andrea "Yes, Mrs. Pulman."
    mc "I'm... ah...!"
    scene w2_6936 with cmet
    "Before I could finish, a fat-ass redhead had invaded my person."
    scene w2_6937 with dissolve
    mc "Mr. O'Doherty looks lonelier than I do..."
    scene w2_6938 with dissolve
    "Not that I personally minded a lap warmer, the woman on top of me was beautiful and voluptuous."
    scene w2_6939 with dissolve
    "*Fwhup... chwup... hhuuwhp...!*"
    "'twas a nice distraction from the less palatable sight next to me."
    scene w2_6940 with dissolve
    jim "Don't worry... If I get cold..."
    scene w2_6941 with dissolve
    jim "Kathy will keep me warm, won't you?"

    if kat_polite == True:
        "For the brief moment, there was a glimmer of something repulsive and violent in Mrs. Pulman's eyes."
    else:
        "For the brief moment, there was a glimmer of something repulsive and violent in Kathleen's eyes."

    scene w2_6942 with dissolve
    kat "Jim, what I have told you...?"
    scene w2_6943 with dissolve
    "She caught herself though, quickly swallowing the bile and adopting a warm smile."
    scene w2_6942 with dissolve
    kat "Don't touch me, you {b}greased{/b} pig."
    scene w2_6943 with dissolve
    "......"
    "..."
    scene w2_6944 with dissolve
    jim "Ha! I almost lost this, didn't I?"
    scene w2_6945 with dissolve
    kat "Are you sure you don't want me to find you a girl? I could call up Alison if you like."
    kat "I know she was your favorite last year."
    scene w2_6946 with dissolve
    jim "She's still on the hook, eh? You're scarier than your husband."
    scene w2_6947 with dissolve
    shel "Speaking of, how is Judge Pulman?"
    kat "Albert is fine."
    scene w2_6948 with dissolve
    jim "Is he going to seek re-election?"
    kat "He hasn't decided. It's still too early."
    scene w2_6949 with dissolve
    shel "He's getting quite old."
    kat "Is he...?"
    shel "It's good to know when to bow out gracefully and give the newly deserving a chance to serve with honor."
    scene w2_6950 with dissolve
    kat "Thank your wife for me, Shelby. Her contributions to Eden Women's Relief Fund mean a lot."
    kat "I hope she'll--"
    scene w2_6951 with dissolve
    "*{b}Booop!{/b}*"
    mct "(She...)"
    scene w2_6952 with dissolve
    andrea "Hey!"
    "Booped me?"
    scene w2_6953 with dissolve
    mc "{i}Hey{/i}..."
    scene w2_6954 with dissolve
    andrea "Hehe...!"
    "She giggled with a genuine geniality, so totally out of place for her profession."
    scene w2_6955 with dissolve
    andrea "I know you don't care about what they're talking about, so put your arms around me instead, alright?"
    scene w2_6956 with dissolve
    mc "Why would I...?"
    scene w2_6957 with dissolve
    andrea "Hmpfh!"
    scene w2_6958 with dissolve
    andrea "Do you need a good reason to grab hold of something sexy, plump, and soft?"
    scene w2_6959 with dissolve
    mc "No, I don't, I guess..."
    scene w2_6960 with dissolve
    andrea "Thanks. Just wanna do what the boss lady asked me to, y'know?"

    if w2ExEmmaFavor == "fulfilled":
        scene w2_6961 with dissolve
        andrea "Never seen the young prince sniff up that tree."
        scene w2_6962 with dissolve

        if w2ExEmmaFavorIan == True:
            "Looked like Ian finally found Emma so he could occupy her time away from the rest of the patrons."
        if w2ExEmmaFavorChuck == True:
            "Looked like Ian finally found Emma so he could tell her she had the night off."

        scene w2_6963 with dissolve
        mc "How long have you been here?"
        scene w2_6964 with dissolve
        andrea "Just a few months. I started in the spring."
        andrea "Guess that makes me your senior."
    else:

        scene w2_6965 with dissolve
        mc "Can I ask you something?"
        scene w2_6966 with dissolve
        andrea "Anything!"
        mc "How long have you been here?"
        andrea "Just a few months. I started in the spring - heh, which I guess technically makes me your senior!"


    scene w2_6967 with dissolve
    andrea "Feel free to call me big sis if you like."
    scene w2_6968 with dissolve
    mc "How..."
    scene w2_6969 with dissolve
    mc "*Whispering* How'd Emma get those bruises?"

    if w2TIWarrenDaliaRepeat:
        "I wanted to confirm what I suspected from overhearing Dalia and Warren's conversation yesterday."

    scene w2_6970 with dissolve
    andrea "Ah, that... ooohf... uh..."
    scene w2_6971 with dissolve
    andrea "*Whispering* Warren got a lil' more than handsy."
    "I was surprised she was so honest."
    scene w2_6969 with dissolve
    mc "*Whispering* He makes a habit out of that?"
    "I don't know why I was asking. Knowing he's an abusive piece of shit didn't do me any favors."
    scene w2_6970 with dissolve
    andrea "Well..."
    "I couldn't fire him and it wasn't like I was going to quit..."
    scene w2_6972 with dissolve
    andrea "I don't think so? Haven't been here very long, remember...?"
    scene w2_6971 with dissolve
    andrea "*Whispering* Dalia warned us it was a once in a blue moon thing."
    scene w2_6973 with dissolve
    mc "Hmm... thanks for being so candid with me."
    scene w2_6972 with dissolve
    andrea "The only people you should lie to are the customers."
    scene w2_6973 with dissolve
    mc "Did Dalia teach you that?"
    scene w2_6974 with dissolve
    andrea "Hehe, nope! My mom!"
    andrea "She sold bridal dresses!"
    scene w2_6975 with dissolve
    mc "Of course, she did!"
    "I didn't know if her air headedness was an act or not, but Andrea was doing a good job putting me at ease. I could see why she worked here."
    scene w2_6976 with dissolve
    shel "Ah, fuck me, I'm about to explode...!"
    shel "Since you aren't doing such a great job making me cum..."
    mct "(Guess he's about to...)"
    scene w2_6977 with dissolve
    shel "You can at least be a proper fucking toilet bowl!"
    "Piss...?!"
    scene w2_6978 with dissolve
    cass "Ghh....?!"
    scene e2_freebeer_a with dissolve
    play ambient "sound effects/gulp.wav"
    show e2_freebeer
    shel "Ah... drink it until your belly is full, you slut!"
    cass "*Glug, glug... gluhg...!*"
    shel "I got a lot more where that came from!"
    cass "*Glug, glug...!*"
    stop ambient
    scene w2_6979 with dissolve
    cass "Pffwhbh...!"
    "That moment at ease was fleeting, as I watched a man piss down a woman's throat."
    kat "Charming."

    if kat_polite == True:
        "Naturally, neither Mrs. Pulman nor the corrupt police chief batted an eye."
    else:
        "Naturally, neither Kathleen nor the corrupt police chief batted an eye."

    scene w2_6980 with dissolve
    cass "Ha... ha...! T-thank..."
    cass "Thank you for the drink, sir..."
    scene w2_6981 with dissolve
    shel "Good girl. You took it well."
    scene w2_6982 with dissolve
    shel "Anyone else need to go? The toilet's free! Ha!"
    scene w2_6983 with dissolve
    jim "I'm good you weird fuck."
    scene w2_6984 with dissolve
    mc "Yeah... I went before I came..."
    "Thankfully the sadist in me was more surprised than excited."
    scene w2_6985 with dissolve
    kat "Well, now..."
    scene w2_6986 with dissolve
    kat "[mcf]. Would you mind letting everyone who's left in the lounge and halls know that they should make their way to the exhibition hall?"
    scene w2_6987 with dissolve
    mc "It's still a little early, isn't it?"
    scene w2_6988 with dissolve
    kat "Well we..."
    scene w2_6989 with dissolve
    kat "Got to give people notice so they can finish what they're doing. Understand?"
    mc "Right. Makes sense..."
    scene w2_6990 with dissolve
    mc "What about the Carnations?"
    scene w2_6991 with dissolve
    kat "Them? Oh..."
    scene w2_6992 with dissolve
    kat "I've already got them.... {i}plated{/i} nicely."
    scene w2_6993 with dissolve
    kat "Everyone! May I have your attention please!"
    scene black with fade
    stop music fadeout 3.0
    "......"
    "..."

    if w2ExEmmaFavor == "promised":
        $ w2ExEmmaFavor = "fulfilled"
        $ w2ExEmmaFavorSolo = True
        $ Jacob_Friendship += 1
        play music "music/cold-sober.ogg"
        scene w2_6994 with dissolve
        mc "Emma!"
        "As everyone was getting ready to move over into the exhibition hall, I found a moment where Emma was unattended."
        emma "...ah!"
        "She jumped at being called."
        scene w2_6995 with dissolve
        emma "...yes, sir?"
        mc "I didn't mean to startle you."
        emma "Oh, no, y-you didn't..."
        scene w2_6996 with dissolve
        "......"
        "..."
        scene w2_6997 with dissolve
        mc "You're not very convincing."
        scene w2_6998 with dissolve
        emma "Did you need something?"
        scene w2_6999 with dissolve
        mc "Actually, I did. Mrs. Pulman encouraged me to enjoy the night as if I'm a patron and..."
        scene w2_7000 with dissolve
        "I stopped myself short of touching the rattled woman, thinking better of it."
        scene w2_7001 with dissolve
        mc "I want you to go to Mahogany Room, set up a video camera, and strap yourself into that fancy leather saddle that's in there."
        mc "Endure it until well after the exhibition ends."
        scene w2_7002 with dissolve
        emma "Umm... why?"
        scene w2_7003 with dissolve
        mc "Maybe because I enjoy seeing women like you squirm?"
        "...and have video proof she was acting on behalf of my desires, should anyone miss her."
        scene w2_7002 with dissolve
        emma "You just want me to sit in an empty room for--"
        scene w2_7001 with dissolve
        mc "{b}That's an order{/b}. From Mrs. Pulman to me to you."
        mc "Don't go too crazy with settings though, okay? Just... make yourself comfortable."
        scene w2_7002 with dissolve
        emma "You're saying two different--"
        scene w2_7004 with dissolve
        mc "{b}Go{/b}."
        emma "Ah, y-yes sir!"
        scene w2_7005 with dissolve

        if kat_polite == True:
            "Emma hurried off. With the promise I made to Jacob taken care of, I set on Mrs. Pulman's task of rounding up any stragglers."
        else:
            "Emma hurried off. With the promise I made to Jacob taken care of, I set on Kathleen's task of rounding up any stragglers."
        stop music fadeout 3.0
        scene black with fade
        "......"
        "..."

    jump w2ExStart


label w2ExStart:
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transition_training session with blinds
    $ renpy.pause(6, hard=True)
    $ date = "june13night"
    scene w2_7006 with curtains
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    "The curtains opened on the event just as they had last week, with the night's guests trickling in from various parts of the building."
    "Everyone seemed to be in good spirits, lightly drunk and engorged on the establishment's pleasures, but that was just an appetizer."

    play music "music/epic-battle-speech.ogg"
    scene w2_7007 with dissolve
    if kat_polite == True:
        "Mrs. Pulman stood eerily unmoving at center stage, waiting for things to settle down so she might begin her twisted spectacle."
    else:
        "Kathleen stood eerily unmoving at center stage, waiting for things to settle down so she might begin her twisted spectacle."
    scene w2_7008 with dissolve
    show june13night with squares
    "The Carnations, I discovered, were already on stage, put on display."
    "Primed and ready to be served up to the crowd."
    mct "(So this is what she meant by \"plated nicely\"...)"
    scene w2_7009 with dissolve
    "Hana stood next to me, and I in turn, found a place next to Ian. We were the only ones here south of forty, after all."
    scene w2_7010 with dissolve
    kil "You ever catch the start of one of these things?"
    scene w2_7011 with dissolve
    hana "I haven't had the \"pleasure\", fortunately."
    scene w2_7012 with dissolve
    mc "Get ready for a lot of talking."
    scene w2_7013 with dissolve
    hana "If only it were just talking..."
    scene w2_7014 with dissolve
    kil "Nervous, {i}Miss Rhodes{/i}?"
    scene w2_7015 with dissolve
    hana "Fuck off, you chode."
    scene w2_7016 with dissolve
    kil "After all your holier-than-thou shit, you're going to willingly graduate to pimp? Kinda fuckin' hilarious if you ask me."
    scene w2_7015 with dissolve
    hana "Then why aren't I laughing?"
    scene w2_7012 with dissolve
    mc "You properly introduce yourself to Felicia and Rosalind?"
    scene w2_7013 with dissolve
    hana "Yeah, it went a little better than with the scary big lady."
    scene w2_7012 with dissolve
    mc "Yeah, they're a little more congenial..."
    scene w2_7009 with dissolve
    kat "Is everyone settled and ready to begin?"
    scene w2_7017 with dissolve
    "A hush fell over the exhibition hall and all attention was on the stage. Things were about to begin."
    "A knot formed in the pit of my stomach and suddenly I was all too keenly aware of the overbearing lights blanketing the stage."
    scene w2_7018 with dissolve
    kat "Excellent. Then without further delay, tonight's theme is... {b}humbleness{/b}."
    kat "It was pride that changed angels into devils; it is humility that makes men as angels."
    scene w2_7019 with dissolve
    kat "So, I ask you devils, do these three caged women resemble angels?"
    scene w2_7020 with dissolve
    "The rhetorical question quieted what was left of the crowd's murmuring."
    scene w2_7021 with dissolve
    kat "No, no they absolutely don't, do they?"
    kat "Caged up like this, they look more like livestock."
    scene w2_7019 with dissolve
    kat "Well, {b}don't be fooled{/b}. Tarnished as it is, they each have their pride."
    scene w2_7028 with dissolve
    kat "In their need, they mistake themselves as deserving."
    scene w2_7022 with dissolve
    kat "Success...."
    scene w2_7023 with dissolve
    kat "Self-image..."
    scene w2_7024 with dissolve
    kat "Motherhood."
    scene w2_7025 with dissolve
    kat "Each an admirable pursuit, made a twisted mockery when seated in the mind of {b}failures{/b}."
    scene w2_7026 with dissolve
    kat "Such as, these sources of dignity are cancerous tumors in need of excision - and tonight, for your viewing pleasure, I will be the surgeon."
    scene w2_7027 with dissolve
    kat "The root word humiliation comes from Latin, meaning to \"humble.\""
    scene w2_7026 with dissolve
    kat "I will endeavor to humble these bitches and mold them into beautiful angels."
    scene w2_7028 with dissolve
    kat "...but I challenge them. {b}Endure{/b}."
    scene w2_7027 with dissolve
    kat "Angels are pitiful creatures, devoid of free will in heralding the vanities of their master."
    scene w2_7025 with dissolve
    kat "{b}Humility need not be a virtue{/b}. In fact, humbleness can be a deadly weapon."
    scene w2_7026 with dissolve
    kat "Shame need not topple you. In fact, it can give you strength."
    scene w2_7028 with dissolve
    kat "In humiliation, there is meaning. In--"
    scene w2_7029 with dissolve
    ver "Bullshit."
    scene w2_7030 with dissolve
    kat "Ha! You think, Miss Lynch? What say you, Mrs. Carter...?"
    scene w2_7031 with dissolve
    kat "Will you let humiliation destroy your resolve or will you use it to show our valued patrons what inner-strength looks like?"
    scene w2_7032 with dissolve
    rose "...I... I'll do my best, Mrs. Pulman."
    scene w2_7031 with dissolve
    kat "You'll do your best? Oh dear, you dumb cow..."
    scene w2_7033 with dissolve
    kat "Felicia?"
    kat "What do you think about all this?"
    scene w2_7034 with dissolve
    fel "Shame is, like all things of mind, a matter of perception."
    scene w2_7035 with dissolve
    kat "Ha! Leave it to a gold-digging whore to claim she has no shame."
    scene w2_7021 with dissolve
    kat "There you have it gentlemen. Our Carnations are going to prove I'm just an ineffectual, inept old woman tonight, incapable of imprisoning their spirits."
    scene w2_7019 with dissolve
    kat "Please, enjoy the night's entertainment."
    stop music fadeout 3.0
    scene w2_7036 with dissolve
    kat "Warren, get our \"princess\" out of her cage and on her knees. She went third last week, it is only proper she begins the night."
    scene w2_7037 with dissolve
    war "Yes, Ma'am."
    scene w2_7038 with dissolve
    kat "Hana, come up here for a moment dear. I want you to have a better look at our guests."
    scene w2_7039 with dissolve
    hana "Ah, shit, here I go..."
    scene w2_7040 with dissolve
    mc "Good luck..."
    scene w2_7041 with dissolve
    "Just as Hana took to the stage, they were joined by Veronica who had been guided and forced to her knees."
    scene w2_7042 with dissolve
    war "Har har har, good bitch."
    scene w2_7043 with dissolve
    kat "Now then..."
    scene w2_7044 with dissolve
    kat "I wanted you to get a good look at our patrons, Hana."
    play music "music/doll-dancing.ogg"
    scene w2_7045 with dissolve
    "Hana surprised me. She put on a confident face, keeping her shoulders straight and her eyes on the crowd."
    scene w2_7046 with dissolve
    kat "These are the faces of those that afford your mother's care."
    kat "It's not only you, either. We {b}all{/b} owe a lot to them."
    scene w2_7045 with dissolve
    "That was true. In a roundabout way, these men were paying for my college..."
    scene w2_7047 with dissolve
    kat "If you don't have a passing acquittance with August's daughter, then you at least are familiar with her glowering face."
    kat "Allow me to formally introduce to you my fellow judge of tonight's game, Miss Hana Rhodes. She's elected to take a more active interest in our activities."
    scene w2_7046 with dissolve
    kat "In time, {b}you may even come to regard this place as hers{/b}."
    scene w2_7045 with dissolve
    "......"
    "..."
    scene w2_7048 with dissolve
    hana "Ah, ha..."
    scene w2_7049 with dissolve
    hana "Hello."
    scene w2_7050 with dissolve
    "The crowd murmured in salutation, a mixture of curious expressions and lecherous grins."
    scene w2_7051 with dissolve
    kat "Yes, indeed! She will be an arbiter of our Carnations' fate tonight!"
    scene w2_7052 with dissolve
    hana "What do I have to do, exactly...?"
    scene w2_7053 with dissolve
    kat "You only need to watch and appraise, to decide who in their abjection, most finely displayed their determination and will."
    scene w2_7054 with dissolve
    hana "How the...?"
    "...{i}how the fuck do you judge that?{/i} Hana's look said it all."
    hana "I don't know what that looks like."
    scene w2_7055 with dissolve
    kat "You'll know it when you see it. What I ask of you tonight is to simply not look away and to observe closely."
    scene w2_7056 with dissolve
    kat "Contemplate why this proud and accomplished woman, who has contempt for anyone and everyone here - you included, dearie - is on her knees right now before us."
    kat "Why do you think that is, Miss Rhodes?"
    scene w2_7057 with dissolve
    hana "She's desperate and you're taking advantage."
    scene w2_7058 with dissolve
    kat "So true, but there's more to it than that..."
    scene w2_7059 with dissolve
    kat "Look up at Hana, slut."
    ver "Ha... give me a break..."
    scene w2_7060 with dissolve
    kat "Miss Lynch is trying to save her business, having lived her whole life chasing after a standard not a single human being could possibly live up to."
    kat "I dare say it's not her fault that her expectations are so high, but I'll go into that later."
    scene w2_7061 with dissolve
    kat "Now, Mrs. Carter..."
    kat "Her husband left her in a bad state, footing a bill made of his own stupidity and greed. Yet, it didn't happen overnight. There was an escalation of behavior."
    scene w2_7062 with dissolve
    kat "Ask yourself, why did she stick around and tolerate that fool for so long, even though the writing was on the wall?"
    scene w2_7063 with dissolve
    kat "Lastly we have Mrs. Ford. A woman who has spent a lifetime running away from the past and brilliantly distancing herself from her origins."
    kat "She's rich and she {i}says{/i} she's here for the kick of it. {b}What. {w}The fuck. {w}Is up. {w}With that?{/b}"
    scene w2_7064 with dissolve
    kat "Maybe tonight, I'll find answers to those questions myself. All you are required to do, however, is to commit their pathetic expressions to memory."
    scene w2_7065 with dissolve
    kat "By the end of the night, {b}you will feel something{/b}. You may not find it beautiful like I will, but you will feel something."
    scene w2_7064 with dissolve
    kat "You'll know who shined the most defiantly. You'll recognize who gave the most of themselves away, yet paradoxically, ended the night with more parts than they started with."
    scene w2_7066 with dissolve

    if kat_polite == True:
        "Hana's disgust with Mrs. Pulman was written plain as day on her face."
    else:
        "Hana's disgust with Kathleen was written plain as day on her face."

    scene w2_7067 with dissolve
    hana "I..."
    scene w2_7068 with dissolve
    hana "Whatever."
    "She didn't let it out."
    scene w2_7069 with dissolve
    kat "Good enough."
    kat "Now, one last thing..."
    scene w2_7070 with dissolve
    kat "The photoshoot."
    scene w2_7071 with dissolve
    mc "Welcome back."
    scene w2_7070 with dissolve
    hana "......"
    hana "..."
    mct "(I bet she's wishing she didn't talk to them before the show...)"
    kat "The photoshoot that received the most votes tonight was..."
    if mod_week2_rose_park:
        scene black with fade
        m_dev "My Master says since we really boosted Rose's photo count we get to rig the \"votes\" Who do you want to win?"
        menu:
            "Rosalind":
                jump mod_w2ExStart_r
            "Felicia":
                jump mod_w2ExStart_f
            "Veronica":
                jump mod_w2ExStart_v



    if w2FelShootPoints >= w2RoseShootPoints and w2FelShootPoints >= w2VeroShootPoints:
        label mod_w2ExStart_f:
        $ w2ShootWinnerFel = True
        scene w2_7072 with dissolve
        kat "Mrs. Ford. Congratulations, pig."
        scene w2_7073 with dissolve
        fel "I expected as much with that bullshit you pulled."
        scene w2_7072 with dissolve
        kat "You didn't react quite how I'd hoped."
        scene w2_7073 with dissolve
        fel "I'm sorry to disappoint you, Mrs. P."
        scene w2_7072 with dissolve
        kat "Oh, don't mention it. I'll get my gratification another way tonight."
        scene w2_7074 with dissolve
        "......"
        "..."
        scene w2_7075 with dissolve
        fel "So, what do I win?"
        scene w2_7076 with dissolve
        kat "Oh, good question..."
        kat "Hmm, let's see..."
        scene w2_7077 with dissolve
        hana "*Whispering* Does she really not know or is she just being a cunt?"
        kil "*Whispering* Could be both."
        mc "*Whispering* Definitely the last part..."
        scene w2_7072 with dissolve
        kat "You have the audience's vote. Now all you need is one more vote, from either Hana or myself, and you'll be crowned tonight's winner. Congratulations."
        scene w2_7073 with dissolve
        fel "So it's in the bag then?"
        scene w2_7078 with dissolve
        kat "{size=-10}Oh, you stupid whore...{/size=-10}"

    elif w2RoseShootPoints >= w2VeroShootPoints and w2RoseShootPoints >= w2FelShootPoints:
        label mod_w2ExStart_r:
        $ w2ShootWinnerRose = True
        scene w2_7079 with dissolve
        kat "Mrs. Carter, amazingly! Good job, you fat-titted cow."
        scene w2_7080 with dissolve
        rose "Ah...!"
        hana "{size=-10}Shit, her first reaction is to smile... fuckin' gut-wrenchin'...{/size=-10}"
        scene w2_7081 with dissolve
        rose "So, I... what does that mean?"
        scene w2_7082 with dissolve
        kat "Oh, I did say you'd get an advantage didn't I?"
        kat "Hmm, let's see..."
        scene w2_7077 with dissolve
        hana "*Whispering* Does she really not know or is she just being a cunt?"
        kil "*Whispering* Could be both."
        mc "*Whispering* Definitely the last part..."
        scene w2_7083 with dissolve
        kat "You have the audience's vote. Now all you need is one more vote, from either Hana or myself, and you'll be crowned tonight's winner."
        rose "Oh, o-okay... great..."
    else:

        label mod_w2ExStart_v:
        $ w2ShootWinnerVero = True
        scene w2_7084 with dissolve
        kat "Miss Lynch. Guess most people liked seeing a bitch be put in her proper place."
        scene w2_7085 with dissolve
        ver "{b}Great{/b}."
        scene w2_7084 with dissolve
        kat "Isn't it? You worked so hard, crawling around on your hands and knees."
        scene w2_7085 with dissolve
        ver "What's my prize?"
        scene w2_7086 with dissolve
        kat "I did promise something, didn't I?"
        kat "Hmm, let's see..."
        scene w2_7077 with dissolve
        hana "*Whispering* Does she really not know or is she just being a cunt?"
        kil "*Whispering* Could be both."
        mc "*Whispering* Definitely the last part..."
        scene w2_7087 with dissolve
        kat "You have the audience's vote. Now all you need is one more vote, from either Hana or myself, and you'll be crowned tonight's winner. Aren't you happy?"
        ver "Not at all, you crazy cunt."

    stop music fadeout 3.0
    scene w2_7088 with dissolve
    kat "Now! Let's say we begin. Warren, Mr. Beaufort... bring out the equipment."
    scene w2_7089 with dissolve
    kat "You'll be my shadow tonight, Mr. [mcl]."
    mct "(What does that mean...?)"
    scene black with fade
    "......"
    "..."

label w2ExVeronicaHumiliation:
    scene w2_7090 with w20
    "I quickly had my answer."
    play music "music/devious-little-smile.ogg"
    scene w2_7091 with dissolve
    mct "(She's waiting, and everyone's watching. Hana included.)"
    scene w2_7092 with dissolve
    "{b}Hana especially{/b}."

    if kat_polite == True:
        "I was to follow Mrs. Pulman's lead tonight, and in her words, do what felt natural."
    else:
        "I was to follow Kathleen's lead tonight, and in her words, do what felt natural."

    scene w2_7093 with dissolve
    "...and her first item of instruction, while she took a brief leave, was to take these steel handcuffs and restrain the vaguely nervous-looking bodybuilder."
    scene w2_7094 with dissolve
    mc "Sorry, Veronica. I'm to cuff you..."
    scene w2_7095 with dissolve
    ver "Don't apologize so flippantly. It's annoying."
    scene w2_7096 with dissolve
    mc "Sorry about that."
    scene w2_7097 with dissolve
    ver "Well...? Go ahead."
    scene w2_7098 with dissolve
    mc "'Fraid not. Hands behind your back."
    scene w2_7099 with dissolve
    ver "You like saying that, you little pervert? I can hear it in your voice."
    scene w2_7100 with dissolve
    mc "Everyone's waiting."
    mc "As you like to say, \"let's get this over with.\" So, just turn around, please."
    scene w2_7101 with dissolve
    "Flashing a smirk, she did as requested and turned her broad and beautifully sculpted back my direction."
    mc "Hands, please."
    scene w2_7102 with dissolve
    "Bending over slightly, Veronica offered me her hands, placing them directly above her shapely, muscular ass."
    mct "(Certainly a nice sight...)"
    play sound "sound effects/handcuffs.wav"
    scene black with fade
    "She wasn't too far off with her accusation, was she [mcf]?"
    scene w2_7103 with dissolve
    mc "It's not too tight I hope."
    scene w2_7104 with dissolve
    ver "It's better if it is, am I right?"
    scene w2_7105 with dissolve
    ver "*Whispering* The rules of this game are pretty fucking vague. I don't know if I'm supposed to resist or pretend to be humiliated."
    scene w2_7106 with dissolve
    mc "Come on..."
    scene w2_7107 with dissolve
    "All eyes were on us."
    scene w2_7108 with dissolve
    mc "*Whispering* You and I both know you won't have to pretend. It's just a question of if you drop the tough act or not."
    scene w2_7109 with dissolve
    ver "...let's get this over with."
    scene w2_7110 with dissolve
    mc "Over there, Miss Lynch."
    scene w2_7111 with dissolve

    if kat_polite == True:
        "I watched her lightly sashay to where she would next be bound, the second step in the missing Mrs. Pulman's instructions."
    else:
        "I watched her lightly sashay to where she would next be bound, the second step in the missing old woman's instructions."

    scene w2_7112 with dissolve
    ver "I think I know what's next."
    mc "Bend over."
    scene w2_7113 with dissolve
    "Veronica allowed my light push to carry her body forward, draping her torso over the leather perch and giving me an eyeful of her sizably broad behind."
    scene w2_7114 with dissolve
    "I felt like giving it a little smack..."
    mct "(I am supposed to do what came naturally, but...)"
    scene w2_7115 with dissolve
    "Hana's eyes were glued to both of us, watching with apprehension of what's to come. It was likely she was going to see me do unsavory things as part of my job, but did I want to add to that?"
    "Do I care if I disgust her?"
    hide screen textbox2 with dissolve
    scene w2_7114 with dissolve
    menu:
        "A *small* smack wouldn't hurt."(chg=["hana_down","kathleen_up"]):
            $ Hana_Affection -= 1
            $ Kathleen_Affection +=1
            scene w2_7116 with dissolve
            play sound "sound effects/slap3.wav"
            scene w2_7117 with vpunch
            "*Smack!*"
            scene w2_7114 with dissolve
            show screen textbox2 with dissolve
            mc "I'm going to handcuff your legs now."
            "Shit. That had a louder crack than I intended."
        "Give her butt a rub instead."(chg=["veronica_passion_up"]):

            $ Veronica_Horniness +=1
            scene w2_7118 with dissolve
            "A compromise. A vaguely innocent touch tracing the curve of Veronica's left buttock."
            scene w2_7119 with dissolve
            mc "I'm going to handcuff your legs now, okay?"
            show screen textbox2 with dissolve
            ver "Ah..."
        "Control your urges. You're not an animal.":


            show screen textbox2 with dissolve
            mc "I'm going to handcuff your legs now, okay?"

    scene w2_7120 with dissolve
    ver "Guess I'm not going to do much moving. At least this thing is pretty soft."
    play sound "sound effects/handcuffs.wav"
    scene black with fade
    "One leg. Two legs."
    stop sound
    stop music fadeout 3.0
    scene w2_7121 with dissolve
    mc "Comfortable?"
    scene w2_7122 with dissolve
    ver "Seriously? Not a fucking chance... I'm staring down a bunch of old pricks nearly tits out right now."
    scene w2_7123 with dissolve
    mc "Fair point. I ask stupid things sometimes."
    scene w2_7124 with dissolve
    ver "...hey. Could you do me a favor, [mcf]?"
    "It was a shock to hear her address me so directly."
    mc "What is it?"
    scene w2_7125 with dissolve
    ver "*Whispering* I know you're a pervert, so don't even think about going easy on me tonight."
    scene w2_7126 with dissolve
    mc "Make it a good show, you mean?"
    scene w2_7127 with dissolve
    ver "*Gulp* Uh huh."
    scene w2_7128 with dissolve
    mc "We'll see."
    scene w2_7129 with dissolve

    if kat_polite == True:
        "With Mrs. Pulman leading the show, there was no danger of that."
    else:
        "With Kathleen leading the show, there was no danger of that."

    scene w2_7130 with dissolve
    kat "Good, she's in position."
    "Speaking of..."
    play music "music/thunder.ogg"
    scene w2_7131 with dissolve:
        subpixel True
        yalign 1.0
        xalign 0.6
        linear 10 yalign 0.15
    "Kathleen had rejoined us, minus her pants, and sporting..."
    "...a giant fuckin' dildo."
    mct "(Yeeesh...)"
    "Yeah, there was no danger of Veronica having it easy tonight."
    scene w2_7132 with dissolve
    kat "Beautiful. I see you got her strapped in nicely."
    scene w2_7133 with dissolve
    kat "Let's not dally then. You gentlemen ready to get to know this dumb slut a little better?"
    scene w2_7134 with dissolve
    "The crowd jeered, showing their interest, while Veronica very clearly tried to quiet her mind."
    scene w2_7135 with dissolve
    kat "I hope I'll be able to make this encounter as fun as our previous one."
    kat "However, I won't fuck you until you ask me to. Truly, we can just spend our time talking if that's what you desire."
    scene w2_7136 with dissolve
    ver "Oh, yeah...? What's the fucking catch?"
    ver "You're banking on that I'd rather take a plastic dick than be bored to death by your yapping?"
    scene w2_7137 with dissolve
    kat "..."
    scene w2_7138 with dissolve
    kat "Tell me, what are you afraid of?"
    scene w2_7139 with dissolve
    ver "Uh... what? {b}Normal shit{/b}."
    scene w2_7138 with dissolve
    kat "What's your greatest fear?"
    scene w2_7139 with dissolve
    ver "That the people I care about will be hurt, I guess?"
    scene w2_7140 with dissolve
    kat "Really? I call bullshit!"
    kat "You don't have anyone you care about. At least, not anymore."
    kat "Unless... don't tell me you're still hung up on that pretty ex-wife of yours?"
    scene w2_7141 with dissolve
    ver "Don't bring her into this!"
    scene w2_7142 with dissolve
    kat "Pssh! My, you're easy!"
    kat "If that's how you feel, you should've worked more on your marriage than you did your failing business."
    scene w2_7143 with dissolve
    ver "That has nothing to do with it. She wanted kids and I didn't."
    scene w2_7142 with dissolve
    kat "That WAS a convenient excuse, wasn't it? You could convince yourself it wasn't a personal {b}failing{/b}, so you could begrudgingly let go."
    scene w2_7144 with dissolve
    ver "Things just don't work out sometimes between people and that's okay..."
    scene w2_7145 with dissolve
    kat "Don't look away from me unless you're ready for me to destroy you, Miss Lynch."
    scene w2_7146 with dissolve
    ver "I see... you think I'm going to beg for it just because you annoy me by going for some low-hanging fruit?"
    scene w2_7147 with dissolve
    kat "Of course not, that would be boring... Make no mistake bitch, thirty minutes from now and you'll be begging me NOT to stop, when I fuck all your vanity out of the already half-empty head of yours."
    scene w2_7148 with dissolve
    kat "I just thought your answer to my question about your biggest fear was... suspect."
    kat "All my research indicates you live a lonely, pathetic life of your own making. You have no one."
    scene w2_7149 with dissolve
    ver "Happiness doesn't come from other people."
    scene w2_7150 with dissolve
    kat "Ha! Mr. [mcl]!"
    scene w2_7151 with dissolve
    "Like a shadow, I moved as I was beckoned."
    scene w2_7152 with dissolve
    mc "Yes?"
    scene w2_7151 with dissolve

    if kat_polite == True:
        "Mrs. Pulman's line of questioning even irked me, as I began to grasp how this \"game\" of hers would go."
    else:
        "Kathleen's line of questioning even irked me, as I began to grasp how this \"game\" of hers would go."

    "Dredging up the past, attacking sore spots, getting intimately personal - even in this absurd and ridiculous setting, it felt distasteful."

    scene w2_7153 with dissolve
    kat "If you wouldn't mind, would you please get Miss Lynch warmed up for me?"
    kat "I want to make sure I can easily fit when the time comes."
    scene w2_7151 with dissolve
    "She was confident Veronica would ask her to begin."
    scene w2_7152 with dissolve
    mc "How should I...?"
    scene w2_7154 with dissolve
    kat "*Whispering* Whatever you please, short of fucking her yourself. That would otherwise defeat the purpose of the scene I'm crafting."
    scene w2_7155 with dissolve
    mct "(Whatever I want to, huh...?)"
    scene w2_7156 with dissolve
    "Why do I keep getting distracted by her watching?"
    "Is it cause she's the only one here with any sense of decency?"
    scene w2_7157 with dissolve
    "......"
    "..."
    scene black with dissolve
    m_dev "Just a moment want to explain something"
    m_dev "w2ExPts are the week 2 exhibition points which determines who wins this weeks exhibition"
    m_dev "ver-veronica,ros-rosalind,fel-felicia these will be the short form i will used to indicate their w2ExPts"
    m_dev "Example:w2ExPts(ver)=+1 means +1 point for veronica to win the week 2 exhibition"
    m_dev "So choose accordingly so as to get your favorite girl to win"
    m_dev "At choice you will see current points for all girls in the top right corner fo the screen"
    m_dev "Anyway enough talk lets contine with game"
    scene w2_7158 with dissolve
    "Compartmentalize, [mcf]. I've accepted my part in this for my own self-gain."
    "Everything else is just noise."

    hide screen textbox2 with dissolve
    show screen mod_week2_expo
    menu:
        "Focus on Veronica's comfort."(chg=["hana_up","veronica_passion_up","kathleen_down"]):

            hide screen mod_week2_expo
            $ Hana_Affection += 1
            $ Veronica_Horniness += 1
            $ Kathleen_Affection -= 1
            "...it is what it is."

            scene w2_7159 with dissolve
            "My job is to help Veronica get through the night and to that end, as improbable as it was considering she's shackled butt naked to a stool, I would attempt to give her a brief window of pleasure."
            mc "*Whispering* Don't hold this against me when you get untied, alright?"
            scene w2_7160 with dissolve
            ver "I probably will, but what are you..."
            scene w2_7161 with dissolve
            ver "Hmpfh?"
            "With a slight touch, I tilted Veronica's head and conjoined our lips."
            "This, no doubt, from someone she found contemptable wouldn't do it under normal circumstances, but it was a start."
            scene vero_e2_warmup1_a with dissolve
            show vero_e2_warmup1
            mc "Hmaa...!"
            "A kiss to ease things into more carnal waters."
            ver "...ehh?"
            "...and how could I not, with it just hanging there?"
            ver "Hnngh...!"
            "My thumb caught and encircled at the redhead's areola through the fabric of her top, before fitting as much as I could of the full thing in my hand."
            ver "Hnggh...?"
            "In the same window, I managed to ferret my tongue into the slackjawed woman's mouth, clumsily interweaving the two appendages together."
            ver "Hnaaah..."
            "This wouldn't do it either, but it was a start."
            scene vero_e2_warmup2_a with dissolve
            show vero_e2_warmup2
            "Next, my lips broke from hers, lingering down to Veronica's thick and pale neck."
            "*Smooch, fwoooh, cwhup...!*"
            "Small, tingly kisses."
            ver "Oh... what the..."
            "Small, varied kisses to suss out where best I might find purchase to tease this particular stretch of erogenous zone."
            scene w2_7162 with dissolve
            ver "Ehh..!"
            mct "(There! I found it!)"
            scene w2_7163 with dissolve
            "Wrapping my lips where I deemed Veronica's neck most sensitive, I nibbled and sucked, using my tongue to soften the flushed flesh and then lightly grazing it with my teeth make her flinch."
            "*Smmfwooch, fwhoop, ch...!*"
            scene w2_7164 with dissolve
            ver "D-damn it... what the hell are you doing, you weirdo?"
            ver "You think this is the kind of situation where you just go necking on a woman?"
            scene w2_7165 with dissolve
            ver "*Whispering* Read the room, you're boring everyone."
            "That was likely true, but..."
            scene w2_7166 with dissolve
            mc "Fuck everyone else."
            scene w2_7167 with dissolve
            "I deliberately said it loud enough for some people to hear, in the dumb hope it might make her feel like I'm on her side."
            scene w2_7168 with dissolve
            mc "I know I'm not choice, but at least..."
            scene w2_7169 with dissolve
            mc "*Whispering* My fat head is partially in the way of your view of those old perverts, am I right?"
            scene w2_7170 with dissolve
            ver "......"
            scene w2_7171 with dissolve
            ver "..."
            scene w2_7172 with dissolve

            if w2VeronicaHeated == True:
                ver "Do... do my ears... like you last time..."
                "So, she had a request..."
            else:
                ver "My ears. My ears are... {i}sensitive{/i}."
                mct "(Is she directing me to...?)"

            scene w2_7173 with dissolve
            mc "Okay!"
            scene w2_7174 with dissolve
            "Feeling like I had gained a little of Veronica's trust, I moved my attention to her earlobe."
            ver "Hmm...!"
            "A jolt of pleasure immediately ran through the Amazon's body, causing a clangorous din as her restraints knocked together."
            scene w2_7175 with dissolve
            "In contrast with her overshadowing physique, what rolled across the tip of my tongue was a small, delicate nub like any other woman's."
            ver "O-ohhh!"
            scene w2_7176 with dissolve

            if w2VeronicaHeated == True:
                "Just like a few days ago, it proved VERY effective."
            else:
                "I'll be damned, she wasn't kidding. Her ears were the ticket."

            ver "Gaah...!"
            "Sweet moans gradually began to escape her lips."
            scene w2_7177 with dissolve
            sam "I'll be damned, that frigid bitch actually asked for something."
            jim "She didn't seem frigid last week."
            scene w2_7178 with dissolve
            hana "..."
            frank "Look at her expression. She's actually feeling it from just her ears!"
            scene w2_7179 with dissolve
            ver "Nggh, haat...!"
            "The way her neck twitched and jerked made delicately balancing her ear between my teeth a mindful task, conscientious as I was of not hurting the woman in the grasp. "
            scene w2_7180 with dissolve
            kat "Mr. [mcl]?"

            if kat_polite == True:
                "Mrs. Pulman's voice pulled me away from my ear buffet."
            else:
                "Kathleen's voice pulled me away from my ear buffet."

            scene w2_7181 with dissolve
            mc "Yes, Ma'am?"
            scene w2_7182 with dissolve
            kat "Switch ends, will you? I have some stuff I want to talk about with Miss Lynch."
            scene w2_7183 with dissolve
            ver "Oh, great..."
            scene w2_7184 with dissolve
            mc "Focus on the feeling. Don't think about me or whatever the old woman is going to do with you, okay?"
            scene w2_7185 with dissolve
            "I was asking something preposterous, but mind over matter seemed right up Veronica's alley."
            scene w2_7186 with dissolve
            "Slipping behind the silent redhead, I once again got an eyeful of her beautifully buff butt."
            "A sight fat and juicy enough to make a man want to dive in."
        "(w2expts(ver)=+1)Put on a good show for the crowd{vspace=50}."(chg=["hana_down","kathleen_trust_up","veronica_up"]):

            hide screen mod_week2_expo
            $ Hana_Affection -= 1
            $ Kathleen_Trust += 1
            $ Veronica_Affection += 1
            $ w2ExPointsVeronica += 1

            "Hana's feelings aside, Veronica did ask me not to take it easy on her."
            scene w2_7187 with dissolve
            mc "I'm going to just jump into it."
            scene w2_7188 with dissolve
            ver "What are you waiting for then?"
            scene w2_7189 with dissolve
            mc "Suck on them."
            scene w2_7190 with dissolve
            mc "The wetter the better."
            scene w2_7191 with dissolve
            ver "...yeah, I gotcha."
            scene w2_7192 with dissolve
            "In an agreeable display, Veronica pried apart her lips, giving me unfettered access to her mouth."
            "From my position above, I had a tantalizingly clear view of the soft lining of her throat and her deliciously pink tongue anxiously wriggling around."
            scene w2_7193 with dissolve
            mc "Have at it."
            "Like a venus fly trap being sprung, her mouth immediately enclosed on my fingertips the moment they touched the back of her throat."
            scene vero_e2_fsuck_a with dissolve
            show vero_e2_fsuck
            "*Chwup, fhwhuup~*"
            "Veronica made it intentionally theatrical, sucking on my digits to produce an exaggerated popping sound that could be heard well across the room."
            "As she did so, she peered up at me with a raging fire burning in her eyes."
            ver "Mmhh... *Chwup, fwhup..!*"
            "It was a complicated expression. A submissive display married with overpowering spirit..."
            ver "*Fwhh----uuuch!*"
            mct "(Damn it...)"
            "As cool as I was trying to play it..."
            ver "Fwuuuch, chwwwup, swwwup...!*"
            scene w2_7194 with dissolve
            ver "Fmmh... *cough, cough!* *Cwhup, fwwwup!* MMmh... *cough!*"
            "That look in Veronica's eyes had spurred me on.."
            "I moved as far back into her mouth as she would allow passage, grazing the back of her throat and unleashing a deluge of sticky saliva that drenched my fingers. "
            scene w2_7195 with dissolve
            ver "Mmmh, *cwhup, fwhup...!* *cough!* *Chwup, chwhuuup...!*"
            "My rudeness didn't impede her fervor, however. Her lips held my fingers firm, suctioning strong and strangling them with her tongue."
            mc "Ah...! That's..."
            scene w2_7196 with dissolve
            mc "Enough."
            "After all, I'm not the one supposed to be getting turned on here."
            scene w2_7197 with dissolve
            "I freed my fingers from the snake-like grip of her mouth and they were truly and sufficiently lubed up."
            mc "..."
            scene w2_7198 with dissolve
            ver "Well, what are you waiting for now?"
            "She's right."
            scene w2_7199 with dissolve
            ver "Ghukk!"
            "I had a job to do."
            scene w2_7200 with dissolve
            "I forgot I had more than two dozen eyes staring a hole in my back."
            "Best get to it."
            scene w2_7201 with dissolve
            "With my hand on Veronica's throat, I moved to her flank."
            scene w2_7202 with dissolve
            ver "Ah, hatta...!"
            "Perhaps surprisingly, my cold and wet finger disappeared into Veronica's fiery hot depths with relative ease."
            scene w2_7203 with dissolve
            mc "Get a good view of the crowd."
            "Probably not a bad trait to have when you're a bodybuilder."
            scene w2_7204 with dissolve
            ver "Hnng, just get on with it, you prick."
            scene w2_7203 with dissolve
            mc "Alright..."
            scene vero_e2_finger1_a with dissolve
            show vero_e2_finger1
            ver "Ah...!"
            "Without fanfare, I set to it. Furiously fingering the redhead's hole without any appreciable buildup."
            ver "Nghh, whooaaah...!"
            mc "Look everyone in the eyes!"

            if kat_polite == True:
                "Taking a page from Mrs. Pulman's book, I decided to play showman a little."
            else:
                "Taking a page from Kathleen's book, I decided to play showman a little."

            mc "They're here for you, slut."
            "With a firm grip on Veronica's neck, I made sure everyone had a clear view of her face."
            ver "Haa... I see 'em!"
            scene w2_7205 with dissolve
            ver "I see a bunch of limp-dicked old farts with one foot in the grave."
            scene w2_7206 with dissolve
            "I had to stop myself from agreeing with her."
            hana "..."
            scene vero_e2_finger1_a with dissolve
            show vero_e2_finger1
            "Veronica's acidic strategy aside, her body was physically responding to my rough treatment."
            "*Schlick, fwhlich...!*"
            ver "Haaa... c'mon, you can do better than this, can't you errand boy?"
            "*Fwhichk, slhiiick, slhick...!*"
            "Her spit on my fingers was quickly replaced by her other mouth's excretions, making gliding in and out of her sloppy hole an easy task."
            ver "Ha, haa.... you call this a warm up?"
            scene vero_e2_finger2_a with dissolve
            show vero_e2_finger2
            "Her words were at odds with her hips, bucking back into my hand with repeated numbing impact."
            "Honestly, going this angle, this hard... I couldn't go any faster if I wanted to."
            ver "Haa, haaa...."
            "My hand was already hurting."
            ver "Ha, mmmhhha.... give me... something to work with here... I'm a big gal..."
            ver "Elsewise, I... ha... might just vomit looking at all these ugly faces."
            "Not quite convincing when being choked out in breathy moans, but..."
            jim "I preferred when she was sucking. She was a lot more quiet."
            ver "Oh, yeah..."
            scene vero_e2_finger3_a with dissolve
            show vero_e2_finger3
            chuck "Ha! Amazing!"
            "Veronica, surprisingly, accommodated the man's request, wrestling her neck from my grip just enough to wedge my finger into her mouth."
            ver "Bwuhtter, ywhoo fhatt fhwuck?"
            frank "I really like this one. Better than all the ones from last year combined."
            jiji "I agree!"
            "It seemed she got the reaction she was hoping for."
            scene vero_e2_finger4_a with dissolve
            show vero_e2_finger4
            "To my surprise, despite my aching wrist, I miraculously found the wherewithal to go faster."
            ver "Ha, haa... fhucking... fhwwlooodd...!"
            "She wasn't sucking on it as she did before, but the gesture was enough to conjure that indomitable image in my mind."
            ver "Ha... haaahht...! Thwereshnh ehy ess, gwreeenbboowy!"
            ver "Ha, haa...!"
            "Her strained voice made my pants equally as stiff."
            "*Shlick, shlick, fwhiclkk...!*"
            "Splashes of femcum had made its way past my top knuckles by this point, nearly reaching my wrist."
            mct "(I--)"
            scene w2_7207 with dissolve
            kat "Mr. [mcl]?"
            scene w2_7208 with dissolve
            "I had forgotten all about the old woman until her voice pulled me away from her mission."
            mc "Uh... *ahem, yes, Ma'am?"
            scene w2_7209 with dissolve
            kat "Move over and shift tactics, will you? I have some stuff I want to talk about with Miss Lynch."
            scene w2_7210 with dissolve
            ver "Haa... whaa... wha...? Oh..."
            ver "Great..."
            scene w2_7211 with dissolve
            "Both of us took a second to process her request."
            mct "(Guess she still wants me to keep going.)"
            scene w2_7212 with dissolve
            mc "Yes, Ma'am."
            scene w2_7213 with dissolve
            "Slipping behind the silent redhead, I once again got an eyeful of her beautifully buff butt."
            "A sight fat and juicy enough to make a man want to dive in."


    scene vero_e2_mcc_a with dissolve
    show vero_e2_mcc
    ver "Eeeuhh...!"
    kat "Now, where were we?"
    ver "Ha, whhh--"
    kat "Oh, that's right. You don't have anyone, do you? Heh...!"

    if kat_polite == True:
        "As Mrs. Pulman continued on, so did I, prying open her labia with my lips and tasting her increasingly familiar insides."
    else:
        "As Kathleen continued on, so did I, prying open her labia with my lips and tasting her increasingly familiar insides."

    kat "I believe you only speak to your parents during the holidays? Is that right?"
    "I was taking it slow, circling the outer edges of her lips and exploring the underside of Veronica's exposed clit."
    "I knew I was going to be down here for quite a while, after all..."
    scene w2_7214 with dissolve
    ver "Hwwh-how the hell do you know that...?"
    scene w2_7215 with dissolve
    kat "I've learned more about your life than I even cared to, quite frankly. Down to the last frivolous detail."
    scene w2_7216 with dissolve
    kat "Why, I've even called up your soft-spoken \"papa\". He seemed nice, if not loose-lipped and slow."
    scene w2_7217 with dissolve
    ver "You had no -- bah!"
    scene w2_7215 with dissolve
    kat "I had no right? Is that what you were going to say?"
    scene w2_7216 with dissolve
    kat "Even for a woman with no public persona like Mrs. Carter, it is {i}concerning{/i} how much information on a person you can legally dig up if you have the know-how, people skills, and reach."
    scene w2_7218 with dissolve
    kat "Now, for someone with a public face like yours... ha..."
    scene vero_e2_mcc_a with dissolve
    show vero_e2_mcc
    "Back here, dwarfed by Veronica's wide hips and extraordinarily shapely ass, I felt less a participant and more of a cog in the old woman's prattling."
    "There was an odd, almost serene comfort being obscured to the crowd and only needing to focus on eating the redheaded beauty out."
    "To that end, I would be diligent. Leaving no part of her, inside or out, untouched."
    scene w2_7219 with dissolve
    kat "I found it interesting that your father is an accomplished athlete in his own right, but you two never really meshed."
    kat "The workings of human relationships often have such an elaborate underpinning, don't they?"
    scene w2_7220 with dissolve
    ver "Mmhh...! Ah...! Don't... read into nothing... you crazy bitch..."
    scene w2_7221 with dissolve
    kat "Oh, I'm not drawing any conclusions myself, just broadly painting a picture of the whore in front of me for our wonderful guests."
    scene w2_7222 with dissolve
    "Grunts and belabored breaths were my only minor reward, my partner's attention otherwise occupied by the woman in front of her."
    "The only other proof that Veronica was feeling it was the amalgam of spittle and girl juices that coated Veronica's groin and dripped messily down my chin."
    scene w2_7223 with dissolve
    kat "You even went as far as winning a silver medal on the world stage. He must've been proud, but... I don't think you were, were you?"
    scene w2_7224 with dissolve
    ver "What are you talking about? Of course I was...!"
    scene vero_e2_mcc_a with dissolve
    show vero_e2_mcc
    kat "Really? That's not what I got from watching your interviews after the fact."
    "Every lick and lash opened her flower more."
    "Her inner walls would contract against my tongue, as if welcoming me further in."
    kat "Oh, sure you put on a sportsman-like face, but your body language made your feelings as clear as day."
    "So deeper I went with a gentle push, until the tightness of her muscles gave no quarter."
    ver "Hutt- e-everyone at that level wants to finish first, more than anything. It's normal... to be disappointed... ah!"
    scene w2_7224 with dissolve
    kat "I'm sure that is true for most, but for you... it was more than simple disappointment. It was personal, gut-wrenching disgust."
    kat "You failed there, just as you later did with your marriage."
    scene w2_7226 with dissolve
    ver "Fuck you!"
    "Despite her agitation, her hips had a mind of their own, gently swaying and pushing my nose deeper into her sex, entreating me to an intoxicating mixture of human arousal and soap."
    scene w2_7225 with dissolve
    kat "It's true, isn't it? You worked so hard - blood, sweat, and tears - and you came in second. {b}Second.{/b}"
    scene w2_7227 with dissolve
    kat "That's just a nice way of saying the first loser, isn't it?!"
    scene w2_7228 with dissolve
    ver "Tsk! You-- ah...! Sh-shit...! Aaah-!"
    scene vero_e2_mcc_a with dissolve
    show vero_e2_mcc
    "Every second she was pleasured prevented her from finding firm ground in their exchange. Every time I'd glide my tongue over her clit, she'd stumble over her words."
    "Veronica, before either of us realized it, was being worn down on both ends in both temperament and sex."

    if kat_polite == True:
        "On an even playing field, Mrs. Pulman's carefully chosen barbs wouldn't likely dredge up this degree of agitation in her, but this wasn't anywhere near an even playing field."
    else:
        "On an even playing field, Kathleen's carefully chosen barbs wouldn't likely dredge up this degree of agitation in her, but this wasn't anywhere near an even playing field."

    ver "Gh-- huuuh... damn it...!"
    "Veronica was shackled, nearly nude, and adorned in a set of goofy lingerie, her emotions on edge from being sexually stimulated publicly."
    "The old woman had crafted a scenario where Veronica should feel exposed and vulnerable enough for her cruel words to have maximum impact."
    scene w2_7229 with dissolve
    ver "Ha... life isn't that simple! Everyone wins and loses!"
    "The evil was not in the crudeness, but the simplicity of it."
    scene w2_7230 with dissolve
    kat "Sure, comfort yourself with that."
    scene w2_7231 with dissolve
    kat "You just couldn't cut it athletically or romantically, could you? As hard as you tried, you failed."
    scene w2_7232 with dissolve
    ver "Ng, ah...! I cherish my time in athletics, and even more, my time with Lily! You don't know shit!"
    scene w2_7233 with dissolve
    kat "So, you have no regrets then?"
    scene w2_7234 with dissolve
    ver "That... ah... who doesn't?!"
    scene w2_7233 with dissolve
    kat "...but you're not afraid of failing then?"
    scene w2_7234 with dissolve
    ver "No one likes failing!"
    scene w2_7235 with dissolve
    kat "They don't, that's true."
    scene w2_7236 with dissolve
    kat "To every soul here watching you debase yourself, that word is a foul drop of poison on the tongue. It's human to be afraid of failure, but you've taken it to the extreme, no?"
    scene w2_7235 with dissolve
    kat "Why else would you be here, doing all this to save your crummy business? You don't want to add another mark of failure to your life!"
    scene w2_7237 with dissolve
    ver "Ba-ah, whatever! No shit!"
    scene w2_7238 with dissolve
    ver "I poured a lot of money and time into it! It cost me my relationship! I'm not going to let the damn thing die!"
    ver "Even if I have to toss aside my pride and--"
    stop music fadeout 3.0
    scene w2_7239 with dissolve
    kat "Beautiful! Your resolve is beautiful!"
    kat "That's what I...!"
    play ambient "sound effects/kiss2.wav"
    scene vero_e2_katkiss_a with dissolve
    show vero_e2_katkiss
    ver "Gh--?!!"
    "To my utter disbelief, Kathleen stole a kiss from the bound woman."
    ver "Mmmh?! Mmhhh...!"
    "It was rough and violent, full of passion and fury - like she was trying to suffocate her with her tongue."
    "The blush on Mrs. Pulman's face betrayed her feeling of arousal."
    scene w2_7240 with dissolve
    hana "Holy..."
    scene w2_7241 with dissolve
    kil "...shit."
    scene w2_7242 with dissolve
    mct "(Fuck me...)"
    scene vero_e2_katkiss2_a with dissolve
    show vero_e2_katkiss2
    ver "Hmmm.... ha..."
    "Their kiss continued, unabated by the passage of time."
    "Seconds turned into a dozen. You could hear a pin-drop in the exhibition hall, as everyone eagerly watched Kathleen devour Veronica."
    kat "Mmmhh--!"
    stop ambient
    scene w2_7243 with dissolve
    kat "M~wah! You're a beautiful human being Miss Lynch."
    play music "music/from-russia-with-love.ogg"
    scene w2_7244 with dissolve
    kat "That miserable look on your face... oh, if only I could bottle it up."
    kat "I'd drink it {b}every{/b}, {i}single{/i} day."
    scene w2_7245 with dissolve
    ver "Haat... insane bitch..."
    scene w2_7246 with dissolve
    kat "Warren! You back?"
    scene w2_7247 with dissolve
    war "I am, ma'am."
    mct "(That's a...!)"
    scene w2_7248 with dissolve
    kat "You have our spider friend?"
    ver "Wha, ah... uh, spha-s-spider?"
    scene w2_7249 with dissolve
    war "I do, ma'am."
    scene w2_7250 with dissolve
    "The color drained from Veronica's reddened cheeks, telling me everything I needed to know about how she felt about arachnids."
    ver "What the hell do you mean spider--?!"
    scene w2_7251 with dissolve
    kat "Oh...? That reaction..."
    kat "When I asked about your fears, you didn't neglect to mention a phobia of spiders, did you...?"
    scene w2_7252 with dissolve
    "Veronica's legs faintly tremored, only perceivable thanks to the metallic clamor of her shackles."
    ver "No, it's just... ah... y-yo're pulling my leg, right?"
    kat "Why would I ever joke around with you, Miss Lynch? Don't tell me..."
    scene w2_7253 with dissolve
    kat "...for all your bravado and self-posturing, to think that you'd be afraid of something harmless like a {b}taruntula{/b} would be..."
    play sound "sound effects/surprise.wav"
    scene w2_7254 with vpunch
    kat "Look out!"
    ver "Ah-! Wha, sh...!"

    if kat_polite == True:
        "Mrs. Pulman's cruel fake out drummed up the reaction she was looking for."
    else:
        "Kathleen's cruel fake out drummed up the reaction she was looking for."

    scene w2_7255 with dissolve
    ver "G-gh--ghet it...! Awahaha...!"

    "Her chains and the stool groaned in distress, as Veronica tried to escape her bindings."

    kat "Haha, bwhaa...! Oh, my... fwwwhhpfh...!"
    ver "Gh, ghet it.. s-stop...!"
    scene w2_7256 with dissolve
    kat "Relax, dear! It was just my hand."
    ver "Ah, ha... *gulup* Oh..."
    scene w2_7257 with dissolve
    kat "Pretty comical to think a big gal like you would be aghast of something so small and harmless."
    ver "N-no one likes spiders!"
    scene w2_7258 with dissolve
    kat "Really...?"
    kat "Dear, dear, dear... \"no one likes failing\" and \"no one likes spiders\"..."
    scene w2_7259 with dissolve
    ver "Ah, wha-whatt...gggh...!"
    kat "You really got to stop thinking in absolutes. I don't seem too bothered, do I?"
    scene w2_7260 with dissolve
    ver "D-don't... d-don't..."
    kat "You... you really are petrified, aren't you?"
    kat "You know there's nothing to be afraid of, right dear? This little guy can't hurt you."
    scene w2_7261 with dissolve
    ver "Sh-she...shooo.. s-so..."
    kat "It's got less venom than a common bee!"
    "Veronica stumbled over her words."
    ver "Get it, p-ph, phullease..."
    "The cruel woman was being absurd. I didn't even have a dislike of spiders and I was getting the heebie jeebies from this distance."
    scene w2_7262 with dissolve
    kat "*sigh* We can't hold a conversation like this."
    ver "Ha, haa....! Oh... oh, no..."
    "The old woman mercifully withdrew the tarantula from Veronica's sight."
    scene w2_7263 with dissolve
    ver "No, no... that wasn't..."
    scene w2_7264 with dissolve
    ver "That wasn't fucking funny!"
    scene w2_7265 with dissolve
    "...and gave her a moment to compose herself."
    kat "I thought it was hilarious. Anyway, that reaction... your choice should be pretty easy then."
    scene w2_7264 with dissolve
    ver "What choice...?!"
    scene w2_7266 with dissolve
    kat "You have three. One..."
    kat "You can give up. Forfeit the night."
    scene w2_7267 with dissolve
    ver "Like hell I will! That, t-that isn't an option!"
    scene w2_7268 with dissolve
    kat "It IS an option! There's no beauty in humiliation that isn't willingly offered!"
    scene w2_7269 with dissolve
    ver "I'm not forfeitting! What are the other two?!"
    scene w2_7270 with dissolve
    "There was a dreadful look on Veronica's face, one stronger than her anger. Everyone knew what was coming."
    scene w2_7271 with dissolve
    kat "Well... option two..."
    scene w2_7272 with dissolve
    ver "W-waahhwa?!"
    kat "Five measly minutes of facing your phobia."
    scene w2_7273 with dissolve
    "The spider crawled up Veronica's back and the look of terror instantly returned to the Amazon's beautiful face."
    ver "Get-- get it...!"
    scene w2_7274 with dissolve
    mct "(How the hell is any of this supposed to be sexy?!)"
    ver "Buhh, th-wthweee? Three...?! What, t-three...!"
    scene w2_7275 with dissolve
    kat "Five minutes isn't a long time, honestly! I'll even start the clock right now. Option three..."
    ver "P-please! F-fuck me!"
    scene w2_7276 with dissolve
    kat "O-hoh! Quick on the uptake!"
    scene w2_7277 with dissolve
    "Veronica even in her frightened state, knew where this was going."
    scene w2_7278 with dissolve
    kat "Instead of walking away or just letting a silly little bug scuttle across your back--"
    scene w2_7279 with dissolve
    ver "F-fuck me, Mrs. Pulman! Please! I want you to fh-fuck me!"
    scene w2_7280 with dissolve
    kat "Really? You'd rather show everyone how small and weak you really are? You'll degrade yourself?"
    scene w2_7279 with dissolve
    ver "Y-yes! Fuck me! Hurry up!"
    scene w2_7280 with dissolve
    kat "I'm not convinced, dear."
    scene w2_7279 with dissolve
    ver "Please! I'm weak.. I'm... just... just... g-gh-give it to me!"
    ver "Stuff my pussy with your--"
    stop music fadeout 2.0
    scene w2_7281 with dissolve
    kat "Okay~♥"
    kat "You asked so nicely. I wouldn't want to be a poor host~"
    scene w2_7282 with dissolve
    "Kathleen Pulman, without question, was a truly evil woman."
    ver "Ha... ha... oh God, thank you..."
    scene w2_7283 with dissolve
    "...and tonight, I was her shadow. Complicit, just as everyone else in this room was."
    "Even Hana, who unwittingly wore a horrified expression, was condoning this exploitation with her silence."
    scene w2_7284 with dissolve
    kat "To think, I'd see you... a big tough woman... blubber like a baby."
    scene w2_7285 with dissolve
    ver "...hng... ha... fuck off."
    "It was an automatic response, with none of the typical fire in her voice."
    scene w2_7286 with dissolve
    kat "You've made me a happy woman tonight, Miss Lynch. As a reward, I'll make you feel good."
    play music "music/addict.ogg"
    scene w2_7287 with vpunch
    ver "Haa-!"

    if kat_polite == True:
        "With force, Mrs. Pulman brought her hips to bear, submerging the entire length of her giant fake cock into Veronica's accommodating fuckhole."
    else:
        "With force, Kathleen brought her hips to bear, submerging the entire length of her giant fake cock into Veronica's accommodating fuckhole."

    kat "Now, let everyone here see your debauched expression!"
    scene vero_e2_strapon1_a with dissolve
    show vero_e2_strapon1
    ver "Gh-!"
    "So began the marathon fuck session, with the old woman riding high off of Veronica's submission, a wild and lustful look in her eyes."
    kat "Let's show everyone the face of a woman who's chosen to be a good-for-nothing-else whore!"

    if kat_polite == True:
        "There was no need to start slow, I had made sure of that by playing my part. Mrs. Pulman pulled herself out and hilted her massive strapon back in again with relative ease."
    else:
        "There was no need to start slow, I had made sure of that by playing my part. Kathleen pulled herself out and hilted her massive strapon back in again with relative ease."

    scene w2_7288 with dissolve
    jim "Woah! Kathy's part of the show this time!"
    "I took it that it was unusual for her to get this directly involved in the action."
    scene w2_7289 with dissolve
    chuck "Yes, {b}indeed{/b}..."
    "The look in a few of their eyes told me why that was, exactly."
    scene vero_e2_strapon2_a with dissolve
    show vero_e2_strapon2
    ver "Ha, eehh...!"
    "Veronica was given no time to refocus herself. Her emotions, still riding high from coming face-to-face with her phobia, resulted in an unfiltered, shrill cry of pleasure being wretched from her throat."
    ver "Whoah, ah... ah... ng!"

    if kat_polite == True:
        "Her defenses had been shattered and all she could do was squirm and moan as Mrs. Pulman developed a discordant rhythm to fuck her to."
    else:
        "Her defenses had been shattered and all she could do was squirm and moan as Kathleen developed a discordant rhythm to fuck her to."

    ver "Heehh, s-shit... it's... b-big!"
    kat "It is! And you're taking it beautifully, slut!"
    "No kidding. The \"tool\" she was slogging around was three-fourths the length of her fore arm and she was slamming it home on every thrust."
    ver "Haa, nnggh....! You're ah, why... why...?"
    kat "Why does it feel so fucking good? I'll tell you, sweet pea~"
    scene w2_7290 with dissolve
    play sound "sound effects/slap3.wav"
    scene w2_7291 with vpunch
    "*Cra-ack!*"
    ver "Yeee...!"
    scene w2_7292 with dissolve
    kat "It's the adrenaline! Fear is a powerful aphrodisiac!"
    scene w2_7290 with dissolve
    play sound "sound effects/slap3.wav"
    scene w2_7291 with vpunch
    "*Smack!*"
    scene w2_7292 with dissolve
    kat "So... just {b}feel{/b}, slut. Let go and be free!"
    scene w2_7293 with dissolve
    ver "Heeh...?"
    scene w2_7292 with dissolve
    kat "... and move your fucking hips!"
    scene vero_e2_strapon1_a with dissolve
    show vero_e2_strapon1
    ver "Ohw-ah, f-fine! Jeez!"
    kat "Ha! How the hell does an ass this large barely shake?"
    "Without the benefit of sensory feedback, the old woman could only rut crudely, her unfeeling tool unable to grasp how Veronica's lower half was responding to her motions."
    ver "Ha, ngh...!"
    "Like a battering ram trying to burst through a gate, she just violently smashed herself again and again. However, despite the lack of nuance..."
    ver "Heeh, huttt...!"
    "It was, in a particular way, effective."
    kat "Drop the pretense! Throw away your pride, cunt!"
    scene vero_e2_strapon2_a with dissolve
    show vero_e2_strapon2
    "Adding to the chaos and playing the backing track to the chorus of groans and cursing, Veronica's support rest creaked from the shifting weight."
    kat "Forget yourself! Scream in pleasure!"
    ver "Gh...! Haaat...! Nhhh, anahh... I..."
    kat "Be honest! Beg for it!"
    scene w2_7290 with dissolve
    play sound "sound effects/slap3.wav"
    scene w2_7291 with vpunch
    "*Thwap!*"
    scene w2_7292 with dissolve
    kat "Let everyone hear you beg! Let everyone know you don't want me to stop!"
    "Kathleen's treatment distinctly mirrored what Veronica had done to her during the last \"game\" of her interview."
    scene w2_7293 with dissolve
    ver "Ah, nah... eugh, p-pl..."
    scene w2_7290 with dissolve
    play sound "sound effects/slap3.wav"
    scene w2_7291 with vpunch
    "*Smack!*"
    scene w2_7292 with dissolve
    kat "Say it loud enough for everyone to hear!"
    scene w2_7294 with dissolve

    if kat_polite == True:
        "Veronica, for all her obstinacy, was now enveloped in the depraved tapestry of Mrs. Pulman's weaving."
    else:
        "Veronica, for all her obstinacy, was now enveloped in the depraved tapestry of Kathleen's weaving."

    ver "Ihgghh, I..."
    scene w2_7294 with dissolve
    play sound "sound effects/slap3.wav"
    scene w2_7295 with vpunch
    ver "Guhh...! I, I..."
    kat "Say it clear--"
    scene vero_e2_strapon1_a with dissolve
    show vero_e2_strapon1
    ver "Fuck me! P-hhhwlease!"
    ver "F-fhu, fhuc, fhuckk.... meeee!"
    "She had, at least in this moment, given in - and I didn't believe it was just theatrics either."
    kat "Yeah?! You feel good?!"

    if kat_polite == True:
        "How quickly she unraveled was a marvel. Mrs. Pulman was scary."
    else:
        "How quickly she unraveled was a marvel. Kathleen was scary."

    ver "Eheh... gho- gh, good? Ah... I'm..."
    kat "You feel overwhelmed?!"
    "To heighten her senses using fear..."
    ver "Ha, nggh... ahhh, eyhh..."
    scene w2_7296 with vpunch
    with flash
    ver "Gwhhh...! Ahhhattta...!"
    kat "What's this? You just...? Pfft, really?!!!"
    ver "Guhh... haa...."
    scene w2_7297 with dissolve
    "Veronica's squirt splattered against the old woman's leather-clad tummy and trickled back down to the messy flurry of their ever-thrusting sexes."
    kat "Dumb slut! You just made a fucking mess of me! However, I'm just getting started!"
    scene vero_e2_strapon2_a with dissolve
    show vero_e2_strapon2
    ver "Ha, eehh...!"
    "Kathleen didn't stop. For an old woman, her stamina was impressive."
    aug "Don't break a hip, Kathy!"
    "As ridiculous as it sounded, the sheer intensity at which she was going at it made August's off-handed joke seem plausible..."
    kat "I actually owe you two more, Miss Lynch!"
    scene vero_e2_strapon1_a with dissolve
    show vero_e2_strapon1
    "So that was it. There wasn't any room left to doubt: this was payback."
    ver "Hhhhh...!"
    kat "Won't you cream yourself just two more times? For me?"
    kat "Like a shameless bitch? Pretty please?"
    ver "Hattnn... ayy, ah... t-two more th-thimes...?"
    "I did not envy the prospect of going back-to-back-to-back rounds with that monsterous rubber cock."
    ver "Ah, eugh... y-you vindictive...!"

    scene vero_e2_strapon3_a with dissolve
    show vero_e2_strapon3
    ver "Wh-.. what, ah...?!"

    if kat_polite == True:
        "With a bit of physical ingenuity, Mrs. Pulman lifted Veronica and every pound of dense muscle off the support stool. The physical discomfort of the position ensured the Amazon pulled her own weight, lightening the load as she continued pounding her cunt."
    else:
        "With a bit of physical ingenuity, Kathleen lifted Veronica and every pound of dense muscle off the support stool. The physical discomfort of the position ensured the Amazon pulled her own weight, lightening the load as she continued pounding her cunt."

    kat "There! Upsie-daisy~"

    ver "Hyyynnggg...!"
    "Stretched as her arms and shoulders were, Veronica bucked her hips in tandem with her partner's movements in search of relief."

    kat "Ha...! You're moving your hips so fast too! I'm glad you're being so honest~"
    sam "Oh my god...! This is...!"
    scene w2_7298 with dissolve
    eric "Christ, put your dick away!"
    scene w2_7299 with dissolve
    sam "What do you care? We just double-teamed the same whore an hour ago!"
    scene w2_7300 with dissolve
    eric "Shouldn't you be satiated then, you dumb animal?"
    scene w2_7301 with dissolve
    sam "Bahaha, nope! You fuckin' limp dick!"
    scene vero_e2_strapon4_a with dissolve
    show vero_e2_strapon4
    "The crowd came to life, surprised by the sudden physicality from the night's devious ringleader."

    if kat_polite == True:
        "The relatively frail Mrs. Pulman manhandling a woman twice her size was indeed an interesting sight."
    else:
        "The relatively frail Kathleen manhandling a woman twice her size was indeed an interesting sight."

    ver "I, you, this-thdhis--"
    kat "Look at that, Miss Lynch! Seems your fans are enjoying the show!"
    kat "Say thank you!"
    ver "Eh... ehh, ah... thhwww-- ehyyooou...!"
    kat "Try again, whore!"
    ver "Thank... thank, yhhouuu!"
    "Overwhelmed, Veronica still went along with Mrs. Pulman's requests."
    scene vero_e2_strapon3_a with dissolve
    show vero_e2_strapon3
    kat "Well, that was fucking pitiful. If you can't say it clearly, then you should do it with your body language."
    kat "Don't close your eyes now, okay? Get a good view of the gentlemen that will finance your future!"
    ver "Ehhyy, hee...!"
    kat "You're looking, right? You see it?"
    ver "Ha, sshut, shut up... and just..."
    kat "You see Samson stroking his fat cock?"
    ver "Yh, ngh.. yheehg...! Yesh!"
    kat "Lucky you! You're going to be a tough act to follow tonight!"
    ver "Eyhhehh, what... whatthever...yyuhhou...ah...!"
    kat "Heh, to think... every time you flick the lights off at night... {b}it's their faces you'll see in the dark{/b}!"
    "Even I wanted to tell the old woman to go fuck herself after that one."
    ver "Gah...! Y-yhou... bh-buu-bhu, eetch...! T-thalk, twwooo, mhucch...!"
    "...but it seemed that despite her blubbering, that one irritated her. The fire wasn't completely gone from the bodybuilder."
    ver "Gyeeeeh, ghhhe, haaat...!"
    "That, in a fucked-up way, was a relief to me - not that it mattered to anyone else."
    scene vero_e2_strapon4_a with dissolve
    show vero_e2_strapon4
    ver "Ha, haaat...!"
    "It was after all a lone lingering ember growing cold in the shadow of her successful humiliation."
    sam "Gaahhahaha, give it to her! Yeah!"
    "Her \"sponsor's\" lone voice carried over the clamor, but everyone was laughing and having a good time at this point."
    ver "Tskhh... ha, ha...!"
    "No one looked or sounded human to me right now."
    mct "(Ha... this is...)"
    ver "Haahtt, essh... it feels gooood! It doeshssh!"
    "Our star performers, for all their physical beauty, looked like animals."
    mct "(This is madness.)"
    kat "Bah, ah... lovely!!"
    "They were sweating profusely under the stage's heat lamp, and every thrust was nearly palpable from the sticky sight of skin being pried off skin."
    ver "Gheeh... gha....!"
    kat "Your sounds are becoming even more rich, dear!"
    ver "It fheels-- sh, ghh..."
    kat "So you've already said!"

    if kat_polite == True:
        "For another minute, Mrs. Pulman pounded away in an impressive display of stamina. And my job was to just stand here, watching the sweat drip down an old woman's asscrack."
    else:
        "For another minute, Kathleen pounded away in an impressive display of stamina. And my job was to just stand here, watching the sweat drip down an old woman's asscrack."

    "......"
    "..."
    ver "Oh, no... twhhtwho....!"
    kat "Oh-hoho, feel free~! Feel free to make another mess~♥ Chawaha!"
    "I'd never seen the old woman this ecstatic, did she just...?"
    scene w2_7302 with dissolve
    ver "Ghheeeee...!!"
    mct "(...did she really just fucking cackle?)"
    scene w2_7303 with vpunch
    "For the second time, Veronica squirted."
    ver "Haaa, hannngh...!"
    "Her hoarse cries stifled in her throat by her very own pleasure."
    scene vero_e2_strapon5_a with dissolve
    show vero_e2_strapon5
    ver "Ha... ha...!"
    kat "Ah, that's number two..."
    "Kathleen never stopped her rut."
    ver "Gyeeh..."
    "Veronica was undoubtedly sensitive right now, thoughts fast replaced with animal urge."
    kat "Uh, uh, uh... no rest. We got one more!"
    scene w2_7304 with dissolve
    hana "...this is--"
    scene w2_7305 with dissolve
    eric "Damn, what the...! You got it all over me you caveman!"
    sam "Bahaa, cool it! Dalia will get you a towel!"
    scene w2_7306 with dissolve
    kat "Now, let's give everyone a good view of those preposterous tits of yours flopping around!"
    kat "Mr. [mcl]...?"
    "......"
    "..."
    scene w2_7307 with dissolve
    kat "[mcf]! Snap out of it!"
    mc "O, oh-oh...?"
    scene w2_7308 with dissolve
    "My name sounded alien to me, I had forgotten I was even here..."
    scene w2_7309 with dissolve
    mc "Yes, Ma'am?"
    scene w2_7308 with dissolve
    kat "Would you give me a hand with her top? My hands are full."
    scene black with fade
    "Instead of answering, I just did it."
    scene vero_e2_strapon6_a with dissolve
    show vero_e2_strapon6
    ver "Ha, hhaaa....!"
    "The moment I came face-to-face with the red-headed beauty, my heart skipped a beat. Veronica looked up at me with a mystifying expression."
    "It was a tangled, homogeneous mixture of bliss and misery. Part of me wanted to reach out in an impotent gesture of reassurance, the other..."
    ver "Ha, hnnng...! Huutt...! [mcf]...?"
    "...just didn't want to look away."
    scene black with fade
    "But I did, opening up and pulling back the flap of her lingerie."
    kat "Now, straighten up!"
    scene vero_e2_strapon7_a with dissolve
    show vero_e2_strapon7
    ver "Gh...ahh..."
    "So it continued, Veronica now on her feet."
    ver "Ghh..asshhh..."
    "Starry-eyed and slack jawed, by now all sense had been scraped out of her by the dauntingly huge dildo."
    "Minute after minute passed like this, and although worn down mentally from the pleasure, Veronica physically kept up with the old woman's tenacious pace."
    "*Fwap, thwap, sthhwwap...!*"
    "Kat would push forward, and the steel-bound Amazon still had the wherewithal to push back equally as hard, the impact of which carried clear across the hall."
    kat "Haaa, n-nghh...! C'mon...!"
    "Whether it was instinct or a conscientious attempt to meet the vague, nebulous criteria on which she would ultimately be judged, Veronica refused to be a passive participant."

    if kat_polite == True:
        "Mrs. Pulman was finally showing her age too, her snide remarks coming out less frequently and in a more measured tone to mask her labored breathing. "
    else:
        "Kathleen was finally showing her age too, her snide remarks coming out less frequently and in a more measured tone to mask her labored breathing."

    kat "Hhh, hhoo... ah, c'mooon...!"
    "*Thwahp, chwup, fwap, tchhup...!*"
    "The old woman was gripping Veronica's elbows so tightly that her own hands were ghost white, lest the Amazon get dropped on her chest."
    kat "One... ah, more...!"
    "*Thwahp... hwhupp... thwhap...!*"
    "Her small, pencil-like arms were clearly strained even with Veronica carrying most of her weight."
    "Her face, however, never lost its smugness."
    kat "Just...!"
    scene vero_e2_strapon8_a with dissolve
    show vero_e2_strapon8
    ver "Ah, haaat...!"
    "She pistoned her hips faster still. For an old lady..."
    "*Twap, smack, thwack...!*"
    "It was impressive."
    scene vero_e2_strapon9_a with dissolve
    show vero_e2_strapon9
    "Very impressive."
    "*Thwahp, chwup, fwap, tchhup...!*"
    "Her last orgasm didn't come as quickly. She was making the old woman work for it."
    "*Fwap, thwap, sthhwwap...!*"
    ver "Ha, haaaa, haaaa....hhhggg...!"
    "I was getting tired just watching, even before the minutes disappeared once again."
    "Minute."
    ver "Ghh...!"
    "After Minute."
    kat "H-hhaaa, haaat..!"
    "...after minute after minute."
    ver "Ghhh....!"
    "*Thwahp... hwhupp... thwhap...!*"
    "Five minutes passed and both women looked to be at the wick's end."
    scene w2_7310 with dissolve
    "Kathleen's own juices dripped steadily down her leg, thickened by Veronica's own gush that had splattered her and floor beneath them."
    "*Thwahp, chwup, fwap, tchhup...!*"
    scene vero_e2_strapon8_a with dissolve
    show vero_e2_strapon8
    kat "Ha, haa....! Your... legs are... trembling, dear. Ha...!"
    "*Twap, smack, thwack...!*"
    kat "Is it... or..."
    ver "Ghhwaaah... gwwwahhh... gwaahhh... haa, ghhhuut...!"
    "Veronica's body shook violently with pleasure. Brutal, mind-melting pleasure."
    "Six minutes in, under the spell of a full-body orgasm..."
    scene w2_7311 with vpunch

    if kat_polite == True:
        "Mrs. Pulman had gotten her number three."
    else:
        "Kathleen had gotten her number three."

    ver "Haa... howgghh.. ssh-shooo much...!"
    "It was like the dam broke."
    ver "Hat, shhhho, ssshhhiaaa.. shhhwo.."
    scene vero_e2_strapon10_a with dissolve
    show vero_e2_strapon10
    kat "Bahaa... ha....! You're like a fucking fire hydrant... bahaha, ha...!"
    ver "G-guh..."
    kat "You whore! Did it... feel that good getting... {b}FUCKED{/b} for everyone to see...?!"
    kat "I..."
    kat "I... I..."
    kat "I... I... aaaaah...!"
    scene w2_7312 with dissolve

    if kat_polite == True:
        "Mrs. Pulman wasn't far behind her, and with her body wracked with pleasure, she lurched forward and..."
    else:
        "Kathleen wasn't far behind her, and with her body wracked with pleasure, she lurched forward and..."

    "To my astonishment, she had actually worked herself into her own orgasm."
    stop music
    scene w2_7313 with vpunch
    ver "Ghh...!"
    "Like a beast, she sunk her teeth into Veronica's back and claimed the redhead as her property."
    kat "Grr... ghh....!"
    ver "Ayhh--"
    scene w2_7314 with dissolve
    ver "Ahh...?!"
    kat "Ha..."
    scene w2_7315 with dissolve
    kat "Heheh... ha..."
    scene w2_7316 with dissolve
    kat "Ha... looks... ha... looks like you actually owe me one more, Miss Lynch."
    kat "{b}Let's take it to the floor{/b}."
    show screen textbox2 with dissolve
    scene black with fade
    if not persistent.veroW2Shame:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.veroW2Shame = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    "......"
    "..."
    $ renpy.end_replay()
    play music "music/jazz-piano-bar.ogg"
    scene w2_7317 with blinds
    "The short trek to the wash room was made in complete silence, save for a few grunts and sighs."
    "She didn't even protest when I offered her my shoulder for support. Veronica was exhausted, both physically and mentally."
    scene w2_7318 with dissolve
    ver "*Sigh* ...what are we doing here, [mcf]...? How did... how did I get here?"
    scene w2_7319 with dissolve
    mc "You..."
    mct "(...just followed along without realizing it?)"
    mc "You didn't hear Mrs. Pulman?"
    scene w2_7320 with dissolve
    ver "I was..."
    scene w2_7321 with pixellate
    ver "...I guess I was tuning her annoying yapping out or... or... {i}something{/i}."
    mc "Ah, well..."
    scene w2_7319 with pixellate
    mc "She called a fifteen minute intermission, for the both of you to get cleaned up and {i}changed{/i}."
    scene w2_7320 with dissolve
    ver "Oh..."
    scene w2_7322 with dissolve
    ver "Okay."
    "She sounded listless and deflated, but pulled away as requested to wash off the dried up sex juices and sweat from her body."
    scene black with fade
    "*Sqeeeek!*"
    scene w2_7323 with fade
    play ambient "sound effects/shower.wav"
    mc "Ah..."
    mct "(Why am I just standing and staring? She's got it covered...)"
    scene w2_7324 with dissolve
    "So I sat down. The mood in the room making me uncomfortable and nervous."
    mct "(Should I say something...?)"
    "Wasn't it my job to say something? To keep her spirits up, determined and cleanly on the hook?"
    scene w2_7325 with dissolve
    "That would be a dumbass, horseshit move. {b}She's clearly determined{/b}."
    "Nothing my clueless ass or even the most sagely councilor could say would erase the stain of humiliation or assuage the suffocating reality that she's staking her dignity on a gamble."
    "What she's feeling right now is just the baggage that comes with this."
    scene w2_7326 with dissolve
    mc "....."
    mc "..."
    scene w2_7327 with dissolve
    "Why, then, do I want to do something to make her feel better?"
    "It won't help."
    scene w2_7326 with dissolve
    "Yet, I thought about it."
    "I thought about it and I thought about it. What could I do?"
    stop ambient fadeout 2.0
    scene w2_7328 with dissolve
    "The silence in the room wouldn't let me think about anything else."
    mct "(No, it won't help...)"
    scene w2_7329 with dissolve
    ver "I'm... done. What now?"
    scene w2_7330 with dissolve
    "It won't help {b}in the least{/b}."
    hide screen textbox2 with dissolve

    menu w2VeronicaComfort:
        "{color=#FF1493}[[Affection]{/color} Try to comfort her(if veronica affection>=22)."(chg=["veronica_up3"]) if Veronica_Affection >= 22:
            $ veronicaFriend = True
            $ Veronica_Affection +=3
            show screen textbox2 with dissolve
            "If I'm lucky, maybe it will piss her off. An annoyed Veronica, to me, seemed preferable to a melancholic one."
            scene w2_7331 with dissolve
            mc "I..."
            scene w2_7332 with dissolve
            "Maybe this was selfish of me and I was just trying to get away from how her feelings are making me feel, but..."
            scene w2_7333 with fade
            "I started from the top, determined to work my way down."
            "She didn't stop me or proclaim she could do it herself, she just stood vacantly on stand-by, like an unattended computer."
            "I worked my way down to her shoulders."
            scene w2_7334 with dissolve
            "Then her breasts, playing it as cooly as I could muster."
            "I worked my way all the way down to the drops of water pooling in the divots of her abs."
            scene w2_7335 with dissolve
            "All-in-all, I scrubbed her down, ignoring the painful intimacy of the act and the growing sexual urge that I dearly wished wasn't there."
            scene w2_7336 with dissolve
            ver "I..."
            ver "I don't think you need to get in between my toes..."
            scene w2_7337 with dissolve
            "I boneheadedly ignored her."
            scene w2_7338 with dissolve
            ver "......"
            scene w2_7339 with dissolve
            ver "..."
            scene w2_7340 with dissolve
            "This..."

            if kat_polite == True:
                "Per Mrs. Pulman's instructions, would be coming off soon, but I wanted to grant Veronica at least a temporary veneer of modesty."
            else:
                "Per Kathleen's instructions, would be coming off soon, but I wanted to grant Veronica at least a temporary veneer of modesty."

            scene w2_7341 with dissolve
            "Something was missing..."
            mct "(Ah!)"
            stop music fadeout 3.0
            "One more thing to put her back together."
            scene w2_7342 with dissolve
            mct "(There.)"
            "Right as rain."
            scene w2_7343 with dissolve
            mc "I, um... *ahem*"
            "Now that she was a little less exposed..."
            play music "music/ill-remember-you.ogg"
            scene w2_7344 with vpunch
            "It was naïve."
            "It was naïve as all fuck, but this was what I had to offer."
            scene w2_7345 with dissolve
            "I worked for the woman who was exploiting her. I stood on stage, as her assistant, profiting off Veronica's own financial troubles."
            mc "I..."
            "I was not her friend. She would be insane to believe me, but..."
            scene w2_7346 with dissolve
            mc "Can I be your friend, Veronica?"
            "She didn't respond, verbally or physically. {i}That logically followed{/i}."
            "I was making an ass out of myself. In a way I was selfishly asking her to process the evening according to my wishes."
            scene w2_7347 with dissolve
            "......"
            "..."
            mct "(I should let go now--)"
            scene vero_e2_hug_a with dissolve
            show vero_e2_hug
            "She squeezed, like she was trying to pop me."
            "She didn't say anything though. She just rested her chin on my shoulder and ran her fingers up my back."
            "Her body was firm and her flesh ungiving, but she felt incredibly soft right now. Soft and exposed."
            ver "[mcf], I..."
            "I knew not to open my fucking mouth right now."
            "I was not her friend, though I really wanted to be. She was insane to believe me, but she was worn down enough to pretend."
            ver "[mcf], I feel like I'm nothing... I feel inhuman."
            "Opening my mouth without thinking right now would just shatter that illusion. Instead I just held on."
            "I pulled her tighter, as tight as the bone and muscles in my arms would permit."
            mc "Don't let that old bitch or the members here trick you into thinking you're like them. You're not."
            mc "They're the ones who are inhuman."
            scene w2_7348 with dissolve
            ver "Tsk...! F-fuckers...!"
            ver "She's right though..."
            scene w2_7350 with dissolve
            mc "No she isn't. Not in the least."
            scene w2_7349 with dissolve
            "I think I was finally grasping how important that place was to her."
            scene w2_7348 with dissolve
            ver "What does it say about me, that I walked in here on my own two feet?"
            scene w2_7349 with dissolve
            "She lost her marriage to it and she didn't even have a home. She quite literally lived out of that gym."
            scene w2_7350 with dissolve
            mc "It says..."
            scene w2_7351 with pixellate
            mc "Am I going to have to go to a different school?"
            scene w2_7352 with dissolve
            vic "Why would you think that, hun?"
            scene w2_7351 with dissolve
            mc "When Jeremy's dad died, he had to leave school."
            scene w2_7352 with dissolve
            vic "That's because he moved to a different house."
            scene w2_7351 with dissolve
            mc "Are we going to have to move to a different house?"
            scene w2_7353 with dissolve
            vic "No! Of... of course not!"
            scene w2_7354 with dissolve
            mc "Really?"
            scene w2_7355 with dissolve
            vic "I couldn't dream of giving up this place. This is {b}our{/b} home."
            scene w2_7356 with dissolve
            vic "You were born here. Your father, you, and I spent 8 wonderful Christmases here. No way in hell am I...!"
            scene w2_7357 with dissolve
            vic "...ah. Don't worry your head, my little angel. We're not moving to a different house."
            scene w2_7358 with pixellate
            mc "It says you're willing to fight for what's important to you."
            scene w2_7359 with dissolve
            ver "..."
            scene w2_7358 with dissolve

            if kat_polite == True:
                mc "Seriously. Please, please, {b}please{/b} don't buy into a single thing Mrs. Pulman accuses you of. She doesn't know how important four walls can be to a person."
            else:
                mc "Seriously. Please, please, {b}please{/b} don't buy into a single thing Kathleen accuses you of. She doesn't know how important four walls can be to a person."

            scene w2_7359 with dissolve
            ver "It's..."
            scene w2_7360 with dissolve
            ver "It's... It's all I fuckin' have, [mcf]! I got nothing else!"
            ver "It's all...!"
            scene black with fade
            play sound "sound effects/notification.wav"
            $ Veronica_Relations = "Friends"
            show relationvero with dissolve
            "A faint, warm dampness spread across the yoke of my shirt."
            hide relationvero with dissolve
            "The time for talking was over."
            stop music fadeout 3.0
            $ unread_veronica = True
            $ history_veronica = "I hugged a dejected Veronica. It was all I could do."
            play sound "sound effects/notification.wav"
            show bioupdate with dissolve
            "......"
            hide bioupdate with dissolve
            "..."
            jump w2ExFeliciaHumiliationPre
        "Just sit here, she doesn't need an awkward gesture of pity.":




            scene w2_7331 with dissolve
            show screen textbox2 with dissolve
            mc "Dry off."
            scene w2_7361 with dissolve
            ver "Should I change back into my costume?"
            mc "Ah, yeah... no. Mrs. Pulman, well..."
            "Having stripped her of her bravado, she was now going to strip her of her clothes."
            scene w2_7362 with dissolve
            mc "She wants you naked."
            ver "I see... I guess I kinda prefer that."
            scene w2_7363 with dissolve
            mc "Sit down. We've got some time before we have to be back."
            mc "Try to collect yourself. I know that was rough."
            scene w2_7364 with dissolve
            ver "Yeah, rough... heh."
            scene w2_7365 with dissolve
            "She looked lost and I reminded myself nothing I could say or do would help that."
            scene black with fade
            "She needed her own time to process things - and she would have it, watching the other two Carnations take their turns."
            stop music fadeout 3.0
            $ unread_veronica = True
            $ history_veronica = "Dejected from her humiliation round, I decided that any simple-minded gesture of friendship would be meaningless."
            play sound "sound effects/notification.wav"
            show bioupdate with dissolve
            "......"
            hide bioupdate with dissolve
            "...."
            jump w2ExFeliciaHumiliationPre

        "{color=#696969}[[Affection] Try to comfort her.{/color}" if Veronica_Affection <= 21:
            jump w2VeronicaComfort




label w2ExFeliciaHumiliationPre:

    play music "music/that-one-bar-scene.ogg"
    scene w2_7366 with circlewipe
    if veronicaFriend == True:
        "After our little moment, Veronica and I headed back to the exhibition hall."
        "The redhead followed behind me, sans clothing, as per the old woman's instructions."
    else:
        "After letting Veronica compose herself, we headed back to the exhibition hall."
        "The redhead followed behind me, sans clothes."

    hana "Hey!"
    kil "[mcf]!"
    scene w2_7367 with dissolve
    mc "What are you doing back here?"
    scene w2_7368 with dissolve
    hana "I was getting sick of people staring at the back of my head. Plus, they were starting to talk to me..."
    scene w2_7369 with dissolve
    kil "You're gonna have to get freakin' used to that now that you have more skin in the game, y'know? I mean, I don't like being all buddy-buddy with some of those..."
    scene w2_7370 with dissolve
    "Ian gave a quick, cautious glance around the room."
    scene w2_7369 with dissolve
    kil "...some of those {i}freaks{/i} either, but you can't pick-and-choose."
    scene w2_7371 with dissolve
    ver "...looks like Blondie is already set up."
    scene w2_7372 with cmet
    "She was right. Felicia was on stage, vulva-planted on the rather harsh ridge of a metal horse. It went without saying, it didn't look very comfortable."
    scene w2_7373 with dissolve
    "Gravity pushed down on the blonde's body weight, prying apart her cunt and firmly wedging the upper leather strip inside her."
    kil "Happy to know she isn't getting off easy? Jeez, I couldn't believe she brought out a goddamn spider!"
    scene w2_7374 with dissolve
    kil "Ugh, euch...!"
    scene w2_7375 with dissolve
    hana "Ah... that was... awful..."
    "Veronica didn't acknowledge my ginger friend's words, instead her eyes remained transfixed on the stage."
    scene w2_7376 with dissolve
    hana "How the hell am I supposed to judge something like {b}that{/b}?"
    scene w2_7377 with dissolve
    kil "Don't think too hard about it, you'll drive yourself crazy."
    hana "That wouldn't be fair to these poor..."
    scene w2_7378 with dissolve
    "She trailed off, still conscientious of Veronica's presence, even if she had somewhat wandered off."
    scene w2_7379 with dissolve
    kil "And what bit of this is fair?"
    scene w2_7380 with dissolve
    hana "It makes you think though... if I wasn't \"lucky\" enough to be right here..."
    hana "...would I be able to endure something like this if that was the only way I could support my mom?"
    scene w2_7381 with dissolve
    kil "No way! You're...!"
    scene w2_7382 with dissolve
    kil "You're... you're... too cool for that?"
    scene w2_7383 with dissolve
    hana "Ian..."
    scene w2_7384 with dissolve
    mc "There's... more ignoble things in the world than getting fucked in the ass to provide for your family."
    scene w2_7385 with dissolve
    kil "Speaking from experience, asshole?"
    scene w2_7386 with dissolve
    mc "..."
    kil "Why are you looking at me so--"
    scene w2_7387 with dissolve
    kat "Good, Mr. [mcl], you're back!"
    scene w2_7388 with dissolve
    fel "G..gah... don't push me... I'm trying to not move...!"
    kat "I had things get set up in advance, since this is going to be... {i}a long one{/i}."
    scene w2_7389 with dissolve
    fel "W-wahhh...!"
    kat "Put Miss Lynch back in the cage and we'll begin working on slut number two."
    kat "Oh, and... join us on stage, Mr. Beaufort. Everyone else, please return to your seats."
    scene w2_7390 with dissolve
    mc "Guess it's showtime again."
    hana "Break a leg..."
    scene black with fade
    stop music fadeout 3.0
    "......"
    "..."
    play sound "sound effects/metal-crash.mp3"
    "*Cl-chwiiick!*"
    scene w2_7391 with wipeleft
    "Without much fanfare, I led Veronica back to the cage and locked it."
    scene w2_7392 with dissolve
    mc "Sit tight."
    scene w2_7393 with dissolve
    ver "Very funny..."
    scene w2_7394 with dissolve
    kil "Hey, your hard part is over with. All you got to do now is sit on your ass and anxiously await the results."
    scene w2_7395 with dissolve
    ver "Even more funny..."
    scene w2_7396 with dissolve
    mc "How are you holding up, Rose?"
    scene w2_7397 with dissolve
    rose "Uh... heh... my legs are asleep."
    scene w2_7396 with dissolve
    mc "Hang in there."
    scene w2_7398 with dissolve
    rose "Yeah, it'll be my turn soon..."
    play music "music/from-russia-with-love.ogg"
    scene w2_7399 with dissolve
    kat "Before we begin, let me give you boys the run down of the next leg."
    scene w2_7400 with dissolve
    kil "It requires an explanation?"
    "With how the first game went, I had hoped that I was taking a more backseat role tonight..."
    scene w2_7401 with dissolve
    kat "Yes, indeed. Last week, I'd promised Mr. [mcl] I'd let him stretch his wings some if he didn't disappoint me, so I'm going to let you take a more {i}driving{/i} role this round."
    scene w2_7402 with dissolve
    mc "Please, explain."
    scene w2_7401 with dissolve
    kat "I'll guide the event, but I'll be off to the side. It'll be your job to reiterate my questions and help me get the answers I want out of Mrs. Ford."
    scene w2_7403 with dissolve
    kat "That's vague I know, but things will click into place once we get started."
    scene w2_7404 with dissolve
    kil "What about me? Why am I up here?"
    scene w2_7403 with dissolve
    kat "I understand you and Mrs. Ford are socially acquainted. I'm hoping having you nearby will throw her off her game."
    scene w2_7405 with dissolve
    kil "So you just want me to stand there?"
    scene w2_7401 with dissolve
    kat "More or less, the more being... well, it's [mcf]'s call. If he asks for a helping hand, please provide one."
    scene w2_7404 with dissolve
    kil "Gotcha. Second fiddle."
    scene w2_7406 with dissolve
    kat "Aw, now. Don't be so glum."
    kat "I'm just giving your good friend a chance to flourish. His performance reflects warmly on you! Now!"


label w2ExFeliciaHumiliation:

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
        "Did [mcf] degrade Felicia during the interview with Felicia's husband??"
        hide screen textbox2 with dissolve
        menu:
            "Yes.":
                $ w2FeliciaDegrade = True
            "No.":
                pass
        play music "music/from-russia-with-love.ogg"
        show screen textbox2 with dissolve


    scene black with fade
    kat "Let's have some fun."
    scene w2_7407 with fade
    kat "You ready to begin, Mrs. Ford?"
    scene w2_7408 with dissolve
    fel "Oh... ah... oh, yeah. Let's get this show on the road, boss."
    scene w2_7409 with dissolve
    fel "I can see how this is already going to play out..."
    scene w2_7410 with dissolve
    kat "First time on one of these before?"
    scene w2_7409 with dissolve
    fel "You can tell?"
    scene w2_7410 with dissolve
    kat "Oh, you're in for a novel experience. You'll find, as time goes on, that what you're currently feeling will grow... {i}exponentially{/i}. "
    scene w2_7411 with dissolve
    fel "A-ah...!"
    "A gentle nudge sent the blond uncomfortably squirming."
    scene w2_7412 with dissolve
    kat "How about you gentlemen? You ready?"
    scene w2_7413 with dissolve

    if kat_polite == True:
        "The crowd unanimously cried for Mrs. Pulman to move on."
    else:
        "The crowd unanimously cried for Kathleen to move on."

    scene w2_7414 with dissolve
    kat "Ah, ha...!"
    scene w2_7415 with dissolve
    kat "Mrs. Ford fashions herself an exhibitionist. She's a dirty woman who derives pleasure from having her naked body looked upon."
    kat "{b}She desires to be seen.{/b} Even right now..."
    scene w2_7416 with dissolve
    kat "This bitch is already dripping. It's a beautiful disposition, if I may say so myself."
    kat "Yet! For someone who likes to expose themselves, very few people have seen the real you."
    scene w2_7417 with dissolve
    kat " Very few people know anything about you, do they?"
    scene w2_7418 with dissolve
    fel "*Sigh* Who gives a shit about that boring crap? None of you care about my feelings, you just want to watch me get destroyed."
    scene w2_7419 with dissolve
    kat "Au contraire, Mrs. Ford! I think you'll find the men here care about that more than anyone else in your life."
    scene w2_7420 with dissolve
    kat "Any whore can remove their clothes and get fucked, but the devil is in the details."
    kat "For me, those pretty personal details are perhaps the only way I can embarrass a whore like you."
    scene w2_7421 with dissolve
    kat "That's why I'm calling your part tonight a display of {b}true exhibitionism{/b}. I'm going to put you under the microscope, dear."
    scene w2_7422 with dissolve
    fel "You guys have a weird definition of hot."
    scene w2_7423 with dissolve
    mct "(I guess I'm supposed to use these on Felicia?)"
    mct "(Lotta interesting things here...)"
    scene w2_7424 with dissolve
    "Things that will make her jerk and move, and dig the edge of the horse deeper into her vulva."
    kat "All you have to do tonight is answer my questions sufficiently and we'll jump to the part you find fun, Mrs. Ford."
    scene w2_7425 with dissolve
    fel "Hurry up and ask. I'm starting to {i}itch{/i}..."
    scene w2_7426 with dissolve
    kat "You were born in Wheatley, correct?"
    scene w2_7427 with dissolve
    fel "I was. That's no secret."
    scene w2_7426 with dissolve
    kat "No, it's not. From what I gathered, it's one of the few personal pieces of information you readily volunteer about yourself."
    scene w2_7428 with dissolve
    kat "You take {b}pride{/b} in leaving your kin behind?"
    scene w2_7429 with dissolve
    fel "I'm proud of getting where I am. That's all."
    scene w2_7430 with dissolve
    kat "True as that may be, you did leave your family behind. Do you miss them?"
    scene w2_7429 with dissolve
    fel "...no."
    scene w2_7430 with dissolve
    kat "No? Afraid their poorness will drag you down?"
    scene w2_7431 with dissolve
    fel "This is dumb. I didn't sign up to be interrogated."
    scene w2_7426 with dissolve
    kat "Would you like to stop?"
    scene w2_7427 with dissolve
    fel "Absolutely not."
    scene w2_7432 with dissolve
    kat "I didn't think so. Just keep swimming upstream until the bitter end, Mrs. Ford."
    scene w2_7433 with dissolve
    fel "..."
    scene w2_7426 with dissolve
    kat "So, in your own words then, tell me about your parents."
    scene w2_7427 with dissolve
    fel "I may not want to stop, but I also..."
    scene w2_7429 with dissolve
    fel "Wouldn't you rather use that crap on the table over there? Isn't that what you're into?"
    scene w2_7434 with dissolve
    kat "...we'll come back to this in ten minutes. Give my question some thought in the meantime, please."
    fel "Ten minutes...?!"
    scene w2_7435 with dissolve
    kat "Let her stew for that time and then pick up where I left off."
    scene w2_7436 with dissolve
    kat "Ask her about her family and make her... squirm."

    if feliciaFlag == True:
        "Suddenly, all the things I had learned about her, things that she had shared due to our worlds being separate, became a weapon to use against her."

    scene w2_7437 with dissolve
    mc "..."
    scene w2_7438 with dissolve
    kat "Feel free to talk amongst yourselves while you watch Mrs. Ford perform."
    scene w2_7439 with dissolve
    kil "I don't think that's going to be the only break."
    stop music fadeout 3.0
    scene w2_7440 with dissolve
    kil "We should have chairs."
    scene w2_7441 with dissolve
    mc "Has she done this one before?"
    scene w2_7442 with dissolve
    kil "No, but she did say it'd be a long one, so..."
    scene fel_e2_squirm1_a with dissolve
    show fel_e2_squirm1
    "That's right..."
    "The longer this went on, the more uncomfortable her perch would become."

    if kat_polite == True:
        "Which, in turn, means the more open she'll be to answering Mrs. Pulman's questions."
    else:
        "Which, in turn, means the more open she'll be to answering Kathleen's questions."

    scene w2_7443 with dissolve
    kil "So... how's it hanging, Felicia?"
    scene w2_7444 with dissolve
    fel "Just swell, Ian! You dumb prick!"
    scene w2_7445 with dissolve
    kil "Dumb...?!"
    if killianHeadsUp == True:
        mc "She knows about the sex tape, remember?"
        scene w2_7446 with dissolve
        kil "Riiiight..."
        kil "You'd think that cheating slut would cut me some slack."
    else:
        mct "(She knows about the sex tape, numbnuts...)"
        scene w2_7446 with dissolve
        kil "Pretty fuckin' rude..."
    scene w2_7446 with dissolve

    scene w2_7447 with dissolve
    mc "She just likes Mina better than you."
    play music "music/devious-little-smile.ogg"
    scene fel_e2_squirm1_a with dissolve
    show fel_e2_squirm1
    "So Felicia stewed for ten minutes, atop her artificial steed."
    "It was a long ten minutes for a rubber edge to be biting into your sex."
    "I didn't try and say anything to her in that time. We had a friendly rapport and that wouldn't really help in my role as an interrogator."
    "So, I just watched her squirm at decreasing intervals."
    "Squirm and squirm and squirm and..."
    "...watch a thin line of feminine ooze creep down the metal body of her seat."
    "Despite the discomfort of the setup, her exhibitionist spirit remained high."
    kat "Oh, my! It's been twelve minutes!"
    scene w2_7448 with dissolve
    kat "I guess I lost track of the time."
    kat "[mcf]...?"
    scene w2_7449 with dissolve
    "She looked at me expectantly. It was time, as Hana said, to break a leg."
    mct "(Uh... what specifically did the old woman ask her again...?)"
    scene w2_7450 with dissolve

    if kat_polite == True:
        "There was no way in hell I could manage the same level of gusto as Mrs. Pulman and meet these perverts' expectations, but I had to at least make a cursory attempt."
    else:
        "There was no way in hell I could manage the same level of gusto as Kathleen and meet these perverts' expectations, but I had to at least make a cursory attempt."

    scene w2_7451 with dissolve
    mc "What are your mother and father like, Felicia?"
    scene w2_7452 with dissolve
    "--whatever, just focus on her. Pretend this is a private conversation and things might just go smooth."
    fel "..."
    scene w2_7453 with dissolve
    mc "You don't want to say?"
    fel "Ngg...!"
    scene w2_7454 with dissolve
    "She jerked uncomfortably from the touch."
    scene w2_7455 with dissolve
    mc "Why are you being so difficult about it?"

    if feliciaFlag == True:
        "Felicia was a woman who was used to picking and choosing what she revealed to people. She had told me about herself, but I was safe. I was a nobody."
        "The people in front of her, on the other hand, were a pack of jackals and her would-be peers. I did understand why she would be hesitant, however..."
    else:
        "Felicia was a woman who was used to picking and choosing what she revealed to people. The people in front of her right now were a pack of jackals and her would-be peers."
        "I did understand why she would be hesitant, however..."

    scene w2_7456 with dissolve
    mc "You're an absurdly practical woman. Mrs. Pulman didn't set a time limit on this, so if you're not going to forfeit the night and get off this thing, then all you're doing is making it hard on yourself."
    mc "Isn't...{i}that{/i} uncomfortable?"
    scene w2_7457 with dissolve
    fel "Ah, haat...! A little... heh..."
    mct "(...or is she just dragging this out for the sake of the show?)"
    scene w2_7458 with dissolve
    mc "Tell me about your mother. Was she nice?"
    scene w2_7457 with dissolve
    fel "Y-yeah, I guess..."
    scene w2_7458 with dissolve
    mc "Did you two have a good relationship?"
    scene w2_7459 with dissolve
    fel "..."
    hide screen textbox2 with dissolve
    show screen mod_week2_expo
    menu:
        "Use a gentle approach."(chg=["felicia_up","hana_up","rosalind_up","august_up"]):
            hide screen mod_week2_expo
            $ Felicia_Affection += 1
            $ Hana_Affection +=1
            $ Rosalind_Affection +=1
            $ August_Friendship +=1

            scene w2_7460 with dissolve
            show screen textbox2 with dissolve
            mc "For me, my mother is the most important person in my life."
            scene w2_7461 with dissolve
            "I decided I would play a game of give-and-take, in hopes that exposing a little bit about myself to the crowd at large would make her comfortable to do the same."
            scene w2_7460 with dissolve
            mc "My father died when I was young, so she raised me as a single mother for my entire adolescence."
            scene w2_7461 with dissolve
            "Felicia knew some of this, but the men in the crowd didn't."
            scene w2_7462 with dissolve
            mc "She's beautiful, patient, and kind... so the fact she never remarried was an odd one. The few and far between dates she went on never really went anywhere..."
            scene w2_7463 with dissolve
            mc "I think she never got over my father or maybe she just didn't want to replace him."
            scene w2_7464 with dissolve
            mc "Did you have a good relationship with your mother?"
            scene w2_7465 with dissolve
            fel "My mom..."
            scene w2_7466 with dissolve
            fel "My mom... was a hard worker..."
            fel "She worked very hard for very little. As a result, she didn't have time to put up with bullshit, but she... provided."
            scene w2_7464 with dissolve
            mc "What about your dad?"
            scene w2_7465 with dissolve
            fel "...wasn't in the picture."
            scene w2_7467 with dissolve
        "(w2expts(fel)=+1)When in Rome...{vspace=50}"(chg=["hana_down"]):

            hide screen mod_week2_expo
            $ w2ExPointsFelicia += 1
            $ Hana_Affection -=1
            scene w2_7468 with dissolve
            play sound "sound effects/slap2.wav"
            scene w2_7469 with hpunch
            "*Thwwaaaack!*"
            fel "G'yeeeh...! Y-yeeeah...!"
            "The sudden blow caused her to writhe, dragging the edge of the horse across her soft spots."
            scene w2_7470 with dissolve
            fel "It was... fine.. t-typical... I guess... ah..."
            scene w2_7471 with dissolve
            mc "What does typical mean?"
            scene w2_7470 with dissolve
            fel "S-she... she worked herself to the bone at a factory. Always came home tired."
            fel "She wasn't warm, but... she took care of me. She provided."
            scene w2_7471 with dissolve
            mc "What about your father...?"
            scene w2_7472 with dissolve
            fel "He..."
            scene w2_7473 with dissolve
            play sound "sound effects/slap3.wav"
            scene w2_7474 with hpunch
            "*Slap!*"
            show screen textbox2 with dissolve
            scene w2_7470 with dissolve
            fel "H-he wasn't in the picture!"


    "So, we had that in common."
    scene w2_7475 with dissolve
    kat "Growing up, were you ashamed that your mom was just a poor, stupid factory worker?"
    scene w2_7476 with dissolve
    fel "{size=-10}Stupid...?{/size=-10} Fuck you!"
    scene w2_7475 with dissolve
    kat "Oh, my! Am I mistaken?"
    scene w2_7477 with dissolve
    fel "My mom is a bright woman!"
    scene w2_7478 with dissolve
    kat "Is she? From all appearances, I wouldn't think so."
    scene w2_7477 with dissolve
    fel "What the hell would you know? You've had everything handed to you. "
    scene w2_7478 with dissolve
    kat "Yes, you've earned everything you've had, didn't you? {b}Your poor, hardworking back{/b}."
    scene w2_7477 with dissolve
    fel "You don't know how people get trapp--"
    play sound "sound effects/vib-start.wav"
    scene w2_7479 with dissolve
    "*Bzzzt...!*"
    fel "Gehhh!"
    scene w2_7480 with dissolve
    kat "Oh, {b}I know{/b}, but I apologize if I offended you all the same."
    stop sound
    $ renpy.music.set_volume(.3, 0, channel = "ambient")
    play ambient "sound effects/vib-ongoing.wav"
    scene fel_e2_squirm2_a with dissolve
    show fel_e2_squirm2
    "The rubber edge of Felica's perch hummed to life, vibrating violently."
    fel "H-ha, wha...~"
    kat "It makes you wonder... if you aren't embarrassed by her, and you really have a good relationship with her, then why is she still working that same job?"
    kat "You have money now. You could provide a better life for her..."
    fel "T-thaa... she doesn't..."
    fel "S-She doesn't..."
    kat "She doesn't what, Mrs. Ford?"
    scene w2_7481 with dissolve
    fel "..."
    scene w2_7482 with dissolve
    kat "Oh, well... think about it for five minutes and then Mr. [mcl] will pick this conversation back up."
    scene w2_7483 with dissolve
    fel "Ha...! You're good at what you do, boss lady."
    scene w2_7484 with dissolve
    kat "I feel the same way, Mrs. Ford."
    scene fel_e2_squirm3_a with dissolve
    show fel_e2_squirm3
    "So, another five was set to pass."
    "This time, with the accompanying whirl of the vibrator's motors atop of the surreal murmur of casual conversation."
    fel "Gh-gh...!"
    "Felicia endured it admirably, but cracks were starting to show. The signs of strain were taking form on her face."
    fel "Ha--haaa...?"
    mct "(Pick up where she left off? Where the hell do I go from there?)"
    scene w2_7485 with dissolve
    "To Hana's credit, she stared intently at Felicia, never taking her eyes off the beleaguered woman."
    "I had a feeling she was more wrestling with her own feelings than appraising the \"quality\" of the performance."
    scene w2_7486 with dissolve
    "Ian, on the other hand..."
    "Just looked bored."
    scene fel_e2_squirm2_a with dissolve
    show fel_e2_squirm2
    fel "Haa.... hhhaa..."
    mc "You... doing alright?"
    "This time I couldn't help but ask."
    fel "Ahh... trying to focus here, stud."
    "If she wanted, she could take all the power away from the old lady. If she just answered her questions, this would be over in an instant..."
    scene w2_7487 with dissolve
    mc "...?"

    if kat_polite == True:
        "Mrs. Pulman caught my eye, gesturing toward me and pointing at Felicia."
    else:
        "Kathleen caught my eye, gesturing toward me and pointing at Felicia."

    stop ambient fadeout 3.0
    $ renpy.music.set_volume(1, 0, channel = "ambient")
    mct "(Guess she's telling me to start.)"
    scene w2_7488 with dissolve
    mc "Why..."
    fel "Ah, ehe...!"
    mc "Why did you leave home for the city, Felicia?"
    scene w2_7489 with dissolve
    play sound "sound effects/finger-snap.wav"
    mc "Felicia!"
    "By this point, her attention was divided by what was going on with her lower half."
    mc "Why did you--"
    scene w2_7490 with dissolve
    fel "I... I wanted t-to... I wanted more... you can't get much from a place like Wheatley..."
    fel "Not culturally... not.... financially.... it'd be like trying to squeeze water from a stone..."

    if feliciaFlag == True:
        "Of course, I had learned that much myself, but this was a matter of procedure."

    scene w2_7491 with dissolve
    mc "You craved culture?"
    scene w2_7490 with dissolve
    fel "Yeah... and excitement and... everything. I wanted to live... heh..."
    scene w2_7492 with dissolve
    mc "Looks like you found it, eh?"
    fel "Heh... heheh..."
    "She chuckled defiantly."
    scene w2_7493 with dissolve
    fel "R-right now... we're just moving our mouths and not in the fun way."
    scene w2_7494 with dissolve
    "......"
    "..."
    scene w2_7495 with dissolve
    fel "Leaving was a no-brainer. All I did was cause a lot of trouble for my mom, she got by better without me."
    scene w2_7496 with dissolve
    mc "Felicia..."
    "It was a sad sentiment I could relate to."
    mc "Do you... keep in touch with your mother?"
    scene w2_7495 with dissolve
    fel "I... I..."
    scene w2_7494 with dissolve
    "..."
    hide screen textbox2 with dissolve
    show screen mod_week2_expo
    menu:
        "Tickle the answer out of her."(chg=["kathleen_down","hana_up"]):
            hide screen mod_week2_expo
            $ Kathleen_Affection -=1
            $ Hana_Affection += 1
            scene w2_7497 with dissolve
            "It was an odd impulse, but I followed it."
            fel "Ehh--"
            scene w2_7498 with dissolve
            fel "G-gyeeaah...?"
            mc "Do you still keep in touch?"
            "Helpless and precariously seated as she was, her automatic emotional response to being tickled was..."
            scene w2_7499 with dissolve
            fel "Pfftahhhaahaa... eyeehhaha...!"
            "...to shake and magnify the sensation digging into her lower half."
            mc "Well? Well...?"
            scene w2_7500 with dissolve
            fel "W-whaa... haa... sttoop, haa... stop... pfft....!"
            fel "Y-yes! Y-yess...! I...!"
            scene w2_7501 with dissolve
            mc "Oh, yeah? How often?"
            fel "I--"
            scene w2_7502 with dissolve
            fel "T-twice a month. We talk on the phone..."
            show screen textbox2 with dissolve
        "(w2expts(fel)=+1)Pinch her nipples{vspace=50}."(chg=["hana_down"]):


            hide screen mod_week2_expo
            $ w2ExPointsFelicia += 1
            $ Hana_Affection -= 1
            scene w2_7503 with dissolve
            show screen textbox2 with dissolve
            "That outfit looked good on her, but..."
            scene w2_7504 with dissolve
            fel "Hehhhg..."
            mc "Do you still keep in touch?"
            fel "I..."
            scene w2_7505 with dissolve
            fel "I... eyehhh... I..."
            "A simple pinch of her overly-sensitive teat caused her to shake and magnify the sensation digging into her lower half."
            fel "Hyyy hhh.... I..."
            scene w2_7506 with vpunch
            fel "Haaa... haaat...!"
            "The felling of having both her crotch and breasts stimulated at once made the blonde go momentarily cross-eyed."
            fel "Y--yyyesh.... yesh!"
            scene w2_7507 with dissolve
            mc "Oh, yeah? How often?"
            fel "T-twice a month. We talk on the phone..."

    scene w2_7508 with dissolve
    show screen textbox2 with dissolve
    kat "That often...? Really?"
    "The old woman looked mildly surprised, like she had miscalculated."
    scene w2_7509 with dissolve
    kat "Interesting..."
    kat "She doesn't want your money then, is that it?"
    scene w2_7510 with dissolve
    fel "..."

    if kat_polite == True:
        "It seemed Mrs. Pulman hit the nail on the head."
    else:
        "It seemed Kathleen hit the nail on the head."

    scene w2_7511 with dissolve
    kat "Ha, very interesting! If only your mother could see her whore daughter right now!"
    scene w2_7512 with dissolve
    fel "...and I wonder what your late sister would think of you using her charity to pimp out women."
    scene w2_7513 with dissolve
    kat "Oh, I have a good idea. {b}She would strangle me to death!{/b}"
    scene w2_7514 with dissolve
    "......"
    "..."
    scene w2_7515 with dissolve
    kat "Heheh, aren't we having fun?"
    fel "O-oh y-yeah... you've dragged out of me the fact I have a... ha... decent relationship with the woman w-who gave birth to me. {b}Fun{/b}."
    scene w2_7516 with dissolve
    kat "Tell me about your relationship with art."
    scene w2_7517 with dissolve
    fel "That--"
    "That knocked the words out of her mouth."
    scene w2_7518 with dissolve
    fel "J-just a childish thing I did for fun..."
    scene w2_7519 with dissolve
    kat "That's not true, Mrs. Ford. You won regional awards and you even took first place in a national competition."
    scene w2_7520 with dissolve
    kat "You had talent."
    scene w2_7518 with dissolve
    fel "I was {b}mundane{/b}."
    scene w2_7519 with dissolve
    kat "Was it your dream to paint? Do you still do it? Tell me all about it~"
    scene w2_7521 with dissolve
    fel "...s-shit!"
    scene w2_7522 with dissolve
    fel "...ahh... ha... drag it out of me, [mcf]."
    scene w2_7523 with dissolve
    mc "Why don't you just answer the question th--"
    fel "{b}Drag. It. Out. Of Me{/b}."
    scene w2_7524 with dissolve
    kil "Careful what you ask for..."
    scene w2_7525 with dissolve
    hide screen textbox2 with dissolve
    show screen mod_week2_expo
    menu:
        "Take a sensual approach to getting the answers."(chg=["hana_up","felicia_up","veronica_passion_up"]):
            hide screen mod_week2_expo
            $ Hana_Affection += 1
            $ Felicia_Affection += 1
            $ Veronica_Horniness +=1
            scene w2_7526 with dissolve
            "She asked for it."
            scene w2_7527 with dissolve
            mc "Hmm..."
            scene w2_7528 with dissolve
            play sound "sound effects/ice-glass.wav"
            "There were a lot of colorful options, but I opted for the most understated of the bunch."
            scene w2_7529 with dissolve
            mc "Felicia..."
            scene w2_7530 with dissolve

            if feliciaFlag == True and w2FeliciaImpressed == True:
                "Just two days ago, I had gotten a glimpse of what the old woman was getting at with this topic. To be honest, I wanted to know more about the subject myself."
            else:
                mct "(So she's a painter...? I didn't expect that.)"

            scene w2_7531 with dissolve
            mc "What does art mean to you?"
            fel "C'mon...! That's too open-ended, can't you ask something more--"
            scene w2_7532 with vpunch
            fel "C-cooold! Ah!"
            "Luckily for me, Felicia's skin proved to be sensitive to even a brief touch of cold."
            scene w2_7533 with dissolve
            mc "Sorry. You're right. Let's not give you an essay."
            $ renpy.music.set_volume(.2, 0, channel = "ambient")
            play ambient "sound effects/vib-ongoing.wav"
            scene w2_7534 with vpunch
            fel "Y-yeeoh....!?"
            mc "When did you start painting?"
            fel "I was... ah..."
            scene w2_7535 with vpunch
            fel "--Ghe!"
            "Every dab, cooled by the heat of her skin, left a strand of water inching down her inner thigh."
            fel "I... I was... p-probably like six or seven at the time."
            scene w2_7536 with dissolve
            "Every dab brought a faint agitation to her flawlessly tanned skin."
            mc "Did you pick it up on your own? Did someone teach you?"
            scene w2_7537 with vpunch
            fel "Y-yatthhaaa!"

            if feliciaFlag == True and w2FeliciaImpressed == True:
                mc "Your mother? {b}A school?{/b}"
            else:
                mc "Your mother, maybe?"

            scene w2_7538 with dissolve
            fel "I... it was... my mother used it like daycare..."
            mc "Used what?"
            scene w2_7539 with dissolve
            "The blonde looked past me and at the crowd, trepidatious of revealing this part of her to that pack of hyenas."
            scene w2_7540 with vpunch
            fel "Ghhhaaa.... s-suddd, c-cold...!"
            "This time I pressed it lightly into her skin, lightly holding it and tracing the circumference of her belly button."
            scene w2_7541 with dissolve
            fel "Ghh... haa....!"
            "The sensation made her writhe, which of course, increased her discomfort."
            scene w2_7542 with dissolve
            mc "Did you pick painting up on your own?"
            fel "No- I...."
            scene w2_7541 with dissolve
            "...and the more uncomfortable she was, the more she writhed. It was a vicious cycle."
            scene w2_7542 with dissolve
            fel "There was a-a s-school? An a-art.... s-schoool...!"
            scene w2_7543 with dissolve
            mc "Sounds expensive."
            fel "I-it was f-freeee....! Aaaahhat...!"
            scene w2_7544 with vpunch
            mc "Really?"
            fel "Y-yeah...! Yes!"
            scene w2_7545 with dissolve
            fel "I went there three times a week a-after s-s-scchoooool...!"
            mc "...and you took to it?"
            fel "G-gradually..."
            scene w2_7546 with dissolve
            fel "Art taught me to pay attention to my surroundings and I learned how to distinguish between the form and essence of things..."
            fel "Most important lesson of my life, considering where I e-ended up... ha...."
            scene w2_7547 with dissolve
            kat "Was it your dream to be a painter?"
            scene w2_7548 with dissolve
            fel "N-not really..."
            scene w2_7547 with dissolve
            kat "Oh...?"
            scene w2_7549 with dissolve
            fel "Ghhehhh...! Y-yesh...Haaaat! Yes...?"
            scene w2_7550 with dissolve
            fel "Ght...yah-eh...!"
            mc "Honest?"
            fel "H-honest...!"
            scene w2_7551 with dissolve
            mc "You went so far as to win a national award and you only ever considered it a hobby?"
            scene w2_7552 with dissolve
            fel "...I mean... even as a teenager I knew..."
            fel "I knew I wouldn't make a living off of it..."
            scene w2_7551 with dissolve
            mc "Did you want to, though?"
            scene w2_7552 with dissolve
            fel "I... n-no..."
            scene w2_7550 with dissolve
            mc "Really?"
            fel "Yeeh.... n-no!"
            mc "No?"
            fel "No-nooohhh....! I wanted to teach!"
            scene w2_7553 with dissolve
            "The melting icecube had quickly brought her teat to a sharp and shiny point, planting a certain idea in my head."
            stop ambient fadeout 3.0
            scene w2_7604 with dissolve
            kat "You wanted to be an art teacher?"
        "(w2expts(fel)=+2)Give Ian something to do.{vspace=50}"(chg=["killian_up","chuck_up"]):


            hide screen mod_week2_expo
            $ Killian_Bromance += 2
            $ w2ExPointsFelicia += 2
            $ Chuck_Friendship +=1

            scene w2_7554 with dissolve
            "The old woman did say I was free to ask for a helping hand, so..."
            scene w2_7555 with dissolve
            mc "*Whisper* Tag you in?"
            "No sense in Ian worthlessly standing there."
            scene w2_7556 with dissolve
            kil "What are you thinkin'?"
            scene w2_7555 with dissolve
            mc "I'll ask the questions and you'll... make it interesting?"
            scene w2_7557 with dissolve
            kil "Interesting? Oh, yeah. I can do that!"
            $ renpy.music.set_volume(.2, 0, channel = "ambient")
            play ambient "sound effects/vib-ongoing.wav"
            scene w2_7558 with dissolve
            mc "So... Felicia..."
            mc "What's art to you?"
            scene w2_7559 with dissolve
            fel "Nghhh... haa.... can't you break that down into something simpler please?"
            fel "Kinda a big fuckin' question and I'm a bit... haa-!"
            scene w2_7560 with dissolve
            kil "Hey, Felish!"
            fel "Ng, ohh..!"
            kil "You're glowing tonight. Like a real star."
            scene w2_7561 with dissolve
            kil "Then again, it's so rare you're not."
            "Ian wore an undeserved, smug look on his face, relishing the opportunity to have a position of power over his friend."
            scene w2_7562 with dissolve
            fel "Ahhh... that's nice of you to say, Ian. Real {i}charming{/i}..."
            "His hands pawed savagely at her bust, cupping the tanned mounds and squeezing hard."
            scene w2_7563 with dissolve
            fel "Nnnhhh... [mcf]..."
            "His fingers played over her nipples, running over and plucking at them like a guitar string."
            scene w2_7564 with dissolve
            fel "W-would you m-mind rephrasin' a tad? Eh...? G-get this show on the road?"
            mc "When did you first start painting?"
            fel "I... I don't know, um--"
            scene w2_7565 with dissolve
            fel "G-gahh...!"
            "Jumping the gun, my friend tugged on the blonde's body, plucking a pleasure-wracked cry from the blonde's throat."
            scene w2_7566 with dissolve
            kil "{size=-10}Man, these puppies are a work of art...{/size=-10}"
            mc "{b}When did you first start painting{/b}, Felicia?"
            fel "Nnnh.... I-I d-don't know...! L-like seven, maybe? S-six or..."
            scene w2_7567 with dissolve
            fel "Ghh-! Six or seven!"
            "Ian was undoubtedly having fun."
            kil "You sure are responsive..."
            scene w2_7568 with dissolve
            fel "How 'bout you stick a vibrating triangle up your ass for twenty minutes and find out why...!"

            if kat_polite == True:
                "He was distracting her and drawing things longer than needed, but I was gaining an infinitesimal inkling of why Mrs. Pulman liked having a \"helper\" for these tasks."
            else:
                "He was distracting her and drawing things longer than needed, but I was gaining an infinitesimal inkling of why Kathleen liked having a \"helper\" for these tasks."

            scene w2_7569 with dissolve
            mc "Did you pick up painting on your own or did someone teach you?"
            fel "H-huh? Uh... say ag--"
            play sound "sound effects/slap1.wav"
            scene w2_7570 with hpunch
            "*Thwack!*"
            fel "C-christ! Ian! Ah... let 'im ask, first!"
            scene w2_7571 with dissolve
            mc "Did you pick up painting on your own or..."
            play sound "sound effects/slap1.wav"
            scene w2_7572 with vpunch
            "*Fwhack!*"
            fel "G-gahh...!"
            scene w2_7573 with dissolve
            mc "...did someone teach--"
            fel "T-teach me!"
            mc "Was it your mother?"
            play sound "sound effects/slap1.wav"
            scene w2_7574 with hpunch
            "*Fwhhiiip!*"
            fel "No!"
            scene w2_7575 with dissolve
            mc "Someone from school?"
            play sound "sound effects/slap1.wav"
            scene w2_7576 with vpunch
            "*Thwap!*"
            fel "Soooort of!"
            scene w2_7577 with dissolve
            mc "Sort of?"

            if feliciaFlag == True and w2FeliciaImpressed == True:
                "I, of course, knew the answer. It was the..."

            scene w2_7578 with dissolve
            fel "Ac-academy...! Art academy!"
            scene w2_7579 with dissolve
            fel "I went there three times a week..."
            scene w2_7580 with dissolve
            mc "Was it something you wanted for yourself?"
            scene w2_7581 with dissolve
            show screen textbox2 with dissolve
            fel "N-no... but I... gradually learned to... {b}love{/b} it."
            fel "Art taught me to pay attention to my surroundings and I learned how to distinguish between the form and essence of things..."
            scene w2_7582 with dissolve
            mc "To cut through the bullshit, you mean?"
            scene w2_7583 with dissolve
            fel "S-something like that."
            scene w2_7584 with dissolve
            kil "This isn't really my type of thing, so sorry if I'm a little rough at first."
            scene w2_7585 with dissolve
            play sound "sound effects/slap3.wav"
            scene w2_7586 with hpunch
            "*Thwack!*"
            fel "G-gaah! He hasn't asked a new question yet!"
            scene w2_7587 with dissolve
            kil "H-heh... sorry!"
            mc "Um... right..."
            mc "Did you want to be a painter when you grew up?"
            scene w2_7588 with dissolve
            fel "I... did not. Even as a teenager I had enough sense to know better."
            scene w2_7589 with dissolve
            mc "Really?"
            play sound "sound effects/slap3.wav"
            scene w2_7590 with vpunch
            "*Thwack!*"
            fel "G-ggeeeh, why would I lie?!"
            scene w2_7591 with dissolve
            mc "Well, I mean... you were good enough to win a national award and you only ever considered it a hobby?"
            scene w2_7592 with dissolve
            fel "...y-yeah. Why would you ever mix something you enjoy with {i}money{/i}?"
            "That struck me as an odd thing for her to say..."
            scene w2_7591 with dissolve
            mc "What did you want to be then?"
            scene w2_7593 with dissolve
            fel "..."
            scene w2_7594 with dissolve
            kil "Nah, for me... I'd rather..."
            scene w2_7595 with dissolve
            mc "What did you want to be when you were a kid?"
            stop ambient fadeout 3.0
            scene w2_7596 with dissolve
            fel "It's d-dumb--"
            scene w2_7597 with dissolve
            fel "Ahht...!"
            "Plugging Felicia's nose and locking lips, Ian kissed Felicia."
            "It was deep and long and every second stole her breath away, causing her to wriggle and writhe atop her triangular roost."
            scene w2_7598 with dissolve
            fel "Mmmh... mmmh...!"
            "He held it an alarming amount of time, to the point where I was afraid she might pass out..."
            scene w2_7599 with dissolve
            kil "You know, I always thought you'd be a better kisser than that."
            scene w2_7600 with dissolve
            fel "Y-yyou..! I--"
            scene w2_7601 with dissolve
            kil "I guess I can give you a pass considering the circumstances."
            scene w2_7602 with dissolve
            mc "What did you want to be when you were a kid, Felicia?"
            scene w2_7603 with dissolve
            fel "Ha... haa.... a... teacher. I wanted to be a teacher."
            scene w2_7604 with dissolve
            kat "...really? Hmmpfh."
            kat "You wanted to be an art teacher?"

    $ renpy.music.set_volume(1, 0, channel = "ambient")
    stop music fadeout 3.0
    scene w2_7605 with dissolve
    fel "I... I... I wanted to be like her..."
    scene w2_7606 with dissolve
    fel "..."
    scene w2_7607 with dissolve
    kat "That's twice you've surprised me tonight, Mrs. Ford. A woman like you aiming so... {i}low{/i}."
    scene w2_7608 with dissolve
    fel "I went on to better things."
    scene w2_7609 with dissolve
    kat "If you truly believed that, you wouldn't be sitting here. You, my dear, are not satisfied."
    scene w2_7610 with dissolve
    kat "You'll never be satisfied."
    kat "It's what's taken a redneck like you further than you ever could've dreamed, it's what makes you beautiful, and it's why you'll never feel happy and secure in who you are."
    play music "music/modern-situations.ogg"
    scene w2_7611 with dissolve
    fel "...ha, are an-any of you satisfied yourselves?"
    scene w2_7612 with dissolve
    "Despite her growing exhaustion, Felicia ignored the old woman and aimed a fierce look at the crowd."
    scene w2_7611 with dissolve
    fel "You... you all want more than what you have and need, else {b}you{/b} wouldn't be sitting here right now. Eat until you burst, right?"
    scene w2_7613 with dissolve
    chuck "Bahaha, you're right! Wonderful!"
    "Her spirit resonated with my old mentor, who freely voiced his agreement."
    chuck "Eat until you burst!"
    scene w2_7614 with dissolve
    frank "I like her."
    scene w2_7615 with dissolve
    kat "Tsk...!"
    scene w2_7617 with dissolve
    kat "Oh, let's take, say... a {b}twenty{/b} minute break, shall we?"
    scene w2_7618 with dissolve
    fel "{b}T-tweeenty...{/b}! I'll...! I'll.. {i}die{/i}!"
    scene w2_7619 with dissolve
    kat "Don't be dramatic. You won't {i}burst{/i}."
    kat "Instead, focus on {i}what is{/i} and {b}what could've been{/b}."
    scene w2_7620 with dissolve
    fel "Ah... ha... I'd rather think about {b}what will be{/b}, Ma'am."
    scene w2_7621 with dissolve
    kat "..."
    scene w2_7622 with dissolve
    kil "*Whispering* I think she might've met her match."
    hide screen textbox2 with dissolve
    scene fel_e2_squirm4_a with dissolve
    show fel_e2_squirm4
    "So the room settled in once more to watch the golddigger's descent into a blend of rapturous agony."
    "Felicia wore a half-cocked smile, a remnant from her brief repartee with the old woman, but that bluster was visibly wearing thin."
    mct "(I wonder how long she can stand...?)"
    "From the moment I had returned with Veronica, she had been in that position for more than thirty minutes."
    "We start pushing toward an hour and..."
    kil "She's gonna come out of this looking like a car wreck."
    fel "Heeh, ha....!"
    "He said it loud enough for the blonde to hear."
    scene w2_7623 with dissolve
    show screen textbox2 with dissolve
    kil "Wanna make a wager on how long it'll take her to crack?"
    scene w2_7624 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Felicia can take this."(chg=["felicia_up"]):
            $ Felicia_Affection += 1
            scene w2_7625 with dissolve
            show screen textbox2 with dissolve
            mc "She can handle another twenty minutes."
            scene w2_7624 with dissolve
            "I wasn't actually certain, but even as a pittance, I hope the words would boost her twisted mind's morale."
            scene w2_7626 with dissolve

            if toughness >= 21:
                mc "I believe in that slut."
            else:
                mc "I believe in her."

            scene w2_7627 with dissolve
            fel "Ha, haa....!"
            scene w2_7623 with dissolve
            kil "It doesn't sound like it to me."
            scene w2_7625 with dissolve
            mc "She'll surprise you."
        "Tell Ian no thanks.":


            scene w2_7625 with dissolve
            show screen textbox2 with dissolve
            mc "No, I don't think I do."
            scene w2_7628 with dissolve
            kil "What about you, Felish? You want to make a bet?"
            scene w2_7627 with dissolve
            fel "Ha! F-fuck you very kindly, Ian."
            "She took Ian's \"humor\" in stride."

    scene w2_7629 with dissolve
    kil "Wanted a closer look?"
    scene w2_7630 with dissolve
    hana "Actually, {b}yes{/b}..."
    "Hana approached the blonde with a curious glint in her eye."
    scene w2_7631 with dissolve
    fel "Ha, haa...? Y-yeah...?"
    scene w2_7632 with dissolve
    hana "You're the one who's doing this to join the club?"
    scene w2_7631 with dissolve
    fel "He, ha... s-something like that."
    scene w2_7633 with dissolve
    kil "It's exactly like that."
    scene w2_7631 with dissolve
    fel "You think I'm insane...?"
    scene w2_7634 with dissolve
    hana "No, I don't have the right to judge you, I'm just..."
    hana "Is this fun for you?"
    scene w2_7631 with dissolve
    fel "I d-don't know, I've never done this one before. I'll tell you when it's over."
    scene w2_7635 with dissolve
    "She did indeed look at Felicia like she was insane."
    scene w2_7632 with dissolve
    hana "I don't get it, but..."
    scene w2_7636 with dissolve
    hana "I wish everyone who performed was like you."
    "I could see the gears spinning in the rocker girl's pig-tailed head."
    mct "(Changes for the better, eh? That one felt unlikely...)"
    scene w2_7637 with dissolve
    fel "Ha, hhhhnggg... M-Mina talked about you a little bit, y'know..."
    fel "You're freakin' adorable."
    scene w2_7638 with dissolve
    hana "Thanks, you're, uh, well..."
    fel "About to--"
    scene w2_7639 with vpunch
    fel "Gyyyaaaaaah....! S-shit...!"
    "A streak of fem cum shot out from her slit and gave the dull metal body of her ride a nice sheen."
    scene w2_7640 with dissolve
    fel "Ghaaa... ha..."
    "The vibrator had taken its toll, however..."
    scene w2_7641 with dissolve
    fel "Ngh..."
    "It had only been a few minutes since we broke."
    scene w2_7642 with dissolve
    fel "Damn it... gghhh... sorry about your shoe..."
    hana "O-oh..."
    scene w2_7643 with dissolve
    hana "That's alright. My fault for standing so close..."
    scene fel_e2_squirm5_a with dissolve
    show fel_e2_squirm5
    "Her sudden orgasm had put a pin in their odd conversation and Hana joined us on the side as Felicia went back to not-quite-silently running out the clock."
    fel "Haahh... ghhhnn...."
    "The three of us didn't make small talk, we just watched with muted interest, enthralled by the sight unfolding not a few feet away."
    "Even Hana was mesmerized, seemingly less bothered by this than the opening act."
    fel "G-ghhaa!"
    "Every minute or so, she would be hit with another slight orgasm. Her thighs would shake and clap against her perch with a boisterous clamor, exhausting her deeper into a sexual fog."
    fel "Mmmh... haaaat..."
    "Ten minutes in and forty minutes total..."
    scene w2_7644 with dissolve
    fel "Myyyhhhhh...!"
    "Felicia gritted her teeth as another wave of terrible pleasure consumed her body."
    scene w2_7645 with dissolve
    fel "Haaa..."
    scene fel_e2_squirm6_a with dissolve
    show fel_e2_squirm6
    "Felicia was no longer smiling, instead she looked out to lunch. She was too focused on quelling the way her body involuntarily shivered and jerked."
    "It looked like a perverse form of meditation."
    "{b}Fifteen minutes in{/b}."
    mc "She's hanging in there."
    fel "Ghh... gh-guh..."
    kil "Is that what you call it?"
    "Seventeen minutes."
    hana "This is absurd, right?"
    fel "Hyy, yaahh.. nghhyaa....!"
    "Eighteen minutes."
    mct "(Had the old woman met her match?)"
    fel "Ghhaaa..."
    "Nineteen..."
    scene w2_7646 with dissolve
    fel "Nhhh... nhh...! Haaa...! Oh, shit--!"
    mc "Oohh...!"
    scene w2_7647 with dissolve
    "A momentarily lapse in concentration saw the blonde almost losing her balance."
    fel "G-geeh... t-thanks... g-good catch..."
    scene w2_7648 with dissolve
    kat "You're quite hardy, aren't you Mrs. Ford?"
    scene w2_7649 with dissolve
    kat "It's difficult to believe you're inexperienced with this type of play, even Harper would be..."
    "Felicia braced her body and supported herself under her own strength once more."
    scene w2_7650 with dissolve
    fel "Hnngh... it's just... {b}sitting{/b}, isn't it?"
    scene w2_7651 with dissolve
    kat "Your tenacity is commendable, but I know you're exhausted. By now, your waist should be numb and your back should be on fire."
    kat "I wonder how much it would take to break you~ oh, how I do love a challenge~"
    scene w2_7652 with dissolve
    jim "Twenty more minutes would do it!"
    tom "Yeah, let the bitch sit!"
    scene w2_7653 with dissolve
    kat "Hmmm..."
    "It seemed she no longer cared about the interrogation, but she looked elated at the prospect of pushing Felicia's endurance to the limit."
    scene w2_7654 with dissolve
    fel "H-heh... t-that's..."
    "{i}Please no{/i} was what she was thinking. It was written clear on her face."
    scene w2_7655 with dissolve
    kat "What say you, Miss Rhodes?"
    scene w2_7656 with dissolve
    hana "H-huh?"
    kat "I want to know if you think another twenty minutes would do it?"
    scene w2_7657 with dissolve
    hana "Um, why are you..."
    scene w2_7658 with dissolve
    "Hana's gaze wandered over to Felicia and the two shared a look."
    scene w2_7659 with dissolve
    hana "...don't you think this is getting old?"
    scene w2_7660 with dissolve
    kat "......"
    scene w2_7661 with dissolve
    kat "...I agree."
    scene w2_7662 with dissolve
    "Boop!"
    scene w2_7663 with dissolve
    kat "You've got a good sense for this, dear. We should change things up..."
    scene w2_7664 with dissolve
    kat "Mr. [mcl]?"
    scene w2_7665 with dissolve
    kat "I don't want the bitch to be able to stand after this."
    scene w2_7666 with dissolve
    mc "What do you want me to...?"
    scene w2_7665 with dissolve
    kat "The talking is over with. Move onto the main event."
    scene w2_7667 with dissolve
    mc "...got it."
    mct "(--not really.)"
    scene w2_7668 with dissolve
    kat "Make this a good show, Mrs. Ford. Shamelessly moan and thrust, even when you no longer have the stamina to."
    kat "You'll continue to impress us, won't you? You won't let [mcf] here upend your pride as a {i}slut{/i}, will you?"
    scene w2_7669 with dissolve
    fel "Ghhh... f-finally..."
    scene w2_7670 with dissolve
    kat "Floor's yours, Mr. [mcl]. Proceed however you find fitting."
    scene w2_7671 with dissolve
    mc "..."
    "{i}The floor was mine{/i}."
    hide screen textbox2 with dissolve
    stop music fadeout 2.0
    show screen mod_week2_expo

    menu:
        "(w2expts(fel)=+2)Mosey over to Felicia and get a taste before railing her good.{vspace=50}"(chg=["kathleen_up2","hana_down"]):
            hide screen mod_week2_expo
            $ w2FelSex = True
            $ w2ExPointsFelicia +=2
            $ Kathleen_Affection +=2
            $ Hana_Affection -=1

            scene w2_7672 with dissolve
            "Back strained by her {i}predicament{/i}, {b}they{/b} had been stealing my eyeline all night."

            if toughness >=21:
                mct "(Might as well do what I want to do.)"
            else:
                mct "(Let's make an effort for us to both feel good.)"

            fel "H-heh... y-you got a f-funny look."
            "Bon appétit."
            play music "music/bellissimo.ogg"
            scene fel_e2_ts1_a with dissolve
            show fel_e2_ts1 with dissolve
            fel "Hy-uhhh...!"
            "*Fwup, chwup...!*"
            "Without much ado, I latched onto the half-sensate blonde's nipple and sucked on the beautiful, diamond-hard nub like a starving infant."
            "At the same time, my hand found rest on the opposite breast, teasing and gently stroking its pliant titflesh, brushing and flicking its pale-pink point."
            fel "Hehhh... heehhh...!"
            "The sudden titty assault had the overwrought Felicia immediately whistling like a tea kettle."
            "A sheen of perspiration made the blonde quite the salty snack, beads of sweat funneling down her ample breasts and tickling my lips."
            fel "Ka-, ch- c'mon... get me down from here...!"
            "All the while I sucked, the vibrating edge of her seat continued buzzing and purring into her puffy sex without mercy."
            fel "Hehh... kh-khaa...!"
            "As a man, her discordant moans were the only appreciable clue I had to understanding what nearly an hour on that thing would feel like."
            fel "S-seriously...! She s-saihd m-main eveeeent...!"
            "It sounded sweet to my ears, tickling the ugly parts of me while I pursued the old woman's unsparring directive."
            fel "J-just f-fuck me al-already...! Ah...!"
            "I wanted as much myself, to find relief from the uncomfortable strain in my slacks, but..."
            scene fel_e2_ts3_a with dissolve
            show fel_e2_ts3 with dissolve
            fel "G'yyahh....!"
            "...but if my mission was to fuck her until she lost all feeling in her legs, then it couldn't hurt to stack the deck in my favor by letting her go another minute or so."
            fel "Fhh- ah, haaa...!"
            "I went full-on vacuum. Her nipple firmly between my lips, I roughly tugged and pulled, stretching the pink protuberance as far as it would reasonably go."
            "There was no sense in building a tempo, all semblance of delicacy had been taken out back and shot within the past hour."
            fel "Fye, hmm.... hnng...!"
            "Felicia's body was simply going haywire."
            "*Chwup, fhwhup...!*"
            "The skin of her back was burning hot to the touch. Even the gentlest of stimulation would've had her howling and {i}this wasn't gentle{/i}."
            "*Chwup, fhwhup, kwhup...!*"
            fel "Hyee... hhaaaaaaaaaa...!"
            "I was suckling these suckers raw."
            "*Fwhup, khwup, fwhup, cwhup!!!*"
            scene fel_e2_ts2_a with dissolve
            show fel_e2_ts2 with dissolve
            fel "[mcf]! Ha... y-yyeaahhh, It's lihhhk.... I c-can't feel aah-anything else, but mhy yyttttiiihhts....!"
            "Her befuddled admission trailed off into a delightful, high-pitched moan."
            mct "(Good!)"
            fel "A aaaahhhh....! Just...! Only.... m-mhy...!"
            mct "(That's right!)"

            if toughness >= 24:
                mct "(Focus on nothing else, but what I'm doing to you, slut!)"
            else:
                mct "(Focus on nothing else, but what I'm doing to you!)"

            fel "G-gaaaah, hhhnnggg...!"
            "This was playing on easy mode! She was getting {b}there{/b} fast, stimulated as she was on both halves of her body."
            mct "(C'mon...!)"
            fel "Hnng, gguah, ha-haaat...!"
            mct "(C'mon, just one more time and you're off that thing!)"
            fel "Hnn, hghhh... haaa, hnng--!"
            "Her moans devolved into gibberish and--"
            scene w2_7673 with flash
            fel "Ghhuhuhhhguheheheh....!"
            "The sound of all control and sense jettisoning out of her body filled the exhibition hall."
            fel "Ghehhheh... Immmsasooofhooockingggg--"
            scene w2_7674 with vpunch
            fel "Eyyuchh...!"
            scene w2_7675 with dissolve
            "*Plop!*"
            "Her time on the horse had finally taken its toll and so spellbound by her guttural cry, I let the rapidly weakening blonde slip through my fingers."
            fel "Ha, haa... heh.. heheh... haha..."
            eric "Is the bitch broken?"
            scene w2_7676 with dissolve
            mct "(...she's smiling?)"
            scene black with fade
            play sound "sound effects/zipper.wav"
            "Alley oop!"
            scene w2_7677 with fade
            mc "Are you...?"
            fel "Tch, h-hehh...!"
            "Her crotch was so inflamed that just grazing it with my fingernail caused her to shudder."
            scene w2_7678 with dissolve
            fel "F-finally... c'mon, stud..."
            scene w2_7679 with dissolve
            "{b}She's smiling{/b}."
            mct "(Fucking incredible.)"
            scene w2_7680 with dissolve
            mct "(And her...)"
            "Well, she was going to inevitably see me do this."
            mct "(Let's get this dancing monkey show started.)"
            scene w2_7681 with dissolve
            fel "Ghhhaaaah...!"
            "The moment I inserted myself, Felicia clamped down hard and a gush of lady squirt stained my pants."
            scene w2_7682 with dissolve
            mc "Did you really just fucking cum again?"
            fel "Gghhh... hehheh... f-fuck me, [mcf]."
            play ambient "sound effects/boobjob.wav"
            scene fel_e2_gb2_a with dissolve
            show fel_e2_gb2 with dissolve

            if toughness >= 21:
                mct "(Have it your way, you crazy bitch!)"
            else:
                mct "(Have it your way!)"

            "Leave it to Felicia to make it seem like she has the upper hand, even when her mind is melted from pleasure."
            "I put nearly all my strength into it from the git-go, withdrawing and ramming my cock back in with ass-quaking force, and causing Felicia's loose limbs to flop around like spaghetti."


            scene fel_e2_gb3_a with dissolve
            show fel_e2_gb3 with dissolve

            if w2FeliciaDegrade == True:
                mc "Is this is what you've been looking forward to, dick-for-brains?!"
            else:
                mc "Is this what you've been looking forward to?"

            fel "Heehh... haahh..."
            mc "Well...?!"
            scene fel_e2_gb2_a with dissolve
            show fel_e2_gb2 with dissolve
            fel "Ghhuu..."
            "The force of the fucking, as weighed down and secure as it was, had our impromptu metal support brace creaking."

            if w2FeliciaDegrade == True:
                mc "You heard Mrs. Pulman! Let everyone hear you, slut!"
            else:
                mc "Well, enjoy then!"



            scene fel_e2_gb1_a with dissolve
            show fel_e2_gb1 with dissolve

            fel "{size=-10}Hehah, ghhuhh...!{/size=-10}"
            "Despite the determined smile that was tattooed on her face, Felicia's body was dead weight and her moans could barely be heard over our copulation."
            fel "{size=-10}Ghh, ghhu...!{/size=-10}"
            "She mainly just grunted from the force of our sexes impacting each other."
            fel "{size=-10}He, ghhee...!{/size=-10}"

            if kat_polite == True:
                "She was utterly exhausted, worn down by Mrs. Pulman's game of attrition."
            else:
                "She was utterly exhausted, worn down by Kathleen's game of attrition."

            "Even still, she felt fucking amazing. She was so wet that I had no trouble coming or going. She just accepted me."
            "It was like we were in a near-frictionless state of rut. I would've felt like I was floating, if not for the strain on my back bringing me back to reality."

            $ renpy.music.set_volume(.2, 0, channel = "ambient")
            scene w2_7683 with dissolve
            kil "Eh? Eh? That could be you, y'know?"
            kil "Or have you two already...?"
            scene w2_7684 with dissolve
            hana "S-shut up, moron."
            scene w2_7685 with dissolve
            kil "Wait... {i}you're blushing{/i}?"
            scene w2_7686 with dissolve
            hana "I've never... I've never seen someone fuck this up close before."
            scene w2_7685 with dissolve
            kil "Wait, really? With how long you've been working here...?"
            scene w2_7686 with dissolve
            hana "I don't make a habit of staring!"
            $ renpy.music.set_volume(1, 0, channel = "ambient")
            scene fel_e2_gb2_a with dissolve
            show fel_e2_gb2 with dissolve
            kil "Well, drink it in. [mcf]'s balls deep in that slut."
            hana "Seriously, shut the fuck up! I can do without the commentary!"
            kil "That's nine inches of pipe splitting her--"
            $ renpy.music.set_volume(.2, 0, channel = "ambient")
            scene w2_7687 with dissolve
            show w2_7688 with vpunch
            kil "G-guh..."
            hana "I can see what's happening!"
            kil "O-owwh...!"
            $ renpy.music.set_volume(1, 0, channel = "ambient")
            scene fel_e2_gb3_a with dissolve
            show fel_e2_gb3 with dissolve
            mct "(...did Ian just groan?)"
            "I didn't know. My focus was on the woman in my hands."
            fel "{size=-10}He, ghhee...! G-good it...! Ha... this is...{/size=-10}"
            "Felicia murmured to herself, brain-cooked."
            fel "{size=-10}G-give me your fat load, stud...{/size=-10}"
            "She was insane, but she was a true succubus and a consummate performer, I'd give her that. Even in a half-lidded fuck coma, she prodded her partner on. "
            scene fel_e2_gb1_a with dissolve
            show fel_e2_gb1 with dissolve
            mc "Ha... you want it?"
            fel "{size=-10} Ghh-- gghu!{/size=-10}"
            "Back to just grunts. Well, whatever..."

            if w2FeliciaDegrade == True:
                mc "You can have it, you cum-sucking, piggy bitch!"
            else:
                mc "You can have it!"

            "*Schlick, schlick, fwhich...!*"
            "Tightening my grip on the back of her neck, I mustered everything I had and barreled for home plate."
            fel "{size=-10} Ghh-- gghu, gh--!{/size=-10}"
            "I focused my thoughts on my only purpose for this indeterminable span of minutes."
            "I concerned myself with only our mechanical act, of dwelling on the sensation of my cock splitting Felicia open and repeatedly ripping itself out from her clinging insides."
            mc "Ha...!"
            "Her sticky skin was rubbing my forearms raw, but the only sensation I paid attention to was the one building in my nuts."
            mc "Hah, oh yeah...!"
            "Yeah, I was feeling it. A swell of sexual urge was giving me that familiar sick feeling in my stomach, like I had to expel my desire lest I perish."
            scene fel_e2_gb2_a with dissolve
            show fel_e2_gb2 with dissolve
            mc "He, haa...!"
            "*Plop, plop, plop!*"
            "Sandwiched as close as we were, my ball sack beat brutally against her sloppy quim, flooding my brain with a surge of dopamine and the feeling that we both might break from this."
            mc "Ha...! Gah...!"
            mc "Gah, f-fuck, Felicia!"
            fel "{size=-10}Heh, ha--!{/size=-10}"
            "She tightened up, her insides squeezing me softly enough to feel perilous at the speed we were fucking."
            "Her body's instincts were flawless."
            scene fel_e2_gb1_a with dissolve
            show fel_e2_gb1 with dissolve
            mc "F-fuck...!"
            "I wasn't sure how long I had been at it, but..."
            mct "(I'm going to...!)"
            stop ambient
            stop music
            play sound "sound effects/spurt.wav"
            scene fel_e2_gb4_a with flash
            play sound "sound effects/spurt.wav"
            show fel_e2_gb4 with flash
            fel "{size=-10}Hnnng!{/size=-10}"
            "A gush of baby batter flooded Felicia's insides, mixing itself finely with her own sexual juices as I scraped the overflowing filling back in and out with my cock, packing my genetic code deeper and deeper inside her."
            play sound "sound effects/spurt.wav"
            with vpunch
            mc "Guh, ghhuh...!"
            "Her insides knew what to do, clinging securely and squeezing out every last drop of spunk from my urethra."
            mc "Ha...!"
            scene w2_7689 with dissolve
            "My hips finally got the memo they could stop."
            mct "(Holy shit...)"
            scene w2_7690 with dissolve
            "Felicia was indeed ruined."
            "It was thanks largely in part to the physics of sitting on a triangular wedge for an hour, but I still felt a perverse sense of accomplishment seeing my semen ooze from her gaping cunt."
            scene w2_7691 with dissolve
            kat "Good work, Mr. [mcl]. A fine job."
            scene w2_7692 with dissolve
            mc "Uh... thanks."
            scene w2_7693 with dissolve
            kat "Ha! The slut is truly fucked. Someone take a picture!"
            scene w2_7694 with dissolve
            "*Click*"
            kat "......"
            scene w2_7695 with dissolve
            kat "I was being rhetorical."
            kil "Heh... I can send it to you if you want..."
            kat "You...! Ah..."
            scene black with fade
            if not persistent.felW2Shame:
                play sound "sound effects/notification.wav"
                show memoryunlock with dissolve
                $ renpy.pause(3, hard=True)
                $ persistent.felW2Shame = True
                hide memoryunlock with dissolve
                $ renpy.pause(0.5, hard=True)
            kat "Get a few more, will you?"
            "......"
            "..."
            "I was going to need to change my pants after this, copious amounts of fem cum seeped through my slacks and stuck the fabric to my legs."
            $ renpy.end_replay()
            jump w2ExRosalindHumiliationPre
        "Focus on Felicia and forgo your own gratification."(chg=["felicia_up2","chuck_up","kathleen_down","kathleen_trust_down"]):


            hide screen mod_week2_expo
            $ Felicia_Affection += 2
            $ Chuck_Friendship +=1
            $ Kathleen_Affection -=1
            $ Kathleen_Trust -=1

            scene w2_7696 with dissolve
            mct "(First things first...)"
            "Between the old woman's harping and a losing battle against gravity, Felicia's had it rough."
            scene w2_7697 with dissolve
            mc "Need a hand off that thing?"
            fel "Y-yes! God, yes! That'd be... {b}very{/b} gentlemanly."
            scene w2_7698 with dissolve
            fel "Ghh-"
            scene black with fade
            "Her body was beyond sensitive right now, it would be a cakewalk getting her to sing for the audience - but I wanted to make this enjoyable for her and her perverted inclinations foremost."
            scene w2_7699 with dissolve
            fel "W-woah...!"
            mc "I've got you."
            fel "{size=10}Gah, my l-legs are fucking numb, but...{/size=10}"
            scene w2_7700 with dissolve
            fel "Looks like I'm standing. You've got your work cut out for you, stud."
            scene w2_7701 with dissolve
            "Ever and always the tenacious slut, Felicia stole a glance at the leering crowd."
            scene w2_7702 with dissolve
            mc "*Whispering* Need a minute?"
            scene w2_7703 with dissolve
            fel "*Whispering* I don't think we have a minute. They're waiting."
            scene w2_7704 with dissolve
            mc "*Whispering* Alright. Let's have some fun now then."
            scene w2_7705 with dissolve
            scene w2_7706 with dissolve
            scene w2_7705 with dissolve
            "She simply nodded with confidence, a smile on her face."
            scene w2_7707 with dissolve
            fel "I'm in your hands, Mr. [mcl]."
            scene black with fade
            mc "Let's get a better look then."
            play music "music/ode-to-joy.ogg"
            scene w2_7708 with snake
            mc "See 'em all so clearly?"
            mc "This is catnip to an exhibitionist slut like you, right?"
            mc "All these curious, lecherous faces held captivated by your naked body..."
            scene w2_7709 with dissolve
            fel "Hhhghh...."
            scene w2_7710 with dissolve
            "Felicia shivered in my arms. This may have been about her own gratification, but I took pleasure from her response."
            scene w2_7711 with dissolve
            fel "Yeah, I see them..."
            scene w2_7712 with dissolve
            mc "You have CEOs and all other manner of powerful men's eyes glued to you right now."
            scene w2_7713 with dissolve
            mc "Dr. Van Doren is a pioneer in the field of medicine. He did business with your father-in-law."
            mc "He's ten feet away, watching you throw all your self-respect away and getting groped like a common whore."
            scene w2_7714 with dissolve
            fel "Nnnghh..."
            scene w2_7713 with dissolve
            mc "There's a five-time elected congressman here, as well as the Morehead Hills Chief of Police watching you."
            scene w2_7715 with dissolve
            fel "H-haaat...!"
            mc "How does that make you feel, slut?"
            fel "I-incredible!"
            scene w2_7716 with dissolve
            mc "Hmpfh. And then there's Dr. Kohler. He made millions engineering something your hick ass couldn't even begin to comprehend. See him?"
            scene w2_7717 with dissolve
            fel "Hhhgh..."
            scene w2_7716 with dissolve
            mc "Dirty whore. He's here for you."
            scene w2_7717 with dissolve
            fel "H-haaaah! F-fuck me...!"
            "She called out in a plaintive tone, so sad and needy that I felt bad saying..."
            scene w2_7718 with dissolve
            mc "No. I'm not going to fuck you."
            fel "C'm-what...? Eh?"
            scene w2_7719 with dissolve
            mc "Don't fret. You're going to get off, but it's not going to be my dick that does it."
            scene w2_7720 with dissolve
            mc "It's going to be all these gentlemen's eyes that do it. We're going to give them a VERY close look at that pretty pink pussy of yours."
            fel "Hgggg....!"
            scene w2_7721 with dissolve
            mc "Let's take this to the floor, {b}Mrs. Ford{/b}."
            fel "Ha, haa...!"
            scene w2_7722 with dissolve
            "Guiding the beautiful blonde to the floor, I pried her limbs apart to grant everyone an unfettered view."
            "I wanted to be sure that no amount of thrashing in the throes of sexual ecstasy would obstruct their eyes from her intoxicating body."
            "This is what she likes right, well then..."
            scene w2_7723 with dissolve
            mc "*Whispering* Enjoy, Felicia. Eat until you burst."
            fel "[mcf]--"
            scene fel_e2_fs1_a with dissolve
            show fel_e2_fs1 with dissolve
            fel "Hng, aah...!"
            "Setting any more fanfare aside, I dipped my middle and ring fingers into Felicia's honeypot and stirred."
            "Her pussy was swollen and red, engorged from almost an hour of nonstop stimulation, so I took it slow and paid attention to her response."
            fel "Hhhghh... you sure you wouldn't rather just fuck me, stud?"
            "Every rub and touch resulted in either an uncomfortable wince or a pleasured shiver from Felicia, and distinguishing between the two and just doing the latter was my principle concern."
            mc "I'd just get in the way of everyone looking at you."
            fel "Hhhhuuu...!"
            scene fel_e2_fs2_a with dissolve
            show fel_e2_fs2 with dissolve
            "Eventually, I found a satisfactory pace and angle that had the hazy-eyed blonde squirming sweetly in my arms."
            "Her lower mouth swallowed my digits with ease, allowing me unburdened access to scrape and prod the slippery lining of her sex to my heart's content."
            mc "It's not just the men in front of you that are watching either. You've got eyes on you from all around."
            fel "Haa... y-yes!"
            mc "There's Rosalind and Veronica to our left, contemptuously staring a hole into your side, but you don't care."
            mc "You like being hard to figure out. You take pride in it."
            fel "Huuuughh... m-maybe..."
            mc "That's not all either, Ian and Hana are to our right."
            mc "He's your friend's boyfriend, you dirty slut."
            fel "H-heh...! You sure know how to sweet talk a gal, [mcf]."
            mc "I'm not doing a damn thing, Felicia. This is all you~"
            "She shuddered with each syllable, each being carried on a puff of hot air that traveled down and tickled the nape of her neck."
            scene fel_e2_fs1_a with dissolve
            show fel_e2_fs1 with dissolve
            mc "You were destined to be in the spotlight- - your perverted mind and that slutty body of yours."
            fel "Hhhng--"
            "Every lewd accusation caused her slippery hole to hug my fingers all the more, to fruitlessly wrangle a urethra that wasn't there."
            fel "K-keep talking...!"
            mc "They see EVERYTHING right now. Your battered pussy..."
            fel "Ha, hhggg..."
            mc "Your beautiful pink pucker...!"
            fel "Y-yeees!"
            mc "Your fat, ripe--"
            scene w2_7724 with dissolve
            fel "Ghhaaaa!"
            "A spurt of sex juice shot out like a geyser, ending just as abruptly as it started."
            scene fel_e2_fs3_a with dissolve
            show fel_e2_fs3 with dissolve
            "--but I didn't stop, instead I carried on faster. I kept talking."
            mc "They see everything~ Your fat, delicious tits~"
            fel "Hhh-haaa...!"
            mc "Your tight tummy~ Your full lips~"
            "Even I was getting pulled into the excitement, buzzed on the feeling of her damp naked back pressed into my chest and the power of prying her open for display."

            if w2FeliciaDegrade == True:
                mc "You dirty, no good whore! You love it, don't you?"
            else:
                mc "You horny bitch! You love it, don't you?"

            fel "Waah? Eeeugnghhh...!"
            mct "(Holy hell...)"
            fel "-it's g-good! This is better than a cock...?!"
            "It was as if her sex was trying to suck my fingers out of their sockets. Felicia was turned on greater than I had ever previously seen her - or any woman for that matter..."
            fel "This feeling...! In my stomach, my back, my chest...!"
            fel "I can barely breathe! I could die...! Ha...!"
            "As if under a spell, the words poured out of Felicia's mouth like flowing water."
            fel "Thiseeessthebeeeest!"
            fel "E-everyone look at me! G-get a good look...!"
            "She dared to address the men in front of us."
            scene w2_7725 with dissolve
            fel "Vincenzo, Frank, Eric, Joe, Thomas... everyone, aaahh...!"
            scene w2_7726 with dissolve
            "As simple of a \"main event\" this was, Felicia sold it to the crowd."
            scene w2_7727 with dissolve
            fel "I see you. You're not men. You're just filthy animals-! Just pure egos bumping into each other for dominance~"
            scene w2_7728 with dissolve
            fel "I see you for what you are. {b}Do you see me{/b}?"
            "She showed her would-be peers who she was, better than the old woman's attempt."
            scene w2_7729 with dissolve
            shel "The bitch is losing it!"
            scene w2_7730 with dissolve
            chuck "Shut up, Joe."
            shel "H-huh?"
            chuck "Let me enjoy this moment without you demeaning it, you dumb bastard."
            scene w2_7731 with dissolve
            "The whole crowd fell silent from Dr. Chuck's demand. Since starting here, I'd seen many new sides of him, but this was the first time I had glimpsed irritation."
            mct "(...and for what?)"
            fel "Eeeeh...!"
            scene fel_e2_fs4_a with dissolve
            show fel_e2_fs4 with dissolve
            "It wasn't my concern. The blonde in my arms was my whole world right now."
            fel "This is what... {size=10}this is....{/size=10} {size=5}this...{/size=5}"
            "...but her enthusiasm was wearing her down and she was finally succumbing to the effects of the last hour."
            mc "*Whispering* I'm glad you're enjoying yourself Felicia."
            fel "G-guhhh.... eeehuuhhh...."
            mc "*Whispering* This was the best I could come up with for you. Are you happy?"
            fel "{size=10}Y-yesshh...! C-can't you tell?{/size=10}"
            "I may not understand it, but..."
            mc "*Whispering* I'm glad."
            "Felicia's hedonism was absurd, but in the madness of her perversion, there was purity and beauty. An unwillingness to be held down."
            fel "Gggh, hhaaa... th-thank..."
            "My dick pressed painfully into her back and I was, in a way that defied all reason, happy to be the hand showing her off."
            stop music
            scene w2_7733 with flash
            with vpunch
            fel "Ghhh, eeennnhhh, hhaaaathank you...!!"
            "Felicia erupted and the tension was cut from her body."
            scene w2_7734 with vpunch
            fel "Hhhhnghh!"
            "She shook and squirmed, but she was more or less dead weight in my arms as she let her faculties vacate her body."
            fel "Heheh... hehh...."
            scene w2_7735 with dissolve
            mc "*Whisper* Good girl..."
            fel "Ha-haa...."
            "It was... {b}a lot{/b}. The carpet in front of us was stained with Felicia's piss and cum."
            scene w2_7736 with dissolve
            fel "{size=-10}H-huh...{/size=-10}"
            mct "(Wow...)"
            "What a fucking mess."
            scene w2_7737 with dissolve
            fel "{size=10}I c-can't feel my legs...{/size=10}"
            fel "{size=10}N-nnever.. c-cumsso - h-hard...{/size=10}"
            "Was this good enough? Should I stop it here?"
            show screen mod_week2_expo
            menu:
                "End it here.":
                    hide screen mod_week2_expo
                    "It might not have been what anyone watching was expecting, the old woman included, but Felicia had burned brightly in my opinion."
                    scene w2_7738 with dissolve
                    mc "It's done. She's exhausted."
                    scene w2_7739 with dissolve
                    kat "...hmmm."
                    scene w2_7740 with dissolve
                    fel "{size=-10}Heehh... m-more...{/size=-10}"
                    "Kat gave the blonde a rousing kick."
                    scene w2_7741 with dissolve
                    kat "So she is, it seems."
                    scene w2_7742 with dissolve
                    "She said it with a curious smile, but I got the impression she wasn't completely happy with how I handled it."
                    scene w2_7741 with dissolve
                    kat "Clean the slut up. We'll move onto Mrs. Carter."
                    scene black with fade
                    if not persistent.felW2Shame:
                        play sound "sound effects/notification.wav"
                        show memoryunlock with dissolve
                        $ renpy.pause(3, hard=True)
                        $ persistent.felW2Shame = True
                        hide memoryunlock with dissolve
                        $ renpy.pause(0.5, hard=True)
                    mc "...same deal as last time?"
                    "......"
                    "..."
                    $ renpy.end_replay()
                    jump w2ExRosalindHumiliationPre
                "(w2expts(fel)=+2)Put a final degrading flourish on it to make it more palatable to the patrons{vspace=50}."(chg=["kathleen_up2","kathleen_trust_up","veronica_down","felicia_down2","rosalind_down","hana_down2"]):

                    hide screen mod_week2_expo
                    $ w2ExPointsFelicia +=2
                    $ Kathleen_Affection +=2
                    $ Kathleen_Trust +=1
                    $ Veronica_Affection -=1
                    $ Felicia_Affection -= 2
                    $ Rosalind_Affection -=1
                    $ Hana_Affection -=2
                    $ w2FelHalfMeasure = True
                    "When she said she didn't want Felicia to be able to walk, it {i}might{/i} not have been so literal, however..."
                    play music "music/leaving-home.ogg"
                    scene w2_7743 with dissolve
                    "Standing up, I held the woman by her fine golden hair."
                    fel "{size=10}Heehh... oh-oh...{/size=10}"
                    mc "It's done. The slut's exhausted."
                    scene w2_7744 with dissolve
                    mc "Thank everyone for watching you tonight, whore."
                    "It was my best impression of the old woman."
                    scene w2_7745 with dissolve
                    fel "{size=10}T-thank{/size=10} {size=5}yyooo{/size=5}ouuu..."
                    scene w2_7744 with dissolve
                    mc "There you have it, gentleman. You've now seen Felicia for who she really is."
                    play sound "sound effects/thud-floor.mp3"
                    scene w2_7746 with vpunch
                    fel "W-hoah..."
                    "*Thwap!*"
                    "Letting go, I let her fall into her own dirty mess."
                    play sound "sound effects/spit.wav"
                    scene w2_7747 with dissolve
                    mc "*Hock--!*"
                    scene w2_7748 with dissolve
                    "I added my contribution to the pool of fluids Felicia was lying in."
                    scene w2_7749 with dissolve

                    if feliciaAnger == True:
                        mc "Disgusting fucking pig. Soak it in."
                        scene w2_7750 with dissolve
                        "I had only intended my words to be theatrics, but as I spoke them, the same irrational contempt I felt during her husband's interview rose to the surface. "
                    elif feliciaFlag == True and feliciaAnger == False:
                        mc "Soak it in."
                        scene w2_7750 with dissolve
                        "This was a half measure, having finally done my best to fulfill Felicia's fantasy, of giving these perverted fucks what they wanted. Of course, despite any \"professional\" intentions, treating the rich woman like dirt.."
                        mct "(Made me so fucking hard.)"
                    else:
                        mc "Soak it in."
                        scene w2_7750 with dissolve
                        "This was my half-measure, in between making this fun for Felicia and giving these perverted fucks what they wanted."

                    scene w2_7751 with dissolve
                    kat "Hmmpfh."
                    scene w2_7752 with dissolve
                    kat "So it does indeed seem."
                    scene w2_7753 with dissolve
                    kat "Go clean her up, Mr. [mcl]. We'll move onto Mrs. Carter."
                    scene black with fade
                    if not persistent.felW2Shame:
                        play sound "sound effects/notification.wav"
                        show memoryunlock with dissolve
                        $ renpy.pause(3, hard=True)
                        $ persistent.felW2Shame = True
                        hide memoryunlock with dissolve
                        $ renpy.pause(0.5, hard=True)
                    stop music fadeout 3.0
                    "......"
                    "..."
                    $ renpy.end_replay()
                    jump w2ExRosalindHumiliationPre

label w2ExRosalindHumiliationPre:
    scene w2_7754 with wiperight
    play music "music/cold-sober.ogg"
    show screen textbox2 with dissolve
    war "Gh-! Would you mind trying LIFTING next time, kid?"
    scene w2_7755 with dissolve
    kil "A big strong man like you surely isn't complaining over a couch, is he?"
    scene w2_7756 with dissolve
    war "Just shut up and go get the other camera, dipshit."
    scene w2_7757 with dissolve
    kil "Why does everyone always call me--"
    scene w2_7758 with cmet
    "*Cl-chwiiick!*"
    scene w2_7759 with dissolve
    "Just as with Veronica, I had returned the gold-digging blonde to the cage sans clothing. Apart from nodding off in the shower once or twice, it was a less somber cleanup than Veronica."
    mc "Were you shocked by the way I behaved?"
    scene w2_7760 with dissolve
    hana "Do you care what I think?"
    scene w2_7761 with dissolve
    mc "Yes."
    if w2FelHalfMeasure == True:
        scene w2_7762 with dissolve
        hana "I know you were just doing your job, but... you enjoyed it on some level, right?"
        scene w2_7761 with dissolve
        mc "...right."
        scene w2_7763 with dissolve
        hana "..."
    elif w2FelSex == True:
        scene w2_7760 with dissolve
        hana "It was..."
        scene w2_7764 with dissolve
        hana "Interesting."
    else:
        scene w2_7760 with dissolve
        hana "It could've been a lot worse."

    scene w2_7765 with dissolve
    hana "I'm glad {i}she{/i} seemed to enjoy herself at least--"
    scene w2_7766 with dissolve
    fel "Aaffwwwh...!"
    scene w2_7765 with dissolve
    hana "I-is she asleep?!"
    mc "I mean, have you ever been on one of those things? For an hour?"
    scene w2_7767 with dissolve
    hana "Of course not! I..."
    scene w2_7768 with dissolve
    hana "Eugh... I'm imagining it."
    scene w2_7769 with dissolve
    mc "Yeah, probably tuckers you the fuck out to say the least."
    scene w2_7770 with dissolve
    kat "To say the least."
    scene w2_7771 with dissolve
    kat "How are you finding the show so far, Miss Rhodes?"
    scene w2_7772 with dissolve
    hana "Oh, it's just lovely Mrs. Pulman. I'm having a great time."
    scene w2_7771 with dissolve
    kat "You'll take to this business. You've got pornography in your blood, after all."
    scene w2_7773 with dissolve
    if w2FelSex == False:
        kat "I enjoyed the direction you took it tonight. Good work."
        scene w2_7774 with dissolve
        mc "Did you really? I was worried it might be a little too..."
        scene w2_7773 with dissolve
        kat "It was fine. It wasn't exactly to my tastes, but the men seemed to enjoy it."
        kat "That's the beauty of having another mind to rely on."
        mct "(If you say so...)"
    else:
        kat "You gave it to Mrs. Ford good tonight. You're a natural."
        scene w2_7774 with dissolve
        mc "Um, thanks..."
        mct "(It's easy to tune out the crowd when you have beautiful women to work with.)"

    scene w2_7775 with dissolve
    ver "Ha! Things didn't go the way you hoped with her, did it?"
    ver "She didn't lose her composure!"
    scene w2_7776 with dissolve
    kat "No, certainly not like you did, Miss Lynch. However..."
    scene w2_7777 with dissolve
    kat "Mrs. Ford has given me some wonderful ideas to go forward."
    kat "The unpredictability of these games keeps things fun and interesting."
    scene w2_7778 with dissolve
    kat "Maybe Mrs. Carter will surprise me too."
    scene w2_7779 with dissolve
    hana "What's with the couch? It's dramatically less..."
    scene w2_7780 with dissolve
    kat "Oh, Rosalind willing, we'll be putting them to good use."
    scene w2_7779 with dissolve
    hana "Right, of course, {i}stupid question{/i}..."
    scene w2_7781 with dissolve
    kat "Now, get the cow out of her pen and onto the couch, will you?"
    mc "Sure..."
    scene black with fade
    play sound "sound effects/metal-crash.mp3"
    "*Cl-chwiiick!*"
    scene w2_7782 with dissolve
    rose "Ugh..."
    rose "I'm getting old."
    scene w2_7783 with dissolve
    mc "I hate to be the one to tell you to go sit back down, but..."
    scene w2_7784 with dissolve
    mc "Go sit down."
    scene w2_7785 with dissolve
    rose "...yes, sir."
    scene w2_7786 with dissolve
    "With small footsteps, she slowly disembarked."

    if veronicaFriend == True:
        scene w2_7790 with dissolve
        ver "Hey, [mcf]?"
        ver "I know it's..."
        scene w2_7791 with dissolve
        ver "I mean..."
        scene w2_7792 with dissolve
        mc "What is it?"
        scene w2_7793 with dissolve
        "......"
        "..."
        scene w2_7794 with dissolve
        stop music fadeout 3.0
        ver "*Sigh* Go do your job, you fucking pervert."
        mc "...yeah, I will?"
        scene black with fade
        "What else would I do?"
    else:

        scene w2_7787 with dissolve
        ver "Night's soon finally going to be fucking over."
        scene w2_7788 with dissolve
        mc "Why don't you get some sleep like your cellmate? Be over even quicker."
        scene w2_7787 with dissolve
        ver "Are you fucking kidding? She's the only woman who could be snoozing at a time like this."
        scene w2_7789 with dissolve
        stop music fadeout 3.0
        ver "She's tougher than she looks, huh?"
        scene black with fade
        "Indeed."

    scene w2_7795 with fade
    kil "You have any plans for tomorrow?"
    mc "Just a lazy Sunday hopefully. This week's been... {b}draining{/b}."
    play music "music/hotshot.ogg"
    scene w2_7796 with dissolve
    "..."
    scene w2_7797 with dissolve
    kil "{b}Same{/b}, tell me about it. I just wanna..."
    scene w2_7798 with dissolve
    mc "What's with that dumb look on your face?"
    scene w2_7799 with dissolve
    kil "...that's just my face, asshole."
    scene w2_7800 with dissolve
    mc "..."
    scene w2_7801 with dissolve
    kil "Anyway, I was trying to ask, you wanna kick it or something?"
    scene w2_7802 with dissolve
    mc "I don't really feel like going to a nightclub, Ian."
    scene w2_7801 with dissolve
    kil "No... I just mean, you and me - chillin' y'know?"
    scene w2_7802 with dissolve
    mc "No alcohol or girls...?"
    scene w2_7801 with dissolve
    kil "Yeah, like the old days... play some games or just... {i}talk{/i}?"
    scene w2_7803 with dissolve
    mc "We're not kids anymore, dude. Why are you always so like {i}old times{/i} and shit?"
    scene w2_7804 with dissolve
    kil "Are you serious? Don't you miss how simple things used to be?"
    scene w2_7805 with dissolve
    mc "What do you mean? Your life's way better now."
    scene w2_7806 with dissolve
    kil "I mean yeah, of course it is. Duh. Right? Heh..."
    kil "I'm just sayin'..."
    scene w2_7807 with dissolve
    mc "To be honest, I don't think about it that much. I don't see the point."
    scene w2_7808 with dissolve
    kil "..."
    scene w2_7809 with dissolve
    mc "Hah, sorry -- yeah. Alright."
    mc "Let's \"kick\" it tomorrow. It'll be fun."
    scene w2_7810 with dissolve
    kil "...you couldn't have just started with that?"
    kil "Were you tryin' to make me feel like a blubbering pussy, you robotic cunt?"
    scene w2_7811 with dissolve
    mc "Sorry. You know how I am. Beep, boop."
    scene w2_7812 with dissolve
    kil "There's a reason I'm your only friend."
    mc "Same to you."
    scene w2_7813 with dissolve
    kat "If everyone's settled, then we can begin."
    scene w2_7814 with dissolve
    hana "Ah, fuck. Ummm... good luck, Rose."
    rose "Thanks..."
    scene w2_7815 with dissolve
    hana "*Whispering* What the fuck, do you know what her husband..."
    scene w2_7816 with dissolve
    mc "Yeah, I do."
    scene w2_7817 with dissolve
    hana "...eugh!"
    scene w2_7818 with dissolve
    kat "Please take your seat Miss Rhodes."
    scene w2_7819 with dissolve
    kat "Ian, would you please make sure both video cameras are working properly?"
    kil "Got it."
    scene w2_7820 with dissolve
    mc "What should I do?"
    kat "Just stand off to the side awaiting direction. We'll begin once Ian is finished."
    scene black with fade
    stop music fadeout 3.0
    "It didn't take long for Ian to finish."
    "A couple minutes later..."

label w2ExRosalindHumiliation:
    play music "music/doll-dancing.ogg"
    scene w2_7821 with curtains
    kat "Ending the night, we have Mrs. Carter. Say hello, dear."
    rose "H-hello..."
    scene w2_7822 with dissolve
    kat "I know you watched the first two events closely. So, you must think you have an idea of how this is going to go?"
    scene w2_7823 with dissolve
    rose "I got no id--"
    kat "Well, I'm afraid to say, you're not as interesting as the other two. No one here really gives a damn about your background."
    scene w2_7824 with dissolve
    kat "You're just a meek, pathetic woman. Am I wrong?"
    scene w2_7825 with dissolve
    rose "I, uh... I mean..."
    scene w2_7826 with dissolve
    rose "{b}You're wrong...{/b}."
    scene w2_7827 with dissolve
    kat "I'm glad you didn't agree, because I know deep down you believe yourself to be practical."
    kat "You're not a whore, you're a survivor.... is it something like that?"
    scene w2_7826 with dissolve
    rose "I'm whatever you say I am, Mrs. Pulman."
    scene w2_7828 with dissolve
    kat "Please, don't back track, dear. I want you to speak your mind."
    scene w2_7826 with dissolve
    rose "...so you can twist what I say and use it against me?"
    scene w2_7827 with dissolve
    kat "Ha! You're wiser than those other two whores, I'll give you that."
    scene w2_7826 with dissolve
    rose "...thank you, Ma'am."
    scene w2_7829 with dissolve
    kat "I didn't say it was a good thing. Being so \"malleable\" won't make you stand out tonight."
    scene w2_7830 with dissolve
    kat "You've got to make an impression on Miss Rhodes. She'll be weighing your humiliation against your conviction tonight."
    scene w2_7825 with dissolve
    rose "I'm not sure that makes any sense..."
    scene w2_7831 with dissolve
    kat "Mrs. Carter, you'll do anything for your daughter, is that true?"
    scene w2_7832 with dissolve
    rose "Please don't bring her into this."
    scene w2_7831 with dissolve
    kat "I like that about you. You don't try to hide your shame like Miss Lynch does."
    scene w2_7832 with dissolve
    rose "Why would I? What I'm doing IS shameful."
    scene w2_7831 with dissolve
    kat "Yet you're doing it, because you'll do anything for your daughter. I do wonder though..."
    scene w2_7833 with dissolve
    kat "If you're really such a good mother, why the hell did you stick around with that failure of a husband of yours?"
    scene w2_7834 with dissolve
    rose "I..."
    scene w2_7835 with dissolve
    rose "I've got no excuse."
    scene w2_7836 with dissolve
    kat "As far as I'm concerned, you're responsible for your own predicament. The thing that sunk you wasn't the first blow. You weren't blindsided by his behavior."
    scene w2_7835 with dissolve
    rose "He was sick, I didn't think he'd take it as far as borrowing from--"
    scene w2_7837 with dissolve
    kat "Yes! Gambling is an addiction, isn't it?"
    kat "Apart from cards, he also liked to gamble whatever money you two managed to save in ill-conceived investments. {b}More than a dozen of them{/b}, if my research is to be believed."
    scene w2_7838 with dissolve
    rose "I lost count."
    scene w2_7839 with dissolve
    kat "You two got into it a lot. You fought and fought."
    kat "Once it was even bad enough that your neighbors called the cops, but that wasn't a wake up call for you. I wonder what impression that will leave onto your precious daughter?"
    scene w2_7840 with dissolve
    rose "Please, {b}leave her out of this{/b}."
    scene w2_7841 with dissolve
    kat "You should've left him, Mrs. Carter. I see women like you all the time at the Fund, refusing to help themselves in lieu of playing the victim."
    scene w2_7842 with dissolve
    kat "What kind of example did your lack of self-worth set? What kind of lesson were you teaching your daughter by sticking around with a man who hit you?"
    rose "Stop..."
    scene w2_7843 with dissolve
    kat "Right now, she's young enough that her love is unconditional, but in a couple of years, if you're lucky, she'll resent you. If you're not..."
    kat "Maybe I'll see her in a decade or two if I'm still doing--"
    scene w2_7844 with dissolve
    stop music
    play sound "sound effects/slap2.wav"
    scene w2_7845 with hpunch
    rose "You're going too far!"
    "All the air was sucked out of the room, as the realization of what happened dawned on the slow-witted of us."
    scene w2_7846 with dissolve
    rose "......"
    scene w2_7847 with dissolve
    rose "..."
    scene w2_7848 with dissolve
    rose "I a-apologize!"
    kat "You...!"
    scene w2_7849 with dissolve
    kil "Can't say she didn't fucking deserve that."
    "At the same time, the slap made me unspeakably happy and also deeply concerned."
    scene w2_7850 with dissolve
    kat "You...! You...!"
    rose "I'm sorry, I let my--"
    scene w2_7851 with dissolve
    kat "Don't be!"
    kat "That was the most truthful response I've dragged out of you yet! It makes me so very, VERY happy to see you've got some fire in you!"
    scene w2_7852 with dissolve
    rose "Uh... w-ha...?"
    "Rose looked utterly stupefied by the cruel woman's reaction."
    scene w2_7851 with dissolve
    kat "That was a \"stand up for yourself\" moment, Rose. I'm proud of you."
    scene w2_7853 with dissolve
    kat "C'mon, stand up... I was out of line."
    rose "O-okay... still, I'm sorr--"
    play sound "sound effects/punch.wav"
    scene w2_7854 with vpunch
    rose "G-guh!"
    kat "Who the fuck do you think you are, cow?!"
    play music "music/from-russia-with-love.ogg"
    scene w2_7855 with dissolve
    kat "Do you think I'd let that impudence pass without consequence?!"
    kat "{b}Don't. Get. Up.{/b}"
    rose "I--"
    kat "Lie flat on your back, where you belong."
    scene w2_7856 with dissolve
    rose "Y-yes, Ma'am!"
    kat "Did I hit a nerve earlier?"
    kat "Was anything I said untrue?"
    rose "Y-yes! It was!"
    scene w2_7857 with dissolve
    kat "Good grace, look at these stupid things."
    scene w2_7858 with dissolve
    rose "G'gghh....!"
    kat "This right here is what you are worth!"
    scene w2_7859 with hpunch
    play sound "sound effects/slap3.wav"
    scene w2_7860 with hpunch
    rose "Hhhnngg!"
    kat "You...!"
    play sound "sound effects/slap2.wav"
    scene w2_7861 with hpunch
    play sound "sound effects/slap3.wav"
    scene w2_7860 with hpunch
    kat "You moronic, fat-assed cow. You like getting your udders played with?"
    scene w2_7862 with dissolve
    rose "W-what do you want me to say, bitch?!"
    scene w2_7863 with dissolve
    kat "Oh, bitch, is it? Hmmph!"
    scene w2_7864 with dissolve
    kat "I'd say an escalation of what I had originally planned for tonight is in order."
    scene w2_7865 with dissolve
    "Reaching into her corset, she produced a marker, as if she knew the item would be needed."
    mct "(Did she expect to be smacked...? No way...)"
    scene black with fade
    kat "Off with this~"
    scene w2_7866 with dissolve
    rose "You haven't even told me what you're going to do to me tonight..."
    scene w2_7867 with dissolve
    kat "I'm not going to do anything to you, dear."
    kat "All I want to know is if you're willing to shoot a video?"
    scene w2_7868 with dissolve
    rose "O-of course I am...?"
    scene w2_7869 with dissolve
    kat "Don't be so hasty to agree. It won't quite be like the other times you've been photographed and filmed."
    scene w2_7870 with dissolve
    rose "It doesn't really matter what craziness you throw on top of it... I'm willing."
    scene w2_7871 with dissolve
    kat "Hmm. You've got beautiful eyes, Mrs. Carter."
    kat "The way they're set right now is making me all tingly~"
    scene w2_7872 with dissolve
    rose "...w-what ARE we filming?"
    scene w2_7873 with dissolve
    kat "A porn video, duh~ To be exact... one to be cut and sold to the whole world at large!"
    scene w2_7874 with dissolve
    rose "You're... gonna... sell...?"
    kat "I'm giving you a chance to be a star!"
    scene w2_7875 with dissolve
    rose "You're going to sell it? T-to everyone...? P-publicly?"
    scene w2_7876 with dissolve
    kat "What are you, all tit and no brain? What's so hard to understand about that, cow?"
    scene w2_7875 with dissolve
    rose "I thought all of this was private...!"
    scene w2_7876 with dissolve
    kat "Well.... that's actually all up to you, isn't it? Just how far are you willing to go tonight, Mrs. Carter?"
    scene w2_7877 with dissolve
    kat "Like the other Carnations, you have a choice."
    kat "You can forfeit the night and save yourself from exposing just how much of a whore you are to the world."
    scene w2_7878 with dissolve
    rose "*gulp* I..."
    kat "I mean... after all, there's no guarantee you'll even win tonight if you do it. I'll understand if you give up, you can always make it up over the next two--"
    scene w2_7879 with dissolve
    rose "I'll do it!"
    rose "Let's... make a movie..."
    stop music fadeout 3.0
    scene w2_7880 with dissolve
    kat "You sure? Once it's out there, it's out there. Sure, the chances of anyone recognizing a nobody like you is slim, but..."
    scene w2_7881 with dissolve
    kat "There will be a sword of Damocles above your head for the rest of your life."
    scene w2_7882 with dissolve
    rose "That's a worry for later."
    scene w2_7883 with dissolve
    kat "There you have it, folks. The 8 of you who voted she'd accept win the wager."
    scene w2_7884 with dissolve
    mihir "How could there be any doubt?"
    tom "I expected more prudence..."
    play music "music/i-knew-a-guy.ogg"
    scene w2_7885 with dissolve
    mc "Writing her name on her chest like that is really messed up."
    scene w2_7888 with dissolve
    kil "That's the point. It ups the stakes."
    scene w2_7887 with dissolve
    "Veronica's trial broke her down and Felicia's was arduous. Rosalind's had potential long-reaching ramifications for her career, social life, and that of her child's."
    scene w2_7885 with dissolve
    mc "She isn't getting off light."
    scene w2_7886 with dissolve
    kil "Eh. It's the 21st century. Doing some porn isn't a BIG deal."
    scene w2_7889 with dissolve
    mc "You are SERIOUSLY out of touch, dude. How would you feel if when we were in school, your mom swallowed some baby gravy on camera, and everyone knew about it?"
    scene w2_7890 with dissolve
    kil "Don't make this weird!"
    scene w2_7889 with dissolve
    mc "Like us standing here isn't weird already. Just don't think about your dad's balls resting on your mother's chin and everything will be--"
    scene w2_7891 with dissolve
    mc "C-crap! D-dead arm...!"
    scene w2_7892 with dissolve
    "That was well earned."
    scene w2_7890 with dissolve
    kil "Point taken, fucker."
    scene w2_7893 with dissolve
    kat "You guys bored of my little show?"
    kil "Uh, no Ma'am!"
    mc "Sorry."
    scene w2_7894 with dissolve
    kat "I don't actually care. Just go over and get into position, [mcf]. We're about to start shooting."
    scene w2_7895 with dissolve
    "......"
    "..."
    scene w2_7896 with dissolve
    mc "Oh fuck, of course you would ask me to...!"
    "I was one hundred and ten percent NOT COOL WITH THIS. The \"private\" recordings and pictures were one thing, but this..."
    scene w2_7897 with dissolve
    kil "Ha! Looks like you get to add porn star to your résumé!"
    scene w2_7898 with dissolve
    mc "Mrs. Pulman... I respectfully decline. Surely there's someone else here who's willing to--"
    scene w2_7899 with dissolve
    kat "Good grief, [mcf]. Don't look so mortified."
    kat "You've done worse this week. You rubbed elbows with Elias Ford after stuffing his wife full of egg vibes!"
    scene w2_7900 with dissolve
    mc "I'd rather do that again."
    scene w2_7899 with dissolve
    kat "The video isn't even..."
    scene w2_7901 with dissolve
    mc "Isn't even what?"
    scene w2_7902 with dissolve
    kat "*Sigh* Your face and voice will be digitally obscured. No one gives a damn about the men in these things anyway."
    kat "Now hurry up. Everyone's waiting."
    scene w2_7903 with dissolve
    hide screen textbox2 with dissolve
    show screen mod_week2_expo
    menu w2ExRoseFuck:
        "Well, if your anonymity is secured..."(chg=["kathleen_up2","kathleen_trust_up2"]):
            hide screen mod_week2_expo
            $ Kathleen_Trust += 2
            $ Kathleen_Affection += 2
            scene w2_7904 with dissolve
            show screen textbox2 with dissolve
            mc "You're right."
            "I've done much worse. I'll just have to trust her I'll be unidentifiable."
            scene w2_7905 with dissolve
            mc "Guess I'll add porn star to my résumé."
            kil "Have fun, bro. Fuckin' on camera's great!"
            stop music fadeout 3.0
            scene black with fade
            "..."
            kat "Are we rolling?"
            jump w2ExRosalindHumiliationMC
        "Staunchly refuse to budge."(chg=["kathleen_down"]):

            hide screen mod_week2_expo
            $ Kathleen_Affection -= 1
            scene w2_7906 with dissolve
            show screen textbox2 with dissolve
            mc "I'm just not comfortable with the idea of this."
            scene w2_7907 with dissolve
            kat "*Whispering* You've got to be fucking kidding me. This is where you draw the line?"
            scene w2_7908 with dissolve
            kil "Lay off him. I'll do it!"
            scene w2_7909 with dissolve
            kat "Stay out of this, I'm talking to Mr. [mcl]--"
            scene w2_7908 with dissolve
            kil "He's already done enough crazy shit for you, so cut him some slack. He's going to be a doctor one day."
            scene w2_7910 with dissolve
            kat "..."
            scene w2_7908 with dissolve
            kil "Dick's a dick right? There's two of us and I know how to use mine better anyway."
            scene w2_7910 with dissolve
            hide screen textbox2 with dissolve
            show screen mod_week2_expo
            menu:
                "(w2expts(ros)=+5)Let Ian do it.{vspace=50}"(chg=["kathleen_trust_down2","killian_up3","hana_up2","rosalind_down2"]):
                    hide screen mod_week2_expo
                    $ Kathleen_Trust -=2
                    $ Killian_Bromance += 3
                    $ Hana_Affection += 2
                    $ Rosalind_Affection -= 2
                    $ w2ExPointsRosalind += 5
                    $ w2ExRoseIanSex = True
                    show screen textbox2 with dissolve
                    "There's two of us. Why should I be the one to do everything?"
                    "......"
                    "..."
                    scene w2_7911 with dissolve
                    kat "I'm disappointed, but you've exceeded my expectations up to this point."
                    scene w2_7912 with dissolve
                    kat "Fine. Get into position, Mr. Beaufort."
                    kil "Aye, aye Ma'am!"
                    scene w2_7913 with dissolve
                    mct "(...thanks Ian.)"
                    "He was quick to defend and stick up for me there."
                    mct "(Maybe I shouldn't break his balls, like an asshole, about living in the past so much.)"
                    scene black with fade
                    stop music fadeout 3.0
                    "..."
                    kat "Are we rolling?"
                    jump w2ExRosalindHumiliationIan
                "Reconsider and perform yourself."(chg=["kathleen_up","kathleen_trust_up"]):

                    hide screen mod_week2_expo
                    $ Kathleen_Affection += 1
                    $ Kathleen_Trust += 1

                    scene w2_7914 with dissolve
                    show screen textbox2 with dissolve
                    mc "Thanks Ian, but she's right. I'm being stupid."
                    "I've done much worse. I'll just have to trust her I'll be unidentifiable."
                    scene w2_7915 with dissolve
                    kil "You sure? I don't want you to do anything you're uncomfortable with."
                    scene w2_7916 with dissolve
                    "He was quick to defend and stick up for me there."
                    mct "(Maybe I shouldn't break his balls, like an asshole, about living in the past so much...)"
                    scene w2_7917 with dissolve
                    mc "We're past that. Now it's just a drop in the bucket."
                    scene w2_7918 with dissolve
                    mc "Guess I'll add porn star to my résumé."
                    kil "...s'alright."
                    scene w2_7919 with dissolve
                    kil "{size=10}*Under his breath* I don't like you bending to that bitch...{/size=10}"
                    scene black with fade
                    stop music fadeout 3.0
                    "..."
                    kat "Are we rolling?"
                    jump w2ExRosalindHumiliationMC


        "(w2expts(ros)=+5){color=#FF1493}[[Social Chameleon]{/color} Suggest Ian perform instead.{vspace=50}"(chg=["killian_up2","hana_up2","rosalind_down2"]) if perk_socialChameleon == True:
            hide screen mod_week2_expo
            $ Killian_Bromance += 2
            $ Hana_Affection += 2
            $ Rosalind_Affection -= 2
            $ w2ExPointsRosalind += 5
            $ w2ExRoseIanSex = True
            scene w2_7984 with dissolve
            mc "Ian should do it. Fucking on camera is practically his hobby."
            scene w2_7985 with dissolve
            kat "I'm asking you to do it, [mcf]."
            scene w2_7986 with dissolve
            mc "He'll put on a better show for the patrons. I'll be too anxious."
            mc "Besides, he hasn't been given a chance to do much all night. I think he and Rosalind will have a surprising amount of compatibility."
            scene w2_7987 with dissolve
            kil "What makes you say that?"
            scene w2_7988 with dissolve
            mc "It's just that, well..."
            scene ian_3some_a with pixellate
            show ian_3some
            kil "Don't forget who you work for just because I was nice enough to clean out the cobwebs down there."
            alice "A-ah, y-you used to be s-so...!"
            kil "Sweet? Bullshit. I've always wanted to fuck this fat ass--"
            scene w2_7989 with dissolve
            mc "She's his type."
            kil "What isn't?"
            scene w2_7990 with dissolve
            mc "I've done a good job so far, haven't I?"
            scene w2_7991 with dissolve
            kat "Hmmpfh. Don't get full of yourself."
            scene w2_7992 with dissolve
            kat "Get into position, Mr. Beaufort. Everyone's waiting."
            kil "Yes, Ma'am."
            scene w2_7993 with dissolve
            kat "*Sigh* You really think I would risk anything tracing back to you?"
            mc "I know you wouldn't."
            scene w2_7994 with dissolve
            mc "(...but I'm not taking the chance.)"
            scene black with fade
            stop music fadeout 3.0
            "..."
            kat "Are we rolling?"
            jump w2ExRosalindHumiliationIan

        "{color=#696969}[[Social Chameleon] Suggest Ian perform instead. {/color}" if perk_socialChameleon == False:
            jump w2ExRoseFuck

label w2ExRosalindHumiliationIan:


    play music "music/future-rennaisance.ogg"
    scene w2_7920 with curtains
    aug "We're good to go, Kathy."
    kat "Excellent."
    kat "How old are you Rosalind?"
    $ renpy.music.set_volume(.2, 0, channel = "music")
    scene w2_7921 with dissolve
    aug "When you set the manual focus, you need to zoom in on the subject as tight as you can and..."
    scene w2_7922 with dissolve
    aug "You don't give a crap about any of this, huh?"
    scene w2_7923 with dissolve
    hana "Not really. I hate cameras."
    scene w2_7924 with dissolve
    aug "C'mon, this is the family business!"
    hana "..."
    scene w2_7925 with dissolve
    aug "Ack, that was a dumb thing to say..."
    rose "--to get fucked by young cock."
    scene w2_7926 with dissolve
    aug "[mcf], hey. You like cameras, don't you?"
    scene w2_7927 with dissolve
    mc "I prefer the end result."
    scene w2_7928 with dissolve
    aug "Bah!"
    hana "Speaking of which... why aren't you the one in front of the camera? Isn't your job to do whatever she wants?"
    scene w2_7929 with dissolve
    mc "I refused to do it."
    scene w2_7930 with dissolve
    hana "Ha! Cool shit!"
    mc "I don't think she was happy about it."
    scene w2_7931 with dissolve
    aug "There's more to this place than these shows. She'll get over it."
    $ renpy.music.set_volume(1, 0, channel = "music")
    scene w2_7932 with wipeleft
    "Back on stage, things had finally begun heating up between Rosalind and Ian after a brief exchange of questions and answers."

    if kat_polite == True:
        "The core concept, as directed by Mrs. Pulman, was a younger man roughly and enthusiastically having his way with an older woman. Not exactly a stretch of the imagination."
    else:
        "The core concept, as directed by Kathleen, was a younger man roughly and enthusiastically having his way with an older woman. Not exactly a stretch of the imagination."

    scene w2_7933 with dissolve
    kil "You ready?"
    scene w2_7932 with dissolve
    scene w2_7934 with dissolve
    scene w2_7935 with dissolve
    "Rosalind only nodded and Ian returned her acceptance with a smile, in a brief show of humanity before flipping the script to something more..."
    scene w2_7936 with dissolve
    kil "No shit, you fat-assed hag. Why the FUCK would you be here otherwise?"
    "...typical of this place."
    scene w2_7937 with dissolve
    kil "You want this young dick?"
    rose "Y-yes, please!"
    scene w2_7938 with dissolve
    kil "Please? You're already a step ahead of me, but I want it to be along the lines of \"yes, please\" and \"yes, Daddy\", you got it slut?"
    scene w2_7939 with dissolve
    rose "Yes, D-daddy!"
    scene w2_7938 with dissolve
    kil "Holy hell, that sounds ridiculous coming out of an old woman's mouth. I love it!"
    scene w2_7940 with dissolve
    "Ian was really getting into it..."
    scene w2_7938 with dissolve
    kil "We have a problem, though. I'm not even close to being hard from a dried up bitch like you."
    scene w2_7940 with dissolve
    kil "Take off my underwear."
    scene w2_7941 with dissolve
    rose "Yes, daddy..."
    scene w2_7942 with dissolve
    hana "Disgusting."
    scene w2_7943 with dissolve
    mc "..."
    scene w2_7944 with dissolve
    hana "What a fuckin' ass."
    scene w2_7945 with dissolve

    if kat_polite == True:
        mc "He's just doing what Mrs. Pulman wants. Don't be {i}too{/i} judgmental."
    else:
        mc "He's just doing what Kathleen wants. Don't be {i}too{/i} judgmental."

    scene w2_7946 with dissolve
    hana "{b}Too{/b} judgmental?"
    scene w2_7947 with dissolve
    "Maybe it was the fact he was so quick to stick up for me only just a moment ago or because I would be doing a very similar \"disgusting\" thing if I was up there, but I felt the nascent urge to defend Ian."
    scene w2_7948 with dissolve
    hana "You really think ALL of this is just an act? That he's pulling all this ugly degrading male-fantasy shit out from thin air?"
    scene w2_7945 with dissolve
    mc "Well, no..."
    scene w2_7947 with dissolve
    "She wasn't wrong. I'd seen second hand the way he talked to his maid in that video tape. He, without a doubt, got off on lording over women older than him."
    scene w2_7945 with dissolve
    mc "It is part of the job though. The one you're now a part of."
    scene w2_7946 with dissolve
    hana "Exactly. I'm just saying there's no way a young adult male spends as long as Ian has in this environment without it sucking out all empathy he has for his partners."
    scene w2_7945 with dissolve
    mc "I wouldn't go that far..."
    scene w2_7949 with dissolve
    hana "You're seeing the same shit I am."
    scene w2_7950 with dissolve
    rose "*Chwup, chwup, fwhup...!*"
    kil "Don't neglect the other one, he's getting lonely!"
    scene w2_7951 with dissolve
    rose "Mmmh, mmmhhh..."
    kil "You're a lot prettier with my balls on your face."
    rose "Mmmh, mmhh, thwank yhwooo..."
    scene w2_7952 with dissolve
    kil "Open your mouth."
    rose "O-okay...? Errr y-yes, Daddy!"
    scene w2_7953 with dissolve
    rose "Ah~!"
    stop music
    play sound "sound effects/spit.wav"
    kil "Stupid cow! Ah--"
    scene w2_7954 with vpunch
    "*Speeewt!*"
    scene w2_7955 with dissolve
    kil "I'm still not hard. Try the other end."
    play music "music/hypnosis.ogg"
    scene w2_7956 with cmet
    rose "Mmmpfh...!"
    with vpunch
    "Guiding Rosalind's head, he buried the flustered brunette's face into his anus."
    with vpunch
    kil "Get your fucking tongue in there if you want me to fuck you!"
    scene w2_7957 with dissolve
    rose "Mmmh... mmhh...!"
    kil "Get it nice and wet! Don't miss a fucking inch!"
    scene w2_7958 with pixellate
    cm "Look at her go! You ever see a nastier slut?"
    vic "Mmmpfh...!"
    scene w2_7959 with dissolve
    cm "I mean fuck, that's someone's mother, right! It makes me want to puke!"
    fm "It's like a snake. Holy shit I'm about to--"
    $ renpy.music.set_volume(.2, 0, channel = "music")
    scene w2_7960 with pixellate
    mc "..."
    kil "Aaah, that's it! I'm finally feeling something!"
    scene w2_7961 with dissolve
    hana "Like I said... disgusting, right?"
    scene w2_7962 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Agree with her."(chg=["hana_up"]):
            $ Hana_Affection +=1
            scene w2_7963 with dissolve
            show screen textbox2 with dissolve
            mc "It is, but..."
            scene w2_7964 with dissolve
            mc "*Sigh* Yeah. I am watching my friend's ass get eaten out. It's not a good view."
            scene w2_7965 with dissolve
            hana "Pfft-!"
            mc "Liking what you see?"
            scene w2_7966 with dissolve
            hana "Hell no, but I'm glad!"
            scene w2_7967 with dissolve
            mc "...of what?"
        "You're not any better"(chg=["killian_up"]):

            $ Killian_Bromance +=1
            scene w2_7963 with dissolve
            show screen textbox2 with dissolve
            mc "I don't know if I'm any better..."
            scene w2_7968 with dissolve
            hana "What the hell are you talking about? Of course you are. You didn't approach anything near this when you worked with Felicia."
            scene w2_7969 with dissolve
            "Thank God she can't see inside my skull or what else I did this week..."
            scene w2_7963 with dissolve
            mc "You said it yourself. Given enough time, this environment will warp a guy's mind.."

            if w1RosalindPhoto or w2RosalindPhoto or roseTakeAdvantage == True:
                mct "(And it's not like I haven't treated Rosalind poorly to begin with...)"

            scene w2_7970 with dissolve
            hana "Aw, c'mon... I was... I was just talking out of my usual judgmental ass. You know how I don't get along with Ian."
            scene w2_7971 with dissolve
            mc "Don't back track you fucking dweeb!"
            hana "Ow! Fine! I meant what I said, but you're a lot more self-aware than that jerk. Just don't forget about your partner when you're up there or whatever!"
        "You disagree, but don't say anything."(chg=["hana_down"]):

            $ Hana_Affection -=1
            scene w2_7972 with dissolve
            show screen textbox2 with dissolve
            "I wanted to say she was the one judging this whole damn thing, but I held my tongue."
            scene w2_7973 with dissolve
            "She didn't know Ian like I did. He wasn't irredeemable trash. He had his rough edges and he liked his dirty talk, but so did I."
            scene w2_8019 with pixellate
            if roseFlag == True:
                mct "(And so did Rose for that matter.)"
                scene w2_7974 with pixellate
            else:
                scene w2_7974 with dissolve
            hana "Hey... I'm not accusing you of anything."

    scene w2_7975 with dissolve
    hana "You already showed me you're capable of telling that crazy bitch no. That's something."
    $ renpy.music.set_volume(1, 3, channel = "music")
    scene w2_7976 with dissolve
    mct "(Was it? I just didn't want to be on film...)"
    "While Hana and I flapped our gums, Ian had shoved his half-erect cock partly into Rosalind's maw."
    kil "Hands behind your back!"
    scene w2_7977 with dissolve
    rose "Mmhmyyyeah dwwwaddy!"
    scene w2_7978 with dissolve
    kil "Good slut!"
    "As expected, Rosalind complied beautifully. She was over the hurdle of accepting starring in a porn video, and as she was skilled at, adapted to the flow of things quick."
    rose "Mmmhww--!!"
    "Every inch of Ian's cock disappeared down her throat with nary a gag."
    scene w2_7977 with dissolve
    kil "How's the taste of my dick?"
    rose "Mmmhhhh...!"
    $ renpy.music.set_volume(.5, 0, channel = "ambient")
    scene rose_e2_ianbj1_a with dissolve
    show rose_e2_ianbj1
    hide screen textbox2 with dissolve
    play ambient "sound effects/fel2.wav"
    kil "Oh, just shut the fuck up you walking cock holster! I was talking to myself!"
    rose "Gluuuhk! Ghuk...! Guhk...!"
    "With no regard for the MILF's cock-stuffed mouth, he began the oral onslaught, shoving his thick dick in-and-out with a frenetic fervor."
    kil "Ha, d-dirty bitch!"
    rose "Glug! glug...!! Ghlug!!!!"
    mct "(Yeah, {b}Ian was fucking into it{/b} - and why wouldn't he be?)"
    "Rosalind was beautiful and he was getting paid to dominate her. He controlled her neck and hammered in with such tonsil-bashing force that I was quite frankly as impressed as I was concerned."
    rose "Mmmh, ggghhu, ghuk, glug...!"
    tom "Holy...!"
    $ renpy.music.set_volume(1, 3, channel = "ambient")
    scene rose_e2_ianbj2_a with dissolve
    show rose_e2_ianbj2
    "Apart from the odd whisper, everyone watched Ian's furious display with unabated interest. Rosalind would bend, but she wouldn't break."
    kat "She holds up well, doesn't she?"
    rose "Ghk! Ghuk! Ghhhuuuchk!"
    "Muted whispers, the odd observation, AND the increasingly sloppy sound of Ian's flesh missile battering the oral mucosa of Rosalind's mouth."
    rose "G-guh, ggh-ghhaaa...!"
    "Every half-second or so, Ian's balls would plop against the mother's chin, splattering the spit that his dick displaced from her mouth in a frothy drizzle."
    kil "You're taking it well. Good girl, good dirty fucking, ha...!"
    rose "Thwhnnkkyyuouuu...!"
    $ renpy.music.set_volume(.5, 3, channel = "music")
    $ renpy.music.set_volume(.2, 0, channel = "ambient")
    scene w2_7979 with dissolve
    hana "Yeesh. I gag the moment anything weird touches the back of my throat."
    scene w2_7980 with dissolve
    mc "She's improved from earlier this week..."
    scene w2_7981 with dissolve
    mct "(Well, she is working with a smaller package...)"
    hana "Eh...? Why are you looking so smug?"
    scene w2_7982 with dissolve
    mc "Oh, uh... nothing."
    scene w2_7983 with dissolve
    hana "Nothing, eh?"
    $ renpy.music.set_volume(1, 3, channel = "music")
    $ renpy.music.set_volume(1, 2, channel = "ambient")
    scene rose_e2_ianbj3_a with dissolve
    show rose_e2_ianbj3
    play ambient "sound effects/fel1.wav"
    "By this point, Rosalind's face was a mess. Spittle covered her chin and mascara streaked down her face like lightning."
    rose "Ghk, gluhg, ghhuuuk-!!!*"
    "Incongruous with her appearance, Rosalind looked up at my redheaded friend with an unwavering expression."
    kil "Oh? Nasty slut! That face...!"
    rose "Mm, ghuuuk, mmmhhh...!"
    kil "It suits you!"
    rose "Guuhuhh....! Mmmh...! Ghhhuuuk...!"
    kil " You love getting throat-fucked on camera, don't you?"
    rose "Mmmh, mmmhhh... gluhgg...!"
    kil "Good! This is what an old cow like you is best suited for~"
    rose "Ghk, gluhg, ghuuut...!"
    kil "Scarfing down dicks of a young bull~"
    rose "Ghuk, ghlluuk, ghhhuuff...!"
    "Ian gleefully prattled on, intoxicated on his own words, with Rosalind answering each jeer in kind with the sound of getting her face plugged."
    rose "Ghhuk gghhkk...!"
    "Each squelch, pop, and plap formed together in a beautiful melody, and like a conductor leading an orchestra, one kept in time by the tip of my friend's dick."
    rose "Ghu, hhuhuuk...!"
    "The lewd, lusty noises would be enough to stoke the devilish side of me, but watching the sense get slowly face-fucked out of her was truly the best."
    $ renpy.music.set_volume(.5, 2, channel = "ambient")
    scene rose_e2_ianbj4_a with dissolve
    show rose_e2_ianbj4
    "Half deprived of oxygen, Rosalind was slowly getting drunk on dick. That unwavering expression had dithered."
    aug "What a trooper!"
    kat "Is that your professional opinion, August?"
    rose "Guh, glug, gluhh....!"
    tom "Wow...!"
    "Thrust after thrust, she was having my friend's cock gradually seared into her memory."
    "Her eyes clouded over, consumed by the all-encompassing presence of Ian's cock. Her throat, no doubt scratchy and sore from the act, had been completely rendered a sex toy."
    rose "Ghuk, gluhh... hhheeugh...!"
    "There was simply no advantage to have any other thoughts in her head."
    "For minutes all she tasted, breathed, and smelled was dick."
    rose "Ghuk, gluhk, guuuh...!"
    "For minutes, her entire purpose was devoted to satisfying the lust of not a specific person, but a cock. No matter whose it was."
    rose "Gluh, ghhuk, guhh...!"
    "Minutes until..."
    kil "Ah...! Fuck...! R-rosie...!"
    stop ambient
    scene w2_7995 with vpunch
    rose "Mmmh...!!!"
    "...my friend cried out in a way that could be mistaken as affectionate, stoutly holding Rosalind's face to his groin, and presumably unloading a stream of fat sticky jizz down her throat."
    stop music
    play sound "sound effects/spurt.wav"
    with flash
    kil "Swallow it all!!"
    play sound "sound effects/spurt.wav"
    with flash
    $ renpy.music.set_volume(1, 0, channel = "ambient")
    play ambient "sound effects/gulp.wav"
    rose "Guhhk, ghuhhk, ghuhh...!"
    scene rose_e2_ianbj5_a with dissolve
    show rose_e2_ianbj5
    kil "Swallow every fucking drop!"
    "And having fully embraced the role of a prostitute, she patiently waited for every last bit of semen to be ejected from my friend's expanding cum slit."
    rose "Mmmh.. mmhhh..."
    kil "Ha... haa...."
    stop ambient
    scene w2_7996 with dissolve
    kil "Holy shit... ha... good work... ha..."
    rose "Ha... w-hwah..."
    scene w2_7997 with dissolve
    rose "Thank you for the yummy dick juice, Daddy."
    scene w2_7998 with dissolve
    kil "You--!"
    scene w2_7999 with dissolve
    "She ensnared him with a bold declaration, as deftly spoken as it would sound coming from a practiced tongue like Felicia's."
    scene w2_8000 with dissolve
    rose "Kyeaaaah!"
    kil "Don't think we're finished yet!"
    $ renpy.music.set_volume(.5, 0, channel = "music")
    play music "music/thunder.ogg"
    scene w2_8001 with dissolve
    hana "How the hell can you say something like that with a straight face?"
    scene w2_8002 with dissolve
    mc "She needs money."
    scene w2_8003 with dissolve
    hana "I mean yeah, but... it sounded so..."
    scene w2_8004 with dissolve
    mc "Lewd?"
    scene w2_8005 with dissolve
    hana "God no! I mean, I'm surprised she didn't die from cringe."
    hana "Honestly, I'm impressed. All three of them are on another level..."
    scene w2_8006 with dissolve
    "Hana stood strangely in awe of Rosalind. So did I for that matter, but it was for a vastly different reason."
    scene w2_8007 with dissolve
    hana "...what? Did {i}you{/i} think that dick juice and Daddy shit was hot?"
    mc "I take the fifth."
    scene w2_8008 with dissolve
    hana "Pfft-!"
    "It occurred to me it was nice being on the side lines with Hana rather than up there."
    scene w2_8009 with dissolve
    hana "I don't get it."
    scene w2_8010 with dissolve
    rose "Ehh, hhaaa... haaa...!"
    $ renpy.music.set_volume(.5, 0, channel = "ambient")
    $ renpy.music.set_volume(1, 2, channel = "music")
    scene rose_e2_ianf1_a with dissolve
    show rose_e2_ianf1
    play ambient "sound effects/fap.wav"
    "Moving my attention back to the stage, Ian had already begun the task of fucking Rosalind stupid."
    kil "There you go, bitch!"
    mct "(...or perhaps it's the other way around?)"
    kil "Move your hips!"
    "The pair shared in a vigorously impressive carnal embrace, Ian generating the power to bounce Rosalind off of his lap and push her back down with his hand."
    rose "Eh, y-yes...! I a-am...?!"
    "Rosalind, as best she could, followed suit using the muscles in her back to give her fat ass that extra bounce whenever she made contact with my friend's thighs."
    kil "Just yes...? What did I say?"
    rose "Ah, I m-mean... D-daddy! D-daddy!"
    kil "That's right!"
    rose "Nnyeeee...!"
    kil "I fucking own you right now!"
    "Ian plowed the plump MILF without restraint. There was no build up to any of this, his glans simply barreled through Rose's slick folds, stabbing deep inside her and prying out reluctantly sweet cries."
    $ renpy.music.set_volume(1, 1, channel = "ambient")
    scene rose_e2_ianf2_a with dissolve
    show rose_e2_ianf2
    rose "Haa, ha...! Y-you think?!"
    "That wasn't to say Rosalind wasn't meeting my friend half way. Her insides handily swallowed every inch of cock that it was fed, massaging and driving Ian's lust and pulling them both deeper into an endless cycle of rutting depravity."
    rose "Y-you're a s-spoiled brat!"
    "It seemed she was tired of Ian's voice, and in a moment of cute frustration, wanted to flip the script."
    kil "Ah, w-what...? What do... ah..."
    rose "A-anyone, ha...! Anyone ever t-tell you that...?"
    kil "A-as a matter of fact..."
    mct "(What the hell?)"
    "My friend seemed momentarily caught off guard and flustered."
    kil "You're not the first hag to mention it!"
    $ renpy.music.set_volume(1, .5, channel = "ambient")
    scene rose_e2_ianf3_a with dissolve
    show rose_e2_ianf3
    play sound "sound effects/boobjob.wav"
    rose "Nhoooohh! Oh! Gh...!"
    "The challenge energized Ian, and he gripped the mother in his arms tighter and pushed harder."
    "*Plop, plahp, plap...!*"
    kil "What's so wrong with getting what I want?!"
    rose "Hnng, haa...! Ghhuk...!"
    kil "Everyone would if they could~"
    rose "Ah, heeee...! W-what...?!"
    "Rosalind's moans turned into a honeyed cry of surprise."
    kil "Oh...? Did I find your G-spot? Finally~"
    rose "Ghh... so....!"
    kil "This kinda angle never fails to turn bitches into putty!"
    rose "Fhhh....! Tchk...!"
    kil "You may have 15 years on me, but in my hands you're just a woman!"
    $ renpy.music.set_volume(.2, 1, channel = "ambient")
    $ renpy.music.set_volume(.5, 1, channel = "music")
    scene w2_8011 with dissolve
    mc "......"
    hana "..."
    scene w2_8012 with dissolve
    mc "In my hands..."
    hana "Stop!"
    scene w2_8013 with dissolve
    rose "Gyyeeeeeeh....!"
    scene w2_8014 with dissolve
    frank "Beautiful!"
    rose "Hnng, haa... ha...!"
    mihir "She's cracking."
    $ renpy.music.set_volume(.5, 1, channel = "ambient")
    $ renpy.music.set_volume(1, 1, channel = "music")
    scene rose_e2_ianf3_a with dissolve
    show rose_e2_ianf3
    rose "Hy, hhng... hnghh...!"
    "As much as we were eye-rolling at his line, Ian did indeed find the angle of attack that completely mollified his partner."
    aug "She's a natural on camera."
    "And that attack didn't stop, it would carry on in a surreal fashion as the room made casual remarks."
    kat "Yet another professional opinion?"
    "It would carry on, endlessly poking and prodding her most sensitive spot, until my friend blew his load in the MILF."
    $ renpy.music.set_volume(1, 1, channel = "ambient")
    scene rose_e2_ianf4_a with dissolve
    show rose_e2_ianf4
    rose "Haa, hngg, haanng...!"
    "It carried on..."
    rose "Sh, shhk..."
    "...turning Rosalind's face into a beautiful contorted mess."
    rose "Hnngh... hnggg...!"
    "This was actually only my second time seeing him fuck. The first, with Lucy, didn't exactly give him a chance to show off his skills."
    kil "Don't stop shaking your hips just yet!"
    "I was fairly impressed. To think this was the same dork I used to play video games with."

    if Killian_Bromance >= 20:
        "I fought back the instinct to give my bro a pat on the back."
        "...this wasn't the time or place after all."
    else:
        mct "(Hmmpfh. I could do better.)"

    rose "Hng, haa...!"
    "Rosalind's fucking carried on while I had those sorts of silly thoughts. Thoughts to be interrupted by..."
    kil "Shit, I'm almost..."
    stop ambient
    scene w2_8015 with dissolve
    "Clumsily, Ian escaped Rosalind's embrace and..."
    kil "Get ready, I'm...!"
    stop music
    play sound "sound effects/spurt.wav"
    scene w2_8016 with flash
    kil "Gah!"
    "Shots of hot white streaks spewed into the air, only to have it rain back down on the both of them."
    rose "Gahh, hgga... w-wha...?"
    scene w2_8017 with dissolve
    "He was a good choice for this, I'd give him that. Mindful of the camera, he knew not to waste the money shot, instead coating Rosalind's tummy and tits for all the world to enjoy."
    "......"
    "..."
    scene w2_8018 with dissolve
    kil "Ummm, you alright, Rosie?"
    rose "Ha... ha... ha..."
    kil "I know that was a bit rough..."
    scene black with fade
    if not persistent.roseW2Shame:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.roseW2Shame = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    "With almost schizophrenic words of deference, Rosalind's porno came to a close, and so did Week 2's exhibition."
    "......"
    "..."
    $ renpy.end_replay()
    jump w2ExWinner


label w2ExRosalindHumiliationMC:

    scene w2_8020 with curtains
    aug "We're good to go, Kathy."
    kat "Excellent."
    kat "How old are you Rosalind?"
    play music "music/as-i-figure.ogg"
    scene w2_8021 with dissolve
    rose "I'm... thirty-six."
    scene w2_8022 with dissolve
    mct "(Ugh.)"
    kat "Is this the first time you've shot a porno?"
    scene w2_8021 with dissolve
    rose "Y-yes, it is."
    scene w2_8022 with dissolve
    mct "(I think I'd prefer just being naked right now...)"
    scene w2_8023 with dissolve
    "At least she's getting a laugh out of it..."
    kat "Thirty-six is quite old to be doing this the first time."
    scene w2_8024 with dissolve
    mct "(Uh huh... pole out would've definitely been preferred.)"
    kat "What makes a married woman your age suddenly want to do something like this?"
    scene w2_8025 with dissolve
    rose "What makes...? Uh..."
    scene w2_8026 with dissolve
    kat "Is your husband unable to satisfy you?"
    "Like God talking down from up high, so distanced from our little world of stage lighting and the camera's viewfinder, the old woman still got her petty jabs in."
    scene w2_8027 with dissolve
    rose "I... {b}I suppose...{/b}."
    rose "Uh... well..."
    scene w2_8028 with dissolve
    rose "No, he wasn't! He had a pitiful... {i}unit.{/i}"
    scene w2_8029 with dissolve
    kat "How cute. Do you not like saying the word dick or cock?"
    scene w2_8025 with dissolve
    rose "No. He... he didn't know how to use his dick. He only cared about himself."
    scene w2_8026 with dissolve
    kat "You're just saying that for the camera, aren't you?"
    scene w2_8030 with dissolve
    rose "...believe what you like."
    scene w2_8031 with dissolve
    kat "Well, lucky for you, today we have a big cock for you to try, that also just so happens to have a nice young man attached to it."
    kat "Say hello you two."
    scene w2_8032 with dissolve

    if kat_polite == True:
        "The scenario, as Mrs. Pulman explained to us in the interim, was a young guy roughly and enthusiastically having his way with an older woman."
    else:
        "The scenario, as Kathleen explained to us in the interim, was a young guy roughly and enthusiastically having his way with an older woman."

    scene w2_8033 with dissolve
    hide screen textbox2 with dissolve
    "A curious emphasis, but..."
    show screen mod_week2_expo
    menu:
        "Say hello.":
            hide screen mod_week2_expo
            $ w2ExRoseDialogue = "A"
            scene w2_8034 with dissolve
            mc "Hello."
            scene w2_8035 with dissolve
            rose "H-hey."
            scene w2_8033 with dissolve
            "Yep. It was weird pretending like we didn't know each other, but I can play the role of a porn actor I guess."
            scene w2_8034 with dissolve
            mc "I look forward to working with you."
            scene w2_8035 with dissolve
            rose "Likewise..."
        "(w2expts(ros)=+1)Greet the MILF enthusiastically.{vspace=50}":

            hide screen mod_week2_expo
            $ w2ExPointsRosalind +=1
            $ w2ExRoseDialogue = "B"
            scene w2_8036 with dissolve
            mc "Hello, Ma'am! It's nice to meet you."
            scene w2_8037 with dissolve
            rose "Um... likewise. H-hello!"
            "It was weird pretending like we didn't know each other, but even if it was make believe, I should be pleasant about it."
            scene w2_8036 with dissolve
            mc "I look forward to fucking you."
            "Plus, saying shit like that with a chipper tone and a straight face was kind of wild."
            scene w2_8037 with dissolve
            rose "Heh... yeah, um... me too."

    scene w2_8038 with dissolve
    kat "Good, now you two know each other. Are you excited to be here, Rosalind?"
    scene w2_8039 with dissolve
    rose "I'm a little nervous..."
    scene w2_8038 with dissolve
    kat "That's understandable. Are you looking forward to what's to come?"
    scene w2_8039 with dissolve
    rose "Yes. I'm here to fuck."
    scene w2_8038 with dissolve
    kat "That's great to hear. One last question, before we begin. What's your favorite thing in the world?"
    scene w2_8040 with dissolve
    rose "Heh, that's easy..."
    rose "I love to get fucked by young cock."
    scene w2_8041 with dissolve
    kat "That's great. You like big ones, right?"
    scene w2_8042 with dissolve
    rose "What do you think?"
    scene w2_8041 with dissolve
    kat "I think you're just saying that for the camera again."
    scene w2_8042 with dissolve
    rose "Believe what you like."
    scene w2_8043 with dissolve
    kat "Ha! You two have fun and just do what comes natural."
    "That was our signal to begin, but..."
    mct "(...natural? What a joke.)"
    scene w2_8044 with dissolve
    "Rosalind looked up at me, a mix of anxiousness and expectation. Even still, she was beautiful."
    "How would I play this?"
    show screen mod_week2_expo
    menu:
        "(w2expts(ros)=+1)Take it slow and encourage Rosalind to take some initiative.{vspace=50}"(chg=["rosalind_passion_up"]):
            hide screen mod_week2_expo
            $ w2ExPointsRosalind +=1
            $ Rosalind_Libido += 1

            "I didn't want to throw her down and rut - at least, not yet."

            if w2ExRoseDialogue == "A":
                scene w2_8045 with dissolve
                mc "Stand up, Rose. Let the camera get a better look at you."
                rose "A-ah..."
                scene w2_8046 with dissolve
                rose "Alright. How's this?"

            if w2ExRoseDialogue == "B":
                scene w2_8047 with dissolve
                mc "Please stand up, Ma'am."
                rose "A-ah..."
                scene w2_8048 with dissolve
                rose "You don't have to call me ma'am."

            scene w2_8049 with dissolve
            mc "Come closer."
            "Doing what I wanted, I pulled the nervous ball of energy into me."

            if w2ExRoseDialogue == "A":
                mc "That's better. You feel nice."
                scene w2_8050 with dissolve
                rose "Umm, you too...?"
            if w2ExRoseDialogue == "B":
                mc "That's better. You're very warm, Ma'am."
                scene w2_8050 with dissolve
                rose "I told you not to..."

            scene w2_8049 with dissolve
            mc "I don't want to be the one who does everything."
            scene w2_8051 with dissolve
            mc "Touch me.."
            scene w2_8052 with dissolve
            rose "I... {b}okay{/b}."
            scene w2_8053 with dissolve
            "Rosalind started with my chest, running her delicately thin fingers across my sternum and resting her hand on my breast."
            scene w2_8054 with dissolve
            mc "You can go lower."
            scene w2_8055 with dissolve
            rose "I know. Don't rush me..."
            scene w2_8056 with dissolve
            "She caught on quick to the pace I was going for."
            scene w2_8057 with dissolve
            rose "You're... firm."
            scene w2_8058 with dissolve
            mc "The benefit of being young, I guess."
            scene w2_8059 with dissolve
            rose "{b}This{/b}... this isn't as hard. It's big, but..."
            scene w2_8060 with dissolve
            rose "It's not nearly as hard as it should be..."
            scene w2_8061 with dissolve
            "She gave me, as best as she could muster, a sultry look while gently cupping and kneading my tightly packaged equipment. The unpracticed, but earnest attempt made the expression as effective as a seasoned whore's."
            scene w2_8060 with dissolve
            rose "...I should do something about that, right?"
            scene rose_e2_kiss_a with dissolve
            show rose_e2_kiss
            rose "Mmmhh..."
            "In place of an answer, I planted a kiss on Rosalind's conspicuously lonely lips."
            "The fledgling porn star didn't shy away from the gesture, instead prying my lips open with her tongue and pulling me deeper into our embrace."
            "*Chwup, fwup, chwup...!"
            "Under the hot lights of the exhibition stage it might've seemed long, but we only spent a brief moment in each other's grasp."
            scene w2_8062 with dissolve
            mc "Ha, ha...."
            rose "Heh... you..."
            scene w2_8063 with dissolve
            rose "I think I felt you stiffen up a little."
            mc "It was just a twitch."
            scene w2_8064 with dissolve
            rose "I think I need to take a closer look."
            scene w2_8065 with dissolve
            "Under the right circumstances, Rosalind could be bold. Our time spent in the park this week, her striking Mrs. Pulman, our bout of make believe in this very moment..."
            "I started to wonder if the meek and stuttering perception I held of her was an illusion cooked up in my head."
            scene w1_0004 with pixellate
            cm "That's great. You like big ones, right?"
            vic "Yes, I love {b}huge{/b} cock."

            if kat_polite == True:
                mct "(Did Mrs. Pulman...)"
            else:
                mct "(Did Kathleen...)"

            scene w2_8066 with dissolve
            rose "You're bigger than my husband."
            scene w2_8067 with dissolve
            mc "Ah, uh... what?"
            scene w2_8068 with dissolve
            rose "I said..."
            "She gave a curious glance in the direction of the crowd."
            scene w2_8069 with dissolve
            rose "You're bigger than my husband."
            scene w2_8070 with dissolve
            mc "This isn't your first time see-- ah."
            mct "(Right.)"

            if w2ExRoseDialogue == "A":
                mc "That's not a very nice thing to say..."
            if w2ExRoseDialogue == "B":
                mc "What a cruel thing to say, Ma'am."

            scene w2_8071 with dissolve
            rose "Aaaaah... I..."
            scene w2_8072 with dissolve
            "The MILF brought her face to my ballsack and took a deep whiff."
            scene w2_8071 with dissolve
            rose "I don't care."
            scene w2_8073 with dissolve
            "Daringly, she began layering tiny kisses down the length of my gradually stiffening cock."
            scene w2_8074 with dissolve
            "*Chwup...!*"
            scene w2_8075 with dissolve
            "All the way down to my scrotum."
            scene w2_8076 with dissolve
            rose "You can grow harder than this, right?"
            scene w2_8077 with dissolve
            "In one swift motion..."
            scene w2_8078 with dissolve
            rose "*Cough* Ghk...!"
            "...she buried my length in the warm, velvety cradle of her mouth. It felt {b}good{/b}."
            scene w2_8079 with dissolve
            mc "A-h-hah..."
            "Amazingly good. She didn't move her head, she simply held my cock in place and gently massaged it's underside with her tongue. All the while..."
            scene w2_8078 with dissolve
            "She never once broke eye contact, looking up at me with a set of baby blues that would've been enough to finish the job by it self."
            "I was hard."
            scene w2_8080 with dissolve
            "I was super fucking hard."
            scene w2_8081 with dissolve
            rose "I want another taste..."
            scene w2_8082 with dissolve
            mc "Wait."
            "She looked at me calmly, waiting for me to proceed."
            mc "I..."
            if w2ExRoseDialogue == "A":
                mc "Let's both have fun. Stand up."
            if w2ExRoseDialogue == "B":
                mc "Let's both enjoy this, Ma'am. Stand up, please."

            scene black with fade
            rose "Alright..."
            jump w2ExRoseSixtyNine
        "(w2expts(ros)=+2)Take charge. Get creative.{vspace=50}"(chg=["rosalind_down","kathleen_up","kathleen_trust_up","hana_down"]):


            hide screen mod_week2_expo
            $ w2ExPointsRosalind += 2
            $ Rosalind_Affection -=1
            $ Kathleen_Affection +=1
            $ Kathleen_Trust += 1
            $ Hana_Affection -=1
            "The scenario the old woman laid out was pretty clear. She wanted me to play the role of an ingrate."
            scene w2_8083 with dissolve

            if w2ExRoseDialogue == "A":
                mc "Spread your legs."
                scene w2_8084 with dissolve
                "She snapped to it immediately, doing as I asked, as if responding to a well-practiced drill."
                scene w2_8085 with dissolve
                mc "You look..."
                "Even with her tacky costume and garish body writing, Rosalind's familiar countenance filled me with an ineffable mixture of warmheartedness and gloom."
                mc "...pretty silly in that."
            if w2ExRoseDialogue == "B":
                mc "Would you please spread your legs, Ma'am?"
                scene w2_8084 with dissolve
                "She snapped to it immediately, doing as I asked, as if responding to a well-practiced drill."
                scene w2_8085 with dissolve
                mc "That costume..."
                "Even with her tacky costume and garish body writing, Rosalind's familiar countenance filled me with an ineffable mixture of warmheartedness and gloom."
                mc "...is pretty ridiculous for a mother to be wearing, don't you agree?"

            scene w2_8086 with dissolve
            rose "Heh... it's not like I picked it or anything..."
            scene w2_8087 with dissolve
            rose "So.. uh... should I...?"
            scene w2_8088 with dissolve
            mc "I don't think so. Not yet."
            scene w2_8089 with dissolve
            mc "Instead, let's make this interesting. Let's turn this into a challenge."
            rose "What ever happened to just.."
            scene w2_8090 with fade
            rose "Ah... to just... screwing..."
            scene w2_8091 with dissolve
            mc "We will, but first things first!"

            if w2ExRoseDialogue == "A":
                mc "I want to see if you can get me hard without even touching me."
            if w2ExRoseDialogue == "B":
                mc "You think you're able to get me hard without laying a finger on me?"

            scene w2_8092 with dissolve
            rose "Without touching you? How could I possibly...?"
            scene w2_8093 with dissolve
            mc "Think about it. Use your head."
            rose "I... um..."
            scene w2_8094 with dissolve
            mc "You've got sex appeal. Don't underestimate it."
            scene w2_8095 with dissolve
            rose "Mmmh...?"
            mc "You're a young man's dream, you know?"
            scene w2_8096 with dissolve
            mc "A giant set of tits, a fat ass, a face of an angel, and soft in all the right ways."

            if w2ExRoseDialogue == "A":
                mc "You're gorgeous. Don't think I, or the viewers at home, don't see or appreciate that"
            if w2ExRoseDialogue == "B":
                mc "You're hot as hell, Ma'am. Don't think I, or the viewers at home, don't see or appreciate that."

            scene w2_8097 with dissolve
            mc "You're truly..."
            mct "(Shit!)"
            scene w2_8098 with dissolve
            "She was such a natural, I felt my cock stiffen from just Rosalind's lustful expression."
            mct "(That would've defeated the whole purpose of this dumbass challenge.)"
            scene w2_8099 with dissolve
            mc "You get the picture?"
            "This was as much for the crowd's benefit as it was my own perverted inclinations."
            scene w2_8100 with dissolve
            rose "I... {b}do{/b}."
            scene w2_8101 with dissolve
            rose "Something like this...? Or..."
            scene w2_8102 with dissolve
            rose "This?"
            "She roughly squeezed her breast, letting the volume tantalizingly spill through her fingers. All the while, she didn't blink. Her focus was entirely on my expression."
            scene w2_8103 with dissolve
            rose "Ah... ng, m-master...?"
            "......"
            "..."
            scene w2_8104 with dissolve
            rose "No...?"
            "Two weeks ago, I would've been rock hard, but not now. A little touching and exaggerated lip-service wouldn't do it."
            scene w2_8103 with dissolve
            rose "Don't you love my fat tits...? If that's not doing it, how about..."
            scene w2_8105 with dissolve
            rose "Hnngh... look at my pussy, sir."
            rose "See how pink it is? Can you even believe I gave birth?"
            scene w2_8106 with dissolve
            rose "Watch me spread and play with it... don't you think you'd be a good fit?"
            rose "You'd be a very good fit. You'd feel {b}so amazing{/b} inside me."
            "......"
            scene w2_8107 with dissolve
            "..."
            "Nothing."
            scene w2_8108 with dissolve
            rose "Heh... then... I know what you like..."
            scene w2_8109 with dissolve
            rose "Hhhg...! L-look!"
            scene w2_8110 with dissolve
            "To my surprise, Rosalind slowly applied pressure to her neck, her lower hand persisting in jilling herself off."
            rose "Gh, hhkk...! "
            scene w2_8111 with dissolve
            "Still, her brilliant eyes were locked on mine, and I was consumed by the way they fluttered while she choked herself."
            rose "T-this... this is more your thing right? Haa... hhngng..."
            scene w2_8112 with dissolve
            rose "This..."
            scene w2_8113 with dissolve
            scene w2_8114 with dissolve
            rose "This is what you love? Hnng...!"

            if w2RosalindPhoto == True:
                mct "(She did know what I liked...)"
                "I had revealed as much earlier in the parking lot, and in this moment, she was using it against me."
            else:
                "She saw right through me, making her dirty talk feel more like an accusation."

            scene w2_8110 with dissolve
            mc "You..."
            rose "I'm just a dumb cow... hngg... dumb, but sturdy..."
            scene w2_8111 with dissolve
            rose "I can take a lot you know. Anything you want to dish out. I'm yours...! Hnng...!"
            rose "You want to choke me, sir? You want to spank me...? You..."
            scene w2_8115 with dissolve
            rose "Hmpfh."
            scene w2_8116 with dissolve
            rose "Well... heh... it's bigger than my husband's."
            scene w2_8117 with dissolve
            "She got me. I was really fucking hard."
            "In a way, she exposed me more than she had herself."
            scene w2_8118 with dissolve
            rose "Can I touch it now? Please?"
            scene w2_8119 with dissolve
            "She looked at me daringly, waiting for me to proceed."
            if w2ExRoseDialogue == "A":
                mc "Sure, but I got an idea. Move over some."
            if w2ExRoseDialogue == "B":
                mc "Sure, but let's both enjoy this, Ma'am. Move over, please."
            scene black with fade
            rose "Alright..."
            jump w2ExRoseSixtyNine


label w2ExRoseSixtyNine:

    stop music fadeout 3.0
    rose "Umm, like this?"
    mc "Move your legs over... ah, there! Like that!"
    scene w2_8120 with fade
    "Taking position on the couch, Rosalind laid opposite of me, placing both our junks square in each other's face."
    mc "I've never tried this position before."
    play music "music/six-days-of-heat-pt2.ogg"
    scene w2_8121 with dissolve
    rose "Me either... there's a first time for everything."
    scene w2_8122 with dissolve
    "...and sometimes that first time is in front of a dozen rich perverts, all caught on camera. {i}I'm sure I'll cherish this memory for the rest of my life{/i}."
    scene w2_8121 with dissolve
    rose "Should I suck it--"
    scene w2_8123 with dissolve
    rose "O-oh...!"
    "Getting a jump start on my parallel partner, I seized the first taste, lapping at her labia and pushing into her sex with a folded tongue."
    scene w2_8124 with dissolve
    rose "{size=10}That tickles...{/siz=10}"
    "For a moment, she just held my dick inert in her hand, her balmy breath beating against my boys, while I acclimated to the topsy-turvy angle of attack."
    scene w2_8123 with dissolve
    rose "That feels nice..."
    "Perhaps, but her juices weren't quite flowing, not yet. They would be though."
    scene w2_8124 with dissolve
    rose "It's going to be hard to focus on my job with you doing that, but..."
    "I had grown confident in my skills over these past couple of weeks."
    scene w2_8121 with dissolve
    rose "...I'll do my best."
    scene w2_8125 with dissolve
    rose "Ahssp--!"
    "The MILF coated my equipment with a generous application of spit, a preamble to things to come."
    scene w2_8126 with dissolve
    rose "Excuse me..."
    scene w2_8127 with dissolve
    "At last, my toes curled as I felt the ever growingly familiar sensation of a woman's mouth enveloping my junk."
    "She momentarily just held it there, lightly tugging at my shaft with her hand and lathering it with the makeshift lube."
    scene rose_e2_69a_a with dissolve
    show rose_e2_69a
    "I focused on my end, trying my best not to be distracted by what the beautiful woman on top of me was doing, but she quickly made that more difficult by finally setting on her own task."
    mc "Mmmhah...!"
    "A small, involuntary groan escaped my pussy-covered mouth."
    mct "(That feels {b}nice{/b}.)"
    "She was only blowing about a third of my shaft, but her hand deftly covered the remaining length."
    mct "(Really nice!)"
    scene rose_e2_69b_a with dissolve
    show rose_e2_69b
    "The feeling of her fingers' tight grip chasing the tail end of her fellatio added a pleasurable distinction to the act, making it feel more akin to sex than simple fellatio."
    mc "Mmh...!"
    "Unable to express as much with my words, I let my hips do the talking, ever-so-gently wagging them on instinct."
    "*Schlup, chwup...!*"
    mct "(Hng, that's right. Suck it!)"
    "...and with my mouth preoccupied, I could only voice that sentiment with my tongue, intensifying my efforts to pleasure the whore mother."
    rose "Mmmh, mmh!"
    "That was the satisfaction to be found in mutual gratification. Not unlike sex, we both spurred each other on in an increasingly lewd feedback loop of oral sex."
    rose "Hmm, mhhh...!"
    mct "(Oh, crap...)"
    "The way the big-tittied MILF's vocal chords pleasurably hummed as she sucked my dick had me bewitched."
    mc "Mmhhaaa...!"
    scene rose_e2_69c_a with dissolve
    show rose_e2_69c
    "{b}*~plop!*{/b}"
    rose "You're really good at that, baby. I'm feeling..."
    "As she spoke, she jacked me off more furiously, the sudden change of pace in combination with the hushed dulcet tone of her words almost making me cum on the spot."
    rose "I'm feeling {b}amazing{/b}."
    "She didn't need to tell me that. By now, her sticky secretions were rolling down my throat and her passage was welcoming me with open arms."
    rose "Mmmh...!"
    "She needily pressed her groin tighter to my face, as if highlighting her urge."
    rose "I love it~ keep it up, p-please...!"
    "If this was a performance for the crowd's sake, it was a good one."
    rose "Please keep tongue fucking me....!"
    "The unusually lewd and boisterously out of character expression was unbelievably hot and encouraged me {b}to do just that{/b}."
    rose "Ha, hhaa... y-yes... p-please..."
    scene rose_e2_69a_a with dissolve
    show rose_e2_69a
    "*Schlup, chwup...!*"
    "With a plaintive whine, Rosalind got back to eating my dick, this time at an invigorated pace."
    "I don't know if it was instinct or if she simply had more experience working a dick then she let on, but the way she twisted her hand counter-clockwise to her mouth, was..."
    "{b}*Schlup, fwhip, chwup!*{/b}"
    mc "Hnng, fhwwhuuck...!"
    "...was enough to, ironically opposed to her lip-service, momentarily stop me in my tracks and call out in vulva-muffled pleasure."
    scene rose_e2_69c_a with dissolve
    show rose_e2_69c
    rose "{b}Ha...! Your dick is so fucking big{/b}!"
    "Again, she removed herself from my cock to coax me along with her words."
    rose "I can't wait for it to split me open and fuck me stupid, baby."
    "I guess this was what she thought porn-talk was like. Not that I minded."
    rose "Mmmh... would you like that? You want to slip it in my pussy?"
    "Having the motherly woman loudly proclaim herself a slut was a treat for the ears."
    rose "Fuck me raw? No condom? Until you fill me with your hot spunk? Hnnaa..."
    "That said..."
    scene w2_8128 with dissolve
    scene w2_8129 with dissolve
    "*Thwap!*"

    if w2ExRoseDialogue == "A":
        mc "Put my dick back in your mouth!"
        rose "Y-yes, sir!"
    if w2ExRoseDialogue == "B":
        mc "Suck it, Ma'am!"
        rose "Y-yes!"

    scene rose_e2_69d_a with dissolve
    show rose_e2_69d
    rose "*Gluhk, glhuk, gluhk!*"
    "{b}Woah!{/b}"
    rose "*Gluhk, hnng...*"
    "That little bit of encouragement was all Rosalind needed to spear her throat with my cock and commence face fucking herself."
    rose "{b}Ghulk, ghuug, glug!{b}"
    "The obscene sound of her throat being voluntarily ravaged and plugged reminded me that I myself needed to not slack. I had a job to do and one good turn deserved another."
    "So, putting aside the building pleasure in my groin, I blanked out the external world and focused solely on the pussy in front of me."
    rose "*Gluhk, hnng...*"
    "I voraciously ate every part of her, alternating from exploring her inner parts to teasing her outer ones."
    "I pulled apart her folds, grazed their less traveled underside, and kissed her entrance."
    rose "Mmh~ *gluhk!*"
    "I poked and prodded her clit, taking no great care with the fragile nub and savaging it to my heart's contentment."
    "I snaked my tongue past her entrance and plumbed her slimy depths, delighting in the subtle way her insides contracted."
    rose "*Gluhk, ghug, ghluhk...!*"
    "In short, I tasted, smelled, breathed, {b}lived{/b} the motherly woman's sex."
    rose "*{b}Gluhk, glu, glug, gluuunhk, fwuuhk, gluhk...!{b}*"
    mct "(Oh, shit!)"
    "So preoccupied by Rosalind's lower half, I failed to recognize the signs of my own near eruption, until my mind completely blanked and hot streaks of white seared the inside of my eyelids."
    mct "(I'm...!)"
    $ renpy.music.set_volume(.1, 0, channel = "music")
    play sound "sound effects/spurt.wav"
    scene w2_8130 with flash
    mc "Hhhnng!"
    "To both our surprise, a torrent of sticky white goo shot down the MILF's throat."
    rose "*Cough!* Huuhk, hnnggk...!"
    $ renpy.music.set_volume(.1, 0, channel = "music")
    play sound "sound effects/spurt.wav"
    scene w2_8131 with flash
    "Not every drop would make it to her stomach though. Most of it wouldn't, actually."
    rose "*Cough!* Hnnng...! Huhk!"
    "As gravity and the force of violently expelling air from her lungs caused the majority of it to pool and dribble out of her mouth."
    mc "Ha... ha...."
    scene black with fade
    mc "Rose..."
    scene w2_8132 with fade
    mc "Heh, I..."
    scene w2_8133 with dissolve
    "She still had a somewhat full mouth, like she was waiting for me to tell her what to do with it!"
    "What {b}should{/b} she do with it?"
    show screen mod_week2_expo
    menu:
        "Verbally tell her to swallow.":
            hide screen mod_week2_expo
            stop music fadeout 3.0
            $ renpy.music.set_volume(1, 3, channel = "music")
            scene w2_8134 with dissolve
            mc "Go ahead and swallow. What are you waiting for?"
            scene w2_8133 with dissolve
            scene w2_8135 with dissolve
            scene w2_8133 with dissolve
            "She absently nodded."
            scene w2_8136 with dissolve
            "*Gulp*"
            scene w2_8137 with dissolve

            if w2ExRoseDialogue == "A":
                mc "Good girl."
            if w2ExRoseDialogue == "B":
                mc "Good job, Ma'am."

            scene w2_8138 with dissolve
            "Damn. Even in a situation like this, Rosalind's smile was confusingly warm and reassuring."
            scene w2_8139 with dissolve
            rose "What's next?"
            scene w2_8140 with dissolve
            mc "Well, what do you think?"
            scene w2_8139 with dissolve
            rose "In that case, would you mind... lying on your back?"
            scene w2_8138 with dissolve
            "Oh...?"
            scene black with fade
            "Guess she was feeling proactive."
        "(w2expts(ros)=+2)Kiss her and physically encourage her to swallow.{vspace=50}"(chg=["rosalind_passion_up2"]):


            hide screen mod_week2_expo
            $ w2ExSnowball = True
            $ w2ExPointsRosalind += 2
            $ Rosalind_Libido += 2

            scene w2_8141 with dissolve
            mc "C'mere!"
            rose "Whhwait ah mhhunite, my mhouth--!"
            $ renpy.music.set_volume(1, 3, channel = "music")
            scene w2_8142 with dissolve
            "Without any hesitation, and inexplicable even to my diseased mind, I thrust my tongue into Rosalind's mouth to share in my own taste."
            rose "Mmmh...!"
            "Diluted with her saliva, it was like most things, more disgusting in theory than practice."
            scene w2_8143 with dissolve
            hana "What the fuck...!"
            chuck "Hot damn..."
            scene w2_8144 with dissolve
            kil "Dude, gross!"
            mct "(...was it?)"
            scene w2_8145 with dissolve
            "No matter, I used my tongue to push and corral my seed to the back of Rosalind's throat, until she finally reflexively swallowed."
            rose "Mmh...! *{b}Gulp!{/b}*"
            scene w2_8146 with dissolve
            rose "Ha... ha...?"
            "She looked kinda confused and, honestly, so did I. It was just one of those things that felt hot during the moment."
            mc "Let's move on."
            rose "O-okay...! I... um... can you..."
            stop music fadeout 3.0
            scene black with fade
            mc "Like this?"
            "It seemed Rosalind wanted to take a proactive approach."

    scene w2_8147 with fade
    "I laid back and the curvy woman straddled me, pinning my cock to my waist and fiercely eyeing me down."

    if roseFlag == True:
        mc "*Whispering* It's nice seeing you on top for once..."
    else:
        mc "Quite the view..."

    "Rosalind, as I had slowly learned, was even better at compartmentalization than I. She had the remarkable ability to remove all sense of self from the equation and do what needed to be done."
    rose "Ah... I can't..."
    scene w2_8148 with dissolve
    rose "I don't want to wait any longer, baby. Let's make each other feel good..."
    "There was something genuinely desperate and lonely in her words."
    scene w2_8149 with pixellate
    show screen camcorder
    vic "*Ha, ha... don't make me laugh... while I'm...!"
    hm "...but you're so cute when you laugh?"
    vic "No, I look stupid! It's not sexy!"
    hide screen camcorder
    scene w2_8150 with pixellate
    play music "music/a-kiss-for-amanda.ogg"
    "I realized that simplifying her as only a \"victim\" and reducing her down to the most conveniently digestible terms only served my delusions."
    rose "D-dang it, I'm... {b}stuffed{/b}."
    "I wasn't peering up at a \"desperate mother\", but a living, breathing woman navigating a difficult situation the best she could."
    scene w2_8151 with dissolve
    rose "I'm going to move."
    scene w2_8152 with dissolve
    "Her smile was inexplicable, in a way that defied communication. I don't think I could ever truly understand the mix of emotions that were bubbling behind those lips."
    show screen mod_week2_expo
    menu:
        "Play it cool.":
            hide screen mod_week2_expo
            if w2ExRoseDialogue == "A":
                mc "What are you waiting for?"
            if w2ExRoseDialogue == "B":
                mc "Go ahead, Ma'am."
        "(w2expts(ros)=+1)Be mean and demanding.":

            hide screen mod_week2_expo
            $ w2ExPointsRosalind +=1
            if w2ExRoseDialogue == "A":
                mc "Well, you waiting for an invitation? Get that ass moving!"
                $ w2ExRoseDialogue = "C"
            if w2ExRoseDialogue == "B":
                mc "Get your ass moving, Ma'am."
                $ w2ExRoseDialogue = "D"

    scene w2_8153 with dissolve
    scene w2_8152 with dissolve
    "With a nod, she began to gently roll her hips, agonizingly dragging her insides slowly across my length."
    scene w2_8154 with dissolve
    rose "Hnng..."
    "For the time being, I laid back and let Rosalind dictate the pace."
    scene w2_8155 with dissolve
    "The way she moved her hips was a tad clumsy, but it was not without appeal."
    scene w2_8154 with dissolve
    "From my position, I could eagerly watch her expression as she explored her range of movement: short humps, long humps, feverish grinding, and everything in between. She rode my dick like a sampler platter, in search of what best scratched the itch."
    scene rose_e2_cg1_a with dissolve
    show rose_e2_cg1
    rose "That's it, baby."
    "Finally, she found a tempo that suited her tastes. She fucked me slow and softly, more so rocking her fat ass than bringing it down to bear."
    "It wasn't my type of sex. Not in the least."
    "It wasn't fast or rough. It wasn't mean or degrading."
    "It wasn't even a question of top and bottom."
    "It wasn't any of that, but it was nice in its own way. Comforting even."
    "From here, I had a nice view of Rosalind's jiggling tits as they rose and fell."
    "I could see her tummy dance and take a long, hard look at where we were connected."
    "No, it wasn't so bad to just lie back and enjoy the sickly sweet slimy sensation of a woman gently pleasuring you."
    "No, it really fucking wasn't. {b}For now, at least{/b}."
    rose "Hey, are you feeling good?"
    "Ha. She asked like she actually cared."

    if w2ExRoseDialogue == "A" or w2ExRoseDialogue == "C":
        mc "Yeah, I'm feelin' pretty good..."
    if w2ExRoseDialogue == "B" or w2ExRoseDialogue == "D":
        mc "Yes, Ma'am. Sure as shit am."

    rose "Heh, I'm glad..."
    mc "What about you? Be truthful."
    rose "Well... my stomach..."
    scene rose_e2_cg2_a with dissolve
    show rose_e2_cg2
    rose "My whole torso really... it's itching like something mad..."
    rose "Every time your dick presses against my stomach, my mind goes blank and I feel like I gotta piss..."
    "She was right. She WAS fucking me at an interesting angle."
    "Instead of traveling toward her cervix, my dick traveled up and knocked against the walls of her sex, putting pressure on her bladder."
    mc "You like the way that feels?"
    rose "H-hng, k-kind of? I think? It's a {i}new{/i} feeling..."
    mct "(I see...)"
    "That was a valuable piece of information, one I could potentially utilize."
    scene rose_e2_cg1_a with dissolve
    show rose_e2_cg1
    rose "Hey... would you grab my chest?"
    "It seemed she was set on doing what she wanted and controlling her leg of the event."
    mct "(Of course, in this case...)"
    scene w2_8156 with dissolve
    "I didn't mind going along and copping a feel."
    "She had placed herself front and center of the main camera. I didn't think the old woman had any complaints so far."
    scene rose_e2_cg3_a with dissolve
    show rose_e2_cg3
    rose "Y-yeah, like that. Ha...!"
    "The moment I grabbed her tits, her hips hastened."
    rose "Your hands feel nice."
    "If I wanted, these puppies were the ticket to controlling the wanton mother, to make her sing or cry to my heart's satisfaction."
    rose "Even just grabbing them like that is making me tingle."

    if w2ExRoseDialogue == "A":
        mc "Your body is so responsive. I bet the camera is loving it."
        mc "It was like you were made to suck and fuck on film."
    if w2ExRoseDialogue == "B":
        mc "Your body is wonderful, Ma'am. I bet the camera loves you."
        mc "It was like you were made to suck and fuck on film."
    if w2ExRoseDialogue == "C":
        mc "You're looking like such a slut right now."
        mc "You should've just done porn instead of becoming a wife. It suits you."
    if w2ExRoseDialogue == "D":
        mc "It's incredible. You're making a face like a hungry slut, Ma'am."
        mc "You should've just done porn instead of becoming a wife. It suits you."

    "That wasn't just dirty talk. The woman I was looking up at right now was unordinarily composed."
    rose "Ha... hng... if you say so..."
    mc "Aren't you worried about your friends and family seeing this?"

    if w2ExRoseDialogue == "A" or w2ExRoseDialogue == "B":
        mc "Someone you know might see this."
    if w2ExRoseDialogue == "C" or w2ExRoseDialogue == "D":
        mc "Someone you know might learn just how much of a cock-hungry bitch you are."

    rose "Heh, I mean... ha... what are the chances?"
    mc "More than you might think..."
    "I mean, I knew the answer didn't matter. Taking care of her loan shark problem superseded all, but for obvious reasons I still asked another question."
    mc "What about your daughter? Aren't you worried what she'd think? Or how her friends at school might treat her?"
    rose "Haa, hng... b-baby, don't bring the real world into this right now."
    show screen camcorder
    scene w2_8157 with pixellate
    vic "Ha, hhnngg..."
    hm "You like it?"
    scene w2_8158 with dissolve
    vic "Y-yes...! Hnng... ha...! F-fuck!"
    scene w2_8157 with dissolve
    hm "Should we take a break?"
    scene w2_8158 with dissolve
    vic "No, keep fucking me you idiot!"
    hide screen camcorder
    scene rose_e2_cg3_a with pixellate
    show rose_e2_cg3
    mct "(Just have fun with it, huh?)"
    "She wasn't flustered or mad, no the look on her face read more like she was politely asking me to stop, and quite frankly, with where my mind was going, I agreed with her."
    mct "(Alright... let's just enjoy the fantasy of being on camera.)"
    scene rose_e2_cg4_a with dissolve
    show rose_e2_cg4
    rose "Gyyeeeh...! T-that spot...! Hhuuhk...!"
    "Using the science from earlier, I thrusted short and fast against the upper lining of Rosalind's sex."
    mct "(Hope she doesn't piss herself...)"
    "...or do I?"
    scene w2_8159 with dissolve
    chuck "You always impress me."
    kat "How so?"
    scene w2_8160 with dissolve
    chuck "The rich way you prepare your meals. The way you layer games inside of games. "
    scene w2_8161 with dissolve
    kat "It's just two people fucking on stage, Charles."
    scene w2_8162 with dissolve
    chuck "I know you. Right now, you're feeding off what you're imagining is going on in the lad's head."
    chuck "I mean a porn video, really?"
    scene w2_8163 with dissolve
    kat "...I'm just offering him opportunities to enjoy different things."
    scene w2_8164 with dissolve
    chuck "He's very lucky to be working so closely with you, but I want to caution you."
    kat "...oh?"
    scene w2_8165 with dissolve
    chuck "I don't mind you messing with his head a little, but just don't pull him into whatever nasty business you have going on with Abel. {b}[mcf]'s family{/b}."
    chuck "I don't want him inadvertently jeopardizing his future by playing your {i}office politics{/i}. Say you understand."
    scene w2_8161 with dissolve
    kat "You have nothing to worry about in the first place, but I... {i}understand{/i}."
    scene w2_8166 with dissolve
    chuck "Good girl."
    chuck "Great show tonight, by the way."
    scene w2_8167 with dissolve
    rose "Gngg... AAAAAH...!"
    scene rose_e2_cg5_a with dissolve
    show rose_e2_cg5
    "This position was working magic. It was like a cheat code."

    if w2ExRoseDialogue == "A" or w2ExRoseDialogue == "C":
        mc "You should see the look on your face, Rosalind."
    if w2ExRoseDialogue == "B" or w2ExRoseDialogue == "D":
        mc "Jeez, you should see your face right now, Ma'am...!"

    "Rosalind had quickly devolved into looking like a slovenly wreck."
    "I don't know if this shallow sort of attack would work on other women, but for her, she was fucking loving it."

    if w2ExRoseDialogue == "A" or w2ExRoseDialogue == "B":
        mc "You look incredible right now!."
    if w2ExRoseDialogue == "C" or w2ExRoseDialogue == "D":
        mc "You look so dumb right now!"


    "My dick simply hammered away, glancing blow after glancing blow tickling her bladder."
    rose "Gyyhaaa.. haa...!"
    "Every thrust sent her eyes knocking around inside her skull and caused her face to scrunch up like she was taking a shit."
    rose "Ghnn...!"
    "Every jab mashed the head of my dick against the soft barrier, causing her insides to writhe and spasm."
    mct "(This was...)"
    rose "Gwhuh...!"
    scene rose_e2_cg4_a with dissolve
    show rose_e2_cg4
    "Every knudge, smack, stab of my dick produced a result you would only imagine in your fantasies. Like the air was being fucked out of her."
    mct "(This was her G-spot...?)"
    rose "Owhnoo....!"
    "Interesting!"

    if w2ExRoseDialogue == "A" or w2ExRoseDialogue == "B":
        mc "This is incredible! You sound so...!"
        mc "Wow!"
        "Obviously, she wasn't the only one enjoying herself. The tempo still wasn't to my tastes, but her expression and the noises she was making..."
        rose "Hnng...!"
        mc "You're beautiful!"
    if w2ExRoseDialogue == "C" or w2ExRoseDialogue == "D":
        mc "Eat it! Enjoy my cock, you bitch!"
        mc "To think a mother is making a face like that!"
        "Obviously, she wasn't the only one enjoying herself. The tempo still wasn't to my tastes, but her expression and the noises she was making..."
        rose "D-don't say that!"
        mc "Why not? It's incredible! You're beautiful!"

    "... it filled me with a sublime sense of conquest."
    scene rose_e2_cg5_a with dissolve
    show rose_e2_cg5
    rose "So, s-hshoho... ghoood... I cchant'thwink...!"
    "It was threatening to make me nut right here and now."

    if w2ExRoseDialogue == "A" or w2ExRoseDialogue == "B":
        mc "Good, just enjoy yourself."
        rose "Ghuhh... yhyhes..."
    if w2ExRoseDialogue == "C" or w2ExRoseDialogue == "D":
        mc "What does a cow like you even need any thoughts for?"
        rose "Ghuhh... idohnyyttkanhow...!"

    rose "Ahhhjust... ahjustt... f-fhuck me [mcf]!"
    "Rosalind, who had taken care not to say my name, had slipped. Quite frankly, I didn't even care any more."
    "I was less preoccupied with being on camera and more consumed by the excitement of plowing the babbling MILF."
    rose "Ohhfhhunnyy...!Fheeeling...! SShofttmushy...!"
    "I think she had come once or twice already and I myself wasn't too far behind."
    rose "O-owwoh...!"
    "Scatterbrained as she was, her instincts had won their prize. Her fuck hole gripped and massaged my pistoning cock, until..."

    if w2ExRoseDialogue == "A" or w2ExRoseDialogue == "B":
        mc "Get ready, I'm...!"
    if w2ExRoseDialogue == "C" or w2ExRoseDialogue == "D":
        mc "Take it, whore!"

    rose "Ghhtiviveittomeeee!"
    $ renpy.music.set_volume(.2, 0, channel = "music")
    play sound "sound effects/spurt.wav"
    scene w2_8168 with flash
    mc "Gh...!"
    "Gritting my teeth, I poured my white hot lust into Rosalind's cunt."
    rose "Hnnyeeh... hnngg..."
    play sound "sound effects/spurt.wav"
    scene w2_8169 with flash
    "Spurt after spurt filled Rosalind's honey pot, her lower mouth lapping it up without stop."
    mct "(Ghha... so... so good...)"
    "Suddenly I felt so incredibly sleepy in her soothing embrace. It was..."
    rose "Gyeehh...! W-woah... oh, no...! Fheel, fhheel... ehh..."
    scene rose_e2_cg5_a with dissolve
    show rose_e2_cg5
    tom "He didn't break her, did he?"
    "A striking look of concern pulled me from my haze. It told me..."
    show screen mod_week2_expo
    menu:
        "(w2expts(ros)=+1)Give her a final push toward an explosive finish.{vspace=50}"(chg=["kathleen_up"]):
            hide screen mod_week2_expo
            $ w2ExPointsRosalind +=1
            $ Kathleen_Affection +=1
            "It told me I wasn't finished!"
            $ renpy.music.set_volume(1, 0, channel = "music")
            scene rose_e2_cg4_a with dissolve
            show rose_e2_cg4
            rose "Gnnh, w-wait..whhwati...! If you do thhhwat...!"
            "I know."
            rose "Ghheehh... wwhahwoo..."
            "If I do that..."
            rose "Chum... chhhhcumingg..."
            "If I do that you'll..."
            rose "Eh'ts, fh-funhy... thh...!"
            scene w2_8170 with dissolve
            mct "(You'll make a mess!)"
            rose "Gyhheeh...."
            "I took immense pleasure in seeing the matronly woman piss herself. To see her warm nature unravel into a lurid mess."
            "I even felt a little good about it too, because..."
            stop music
            play sound "sound effects/thud-floor.mp3"
            scene w2_8171 with vpunch
            "*Fwhlop!*"
            rose "Hnng, ha..."
            "She looked utterly at peace, if only for the briefest of time."
            scene w2_8172 with dissolve
            rose "Haa.. whwa..."
            chuck "Bravo, lad!"
            "It was absurd, but I felt like... I did a good job?"
            "That was the ridiculous last thought that marked the end of this week's exhibition."
            scene black with fade
            "A delusion my tired mind was willing to accept."
            if not persistent.roseW2Shame:
                play sound "sound effects/notification.wav"
                show memoryunlock with dissolve
                $ renpy.pause(3, hard=True)
                $ persistent.roseW2Shame = True
                hide memoryunlock with dissolve
                $ renpy.pause(0.5, hard=True)
            "......"
            "..."
            $ renpy.end_replay()
            jump w2ExWinner
        "Pull her into your arms and let her come down gently."(chg=["hana_up","rosalind_up"]):

            hide screen mod_week2_expo
            $ Hana_Affection +=1
            $ Rosalind_Affection +=1
            stop music fadeout 3.0
            mc "H-hey...!"
            scene w2_8173 with dissolve
            mc "It's okay..."
            "With care, I pulled the chesty woman into my arms."
            rose "Hnn, hwaa...? Hhaa...?"
            scene w2_8174 with dissolve
            "She shook and trembled as she rode out her full-body orgasm, but I held tight."
            frank "Ha, she looks like a newborn deer!"
            rose "Hnng... hhahh... hngg..."
            mc "I got you."
            scene w2_8176 with dissolve
            rose "O-oh...? That was... ah..."
            rose "Hehehe... that was weird."
            scene w2_8175 with dissolve
            "The way she pleasantly giggled was at odds with what happened."
            "This woman..."
            "That was the last thought that marked the end of this week's exhibition."
            $ renpy.music.set_volume(.2, 0, channel = "music")
            scene black with fade
            if not persistent.roseW2Shame:
                play sound "sound effects/notification.wav"
                show memoryunlock with dissolve
                $ renpy.pause(3, hard=True)
                $ persistent.roseW2Shame = True
                hide memoryunlock with dissolve
                $ renpy.pause(0.5, hard=True)
            "She giggled in a way that conveniently let me forget how fucked up her situation was."
            "......"
            "..."
            $ renpy.end_replay()
            jump w2ExWinner



label w2ExWinner:

    if w2ExPointsVeronica >= w2ExPointsFelicia and w2ExPointsVeronica >= w2ExPointsRosalind:
        $ w2ExKatVeronica = True
    elif w2ExPointsFelicia >= w2ExPointsRosalind and w2ExPointsFelicia >= w2ExPointsVeronica:
        $ w2ExKatFelicia = True
    else:
        $ w2ExKatRosalind = True

    play music "music/victim-to-victor.ogg"
    scene w2_8177 with curtains
    show screen textbox2 with dissolve
    "There it finally was, all three Carnations stood side by side, completely stripped and waiting for the proverbial axe to drop."

    if w2ExRoseIanSex == True:
        "Rosalind cleaned up nicely, looking a little pensive perhaps, but no worse for wear from my friend's rough treatment,"
    else:
        "Rosalind cleaned up nicely, there was no trace of her earlier confidence, but she was looking composed."

    scene w2_8178 with dissolve
    "Felicia, on the other hand, was tired. Very, very tired."
    "She looked worse than she did earlier. The physical exhaustion from her trial had fully taken hold."
    "...and lastly Veronica, who had lent the shaky legged blonde her shoulder, was unusually difficult to read."
    "For the most part, she just blankly scanned the room."

    if veronicaFriend == True:
        scene w2_8179 with dissolve
        "It might've been my imagination, but there was a teensy, quickly fading smile buried when she got to me."

    scene w2_8180 with dissolve
    kat "The results of the silent auction are in - Vincenzo takes it."
    scene w2_8181 with dissolve
    tom "Damn it."
    jim "That fatty always overpays."
    tom "How much did he bid?"
    scene w2_8182 with dissolve
    kat "You know perfectly well that's a secret, Thomas. If you really wanted it, you should've bid more."
    scene w2_8183 with dissolve
    rose "W-wah...?"
    scene w2_8187 with dissolve
    fel "I guess I slept through something interesting..."
    scene w2_8188 with dissolve
    ver "She put a blanket over the cage, all you missed was Rosie moaning like a bitch."
    scene w2_8189 with dissolve
    rose "H-hey! You weren't any different!"
    scene w2_8190 with dissolve
    fel "Yeah, you sounded like a banshee in a blender!"
    ver "...bah."
    scene w2_8191 with dissolve
    kat "You all performed admirably tonight, but only one of you will be deemed the winner and only one of you will be deemed the loser."
    scene w2_8192 with dissolve
    ver "How is there only one winner and one loser?"
    scene w2_8193 with dissolve
    kat "Only one loser for the purpose of the penalty game."
    scene w2_8194 with dissolve
    fel "Another game... p-please no? H-heh..."
    ver "Greeeeeat."
    scene w2_8193 with dissolve
    kat "Before we get to that, we must first crown the winner. You girls excited?"
    scene w2_8195 with dissolve
    fel "........."
    scene w2_8196 with dissolve
    ver "......"
    scene w2_8197 with dissolve
    rose "..."
    scene w2_8198 with dissolve
    kat "As you already know, the Carnation whose photoshoot generated the greatest response automatically secured the first vote."

    if w2ShootWinnerVero == True:
        scene w2_8199 with dissolve
        ver "Hmmpfh."
        kat "That's right. Miss Lynch has one vote."
        kat "That leaves the rest of the determination to Miss Rhodes and me. Which Carnation made the greatest impression on you, Hana?"
        scene w2_8200 with dissolve
        hana "...I'm first?"
        scene w2_8201 with dissolve
        kat "If it's all the same to you."

        if kat_polite == True:
            "It wasn't all the same. Mrs. Pulman could potentially put an end to the whole thing right now and spare Hana some face with the girls."
        else:
            "It wasn't all the same. Kathleen could potentially put an end to the whole thing right now and spare Hana some face with the girls."

        scene w2_8202 with dissolve
        kat "Go ahead. Pick a Carnation and state your reason."
        scene w2_8203 with dissolve
        hana "No hard feelings I hope."
        scene w2_8204 with dissolve
        fel "Ha! Go ahead. I understand."
        "It was obvious from the start she wasn't picking Felicia."
        scene w2_8205 with dissolve
        hana "I pick Rosalind."
        scene w2_8206 with dissolve
        rose "Yes!"
        scene w2_8207 with dissolve
        hana "She didn't hesitate at all. It's as simple as that."
        scene w2_8182 with dissolve
        kat "So we have it. One vote for Miss Lynch and one for Mrs. Carter."
        scene w2_8208 with dissolve
        kat "Things are looking fruitless for you, Mrs. Ford. You feeling stupid?"
        scene w2_8209 with dissolve
        fel "Who do you pick, Kathleen?"

        if w2ExKatFelicia == True:
            $ w2ExLosersAll = True
            scene w2_8214 with dissolve
            kat "Honestly...? You."
            kat "Are you even human? You lasted more than an hour, on top of everything the boys did to you."
            scene w2_8215 with dissolve
            fel "Wait, so we..."
            ver "We tie?"
            scene w2_8216 with dissolve
            kat "That's right."
            scene w2_8217 with dissolve
            rose "We all win?"
            scene w2_8216 with dissolve
            kat "That's one way of looking at it. You could also say you all lose."
            kat "None of you succeeded in standing out."
            scene w2_8218 with dissolve
            ver "It's a wash? What does that mean for us?"
            scene w2_8208 with dissolve
            kat "That means, none of you fell behind this week, and come Monday, you're all subject to the penalty."
            scene w2_8209 with dissolve
            fel "You're not going to tell us what it is, are you?"
            scene w2_8208 with dissolve
            kat "Not at all."
            scene w2_8219 with dissolve
            kat "Looks like you win tonight's pool, Abel."
            kat "You're the only one who anticipated a tie."
            scene w2_8220 with dissolve
            abel "Donate it to a charity of Miss Rhodes' choosing please."
            scene w2_8221 with dissolve
            hana "Why me?"
            scene w2_8222 with dissolve
            abel "I'm simply happy you joined us tonight. I know of an excellent lab that researches Huntington's, perhaps you want to donate it there?"
            scene w2_8221 with dissolve
            hana "How do you know--"
            scene w2_8223 with dissolve
            jim "Kind of an anticlimatic ending? Why don't we have a tie-breaker?"
            chuck "Sometimes it's about the journey, Jim."
            frank "Where are the whores? I got--"
            scene black with fade
            stop music fadeout 3.0
            "......"
            "..."
            jump w2ExHanaTalk

        if w2ExKatRosalind == True:
            $ w2ExWinnerRosalind = True
            $ w2ExLoserFelicia = True
            scene w2_8224 with dissolve
            kat "I'm... I'm inclined to agree with Miss Rhodes."
            kat "She was an obedient old cow."
            scene w2_8225 with dissolve
            rose "I... win?"
            scene w2_8226 with dissolve
            kat "That's right, Mrs. Carter. You win and Mrs. Ford, having no votes, is the loser."
            vinc "Ha, ha! Yes!"
            kat "Come Monday, our little slut wife will face the penalty."
            scene w2_8227 with dissolve
            fel "You're not going to tell us what it is, are you?"
            scene w2_8226 with dissolve
            kat "Not at all."
            scene w2_8228 with dissolve
            kat "Looks like Mihir, Thomas, Andrew, and Vincenzo are splitting tonight's pool."
            scene w2_8229 with dissolve
            kat "Congratulations gentlemen."
            scene black with fade
            hana "So, it's over?"
            mc "Looks like it's going to be pretty soon."
            stop music fadeout 3.0
            "......."
            "..."
            jump w2ExHanaTalk

        if w2ExKatVeronica == True:
            $ w2ExWinnerVeronica = True
            $ w2ExLoserFelicia = True
            scene w2_8214 with dissolve
            kat "My vote coincides with the audience's."
            kat "Miss Lynch's submission was simply sublime tonight."
            scene w2_8230 with dissolve
            ver "Holy shit...!"
            rose "..."
            scene w2_8231 with dissolve
            kat "Tonight's winner is determined. Mrs. Ford, having no votes, is the loser."
            sam "That's my girl!"
            kat "Come Monday, our little slut wife will face the penalty."
            scene w2_8232 with dissolve
            fel "You're not going to tell us what it is, are you?"
            scene w2_8231 with dissolve
            kat "Not at all."
            scene w2_8228 with dissolve
            kat "Looks like Samson, Joe, Jim, and Kristoff are splitting tonight's pool."
            scene w2_8229 with dissolve
            kat "Congratulations gentlemen."
            scene black with fade
            hana "So, it's over?"
            mc "Looks like it's going to be pretty soon."
            stop music fadeout 3.0
            "......."
            "..."
            jump w2ExHanaTalk


    if w2ShootWinnerFel == True:
        scene w2_8210 with dissolve
        fel "That was me."
        scene w2_8211 with dissolve
        kat "Indeed it was, Mrs. Ford. I guess you had such a lovely home, it left an impression."
        scene w2_8212 with dissolve
        fel "I'm sure that's what it was..."
        scene w2_8211 with dissolve
        kat "She presently has one vote."
        kat "That leaves the rest of the determination to Miss Rhodes and I. Which Carnation made the greatest impression on you, Hana?"
        scene w2_8200 with dissolve
        hana "...I'm first?"
        scene w2_8201 with dissolve
        kat "If it's all the same to you."

        if kat_polite == True:
            "It wasn't all the same. Mrs. Pulman could potentially put an end to the whole thing right now and spare Hana some face with the girls."
        else:
            "It wasn't all the same. Kathleen could potentially put an end to the whole thing right now and spare Hana some face with the girls."

        scene w2_8202 with dissolve
        kat "Go ahead. Pick a Carnation and state your reason."
        scene w2_8203 with dissolve
        hana "No hard feelings I hope."
        scene w2_8204 with dissolve
        fel "Ha! Go ahead. I understand."
        "It was obvious from the start she wasn't picking Felicia."
        scene w2_8205 with dissolve
        hana "I pick Rosalind."
        scene w2_8206 with dissolve
        rose "Yes!"
        scene w2_8207 with dissolve
        hana "She didn't hesitate at all. It's as simple as that."
        scene w2_8182 with dissolve
        kat "So we have it. One vote for Mrs. Ford and one for Mrs. Carter."
        scene w2_8208 with dissolve
        kat "Things are looking unfortunate for you, Miss Lynch."
        scene w2_8209 with dissolve
        ver "You still have a vote."

        if w2ExKatFelicia == True:
            $ w2ExWinnerFelicia = True
            $ w2ExLoserVeronica = True
            scene w2_8214 with dissolve
            kat "My vote goes toward Mrs. Ford, making her tonight's winner."
            scene w2_8233 with dissolve
            ver "Tsk...!"
            fel "R-really...? Ha!"
            scene w2_8234 with dissolve
            kat "Looks like you're going to have to play the penalty game, Miss Lynch."
            kat "We'll get to that on Monday, when we all meet."
            scene w2_8228 with dissolve
            kat "Looks like Frank, Eric and Isaak are splitting tonight's pool."
            scene w2_8229 with dissolve
            kat "Congratulations gentlemen."
            scene black with fade
            hana "So, it's over?"
            mc "Looks like it's going to be pretty soon."
            stop music fadeout 3.0
            "......."
            "..."
            jump w2ExHanaTalk


        if w2ExKatRosalind == True:
            $ w2ExWinnerRosalind = True
            $ w2ExLoserVeronica = True
            scene w2_8224 with dissolve
            kat "I'm... I'm inclined to agree with Miss Rhodes."
            kat "She was an obedient old cow."
            scene w2_8225 with dissolve
            ver "Tsk...!"
            rose "I... win?"
            scene w2_8226 with dissolve
            kat "That's right, Mrs. Carter. You win. Miss Lynch, having no votes, is the loser."
            vinc "Ha, ha! Yes!"
            kat "Come Monday, she will face the penalty."
            scene w2_8227 with dissolve
            fel "You're not going to tell us what it is, are you?"
            scene w2_8226 with dissolve
            kat "Not at all."
            scene w2_8228 with dissolve
            kat "Looks like Mihir, Thomas, Andrew, and Vincenzo are splitting tonight's pool."
            scene w2_8229 with dissolve
            kat "Congratulations gentlemen."
            scene black with fade
            hana "So, it's over?"
            mc "Looks like it's going to be pretty soon."
            stop music fadeout 3.0
            "......."
            "..."
            jump w2ExHanaTalk

        if w2ExKatVeronica == True:
            $ w2ExLosersAll = True
            scene w2_8214 with dissolve
            kat "Honestly...? I picked you, Miss Lynch. Your submission tonight was utterly sublime."
            scene w2_8215 with dissolve
            fel "Wait, so we..."
            ver "We tie?"
            scene w2_8216 with dissolve
            kat "That's right."
            scene w2_8217 with dissolve
            rose "We all win?"
            scene w2_8216 with dissolve
            kat "That's one way of looking at it. You could also say you all lose."
            kat "None of you succeeded in standing out."
            scene w2_8218 with dissolve
            ver "It's a wash? What does that mean for us?"
            scene w2_8208 with dissolve
            kat "That means, none of you fell behind this week, and come Monday, you're all subject to the penalty."
            scene w2_8209 with dissolve
            fel "You're not going to tell us what it is, are you?"
            scene w2_8208 with dissolve
            kat "Not at all."
            scene w2_8219 with dissolve
            kat "Looks like you win tonight's pool, Abel."
            kat "You're the only one who anticipated a tie."
            scene w2_8220 with dissolve
            abel "Donate it to a charity of Miss Rhodes' choosing please."
            scene w2_8221 with dissolve
            hana "Why me?"
            scene w2_8222 with dissolve
            abel "I'm simply happy you joined us tonight. I know of an excellent lab that researches Huntington's, perhaps you want to donate it there?"
            scene w2_8221 with dissolve
            hana "How do you know--"
            scene w2_8223 with dissolve
            jim "Kind of an anticlimactic ending? Why don't we have a tie-breaker?"
            chuck "Sometimes it's about the journey, Jim."
            frank "Where are the whores? I got--"
            scene black with fade
            stop music fadeout 3.0
            "......"
            "..."
            jump w2ExHanaTalk

    if w2ShootWinnerRose == True:
        $ w2ExWinnerRosalind = True
        scene w2_8186 with dissolve
        kat "That was Mrs. Carter. She presently has one vote."
        scene w2_8207 with dissolve
        kat "That leaves the rest of the determination to Miss Rhodes and I. Which Carnation made the greatest impression on you, Hana?"
        scene w2_8200 with dissolve
        hana "...I'm first?"
        scene w2_8201 with dissolve
        kat "If it's all the same to you."

        if kat_polite == True:
            "It wasn't all the same. Mrs. Pulman could potentially put an end to the whole thing right now and spare Hana some face with the girls."
        else:
            "It wasn't all the same. Kathleen could potentially put an end to the whole thing right now and spare Hana some face with the girls."

        scene w2_8202 with dissolve
        kat "Go ahead. Pick a Carnation and state your reason."
        scene w2_8203 with dissolve
        hana "No hard feelings I hope."
        scene w2_8204 with dissolve
        fel "Ha! Go ahead. I understand."
        "It was obvious from the start she wasn't picking Felicia."
        scene w2_8205 with dissolve
        hana "I pick Rosalind."
        scene w2_8213 with dissolve
        rose "Yes!"
        hana "She didn't hesitate at all. It's as simple as that."
        scene w2_8180 with dissolve
        kat "So we have it. Tonight's winner is chosen, simple as that."
        scene w2_8181 with dissolve
        chuck "What about the loser?"
        scene w2_8182 with dissolve
        kat "I guess that's my determination."

        if w2ExKatFelicia == True:
            $ w2ExLoserVeronica = True
            scene w2_8214 with dissolve
            kat "I was going to give Mrs. Ford my vote. Which makes..."
            scene w2_8235 with dissolve
            kat "You the loser."
            scene w2_8236 with dissolve
            ver "I'm not surprised..."
            scene w2_8235 with dissolve
            kat "Don't make that face. Your submission was sublime, but Felicia..."
            kat "She was hardly human, was she?"
            scene w2_8237 with dissolve
            ver "..."
            kat "The penalty will be for Monday when we all meet, however. Tonight's a wrap."
            scene w2_8228 with dissolve
            kat "Looks like Samson, Joe, Jim, and Kristoff are splitting tonight's pool."
            scene w2_8229 with dissolve
            kat "Congratulations gentlemen."
            scene black with fade
            hana "So, it's over?"
            mc "Looks like it's going to be pretty soon."
            stop music fadeout 3.0
            "......."
            "..."
            jump w2ExHanaTalk

        if w2ExKatVeronica == True:
            $ w2ExLoserFelicia = True
            scene w2_8214 with dissolve
            kat "I was actually going to give Miss Lynch my vote. Which makes..."
            scene w2_8238 with dissolve
            kat "You the loser."
            scene w2_8239 with dissolve
            fel "I hope I can do the game sitting down."
            scene w2_8240 with dissolve
            kat "Oh, don't worry. Tonight's a wrap. The penalty is for when we all meet on Monday."
            scene w2_8239 with dissolve
            fel "That's... {b}a relief{/b}."
            scene w2_8240 with dissolve
            kat "Well, I wouldn't want to break you."
            scene w2_8228 with dissolve
            kat "Looks like Frank, Eric and Isaak are splitting tonight's pool."
            scene w2_8229 with dissolve
            kat "Congratulations gentlemen."
            scene black with fade
            hana "So, it's over?"
            mc "Looks like it's going to be pretty soon."
            stop music fadeout 3.0
            "......."
            "..."
            jump w2ExHanaTalk

        if w2ExKatRosalind == True:
            $ w2ExLoserDuo = True
            kat "I'm... I'm inclined to agree with Miss Rhodes."
            kat "Miss Carter was an obedient old cow. No hesitation what so ever."
            scene w2_8225 with dissolve
            rose "I... have all three votes?"
            scene w2_8226 with dissolve
            kat "That's right, Mrs. Carter. You win, while both Mrs. Ford and Miss Lynch..."
            vinc "Ha, ha! Yes!"
            kat "...are {b}losers{/b}. Come Monday, the pair will face a penalty game."
            scene w2_8227 with dissolve
            fel "You're not going to tell us what it is, are you?"
            scene w2_8226 with dissolve
            kat "Not at all."
            scene w2_8228 with dissolve
            kat "Looks like Mihir, Thomas, Andrew, and Vincenzo are splitting tonight's pool."
            scene w2_8229 with dissolve
            kat "Congratulations gentlemen."
            scene black with fade
            hana "So, it's over?"
            mc "Looks like it's going to be pretty soon."
            stop music fadeout 3.0
            "......."
            "..."
            jump w2ExHanaTalk



label w2ExHanaTalk:

    play music "music/cold-sober.ogg"
    scene w2_8287 with circlewipe
    "As the audience trickled across the room to yammer and get a close up look at the Carnations, Hana, Ian, and I slipped out with the powers-that-be's blessing."
    kil "Another night for the books. Can't believe she got a spider involved this time."
    mc "Yeah, I don't know if I'll forget that look on her face."

    if w2ExRoseIanSex == True:
        scene w2_8288 with dissolve
        hana "...and I'm going to need drugs to forget the sight of Ian's asshole."
        kil "Fuck you, I've got a hella cute pucker."
        scene w2_8289 with dissolve
        mc "You were really into that old lady shit."
        kil "You want to know what the worst part about aging is?"
        hana "This will be good..."
        kil "One day older women will just be women."
        scene w2_8290 with dissolve
        hana "Yeah, but then you get to be a dirty old man like your uncle."
        mc "Heh, {b}yeah{/b}. Call women a third of your age lassie."
        kil "Eh, perfect age... thirties? Best of both worlds. Younger women will be younger women and older women will be older women."
        scene w2_8289 with dissolve
        hana "You're a weird fucking dude."
        mc "The unbidden wisdom of a pervert."
        kil "Like you're not..."
        mc "I'm not as... {b}advanced.{/b}."
    else:

        scene w2_8291 with dissolve
        hana "I don't know how you didn't lose your cool up there, especially being on camera like that."
        kil "[mcf]'s pretty talented, eh?"
        mc "That's one way of putting it."
        scene w2_8288 with dissolve
        kil "Ever since he was a kid, my man can turn it off like that."
        hana "What the hell does that mean?"
        mc "I've got no clue either."
        scene w2_8287 with dissolve
        kil "Yeah, you do. Sometimes you'd go from your usual self to blank-faced at a drop of the hat."
        mc "Don't listen to him. I'm just not an expressive person."


        if w2ExSnowball == True:
            scene w2_8292 with dissolve
            hana "Pfft, not expressive? What do you call tongue punching your own cum down a woman's throat?"
            mc "Oh God. Heat of the fuckin' moment, okay?"
            kil "Hey, man. I'm not judging you."
            scene w2_8293 with dissolve
            hana "Shit, I am. You freaky fuck."
            mc "If I ask a woman to swallow, it'd be hypocritical to be dis--"
            hana "Oh, yeah, you're a real feminist, [mcf]."
            mc "My mom raised a gentleman!"
        else:
            scene w2_8294 with dissolve
            hana "Pffft, not expressive? What was the song-and-dance you did with Rosalind?"
            kil "Yeah, you sounded real cute moaning up there."
            scene w2_8295 with dissolve
            mc "Thanks, I was imagining fucking your mom."
            kil "H-hey!"
            hana "What's a matter, Ian? Afraid to let a girl know she's making you feel good or something?"
            scene w2_8289 with dissolve
            kil "A man should only moan while choking the chicken in the privacy of his own home."
            mc "I guess I'll remember that for the future."


    scene w2_8296 with dissolve
    hana "Hey. You've sat in on most of these, right?"
    scene w2_8297 with dissolve
    kil "The exhibitions? All, but one? Why?"
    scene w2_8296 with dissolve
    hana "How does tonight stack up against most nights? What's the most disgusting thing you've seen?"
    scene w2_8297 with dissolve
    kil "C'mon, why do you want to know something like that?"
    scene w2_8298 with dissolve
    mc "Actually, I'm kinda curious too."
    scene w2_8299 with dissolve
    kil "Hmm, well... it depends on what you mean by disgusting. Sometimes it's a funnel, coffee grounds, and an explosive finish if you know what I mean."
    scene w2_8300 with dissolve
    hana "That's what the stain was?!"
    scene w2_8299 with dissolve
    kil "Other times, it's in your head. That's where the bitch gets real creative."
    scene w2_8298 with dissolve
    mc "I suppose we got a taste of that tonight."
    scene w2_8297 with dissolve
    kil "To answer your question, personally, I think tonight was... average? Average and atypical all the same."
    scene w2_8298 with dissolve
    mc "Those are two opposite words."
    scene w2_8301 with dissolve
    kil "Heh, yeah... every year is different, every Carnation is different, but the contest follows the same crescendo."
    scene w2_8302 with dissolve
    kil "It's something you've got to see to know how it hits you. Can't really mentally prepare yourself for it or anything."
    scene w2_8303 with dissolve
    hana "I wasn't tryin' to, I was just wondering."
    scene w2_8304 with dissolve
    kil "You and [mcf] have that much in common. Fuckin' pessimists."
    hana "..."
    scene w2_8305 with dissolve
    kil "Anyway, I'll leave you two alone."
    mc "You don't have to."

    if w2ExEmmaFavorIan == True:
        scene w2_8306 with dissolve
        kil "Don't I? I need to go find Emma before anyone snatches her up."
        scene w2_8307 with dissolve
        hana "Emma? Why are you fuckin' around with Jacob's--"
        scene w2_8308 with dissolve
        mc "Ian's just giving her a night off as a favor."
        hana "A night off...? Oh... OH! Yeah, I follow."
    else:
        scene w2_8306 with dissolve
        kil "I want to. Gonna go find one of the house girls."

        if w2ExRoseIanSex == True:
            scene w2_8309 with dissolve
            kil "Fucking that boring, fat-assed slut only whet the appetite."
            hana "Christ, you disgust me."
            mc "You didn't seem so bored to me."
            hana "You were watching closely were you?"
        else:
            scene w2_8309 with dissolve
            kil "No homo, but watching you fuck that fat-assed slut got me going."
            hana "Christ, you disgust me."
            mc "What a totally normal thing to say."

    scene w2_8310 with dissolve
    kil "See you tomorrow, doc!"
    mc "Yeah, see you..."
    scene w2_8311 with dissolve
    "......"
    "...."
    scene w2_8312 with dissolve
    mc "You two seem to be getting along better."
    scene w2_8313 with dissolve
    hana "Is that what you think? What gave you that miserable idea?"
    scene w2_8312 with dissolve
    mc "That's the impression that I get."
    scene w2_8314 with dissolve
    hana "Man, I hate ska."
    scene w2_8315 with dissolve
    mc "So, just between us, how are you doing?"
    scene w2_8316 with dissolve
    hana "I'm not sure actually, but you'll be the first to know when I work that out."
    scene w2_8317 with dissolve
    "That revealed all there was to know about how the rocker girl was presently feeling. There's only so much stimulation and doubt one can handle."

    if w2HanaSex == True:
        stop music fadeout 3.0
        scene w2_8318 with dissolve
        hide screen textbox2 with dissolve
        "So, I did what felt right, taking Hana's hand into mine and encircling her pale fingers with my own."
        play music "music/modern-situations.ogg"
        scene w2_8319 with dissolve
        "As if it was natural, she smiled and let it pass without comment."
        scene w2_8320 with dissolve
        hana "Feelin' bold?"
        scene w2_8321 with dissolve
        mct "(Well, almost without comment.)"
        scene w2_8322 with dissolve
        mc "I know how you're feeling. My brain's a bowl of alphabet soup right now too."
        scene w2_8323 with dissolve
        hana "Yeah, I bet. It's kinda like I just got done playing a two-hour set, except my arms aren't on fire."
        scene w2_8324 with dissolve
        hana "You wanna know what's been screwing with me the most tonight? I realized, in my head, I've been making this whole thing about me."
        hana "Like... I've been so preoccupied with feeling like an immoral sell out, that Rosalind, Veronica, and even that weirdo Blondie, felt secondary. I'm... starting to doubt why I even object to working here."
        scene w2_8325 with dissolve
        mc "You're being too hard on yourself. You know why you object."
        hana "Do I?"
        hana "Maybe I do..."
        scene w2_8326 with dissolve
        mc "I saw you buzz around the girls tonight, putting in the effort to understand the whys."
        scene w2_8327 with dissolve
        hana "Honestly, more than being concerned about them, I think I might have been trying to make myself feel better."
        scene w2_8326 with dissolve
        mc "There's no selfless act made without using yourself as a frame of reference. {i}The important thing is what you do{/i}."
        scene w2_8327 with dissolve
        hana "Isn't why we do something important?"
        scene w2_8326 with dissolve
        mc "Isn't the {i}why{/i} because of your mom's illness?"
        scene w2_8327 with dissolve
        hana "The funny thing is she'd be pissed if she knew I had anything to do with my old man..."
        scene w2_8328 with dissolve
        hana "Hey! I've decided!"
        scene w2_8329 with dissolve
        mc "Decided on what?"
        scene w2_8328 with dissolve
        hana "Let's go on a date tomorrow night. Like a date-date, just you and me, and nothing else."
        scene w2_8329 with dissolve
        mc "That's... surprising. Aren't you still hung up about me and the job? Nothing's changed."
        scene w2_8330 with dissolve
        hana "Ah, fuck that! I'm not going to let this place dictate what I do. All I could think about tonight was getting out of here and doing something fucking normal."
        scene w2_8331 with dissolve
        mc "You can easily find a guy who'snot-"
        scene w2_8330 with dissolve
        hana "I don't care. I want to go out with you."
        scene w2_8331 with dissolve
        mc "I, ah..."
        "The sad thing, that I didn't point out, was that without our connection to this place, a girl like Hana would find me utterly boring."
        scene w2_8330 with dissolve
        hana "Come on. For one night, I'd like to have fun like a normal person, and forget this place even exists. Seriously - no mention of it, from either of us. Slap me if I bring it up!"
        scene w2_8328 with dissolve
        hana "So, you in?"
        scene w2_8329 with dissolve
        mc "How can I say no to a proposal like that?"
        scene w2_8328 with dissolve
        hana "Great...!"
        scene w2_8333 with dissolve
        "She hugged me with an exuberance that made it better than any kiss."
        scene w2_8332 with dissolve
        hana "Thank you, [mcf]!"
        scene w2_8334 with dissolve
        mc "So... where are we going?"
        scene w2_8335 with dissolve
        hana "Umm..."
        scene w2_8336 with dissolve
        hana "I don't know. I haven't been on a date since high school. Since you're the man, why don't you come up with something?"
        scene w2_8337 with dissolve
        mc "You only use gender roles when it suits you."
        scene w2_8338 with dissolve
        hana "Yup."
        scene w2_8337 with dissolve
        mc "Alright, but you can't complain that anything I pick is boring."
        scene w2_8336 with dissolve
        hana "I'll be happy with anything. Promise."
        stop music fadeout 3.0
        "......"
        "..."
    else:

        scene w2_8339 with dissolve
        hana "You wanna know what's been screwing with me the most tonight? I realized, in my head, I've been making this whole thing about me."
        hana "Like... I've been so preoccupied with feeling like an immoral sell out, that Rosalind, Veronica, and even that weirdo Blondie, felt secondary. I'm... starting to doubt why I even object to working here."
        scene w2_8340 with dissolve
        mc "You're being too hard on yourself. You know why you object."
        scene w2_8339 with dissolve
        hana "Do I?"
        hana "Maybe I do..."
        scene w2_8340 with dissolve
        mc "I saw you buzz around the girls tonight, putting in the effort to understand the whys."
        scene w2_8339 with dissolve
        hana "Honestly, more than being concerned about them, I think I might have been trying to make myself feel better."
        scene w2_8340 with dissolve
        mc "I don't mean this cynically, but even if you threw yourself on a grenade to save their lives, you'd be doing it because of YOU. There's no selfless act made without using yourself as a frame of reference."
        scene w2_8341 with dissolve
        hana "Isn't why we do something important?"
        scene w2_8340 with dissolve
        mc "Isn't the {i}why{/i} because of your mom's illness?"
        scene w2_8339 with dissolve
        hana "The funny thing is she'd be pissed if she knew I had anything to do with my old man."
        scene w2_8342 with dissolve
        "......."
        "..."

    scene w2_8343 with dissolve
    hana "You heading out?"
    mc "No, I want to, but I think I'm going to clean myself up, hang around and check up on the girls. What about you?"
    hana "I'm getting the fuck out of here. Think I'm going to pick up some fried chicken, and have a late dinner with my mom."
    scene w2_8344 with dissolve
    mc "Tonight does have a way of making you want to do that. Won't your dad be looking for you though?"
    hana "Like I give a fuck if he is."
    scene black with fade
    mc "Yeah, what was I thinking? Have a good time."

    if w2HanaSex == True:
        hana "See you tomorrow, [mcf]."
    else:
        hana "See you later, [mcf]."

    "Forty minutes later..."
    play music "music/doll-dancing.ogg"
    scene w2_8345 with wet
    show screen textbox2 with dissolve
    "Once I was alone, soaking in my own filth, I began to carefully consider a question that had been gnawing at my mind ever since I parted ways with Hana."
    "The questions she asked shone a light on an uncomfortable truth about myself."
    "{i}Isn't why we do something important?{/i}"
    "I had always been preoccupied with simply doing and appearing good, and my seeming difficulty to do even that, that I never saw the point in pondering that in a practical sense."
    "I {b}knew{/b} what was inside my soul and I can't change that, can I?"


    if w2ExEmmaFavorSolo == True:
        scene w2_8346 with dissolve
        mc "Hmmm...?"
        scene w2_8347 with dissolve
        "I didn't know the number, but the message contained a video of Emma."
        "She had done as I asked."
        scene w2_8348 with dissolve
        "I didn't even bother watching it, I just needed it in case she got any shit for disappearing."

    scene w2_8349 with dissolve
    mct "(...was genuinely wrestling with that question the difference between me and a truly good person like Hana?)"
    "She reflected on the {i}why{/i}, bogging herself down with self-doubt, while I didn't even try."
    "...what was better? My reticent acceptance of my situation or her perpetual misgivings?"
    scene black with fade
    "Did it even matter? We're both on the some slippery slope here - what difference does the type of hand-wringing you do even make?"
    scene w2_8350 with dissolve
    "After that, I thought about a lot of things."
    "I considered why August was so hell-bent on forcing his daughter into a life she obviously didn't want."

    if w2ExEmmaFavorChuck == True or w2ExEmmaFavorSolo == True or w2ExEmmaFavorIan == True:
        scene w2_8351 with dissolve
        "I thought about Emma, her bruises, and the meaningless favor of giving her a break."
        scene w2_8352 with dissolve
        mc "Eheh, I never know what to go for..."
        "I thought about how appreciative Jacob looked, despite the fact that tomorrow and the days past that, she'll still work here."
        scene w2_8353 with dissolve
        "It was only a small temporary relief."
    else:
        "I thought about the house girls, their many faces and unknowable circumstances."
        "I thought of Yoo-ri's baby that will grow up having no idea which of these bastards his father is."

    scene black with fade
    "I thought a lot about the Carnations too, all the thinking I had put off all night."
    scene w2_8407 with pixellate
    "I thought of Veronica clinging desperately to the one thing she had left, having her past put on display for everyone's amusement."
    scene w2_8412 with dissolve
    "I thought of how dreary and worn down she looked in the shower."
    scene w2_8408 with dissolve
    "I thought of Felicia who, so unable to find contentment, had thrown herself into absurdity."
    scene w2_8409 with dissolve
    "...and of course, there was Rose. What needed to be said about that and the parallels my mind made?"
    scene w2_8354 with pixellate
    mc "Shit, is it just you?"
    ver "You disappointed to see me?"
    mc "I was hoping to check in on all of you."
    scene w2_8355 with dissolve
    ver "They already left. Like fifteen minutes ago."
    ver "Sorry, it's just me."
    mc "No, I'm glad to find at least one of you, but how come you're still here?"
    scene w2_8356 with dissolve
    ver "I... don't know."
    scene w2_8357 with dissolve
    "The answer I was imagining was sad. It's not like she had a home, once she left here, she would likely go lay her head down within the same four walls that brought her here."
    scene w2_8358 with dissolve
    mc "How are you doing?"
    scene w2_8356 with dissolve
    ver "Fine."
    scene w2_8358 with dissolve
    mc "Just fine?"
    scene w2_8360 with dissolve
    ver "Not {i}just{/i} fine. {b}I'm fine{/b}."
    scene w2_8359 with dissolve
    "Suddenly, I thought about where I was going to lay my own head down tonight."
    scene w2_8361 with dissolve
    mc "Of course you are."
    scene w2_8359 with dissolve
    "It was comparatively less drab, but dingy none-the-less."
    scene w2_8361 with dissolve
    mc "You should get dressed."
    scene w2_8360 with dissolve
    ver "I'm working on it."
    scene w2_8359 with dissolve
    "Would I go home alone and brood like I did last week? I didn't want to."
    "...and why should I? I wasn't alone and I didn't have to be."
    hide screen textbox2 with dissolve
    $ mod_var_1 = False
    $ mod_var_2 = False
    $ mod_var_3 = False
    menu w2ExEnding:
        "[mod_option] All":
            $ mod_week2_ending = True
            scene black with fade
            m_dev "Hey my Master wanted me to explain something about this choice"
            m_dev "So playing all these aren't going to make sense with the story, for all events you meet the requirements for will be played back to back until the last one"
            m_dev "So there will be weird \"time jumps\" if you aren't ok with that rollback now and pick a different option"
            m_dev "Still here? Ok let's start with the first \"ending\" I'll see you at the end of it, now back to the game"
            if w2MinaLovers and not mod_var_1:
                $ mod_var_1 = True
                jump mod_w2ExEnding_mina
            label mod_w2ExEnding_main:
                if veronicaFriend and not mod_var_2:
                    $ mod_var_2 = True
                    jump mod_w2ExEnding_vero
                elif not mod_var_3:
                    $ mod_var_3 = True
                    jump mod_w2ExEnding_kat
                else:
                    $ mod_var_1 = False
                    $ mod_var_2 = False
                    $ mod_var_3 = False
                    jump mod_w2ExEnding_mom
        "{color=#FF1493}[[Lovers]{/color} Go visit Mina(if w2minalovers=true){vspace=50}."(chg=["mina_up3"]) if w2MinaLovers == True:
            label mod_w2ExEnding_mina:
            $ Mina_Affection += 3
            scene w2_8361 with dissolve
            show screen textbox2 with dissolve
            mc "Sorry to annoy, but if you ever need to talk, I'll listen."
            mc "I mean, you might doubt my motives, but... it can be good to just have another human being to talk to, even if they can't really help."

            if veronicaFriend == True:
                scene w2_8362 with dissolve
                ver "You think just because I...!"
                scene w2_8363 with dissolve
                ver "Thanks, [mcf]. I might just take you up on that sometime."
            else:
                scene w2_8356 with dissolve
                ver "Yeah, maybe..."

            scene w2_8358 with dissolve
            mc "I'll get out of your hair then."
            scene w2_8357 with dissolve
            "She was clearly out-of-sorts, but I couldn't force anything."
            scene w2_8356 with dissolve
            ver "Good night, errand boy."
            stop music fadeout 3.0
            scene black with fade
            "And free from this place, I went to seek out a little bit of the comfort I enjoyed yesterday."
            "In hopes of getting Veronica's sullen face out of my mind."
            jump w2ExMinaEnding

        "{color=#FF1493}[[Friends]{/color} Invite Veronica home."(chg=["veronica_up4"]) if veronicaFriend == True:
            label mod_w2ExEnding_vero:
            $ Veronica_Affection += 4
            scene w2_8361 with dissolve
            show screen textbox2 with dissolve
            mc "Come over and let me cook you dinner."
            scene w2_8362 with dissolve
            ver "You think just because we talked earlier when I was--"
            scene w2_8361 with dissolve
            mc "You look like you can use a home-cooked meal and place other than your gym to sleep for the night."
            scene w2_8363 with dissolve
            ver "...am I that fucking obvious?"
            scene w2_8365 with dissolve
            mc "Would it make you feel better if I say you're a fount of stoic beauty, but my powers of observation are unbeatable?"
            scene w2_8364 with dissolve
            ver "..."
            scene w2_8365 with dissolve
            mc "Yeah, you're kinda fucking obvious, Veronica. Just like anyone else would be."
            mc "Don't take it too hard, just say yes and let me feed you."
            scene w2_8364 with dissolve
            ver "..."
            scene w2_8365 with dissolve
            mc "I'm a pretty damn good--"
            scene w2_8363 with dissolve
            ver "Okay."
            scene w2_8361 with dissolve
            mc "O-oh, y-yeah?"
            scene w2_8359 with dissolve
            "I wanted her to, but I did not expect her to accept."
            scene w2_8360 with dissolve
            ver "This isn't a ploy to fuck me, right?"
            scene w2_8361 with dissolve
            mc "No! Just get dressed and let's get out of here."
            scene black with fade
            stop music fadeout 3.0
            mc "Uh, you drove right...? I don't..."
            "My good deed for the day."
            jump w2ExVeronicaEnding
        "Seek advice from Kathleen.":

            label mod_w2ExEnding_kat:
            $ w2ExKathleenAdvice = True
            scene w2_8361 with dissolve
            show screen textbox2 with dissolve
            mc "Sorry to annoy, but if you ever need to talk, I'll listen."
            mc "I mean, you might doubt my motives, but... it can be good to just have another human being to talk to, even if they can't really help."

            if veronicaFriend == True:
                scene w2_8362 with dissolve
                ver "You think just because I...!"
                scene w2_8363 with dissolve
                ver "Thanks, [mcf]. I might just take you up on that sometime."
            else:
                scene w2_8356 with dissolve
                ver "Yeah, maybe..."

            scene w2_8358 with dissolve
            mc "I'll get out of your hair then."
            scene w2_8357 with dissolve
            "She was clearly out-of-sorts, but I couldn't force anything."
            scene w2_8356 with dissolve
            ver "Good night, errand boy."
            stop music fadeout 3.0
            scene black with fade
            "And having effected absolutely nothing positive in the red-head, I made the dubious decision to seek out Mrs. Pulman."
            jump w2ExKathleenEnding
        "Go crash at your mom's.":

            label mod_w2ExEnding_mom:
            $ w2ExMomConcern = True
            scene w2_8361 with dissolve
            show screen textbox2 with dissolve
            mc "Sorry to annoy, but if you ever need to talk, I'll listen."
            mc "I mean, you might doubt my motives, but... it can be good to just have another human being to talk to, even if they can't really help."

            if veronicaFriend == True:
                scene w2_8362 with dissolve
                ver "You think just because I...!"
                scene w2_8363 with dissolve
                ver "Thanks, [mcf]. I might just take you up on that sometime."
            else:
                scene w2_8356 with dissolve
                ver "Yeah, maybe..."

            scene w2_8358 with dissolve
            mc "I'll get out of your hair then."
            scene w2_8357 with dissolve
            "She was clearly out-of-sorts, but I couldn't force anything."
            scene w2_8356 with dissolve
            ver "Good night, errand boy."
            scene black with fade
            "And free from this place, I went to seek out the one person I never had any doubts around."
            jump w2ExVictoriaEnding

        "{color=#696969}[[Lovers] Go visit Mina.{/color}" if w2MinaLovers == False:
            jump w2ExEnding

        "{color=#696969}[[Friends] Invite Veronica home.{/color}" if veronicaFriend == False:
            jump w2ExEnding

label w2ExMinaEnding:
    $ w2ExEndingMina = True
    play sound "sound effects/door-knock.wav"
    "*Knock, knock*"
    "Mina's apartment."
    mina "[mcf]...? What are you-- Come in."
    play music "music/jazz-piano-bar.ogg"
    scene w2_8241 with fade
    mc "Should I have called?"
    mina "No, it's cool. I was actually just thinking about you. What's--"
    scene w2_8242 with dissolve
    mina "--uuuuuup. He-heh..."
    mina "I never took you for a surprise hugger. Is everything alright?"
    mc "I just wanted to see you."
    mina "O-oh... I s-see... you just come out with it, huh?"
    scene w2_8243 with dissolve
    mina "...now I feel stupid for not calling you today."
    scene w2_8244 with dissolve
    mc "What do you mean?"
    scene w2_8243 with dissolve
    mina "I wanted to, I reeeeeally did, but I didn't want you to think I was too clingy or misunderstood things..."
    scene w2_8244 with dissolve
    mc "Why would I think that?"
    scene w2_8245 with dissolve
    mina "Y'know, after... well, after what we did..."
    scene w2_8246 with dissolve
    mc "You're way too hot to be worried about that, idiot."
    scene w2_8247 with dissolve
    mina "Looks got nothin' to do with it..."
    scene w2_8248 with dissolve
    mc "Invite me in to sit down?"
    scene w2_8249 with dissolve
    mina "Oh, right! Sorry!"
    scene w2_8250 with dissolve
    mina "Can I get you anything? A drink or..."
    scene w2_8251 with dissolve
    mc "There is something I want."
    scene w2_8252 with dissolve
    mina "Oh, it's..."
    mina "It's one of those kind of visits? I need to take a shower first."
    scene w2_8253 with dissolve
    mc "Don't be stupid. Just sit down."
    mina "O-okay, I guess...."
    scene black with fade
    mina "Just take it-- eeeeh, what are you doing?"
    scene w2_8254 with fade
    mc "......"
    mc "..."
    scene w2_8255 with dissolve
    mina "What am I supposed to make of this?!"
    scene w2_8256 with dissolve
    mc "Sorry for imposing."
    scene w2_8255 with dissolve
    mina "N-no! That's okay, it's just I thought that you were here to..."
    scene w2_8257 with dissolve
    mina "Ah... more importantly..."
    mina "Something IS the matter, isn't it?"
    scene w2_8258 with dissolve
    mc "Just a heavy day."
    scene w2_8257 with dissolve
    mina "Tell me about it."
    scene w2_8258 with dissolve
    mc "I... can't."
    hide screen textbox2 with dissolve
    scene w2_8259 with dissolve
    mina "Oh. I didn't mean to pry."
    scene w2_8260 with dissolve
    mc "It's just the details aren't important. What I can tell you is, I'm really good at shutting my feelings off, but sometimes..."
    scene w2_8261 with dissolve
    mina "It hits you all at once?"
    scene w2_8262 with dissolve
    mc "Yes."
    scene w2_8261 with dissolve
    mina "I can relate."
    scene w2_8262 with dissolve
    mc "I thought you might. You remember the other day when you asked me if I doubted the way I felt about things?"
    scene w2_8263 with dissolve
    mina "Of course I do and if I remember correctly, you answered me \"sometimes\"..."
    mina "Today was one of those days, huh? They sure fuckin' suck."
    scene w2_8264 with dissolve
    mc "Ah, this is stupid--"
    scene w2_8265 with dissolve
    mina "Hush! You don't need to say anything else. Just..."
    mina "Just close your eyes."
    scene w2_8266 with dissolve
    mc "Alright..."
    scene black with fade
    mc "What now?"
    mina "Think about the things that make you truly happy. The ones that just immediately come to mind without any doubt."
    mina "Can you think of any?"
    mc "Yes..."
    mct "(I can think of a few...)"
    hide screen textbox2 with dissolve
    scene w2_8267 with pixellate
    movie "The impulse had become irresistible. There was only one answer to the fury that tortured him..."
    kil "Don't you have this in Italian?"
    vic "What are you talking about? The English ADR is part of the charm!"
    scene w2_8268 with pixellate
    dylan "What are you going to do with--"
    scene w2_8269 with pixellate
    marlow "Say ~cheese!"
    scene w2_8410 with pixellate
    pause
    scene w2_8411 with pixellate
    pause
    scene w2_8270 with pixellate
    mc "Okay, but what about them?"
    scene w2_8271 with dissolve
    mina "Just think of the person you were during those moments, of all the things they had in common, and latch onto those feelings again. Maybe even... {b}try and be that person from your memories?{/b}"
    scene w2_8272 with dissolve
    mc "Does that help you?"
    scene w2_8273 with dissolve
    mina "Sometimes, but not always."
    scene w2_8274 with dissolve
    mc "Next week, I can't be that person..."
    scene w2_8275 with dissolve
    mina "Who cares about next week? Just try and be that person right now."
    scene black with fade
    mc "Mina..."
    scene w2_8276 with dissolve
    mina "I'm glad to have met you."
    mina "Very glad..."
    mc "Can we... stay like this for a while?"
    mina "As long as you want. Until you fall asleep even..."
    "I'm glad to have met you too, Mina."
    scene black with fade
    mina "Sleep well, [mcf]."
    "One notable thing about me was..."
    "......"
    "..."
    "No matter what, I never had any trouble sleeping."
    stop music
    jump w3MinaStart

label w2ExVictoriaEnding:

    play sound "sound effects/door-knock.wav"
    "*Knock, knock*"
    vic "Eh? What are you doing here at this hour, [mcf]?"
    scene w2_8277 with dissolve
    mc "I'm not interrupting a hot date, am I?"
    scene w2_8278 with dissolve
    vic "You are, actually!"
    scene w2_8279 with dissolve
    "......"
    "..."
    scene w2_8280 with dissolve
    mc "Who's the director?"
    scene w2_8278 with dissolve
    vic "Umberto Lenzi."
    scene w2_8280 with dissolve
    mc "Cannibal Ferox?"
    scene w2_8281 with dissolve
    vic "You got it in one guess, I suppose I raised you right after all."
    mc "You do love that one, you damn sicko."
    scene w2_8282 with dissolve
    vic "...but why are you here? You look... {i}tired{/i} [mcf]."
    scene w2_8283 with dissolve
    mc "I thought... I thought we could order some fried chicken and watch a movie."
    scene w2_8282 with dissolve
    vic "Are you ok--"
    scene w2_8284 with dissolve
    "......."
    "..."
    scene w2_8285 with dissolve
    vic "I'm very, very {b}happy{/b} you're here, hun."
    scene black with fade
    "My mother had the talent of knowing what to say and what not to say, never making a bigger deal out of something than the person she was talking to wanted."
    "...and half way through Black Sunday--"
    scene w2_8286 with dissolve
    vic "Oh, [mcf]..."
    "I fell asleep."
    scene black with fade
    "I never had any trouble sleeping did I?"
    "......"
    "..."
    vic "What the hell have you gotten yourself into?"
    stop music
    jump w3VictoriaStart

label w2ExVeronicaEnding:
    $ w2ExEndingVeronica = True
    play music "music/jazz-piano-bar.ogg"
    scene w2_8366 with fade
    ver "Are your parents loaded?"
    scene w2_8367 with dissolve
    mc "Not in the least."
    scene w2_8368 with dissolve
    ver "The club pays THIS well?"
    scene w2_8369 with dissolve
    mc "Not enough to afford an industrial loft in the city. This place isn't in my name, it's the club's actually, I'm just squatting here for the time being."
    scene w2_8370 with dissolve
    ver "Must be nice..."
    scene w2_8369 with dissolve
    mc "It's too much space for a single person in my opinion."
    scene w2_8371 with dissolve
    mc "You... actually did me a favor when you accepted my invite. I didn't really want to come home alone tonight."
    scene w2_8372 with dissolve
    ver "You say that to all the women you bring home?"
    scene w2_8373 with dissolve
    mc "Of course not. You think someone like me has ever successfully picked up a woman before?"
    scene w2_8374 with dissolve
    ver "What do you mean someone like you? You're not bad looking... a bit lanky, but you're surprisingly toned."
    scene w2_8375 with dissolve
    mc "I wasn't fishing for a compliment."
    scene w2_8376 with dissolve
    ver "I wasn't giving you one, just an observation."
    scene w2_8377 with dissolve
    mc "Well, thank you for the observation."
    scene w2_8378 with dissolve
    "......"
    "..."
    scene w2_8379 with dissolve
    ver "So... uh... I'm fucking starving, can we...?"
    "Right. She's here for food."
    scene w2_8380 with dissolve
    mc "You have any food allergies?"
    scene black with fade
    "We ate in relative silence, Veronica often looking like she wanted to say something but never quite finding the words, just like the quiet drive here."
    scene w2_8381 with fade
    ver "Fuck me, I ate too much... "
    mc "You'll work it off tomorrow I'm sure."
    ver "Fuck no, I won't. I'm not doing jack shit tomorrow."
    scene w2_8382 with dissolve
    mc "Good, take care of your head."
    scene w2_8383 with dissolve
    ver "The food was... {i}okay{/i}... by the way."
    scene w2_8384 with dissolve
    mc "You ate a lot for it being \"okay\"."
    scene w2_8383 with dissolve
    ver "I didn't realize how hungry I was until you asked me to eat."
    scene w2_8385 with dissolve
    mc "..."
    scene w2_8386 with dissolve
    ver "Okay, fine! It was good!"
    scene w2_8387 with dissolve
    mc "Thank you."
    mc "It's always good to hear."
    scene w2_8388 with dissolve
    ver "You'd be surprised at how many people don't know how to cook. Like even into their 40s..."
    ver "I'm actually a little impressed."
    scene w2_8389 with dissolve
    mc "That's a low bar..."
    scene w2_8390 with dissolve
    ver "I know, right? It's an essential life skill, but so many of my clients act like looking after their diet is asking too much."
    scene w2_8391 with dissolve
    ver "Like they're genuinely perplexed by how to steam a vegetable."
    scene w2_8392 with dissolve
    mc "Yeah, it's outrageous. You have your mom cook for you until you go off to college and then when you're out on your own, instead of learning how to do it, you build poor habits by eating cheap and easy foods."
    scene w2_8393 with dissolve
    mc "Did you know eating too much junk food can alter your brain chemistry?"
    scene w2_8391 with dissolve
    ver "Of course I know that, that's my job. You're preaching to the choir right now."
    scene w2_8390 with dissolve
    ver "I didn't know you were so health conscious."
    scene w2_8392 with dissolve
    mc "I'm not a nut, but... well, a fat doctor doesn't really inspire confidence."
    scene w2_8391 with dissolve
    ver "People don't realize the success of their goals is tied to many, many small personal choices. Your choices turn into habits and many habits form a lifestyle."
    scene w2_8390 with dissolve
    ver "It's wise that you're working backwards from what you want. You have a good head on your shoulders."
    scene w2_8394 with dissolve
    "Goals. Aspirations. Dreams."
    "That was the one topic, more than others, that made me feel connected to the run-ragged redhead next to me."
    scene w2_8395 with dissolve
    mc "You're just full of \"observations\" tonight."
    scene w2_8396 with dissolve

    if VeroFlag == True:
        "Samson's earlier revelation came to mind, and I certainly wouldn't do it now, but I did wonder if {i}ever{/i} telling Veronica about her coach's {i}hot potato{/i} would do her any good?"
        "I wanted to help her, but I still didn't know how..."

    scene w2_8397 with dissolve
    ver "THAT one was a compliment, errand boy."
    scene w2_8398 with dissolve
    mc "Am I blushing?"
    ver "Nope!"
    scene w2_8399 with dissolve
    ver "Say, you don't mind if I borrow this, do you? As I understand it, this is your job."
    scene w2_8400 with dissolve
    mc "...it's yours, for as long as you like."
    scene w2_8401 with dissolve
    "Any port in the storm they say."
    "She probably didn't trust me, but by way of human warmth, I was presently the only choice."
    scene w2_8402 with dissolve
    ver "I'm... so very, very tired."
    scene w2_8403 with dissolve
    mc "You have a very good reason to be, but there's nothing left that you can affect for today, except getting some needed rest."
    mc "So clear your head and let go for now."
    scene w2_8401 with dissolve
    "......"
    "..."
    scene w2_8404 with dissolve
    ver "This isn't very comfortable. {b}Lay down{/b}."
    "I did so, without complaint."
    scene w2_8405 with dissolve
    "It was a humid summer night and Veronica was a big lady, but it wasn't in me to deny her right now."
    scene w2_8406 with dissolve
    mc "Is this better?"
    scene w2_8405 with dissolve
    "Her silence was my answer and her heartbeat the timer I gradually marked my sleepy descent to."
    "Part of me hoped she'd go back to her usual stand-offish self tomorrow."
    "The other part didn't."
    "As I joined her in catching some Z's, I only had one thought..."
    scene black with fade
    "I never had any trouble sleeping did I?"
    "......"
    "..."
    stop music
    jump w3VeronicaStart
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
