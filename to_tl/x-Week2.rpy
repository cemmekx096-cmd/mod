







label june07start:
    if prBirthdayMinaGift == False and prAfterParty == True:
        scene bugfix with w20
        "Due to a bug in the initial release, older saves will not have a certain variable properly registered. Please set that now."
        hide screen textbox2 with dissolve

        menu:
            "During the after party, you told Mina your birthday.":
                $ prBirthdayMinaGift = True
                show screen textbox2 with dissolve
                "Thank you. Please enjoy the update."
            "During the after party, you declined telling Mina your birthday.":
                pass





    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionkillian01 with blinds
    $ renpy.pause(6, hard=True)
    $ date = "june07day"

    scene w2_0001 with bites
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    "After the last couple of days, sleep came easily."
    scene w2_0002 with dissolve
    show june07day with squares
    "It felt like no sooner had I closed my eyes than I was already opening them, but the night darkening my windows had been replaced by sunlight pleasantly warming my face."
    scene w2_0003 with dissolve
    play music "music/lobby-time.ogg"
    mct "(Mmh... what's that smell?)"
    "A faint smell hung in the air."
    scene w2_0004 with fade
    mct "(Something like... {b}caramelized bacon{/b}. Just like Mom used to...)"
    scene w2_0005 with dissolve
    play ambient "sound effects/bacon-sizzle.wav"
    mct "(Just like Mom used to make Ian and me after a sleepover.)"
    mc "Yo, good morning."
    kil "Happy birthday, dude."
    stop ambient fadeout 3.0
    scene w2_0006 with dissolve
    mc "Thanks. I see you let yourself in."
    kil "Yeah, you should remember to lock your door. Not everyone who creeps into your apartment will be doing it to cook you bacon."
    mc "I could've sworn I did lock it..."
    scene w2_0007 with fade
    kil "Missed you last night. You made off like a wallflower after the show ended."
    scene w2_0008 with dissolve
    mc "I had my fill of the evening."
    mc "You're up awful early, by the way. Did you even go home last night?"
    scene w2_0007 with dissolve
    kil "Ha! Yep! Had to, Mina would've been pissed if I pulled that stunt twice in the same week."
    scene w2_0008 with dissolve
    mc "What the hell, you're actually learning from your mistakes?"
    scene w2_0009 with dissolve
    kil "Here you go, our mutual favorite."
    scene w2_0010 with dissolve
    mc "Thanks, Ian."
    scene w2_0011 with dissolve
    kil "Of course, it's your birthday after all. You've got to start the day off right."
    kil "Plus, you agreed to come with me to see my mom, remember?"
    scene w2_0012 with dissolve
    mc "Ah, yeah... I did, huh? That kind of slipped my mind after last night's business."
    scene w2_0014 with dissolve
    kil "You're not going to flake, right?"
    scene w2_0012 with dissolve
    mc "No, I said I'll go with you, so I'll go. Condo or house?"
    scene w2_0013 with dissolve
    kil "House."
    scene w2_0012 with dissolve
    mc "The one in Perigrine Terrace or...?"
    scene w2_0013 with dissolve
    kil "The summer house."
    scene w2_0012 with dissolve
    mc "Dang, that's the furthest one."
    scene w2_0015 with dissolve
    kil "Don't worry. We'll be finished before lunch and I'll drop you off wherever you're meeting Vicky. Besides, my mom will be happy to see you!"
    scene w2_0012 with dissolve
    mc "Really? As far as I could tell, she hated me."
    scene w2_0014 with dissolve
    kil "She didn't hate you! She just... didn't like me hanging out with you is all."
    scene w2_0012 with dissolve
    mc "That always kind of bothered me, you know? Really fucked with my self-esteem..."
    scene w2_0014 with dissolve
    kil "Oh, shut up. No it didn't! You jumped at any chance to piss her off."
    scene w2_0012 with dissolve
    mc "Yeah, I guess it wasn't so unearned, was it?"
    scene w2_0016 with dissolve
    mc "What can I say, your mom looked fine as hell when she scolded us. Like a sexy librarian or something."
    scene w2_0017 with dissolve
    kil "Guh, not before we eat, please."
    scene w2_0018 with dissolve
    mc "What...? I'm sorry, am I making you uncomfortable?"
    scene w2_0019 with dissolve
    kil "Yeah, that's my fucking mom, you asshole! Just dig in before it gets cold!"
    scene black with fade
    "All the while enjoying the nice breakfast Ian had made me, I continued to relentlessly tease him. It was my birthday."
    stop music fadeout 3.0
    "......"
    "..."
    play sound "sound effects/door-bell.wav"
    scene w2_0020 with blinds
    "*Ding Dong*"
    mc "Eh? You don't have a key?"
    scene w2_0021 with dissolve
    kil "Not since last winter."
    scene w2_0022 with dissolve
    mc "What happened last winter?"
    scene w2_0023 with dissolve
    kil "Eheh... I don't remember all too well, but the place had to be disinfected."
    scene black with fade
    mc "Jeez..."
    maid "Ah, boys...!"
    scene w2_0024 with dissolve
    play music "music/a-brand-new-start.ogg"
    maid "What's it been? Five or six years since I last saw the pair of you together?"
    maid "You two always used to barrel through the front door after school and stomp through the house just to play your games quicker."
    scene w2_0025 with dissolve
    mc "Yeah, and you'd always ask us what the hurry was and tell us that they weren't going anywhere. How are you, Alice?"
    scene w2_0026 with dissolve
    alice "I'm good, [mcf]. A little surprised to see you."
    scene w2_0027 with dissolve
    kil "Mom wanted to catch up, so I brought him along on an errand. She's not on a call or anything is she?"
    scene w2_0028 with dissolve
    alice "No. I believe she's just freshening up. I'll go tell her you're here."
    scene w2_0029 with dissolve
    play sound "sound effects/slap3.wav"
    scene w2_0030 with hpunch
    "*Smack*"
    alice "--!"
    scene w2_0031 with dissolve
    kil "Yeah, you go do that."
    scene w2_0032 with dissolve
    "The maid had an embarrassed, mortified look on her face."
    scene w2_0033 with dissolve
    alice "M-make yourself at home..."
    scene w2_0034 with fade
    mc "What the hell was that? Of all people, you're sexually harassing Alice now?"
    kil "Heh, I guess I never told you."
    scene w2_0035 with dissolve
    mc "You really going to wait for me to ask \"told me what?\"...?"
    kil "Heh, I'm glad you asked. I tapped that about a couple of years back."
    scene w2_0036 with dissolve
    mc "Huh...? You had sex with Alice? Isn't that kinda weird? She helped raise you."
    kil "So? It wasn't like she did it out of love. She was paid to."
    scene w2_0038 with dissolve
    mc "Man, you've got issues. How the hell did that even happen?"
    scene w2_0039 with dissolve
    kil "Just kinda did. I was at the other house. I had just taken a shower and was feeling pretty horny when she walked in on me changing."
    scene w2_0038 with dissolve
    mc "Okay, but normally that's just an embarrassing situation. How'd that turn into you two screwing?"
    scene w2_0039 with dissolve
    kil "Oh, she was embarrassed. She apologized profusely, but before she could backtrack out the door, I yelled at her to stop."
    scene w2_0040 with dissolve
    kil "She got this funny look on her face. Like a deer {i}excited{/i} to be caught in the headlights. That's when I knew. I told her to close the door and get her ass in there and before long..."
    kil "I had her screaming my name. With a little prodding, I even got her to admit I was fucking her better than her dead husband ever did. Can you believe it?"
    scene w2_0038 with dissolve
    mc "No, I can't. This is just some fucked up fantasy you had as a teenager, isn't it?"
    scene w2_0041 with dissolve
    kil "I can prove it. I took some photos as a keepsake. You want me to send them to you later?"
    scene w2_0037 with dissolve
    mct "(He took photos...?)"
    hide screen textbox2 with dissolve

    menu w2KillianAliceBet:
        "Yes, because you're calling him on his bullshit." if w2Bullshit == False:
            $ w2Bullshit = True
            scene w2_0038 with dissolve
            show screen textbox2 with dissolve
            mc "Yeah, go ahead. I can just see them now... up close, grainy shots with no identifying characteristics."
            scene w2_0039 with dissolve
            kil "Fine. It's a bet then."
            scene w2_0038 with dissolve
            mc "What are we wagering?"
            scene w2_0039 with dissolve
            kil "The loser has to do what the other dares, redeemed at a point to be determined."
            scene w2_0038 with dissolve
            mc "Within reason?"
            scene w2_0040 with dissolve
            kil "No. What you consider reasonable vastly differs from what I'd call reasonable. Let's say within the blast radius of reasonable. Sound good?"
            scene w2_0037 with dissolve
            mct "(Hmm... he's sounding pretty confident about this. Do I make that wager?)"
            hide screen textbox2 with dissolve
            jump w2KillianAliceBet

        "Yes, because you have a morbid curiosity."(chg=["tough_up","killian_up"]) if w2Bullshit == False:
            $ w2AlicePhotos = True
            $ Killian_Bromance += 1
            $ toughness += 1
            scene w2_0038 with dissolve
            show screen textbox2 with dissolve
            mc "Wait, you're not kidding? Huh..."
            scene w2_0039 with dissolve
            kil "I know that look. You're interested. Want to see what pudgy, homely Alice looks like when she's creaming herself on a cock."
            scene w2_0038 with dissolve
            mc "I'd be lying to say I wasn't curious. She was always around when we were kids and she was really nice, which..."
            scene w2_0040 with dissolve
            kil "Makes it that much more perverse and twisted, am I right?"
            scene w2_0038 with dissolve
            mc "Yeah, so if you're not full of shit, I'm interested. Send me the pics."
            scene w2_0041 with dissolve
            kil "Ha! Will do, bud."


        "No, because that's scummy as hell."(chg=["tough_down","killian_down"]) if w2Bullshit == False:
            $ Killian_Bromance -= 1
            $ toughness -= 1
            scene w2_0043 with dissolve
            show screen textbox2 with dissolve
            mc "No. Why would I want to see that? That's weird and pretty damn scummy."
            scene w2_0042 with dissolve
            kil "Huh? She knows I took 'em."
            scene w2_0043 with dissolve
            mc "That's not what I'm getting at. On the slightest chance you're not full of crap, she wouldn't want you sharing them with me."
            scene w2_0042 with dissolve
            kil "Ah, whatever. Suit yourself. You're pretty picky and choosy about the shit you get moralistic about."


        "Yes, take the wager."(chg=["killian_up"]) if w2Bullshit == True:
            $ w2AlicePhotos = True
            $ w2KillianBet = True
            $ Killian_Bromance += 1
            scene w2_0038 with dissolve
            show screen textbox2 with dissolve
            mc "Okay, then. You're on. Send me the photos. If I can tell who it is, you win."
            scene w2_0039 with dissolve
            kil "And you'll do whatever I ask?"
            scene w2_0038 with dissolve
            mc "Yep, I'll do whatever you ask. Same goes the other way though, yeah?"
            scene w2_0041 with dissolve
            kil "It's a bet."

        "No, don't take the wager." if w2Bullshit == True:
            scene w2_0038 with dissolve
            show screen textbox2 with dissolve
            mc "I'm not making that wager."
            scene w2_0039 with dissolve
            kil "Is that because you believe me?"
            scene w2_0038 with dissolve
            mc "Not necessarily, but it ain't worth the risk. To be honest, I would rather not know the truth."
            scene w2_0043 with dissolve
            mc "I'd hate to know she had terrible taste in men."
            scene w2_0040 with dissolve
            kil "'ey, fuck you. I made her slutty dreams come true. I'm a giver."

    stop music fadeout 3.0
    scene w2_0044 with dissolve
    grace "This is a nice surprise. You actually brought [mcf] along."
    scene w2_0045 with dissolve
    "Cutting dangerously close to the end of our bawdy conversation, Mrs. Beaufort had appeared seemingly out of nowhere."
    scene w2_0046 with dissolve
    "It was a bit nostalgic in a way. As kids and teens, she had a habit of sneaking up on us in the midst of mischief. The woman almost had no footsteps."
    scene w2_0047 with dissolve
    kil "I said I would. You doubted it?"
    grace "You do tend to forget things."
    scene w2_0048 with dissolve
    stop sound
    grace "Hello, [mcf]. It's been some time."
    play music "music/no1-a-minor-waltz.ogg"

    scene w2_0049 with dissolve:
        subpixel True
        yalign 0.7
        xalign 0.5865
        linear 5 yalign 0.1

    mc "It has. It's nice to see you, Mrs. Beaufort. You look well."
    scene w2_0051 with dissolve
    grace "Thank you, as do you. Time has shaped you into a handsome young man."
    scene w2_0052 with dissolve
    grace "Ian told me you were pursuing a career in medicine?"
    scene w2_0050 with dissolve
    mc "I'm just pre-med right now, but I feel confident about my MCATs."
    scene w2_0052 with dissolve
    grace "Have you decided on a specialty?"
    scene w2_0050 with dissolve
    mc "Well, I've always wanted to be a general practitioner, but I've given some thought about going into research recently."
    scene w2_0052 with dissolve
    grace "Everyone's different, but I think you'd find clinical work very rewarding. I do."
    scene w2_0050 with dissolve
    mc "You don't get tired of working with kids?"
    "I thought back to my time as a tutor and how I came away from that with a stronger dislike for children."
    scene w2_0052 with dissolve
    grace "No, that'd be a dire outcome for a pediatrician I would think."
    scene w2_0053 with fade
    grace "How have you been, son?"
    kil "I've been good."
    grace "Why do I find that hard to believe?"
    scene w2_0054 with dissolve
    kil "I've got all my fingers at least."
    scene w2_0055 with dissolve
    grace "Don't be shy."
    scene w2_0056 with dissolve
    "I think I must've given Mrs. Beaufort a reflexive, dubious look."
    scene w2_0055 with dissolve
    grace "I know you do hugs, [mcf]."
    scene w2_0057 with dissolve
    "Never in my life had I given that chilly woman a hug."
    scene w2_0058 with dissolve
    grace "Thank you."
    "Maybe the distance in years had made her sentimental?"
    scene w2_0059 with dissolve
    grace "I hope coming all this way to just catch up wasn't too inconvenient for you?"
    scene w2_0060 with dissolve
    mc "No, it's nice to see you, Mrs. Beaufort."
    scene w2_0061 with dissolve
    kil "It's actually [mcf]'s birthday today."
    scene w2_0062 with dissolve
    grace "Really? If I recall, you're a year older than Ian, which means you're turning 22?"
    scene w2_0063 with dissolve
    mc "That's right."
    scene w2_0064 with dissolve
    grace "Happy birthday."
    scene w2_0065 with dissolve
    mc "Thank you."
    scene w2_0067 with dissolve
    grace "Would you like some tea?"
    scene w2_0068 with dissolve
    kil "No, we can't stay long. I just came to drop off that paperwork and then [mcf] needs to meet his mother for lunch."
    scene w2_0069 with dissolve
    grace "Can you spare ten minutes at least?"
    scene w2_0070 with dissolve
    kil "I don't-"
    mc "Of course. Ten minutes won't hurt."
    scene w2_0071 with dissolve
    grace "Good. Then I would like to ask a small favor of my son, involving removing some boxes from the attic crawl space..."
    scene black with fade
    stop music fadeout 3.0
    "..."
    mc "You sure you don't want me to help him?"
    scene w2_0072 with dissolve
    grace "No. I actually wanted us to talk."
    scene w2_0073 with dissolve
    mc "You mean catch up...?"
    scene w2_0074 with dissolve
    grace "No."
    scene w2_0075 with dissolve
    mct "(Just... no?)"
    scene w2_0076 with dissolve
    mc "What then?"
    scene w2_0077 with dissolve
    grace "Sit down, please."
    "Mrs. Beaufort had adopted a more familiar and stern tone."
    scene w2_0078 with fade
    grace "I suggested Ian bring you along today for one specific reason."
    scene w2_0079 with dissolve
    "She paused for a moment, to unblinkingly appraise me with her eyes."
    play music "music/doll-dancing.ogg" fadein 3.0
    scene w2_0078 with dissolve
    grace "I have a proposition for you."
    scene w2_0080 with dissolve
    mc "Alright..."
    scene w2_0078 with dissolve
    grace "For whatever reason, you always had a damnable hold over my son. He looked up to you, respected you, and even loved you."
    grace "That is true, even now. He told me you two are working the same part-time job and I couldn't remember the last time I heard him so genuinely happy."
    scene w2_0079 with dissolve
    mc "..."
    scene w2_0078 with dissolve
    grace "To my surprise, you've actually become a respectable adult."
    scene w2_0080 with dissolve
    mc "Thank you..."
    scene w2_0081 with dissolve
    grace "More respectable than Ian certainly. That boy isn't doing anything with his life."
    scene w2_0080 with dissolve
    mc "He's a photographer."
    scene w2_0078 with dissolve
    grace "No, he's a man-child using a camera to get laid."
    scene w2_0082 with dissolve
    mc "Eheh..."
    mct "(It's not like I could refute her assessment exactly...)"
    scene w2_0085 with dissolve
    mc "What are you getting at, Mrs. Beaufort?"
    scene w2_0086 with dissolve
    grace "Yes, we should get straight to the point before Ian returns."
    grace "I want you to use your influence over Ian to persuade him to go to college and pursue a proper career working with his father."
    scene w2_0085 with dissolve
    mc "I don't know what you imagine, but Ian doesn't just do anything I tell him. Plus, y'know, it's his life..."
    scene w2_0084 with dissolve
    grace "You have more control over my son than you give yourself credit for. I've always despised that, but now I see it could work in his advantage."
    grace "I don't know where I went wrong in raising him, but he's a philanderer and a leech. Something has got to give, his father is growing impatient."
    scene w2_0083 with dissolve
    "Hearing Ian's own mother say those things made me feel sorry for him. Not that her appraisal was necessarily wrong, but the callous way she said it put some things into perspective."
    scene w2_0085 with dissolve
    mc "Why would I do that?"
    scene w2_0086 with dissolve
    grace "I would hope it would be because he's your friend and this is what's best for him, but..."
    grace "Francis and I will pay you $5,000 if he enrolls next spring."
    scene w2_0085 with dissolve
    mc "Mr. Beaufort knows about this?"
    scene w2_0086 with dissolve
    grace "Of course. It was my idea, but he agreed with it. He wants nothing more than to give Ian a job at his firm, but he needs a degree first, if only for credibility's sake."
    scene w2_0085 with dissolve
    mc "Shouldn't you just talk to him?"
    scene w2_0084 with dissolve
    grace "I've tried dozens of times. He's impossible, so now I'm looking to you."
    scene w2_0083 with dissolve
    mct "(Jeez...)"
    scene w2_0084 with dissolve
    grace "If you don't want the money, we can find another form of restitution."
    scene w2_0086 with dissolve
    grace "For example, I know people. I could help you get into med school."
    scene w2_0085 with dissolve
    mc "..."
    scene w2_0088 with dissolve
    "All I could think was poor Ian."
    scene w2_0087 with dissolve
    mc "You do know he's turned out this way because of shit like this, right?"
    scene w2_0088 with dissolve
    grace "It's crossed my mind, but I'm not going to entertain criticism from you of all people."
    scene w2_0089 with dissolve
    mc "..."
    stop music fadeout 3.0
    scene w2_0090 with dissolve
    grace "Shoot. It sounds like Ian's finished upstairs."
    scene w2_0091 with dissolve
    grace "I don't need an answer from you. If the terms are amenable, get it done. Then we can square away your payment. Whatever you want."
    grace "If you find this reprehensible, then I only ask you please treat this conversation as having never taken place. Surely you realize Ian knowing about this would hurt--"
    play music "music/hotshot.ogg"
    scene w2_0092 with dissolve
    kil "Heh, I think I made record time."
    kil "What are you two talking about?"
    scene black with fade
    grace "Oh, he was just telling me about how Victoria is doing."
    "......"
    "..."
    scene w2_0093 with circlewipe
    play sound "sound effects/notification.wav"
    $ met_grace = True
    $ history_killian = "Playing \"catch up\" with Mrs. Beaufort was a refresher course in understanding Ian's glaring trust issues. I'm uncomfortable at the prospect of taking Ian's mother up on her offer, but maybe pushing him to be more responsible wouldn't be such a bad thing?"
    $ unread_killian = True
    show bioadd with dissolve
    $ renpy.pause(2, hard=True)
    hide bioadd
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    "On the ride back to the city, my mind was unsettled by my conversation with Mrs. Beaufort."
    hide bioupdate with dissolve
    "I did my best to engage Ian in our usual small talk, but I couldn't shake the nagging pangs of sympathy for him."
    mct "(Not that Ian couldn't use a dose of growing up, but...)"
    mct "(He'd be livid if he knew what his mother just tried to bribe me to do.)"
    scene w2_0094 with dissolve
    kil "Hey, stop spacing out."
    kil "You've been acting weird ever since we left my mom. That bitch didn't say something shitty to you, did she?"
    scene black with fade
    mc "Nah, we just talked about college. I just have other things on my mind is all."
    kil "Wanna tell me about any of 'em? Maybe talking about it will help? At the very least, I'd like to know what's going on inside your head."
    stop music fadeout 3.0
    "..."
    scene w2_0095 with blinds
    vic "I'm glad you invited Ian to join us for lunch, but it's a shame he couldn't stick around for ice cream."
    mc "It would've felt wrong not to ask him."
    play music "music/crinoline-dreams.ogg" fadein 3.0
    scene w2_0096 with dissolve
    vic "The three of us used to spend a lot of birthdays together, huh?"
    scene w2_0097 with dissolve
    mc "Stop talking like you're an old lady."
    scene w2_0098 with dissolve
    vic "I am an old lady. I've got a 22 year old son."
    scene w2_0100 with dissolve
    "She said it proudly, with a warm smile. Which pretty much put an end to the topic."
    scene w2_0096 with dissolve
    vic "How are you enjoying your new job?"
    scene w2_0097 with dissolve
    mc "I think I've gotten used to it by now. Compared to my job as a tutor, the ups outweigh the downs."
    mc "Although in some sense, I guess I've traded entitled parents for another kind of pompous asshole."
    scene w2_0099 with dissolve
    vic "It's some sort of bar, right? Could I drop in and get a cup of coffee sometime? I have to admit, having my own son wait on me would be nice..."
    scene w2_0101 with dissolve
    mc "Ah..."
    mc "Well..."
    scene w2_0102 with dissolve
    vic "Oh, don't worry! I was just kidding. You wouldn't want your mother embarrassing you."
    scene w2_0103 with dissolve
    mc "Quiet. I'd never, no matter what you did, find you embarrassing. Not even for a second."
    scene w2_0104 with dissolve
    vic "[mcf]..."
    scene w2_0105 with dissolve
    mc "..."
    vic "You're so full of it!"
    scene w2_0101 with dissolve
    mc "No, really. It's just that the place is... sort of exclusive. Men only."
    scene w2_0106 with dissolve
    vic "You're not working at some sort of strip club, are you?"
    scene w2_0107 with dissolve
    mc "No! It's like a cross between a lodge and a bar. Y'know, like a society."
    scene w2_0096 with dissolve
    vic "Like the Shriners?"
    scene w2_0097 with dissolve
    mc "Something like that..."
    scene w2_0099 with dissolve
    vic "That's great. It must be good for networking then."
    scene w2_0108 with dissolve
    mc "Yeah, that's one of the ups. How about you? How's work? How have you been?"
    "I most deliberately forced a change of topic."
    scene w2_0109 with dissolve
    vic "Nothing worth mentioning... oh! I had the nicest conversation with a stranger on the phone this morning."
    scene w2_0108 with dissolve
    mc "You had a conversation with a random caller?"
    scene w2_0112 with dissolve
    vic "Not random. It was a woman who said she was in charge of a scholarship you applied for. A, uh... Katherine Grossman?"
    scene w2_0108 with dissolve
    mc "You don't mean..."

    if toughness >= 20:
        mct "(Why the hell did that bitch...)"
    else:
        mct "(Why the hell did that woman...)"

    mc "Kathleen Pulman?"
    scene w2_0111 with dissolve
    vic "Ah-huh! That was the name. She was an extremely pleasant lady."
    scene w2_0108 with dissolve
    mc "What... did... you... two talk about, exactly?"
    scene w2_0112 with dissolve
    vic "She said it was a character reference check, but we ended up talking about a little of everything."
    scene w2_0110 with dissolve
    vic "I talked about how hard of a worker you are, shared some cute stories from when you were a kid, even told her it was your birthday today. She told me about her own children and ended up getting me to talk about myself a little."
    scene w2_0111 with dissolve
    vic "We chatted for a whole hour."
    scene w2_0108 with dissolve
    "I could feel my nose twitch in irritation and my stomach turn over on itself out of anger."
    "My new world had intersected with the old. Not by accident, either..."
    mc "That sounds nice."
    scene w2_0109 with dissolve
    vic "Yeah, it was! That or I'm starved for a social life."
    scene w2_0108 with dissolve
    mc "Did she get everything she needed?"
    scene w2_0112 with dissolve
    vic "I think so. She agreed with me that you sounded like a deserving kid."
    scene w2_0108 with dissolve
    mct "(...I'll have to ask what the fuck that was about later.)"
    "For now, I should just put it out of my mind."
    scene w2_0113 with dissolve
    vic "Do you have any special plans tonight?"
    scene w2_0114 with dissolve
    mc "No, I'm just gonna stay in. You know I don't like to do anything for my birthday."
    scene w2_0115 with dissolve
    vic "I don't know how that ever happened. You used to get so excited about them."
    mc "Yeah, when I was like 9..."
    scene w2_0116 with dissolve
    vic "You don't have to try so hard. It's okay to be uncool sometimes."
    mc "I don't think you have to worry about anyone using that word to describe me."
    vic "You should give yourself more credit."
    scene w2_0117 with dissolve
    vic "I think you're the coolest."
    vic "Happy birthday. I love you."
    mc "I love you too, mom."
    scene w2_0118 with dissolve
    vic "The ladies' room is calling."
    mc "Don't worry. I won't try and make an escape."
    scene black with fade
    play sound "sound effects/high-heel-footsteps.wav"
    vic "Good. It would be futile."



    if w2AlicePhotos == True:
        stop sound fadeout 3.0
        scene w2_0119 with dissolve
        $ history_kathleen = "Mrs. Pulman recently contacted and had an hour-long conversation with my mother, a fact that disturbs me greatly. I'll have to bring this up the next time we meet face-to-face."
        $ unread_kathleen = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve
        mct "(...)"
        hide bioupdate with dissolve
        "Just as I felt a smile coming on..."
        play sound "sound effects/sms-chime.wav"
        scene w2_0120 with dissolve
        stop music fadeout 3.0
        "*Chirp, chirp.*"
        "The face of my phone lit up and told me I had a message from Ian."
        scene w2_0121 with dissolve
        mct "(I wonder what this is about...)"
        scene w2_0122 with vpunch
        mc "-gh! *cough* -gh! *cough, chough*"
        "The message's attachment sent a shock through my system, causing me to momentarily sputter and choke on my own spit."
        play music "music/echo-sclavi.ogg"
        hide screen textbox2 with dissolve
        scene w2_0123 with pixellate
        "On screen, was Alice."
        "Mild mannered Alice, who had always been cordial to me when I was growing up, was in frame. Ian held a tight grip on one of her ankles, pulling her leg back past her shoulder and putting her wide hips and oozing cunt on display."
        "The normally frumpy-looking woman had a dopey look on her face, eyes glazed over from pleasure and lips wet with drool and who knows what else. A wad of jizz sat squarely on her deceptively shapely breasts."
        "I was caught somewhere between astonishment at my friend's shameless conquest of his former nanny and disbelief at just how much of a horndog he actually was."
        scene ice-cream-parlor with pixellate
        call phone_start_kil from _call_phone_start_kil_6


        if w2KillianBet == True:
            call message_img ("Killian", "That enough identifying characteristics for you, bud?", "killian02") from _call_message_img_7
            call reply_message ("Shit. I can't believe you fucked your old nanny. I guess you win the bet.") from _call_reply_message_31
        else:

            call message_img ("Killian", "This satisfy your curiosity, pervert?", "killian02") from _call_message_img_8
            call reply_message ("Damn, you really did it...") from _call_reply_message_32

        call message ("Killian", "I know, not my usual lay, but it doesn't hurt to throw an old bitch a bone. I like to think I did her a favor.") from _call_message_76
        call reply_message ("How magnanimous of you and your cock. You are so fucking full of yourself dude.") from _call_reply_message_33
        call message ("Killian", "You know, she might let us double team her if you want.") from _call_message_77
        call reply_message ("No thanks.") from _call_reply_message_34
        call message ("Killian", "You sure? She's pretty freaky when you get her drunk on cock. I even had her cleaning my cum off the floor with her tongue, just like a good maid.") from _call_message_78
        call reply_message ("I'm going to bow out of this conversation now.") from _call_reply_message_35

        if w2KillianBet == True:
            call message ("Killian", "Sure thing, just don't try and wiggle out of our wager later.") from _call_message_79
            call reply_message ("I wouldn't dream of it.") from _call_reply_message_36
        else:

            call message ("Killian", "Talk to you later.") from _call_message_80

        call phone_end_kil from _call_phone_end_kil_9

        scene w2_0124 with dissolve
        play sound "sound effects/high-heel-footsteps.wav"
        show screen textbox2 with dissolve
        mct "(...jeez, what the fuck is wrong with him?)"
        stop sound
        scene w2_0125 with dissolve
        vic "You tired of me yet?"
        scene w2_0126 with dissolve
        mc "Of course not, why?"
        scene w2_0125 with dissolve
        vic "I could use a walk in the park after eating all that ice cream."
        scene w2_0126 with dissolve
        mc "Let's go then."
        scene black with fade
        stop music fadeout 3.0
        "......"
        "..."
    else:

        $ history_kathleen = "Mrs. Pulman recently contacted and had an hour-long conversation with my mother, a fact that disturbs me greatly. I'll have to bring this up the next time we meet face-to-face."
        $ unread_kathleen = True
        show bioupdate with dissolve
        play sound "sound effects/notification.wav"
        stop music fadeout 3.0
        "......"
        "..."

    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionminahana01 with blinds
    $ renpy.pause(6, hard=True)
    scene w2_0127 with dissolve
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    $ date = "june07night"

    if w2AlicePhotos == True:
        "After spending my afternoon in the park with mom, I was happy to be home. Free to decompress and relax."
    else:
        "After a nice walk in the park to burn off the calories, I found myself back home. Glad to be able to decompress and relax."

    "The last week had felt jam-packed. At least to my sleepy, student standards."
    scene w2_0128 with dissolve
    show june07day with squares
    "In the last couple of days, I felt like I had tasted more of life than I had previously in my 22 years."
    play ambient "sound effects/shower.wav"
    scene w2_0129 with wet
    mct "(An evening with just me, a pizza, and a couple of movies would be appreciated...)"
    play sound "sound effects/door-bell.wav"
    "*Ding Dong*"
    scene w2_0130 with dissolve
    mc "...fuck."
    scene black with fade
    stop ambient
    play sound "sound effects/walk-wood.mp3"
    mct "(It's funny, just a few weeks ago I would've been embarrassed to answer the door like this, but that notion seems so... quaint now.)"
    stop sound
    scene w2_0132 with w20
    mc "Who is it?"
    scene w2_0131 with dissolve
    hana "Your favorite bartender. Open up."
    play sound "sound effects/door-openclose.wav"
    play music "music/everything-you-wanted.ogg"

    scene w2_0133 with fade:
        subpixel True
        yalign 0.7
        xalign 0.5865
        linear 5 yalign 0.1

    hana "Whoa, there. You're not dressed? I'm definitely here on time..."
    scene w2_0134 with dissolve
    hana "Opening the door with only a towel on... this isn't some half-assed attempt to seduce me, is it?"
    scene w2_0135 with dissolve
    mc "On time for what?"
    scene w2_0136 with dissolve
    hana "Ian said it was your birthday. Gave me your address and a time to get here... nice place, by the way."
    scene w2_0137 with dissolve
    mc "Thanks, but it belongs to the club."
    scene w2_0138 with dissolve
    hana "Heh, I guess my dad has both of us bought and paid for."
    scene w2_0139 with dissolve
    mc "I was actually planning on spending the night alone."
    hana "I can dig the value of a lil' alone time, but no offense, that sounds pretty sad."
    scene w2_0140 with dissolve
    mc "What did Ian tell you exactly?"
    hana "He said you were having a small get together. Nothing big, just a few people."

    if hanaFlag == True:
        hana "You were nice enough to come to my gig this week, so I thought I would pay you back and return the favor."
    else:
        hana "I figured I'd be a good co-worker and stop by."

    scene w2_0141 with dissolve
    mc "That's news to me."
    scene w2_0142 with dissolve
    hana "Maybe it was supposed to be a surprise party?"
    scene w2_0143 with dissolve
    mc "Pretty piss poor execution if it is."
    scene w2_0142 with dissolve
    hana "You sound a little iffy..."
    scene w2_0144 with dissolve
    hide screen textbox2 with dissolve
    hana "I did come ALL this way, but do you want me to go?"
    scene w2_0145 with dissolve
    "Hana stuck out her chest and batted her eyes at me in an atypical display of her womanly wiles."
    mc "What kind of man would I be if I turned you away?"
    scene w2_0146 with dissolve
    hana "A foolish one."
    scene w2_0147 with dissolve
    mc "Make yourself at home. I'm going to go get dressed."
    mc "Help yourself to the fridge."
    scene w2_0148 with fade
    show screen textbox2 with dissolve
    hana "What did you have planned for all by your lonesome?"
    scene w2_0149 with dissolve
    mc "Movies. A double bill, actually. You interested?"
    scene w2_0148 with dissolve
    hana "Double features can be fun. What were you thinking?"
    scene w2_0150 with dissolve
    mc "The first is {i}Tampopo{/i}, a movie by Juzo Itami. It starred his wife in the titular role, playing a proprietress of a struggling noodle shop."
    mc "It has the peculiar distinction of being the first \"ramen\" western. Get it?"
    scene w2_0152 with dissolve
    hana "Yeah, that's funny."
    scene w2_0151 with dissolve
    mc "It's a movie that always puts a smile on my face."
    scene w2_0152 with dissolve
    hana "What's the other half of the bill?"
    scene w2_0153 with dissolve
    mc "The second film is a fun, satirical look at 80s American consumerism: {i}The Stuff{/i}."
    scene w2_0154 with dissolve
    mc "It's about an addictive cream-like alien substance that is put on grocery store shelves and sold to the general public, gradually turning the masses into mind-controlled zombies."
    scene w2_0155 with dissolve
    scene w2_0156 with dissolve
    hana "That's the guy who did Q the Winged Serpent, right? That's Spider's favorite movie."
    mc "Correct. Those two movies not only share the same director, but also the same star."
    scene w2_0157 with dissolve
    mc "Can you guess what links the two?"
    scene w2_0158 with dissolve
    stop music fadeout 3.0
    hana "You made it pretty easy to guess: {b}food{/b}."
    scene w2_0159 with dissolve
    mc "Bingo! So, you hungry?"
    scene black with fade
    play sound "sound effects/bacon-sizzle.wav"
    "..."
    stop sound fadeout 2.0
    hana "What the hell? This tastes awesome."
    scene w2_0160 with dissolve
    mc "Thanks."
    hana "Where'd you learn to cook like this?"
    scene w2_0161 with dissolve
    mc "Byproduct of being raised by a single mother I guess."

    if hanaFlag == True:
        mc "You can relate, right?"
        scene w2_0162 with dissolve
        hana "Nah. My grandfather did all the cooking when he was alive. After that, it was always takeout for my mom and I."
    else:
        scene w2_0162 with dissolve
        hana "I wish I could say the same. My grandfather did all the cooking when he was alive. After that, it was always takeout for my mom and I."

    if w1ExGame3Avoid == True:
        scene w2_0163 with dissolve
        mc "Right. Your grandfather. You told me about him."

    scene w2_0164 with dissolve
    hana "I mean, I can cook enough to sustain myself, but this is surprisingly delicious. Consider me impressed."
    scene w2_0163 with dissolve
    mc "It really isn't that impressive."
    scene w2_0165 with dissolve
    hana "Take the compliment you dork."
    play sound "sound effects/door-bell.wav"
    scene w2_0166 with dissolve
    "*Ding Dong*"
    kil "Coming in!"
    play sound "sound effects/door-openclose.wav"
    play music "music/sugar-zone.ogg"
    scene w2_0167 with wipeleft
    kil "Aw, damn. I never catch you doing anything fun."
    scene w2_0168 with dissolve
    mina "Sorry about barging in!"
    "Mina quickly elbowed past her boyfriend and apologetically gave a little bow."
    scene w2_0169 with dissolve
    mina "You know how he is..."
    mina "Hello, [mcf]! Happy birthday!"
    scene w2_0170 with dissolve
    mc "Thank you, Mina. How are you?"
    scene w2_0169 with dissolve
    mina "I'm great! Still riding the excitement from getting the part yesterday!"
    scene w2_0171 with fade
    kil "I know you'd rather be by yourself tonight, but fuck that! You're my best friend!"
    kil "I can't just let that pass. Plus, we brought presents and cake. So no bitching, okay?"
    mc "Okay, no bitching."
    scene w2_0172 with dissolve
    kil "Plus, I invited Hana. You two seemed to get along pretty well yesterday."

    if hanaFlag == False:
        mct "(He's really misreading things there... I've got no interest in her like that.)"

    kil "Personally, I can't stand that bitch, but that's got nothing to do with getting you laid. I even told her the wrong time so you two could get some 1-on-1 time and work your charm before we got here."
    scene w2_0173 with dissolve
    mc "Uh, thanks..."
    scene w2_0174 with dissolve
    mina "Eeeey, what are you two whispering about?"
    hana "You're probably better off not knowing."
    mina "Oh! Right! We haven't been introduced yet."
    scene w2_0175 with dissolve
    "With a cute hop, Mina bounded toward Hana and closed the distance between them."
    scene w2_0176 with dissolve
    hana "No, we haven't..."
    scene w2_0177 with dissolve
    "Hana ran her gaze down Mina's body from top to bottom, as if making a careful appraisal of the bubbly woman."
    scene w2_0176 with dissolve
    hana "You're Ian's girlfriend?"
    scene w2_0178 with dissolve
    mina "Yup, I'm Mina! You're Hana, right?"
    scene w2_0176 with dissolve
    hana "You're both exactly and not at all what I imagined you to be."
    scene w2_0179 with dissolve
    mina "Uh... what? Eh..."
    scene w2_0180 with dissolve
    mina "I love your tattoos. They're really, {b}really{/b} cool!"
    "Momentarily flabbergasted, Mina quickly found room for a rebound."
    scene w2_0181 with dissolve
    hana "Hmmm... you kind of look familiar."
    scene w2_0182 with dissolve
    mina "Just one of those faces I guess..."
    scene w2_0183 with dissolve
    kil "Mina's a model. Maybe you've seen her face on a bus stop ad or something."
    scene w2_0181 with dissolve
    hana "Maybe, but I feel like it's something else..."
    scene w2_0182 with dissolve
    mina "We definitely haven't met before. I'd remember someone as beautiful as you."
    scene w2_0181 with dissolve
    hana "You really lay it on thick, don't you?"
    scene w2_0184 with dissolve
    mina "S-sorry..."
    scene w2_0185 with dissolve
    hana "Don't be. It's nice to meet you too, Mina. I'll try not hold your choice of boyfriend against you."
    scene w2_0186 with dissolve
    mina "Heheh~♥ I'd appreciate that."
    "Looking like an excited puppy dog, Mina emphatically shook the rocker girl's offered hand."
    scene w2_0187 with dissolve
    mc "Guess we're all friends now."
    scene w2_0188 with dissolve
    kil "The two of them mingling sends a chill up my spine..."
    scene black with fade
    stop music fadeout 3.0
    mc "You only have yourself to blame for that."
    "......"
    "..."
    scene w2_0189 with fade
    "After sharing in the cake Mina had bought, it was time to open the gifts. The normality of the scene felt striking to me, considering I was balls deep in yesterday's wall-to-wall debauchery."
    scene w2_0190 with dissolve
    kil "Me first!"
    play sound "sound effects/slide-wood.wav"
    scene w2_0191 with dissolve
    pause 0.8
    "Killian slid the wrapped present my way, wearing an eager grin."
    scene w2_0192 with dissolve
    "Picking up the gift in front of me, I gave it a tentative shake, making note of its weight and shape like a kid on Christmas Eve."
    "It had a decent heft to it and was tightly packaged."
    scene w2_0193 with dissolve
    kil "Just go ahead and open it."
    hana "Someone's excited..."
    scene black with fade
    play sound "sound effects/gift-unwrap.wav"
    "..."
    stop sound
    scene w2_0194 with fade
    play music "music/hep-cats.ogg"
    kil "I know you don't play games much anymore, but I couldn't think of much else."
    scene w2_0195 with dissolve
    mc "This is an expensive gift, Ian..."
    scene w2_0196 with dissolve
    kil "Maybe we could start playing again sometime, eh?"
    scene w2_0197 with dissolve
    "Killian flashed me a child-like smile."
    mc "Yeah, we'll do that. Thank you."


    if prBirthdayMinaGift == True and minaFlag == True:
        $ Mina_KLove -= 1

        scene w2_0198 with dissolve
        mina "I'm next!"
        scene w2_0199 with dissolve
        mina "I hope you like it."
        scene w2_0202 with dissolve
        kil "Me too. She spent a week probing me for information."
        "I thought back to the drinking game Felicia, Mina, Ian, and I played a while back."
        mct "(She actually remembered that?)"
        kil "She's weird about crap like that."
        scene w2_0203 with dissolve
        mina "No I'm not! That's what normal people do."
        scene w2_0200 with dissolve
        mc "With how much thought you put into it, I'm sure it's a great gift."
        scene w2_0201 with dissolve
        "Mina beamed as she put the present in front of me."
        scene w2_0204 with fade
        "Just like before, I picked up the box in front of me and gave it a test shake."
        mct "(Hmm...)"
        "It had much less heft to it than Ian's, but it was also tightly packaged."
        scene black with fade
        play sound "sound effects/gift-unwrap.wav"
        "..."
        stop sound
        scene w2_0205 with fade
        mina "I hope you didn't already have one. I did a little research and that topped the list of things new med students needed..."
        mina "It's cardiology grade. That's good, right?"
        scene w2_0206 with dissolve
        kil "A little research? She spent a whole evening trying to narrow down the best one."
        mct "(This is... at least as expensive as Ian's gift. Maybe even more...)"
        scene w2_0207 with dissolve
        mc "This is an extremely, EXTREMELY thoughtful gift. Thank you."
        mc "You spent way too much money on this."
        scene w2_0208 with dissolve
        mina "No, I didn't. Happy birthday, [mcf]. I'm glad we met!"
        "Mina leaned over and gave me a big, genuine hug that matched her warm words."
        mc "No, you really did. These things cost-"
        scene w2_0209 with dissolve
        mina "Shuuush! I was raised not to talk about money. Just accept the dang gift!"
        mc "Heh, alright... thanks again."
        scene w2_0210 with dissolve
        hana "Bleugh..."
        scene w2_0211 with dissolve
        kil "..."
    else:


        scene w2_0198 with dissolve
        mina "I wish I would've went first."
        scene w2_0199 with dissolve
        mina "It really isn't that great of a gift..."
        scene w2_0200 with dissolve
        mc "That's okay. We've only known each other a month. It's difficult enough giving gifts to people you've known your whole life."
        mc "I suck at it, at least."
        scene w2_0199 with dissolve
        mina "Hehe... me too! Still, I hope you'll like it."
        scene w2_0201 with dissolve
        "Mina beamed as she put the present in front of me."
        scene w2_0204 with fade
        "Just like before, I picked up the box in front of me and gave it a test shake."
        mct "(Hmm...)"
        "It had much less heft to it than Ian's and with less give."
        scene black with fade
        play sound "sound effects/gift-unwrap.wav"
        "..."
        stop sound
        scene w2_0212 with fade
        mina "Again, it was a bit last minute... I usually like to have more time to pick out gifts..."
        scene w2_0213 with dissolve
        kil "No kidding. Mina spent two weeks researching and picking out a graduation gift for her niece earlier this year."
        kil "She's weird about crap like that."
        scene w2_0214 with dissolve
        mina "No I'm not! That's just what normal people do."
        "These were pretty expensive-looking sunglasses. Not exactly my style, but they seemed quality."
        scene w2_0215 with dissolve
        mc "Thank you Mina. I don't own a pair of sunglasses, this is a nice gift."
        scene w2_0216 with dissolve
        mina "I'm glad you like it. Happy birthday, [mcf]. I'm glad we met!"
        "Mina leaned over and gave me a big, genuine hug that matched her warm words."
        scene w2_0210 with dissolve
        hana "Bleugh..."


    scene w2_0217 with fade
    kil "Now that the cake and gifts are out of the way..."
    scene w2_0218 with dissolve
    hana "It's time to start drinking?"
    scene w2_0219 with dissolve
    kil "Why, what a brilliant idea, Hana. What do you say, birthday boy?"
    scene w2_0220 with dissolve
    mc "Ah, hell... this place is stocked I guess, might as well bust open a bottle of gin or something."
    scene w2_0221 with dissolve
    mina "{size=-10}Why do hangouts always have to end with a hangover?{/size=-10}"
    scene w2_0222 with dissolve
    hana "So, the plan is to get liquored up and watch some movies?"
    scene w2_0223 with dissolve
    mc "Hmm..."
    "I gave it some thought. Of course, I liked the idea of ending the night quietly, but..."
    scene w2_0224 with dissolve
    mc "Why don't we play a drinking game instead? Something fun that will let us get to know each other better."
    scene w2_0225 with dissolve
    "Opening up and doing things differently wouldn't be so bad."
    kil "What did you have in mind?"
    scene w2_0224 with dissolve
    mc "How about... {i}Never Have I Ever{/i}?"
    scene w2_0226 with dissolve
    mina "Yes, please! That is so much better than one of Ian's convoluted games!"
    scene black with fade
    stop music fadeout 3.0
    "......"
    "..."
    scene w2_0227 with fade
    play music "music/sneaky-snitch.ogg"
    mc "Everyone is familiar with how this goes?"
    scene w2_0228 with dissolve
    hana "Someone admits to something they've never done before and the people who've done it drink. That continues until we're all smashed."
    scene w2_0227 with dissolve
    mc "Exactly. It's not complicated, but there is some finesse to it. Try and pick an answer that will drag an embarrassing story out from someone."
    mc "However, let's make things more interesting."
    scene w2_0229 with dissolve
    kil "What do you got cooking in that head of yours?"
    scene w2_0230 with dissolve
    mc "Let's say... every time someone drinks on your turn, you get a point. The person with the most points by the end of the game will be declared the winner."
    mc "The losers will have to do something the winner commands. One big group dare."
    scene w2_0231 with dissolve
    hana "What if there's a tie?"
    scene w2_0230 with dissolve
    mc "Then there will be multiple winners, but only one command."
    scene w2_0231 with dissolve
    hana "Hmm, alright. I'm game."
    scene w2_0232 with dissolve
    mina "Me too, I {b}guess{/b}..."
    scene w2_0233 with dissolve
    kil "Who goes first?"
    scene w2_0230 with dissolve
    mc "I'll start and then we'll just go around the room from there."
    scene w2_0234 with dissolve
    "There's a lot of things I {i}haven't{/i} done, but I should make the first answer a good one..."
    scene w2_0235 with dissolve
    mc "Alright, let's see..."
    scene w2_0234 with dissolve
    hide screen textbox2 with dissolve

    m_dev "Six points yields Killian +3, otherwise results in Killian +1, Mina BiCurious +1"
    menu:
        "Never have I ever been nude in public."(chg=["DP_up3"]):
            $ minaBully = True
            $ DP += 3

            scene w2_0230 with dissolve
            show screen textbox2 with dissolve
            mc "Never have I ever... been inappropriately nude or exposed myself in a {b}public{/} space."
            scene w2_0236 with dissolve
            "Ian and Hana each quickly knocked back a shot of gin with no hesitation."
            scene w2_0237 with dissolve
            kil "A few times, actually."
            hana "I did a drum solo topless one time."
            scene w2_0238 with dissolve
            kil "Shit, for real? Haha!"
            hana "It was our singers' idea."
            scene w2_0239 with dissolve
            "To my surprise, Mina cocked her head back and slid the clear liquid down her throat."
            scene w2_0240 with dissolve
            mina "Eeugh, that's sharp!"
            scene w2_0241 with dissolve
            hana "Well, that was delayed."
            mc "Eh? So, all of you then? Even you, Mina?"
            scene w2_0242 with dissolve
            mina "Why do you single me out?"
            scene w2_0243 with dissolve
            mc "I'm just surprised is all."
            scene w2_0244 with dissolve
            kil "Me too. When did this happen?"
            scene w2_0245 with dissolve
            "Killian looked at Mina with an incredulous look in his eyes."
            scene w2_0246 with dissolve
            "Mina uncharacteristically avoided making eye contact."
            scene w2_0247 with dissolve
            stop music fadeout 3.0
            mina "It's not what you're thinking... it's just..."
            mina "Some girls played a little joke on me one time by stealing my clothes when I was in the locker room shower."
            scene w2_0248 with dissolve
            mc "That doesn't sound like a joke."
            scene w2_0247 with dissolve
            mina "No, it wasn't very funny... I had to wait until it got late and then run back to my dorm room naked."
            scene w2_0249 with dissolve
            kil "When was this?"
            scene w2_0247 with dissolve
            mina "When I was in boarding school... it was just a harmless prank though..."
            scene w2_0248 with dissolve
            hana "It sounds like a bunch of cunts."
            scene w2_0250 with dissolve
            mina "No, it was just some girls having fun. Can we move on please?"
            scene w2_0251 with dissolve
            "Mina squirmed uncomfortably in her seat and pointedly asked Hana to take her turn."
            scene w2_0252 with dissolve
            "The room shared a collective awkward silence, before the rocker girl had the decency to spare us."
            scene w2_0253 with dissolve
            hana "Okay, yeah... my turn..."
            play music "music/sneaky-snitch.ogg"
        "Never have I ever used a vacuum cleaner on my genitals."(chg=["DP_up","hana_up","mina_up"]):

            $ DP += 1
            $ Hana_Affection += 1
            $ Mina_Affection += 1

            scene w2_0230 with dissolve
            show screen textbox2 with dissolve
            mc "Never have I ever used a vacuum cleaner on my junk."
            scene w2_0254 with dissolve
            kil "Oh, fuck you!"
            scene w2_0255 with dissolve
            hana "Euh? Whaaaaat? You haven't..."
            mina "Why am I not surprised? That SHOULD surprise me, but it doesn't..."
            scene w2_0256 with dissolve
            ham "Pfft... hahahaha...."
            hana "Hahaha..."
            mina "Hehehe..."
            scene w2_0257 with vpunch
            ham "Bahahaha-!"
            scene w2_0258 with dissolve
            kil "Okay, now you guys are being absurd."
            "The girls shared a hearty laugh at Ian's expense, to a degree that almost made me feel bad for Ian."
            scene w2_0259 with dissolve
            "To his credit, he took his lump respectably."
            scene w2_0260 with dissolve
            kil "Picking questions you know the answer to isn't really in the spirit of the game!"
            scene w2_0261 with dissolve
            hana "You've crammed your cock into a vacuum cleaner before?"
            scene w2_0262 with dissolve
            kil "I was curious! It, uh... wasn't for me."
            scene w2_0261 with dissolve
            ham "Pft... hahahaha!"
            scene w2_0262 with dissolve
            kil "It's your turn, Hana!"
            scene w2_0261 with dissolve
            "Ian more or less begged the rocker girl to spare him from their laughter."
            hana "Hahahaha...! F-Fine! Sure!"

    scene w2_0263 with dissolve
    hana "Hmm..."
    scene w2_0264 with dissolve
    hana "Never have I ever..."
    scene w2_0265 with dissolve
    hana "Never have I ever had sex while other people were in the room."
    scene w2_0266 with dissolve
    "Hana delivered her move with a devious smile, knowing full well that Ian and I fit the criteria if only for the club alone. I wasn't sure if she was playing to win or if she was just trying to make us squirm."
    scene w2_0267 with dissolve
    "He and I shared a sly look, before a slight roll of the shoulders signaled to me to go ahead and drink."
    scene w2_0268 with dissolve
    mc "..."
    mina "What?!" with vpunch
    scene w2_0269 with dissolve
    hana "Oh, really? Both of you? That's interesting. You guys a pair of perverts or something?"
    scene w2_0270 with dissolve
    mina "How could either of you do something like that? That's... mortifying!"
    scene w2_0271 with dissolve
    kil "I don't know about [mcf], but that's part of the thrill."
    scene w2_0272 with dissolve
    hana "Your boyfriend is an exhibitionist."
    scene w2_0273 with dissolve
    mina "What about you, [mcf]?"
    scene w2_0274 with dissolve
    mc "Well, you know... college dorm rooms can be small."
    scene w2_0275 with dissolve
    "I lied. I had never stayed in a college dorm, but it's not like I could just say I got my dick sucked in front of a dozen rich perverts just yesterday."
    scene w2_0276 with dissolve
    mina "Eeugh, I don't know how you could do that!"
    scene w2_0277 with dissolve
    kil "Want to try it some time?"
    scene w2_0278 with dissolve
    mina "No!"
    scene w2_0279 with dissolve
    hana "It's your go, Goldilocks."
    scene w2_0280 with dissolve
    mina "Okay, okay... let me think..."
    scene w2_0281 with dissolve
    mct "(Eh? Goldilocks...?)"
    scene w2_0282 with dissolve
    mina "{size=-10}Geez, I still can't believe you two...{/size=-10}"
    scene w2_0283 with dissolve
    mina "Okay! Never have I ever shoplifted."
    scene w2_0284 with dissolve
    "The three of us downed our drinks at about the same time."
    scene w2_0285 with dissolve
    mina "Hehehe, yes! Three pointer!"
    kil "You're actually into this?"
    scene w2_0286 with dissolve
    mina "All I'm going to say is get ready to bow down to your new queen, because at the end of the game that's exactly what you're going to do."
    "Mina proudly puffed out her chest in an exaggerated display."
    kil "This is only round one, babe. Don't count your chickens before they hatch."
    scene w2_0287 with dissolve
    hana " What are you, a country bumpkin?"
    scene w2_0288 with dissolve
    kil "It's a saying!"
    scene w2_0287 with dissolve
    hana "Yeah, one I'd not expect to come from your lips."
    scene w2_0289 with dissolve
    kil "Ah, whatever. It's my turn. I've got couple questions in mind, but the question is which one...?"
    scene w2_0290 with dissolve
    mc "You don't have to make this complicated."
    scene w2_0291 with dissolve
    kil "Alright. Here's a three pointer for you... never have I ever run from a cop."
    scene w2_0290 with dissolve
    mc "That's a surprisingly clean one..."
    scene w2_0292 with dissolve
    kil "Just a lil' icebreaker. Now, drink up you three."
    scene w2_0293 with dissolve
    "To my surprise, I wasn't the only one to raise a drink."
    kil "Ah, damn. I knew I'd get [mcf] and Mina, but I took a gamble on you."
    scene w2_0294 with dissolve
    hana "Hell, no. What do you think I get up to?"
    scene w2_0295 with dissolve
    hana "I mean, why tack an extra misdemeanor onto a drunk and disorderly? That's just stupid."
    scene w2_0296 with dissolve
    mc "{b}You've{/b} run from the cops?"
    scene w2_0297 with dissolve
    mina "K-kinda, heh..."
    scene w2_0298 with dissolve
    kil "It's a great story. You should tell it."
    mc "Yeah, I think I might need to hear this."
    stop music fadeout 3.0
    scene w2_0297 with dissolve
    mina "It's not a big deal. It was just a little misunderstanding..."
    scene w2_0299 with pixellate
    play music "music/you-should.ogg"
    mina "Ten months ago, just a little bit after Ian and I had started dating, we were standing on the corner of Oak and Old Row."
    mina "Like... forty minutes earlier, I had just smoked a joint for the first time in my life."
    kil "Let me clarify: she had like two hits before she was all \"woaaaah\" and \"I feel weeeeird\"."
    scene w2_0300 with dissolve
    mina "Eheh, yeah... anyway, we were standing on the corner of Oak and Old Row and I spotted a police officer coming our way."
    scene w2_0301 with dissolve
    kil "He wasn't coming {i}our{/i} way. He was just giving the buskers a hard time."
    mina "Am I telling the story or are you?!"
    kil "Sorry. I'll let you tell it."
    scene w2_0302 with dissolve
    mina "Thank you! So, I may have gotten the {b}teensiest{/b} bit nervous. Like, I couldn't take my eyes off him."
    mina "I watched him walk past that retro candy-shop. Then that mexican place..."
    mina "He got close enough to make eye contact and give me a funny look."
    kil "It was a friendly nod."
    mina "So I just..."
    scene w2_0303 with cmet
    mina "Went in the opposite direction." with vpunch
    kil "No. It was more like she hauled ass. She lost a heel."
    hana "Pfft,ha-wa-wait, the state decriminalized pot like... a couple of years ago!"
    scene w2_0304 with fade
    kil "Yeah. I know! That's what made it so fucking funny. After Mina's little disappearance trick, the cop came over looking pretty confused. I told him she was just a little high and we had a good laugh about it."
    scene w2_0305 with dissolve
    mina "I didn't know! It's not like I get a drug newsletter!"
    scene w2_0306 with dissolve
    mina "What about you, [mcf]? What's your story?"
    scene w2_0307 with dissolve
    mc "Oh, it wasn't a big deal. As usual, Ian and I were kids. I think we were breaking bottles on the sidewalk or something stupid like that."
    mc "Cop stopped by and I took off. Ian froze in place."
    scene w2_0308 with dissolve
    mina "Hehe, we have that in common."
    scene w2_0309 with dissolve
    stop music fadeout 3.0
    kil "Okay, so the tally for round one..."

    if minaBully == True:
        scene w2_0310 with dissolve
        kil "3 for [mcf], 2 for Hana, 3 for Mina, and 2 for me."
        scene w2_0311 with dissolve
        mina "Yes! Tied for first isn't bad."
    else:
        scene w2_0310 with dissolve
        kil "1 for [mcf], 2 for Hana, 3 for Mina, and 2 for me."
        scene w2_0311 with dissolve
        mina "Yes!"

    scene w2_0312 with dissolve
    mina "Hey, where you going? I'm winning!"
    scene w2_0313 with dissolve
    kil "Relax, I'm just draining the lizard. I'll be RIGHT back and then we can get back to it, your majesty."
    play sound "sound effects/door-slide.wav"
    scene black with fade
    "..."
    stop sound
    scene w2_0314 with dissolve
    "Ian's departure reset the conversation and a brief silence fell over the room."
    scene w2_0315 with dissolve
    play music "music/happy-boy-end-theme.ogg"
    hana "So... you and Ian have been dating for ten months?"
    scene w2_0316 with dissolve
    mina "Closer to eleven I guess. You work at Ian's uncle's place, right?"
    scene w2_0317 with dissolve
    "Before answering, Hana gave me a questioning look on the sly. I guess she was unclear on how much Mina knew."
    scene w2_0318 with hpunch
    "To which, like some doofus, I kicked her foot in confirmation."
    scene w2_0315 with wipeup
    hana "Yeah, that's right."
    scene w2_0316 with dissolve
    mina "How long have you two known each other?"
    scene w2_0315 with dissolve
    hana "I've worked there a little over a year now."
    scene w2_0319 with dissolve
    mina "Hmm..."
    scene w2_0320 with dissolve
    "Mina took time to slowly give Hana a once-over before speaking again."
    scene w2_0316 with dissolve
    mina "You two must be pretty good friends then."
    scene w2_0321 with dissolve
    hana "Eh, him and I don't exactly gel. It's a more {i}cordial{/i} thing."
    "Her choice of words had me scoffing inwardly."
    scene w2_0322 with dissolve
    mina "Ha! That's a polite no if I've ever heard one."
    scene w2_0323 with dissolve
    hana "What do you do, Mina?"
    scene w2_0324 with dissolve
    mina "Oh, I'm just a student..."
    scene w2_0325 with dissolve
    mc "Mina's a model and actress."

    if minaFlag == True:
        mc "She actually just landed a big gig on television."
        scene w2_0326 with dissolve
        mina "It's not {b}BIG{/b}."
        scene w2_0327 with dissolve
        mc "It's a speaking part with a storyline isn't it?"
        scene w2_0326 with dissolve
        mina "Yeah, still..."
        "Mina seemed unusually shy for whatever reason."
    else:


        scene w2_0323 with dissolve
        hana "Really? Have I seen anything you've done?"
        scene w2_0326 with dissolve
        mina "Well... uh, I recently got a tv-part."

    scene w2_0323 with dissolve
    hana "That's cool. Is it a show I know?"
    scene w2_0324 with dissolve
    mina "Probably not... it's just a crappy soap opera. It's called {i}Loving Days in Lafayette{/i}."
    scene w2_0328 with dissolve
    hana "It sounds like a big deal to me. You should own that shit."
    scene w2_0329 with dissolve
    mina "Eheh, you're right! It's the biggest role I've gotten! I'm really, really excited!"
    scene w2_0323 with dissolve
    hana "That's better."

    if minaFlag == True:
        scene w2_0330 with dissolve
        mina "Oh! Could I ask a {b}big{/b} favor of you, [mcf]?"
        scene w2_0331 with dissolve
        mc "What is it?"
        scene w2_0332 with dissolve
        mina "Would you... if you have the time... help do some line-readings tomorrow?"
        mina "I'd ask Ian, but he never takes anything like that seriously... plus given the kind of scene it is, he'll probably just try and get into my pants mid-scene."
        scene w2_0333 with dissolve
        "Mina looked at me expectantly, with a shy, hopeful smile. It really didn't leave me any choice."
        scene w2_0334 with dissolve
        mc "Sure, but I'm not an actor or anything... I don't know what good I'll be."
        scene w2_0332 with dissolve
        mina "Oh, you'll be plenty! All you have to do is read from a script!"
        scene w2_0334 with dissolve
        mc "Reading from a piece of paper is one of my greatest abilities. Sure, I'd love to help."
        scene w2_0335 with dissolve
        mina "Thank you!"
        hana "Eh...? G-get off of..."
        "Mina practically leapt over Hana to give me something resembling a hug."
        mina "I'm SO glad you said yes. You're my good luck charm!"
        scene w2_0336 with dissolve
        mc "...good luck charm?"
        scene w2_0330 with dissolve
        mina "Well, you did help me prepare for the audition and I got the part!"
        scene w2_0337 with dissolve
        "Hana looked at Mina dubiously, but said nothing."
        scene w2_0338 with dissolve
        mina "Actors and actresses are superstitious, okay?!"
        scene w2_0339 with dissolve
        hana "I didn't say anything."

    scene w2_0340 with dissolve
    mina "So..."
    "Looking for a change of topic, Mina searched for a topic."
    scene w2_0324 with dissolve
    mina "When did you get your first tattoo?"
    scene w2_0323 with dissolve
    hana "The day I turned eighteen."
    scene w2_0324 with dissolve
    mina "That's so neat. I've always wanted one, but I'm a big wuss... did it hurt?"
    scene w2_0323 with dissolve
    hana "Some more than others. It just depends on the location."
    scene w2_0341 with fade
    "..."
    scene w2_0342 with fade
    "The two quickly found themselves excitedly talking amongst themselves, like I wasn't there."
    "Not that I minded. Watching the two carry on like friends filled me with warmth."
    scene w2_0343 with dissolve
    kil "Sorry that took so long. My uncle called."
    mc "No biggie. Ready to get back to the game?"
    scene black with fade
    stop music fadeout 3.0
    mina "Yep!"
    scene w2_0235 with curtains
    mc "Alright, time to get things rolling again. Hmm..."
    scene w2_0234 with dissolve
    mct "(What should I pick here?)"
    hide screen textbox2 with dissolve

    menu:
        "Never have I ever given oral sex to someone of my own gender."(chg=["DP_up","mina_bi_up2"]):
            $ DP += 1
            $ Mina_BiCurious += 2

            scene w2_0422 with dissolve
            show screen textbox2 with dissolve
            play music "music/sneaky-snitch.ogg"
            mc "Never have I ever gone down on a person of the same sex."
            jump w2HanaLezStory
        "Never have I ever been handcuffed."(chg=["DP_up2","hana_up","killian_up"]):

            $ DP += 2
            $ Killian_Bromance +=1
            $ Hana_Affection += 1

            scene w2_0422 with dissolve
            show screen textbox2 with dissolve
            play music "music/sneaky-snitch.ogg"
            mc "Never have I ever... worn a pair of handcuffs."
            scene w2_0423 with dissolve
            mina "For... ANY reason?"
            mc "That's right."
            scene w2_0424 with dissolve
            mina "Uggg..."
            scene w2_0425 with dissolve
            "After some thought, Mina quickly downed her shot of gin."
            kil "Eh? You've never been arrested?"
            scene w2_0426 with dissolve
            mina "It's not that."
            kil "Nor have we ever done that in the..."
            mina "It's not that either! Yeesh..."
            kil "What is \"it\" then?"
            scene w2_0427 with dissolve
            mina "I don't want to say."
            scene w2_0428 with dissolve
            hana "Why not?"
            scene w2_0429 with dissolve
            mina "It's too embarrassing."
            scene w2_0430 with dissolve
            mc "Alright, no one's gonna force you to tell it. It's your go, Hana."
            hana "Okay... hm, never have I ever..."
            scene w2_0431 with dissolve
            mina "W-wait! Don't just move on..."
            scene w2_0432 with dissolve
            mc "You just said it was too embarrassing."
            scene w2_0431 with dissolve
            mina "Mmh... yeah, but..."
            scene w2_0432 with dissolve
            hana "But what...?"
            scene w2_0429 with dissolve
            mina "I don't want you to think I'm lame."
            scene w2_0430 with dissolve
            "All of us collectively raised our eyebrows for a moment."
            scene w2_0429 with dissolve
            mina "Just give me a moment..."
            scene w2_0433 with dissolve
            "........."
            "......"
            "..."
            scene w2_0434 with dissolve
            mina "A couple months ago, I was sleeping over at a friend's house. Her husband was out of town, so we were having a girl's night in."
            scene w2_0435 with pixellate
            mina "Her husband is like a HUGE jerk, gets massively crabby about even the smallest disturbance. So this was actually the first time I'd ever been over to her place."
            scene w2_0436 with dissolve
            mina "This friend... even though I don't exactly agree with how she lives her life... I still look up to her. She's got a ton of life experience, on top of being beautiful, sophisticated, and adventurous. She's done things I've only dreamed of."
            scene w2_0437 with dissolve
            mina "Which is why, when she left me alone in her apartment to run out to the corner store and get us some cheap wine, my curiosity got the better of me and I decided to take a look around."
            scene w2_0438 with pixellate
            mina "I don't mean like invade-a-person's privacy look around, I mean just a look on what was out in the open."
            mina "It can be fun. You learn a lot about a person from just the stuff they leave lying around."
            scene w2_0439 with dissolve
            kil "You're always just hoping to find someone as messy and untidy as you."
            scene w2_0440 with dissolve
            mina "I'm not messy! You're just a neat freak! Back me up, [mcf]."
            scene w2_0441 with dissolve
            mc "Eh...? Oh, yeah. Ian's always been fussy about cleanliness and putting things away."
            scene w2_0442 with dissolve
            kil "Just move on with the story."
            scene w2_0443 with pixellate
            mina "Ehehe, okay... so anyway, I took a peek around her apartment and it wasn't long before I found something that piqued my interest."
            scene w2_0444 with dissolve
            mina "Just lying on the bar was a set of handcuffs. Not some fuzzy pink, for-her-comfort handcuffs. These were like a cop's set."
            scene w2_0445 with pixellate
            mina "Which... was a lot more appealing."
            scene w2_0446 with dissolve
            hana "Appealing...?"
            scene w2_0447 with dissolve
            mina "I got... {i}curious{/i}."
            mina "I'd never worn any, you see..."
            scene w2_0448 with dissolve
            kil "You tried them on?"
            mina "..."
            scene w2_0449 with pixellate
            mina "Yes."
            mina "Some of my girlfriends talked like it was fun and I wanted to see what it felt like."
            kil "I didn't know you were interested in that sort of thing."
            scene w2_0450 with dissolve
            mina "I'm not! I was... {b}just being stupid{/b}."
            "It might have just been wishful thinking, but she sounded pretty unconvincing in refuting Ian's conclusion."
            mina "{size=-10}So, anyway I left the key on the bar...{/size=-10}"
            hana "What was that?"
            scene w2_0451 with dissolve
            mina "I said it really was stupid... because..."
            mina "I handcuffed myself to a nearby railing and.."
            scene w2_0452 with dissolve
            play sound "sound effects/surprise.wav"
            mina "I-left-the-{size=+10}KEY-ON-THE{/size=+10}{size=+15}BAR!{/size=+15}" with vpunch
            scene w2_0453 with pixellate
            mina "Ehehe..."
            scene w2_0454 with dissolve
            "Mina's face turned a beet red with her admission."
            scene w2_0453 with dissolve
            mina "It's not like I'm a total moron. I didn't just see a pair of handcuffs and handcuff myself without thinking about how to unlock it, okay? I confirmed the key worked first, but then I just..."
            mina "Forgot it on the table."
            scene w2_0454 with dissolve
            mc "Well, no harm, right? It sounded like your friend would be back pretty soon."
            scene w2_0455 with dissolve
            mina "Ahahaha, no. Unfortunately, that's the punchline to all of this..."
            scene w2_0456 with pixellate
            mina "Grr... eh...!" with vpunch
            mina "So... close...! C'mon...! C'mon...!" with vpunch
            mina "Eeeeh....! You're so,so stupid, Mina!" with vpunch
            play sound "sound effects/door-openclose.wav"
            "..."
            scene w2_0457 with dissolve
            mina "F-Felish...! You're back! I could use some..."
            stop music
            play sound "sound effects/record-scratch.wav"
            scene w2_0458 with dissolve
            elias "..."
            elias "You must be one of Felicia's {i}friends{/i}."
            mina "Uh, um... I can explain..."
            scene w2_0459 with pixellate
            hana "I thought he was out of town!"
            mina "He was supposed to be, but his plans unexpectedly changed..."
            mc "Did he uncuff you at least?"
            mina "No. He just gave me a stern look and went to his office..."
            hana "Ahahaha, no he didn't! That's hilarious!"
            scene w2_0460 with dissolve
            mina "He did. He really, REALLY did."
            scene w2_0461 with dissolve
            hana "Did you figure out if you liked it at least?"
            scene w2_0462 with dissolve
            mina "No... I was too busy panicking..."
            scene w2_0463 with dissolve
            hana "You got a pair of handcuffs lying around, [mcf]?"
            mina "S-shut up...!"
            scene w2_0464 with dissolve
            mc "You're up, Hana."
            scene w2_0465 with dissolve
            hana "I don't know how I'll follow that, but let's see..."
            jump w2BirthdayGameR2Continue


label w2HanaLezStory:

    if _in_replay:
        play music "music/sneaky-snitch.ogg"
        show screen textbox2 with dissolve

    scene w2_0344 with dissolve
    "No one immediately raised their glass, which wasn't a surprise. It was a Hail Mary type question."
    scene w2_0345 with dissolve
    hana "......"
    scene w2_0344 with dissolve
    hana "..."
    scene w2_0346 with dissolve
    "Which is why I felt a smile stretch across my face when Hana finally took a drink."
    scene w2_0347 with dissolve
    hana "Just me, huh?"
    scene w2_0348 with dissolve
    kil "You know, I always kind of thought you swung that way."
    scene w2_0349 with dissolve
    hana "What? Because I don't swoon over you? Get bent, you jackass. I'm not gay."
    hana "I wasn't even testing the waters. I've always been fairly confident I loved dick."
    scene w2_0350 with dissolve
    hana "It was just a one time thing, in a... very unique circumstance."
    scene w2_0351 with dissolve
    kil "Now you've got to go into detail."

    if Mina_BiCurious >=3:
        scene w2_0352 with dissolve
        mina "I kinda want to hear about it too..."
        "I could tell by the way her eyes were locked on Hana that there was no \"kinda\" about it."

    scene w2_0353 with dissolve
    hana "Sure, it's not like I'm embarrassed about it."
    scene w2_0354 with dissolve
    mc "Even if you were, that is the name of the game."

    if Mina_BiCurious >=3:
        scene w2_0355 with dissolve
        mina "Y-yeah, spill it."

    scene w2_0357 with dissolve
    hana "Alright, this was around two and a half years ago. I had just turned twenty and my best friend Jerrica got us tickets to see Blackwing Eternal, eh--"
    scene w2_0356 with dissolve
    hana "You ever heard of them? They're like my fourth favorite band of all time."
    scene w2_0354 with dissolve
    "We collectively shook our heads no."
    scene w2_0357 with dissolve
    hana "They're a groove metal band. Think like Pantera or White Zombie."
    scene w2_0355 with dissolve
    "That didn't wipe the blank look off our faces."
    scene w2_0358 with dissolve
    hana "Ah, jeez. You guys are lame as fuck."
    scene w2_0355 with dissolve

    if Mina_BiCurious >=3:
        mina "Come on, tell the story..."
    else:
        kil "Get to the good stuff."

    scene w2_0356 with dissolve
    hana "Okay, right. So like I said: it was not only my birthday, but this was the first time I had the chance to see them play live."
    scene w2_0357 with dissolve
    hana "If you ask me, even for the shittiest of bands, nothing really beats live music and Blackwing Eternal..."
    hana "Well, they're kickass. So, it was a fucking amazing time. That was even before I got to meet the band."
    scene w2_0355 with dissolve
    kil "I see where this is going. You got starstruck?"
    stop music fadeout 3.0
    scene w2_0356 with dissolve
    hana "More than that. I practically creamed my pants when Jerrica told me her boyfriend's cousin was concert staff and could get us backstage for fifty bucks."
    play music "music/higher-octane.ogg"
    scene w2_0359 with pixellate
    hana "Flash forward, I got to meet the lead singer: {b}Zara Tessman{/b}. She's a damn icon, one of the baddest bitches in metal and thankfully it wasn't a \"don't meet your heroes\" type deal."
    hana "She was super cool, and even though I acted like an annoying gaga-eyed fangirl, she invited us to the after party."
    hana "We hit a couple of nearby watering holes, and a few hours later, I found myself back at her place. It was under the pretense of checking out her album collection, but I could read the air..."
    hana "With the way she sidled up close to me at the bar, the way she touched my shoulder when she got to the punchline of a joke, and the way she would casually brush stray hairs out of my face..."
    scene w2_0360 with circlewipe
    hana "She was expecting something for giving a stupid girl like me the time of night."
    hana "When she told me..."
    zara "Get your tits out."
    hana "In a cocky voice that would've pissed me off 99.9 percent of the time..."
    scene w2_0361 with dissolve
    mina "You didn't...?"
    scene w2_0362 with dissolve
    scene w2_0363 with instantdissolve
    scene w2_0364 with instantdissolve
    scene w2_0365 with instantdissolve
    scene w2_0366 with instantdissolve
    scene w2_0365 with instantdissolve
    scene w2_0366 with instantdissolve
    hana "I did."
    scene w2HanaStory with dissolve
    hana "I knew she saw me as just another fame-stricken floozy to add as a notch in her bedpost."
    hana "You see it at every concert, countless women throwing themselves at gussied-up pretty boys with the charisma of rocks. Until that night, I could never wrap my head around it."
    mina "So, why did you? Especially if you're not even really into girls..."
    scene hanazara1_a with dissolve
    show hanazara1
    hana "Because, at that precise moment, I WAS a fame-stricken floozy."
    hana "She was fucking Zara Tessman. She was everything I wanted to be. She was so cool, so mature..."
    $ renpy.music.set_volume(.1, 2, channel = "music")
    scene w2_0378 with fade

    if Mina_BiCurious >=3:
        mina "How was it?!"
    else:
        mina "What happened next?"

    scene w2_0379 with dissolve
    hana "Oh? You seem awfully interested, Mina,"
    scene w2_0380 with dissolve
    mina "It's just you told such a detailed story... I'm just curious with how the rest went..."
    scene w2_0379 with dissolve
    hana "Is that right? Well, since we're friends and all..."
    scene w2_0381 with dissolve
    hana "*Gluhg*"
    scene w2_0382 with dissolve
    hana "You want the grisly details?"
    mina "Uh-huh..."
    $ renpy.music.set_volume(1, 3, channel = "music")
    scene hanazara1_a with pixellate
    show hanazara1
    hana "It started out with plenty of foreplay. I told her I'd never been with a chick before, so she wanted to ease me into things slowly."
    hana "And shit, by the agonizing end of it all, I was begging her to move on. "
    mina "Really?"
    hana "Oh, yeah. Goldilocks. Just picture it..."
    scene hanazara2_a with dissolve
    show hanazara2
    hana "She got to know every inch of my body, exploring and caressing with both her hands and mouth."
    hana "It was eye-opening, the way she used her fingers."
    hana "Not just my breasts either, but parts of my body I'd never derived pleasure from."
    hana "You ever realize your inner wrist is an erogenous zone?"
    mina "What? No it isn't!"
    hana "It is. The scalp too."
    hana "The earlobe..."
    mina "J-jeez!"
    hana "Yep. She had her way with me."
    hana "At the height of it all, that twisted bitch had me calling her mommy and begging to cum."
    mina "Nu-uh? That's..."
    $ renpy.music.set_volume(.1, 1, channel = "music")
    scene w2_0390 with pixellate
    hana "Oooh, lemme cum! Ah~♥! P-please!"
    "Hana looked like she was having the time of her life relaying the story to Mina. In fact, I'm pretty sure she had forgotten Ian and I were even here..."
    "Mina hung off of every word, with a noticeable blush on her cheeks."
    $ renpy.music.set_volume(1, 3, channel = "music")
    scene hanazara3_a with pixellate
    show hanazara3
    zara "Call me mommy, slut!"
    hana "M-mommy! P-please--"
    scene w2_0397 with flash
    with vpunch
    with flash
    with vpunch
    hana "Aaaah--!!!!!!" with flash
    mina "W-woah..."
    hana "That was just the start of the night."
    $ renpy.music.set_volume(.1, 1, channel = "music")
    scene w2_0398 with pixellate
    mina "W-woah..."
    hana "Pfhahaha, you should see your face, Goldilocks."
    scene w2_0399 with dissolve
    mina "How did the rest of the night go?"
    scene w2_0400 with dissolve
    "Despite the teasing, Mina's interest in Hana's story was unabated."
    scene w2_0401 with dissolve
    hana "The rest of the night...?"
    scene w2_0400 with dissolve
    scene w2_0402 with dissolve
    scene w2_0400 with dissolve
    "Mina gave a wordless nod to the question."
    hana "Hmm..."
    scene w2_0404 with dissolve
    mina "W-what are you doing?"
    $ renpy.music.set_volume(1, 3, channel = "music")
    scene w2_0405 with pixellate
    hana "First she had me eat out her cunt for about half an hour. I had never seen a vagina that close up, but I didn't have time to take in the sights."
    hana "She grabbed me by the head and put me to work. It being my first time, I was awful at it - not to mention, pretty tuckered out after being put through the paces, but I think she liked how inexperienced I was."
    scene w2_0406 with flash
    with vpunch
    with flash
    with vpunch
    hana "Pretty sure she got off on teaching straight women how to give oral or something stupid like that."
    $ renpy.music.set_volume(.1, 1, channel = "music")
    scene w2_0408 with pixellate
    mina "That's so... {i}perverted{/i}."
    scene w2_0407 with dissolve
    hana "The last part of the night is rather difficult to describe."
    scene w2_0408 with dissolve
    mina "It is?"
    scene w2_0407 with dissolve
    hana "Yes, it's best I show you."
    scene w2_0409 with dissolve
    mina "W-wait..!"
    $ renpy.music.set_volume(1, 3, channel = "music")
    scene black with fade
    mina "Gh- what are you doing?" with vpunch
    hana "Pfft-hold still, Goldilocks. Just a demonstration!" with vpunch
    mina "Eeeg, y-you're heavy! Get off of me?" with vpunch
    scene hanazara4_a with pixellate
    show hanazara4
    mc "Should we put a stop to this?"
    kil "Fuck no."
    hana "Just hold still for a minute!" with vpunch
    mina "Hey... don't grab...!" with vpunch
    scene w2_0411 with pixellate
    stop music fadeout 3.0
    hana "Aaaaaaand that's about how the night ended. It's not an easy position to describe, is it?"
    scene w2_0413 with dissolve
    mina "No, it isn't..."
    scene w2_0412 with dissolve
    "Mina's growing blush had hit a fever pitch. She looked like she had just run a few miles."
    scene w2_0411 with dissolve
    hana "To be frank, she taught me more about sex over a span of a few hours than I had previously learned in my short adult life."
    scene w2_0414 with dissolve
    hana "Or did it feel more like fucking...?"
    scene w2_0415 with dissolve
    mina "W-wow...."
    kil "Holy shit..."
    scene w2_0416 with dissolve
    mc "Don't you think you got carried away there?"
    scene w2_0417 with dissolve
    hana "She's just so easy and fun to tease. I couldn't help myself."
    scene w2_0418 with dissolve
    mina "Um, could you... let go of me?"
    hana "Oh, yeah! Sorry!"
    scene w2_0419 with fade
    hana "So, that's the story of the first and so far only time I've ever gotten down with a woman."
    hana "I guess it's my turn now? Feels like I just talked forever."
    $ renpy.end_replay()
    scene w2_0420 with dissolve
    if not persistent.w2HanaZaraFBGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w2HanaZaraFBGallery = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    mc "Yep, you're up. I don't know if anyone will be able to follow a story like that though."
    scene w2_0421 with dissolve
    hana "Don't worry, I'll cook up something good..."
    jump w2BirthdayGameR2Continue


label w2BirthdayGameR2Continue:

    play music "music/echo-sclavi.ogg"
    scene w2_0466 with dissolve
    hana "Never have I ever... had sex with someone old enough to be my parent."
    scene w2_0467 with dissolve
    mct "(...she's going for direct hits.)"
    scene w2_0268 with dissolve
    "Naturally, Ian and I knocked back our glasses."
    scene w2_0468 with dissolve
    mina "What? Both of you, again?!"
    mina "It wasn't the same person, was it?!"
    scene w2_0469 with dissolve
    mc "No... why would you think that?"
    mina "I mean... you two are... well, at least Ian is..."
    "Mina trailed off, unsure of how to put it."
    scene w2_0470 with dissolve
    kil "Good enough friends that we wouldn't have a problem tag teaming the same chick?"
    mina "No, I was NOT going to say THAT."
    kil "Hey, if you're ever interested in that sort of thing, I'm sure [mcf] wouldn't mind-"
    mina "OHMIGOSH shut up! I would n- I would never--!"
    scene w2_0471 with dissolve
    mc "Ehe..."
    scene w2_0472 with dissolve
    "Hana just sat back, chuckling to herself."
    mct "(That woman is evil...)"
    scene w2_0473 with dissolve
    mina "Okay, whatever... you guys are animals! It's my turn...!"
    scene w2_0474 with dissolve
    mina "Never have I ever..."
    "Mina glanced about the room, trying to grasp at something, anything that would move the game along."
    scene w2_0475 with dissolve
    mina "Uh... oh, I know!"
    mina "Never have I ever had a crush on a friend's parent."
    scene w2_0476 with dissolve
    kil "You're just piggybacking off of Hana's question!"
    scene w2_0477 with dissolve
    mina "So?"
    scene w2_0478 with dissolve
    if w1ExGame3Avoid == True:
        "As per our conversation in the sauna, Hana gave me a knowing look before she took a drink herself."
    else:
        "Hana nonchalantly shrugged before taking a drink."
    scene w2_0479 with dissolve
    mina "Ooooh, you have a thing for older men, eh?"
    scene w2_0480 with dissolve
    hana "Experience has its appeal."
    scene w2_0481 with dissolve
    "Meanwhile, Killian and I shared a dubious look at one another."
    "On my side of things, with all my teasing about Ian's mother over the years, it wasn't even an open secret."
    scene w2_0482 with dissolve
    kil "Drink up, mother fucker."
    scene w2_0483 with dissolve
    mc "Nice choice of words."
    scene w2_0484 with dissolve
    "I had no qualms in admitting it, and despite his reaction to my jokes, I knew he didn't have a problem with it either."
    "His mother is an attractive woman and we went through puberty together. It was an understandable, innocent thing for a kid. At least in my view."
    scene w2_0485 with dissolve
    mina "Eh? You think Grace is...? She scares me..."
    scene w2_0486 with dissolve
    "I had always assumed the same was true of Ian, but it was something he ardently denied once before."
    "He does pretty much think of her as a second mother, so maybe that's truly the case. At any rate, I'm not gonna twist his arm about it over a drinking game."
    scene w2_0487 with dissolve
    mina "Hehehe, anyway, another two points!"
    mina "Your go Ian."
    scene w2_0488 with dissolve
    kil "Never have I ever had a sexual fantasy I was too embarrassed to admit."
    scene w2_0489 with dissolve
    mina "You SHOULD be embarrassed..."
    scene w2_0490 with dissolve
    "I didn't have to think very hard about it, instead I just dutifully paid my penance."
    "To my surprise, I was the only one to do so."
    scene w2_0491 with dissolve
    mc "Everyone's got at least one, right?"
    scene w2_0492 with dissolve
    hana "Nope, I'm usually pretty above board about what I want."
    scene w2_0493 with dissolve
    mina "I mean, I've got some stuff I'm curious about, but I wouldn't call any of them fantasies..."
    scene w2_0494 with dissolve
    "Pretty sure that qualifies, but I wasn't about to rules lawyer a friendly game."
    scene w2_0495 with dissolve
    mc "Guess I'm the only one with a proper sense of shame..."
    "That said, I did let a little passive aggressiveness slip out."
    scene w2_0496 with dissolve
    mina "Ooooh, you got to tell us!"
    scene w2_0497 with dissolve
    mc "If it's too embarrassing to admit to a sexual partner, why would I...?"
    scene w2_0498 with dissolve
    hana "That's the game."

    if hanaFlag == True:
        hana "Plus you never know, that information could be useful for later."
    else:
        mct "(I suppose she has a point.)"

    scene w2_0499 with dissolve
    mc "Fair enough."
    scene w2_0500 with dissolve
    mc "I've always kind of wanted to..."
    hide screen textbox2 with dissolve
    $ mod_var = False
    menu:
        "[mod_option] All":
            $ mod_var = True
            call mod_BirthdayGame_1
            call mod_BirthdayGame_2
            call mod_BirthdayGame_3
        "Choke a woman during sex."(chg=["hana_up"]):
            label mod_BirthdayGame_1:
            $ w2FetishChoke = True
            $ Hana_Affection += 1

            scene w2_0499 with dissolve
            show screen textbox2 with dissolve
            mc "I've always kind of wanted to try breath play on a partner."
            scene w2_0501 with dissolve
            "I did my best to put it in the least embarrassing, most legitimate way possible."
            scene w2_0502 with dissolve
            mina "Breath play? What the heck does that mean?"
            scene w2_0503 with dissolve
            "Mina eyeballed me suspiciously."
            scene w2_0502 with dissolve
            mina "It's not a weird internet thing, right? Because I learned about those balloon people the other day..."
            scene w2_0504 with dissolve
            hana "He means he wants to choke the shit out of a chick during sex."
            scene w2_0505 with dissolve
            mina "Whaa...?"
            scene w2_0503 with dissolve
            "Mina eyeballed me again, not sure of what to make of this information."
            scene w2_0502 with dissolve
            mina "Why on earth would you want to do that?"
            scene w2_0503 with dissolve
            mc "Ehehe... I don't know..."
            "The question made me feel exceedingly self-conscious. Making sense of your sexual desires and putting it plainly into words for someone else to understand is a tall ask during a casual social situation."
            scene w2_0506 with dissolve
            hana "That's not weird at all, Goldilocks. In fact, it's common enough that it's borderline innocent."
            hana "You haven't ever wanted someone to smack your ass, pull your hair, or shove your face into a pillow?"
            scene w2_0507 with dissolve
            mina "No...?"
            scene w2_0506 with dissolve
            hana "What about the other way around? You ever just want to slap some dude in his smug face?"
            scene w2_0507 with dissolve
            mina "Um... of course not..."
            scene w2_0508 with dissolve
            hana "Eh, don't knock it until you try it. With someone you trust, rough sex can be fun."
            scene w2_0507 with dissolve
            mina "That just sounds scary to me..."
            scene w2_0509 with dissolve
            "Now Mina was eyeballing Hana dubiously."
            scene w2_0510 with dissolve
            mina "Oh! Sorry, [mcf]! I'm not making fun of you, I was just trying to understand. I hope I'm not embarrassing you..."
            scene w2_0511 with dissolve
            mc "Don't worry about it."
            if mod_var:
                return
        "Have a woman edge me."(chg=["mina_up"]):

            label mod_BirthdayGame_2:
            $ w2FetishEdging = True
            $ Mina_Affection += 1

            scene w2_0499 with dissolve
            show screen textbox2 with dissolve
            mc "I've always kind of wanted a woman to edge me."
            scene w2_0502 with dissolve
            mina "What the heck does that mean?"
            scene w2_0503 with dissolve
            "Mina eyeballed me suspiciously."
            scene w2_0502 with dissolve
            mina "It's not a weird internet thing, right? Because I learned about those balloon people the other day..."
            scene w2_0512 with dissolve
            kil "It means he wants to put a cork in it before he pops."
            kil "You know, with it being his dick."
            scene w2_0503 with dissolve
            mc "That's a colorful way of describing it."
            scene w2_0505 with dissolve
            mina "What? Why would you want to do that? That defeats the purpose, doesn't it?"
            scene w2_0503 with dissolve
            mc "How should I explain this...?"
            "I gave the next words out of my mouth some careful consideration."
            mc "The idea behind is to {i}delay{/i} orgasm, not deny it. When you finally do orgasm, it's supposed to make it more intense. Plus..."
            if trait_governor == True:
                mct "(As much as I've lived my life, preoccupied with the notion of living my life in control, carefully steering it in the right direction...)"
            mc "I find the idea of lying back, giving up control to my partner, and having them tease me kind of hot."
            scene w2_0504 with dissolve
            hana "[mcf]'s a bit of a masochist."
            scene w2_0503 with dissolve
            mc "Not really. I just don't mind being on the bottom of things sometimes."
            scene w2_0502 with dissolve
            mina "I don't think I get it."
            scene w2_0503 with dissolve
            mc "Well, just picture it for a second. Imagine if you could control when a dude came? You had him exactly where you want him, on the precipice of release, and then you just stop short of that."
            mc "You don't think his agonizing, pleading face would be hot?"
            mc "You haven't ever wanted Ian to last longer than a minute in-"
            scene w2_0513 with dissolve
            kil "Hey, fuck you buddy!"
            scene w2_0514 with dissolve
            mina "..."
            scene w2_0515 with dissolve
            mina "Yeah, okay. I think I get it now. That actually sounds like it could be fun."
            if mod_var:
                return
        "Treat a woman like an inanimate object"(chg=["killian_up"]):


            label mod_BirthdayGame_3:
            $ w2FetishObjectify = True
            $ Killian_Bromance += 1

            scene w2_0501 with dissolve
            show screen textbox2 with dissolve
            "I paused for some time to carefully consider how I was going to put this."
            "Long enough for the break in my words to feel pronounced and heavy."
            scene w2_0499 with dissolve
            mc "I've always wanted to..."
            scene w2_0516 with dissolve
            mc "Okay, I know this is gonna sound weird and fucked up, but this is just a fantasy okay?"
            scene w2_0517 with dissolve
            hana "Well, that's a real good fucking way to preface something weird and fucked up."
            scene w2_0518 with dissolve
            mc "...I've always wanted to treat a woman like a literal object."
            scene w2_0519 with dissolve
            "Saying it out loud made it sound horrible. I felt like I had just set myself adrift smack dab in the middle of a sea of judgement."
            scene w2_0520 with dissolve
            hana "Go on."
            scene w2_0521 with dissolve
            mc "Shit, it's like, um..."
            scene w2_0522 with dissolve
            mina "You mean like... uh, what was it called?"
            scene w2_0514 with dissolve
            "Mina searched her mind for the word."
            scene w2_0523 with dissolve
            mina "Forniphilia...?"
            scene w2_0524 with dissolve
            mc "Like what now?"
            scene w2_0523 with dissolve
            mina "The fetish of creating and using people like human furniture!"
            scene w2_0525 with dissolve
            kil "You know the damn word for that?"
            scene w2_0526 with dissolve
            mina "There was an article about that kinda weird crap in a women's mag I modeled for, okay?"
            scene w2_0527 with dissolve
            kil "...and you remembered it?"
            scene w2_0528 with dissolve
            mina "I have a good memory!"
            "......"
            scene w2_0529 with dissolve
            "..."
            scene w2_0502 with dissolve
            mina "Anyway, it's like that?"
            scene w2_0503 with dissolve
            mc "Uh, yeah. That could be included, but..."
            mc "What I had in mind is more like sex in the middle of everyday situations. Like while eating breakfast or in the middle of a meeting..."
            scene w2_0530 with dissolve
            mina "Interesting..."
            scene w2_0511 with dissolve
            mc "Yeah... it is pretty weird, I guess."
            scene w2_0531 with dissolve
            hana "So basically, you're a huge pervert?"
            scene w2_0532 with dissolve
            mc "Yes."
            scene w2_0531 with dissolve
            hana "Heh, that's okay! There's nothing wrong with that."
            hana "A lot of people are."

    scene w2_0499 with dissolve
    mc "Okay, if no one else is going to drink, I'm next then."
    scene w2_0501 with dissolve
    "I happily seized the opportunity to move on from the topic."
    stop music fadeout 3.0
    scene w2_0533 with dissolve
    kil "Let's make this next round the last."
    scene w2_0534 with dissolve
    mina "How come?"
    scene w2_0535 with dissolve
    mc "Yeah, you're only half-blasted."
    scene w2_0536 with dissolve
    kil "Well, I just thought if we ended a little early. We could finish the night with a movie like I know the birthday boy would prefer. Does that sound good to you all?"
    scene w2_0534 with dissolve
    mina "A movie sounds fun!"
    hana "I'm cool with it."
    scene w2_0537 with dissolve
    "Sometimes, Ian could be deceptively considerate."
    scene w2_0538 with dissolve
    mc "It's a good excuse to avoid a raging hangover."
    kil "Alright, so make your last turns a doozy."
    scene w2_0235 with dissolve
    mc "Hmm, alright..."
    scene w2_0539 with dissolve
    "Scrambling to come up with an answer on the spot, my mind immediately latched onto two options."
    "For some reason, the image of Ian flirting with that bar girl the night we went out with Mina and Felicia sprang to mind. As did Felicia's comment about it happening all the time."
    "Mina seems almost begrudgingly accepting of it... I could use it to rustle Ian's feathers a little. Then again, would that even be taken as humor?"
    if perk_socialButterfly == True or perk_socialChameleon == True:
        "No. There's teasing and then there's being a giant dickhole. You don't need to be a social savant to know this would pretty much be twisting the knife."
    "The second option is to pick something simple and try and score the most points."
    scene w2_0540 with dissolve
    mct "(Never have I ever...)"
    stop music fadeout 3.0
    hide screen textbox2 with dissolve

    menu:
        "Never have I ever hit on someone while on a date with a different person."(chg=["DP_up","killian_down2","mina_killian_down"]):
            $ DP += 1
            $ Mina_KLove -= 1
            $ Killian_Bromance -= 2

            show screen textbox2 with dissolve
            mc "Never have I ever… hit on, flirted with, or otherwise made advances to someone while on a date with someone else."
            scene w2_0541 with dissolve
            "........."
            "......"
            scene w2_0542 with dissolve
            "..."
            "No one made a move to take a shot."
            mc "We're all saints, hu--?"
            scene w2_0543 with dissolve
            mina "Just drink up."
            scene w2_0544 with dissolve
            "Mina cut Ian a cold glare, before plainly putting her command into words."
            "The two of them shared a knowing look, before..."
            scene w2_0545 with dissolve
            "Killian tilted his glass and drunk. He didn't look particularly pleased."
            "Meanwhile, Hana shot me a look like she was asking if I did that on purpose."
            mct "(...did I? Why would I?)"

            if minaFlag == True:
                scene w2_0546 with dissolve
                "My eyes involuntary wondered over to Mina and part of me grasped the answer."

            scene w2_0547 with dissolve
            hana "Alright, mooooving on..."
        "Never have I ever pretended to be sick to get out of something unpleasant."(chg=["DP_up3","hana_up","mina_up2"]):



            $ DP += 3
            $ Mina_Affection += 2
            $ Hana_Affection += 1

            play music "music/ill-remember-you.ogg"
            show screen textbox2 with dissolve
            mc "Never have I ever pretended to be sick to get out of something I didn't want to do."
            "I decided to go for the gold, so I went with a safe question. I hadn't, but I'm sure most people had."
            scene w2_0548 with dissolve
            "I was right."
            scene w2_0549 with dissolve
            hana "I played hooky from school every now and then. My grandfather let me get away with it occasionally."
            mina "I've gotten out of an agency Christmas party that way."
            scene w2_0550 with dissolve
            kil "I did it to avoid the class bully."
            scene w2_0551 with dissolve
            hana "Oh... for real?"
            scene w2_0552 with dissolve
            mc "I don't remember you ever skipping school without me."
            scene w2_0553 with dissolve
            kil "It was actually a few weeks before we became friends. You remember Austin Kelly?"
            scene w2_0552 with dissolve
            mc "He had a new target every week."
            scene w2_0553 with dissolve
            kil "He did. Until he got around to me. For some reason, he got real hung up on me. It carried on for weeks. Remember how we first met?"
            scene w2_0552 with dissolve
            mc "Hmm... yeah, I do."
            scene w2_0554 with pixellate
            kil "He gave anyone who tried to talk to me a hard time, until people started avoiding me. Eventually, it got to the point that if I sat down at the lunchroom table, other kids would get up and move."
            scene w2_0555 with dissolve
            kil "[mcf] didn't though."
            kil "He made it a point to sit with me."
            mc "Having a whole table to ourselves was pretty sweet."
            scene w2_0557 with pixellate
            kil "Fuck yeah it was. I still remember how gobsmacked that fatass looked when you told him to fuck off back to the trailer park. He looked like you sucker punched him."
            scene w2_0556 with dissolve
            "That was an understatement. I still remembered how deeply hurt he looked and how instantaneously I regretted my choice of words."
            scene w2_0557 with dissolve
            kil "You always did know how to get under people's skin."
            scene w2_0556 with dissolve
            mc "Well, it was obvious that would tick him off. I'm pretty sure your parents' money was why he bullied you so much longer than anyone else in the first place."
            scene w2_0533 with dissolve
            kil "That was probably it."
            scene w2_0534 with dissolve
            hana "So, the rest is history?"
            scene w2_0535 with dissolve
            "Ian looked at me with nostalgia in his eyes."
            scene w2_0536 with dissolve
            kil "Yep. That was when things started to get better. I mean kids could still be mean, but [mcf] stuck to me like glue after that. I never felt alone."
            stop music fadeout 3.0
            scene w2_0537 with dissolve
            mina "That's sweet."
            scene w2_0558 with dissolve
            stop music fadeout 3.0
            mc "Three points for me then."
            scene w2_0559 with dissolve
            mc "Your turn, Hana."

    play music "music/sneaky-snitch.ogg"
    scene w2_0560 with dissolve
    hana "Hmm... it's a little too serious now. Let's get the mood back to where it was. What am I at?"
    scene w2_0561 with dissolve
    mc "You have four points, Mina has five, Ian has three, and I have [DP]."
    scene w2_0562 with dissolve
    hana "Never have I ever..."
    scene w2_0563 with dissolve
    hana "Been caught with my pants down."
    scene w2_0564 with dissolve
    kil "You mean...?"
    scene w2_0565 with dissolve
    hana "Oh, you know. In an act of {i}sexual congress{/i} or self-debasement. Either or."
    scene w2_0564 with dissolve
    kil "Ah, well... check and check."
    scene w2_0566 with dissolve
    hana "Aw, really? Just him?"
    scene w2_0567 with dissolve
    mc "I've always been careful. Thin walls growing up."
    mina "I would just... DIE. My mom isn't exactly the most sex-positive person..."
    scene w2_0568 with dissolve
    kil "I still haven't met your parents, huh?"
    scene w2_0569 with dissolve
    mina "Nope. With any luck, you won't for a long time."
    scene w2_0570 with dissolve
    mc "How come?"
    scene w2_0571 with dissolve
    mina "If my mother got one whiff of how successful Ian's parents are, she'd stick her nose where it didn't belong."
    scene w2_0572 with dissolve
    kil "So she says, but I think she's just embarrassed by me."
    "Ian smiled, looking almost proud of this."

    if minaFlag == True:
        scene w2_0573 with dissolve
        mina "You remember me mentioning her backwards view on higher education, [mcf]?"
        scene w2_0570 with dissolve
        mc "Yeah... something about using it to find a well-to-do husband?"
        scene w2_0571 with dissolve
    else:
        scene w2_0571 with dissolve
        mina "She says college for a young lady should be about finding a husband."

    mina "With Ian, she'd be like a shark with blood in the water..."
    scene w2_0568 with dissolve
    kil "Would that really be so bad?"
    scene w2_0569 with dissolve
    mina "Yes! I'm 19! What sane girl my age is looking to settle down?"
    scene w2_0574 with dissolve
    hana "If you find that right person, I don't think it's so bad giving up part of your youth to have something you could call a family."
    scene w2_0575 with dissolve
    mina "Maybe... but my mother and my revolving door of stepdads is proof that tying the knot does not a family make. I guess your parents must've had a good marriage?"
    scene w2_0576 with dissolve
    hana "Um..."
    mina "S-sorry if that's too personal of a question. It just sounded like you had a positive view of--"
    scene w2_0577 with dissolve
    hana "No, it's cool. The answer to your question is a big ol' fuck no. I was brought up by mom."
    scene w2_0578 with dissolve
    scene w2_0579 with dissolve
    scene w2_0578 with dissolve
    "Mina chose not to speak, instead she simply nodded in solidarity."
    mct "(Sounds like she can sort of relate.)"
    scene w2_0580 with dissolve
    hana "It's your go, Mina."
    scene w2_0581 with dissolve
    mina "Okay, I've got a pretty good one. Never have I ever..."
    mina "Lied during this game."
    scene w2_0582 with dissolve
    "......"
    "..."
    scene w2_0583 with dissolve
    "No one drank."
    scene w2_0584 with dissolve
    kil "It's a fun question, but did you forget you were trying really hard to win?"
    scene w2_0583 with dissolve
    mina "..."
    scene w2_0585 with dissolve
    mina "Ah... DAMN!"
    hana "Pftt-!"
    kil "If anyone HAS lied in the first place, why would you think they'd admit to it?"
    scene w2_0586 with dissolve
    hana "*Whisper* Ian's girlfriend isn't what I pictured."
    mina "I don't know! For dramatic effect?"
    scene w2_0587 with dissolve
    kil "Well, that puts you and Hana tied at 5, with [mcf] at [DP]."
    kil "I'm at 3, so that means..."


    if DP == 8 or DP == 7:
        scene w2_0588 with dissolve
        kil "I have absolutely no hope of winning."
        scene w2_0589 with dissolve
        hana "What? You're just ending it like that?"
        scene w2_0590 with dissolve
        kil "Why not? Might as well let the birthday boy get straight to his kingly command."
        scene w2_0591 with dissolve
        kil "What would you have us do, My Lord?"
        scene w2_0592 with dissolve
        mina "Welp, better [mcf] than Ian."
        scene w2_0593 with dissolve
        hana "You better not ask us to do something perverted."
        mina "[mcf] wouldn't do that. Would he...?"
        scene w2_0594 with dissolve
        mc "Me? No..."
        scene w2_0595 with dissolve
        "I knew {b}exactly{/b} what I wanted them to do, but first..."
        scene w2_0596 with dissolve
        mc "The three of you line up in a row over there and kneel, please."
        scene black with fade
        "Each of them looked at me doubtingly, but complied with my request, moving away from the couch and into the open."
        scene w2_0597 with fade
        mc "Now, what will I have you do...?"
        scene w2_0598 with dissolve
        mina "Huh? I thought you already knew because of this pose."
        scene w2_0599 with dissolve
        mc "I just wanted to have your waiting faces looking up to me while I thought about it."
        scene w2_0600 with dissolve
        hana "Pfft, jerkass!"
        scene w2_0601 with dissolve
        "That was a lie. I did know {b}exactly{/b} what I wanted them to do, but I wanted to drag it out some."
        mc "I got it!"
        "I feigned like it had just hit me."
        stop music fadeout 3.0
        mc "Now..."
        hide screen textbox2 with dissolve

        menu:
            "I dare you to say something nice about each other."(chg=["hana_up","killian_up","mina_up"]):
                $ Mina_Affection += 1
                $ Hana_Affection += 1
                $ Killian_Bromance += 1

                show screen textbox2 with dissolve
                play music "music/jazz-piano-bar.ogg"
                mc "I dare you to say something nice about the other two."
                scene w2_0602 with dissolve
                mina "Eh...? That's it?"
                hana "You got us down on our knees for that?"
                scene w2_0603 with dissolve
                mc "Yes. Why don't you start it off, Hana?"
                mc "Say something nice about {b}Ian{/b}..."
                scene w2_0604 with dissolve
                hana "Eugh..."
                scene w2_0605 with dissolve
                "I folded my arms and patiently let Hana mull over ALL that she liked about Ian."
                hana "Mmh...?"
                "This was meant to be a small gesture to bring everyone closer together, but I'd be lying if I said making Hana say something nice about the man she despises didn't tickle a sadistic instinct in me."
                scene w2_0606 with dissolve
                hana "Fine, I got it. Ian..."
                hana "I like that you always bring coffee for everyone when you come into... {i}your Uncle's{/i}. You always remember everyone's specific order..."
                scene w2_0607 with dissolve
                kil "A squirt of cardomon to sweeten it up and a spritz of coconut oil to thicken up the drink."
                scene w2_0608 with dissolve
                hana "Yes... it's surprisingly conscientious and thoughtful..."
                scene w2_0609 with dissolve
                "I could just hear the \"for you\" tacked onto the end of that in Hana's mind."
                scene w2_0610 with dissolve
                kil "Thank you, Hana. It's nice to feel appreciated."
                scene w2_0611 with dissolve
                "Especially with how smug Ian looked hearing just the smallest amount of praise."
                scene w2_0612 with dissolve
                hana "As for Mina... we just met, but she's been very friendly and warm toward me almost like we were already pretty good friends. Plus..."
                scene w2_0613 with dissolve
                hana "Her pigtails are good."
                scene w2_0614 with dissolve
                mina "Hehe~ I got praised..."
                scene w2_0615 with dissolve
                mc "Your turn Ian."
                scene w2_0616 with dissolve
                kil "I... respect that Hana is not afraid to freely speak her mind."
                kil "I think that's a pretty cool way to go through life."
                scene w2_0617 with dissolve
                hana "Thanks."
                scene w2_0618 with dissolve
                kil "As for Mina, I couldn't ask for a more attractive girlfriend."
                scene w2_0619 with dissolve
                mina "That's it?"
                scene w2_0620 with dissolve
                kil "I mean, uh... how do I love thee? Let me count the ways..."
                kil "I love thee to the depth and breadth and height--"
                scene w2_0621 with dissolve
                mina "I like that Ian can still surprise me. He's goofy and it's almost like he's stumbling through life with blinders on, but..."
                scene w2_0622 with dissolve
                "Mina looked at Ian, for the briefest of moments as if looking back on their relationship."
                scene w2_0621 with dissolve
                mina "Sometimes he blindly walks into making a girl feel special. Not that this is one of those times..."
                scene w2_0623 with dissolve
                "I got the sense Mina was speaking nostalgically."
                scene w2_0624 with dissolve
                mina "As for, Hana! Where do I start?"
                mina "She is so, so cool. I already told her I love her... \"ink\", but I also love her sense of fashion and..."
                scene w2_0625 with dissolve
                mina "Even the way she's looking at me is so cool! She's also here because of [mcf], which tells me she's got good taste in friends!"
                mina "Not to mention...!"
                "......"
                "..."
                scene w2_0626 with dissolve
                "Mina spent the next 30 seconds spewing all kinds of compliments Hana's direction, by the end of it all the would be rockstar was blushing."
                hana "Um... thanks. That was... a lot."
                mina "Hehe~"
                scene w2_0627 with dissolve
                kil "Alright, my knees are killing me. That's enough of this pose."
                scene w2_0628 with dissolve
                kil "Let's pop in a movie and get cozy?"
                mc "Sure. I'll pop some popcorn. What are you feeling?"
                scene black with fade
                stop music fadeout 3.0
                "......"
                "..."
                jump w2BirthdaySegue
            "*Boop their noses*"(chg=["tough_down","mina_up2"]):



                $ Mina_Affection += 2
                $ toughness -= 1

                show screen textbox2 with dissolve
                play music "music/you-should.ogg"
                mc "I got you where I want you."
                scene w2_0629 with dissolve
                mina "What the heck does that--"
                scene w2_0630 with vpunch
                "Boop!"
                scene w2_0631 with vpunch
                "Boop!"
                scene w2_0632 with vpunch
                "Boop!"
                scene w2_0633 with dissolve
                mc "Alright, I'm all done. We can watch a movie now."
                mina "Pftt-tck-!"
                scene w2_0634 with dissolve
                mina "*Snort* Khtt- haha~ *Snort* What...!"
                kil "That was it? You're just gonna squander your dare?"
                mc "The drinking game itself was a reward enough. I got to know you all better."
                scene w2_0635 with dissolve
                mina "Hehe~hahAHAHAHA!"
                mc "Are you okay?"
                mina "Pftt...! No-! *Snort* I c-can't breathe!"
                scene black with fade
                kil "Alright, my knees are killing me. That's enough of this pose."
                kil "Let's pop in a movie and get cozy?"
                mc "Sure. I'll pop some popcorn while Mina comes back to her senses."
                stop music fadeout 3.0
                "......"
                "..."
                jump w2BirthdaySegue
            "Use the opportunity to score a memorable selfie."(chg=["tough_up","killian_up"]):



                $ Killian_Bromance += 1
                $ toughness += 1

                show screen textbox2 with dissolve
                play music "music/frame-of-mine.ogg"
                "I thought about it some, and there was no need to make this some long, protracted thing. A quick picture marking me as a winner and them as the loser would do."
                mc "I think I'll use this opportunity to snag a victory photo."
                scene w2_0670 with dissolve
                mina "Uh... why do you look so... evil?"
                scene w2_0671 with dissolve
                mc "You're just imagining things. Now, do you three know how to kotow?"
                scene black with fade
                mc "More over to the left... you're not in the shot --"
                hana "Like this?"
                mc "A little more... perfect! You got it!"
                mc "I want you to look like you just found God!"
                kil "This is stupid..."
                scene w2_0672 with dissolve
                mc "Now, say \"You are the most charasmatic, savvy, magn--\"...!"
                hana "Just take the damn photo!"
                play sound "sound effects/camera-phone-shutter.wav"
                with flash
                with flash
                mc "Good enough."
                scene w2_0673 with dissolve
                kil "Alright, my knees are killing me. That's enough of this pose."
                scene w2_0674 with dissolve
                kil "Let's pop in a movie and get cozy?"
                mc "Sure. I'll pop some popcorn. What are you feeling?"
                scene black with fade
                stop music fadeout 3.0
                "......"
                "..."
                jump w2BirthdaySegue


    if DP == 6:
        kil "I could tie this up at least."

    if DP <= 5:
        kil "I could win this."

    scene w2_0636 with dissolve
    kil "Never have I ever swallowed a pill."
    scene w2_0637 with dissolve
    hana "Are you kidding me? That's what you're gonna end this on?"
    scene w2_0636 with dissolve
    kil "It's the truth. I haven't been sick since I was a kid."
    scene w2_0638 with dissolve
    mc "Why do you sound like you're bragging?"
    scene w2_0639 with dissolve
    kil "Drink up. That's a critical hit, right?"
    scene w2_0640 with dissolve
    "The three of us shared a mutual look, before knocking back our glasses."
    scene w2_0641 with dissolve
    "With that our short little drinking game came to an end."

    if DP == 6:
        $ Killian_Bromance += 3
        scene w2_0642 with dissolve
        kil "That means [mcf] and I tied and that puts you two ladies on the chopping block."
        scene w2_0643 with dissolve
        mina "Why do you have to phrase it that way?"
        stop music fadeout 3.0
        scene w2_0644 with dissolve
        kil "[mcf], my buddy..."
        mc "Yes, friend?"
        play music "music/hotshot.ogg"
        scene w2_0645 with dissolve
        kil "Please, consult with me for a moment. We need to discuss a fitting prize."
        mc "Of course, let's confer in my office."
        scene w2_0646 with dissolve
        "......"
        "..."
        mc "Oh, yeah. Sure. That's good! It needs a little something extra though..."
        scene w2_0647 with dissolve
        kil "What do you have in mind, partner?"
        mc "Oh.. I know! I saw something strange in a trunk the other day."
        "..."
        scene w2_0648 with dissolve
        kil "I remember these are definitely Darius'."
        mc "I think they're perfect."
        scene w2_0649 with cmet
        kil "Great! Stand just like that!"
        scene w2_0650 with dissolve
        hana "What is this? A photoshoot?"
        scene w2_0651 with dissolve
        mina "That is his thing."
        scene w2_0649 with dissolve
        kil "We're just gonna take a commemorative losers photo. Only, it's missing something..."
        scene w2_0652 with dissolve
        mc "Luckily, I have just the thing lying around that'll add the perfect final touch."
        mc "Hold still girls."
        scene black with fade
        mina "He- what's this? Oh, c'mon..."
        hana "This is stupid."
        kil "Wow, you girls look great. Now, grab ahold of each other like long lost sisters!"
        play sound "sound effects/camera-phone-shutter.wav"
        kil "I want to feel your intensity!"
        play sound "sound effects/camera-phone-shutter.wav"
        kil "No... no, that won't do. Closer! Like you haven't seen each other in a decade."
        play sound "sound effects/camera-phone-shutter.wav"
        kil "Perfect! You got it!"
        scene w2_0653 with goslow
        kil "You girls look beautiful. Don't they, [mcf]?"
        play sound "sound effects/camera-phone-shutter.wav"
        with flash
        mc "They sure do. Like a pair of angels."
        mina "Grr..."
        scene w2_0654 with vpunch
        hana "Okay, that's enough! You two had your fun."
        kil "You want a copy for your social media profiles?"
        "The scene that played out was utterly stupid, but... it was fun."
        scene w2_0655 with dissolve
        mina "Can we watch that movie now?"
        mc "Sure. What are you guys feeling?"
        mina "It's your birthday."
        scene w2_0656 with dissolve
        kil "Hmm... you girls familiar with the work of Groucho Marx? I think you'd love his comedy..."
        scene w2_0657 with dissolve
        scene black with fade
        kil "...get it?"
        mina "I don't get it."
        mc "I'll cook some popcorn while you explain it."
        stop music fadeout 3.0
        "......"
        "..."
        jump w2BirthdaySegue


    if DP <= 5:
        $ Killian_Bromance += 1
        $ Mina_BiCurious += 1

        scene w2_0642 with dissolve
        stop music fadeout 3.0
        kil "That means I win and you three are up on the chopping block."
        scene w2_0643 with dissolve
        mina "Why do you have to phrase it that way?"
        scene w2_0658 with dissolve
        mc "Go easy on us, please."
        scene w2_0659 with dissolve
        kil "Easy...? Hmm, well. It is your birthday and I am a magnanimous man."
        scene w2_0660 with dissolve
        kil "Sit tight for just a second, while I see what you got going in your fridge."
        mina "The fridge...? Please don't get food involved..."
        play sound "sound effects/door-open.wav"
        scene w2_0661 with fade
        "We waited as Ian rummaged throughout the kitchen, until he found what he was looking in the freezer."
        scene w2_0662 with wiperight
        play sound "sound effects/ice-glass.wav"
        "He returned with a glass clutched tightly in his hand, giving it a demonstrative shake that produced a distinctive clank."
        scene w2_0663 with dissolve
        mc "A glass of ice? What are you planning on having us do with that?"
        scene w2_0664 with dissolve
        play music "music/helping-hands.ogg"
        kil "Simple. I want you three to pass it along to the person next to you, using only your mouth."
        scene w2_0663 with dissolve
        mc "Oh...?"
        scene w2_0665 with dissolve
        hana "Geez, that's not so bad, but I am a little perplexed at what you get out of this."
        "I knew right away what he was trying to do. He was playing wingman for me with Hana."
        scene w2_0666 with dissolve
        kil "Maybe I just like to watch?"
        scene w2_0667 with dissolve
        mina "He probably just wants to see you and I kiss."
        hana "That's typical."
        "Ian gave me a quick thumbs up on the sly, confirming my suspicion."

        if hanaFlag == True:
            "I wanted to tell him I didn't need the help, but hey... he won fair and square. It's his dare."
        else:
            "I wanted to tell him he had the wrong idea about Hana and I, but that would just make things awkward."

        scene w2_0668 with dissolve
        kil "[mcf] will start."
        play sound "sound effects/ice-glass.wav"
        scene w2_0669 with dissolve
        mc "Just pop these in my mouth and pass it to Hana?"
        kil "Yep. You got it."
        jump w2BirthdayIanWins

label w2BirthdayIanWins:
    if _in_replay:
        show screen textbox2 with dissolve
        play music "music/helping-hands.ogg"

    scene w2_0675 with dissolve
    "I angled the glass and let the ice slide into my mouth on a bed of pooling water."
    "Needing to be quick about it before it melted, I quickly sidled up next to Hana."

    if hanaFlag == True:
        scene w2_0676 with dissolve
        "She looked dead in my eyes, lips pursed into a slight grin."
        scene w2_0677 with dissolve
        hana "Well... let me have it, [mcf]."
        scene w2_0676 with dissolve
    else:
        scene w2_0678 with dissolve
        "She met my own awkward look with her own."
        scene w2_0679 with dissolve
        hana "Well... ready when you are."
        scene w2_0678 with dissolve

    "The chill of the ice quickly grew unpleasant to my gums, so I craned my neck down toward the rocker girl and she rose up to meet me."
    scene w2_0680 with dissolve
    "Our lips met without ceremony and were soon engaged in the commission of our task."
    "I did take a moment to enjoy the sensation of Hana's soft lips pressing into mine. The warmth of it made an unusual contrast to the feeling of having ice sit square on the flesh of your tongue."
    "I quickly found out the task required more concentration than one would've thought, owed largely to how crowded the inside of my mouth was."

    if hanaFlag == True:
        scene w2_0681 with dissolve
        "To help things along, Hana grabbed the back of my neck and used the leverage to redirect my efforts."
        "One by one, the ice cubes slipped from my mouth into hers."
        "Along the way, our tongues would naturally bump into one another, flooding my head with a pleasant feeling."
        "Sometimes it felt lingering, like they were intertwined longer than they had to. Still, eventually..."
        scene w2_0683 with dissolve
        "They were gone. Our task was complete and Hana pulled herself back from me."
    else:

        scene w2_0682 with dissolve
        "One by one, I slipped the ice cubes from my mouth into hers."
        "Along the way, our tongues would naturally bump into one another, but we remained focused on the task."
        scene w2_0683 with dissolve
        "Eventually our task was complete and Hana pulled herself back from me."

    scene w2_0684 with dissolve
    "Hana wasted no time of her own and moved on to do the same to Mina."

    if Mina_BiCurious >=4:
        scene w2_0685 with dissolve
        "They shared a fleeting look, causing a noticeable blush on the blonde's cheeks and an unduly long pause before the two set out on their given task."
        scene w2_0686 with dissolve
        mina "Mmmh...!"
        "Mina let out a sharp, surprising sound as soon as their lips met."
    else:

        "The two briefly looked into each other's eyes, before setting out on the given task."
        scene w2_0686 with dissolve
        "The pair pressed their lips against one another and Hana began the process anew."


    "Watching their lips gently undulate as the ice cubes passed from one to the other was a beautiful sight."
    scene w2_0687 with dissolve
    "Hana instinctually grabbed at Mina's upper arms, adding an illusion of intimacy between the two."
    "Meanwhile, Mina's lower half squirmed in place, hips ever-so-lightly swaying with an anxious energy."
    "Melted ice pooled around the corners of their mouth."

    if Mina_BiCurious >=4:
        scene w2_0688 with dissolve
        "By the time it occurred to me that I was maybe watching {i}too{/i} intently, it was over."
        "Mina looked like she was in a daze as she chewed on the ice in her mouth."
    else:
        scene w2_0689 with dissolve
        "By the time it occurred to me that I was maybe watching {i}too{/i} intently, it was over."
        "The two shared a smile, as Mina chewed on the ice in her mouth."

    "..."
    scene w2_0690 with dissolve
    hana "So, movie now?"
    scene w2_0691 with dissolve
    mc "Yeah, that sounds good to me."
    mc "What are you guys feeling?"
    scene black with fade
    stop music fadeout 3.0
    hana "It's your birthday. Why don't you pick?"
    mc "Okay. You guys get settled first and I'll cook up some popcorn while I think about it."
    $ renpy.end_replay()
    scene black with fade
    if not persistent.w2MCHanaMinaKissGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w2MCHanaMinaKissGallery = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    "......"
    "..."
    jump w2BirthdaySegue


label w2BirthdaySegue:

    scene w2_0692 with ccirclewipe
    play music "music/night-on-the-docks-sax.ogg"
    "Over the next couple of hours, the night petered out."
    scene w2_0693 with dissolve
    hana "*Whisper* Wait... is that one of...?"
    "The film of choice: Terminal Action, one of the handful of B-movie action flicks that Samson Garcia was known for."
    scene w2_0694 with dissolve
    hana "He never shuts up about them, but I've never actually seen one of his movies."
    scene w2_0692 with dissolve

    if minaFlag == True:
        "I had recalled Mina mentioning her love for this one earlier this week. It also felt like a nice in-joke for the Carnation Club-adjacent of us."
    else:
        "Something dumb and simple for our inebriated minds, with the added something for the Carnation Club-adjacent of us."

    scene w2_0695 with dissolve
    mina "Oh, I love this part!"
    scene w2_0696 with pixellate
    sam "We're gonna have us a little barbecue! How do you like your ribs, Senator?"
    man "Wait, please--!"
    scene w2_0697 with pixellate
    with vpunch
    tv "*Explosion* Boom!"

    "The film was terrible as it had always been, but it felt like I was seeing it with new eyes. Veronica was on my mind."
    scene w2_0698 with dissolve
    mct "(What a fucking bastard...)"

    if VeroFlag == True:
        "I don't know how I'm going to do it, but I reaffirmed the promise I made to myself."
        "I'm going to figure out exactly what that shithead is doing to tank Veronica's business and go from there."
    else:
        "The thought of him purposefully tanking Veronica's business pissed me off, but it was outside of anything I could help."

    scene w2_0699 with dissolve
    hana "It's no wonder he wound up selling gym equipment."
    scene w2_0700 with dissolve
    mc "*Whisper* Tell me about it."
    scene black with fade
    mina "Looks like they're out."

    if hanaFlag == True:
        scene w2_0701 with w12
        mina "I knew this would happen. I told Ian to stop drinking."
        scene w2_0702 with dissolve
        mc "None of you have any business driving home. Why don't you sleep here tonight?"
        scene w2_0701 with dissolve
        mina "Thanks, [mcf]. That would be for the best."
        scene w2_0702 with dissolve
        mc "Why don't you and Hana take my bed. There's room for two."
    else:


        scene w2_0703 with w12
        mina "I told Ian to stop drinking. I knew this would happen."
        scene w2_0704 with dissolve
        mc "None of you have any business driving home. Why don't you sleep here tonight?"
        scene w2_0703 with dissolve
        mina "Thanks, [mcf]. That would be for the best."
        scene w2_0704 with dissolve
        mc "Why don't you and Hana take my bed. There's room for two."

    scene w2_0705 with dissolve
    mina "No, this is a big couch. I'll sleep here with Ian tonight. Make sure he doesn't puke all over your apartment."
    scene w2_0706 with dissolve
    mc "That... would be HIGHLY appreciated."
    scene w2_0707 with dissolve
    hana "Eh...? How long have I been out?"
    scene w2_0708 with dissolve
    mc "The last 15 minutes of the movie. Mina and I were just discussing sleeping arrangements. Do you want to stay here or should I call you a taxi?"
    scene w2_0709 with dissolve
    hana "Here, if you don't mind. I'm not that tipsy, but better safe than sorry."
    hana "Plus, my bike's here and I don't want to spend the money going home and then coming back to get it."
    scene w2_0708 with dissolve
    mc "Smart."
    scene w2_0710 with wipeup
    "After getting Ian and Mina settled downstairs with blankets, I showed Hana to my bed."
    scene w2_0711 with dissolve
    hana "So, this is where the magic happens?"
    scene w2_0712 with dissolve
    mc "It's a new place. No magic yet."

    if hanaFlag == True:
        scene w2_0713 with dissolve
        hana "That right?"

    scene w2_0714 with dissolve
    mc "If you need anything, I'll be asleep in a chair downstairs."
    scene w2_0716 with dissolve
    hana "Eh? Don't be ridiculous. There's enough room for both of us."
    scene w2_0714 with dissolve
    mc "No, that's okay. I wouldn't want you to feel..."
    scene w2_0715 with dissolve
    hana "Uncomfortable? I'd be more uncomfortable knowing I kicked you out of your own bed on the night of your birthday of all nights."

    if hanaFlag == True:
        scene w2_0717 with dissolve
        hana "We're friends. Just get in the freakin' bed!"
    else:

        scene w2_0717 with dissolve
        hana "We're pretty much friends now. Just get in the freakin' bed!"
        scene w2_0718 with dissolve
        "No point in arguing with her."
        scene black with fade
        "......"
        "..."
        jump w2June08Start

    scene w2_0718 with dissolve
    mc "Well..."
    "I gave Hana one long look before finishing my train of thought."
    "I wouldn't mind sharing a bed with her, but of course I didn't say as much."
    mc "You've convinced me."
    scene w2_0719 with fade
    "After getting a little more comfortable, it didn't take long for either of us to settle in."
    "Soon..."
    scene black with fade
    "A feeling of drowsiness ushered me into..."
    scene w2_0719 with dissolve
    hana "You awake?"
    scene w2_0720 with dissolve
    mc "Yes, I do believe I am. What's up?"
    "Both of us spoke in a hushed tone."
    scene w2_0721 with dissolve
    hana "I had fun tonight."
    scene w2_0722 with dissolve
    mc "Me too, I'm glad you came, but you sound almost surprised."
    scene w2_0723 with dissolve
    hana "Heh, yeah. I am. I wouldn't ever dream of spending an evening drinking with that jackass downstairs."
    scene w2_0722 with dissolve
    mc "Yeah, but you DID come."
    scene w2_0721 with dissolve
    hana "Don't get cocky. I owed you one from the concert."
    scene w2_0720 with dissolve
    mc "Is that the only reason you came?"
    scene w2_0721 with dissolve
    hana "No."
    scene w2_0720 with dissolve
    mc "Well, I'm glad to hear it. Thanks for being here, Hana."
    scene w2_0724 with dissolve
    hana "My pleasure, [mcf]."
    scene w2_0725 with dissolve
    mc "..."
    scene w2_0726 with dissolve
    mct "(What a nice smile...)"
    scene w2_0727 with dissolve
    hana "You're tired?"
    scene w2_0726 with dissolve
    mc "Mmmhmh... got up pretty early today... visited Ian's mom... zZZzz... had lunch with... zZZzz..."
    scene w2_0727 with dissolve
    hana "I have trouble picturing what his mom would be like."
    scene w2_0726 with dissolve
    mc "...mmh, that's a tough nut to crack."
    scene w2_0727 with dissolve
    hana "How come?"
    scene w2_0720 with dissolve
    mc "Well, she's... a bitch? I mean, she cares about him. I'm ninety nine percent sure about that, but she's..."
    scene w2_0721 with dissolve
    hana "Got a funny way of showing it?"
    scene w2_0720 with dissolve
    mc "Yes. That's a good way of putting it."
    scene w2_0727 with dissolve
    hana "The world is filled with people like that."
    scene w2_0726 with dissolve
    mc "Mmhmh..."
    scene black with fade
    hana "You know, it occurs to me I haven't given you a birthday present yet."
    mc "Mmh... that's fine. I wasn't expecting anything. It was sprung on you at the last minute."
    hana "...that's not what I was getting at, stupid."
    scene w2_0728 with dissolve
    "I felt a cold grip grab ahold of my hand, pulling me once more from the edge of sleep."
    mc "Eh, your hands are cold... what are you...?"
    scene w2_0730 with dissolve
    hana "I know. I need help warming them up."
    scene w2_0729 with dissolve
    "Her voice, which had been delivered to my ears in a pleasantly soft bedside whisper, had dropped even lower and pulled me from my half-asleep state with its smokey timbre."
    mc "You could always get underneath the covers."
    "I teased Hana, playing painfully dumb."
    scene w2_0730 with dissolve
    hana "Come on, [mcf]..."
    scene w2_0729 with dissolve
    "It was a husky, needy voice that made her intention feverishly clear."
    scene w2_0730 with dissolve
    hana "Don't try and poke holes in a girl's excuse."
    scene w2_0729 with dissolve
    "The sultry way she formed her words had lit up a feeling of desire in me as fast and violent as a gasoline fire."
    "Inwardly, I marveled at how the right woman could fan the flames of arousal using only her voice."
    mc "This feels... abrupt."
    scene w2_0731 with dissolve
    hana "Don't let your head go and ruin a nice thing either."
    scene w2_0729 with dissolve
    "For just a brief moment, her expression shifted subtly and she looked at me with lonely, borderline despondent eyes."
    stop music fadeout 3.0
    hide screen textbox2 with dissolve

    menu:
        "Kiss her."(chg=["hana_anger_down","hana_up5"]):
            $ Hana_Affection += 5
            $ Hana_Anger -= 1
            $ w2HanaSex = True
        "Pull her close and hold her until you fall asleep."(chg=["hana_up2"]):


            $ Hana_Affection += 2
            $ hanaFriendFlag = True

            show screen textbox2 with dissolve
            "Truth be told, I wasn't sure I wanted to go barking up this tree."
            "The proverbial tree being the boss' daughter."
            "However, that look she was giving me, I couldn't fully rebuke her without feeling like a piece of shit."
            scene w2_0795 with dissolve
            "So I pulled her close to me and held her."
            scene w2_0796 with dissolve
            mc "Sorry, I'm feeling a little tired. If you don't mind, do you think we could just...?"
            scene w2_0795 with dissolve
            hana "..."
            "Hana looked at me curiously, with a briefly frustrated expression."
            scene w2_0797 with dissolve
            hana "Yeah, of course."
            scene w2_0798 with dissolve
            hana "This can be nice too..."
            scene w2_0799 with dissolve
            mc "Is everything okay with you?"
            scene w2_0798 with dissolve
            hana "Why do you ask?"
            scene w2_0799 with dissolve
            mc "I don't know. Just seemed like the question to ask."
            scene w2_0798 with dissolve
            hana "Mmmh... yeah, I'm fine. Just the usual stress in my life."
            scene w2_0799 with dissolve
            mc "Want to tell me about it?"
            scene w2_0798 with dissolve
            hana "Not right now, but... maybe later?"
            scene w2_0799 with dissolve
            mc "I'd be happy to hear it."
            scene w2_0798 with dissolve
            hana "...thanks, [mcf]."
            scene w2_0799 with dissolve
            "Just like that, we fell into a comfortable silence."
            "So comfortable that..."
            scene black with fade
            mc "......."
            hana "..."
            jump w2June08Start

label w2BirthDayHanaPresent:

    play music "music/everything-you-wanted.ogg"
    scene w2_0732 with hpunch
    show screen textbox2 with dissolve
    "That was all it took for the doors of self control to fling wide open."
    "I wasted no time in burying my face in the pale, beautiful expanse of her neckline."
    "Hana met my fervor by hiking her naked legs up and around my waist, pulling me closer and locking our bodies together."
    scene w2_0733 with dissolve
    "My hands naturally worked their way down and groped at the rocker girl's ass, fingers sinking pleasantly into the soft flesh and succeeding in pulling our waists closer together still."
    "Hana began to gently rock her hips as if on cue, grinding her crotch into mine and igniting a spreading warmth in my crotch as the outline of her vulva traced repeatedly against my tenting cock."
    hana "Fuck, I need thi--!"
    scene w2_0734 with dissolve
    hana "{b}Mmh...!{b}"
    "In a bout of passion, I violently pressed my lips to Hana's, conveniently cutting her excited cry short from any listening ears downstairs."
    "One of my hands clumsily found perch on a breast, fingers pawing at the thin cotton material that painfully separated them from making direct contact."
    scene w2_0735 with dissolve
    mc "Oh, god. You're so--"
    scene w2_0736 with dissolve
    "This time it was Hana that kissed me, cutting off my words in a change of initiative."
    scene w2_0737 with dissolve
    hana "Ammh...♥"
    "It occurred to me that it felt nice to lock lips with a woman that had nothing to gain from it, but I immediately put that out of mind."
    "Instead, I focused on the wiry movements of Hana's tongue as it snaked past mine in a long, impassioned game of tonsil hockey."
    scene w2_0736 with dissolve
    hana "Hhhmmm...!"
    scene w2_0738 with dissolve
    "When the kiss finally broke, both of us had to catch our breaths."
    hana "[mcf]..."
    "Hana placed a firm set of hands on my chest and gave me a suggestive push."
    scene w2_0739 with cmet
    "A suggestion I was happy to follow, as I rolled over and allowed Hana to slip into the driver's seat."
    hana "I meant it about needing this."
    scene w2_0740 with dissolve
    pause 0.5
    scene w2_0741 with dissolve
    "With one quick motion, the oversized shirt that had been distracting me all night lay in a clump on the bedroom floor."
    scene w2HanaGrope with dissolve
    "My hands wasted no time, sinking nice and deep into the supple flesh of Hana's glorious tits."
    hana "Nng..! Ah, yeah...! It's been... an embarrassing amount o-of... time since anyone's... touched me... like this..."
    "Her words came out in clumps, as if being modulated by my finger tips."
    scene w2_0754 with dissolve
    mc "How long?"
    scene w2_0755 with dissolve
    hana "Let's see..."
    scene w2_0756 with fade
    "Hana and I worked together to wiggle out of my pants and they soon joined Hana's shirt in a pile on the floor."
    hana "A year."
    scene w2_0757 with dissolve
    hana "Y'know, ever since I got a glimpse of this thing at the exhibition last night..."
    scene w2_0758 with dissolve
    "Without a modicum of shyness, Hana wrapped her fingers around my stiffened cock."
    hana "I've been wanting to see this thing up close."
    mc "Mmh... r-really?"
    "Her cold fingers wrapped around my burning cock felt amazing."
    hana "Uh huh."
    "My eyes were drawn to the thin piece of fabric that covered her womanly bits, keenly aware of its close proximity to my own sex."
    "The heat radiating from it was palpable, causing my dick to eagerly twitch for what was ahead."
    scene w2_0759 with dissolve
    "Instead of what I was imagining however, Hana decided to tease me."
    "Rubbing and touching the slightly exposed lips of her opening."
    hana "Ah... oh... mmh...!"
    scene w2_0760 with dissolve
    mc "What are you doing?"
    "I said it in a tone that was more {i}what are you waiting for{/i}?"
    hana "Don't be so eager, lover. I'll give you your present soon enough, but for now..."
    mc "N-now...?"
    scene w2_0761 with dissolve
    hana "I want you to watch."
    "Her intonation was utterly obscene at this point."
    "I hesitated to call it pornographic, because there was no artifice to it. It was words wrapped in pure, raw, sensual need."
    scene w2_0762 with dissolve
    "All I could do was control myself and wait patiently, as her fingers played and teased at her vulva, ever so occasionally pushing aside her panties and burrowing to parts unseen."
    mc "Fuck..."
    "The sight itself was enough to make me want to cum."
    scene w2_0764 with dissolve
    mc "You're enjoying teasing me..."
    scene w2_0763 with dissolve
    hana "I'm enjoying the look on your face."
    hana "It {i}really{/i} turns me on."
    scene w2_0764 with dissolve
    "The pent-up expression on her face said it all."
    mct "(A {b}year{/b}, huh? Not since she started working at the Club...)"
    scene w2_0763 with dissolve
    hana "I REALLY am enjoying that look on your face, but..."
    scene w2_0765 with dissolve
    "The way she trailed off left me hopeful."
    scene w2_0766 with dissolve
    hana "It's not like I'm going to make you beg."
    scene w2_0767 with dissolve
    "Hana leaned back and braced herself on my knees, extending her legs past me, and kissing the underside of my cock with her yet uncovered sex."
    hana "I don't... want to go all the way tonight."
    "My stomach tightened when I heard the sad news. It must've shown on my face, because..."
    scene w2_0768 with dissolve
    hana "S-sorry...! I mean that doesn't mean either of us won't be getting off to--"
    scene w2_0769 with dissolve
    mc "Of course. We'll only go as far as you're comfortable with."
    scene w2_0770 with dissolve
    "I did my best to cover up my disappointment with a reassuring smile, which was returned with a relieved smile of the rocker girl's own."
    hide screen textbox2 with dissolve
    scene hanarub1_a with dissolve
    show Hanarub1
    "We shared a few moments of silence between us, before things turned unbearably lewd again as Hana rocked her hips back and forth, using her panties and the outline of her twat to stimulate my near-painfully engorged dick."
    hana "Ah...♥ You ever... done it like this before?"
    mc "N-no...! This is a first..."
    hana "Me either, but it's really. Fucking. Hot."
    "The spreading damp spot on her panties testified to that true enough."
    hana "The only thing stopping your fat cock from gorging my insides is this little piece of fabric."
    hana "Oooh..! Mmmh...♥ I can feel that bad boy twitch."
    "Was she getting off on denying herself or from teasing me? I didn't know which."
    scene hanarub2_a with dissolve
    show Hanarub2
    "Not that I cared, the feeling of the sheer material of her underwear felt amazing. Instead of the full, bloated feeling of penetrating a woman, the pleasure came in almost unbearably ticklish waves."
    "The rough, non-patterned movements created a myriad of sensations. The material of her underwear, damp with her juices, would cling ever-so-slightly to my dick, at varying times, for varying lengths..."
    hana "Ngh..! Y-you're feeling good, right?"
    mc "I'm feeling amazing..."
    hana "G-good! I'm glad...!"
    scene hanarub3_a with dissolve
    show Hanarub3
    "The next swath of time saw us sharing in a a heavy silence, as we let all pretense of speaking fall away and be replaced by the sounds of sexual exhaustion."
    "We just looked at one another."
    "Hana's eyes would erratically dart between my face and the cock sitting between her legs, while I enjoyed the incredible view of her tits bouncing up and down."
    "My mind invariably wandered to what it would feel like to be inside her. How tight she would feel, how needily her cunni would clamp down on my dick after a year of sexual starvation."
    mc "Ah, H-hana!"
    "I called out like a girl, the words reflexively forming and leaving my lips in an instant."
    scene hanarub1_a with dissolve
    show Hanarub1
    hana "Heh, I wonder if Goldilocks is hearing any of this?"
    mc "Keep it down then!"
    hana "Heh, maybe she's lying down there. Pretending to be asleep."
    scene w2_0771 with dissolve
    hana "Maybe she's touching herself...♥ Does that excite you even more?"
    scene w2_0772 with dissolve
    "Hana was becoming more and more cocksure with herself."

    menu:
        "Tell her the thought DOES excite you even more."(chg=["mina_up"]):
            $ Mina_Affection += 1
            mc "Fuck yeah, it does."
            scene w2_0771 with dissolve
            hana "I know, right? Mmh... it's easy to see... despite how cute she acts, she's horny as hell."
            hana "I bet you want to teach her a few things, don't you? Put your hands on your best friend's girlfriend."
            scene w2_0772 with dissolve
            mc "...ooohm, n-no comment..."
        "Tell her you think the thought excites her more than you.":


            mc "I think the thought turns you on more than me, you dirty slut."
            scene w2_0771 with dissolve
            hana "Mmmh... can't say it wouldn't be... interesting to teach her a few things...♥"
            hana "She's just so adorable... makes me want to... bully her...!"
        "Tell her you just want to focus on you and her."(chg=["hana_up"]):


            $ Hana_Affection += 1
            scene w2_0788 with dissolve
            mc "Right now... I just want to focus on me and you, Hana."
            mc "You're b-beautiful..."
            scene w2_0771 with dissolve
            hana "Nngh...ah, mmh...♥ Y-yeah, I am..."
            scene w2_0788 with dissolve
            "Despite her words, she looked pleased to hear it."


    scene hanarub1_a with dissolve
    show Hanarub1
    "Hana picked up the pace, almost painfully so. The already uneven movements of her hips went feverishly erratic."
    hana "[mcf]...!"
    "Her panties were {b}drenched{/b} at this point, coated in a mixture of both our love juices. Her lower lips were so plump with arousal that it almost felt like she was wearing nothing at all."
    hana "{b}[mcf]...!{/b}"
    "The closer and closer I got to orgasm, the more it felt like I was actually inside and fucking her."
    hana "{b}[mcf]...♥{/b}"
    "It felt like my head was taking in individual parts of her body all at once."
    scene hanarub3_a with dissolve
    show Hanarub3
    "My eyes would dart from her sweat-lined tummy to the pendulous sway of her breasts."
    scene hanarub2_a with dissolve
    show Hanarub2
    "They would focus on the source of the action."
    scene hanarub4_a with dissolve
    show Hanarub4
    "They would even curiously marvel at the way her elbows bent and retracted as she used her body like a rocking horse."
    "Most of all, my eyes would always return to her face. The way she pursed her lips, the way it scrunched up in pleasure, and the way the pools of her eyes had swamped over with muggy sexual arousal. "
    "She felt like a work of art to me."
    hana "Oh damn, I love the way you're looking at me!"
    mc "Ngh...! D-don't stop...!"
    hana "You're close?"
    mc "Yes!"
    hana "How close? Tell me."
    "Our voices had mostly been quiet up to this point, but now it dropped down to a sensual whisper."
    mc "Really, really close! Keep going! You're about to make me--!"
    play sound "sound effects/spurt.wav"
    scene w2_0773 with flash
    mc "Eugh~!"
    "In a flash of blinding pleasure, my balls churned violently and forced a stream of white-hot cum out through the opening of my engorged penis."
    play sound "sound effects/spurt.wav"
    scene w2_0774 with flash
    mc "--!"
    "Through half-lidded eyes I watched my ejaculate rain down on the would-be rock star's lower half, semen spattering her stomach."
    hana "Is that a normal amount?"
    scene w2_0775 with dissolve
    "After a few blurry moments, my senses finally came back to me and I took a second to admire my - or rather her - handiwork."
    "A beautiful woman dripping with my cum... it filled me with perverse satisfaction and gave me an even more perverse idea."
    scene w2_0776 with dissolve
    scene w2_0777 with dissolve
    "Wordlessly, I raked the tip of my index finger across her stomach, coating it with my spunk and presented it to Hana."
    scene w2_0778 with dissolve
    hana "Eh? You want me to...?"
    scene w2_0779 with dissolve
    "I answered her question with a nod."
    "For a brief moment, she looked unsure."
    scene w2_0780 with dissolve
    hana "Not gonna lie, that seems kinda gross, but..."
    scene w2_0781 with dissolve
    hana "Happy birthday."
    scene w2_0782 with dissolve
    "With a cute wink, she went above and beyond my expectations, guiding my finger into her mouth up with one unbroken motion to the knuckle."
    hana "Mmmh...~♥"
    scene w2_0783 with dissolve
    "Her tongue wrapped around the digit, lapping enthusiastically at the glob of cum."
    "It didn't take long for her to have it cleaned, but she didn't stop there."
    scene w2_0784 with dissolve
    "She made a show of fellating my finger, lewdly simulating a blowjob."
    "Sucking, bobbing, using it to probe the inside of her cheeks..."
    "The sight caused another swell of desire in me. I wished for that to be my dick."
    scene w2_0785 with vpunch
    play sound "sound effects/mouth-pop.wav"
    hana "*Pop* M'wah..!"
    "Hana concluded her stimulatory fellatio with an exaggerated plop."
    scene w2_0786 with dissolve
    hana "That was fun, [mcf]. Thanks for indulging me."
    scene w2_0787 with dissolve
    mc "Why are you talking like we're finished?"
    scene w2_0786 with dissolve
    hana "You want to go again?"
    scene w2_0787 with dissolve
    mc "You haven't cum yet."
    scene w2_0786 with dissolve
    hana "That's alright, I think--"
    scene w2_0789 with hpunch
    hana "Oohm...?!"
    "With a gentle, but quick push I put the rocker girl on her back."
    scene w2_0790 with dissolve
    "After the initial shock wore off, she peered up at me with growing need in her eyes."
    scene w2_0791 with dissolve
    hana "Alright... have it your way."
    scene black with fade
    hana "Hey, careful not to tear 'em! ...eh, you're cleaning it up with your shirt?"
    mc "Wouldn't be the first time."
    scene w2_0792 with bites
    "After playing a veritable game of twister with our limbs, I had Hana's sex completely exposed and in front of me."
    hana "Nnhee... your breath is... this position is..."
    scene w2_0793 with dissolve
    "I had Hana right where I wanted her, a firm hand on her tush and back arched like a whore."
    "The heat radiating from her twat was already obvious from this distance. I could only imagine how blazing she'll be to the touch..."
    mct "(Well, what am I waiting for? It's an all you can eat buffet!)"
    scene w2_0794 with dissolve
    "I dived right into it. No need for testing the water with a few half-hearted licks, no... I was propelled by the singular desire to return the pleasure Hana gave in equal measure."
    hana "Mmmh..."
    scene hanabuffet1_a with dissolve
    show HanaBuffet1
    "No - I was going to return the pleasure she gave to me two fold."
    hana "You're not wasting any time-!"
    "Sinking my hands deeper into her fat ass, I used my grip to get just the {i}right{/i} angle, sending my tongue barreling into her opening with full gusto."
    "She was already so wet, primed and raring to go that it met little resistance on the way in."
    "Instead, she welcomed me fully. Her inner walls gently kissing my tongue, undulating like she was trying to swallow it whole."
    hana "Mmmh, mmhhh...♥"
    hana "That's... that's nice, [mcf]."
    scene hanabuffet2_a with dissolve
    show HanaBuffet2
    "I thought the same too. It was heavenly being wedged between Hana's thighs. The sheer thrill of having such a headstrong woman practically bent over backwards in your hands..."
    mct "(Fuck, I'm so turned on!)"
    "Desire swelled in me."
    hana "Oh, [mcf]...!"
    "I intended to make the most of this chance. Who knows if Hana and I would ever do anything like this again after all?"
    hana "*pant* Ha... ha...!"
    scene hanabuffet1_a with dissolve
    show HanaBuffet1
    "I would use my tongue to make these feelings clear to her."
    hana "Mmmh, ha... ha...♥"
    "I reached as far back as I could and then some, pulling my tongue back in alternating shallow and deep motions, probing and tasting every inch of her sex."
    hana "Oh, fuck I really did need this! Don't stop, please."
    hana "Don't stop until I cum, okay? Please?"
    "There was a heavy and torrid twang in her voice."
    scene hanabuffet2_a with dissolve
    show HanaBuffet2
    "I wanted to scoff that she didn't have to ask, but that would needlessly get in the way of tongue fucking her."
    hana "Ohoho....!"
    "I could feel Hana unconsciously begin to rock her hips, her body trembling in my hands."
    "I scraped and I scraped, I teased, I licked, I caressed, grazed, fondled her all with my mouth."
    hana "Ehehe...!"
    scene hanabuffet1_a with dissolve
    show HanaBuffet1
    "I intermittently changed my focus, switching between her love tunnel and giving the engorged, pearly pink nub the attention it deserved."
    hana "F-fuck me, that's...!"
    "Her clit was fully out of its hood and I used everything in my toolbox to tease it. Tongue, nose, even going so far as to graze it ever-so-slightly with my teeth."
    scene w2_0800 with dissolve
    hana "Emmh-♥"
    "Hana chomped down on her hand, using it as a makeshift gag to stifle her moans. A conscientious effort that I appreciated, given Ian and Mina were not 20 feet away downstairs."
    "The thought was a salacious one, wasn't it?"
    "My sex-addled lizard brain wanted to imagine the bubbly blonde knuckle deep in her own snatch listening to us go at it. Of course, that was just a fantasy, but still..."
    mct "(That's so hot...!)"
    scene hanabuffet3_a with dissolve
    show HanaBuffet3
    hana "Mmmfhh-!"
    "With a violent jerk, Hana arched her back even further, wrapping her legs around my head and clamping down to pull me even impossibly deeper into her snatch."
    hana "C-chhmhm-!"
    hana "C-chhmhm-! C-chhmhm-!"
    mct "(She's close!)"
    "I extended and twisted my tongue to the point of soreness, spurred on by knowing how close she was."
    "At a certain point, all thought disappeared from my head. It was just strenuous focus on a singular task."
    "I was no longer [mcf], the student."
    hana "Gh..mmmffh...! Mffhh...!♥"
    "I was [mcf], the tongue."
    scene w2_0801 with vpunch
    hana "Nggghh......!!!!♥"
    "Hana clamped down around my neck even tighter, cutting off my airflow and signaling with gusto the arrival of her orgasm."
    mc "Ghmm-!"
    "Equally, the inner walls of her love hole tugged at the length of my tongue, squeezing and massaging the wiry, slimy muscle like it was a cock to be milked."
    "Just for a moment, breathing on both of our sides ceased - Hana in the throes of sexual release and me, head crushed between the rocker girl's pale thighs."
    scene w2_0802 with dissolve
    hana "Geh...!"
    "Just like that it was over."
    "A sudden, short, and sharp orgasm and Hana released me from her hold."
    "Breathing resumed. On both of our ends."
    "Erratic, short, soft breaths."
    hana "Good o-one, [mcf]. That was...."
    hana "Awesome."
    scene black with fade
    mc "C'mere you..."
    show screen textbox2 with dissolve
    scene w2_0804 with fade
    hana "Mmmh, cuddles..."
    scene w2_0803 with dissolve
    "Pulling her close so we could share in a collected post-coital bliss, Hana snuggled next to me."
    scene w2_0805 with dissolve
    mc "Didn't take you for the type."
    scene w2_0806 with dissolve
    hana "Eh? EVERYONE loves cuddling, numbskull."
    scene w2_0805 with dissolve
    mc "That's not true. Try to picture Mrs. Pulman..."
    scene w2_0807 with dissolve
    hana "First of all, gross."
    hana "Secondly... anyone who's NOT a vampire likes to cuddle."
    "She rubbed her face into my chest like some kind of cat."
    scene w2_0804 with dissolve
    hana "Let's stay like this awhile, please..."
    scene w2_0805 with dissolve
    mc "Yeah, of course..."
    mc "Is everything okay with you?"
    scene w2_0806 with dissolve
    hana "Why do you ask?"
    scene w2_0805 with dissolve
    mc "Just felt like the question to ask."
    scene w2_0804 with dissolve
    hana "Mmmh... yeah, I'm fine. Just the usual stress in my life."
    scene w2_0805 with dissolve
    mc "Want to tell me about it?"
    scene w2_0804 with dissolve
    hana "Not right now, but... maybe later?"
    scene w2_0805 with dissolve
    mc "I'd be happy to hear it."
    scene w2_0804 with dissolve
    stop music fadeout 3.0
    hana "...thanks, [mcf]."
    scene w2_0803 with dissolve
    "Just like that, we fell into a comfortable silence."
    "So comfortable that..."
    scene black with fade
    if not persistent.w2HanaBDGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w2HanaBDGallery = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    "........."
    mc "......."
    hana "..."
    $ renpy.end_replay()
    jump w2June08Start



label w2June08Start:

    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/page-turn.wav"
    scene titlecard_base with blinds
    $ renpy.pause(1.5, hard=True)
    play music "music/ill-remember-you.ogg"
    scene titlecard_week2 with dissolve
    $ renpy.pause(3, hard=True)
    scene titlecard_week2full with dissolve
    $ renpy.pause(3, hard=True)

    scene w2_0808 with pixellate
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    mc "Why do I have to apologize? They had him pinned on the ground!"
    scene w2_0809 with dissolve
    vic "It's good that you wanted to stand up for your friend, but there's such a thing as a disproportionate response. Do you know what that means, [mcf]?"
    scene w2_0810 with dissolve
    mc "Ummm..."
    scene w2_0811 with dissolve
    vic "That's okay. It's a big word, isn't it?"
    vic "Let's say I grounded you for a month and took away your TV privileges for chewing with your mouth open. How would that make you feel?"
    scene w2_0812 with dissolve
    mc "Angry..."
    scene w2_0813 with dissolve
    vic "Exactly. It wouldn't be fair. The punishment doesn't fit the crime."
    vic "Do you see what I'm getting at? A rock is a dangerous weapon, it can seriously hurt or kill someone."
    vic "You're lucky that boy only needed a few stitches and that his father is a reasonable man, but you've got to go to his house and apologize in person."
    scene w2_0808 with dissolve
    mc "But, mom... I don't FEEL sorry about it. It even felt good to--"
    scene w2_0809 with dissolve
    vic "I know, and that's something you and I will work on together, but for now you need to at least pretend you're sorry."
    scene w2_0808 with dissolve
    mc "You want me to lie?"
    scene w2_0809 with dissolve
    vic "You've got to pretend. I know it's not something a good mother would say, but it's the only way to keep the school out of it. You could get expelled."
    scene w2_0808 with dissolve
    mc "I understand. I'll do it."
    scene w2_0814 with dissolve
    vic "Thank you, [mcf]."
    "..."
    scene w2_0815 with dissolve
    mc "Ummm, Mom..."
    scene w2_0816 with dissolve
    vic "Yes, dear?"
    scene w2_0817 with dissolve
    mc "Am I bad person if I liked hitting him?"
    scene w2_0818 with dissolve
    vic "[mcf]... that's..."
    scene w2_0819 with dissolve
    vic "A person can't help how they feel. What they can control is what they choose to do."
    scene w2_0820 with dissolve
    vic "Your heart was in the right place in wanting to help Ian. That's one of the things I love the most about you."
    vic "Your father was the same way with his nonprofit work. It's just... if there's no adults around to help you, use your... fists?"
    scene w2_0817 with dissolve
    mc "So punching them is not a disproportionate response?"
    scene w2_0821 with dissolve
    vic "{size=-10}Oh god, I'm so bad at this...{/size=-10}"
    scene w2_0822 with dissolve
    mc "Okay, I'll punch them next time."
    scene w2_0819 with dissolve
    vic "No, I didn't mean-- mmmg, o-only if there isn't an adult to help and it's your only option!"
    scene black with fade
    "......"
    "..."
    scene w2_0823 with sunshine
    mc "Mmmh..."
    $ date = "june08day"
    show june08day with squares
    "The morning rolled around in an unexpectedly quiet way for having three house guests."
    scene w2_0824 with dissolve
    "My eyes opened on their own, not pried open by any commotion or noise."
    scene w2_0825 with dissolve
    $ unread_hana = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve

    if hanaFriendFlag == True:
        $ history_hana = "Along with Ian and Mina, Hana crashed at my place following my birthday party. We shared a bed and she got more than a little amorous, but I turned her down. I'm unsure if I want to go down that route with her."
    if w2HanaSex == True:
        $ history_hana = "Along with Ian and Mina, Hana crashed at my place following my birthday party. We shared a bed and one thing led to another..."
    if hanaFlag == False:
        $ history_hana = "Along with Ian and Mina, Hana crashed at my place following my birthday party. We shared a bed and had a good night's sleep."

    mct "(Hana must already be up.)"

    scene w2_0826 with fade
    mct "(...or maybe she's already left?)"
    mct "(Ian and Mina are nowhere in sight, either.)"
    $ renpy.music.set_volume(.3, 2, channel = "ambient")
    play ambient "sound effects/shower.wav"
    scene w2_0827 with fade
    mct "(Well, at least one of them is in the shower.)"
    mct "(I'd be surprised if it was all three...)"
    stop music fadeout 3.0
    scene black with fade
    mct "(Whoever it is, will be greeted with a hot cup of coffee when they get out.)"
    "......"
    "..."
    scene w2_0828 with fade
    mct "(...oh?)"
    stop ambient fadeout 3.0
    "It seems Ian left me a text message while I slept."
    "It read: \"I wanted to give you two lovebirds some space, so Mina and I split. Just don't forget your weekly meeting with Kat today."

    if w2HanaSex == True:
        mct "(Oh, give me a break...)"

    if hanaFriendFlag == True:
        mct "(Oh, give me a break...)"
        mct "(He misunderstood things.)"


    if hanaFlag == False:
        mct "(Oh, give me a break...)"
        mct "(He's still misunderstanding things...)"

    $ renpy.music.set_volume(1, 2, channel = "ambient")
    mct "(Right though, it is Monday. Which means I need to be at the Club by noon.)"
    mct "(It's when we all learn what the week's theme will be.)"
    play sound "sound effects/door-open.wav"
    scene w2_0829 with dissolve
    play music "music/that-one-bar-scene.ogg"
    hana "*yawn* Moooorning."
    scene w2_0830 with dissolve

    if toughness >= 20:
        mc "Hey. I made some coffee. Take it."
    else:
        mc "Hey. I made some coffee. Want some?"

    scene w2_0831 with dissolve
    hana "I used some of your body wash, I hope you don't mind."

    if w2HanaSex == True:
        scene w2_0835 with dissolve
        hana "Definitely needed it after the mess we made."

    scene w2_0833 with dissolve
    mc "Heh, yeah... of course I don't mind. Did you sleep well?"

    if w2HanaSex == True:
        scene w2_0834 with dissolve
        hana "Hehehe, after what you did to me last night, what do you think?"
        hana "Thanks for the coffee."

    if hanaFriendFlag == True:
        scene w2_0835 with dissolve
        hana "Like a baby. Last night was... nice."
        hana "Thanks for the coffee."

    if hanaFlag == False:
        scene w2_0835 with dissolve
        hana "Yep, all good. Thanks for letting me use your bed."
        scene w2_0833 with dissolve
        mc "I was just being a good host like I was taught."
        scene w2_0835 with dissolve
        hana "Thanks for the coffee too."

    scene w2_0836 with dissolve
    mc "Y'know, Miss Rhodes... you're quite the polite young woman."
    scene w2_0837 with dissolve
    hana "Oh, shut up. Did you take me for some sort of ingrate?"
    scene w2_0838 with dissolve
    mc "You do cultivate a certain persona..."
    scene w2_0839 with dissolve
    hana "Okay, well fuck you for the coffee then."
    scene w2_0840 with dissolve
    mc "That's more like it."
    scene w2_0841 with dissolve
    hana "..."
    "Hana looked down at her coffee as if suddenly lost in thought."
    mc "Is everything okay?"

    if w2HanaSex == True:
        scene w2_0842 with dissolve
        hana "Yeah, it is, you're not going to be weird about this going forward, right?"
        scene w2_0841 with dissolve
        mc "Are you asking if I think you're my girlfriend now? Don't be silly."
        scene w2_0843 with dissolve
        hana "Oh? Would that be silly?"
        scene w2_0844 with dissolve
        "She had a blank expression that was hard to read."
        mc "No, it's just I know we were both just a little drunk and horny."
        scene w2_0843 with dissolve
        hana "Actually, I don't normally do that even if I'm shitfaced. I'm usually a more traditional kind of girl..."

    if hanaFriendFlag == True:
        scene w2_0842 with dissolve
        hana "Yeah, uh... I just hope you don't think I'm a weirdo for what I tried to do last night."
        scene w2_0841 with dissolve
        hana "..."
        "A thick silence hung in the air between us as I considered my words."
        scene w2_0844 with dissolve
        mc "Hey, not at all... I just hope you're not insulted I turned you down."
        scene w2_0843 with dissolve
        hana "No, I get it. I don't usually just throw myself at someone I know a few weeks. I'm actually a more traditional kind of girl..."


    if hanaFlag == True:
        scene w2_0842 with dissolve
        hana "I owe that to being raised by a woman like my mom I guess."
        scene w2_0841 with dissolve
        mc "Would you tell me a little about her? I'm a bit curious, given our similar childhoods."
        scene w2_0843 with dissolve
        hana "I guess I wouldn't mind talking about her, but it's kind of a bummer for morning coffee. You sure you want to hear it?"
        scene w2_0844 with dissolve
        "I gave Hana the go-ahead to talk my ear off with a nod."
        scene w2_0845 with dissolve
        hana "Okay..."
        scene w2_0847 with dissolve
        hana "You remember what I said about August and her sickness?"
        scene w2_0846 with dissolve
        mc "You said she had a neurodegenerative disease, right?"
        scene w2_0847 with dissolve
        hana "Uh huh. Huntington's. You know anything about it?"
        scene w2_0836 with dissolve
        mc "A little..."
        scene w2_0846 with dissolve
        "Huntington's disease was a terrible thing, but the most sobering and pressing thing about it at this very moment was..."
        scene w2_0848 with dissolve
        hana "..."
        mc "Do you have...?"
        scene w2_0849 with dissolve
        hana "No, thank god. I got lucky. Fifty fifty shot of her passing down the gene and it missed me. It's about the only thing I'm thankful to August for."
        scene w2_0848 with dissolve
        "Hana continued to stare a hole in the surface of her drink, before looking up and smiling at me."
        scene w2_0834 with dissolve
        hana "That part is kind of funny in a cosmic, fucked up \"God laughs\" sort of way."
        scene w2_0833 with dissolve
        "All I did was simply return her smile. No doubt she'd heard the usual platitudes in droves. Stuff like \"I can't imagine what you're going through\" or something else as equally vacant."
        scene w2_0836 with dissolve
        mc "How bad is she?"
        scene w2_0837 with dissolve
        hana "She had her first onset of symptoms in her mid 30s. Some coordination loss, depression, irritability..."
        hana "It got bad a year and a half ago. Difficulty walking, memory loss, trouble speaking... that's when she had to get live-in care. I couldn't cut it by myself anymore."
        scene w2_0838 with dissolve
        mc "That's what August pays for?"
        scene w2_0847 with dissolve
        hana "Among other things. He takes care of some of her other bills too."
        scene w2_0846 with dissolve
        mc "Does she know?"
        scene w2_0837 with dissolve
        hana "Fuck, no. She'd absolutely refuse his help - which I get, trust me, but there's also being pragmatic."
        hana "Do you think I'm wrong to hide that from her?"
        scene w2_0838 with dissolve
        mc "No. You should do what you've got to do to keep her comfortable and make things easier for you."
        scene w2_0850 with dissolve
        hana "Thanks. That's what Jerrica says too, but it's more convincing coming from a person who hasn't pushed a car into a lake to defend my honor."
        scene w2_0851 with dissolve
        "I raised a curious eyebrow."
        scene w2_0852 with dissolve
        hana "Hehe, yeah. She's my ride-or-die bitch. Maybe I'll tell you about it later?"
        scene w2_0851 with dissolve
        mc "Yeah, I'd like to hear THAT story."
        scene w2_0853 with dissolve
        hana "She's usually all \"fuck what she wants\", but she's blinded by her concern for me."
        hana "I don't think she fathoms how scary it must be to slowly lose your ability to walk or the sheer terror and confusion at not being able to speak sometimes."
        scene w2_0851 with dissolve
        mc "Was that what was on your mind last night?"
        scene w2_0853 with dissolve
        hana "Uh huh, we had a fight about something stupid and small yesterday... oh!"
        scene w2_0854 with dissolve

        if w2HanaSex == True:
            hana "Please don't get the wrong idea. I didn't jump your bones just because I was feeling bad and you were a convenient lay."
        if hanaFriendFlag == True:
            hana "Please don't get the wrong idea. I didn't try and jump your bones just because I was feeling bad and you were a convenient lay.."

        scene w2_0850 with dissolve
        hana "I wouldn't just do that with anyone. I do think you're cool."
        scene w2_0851 with dissolve
        mc "You do, do you?"
        scene w2_0853 with dissolve
        hana "Ugh, that fucking look. I'm not saying I want to date you, it's just something clicked the other night after that run in with Warren and I just thought we could both have some fun last night."
        scene w2_0851 with dissolve
        mc "So I guess you don't mind if I tell people we're friends then?"
        scene w2_0852 with dissolve
        hana "I can live with that."
        scene w2_0851 with dissolve
        "Hana and I shared a moment of solidarity. I wasn't really sure of the path we were going down. Friend or something more, but it felt good."
        scene w2_0855 with dissolve
        hana "So, what's on your busy schedule today? Should I get out of your hair?"


    if hanaFlag == False:
        scene w2_0855 with dissolve
        hana "Yep, everything is fine. What are you getting up to today? Should I get out of your hair?"


    scene w2_0836 with dissolve
    mc "I have to be at the club by noon. There's a weekly meeting about the exhibition."
    scene w2_0856 with dissolve
    hana "Blech."
    scene w2_0837 with dissolve
    hana "What could you possibly need to meet about? You got graphs and pie charts about the number of times those old fucks cream their pants?"
    scene w2_0833 with dissolve
    mc "I haven't seen that so far, but it's still early in the month."
    scene w2_0836 with dissolve
    mc "{size=-10}Wouldn't be surprised, though...{/size=-10}"
    scene w2_0847 with dissolve
    hana "Noon? You don't have a car, right?"
    scene w2_0855 with dissolve
    hana "Want a ride? I've got to go in sometime today and speak with the old man. Might as well be then."
    scene w2_0832 with dissolve
    mc "Really? Yeah, that'd be great."
    scene w2_0857 with dissolve
    hana "Alright, then. Guess you need to get ready?"
    scene w2_0858 with dissolve
    mc "Yeah, I'll take a shower first. Just make yourself at home."
    scene w2_0857 with dissolve
    hana "Will do."
    scene black with fade
    stop music fadeout 3.0
    play sound "sound effects/notification.wav"
    $ Hana_Relations = "Friends"
    show relationhana with dissolve
    ".........."
    "......"
    "..."
    scene pr0042 with blinds
    play sound "sound effects/car-beep.wav"
    "After a trek up to the top, Hana and I found Warren in Jacob's usual spot."
    "The way Warren asked if we came in together bugged me for some reason."
    play music "music/cello-suite-No-1-G-Major-Prelude.ogg"
    scene w2_0859 with blinds
    war "Meeting's in the studio this week, kid."
    scene w2_0860 with dissolve
    mc "How come?"
    scene w2_0859 with dissolve
    war "Head back down and find out."
    scene w2_0861 with dissolve
    hana "Is the old man in his office?"
    scene w2_0862 with dissolve
    war "As far as I know. Want me to check for you?"
    scene w2_0863 with dissolve
    hana "No, I'll just knock on the door myself."
    scene w2_0864 with dissolve
    war "I was hoping you'd say that."
    scene black with fade

    if mod_week1_interview:
        "With that, Hana and I split off and I made my way to the room where I interviewed the girls earlier last week."
    if w1RoseGonzo == True and not mod_week1_interview:
        "With that, Hana and I split off and I made my way to the room where I interviewed Rosalind earlier last week."
    if w1FelGonzo == True and not mod_week1_interview:
        "With that, Hana and I split off and I made my way to the room where I interviewed Felicia earlier last week. "
    if w1VeroGonzo == True and not mod_week1_interview:
        "With that, Hana and I split off and I made my way to the room where I interviewed Veronica earlier last week. "

    scene w2_0865 with circlewipe
    "In the studio, stood Kat. All by her lonesome."
    scene w2_0866 with dissolve
    kat "Good afternoon, [mcf]. You're right on time."
    scene w2_0867 with dissolve
    "Without even looking at me, she eerily greeted me by name as if she had eyes on the back of her head."
    scene w2_0868 with dissolve
    mc "Is it just me so far?"
    scene w2_0866 with dissolve
    kat "The girls have already arrived and are getting dressed as per my instructions. How are you doing today?"
    scene w2_0868 with dissolve
    mc "Pretty good actually, thanks for asking."
    scene w2_0869 with dissolve
    kat "I'm happy to hear that. Since yesterday was your birthday, you must've spent it wisely."
    scene w2_0870 with dissolve
    kat "One should celebrate their youth while they have the chance."
    scene w2_0871 with dissolve
    mc "That's right, it was. I had lunch with my mom and then spent the evening with Ian and Hana."
    mc "Speaking of which..."
    "The conversation I had with my mother yesterday struck me like a bolt of lightning and sparked a fit of anger."
    scene w2_0872 with dissolve
    kat "You suddenly look agitated. Is something wrong?"
    scene w2_0873 with dissolve
    mct "(Am I really making it that obvious...?)"
    "Whatever. Putting that aside, her trespass into my personal life wasn't something I could simply overlook. I had to bring it up and say something."
    hide screen textbox2 with dissolve

    menu:
        "Calmly bring up her phone call with your mother.":

            show screen textbox2 with dissolve
            mc "There is, actually. Your bit of subterfuge the other day with my mother."
            mc "What was that about, Mrs. Pulman?"
            "I swallowed my anger and delivered the question with a steady voice."
            scene w2_0874 with dissolve
            kat "Oh, that?"
            scene w2_0873 with dissolve
            mc "Yes. {b}That{/b}."
            scene w2_0875 with dissolve
            kat "Mmmh, you hide it well [mcf], but I can tell that underneath that placid expression you're angry with me."
            scene w2_0877 with dissolve
            mc "Yes."
            scene w2_0878 with dissolve
            kat "I love that look in your eye by the way. It reminds me of the suffocating silence just before a lioness snatches up its prey. You're not going to gobble me up, are you?"
            scene w2_0879 with dissolve
            mc "Can't you just answer me like a normal person"
            scene w2_0880 with dissolve
            kat "Sorry. You have every right to be mad with me."
            scene w2_0878 with dissolve
            kat "Your work for the club and private life are separate things. From your perspective, I had no business crossing the two all willy nilly like that."
            scene w2_0875 with dissolve
            kat "Please understand, I didn't do it to get a rise out of you nor did I expect it to be a secret that wouldn't get back to you."
        "Angrily bring up her phone call with your mother.":

            $ w2KatAnger = True

            show screen textbox2 with dissolve
            mc "Yeah, I was just wondering what business it is of yours to be calling my mother with some bullshit excuse."
            mc "What was that about, {i}Kathleen{/i}?"
            "I decided here and now that some transgressions fall outside the need for carefully considered, pro-and-con, calculated reaction."
            scene w2_0874 with dissolve
            kat "Oh, that?"
            scene w2_0873 with dissolve
            mc "That...?!"
            scene w2_0875 with dissolve
            kat "Mmmh, that look in your eyes..."
            kat "You're very angry with me, aren't you?"
            scene w2_0877 with dissolve
            mct "(No shit...)"
            scene w2_0876 with dissolve
            kat "Interesting."
            scene w2_0877 with dissolve
            mc "What is?"
            scene w2_0875 with dissolve
            kat "You look like you want to smack me and put me in my place, which is... fair."
            scene w2_0878 with dissolve
            kat "Your work for the club and private life are separate things. From your perspective, I had no business crossing the two all willy nilly like that."
            scene w2_0879 with dissolve
            mc "I think you just like toying with people and pushing their buttons."
            scene w2_0880 with dissolve
            kat "There is truth in that accusation. That's my job here after all, but please understand my phone call to your mother wasn't me twisting your screws."


    scene w2_0877 with dissolve
    mc "Why did you do it then?"
    scene w2_0875 with dissolve
    kat "I was turning over some rocks, looking to glean a little more about you."
    scene w2_0877 with dissolve
    mc "Was the background check you ran not enough?"
    scene w2_0881 with dissolve
    kat "You can only learn so much from a piece of paper. Hearing it straight from a mother's mouth has its own advantages."
    scene w2_0877 with dissolve
    mc "What were you hoping to learn?"
    scene w2_0875 with dissolve
    kat "Anything that could be useful in knowing how to motivate and manage you. Normally I wouldn't just come out and say it, but I'm well aware of how your mind works."
    kat "You do your due diligence in securing your own best interests, so I hope you would respect me doing the same."
    scene w2_0877 with dissolve
    mc "I'm sorry, but \"manage\" me? Why would you ever...?"
    scene w2_0882 with dissolve
    kat "Darius... the answer to your question is {b}Darius{/b}. The last person who had your job {b}blackmailed{/b} me."
    scene w2_0883 with dissolve
    mc "........."
    scene w2_0884 with dissolve
    mc "......"
    mc "..."
    scene w2_0885 with vpunch
    stop music
    mc "--!"
    "A chill ran down my spine as my mind drew what felt like a foregone conclusion."
    scene w2_0899 with pixellate
    chuck "The lad who had your job before you, Darius, used to live here as well - before he suddenly disappeared on us, that is."
    scene w2_0886 with pixellate
    mc "He blackmailed you and just... \"disappeared\"?"
    scene w2_0887 with dissolve
    kat "Oh...?"
    scene w2_0888 with dissolve
    kat "Hahaha! Oh! Seriously?"
    scene w2_0889 with dissolve
    kat "I'm glad you think I'm capable of something like that, but no. I didn't say he {i}tried{/i} to blackmail me. He succeeded"
    kat "He up and absconded after he got what he was after. Basically, he fell in love and wanted to void an agreement we had with one of the whores."
    scene w2_0890 with dissolve
    mct "(Why was she telling me this...?)"
    "I traced the lines of her face in my mind, looking to discern what lurked behind her composure."
    scene w2_0891 with dissolve
    kat "A trifling reason for such a monumentally stupid action, but a lesson learned for me. A fool will always find a way to surprise you..."
    kat "As far as August and Chuck are concerned, he simply left. August would've overreacted if he knew the details of his departure."
    scene w2_0892 with dissolve
    mct "(Dealing with this woman was exhausting.)"

    if w2KatAnger == True:
        scene w2_0893 with dissolve
        mc "I don't give a damn why you made the call, just don't poke your nose into my family life."
    else:
        scene w2_0894 with dissolve
        mc "I don't care why you made the call, just don't go poking around in my family life."

    mc "As good as this job is, that's non-negotiable for me."
    scene w2_0895 with dissolve
    kat "One conversation with your lovely mother was enough. On the plus side, it did help me come up with a present for-"
    scene w2_0896 with dissolve
    fel "Got to say, Kat, you've got some interesting pieces in your wardrobe."
    play music "music/dancebroom-riddim.ogg"
    scene w2_0897 with wipeleft:
        subpixel True
        yalign 1.0
        xalign 0.6
        linear 4 yalign 0.3
    fel "You wear this at home for Judge Hubby?"
    "Felicia made her appearance adorned in a mouth-droppingly skimpy..."
    scene w2_0898 with dissolve
    mct "(Is that even a bikini?)"
    "Whatever you'd call it, the small straps of embossed material that nearly constituted the entire outfit were tautly stretched across her torso, held up from the sheer shapeliness of her curves."
    scene w2_0900 with dissolve
    $ renpy.music.set_volume(.2, 0.5, channel = "music")
    kat "Wouldn't you like to know what I get up to."
    scene w2_0901 with dissolve
    fel "I'm sure you get into all kinds of freaky stuff."
    play sound "sound effects/cowbell.wav"
    scene w2_0902 with dissolve
    "*Clank*"
    scene w2_0903 with dissolve
    mct "(...eh?)"
    scene w2_0900 with dissolve
    kat "I'm glad your sense of humor is still intact after the last exhibition."
    scene w2_0901 with dissolve

    if w1ExIntuitionGameWinnerFel == True:
        fel "Why wouldn't it be? I barely got to participate."
    else:
        fel "The second game was pretty rough, I'll give you that, but if that was only the first week..."

    play sound "sound effects/cowbell.wav"
    scene w2_0902 with dissolve
    play sound "sound effects/cowbell.wav"
    "*Clank* *Clank*"
    "A tin-like ring grew less and less distant."
    scene w2_0903 with dissolve
    mct "(Is that a... bell?)"
    play sound "sound effects/cowbell.wav"
    pause 0.8
    play sound "sound effects/cowbell.wav"
    pause 0.8
    play sound "sound effects/cowbell.wav"
    "*Clank* *Clank* *Clank*"
    scene w2_0904 with dissolve
    fel "I'm looking forward to hearing what's next."
    scene w2_0905 with dissolve
    kat "You won't be waiting long, since it seems the other two were on your heel."
    $ renpy.music.set_volume(1, 0.5, channel = "music")

    scene w2_0906 with dissolve:
        subpixel True
        xpan -60
        yalign 0.38
        linear 3 xalign 0.14

    mc "--!"
    "Where Felicia was risqué, the other two were equally ridiculous but in different ways."
    "From a glance, the three outfits had nothing else in common. If there was a unifying theme here, it was lost on me."

    scene w2_0907 with dissolve:
        subpixel True
        yalign 1.0
        xalign 0.6
        linear 4 yalign 0.225

    "Rosalind, at least when compared to Felicia, wore a moderately modest bikini. The kicker was the cow print pattern and the bell draped from a leather collar around her neck."
    "Veronica wore an overly cute, obnoxiously pink set of lingerie accented with numerous pearlescent beads. It was, to say the least, totally incongruent with her fiery personality and Amazonian build."
    scene w2_0908 with dissolve
    "Both of them wore muddied expressions. Rosalind looked like she was trying to hide her unease, but Veronica set her eyes straight ahead, in an alluring mix of embarrassment and anger."
    scene w2_0909 with dissolve
    rose "Ngh... what was... wrong with the bunny costume?"
    scene w2_0910 with dissolve
    kat "Don't be so self-conscious dear. You look adorable."
    scene w2_0911 with dissolve
    kat "You remind me of the cute Holstein dairy cow we had on our ranch growing up. Mother gave her to me as a pet."
    kat "Unlike you however, she was wickedly smart. She was always trying to escape."
    scene w2_0912 with dissolve
    ver "I'm sorry you asked."
    scene w2_0913 with dissolve
    kat "How do you find your attire, Miss Lynch? I thought you could use a touch of femininity in your life."
    scene w2_0914 with dissolve
    ver "You're not going to get a rise out of me."
    scene w2_0913 with dissolve
    kat "Why are you blushing then dear?"
    scene w2_0915 with dissolve
    fel "That looks really good on you, Red! You think so too, right [mcf]?"
    "Jumping in to beat back Veronica's self-consciousness, Felicia tossed a question in my lap like a game of hot potato and brought me into a conversation I was happily staying out of."
    scene w2_0916 with dissolve

    if toughness>=20:
        mc "I agree, she looks smoking hot."
    else:
        mc "I agree, I think she looks cute."

    if Veronica_Affection>=10:
        scene w2_0918 with dissolve
        ver "Pssh, who asked you?"
        scene w2_0919 with dissolve
        mc "Felicia did."
        scene w2_0918 with dissolve
        ver "So she did..."
    else:

        scene w2_0917 with dissolve
        ver "Gee, thanks."

    scene w2_0920 with dissolve
    fel "So... We're all here then?"
    scene w2_0921 with dissolve
    kat "Not all. I sent Ian to grab me a coffee, but I can begin explaining this week's theme and then I'll tease your little \"side\" mission."
    stop music fadeout 3.0
    scene w2_0922 with dissolve
    "That last bit perilously stuck out like a sore thumb."
    scene w2_0923 with dissolve
    kat "Take a seat, girls."
    play music "music/covert-affair.ogg"
    scene w2_0924 with fade
    kat "Good. Now, this week's theme is a fun one... {b}shame{/b}."
    kat "Some people believe that shame is a social construct, a thing that only exists when perceived through the lens of a culture's mores and norms."
    scene w2_0925 with dissolve
    kat "Other people believe it's an evolutionary part of the human condition, an adaptive trait for a social, group-living animal."
    scene w2_0924 with dissolve
    kat "It has many other words: humiliation, indignity, disgrace, self-abasement..."
    scene w2_0926 with dissolve
    ver "We know what the word means."
    scene w2_0927 with dissolve
    rose "How is that any different from last week?"
    scene w2_0928 with dissolve
    kat "The difference is shame was the byproduct last week. This time it's the focus."
    scene w2_0929 with dissolve
    fel "What does that mean practically speaking?"
    scene w2_0924 with dissolve
    kat "You'll have to wait and see. If I gave you time to prepare, it would lessen the impact."
    kat "Now, where was I?"
    scene w2_0930 with dissolve
    mc "The two theories."
    scene w2_0925 with dissolve
    kat "Right! Thank you, [mcf]."
    kat "Now, speaking from personal experience, I'm inclined to believe the first theory. However, it really doesn't matter what shame {i}is{/i}."
    scene w2_0924 with dissolve
    kat "What's important is that in your training to become proper whores, you learn to {b}weaponize{/b} it. To use being ashamed as a tool to entice men."
    scene w2_0931 with dissolve
    ver "Oh, of course. That's totally a natural way of thinking."
    scene w2_0928 with dissolve
    kat "Sarcasm aside, you're right. Using your own embarrassment to your advantage is an unnatural thing, that's why over the next few days [mcf] and each of you girls will carry out a \"mission\" for our patrons' pleasure that will help that."
    scene w2_0932 with dissolve
    rose "I'm afraid to ask..."
    scene w2_0928 with dissolve
    kat "Just know that each one of you will be called upon sometime over the next four days to participate in a photoshoot. You'll be filled in on the details closer to each of your appointed missions."
    kat "Speaking of photoshoots, that's also why we're in the studio today. We're going to prepare a small photo album for our patrons."
    play sound "sound effects/door-openclose.wav"
    scene w2_0929 with dissolve
    fel "I kinda figured as much."
    scene w2_0933 with wipeleft
    kil "Hey! Sorry, I'm late. They fucked your order."
    mc "You sure you weren't flirting with the barista?"
    scene w2_0934 with dissolve
    kil "Very funny."
    scene w2_0935 with dissolve
    kil "Guess I'm now the official gofer."
    mc "Sorry."
    kil "You kidding? It's great that you're here."
    scene w2_0936 with dissolve
    kil "So, you have a good time last night bunking down with our moody princess?"

    if hanaFriendFlag == True:
        mc "I think you're reading too much into it. We didn't do anything."
        scene w2_0937 with dissolve
        kil "Even if that's true, I still think there's something there."

    if w2HanaSex == True:
        mc "I'll just say I'm glad you invited her."
        scene w2_0937 with dissolve
        kil "Hehe, you're welcome."

    if hanaFlag == False:
        mc "You've got the completely wrong idea, dude."
        scene w2_0938 with dissolve
        kil "Eh, really? I could've sworn I was picking up on some mutual attraction thing."

    scene w2_0939 with dissolve
    kat "Both Mr. Beaufort and [mcf] will be photographers for this session."
    kil "Two is a bit unusual.."
    scene w2_0940 with dissolve
    kat "[mcf] will be acting independently for me later in the week, so this will be a good chance for him to get acclimated to using a camera. You'll show him the ropes, won't you?"
    kil "Sure, it's not too complicated."
    stop music fadeout 3.0
    stop ambient fadeout 1.0

label w2ShamePhotoshoot:

    if _in_replay:
        show transitionkathleen01 with cmet
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

    scene w2_0941 with circlewipe
    "After a quick tutorial from Ian about how to work the camera, which basically boiled down to what some odd five buttons did, we were ready to start the shoot."
    scene w2_0942 with dissolve
    mc "Good to go. Should they start posing?"
    scene w2_0943 with dissolve
    kat "I'll let you direct the models, Mr. [mcl]. Instruct them on what to do."
    scene w2_0944 with dissolve
    mc "Me? Okay, uh..."
    "Put on the spot, I was at a loss on how to begin."
    scene w2_0945 with dissolve
    kil "Start with some basic posturing and go from there. It might give you some idea on how to continue."
    scene w2_0946 with dissolve
    mc "That makes sense."
    mc "Alright, girls let's get some poses going."
    $ renpy.music.set_volume(.2, 0, channel = "music")
    play music "music/six-days-of-heat-pt2.ogg"
    scene w2_0947 with fade
    "A few shots of the Carnations together seemed like a good way to start things off."
    play sound "sound effects/camera-phone-shutter.wav"
    with flash
    mc "You're looking a bit uninterested, Veronica."
    scene w2_0948 with dissolve
    ver "Sorry?"
    scene w2_0947 with dissolve
    mct "(Well, it is kind of attractive in its own weird way.)"
    mc "Get closer together like you're all best friends."
    scene w2_0949 with dissolve
    $ renpy.music.set_volume(.4, 2, channel = "music")
    "Veronica pulled the girls closer."
    play sound "sound effects/camera-phone-shutter.wav"
    with flash
    mc "That's good, maybe smile a little more?"
    scene w2_0950 with dissolve
    play sound "sound effects/camera-phone-shutter.wav"
    with flash
    "One of the few times you can tell a woman to smile without being an asshole."
    scene w2_0951 with dissolve
    kat "What is this, a family photo?"
    scene w2_0952 with dissolve
    mc "Right. How about something more flirty?"
    scene w2_0953 with dissolve
    rose "Flirty...?"
    scene w2_0952 with dissolve
    mc "Just do what comes to your head."
    scene w2_0954 with dissolve
    play sound "sound effects/camera-phone-shutter.wav"
    with flash
    mc "Hmm, something's missing..."
    mc "Veronica, why don't you strike a pose?"
    scene w2_0955 with dissolve
    $ renpy.music.set_volume(.6, 2, channel = "music")
    ver "Like this?"
    scene w2_0956 with dissolve
    play sound "sound effects/camera-phone-shutter.wav"
    with flash
    mc "Perfect."
    scene w2_0957 with dissolve
    kil "We should get some solo action I think."
    kat "That's a good idea, Mr. Beaufort."
    mc "Alright, girls you heard 'em. Let's get individual shots. We'll start with Rosalind."
    scene w2_0958 with dissolve
    rose "Where do you want me?"
    scene w2_0959 with dissolve
    mc "Right where you are."
    scene w2_0960 with dissolve
    kil "That means you two need to get out of our shot."
    $ renpy.music.set_volume(.1, 2, channel = "music")
    scene w2_0961 with wiperight
    "Veronica and Felicia left Rosalind alone under the scrutiny of our viewfinders."
    rose "Hehe..."
    kil "You're the star now, Rosie. Give us something good."
    rose "Um..."
    scene w2_0962 with dissolve
    play sound "sound effects/camera-phone-shutter.wav"
    with flash
    "Rosalind contorted her body into an odd, distinctly unflattering pose."
    "We were both inexperienced with this, but I was sure as hell glad to be on this side of the camera."
    scene w2_0963 with dissolve
    rose "This is no good... is it?"
    scene w2_0964 with dissolve
    "If I had to guess, Rosalind probably picked that up from our expressions."
    scene w2_0965 with dissolve
    kil "Something more sexy."
    scene w2_0964 with dissolve
    "She looked at me expectantly, as if asking me for more concrete direction."
    mc "Hmm, how about..."
    "One obvious route came to mind, given the theme of her outfit."

    if toughness>=21:
        mc "You strike a pose that shows off those \"udders\" of yours?"
    elif toughness>=18:
        mc "How about you strike a pose that shows off those beautiful breasts of yours? Seems fitting."
    elif toughness<=14:
        mc "How about you strike a pose that shows off your bust. Y'know considering what you're wearing..."

    scene w2_0966 with dissolve
    "Rosalind thought for a moment, before deciding on a pose."
    play sound "sound effects/boing.wav"
    scene w2RoseBoobBounce with dissolve
    $ renpy.music.set_volume(.5, 3, channel = "music")
    "Slowly she lifted her arms up, stuck out her chest, and placed her arms behind her head. The pose lent her already large breasts an even greater sense of heft."
    "I waited for the eye-pleasing jiggle of her breasts to settle, before..."
    play sound "sound effects/camera-phone-shutter.wav"
    with flash
    "*Snap!*"
    mc "Perfect. Let's get a couple more. Sit down on the couch and use your forearm to cup your breasts."
    scene w2_0973 with fade
    rose "...like this?"
    play sound "sound effects/camera-phone-shutter.wav"
    with flash
    scene w2_0974 with dissolve
    mc "Even more perfect."
    scene w2_0975 with dissolve
    rose "T-thanks..."
    scene w2_0974 with dissolve
    mc "Same pose, but pull your bikini top to the side this time."
    scene w2_0976 with dissolve
    rose "Okay..."
    scene w2_0977 with dissolve
    "Rosalind did as I asked, exposing her pinkish pale bud."
    play sound "sound effects/camera-phone-shutter.wav"
    with flash
    mc "Let's get one last shot. Something with some oompph to finish off the set."
    scene w2_0978 with dissolve
    rose "What does \"oompfh\" mean?"
    scene black with fade
    mc "Do you have..."
    kil "I uh... I can run up and grab some."

    if toughness>=21:
        mc "Yes, do that."
    elif toughness>=15:
        mc "Would you, please?"
    elif toughness<=14:
        mc "No worries, I can go get it myself."

    "......"
    "..."
    rose "It's c-cold!"
    mc "Just bear with me."
    scene w2_0979 with dissolve
    if toughness>=21:
        mc "It makes you look like a proper dairy cow. What was the name of your cow, Mrs. Pulman?"
        kat "Clarabelle."
        mc "Alright, Rose. Do your best \"Clarabelle\" impression."
        scene w2_0980 with dissolve
        rose "That's not funny..."
        scene w2_0979 with dissolve
        mc "Smile!"
    else:

        mc "It really hammers home the motif."
        kil "Ten minutes behind the camera and he's talking about \"motifs\"..."
        scene w2_0980 with dissolve
        rose "The motif being that I'm a cow..."
        scene w2_0979 with dissolve
        mc "Sorry..."
        scene w2_0980 with dissolve
        rose "It is what it is..."
        scene w2_0979 with dissolve
        mc "Smile for me, this will be the last one."

    scene w2_0981 with dissolve
    play sound "sound effects/camera-phone-shutter.wav"
    with flash
    mc "That should do it."
    if toughness<18:
        mc "Thank you, Rose."
    scene w2_0982 with dissolve
    kil "Who next?"
    scene w2_0983 with dissolve

    if toughness>=21:
        mc "Veronica. Get your ass over here."
    elif toughness<=20:
        mc "Veronica. Switch with Rosalind."

    scene w2_0984 with dissolve
    kil "You're really getting into this directing thing."
    scene w2_0985 with dissolve
    mc "Guess the feeling of being behind a camera does something to you."
    scene w2_0986 with dissolve
    ver "Is this where you want me?"
    mc "Yep, you've got it."
    scene w2_0987 with dissolve
    play sound "sound effects/camera-phone-shutter.wav"
    with flash
    kil "You've got modeling experience, right?"
    scene w2_0988 with dissolve
    ver "For some sports magazines..."
    play sound "sound effects/camera-phone-shutter.wav"
    with flash
    kil "A body like yours is made for showing off."
    mc "Put your arms above your head."
    scene w2_0990 with dissolve
    ver "This good?"
    play sound "sound effects/camera-phone-shutter.wav"
    with flash
    scene w2_0989 with dissolve
    mc "Now get on your stomach like you're crawling."
    scene w2_0992 with dissolve
    ver "Crawling...?"
    scene w2_0991 with dissolve

    if kat_polite == True:
        "As insulting, fucked up, and backwards as Mrs. Pulman's thought process was for Veronica's costume, it was the obvious thing to lean on for the shoot."
    else:
        "As insulting, fucked up, and backwards as Kathleen's thought process was for Veronica's costume, it was the obvious thing to lean on for the shoot."

    mc "Yep, pretend you're a... defeated and humiliated warrior that's been forced to parade around in embarrassing lingerie."
    scene w2_0993 with dissolve
    ver "...okay."
    scene black with fade
    ver "Is this defeated enough for you?"
    scene w2_0994 with dissolve
    play sound "sound effects/camera-phone-shutter.wav"
    with flash
    mc "Beautiful. Kat, would you mind putting a foot on her back?"
    scene w2_0995 with dissolve
    "Veronica glared up at me with a sour expression on her face."

    if toughness<=20:
        "I made sure to mouth a wordless apology."

    kat "Oh? ...sure, it'd be my pleasure."
    scene w2_0996 with fade
    kat "Is this to your satisfaction?"
    play sound "sound effects/camera-phone-shutter.wav"
    with flash
    mc "It is. Let's expand on this concept some more."
    "The question is, who'll be the prop?"
    hide screen textbox2 with dissolve

    menu:
        "Continue with using Kat as a model."(chg=["kathleen_up","veronica_down"]):
            $ Kathleen_Affection += 1
            $ Veronica_Affection -= 1

            show screen textbox2 with dissolve
            "Well, she's already involved in the shoot. Might as well conclude the shoot with her."
            scene w2_0997 with dissolve
            mc "Would you mind sitting back on the couch for me, Mrs. Pulman?"
            scene w2_0998 with dissolve
            kat "What are you thinking?"
            scene w2_0997 with dissolve
            mc "I just think you've been on your feet too long. They could use some rest and care."
            scene w2_0999 with dissolve
            ver "Ugh... let's get it over with."
            scene w2_1000 with circlewipe
            ver "Ggggh..."
            mc "You have it. Now hold that pose."
            play sound "sound effects/camera-phone-shutter.wav"
            with flash
            mc "Give it a quick taste?"
            scene w2_1001 with dissolve
            ver "..."
            mc "Last shot, I promise."
            ver "Mmh..."
            scene w2_1002 with dissolve
            play sound "sound effects/camera-phone-shutter.wav"
            with flash

            if kat_polite == True:
                "Veronica begrudgingly slid her tongue across the sole of Mrs. Pulman's black stockings."
            else:
                "Veronica begrudgingly slid her tongue across the sole of Kathleen's black stockings."

            kat "That's a good look for you, Miss Lynch."
            scene w2_1003 with dissolve
            mc "Thanks for doing that, Veronica."
            scene w2_0984 with dissolve
            kil "Did I already remark that you seem to be really getting into this?"
            scene w2_0985 with dissolve
            mc "We'll move onto Felicia now."
        "Bring Ian in as the final model"(chg=["killian_up"]):

            $ Killian_Bromance +=1

            scene w2_1004 with dissolve
            show screen textbox2 with dissolve
            "Ian seemed to have a thing for Veronica over the last week, so why not let him be the model? Throw the dog a bone, so to speak."
            scene w2_1005 with dissolve
            mc "Ian would you mind stepping in as a model? I'll get all the shots we need."
            scene w2_1006 with dissolve
            kil "What do you want me to do?"
            scene w2_1010 with dissolve
            mc "Some sort of pose that says domineering. Your choice."
            scene w2_1009 with dissolve
            kil "Domineering, eh...? Hmm, I've got an idea."
            scene black with fade
            kil "Let me know if I'm squeezing too tight."
            ver "You don't have to worry about that, pencil arms. Just get the photo quick."
            scene w2_1007 with curtains
            "Ian positioned himself behind Veronica, one arm around her neck and the other pulling her back in an impressive limber display."
            "It definitely fit what I was going for, and deep down, there was something about the position that my lizard brain found pleasing. "
            mct "(Nice one, Ian.)"
            play sound "sound effects/camera-phone-shutter.wav"
            with flash
            "Of course, this was all just a pose. Veronica could easily turn it around on Ian if she wanted."
            mc "Alright, now drop your arm like you just passed out."
            scene w2_1008 with dissolve
            play sound "sound effects/camera-phone-shutter.wav"
            with flash
            mc "Alright, I got the shots."
            mc "Thanks for doing that, Veronica."
            scene w2_1040 with fade
            ver "Honestly, a headlock is pretty low on the list of things you could've asked me to do."
            kil "Did I already remark that you seem to be really getting into this?"
            mc "We'll move onto Felicia now."
        "Do it yourself. Ian can get the shot"(chg=[("maid", Veronica_Horniness >= 4)]):


            scene w2_1005 with dissolve
            show screen textbox2 with dissolve
            mc "I'll jump in and be the model real quick."
            scene w2_1009 with dissolve
            kil "You?"
            scene w2_1010 with dissolve
            mc "I've got a pretty good pose in mind. You can get the shot."
            scene w2_1009 with dissolve
            kil "Yeah, sure. Photographer, model, doctor... you're a real triple threat."
            scene w2_1010 with dissolve
            mc "Don't you forget it."
            scene black with fade
            "..."

            if toughness>=21:
                mc "Open up."
                ver "Just get the shot."
            else:
                mc "You alright with this?"
                ver "Yeah, it's fine just get the shot."

            scene w2_1011 with dissolve
            ver "Mmmfggh..."
            "I stuck my finger into Veronica's mouth with one hand, while the other roughly groped at a breast."

            if Veronica_Horniness >= 4:
                scene w2_1012 with dissolve
                ver "Mmmh, oha!"
                "The idea was to make Veronica look like she was snared and in distress, but an ever-so-slight moan left me with a different impression."

                if toughness>=28:
                    mct "(Is this slut enjoying this?)"
                else:
                    mct "(Is she enjoying this?)"

                "Do I dare to find out...?"
                hide screen textbox2 with dissolve

                menu:
                    "Go a little beyond what's needed for the shoot."(chg=["veronica_passion_up"]):
                        $ Veronica_Horniness += 1
                        $ VeronicaPentUp = True

                        show screen textbox2 with dissolve
                        "Yes, I was so very, very curious."
                        scene w2_1013 with dissolve
                        ver "G-ghu..!"
                        "Setting aside any sense of propriety, I pushed my fingers deeper into Veronica's mouth and used my other hand to tweak her stiffening buds through the fabric of her lingerie."
                        scene w2_1041 with dissolve
                        ver "*Cough* *Cough* --!" with dissolve
                        "The tips of my two fingers brushed the back of her throat, effectively deep throating them and causing her to sputter in surprise."
                        scene w2_1042 with hpunch
                        ver "Mmmh...!"
                        scene w2_1014 with dissolve
                        mc "*Whisper* You're supposed to be acting distressed. What's the matter?"
                        ver "Eurh-beeing-twoo-"
                        scene w2_1015 with dissolve
                        ver "Ack-!"

                        if toughness>=23:
                            mct "(That was rhetorical.)"
                        else:
                            mc "You must be pent up."

                        "I don't know what had possessed me all of a sudden, but I pushed my luck, prying the Amazon's soft pink tongue from her mouth and holding it between my fingers."
                        hide screen textbox2 with dissolve
                        scene w2VeroGrope with dissolve
                        mc "You getting some good shots here?"
                        kat "You're supposed to be posing, not molesting the model."
                        kil "We're getting some {b}damn{/b} good shots here."
                        "Veronica was totally blanking, just freely letting my hands dig into the pale speckled flesh of her breasts with nary a peep to the contrary. It felt totally unlike her."
                        scene w2_1033 with dissolve
                        show screen textbox2 with dissolve
                        "So much so that I involuntarily found myself softly stroking her head and massaging her scalp as if to comfort her."
                        "Meanwhile, my other hand was up to something much more naughty. Her nipples were as hard as diamonds, completely engorged and just begging to be played with."
                        "So that's what my right hand did, lackadaisically brushing its fingertips against the stoney protuberance, flicking and teasing..."
                        scene w2_1043 with dissolve
                        ver "Ah...♥"
                        kil "I think I got enough though."
                        kil "Did I already remark that you seem to be really getting into this?"
                        scene w2_1034 with dissolve
                        mc "Thanks for doing that, Veronica. It was all for the shoot."
                        scene w2_1035 with dissolve

                        if toughness>=21:
                            scene w2_1036 with dissolve
                            ver "The h-hell it was, you perv."
                            mc "Hey, you seemed to enjoy it."
                        else:
                            scene w2_1035 with dissolve
                            ver "The h-hell it was, you perv."
                            mc "Hehe, no honest! Really!"

                        scene black with fade
                        "After taking a few moments to collect herself, Veronica fixed her \"clothes\" and scrambled off the backdrop."
                        kil "That leaves Felicia for next."
                    "No. Don't risk it.":


                        scene w2_1037 with dissolve
                        show screen textbox2 with dissolve
                        mct "(Better not push it.)"
                        mc "You got the shot?"
                        kil "Yep, I think we're good."
                        kil "Did I already remark that you seem to be really getting into this?"
                        scene w2_1038 with dissolve
                        mc "Thanks for doing that, Veronica. It was all for the shoot."
                        ver "Not the worst thing you could've asked me to do."
                        kil "That leaves Felicia for next."
            else:



                scene w2_1037 with dissolve
                show screen textbox2 with dissolve
                "Veronica did her best to give the camera a distressed, uncomfortable look. Not all of it was acting I'm sure."
                "Even if it was just pretend, it felt nice having Veronica in my grasp like this."
                kil "Alright. I got the shot."
                scene w2_1038 with dissolve
                mc "Thanks for doing that, Veronica."
                ver "Not the worst thing you could've asked me to do."
                kil "Did I already remark that you seem to be really getting into this?"
                scene w2_1039 with dissolve
                mc "We'll move onto Felicia now."

    scene w2_1044 with circlewipe
    $ renpy.music.set_volume(1, 2, channel = "music")
    "Felicia was a natural, right out of the gate."
    play sound "sound effects/camera-phone-shutter.wav"
    with flash
    "Instead of waiting for direction, she quickly switched from pose to pose."
    scene w2_1045 with dissolve
    play sound "sound effects/camera-phone-shutter.wav"
    with flash
    "No doubt from her experience helping out at Mina's modeling agency."
    mct "(Damn, she looked great.)"
    scene w2_1046 with dissolve
    play sound "sound effects/camera-phone-shutter.wav"
    with flash
    "*Snap*"
    scene w2_1047 with dissolve
    play sound "sound effects/camera-phone-shutter.wav"
    with flash
    "*Snap*"
    fel "It'd be a shame if you only got one side of me."
    scene w2_1048 with dissolve
    play sound "sound effects/camera-phone-shutter.wav"
    with flash
    "*Snap*"

    if w1FelAss == True:
        fel "I think I remember you saying you were an ass man, [mcf]."
    else:
        fel "I always thought I could've been in a rap video."

    scene w2_1049 with fade
    "After a couple minutes of continuous posing, Felicia was on the floor, looking hot and flustered for the camera."
    "Hand placed between her legs. Not masturbating, but it certainly looked like she was barely containing herself."
    kat "Ha! The slut got herself worked up just from being photographed."
    scene w2_1050 with dissolve
    "It occurred to me that as good as Felicia's portion of the shoot was, it lacked the same thematic punch the other two had. This week was about shame. Rosalind was dressed up like an animal and Veronica was wearing something frilly and totally out of character, but she was the odd woman out."
    "How do you shame an audacious woman like Felicia?"
    scene w2_1051 with dissolve
    kat "I have one last picture I want you boys to get of our star. One that'll surely be a favorite. I'll need to borrow your penis though, [mcf]."
    scene w2_1052 with dissolve
    mc "...{b}of course{/b}, you will."
    scene black with fade
    "It sounded like she was about to answer my question."
    fel "Where did you get that photo...?"
    kat "It wasn't hard, even if you and Elias don't have a social media presence."

    scene w2_1053 with dissolve
    if kat_polite == True:
        "Mrs. Pulman's \"choice shot\" was a twisted one. She had pulled up a photograph of Felicia and her husband on her phone and was now having the conspicuously silent slut wife hold it up like a placard in a mugshot."
    else:
        "Kathleen's \"choice shot\" was a twisted one. She had pulled up a photograph of Felicia and her husband on her phone and was now having the conspicuously silent slut wife hold it up like a placard in a mugshot."

    kat "You're a surprisingly private person, Mrs. Ford."
    fel "..."
    "I guess it was one thing to talk about it on stage, but holding up a photo of her marital life was another thing altogether."
    kat "Now open your whore mouth and stick out your tongue, pig."
    fel "Mmh..."
    kat "Did you not hear me...?"
    scene w2_1054 with dissolve
    fel "Aaaah..."
    "Felicia did as the old woman commanded, adding a not-so-zealous flourish to it."
    scene w2_1055 with dissolve
    kil "Got the shot. We good?"
    stop music fadeout 3.0
    scene w2_1056 with dissolve
    kat "Almost, I wanted to get one last group photo."
    scene black with fade
    "......"
    "..."
    scene w2_1057 with dissolve
    kat "Yep, just like that. Hold out your hands, Miss Lynch."
    play sound "sound effects/camera-phone-shutter.wav"
    with flash
    kat "Perfect. Between this and what's coming later this week, our patrons are going to {b}treasure{/b} this set."
    rose "What's coming later?"
    kat "I already told you. That'll be a surprise."
    scene w2_1058 with dissolve
    kat "We're done for now. You two can go."
    scene w2_1059 with dissolve
    kat "Take that camera with you, [mcf]. You'll need it for when you're in the \"field\" later."
    scene w2_1060 with dissolve
    "Naturally, whatever she has in store for the Carnations I'll be dragged into."
    scene w2_1061 with dissolve
    mc "That's all? You don't need help cleaning up any of this?"
    scene w2_1058 with dissolve
    kat "That's okay. You boys must be hungry. Go grab lunch or something. I'll see you later."
    $ renpy.end_replay()
    scene w2_1062 with dissolve
    if not persistent.w2ShamePhotoshootGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w2ShamePhotoshootGallery = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    "Glad to be dismissed, Ian and I parted and went separate ways."
    scene club-fr-day with blinds
    "He had some errands to run, which thankfully he didn't try to pull me into."
    mct "(I guess my day's wide open. What should I do with it...?)"
    $ renpy.music.set_volume(.4, 0, channel = "ambient")
    play ambient "sound effects/city-night.wav"

    if minaFlag == True:
        mct "(Ah, yeah! Didn't Mina mention something about helping her rehearse for her TV gig sometime today?)"
        "I'll give her a call."
        jump w2MinaLineReadingStart
    else:

        mct "(I guess I'll just do jack shit.)"
        "First, I made sure to spend a nominal amount of effort trying to think of something more productive to do... just so I could at least say I tried before arriving at my current lazy course."
        scene black with fade
        stop ambient fadeout 3.0
        "......"
        "..."
        jump w2June08Evening


label w2MinaLineReadingStart:

    scene club-fr-day blur with dissolve
    show mina-call with dissolve
    play sound "sound effects/ringing-outbound.mp3"
    "{i}*Ring... ring...*{/i}"
    "{i}*Ring... ring... ring...*{/i}"
    stop sound
    mina "Heeeeey! Heh, I was just thinking about you!"
    smv "Who are you talking to?"
    "A soft-spoken question came from a tenor like voice on the other line."
    mina "{size=-10}A friend.{/size=-10}"
    smv "It's not your asshole--"
    mina "Hey! Only I can... {size=-10} call him an asshole!{/size=-10}"
    mina "Sorry about that, [mcf]."
    mc "No problem. I hope I'm not calling at a bad time."
    mina "Nope! Just sitting at home at the moment."
    mc "Well, I'm glad I'm not interrupting anything then. I was just leaving work and remembered you asked me to help you rehearse today."
    mina "Oooh, yeah! You actually remembered that?"
    mc "I didn't get that bombed last night."
    mina "Even still, I'm happy you remembered. Since I'm the one imposing, what time would work best for you?"
    mc "Uh, well... how about now?"
    "It sounded like she had company so I was a bit hesitant in picking that time, but I decided I'd leave the ball in her court."
    mina "Now works great! Where do you want to meet?"
    mc "Is your place fine? I bet I'm closer to you than you are to my place."
    mina "Sure, let me give you the address...!"
    hide mina-call with dissolve
    scene black with fade
    $ renpy.music.set_volume(.2, 2, channel = "ambient")
    "......"
    "..."
    scene w2_1063 with blinds
    "My hunch was right. Mina lived reasonably close to the city center, which meant it was a closer trek from the outskirts where the Carnation Club sat."
    mct "(Hmm... do I just let myself in? There's the buzzer.)"
    mct "(Ah, crap she didn't tell me her apartment number. I guess I should give her another call...)"
    scene w2_1064 with dissolve
    "As if on cue, just as I was about to reach for my phone, Mina came out her apartment building with a blonde boy in tow."
    scene w2_1065 with dissolve
    play music "music/happy-boy-end-theme.ogg"
    mc "Hey! Just in time, I guess!"
    mina "Hehe, looks like it!"
    scene w2_1066 with dissolve
    "Mina and company made the short jaunt past the stoop and down the apartment building's stairs until we came face-to-face."
    scene w2_1067 with dissolve
    mc "Who's this?"
    scene w2_1068 with dissolve
    "The boy stood sheepishly to Mina's side. Not quite hiding behind her, but he was clearly feeling pretty timid."
    "I immediately noticed the bruising and swelling underneath his right eye."
    hide screen textbox2 with dissolve

    menu:
        "Warmly introduce yourself to the boy."(chg=["mina_up"]):
            $ Mina_Affection +=1

            scene w2_1069 with dissolve
            show screen textbox2 with dissolve
            mc "I'm [mcf]. Nice to meet you. I'm a friend of Mina's."
            "The boy sized me up in a familiar, almost nostalgic way. Before..."
            scene w2_1070 with dissolve
            sora "I'm Sora. I'm Mina's brother."
            scene w2_1074 with dissolve
            mina "My little brother! Isn't he cute?"
        "Make a joke in an attempt to put the boy at ease.":


            scene w2_1071 with dissolve
            show screen textbox2 with dissolve
            mc "I should see the other guy, right?"
            scene w2_1072 with dissolve
            smv "..."
            scene w2_1073 with dissolve
            mina "Aw, c'mon Sora. Don't be shy. He's a friend. Let me introduce you to [mcf]."
            sora "Hello..."
            scene w2_1074 with dissolve
            mina "[mcf], this is my little brother Sora. Isn't he cute?"


    scene w2_1075 with dissolve
    mct "(Mina and Sora, eh?)"
    "I agreed with her sisterly assessment, but I treated the question rhetorically to avoid further embarrassing him."
    mc "I can see the family resemblance."
    scene w2_1076 with dissolve
    mina "Hehe!"
    sora "Yeah, right..."
    scene w2_1075 with dissolve
    mc "I'm not interrupting family time, am I?"
    scene w2_1077 with dissolve
    mina "No. Sora was paying his lonely big sis a visit, but he has to sadly get going to violin practice."
    scene w2_1075 with dissolve
    mc "Oh? I'm not very good at it, but I know a little bit about playing a musical instrument."
    scene w2_1078 with dissolve
    sora "I'm not that good either. It's stupid, Mom just makes me take lessons... not like I'm going to use it for anything."
    mc "Hmm..."
    $ renpy.music.set_volume(.2, 2, channel = "music")
    scene w2_1079 with pixellate
    mc "This is dumb! Why do I have to learn this? I'm not ever going to use it."
    scene w2_1080 with dissolve
    vic "Not everything needs to be fun or immediately useful, [mcf]. Learning piano will help teach you a number of things that are important in life."
    scene w2_1079 with dissolve
    mc "Like what?"
    scene w2_1080 with dissolve
    vic "Well... it'll improve your concentration. That's one."
    scene w2_1081 with dissolve
    vic "It'll also teach you discipline and improve your listening skills, both of which you're in dire need of if the last teacher-parent conference is anything to go by."
    scene w2_1079 with dissolve
    mc "Mmmh... but it's boring!"
    scene w2_1082 with pixellate
    $ renpy.music.set_volume(1, 2, channel = "music")
    mc "Hmm... stick with it. Not everything is immediately useful, but you'll be glad you did."
    "Sora looked at me dubiously, in the way only a teenager can."
    scene w2_1083 with dissolve
    mc "Sorry, didn't mean to lecture you."
    scene w2_1084 with dissolve
    sora "No, it's cool... I'll take your word for it."
    scene w2_1085 with dissolve
    mina "You need to get going, Sora. Have a safe trip."
    sora "Right, love ya sis."
    mina "I love you too."
    scene w2_1086 with dissolve
    sora "It was nice meeting you, [mcf]."
    mc "You too, Sora."
    scene w2_1087 with dissolve
    "..."
    scene w2_1088 with dissolve
    mc "He seems like a nice kid."
    scene w2_1089 with hpunch
    mina "You seem like a good judge of character."
    "Mina playfully punched my shoulder and flashed a proud grin."
    scene w2_1090 with dissolve
    mina "He's just ... going through a rough patch right now. More than I did at that age."
    scene w2_1091 with dissolve
    mc "Does that have anything to do with that black eye"
    scene w2_1092 with dissolve
    mina "He wouldn't tell me where he got it, but from what I can piece together, some kids started giving him a lot of crap this year."
    mina "Mom tells him to just focus on school and ignore them and they'll go away."
    scene w2_1093 with dissolve
    mc "That's... not how that works."
    scene w2_1094 with dissolve
    mina "Yeah, even I could tell you that's awful advice. She lives in another world."
    scene w2_1095 with dissolve
    mc "You should get Ian to talk to him. He might have some insight he could pass along."
    scene w2_1096 with dissolve
    mina "Maybe..."
    scene w2_1097 with dissolve
    mina "Well, you wanna come in?"
    scene black with fade
    stop music fadeout 2.0
    stop ambient fadeout 1.0
    $ renpy.music.set_volume(1, 1, channel = "ambient")
    "......"
    "..."
    scene w2_1098 with w20
    play music "music/inner-light.ogg"
    "After a quick tour of her apartment, Mina led me to her living space."
    mc "You have a nice place."
    mina "Thanks, but my parents foot the bill. Not really anything to be proud of."
    mc "They may pay the rent, but all the warmth is your doing, right? Just take the compliment."
    scene w2_1099 with dissolve
    mina "Sorry, you're right. I just wish I could be more independent."
    scene w2_1100 with dissolve
    mc "This TV job is a step toward that, right?"
    scene w2_1101 with dissolve
    mina "Um hum, hopefully!"
    scene w2_1102 with dissolve
    mct "(This place looks just about how I imagined it would.)"
    scene w2_1103 with dissolve
    "It had a lived-in touch you'd expect from any person's bedroom, but there was a particular blend of cute and stylish that was distinctly Mina."
    scene w2_1104 with dissolve
    mina "Hey! You hungry? It's way past lunch and I'm starving."
    mc "I could go for something."
    mina "Great! You like sushi?"
    mc "Sushi would be great. I don't usually get the chance to eat it."
    scene w2_1105 with dissolve
    mina "Sit tight then, I've got a menu in the kitchen. I'll put in an order for delivery."
    play sound "sound effects/door-open.wav"
    scene w2_1106 with dissolve
    mina "Oh, and I'm paying for it. As thanks for you taking time out of your day. No arguments!"
    "She was artfully already out of the door when she added that last part. Not that I was complaining. Being fed on someone else's dime was a college student's pleasure."
    mct "(I'm not hurting for cash anymore though, I guess.)"
    scene w2_1107 with dissolve
    "With Mina momentarily out of the room and nothing else to do, I decided to take a closer look at the wall of photos that were definitely the centerpiece of her bedroom."
    scene w2_1108 with fade
    "It was lined with various memories of things that I'm certain were important to Mina."
    "Should I inspect any of these?"
    jump w2MinaPhotoWall

image BotHHover = "gui/screens/imagemaps/w2MinaPhotoWall_fix.png"
screen BotHFix(who):
    if who == "BotHHover":
        add "BotHHover"

screen w2MinaPhotoWall:

    imagemap:

        imagebutton auto "gui/screens/imagebuttons/exitphotowall_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w2MinaLineReadingContinue")] hovered [ Play ("hover_extra", "sound effects/click.wav") ] xpos 0.93



        idle "gui/screens/imagemaps/w2MinaPhotoWall_idle.png"
        hover "gui/screens/imagemaps/w2MinaPhotoWall_hover.png"
        ground "gui/screens/imagemaps/w2MinaPhotoWall_ground.png"

        hotspot (7, 0, 628, 834) action Jump("w2MinaFashionShow")
        hotspot (1078, 153, 411, 575) action Jump("w2MinaFamilyPhoto")
        hotspot (652, 440, 409, 500) action Jump("w2MinaGlamourMagazine")
        hotspot (1080, 720, 174, 214) action Jump("w2MinaMinaDad")
        hotspot (1248, 727, 174, 207) action Jump("w2MinaKillian")
        hotspot (1501, 416, 362, 279) clicked Jump("w2MinaBridesOfTheHunt") hovered ShowTransient("BotHFix",who="BotHHover") unhovered Hide ("BotHFix")
        hotspot (1485, 209, 148, 191) action Jump("w2MinaArchery")
        hotspot (1641, 175, 211, 235) action Jump("w2ExJuliet")


label w2MinaPhotoWall:
    show black
    hide mina-room-wall blur
    hide mina-family
    hide mina-archery
    hide mina-both
    hide mina-dad
    hide mina-juliet
    hide mina-killian
    hide mina-magazine
    hide w2_1108
    call screen w2MinaPhotoWall with dissolve

label w2MinaFashionShow:

    show w2_1108

    if w2MinaFashionShow == False:
        $ w2MinaFashionShow = True
        "It's a poster for a fashion show. Could be solely decorative or perhaps even a souvenir from something Mina attended."
    else:
        mct "(To be honest, I don't really get fashion. Not that I can't appreciate a good-looking pair of boots or an attractive shirt, but the artistic side of it is lost on me.)"

    jump w2MinaPhotoWall

label w2MinaFamilyPhoto:

    show mina-room-wall blur
    show mina-family with dissolve:
        ypos 0.05

    if w2MinaFamilyPhoto == False:
        $ w2MinaFamilyPhoto = True
        "It was a recent-looking photo of Mina, her brother, and a remarkably beautiful woman who I presumed to be their mother."
        "The photo reminded me about Mina's comment last night about having a \"revolving door of stepdads\", but they looked reasonably happy and not in a smile-for-the-camera sort of way."
        "There was a genuine warmth found in the photo that reinforced what I already firmly believed. Life doesn't have to be picture perfect to have happiness."
    else:

        mct "(Then again, that's a wild assumption to make for a single photo.)"

    jump w2MinaPhotoWall

label w2MinaGlamourMagazine:

    show mina-room-wall blur
    show mina-magazine with dissolve:
        ypos 0.05

    if w2MinaGlamourMagazine == False:
        $ w2MinaGlamourMagazine = True
        "It's a magazine cover with Mina on it from earlier this year. Her hair is down and she's wearing a revealing set of white netted lingerie."
        "This must have been an important gig to her if she memorialized it on her wall like this."
    else:
        mct "(If I looked that good, I'd probably have a poster of me on the wall too.)"

    jump w2MinaPhotoWall

label w2MinaMinaDad:

    show mina-room-wall blur
    show mina-dad with dissolve:
        ypos 0.05

    if w2MinaMinaDad == False:
        $ w2MinaMinaDad = True
        "It's a picture of a blonde man holding an infant. While tired, he also looks incredibly proud and happy. He clearly loves being a father."
        "Maybe baby Mina and her dad?"
    else:

        mct "(Whoever it is, that is a {b}fabulous{/b} head of hair.)"

    jump w2MinaPhotoWall

label w2MinaKillian:

    show mina-room-wall blur
    show mina-killian with dissolve:
        ypos 0.05

    if w2MinaKillian == False:
        $ w2MinaKillian = True
        "It's a picture of Mina and Ian, shoulder to shoulder. It's difficult to make out where they are, but it looks like they're on a date."
        "They look happy. I know they met during a photoshoot, but maybe I'll ask her more about it sometime. "
    else:
        mct "(I can't help but wonder what drew her to Ian in the first place and why she's stuck around so long.)"

    jump w2MinaPhotoWall



label w2MinaBridesOfTheHunt:

    show mina-room-wall blur
    show mina-both with dissolve:
        ypos 0.03

    if w2MinaBridesOfTheHunt == False:
        $ w2MinaBridesOfTheHunt = True
        "It's a poster for the fantasy television drama \"Brides of the Hunt\", displayed prominently on the wall. She must really be a fan of that show."

        if feliciaFlag == False:
            "I actually just caught that one recently too."
        else:
            "Maybe I'll have to check it out some time."
    else:

        mct "(These foreign dramas have really blown up in popularity.)"


    jump w2MinaPhotoWall

label w2MinaArchery:

    show mina-room-wall blur
    show mina-archery with dissolve:
        ypos 0.05

    if w2MinaArchery == False:
        $ w2MinaArchery = True
        "It's a surprising photograph of Mina and two other girls, each of them brandishing a bow."
        "They look happy, like they had just done well at an event."
    else:

        mct "(It looks like an important memory for Mina.)"

    jump w2MinaPhotoWall



label w2ExJuliet:

    show mina-room-wall blur
    show mina-juliet with dissolve:
        ypos 0.05

    if w2ExJuliet == False:
        $ w2ExJuliet = True
        "It's a photograph of Mina in what appears to be a stage play. A woman is cradling Mina in her arms, looking despondent."
        "If I had to hazard a guess, going by the costumes and from what's going on in the picture, I'd say this is an all-girls production of Romeo and Juliet."
        "It looked really high quality. Either this must have been a fairly large show or their costume designer was at least big league."
    else:
        mct "(I wonder what it feels like to be in the spot light like that? I mean, I only have my recent experiences to go off of, but...)"
        mct "(I imagine performing a piece of literature probably hits a little differently than getting your dick sucked for the viewing pleasure of a room full of perverts.)"

    jump w2MinaPhotoWall


label w2MinaLineReadingContinue:

    scene w2_1109 with fade
    mct "(Hmm...)"
    play sound "sound effects/door-openclose.wav"
    mina "I just ordered us a variety platter. That's cool, right?"
    scene w2_1110 with dissolve
    mc "Works for me."
    scene w2_1111 with dissolve
    mina "What were you doing?"
    scene w2_1112 with dissolve
    mc "Just taking a look at some of the stuff on your wall. You keep a lot of memories."
    scene w2_1113 with dissolve
    mina "Oh yeah... hope you don't think I'm a smidge narcissistic."
    scene w2_1114 with dissolve
    mc "Why would I ever think that?"
    scene w2_1115 with dissolve
    mina "I mean, do you know many people who keep a blown up, half-naked photo of themselves on their bedroom wall?"
    scene w2_1116 with dissolve
    mc "I don't know. Did Ian ever take his down?"
    scene w2_1117 with dissolve
    mina "*Snort* Ha! Funny!"
    scene w2_1118 with dissolve
    mc "No, but for real, I'm sure you have a good reason besides vanity for every single one of these."
    scene w2_1108 with fade
    "For example..."
    hide screen textbox2 with dissolve

    menu w2MinaWallMenu:
        "Point out the family photo." if w2MinaFamilyPhotoQ == False and w2MinaConversate == 0 or w2MinaFamilyPhotoQ == False and w2MinaConversate == 2:
            $ w2MinaFamilyPhotoQ = True
            $ w2MinaConversate += 1

            scene w2_1119 with dissolve
            show screen textbox2 with dissolve
            if w2MinaConversate == 0:
                mc "For example, it isn't weird to have a family photo. That's your mom next to you and your brother?"
            else:
                mc "That's your mom next to you and your brother?"

            scene w2_1120 with dissolve
            mina "It is indeed. That is Mrs. Eiko Umeda HYPHEN Wright, formerly Mrs. Eiko Scott, and even more formerly Mrs. Eiko Adams. First of her names."
            mina "She's very beautiful, isn't she?"
            scene w2_1121 with dissolve
            mc "She is."
            scene w2_1122 with dissolve
            mina "Hehe~ people tell me I get my looks from her, so thanks!"
            scene w2_1123 with dissolve
            mc "Smidge narcissistic were your words, huh?"
            scene w2_1124 with dissolve
            mina "Oof. Using my words against me... that's mean! You play dirty, [mcf]."
            scene w2_1125 with dissolve
            "Mina and I shared a dumb look between us before she moved the conversation along."
            scene w2_1120 with dissolve
            mina "She's a great woman. We may butt heads sometimes over what's \"traditional\", but I love her dearly. She's got a generous heart."
            mina "Maybe a little too generous when it comes to the men, but hey..."
            scene w2_1121 with dissolve
            mc "Was this taken on vacation?"
            scene w2_1127 with dissolve
            mina "Yep! I'd always wanted to go to Italy and she surprised me last summer out of the blue. It took some convincing to get Sora to come along, but I wouldn't take no for an answer."
            mina "That photo was taken in Venice. No roads or cars, just canals... isn't that amazing? A floating city. It's like something out of a story."
            scene w2_1126 with dissolve
            mc "That does sound peaceful."
            scene w2_1127 with dissolve
            mina "Yep, I had a great time. We all did, even if my brother won't admit it. You ever been to a foreign country?"
            scene w2_1126 with dissolve
            mc "No. I've barely been out of the state. It feels like a small world sometimes."
            scene w2_1127 with dissolve
            mina "You have any place you'd like to visit if you got the chance?"
            scene w2_1126 with dissolve
            mc "I don't know, I always thought that..."
            hide screen textbox2 with dissolve

            menu:
                "You would like to visit Iceland one day.":
                    show screen textbox2 with dissolve
                    mc "I always thought Iceland sounded beautiful. Volcanoes, geysers, hot springs... not sure about the fermented shark, but it sounds like a nice place to visit."
                    scene w2_1128 with dissolve
                    mina "Oooh, yeah! It really does. Hot springs, that sounds SO nice right now..."
                "You would like to visit Australia one day":

                    show screen textbox2 with dissolve
                    mc "I always thought Australia would be neat to visit. See the Great Barrier Reef, see the rugged outback of the western parts, try the barbecue..."
                    scene w2_1129 with dissolve
                    mina "Mmmh... barbecue. Don't mention food to me, I'm hungry!"
                "You would like to visit Japan one day.":

                    show screen textbox2 with dissolve
                    mc "I always thought it'd be cool to visit Japan. See Tokyo and the sights, drive the country side, stay at an old inn and enjoy a hot spring."
                    scene w2_1129 with dissolve
                    mina "I always wanted to go there too. That's where a lot of my favorite dramas are filmed. Heh, I guess that's a pretty dorky reason..."
                    scene w2_1126 with dissolve
                    mc "It's as good a reason as any other."
                "Venice sounded pretty nice.":

                    show screen textbox2 with dissolve
                    mc "You made Venice sound pretty nice. Seriously, no cars? That's sounds like heaven to someone who's lived in a city suburb most his life."
                    scene w2_1130 with dissolve
                    mina "No fair. You should pick your own answer."
                    scene w2_1131 with dissolve
                    mc "Nope, I still pick Venice. Sorry."

            scene w2_1132 with dissolve
            "A small moment of silence passed between us, before Mina deftly maneuvered the conversation back on topic."
            scene w2_1133 with dissolve
            mina "Do you see yourself traveling much when you get out of school?"
            scene w2_1134 with dissolve
            mc "I haven't really thought about it. One thing at a time. That's usually how my mind works."
            mc "Get into medical school. Focus on my studies. Become a doctor."
            scene w2_1133 with dissolve
            mina "You're a pretty serious person, [mcf]."
            scene w2_1134 with dissolve
            mc "Sorry."
            scene w2_1133 with dissolve
            mina "No, I like that about you. It's a good quality in a man."
            scene w2_1135 with dissolve
            "......"
            "..."
            scene w2_1136 with dissolve
            mc "Aw, I'm a man? Thanks!"
            scene w2_1137 with hpunch
            mina "Shut up!"
            scene w2_1126 with dissolve
            mc "Anyway, it sounds like you had a nice trip with your family. Big memory, big photo."

            if w2MinaConversate == 0:
                mc "Nothing narcistic about that."

            scene w2_1128 with dissolve
            mina "Yeah, I really did. It was one of the best trips in my life."

            if w2MinaConversate == 3:
                pass
            else:
                scene w2_1126 with dissolve
                mc "I'd like to hear about another one of these photos."
                scene w2_1127 with dissolve
                mina "Sure. It's fun to reminisce. Which one do you want to hear about?"
                hide screen textbox2 with dissolve
                scene w2_1108 with fade
                jump w2MinaWallMenu

        "Point out the photo of the man with the baby." if w2MinaDadQ == False and w2MinaConversate == 0 or w2MinaDadQ == False and w2MinaConversate == 2:
            $ w2MinaDadQ = True
            $ w2MinaConversate += 1

            scene w2_1138 with dissolve
            show screen textbox2 with dissolve
            if w2MinaConversate == 0:
                mc "For example, who's that man holding a baby?"
            else:
                mc "Who's that man holding a baby?"

            scene w2_1139 with dissolve
            mina "That's my dad and little brother."
            scene w2_1140 with dissolve
            mc "He looks pretty stoked to be a dad."
            scene w2_1139 with dissolve
            mina "He's great. He and my mom split when I was six and even though he lives in another city now due to work, he still calls me two times a week."
            mina "I like to look at that photo when we talk and pretend that he's here."
            scene w2_1140 with dissolve
            mc "He sounds like a good dad. What does he do?"
            scene w2_1141 with dissolve
            mina "He's an inventor or well, er... his official title is something fancy, but that's the word he always used and that's how I always thought of him. How about your dad?"
            scene w2_1140 with dissolve
            mc "He was a social worker for the state. My mom tells me he also helped grow this charity that supports the Morehead Hill's library. She speaks very fondly about that."
            scene w2_1142 with dissolve
            mina "Was...? I'm sorry."
            scene w2_1143 with dissolve
            mc "It's alright. He passed when I was little."
            scene w2_1144 with dissolve
            mina "..."
            scene w2_1145 with dissolve
            mc "It looks like you get your head of hair from your dad, huh?"
            scene w2_1139 with dissolve
            mina "Yep, my brother and I both."
            scene w2_1146 with dissolve
            mc "Uh, this might be weird, but would you mind...?"
            scene w2_1147 with dissolve
            mina "Go ahead! I don't know what it is about pigtails, but you get used to people wanting to touch them."
            scene w2_1148 with dissolve
            "Taking the proffered pigtail in my hand, I lightly ran my finger tips over the flaxen strands."
            "It was incredibly soft and had a healthy, almost glow-like shine to it. She took good care of her hair, as befitting her profession, and most likely prided herself in it."
            scene w2_1149 with dissolve
            mina "You like blondes, [mcf]?"
            scene w2_1150 with dissolve
            "Mina looked at me in a teasing way, a few steps removed from her usual geniality."
            hide screen textbox2 with dissolve

            menu:
                "Admit you do like blonde hair.":

                    scene w2_1151 with dissolve
                    show screen textbox2 with dissolve
                    mc "I guess I do."
                    scene w2_1152 with dissolve
                    mina "Ha! I knew it!"

                    if feliciaFlag == True:
                        scene w2_1153 with dissolve
                        mina "Is that what's got you taken with Felicia? Hmmm?"
                        scene w2_1154 with dissolve
                        mc "Come on, we just had dinner one time. I'm not taken with her."
                        mina "Really...?"
                        scene w2_1155 with dissolve
                        mc "Don't worry, I remember your warning: She's married, be careful."
                        mina "Heh, that's good!"
                        scene w2_1126 with dissolve
                        "For just a moment, we shared in a comfortable silence punctuated by Mina's warm smile."
                "Tease her back. You like HER blonde hair.":


                    show screen textbox2 with dissolve
                    "Summoning my most dead serious expression, I caught Mina's eyes with mine and peered into them unfalteringly..."
                    scene w2_1156 with dissolve
                    mc "I like YOUR blonde hair. It's very pretty."
                    "Mina's eyes briefly lit up for a moment, before..."

                    if perk_socialButterfly == True or perk_socialChameleon == True:
                        scene w2_1157 with dissolve
                        mina "Ugh, saying it so convincingly as a joke is cheating!"
                        mc "You started it."
                        scene w2_1158 with dissolve
                        mina "You jerk."
                        "She did her best to hide her grin, but I saw it."
                        scene w2_1126 with dissolve
                        "For just a moment, we shared in a comfortable silence punctuated by Mina's warm smile."
                    else:

                        scene w2_1159 with dissolve
                        mina "That's... Ppft...! that's... Pfft...!"
                        "She did her best not to burst out laughing, but failed."
                        scene w2_1160 with dissolve
                        mina "Hahaha!"
                        mc "What?"
                        mina "You just... pfft... you just said it so seriously! With such a straight face! It's funny!"
                        scene w2_1161 with dissolve
                        mc "Pfft...!"
                        "Mina's mirth proved contagious and we shared in the laughter."
                        mc "That was my best! Don't laugh!"
                        scene w2_1126 with dissolve
                        "The laughter eventually died down and Mina and I shared a comfortable silence, punctuated by Mina's warm smile."
                "Tell her you don't really have a preference.":



                    scene w2_1151 with dissolve
                    show screen textbox2 with dissolve
                    mc "Eh, I don't really have a preference. Pretty girls come in all different packages."
                    scene w2_1162 with dissolve
                    mina "Blah! You're no fun. I was teasing you and you gave me a serious answer."
                    scene w2_1163 with dissolve
                    mc "Heh, sorry!"
                    scene w2_1126 with dissolve
                    "For just a moment, we shared in a comfortable silence punctuated by Mina's warm smile."

            if w2MinaConversate == 3:
                pass
            else:
                mc "Would you mind telling me about another one of these photos, Mina?"
                scene w2_1127 with dissolve
                mina "Sure. It's fun to reminisce. Which one do you want to hear about?"
                hide screen textbox2 with dissolve
                scene w2_1108 with fade
                jump w2MinaWallMenu


        "Ask Mina to tell you about the photo of her with a bow." if w2MinaArcheryQ == False and w2MinaConversate == 1 or w2MinaArcheryQ == False and w2MinaConversate == 2:
            $ w2MinaArcheryQ = True
            $ w2MinaConversate += 1

            scene w2_1164 with dissolve
            show screen textbox2 with dissolve
            mc "Do you actually know how to use that thing?"
            "I pointed at the photo of Mina and the two other girls, each sporting some serious looking compound bows."
            scene w2_1165 with dissolve
            mina "I would hope so. I was captain of my high school archery team."
            scene w2_1166 with dissolve
            mc "I didn't know schools around here had those."
            scene w2_1165 with dissolve
            mina "There's a couple, but it was more of a club than a sports team. We were student funded and the chance to compete didn't come up often."
            scene w2_1166 with dissolve
            mc "So... hypothetically, if you decided to kill me, how far away would I have to be before I had a fighting chance at escape?"
            scene w2_1167 with dissolve
            mina "I'm accurate up to 50 yards."
            scene w2_1168 with dissolve
            "Mina puffed up her chest in an exaggerated fashion. I'm guessing that was a respectable number."
            scene w2_1169 with dissolve
            mc "So, what's the story with that photo in particular then?"
            scene w2_1165 with dissolve
            mina "You're looking at half of the archery team there. The ones whose parents allowed them to travel out of state and compete regionally."
            mina "We had to provide our own transport, so the girls and I carpooled to the event. Just the three of us, without adult supervision."
            scene w2_1166 with dissolve
            mc "When was this?"
            scene w2_1165 with dissolve
            mina "Our senior year of high school."
            mina "Those girls are a hoot, I had such a blast that weekend. We don't talk as much as we should anymore, but I guess that's what happens after high school."
            scene w2_1166 with dissolve
            mc "Yeah, you go in different directions."
            scene w2_1170 with dissolve
            mina "Not you and Ian though?"
            scene w2_1166 with dissolve
            mc "Actually... we did? I mean, we kept in touch, mainly from the effort on his part, but until he got me a job at his Uncle's..."
            "I dug deep to remember our previous conversation about Dr. Chuck and what she thought it was."
            mc "...jazz bar, I'd say we were on the outs."
            scene w2_1170 with dissolve
            mina "The way he always talked about you, I figured you guys still carried on like schoolboys. You came up, like a lot. All his anecdotes involved you."
            scene w2_1171 with dissolve
            mc "Yeah, that's pretty weird, huh?"
            scene w2_1172 with dissolve
            mina "Hehe, sometimes I joked that he was in love with you, but now I think he just didn't have many friends."
            scene w2_1173 with dissolve
            "..."
            scene w2_1174 with dissolve
            "We both let that thought hang in the air between us for a number of moments."
            scene w2_1175 with dissolve
            mc "Well, there was that one time we promised to marry each other if we were still single when we turned 40."
            scene w2_1176 with dissolve
            mina "R-really...?!"
            mc "No, I'm kidding."
            scene w2_1177 with dissolve
            mina "Iknewthat!"
            mc "Sure you did, you dweeb. You looked worried!"
            scene w2_1178 with dissolve
            mina "Okay fine, you got me. Hehe~♥"
            scene w2_1126 with dissolve
            mc "So going by your expression in the photo, you guys must've done pretty good at your competition?"
            scene w2_1129 with dissolve
            mina "Nope! We came fourth out of five teams. Any and all smiles was all us."
            scene w2_1126 with dissolve
            mc "You don't look defeated at all."
            scene w2_1179 with dissolve
            mina "Going on a trip with friends was more important to us than landing center of target."
            "The look on her face told me she really did mean that."


            if w2MinaConversate == 3:
                pass
            else:
                scene w2_1126 with dissolve
                "While I was here to help her prepare for her role, I was enjoying learning more about Mina."
                mct "(I'll ask her about one more thing before moving on.)"
                mc "So..."
                hide screen textbox2 with dissolve
                scene w2_1108 with fade
                jump w2MinaWallMenu


        "Ask about her theatrical experience." if w2MinaJulietQ == False and w2MinaConversate == 1 or w2MinaJulietQ == False and w2MinaConversate == 2:
            $ w2MinaJulietQ = True
            $ w2MinaConversate += 1

            scene w2_1180 with dissolve
            show screen textbox2 with dissolve
            mc "Is that you performing Shakespeare?"
            mina "Yeah, an all-girl rendition of Romeo and Juliet. Would you believe I wanted the role of Mercutio? I got stuck with Juliet."
            scene w2_1181 with dissolve
            mc "You didn't want to be the star of the play?"
            scene w2_1182 with dissolve
            mina "Heck no! Juliet is a dumb kid who dies for a man she knew less than a week. Mercutio, on the other hand, is hilarious."
            scene w2_1183 with dissolve
            mina "He calls Romeo out on his bull crap and he uses his dying words to make a pun. That's way more fun than playing a love sick floozy!"
            scene w2_1181 with dissolve
            mc "Well, when you put it that way..."
            scene w2_1182 with dissolve
            mina "To be honest, I pushed hard for something other than Romeo and Juliet. I wanted King Lear or Merchant of Venice, but for some stupid reason Romeo and Juliet is tradition for an all girl's school."
            scene w2_1183 with dissolve
            mina "I would've {b}loved{/b} to play Cordelia."
            scene w2_1181 with dissolve
            mc "Doesn't she also die for a stupid reason?"
            scene w2_1184 with dissolve
            mina "No, it's a great death! Juliet dies for a stranger. Cordelia dies for her father. Even if he's a jerk, there's a world of difference in my book."
            scene w2_1183 with dissolve
            mina "I mean, she's cast out by King Lear for her unflinching honesty in the very first act and what does she do? She doesn't swear revenge or harbor any hatred for her father like she probably should."
            scene w2_1184 with dissolve
            mina "Instead, she proves her devotion by returning with an army and coming to his aid in the final acts. You could say she's unrealistic, but that's okay. Sometimes characters in stories should exemplify something bigger than ourselves."
            scene w2_1185 with dissolve
            "Mina's face was practically alight, animated by a surprising degree of enthusiasm. More so than her usual manufactured amount."
            scene w2_1186 with dissolve
            mc "You seem to really love this stuff. Is that why you want to be an actor?"
            scene w2_1187 with dissolve
            mina "I actually fell into acting just like I did modeling: it was something I tried out and just happened to learn how much fun it was."
            scene w2_1186 with dissolve
            mc "Heh, I bet a ton of struggling actors, whose lifelong dream it is, would hate you if they heard that. "
            scene w2_1187 with dissolve
            mina "Did you always want to be a doctor?"
            scene w2_1188 with dissolve
            mc "Always? Hmm... I mean I probably wanted to be a superhero when I was really young, but it was the first {i}realistic{/i} thing."
            scene w2_1187 with dissolve
            mina "That's fascinating how some people always knew."
            scene w2_1189 with dissolve
            mc "Oh? You find me fascinating do you?"
            scene w2_1190 with dissolve
            mina "Of course I do! You're a pretty interesting guy, [mcf]."
            scene w2_1191 with dissolve
            "The way she answered my teasing matter-of-factly, like it was an obvious thing, actually caused me to blush."
            scene w2_1127 with dissolve
            mina "Me? I've always struggled with who and what I want to be, but I think I've found it now. That's what you're here lending me a hand for."


            if w2MinaConversate == 3:
                pass
            else:
                scene w2_1126 with dissolve
                "She was right. I was here for a purpose, but I was enjoying learning more about Mina."
                mct "(I'll ask her about one more thing before we move on.)"
                "So..."
                hide screen textbox2 with dissolve
                scene w2_1108 with fade
                jump w2MinaWallMenu


        "Ask her about the magazine cover." if w2MinaMagazineQ == False and w2MinaConversate == 1 or w2MinaMagazineQ == False and w2MinaConversate == 2:
            $ w2MinaMagazineQ = True
            $ w2MinaConversate += 1

            scene w2_1192 with dissolve
            show screen textbox2 with dissolve
            mc "Tell me about the blown up, half-naked photo of yourself that you keep on your bedroom wall."
            scene w2_1193 with dissolve
            mina "Oh, you jerk!"
            scene w2_1194 with dissolve
            mc "I mean, you DID draw attention to it."
            mina "D-don't look so closely at it!"
            scene w2_1195 with dissolve
            mc "What are you suddenly embarrassed about? Didn't you think you looked good enough to hang it up on your wall?"
            mina "Mmmh...!"
            scene w2_1196 with dissolve
            mc "Heh, sorry! I couldn't resist. You seem a tad self-concious about it, but here it is. What is the story with it?"
            scene w2_1197 with dissolve
            mina "Ah, well... it's pretty simple really. Earlier this year was the first time I was on a magazine cover."
            scene w2_1198 with dissolve
            mc "That sounds like a big deal."
            scene w2_1199 with dissolve
            mina "It is...! Although, sticking it on the wall wasn't my idea. I mean, it is..."
            scene w2_1198 with dissolve
            mc "A blown up, half-naked photo of yourself."
            scene w2_1200 with dissolve
            mina "Stop using my exact words, please and thank you!"
            scene w2_1201 with dissolve
            mina "...but yeah, would you believe it was a gift from my mother? She never really liked me modeling, but the moment she saw me on that cover, she was very proud."
            scene w2_1198 with dissolve
            mc "What, she showed all her friends?"
            scene w2_1199 with dissolve
            mina "Um... yes, actually. It was really embarrassing. She even showed her pastor! Still..."
            scene w2_1201 with dissolve
            mina "It was also very reaffirming, you know? It felt really good! So much so that when she had it framed and insisted I hang it up in my apartment, I could hardly refuse her."
            mina "Not that I REALLY mind. Every time I look at it, I remember my mom's reaction and get that same nice feeling again. You have anything like that? That you look at and it reminds you of your feelings?"
            scene w2_1202 with dissolve
            mc "......"
            mc "..."
            mct "(\"My mom's porn videos\", but it's not like I can tell her that.)"
            scene w2_1126 with dissolve
            mc "...I'm not really the sentimental type I guess."
            scene w2_1128 with dissolve
            mina "Hehe, that's okay! Not many guys are."

            if w2MinaConversate == 3:
                pass
            else:
                scene w2_1126 with dissolve
                "Hmm... while I was here to help her prepare for her role, I was also enjoying learning more about Mina."
                mct "(I'll ask her about one more thing before moving on to the main reason I'm here.)"
                mc "So..."
                hide screen textbox2 with dissolve
                scene w2_1108 with fade
                jump w2MinaWallMenu

    scene w2_1203 with dissolve
    mc "Ah, what do you say we finally get down to why I'm here?"
    mina "Sure! We can stop and have lunch when the food gets here."
    mc "Helping an actor rehearse is a first for me. What do I need to do?"
    scene w2_1204 with dissolve
    mina "Read from a piece of paper! Err.. well, a screen."
    mina "I have the script for the first episode right here on my tablet. I've got two scenes in it."
    mc "If I remember correctly, you said you were playing a student who's having an affair with her professor?"
    scene w2_1205 with dissolve
    mina "Good memory! Yeah, it's not a huuuge role, but I am playing adjacent one of the show's leading men."
    scene w2_1206 with dissolve
    mct "(Loving Days in Lafayette...)"
    scene w2_1207 with dissolve
    mc "Seems pretty tawdry for daytime television."
    scene w2_1206 with dissolve
    mina "It's television for bored housewives and aging spinsters. Tawdry is what sells."
    scene w2_1207 with dissolve
    mc "I'm reading for the part of Nick?"
    scene w2_1206 with dissolve
    mina "You are. Dr. Nick Rawlings, a southern gentleman, married man, father of three, and professor of history at Lafayette University."
    scene w2_1208 with dissolve
    play sound "sound effects/furniture-moving.wav"
    mina "He's sexually frustrated and has recently found his eyes wandering up co-ed's legs and down their shirts. "
    mc "That's... colorful."
    stop sound
    scene w2_1209 with dissolve
    mina "I'm playing Elizabeth 'Liv' Forester, one of his history students that has her sights set on him. She's pretty crazy."
    scene w2_1210 with dissolve
    mc "I see here the scene opens with me sitting down?"
    scene w2_1211 with dissolve
    mina "That's correct. The scene opens pre-affair, with Nick grading papers in his office after hours. He's trying to hurry and get home to his wife when..."
    scene w2_1212 with vpunch
    "Mina gave a cute bunny hop for emphasis."
    mina "I enter, a siren who'll stop at nothing to seduce and ensnare the good professor with her womanly wiles. Muhaha!"
    scene w2_1213 with dissolve
    mc "You're already into it, huh?"
    scene w2_1214 with dissolve
    mina "Just setting the mood. You don't feel like you have to match my energy or even act, I can work off of just a basic reading. Whatever you're most comfortable with, [mcf]."
    scene w2_1213 with dissolve
    mc "I don't know how good I'll be, but it could be fun. I'll at least try to give you something to work off of."
    scene w2_1215 with dissolve
    stop music fadeout 3.0
    mina "Hehe, thanks! Okay, I'm going to go out in the hall. When I enter, that'll be your cue! You have the first line"
    scene black with fade
    "......"
    play sound "sound effects/door-openclose.wav"
    "..."
    scene w2_1216 with curtains
    mc "We didn't have an appointment..."
    scene w2_1217 with dissolve
    mc "...did we Miss Forester?"
    scene w2_1218 with dissolve
    play music "music/together-with-you.ogg"
    mina "We did not, Professor Rawlings -- and call me Liv."
    mc "Can I help you with something? The campus is about to close down."
    scene w2_1219 with dissolve
    mina "I know, the building is almost empty. All the other offices are locked up and I reckon it's just {b}you and lil' ol' me{/b} on this floor."
    mc "That didn't answer my question. I'm in a rush to get grading done, so if you could just please tell me how I might help you..."
    scene w2_1220 with dissolve
    mina "I noticed something inappropriate in yesterday's class and I wanted to discuss it."
    scene w2_1221 with dissolve
    mc "Inappropriate? Yesterday was about generational conflict at the turn of the 19th century. What could you possibly have a problem with?"
    scene w2_1220 with dissolve
    mina "Oh, it wasn't anything to do with the lecture, Professor Rawlings. Not at all. Your lesson was simply impeccable, as always."
    scene w2_1221 with dissolve
    mc "What did you find inappropriate then?"
    scene w2_1222 with dissolve
    "Mina bent forward, pointing her chest square in my face as if she was leaning over an imaginary desk."
    scene w2_1223 with dissolve
    mina "The way you kept staring down my shirt."
    scene w2_1224 with dissolve
    show layfeyette-script with dissolve
    "A quick glance down at the tablet only denoted to leave a pregnant pause before the next line. I guess how I act out that pause is up to me..."
    hide screen textbox2 with dissolve
    m_dev "If you get 6 or more scene points, you'll have the option to end the scene with a kiss."
    menu w2MinaDateSC:
        "{color=#FF1493}[[Social Chameleon]{/color} Momentarily linger on her chest before looking her in the face."(chg=["MinaSP_up2"]) if perk_socialChameleon == True:
            $ w2MinaScenePoints += 2

            scene w2_1225 with dissolve
            show screen textbox2 with dissolve
            "Taking a second to consider how a burgeoning pervert might actually respond, I let my gaze linger on Mina's chest."
            scene w2_1226 with dissolve

            if toughness <= 17:
                "While her being in sweats certainly made things easier, her large bust crammed into a tight hoodie still made me feel like I was being impolite for staring."
            else:
                "Even though she was only wearing sweats, it was still an enticing sight thanks to her large bust being crammed inside the tight hoodie."

            "It didn't take much \"acting\" for my eyes to wantonly linger on her chest before delivering my character's half-hearted denial."
            scene w2_1227 with dissolve
            mc "That's outrageous. I did no such thing!"
        "Look away.":


            show screen textbox2 with dissolve
            "While her being in sweats made Mina's pose less suggestive, her large bust crammed into the tight hoodie still made me feel like I was being impolite for staring."
            scene w2_1228 with dissolve
            "Naturally, I felt like I should look away."
            scene w2_1229 with dissolve
            mc "That's outrageous. I did no such thing."
            scene w2_1228 with dissolve
            "My delivery felt pretty flat, but then again, I'm not an actor."
        "Stare at Mina's chest like a deer caught in the headlights."(chg=["MinaSP_up"]):

            $ w2MinaScenePoints += 1

            scene w2_1230 with dissolve
            show screen textbox2 with dissolve
            mct "(I'm supposed to be playing a pervert, right...?)"
            scene w2_1226 with dissolve
            "With that in mind, I kept my eyeline firmly on her chest."
            "While her being in sweats made Mina's pose less suggestive, it was still quite the sight. Her large chest was crammed into a tight hoodie and shoved in front of my face after all."
            if toughness <= 17:
                "The civilized part of me felt averse to it, but I decided it was what my character would do."
            scene w2_1227 with dissolve
            mc "...that's outrageous. I did no such thing."

        "{color=#696969}[[Social Chameleon] Momentarily linger on her chest before looking her in the face. {/color}" if perk_socialChameleon == False:
            jump w2MinaDateSC

    scene w2_1231 with dissolve
    mina "That's not a very convincing denial, Professor."
    scene w2_1224 with dissolve
    show layfeyette-script2 with dissolve
    "The next line read: \"I don't care what you believe, it simply isn't true.\""
    hide layfeyette-script2 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Forcefully deliver the line.":

            scene w2_1232 with dissolve
            show screen textbox2 with dissolve
            mc "I don't care what you believe, it simply isn't true!"
            "Summoning as much conviction as I could muster, I vehemently denied the accusation as if it was actually being levied against me."
            scene w2_1233 with dissolve
            mina "Don't misunderstand me, sir. I said it was inappropriate, but I didn't say I was offended."
            scene w2_1234 with dissolve
            "......"
            "..."
            scene w2_1235 with dissolve
            mct "(Ah! Wait! I was supposed to stand up.)"
        "Stand up for emphasis."(chg=["MinaSP_up"]):

            $ w2MinaScenePoints += 1

            scene w2_1236 with dissolve
            show screen textbox2 with dissolve
            mc "I don't care what you believe, it simply isn't true."
            scene w2_1237 with dissolve
            "Standing up. A total power play. That seemed to me to be the correct way to deliver the line."
            scene w2_1238 with dissolve
            mina "Don't misunderstand me, sir. I said it was inappropriate, but I didn't say I was offended."

    scene w2_1239 with hpunch
    mc "I'll tell you what's inappropriate, you coming in here and--"
    scene w2_1240 with dissolve
    mc "Ah, shit. Sorry! Are you...?"
    mina "I'm alright, just keep going. You're getting into it!"
    "She was right. This was kind of fun."
    scene w2_1241 with dissolve
    mct "(Right, um... where was I? Oh!)"
    scene w2_1242 with dissolve
    mc "*clear throats* Ah-um, I'll tell you what's inappropriate, you coming in here and making such outlandish claims..."
    "Mina's going to cut me off at..."
    mc "I'm a respectable--"
    scene w2_1243 with dissolve
    mina "Relax. Even assuming what I said was true, it's not like it's a crime if your gaze just happens to drop below a girl's neckline. Nor do I have any proof, nor would any take my word against the word of the esteemed, {b}respectable{/b} Dr. Rawlings."
    mc "Then why are you here?"
    mina "For a very smart man, you sure are dense, Professor. What I'm trying to say is... I {b}like it{/b} when you stare down my shirt in class."
    scene w2_1244 with dissolve
    mc "You do...?"
    mina "Mmmhum, I certainly do."
    scene w2_1245 with dissolve
    "The script called for another pause. However, Mina's next line read \"Would you like to touch them?\" but it didn't prescribe any direction before that."
    hide screen textbox2 with dissolve

    menu:
        "Look down at Mina's breasts."(chg=["MinaSP_up"]):
            $ w2MinaScenePoints += 1

            show screen textbox2 with dissolve
            "Logically, the Professor's eyes would be drawn down to Elizabeth's bust and then she would deliver the offer."
            scene w2_1246 with dissolve
            mc "..."
            scene w2_1247 with dissolve
            mina "Would you like to touch them?"
        "Let a hand languidly find their way to Mina's waist.":


            show screen textbox2 with dissolve
            "There was something about Mina's close proximity that made grabbing a hold of her waist feel natural, so that was what I did."
            scene w2_1248 with dissolve
            mc "..."
            scene w2_1249 with dissolve
            mina "Would you like to touch them?"

    scene w2_1250 with dissolve
    mct "(Hmmm, physically rebuke...?)"
    hide screen textbox2 with dissolve

    menu:
        "Push Mina away from you."(chg=["MinaSP_up"]):
            $ w2MinaScenePoints += 1

            scene w2_1251 with hpunch
            show screen textbox2 with dissolve
            mc "That's enough of that! I don't know what you think you're doing, but this is wholly out of line. Get out of my office, before I report your clumsy attempt at seduction to the dean!"
        "Forcefully turn away and point to the door.":


            scene w2_1252 with dissolve
            show screen textbox2 with dissolve
            mc "That's enough of that! I don't know what you think you're doing, but this is wholly out of line."
            scene w2_1253 with dissolve
            mc "Get out of my office, before I report your clumsy attempt at seduction to the dean!"

    scene w2_1254 with dissolve
    stop music fadeout 3.0
    mina "Alright, Professor Rawlings. Have it your way. Just let it be known, I'm {b}very{/b} willing."
    scene w2_1255 with dissolve
    mina "If you change your mind, let me know with one of your pervy gazes. I'll come running~♥"
    scene w2_1256 with dissolve
    "Mina finished out the scene with an improvised wink."
    scene w2_1257 with dissolve
    play music "music/ukulele-fun.ogg"
    mina "Aaaaaand scene! Great job, [mcf]."

    if w2MinaScenePoints >= 3:
        scene w2_1258 with dissolve
        mina "You've never acted before?"
        scene w2_1259 with dissolve
        mc "Never."
        scene w2_1258 with dissolve
        mina "Well, you could fool me. You seem like a natural."
    else:

        scene w2_1261 with dissolve
        mina "That was good. You really gave me a lot to work with."

    scene w2_1260 with dissolve
    mc "Thanks."
    scene w2_1261 with dissolve
    mina "No, thank you. I have one more scene I'd like to run through with you. There's a few minor things in between, but it's all nonverbal. The teacher perving out some more, some dirty looks in the classroom..."
    mina "All of it amounts to your character finally succumbing to the temptation of a hot and horny co-ed and throwing his better judgement out the window."
    scene w2_1260 with dissolve
    mc "That makes a ton of sense to me."
    scene w2_1261 with dissolve
    mina "Did I make a convincing seductress?"
    scene w2_1260 with dissolve
    mc "I don't know about Professor Rawlings, but I probably would've fallen for it."
    scene w2_1262 with dissolve
    mina "Hehe, I'll take it!"
    scene w2_1263 with dissolve
    mina "If the next scene makes you uncomfortable, it's TOTALLY fine if you just give me a line reading. We don't have to emote it as--"
    play sound "sound effects/door-bell.wav"
    scene w2_1264 with dissolve
    mina "Oooh, I hope that's the food! I'm starving!"
    scene black with fade
    mct "(What happens in the next scene?)"
    scene w2_1265 with bites
    mc "Thanks for lunch."
    mina "Mmmh~dhont mhenthionet!"
    "The pair of us dug into the platter, an assortment of various types of sushi. Not a bad payment for a couple of hours of my time."
    scene w2_1266 with dissolve
    mc "Is this that place on the corner?"
    mina "Uhuh, it's conveniently close."
    scene w2_1267 with dissolve
    mc "It was pretty fun running through that with you."
    scene w2_1268 with dissolve
    mina "Oh, yeah? I'm glad to hear I'm not just sucking up your time."
    scene w2_1269 with dissolve

    if toughness >=20:
        mc "Don't worry about that, I've got jack shit to do this summer now that I'm not tutoring brats any more."
    else:
        mc "Don't worry about that, I've got almost nothing to do this summer now that I'm tutoring anymore. "

    scene w2_1270 with dissolve
    mina "Did you not enjoy teaching?"
    scene w2_1269 with dissolve
    mc "Eh, well... it was a cushy job. It paid well, for what was basically just making sure someone's kid kept their nose in the books and grilling them on the material."
    scene w2_1270 with dissolve
    mina "...but?"
    scene w2_1269 with dissolve
    mc "It was grating dealing with the parents. That and most of them were just rich assholes that took a lot of things for granted."
    scene w2_1271 with dissolve
    mina "Life's too short, right? It's a good thing you left it behind then."
    scene w2_1272 with dissolve
    mc "Let's move away from \"don't likes\". What do you like about acting so much that you want to do it as a career?"
    scene w2_1273 with dissolve
    mina "Hmm... this will probably sound cliché, but it IS true for me."
    scene w2_1270 with dissolve
    mina "The thing I like best about acting is being someone else. I can leave indecisive Mina and her baggage at the door and totally forget about my silly worries."
    scene w2_1271 with dissolve
    mina "A lot of actors try and draw from their own personal experience to genuinely portray a character, but that doesn't work for me. I need to be in the moment, to get out of my own head and operate on pure instinct."
    scene w2_1269 with dissolve
    mc "So, acting as a form of escapism?"
    scene w2_1270 with dissolve
    mina "Maybe. I just wouldn't have fun if I had to do it inside of my head."
    scene w2_1278 with dissolve
    "I had always written off things like modeling and acting as vain pursuits, but to hear Mina talk about acting so whole heartedly with full pathos had me feeling a little foolish."
    scene w2_1269 with dissolve
    mc "I think that's really cool."
    scene w2_1274 with dissolve
    mina "Hehe~ thanks, Ian never wants to talk about work, mine or his, so it's nice that you asked."
    scene w2_1275 with dissolve
    mina "Oh, you got a piece of..."
    mc "Here?"
    mina "No, no... let me..."
    scene w2_1276 with dissolve
    "Mina got up close, bringing her dainty hand up to my chin and extending a delicate finger to wipe off the offending detritus."
    scene w2_1277 with dissolve
    mina "There!"
    mc "Thanks..."
    "I wasn't sure what it was about this particular moment, but I was acutely and abruptly aware that her and I were {i}alone{/i} in her room."
    scene w2_1278 with dissolve
    "She didn't NEED to do that, I thought."
    scene w2_1271 with dissolve
    mina "So... Hana was super cool. Are you two...?"
    scene w2_1269 with dissolve

    if hanaFriendFlag == True:
        mc "No, we're not. Why do you ask?"
    if w2HanaSex == True:
        mc "That's... no, not really. Why do you ask?"
    if hanaFlag == False:
        mc "No, nothing of the sort. Why do you ask?"

    scene w2_1270 with dissolve
    mina "With the way Ian pushed me out the door this morning mumbling about giving you two some space, I got the impression you guys might be... involved?"
    scene w2_1278 with dissolve

    if w2HanaSex == True:
        "Hana and I did fool around last night, but {i}involved{/i} didn't quite fit it."

    scene w2_1269 with dissolve
    if hanaFlag == True:
        mc "Well, you're right about her being cool, but we're not dating. That was the second time we've ever hung out."
    else:
        mc "Well, you're right about her being cool, but we're not dating. That was the first time we've hung out."

    scene w2_1279 with dissolve
    mc "Yeesh, thinking about it, I've been single for a couple of years now."
    scene w2_1280 with dissolve
    mina "How come? Too focused on school?"
    scene w2_1281 with dissolve
    mc "Mmmhh... I guess, but it's not like I purposefully put it on the backburner. Meeting people to date just never happened for me."
    scene w2_1280 with dissolve
    mina "Ah... I can't say anything, up until 11 months ago, I'd never been in a relationship."
    scene w2_1282 with dissolve
    "......"
    "..."
    scene w2_1283 with dissolve
    mc "Ian's your first boyfriend?"
    scene w2_1284 with dissolve
    "That... made all the sense in the world, actually. THERE was my answer about why she's put up with his crap for so long."
    scene w2_1285 with dissolve
    mina "I w-went to an all girl's school, okay? It's not like I had a ton of options for normal romance growing up."
    mina "I did have a \"girlfriend\" for a couple of months, but that was just something the student body did for fun since there weren't any boys around."
    scene w2_1286 with dissolve
    mc "Don't get self-conscious about it. You're nineteen. That's not TOO weird."
    scene w2_1287 with dissolve
    mina "It's... not?"
    scene w2_1286 with dissolve
    mc "No. You just skipped a bunch of hormonal, awkward shit."
    scene w2_1288 with dissolve
    mina "Mmmh, Felicia teases me about it though."
    scene w2_1289 with dissolve
    mc "Heh, I wouldn't look to her as an arbiter of what's normal."
    scene w2_1274 with dissolve
    mina "Hehe~ you're right. She IS kinda a ho -- in a lovable way, of course!"
    scene w2_1290 with dissolve
    mina "Speaking of, let's finish eating. I've got another scene to slut it up in!"
    scene black with fade
    stop music fadeout 3.0
    "Hearing her say that with a pure-hearted smile was a detonative combination."
    "......"
    "..."

label w2MinaLineReadingPart2:

    play sound "sound effects/door-openclose.wav"
    scene w2_1291 with curtains
    "Just as before, Mina exited and re-entered the room to kickstart the scene."
    "As she had described, apparently between the first scene and this one, Nick Rawlings had tossed all professional propriety out the window through a montage of goo-goo eyed classroom flirtations."
    mct "(Got to get to the good stuff quick for the viewers at home, I suppose.)"
    scene w2_1292 with dissolve
    mina "You wanted to see me, Professor?"
    scene w2_1293 with dissolve
    mc "Get out of the doorway and come in, Miss Forester."
    play music "music/together-with-you.ogg"
    scene w2_1294 with dissolve
    mina "It sounded serious, is something the matter?"
    scene w2_1295 with dissolve
    show layfeyette-script3 with dissolve
    "Let's see... the script says to leer at her before moving onto the next line."
    hide screen textbox2 with dissolve

    menu:
        "Lean forward in your seat and give her a look over."(chg=["MinaSP_up"]):
            $ w2MinaScenePoints += 1

            scene w2_1296 with dissolve
            show screen textbox2 with dissolve
            mc "..."
            scene w2_1297 with dissolve:
                subpixel True
                yalign 1.0
                xalign 0.6
                linear 12 yalign 0.3
            "Perhaps a worrying thought, but slipping into the right mindset came shockingly easy to me as I slid my eyes past Mina's shapely thighs and well-pronounced hips, up the flat of her tummy and lingered on her breasts to fully admire the view."
            "It was a proper and despicable eye-fucking, grimy and filthy, the kind that would not fail to send a shiver up someone's back. Man or woman."
            "It was a look that I would never, in my life, dare to make."
            mct "(Isn't acting great?)"
            scene w2_1298 with dissolve
            mc "I've noticed your attention drifting in class this week."
            scene w2_1299 with dissolve
            mina "Ehmm...?"
            scene w2_1300 with dissolve
            mina "..."
            scene w2_1301 with dissolve
            mina "Line please?"
            scene w2_1302 with dissolve
            "Mina looked at me expectantly and I glanced down at the tablet."
            mc "Sorry, professor. I have just had a lot on my mind."
            scene w2_1303 with dissolve
            mina "Right, right... sorry professor..."
            scene w2_1309 with dissolve
            mc "When you're in my class, I require nothing short of your undivided attention."
        "Stand up and circle around, giving her a look over.":




            scene w2_1304 with dissolve
            show screen textbox2 with dissolve
            "I decided to circle around Mina like she was a piece of meat."
            scene w2_1305 with dissolve:
                subpixel True
                yalign 1.0
                xalign 0.6
                linear 6 yalign 0.6
            "Once behind her, I took in the sights, running my gaze up her shapely thighs and fixated on her perfectly round bubble butt."
            "The slight arch in her back would draw my gaze ever so often, and I couldn't help but see in my mind's eye a more exaggerated picture of Mina being ridden."
            scene w2_1306 with dissolve
            "It was a little worrying how easily I slipped into this sort of grimy mindset and I was glad she couldn't see the eye-fucking I was giving her all in the pursuit of a convincing portrayal."
            mct "(Isn't acting great?)"
            scene w2_1307 with dissolve
            mc "I've noticed your attention drifting in class this week."
            scene w2_1308 with dissolve
            mina "Sorry, professor. I have just had a lot on my mind."
            scene w2_1309 with dissolve
            mc "When you're in my class, I require nothing short of your undivided attention."

    scene w2_1310 with dissolve
    mina "That's the problem. I can't focus on the material when I've got my eyes on you, Professor."
    mct "(Ugh, who writes this crap?)"
    scene w2_1311 with dissolve
    mc "That's... unacceptable. We've got to fix that."
    scene w2_1312 with dissolve
    "Looking ahead a handful of lines, it looks like my character is going to be taking an active, borderline {b}aggressive{/b} role this time."
    scene w2_1313 with dissolve
    mina "How do you propose we remedy this problem, professor?"
    hide screen textbox2 with dissolve
    scene w2_1312 with dissolve

    menu:
        "Stroke Mina's cheek.":

            scene w2_1314 with dissolve
            show screen textbox2 with dissolve
            "Gently, I brushed the underside of my fingers against the supple skin of her cheek."
            mc "That depends on you, {b}Elizabeth{/b}."
            scene w2_1315 with dissolve
            "Slowly, Mina looked up at me, eyes brimming with anticipation, like a prisoner who was about to be set free."
            mct "(She's a damn good actor.)"
            scene w2_1316 with dissolve
            mina "Depends on what, sir?"
            scene w2_1317 with dissolve
            mc "We do this my way."
        "Grab Mina's chin and look into her eyes."(chg=["MinaSP_up"]):


            $ w2MinaScenePoints += 1

            scene w2_1318 with dissolve
            show screen textbox2 with dissolve
            "Taking care not to do it too rough, but still putting a bit of gusto into it, I forcefully grabbed Mina by the chin and leveled her gaze with mine."
            mc "That depends on you, {b}Elizabeth{/b}."
            scene w2_1319 with dissolve
            "Mina's eyes smoldered with sexual tension, challenging me with a dirty look that would give a lecher pause."
            mct "(She's a damn good actor.)"
            mina "Depends on what, sir?"
            scene w2_1317 with dissolve
            mc "We do this my way."

    scene w2_1320 with dissolve
    mc "This can't leave this room. You understand? The university has a strict no fraternization policy between teachers and students."
    scene w2_1321 with dissolve
    mina "Of course, my lips are sealed. Where~EVER you'd like them."
    "Mina's inflection dripped with sex appeal, one that perfectly suited the incongruency of Mina's innocent, sweet-looking face and her bombastic curves."
    scene w2_1322 with dissolve
    "She could easily have men at her feet if she wanted. The fact that she seemingly doesn't know that only added to her charm."
    scene w2_1323 with dissolve
    mina "Next line?"
    scene w2_1324 with dissolve
    mc "Eh, oh...? I guess I got lost in your eyes for a second."
    scene w2_1330 with dissolve
    mina "Oh..."
    scene w2_1331 with dissolve
    mc "Let's go back a line, please."
    scene w2_1322 with dissolve
    mina "..."
    scene w2_1321 with dissolve
    mina "Of course, my lips are sealed. WhereEVER you'd like them."
    scene w2_1325 with dissolve
    mc "Elizabeth..."
    scene w2_1326 with dissolve
    mina "Y-yes, Professor?"
    scene w2_1327 with dissolve
    mc "You're a good girl, right?"
    scene w2_1328 with dissolve
    mina "If that's what you want."
    scene w2_1329 with dissolve
    mc "I need you to be serious."
    mc "I need you to promise me, Elizabeth. I'm a married man, this is nothing more than a fling. If word got out..."
    scene w2_1332 with dissolve
    mina "I am, Professor. Feel!"
    scene w2_1333 with dissolve
    mc "--!"
    scene w2_1334 with dissolve
    mina "Feel how fast my heart is beating, I'm very serious about this."
    scene w2_1333 with dissolve
    "Bereft of any hesitation, Mina took ahold of my hand in hers and boldly placed it on her left breast."
    scene w2_1334 with dissolve
    mina "I promise. We'll do this on your terms."
    scene w2_1333 with dissolve
    "The tips of my fingers all but clamped down, held back at the last microsecond by a snap response of ingrained civility."
    scene w2_1335 with dissolve
    mina "This is all strictly just a professor helping out a student with her problem."
    scene w2_1336 with dissolve
    mct "(This woman, does she not see me as a man?)"
    "Of course, there was no way I could feel Mina's heartbeat through a handful of meaty tit flesh, but I DID spot an inkling of inhibition."
    scene w2_1337 with dissolve
    "The moment my palm made hand-over-cloth contact with the upbeat actress' breast, Mina tensed up and a spot of color hit her face."
    mct "(Fuck, what was the next line...?)"
    "Given the circumstances, how could I hope to recall the line I had read just a handful of seconds before?"
    scene w2_1338 with dissolve
    mina "I think the line is something like..."
    scene w2_1337 with dissolve
    "Right, Mina jarred my memory."
    hide screen textbox2 with dissolve

    menu:
        "Massage her breast and deliver the line with full conviction."(chg=["MinaSP_up", ("mina_up", Mina_KLove <= 4)]):

            $ w2MinaScenePoints += 1
            if Mina_KLove <= 4:
                $ Mina_Affection += 1

            show screen textbox2 with dissolve
            "If she had put my hand there without thinking, she wasn't backing down. Part of me considered that she did it simply because she didn't care. This could all just be an exercise in acting to her."
            "In the back of my head however, my thoughts swung the other way. The way she was looking at me..."
            scene minatease1_a with dissolve
            show Minatease1
            mc "You certainly {i}feel{/i} sincere."
            mct "(Could she be purposefully pushing boundaries?)"
            mina "OooOh, um... ahem..."
            "Whether or not that was actually the case, I sunk my fingers deeper into the buoyant flesh of her breast. Enough to get her attention, but taking care not to be too overt about it."
            if Mina_KLove <= 4:
                scene Minatease2 with dissolve
                mina "O-oh...!"
                "The extra attention appeared to confound her, as no line came from her lips. Instead, her head drooped down and her mind veered off elsewhere."
                "It was hard to say if she was simply feeling shy from being called on her game of chicken or if I had taken it too far. Either way, she was suddenly pacified."
                scene w2_1342 with dissolve
                mina "Ha.. ha... [mcf]?"
                scene w2_1340 with dissolve
                mina "Sorry, but that felt so SURPRISINGLY good that I forgot my line, hehe..."
                scene w2_1341 with dissolve
                "Hearing her just coming out and saying it shocked me. She actually doesn't think any of this is crossing the line?"
                scene black with fade
                mina "You could always be a masseuse if the whole med student thing doesn't work out."
                mc "Very funny, okay so you do this next and then the line is... Then I..."
                mina "Ahem..."
            else:


                scene w2_1339 with dissolve
                mina "Ngh, [mcf]...?"
                scene w2_1338 with dissolve
                mina "S-sorry, I forgot the line!"
                scene black with fade
                mc "Okay, so you... and then the line is... Then I..."
                mina "Ahem..."
        "Deliver the line.":



            scene w2_1336 with dissolve
            show screen textbox2 with dissolve
            "If she had put my hand there without thinking, she wasn't backing down. Part of me considered that she did it simply because she didn't care. This could all just be an exercise in acting to her."
            "In the back of my head however, my thoughts swung the other way. Could she be purposefully pushing boundaries?"
            scene w2_1343 with dissolve
            mc "You certainly {i}feel{/i} sincere."
            scene w2_1336 with dissolve
            "Either way, it was best I didn't push it."
            scene w2_1344 with dissolve
            mc "Hold on a second, let me check my next few lines."
            scene black with fade
            mct "(This really airs on TV?)"
            mc "Okay, we were at..."


    scene w2_1345 with fade
    mina "Is there anything else you'd like to feel, Professor?"
    scene w2_1346 with dissolve
    "The moment Mina turned around and pressed her butt into me confirmed that she truly had no qualms with this sort of contact."

    if Mina_KLove <= 4:
        scene minatease3_a with dissolve
        show Minatease3
        "She even took it a step further, subtly rubbing herself against me like an animal seeking warmth. Perfectly suited for the scene perhaps, but nonetheless an obstacle in trying to remember my goddamn line."
        "The action also confirmed what I had previously suspected. She had an IMPECCABLE ass, round and tight, with the right amount of heft a man could get behind."
        "I felt a pull in my arms, telling me to grab her hips. It just seemed right, given the circumstances..."
        mct "(It's part of the scene, right?)"
    else:

        "The action also confirmed what I had previously suspected. She had an IMPECCABLE ass, round and tight, with the right amount of heft a man could get behind."
        "I felt a pull in my arms, telling me to grab her hips. It just seemed right, given the circumstances..."
        mct "(It's part of the scene, right?)"

    hide screen textbox2 with dissolve

    menu:
        "Grab her hips while you deliver the next line."(chg=["MinaSP_up"]):

            $ w2MinaScenePoints += 1

            scene w2_1348 with dissolve
            show screen textbox2 with dissolve
            if Mina_KLove <= 4:
                "Clasping my hands around her hip bone, I brought the gentle sway to a halt and pressed Mina more firmly into me."
            else:
                "Clasping my hands around her hip bone, I pressed Mina more firmly into me."

            scene w2_1347 with dissolve
            mc "I can think of a FEW things."
            scene w2_1348 with dissolve
        "Deliver your next line.":

            scene w2_1349 with dissolve
            show screen textbox2 with dissolve
            mc "I can think of a FEW things."
            scene w2_1346 with dissolve


    "The script didn't specifically call for it, but I felt the urge to..."
    hide screen textbox2 with dissolve

    menu:
        "Add your own flourish. Smack that rear end!"(chg=["MinaSP_up", ("mina_up", Mina_KLove <=4)]):

            $ w2MinaScenePoints += 1

            if Mina_KLove <=4:
                $ Mina_Affection += 1
                scene w2_1350 with dissolve
                scene w2_1351 with hpunch
                play sound "sound effects/slap2.wav"
                show screen textbox2 with dissolve
                "*Smack!*"
                mina "Oh...!"
                "I gave Mina's tight rear end a light tap, the impact of which elicited a cute yelp from my acting partner."
            else:

                scene w2_1350 with dissolve
                scene w2_1352 with hpunch
                play sound "sound effects/slap2.wav"
                show screen textbox2 with dissolve
                "*Smack!*"
                mina "Eeeh?"
                "Give Mina's tight rear end a light tap, the impact of which produced a whelp of confusion from my acting partner.."
        "Resist the urge to slap Mina's beautiful bubble butt.":

            "No. Don't touch. Bad."

    scene w2_1353 with dissolve
    "With a weapons-grade level of pep, Mina spun on the heel of her foot like a ballerina doing a pirouette before twisting her mouth into a predatory, shark-like grin."
    scene w2_1354 with dissolve

    if Mina_KLove <=4:
        mina "Don't just think of them, [mcf]-er, I mean... Professor."
    else:
        mina "Don't just think of them, Professor."

    mina "Do them. "

    if w2MinaScenePoints >=6:
        scene w2_1355 with instantdissolve
        scene w2_1356 with instantdissolve
        scene w2_1357 with instantdissolve
        scene w2_1358 with instantdissolve
        scene w2_1358 with instantdissolve
        scene w2_1357 with instantdissolve
        scene w2_1356 with instantdissolve
        scene w2_1355 with instantdissolve
        "What was called for next by the script was a kiss, shared between our characters, that one would naturally skip over in a situation like this. That, however, didn't seem to be the case."
        "Instead, Mina looked deep into my eyes with a disarming sensuality that was distantly removed from the cheap, tasteless material we were reciting."
        "It was like she was patiently waiting for me to make MY move, like it wasn't an unusual prospect to kiss your friend's girlfriend under the guise of acting practice."
        stop music fadeout 3.0
        "In fact, the certainty in her expression actually made it seem innocent."
        scene w2_1359 with dissolve
        mina "Mmmh...?"
        "Okay, maybe not so patiently."
        hide screen textbox2 with dissolve

        menu:
            "Mina is waiting. Kiss her."(chg=["mina_killian_down", ("mina_up3", Mina_KLove <= 2), ("mina_up2", Mina_KLove <= 3 and Mina_KLove > 2)]):
                $ w2MinaKiss = True
                $ Mina_KLove -= 1

                play music "music/soft-feeling.ogg"
                scene w2_1360 with dissolve
                show screen textbox2 with dissolve
                "Wrapping my hands around Mina, I gave her one last long look in the eyes, before pulling her tightly close to me like an action movie hero who just got the girl."
                mct "(This is kind of weird...)"
                "...is what I thought, but the more her emerald green eyes looked back at me, the less of a sticking point it became."
                scene minakiss1_a with dissolve
                show Minakiss1
                mina "Nhwah..."
                "A cute, sharp coo and then the taste of vanilla mint chapstick."
                mct "(Not a bad flavor...)"
                "It wasn't a deeply lewd kiss or anything, but our lips were wholly and fully locked together."
                "It skirted the line between passionate and tasteful, like a kiss shared between a bride and groom on their wedding day."

                if Mina_KLove <= 3:
                    $ Mina_Affection += 2
                    "However..."
                    scene minakiss2_a with dissolve
                    show Minakiss2
                    "She must have not been content with how I was doing it, because she pulled me deeper into the kiss."
                    "My hands found perch on her ass, prodding and teasing it, almost completely of their own volition."
                    mina "Mmmmh...♥"
                    "Another, even more sharp coo. Not that I wasn't enjoying it either..."
                    "By this point, my cock was firmly pressing into Mina, poking her lower body in a way that would be impossible to miss."

                    if toughness >=22:
                        "Not that she had any room to complain, with the way she was rubbing her body against me like a bitch in heat."
                    else:
                        "Part of me felt embarrassed about it on a instinctual level, but if she did indeed notice, it didn't deter her in the least."

                    if Mina_KLove <= 2:
                        $ Mina_Affection += 1
                        scene w2_1361 with dissolve
                        "By the time we broke up our kiss, it had felt like it had gone on for far longer than it had. Everything felt hazy on my end and Mina's glassed over expression told me she was likely feeling the same."
                        scene w2_1362 with dissolve
                        mina "Ha...♥"
                        scene minakiss3_a with dissolve
                        show Minakiss3
                        "...not that I needed it, considering I could've known that by the way she humped my leg like a wayward wind-up toy slowly losing its pep."
                        mina "Ah, isn't acting grand...?"
                        mc "...um, Mina? I forgot the next line."
                        scene w2_1393 with dissolve
                        mina "Oh? Um, h-hold on... let me think..."
                    else:


                        scene w2_1363 with dissolve
                        mina "Good... \"{i}acting{/i}\" there, partner."
                        mc "...ngh, yeah. You too."
                        scene w2_1364 with dissolve
                        mc "...um, Mina? I forgot the next line."
                else:

                    scene w2_1365 with dissolve
                    "When we broke from our kiss, it hadn't been an inordinate amount of time. Still, I could feel a blush in my cheeks and I could see Mina doing the same."
                    mina "..."
                    mct "(My thoughts exactly...)"
                    scene w2_1364 with dissolve
                    mc "...um, Mina? I forgot the next line."

                scene w2_1366 with dissolve
                mina "You say \"How was that?\" and then I say, \"That was everything I was hoping it'd be.\" or something like that."
                mina "Hehe~, I'm a little fuzzy on the lines all of a sudden for some reason."
                mct "(This woman...)"
                scene w2_1367 with dissolve
                "She carried on, business as usual. Unconcerned with what we just did."
                scene w2_1368 with dissolve
                if not persistent.w2MinaKissGallery:
                    play sound "sound effects/notification.wav"
                    show memoryunlock with dissolve
                    $ renpy.pause(3, hard=True)
                    $ persistent.w2MinaKissGallery = True
                    hide memoryunlock with dissolve
                    $ renpy.pause(0.5, hard=True)
                mina "Then it's fade to black and all my parts are done for the episode, hehe~"
                $ renpy.end_replay()
            "Artfully move past this part.":

                show screen textbox2 with dissolve
                scene w2_1369 with dissolve
                play music "music/together-with-you.ogg"
                mc "Ah, crap. I forgot my next line."
                "I had a semi-plausible, convenient excuse, but I didn't know if kissing my friend's girlfriend was a river I wanted to forge - even if, quite frankly, I wasn't entirely sure he'd give a shit."
                scene w2_1370 with dissolve
                mina "Hmm... I think..."
                mina "You say \"How was that?\" and then I say, \"That was everything I was hoping it'd be.\" or something like that."
                scene w2_1371 with dissolve
                mina "Then it's fade to black and all my parts are done for the episode, hehe~"
    else:

        scene w2_1370 with dissolve
        mina "...then there's a couple more lines."
        mina "You say \"How was that?\" and then I say, \"That was everything I was hoping it'd be.\" or something like that."
        scene w2_1371 with dissolve
        mina "Then it's fade to black and all my parts are done for the episode, hehe~"

    scene w2_1372 with fade
    play sound "sound effects/notification.wav"
    $ Mina_Relations = "Acting Partner"
    show relationmina with dissolve
    mina "It's a small couple of scenes, but things pick up in later episodes - or so I'm told, if they don't kill off my character by having her accidently fall into a volcano or something."
    scene w2_1373 with dissolve
    mc "...a volcano?"
    scene w2_1372 with dissolve
    mina "I'm told that one has has happened in the show's history."
    scene w2_1374 with dissolve
    mc "..."
    scene w2_1375 with dissolve
    mina "Hey, I know I'm not making art here!"
    scene w2_1376 with dissolve
    mina "Pfft--"
    "The two of us shared in a laugh, completely dispelling any lingering tension from the previous scene."
    scene black with fade
    stop music fadeout 3.0
    play ambient "sound effects/city-night.wav"
    "......"
    "..."
    scene w2_1377 with circlewipe
    mina "You sure you don't want me to drive you?"
    mc "Nah, I think I'll walk. I haven't been getting enough exercise lately. I'm getting pretty round around the edges."

    if w2MinaKiss == True:
        scene w2_1378 with dissolve
        mina "Speaking from recent experience, I know that's not true."
        scene w2_1379 with dissolve
        mc "Hehe..."


    scene w2_1380 with dissolve
    mina "Anyway, you suuuuuuure?"
    scene w2_1381 with dissolve
    mc "Yeah, but thanks for offering - and for the lunch. It was delicious."
    scene w2_1382 with dissolve
    mina "Of course...!"
    scene w2_1383 with dissolve
    mina "...hey, by the way, you doing anything this Friday?"
    scene w2_1384 with dissolve
    mc "Not yet. Why?"
    scene w2_1385 with dissolve
    mina "Well, my brother and I have some standing plans. We'll probably go to an arcade or something, you want to join?"
    scene w2_1387 with dissolve
    mc "You want the three of us to go to an arcade?"
    scene w2_1382 with dissolve
    mina "Yep, why not? It'll be fun and, well..."
    scene w2_1383 with dissolve
    mina "It's not like I want you to play big brother or anything, but it would do him some good to socialize with someone like you."
    scene w2_1384 with dissolve
    mc "Someone like me?"
    scene w2_1385 with dissolve
    mina "You know, a young adult male that has his head screwed on straight."
    scene w2_1387 with dissolve
    mc "Let him see what's at the end of the tunnel?"
    scene w2_1386 with dissolve
    mina "Exactly! Jeez, you always know how to put things."
    scene w2_1384 with dissolve
    mc "Sure, I'll be happy to tag along. Not so sure how he'll feel about it though."
    scene w2_1385 with dissolve
    mina "Eh, he'll be shy at first, but he'll get over it! He needs to get out of his comfort zone from time to time."

    if w2MinaKiss == True:
        scene w2_1388 with dissolve
        mina "Anywaaaaay...."
        mina "Um... hug goodbye?"
        scene w2_1389 with dissolve
        "Mina suddenly became... awkward? She's asking for a hug instead of simply throwing herself into one?"
        scene w2_1390 with dissolve
        mina "Hehe~"
        scene w2_1391 with dissolve
        mina "I'll see you later again. Be safe!"
    else:


        scene w2_1392 with dissolve
        mina "Anywaaaaay.... I'll see you later."
        scene w2_1391 with dissolve
        mina "Be safe on the way home, okay?"


    mc "Thanks, I will. Text me the details about Friday later."
    mina "Will do."
    scene black with fade
    if w2MinaKiss == True and w2MinaScenePoints >=6:
        $ history_mina = "I helped Mina work through her scenes for the first episode of the show she's appearing on, even going so far as to kiss her. Despite how weird it was, she seemed ultimately unperturbed by it."
    elif w2MinaKiss == False and w2MinaScenePoints >=6:
        $ history_mina = "I helped Mina work through her scenes for the first episode of the show she's appearing on, stopping short of kissing her. She didn't seem to mind how close some of it got."
    else:
        $ history_mina = "I helped Mina work through her scenes for the first episode of the show she's appearing on and had a good time doing it. She didn't seem to mind how close some of it got."
        $ unread_mina = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    stop ambient fadeout 3.0
    "......"
    "..."
    jump w2June08Evening


label w2June08Evening:
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionhousegirls with blinds
    $ renpy.pause(6, hard=True)

    play sound "sound effects/door-open.wav"
    scene w2_1394 with blinds
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    if minaFlag == False:
        "I went straight home from the club, determined to be productive with my time.."
    else:
        "After leaving Mina's and walking home, the afternoon was pretty much waning. Still, I was determined to make productive use of my time."

    scene w2_1395 with circlewipe
    "I ran through some MCAT exercises, looked into how the hell I'm going to file my taxes next year, and watched videos of people falling down on the internet."
    "Two out of three ain't bad."
    scene w2_1396 with dissolve
    play sound "sound effects/chair-squeek.wav"
    $ date = "june08night"
    show june08night with squares
    mc "Mmmmmm...."
    scene w2_1397 with dissolve
    mc "Muaahh!"
    scene w2_1398 with dissolve

    if minaFlag == False:
        mct "(Come to think of it... fuck, I'm hungry. I only had a snack when I came in...)"
    else:
        mct "(Come to think of it, I'm getting pretty hungry. That sushi was good, but it wasn't very filling...)"

    play sound "sound effects/door-open.wav"
    scene w2_1399 with fade
    mct "(I don't really feel like preparing anything, but takeout twice in one day seems wasteful. What to do?)"
    play sound "sound effects/ringing-outbound.mp3"
    scene w2_1400 with dissolve
    "{i}*Ring... ring...*{/i}"
    mc "..."
    "{i}*Ring... ring... ring...*{/i}"
    scene w2_1401 with dissolve
    if kat_polite == True:
        mct "(It's Mrs. Pulman...)"
    else:
        mct "(It's Kathleen...)"

    scene w2_1402 with dissolve
    "I very seriously considered ignoring it."
    stop sound
    play sound "sound effects/phonemenu.wav"
    scene w2_1403 with dissolve
    mc "Hello?"
    play music "music/leaving-home.ogg"
    kat "I need you to get down here {b}now{/b}. Don't dally."
    mc "Is something w--"
    play sound "sound effects/phonemenu.wav"
    scene w2_1404 with dissolve
    mc "...wrong?"
    "That was it. She had hung up on me."
    scene w2_1405 with dissolve
    mct "(That sounded urgent.)"
    "Naturally, from the terse message, I imagined the worst."
    mct "(It sounded REALLY urgent.)"
    scene w2_1406 with dissolve
    mct "(No time to change!)"
    scene black with fade
    "........."
    "......"
    scene club-fr-night2 blur with blinds
    "..."
    scene w2_1407 with dissolve
    mct "(Hurrying, hurrying, hurrying...)"
    scene w2_1408 with dissolve
    "I busted my ass to catch the next train and managed to make it to the club in record time."
    play sound "sound effects/elevator-bell.wav"
    scene w2_1409 with fade
    mct "(How did she put it...?)"
    mct "(I think it was... \"I need you to get down here NOW. Don't dally.\" Or was there an emphasis on the need?)"
    scene w2_1410 with fade
    mct "(Fuck, no one's here. I guess she's in her office.)"
    play sound "sound effects/door-open.wav"
    scene w2_1411 with fade
    mct "(She's not here... ah! The security room.)"
    scene black with fade

    play sound "sound effects/door-knock.wav"
    "*Knock* Knock*"
    war "Come on in, kid."
    play sound "sound effects/door-open.wav"
    scene w2_1412 with dissolve
    mc "Hey, I'm looking for--"
    mc "Shit, sorry!"
    scene w2_1413 with dissolve
    war "What's with that reaction? You should be used to this shit by now."
    scene w2_1414 with dissolve
    mc "Good point..."
    scene w2_1415 with dissolve
    mc "I'm looking for--"
    scene w2_1416 with hpunch
    hgirl "Ghhyyah...!"
    war "I didn't tell you to stop. Keep shaking that ass!"
    scene w2_1417 with dissolve
    "Wordlessly, the house girl picked up the pace, rocking her hips and grinding her insides against Warren's cock."
    scene w2_1418 with dissolve
    war "You're looking for Mrs. P?"
    scene w2_1417 with dissolve
    mc "Yeah, she called me and told me to get down here. It sounded urgent."
    scene w2_1418 with dissolve
    war "She's in the obsidian room."
    scene w2_1417 with dissolve
    mc "..."
    "The funny-looking expression on my face moved him to continue."
    scene w2_1418 with dissolve
    war "Exhibition level. Room #5."
    scene w2_1417 with dissolve
    mct "(Shit, I got to go all the way to the basement.)"
    mc "Thanks."
    scene w2_1419 with dissolve
    war "Hehe, {b}enjoy{/b}."
    scene black with fade
    mct "(Enjoy...?)"
    play sound "sound effects/slap2.wav"
    war "Ah, get up there like a dog, you fucking bitch. I can't cum with those half-assed movements."
    play sound "sound effects/elevator-bell.wav"

label w2KatBirthdayGift:

    if _in_replay:
        show transitionhousegirls with cmet
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

    scene w2_1420 with circlewipe
    mc "Room 205..."
    mc "There it is!"
    scene black with fade
    stop music fadeout 3.0
    play sound "sound effects/door-knock.wav"
    "*Knock* Knock*"
    kat "That you, [mcf]?"

    if kat_polite == True:
        mc "Yes, Ma'am."
    else:
        mc "Yes."

    kat "Come on in."
    play music "music/no1-a-minor-waltz.ogg"
    scene w2_1421 with w21
    "As soon as I entered the room #5, my eyes beheld a shocking sight."
    scene w2_1422 with dissolve
    "Harper was strung upside down, legs secured to some trapeze like thing and hands bound behind her back."
    "She wore a gag and blindfold, as she dangled gently above what appeared to be a ink-black bath tub."
    scene w2_1423 with dissolve
    kat "Hello, [mcf]. Lucky for Harper, you got here fast."
    scene w2_1424 with dissolve
    mc "...you said I needed to get down here?"
    scene w2_1425 with dissolve
    "The scene in front of me had vacated all sense of urgency from my body, replacing it with a sinking feeling of uncertainty."
    scene w2_1423 with dissolve
    kat "I know I said not to dally, but it wasn't {i}really{/i} urgent. I just couldn't help myself. "
    kat "I wanted to give you your present as soon as possible."
    scene w2_1425 with dissolve

    if kat_polite == True:
        "The uncomprehending look on my face moved Mrs. Pulman to further explain."
    else:
        "The uncomprehending look on my face moved Kathleen to further explain."

    scene w2_1426 with dissolve
    kat "... a belated birthday present. For you."
    scene w2_1424 with dissolve
    mc "No... I put that part together, the thing that doesn't track with me is how this is a gift exactly."
    scene w2_1427 with dissolve
    mc "Are you okay, Harp?"
    scene w2_1429 with dissolve
    harp "Ghughhh...!"
    mct "(Silly question...)"
    scene w2_1428 with dissolve
    scene w2_1429 with dissolve
    "...but she ended up nodding yes."
    scene w2_1430 with dissolve
    kat "I can see your confusion, but it will all evaporate with a push of a button."
    scene w2_1431 with dissolve
    kat "Take this from me."

    if kat_polite == True:
        "Mrs. Pulman offered me a peculiar looking... remote?"
    else:
        "Kathleen offered me a peculiar looking... remote?"

    scene w2_1432 with dissolve
    kat "Press the button."
    scene w2_1433 with dissolve
    mc "......"
    scene w2_1434 with dissolve
    mc "..."
    scene w2_1435 with dissolve
    kat "The floor isn't going to fall out from underneath you."
    scene w2_1436 with dissolve
    mc "Alright..."
    scene w2_1437 with dissolve
    play sound "sound effects/button-beep.wav"
    "*Click*"
    scene harpers1stdiveAZ with dissolve
    show harper1stdive with dissolve
    $ renpy.pause(1, hard=True)
    play sound "sound effects/water-splash2.wav"
    harp "Mmmh!"
    mc "Shit-!"
    "As soon as I pressed the button, a mechanism whirled to life and quickly lowered Harper down into the tub of water beneath her."
    $ renpy.music.set_volume(.4, 0, channel = "ambient")
    play ambient "sound effects/water-splash3.wav"
    harp "*Splash* *Splash* *Splash*"
    scene w2_1438 with dissolve
    mc "Fuck, fuck, fuck...!"
    play sound "sound effects/button-beep.wav"
    scene w2_1439 with dissolve
    "*Click*"
    stop ambient fadeout 3.0
    scene harperriseAZ with dissolve
    show harperrise with dissolve
    "I quickly pressed the button again, and as simple as that, Harper was once more hoisted up in the air."
    mc "What the hell?"
    scene w2_1440 with dissolve
    kat "Tell me, how did that make you feel?"
    mc "Panicked."
    kat "I believe you believe that. Maybe that's even true, but if it is.. that wasn't the only thing you felt, was it?"
    scene w2_1441 with dissolve
    mc "..."
    scene w2_1442 with dissolve
    kat "Come now..."
    play sound "sound effects/button-beep.wav"
    scene w2_1443 with dissolve
    "*Click*"
    scene harper2nddiveAZ with dissolve
    show harper2nddive with dissolve
    $ renpy.pause(1, hard=True)
    play sound "sound effects/water-splash2.wav"
    "*Splash*"
    harp "*Splash* *Splash* *Splash*"
    scene harper2nd_z with dissolve
    scene harper2ndstruggle with dissolve
    play ambient "sound effects/water-splash3.wav"
    kat "You can't tell me you don't feel a huge rush from watching her flop about like a stupid fish."
    "Harper's lithe, toned body jerked and wiggled in a rush of panic. The sight had the hair of my neck standing on end and a lump forming in my throat."
    mc "Hit the button."
    kat "Don't worry, this type of play is a specialty of hers. Harper volunteered for this."
    kat "Not to mention, she's being paid generously for the night."
    mc "Hit the button!"
    play sound "sound effects/button-beep.wav"
    "*Click*"
    stop ambient fadeout 2.0
    scene harper2ndriseZA with dissolve
    show harper2ndrise with dissolve
    kat "As you wish."
    "Harper was raised back up until she hung precariously once more, with full knowledge that one slip of the finger would send her plummeting once more into the tepid water below."
    "The way her body uncomfortably jostled about, the way her breasts bounced as she shook, and the way the water pooled over their cherry points..."
    harp "Gh...ghh...!"
    "Not to mention the sounds she made..."
    scene w2_1444 with dissolve
    "I more or less figured out what my \"present\" was by now."
    scene w2_1445 with dissolve
    mc "You're telling me to use all of that and do whatever I want?"
    scene w2_1444 with dissolve
    kat "That's right."
    scene w2_1445 with dissolve
    mc "...you're out of your mind."
    scene w2_1446 with dissolve
    stop music fadeout 3.0
    kat "[mcf], [mcf], [mcf]..."
    kat "You should learn to be yourself and enjoy life."
    scene w2_1447 with dissolve
    mc "Be myself or be more like you?"
    scene w2_1446 with dissolve
    kat "That's a trick question, dear. We're very similar."
    scene w2_1448 with dissolve
    mc "Hell no we're not."
    scene w2_1449 with dissolve
    play music "music/myst-on-the-moor.ogg"
    if kat_polite == True:
        "Mrs. Pulman sighed deeply."
    else:
        "Kathleen sighed deeply."

    scene w2_1450 with dissolve
    kat "You need to be more convincing than that."
    kat "I've observed you, I've learned about you, and through a little bit of intuition too, I've come to recognize in you a particular quality."
    scene w2_1451 with dissolve
    kat "You see [mcf], my sister and I couldn't have been more diametrically opposed. She was a woman capable of genuine altruism."
    kat "She experienced vicarious joy from helping people at great expense to herself, but as a child there was an uncomfortable truth about myself that I didn't fully grasp until I grew into a young woman."
    kat "I could only experience the same kind of happiness she felt in her charity, by seeing other people suffer."
    scene w2_1452 with dissolve
    kat "Why do you think that is? Why were my sister and I so different? We shared the same genes, were raised in the same home, yet we wound up so opposite..."
    scene w2_1453 with dissolve
    mc "I couldn't tell you."
    scene w2_1450 with dissolve
    kat "If you said you could, you'd be a fool. It's a question beyond the current means of understanding. Funnily enough, the charity she started was a place that satisfied both of us."
    scene w2_1453 with dissolve
    mc "She got to help people and you got to see them at their lowest?"
    scene w2_1454 with dissolve
    kat "Uh huh, and the fact that you understood that so quickly is telling. You and I share a \"feet of clay\" as they say."
    kat "You're a sadist, just like me. We both enjoy seeing other people struggle."
    scene w2_1453 with dissolve
    mc "..."
    "I couldn't flat out deny it. That was a part of me I understood well and was something I purposefully compartmentalized from my everyday life."
    scene w2_1452 with dissolve
    kat "It's a banal thing really, found in plenty of people, but the majority of those never bother to self-reflect on it."
    scene w2_1451 with dissolve
    kat "No. Most people simply live their lives callously enjoying the schadenfreude of everyday misfortune and inequity. They never fully feel out the shape and form of their very own soul."
    scene w2_1453 with dissolve
    mc "What's your point?"
    scene w2_1454 with dissolve
    kat "My point is, this is the gift I'm offering you on your birthday. To fully know yourself."
    scene w2_1455 with dissolve
    kat "Within this building, you don't have to shy away from who you are. I'll accept you and every nook of your being, [mcf]."
    kat "It's just a present. You have the right to refuse of course, and no matter how much thought I may have put into getting you the PERFECT gift, I won't be mad."
    scene w2_1456 with dissolve
    mc "Mmhh..."
    "As I looked into her eyes, I didn't know what to say. I instinctually wanted to turn her down, to vehemently deny all that she was offering, but deep down in me was a hole that I stuffed all my vicious, vile feelings into and it was now bubbling like a geyser about to erupt."
    scene w2_1455 with dissolve
    kat "Harper really did agree to this, y'know. She trusts you won't take it too far. Plus..."
    kat "You've never indulged yourself have you? This is a controlled environment, what better place to learn about yourself?"
    scene w2_1457 with dissolve
    "Before I answered her, I had to be sure of one thing..."
    scene w2_1458 with dissolve
    mc "Harper..."
    scene w2_1459 with dissolve
    mc "Is what she's saying true?"
    scene w2_1460 with dissolve
    harp "Ahem! Aha! Guh... yes."
    scene w2_1461 with dissolve
    mc "For real? You volunteered?"
    scene w2_1462 with dissolve

    if jacobHarpVouch == True:
        harp "I trust you. You have my consent."
    else:
        harp "You have my consent, Mr. [mcl]."

    scene w2_1479 with dissolve
    kat "...and everything is permissible if you have consent."
    mct "(I'm not sure I agree with that.)"
    scene w2_1463 with dissolve
    "I gave one last look at Harper and the table of goodies. It was easy for me to vividly imagine myself tormenting her with them."
    mct "(I have her consent...)"
    scene w2_1464 with dissolve
    mct "(...but what does that mean in a place like this?)"
    "I resigned myself to an answer. I..."
    hide screen textbox2 with dissolve

    menu:
        "Accept her gift."(chg=["tough_up3","kathleen_trust_up3"]):
            $ toughness +=3
            $ Kathleen_Trust +=3

            scene w2_1465 with dissolve
            show screen textbox2 with dissolve
            mc "I accept. Thanks for the gift."
        "Help Harper down."(chg=["tough_down3"]):


            $ toughness -=3
            $ w2HarpRainCheck = True
            show screen textbox2 with dissolve
            jump w2KatGiftDecline


    scene w2_1466 with dissolve
    if kat_polite == True:
        "Mrs. Pulman smiled at me, in a gregarious way I wasn't sure was physically possible for her."
    else:
        "Kathleen smiled at me, in a gregarious way I wasn't sure was physically possible for her."

    scene w2_1467 with dissolve
    kat "Excellent, now why don't you take a minute, go freshen up, and get changed out of those rags?"
    scene w2_1466 with dissolve
    mc "I don't have anything to change into."
    scene w2_1468 with dissolve
    kat "All the better then. Do as you please."
    scene w2_1469 with dissolve

    if kat_polite == True:
        "Mrs. Pulman broadly gestured toward Harper and the table of toys like she was a piece of meat. In some ways, I suppose she was..."
    else:
        "Kathleen broadly gestured toward Harper and the table of toys like she was a piece of meat. In some ways, I suppose she was..."

    scene w2_1457 with dissolve
    "Which quite frankly didn't work for me."
    scene w2_1470 with dissolve
    "Harper winced and blinked incessantly from the sudden removal of her blindfold."
    scene w2_1471 with dissolve
    kat "Oh? I think it's more fun when they don't know when it's coming."
    hide screen textbox2 with dissolve

    menu:
        "You want to see Harper's face for this."(chg=["kathleen_up"]):
            $ Kathleen_Affection +=1

            scene w2_1472 with dissolve
            show screen textbox2 with dissolve
            mc "I want to see the sorry look on her face. I think that's more fun."
            scene w2_1473 with dissolve
            kat "Ha! You're quick to drop your façade, I'll give you that."
            scene w2_1474 with dissolve
            harp "*Gulp* Ehehe... I can take anything you want to give, sir."
            scene w2_1475 with dissolve
            mct "(Despite my bravado just now, what exactly am I supposed to do to her?)"
        "You want Harper to be able to speak."(chg=["tough_down2"]):

            $ toughness -= 2

            scene w2_1476 with dissolve
            show screen textbox2 with dissolve
            mc "I don't feel comfortable if she's unable to speak or tell me to stop."
            scene w2_1477 with dissolve
            kat "How lucky for you, Harper. [mcf] is more conscientious than your typical client."
            scene w2_1478 with dissolve
            harp "Don't worry, I can take anything you want to give, sir."
            scene w2_1475 with dissolve
            mct "(She says that, but... what am I supposed to do to her?)"

    "I've never done this before, which in turn made me afraid."
    "There's a medical condition known as refeeding syndrome. It is a well-documented process where introducing too much food too quickly to a starving man can prove fatal."
    "It might be melodramatic, but for someone who has worked diligently to keep the uglier side of his personality in check for the past 8 years, I was afraid indulging too fully would leave an indelible mark on my self-control."
    scene w2_1480 with dissolve
    harp "Ah..."
    mct "(If I'm going to indulge this side of me, I'm going to need to be slow and deliberate.)"
    scene w2_1481 with dissolve

    if kat_polite == True:
        "Giving someone like me free rein over her body. She must put a lot of trust in Mrs. Pulman."
    else:
        "Giving someone like me free rein over her body. She must put a lot of trust in Kathleen."

    scene w2_1480 with dissolve
    "...or her choices are that limited. It seemed absurd, considering how she was just dangling there like a toy, but..."
    scene w2_1481 with dissolve
    mct "(What kind of woman is Harper?)"
    "I genuinely did wonder. Did she have parents that loved her? What did she originally want to do with her life?"
    scene w2_1480 with dissolve
    "Is she a mother too? Does she support those parents that loved her? How did she end up at the club? Who knows."
    scene w2_1482 with dissolve
    "These were the kind of thoughts I hoped would tether me to acting conscientiously, but..."
    scene w2_1483 with dissolve
    harp "Gh-! *Cough* Gh-! *Cough* Gh-!"
    "They just spurred me on. A whole life of experiences - hopes, dreams, and disappointments, all funneled to this point in time where she's just an object."
    scene w2_1484 with dissolve
    mc "Anything, huh?"
    harp "Anyshwing~"
    scene w2_1485 with dissolve
    mct "(However, I knew...)"
    scene w2_1486 with pixellate
    mct "(Harper wasn't an object. She was a person. I understood that well enough.)"
    scene w2_1487 with dissolve
    harp "Gyeeeh!"
    mct "(That's what made this sadistic.)"
    "While considering the tools at hand, a flash of inspiration hit me."
    hide screen textbox2 with dissolve

    menu:
        "Reassure Harper one final time before explaining your plan."(chg=["tough_down"]):
            $ toughness -= 1
            scene w2_1488 with dissolve

            show screen textbox2 with dissolve
            if kat_polite == True:
                mc "*Whisper* If you want to stop, just say so. I'll make sure Mrs. Pulman doesn't get angry with you."
            else:
                mc "*Whisper* If you want to stop, just say so. I'll make sure Kathleen doesn't get angry with you."

            scene w2_1489 with dissolve
            scene w2_1490 with dissolve
            scene w2_1489 with dissolve
            "Harper nodded to show me she understood."
            scene w2_1491 with dissolve
            mc "Okay, then. Here's what's going to happen."
            scene w2_1492 with dissolve
            mc "I'm going to dunk you in the water until you tell me you've had enough. After that, I'm going to use a crop to whip you until you do the same. Then we go back to the dunking."
            scene w2_1491 with dissolve
            mc "This will repeat until I've had my fill or you truly bow out. Understood?"
            scene w2_1493 with dissolve
        "Explain in excruciating detail what's about to happen."(chg=["tough_up2","kathleen_up"]):



            $ toughness += 2
            $ Kathleen_Affection += 1

            scene w2_1494 with dissolve
            show screen textbox2 with dissolve
            harp "Gyaaaah...!"
            scene w2_1495 with dissolve
            mc "The water's cold, isn't it?"
            scene w2_1496 with dissolve
            harp "A l-little..."
            scene w2_1497 with dissolve
            play sound "sound effects/slap2.wav"
            scene w2_1498 with vpunch
            harp "Eyeee!"
            scene w2_1499 with dissolve
            mc "Good. Your skin gets more sensitive in cold temperatures. You know why that is?"
            scene w2_1497 with dissolve
            play sound "sound effects/slap2.wav"
            scene w2_1498 with vpunch
            harp "Gah! N-no...!"
            scene w2_1499 with dissolve
            mc "You see, when you're cold, your body sends less blood to your extremities and more to your vital organs. It does this to preserve heat."
            mc "This means your skin is more rigid, which due to the pressure, makes your nerves even more sensitive."
            scene w2_1500 with dissolve
            mc "I'm going to turn that into a little game."
            scene w2_1501 with dissolve
            harp "A... game?"
            scene w2_1500 with dissolve
            mc "Yep, one where you get to choose what happens to you."
            mc "I'm going to incessantly dunk you in the water until you can't stand it anymore. Until your body feels like lead and you tire of trying to catch your breath."
            mc "Once you want to stop, we'll stop. Easy as that."
            mc "That's when I'll use the crop to whip you, and I'll batter your cold and wet skin until you yield once again. Then we'll go back to step 1."
            mc "This will repeat until I've had my fill. Understood?"
            scene w2_1501 with dissolve

    harp "*Gulp* Yes..."
    scene w2_1502 with dissolve
    kat "Oh, that's good. Did you just come up with that? I might just have to pick your brain next summer for ideas."
    "Despite how confidently I explained my plan, I still felt a pang of uncertainty. Like I was crossing over the horizon with no clue what lay on the other side."
    scene w2_1503 with dissolve
    mc "We should settle on a word that'll signify you want to switch punishments."
    mc "How about..."
    scene w2_1504 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Harper says uncle.":
            $ w2HarpUncle = True
            scene w2_1505 with dissolve
            show screen textbox2 with dissolve
            mc "Whenever you want to switch, you'll say uncle. That should be easy enough to remember."
            scene w2_1506 with dissolve
            harp "Uncle... got it."
        "Harper barks like a dog":

            $ w2HarpDog = True
            if toughness >= 21:
                scene w2_1507 with dissolve
                show screen textbox2 with dissolve
                mc "Whenever you want to switch, just bark like a bitch. Should be pretty easy, right?"
            else:
                scene w2_1505 with dissolve
                show screen textbox2 with dissolve
                mc "Whenever you want to switch, just bark like a dog."
            scene w2_1506 with dissolve
            harp "...understood."
        "Have Harper say the name of someone important to her.":

            $ w2HarpDad = True
            scene w2_1505 with dissolve
            show screen textbox2 with dissolve
            mc "I want you to say the name of someone important to you when you want to switch."
            scene w2_1506 with dissolve
            harp "W-what?"
            scene w2_1507 with dissolve
            mc "When you surrender, I want you to reflect on your life up to this point. To that end, I want the word on your lips to be the name of someone near and dear to you."
            mc "Do you have anyone like that who fits the bill?"
            scene w2_1506 with dissolve
            harp "Ugh... my..."
            harp "My father's name is Theodore."
            scene w2_1505 with dissolve
            mc "We'll go with that, then. Whenever you want to switch punishments, you'll say {b}Teddy{/b}."
            scene w2_1506 with dissolve
            harp "...understood."

    scene w2_1508 with dissolve
    "With that I felt ready to begin."
    mct "(Remember, take it slow and don't go overboard.)"
    mct "(Harper is putting herself in my hands tonight, I should respect and remain cognizant of that.)"
    scene w2_1509 with dissolve
    play sound "sound effects/button-beep.wav"
    "*Click*"
    scene harperrediveAZ with dissolve
    show harperredive with dissolve
    $ renpy.pause(0.8, hard=True)
    play sound "sound effects/water-splash2.wav"
    "The first time I pushed that button with deliberate aim, an incredible feeling gripped me."
    play ambient "sound effects/water-splash3.wav"
    scene harperredive_z
    show harperrestruggle with dissolve
    harp "*Splash, splash*"

    if kat_polite == True:
        "It wasn't the feeling of freedom Mrs. Pulman had described it as. It felt more like a surrender."
    else:
        "It wasn't the feeling of freedom Kathleen had described it as. It felt more like a surrender."

    mct "(Four, five, six, seven, eight, nine...)"
    play sound "sound effects/button-beep.wav"
    "*Click*"
    stop ambient fadeout 2.0
    scene harperrediveZA with dissolve
    show harperrerise with dissolve
    "The dull mechanical drone of the pulleys was a shockingly sweet sound and Harper shined beautifully underneath the harsh spotlight."
    "Water rolled down from her lower half, and like a river flowing into a valley, scattered with the rise of her chest."
    "Beads of it pooled at the tips of her breasts, agonizingly hanging off of the cherry-like tips for just a tantalizing moment, before gravity returned the water back to the tub below."
    play sound "sound effects/button-beep.wav"
    "*Click*"
    scene harperrediveAZ with dissolve
    show harperredive with dissolve
    $ renpy.pause(0.8, hard=True)
    play sound "sound effects/water-splash2.wav"
    harp "Urheh...!"
    "The splash of Harper hitting the water also sounded sweet. It was pleasant, like the chime of a bell."
    play ambient "sound effects/water-splash3.wav"
    scene harperredive_z
    show harperrestruggle with dissolve
    play ambient "sound effects/water-splash3.wav"
    harp "*Splash, splash*"
    mct "(Four, five, six...)"
    "The way her lower body swayed, like a perverse twist on a belly dance..."
    mct "(Seven, eight, nine...)"
    play sound "sound effects/button-beep.wav"
    "*Click*"
    stop ambient fadeout 2.0
    scene harperrediveZA with dissolve
    show harperrerise with dissolve
    "This experience was a full feast for the senses, I thought."
    harp "Ha... ha... ugh, give me a sec--"
    mc "Do you surrender?"
    harp "No, it's just give me a..."
    play sound "sound effects/button-beep.wav"
    "*Click*"
    scene harperrediveAZ with dissolve
    show harperredive with dissolve
    $ renpy.pause(0.8, hard=True)
    play sound "sound effects/water-splash2.wav"
    "...and down she went again."
    scene black with wet
    "Again, and again, and again, until..."
    scene w2_1510 with wet

    if w2HarpUncle == True:
        harp "Guh, u-uncle! Uncle!"
    if w2HarpDog == True:
        harp "Guh, I g-ive... um... arf arf arf!"
    if w2HarpDad == True:
        harp "Guh, I give! T-teddy! Teddy!"

    "Harper elected to switch punishments."
    scene w2_1511 with dissolve
    kat "Ha, gh...!"
    scene w2_1512 with dissolve
    mct "(Is that...?)"
    scene w2_1513 with dissolve

    if kat_polite == True:
        "Mrs. Pulman was off on the sidelines, leather panties pulled to the side, jilling herself off."
    else:
        "Kathleen was off on the sidelines, leather panties pulled to the side, jilling herself off."

    "With an icy smile upon her lips, her eyes were unerringly fixated not on Harper, but me."
    scene w2_1514 with dissolve
    kat "Don't mind me, dear. I'm just enjoying the show."
    scene w2_1513 with dissolve
    mct "(...was this a present for me or for her?)"
    scene w2_1515 with dissolve
    "Who cares. I was intent on enjoying the taste of what I've been given. Maybe then I thought, it'll be out of my system."
    scene w2_1517 with dissolve
    mc "How old are you, Harper?"
    scene w2_1518 with dissolve
    harp "...thirty one."
    scene w2_1517 with dissolve
    mc "You're nine years older than I am."
    scene w2_1518 with dissolve
    harp "So what?"
    scene w2_1519 with dissolve
    play sound "sound effects/slap1.wav"
    scene w2_1520 with instantdissolve
    harp "Ah, eh-!"
    scene w2_1521 with dissolve
    scene w2_1522 with dissolve
    "I'd never even held a riding crop in my hand before, so I went with a weak, tentative lashing to test the waters. Start light, I thought."
    scene w2_1523 with dissolve
    mc "I just wanted us to get to know each other better. What's your last name?"
    scene w2_1524 with dissolve
    harp "Ivanova."
    scene w2_1519 with dissolve
    play sound "sound effects/slap1.wav"
    scene w2_1520 with instantdissolve
    harp "S-shit!"
    scene w2_1521 with dissolve
    scene w2_1522 with dissolve
    "The crop had an extremely satisfying {b}snap{/b} to it as it cut through the air."
    scene w2_1523 with dissolve
    mc "How did you end up working here?"
    scene w2_1524 with dissolve
    harp "You're supposed to be whipping me, but instead you're talking your mouth off. Is that because you're a {b}virgin{/b} at this?"
    scene w2_1522 with dissolve
    "Harper's words weren't said out of annoyance. At least, I didn't think they were. Instead, like a seasoned prostitute, she's trying to goad me to the benefit of my experience."
    hide screen textbox2 with dissolve

    menu:
        "Don't take the bait. Admit what she said is true.":

            scene w2_1525 with dissolve
            show screen textbox2 with dissolve
            mc "Ehehe, that's probably more than a little true."
            harp "Don't worry too much. Just relax and do what's natural."
            "More honeyed words."
            scene w2_1519 with dissolve
            play sound "sound effects/slap1.wav"
            scene w2_1520 with instantdissolve
            harp "Eyeee!"
        "Take the bait and play along.":

            scene w2_1526 with dissolve
            show screen textbox2 with dissolve
            mc "You cheeky bitch!"
            scene w2_1527 with dissolve
            play sound "sound effects/slap1.wav"
            scene w2_1528 with instantdissolve
            harp "Eyeee!"
            scene w2_1527 with dissolve
            play sound "sound effects/slap3.wav"
            scene w2_1529 with instantdissolve
            harp "Ah...!"
            scene w2_1527 with dissolve
            play sound "sound effects/slap3.wav"
            scene w2_1528 with instantdissolve
            harp "Ghheeee!"
            "One after another, I delivered a series of quick lashings to her breasts."

    scene w2_1521 with dissolve
    scene w2_1517 with dissolve
    mc "How about this. How long have you worked here?"
    scene w2_1518 with dissolve
    harp "Three years."
    scene w2_1519 with dissolve
    play sound "sound effects/slap3.wav"
    scene w2_1520 with instantdissolve
    harp "Ahhe!"
    scene w2_1521 with dissolve
    scene w2_1523 with dissolve
    mc "That seems long."
    scene w2_1524 with dissolve
    harp "Longer than everyone, but Dalia."
    scene w2_1527 with dissolve
    play sound "sound effects/slap3.wav"
    scene w2_1529 with instantdissolve
    harp "F-fhuck!"
    scene w2KatMasturbate with dissolve
    hide screen textbox2 with dissolve
    "By this point, from out of the corner of my eye, I could tell my would-be mentor in sadism was {i}really{/i} into it."
    kat "Ha... ha... ha...!"
    "She was trying hard not to let out her pleasured moans, but they escaped in irregular ecstatic bursts."
    play sound "sound effects/slap3.wav"
    harp "Fhee, ouch!"
    "With every lash, her eyes shined brighter."
    "In the back of my mind, I knew it wasn't Harper driving her gratification. She was relishing in my participation."
    mct "(Well, if she wants a show, Harper and I will give her one!)"
    scene w2_1537 with dissolve
    play sound "sound effects/slap1.wav"
    scene w2_1538 with instantdissolve
    show screen textbox2 with dissolve
    harp "Ahsheet!"
    scene w2_1537 with dissolve
    play sound "sound effects/slap3.wav"
    scene w2_1536 with instantdissolve
    harp "Ngh..!"
    scene w2_1537 with dissolve
    play sound "sound effects/slap3.wav"
    scene w2_1538 with instantdissolve
    harp "Eyeee!"
    scene w2_1539 with dissolve

    if toughness >= 21:
        mc "How's that for a virgin, you slut?"
    else:
        mc "How's that for a virgin?"

    if w2HarpUncle == True:
        harp "Shit, uncle! Ooooncle!"
    if w2HarpDog == True:
        harp "Arf, arf, arf!"
    if w2HarpDad == True:
        harp "Teddy! I want to switch! Teddy!"

    scene black with fade
    "It carried on like that for a number of rounds. Harper was able to take everything I could dish out, until I felt both satisfied and more than just a little shamed by my indulgence."
    "She really was a pro."
    stop music fadeout 3.0
    scene w2_1540 with ccirclewipe
    harp "Ha... ha..."
    harp "Geh.... gah.... gyuu... y-you..."
    hide screen textbox2 with dissolve
    scene w2_1541 with dissolve
    "Now that was over, my mind wandered down south, to the rock hard erection in my sweatpants. I had been so preoccupied with tormenting Harper that my physical needs went unattended."
    "The way it strained and stretched the fabric wasn't unpleasant. I could just imagine the relief I would feel to finally free my cock."

    if not persistent.w2KatBirthdayGiftGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w2KatBirthdayGiftGallery = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)

    "As my hand worked itself to that inevitable conclusion..."
    $ renpy.end_replay()

    if Kathleen_Trust >= 8:
        $ w2KatSex = True
        jump w2EdwinKatScene
    else:
        $ w2HarperSolo = True
        jump w2HarperSoloEnding



label w2EdwinKatScene:

    if _in_replay:
        show transitionkathleen01 with cmet
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

    play music "music/from-russia-with-love.ogg"
    scene w2_1542 with dissolve
    kat "It's not enough!"

    if kat_polite == True:
        "A desperate cry pulled my attention away from my dick and back to Mrs. Pulman."
    else:
        "A desperate cry pulled my attention away from my dick and back to Kathleen."

    scene w2_1543 with dissolve
    "She was knuckle deep in her cunt, fervently pleasuring herself with a mix of frustration and ecstasy written on her face."
    kat "Mmmh, damn it...!"
    "Seeing the cruel and pernicious woman, who bought and sold people's needs and desires, debase herself had its own unique charm."
    scene w2_1542 with dissolve
    "She looked at me the same way she did the Carnations, like I was a mere piece of meat to be cooked up and served."
    "It was an infuriating look."
    scene black with fade
    show screen textbox2 with dissolve
    "In a hurry, I wiggled out of my shirt and practically leapt out of my pants."
    scene w2_1544 with dissolve

    if kat_polite == True:
        "Until I stood before both Mrs. Pulman and Harper, with my pulsating cock in my hand."
    else:
        "Until I stood before both Kathleen and Harper, with my pulsating cock in my hand."

    "Two can play that game, right?"

    kat "My, my, my... all that hands-on activity has your prick positively {b}throbbing{/b}."
    "Meanwhile, she never ceased pleasuring herself, spreading herself open and rhythmically penetrating herself with her digits."
    scene w2_1545 with dissolve
    kat "Mmmh...! You're not finished with Harper, are you? I'm not satisfied yet!"
    "Neither was I, but..."
    scene w2_1546 with dissolve
    kat "No, I guess she isn't in any position to grant you the release you need. Lucky for you... I am."
    kat "Do you know how horny I've been the past two days? Do you know how hard it is for me to deny myself during each and every summer exhibition?"

    if w1ExIntuitionGameWinnerRose == True:
        scene w2_1568 with pixellate
        mct "(Did she call what she did to Veronica and Felicia holding back?)"
    if w1ExIntuitionGameWinnerFel == True:
        scene w2_1569 with pixellate
        mct "(Did she call what she did to Veronica and Rosalind holding back?)"
    if w1ExIntuitionGameWinnerVero == True:
        scene w2_1570 with pixellate
        mct "(Did she call what she did to Rosalind and Felicia holding back?)"

    scene w2_1547 with pixellate
    mc "I don't follow."
    kat "You see, there's a painful double standard I have to abide if I want to be taken seriously by the men of the club."
    scene w2_1548 with dissolve
    kat "Even if I run the goddamn show, I can't ever fully let loose in front of those animals. They can, of course. That's their prerogative, but the moment I do, they'll start to view me as a woman."
    scene w2_1549 with dissolve
    mc "...and that's a bad thing?"
    scene w2_1550 with dissolve
    kat "{b}Yes.{/b}"
    scene w2_1551 with dissolve
    mc "Ah...!"
    "Her hand swiftly moved from my cheek to my dick. The sudden, warm tightness of her grip had my body reeling with pleasure."
    kat "You've enjoyed yourself tonight, right?"
    "Too caught up with the feeling of her hand on my dick to answer, I nodded in affirmative."
    scene w2KatHJ with dissolve
    kat "Good. I'm happy to hear that."
    "Her hand jacked me off at a steady, forceful pace."
    kat "I love good, honest boys like you."
    kat "You know... I've seen you fuck, but I've yet to taste you myself. It'd be a shame to make you cum with just my hand. Would you like me to use something else?"
    "I nodded again."
    scene w2_1554 with dissolve
    kat "Then, show me how obedient you can be."
    kat "Get on your knees and kiss my boot."
    scene w2_1555 with dissolve
    "She and I shared an oddly adversarial look."
    scene w2_1556 with dissolve
    kat "I was nice enough to let you indulge yourself. Now it's your turn to show me some proper respect."
    scene w2_1557 with dissolve
    mc "You want me to kiss your feet..?"
    scene w2_1556 with dissolve
    kat "I'm glad your ears work."
    scene w2_1558 with vpunch

    if kat_polite == True:
        "Mrs. Pulman put an unexpected amount of weight on my shoulder."
    else:
        "Kathleen put an unexpected amount of weight on my shoulder."

    "I could simply do as she says. It's not like I actually have a problem with that kind of foreplay, but doing as much in this situation would basically be telling her it's okay to treat me like a dog."
    hide screen textbox2 with dissolve

    menu:
        "Stand up for yourself.":
            stop music
            play sound "sound effects/slap2.wav"
            scene w2_1559 with dissolve
            show screen textbox2 with dissolve
            "*Slap*"
            scene w2_1560 with dissolve
            kat "Did you forget your pl--"
            scene w2_1561 with dissolve
            mc "I'm a man, not your plaything. If a toy is all you want..."
            play music "music/thunder.ogg"
            scene w2_1562 with dissolve
            mc "Help yourself. I'm done with them."
            scene w2_1563 with dissolve
            "She glared at me in a way that immediately made me doubt this direction, but I knew I needed to persist if I ever hoped for her to view me with respect."
            scene w2_1561 with dissolve
            mc "It's precisely because I'm a man that I can properly pay you back for your \"generosity\", and..."
            scene w2_1564 with vpunch
            kat "Ah...!"
            mc "...treat you like a woman. That's what tonight is all about, right? You said it yourself."
            scene w2_1565 with dissolve
            "I don't know what had come over me."
            "Maybe I was emboldened by what Harper and I had just done."
            scene w2_1566 with dissolve
            kat "Man...? That's a lofty word."
            kat "You're a boy to me until you prove otherwise."
            scene w2_1565 with dissolve
            "She gave me an unwavering look that served as an overt challenge."
            scene w2_1567 with hpunch
            kat "Eh?"

            if toughness >=21:
                "I abruptly and strongly pulled the old, cruel bitch close to me."
            else:
                "I abruptly and strongly pulled the cruel woman close to me."

            scene w2_1571 with dissolve
            kat "No offense [mcf], but you're built like a bean pole."
            scene w2_1572 with dissolve
            mc "You shouldn't have a problem if I'm a little blurry then."
            scene w2_1573 with dissolve
            kat "Careful, those are hard to find."
            scene w2_1574 with dissolve
            mc "You look better without them."
            scene w2_1575 with dissolve
            "I planted a quick smooch on the side of her face, one totally unfit for the setting, and then moved down to..."
            scene w2_1576 with dissolve
            "Kat's unnaturally perky tits."
            mc "*Fwup, fwup!*"
            "Her tear-drop shaped breasts had a pleasant squish as I pressed and nuzzled my face into their pale expanse."
            "All the while my other hand found purchase by sinking its finger tips into the depths of the baby-soft skin of her derriere."
            scene w2_1577 with dissolve
            kat "It doesn't really reinforce you being a man if you suckle at my tits like a baby."
            "I paid no attention to her and kept working at the rosy pink peak, coating it in my saliva and lightly caressing it with the edge of my teeth."
            "It was already engorged with arousal."
            "It probably had been ever since Harper and my torturous display, but I was intent on making it hard enough to cut diamonds before I moved on.."
            scene w2_1578 with dissolve
            kat "You know, I'm not some college slut. I'm two and half times your age. You're going to have to do better than your bumbling idea of foreplay."
            scene w2_1579 with dissolve
            kat "Ah, w-watch your teeth!"
            "Despite her words, I knew she was unquestionably horny. The way she pleasured herself earlier attested to that."
            scene w2_1580 with dissolve
            mc "Do you really want to bring age into this?"
            scene w2_1581 with dissolve
            kat "Oh, eh...!"

            if kat_polite == True:
                "Like a spin in a latin dance, I quickly turned Mrs. Pulman around and firmly pressed her backside into me."
            else:
                "Like a spin in a latin dance, I quickly turned Kathleen around and firmly pressed her backside into me."

            scene w2_1582 with dissolve
            "She let out a deep and contemptuous sigh, but I remained undaunted."
            scene w2_1591 with pixellate
            ver "You got a soft spot for your neck, huh?"
            kat "Gh..!"
            scene w2_1583 with pixellate
            mct "(Veronica, you beautiful woman...!)"
            "In this moment, I was thankful to her for paving the path forward with her golden touch."
            scene w2_1584 with dissolve
            kat "O-oh!"
            "Meanwhile, while I went to town on her neck, one of my hands worked down to her crotch and the other thumbed her breast."
            scene w2_1585 with dissolve
            kat "Mmmh... why do men get cocky when you give them even a quarter of a lead from your leash?"
            "I wanted to chide her for her free use of the word \"men\", but I didn't want to slow my assault on her neck while it was still in its fledgling stages."
            scene katstandup1_a with dissolve
            show katstandup
            mct "(Aaaah...! She smells good.)"
            "Like what I imagined money to smell like. The perfume that had been spritzed on her collar was quickly overwhelming my senses."
            kat "O-oh, oh...! You've got {b}good{/b} instincts, I'll give you that."
            "My fingers met no resistance as they sunk into the depths of her quim, her inner walls having been generously primed for entry by her earlier personal touch."
            kat "Ha... ah... ha...! Yes, I'll certainly give you that."
            "It was funny I thought. Penetrating her was such a simple action, done like with any other woman, despite the sheer gap of social status between us."
            "Not that it didn't occur to me that she could easily ruin my life if she wanted, but that added a perilous spice to the situation that just pushed me further along in my goal of winning her respect."
            mct "(I'm a dumb, stupid creature.)"
            "I vigorously pistoned my hand in and out, while I kissed the nape of her neck, nibbling at it as if we were lovers."

            if kat_polite == True:
                "I made certain not to go too far, too quickly in a conscientious bid to draw out the experience and leave a strong impression in Mrs. Pulman's mind."
            else:
                "I made certain not to go too far, too quickly in a conscientious bid to draw out the experience and leave a strong impression in Kathleen's mind."

            kat "Keep that up, [mcf]. This is good."
            "Of course, I did as I was bidden. My reward being the way her body gradually began to jerk and flinch with my touch."
            "Hot puffs of air escaped from the cruel woman's pursed lips, while her lower mouth sucked greedily on my digits."
            kat "This is good... THIS is good... THIS is GOOD..."
            scene w2_1586 with dissolve
            mc "Don't forget Harper."
            scene w2_1587 with dissolve
            kat "Oh? What of her?"
            scene w2_1586 with dissolve
            mc "Just reminding you that..."
            "It might have just been my imagination, but I thought I felt the insides of her cunt get tighter."
            mc "That we have an audience."
            scene w2_1588 with vpunch
            kat "Ahhhaaah!"
            "A firm love bite caused her head to crane straight up in a jolt surprise."
            scene w2_1589 with dissolve
            kat "Mhhh...."
            kat "You're getting awfully full of yourself."
            "It was as sultry a tone as I had ever heard leave her lips, dripping with pervy intent."
            scene w2_1590 with dissolve
            kat "That's enough. Foreplay is for virgins."
            kat "Let's fuck."
            scene black with fade
            kat "Get on your back. I'm leading now."
        "Quid pro quo here. You've had your fun, now do as she says. [mod_chat]":

            $ w2KatSexSub = True
            show screen textbox2 with dissolve
            mct "(Well, she's the boss, right?)"
            scene w2_1592 with dissolve
            kat "Smart. You understand there's a pecking order."
            scene w2_1593 with dissolve
            "If a dog is good enough, he'll get fed table scraps. That was her logic and one that I was willing to abide."
            scene w2_1594 with dissolve
            kat "Before you clean my boots..."
            scene w2_1595 with dissolve
            kat "Lick it."
            scene w2_1596 with dissolve

            if kat_polite == True:
                "It was a firm, unbending command, but I still took a moment to marvel at the sight of Mrs. Pulman's proffered ass."
            else:
                "It was a firm, unbending command, but I still took a moment to marvel at the sight of Kathleen's proffered ass."

            scene w2_1597 with dissolve
            "It was a strikingly shapely derriere for a woman of her age, well taken care of by exercise and the luxurious trappings of a wealthy lifestyle."
            "A strand of girl cum hung perilously from her vulva, the leftover effect of her previous masturbatory efforts."
            kat "Well, what are you waiting for?"
            "It was like it was staring right back at me, every aroused breath she took giving the impression her asshole was alive."
            scene w2_1598 with dissolve
            "I had never done this before, but slowly, I brought myself to the rim of her anus and did as I was bidden."
            "Thankfully, it tasted like skin and sweat."
            scene w2_1599 with dissolve
            "I used my tongue to circle her hole, like water going down the drain, before finally taking a tentative plunge into her guts."
            kat "Ah...! Good boy."
            scene w2_1598 with dissolve
            "It wasn't as disgusting as I imagined. Honestly, in some ways, it felt no different than cunnilingus. Just a tongue, a hole, and the fervent desire to please..."
            kat "Good, good boy..."
            "Though the situation itself made it feel more degrading."
            scene w2_1600 with dissolve
            kat "Now..."
            scene w2_1601 with dissolve
            kat "..."
            "She didn't have to finish her sentence."
            scene w2_1602 with dissolve
            "I bent over and brought my face to the edge of her boots."
            scene w2_1603 with dissolve
            kat "Ah...! I spend so much time degrading sluts, that I rarely get the pleasure of having a man at my feet."
            kat "It didn't take you much convincing. I know you're not naturally submissive. Are you just that horny?"
            scene w2_1604 with dissolve
            mct "(Why was I doing this? It wasn't just to cum. I could go home and jack off if I really wanted to.)"
            mct "(No... it was because deep down, I thought having her on my side would be an advantage.)"
            mc "You scratch my back, I scratch yours. That's the way of the world."
            scene w2_1605 with dissolve
            kat "Ha! Not a very sexy answer, but I like the challenge."
            scene w2_1606 with dissolve
            kat "It just means I get to ingrain in you the pleasure you can experience if you listen to what I say."
            scene w2_1607 with dissolve
            kat "I'm a big believer in carrot and stick."
            scene black with fade
            kat "Now, lie flat on your back. We're going to fuck."

    kat "No, not the couch. I meant on the {b}floor.{/b}"
    scene w2_1608 with fade
    if kat_polite == True:
        "I did as asked, with Mrs. Pulman lording over and looking down on me like I was cornered prey. The disdain in her eyes, muddled by sexual arousal, gave me goosebumps."
    else:
        "I did as asked, with Kathleen lording over and looking down on me like I was cornered prey. The disdain in her eyes, muddled by sexual arousal, gave me goosebumps."

    scene w2_1609 with dissolve
    if w2KatSexSub == True:
        kat "Good boy. On your back like a whore is a good look for you."
    else:
        kat "I like this more. You look better on your back."

    scene w2_1608 with dissolve
    "Even I had to admit this position had its perks."
    scene w2_1610 with dissolve
    hide screen textbox2 with dissolve
    "I was right between the older woman's legs, with an arousing worm's eye view of her exposed pussy. It was like a deep chasm calling me to take the plunge, but she hovered a calculated distance above my prick."
    scene w2_1611 with dissolve
    kat "Your stupidly oversized tool is standing straight up. Does it want something?"

    if w2KatSexSub == True:
        scene w2_1610 with dissolve
        mct "(...she's going to drag this out isn't she?)"
        scene w2_1611 with dissolve
        kat "All I would have to do for you to taste heaven is lower myself a foot and that monster would be nestled tightly in my dripping, wet cunt."
    else:
        scene w2_1612 with dissolve
        mc "Stop playing around and put it in."
        scene w2_1611 with dissolve
        kat "I could. All I would have to do is lower myself a foot and that monster would be nestled tightly in my dripping, wet cunt."

    scene w2_1612 with dissolve
    mc "What are you waiting for then?"
    scene w2_1611 with dissolve
    kat "I want you to ask me sweetly for it. Something like..."
    kat "Would you, please, PLEASE put it in, Miss Kat?"
    scene w2_1612 with dissolve

    if w2KatSexSub == True:
        mc "Would you please put it in, Miss Kat?"
    else:
        mc "Would you, pretty please with a cherry on top, put it in Miss Kat?"

    scene w2_1611 with dissolve
    kat "Happily."
    scene w2_1613 with dissolve
    "Inch by inch, the gap between us disappeared and her vagina loomed precariously close to my cock."
    mc "Ah...!"
    scene w2_1614 with dissolve
    "The process of entering her was agonizingly slow and deliberate, the mouth of her sex gradually parting as it enveloped the tip of my penis."
    kat "Mmmh... that's the stuff."
    scene w2_1615 with dissolve
    "The further she made it down my length, the more she was spread open."
    kat "God, I love young cock. We don't have enough of it around."
    kat "Beats the hell out of all the old, wrinkly disgustingly discolored dicks of our \"esteemed\" patrons..."
    "With that needlessly colorful description, she finally let gravity do the work."
    $ renpy.music.play("music/thunder.ogg", loop=True, if_changed=True)
    scene w2_1616 with vpunch
    mc "Eeuh--!"
    "She dropped her body weight on me and swallowed my member to the base until it completely disappeared. She was so wet it just slid right in."
    scene w2_1617 with dissolve
    show screen textbox2 with dissolve
    kat "Ghe...! Fuck! You punched my cervix with that stupid thing!"
    scene w2_1618 with dissolve
    mc "It's not my fault if you drop so suddenly."
    scene w2_1619 with dissolve
    kat "I didn't say I hated it, did I?"
    scene w2_1620 with dissolve
    "She dug a sharp nail across my chest as she spoke."
    scene w2_1619 with dissolve
    kat "Heh, if Felicia wins, maybe I'll have to look into finally hiring a man whore..."
    scene w2_1620 with dissolve

    if kat_polite == True:
        "Mrs. Pulman showed no intention of moving, instead she seemed to be enjoying the arduous pace."
    else:
        "Kathleen showed no intention of moving, instead she seemed to be enjoying the arduous pace."

    "And while it did feel good to have the entire length of my cock sheathed in the older woman, after the session with Harper and all the teasing, my body wanted unrelenting ball-slapping sex."
    hide screen textbox2 with dissolve

    menu:
        "Try to verbally goad her into moving":

            if w2KatSexSub == True:
                show screen textbox2 with dissolve
                mc "I'm about to lose my mind here. Could you please move?"
                "In an attempt to appeal to her ego, I did my best to sound as plaintive and desperate as possible. It felt like a small price to get the action started."
                scene w2_1621 with dissolve
                kat "Hmm..."
                "She looked down at me with a smug, satisfied look."
                scene w2_1619 with dissolve
                kat "Okay."
            else:


                show screen textbox2 with dissolve
                mc "What are you drawing this out for? You're hornier than I am."
                scene w2_1619 with dissolve
                kat "There is value in delayed satisfaction. You should learn that."
                kat "I mean, how did my little present feel tonight after finally indulging that side of yourself?"
                scene w2_1620 with dissolve
                mc "...c'mon, I'm about to lose my mind here."
                scene w2_1619 with dissolve
                kat "Ah, those needy eyes..."

            scene katpov1_a with dissolve
            show katpov1 with dissolve
            mc "-gh!"
            "With a burst of fervor, she conceded to my request, prying herself off my cock and lowering herself back down in a smooth, methodical motion."
        "Try to physically goad her into moving.":



            if w2KatSexSub == True:
                show screen textbox2 with dissolve
                "She was hornier than I was, I was sure of that. Without saying a word, I gently rocked my hips as best I could from the position I was in. "
                scene w2_1622 with dissolve
                kat "Nnhe, e-eager, aren't you?"
                "With only a limited range of motion, it was more like I was tickling her inner walls, but it seemed to do the trick."
                scene w2_1621 with dissolve
                "Her smug, satisfied look showed cracks of pleasure and small murmurs of sexual contentment escaped from her lips."
                scene w2_1619 with dissolve
                kat "Ah, no point in dragging this out. You've been a good boy tonight."
                scene katpov1_a with dissolve
                show katpov1 with dissolve
                mc "-gh!"
                "With a burst of fervor, she conceded to my request, prying herself off my cock and lowering herself back down in a smooth, methodical motion."
            else:

                show screen textbox2 with dissolve
                "She was hornier than I was, I was sure of that. Without saying a word, I gently rocked my hips as best I could from the position I was in. "
                scene w2_1622 with dissolve
                kat "Nnhe, e-eager, aren't you?"
                "With only a limited range of motion, it was more like I was tickling her inner walls, so I decided to tack on a different approach."
                scene w2_1623 with dissolve
                play sound "sound effects/slap2.wav"
                scene w2_1624 with vpunch
                "*Smack!*"
                kat "Ah!"
                "The unexpected swat set Kat's hips into motion, as she easily slid up and down my cock at an erratic pace."
                scene w2_1625 with dissolve
                kat "Ah, r-real fucking cheeky..."
                scene katpov1_a with dissolve
                show katpov1 with dissolve
                "The flustered, clumsy dick riding unfortunately didn't last long. She soon regained her composure and adjusted her approach to a more smooth, methodical pace."

    kat "Mmm...! That's the ticket..."
    kat "Watching you have fun with Harper... that really turned me on. I know you enjoyed it, my fledgling sadist."
    mc "You mean you -ah!- y-you get off on watching people dance to your tune."
    kat "Yes! You understand! Every man and woman has a song they'll dance to."
    kat "That's OUR business, [mcf]."
    kat "Ah-! Mmmh...! Did I mention how much I love young dick? It's so goddamn stiff! Grab my tits!"
    scene w2_1626 with dissolve
    "It amazed me just how quickly she traded her façade of control for unrepentant sexual zeal."
    kat "Material wealth, position, love, family, spirituality... even the most religious ascetic has SOMETHING that can be exploited."
    scene katride1_a with dissolve
    show katride1 with dissolve
    kat "For example, Veronica and Rosalind... what do you think it was for them?"
    mc "Ah-! M-money, obviously..."
    scene katride1b_a with dissolve
    show katride1b with dissolve
    kat "Wrong! That's just the remedy for what ails them. If you want to have a full handle on the Carnations, now and in the years to come, you should understand what drives them."
    "Part of me marveled at her ability to launch into a twisted, bullshit diatribe while bouncing on a dick. A larger part of me just focused on the tits in my face"
    kat "I'll spell it out for you this time. Veronica's pitfall is that she's a prideful woman, afraid of failure. Rather than let her business go, she's willing to go to extreme lengths."
    kat "What would you guess for Rosalind?"
    mc "Ah...!"
    "Meanwhile, it was hard to think with the building pleasure in my dick."
    mc "F-family?"
    scene katride1_a with dissolve
    show katride1 with dissolve
    kat "Yes. That was an easy one. Now, Felicia... she's a bit tougher to crack."
    kat "You might assume what drives her is her appetite, but I believe the reality is something far less slippery to control."
    mc "What is it?"
    kat "I'm n-not going, -ah!- to give you all the answers. I'll let you figure that one out for yourself."
    "Thankfully, the conversation receded into the dirty sounds of copulation and I could fully focus on enjoying the moment."
    "On the pleasurable sensation of the older woman rising and falling in quick succession."
    scene katpov1_a with dissolve
    show katpov1 with dissolve
    mc "You're... r-really good at this."
    kat "Of course I am. Don't insult me, [mcf]."
    "Up and down like clockwork, at the same vigorously persistent tempo... it was like she was efficiently milking me for my seed."
    kat "That look on your face. Does my pussy feel that good?"
    mc "Yeah, it does."
    show katride1c with w19

    if kat_polite == True:
        "I had no problem admitting it, and the admission had the added effect of putting just an ounce more pep in Mrs. Pulman's wantonly bouncing ass."
    else:
        "I had no problem admitting it, and the admission had the added effect of putting just an ounce more pep in Kathleen's wantonly bouncing ass."

    kat "Mmh... it's not like I couldn't tell, but it's nice to hear."
    "Up and down like clockwork..."
    scene w2_1627 with wipeleft
    harp "Ghh..."
    kat "Do you like seeing a woman my age shake her ass like a whore?"
    mc "Y-yeah, I do."
    kat "Ohoho, what a perverted rat you are."
    scene katride2_a with dissolve
    show katride2 with dissolve
    mc "Ghk!"

    if kat_polite == True:
        "Mrs. Pulman roughly grabbed ahold of my throat, sinking the tips of her nails into the tender flesh of my neck, and looked down on me with a sinister gaze."
    else:
        "Kathleen roughly grabbed ahold of my throat, sinking the tips of her nails into the tender flesh of my neck, and looked down on me with a sinister gaze."

    kat "I just bet you want to show me just how much of a whore I am."
    "Her grip tightened, not enough for me to be unable to breathe, but enough to stir an urgent, primal feeling in me."
    kat "Mmmh...!"
    "The tempo of her shaking hips increased."
    scene katpov2_a with dissolve
    show katpov2 with dissolve
    kat "I bet you want to treat me like you did Felicia last Saturday night."
    kat "Mmmh...! What's the matter? Why aren't you saying anything?"
    "She moved more and more erratically."

    if w2KatSexSub == True:
        kat "Ah, but you don't have it in you, do you?"
        kat "You so quickly got down on your knees and kissed my boot like a good mutt."
    else:

        kat "You said you were a man, but you don't have it in you, do you?"
        kat "That was all just worthless, bullshit machismo."

    scene katride2_a with dissolve
    show katride2 with dissolve
    mct "(Is she...)"
    kat "You're just going to lie there and let me fuck you like a bitch, aren't you?"
    mct "(...trying to provoke me? Is this another one of her tests?)"
    "Who the hell knows. I just want to..."
    hide screen textbox2 with dissolve

    menu:
        "Just sit back and enjoy the ride.":

            $ w2KatTop = True
            show screen textbox2 with dissolve
            if w2KatSexSub == True:
                "...lie back and enjoy the feeling of having the older woman ride me."
            else:
                "...let the horny bitch ride me until I cum."
            jump w2KatSexTop
        "Turn things around (literally) and take the lead.":


            $ w2KatBottom = True
            show screen textbox2 with dissolve
            "...fuck, not listen to her drone on and on."
            jump w2KatSexBottom


label w2KatSexTop:

    scene w2_1629 with dissolve
    mc "..."
    "I averted my gaze, to signal my lack of interest in continuing her bullshit game. Either way, I'm being led on her leash."
    scene w2_1630 with dissolve
    kat "Ah..."
    "In a fleeting glimpse of softness, her lips furled into a confusingly tender smile."
    kat "Very well."
    scene katride3_a with dissolve
    show katride3
    $ renpy.music.set_volume(1, 0, channel = "ambient")
    play ambient "sound effects/boobjob.wav"
    mc "Eh-!"

    if kat_polite == True:
        "What followed next was a blur of unrestrained fornicating, as Mrs. Pulman forcibly pushed me backwards into the plush leather mat."
    else:
        "What followed next was a blur of unrestrained fornicating, as Kathleen forcibly pushed me backwards into the plush leather mat."

    "She used her hands not only to firmly hold me into place, but to gain better leverage as she truly and properly began to {i}fuck me{/i} into the dirt."
    mc "Ngh, d-damn!"
    "*SMACK* *SCHLICK* *THWIP*"
    "Her hips picked up speed, rapidly increasing in tempo until the sound of her naked ass crashing into my thighs resembled more of a taiko drum than human intercourse."
    "*SHLICK* *SHLICK* *SHLICK*"
    scene katride3b_a with dissolve
    show katride3b
    "It was like I wasn't even there. She had tossed her head back and retreated into the sensation of riding dick."

    if kat_polite == True:
        "For once, in her laxed expression, Mrs. Pulman looked utterly detached from the cruelty of this place and reminded me of an actual person."
    else:
        "For once, in her laxed expression, Kathleen looked utterly detached from the cruelty of this place and reminded me of an actual person."

    "I wanted to reach up and stroke her face, but I dared not break the illusion. Instead, I enjoyed the dizzying view of the older woman's breasts bouncing as she hurled herself toward sexual gratification."
    "A minute passed, and at this speed, I had little hope; An oh so familiar sensation was about to hit its crescendo."
    mc "Ng, ah-- I'm about to cum!"
    kat "I know. Don't worry, you can do it inside me. One of the perks of fucking an older woman."
    mc "Mmh...! O-okay!"
    mc "Ah-"
    play sound "sound effects/spurt.wav"
    scene w2_1631 with flash
    play sound "sound effects/spurt.wav"
    with flash
    mc "Aaaah!"
    "With how deep I was fucking her, I must have hit a bullseye on her uterus."
    kat "Ah, hahaha...! I love that warm feeling creeping into my stomach. You had a lot for me, mutt."
    scene katride3_a with dissolve
    show katride3
    "*SMACK* *SCHLICK* *THWIP*"
    "...and not for a second did she slow down."
    mc "Ngh...!"
    "*SHLICK* *SHLICK* *SHLICK*"
    scene katride3c_a with dissolve
    show katride3c
    "She continued to violently rock her hips into mine, rubbing the post-orgasm, overwrought nerves of my penis against the slippery inner walls of her cunt."
    "It wasn't exactly painful, but it was {b}intense{/b}. As soon as I had tasted sweet release, without a moment's rest, I was ensnared once more by the feeling of building pleasure."
    kat "That's a {b}lovely{/b} expression you're wearing. Like the pitiful look of a virgin bride on her wedding night, ah~! Oh! Marvelous!"
    "With the way the older woman's quim greedily kissed and sucked at my prick, I didn't even have the chance to go soft."
    scene katride3b_a with dissolve
    show katride3b
    kat "You're still so fucking hard! I love it!"
    mc "Uhhh...! Fuck!"
    "The added sensitivity from just cumming, the growing physical strain... as the minutes passed, so did these."
    scene katride3_a with dissolve
    show katride3
    "*SMACK* *SCHLICK* *THWIP*"

    if kat_polite == True:
        "My hips were aching from Mrs. Pulman's weight battering down on me as she violently mashed our crotches together."
    else:
        "My hips were aching from Kathleen's weight battering down on me as she violently mashed our crotches together."

    "*SHLICK* *SHLICK* *SHLICK*"
    mct "(What's with this woman...?)"
    "We hadn't been fucking for long, but I'm getting unusually sore."
    kat "Mmmh...♥"
    scene katride3c_a with dissolve
    show katride3c
    "*SMACK* *SCHLICK* *THWIP*"
    kat "You're almost there. Just how many times are you going to cum for me?"
    mct "(Huh? She was right, but what's more...)"
    "She had even realized it before I had myself."
    mct "(How the hell can she do that?)"
    "An itch once more crept from my scrotum to my shaft, as my body prepared for yet another release."
    "*SHLICK* *SHLICK* *SHLICK*"
    scene katride3b_a with dissolve
    show katride3b
    kat "Ha... ha... ha...!"

    if kat_polite == True:
        "Mrs. Pulman was beginning to look a little ragged herself, sweat matting her bangs and rolling down the side of her cheek. The methodical rhythm of her bucking hips, which you could've previously set your watch to, grew more erratic and less precise."
    else:
        "Kathleen. was beginning to look a little ragged herself, sweat matting her bangs and rolling down the side of her cheek. The methodical rhythm of her bucking hips, which you could've previously set your watch to, grew more erratic and less precise."

    kat "Ha... ah, ha... ha...! Yes!"
    "She dug her nails sharply into my chest. It stung, but in the face of my swelling need, I wasn't in a position to actually care."
    kat "Ah, aaaah! Let me have it, [mcf]."
    kat "Plaster my cunt with your seed!"
    mc "S-shit...!"
    "The look she gave me was the tipping point. With sex-filled, piercing eyes she had pushed me over the edge."
    mc "Ng...!"
    stop ambient
    play sound "sound effects/spurt.wav"
    scene w2_1632 with flash
    play sound "sound effects/spurt.wav"
    with flash
    kat "Ghe..!"
    "Like last time, I released a deluge of semen inside of the cruel woman, the moment of which set her off and had her shrieking like a banshee."
    scene w2_1633 with dissolve
    kat "Aaaaaaah, gh...! Ghe....!"
    scene w2_1634 with vpunch
    kat "Nyeeeeee!"
    "Her quim had my dick in a strangle hold, clamping down hard and refusing to give up its prize until every last drop of precious seed had been squeezed out and deposited."
    mct "(H-huh? I'm still...?)"
    play sound "sound effects/spurt.wav"
    scene w2_1635 with flash
    play sound "sound effects/spurt.wav"
    with flash
    mc "Ahh, ngh!"
    "Her set of nails dug deeper and deeper into the flesh of my chest, strong enough to know even in the mind-melting pleasure, it was going to leave a mark..."
    scene w2_1636 with vpunch
    kat "Ghe, y-yes! Ah! Eughgggh!"

    if kat_polite == True:
        "Mrs. Pulman wasn't done either, as an encore of animalistic moans followed a second orgasm in quick succession of the first."
    else:
        "Kathleen wasn't done either, as an encore of animalistic moans followed a second orgasm in quick succession of the first."
    stop music fadeout 3.0
    scene w2_1637 with dissolve
    kat "Ah..."
    "........."
    "......"
    scene w2_1638 with dissolve
    kat "..."
    scene w2_1639 with dissolve
    kat "That was fun. I needed that..."
    "We fucked for less than ten minutes, but I felt like I had gone for an hour. Every muscle in my body felt sore."
    mct "(She's fucking crazy...)"

    if kat_polite == True:
        "Mrs. Pulman contentedly purred into my chest like a pussy cat, but of course it would be unwise to forget..."
    else:
        "Kathleen contentedly purred into my chest like a pussy cat, but of course it would be unwise to forget..."

    scene w2_1640 with dissolve
    "She was a woman-devouring tiger."
    mc "Uh, we should probably get Harper down. It's not good to be upside down that long..."
    scene black with fade

    if not persistent.w2KatSceneGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w2KatSceneGallery = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)

    "......"
    "..."
    $ renpy.end_replay()
    jump w2June08End



label w2KatSexBottom:

    "For a moment I hesitated, but..."
    scene w2_1641 with dissolve
    kat "Oh-!"
    scene w2_1642 with dissolve
    kat "Oof!"
    mct "(She did basically tell me to do it.)"
    scene w2_1643 with fade
    mc "If you wanted to switch positions..."
    scene w2_1644 with fade
    mc "You could've just asked like a normal person."
    scene w2_1645 with hpunch
    kat "Ggh-!"

    if kat_polite == True:
        "To emphasis my point, I slammed my hips forward all at once, burying the full length of my cock back into Mrs. Pulman's swollen sex."
    else:
        "To emphasis my point, I slammed my hips forward all at once, burying the full length of my cock back into Kathleen's swollen sex."

    scene w2_1646 with dissolve
    kat "Ah, hahaha...! Excellent."
    kat "Now {b}fuck me{/b}, [mcf]."
    scene w2_1647 with dissolve
    "The older woman got the jump on me, shaking her ass and grinding violently into my crotch."
    mc "Ah...!"
    "Even without me moving it felt amazing, what with the way her quim sucked, kissed, and massaged my glans."
    "It probably wouldn't take me long to get off from just this, which is why..."
    hide screen textbox2 with dissolve
    scene katstand1_a with dissolve
    $ renpy.music.set_volume(1, 0, channel = "ambient")
    play ambient "sound effects/boobjob.wav"
    show katstand1
    kat "O-oh!"
    "I was going to be the one to dictate the pace."

    if kat_polite == True:
        "Using Mrs. Pulman's arms for leverage, I repeatedly jackhammered my hips home again and again."
    else:
        "Using Kathleen's arms for leverage, I repeatedly jackhammered my hips home again and again."

    "*Plop!* *Plap!* *Smack!*"
    "Every piston was punctuated by a pleasant smacking sound, as the fat on the older woman's shapely ass careened into my crotch at a rapid pace."
    "Plap!* *Plap!* *Plop!*"
    kat "Mmmh...! Hehehe, yes!"
    kat "Don't hold back, you mutt. Fuck me like an animal."

    if kat_polite == True:
        "Even in this position, it felt like Mrs. Pulman had me on a leash."
    else:
        "Even in this position, it felt like Kathleen had me on a leash."

    "Not like I cared though, my mind was too wrapped up in copulation to give a damn about that sort of thing."
    scene katstand2_a with dissolve
    show katstand2
    "Instead, I focused on what was in front of me."
    "The way the older woman's back arched as I tugged at her arms."
    "The steady rhythm of her sliding on and off my dick."
    "The cloying heat of her quim, as her inner walls stuck and tugged at the flesh of my penis, trying to prevent its escape."
    "The way sweat formed on the nape of Mrs. Pulman's neck, pooling until its weight funneled down her back."
    mc "Ah... ha...! This..."
    "*Plop!* *Plap!* *Smack!*"
    mc "This good enough for you, {b}Mrs. Pulman{/b}?"
    kat "Ng-! No, I need more!"
    mct "(More? I don't know how much harder I can go.)"
    scene katstand3_a with dissolve
    show katstand3
    mct "(Ah, fuck it!)"
    "*PLAP!* *PLAP!* *PLOP!*"
    "I purged any and all concern from my head for either of our physical comforts, gripping the older woman's wrists as tight as I could - hard enough to bleach her hands white - and pulled her into me with as much force as I could muster."
    "My lower half did the same, heaving forward so fast that every time our skin kissed, it actually stung."
    kat "Ah...♥ That's more like it!"
    "The harder I thrusted, the fewer thoughts occupied my head until it was just a word soup of vulgarity."
    mct "(Damn bitch...! Fucking slut...! ...Shit!)"
    mc "Ah...!"
    "I was basically in a state of rut."
    "*SMACK!* *PLOP!* *PLAP!*"
    scene katstand4_a with dissolve
    show katstand4
    kat "Ghh, yes...! That's more like it!"
    "It didn't take long for the ache in my calves to spread up to my thighs."
    "*PLAP!* *PLAP!* *PLOP!*"
    kat "Uggeee!"
    "Soon, it felt like my whole lower half would go numb."
    kat "Ah, haa...! Y-you're about to cum, aren't you?"
    mct "(W-what?)"
    "Like an old country shepherd predicting the weather, she had even realized it before I had."
    mct "(How the hell can she do that?)"
    kat "Do it inside!"
    kat "O-One, -ah!- of the perks of fucking an older woman!"
    mc "Right!"
    scene katstand5_a with dissolve
    show katstand5
    "Letting go of her arms, I grabbed the back of the babbling woman's head and hurled myself into the final stretch."
    kat "Ghh-! Ah...! Ha...! Ha...!"
    "Her legs buckled, but thankfully she didn't fall flat on her face."
    kat "Ehe... haha... ng...!"
    "There was a perverse joy in hearing the overly talkative woman lose the ability to form syllables into words."
    kat "Ghhhheeee!"
    "--not that I was presently in any state to speak."
    kat "Ah, oh... oh..."
    scene w2_1648 with vpunch
    kat "Ngh...aaAaaah!"
    "Her snatch clamped down {i}hard{/i} and a series of even more incoherent shrieking pierced my ears."
    kat "Ghh... gh! Ah...♥" with vpunch
    scene katstand6_a with dissolve
    show katstand6
    kat "Ghh... gh...!"
    "She had reached her peak and I wasn't too far behind."
    mc "Ah...!"
    mc "Ah, ah...!"
    scene white with fade
    mc "Ah, ah, ah...!"
    play sound "sound effects/spurt.wav"
    "--!"
    scene katstand7_a with dissolve
    show katstand7
    mc "F-fuck...!"
    play sound "sound effects/spurt.wav"
    with flash
    "Semen flooded the older woman's uterus."
    play sound "sound effects/spurt.wav"
    with flash
    "Even as I was cumming, my hips never stopped moving. It was like they had a mind of their own."
    play sound "sound effects/spurt.wav"
    with flash
    "Every thrust packed her with more and more of my cum."
    mc "Gh...!"
    play sound "sound effects/spurt.wav"
    with flash
    "Rope after rope..."
    play sound "sound effects/spurt.wav"
    scene w2_1648 with flash
    kat "Ngh, ah! Yeeeeeeees!"

    if kat_polite == True:
        "Mrs. Pulman wasn't done either, as an encore of animalistic moans followed a second orgasm in quick succession of the first."
    else:
        "Kathleen wasn't done either, as an encore of animalistic moans followed a second orgasm in quick succession of the first."

    scene katstand7_a with dissolve
    show katstand7
    "Rope after rope..."
    "I could feel my sanity slowly come back to me, and with it, I quickly became aware of one inescapable truth."
    mc "Ha... ha... ha..."
    "My entire body was in pain."
    stop ambient
    stop music
    scene w2_1649 with dissolve
    mc "Ha....ha...haaaa!"
    play sound "sound effects/thud-floor.mp3"
    scene w2_1650 with fade
    kat "Euggh.... ha..."
    "The room had went from the sound of enthusiastic fornication to tired wheezing at a drop of a hat."
    scene w2_1651 with dissolve
    kat "I needed that..."
    kat "Good job, [mcf]."
    scene w2_1650 with dissolve
    "We fucked for less than ten minutes, but I felt like I had went for an hour. Every muscle in my body was on fire."
    mct "(She's fucking crazy...)"

    if kat_polite == True:
        "Mrs. Pulman contentedly purred like a pussy cat, but of course it would be unwise to forget..."
    else:
        "Kathleen contentedly purred like a pussy cat, but of course it would be unwise to forget..."

    scene w2_1640 with dissolve
    "She was a woman-devouring tiger."
    mc "Uh, we should probably get Harper down. It's not good to be upside down that long..."
    scene black with fade
    if not persistent.w2KatSceneGallery:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w2KatSceneGallery = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)

    "......"
    "..."
    $ renpy.end_replay()
    jump w2June08End

label w2KatGiftDecline:
    stop music
    scene w2_1652 with dissolve
    mc "Thank you for the gift, but I respectfully decline."
    scene w2_1653 with dissolve
    play music "music/george-street-shuffle.ogg"
    kat "Is that so?"
    scene w2_1654 with dissolve
    mc "I don't feel comfortable with any of this."
    scene w2_1655 with dissolve
    kat "It's not good to deny yourself, [mcf]... but it is only a {b}gift{/b} after all, you're within your right to refuse."
    kat "Would you mind helping me get Harper down, then?"
    scene w2_1656 with dissolve
    mc "Yeah, of course."
    scene black with fade
    mct "(Yeeesh, how over-engineered is this contraption?)"
    kat "Watch your hands, don't get it caught in the pulley."
    "..."
    scene w2_1657 with fade
    harp "Coming down is my least favorite part."
    scene w2_1658 with dissolve
    kat "I'm going to go get changed. I'll give you a ride back to your apartment. I have business I need to discuss."
    scene w2_1659 with dissolve
    kat "Sorry for dragging you down here for nothing."
    harp "..."
    scene w2_1660 with dissolve
    mc "Uh... is she mad?"
    harp "Oh, yeah. Seething mad."
    scene w2_1661 with dissolve
    harp "She's not used to being told no and on top of it all you ruined her fun for the evening."
    scene w2_1662 with dissolve
    mc "Her fun...?"
    scene w2_1663 with dissolve
    harp "How to put it, uh...."
    scene w2_1661 with dissolve
    harp "She's really fucking horny."
    scene w2_1662 with dissolve
    mc "...?"
    scene w2_1664 with dissolve
    harp "You see... the summer exhibition gets her going, but she can't do anything about it for appearance's sake."
    harp "She thinks the old, dead fucks of the club would take her less seriously. Truth be told, half of them don't see her as an equal to begin with..."
    scene w2_1662 with dissolve
    mc "So the birthday \"gift\" thing was just a pretense for her to blow off steam?"
    scene w2_1665 with dissolve
    harp "You got it, chief."
    scene w2_1666 with dissolve
    harp "Why did you turn down the offer, by the way? You looked... tempted. I'm skilled at telling that sort of thing."
    harp "I would've made it fun for you. A lot of groaning and squeeling. I'm pretty good, y'know?"
    harp "Am I not your type?"
    scene w2_1667 with dissolve
    mc "Oh, come on. That's not it. It's just..."
    scene w2_1668 with dissolve
    harp "Ah, I'm just kidding 'ya. I get it."
    harp "I really, {b}really{/b} do."
    scene w2_1669 with dissolve
    harp "Who wants someone telling them what to do if they can help it?"
    harp "Guess I have the rest of the night off."
    scene w2_1670 with dissolve
    harp "Oh, by the way..."
    scene w2_1671 with dissolve
    harp "Maybe we'll call tonight a \"rain check\". How does that sound?"
    scene w2_1672 with dissolve
    "Without waiting for my answer, Harper left me alone in the unimaginatively named \"obsidian room\". It occurred to me..."
    "This was the most I'd ever heard her speak."
    scene w2_1673 with dissolve
    mc "*sigh* Ha..."
    mc "Maybe tonight wasn't such a waste of time."
    scene black with fade
    stop music fadeout 3.0
    "......"
    "..."
    jump w2June08End

label w2HarperSoloEnding:

    scene w2_1674 with dissolve
    kat "That was quite the show. I can see how much you enjoyed it."
    mc "You seemed to get as much out of it as I did..."
    play music "music/george-street-shuffle.ogg"
    scene w2_1675 with dissolve
    kat "I did."
    kat "It's just a shame we have to end it here."
    scene w2_1676 with dissolve
    mc "A-ah...!"
    scene w2_1675 with dissolve
    kat "We have some business to discuss and then I need to be some place."
    scene w2_1677 with dissolve
    mc "Business?"
    scene w2_1675 with dissolve
    kat "I'll tell you about it on the ride back to your apartment. Would you please help me get Harper down?"
    scene w2_1677 with dissolve
    mc "Yeah, of course..."
    scene black with fade
    mct "(Yeeesh, how over-engineered is this contraption?)"
    kat "Watch your hands, don't get it caught in the pulley."
    "..."
    scene w2_1657 with dissolve
    harp "Coming down is my least favorite part."
    scene w2_1658 with dissolve
    kat "I'm going to go get changed. I'll meet you at the bar."
    scene w2_1659 with dissolve
    kat "Oh, and happy belated birthday, [mcf]."
    harp "..."
    scene w2_1660 with dissolve
    harp "I'm surprised it stopped there."
    mc "What do you mean?"
    scene w2_1679 with dissolve
    harp "These private sort of deals, she's usually not satisfied just watching."
    scene w2_1680 with dissolve
    harp "You see... the summer exhibition gets her going, but she can't do anything about it for appearance's sake."
    scene w2_1679 with dissolve
    harp "She thinks the old, dead fucks of the club would take her less seriously. Truth be told, half of them don't see her as an equal to begin with..."
    scene w2_1678 with dissolve
    mc "It's hard to muster any sympathy for that."
    scene w2_1681 with dissolve
    harp "Ha, tell me about it."
    scene w2_1678 with dissolve
    mc "...uh, are you okay by the way? I hope I didn't..."
    scene w2_1680 with dissolve
    harp "I sound fine don't I? Legs are just a lil' shaky is all."
    scene w2_1669 with dissolve
    harp "Being strung up like that fucks up your sense of balance."
    scene w2_1671 with dissolve
    harp "Thanks for being so concerned though."
    scene w2_1672 with dissolve
    "With that, she left me alone and horny in the unimaginatively named \"obsidian room\"."
    scene w2_1682 with dissolve
    mc "*sigh* Ha..."
    mc "I've never been this frustrated before."
    scene black with fade
    stop music fadeout 3.0
    "......"
    "..."

label w2June08End:

    play sound "sound effects/car.wav"
    play ambient "sound effects/city-night.wav"
    scene w2_1683 with circlewipe

    if w2KatSex == True:
        if kat_polite == True:
            "After helping Harper down from her restraints, Mrs. Pulman didn't so much {i}offer{/i} to take me home as much as she {b}told{/b} me that was what she was going to do."
        else:
            "After helping Harper down from her restraints, Kathleen didn't so much {i}offer{/i} to take me home as much as she {b}told{/b} me that was what she was going to do."

        $ history_kathleen = "I was pulled into a steamy night of debauchery under the pretense of it being my birthday, where I momentarily let my true colors show and then fucked like a jackrabbit."
        $ unread_kathleen = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve

        "Apparently, she had more in mind than just fun tonight. She had actual \"business\" to discuss. She hadn't gotten to it yet, though."
        play music "music/night-on-the-docks-sax.ogg"
        stop ambient fadeout 2.0
        scene w2_1684 with dissolve
        "Instead, we had just been sitting in silence for some time now, a curious smile on her lips while I marveled at how unaffected she seemed from our earlier strenuous activity."

        if kat_polite == True:
            "I felt, looked, and smelled like utter shit, but Mrs. Pulman was {b}glowing{/b}. Like she had just woken up from a refreshing midday nap."
        else:
            "I felt, looked, and smelled like utter shit, but Kathleen was {b}glowing{/b}. Like she had just woken up from a refreshing midday nap."

        mct "(I'm severely outclassed here.)"
        scene w2_1685 with dissolve
        kat "Thank you for the entertainment tonight, [mcf]. That was at the very least, informative."
        "Finally, she saw fit to move onto some conversation."
        scene w2_1686 with dissolve
        kat "Not to mention, pleasurable."
        scene w2_1687 with dissolve
        mc "Yeah, that was... something."
        scene w2_1688 with dissolve
        kat "Ahaha...!"
        scene w2_1689 with dissolve
        kat "Ah, but we should discuss the \"extracurricular\" activities you and the Carnations will be partaking in this week."

    elif w2HarperSolo == True:

        if kat_polite == True:
            "After waiting for Mrs. Pulman to get dressed, she made good on her word of taking me home and I found myself in the back of her limousine."
        else:
            "After waiting for Kathleen to get dressed, she made good on her word of taking me home and I found myself in the back of her limousine."


        $ history_kathleen = "I was pulled into a flight of sadism under the pretense of it being my birthday. Unfortunately, we stopped short of reaching any sort of grand finale."
        $ unread_kathleen = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve

        "The more pressing part of her promise, of discussing actual \"business\" was still up in the air."
        scene w2_1690 with dissolve
        "Instead, we had just been sitting here for some time now, with the older woman wearing a contemplative smile and raking me over the coals with the silence."
        "I thought back to what Harper had said, about her being frustrated, but that wasn't really my problem."
        scene w2_1691 with dissolve
        mc "Ah, so..."
        "I decided to be the one to break the silence and to broach the reason for why we were sharing a ride."
        scene w2_1692 with dissolve
        mc "You mentioned you had something to talk to me about?"
        scene w2_1689 with dissolve
        kat "That's right."
        kat "We should discuss the \"extracurricular\" activities you and the Carnations will be partaking in this week."
    else:




        if kat_polite == True:
            "After waiting for Mrs. Pulman to get dressed, she made good on her word of taking me home and I found myself in the back of her limousine."
        else:
            "After waiting for Kathleen to get dressed, she made good on her word of taking me home and I found myself in the back of her limousine."

        $ history_kathleen = "Mrs. Pulman tried to entice me into a night of debauchery under the pretense of my birthday, but it felt good not to let her pull the strings for once."
        $ unread_kathleen = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve

        "The more pressing part of her promise, of discussing actual \"business\" was still up in the air."
        scene w2_1717 with dissolve
        "Instead, we had just been sitting here for some time now, with the older woman wearing a painfully neutral expression and killing me with the silence."
        "I thought back to what Harper had said, about her being angry about being denied, but I didn't regret my decision to not dance on strings for her amusement."
        scene w2_1691 with dissolve
        mc "Ah, so..."
        "I decided to be the one to break the silence and to broach the reason for why we were sharing a ride."
        scene w2_1692 with dissolve
        mc "You mentioned you had something to talk to me about?"
        scene w2_1689 with dissolve
        kat "That's right."
        kat "We should discuss the \"extracurricular\" activities you and the Carnations will be partaking in this week."


    scene w2_1692 with dissolve
    "She was talking about what she had alluded to a number of times during the photoshoot and the whole reason I now had a camera in my possession."
    mc "What am I going to have to do?"
    "The vast number of twisted possibilities made me uneasy, so I was direct with my words."
    scene w2_1693 with dissolve
    kat "How do you feel about having sex in risky places?"
    scene w2_1694 with dissolve
    mc "{b}Uncomfortable{/b}."
    scene w2_1693 with dissolve
    kat "I hope you'll come around on the idea, because you'll be tasked with getting some candid snapshots of our girls this week."
    kat "How far you take it will be up to your discretion, but do get some good ones for our patrons, will you?"
    scene w2_1694 with dissolve
    mc "Could you explain a little more about what I'm supposed to do?"
    "No point in fussing about it until I've heard the full details."
    scene w2_1689 with dissolve
    kat "You'll have a session with each of the Carnations this week in a designated spot. Once there, I want you to get some compromising photos of them."
    scene w2_1692 with dissolve
    mc "Designated spots...?"
    scene w2_1695 with dissolve
    kat "Ah, ha! You see, that is where things get fun for you and our members. Each location has been carefully considered and chosen for each woman's maximum embarrassment."
    kat "For Rosalind, you'll be snagging some photos of her at a park nearby her home. Research tells me that it's a pretty popular place for the neighborhood moms to gather after they send their brats off to school."
    kat "The chances of her running into someone she knows should be pretty high. Have her wear something... slutty."
    scene w2_1696 with dissolve
    mc "Isn't that going too far?"
    kat "You're just full of funny questions."
    mc "Okay, so what about Veronica?"
    scene w2_1697 with dissolve
    kat "For Veronica, I want you to make that bitch squirm by getting photos of her at her gym. As I understand it, despite her financial troubles, her gym sees its own share of foot traffic."
    kat "The potential of getting caught by one of her customers... hmmm yes, her gym should be the perfect place for the shoot."
    scene w2_1692 with dissolve
    mc "And Felicia?"
    scene w2_1698 with dissolve
    kat "That's the best one! Our patrons are going to LOVE this. Tell me, have you ever conducted an interview before?"
    scene w2_1699 with dissolve
    mc "Once for a paper for college."
    mc "...and I guess when you had me make that video last week."
    kat "Ah, that's right!"
    mc "Who am I going to be interviewing?"
    "I wanted to cut to the heart of her question."
    kat "{b}Elias Ford{/b}."
    scene w2_1700 with cmet
    mc "Eh-?!"
    scene w2_1701 with dissolve
    kat "I pulled some strings and got in touch with him through a mutual acquaintance. He's agreed to sit down for a puff piece for a magazine."
    scene w2_1718 with pixellate
    mc "You want me to meet with and interview Felicia's husband?!"
    kat "That's right. Conduct an interview with him, in his home, and try to find some time to bend his wife over their family dinner table."
    scene w2_1702 with pixellate
    mc "I can't do that."
    kat "I'm not asking you to build a rocket that'll take you to Mars, [mcf]. You can certainly interview an old stiff and snag some dirty photos of his wife."
    scene w2_1692 with dissolve
    mc "Does Felicia know about your plan? I don't think she'll be cool with that."
    scene w2_1689 with dissolve
    kat "If she's not, you better convince her."
    kat "That is part of your job, after all."
    scene w2_1692 with dissolve
    mc "What about the article? Wouldn't he find it funny if there wasn't an actual article printed?"
    scene w2_1689 with dissolve
    kat "Oh, it's a real interview. I have a friend who owns a number of publications."
    kat "You won't have to write it though, it's just an excuse to get you in the door. Just take notes and they'll find their way into the hands of someone who will."
    scene w2_1694 with dissolve
    mc "I, ah..."
    "I was at a complete loss of words. Taking dirty photos of Rosalind at the park was worrying enough, but meeting Felicia's husband went beyond anxiety and ventured into nefariousness."
    scene w2_1693 with dissolve
    kat "Don't worry, you'll come around on it. You really shined on stage last week. You had no problem whatsoever performing in front of our patrons, did you?"
    kat "You're capable of a lot more than you give yourself credit for."
    scene w2_1703 with dissolve
    mc "Those would be inspirational words if the situation wasn't so fucked up."
    scene w2_1704 with dissolve
    kat "Ah, haha! You make me laugh, [mcf]."
    scene w2_1705 with dissolve
    mc "...you did say the content of the shoot is to my discretion?"
    scene w2_1706 with dissolve
    kat "That's right."
    "It may be small, but having control of how far things went was a consolation."
    scene w2_1703 with dissolve
    mc "Alright, I understand what I need to do."
    scene w2_1704 with dissolve
    kat "Excellent. If those sluts don't show their shamed expressions after that, I'll be convinced they're incapable of it."
    scene w2_1707 with dissolve
    mc "Ah..."
    scene w2_1708 with dissolve
    "*Skreeeen*"
    kat "Almost perfect timing."
    "The limo decelerated into a gentle stop."
    scene w2_1709 with dissolve

    if w2KatSex == True:
        kat "Thanks for showing an old lady a good time, [mcf]. That'll be all."
        kat "Have a good night."
        scene black with fade
        "With a half-hearted wave, I said goodbye to that crazy, man-eating succubus."
    elif w2HarperSolo == True:
        kat "Thanks for the show, [mcf]. That'll be all."
        kat "Have a good night."
        scene black with fade
        "With a half-hearted wave, I said goodbye to the temptress."
    else:

        kat "That'll be all, [mcf]. Have a good night."
        scene black with fade
        "With a half-hearted wave, I said goodbye to my boss."

    scene w2_1710 with dissolve
    mct "(Finally, {b}home{/b} I'm going to sleep for a whole d-)"
    scene w2_1711 with dissolve
    mct "(Hana?)"
    war "Ha, looks like you've got some company."
    scene w2_1712 with dissolve
    mc "Night."
    "I wasn't in the mood, but I gave a perfunctory wave to Warren out of professional politeness."
    scene w2_1713 with dissolve
    mc "Hey, I didn't expect to..."
    scene w2_1714 with dissolve
    hana "I'm here to impose."
    scene w2_1713 with dissolve
    mc "Is everything okay?"
    "Her body language was surprisingly exposed and timid."
    scene w2_1714 with dissolve
    hana "I had a huge fight with my mom and my only other friend lives in a van with her boyfriend, so I was hoping..."
    scene w2_1715 with dissolve
    mc "Say no more."
    "It was as simple as that."
    scene w2_1716 with dissolve
    mc "How long do you need to stay?"
    "For the time being, I had myself a room mate."
    scene black with fade
    "........."
    "......"
    "..."
    jump June09Start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
