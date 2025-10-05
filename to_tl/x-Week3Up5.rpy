label June18Start:

    if roseFlag == True and (w2RosalindPhoto == False or "mod_w2PreExhibitionSplit_1" in visited_labels):
        scene bugfix2 with w20
        "Due to an oversight, older saves will not have a certain variable properly registered. Please set that now."
        hide screen textbox2 with dissolve

        menu:
            "Rosalind met Victoria before the second exhibition.":
                $ w2RoseMomMet = True
            "You went home alone after having lunch with the Carnations.":
                pass

        show screen textbox2 with dissolve
        "Thank you. Please enjoy the update."

    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionvictoria02 with blinds
    $ renpy.pause(6, hard=True)
    $ date = "june18day"
    play music "music/mourning-dove.ogg"
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    scene w3_8035 with blinds
    rose "I have seen the mornin' burnin' golden on the mountain in the skies~"
    show june18day with squares
    "The soft, idle singing of a woman's voice..."
    scene w3_8036 with dissolve
    rose "Achin' with the feelin' of the freedom of an eagle when she flies~"
    "Food, sprawled out on the table..."
    play ambient "sound effects/dishes.mp3"
    scene w3_8037 with dissolve
    rose "Turnin' on the world the way she smiled upon my soul as I lay dyin'~"
    "The pleasant clinking of plates being {i}drowned{/i} in a sink..."
    $ renpy.music.set_volume(.2, 0, channel = "ambient")
    scene w3_8038 with dissolve
    rose "Healin' as the colors in the sunlight and the shadows of her eyes~"
    "How easily, through the morning haze, was I lulled into ascribing this slab of concrete the designation of {i}home.{/i}"
    scene w3_8039 with dissolve
    rose "Wakin' in the mornin' to the feelin' of her fingers on my skin~"
    "The feeling of so-called domestic bliss."
    $ renpy.music.set_volume(1, 0, channel = "ambient")
    scene w3_8040 with dissolve
    rose "Wipin' out the traces of the people and the places that I've been~"
    "From where I was sitting, Rosalind seemed unflappable."
    scene w3_8041 with dissolve
    rose "Teachin' me that yesterday was somethin' that I'd never thought of tryin'~"
    "Like a sturdy tree."
    scene w3_8042 with dissolve
    rose "Talkin' of tomorrow and the money love and time we had to spend~ Lovin' her was easier than anything I'll ever do again~"
    mc "...come on! Sit down and eat!"
    scene w3_8043 with dissolve
    "........."
    stop ambient
    scene w3_8044 with dissolve
    "......"
    scene w3_8045 with dissolve
    rose "...{i}I was about to.{/i}"
    scene w3_8046 with dissolve
    mc "Uh huh, sure you were... there's a discrepancy between our plates."
    scene w3_8047 with dissolve
    rose "That's because I'm fattening you up, of course."
    scene w3_8048 with dissolve
    mc "Does Nora eat this good every morning?"
    scene w3_8049 with dissolve
    "The brief pause had me wonder if casually bringing up her daughter was crossing a line."
    scene w3_8050 with dissolve
    rose "...who has the time to make breakfast every morning?"
    scene w3_8051 with dissolve
    "......"
    scene w3_8052 with dissolve
    mc "...I'm going to miss you when you're gone."
    scene w3_8053 with dissolve
    rose "Yeah, I bet you will..."
    scene w3_8054 with dissolve
    "......"
    scene w3_8055 with dissolve
    rose "...speaking of which, when {i}can{/i} I go home?"
    scene w3_8056 with dissolve
    mc "Well, uh... things are in... {i}motion{/i}, I think."
    scene w3_8057 with dissolve
    mc "I'll... {i}check{/i} on that for you."
    scene w3_8058 with dissolve
    "It'd also be a good opportunity to see if Dalia had Darius' whore-slash-girlfriend's contact info."
    scene w3_8059 with dissolve
    "Missing colleagues and soon-to-be deposed loan sharks."
    scene w3_8060 with dissolve
    mct "({i}Fuck me.{/i})"
    scene w3_8059 with dissolve
    rose "...I'm... actually not all that eager to leave, yet."
    scene w3_8061 with dissolve
    mc "...yeah?"
    scene w3_8059 with dissolve
    rose "I'm pretty good at sticking my head in the sand. That's how I landed in this mess with Rupert..."
    scene w3_8061 with dissolve
    mc "...I wouldn't call any of {i}this{/i} ostrich behavior, Rose."
    scene w3_8062 with dissolve
    "......"
    scene w3_8063 with dissolve
    rose "...do they actually do that?"
    scene w3_8064 with dissolve
    mc "Stick their head in the sand? I... uh... I actually don't know?"
    scene w3_8063 with dissolve
    rose "Why would there be a saying otherwise?"
    scene w3_8065 with dissolve
    "......"
    "..."
    scene w3_8066 with dissolve
    mc "To the inter--"
    play ambient "sound effects/ringing-inbound.wav"
    scene w3_8067 with dissolve
    "*Ring, ring*"
    mc "...after I take this call."
    stop ambient
    play sound "sound effects/phonemenu.wav"
    scene w3_8068 with dissolve
    mc "...hello?"
    scene w3_8069 with dissolve
    mc "...huh? No, I'm not doing anything."
    scene w3_8070 with dissolve
    mc "What? You know more about phones than I do!"
    scene w3_8071 with dissolve
    mc "No, no, no! No, just come on over, I'm not--"
    mc "Yeah, yeah, yeah, we'll make an afternoon of it! Just come over! I'm not doing anything!"
    scene w3_8072 with dissolve
    mc "Alright, see you soon. {i}Love you too.{/i}"
    play sound "sound effects/phonemenu.wav"
    scene w3_8073 with dissolve
    "........."
    "......"
    scene w3_8074 with dissolve
    mc "...oh fuck, you're here."
    scene w3_8075 with dissolve
    rose "Guilty."
    scene w3_8074 with dissolve
    mc "Eeeeeeye forgot about you being {i}here.{/i} My mom is coming over."
    scene w3_8076 with dissolve
    rose "I can get dressed and be out of here in five minutes."
    mc "......"
    mc "Naaaah. I'm not going to kick you out because it's convenient for me. Not when I insisted you be here."
    mc "I'm going to help her pick out a phone. She probably won't even be here for a minute."
    scene w3_8077 with dissolve

    if w2RoseMomMet == True:
        mc "If she sees you, she sees you. It's not like you haven't met before."
    else:
        mc "If she sees you, she sees you. She can assume whatever she wants."

    scene w3_8078 with dissolve
    rose "You don't have to play the good host. At the very least, I could duck into the laundry room for five minutes."
    scene w3_8079 with dissolve
    mc "Yeah, I know, but..."
    scene w3_8080 with dissolve
    mc "......"
    scene w3_8079 with dissolve
    mc "...I kinda don't want you to? I've been lying to my mother a whole lot recently and she knows it..."
    scene w3_8080 with dissolve
    rose "It's not like you can tell her the truth about where you work."
    scene w3_8081 with dissolve
    mc "......"
    scene w3_8082 with dissolve
    mc "...I wonder?"
    scene w3_8081 with dissolve
    "A crazy thought popped into my head. I defaulted to lying to her because that was the obvious thing, but what if I just... told her?"
    scene w3_8083 with dissolve
    rose "You can't tell her the truth about where you work."
    scene w3_8084 with dissolve
    "It's been a little over a month, and she's already gathered a heap of suspicions while I told lie after lie..."
    scene w3_8085 with dissolve
    mc "Would you want to know if...?"
    scene w3_8086 with dissolve
    rose "No! I mean... I would, but! Uh... I mean..."
    scene w3_8087 with dissolve
    "Am I going to lie to her for a year? Two? {i}Three?{/i}"
    scene w3_8086 with dissolve
    rose "Of course I would want to know what's going on in my son's life, but also..."
    scene w3_8087 with dissolve
    mct "(...what's our relationship going to look like if I stay at the club until I finish med-school?)"
    scene w3_8086 with dissolve
    rose "I wouldn't accept him being a criminal. It would drive me crazy."
    scene w3_8085 with dissolve
    mc "...but what if I told her a half-truth?"
    scene w3_8084 with dissolve
    "{i}Not the full truth.{/i} {b}Just a half.{/b}"
    mct "(Calling it a sex club might be more palatable than a prostitution ring...)"
    mct "(She's pretty laissez faire, and with her {b}past{/b}, would she throw a fit..?)"
    scene w3_8083 with dissolve
    rose "If the point is to have an honest relationship, a half-truth isn't the truth, [mcf]."
    scene w3_8084 with dissolve
    "......"
    scene w3_8088 with dissolve
    mc "...ah, you're right. {i}I'm stupid.{/i}"
    scene w3_8089 with dissolve
    rose "Hey, we're all taught honesty is the best policy, but..."
    scene w3_8090 with dissolve
    mc "...I don't think my kindergarten teacher had this scenario in mind."
    scene w3_8091 with dissolve
    rose "...maybe this is backwards self-serving adult thinking, but... telling the truth because it makes you feel better is selfish."
    rose "{i}Some things...{/i} you have to keep hidden. Nora won't know every aspect of my life, and that's okay."
    scene w3_8092 with dissolve
    mc "Probably knows more than you think..."
    scene w3_8093 with dissolve
    rose "Unfortunately..."
    scene w3_8094 with dissolve
    mc "...did she work things out with her bunkmate?"
    scene w3_8095 with dissolve
    rose "Yep! Kids are amazing!"
    scene w3_8096 with dissolve
    "{i}There{/i} was the look I was fishing for. The one I had caught glimpses of over the course of Rosalind's stay."
    scene w3_8097 with dissolve
    rose "Mortal enemies one day, and best friends the next. If only adults were that flexible."
    scene w3_8098 with dissolve
    mc "I'll cook for you tonight, alright?"
    scene w3_8099 with dissolve
    rose "You don't have to do that."
    scene w3_8100 with dissolve
    mc "You didn't have to cook me this delicious breakfast either, and like me, you don't get a choice."
    mc "I've got dinner tonight."
    scene w3_8101 with dissolve
    rose "Alright, [mcf]. I like the {i}spicy-chicken{/i} flavored ramen."
    scene w3_8102 with dissolve
    mc "Hey! Don't you fucking doubt me!"
    mc "I hit above my age bracket when it comes to the kitchen."
    scene w3_8103 with dissolve
    rose "{i}Prove it then.{/i}"

    if w3FeliciaRomanceFocus == True or w3FeliciaLoseControl == True:
        $ w3FeliciaSoloEnd = True
    if history_felicia == "I must have built up some tremendous karma in a past life, as... well... {i}yeah.{/i} I will see this when I close my eyes.":
        $ w3FeliciaMinaThreesomeEnd = True
    if history_felicia == "Even though the night ended without a bang, as I intended, I still had a lovely date with my favorite gold digger.":
        $ w3FeliciaArtSoloFriendEnd = True
    if history_felicia == "I fulfilled my function as Felicia's date, serving as a buffer against awkwardness. As planned, the night ended without a bang, although Felicia could've been in better spirits.":
        $ w3FeliciaArtPrematureEnd = True

    stop music fadeout 3.0
    scene w3_8035 with dissolve
    "By the way... it turns out ostriches {i}don't{/i} actually bury their heads in the sand."
    label w3VickyPhoneShopping:
    play ambient "sound effects/city-night.wav"
    scene w3_8104 with wipeleft
    "And so I met my mom out front, avoiding any complications."
    vic "Want to wager if I can get one of these dorks to waive the activation fee?"
    scene w3_8105 with dissolve
    mc "Sounds like a losing proposition."
    scene w3_8106 with dissolve
    vic "How have you been, stranger?"
    play music "music/crinoline-dreams.ogg"
    scene w3_8108 with dissolve
    mc "I saw you on Tuesday."
    scene w3_8107 with dissolve
    vic "That long? What have you been up to?"
    scene w3_8108 with dissolve
    mc "Sowing oats, as prescribed."
    scene w3_8109 with dissolve
    vic "{b}Uh huh.{/b}"
    scene w3_8108 with dissolve
    mc "How about you? What have you been up to?"
    scene w3_8110 with dissolve
    vic "Looking into things. {i}Thinking about things.{/i}"
    scene w3_8111 with dissolve
    mc "How cryptic."
    scene w3_8107 with dissolve
    vic "Like you weren't!"
    scene w3_8108 with dissolve
    mc "What things?"
    scene w3_8110 with dissolve
    vic "Well, for one, I'm thinking about selling the house."
    scene w3_8112 with dissolve
    "{i}How unexpected.{/i} "
    scene w3_8113 with dissolve
    mc "...yeah? Why would you want to do that?"
    scene w3_8114 with dissolve
    "Six words that I didn't know would feel like a slap."
    vic "It's a big place, and I'm one woman."
    scene w3_8115 with dissolve
    mc "{b}Huh...{/b} it hasn't gotten any bigger last time I checked."
    scene w3_8116 with dissolve
    "It was an eventuality I had never thought about, or imagined I'd even care about, but those six words stirred something deep in me."
    scene w3_8117 with dissolve
    vic "It was big, even for the two of us."
    "All I knew was, on a visceral level, I didn't like it."
    scene w3_8118 with dissolve
    vic "Would you hate it if I did?"
    stop ambient fadeout 3.0
    scene w3_8119 with dissolve
    mc "...you once told me that you couldn't dream of giving up our place."
    vic "You remember that?"
    scene w2_7356 with pixellate
    vic "You were born here. Your father, you, and I spent 8 wonderful Christmases here. No way in hell am I....!"
    scene w3_8120 with pixellate
    vic "That was fourteen years ago."
    scene w3_8121 with dissolve
    mc "...we've almost tripled those Christmases."
    scene w3_8122 with dissolve
    vic "So you {i}do{/i} mind?"
    scene w3_8123 with dissolve
    mc "...you don't?"
    scene w3_8124 with dissolve
    vic "I think downsizing wouldn't be so bad. Maybe finally move into the city..."
    scene w3_8125 with dissolve
    mc "......"
    hide screen textbox2 with dissolve

    menu:
        "Try to look at it philosophically.":
            scene w3_8126 with dissolve
            show screen textbox2 with dissolve
            mc "Well, it's not like you'd be selling our memories."
        "Answer from your gut.":
            scene w3_8126 with dissolve
            show screen textbox2 with dissolve
            mc "...it'd take me some time to get used to it, but I'm an adult."

    scene w3_8125 with dissolve
    "{b}No, I didn't fucking like it.{/b}"
    scene w3_8127 with dissolve
    vic "Ah, I probably won't anyway, it's just something I'm kicking around in my head."
    scene w3_8128 with dissolve
    "A sad look besmirched my beautiful mother's face, and caused me to second guess my frank answer."
    scene w3_8129 with dissolve
    mc "...hey, if it comes to that, I know a couple of strapping young men who can help you move."
    scene w3_8130 with dissolve
    vic "Oh, yeah? Who...?"
    scene w3_8129 with dissolve
    mc "Who do you think!"
    scene w3_8131 with dissolve
    "......"
    scene w3_8132 with dissolve
    vic "...oh! You and Ian? The men part threw me!"
    scene w3_8133 with dissolve
    mc "...uuugh, why the hell hasn't anyone helped us yet?"
    scene w3_8134 with dissolve
    vic "I guess everyone had the same idea I did today."
    scene w3_8132 with dissolve
    vic "Thanks for helping me on short notice, hun. I'll get us ice-cream after this. My treat."
    scene w3_8131 with dissolve
    mc "Subtle. Doubling down on the childish insinuation, eh?"
    scene w3_8135 with dissolve
    vic "You're very strapping, {i}especially{i} with your new hair."
    scene w3_8136 with dissolve
    mc "We're both wearing it a bit differently, eh?"
    scene w3_8137 with dissolve
    vic "You noticed!"
    scene w3_8138 with dissolve
    mc "...it looks good, almost as good as ice cream."
    scene w3_8137 with dissolve
    vic "...and catch a matinee after?"
    scene w3_8138 with dissolve
    mc "And catch a matinee after."
    scene w3_8137 with dissolve
    vic "Give me an inch, I'll take a mile."
    scene w3_8139 with dissolve

    if hanaFlag == True:
        "It was at this juncture I realized the source of my dating playbook. God help me."

    vic "........."
    scene w3_8140 with dissolve
    mc "......"
    scene w3_8141 with dissolve
    vic "...something else has been on my mind. {i}Stuck{/i}, even."
    scene w3_8142 with dissolve
    mc "Consider me a crowbar."
    scene w3_8143 with dissolve
    vic "I tried to look up August Byrnes, but I couldn't find anything he directed."
    scene w3_8144 with dissolve
    "Don't make a face."
    scene w3_8145 with dissolve
    mc "That's because..."
    scene w3_8144 with dissolve
    "Don't. Make. A. Face."
    scene w3_8145 with dissolve
    mc "...he's a local guy. About your age actually."
    scene w3_8144 with dissolve
    "Yet another lie poured from my lips like water."
    scene w3_8145 with dissolve
    mc "Met him at a bar; he mentioned going to the same university you did."
    scene w3_8146 with dissolve
    vic "Oh..."
    "The lines of her face gave nothing away on whether she believed me or not, but I continued."
    scene w3_8147 with dissolve
    mc "He's had a couple of things screened at The Ambassador."
    scene w3_8148 with dissolve
    vic "Ah... I haven't been to Hills Film Festival in a couple of years."
    "{i}Change the subject.{/i}"
    scene w3_8149 with dissolve
    mc "...should we get passes for next month?"
    scene w3_8150 with dissolve
    vic "I'd love that!"
    scene w3_8151 with dissolve
    "{i}Direct hit,{/i} and possibly the first time my mother's unrestrained smile made me feel lesser."
    scene w3_8152 with dissolve
    vic "......"
    scene w3_8153 with dissolve
    vic "Heh, I don't know why that name has been bouncing around in my head."
    scene w3_8154 with dissolve
    vic "Maybe I did have a class with him or something?"
    mc "...by the way, don't ask me what a megapixel is. I don't know."
    vic "What are they even teaching you in pre-med!"
    scene w3_8155 with dissolve
    psemp "...has anyone assisted you, yet?"
    scene w3_8156 with dissolve
    vic "Looks like it's you~"
    mct "(Ah, so that was how she was going to do it.)"
    vic "I don't know anything about phones..."
    stop music fadeout 3.0
    scene black with fade
    "...what did she even need me for?"
    jump w3VickySmutPart1

    label w3VickySmutPart1:
    scene w3_8157 with pixellate
    inter "Alright, Victoria, we're rolling."
    scene w3_8158 with dissolve
    vic "...I'm ready."
    play music "music/love-or-lust.ogg"
    scene w3_8160 with dissolve
    inter "You can start, sweetheart."
    scene w3_8164 with dissolve
    vic "Uh..."
    scene w3_8165 with dissolve
    "........."
    "......"
    scene w3_8161 with dissolve
    vic "Becca Starr. 32."
    scene w3_8162 with dissolve
    vic "Nervous, but..."
    vic "Excited to be here."
    scene w3_8163 with dissolve
    inter "Hello, Becca."
    scene w3_8166 with dissolve
    don "I'm Donovan. You talked to my assistant, but I'm the one with the pleasure of conducting these castings."
    scene w3_8167 with dissolve
    vic "Should I refer to you as Donovan or {b}Mr.{/b} Gun?"
    scene w3_8168 with dissolve
    don "Donny is what my friends call me."
    scene w3_8167 with dissolve
    vic "...but we're not friends yet?"
    scene w3_8169 with dissolve
    don "{i}Everyone{/i} is my friend until they prove otherwise."
    scene w3_8170 with dissolve
    vic "Heh... alright, {i}Donny.{/i}"
    show screen camcorder
    scene w3_8171 with dissolve
    don "As I understand it, this isn't your first time being behind the camera, is it?"
    scene w3_8172 with dissolve
    vic "It's not..."
    scene w3_8171 with dissolve
    don "And we're not talking about promoting a church rummage sale on the local news, are we?"
    scene w3_8174 with dissolve
    vic "{b}No{/b}, we are NOT talking about that."
    scene w3_8171 with dissolve
    don "How many shoots have you been involved in?"
    scene w3_8173 with dissolve
    vic "Oh, uh... a handful, I guess? {i}Four to be exact...{/i} I'm still pretty green."
    scene w3_8171 with dissolve
    don "You'd be surprised. Most girls wash out after one or two shoots, once their curiosity is sated and they realize the work isn't as breezy as they expected it would be."
    scene w3_8172 with dissolve
    vic "Oh, I'm not {i}too{/i} surprised about that..."
    scene w3_8171 with dissolve
    don "The fact that you're on my couch after performing in \"a handful\" speaks to motivation, but I'd still like to ask... why are you interested in working for our production in particular?"
    scene w3_8173 with dissolve
    vic "Well... the money seemed good, and, uh... I'm... I'm looking for something more {i}reputable{/i}. {b}Professional{/b}, even."
    vic "The last guys I worked for weren't... {i}that.{/i}"
    scene w3_8171 with dissolve
    don "Bad experience?"
    scene w3_8172 with dissolve
    vic "Plural, but... I'm trying to look at them as growing pains."
    hide screen camcorder
    scene w3_8178 with dissolve
    don "I'm deeply sorry to hear that."
    scene w3_8179 with dissolve
    vic "Thank you. I... I can already tell this is a step up."
    scene w3_8178 with dissolve
    don "And those experiences haven't soured you on the work?"
    scene w3_8179 with dissolve
    vic "Like I said, it's good money..."
    scene w3_8180 with dissolve
    don "May I be so bold as to suggest something? Fair warning, it may sound a little cliche."
    scene w3_8179 with dissolve
    vic "I have a soft spot for cliches..."
    scene w3_8178 with dissolve
    don "I think there's something, other than the paycheck, that's put you on the other side of my desk."
    scene w3_8181 with dissolve
    vic "Is that a diplomatic way of saying I have screws loose?"
    scene w3_8182 with dissolve
    don "Not in the least, and I don't like the insinuation that anyone who does this job isn't all there."
    scene w3_8183 with dissolve
    vic "I... uh, I'm sorry. I was just talking about myself, really..."
    scene w3_8184 with dissolve
    don "Heh, well, I suppose not a single person has it completely together, eh?"
    scene w3_8185 with dissolve
    vic "...are your interviews typically this candid?"
    scene w3_8186 with dissolve
    don "Our customers go for a little frankness in these vids, plus I like giving them a glimpse at our actress' actual personality."
    scene w3_8187 with dissolve
    vic "Just a glimpse, though?"
    scene w3_8188 with dissolve
    don "Speaking from personal taste, it's more hot when the line between performer and woman is blurred. The unadulterated \"cock-hungry slut\" routine wears thin after 200 or so of these."
    vic "200? Wow... that's... {b}a lot.{/b}"
    don "You're telling me. I've been doing this for more than a decade; I hope that's reputable enough for you."
    show screen camcorder
    scene w3_8171 with dissolve
    don "So, Becca, other than the money... why do you want to work in entertainment?"
    scene w3_8173 with dissolve
    vic "Besides 'It's a thing you can do'? I haven't a notion..."
    scene w3_8171 with dissolve
    don "Not even a hunch?"
    scene w3_8177 with dissolve
    vic "..."
    don "You don't strike me as a bored housewife."
    scene w3_8172 with dissolve
    vic "I'm single..."
    scene w3_8171 with dissolve
    don "Any kids?"
    "......"
    scene w3_8189 with dissolve
    vic "...{i}one.{/i}"
    scene w3_8171 with dissolve
    don "I've got three beautiful triplet girls myself."
    scene w3_8190 with dissolve
    vic "My sympathy for your wife..."
    scene w3_8191 with dissolve
    don "It's just me, actually. She was quite happy to give me full custody."
    scene w3_8192 with dissolve
    vic "I'm sorry to--"
    scene w3_8193 with dissolve
    don "{b}No need.{/b} I only mention my girls because I think it's unfair for this to be one-sided."
    scene w3_8194 with dissolve
    don "I'm evaluating your on-screen presence and that, in part, depends on how comfortable you are working with me."
    scene w3_8195 with dissolve
    vic "...I {b}appreciate{/b} that."
    scene w3_8194 with dissolve
    don "Stand up for me, sweetheart. Let me get a good look at you."
    scene w3_8196 with dissolve
    vic "...alrighty."
    hide screen camcorder
    scene w3_8197 with dissolve
    don "Mmhhh... you..."
    don "You look {i}stunning{/i} - and if I may say so, you're dressed to impress."
    show screen camcorder
    scene w3_8199 with dissolve
    vic "Dress for the job you want, right?"
    scene w3_8198 with dissolve
    don "You bring that from home?"
    scene w3_8200 with dissolve
    vic "I've, uh... I used to have occasion to play {i}sexy legal assistant{/i}."
    scene w3_8198 with dissolve
    don "Used to, eh? I bet he misses it."
    scene w3_8201 with dissolve
    vic "I'm sure you have other questions..."
    scene w3_8202 with dissolve
    don "Just a few, but before that..."
    don "That blouse looks stuffy."
    scene w3_8203 with dissolve
    vic "...do you mind if I get comfortable?"
    don "Be my guest, sweetheart."
    vic "I--"

    stop music
    hide screen camcorder
    if _in_replay:
        jump w3VickySmutPart2
    else:
        show fastfor
        vic "I--"
        jump w3VickyIceCream

label w3VickyIceCream:
    play ambient "sound effects/chatter-low.wav"
    scene w3_8204 with pixellate
    show screen textbox2 with dissolve
    mc "...I didn't want to draw attention to it then, but I noticed something funny."
    scene w3_8205 with dissolve
    vic "Uh, huh...?"
    mc "Did my eyes deceive me or did I see you pay an activation fee?"
    scene w3_8206 with dissolve
    vic "Rules are rules, [mcf]! I've always said that! I didn't want to get that nice man in trouble."
    mc "Oh, was that it?"
    scene w3_8207 with dissolve
    "........."
    "......"
    scene w3_8208 with dissolve
    vic "...should've taken the bet, idiot."
    play ambient2 "sound effects/ringing-inbound.wav"
    scene w3_8209 with dissolve
    vic "Lady friend?"
    scene w3_8210 with dissolve
    mc "Order for me?"
    vic "Two scoops of French vanilla?"
    mc "{i}Please.{/i}"
    scene w3_8211 with dissolve
    vic "Say hello to Ian for me."
    "--{b}fuck{/b}, that was a direct hit."
    stop ambient
    stop ambient2
    play sound "sound effects/phonemenu.wav"
    scene w3_8212 with dissolve
    mc "Mom says hi."
    scene w3_8213 with dissolve
    kil "For Christ's sake dude, lemme get a \"'sup bro\" out!"
    scene w3_8214 with dissolve
    mc "......"
    scene w3_8215 with dissolve
    mc "...*ahem*, go ahead."
    play music "music/hotshot.ogg"
    scene w3_8216 with dissolve
    kil "Wassup bro!"
    scene w3_8217 with dissolve
    mc "Please tell me you got a good night's sleep."
    scene w3_8218 with dissolve
    kil "I was out like a fucking rock. It all caught up to me."
    scene w3_8217 with dissolve
    mc "Glad to hear it. Now, what do I owe the pleasure, my {i}enduring{/i} friend?"
    scene w3_8219 with dissolve
    kil "What's with the pep in your voice, fucker?"
    scene w3_8220 with dissolve
    mc "Two scoops at Miranda's."
    scene w3_8221 with dissolve
    kil "You {b}shitter.{/b} Where's my invite?"
    scene w3_8222 with dissolve
    mc "Impromptu afternoon with Mom."
    scene w3_8218 with dissolve
    kil "Ha! Shit, remember when I said I was jealous that the baseball team got to go there every Saturday?"
    scene w3_8217 with dissolve
    mc "Yeah, and then Mom took us there week after week. We've probably eaten thousands of dollars of ice cream."
    scene w3_8223 with dissolve
    "......"
    "...I could feel a smile creep onto my friend's face from over the phone line."
    scene w3_8224 with dissolve
    kil "So, my {i}enduring friend{/i}, I wanted to see IF and WHEN you wanted to follow up on contacting Isla."
    "Seems he couldn't get Darius' woman off his mind, either."
    scene w3_8225 with dissolve
    mc "I'm catching a movie first, but I plan on going to the club to check in on Rosie's situation. It crossed my mind to see if Dalia is there while I was at it..."
    scene w3_8224 with dissolve
    kil "You were going to do it without me?!"
    scene w3_8226 with dissolve
    mc "I wouldn't dream of it. Want to meet up there?"
    scene w3_8227 with dissolve
    kil "Yeah, sure, just--"
    scene w3_8228 with dissolve
    mc "Eeeeh! Gotta go, ice cream! I'll call you later!"
    kil "Don't just--"
    scene black with fade
    stop music
    play sound "sound effects/phonemenu.wav"
    mc "Ian said hi."
    play music "music/crinoline-dreams.ogg"
    scene w3_8229 with fade
    vic "What's the delicate lug up to?"
    scene w3_8230 with dissolve
    mc "I didn't ask; just made some plans together for later."
    scene w3_8231 with dissolve
    vic "You're inseparable again! Did he want to come to the movie with us?"
    scene w3_8230 with dissolve
    mc "I thought it might be nice if it was just the two of us."
    scene w3_8232 with dissolve
    vic "Hehe, oh yeeeeah? I like the sound of that!"
    scene w3_8233 with dissolve
    "........."
    "......"
    scene w3_8234 with dissolve
    vic "...oh, speaking of Ian, guess what! Grace contacted me yesterday! {b}Get this!{/b}"
    vic "{i}She wants to get lunch!{/i}"
    scene w3_8235 with dissolve
    mc "...ah, {i}shit{/i}, and I can guess why."
    scene w3_8236 with dissolve
    vic "That's one we'd both win... {i}Ian.{/i}"
    if w2ExEndingVictoria == True or mod_week2_ending:
        mct "(Oh yeah, I had told her about Grace's deal after week 2's exhibition.)"
    else:
        mct "(Oh yeah... I did tell her about Grace's deal during one of our calls.)"
    scene w3_8237 with dissolve
    mc "Did you tell her to screw off?"
    scene w3_8243 with dissolve
    vic "Of course not. I don't agree with her outlook on a lot of things, but I am grateful to that woman. She looked after you quite a bit, y'know?"
    scene w3_8239 with dissolve
    mc "No, she didn't! Alice did!"
    scene w3_8238 with dissolve
    vic "Don't take it for granted - how you were always included in stuff."
    scene w3_8239 with dissolve
    mc "That was Ian's doing!"
    scene w3_8240 with dissolve
    vic "And you came home with all your toes and fingers, too."
    scene w3_8241 with dissolve
    mc "That the bar?!"
    scene w3_8237 with dissolve
    "......"
    scene w3_8236 with dissolve
    vic "...if it comes to it, I'll {b}politely{/b} let her down. Who knows, maybe she'll surprise us, and we'll both be wrong."
    scene w3_8237 with dissolve
    mc "When was the last time you spoke to her?"
    scene w3_8242 with dissolve
    vic "......"
    scene w3_8234 with dissolve
    vic "...your high school graduation?"
    scene w3_8235 with dissolve
    mc "We're not wrong. She's going to want you to convince him to go to college."
    scene w3_8238 with dissolve
    vic "{i}As if I had that power...{/i}"
    scene w3_8235 with dissolve
    mc "He does adore you."
    scene w3_8240 with dissolve
    vic "And I would never betray that by going behind his back."
    scene w3_8241 with dissolve
    vic "........."
    scene w3_8242 with dissolve
    vic "......"
    scene w3_8243 with dissolve
    vic "...at best I'd {i}talk{/i} to him and ask him what he wants out of life, how he sees his future. Then, maybe... {b}just maybe{/b}, slide him my two cents."

    if w3IanDealReveal == True:
        scene w3_8244 with dissolve
        mc "I actually already spilled the beans on his mother's offer."
        scene w3_8245 with dissolve
        vic "Oh, lord... and how did he take that?"
        scene w3_8244 with dissolve
        mc "Better than I expected."
        scene w3_8245 with dissolve
        vic "Huh..."
    else:
        scene w3_8244 with dissolve
        mc "That's {i}just{/i} like you."

    stop music fadeout 3.0
    scene w3_8246 with dissolve
    "........."
    "......"
    scene w3_8247 with dissolve
    mc "...ah, what are we doing yammering? The ice-cream's melting."
    hide screen textbox2 with dissolve
    scene black with fade
    vic "Slow down, you're going to get--"
    jump w3VickySmutPart2

label w3VickySmutPart2:
    show fastfor
    vic "I--"
    play music "music/love-or-lust.ogg"
    show screen camcorder
    scene w3_8248 with pixellate
    don "I gotta say, mother of one or not, you look {i}great{/i}."
    scene w3_8249 with dissolve
    vic "Thank you..."
    scene w3_8248 with dissolve
    don "Have you done any modeling before? {i}Besides{/i} adult productions, I mean."
    scene w3_8250 with dissolve
    vic "Uh... well... I did a few beauty pageants when I was a teen..."
    scene w3_8248 with dissolve
    don "{i}Really?{/i} Interesting..."
    scene w3_8251 with dissolve
    vic "I... {i}hated{/i} them."
    hide screen camcorder
    scene w3_8252 with dissolve
    don "Why a few of them, then?"
    scene w3_8253 with dissolve
    vic "They weren't my choice..."
    scene w3_8252 with dissolve
    don "Ah, {i}got you.{/i}"
    scene w3_8254 with dissolve
    don "Well, there's more to this than looking good. Otherwise, we wouldn't need to go any further than this today."
    scene w3_8253 with dissolve
    vic "I understand. I'm... I'm prepared to do a lot more."
    scene w3_8252 with dissolve
    don "I don't doubt that. Are you good at following directions?"
    scene w3_8253 with dissolve
    vic "Oh, uh... you bet. Heh. I will consider {i}every{/i} note as if it was passed down from Fellini himself."
    scene w3_8255 with dissolve
    don "Good. Turn around for me, sweetheart."
    scene w3_8256 with dissolve
    vic "...o-okay."
    scene w3_8257 with dissolve
    don "...beautiful, but your posture is stiff, can you relax a bit?"
    scene w3_8258 with dissolve
    vic "...?"
    don "A little better, but point your ass toward the camera more."
    scene w3_8259 with dissolve
    "........."
    "......"
    scene w3_8260 with dissolve
    don "...don't be surprised, but I'm going to get up and stand behind you."
    scene w3_8261 with dissolve
    vic "Oh, are we moving onto {i}that{/i} part?"
    don "Not so fast. I have a lot more questions for you, actually."
    scene w3_8262 with dissolve
    vic "...then why are you getting...?"
    show screen camcorder
    scene w3_8263 with dissolve
    don "Your nerves got kicked up to eleven."
    vic "I'm fine... I've done this before..."
    scene w3_8264 with dissolve
    don "That's the problem, isn't it?"
    don "You're thinking about your previous experiences and your stomach feels like it's eating itself, am I right?"
    scene w3_8265 with dissolve
    vic "...It'd probably be more weird if I wasn't anxious?"
    don "It's not a bad thing. We can actually use that feeling to make a really memorable... {i}film.{/i}"
    hide screen camcorder
    scene w3_8266 with dissolve
    vic "..."
    scene w3_8267 with dissolve
    don "Too haughty of a word?"
    scene w3_8268 with dissolve
    don "You strike me as a well-watched gal, Becca."
    scene w3_8269 with dissolve
    vic "What makes you say that?"
    scene w3_8270 with dissolve
    don "I've never had an actress call me Fellini before. I like movies too."
    don "As you can imagine, my job requires me to watch a lot of them, although most probably wouldn't call them {i}cinema...{/i}"
    scene w3_8271 with dissolve
    vic "I wouldn't say my taste's any more developed..."
    don "I have a thirty by forty of {i}Deepthroat{/i} in my office. What's your favorite movie?"
    scene w3_8272 with dissolve
    vic "Oh, I don't like to play favorites..."
    scene w3_8273 with dissolve
    don "Just throw one out!"
    scene w3_8274 with dissolve
    "......"
    scene w3_8275 with dissolve
    vic "...Suspiria."
    scene w3_8276 with dissolve
    don "You like horror movies?"
    scene w3_8277 with dissolve
    vic "A... uh... I got dragged to enough that it eventually took."
    scene w3_8278 with dissolve
    don "How's your nerves?"
    vic "...{i}better.{/i} You're really good at the \"comfortable\" thing."
    scene w3_8279 with dissolve
    don "Come sit on my lap."
    vic "...uh, alright."
    scene w3_8280 with dissolve
    don "In light of your poor experiences, I should be clear. Our shoots {i}are{/i} intense."
    scene w3_8281 with dissolve
    vic "...is that a promise?"
    scene w3_8282 with dissolve
    don "I'm not flirting with you, sweetheart. I'm showing you some respect."
    scene w3_8283 with dissolve
    don "After all, it's not my ugly mug selling these tapes. Putting passion on screen is a point of pride of mine, and that is a collaborative effort."
    scene w3_8284 with dissolve
    vic "Oh...?"
    scene w3_8282 with dissolve
    don "Those men you worked with are amateurs and I'm a professional. If we work together in the future, you'll be in good hands."
    scene w3_8283 with dissolve
    don "All that I ask is you extend me a similar courtesy by respecting my time and experience. Too many girls walk through that door and treat this as {i}frivolous{/i}."
    show screen camcorder
    scene w3_8285 with dissolve
    vic "That--"
    scene w3_8286 with dissolve
    vic "Uh... that's... {b}heh.{/b} It's a business. I understand that."
    scene w3_8287 with dissolve
    vic "...would you believe one of my issues was that the filming part seemed {i}tacked{/i} on?"
    vic "I felt more like a prostitute than a--"
    scene w3_8288 with dissolve
    don "...a star?"
    scene w3_8289 with dissolve
    vic "Well... I wouldn't go that grand with it..."
    vic "It's just... I'd prefer a little structure to this..."
    scene w3_8290 with dissolve
    don "You're in luck. We have a woman on our staff that just does hair and makeup. I wasn't kidding when I said we made films..."
    scene w3_8291 with dissolve
    vic "...I believe you had more questions for me?"
    scene w3_8292 with dissolve
    don "Is that what we were doing? It slipped my mind..."
    scene w3_8293 with dissolve
    don "It's a good thing you're here to keep me on task."
    scene w3_8294 with dissolve
    vic "You're not as smooth as you think you are, Don..."
    scene w3_8295 with dissolve
    don "How about we both save our verdicts until the day is a wrap?"
    vic "I--"
    play ambient "sound effects/kissing3.wav"
    scene vpt_01_a with dissolve
    show vpt_01 with dissolve
    vic "...!"
    "........."
    "......"
    hide screen camcorder
    scene black with fade

    stop music
    stop ambient
    if _in_replay:
        vic "...Mmhhh!"
        jump w3VickySmutPart3
    else:
        show fastfor
        vic "...Mmhhh!"
        jump w3VickyMovie

label w3VickyMovie:
    play music "music/i-love-my-mom.ogg"
    scene w3_8296 with pixellate
    show screen textbox2 with dissolve
    vic "The ticket lady was checking you out."
    scene w3_8297 with dissolve
    mc "She was {i}not.{/i}"
    scene w3_8296 with dissolve
    vic "She smiled."
    scene w3_8297 with dissolve
    mc "It's her job to smile."
    scene w3_8298 with dissolve
    vic "Yeah, but she {i}smiled,{/i} {b}smiled.{/b}"
    scene w3_8299 with dissolve
    mc "It was a customer service-grade smile!"
    scene w3_8300 with dissolve
    vic "Uh uh, lemme show you the difference."
    scene w3_8301 with dissolve
    vic "This is a smile."
    scene w3_8302 with dissolve
    vic "And this is a {i}smile.{/i}"
    "The word was beginning to lose meaning."
    scene w3_8303 with dissolve
    vic "See the difference?"
    scene w3_8304 with dissolve
    mc "...{b}no!{/b}"
    scene w3_8305 with dissolve
    vic "Take my woooord for it, [mcf]!"
    mc "For the record, my {i}social{/i} life is going swimmingly. I don't need my mother to illustrate {i}flirting{/i} to me."
    scene w3_8306 with dissolve
    vic "Oh?! How swimmingly?"
    mc "The kind of swimmingly where you don't divulge the {i}explicit{/i} details to your mom!"
    scene w3_8307 with dissolve
    vic "Ohhhhhhhhhoooo...?"
    scene w3_8308 with dissolve
    "......"
    scene w3_8309 with dissolve
    vic "...is it that cutie with the tattoos?"

    if hanaGF == True:
        scene w3_8310 with dissolve
        mc "We..."
        scene w3_8308 with dissolve
        "For some reason, telling {i}her{/i}, felt like I was truly going to breathe life into whatever Hana and I were just starting."
        scene w3_8310 with dissolve
        mc "...we started going out a few days ago."
        scene w3_8311 with dissolve
        vic "H-haaa! Euuaaah!"
        "Strange, happy alien noises emitted from my mother's mouth as a look of raptured joy seized her."
        scene w3_8312 with dissolve
        mc "...did you just win a marathon or some--"
        vic "Ha, {b}ha!{/b}"
        scene w3_8313 with dissolve
        "...then she looked at me in a way that could only be described as Denzel Washington exclaiming--"
        "My. {b}Man{/b}."
        scene w3_8314 with dissolve
        vic "...wait, you waited a few days to tell me?!"
        scene w3_8315 with dissolve
        mc "I think you just displayed the whole spectrum of human emotion in the span of five seconds..."
        scene w3_8316 with dissolve
        vic "I should've been the first to know. Spill the details, you dang brat!"
        scene w3_8317 with dissolve
        vic "Did you ask her or did she ask you?"
        scene w3_8318 with dissolve
        mc "You could say I {i}insisted{/i}, but it's more like we met in the middle."
        scene w3_8319 with dissolve
        vic "Huh... that's {i}surprising.{/i}."
        scene w3_8320 with dissolve
        mc "...why are you saying it like that?"
        scene w3_8319 with dissolve
        vic "I've only known you to go for sure things."
        scene w3_8320 with dissolve
        mc "Do not--"
        scene w3_8321 with dissolve
        vic "You've always kinda reminded me of your father in that sense. I had to {i}insist{/i} too, heh."
        scene w3_8322 with dissolve
        "......"
        "...{i}she looked happy.{/i}"
        scene w3_8324 with dissolve
        mc "I'll have to check with Hana, but how about the three of us get together this Sunday?"
        scene w3_8323 with dissolve
        "{i}This simple, beautiful woman.{/i} God, I wanted her to wear that expression every single day."
        vic "First a film festival next month and now you want me to meet your girlfriend? What have I done to be so lucky!"
        scene w3_8347 with dissolve
        mc "You've already met..."
        scene w3_8325 with dissolve
        vic "I haven't met her {i}as{/i} your girlfriend."
        scene w3_8326 with dissolve
        mc "Is that an important distinc--"
        vic "{b}Duh!{/b}"
        scene w3_8327 with dissolve
        "......"
        scene w3_8328 with dissolve
        vic "...it doesn't have to be on such short notice, but... I'm always free."
        scene w3_8329 with dissolve
        mc "I'll call her later then."
        scene w3_8330 with dissolve
        vic "Okay..."

    elif w3HanaDP >= 4 or w3VeronicaSex == True or w3FeliciaSoloEnd == True or w3FeliciaMinaThreesomeEnd == True or w3MinaHotelFucked == True:

        scene w3_8310 with dissolve
        mc "We're... {i}friends.{/i}"
        scene w3_8331 with dissolve
        vic "{i}Friends?{/i}"
        scene w3_8332 with dissolve
        "She looked so damn hopeful that I {i}wanted{/i} to throw her a bone, but..."
        hide screen textbox2 with dissolve
        hide screen qmenu with dissolve

        menu:
            "Intonate something more with Hana." if w3HanaDP >= 4:
                $ w3MomToldHana = True
                show screen textbox2 with dissolve
                show screen qmenu with dissolve
                "Well, it's not like I have {i}nothing{/i} going on with Hana. And, if it'll make her smile, why not mention it?"
                scene w3_8333 with dissolve
                mc "{i}Friends.{/i} The kind you don't put a name on."
                scene w3_8334 with dissolve
                vic "...you mean casual, but not {i}casual?{/i}"
                scene w3_8333 with dissolve
                mc "Something like that."
                scene w3_8335 with dissolve
                vic "Huh, and you're okay with that...? I remember Marlow; I know how you just go along with things sometimes..."
                scene w3_8336 with dissolve
                mc "It makes sense. We're coworkers."
                scene w3_8337 with dissolve
                vic "So what?!"
                scene w3_8336 with dissolve
                mc "If things don't work out, you know..."
                scene w3_8335 with dissolve
                vic "It's a part time job!"
                scene w3_8338 with dissolve
                mc "Yeah, {i}right...{/i}"
                scene w3_8316 with dissolve
                vic "God! You remind me so much of your father. He was so passive when it came to romance; I had to ask him out!"
                scene w3_8317 with dissolve
                vic "If you want more from her, don't settle just because it's more comfortable. {i}Self-respect,{/i} [mcf]. I raised you better than that!"
                scene w3_8318 with dissolve
                mc "It's not like that! She's fun to be around, but I have other things to worry about. What's wrong with casual?"
                mc "You're always telling me I should have fun."
                scene w3_8319 with dissolve
                vic "Don't use my words against me."
                scene w3_8320 with dissolve
                mc "I can and I will."
                scene w3_8339 with dissolve
                "........."
                "......"
                scene w3_8330 with dissolve
                vic "...alright, I believe you."

            "Bring up the vague mention of your time with a certain bubbly blonde." if w3MinaHotelFucked == True:
                $ w3MomToldMina = True
                show screen textbox2 with dissolve
                show screen qmenu with dissolve
                "It's not like my social life is barren. And, if it'll make Mom smile, why not mention my time with Mina?"
                scene w3_8333 with dissolve
                mc "Not her, but, well... I have been spending time with another girl."
                scene w3_8340 with dissolve
                vic "Euuhhh?! What?! Details, {i}stat!{/i}"
                scene w3_8341 with dissolve
                mc "It's nothing serious--"
                vic "...yet? Eh?"
                scene w3_8336 with dissolve
                mc "It's nothing serious, but she's uh... {i}a ray of sunlight.{/i} Has the most biggest, infectious smile you can imagine."
                scene w3_8337 with dissolve
                vic "...are you {i}my{/i} [mcf]? Did you just describe a girl as a ray of--"
                scene w3_8336 with dissolve
                mc "And underneath that smile... {i}burning{/i} vulnerability, passion, and--"
                scene w3_8342 with dissolve
                vic "Shut up!"
                "{i}I knew what I was doing.{/i}"
                scene w3_8318 with dissolve
                mc "...but seriously, she does theater. {i}Really nice girl.{/i}"
                mc "I like spending time with her."
                scene w3_8343 with dissolve
                vic "What's her name?"
                scene w3_8344 with dissolve
                "Ah... {i}shit.{/i} Pretty sure she knew Ian was dating a {i}Mina.{/i}."
                mc "Nina."
                scene w3_8346 with dissolve
                "{i}Another fucking lie...{/i}"
                scene w3_8345 with dissolve
                vic "Nina... I want to meet her some time!"
                scene w3_8346 with dissolve
                mc "Ah, it's new!"
                scene w3_8345 with dissolve
                vic "Still!"
                scene w3_8346 with dissolve
                "......"
                "..."
                scene w3_8323 with dissolve
                "She smiled."
                "{i}This simple, beautiful woman.{/i} God, I wanted her to wear that expression every single day."
                vic "Are you dating or...?"
                scene w3_8347 with dissolve
                mc "It's just a casual thing."
                scene w3_8348 with dissolve
                vic "You're just like your father. Going with the flow, passive. {i}I remember Marlow...{/i}"
                scene w3_8347 with dissolve
                mc "It's not like Marlow!"
                scene w3_8328 with dissolve
                vic "I hope not..."
                scene w3_8327 with dissolve
                "......"
                scene w3_8329 with dissolve
                mc "...point is, you don't need to set me up with theater workers."
                scene w3_8330 with dissolve
                vic "Think of the free tickets though!"


            "Don't get too specific, but hint at your time with Felicia." if w3FeliciaSoloEnd == True or w3FeliciaMinaThreesomeEnd == True:
                $ w3MomToldFelicia = True
                show screen textbox2 with dissolve
                show screen qmenu with dissolve
                "Obviously it would be misrepresenting things, but it's not like my social life is barren. And, if it'll make Mom smile, why not mention an {i}artist{/i} that I've been spending time with?"
                scene w3_8333 with dissolve
                mc "Not her, but, well... I have been spending time with someone else."
                scene w3_8340 with dissolve
                vic "Euuhhh?! What?! Details, {i}stat!{/i}"
                scene w3_8341 with dissolve
                mc "It's just a casual thing, but I've been on a couple of dates with an artist."
                vic "An artist...?"
                scene w3_8336 with dissolve
                mc "A {i}painter{/i}. A talented one. Wicked smart, and maybe the most beautiful woman I've ever laid eyes on."
                scene w3_8335 with dissolve
                vic "You're making fun of me..."
                scene w3_8336 with dissolve
                mc "I'm serious, she's uh..."
                scene w3_8342 with dissolve
                vic "GET OUT OF TOWN! My [mcf] describing a woman as {i}beautiful{/i} - {i}haaaa!{/i} What's her name...?!"
                "I paused, and thought about concealing it, but a first name wouldn't hurt..."
                scene w3_8338 with dissolve
                mc "Felicia."
                scene w3_8343 with dissolve
                vic "{i}Felicia{/i}..."
                scene w3_8344 with dissolve
                "She rolled the word over her tongue like it was a sweet candy."
                scene w3_8346 with dissolve
                vic "Mmhhh..."
                "......"
                scene w3_8345 with dissolve
                vic "...are you two--"
                scene w3_8338 with dissolve
                mc "{b}No.{/b}"
                scene w3_8314 with dissolve
                vic "Is there a chan--"
                scene w3_8349 with dissolve
                mc "It's just a casual thing."
                vic "There's a chance!"
                "I shrugged, as if there was."
                scene w3_8327 with dissolve
                "{i}Mom smiled.{/i}"
                "{i}This simple, beautiful woman.{/i} God, I wanted her to wear that expression every single day."
                scene w3_8329 with dissolve
                mc "...point is, you don't need to set me up with theater workers."
                scene w3_8330 with dissolve
                vic "Think of the free tickets though!"

            "You had a date the other night with Veronica..." if w3VeronicaSex == True:
                $ w3MomToldVeronica = True
                show screen textbox2 with dissolve
                show screen qmenu with dissolve
                "Obviously, it would be misrepresenting our relationship, but it's not like my social life is barren. And, if it'll make Mom smile, I could mention a certain redhead I've spent time with recently..."
                scene w3_8333 with dissolve
                mc "Not her, but, well... I have been spending time with another woman."
                scene w3_8350 with dissolve
                vic "{i}Woman.{/i}"
                scene w3_8351 with dissolve
                mc "Uh, that is the word for a sexually mature--"
                vic "Shut up! You said it funny!"
                scene w3_8336 with dissolve
                mc "Heh, well... uh... there's no other way to put it. There's a lot of her."
                scene w3_8337 with dissolve
                vic "Hey, there's nothing wrong with a little wei--"
                scene w3_8336 with dissolve
                mc "She's an athlete. She has arms as thick as my neck."
                mc "If I said it funny, that's cause... {i} lotta woman there.{/i}"
                scene w3_8348 with dissolve
                "......"
                "...I watched my mother picture something that I wish she wasn't."
                vic "Ha! Oh! Oh! I {i}never{/i} imagined those words coming out of your mouth! Are you two dating?!"
                scene w3_8347 with dissolve
                mc "We've just gone out once."
                scene w3_8348 with dissolve
                vic "Will there be a twice?"
                scene w3_8322 with dissolve
                mc "It's likely."
                "{i}Mom smiled.{/i}"
                scene w3_8321 with dissolve
                vic "It's likely! That's my son!"
                scene w3_8346 with dissolve
                "{i}This simple, beautiful woman.{/i} God, I wanted her to wear that expression every single day."
                mc "Don't say it like that!"
                scene w3_8343 with dissolve
                vic "You like this {i}woman?{/i} What's her name?"
                scene w3_8344 with dissolve
                mc "I like how serious she is about things. She tackles life head on and--"
                scene w3_8343 with dissolve
                vic "You do like her!"
                scene w3_8329 with dissolve
                mc "--and her name is Veronica."
                scene w3_8327 with dissolve
                "{i}No harm in giving her a first name, was there?{/i}"
                scene w3_8329 with dissolve
                mc "...point is, you don't need to set me up with theater workers."
                scene w3_8330 with dissolve
                vic "Think of the free tickets though!"
            "Be frank: romance isn't in your future.":

                show screen textbox2 with dissolve
                show screen qmenu with dissolve
                scene w3_8353 with dissolve
                mc "We're {i}just{/i} friends."
                scene w3_8354 with dissolve
                vic "Just friends..."

                if w2RoseMomMet == True:
                    scene w3_8334 with dissolve
                    vic "What about that Rosalind woman?"
                    scene w3_8336 with dissolve
                    mc "Oh, shut up. She's just as close to your age as she is mine."
                    scene w3_8337 with dissolve
                    vic "Yeah, so?"
                    scene w3_8336 with dissolve
                    mc "You're too free wheelin'-!"
                    scene w3_8335 with dissolve
                    vic "And you're just like your dad."
                else:
                    scene w3_8319 with dissolve
                    vic "I see a lot of your dad in you."

                scene w3_8320 with dissolve
                mc "Yeah...? How so?"
                scene w3_8319 with dissolve
                vic "I remember how you were with Marlow. {i}Passive.{/i}"
                scene w3_8317 with dissolve
                vic "Your father was like that. I had to ask him out."
                scene w3_8318 with dissolve
                mc "I'm {i}a lot{/i} different than I was back then."
                scene w3_8352 with dissolve
                vic "I know. It's just..."
                vic "I guess I'm seeing what I wanted to see. {i}Reminisce{/i} or whatever."
    else:

        scene w3_8353 with dissolve
        mc "We're {i}just{/i} friends."
        scene w3_8354 with dissolve
        vic "Just friends..."

        if w2vicMomMet == True:
            scene w3_8334 with dissolve
            vic "What about that Rosalind woman?"
            scene w3_8336 with dissolve
            mc "Oh, shut up. She's just as close to your age as she is mine."
            scene w3_8337 with dissolve
            vic "Yeah, so?"
            scene w3_8336 with dissolve
            mc "You're too free wheelin'-!"
            scene w3_8335 with dissolve
            vic "And you're just like your dad."
        else:
            scene w3_8319 with dissolve
            vic "I see a lot of your dad in you."

        scene w3_8320 with dissolve
        mc "Yeah...? How so?"
        scene w3_8319 with dissolve
        vic "I remember how you were with Marlow. {i}Passive.{/i}"
        scene w3_8317 with dissolve
        vic "Your father was like that. I had to ask him out."
        scene w3_8318 with dissolve
        mc "I'm {i}a lot{/i} different than I was back then."
        scene w3_8352 with dissolve
        vic "I know. It's just..."
        vic "I guess I'm seeing what I wanted to see. {i}Reminisce{/i} or whatever."


    prescreen "This was another round of movie trivia--!"
    scene w3_8355 with dissolve
    "........."
    "......"
    scene w3_8356 with dissolve
    mc "...I should reiterate that I'm not going to have a conniption if you sell the house, y'know. {i}It's cool.{/i}"
    scene w3_8357 with dissolve
    vic "Thanks, [mcf], but it {i}is{/i} too soon to say. I don't know why I even mentioned it."
    vic "Part of me thinks I'd regret it, part of me wants a change of scenery..."
    scene w3_8356 with dissolve
    mc "Why don't you take a vacation?"
    scene w3_8357 with dissolve
    vic "I don't want to dip into my savings."
    scene w3_8358 with dissolve
    mc "I could help you pay for it."
    scene w3_8359 with dissolve
    vic "Yeah, right!"
    scene w3_8360 with dissolve
    mc "Uh... Dr. Chuck pays me {i}waaaaay{/i} too much - and I don't pay rent. I could swing it."
    scene w3_8361 with dissolve
    vic "That's {i}so{/i} odd..."
    scene w3_8362 with dissolve
    mc "It pays to have rich friends."
    scene w3_8363 with dissolve
    vic "No matter, you should be putting as much money back as you can. You have your future to think of; don't spend it frivolously on your mother."
    scene w3_8364 with dissolve
    mc "In my mind, that is the very {b}opposite{/b} of frivolous."
    scene w3_8365 with dissolve
    vic "Oh, [mcf]... heh..."
    scene w3_8366 with dissolve
    mc "What's with--"
    scene w3_8367 with dissolve
    vic "Pay me no mind. I'm just feeling {i}emotional{/i} today... you've grown up so well."
    vic "Better than I ever could imagine, so much so that just looking at you... ah..."
    scene w3_8368 with dissolve
    vic "I love you, [mcf]."
    scene w3_8324 with dissolve
    mc "Love you too, Mom."
    scene w3_8369 with dissolve
    "Again that ill-advised, nascent thought from earlier crept into my head."
    scene w3_8370 with dissolve
    "It wouldn't only be selfish to open up to her, it would also be stupid. {i}Making her complicit in a conspiracy stupid.{/i}"
    scene w3_8371 with dissolve
    mc "Nothing beats a weekday matinee. We have the place to ourselves."
    scene w3_8370 with dissolve
    vic "Have you seen any of the previous Quadruple Jeopardy movies?"
    scene w3_8371 with dissolve
    mc "Nope."
    stop music fadeout 3.0
    scene w3_8372 with dissolve
    vic "Me either. Why did we pick this again?"
    scene w3_8373 with dissolve
    mc "Because the movie itself rarely matters when you're with good company. You said that once."
    scene w3_8374 with dissolve
    prescreen "Please silence your--"
    scene w3_8375 with dissolve
    vic "Right on time."
    play sound "sound effects/punch.wav"
    scene w3_8376 with vpunch
    "So, Mom and I watched a very stupid movie."
    "I pushed every thought out of my head."
    play sound "sound effects/big-explosion.mp3"
    scene w3_8377 with dissolve
    "This feeling was about as good as life gets, I thought."
    "The movie itself was thankfully not very long, but also..."
    play music "music/guiton-sketch.ogg"
    scene w3_8378 with dissolve
    "I kinda wish it was longer, too."
    jump w3VickySmutPart3

label w3VickySmutPart3:
    if _in_replay:
        play music "music/guiton-sketch.ogg"

    scene w3_8379 with pixellate
    vic "Ghh, eeuoohh, w-wha--"
    hide screen textbox2 with dissolve
    scene vpt_02b_a with dissolve
    show vpt_02b with dissolve
    vic "W-what was...!"
    don "Mmhh, *Cwhhup-*"
    vic "W-what wass the q-qhaah...♥"
    don "--!"
    vic "Oh, o-ohh...♥♥"
    vic "C-come on...! Y-you're making it... h-hard to answer your questions--"
    scene w3_8380 with flash
    vic "Oh--♥"
    vic "A-ahh, ohhh-♥♥"
    scene w3_8381 with dissolve
    vic "O-ohhh...♥♥♥"
    scene vpt_02b_a with dissolve
    show vpt_02b with dissolve
    vic "..m-my education, was it? H-haa... *Gulp* I didn't..."
    vic "I didn't know a degree was req--"
    scene vpt_02c_a with dissolve
    show vpt_02c with dissolve
    vic "Euaaahh..?! Oh, fuuuuck...."
    vic "I've never been so distracted during one of t-these...I, uh... I..."
    don "The viewers love a girl with brains..."
    vic "Euuaahh! S-sure...!"
    don "*Shlick, fwhhiiick-!*"
    vic "S-sure, they love seeing them spread their legs...!"
    scene vpt_02_a with dissolve
    show vpt_02 with dissolve
    vic "A-aahh.... I've..."
    vic "I've... m-my... under--"
    vic "I did my four years in English lit... aeeeuuh, it sounded..."
    vic "S-sounded {i}slightly{/i} more employable than film studies..."
    vic "The irony of where I'm sitting isn't lost on me... {i}heh.{/i} O-oh..."
    vic "To be honest, I never really... w-wwith my l-life... w-well, until I did..."
    vic "O-ohhh...♥ Oh, d-damn it...♥"
    vic "Hnng, I'm rambling, t-talkin' to myself now... a-ahh...♥"
    scene w3_8382 with dissolve
    don "I didn't even graduate high school. I thought I had it figured out, but it turned out to be a whole lot of trouble."
    scene w3_8383 with dissolve
    vic "Haa... ohh... a man with a face like yours? Getting into trouble?"
    scene w3_8384 with dissolve
    don "My mother couldn't believe it, either."
    scene w3_8383 with dissolve
    vic "...h-how did you start doing... {i}this{/i}, Donny?"
    scene w3_8384 with dissolve
    don "I needed something more stable, and my boss at the time... he... {i}set me up.{/i}"
    scene w3_8383 with dissolve
    vic "S-so, y'knew a guy, huh?"
    scene w3_8385 with dissolve
    don "It's good to have friends..."
    scene w3_8386 with dissolve
    vic "Ah, ohh... hnnnhhh... uh, huh..."
    don "...and I take care of my friends, sweetheart."
    scene w3_8387 with dissolve
    vic "It already sounds like you have a lot of weight on your shoulders..."
    scene w3_8388 with dissolve
    don "It's just I can already tell we'll work well together. I'll make sure you'll never want for nothing."
    scene w3_8387 with dissolve
    vic "We haven't even finished your questions, Donny..."
    scene w3_8389 with dissolve
    "........."
    "......"
    "..."
    scene w3_8390 with dissolve
    don "What do you like in the bedroom, beautiful?"
    vic "I like it when both people feel good..."
    scene w3_8391 with dissolve
    don "Just two?"
    scene vpt_03_a with dissolve
    show vpt_03 with dissolve
    vic "I p-prefer more {i}intimate{/i} pairings, but... uh... y-yeah? Group stuff... my last few scenes were like... {i} that...{/i}"
    vic "I'm not... a-ah... {i}opposed...{/i}"
    don "And girl-on-girl?"
    vic "I haven't tried it... but if the scene requires it..."
    don "Forget the {i}scene{/i}, what about in your personal life? What turns you on, Becca?"
    vic "Uhh... before I did any of {i}this{/i}, you mean? I... ah, uhhh..."
    vic "I once had a fairly typical sex life...♥ Nothing crazy, but...♥"
    don "...but?"
    vic "...also, n-nothing that will ever be topped."
    don "So, you've already written the elegy for your sex life?"
    vic "Of c-course not... it's just, a-ahhh...♥"
    don "Should I take that as a challenge, then?"
    vic "Don't... I'm just saying... sex without love... it's... a cheap imitation..."
    don "That's hard to believe with the way you're moaning..."
    vic "I didn't say it can't feel good... and you're... u-uh... {i}skilled{/i} at what you do..."
    scene w3_8392 with flash
    vic "Oh, {i}God!{/i}"
    don "Let that voice out!"
    vic "Haaaaa...♥ Ohhhh, ohhh...♥"
    scene vpt_03_a with dissolve
    show vpt_03 with dissolve
    don "See, I agree with you there, sweetheart. Sex and making love... just. Can't. Compare."
    vic "O-ohhh...♥"
    don "Don't compare them. A good meal isn't a substitution for a good book, is it?"
    vic "Hnngg, oohhhh- n-noo...♥"
    don "You and I just met this morning, yet we're making something here. It's... {i}beautiful.{/i}"
    vic "Haaa, hhnngnggg...♥"
    don "Doesn't it give you goose pimples?"
    play ambient "sound effects/moan1.mp3"
    show screen camcorder
    scene vpt_03b_a with dissolve
    show vpt_03b with dissolve
    vic "A-aaaahhh... ohh, ohohhh...♥"
    don "Or is that just my doing, hmm?"
    vic "Ahh, haaaa, ohhh- oh, fuck..."
    vic "You're... aa, really... o-ohh... {i}really...{/i}... a-ahh...♥"
    don "I'll take care of you, sweetheart."
    vic "A-aah, {b}ooh-ohh!{/b}"
    don "Steady pay, flexible hours..."
    vic "A-aahh, haaa...♥♥"
    don "All you need to do is look good, {i}work hard{/i}, and {b}help make some art.{/b}"
    vic "Ah, ohh...♥♥♥ I can't-- {b}c-commit{/b}--"
    don "Most girls tell themselves it's a temporary thing, but what in life isn't?"
    vic "Ah, a-ahhh...♥"
    don "How many times have you done this? This is your {b}fifth{/b} time dipping your toe in the water."
    vic "Euhhh...!"
    don "What does that say about you?"
    vic "Ah, ah-"
    don "{i}You're keen on this.{/i} And it doesn't matter if you do this for a year, or two, {i}or three..{/i}"
    vic "Ahhh... that's too--"
    don "In that time, you'll be a star!"
    stop ambient
    hide screen camcorder
    scene w3_8393 with flash
    vic "Oh, ohh--!"
    scene w3_8394 with flash
    vic "W-wooaah, hhaaa, {b}haaaeeuuuuuhhhh!!!{/b}"
    vic "Euhhhh, aaahhh..."
    stop music fadeout 8.0
    scene w3_8395 with dissolve
    vic "Haa... ohh..."
    vic "Eeeehh..."
    scene w3_8396 with dissolve
    don "Look how dirty you've made my hand, sweetheart. My fingers are fuckin' filthy..."
    scene w3_8397 with dissolve
    don "Do you normally cream yourself like that or is there something...?"
    scene w3_8398 with dissolve
    vic "I, mean-- uh..."
    scene w3_8399 with dissolve
    vic "......"
    scene w3_8400 with dissolve
    don "...you know what to do."
    scene w3_8401 with dissolve
    vic "...mmmhhh."
    scene w3_8402 with dissolve
    if not persistent.w3VickyTapePart1:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3VickyTapePart1 = True
    don "{b}Good girl.{/b}"
    vic "Mmhh..."
    play sound "sound effects/click2.wav"
    scene w3_8403
    don "We still have forty minutes scheduled..."
    $ renpy.end_replay()
    jump w3VickyCap

label w3VickyCap:
    play ambient "sound effects/city-night.wav"
    scene w3_8404 with pixellate
    show screen textbox2 with dissolve
    mc "Hmm, alright."
    mc "...that's {i}all four of your contacts.{/i}"
    vic "Hey, I've got like... {i}triple{/i} that! How many do you have?!"
    play music "music/crinoline-dreams.ogg"
    scene w3_8405 with dissolve
    "......"
    scene w3_8406 with dissolve
    mc "...alright, all your data should be transferred over."
    vic "...thanks, hun. Sorry to take up so much of your time."
    scene w3_8407 with dissolve
    mc "Thanks for letting me pick the movie for once."
    scene w3_8408 with dissolve
    vic "Yeah, uh... I {i}enjoyed{/i} it."
    scene w3_8409 with dissolve
    mc "No, you didn't! You hate action movies!"
    scene w3_8410 with dissolve
    vic "...I like that you like them."
    scene w3_8411 with dissolve
    "......"
    scene w3_8412 with dissolve
    vic "...you off to Ian's? Want a ride?"
    mc "Nah, we're in walking distance..."
    scene w3_8413 with dissolve
    mc "I think I'll enjoy the heat."
    scene w3_8414 with dissolve
    mc "When are you getting lunch with his mother?"
    scene w3_8415 with dissolve
    vic "Tomorrow. If she doesn't cancel..."
    scene w3_8414 with dissolve
    mc "...hoping she will?"
    scene w3_8416 with dissolve
    vic "Ah... I have always felt a little awkward around that woman."
    scene w3_8417 with dissolve
    mc "Don't let her intimidate you. She's not better than you are."
    scene w3_8418 with dissolve
    vic "I don't need you to tell me that!"
    scene w3_8417 with dissolve
    mc "...I know, but I know how it feels."
    mc "Let me know how it goes."
    scene w3_8419 with dissolve
    vic "As if I'd keep that from you..."
    vic "I'll tell you all about it right after."
    scene w3_8420 with dissolve
    mc "If I don't hear from you, I'll equip myself with garlic."
    scene w3_8421 with dissolve
    vic "Shut up."
    stop music fadeout 5.0
    scene w3_8422 with dissolve
    "......"
    vic "...goodbye, hun."
    stop ambient fadeout 3.0
    scene black with fade
    vic "Be safe."
    jump w3HanaDaliaConvo

label w3HanaDaliaConvo:
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionhousegirls03 with blinds
    $ renpy.pause(6, hard=True)
    scene w3_8423 with blinds
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    play music "music/helping-hands.ogg"
    hana "This is... less than expected for the total bookings?"
    scene w3_8424 with dissolve
    dal "It's two hours short, to be precise..."
    scene w3_8423 with dissolve
    hana "...that doesn't sound so bad? Two hours, out of dozens?"
    scene w3_8424 with dissolve
    dal "It's within our usual margins, but..."
    scene w3_8425 with dissolve
    hana "{i}Why{/i} are we short?"
    scene w3_8426 with dissolve
    dal "That would be the question, yes."
    scene w3_8425 with dissolve
    hana "I don't want to ask, but... {i}Kimber.{/i}"
    scene w3_8426 with dissolve
    dal "{b}Kimber.{/b}"
    scene w3_8427 with dissolve
    hana "........."
    hana "......"
    scene w3_8428 with dissolve
    hana "*Sigh* She looked me in the eye..."
    scene w3_8429 with dissolve
    hana "......"
    scene w3_8430 with dissolve
    hana "...what should I tell my dad?"
    scene w3_8431 with dissolve
    dal "...the truth?"
    scene w3_8427 with dissolve
    hana "......"
    scene w3_8428 with dissolve
    hana "...if it's within the give and take--"
    scene w3_8432 with dissolve
    dal "He'll see the rescheduled bookings."
    scene w3_8433 with dissolve
    hana "...be real with me, Dal. What kind of shit is she in?"
    scene w3_8434 with dissolve
    dal "Well, most girls have a bit of leeway for this kind of stuff, but Kimber is a ... {i}serial problem.{/i}"
    scene w3_8432 with dissolve
    dal "She pulled the same thing a few weeks ago, and your father sent Warren to scare her."
    scene w3_8435 with dissolve
    hana "Oh, fuck that! No way! Those two hours can come out of my end, and, and uh--"
    scene w3_8436 with dissolve
    hana "I mean, that old bastard wants me to be proactive? {b}Fine!{/b} I'll think of some other way to punish her!"
    scene w3_8437 with dissolve
    dal "......"
    scene w3_8438 with dissolve
    dal "...my thoughts exactly. Kimber isn't the kind of woman who responds positively to a man smacking her around. It's counter-productive, even."
    scene w3_8439 with dissolve
    hana "...how would you punish her?"
    scene w3_8440 with dissolve
    dal "It's not my place to say."
    hana "And why the hell not?! You know these girls better than {i}anyone.{/i} You're in charge of them! Just give me some idea here!"
    scene w3_8441 with dissolve
    dal "......"
    scene w3_8442 with dissolve
    dal "...she likes expensive things."
    scene w3_8434 with dissolve
    dal "I would remove her from the schedule. {i}No work.{/i} Let her sit on her hands, with nothing to do, no money, {i}worried.{/i}"
    scene w3_8447 with dissolve
    hana "...but, she skipped out to see her sugar daddy, I think? That doesn't sound like it would be effective...?"
    scene w3_8444 with dissolve
    dal "{i}This is the life she knows.{/i} Give her a week or two, and she'll go crazy thinking she's been phased out."
    scene w3_8445 with dissolve
    hana "...do you mind if I suggest it to my dad?"
    scene w3_8444 with dissolve
    dal "Just don't tell him the idea came from me."
    scene w3_8443 with dissolve
    hana "And why not? Wouldn't it be more convincing coming from the mouth of someone who--"
    scene w3_8444 with dissolve
    dal "{i}No.{/i}"
    scene w3_8446 with dissolve
    dal "It's better for both of us if this is your stroke of creativity."
    scene w3_8444 with dissolve
    dal "Still, you'll need a kicker to convince him..."
    scene w3_8445 with dissolve
    hana "Like what?"
    scene w3_8444 with dissolve
    dal "Reduce her cut for two months when she comes back."
    scene w3_8446 with dissolve
    hana "......"
    scene w3_8447 with dissolve
    hana "...will that--"
    scene w3_8444 with dissolve
    dal "She'll go along with it without much fuss. I'm certain."
    stop music fadeout 3.0
    scene w3_8448 with dissolve
    hana "......"
    scene w3_8449 with dissolve
    hana "...thanks, Dalia."
    scene w3_8450 with dissolve
    dal "I'm... ah... {i}happy to help.{/i}"
    scene w3_8451 with dissolve
    "........."
    "......"
    play music "music/hotshot.ogg"
    scene w3_8452 with dissolve
    kil "...coming in! Hope no one's decent!"
    scene w3_8453 with dissolve
    kil "--oh, it's just you two."
    hana "You stole the words right out of my mouth."
    scene w3_8454 with dissolve
    mc "You say that like we didn't know who we'd find."
    "{i}Turns out a major part of Jacob's job description is guiding my witless ass to the right rooms.{/i}"
    scene w3_8455 with dissolve
    dal "Mr. Beaufort, Mr. [mcl]."
    scene w3_8456 with dissolve
    hana "Seriously, don't use {i}mister{/i} with them."
    scene w3_8457 with dissolve
    mc "Hello, Dalia... hello, Hana."

    if hanaGF == True:
        scene w3_8458 with dissolve
        hana "........."
        mc "......"
        scene w3_8459 with dissolve
        kil "...just kiss her already, dude! So we can get--"
        hana "A step ahead of you."
        scene w3_8460 with dissolve
        hana "Mmmhh~"
        "Hana pulled me into a kiss, not seeming to mind Dalia's presence, or how it might reflect her fledgling authority."
        scene w3_8461 with dissolve
        "........."
        "......"
        "...and why would she? She's not the type to give a crap about stuff like that."
        scene w3_8462 with dissolve
        hana "...hello, boyfriend."
        scene w3_8463 with dissolve
        hana "You two looking for me?"
        scene w3_8464 with dissolve
    else:

        scene w3_8465 with dissolve
        hana "You two looking for me?"
        scene w3_8466 with dissolve

    mc "Dalia, actually. We have some questions for her about a former house girl..."
    hana "Oh...?"
    scene w3_8467 with dissolve
    dal "Who, exactly?"
    scene w3_8468 with dissolve
    kil "{i}Isla.{/i}"
    scene w3_8469 with dissolve
    dal "Uh... why..."
    scene w3_8470 with dissolve
    "A half-hidden look of concern spread itself across Dalia's lovely face, as she processed the unexpected question."
    scene w3_8469 with dissolve
    dal "...what about her?"
    scene w3_8471 with dissolve
    mc "She left about three or four months ago, right?"
    scene w3_8472 with dissolve
    dal "Give or take, I'd have to check my schedule if you want me to be precise..."
    scene w3_8471 with dissolve
    mc "We're not looking for an exact date, but rather a..."
    scene w3_8470 with dissolve
    kil "{i}Why?{/i}"

    if kat_polite == True:
        "Because if I took Mrs. Pulman at her word..."
    else:
        "Because if I took Kathleen at her word..."

    scene w3_8489 with pixellate
    kat "He up and absconded after he got what he was after. Basically, he fell in love and wanted to void an agreement we had with one of the whores."
    scene w3_8473 with pixellate
    mc "...did she complete her contract with the club?"
    scene w3_8474 with dissolve
    dal "......"
    scene w3_8475 with dissolve
    dal "...why are you interested in that?"
    scene w3_8476 with dissolve
    kil "Just answer the question, eh? You suck dick; it's not your job to be curious."
    "Ah, yes, Ian's lack of tact... charming, {i}occasionally,{/i} but..."
    scene w3_8477 with dissolve
    hana "Oh, shut the fuck up, dill weed! What do you do around here?"
    "...{i}counter-productive{/i} here."
    scene w3_8478 with dissolve
    hana "Come to think of it, it's {i}my{/i} job to be curious."
    scene w3_8479 with dissolve
    hana "So, why {i}are{/i} you asking about a former house girl?"
    scene w3_8480 with dissolve
    "Bringing in a third person on this half-cooked snooping felt dubious, but..."
    scene w3_8481 with dissolve
    kil "You get a little bit of say around here and you--"
    scene w3_8480 with dissolve
    "{i}We were in this together...?{/i}"

    if w3HanaDP >= 4:
        scene w3_8482 with dissolve
        mc "Remember when you asked what we were doing yesterday and asked me to make time to explain it later?"
        hana "...?"
        mc "That time is twenty minutes from now."
    else:

        scene w3_8483 with dissolve
        mc "Remember when you asked what we were doing yesterday and told me to tell you about it if it was important?"
        hana "...?"
        mc "I'll tell you about it twenty minutes from now."

    stop music fadeout 3.0
    scene w3_8484 with dissolve
    hana "........."
    scene w3_8485 with dissolve
    hana "......"
    scene w3_8486 with dissolve
    hana "...alright, I've got to go talk to my dad about something. I'll give you three the room."
    scene w3_8487 with dissolve
    mc "Thank you."
    scene w3_8488 with dissolve
    hana "Just keep him on a leash, huh?"
    scene w3_8490 with dissolve
    hana "You don't have to take his crap, Dal! Step on him if you like!"
    scene w3_8491 with dissolve
    dal "Don't worry, sweetie. You don't have to guard my self-respect."
    hana "I know..."
    scene w3_8492 with dissolve
    hana "Twenty minutes!"
    scene w3_8493 with dissolve
    "........."
    scene w3_8494 with dissolve
    "......"
    play music "music/helping-hands.ogg"
    scene w3_8495 with dissolve
    dal "...so, what did you two want to know about Isla?"
    scene w3_8496 with dissolve
    "Ian was crass when he said it, but obviously, we should and {i}can{/i} not be transparent with this woman."
    "I don't think either of us would get into any trouble poking around about this, but I'd rather not explain ourselves to any of the owners."
    "{i}Still{/i}, a bit of rapport goes a long way, so..."
    scene w3_8497 with dissolve
    mc "I actually want to get in contact with her. I'm staying at Darius' old place, and I found some letters..."
    scene w3_8498 with dissolve
    dal "...Darius, huh?"
    scene w3_8499 with dissolve
    dal "That was..."
    dal "*Sigh* He was cute. Stupid, and {i}cute.{/i}"
    scene w3_8500 with dissolve
    kil "Huh?! Since when do you have a soft spot for anyone?"
    scene w3_8501 with dissolve
    dal "Well, he's not around anymore, so... no harm in that."
    scene w3_8495 with dissolve
    dal "You found some letters? {i}Love{/i} letters?"
    scene w3_8502 with dissolve
    mc "Something like that. You know how he skipped town a month after she left?"
    mc "I thought it might be nice to get them to her somehow."
    scene w3_8498 with dissolve
    dal "Oh, Isla? Knowing her, she probably doesn't want them."
    scene w3_8497 with dissolve
    mc "It doesn't feel right throwing them away..."
    scene w3_8495 with dissolve
    dal "Yeah, okay. She doesn't have her work phone anymore, but I'm sure I can scrounge up a way to contact her."
    scene w3_8497 with dissolve
    mc "I'd really appreciate that, Dalia. You're doing me a favor..."
    scene w3_8503 with dissolve
    dal "And I'll keep this to myself, right?"
    scene w3_8504 with dissolve
    mc "...uh, why would you need to do that?"
    scene w3_8505 with dissolve
    "{i}What did she know?{/i}"
    dal "Darius is a {i}touchy{/i} subject around here."
    scene w3_8506 with dissolve
    kil "What? I've never gotten that impression."
    scene w3_8507 with dissolve
    dal "Well, people come and go around here for all sorts of reasons, but... ah, it's not my place to say..."
    scene w3_8508 with dissolve
    kil "Oh, come on, Dal. I know you're not a loose-lipped woman. If you say something like that, it's {i}intentional.{/i}"
    scene w3_8507 with dissolve
    dal "You and he were friends, right?"
    scene w3_8508 with dissolve
    kil "Of course, you know that."
    scene w3_8509 with dissolve
    dal "People come and go around here all the time, but I've never seen August so nonchalant about {i}anyone's{/i} dereliction."
    scene w3_8510 with dissolve
    "...what did August have to do with any of this? {i}Darius was allegedly blackmailing Kat.{/i}"
    scene w3_8509 with dissolve
    dal "That struck me as odd, is all."
    scene w3_8511 with dissolve
    mc "Why do you mention it?"
    scene w3_8512 with dissolve
    dal "I don't know. Adding to the favors, I suppose..."
    scene w3_8513 with dissolve
    mc "What is Isla like?"
    scene w3_8514 with dissolve
    dal "Beautiful, of course. No ugly whores around here."
    scene w3_8513 with dissolve
    mc "Of course..."
    scene w3_8515 with dissolve
    dal "Unusually open with her feelings. Some of the patrons hated that, but others... it was an asset."
    scene w3_8513 with dissolve
    mc "Anything else?"
    scene w3_8514 with dissolve
    dal "Naïve... definitely naïve."
    scene w3_8513 with dissolve
    mc "Why do you say that?"
    scene w3_8515 with dissolve
    dal "She wasn't stringing Darius along. She actually liked him."
    scene w3_8510 with dissolve
    kil "They were {i}both{/i} stupid, huh?"
    scene w3_8509 with dissolve
    dal "Two peas in a pod, I guess..."
    scene w3_8511 with dissolve
    mc "Was she in love with him?"
    scene w3_8498 with dissolve
    dal "Oh, uh... {i}doubtful?{/i} Who's to say what that word even means around here."
    scene w3_8502 with dissolve
    mc "I guess their situation was a bit unusual?"
    scene w3_8503 with dissolve
    dal "Eh, I mean, Jacob has a soft spot for Emma, but they keep it real. So, yeah, {i}unusual...{/i}"
    scene w3_8497 with dissolve
    mc "I guess she completed her contract with the club?"
    scene w3_8499 with dissolve
    dal "I'm... not sure. I just manage the girls on a day-to-day level."
    dal "Unless they talk about it, I'm not privy to the agreement they have with August."
    scene w3_8497 with dissolve
    mc "I see... she didn't talk about it, then?"
    scene w3_8516 with dissolve
    "......"
    scene w3_8517 with dissolve
    dal "...all I know is her father owed a lot of money and she never had the look of a woman who saw the light at the end of the tunnel."
    scene w3_8518 with dissolve
    dal "I just assumed August moved her to another venture. He does that sometimes. Usually porn. A lot of the girls here look at that like a vacation, and Isla was on loan there from time to time."
    scene w3_8517 with dissolve
    dal "I assumed she switched to doing that full time."
    scene w3_8500 with dissolve
    kil "Wait, I thought he was retired from that side of things?"
    scene w3_8507 with dissolve
    dal "He is, at least from producing it, but he knows people who need girls for shoots."
    scene w3_8519 with dissolve
    kil "Oh! Have you ever--"
    scene w3_8520 with dissolve
    dal "Don't get too excited. Nothing you'd ever see."
    scene w3_8521 with dissolve
    kil "Aw..."
    scene w3_8522 with dissolve
    andrea "Wooooah, I wasn't expecting to find two hunks in here! Heaah~"
    scene w3_8523 with dissolve
    andrea "Hey, boys!"
    scene w3_8524 with dissolve
    kil "And here's the brightest smile in this place. I've seen {i}her{/i} videos."
    scene w3_8525 with dissolve
    andrea "Oh, ho, ho...! What's your favorite?"
    scene w3_8526 with dissolve
    kil "...twosome of the Dazzling Farmgirls?"
    scene w3_8527 with dissolve
    andrea "Oh! You have seen them! Want my autograph?!"
    scene w3_8528 with dissolve
    dal "Well, this is convenient. Isla is actually the reason Andrea works here."
    scene w3_8529 with dissolve
    kil "I'd be more interested in making my own video sometime..."
    andrea "Sorry, cutie! I'm under an exclusive contract!"
    scene w3_8530 with dissolve
    dal "Did you forget something, dear?"
    scene w3_8529 with dissolve
    andrea "It's about that thing..."
    scene w3_8531 with dissolve
    dal "Last time was a one time thing."
    scene w3_8532 with dissolve
    andrea "I knoooow, but--"
    scene w3_8533 with dissolve
    dal "Seems I'm a popular woman today."
    scene w3_8534 with dissolve
    mc "I appreciate your time, Dalia."
    scene w3_8535 with dissolve
    dal "Have you seen Isla at all since you started here?"
    scene w3_8536 with dissolve
    "......"
    scene w3_8537 with dissolve
    andrea "...come to think of it, uh... I think I may have seen her at Daddy Gun's a couple months back?"
    scene w3_8538 with dissolve
    mc "{i}Two{/i} months ago?"
    scene w3_8539 with dissolve
    andrea "Heh, heh... I'm not good with dates... but I'm pretty sure?"
    scene w3_8540 with dissolve
    mc "...really?!"
    scene w3_8541 with dissolve
    mct "(...ack, I need to dial it back--)"
    scene w3_8542 with dissolve
    mc "*Ahem* You did?"
    scene w3_8543 with dissolve
    andrea "Yeah...?"
    scene w3_8544 with dissolve
    "That was, at least, possible confirmation she didn't ride off into the sunset with Darius."
    scene w3_8545 with dissolve
    dal "Was she working a shoot?"
    scene w3_8546 with dissolve
    andrea "It was just a brief run-in, but... I don't think so? I think she was just in-and-out..."
    "Then again, the timeline between her leaving and Darius going missing always struck me as odd."
    scene w3_8547 with dissolve
    andrea "Plus, she had a clip board...?"
    scene w3_8548 with dissolve

    if kat_polite == True:
        "If he blackmailed Mrs. Pulman to cut Isla's strings, then he either stuck around for a month after it happened, or something wasn't adding up..."
    else:
        "If he blackmailed Kathleen to cut Isla's strings, then he either stuck around for a month after it happened, or something wasn't adding up..."

    "An overwhelming feeling of {i}why-the-fuck-am-I-looking-into-this{/i} hit me like a sack of bricks."

    "........."
    "......"
    scene w3_8549 with dissolve
    mc "...again, you are {i}sure{/i} it was a couple months ago?"
    andrea "Probably! Why do you ask?"
    scene w3_8550 with dissolve
    dal "[mcf] has some letters from Darius he wants to get to Isla."
    andrea "Oooohh... {i}romantic!{/i}"
    scene w3_8551 with dissolve
    dal "I'm trying to find a way to get in contact with her, but she lived at the club, and... well... turns out you're my best current lead."
    scene w3_8552 with dissolve
    andrea "Oh! Ummm... I could ask around at my other job..."
    scene w3_8553 with dissolve
    mc "It would be appreciated. Call me sappy, but it's sad to see undelivered letters."
    scene w3_8554 with dissolve
    andrea "You're sappy! Heaah~!"
    scene w3_8555 with dissolve
    andrea "So, about the--"
    dal "Sure thing. Did you break it again?"
    scene w3_8556 with dissolve
    andrea "Maaaaaaaaybe?"
    scene w3_8557 with dissolve
    dal "*Sigh* Alright, let's go see about it."
    scene w3_8558 with dissolve
    andrea "Thaaaaank you, Mama Bear!"
    stop music fadeout 3.0
    scene w3_8559 with dissolve
    dal "Down, girl..."
    scene black with fade
    "..."
    play music "music/hotshot.ogg"
    scene w3_8560 with wipeleft
    kil "...nice thinking with that letters thing. You're a pretty good liar."
    scene w3_8561 with dissolve
    mc "I'm feeling a bit touchy about that today, so shut up with that, eh?"
    scene w3_8562 with dissolve
    kil "{i}Touchy?{/i}"
    scene w3_8561 with dissolve
    mc "Hiding what I'm doing from Mom is--"
    scene w3_8563 with dissolve
    kil "Oh, yeah. That would kinda suck, huh?"
    scene w3_8564 with dissolve
    mc "You've lied to her too, you know. It doesn't bother you?"
    scene w3_8563 with dissolve
    kil "Well, when you say it aloud, it does, but... {i}you don't have to say it aloud.{/i}"
    scene w3_8564 with dissolve
    mc "Ah, shit... since when am I the unpragmatic of us two?"
    scene w3_8565 with dissolve
    "......"
    scene w3_8566 with dissolve
    kil "...so it seems Darius' girl didn't run off with him."
    scene w3_8567 with dissolve
    mc "It's looking like that..."
    scene w3_8568 with dissolve
    kil "Are you sure that's what the old bat said?"
    scene w3_8567 with dissolve
    mc "Actually... I think I just assumed that part."
    scene w3_8568 with dissolve
    kil "...assumed it?"
    scene w3_8569 with dissolve

    if kat_polite == True:
        mc "Well, if he went as far as to strongarm Kathleen to terminate her contract..."
    else:
        mc "Well, if he went as far as to strongarm Mrs. Pulman to terminate her contract..."

    scene w3_8568 with dissolve
    kil "Yeah... you'd think they'd run off together, right?"
    scene w3_8570 with dissolve
    mc "{i}Right...{/i} come to think of it, we shouldn't have this conversation here..."
    scene w3_8571 with dissolve
    kil "Yeah... smart thinking..."
    scene w3_8572 with dissolve
    "........."
    "......"
    scene w3_8573 with dissolve
    mc "...and I should probably go check in on Rosalind's thing."
    scene w3_8574 with dissolve
    kil "You mean that Oliver asshole?"
    scene w3_8573 with dissolve

    if w3RosalindViolentSolution == True:
        mc "August is handling it."
        scene w3_8574 with dissolve
        kil "He didn't do such a good job handling it last time."
        scene w3_8573 with dissolve
        mc "I think he's done being nice... he's sending Jacob to deal with it."
        scene w3_8574 with dissolve
        kil "Poor idiot bastard."
    else:

        mc "Your Uncle is handling it. {i}Sort of.{/i}"
        scene w3_8574 with dissolve
        kil "...yeah?"
        scene w3_8573 with dissolve
        mc "I don't think he's going to be in business very long."
        scene w3_8574 with dissolve
        kil "Good. Fuck that asshole."

    scene w3_8575 with dissolve
    kil "What about Hana? You really going to fill her in on any of this?"
    kil "I don't think Ms. Right-and-Wrong could stomach what we're not even sure happened."
    scene w3_8576 with dissolve
    "......"
    scene w3_8577 with dissolve
    mc "...well, this is our life for the foreseeable future. You, me, and Hana -- we're all entrenched here."
    scene w3_8576 with dissolve
    "......"
    scene w3_8578 with dissolve
    mc "...be honest, you like Hana, don't you? As a person, I mean."
    scene w3_8579 with dissolve
    kil "{b}Yeah.{/b} She's a cool girl."
    scene w3_8580 with dissolve
    mc "She should have a full picture too. Especially since her name's now on the door."
    scene w3_8581 with dissolve
    kil "...*sigh* I'm not going to argue with you because I know you're right."
    scene w3_8582 with dissolve
    mc "I always am."
    kil "Pfft- fuck off, idiot!"
    stop music fadeout 5.0
    scene w3_8583 with dissolve
    mc "Whatever the case, I'll frame it delicately to her. Not because I don't think she can take it, but..."
    scene black with fade
    mc "...because we don't know shit."
    jump w3HanaParkTalk

label w3HanaParkTalk:
    play ambient "sound effects/birds.wav"
    scene w3_8584 with cmet
    hana "...are you {i}seriously{/i} not going to eat anything?"
    mc "I'm good. Is that a problem?"
    hana "I hate eating when other people aren't."
    scene w3_8585 with dissolve
    mc "That's a weird hang up."
    scene w3_8586 with dissolve
    hana "I come by it honestly. Rule of my Mom's."
    scene w3_8585 with dissolve
    mc "I had a big breakfast. Like a {i}really{/i} big breakfast."
    scene w3_8587 with dissolve
    hana "Good lord, you're taking advantage of that woman."
    scene w3_8588 with dissolve
    mc "She's doing it to herself, besides... I, uh..."
    mc "I'm going to cook her dinner tonight."
    scene w3_8589 with dissolve
    hana "How much longer is she going to be at your place?"
    scene w3_8590 with dissolve
    mc "Well..."

    if w3RosalindViolentSolution == True:
        scene w3_8591 with pixellate
        aug "If everything goes smoothly, she'll be safe to go home after the weekend."
    else:
        scene w3_8592 with pixellate
        chuck "Jim says things are in motion. If he doesn't slip away, send her home after the weekend."

    play music "music/dog-park.ogg"
    scene w3_8590 with pixellate
    mc "I have it on good authority tonight is going to be her last night."
    mc "...{i}hopefully.{/i}"
    scene w3_8587 with dissolve
    hana "...goddamn it, I wish I could trade places with you."
    scene w3_8588 with dissolve
    mc "Huh? Why?"
    scene w3_8586 with dissolve
    hana "It beats brow beating a lazy prostitute into working."
    scene w3_8593 with dissolve
    mc "Eh. Our checks come from the same revenue source."
    mc "What were you doing this morning with Dalia?"
    scene w3_8594 with dissolve
    hana "Counting money."
    scene w3_8595 with dissolve
    mc "You've really fallen into your role, huh? I thought it was supposed to be a slow transition."
    scene w3_8597 with dissolve
    hana "That's the thing. I think this is what Dad considers slow."
    scene w3_8596 with dissolve
    mc "You handling all that okay?"
    scene w3_8597 with dissolve
    hana "I'm... I'm more adaptable than I thought. Another thing I get from my mom, I guess."
    hana "That woman can roll with the punches. Being a single mother, or being..."
    scene w3_8599 with dissolve
    hana "...{i}sick.{/i}"
    hana "God, she would whip my ass for saddling up with that bastard."
    scene w3_8600 with dissolve
    mc "First Dad, and now bastard?"
    scene w3_8598 with dissolve
    hana "..."
    scene w3_8599 with dissolve
    hana "It's not just me being flexible though, I..."


    if hanaGF == True:
        scene w3_8602 with dissolve
        hana "It helps that I know I have somebody in my corner."
        scene w3_8603 with dissolve
        mc "..."
        scene w3_8604 with dissolve
        "*Cwhup*"
        hana "Heh, heh... that tickles..."
    else:
        scene w3_8597 with dissolve
        hana "I haven't been feeling so alone."
        hana "I mean it sucks having to hide my life from my mom and Jerrica, but at least I can be honest with someone."

    scene w3_8605 with dissolve
    mc "Hey. I half-seriously considered spilling my guts to my mom about being a part-time pimp."
    mc "We are..."
    scene w3_8606 with dissolve
    hana "We're in this together."
    scene w3_8605 with dissolve
    mc "So you've said and said."
    scene w3_8607 with dissolve
    "........."
    scene w3_8608 with dissolve
    "......"
    scene w3_8609 with dissolve
    hana "...so, what was it that was so secretive you didn't want to talk about it at the club?"
    scene w3_8610 with dissolve
    mc "Ian and I have been trying to find Darius."
    scene w3_8609 with dissolve
    hana "And why do you want to find that jackass?"
    scene w3_8611 with dissolve
    mc "Mainly because I'd like to know if he left {i}our{/i} business on his own two feet?"
    hana "What do you--"
    scene w3_8612 with dissolve
    "So, I filled her in."
    "About Kat, about my apartment being bugged, and what little we had learned about Darius."
    scene w3_8613 with dissolve
    "Hana looked concerned, and she had a million questions, but I asked her to stow them."
    "I had the same questions, after all. Still..."
    scene w3_8614 with dissolve
    mc "...you're taking this pretty well."
    hana "Am I?"
    scene w3_8615 with dissolve
    mc "Ian didn't think you could stomach it."
    hana "Psh, I can stomach more than that pussy..."
    scene w3_8616 with dissolve
    "Hana got lost in thought, until she sprung forth with a surprising conclusion."
    scene w3_8617 with dissolve
    hana "...setting aside why that old bitch would tell you about it in the first place, let's hypothetically say Darius didn't {i}successfully{/i} blackmail the club and... {b}faced{/b} the consequences..."
    scene w3_8618 with dissolve
    hana "Who are we kidding here? My dad is involved in organized crime and our client list contains influential and powerful people."
    scene w3_8619 with dissolve
    mc "{b}Wow...{/b} you really do adapt!"
    scene w3_8620 with dissolve
    hana "Don't look at me that way!"
    scene w3_8621 with dissolve
    hana "I'm... I'm...!"
    scene w3_8622 with dissolve
    mc "Yeah. {i}We're{/i} in this together."
    mc "I'm not judging you."
    scene w3_8623 with dissolve
    mc "I've been asking myself if I could stomach working for people with blood on their hands, but I think all this digging we've been doing... it's coping about the obvious answer that I'm afraid of."
    mc "You know... I'm going to swear the Hippocratic oath one day..."
    scene w3_8624 with dissolve
    mc "It'd be cool if it meant something..."
    scene w3_8625 with dissolve
    "........."
    "......"
    scene w3_8626 with dissolve
    hana "...thanks for telling me about this, [mcf]."
    scene w3_8627 with dissolve
    mc "...yeah? I didn't tell you something you'd rather not know?"
    scene w3_8626 with dissolve
    hana "...you did, but I'm trying to face reality head-on from now."
    hana "I mean... I still will probably sell my stakes to Kat when the time comes, but in the meantime..."
    scene w3_8628 with dissolve
    mc "Take care of your mom."
    scene w3_9500 with dissolve
    hana "Yeah, right now isn't so bad."

    if hanaGF == True:
        scene w3_9501 with dissolve
        mc "By the way, I told my mom I'd like to introduce you to her as my girlfriend."
        scene w3_9502 with dissolve
        hana "...don't you think that's too soon?"
        scene w3_9503 with dissolve
        mc "What even are the ground rules for {i}any{/i} of this. You don't want to?"
        scene w3_9504 with dissolve
        hana "N-no! I... I'd really love that!"
        scene w3_9505 with dissolve
        mc "...yeah? Does Sunday work?"
        scene w3_9504 with dissolve
        hana "{b}Yeah!{/b} Sunday! I'll... I'll find something nice to wear."
    else:
        scene w3_8629 with dissolve
        "........."
        "......"

    scene w3_8630 with dissolve

    if hanaFlag == True:
        jer "Yoooooooo!"
        mc "...ah, there's Jerrica."
    else:
        jer "Yoooooooo!"
        mc "Uh, I think that's your friend."

    hana "Yeah... I've been blowing her off too much..."
    mc "Forget about all this shit for a couple of hours and pretend you're in high school again."
    scene w3_8631 with dissolve
    hana "I'll try..."
    stop ambient fadeout 3.0
    stop music fadeout 3.0
    scene black with fade
    "......"
    "..."

label w3RosalindMidday:
    play sound "sound effects/door-close.wav"
    play music "music/mourning-dove.ogg"
    scene w3_8632 with w22
    "So it was."
    "Leaving Hana, I trudged back to my apartment, carrying a vague assurance that Rosalind wouldn't be here much longer."
    rose "Oh, hey!"
    scene w3_8633 with dissolve
    mc "Sorry for being gone so long. You've been here a few days and it feels like I've left you alone more than not."
    rose "Oh... I don't mind... you've got a life... and it's not your job to babysit me."
    scene w3_8634 with dissolve
    mc "Still, I feel like I've been a bad host."
    rose "Well, you can make up for that with dinner tonight."
    scene w3_8635 with dissolve
    mc "Oh...?"
    "...was she looking forward to that?"
    scene w3_8636 with dissolve
    rose "That's what you said--"
    scene w3_8637 with dissolve
    mc "Yeah! I'm cooking!"
    scene w3_8638 with dissolve
    rose "......"
    scene w3_8639 with dissolve
    rose "5 letters. Starts with ST. {i}Amoxicillin target.{/i}"
    scene w3_8640 with dissolve
    mc "Strep."
    scene w3_8641 with dissolve
    rose "...?"
    scene w3_8642 with dissolve
    rose "It fits!"
    scene w3_8643 with dissolve
    mc "Nora never had it?"
    rose "Actually, she had scarlet fever when she was seven."
    scene w3_8644 with dissolve
    rose "I was shocked to learn that was a thing that still exists... I always thought it was like an {i}Oregon Trail{/i} disease... she took penicillin for it, though."
    scene w3_8645 with dissolve
    mc "For what it's worth, dysentery is still a thing too."
    scene w3_8646 with dissolve
    rose "I know that! I'm not {i}stupid!{/i}"
    "In a rare bout of cuteness, defiant her age..."
    scene w3_8647 with dissolve
    "...Rose puffed herself up in faux-anger."
    rose "........."
    scene w3_8648 with dissolve
    mc "......"
    "{i}It was adorable.{/i}"
    scene w3_8649 with dissolve
    mc "...uh, SO. What would {i}you{/i} like for dinner?"
    scene w3_8648 with dissolve
    rose "Surprise me!"
    scene w3_8649 with dissolve
    mc "Any food allergies?"
    scene w3_8648 with dissolve
    rose "Uh uh!"
    "{i}Ha.{/i} She was in a surprisingly vibrant mood today."
    "Perhaps it was as she said... {i}time away.{/i}"
    scene w3_8650 with dissolve
    "...or perhaps that was wishful thinking."
    scene w3_8651 with dissolve
    rose "Coastal inlet. Starts with R."
    scene w3_8652 with dissolve
    "........."
    "......"
    scene w3_8653 with dissolve
    mc "...no fucking clue. I slept through geography."
    rose "Heh! Bad!"
    scene w3_8652 with dissolve
    mc "Hmm..."
    "I ran through the staple meals in my head. All the ones I associated with positive memories."
    "Pasta salad, spaghetti, porkchops and carrots..."
    scene w3_8654 with dissolve
    mc "Surprise you it is, then."
    scene w3_8655 with dissolve
    "........."
    "......"
    scene w3_8656 with dissolve
    mc "...{i}check for immunity.{/i} That one is {i}antibody{/i} testing."
    scene w3_8657 with dissolve
    rose "Thanks!"
    scene w3_8658 with dissolve
    mc "...you like crosswords?"
    scene w3_8657 with dissolve
    rose "Not really. Haven't done one in years."
    rose "Something to do, though..."
    scene w3_8659 with dissolve
    "........."
    "......"
    scene rh_stare_a with dissolve
    show rh_stare with dissolve
    "...there was something about Rose right now that I found inordinately attractive."
    "It wasn't the usual suspects, either."
    "Not the flawless sapphires that simmered a quiet resolve."
    "Not the invitation that her neckline gave to the glory below."
    "No, not even her huge fucking tits rising and falling with every breath."
    "It was something else... {i}it was a mood.{/i}"
    "I had seen her as naked as the day she was born."
    "I had seen her in so many compromising positions."
    "Yet this? She was still in the morning's pajamas, casually working a crosswords."
    mct "(Fuck...)"
    "The casualness of it. The {i}unearned{/i} familiarity... the domesticity?"

    if roseFlag == True:
        "This woman was at my beck and call. If I wanted to..."

        if w2RosalindPhoto:
            "I could torment her in sickly sweet ways."
        else:
            "I could do whatever I wanted."
    else:
        "If I made a move, I have no doubt she'd accept it..."
        "That was the kind of woman she was right now."

    if hanaGF == True:
        "Hana, oh Hana..."

    "Was I not satisfied by this point?"
    "Or had my very chemistry been altered by a mere change of surroundings?"
    "...or was it simply the obvious? I was a 22 year old man in the endless company of beautiful women?"
    scene w3_8660 with dissolve
    "........."
    "......"
    scene w3_8661 with dissolve
    mc "...does porkchops sound alright?"
    scene w3_8662 with dissolve
    rose "I'll lay them out."
    play ambient "sound effects/ringing-inbound.wav"
    scene w3_8663 with dissolve
    "*Ring, ring.*"
    stop ambient
    stop music
    play sound "sound effects/phonemenu.wav"
    scene w3_8664 with dissolve
    mc "Hello?"
    "So caught up in the moment, I answered without even looking."
    scene w3_8665 with dissolve
    andrea "Mr. [mcl]?"
    mc "Ah..."
    "A pleasant, valley-girl like lilt greeting me on the other end."
    mc "Andrea...?"
    play music "music/i-knew-a-guy.ogg"
    scene w3_8666 with dissolve
    andrea "Heah! That's me! You know me by the sound of my voice?"
    scene w3_8667 with dissolve
    "If it wasn't her distinctive accent, then it was the adorable tittering {i}chuckle{/i} that punctuated her words that gave her away."
    scene w3_8668 with dissolve
    andrea "I got your number from Dalia. I hope you don't mind..."
    scene w3_8667 with dissolve
    "{i}It suddenly occurred to me I should have a work phone...{/i}"
    mc "Of course not. What's up? Is this about the Isla thing? Have you al--"
    scene w3_8669 with dissolve
    andrea "I put a call into my other boss! Pronto-like!"
    andrea "Isn't that great of me?!"
    hide screen textbox2 with dissolve
    scene w3_8670 with dissolve

    menu:
        "It's {i}wonderful{/i} of her."(chg=["andrea_up"]):
            $ w3AndreaRizz += 1
            scene w3_8671 with dissolve
            show screen textbox2 with dissolve
            mc "It's more than great, beautiful. You did me a favor!"
            scene w3_8672 with dissolve
            "Perhaps she was infectious. I matched the air-headed ginger by putting a smattering of pep in my own voice."
            scene w3_8671 with dissolve
            mc "Thanks for doing it so quickly!"
            scene w3_8672 with dissolve
            andrea "Awww, it seemed like a good cause."
            scene w3_8673 with dissolve
            mc "What did you find out?"
        "Never mind that. Ask her what she found out.":

            scene w3_8675 with dissolve
            show screen textbox2 with dissolve
            mc "So, what do you have for me?"

    scene w3_8674 with dissolve
    andrea "Well... uh... here's the thing! Heeeeee...."
    andrea "...he wants to meet you. {i}Heh.{/i}"
    scene w3_8676 with dissolve
    mc "{i}Who{/i} wants to meet me?"
    scene w3_8677 with dissolve
    andrea "Daddy Gun! He's the head of Lock n' Load! They're a porn studio!"
    scene w3_8678 with dissolve
    mc "...and {i}why{/i} does he want to meet me?"
    scene w3_8679 with dissolve
    andrea "He acted pretty weird when I asked about Isla. {i}Like serious voice{/i}, \"who the fuck is asking?\" and whatnot."
    scene w3_8680 with dissolve
    andrea "I told him you were an associate of Auggy and that changed the mood, but he wanted to know why you're looking for her."
    scene w3_8678 with dissolve
    mct "(Well... {i}fuck.{/i})"
    scene w3_8680 with dissolve
    andrea "I told him about the letter thing, but... {i}still...{/i}"
    scene w3_8678 with dissolve
    mc "He wants to meet me?"
    scene w3_8681 with dissolve
    andrea "Yep! That's what I said!"
    scene w3_8682 with dissolve
    "The chuckle that came from the other side of the line deflated a little alongside my awkward pause, like she was worried it was a misstep of her own that inconvenienced me."
    scene w3_8683 with dissolve
    andrea "I hope I didn't do anything wrong, I just did what Dalia said... uh..."
    hide screen textbox2 with dissolve
    scene w3_8682 with dissolve

    menu:
        "Reassure her that it's fine. You're happy to talk to him."(chg=["andrea_up"]):
            $ w3AndreaRizz += 1
            show screen textbox2 with dissolve
            mc "Aw, come on. Don't sound like that. You did everything you were asked to do to a T."
            scene w3_8681 with dissolve
            andrea "Oh, good! People yell at me for messing up even the simplest things sometimes, so--"
            scene w3_8684 with dissolve
            mc "I wouldn't ever yell at you, Andrea."
            scene w3_8681 with dissolve
            andrea "Heah, I hope you'll remember that!"
            scene w3_8684 with dissolve
            mc "Should I call him, or...?"
        "You'd rather not meet him, but...":

            show screen textbox2 with dissolve
            mc "Ah, whatever. I have time. Should I call him or--"

    scene w3_8685 with dissolve
    andrea "He wants to meet in person... {i}at his office.{/i}"
    "........."
    "......"
    scene w3_8686 with dissolve
    mc "...okay, I needed to go out to the grocery store later anyway. I can swing by."
    scene w3_8685 with dissolve
    "I felt uneasy over the prospect of meeting a likely gangster on the basis of a lie about some imaginary letters, but..."
    andrea "Oh, great! I'll take you!"
    "...perhaps not as much as I should. I might be getting used to this."
    mct "(And it's not like I can blow this off.)"
    andrea "Do you know where--"
    stop music fadeout 3.0
    scene black with fade
    "Some instructions on where to meet up with Andrea later."
    play music "music/mourning-dove.ogg"
    scene w3_8687 with dissolve
    mc "I gotta go check on something, but dinner is still on! Don't think otherwise."
    scene w3_8688 with dissolve
    rose "So I heard..."
    rose "Is this related to your Hawaii call yesterday?"
    scene w3_8689 with dissolve
    mc "..."
    scene w3_8690 with dissolve
    rose "None of my business."
    hide screen textbox2 with dissolve
    scene w3_8691 with dissolve

    menu:
        "Admit to it."(chg=["rosalind_up"]):
            $ Rosalind_Affection +=1
            scene w3_8692 with dissolve
            show screen textbox2 with dissolve
            mc "Yeah, it is. Haven't found a way to contact Ian's friend yet."
            scene w3_8693 with dissolve
            rose "Well, I hope you figure it out..."
            scene w3_8694 with dissolve
            mc "Thanks, Rosie."
        "Moving on...":
            show screen textbox2 with dissolve
            "{i}Best not to say anything.{/i}"
            scene w3_8692 with dissolve
            pass

    mc "...by the way, the powers that be tell me that things with Oliver should be settled and you can go home soon."
    scene w3_8695 with dissolve
    rose "How soon is soon?"
    scene w3_8696 with dissolve
    mc "Maybe before the weekend is over."
    scene w3_8697 with dissolve
    rose "Hmmm..."
    "Rose didn't look happy over the information. Like with everything, she took it in stride, simply filing it away inside her noggin."
    scene w3_8698 with dissolve
    rose "Alright."
    scene w3_8699 with dissolve
    mc "I think I'll pick up some carrots while I'm out?"
    scene w3_8693 with dissolve
    rose "I {i}loooove{/i} carrots."
    scene w3_8694 with dissolve
    mc "Okay! Carrots on the menu, then."
    scene w3_8693 with dissolve
    rose "Oh, by the way! I opened a drawer."
    scene w3_8694 with dissolve
    mc "You opened--"
    scene w3_8700 with dissolve
    rose "You were a cute kid."
    scene w3_8701 with dissolve
    "........."
    "......"
    scene w3_8702 with dissolve
    mc "...what, snooping while I'm out?"
    rose "Just making myself at home, as instructed..."
    scene w3_8703 with dissolve
    "In my hand, was an old photo of my parents I kept in my bedside drawer."

    if w2RoseMomMet == True:
        rose "I'm guessing that's your father?"
    else:
        rose "I'm guessing those are your parents?"

    mc "You guess right."
    rose "You look {i}just{/i} like him."
    scene w3_8704 with dissolve
    "........."
    scene w3_8705 with dissolve
    "......"
    scene w3_8706 with dissolve
    mc "...you'll have to show me your baby photos for us to be even."
    scene w3_8707 with dissolve
    rose "I don't have any..."
    scene w3_8706 with dissolve
    mc "Not a one?"
    scene w3_8707 with dissolve
    rose "Well, I'm sure some exist, but... they're in a town far away."
    rose "With people I haven't spoken to in a long time."
    scene w3_8706 with dissolve
    mc "That's kinda sad."
    scene w3_8707 with dissolve
    rose "Which part?"
    scene w3_8706 with dissolve
    mc "Just the baby photo part, because I'm sure you have a good reason for the latter."
    scene w3_8708 with dissolve
    rose "I make up for it now with scrapbooking. I'd kick myself if I couldn't tease Nora by showing pictures of her to her future boyfriend..."
    scene w3_8709 with dissolve
    "........."
    "......"
    stop music fadeout 3.0
    scene w3_8710 with dissolve
    mc "...see you tonight."
    scene w3_8711 with dissolve
    rose "{i}Be safe.{/i}"
    scene black with fade
    mc "Thanks, Rose."
    "......"
    "..."

label w3AndreaMeetup:
    play ambient "sound effects/city-night.wav"
    scene w3_8712 with wipeleft
    "--but before our quiet evening in, first came the beautiful redhead playing intermediary on my behalf."
    andrea "Hey! What's up?!"
    "And as soon as I approached, the redhead's expression lit up like a Christmas tree."
    scene w3_8713 with dissolve
    mc "You got here before me."
    "Without a doubt, the ginger porn star cut a {i}striking{/i} figure against the dreary urban backdrop."
    mc "You were at the club?"
    scene w3_8714 with dissolve
    andrea "Yep! I drive fast!"
    scene w3_8715 with dissolve
    "It seemed the pangs of desire I thought I had left behind with Rosalind's company, were still simmering..."
    hide screen textbox2 with dissolve

    menu:
        "Enthusiastically greet her."(chg=["andrea_up"]):
            $ w3AndreaRizz += 1
            play music "music/brooklyn-nights.ogg"
            scene w3_8716 with dissolve
            show screen textbox2 with dissolve
            mc "You look great!"
            andrea "...?"
            scene w3_8717 with dissolve
            andrea "Thanks!"
            scene w3_8718 with dissolve
            "The airhead's pep was contagious."
            scene w3_8719 with dissolve
            andrea "I'm wearing the same thing as earlier!"
            "True, but the light of day {i}completed{/i} the image."
            scene w3_8720 with dissolve
            mc "I thought so then, I just didn't get a chance to say it."
            scene w3_8721 with dissolve
            andrea "Hoho, well, it was crowded."
            scene w3_8722 with dissolve
            mc "Did you work last night?"
            andrea "No. Why do you ask?"
            scene w3_8723 with dissolve
            mc "It occurs to me I'm taking up your free time..."
            scene w3_8724 with dissolve
            andrea "Pssh! Don't worry about it, boss!"
            andrea "It's a good cause! Besides, I'm off until Saturday!"
            scene w3_8725 with dissolve
            andrea "Real nice of you to be worryin' about that, though."
            scene w3_8726 with dissolve
            "Her smile took on a shade less effusive, but the warmth didn't abate."
            mc "........."
            andrea "......"
            scene w3_8727 with dissolve
            mc "...so, where we going?"
        "Keep your distance. Just be normal.":

            play music "music/crinoline-dreams.ogg"
            mct "({i}Down, tiger.{/i})"
            scene w3_8713 with dissolve
            mc "Thanks for meeting me."
            scene w3_8728 with dissolve
            andrea "No problem. It's a good cause."
            scene w3_8729 with dissolve
            mc "So, where we going?"

    scene w3_8730 with dissolve
    andrea "A couple of blocks over."
    scene w3_8731 with dissolve
    mc "There's a porn studio that close to here? I had no idea."
    scene w3_8732 with dissolve
    andrea "They don't advertise it."
    scene w3_8733 with dissolve
    andrea "Hmm... oh, shoot. We're gonna be {i}extra{/i} early."
    scene w3_8734 with dissolve
    mc "You didn't say anything about appointment times..."
    scene w3_8735 with dissolve
    andrea "Heah, I hadn't confirmed anything yet when we spoke..."
    scene w3_8736 with dissolve
    andrea "My Bbbeeeee..."
    scene w3_8737 with dissolve
    mc "Ha! Alright. Fine by me."
    mc "Early is on time, on time is late, and late is unacceptable."
    scene w3_8738 with dissolve
    andrea "......"
    scene w3_8739 with dissolve
    andrea "...heah! I'll have to remember that! Who said that, a president?"
    scene w3_8731 with dissolve
    mc "........."
    mc "......"
    mc "...no clue."
    scene w3_8740 with dissolve
    andrea "Oh, well! Lemme get my purse!"
    scene w3_8741 with dissolve
    mc "So, before I step in there... uh... what's this guy I'm meeting like?"
    "After all, as much as it was a preferable experience, I wasn't here to flirt with an air-headed ginger."
    scene w3_8742 with dissolve
    andrea "He's the best! I've never even seen him raise his voice!"
    scene w3_8743 with dissolve
    andrea "Hmmm, whiiiich... I guess makes it worse when he's mad or disappointed in you? Because, well... It's like being scolded by a dad who's {i}not{/i} a piece of shit..."
    scene w3_8744 with dissolve
    andrea "You know what I mean? It sucks when you let him down."
    scene w3_8745 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Sounds like she's fond of him.":
            scene w3_8746 with dissolve
            show screen textbox2 with dissolve
            mc "Sounds like you're fond of him."
            scene w3_8747 with dissolve
            andrea "I'll put it this way... I've known him most of my adult life, and if I ever needed anyone to watch my kid..."
            scene w3_8748 with dissolve
            mc "You have a kid?"
            scene w3_8749 with dissolve
            andrea "Nope! But if I had one, he'd be top of the list!"
            scene w3_8746 with dissolve
            mc "My only frame of reference for this world is August, is he anything like..?"
            scene w3_8750 with dissolve
            andrea "Oh, no, no, no, no, no! August is... uh..."
            "She held her tongue, an act that her very body revolted against, considering the obvious way she furled her brow."
            scene w3_8751 with dissolve
            andrea "Donny is a stand up man. He's a doting father!"
            scene w3_8752 with dissolve
            "...wasn't August too, in a sense?"
            scene w3_8751 with dissolve
            andrea "He makes it his mission to ensure that everyone is {i}whole.{/i} If anyone has a problem, and he doesn't see it, he tries to understand it until it becomes his problem."
            scene w3_8753 with dissolve
            mc "Sounds like he's a good boss."
            scene w3_8749 with dissolve
            andrea "He's a good man!"
            scene w3_8754 with dissolve
            "......"
            "...the absolute certainty with which she said that made me feel better about meeting him."
            scene w3_8755 with dissolve
            mc "I believe you."
            scene w3_8756 with dissolve
            andrea "And why wouldn't you? I'm a good judge of character! Everyone says that!"
            andrea "So, don't be nervous about meeting him! Alright?! Heah!"
        "He can't be that nice, can he?"(chg=["andrea_down"]):

            $ w3AndreaRizz -= 1
            scene w3_8757 with dissolve
            show screen textbox2 with dissolve
            mc "Aw, come on, he can't be that nice, can he? He makes porn!"
            scene w3_8758 with dissolve
            andrea "Yeah? And?! What's wrong with that?!"
            mc "Uh... nothing, I just mean--"
            scene w3_8759 with dissolve
            andrea "I know what you mean! Stop projecting!"
            mc "I..."
            scene w3_8760 with dissolve
            "That accusation dumbfounded me, because she was {i}right{/i} and especially because it was coming from the ditz in front of me."
            "Either I was painfully obvious, and she was keener than I gave her credit for. Both, likely true..."
            scene w3_8761 with dissolve
            mc "Fair enough. I just... you know... he knows August."
            scene w3_8762 with dissolve
            andrea "He's nothing like Auggy!"
            "She almost seemed offended by the comparison..."
            andrea "Take my word for it! You don't have to be nervous about meeting him."


    scene w3_8763 with dissolve
    andrea "I think he's just worried that someone was asking about Isla. He's very protective."
    scene w3_8764 with dissolve
    mc "...and why would he be worried about someone asking about Isla?"
    scene w3_8765 with dissolve
    "......"
    scene w3_8766 with dissolve
    andrea "...huh, why would he?"
    scene w3_8767 with dissolve
    play sound "sound effects/slap2.wav"
    scene w3_8768 with hpunch
    mc "--!"
    andrea "Well, I guess you'll find out!"
    scene w3_8769 with dissolve
    andrea "Let's go!"
    mc "How early are we exactly?"
    scene w3_8770 with dissolve
    andrea "Oh, wait my hand-"
    stop ambient fadeout 2.0
    stop music fadeout 2.0
    scene black with fade
    "......"
    "..."
    play ambient "sound effects/office.ogg"
    scene w3_8771 with blinds
    assistant "I'm afraid he's still in a meeting, so..."
    mc "Understandable. We're the ones 25 minutes early."
    assistant "So you are..."
    play music "music/i-knew-a-guy.ogg"
    scene w3_8772 with dissolve
    "For whatever reason, the assistant showing us in didn't seem pleased by this chronological fact."
    scene w3_8773 with dissolve
    andrea "Uh... early is on time! On time is... late! Late is... {i}not good!{/i}"
    scene w3_8774 with dissolve
    mc "Yeah, what she said."
    scene w3_8775 with dissolve
    assistant "Well... uh... make yourself comfortable. Can I get you anything?"
    scene w3_8776 with dissolve
    andrea "Oh, don't fuss, Genine!"
    andrea "If we neeeeed~ anything, I'll get it! I know where everything is~"
    scene w3_8777 with dissolve
    genine "I'd rather you didn't..."
    scene w3_8778 with dissolve
    andrea "Pssh, I'll keep him away from the dead bodies! Heaah!"
    scene w3_8779 with dissolve
    "And so she left us, without saying anything else."
    scene w3_8780 with dissolve
    andrea "Ahhhh... she doesn't like me."
    hide screen textbox2 with dissolve

    menu:
        "How is that possible?":
            scene w3_8781 with dissolve
            show screen textbox2 with dissolve
            mc "I don't know how that could be possible."
            andrea "Oh... you haven't been around me enough..."
        "You can understand that, but keep your comment to yourself.":
            scene w3_8781 with dissolve
            show screen textbox2 with dissolve
            "Well, she was a bit much..."


    scene w3_8782 with dissolve
    andrea "I think it's cause I put my hands on the glass when I open the door."
    scene w3_8783 with dissolve
    andrea "{i}Neurotic bitch.{/i}"
    "For a moment, Andrea's near incessant chipper tone faltered."
    stop ambient
    scene w3_8784 with dissolve
    andrea "Hehe, heeah..."
    "...or did it? Even cursing someone, it had an earnest tinge to it."
    scene w3_8785 with dissolve
    mc "...maybe use the handle?"
    andrea "I forget!"
    scene w3_8786 with dissolve
    mc "Heh, you are... {i}unique.{/i}"
    scene w3_8787 with dissolve
    andrea "{i}Don't be mean!{/i}"
    scene w3_8788 with dissolve
    mc "I don't mean it that way. I just mean... every other house girl has a vibe between... {i}sanitized{/i} and thinly-veiled anxiety. At least, from what I've seen..."
    scene w3_8789 with dissolve
    "Which, admittedly, I hadn't seen {i}much.{/i}"
    scene w3_8790 with dissolve
    andrea "You think? Most of them are catty bitches."
    scene w3_8788 with dissolve
    mc "Heh, I suppose I wouldn't see any of that."
    scene w3_8790 with dissolve
    andrea "If you think she's bossy now, you should see Dalia when she's drunk! It's like Mama Bear times ten!"
    scene w3_8791 with dissolve
    mc "...by the way, how did you get into this kind of work? I mean, the porn side of things."
    "I had heard earlier that Andrea was on loan from the man I was meeting today, so that answered the prostitution side..."
    scene w3_8792 with dissolve
    andrea "Oh, uh... how does anyone, really? It started with a silly idea. I like to fuck, needed a job, and as a girlfriend told me at the time... uh..."
    scene w3_8793 with dissolve
    andrea "Heeah, I've got no class or shame!"
    scene w3_8794 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Joke with her. Qualities that are overrated."(chg=["andrea_up"]):
            $ w3AndreaRizz += 1
            mc "Eh. Class and shame are for people who don't have fun."
            scene w3_8793 with dissolve
            andrea "Yeah! That's what **I** said!"
        "No, but like...":

            mc "...I mean, you're not in terrible soul-crushing debt and on the hook to gangsters, are you?"
            scene w3_8795 with dissolve
            andrea "You saw my car! You think I could afford my poor life choices if someone was squeezing the blood out of me?"

    scene w3_8791 with dissolve
    mc "...you like this work?"
    scene w3_8792 with dissolve
    andrea "Oh, it has its ups and downs. Sometimes it's {i}work.{/i}"
    scene w3_8796 with dissolve
    andrea "A lot of times even, but... it's not all bad. You meet interesting people, make good money, and there's the partying..."
    scene w3_8793 with dissolve
    andrea "I'm living my best life!"
    scene w3_8797 with dissolve
    mc "It sounds convincing when you say it that way."
    scene w3_8798 with dissolve
    andrea "'cause it's the truth! I wasn't going to go to college, and I wasn't going to wait tables all my life!"
    scene w3_8799 with dissolve
    andrea "And at the end of the day, I make people happy, don't I?"
    scene w3_8800 with dissolve
    "Her smile..."
    scene w3_8801 with dissolve
    mc "Alright, I'm convinced."
    scene w3_8800 with dissolve
    "...left little room for doubt."
    scene w3_8802 with dissolve
    mc "...sorry. Am I asking too many questions or getting too personal?"

    if w3AndreaRizz >=3:
        scene w3_8803 with dissolve
        andrea "...hmmm."
        scene w3_8804 with dissolve
        andrea "It's cool, you're cute, and I love talking about myself."
        scene w3_8805 with dissolve
        andrea "Work doesn't usually call for that though, if you know what I mean..."
        scene w3_8806 with dissolve
        mc "Well, we're not {i}technically{/i} at work, are we...?"
        scene w3_8807 with dissolve
        andrea "No. We. Are. Not."
        scene w3_8808 with dissolve
        "Andrea trailed off, and it might be my imagination, but did so with a seductive lilt."
        scene w3_8809 with dissolve
        "...then again, she could yawn with sex appeal."
        scene w3_8807 with dissolve
        andrea "Why are you so interested, anyway?"
        scene w3_8810 with dissolve
        mc "Well, I... like learning about people, and I find this particular area of life... {i}fascinating.{/i}"
        scene w3_8806 with dissolve
        mc "Besides..."

        menu:
            "You have time to kill.":
                scene w3_8810 with dissolve
                mc "Well... we have a lot of time to kill, don't we?"
                scene w3_8812 with dissolve
                andrea "Heah... true! What are we at?"
                mc "...it's only been a couple of minutes."
                scene w3_8813 with dissolve
                "........."
                "......"
                scene w3_8814 with dissolve
                andrea "...Heah! That's plenty of time to get to know the new boss, then! "
                mc "Yeah, I wasn't going to complain about the company..."
                scene w3_8815 with dissolve
                "She giggled, and {i}beamed.{/i} I thought back to a week ago, to our brief encounter in the VIP lounge, and her innate talent at making a man feel wanted..."
                "This, likely, was the kind of girl Ian warned me about... and, in this moment, I understood my predecessor better..."
                "I wonder if Isla is anything like Andrea...?"
                scene w3_8816 with dissolve
                mc "You know... you remind me of an actress I know."
                scene w3_8815 with dissolve
                "In a sense, Isla's appeal has been far-reaching."
                scene w3_8817 with dissolve
                andrea "Like a movie actress? Someone famous?"
                scene w3_8815 with dissolve
                "After all, she's pulled me into her trajectory and I don't even know the bitch."
                scene w3_8816 with dissolve
                mc "Not yet, but she will be one day..."
                stop music fadeout 3.0
                scene black with fade
                "......"
                "..."
                genine "Donny will see you now."
                jump w3DonovanMeet
            "Flirt with her."(chg=["maid"]):


                scene w3_8810 with dissolve
                mc "...who wouldn't be interested in learning more about a woman like you?"
                scene w3_8811 with dissolve
                "My answer likely sounded like a line, because it was {i}a line{/i}, but there was also a kernel of genuine appraisal behind my words."
                "I thought back to a week ago, to our brief encounter in the VIP lounge..."
                scene w3_8820 with pixellate
                andrea "I know you don't care about what they're talking about, so put your arms around me instead, alright?"
                "In the midst of everything, her bright demeanor left an impression."
                scene w3_8817 with pixellate
                andrea "Aw, c'mon, there's a dozen hot chicks back at the club!"
                scene w3_8815 with dissolve
                "And, as expected, she took it at face value as a line."
                scene w3_8817 with dissolve
                andrea "You must have a lot of interests, [mcf]!"
                scene w3_8815 with dissolve
                "I questioned {i}why{/i} I even fed her it.."

                if hanaGF == True:
                    scene w3_8821 with pixellate
                    "Suddenly that dull whine of desire reverberated in my bones, and it occurred to me, I hadn't ever really availed myself to the benefits of the club..."
                    scene w3_8815 with pixellate
                else:
                    "Suddenly that dull whine of desire reverberated in my bones, and it occurred to me, I hadn't ever really availed myself to the benefits of the club..."

                mct "(...had I?)"

                menu:
                    "Flirt Harder."(chg=["andrea_up2"]):
                        $ w3AndreaRizz += 2
                        scene w3_8816 with dissolve
                        mc "I didn't mean it quite like that..."
                        scene w3_8818 with dissolve
                        andrea "...huh? No?"
                        stop music
                        play sound "sound effects/record-scratch.wav"
                        scene w3_8819 with dissolve
                        mc "Nope!"

                        if hanaGF == True:
                            "I {i}could{/i} help myself, but I didn't. I let myself get carried away."
                        else:
                            "{i}I couldn't help myself.{/i} I let myself get carried away."

                        andrea "O-oh!"
                        scene w3_8822 with dissolve
                        andrea "Pffeeeaah--"
                        "Caught off guard, Andrea chortled, expelling the air from her lungs until--"
                        play music "music/you-should.ogg"
                        scene w3_8823 with dissolve
                        andrea "Hnnnk-!"
                        "...a cute, pig-like snort."
                        scene w3_8824 with dissolve
                        andrea "Hnnk! N-no, no fair! I wasn't ready!"
                        andrea "Ah..."
                        scene w3_8825 with dissolve
                        "........."
                        "......"
                        "...once the mirth subsided, a sensuous feeling followed."
                        "Seeing the self-proclaimed \"shameless\" porn star turn red from embarrassment, and the proximity in which we sat..."
                        scene w3_8826 with dissolve
                        "We both glanced in the same direction, appraising the situation."
                        "I didn't think anyone could see us..."
                        scene w3_8827 with dissolve
                        andrea "Ah... I wasn't ready... heah."
                        scene w3_8828 with dissolve
                        "...had further stimulated my desire."
                        scene w3_8829 with dissolve
                        "........."
                        "......"
                        scene w3_8828 with dissolve
                        "...I was certain no one could see us."

                        menu:
                            "Make an overt move. (w3AndreaFoolAround = True)"(chg=["andrea_up2"]):
                                $ w3AndreaRizz += 2
                                $ w3AndreaFoolAround = True
                                jump w3AndreaAction
                            "You've had your fun. Spend of the rest of the time talking.":
                                scene w3_8830 with dissolve
                                mc "...I've been waiting to pay you back for last week."
                                andrea "Oh, {i}really?{/i} I see I left an impression..."
                                scene w3_8831 with dissolve
                                "This, likely, was the kind of girl Ian warned me about... and, in this moment, I understood my predecessor better..."
                                scene w3_8832 with dissolve
                                mc "How could you not?"
                                scene w3_8833 with dissolve
                                "I began to wonder: was Isla anything like Andrea?"
                                scene w3_8834 with dissolve
                                andrea "How much time do we have left...?"
                                "In a sense, her appeal has been far-reaching."
                                mc "It's only been a minute. We have so much time to talk that you'll hate me by the end of it..."
                                scene w3_8833 with dissolve
                                "After all, she's pulled me into her trajectory and I don't even know the bitch.."
                                scene w3_8835 with dissolve
                                andrea "I doubt that..."
                                scene black with fade
                                stop music fadeout 3.0
                                "......"
                                "..."
                                genine "Donny will see you now."
                                jump w3DonovanMeet
                    "Slow down":

                        scene w3_8816 with dissolve
                        mc "...at the very least, I haven't been bored recently."
                        scene w3_8836 with dissolve
                        "She giggled, and {i}beamed.{/i} A little flirting was fine and fun, but taking it further...? {i}Nah.{/i} Rein in your impulses, you damn horndog."
                        andrea "You're funny! You're a lot like Ian!"
                        scene w3_8815 with dissolve
                        "This, likely, was the kind of girl Ian warned me about... and, in this moment, I understood my predecessor better..."
                        scene w3_8837 with dissolve
                        mc "...I have mixed feelings about that!"
                        "I wonder if Isla is anything like Andrea...?"
                        scene w3_8838 with dissolve
                        mc "I have mixed feelings about that..."
                        "In a sense, her appeal has been far-reaching."
                        scene w3_8839 with dissolve
                        andrea "Why?! He's a nice guy!"
                        "After all, she's pulled me into her trajectory and I don't even know the bitch..."
                        scene w3_8840 with dissolve
                        mc "...you think so?"
                        scene w3_8839 with dissolve
                        andrea "Sure! And I'm good at knowing this kind of stuff!"
                        scene w3_8841 with dissolve
                        andrea "Plus... you know... {i}he's handsome.{/i}"
                        scene w3_8842 with dissolve
                        "........."
                        "......"
                        scene w3_8841 with dissolve
                        andrea "...just like you, get it?"
                        scene w3_8843 with dissolve
                        mc "{i}Smooth{/i}."
                        stop music fadeout 3.0
                        scene black with fade
                        "Maybe not quite as sharp as what Ian warned me about, but a danger all the same."
                        "......"
                        "..."
                        genine "Donny will see you now."
                        jump w3DonovanMeet
    else:

        scene w3_8799 with dissolve
        andrea "Nope! Consider me an open book!"
        scene w3_8817 with dissolve
        andrea "Just don't get mad at me if I yammer too much! Sometimes I don't know when to quit."
        scene w3_8816 with dissolve
        mc "That's perfect. You can talk enough for the both of us."
        andrea "Ha! Deal!"
        stop music fadeout 3.0
        scene black with fade
        "......"
        "..."
        genine "Donny will see you now."
        jump w3DonovanMeet


label w3AndreaAction:

    if _in_replay:
        play music "music/you-should.ogg"
        show transitionhousegirls with cmet
        show screen textbox2 with dissolve
        "Please set [mcf]'s personality (toughness score) for this replay."
        hide screen textbox2 with dissolve
        menu:
            "Nice guy (Toughness: 0)":
                $ toughness = 0
            "Asshole (Toughness: 30)":
                $ toughness = 30
        show screen textbox2 with dissolve


    scene w3_8844 with dissolve
    "Wordlessly, I placed my hand on Andrea's inner thigh, conveying my intention."
    scene w3_8845 with dissolve
    "From there, my gaze held solely on Andrea's face. Like a puppy dog, she proved easy to read."
    scene w3_8846 with dissolve
    andrea "Ah..."
    scene w3_8845 with dissolve
    "Her baby blues narrowed, and there was intrigue peeking back at me, but mixed in was a lingering apprehension."
    scene w3_8847 with dissolve
    "Her eyes once more darted to the partially concealed window behind us."
    "For a carefree woman in her {i}position{/i}, she was surprisingly attentive about the location."
    scene w3_8848 with dissolve
    "And so, I corrected her lapse of judgement."
    scene w3_8849 with dissolve
    "I clasped her soft, makeup-caked cheeks and directed her attention back to the only thing that matters."
    "{i}Me.{/i}"
    scene w3_8850 with dissolve
    "{i}Look at me.{/i}"
    "There was no way my face sufficiently conveyed that message, but I thought it just the same."
    scene w3_8851 with dissolve

    if toughness >= 20:
        "{b}Look at me, slut.{/b}"
    else:
        "{b}Look at me.{/b}"

    "Yet... as I gripped Andrea, her pupils dilated with arousal. She didn't have to read my thoughts exactly to get my message."
    scene w3_8852 with dissolve
    andrea "...Genine would EXPLODE if she caught us going at it... or worse, {i}made a mess.{/i}"
    scene w3_8851 with dissolve
    "I could alleviate that first problem."
    scene w3_8853 with dissolve
    "Again, I let my body do the talking."
    scene w3_8854 with dissolve
    "I got up. {i}Determined.{/i}"
    "Foolishly imagining that there was a swagger in every step I took."
    scene w3_8855 with dissolve
    "Privacy."
    "{i}Just a little more couldn't hurt.{/i}"
    scene w3_8856 with dissolve
    "As I turned to face Andrea, my skin felt the prickly signs of arousal."
    "Not the ambient yearning I had felt all afternoon, but a heightened sensation that demanded I do something about it."
    scene w3_8857 with dissolve
    "God help me, but I was developing a taste for this sort of thing..."
    scene black with fade
    "The thrill of an easy woman, and doing it in public places."
    scene w3_8858 with fade
    "So, I seized Andrea, pulling her to her feet."
    "This time when I studied the lines of her face, I couldn't find a hint of inhibition."
    scene w3_8859 with dissolve
    "She had her game face on."
    mc "Now, we only have to be careful about making a mess..."
    play ambient "sound effects/kiss2.wav"
    scene andrea_01_a with dissolve
    show andrea_01 with dissolve
    andrea "Mmmhh...!"
    "It's not like I was planning on going four rounds and fucking her brains out in the waiting room."
    "I felt possessed, sure, but I wasn't out of control."
    "This was a tentative experiment of my position and would-be charm."
    andrea "Ah, mmhhh..."
    mct "(How far would I take this...?)"
    stop ambient
    scene w3_8860 with dissolve
    andrea "You... heh... when did you eat a mint?"
    scene w3_8861 with dissolve
    andrea "Ahh--"
    scene andrea_02_a with dissolve
    show andrea_02 with dissolve
    andrea "...o-ohh! That tickles!"
    "Moving on from her lips, I worked my way to her ear."
    andrea "...mmmh-- tickles a-amazing~!"
    "A venture made worthwhile from the airhead's immediate reaction."
    andrea "Oh, keep doing {b}that!{/b}"
    "Like a dog getting her belly scratched, she was very honest about what felt good."
    andrea "Keep. {i}Doing.{/i} {b}That.{/b}"
    "{i}I liked that.{/i}"
    andrea "Ae, heahh...♥ That's the spot-♥♥"
    "I loved that, even. {i}Turning her into putty would be straightforward.{/i}"
    andrea "Mmhh, heheah...♥"
    "Even in moments like this she giggled. Andrea had an outward joy that pervaded every facet of her life, from casual conversation to having her erogenous zones attacked."
    scene w3_8862 with dissolve
    "It was music to my ears and a girlish intonation of my effectiveness as a lover."
    "But, on the other hand..."
    scene w3_8863 with dissolve
    andrea "E-even better...♥"
    "That uplifting laugh would sound so much better twisted into slutty, insensate moans."
    scene andrea_03_a with dissolve
    show andrea_03 with dissolve
    andrea "Ghhh, that's an even better spot!"
    "Well, {i}I would get there,{/i} but in the meantime I thanked God for impossible, stupidly tight jeans."
    "It was no substitute for bare contact, but the fabric was flexible enough that I could comfortably trace Andrea's mound through the texture and even tease the inside of her outer lips."
    andrea "Hnnggg...♥"
    "Hell, in a sense, the extra layer of separation added an air of denial and needy desperation to the act."
    mc "*Chwup, fwhhup-!*"
    "Similarly, my fingertips felt the full brunt of Andrea's need."
    andrea "My n-nose... m-my cheeks... that's-"
    "I began to imagine what it'd feel like to be inside her, how satisfying it would be to immerse my dick in that cloying heat, to feel her juices dribble down my sack as I lost all sense of reason."
    scene andrea_03b_a with dissolve
    show andrea_03b with dissolve
    andrea "Heeuuhhhh...♥ Boohhhsss!"
    "She howled like a puppy dog begging for scraps."
    andrea "Haaa, haaaa...♥"
    "Contrary to her earlier worry, she had no qualms about the noise."
    mct "(Which... I think was fine?)"
    "Once we shut the door, the ambience of the office had vanished, but..."
    mc "What if someone hears you...?"
    andrea "Oh, t-then maybe you should s-stop...?"
    "She said, half-heartedly trailing off..."
    scene w3_8864 with dissolve
    mc "*Mmmh, you {i}really{/i} want me to stop?"
    scene w3_8865 with dissolve
    andrea "N-no... heahh... n-no!"
    scene w3_8866 with dissolve
    "{i}I didn't think so.{/i}"
    scene w3_8867 with dissolve
    andrea "Of course not! I... actually... more..."
    scene w3_8866 with dissolve
    "This woman shared a similar vivaciousness as Felicia, I thought. Open and honest about her appetite, but with none of the complication."
    scene w3_8867 with dissolve
    andrea "Touch me m-more..."
    scene w3_8868 with dissolve
    "An honest and sincere plea..."
    scene w3_8869 with dissolve
    mc "*Chwup, fwhhuhup-!* Mmmhh..."
    scene w3_8868 with dissolve
    "Clear. As. Day."
    scene w3_8867 with dissolve
    andrea "Just... uh... {i}try to keep it down?{/i}"
    scene w3_8870 with dissolve
    mc "You got it!"
    scene black with fade
    andrea "Mmhh, mhhhh-?!"
    "{i}Time to go to town.{/i}"
    mc "*Chwwwup, fhwwwup-!* Mmhh...!!"
    scene andrea_04_a with dissolve
    show andrea_04 with dissolve
    andrea "Mmhhffff, hhaa-!"
    mct "({b}Ah!{/b})"
    "This beautiful rack had been on display for a while, and finally, I. Got. My. {i}Mouth on it.{/i}"
    andrea "Eeuhhhh-!"
    "I held her pert nipple firmly between my lips, suckling and suctioning while zealously running my tongue over her areola."
    andrea "Mmhhhffff, mmhhh...!"
    "Andrea's sensitivity was off the charts..."
    andrea "Mmhhhfff, hhheeeee-♥"
    "Every time I pulled her teat toward the back of my throat, Andrea twitched."
    "And twitched."
    "And twitched. And twitched."
    "And twitched. And twitched. And twitched."
    andrea "Euuhh, mmmmf-♥♥"
    "{i}And twitched.{/i}"
    mc "*Chwup, fwhhp!* Mmh, hhhhhmmm...!"
    "Meanwhile, the hand rubbing her crotch switched to a more {i}focused{/i} assault."
    andrea "Ahh, mhmhh, mmppfhhh-!"
    "I grabbed at her, closing my hand around her sex with a crushing motion and doing my best to wedge the tips of my fingers into her slit."
    andrea "Mmfffhhh-!"
    "A paradoxically futile, yet effective effort - and as the porn star moaned into my palm from the needy pawing, I didn't hold back my own enthusiasm."
    mc "Mmmmh...!"
    "I moaned into her milk bags, letting her know what her earnestness was fueling in me."
    andrea "Mmmmf, mfffff-♥♥♥♥♥♥♥"
    "Little micro-orgasms assailed her body, one at a time, as my head swam in a pure elation of masculine potency."
    andrea "Eeuhh...!"
    scene andrea_04b_a with dissolve
    show andrea_04b with dissolve
    "Adding to that high was the tactile feeling of Andrea's moans. Her pleasured coos ran down my arm like a bit of haptic feedback saying {i}good job.{/i}"
    andrea "Mhh, hhhmm, heuhhhhh-!"

    if toughness >= 20:
        mct "(Moan for me, slut!)"
    else:
        mct "(Moan for me!)"

    andrea "Mmmhhhh, hhhaaaa...♥"
    mct "(I wonder how she sounds on camera...?)"
    andrea "Mmmh, hhhmmhmhhh...♥♥"
    "I filed that lovely noise into my brain, making a mental note to find some of her porn videos later."
    andrea "Mmhh, hhheeeaaa-♥♥♥"
    "You know... {i}just to compare...{/i}"
    "And as one last compliment--"
    stop music
    play sound "sound effects/string-break.wav"
    scene w3_8871 with vpunch
    "She lurched forward, weak in the knees."
    scene w3_8872 with dissolve
    andrea "Ahh, whaaa--"
    play ambient "sound effects/kiss2.wav"
    scene andrea_05_a with dissolve
    show andrea_05 with dissolve
    andrea "Mmhhhh...♥"
    "The redhead moaned into my throat, and reoriented herself in my arms."
    andrea "Mmmhh--"
    "As I soaked in the heat of her body and enjoyed the softness of her curves, my mind went to a singular place."
    andrea "Mmhh...♥♥"
    "Turnabout is fair play."
    $ mod_var = False
    menu:
        "[mod_option] Both":
            $ mod_var = True
            jump w3AndreaWankOff
        "Let's not push it. Use Andrea like a jizz rag.":
            jump w3AndreaWankOff
        "Take the risk. {b}Fuck her.{/b}":
            jump w3AndreaQuickie

label w3AndreaWankOff:
    stop ambient
    play music "music/six-days-of-heat-pt2.ogg"
    scene w3_8873 with dissolve
    mc "Get on your knees."
    "It posing a lesser risk of getting caught aside, the thought of the act persuaded me..."
    scene w3_8874 with dissolve
    andrea "Mmmh, kay--"
    "Bringing the bimbo to her knees and stroking myself to completion like she was a picture on a page..."
    play sound "sound effects/zipper.wav"
    scene w3_8875 with dissolve
    "{i}Excitement surged in me.{/i}"
    scene w3_8876 with dissolve
    "Treating her like she was a mere object... a target to slake my lusts on..."
    mc "Haaaa...!"
    scene andrea_06_a with dissolve
    show andrea_06 with dissolve
    andrea "A-ahh...?"
    "That was hotter than simply fucking her, wasn't it?"
    mc "Ah--! Shit!"
    "It was weird, but the thought was {i}consuming.{/i}"
    mc "Shit, shit, shit...!"
    "Yeah, it was so {b}FUCKING{/b} hot."
    mc "Christ, Andrea... you're..."


    menu:
        "Perfect."(chg=["andrea_up"]):
            $ w3AndreaRizz += 1
            mc "...incredible. {i}Beautiful.{/i} {b}Perfect.{/b}"
            "Honey flowed from my mouth, but venom seized my body."
            andrea "Mhhh..."
            "A low coo told me she didn't mind the adoration."
            mc "Andrea...!"
        "A whore. (w3AndreaDemean = True) [mod_chat]":

            $ w3AndreaDemean = True
            mc "You fuckin' bitch... you fuckin' whore...!"
            "I let the venom into my vocal chords."
            andrea "Ahh, ahhh-♥"
            "If she cared, the way she leaned into my musk didn't allow it to show."
            mc "Fuuuuuuck..."
            "She had heard worse, I'm sure."

    scene w3_8877 with dissolve
    mc "Ah... *ahem* Put your hands up!"
    scene w3_8878 with dissolve
    "To say I got a {i}little{/i} lost would be an understatement."
    andrea "Uhhh...?"
    play sound "sound effects/slap1.wav"
    scene w3_8879 with hpunch
    andrea "A-ahh...?!"

    if w3AndreaDemean == True:
        mc "Don't make me ask twice! Now, puppy dog!"
    else:
        mc "C'mon, like a puppy dog..."

    scene w3_8880 with dissolve
    andrea "....mmmhhh?"
    "She got the picture."
    mc "Tongue out!"
    scene w3_8881 with dissolve
    "She got the picture, and {i}complied.{/i}"
    mc "Aaaahh-!"
    "Despite the change in temperature, not missing a single fucking beat, Andrea answered me faithfully by sliding her tongue underneath my cockhead."
    play ambient "sound effects/fap2.mp3"
    scene andrea_07_a with dissolve
    show andrea_07 with dissolve

    if w3AndreaDemean == True:
        mc "A-aaahh..! Just stay like!"
        "So, I ran away with the feeling."
        mc "Ah, mmhh...! I'm going to jizz all over your slutty face!"
    else:
        mc "A-aaahh..! Just stay like that, darling!"
        "So, I ran away with the feeling."
        mc "Ah, mmhh...! I've got something for you!"


    "{i}I followed the impulse.{/i}"
    mc "Ah, haaa...!"
    "Using Andrea like a cum rag...!"
    mc "F-fuck...!"
    "Stroking my cock...!"
    mc "Fuck, fuck, fuck...!"
    "High on the feeling of standing above a gorgeous, star-studded adult actress...!"
    "{i}Me.{/i}"
    "[mcf]."
    "{b}Stroking my cock.{/b}"
    "My God-given, massive cock."
    mc "Ahh... ahhaaa...."
    "In moments like this, this job really was the fucking best..."
    "How many people would trade to be in my place? How many people whacked off to this woman?"
    mc "Hnnggg...!"
    "My moans turned to growls."
    mc "Hnnngg, haaaa...!"
    "Waves of sexual pleasure softened my stance."
    mc "Ahh, hnnggg...!"
    "I felt that familiar tingle in my ankle, and the fleeting numbness in my toes..."
    mc "Oh, fuck..."
    "All sense of self accumulated in my cock as I peppered it with uneven strokes."
    mc "Oh, fuck... oh, fuck... oh, fuck...!"
    "Engorged as it was, bloated and red with hues of purple, it was such an ugly son-of-a-bitch when compared to the beautiful countenance buried underneath it."
    mc "Annhhh...♥"
    "Yet, waving it around and subjecting her delicate features to its vein-ridden, grotesque majesty felt so, so, so, so, so, so, SO right."
    mc "Hnngg, ggaah...!"
    "So, so, so, so {size=+10}{b}FUCKING{/b}{/size} right."
    mc "Andrea, I'm, aahhh..."
    "More and more my cock burned."
    mc "Oh, fuck...!"

    menu:
        "Command her to bark! (w3AndreaBark = True)":
            $ w3AndreaBark = True
            scene w3_8882 with dissolve
            mc "B-bark--!"
            scene w3_8883 with dissolve
            andrea "...eeuuhh?"
            scene w3_8882 with dissolve

            if w3AndreaDemean == True:
                mc "Bark you fucking bitch!"
            else:

                mc "Bark for me, baby!"

            scene w3_8884 with dissolve
            andrea "Arf, arf...?!"
            scene w3_8885 with dissolve
            "She didn't expect the request, but she quickly adapted."
            mc "Ahh...!"
            mc "Puppy hungry?"
            scene w3_8886 with dissolve
            andrea "...arf, wwharf?"
            scene w3_8885 with dissolve
            "Again she promptly complied with my strange and fevered request. {b}This woman was a pro.{/b}"
            mc "F... f-fuck...!"
            scene andrea_07_a with dissolve
            show andrea_07 with dissolve

            if w3AndreaDemean == True:
                mc "Beg for it, bitch!"
            else:
                mc "Beg for it!"

            "Then again, I can imagine she fields weirder requests at the club..."
            andrea "Arf, arff..!"
            mc "Aahh, aahh...!"
            "More and more my turgid cock grew heavy, nearing release..."
            andrea "Arf, arf!"
            "Sperm and seminal fluid mixed in the back of my urethra."
            mc "Ahhh, hhaaaa--"
            andrea "{b}Wharf, arf...!{/b}"
            "Andrea kept cutely barking, and the message to my spinal chord was sent--"
        "Don't get {i}that{/i} lost, weirdo. Appreciate her.":

            "While she reminded me of a dog, I would keep that to myself."
            scene w3_8885 with dissolve
            mc "Ah, hhaaa...♥ {b}Andrea...!{/b}"
            scene w3_8886 with dissolve
            andrea "Mmmhhh...!"
            scene w3_8885 with dissolve
            "The bimbo cooed in response to the affection I put into her name."
            mc "Oh, fuck, fuck, fuck...!"
            scene w3_8886 with dissolve
            andrea "Whhhmmchomefourmeeeh,bbeebbb...!"
            scene w3_8885 with dissolve
            "...and offered encouragement, the best she could, while still keeping to task keeping her pert little tongue out."
            scene andrea_07_a with dissolve
            show andrea_07 with dissolve
            mc "Hnngg, hnnnggg...!"
            "Jacking off had never felt so streneous before."
            mc "Hhnnng, aa-aaaahh...♥♥"
            "My hand strained from how hard I was gripping my cock, my head pulsed from the sheer focus."
            mc "Hnnnggg, hgggaaaah...!"
            "I felt my heart beat in my palm."
            mc "Ahh, hnnggg--"
            "Thump."
            "Thump. Thump."
            "{i}Thump.{/i}"
            mc "Aaah, hheeehh--"
            "I gnashed my teeth, calling out like a beast, and--"


    mc "H-here, e-eat--"
    play sound "sound effects/spurt.wav"
    stop music
    stop ambient
    scene andrea_08_a with flash
    show andrea_08 with dissolve
    play ambient "sound effects/gulp3.mp3"
    mc "Ah, uuuuuuhuhp...!"
    "Quick and powerful contractions funneled strands of jizz into Andrea's receptive mouth."
    andrea "Mhh, mmhmhhh...!"
    "{i}She was good.{/i}"
    andrea "MMmhh, mmaaaa... *gulp* Mmhh...!"
    "She took every drop as it came, gulping it down to make room for me."
    andrea "*Gulp, gulp* MMhh, mmhhh..."
    mc "Ahh... ahhh..."
    "No coughing, no sputtering, no fighting it... she sealed the head of my cock with her lips, doing her best to stick to that \"not a drop\" mission."
    mc "T-there it is...!"
    "It wasn't a complete success, as through the excitement I hadn't quite made it into her mouth fully, but the bits that escaped her lips thankfully found perch in the tanned valley below."
    mc "Mmhh, hhaaa..."
    stop ambient
    scene w3_8887 with dissolve
    mc "Oh, fuck..."
    "Despite guzzling down a load, the look on Andrea's face was implacable."
    scene w3_8888 with dissolve
    andrea "Mmmhh..."
    "She didn't leave a drop..."
    mc "...I don't know what came over me."
    play music "music/lobby-time.ogg"
    play sound "sound effects/thud-floor.mp3"
    scene w3_8889 with hpunch
    "{i}That succubus.{/i}"
    andrea "Heah... you came {i}in{/i}, not {b}over!{/b}"
    "She laughed at her own joke, having taken my load in complete stride."
    scene w3_8890 with dissolve
    andrea "...heh, that was fun! If only we had more time..."
    scene w3_8891 with dissolve
    mc "You're a fucking doll..."
    scene w3_8892 with dissolve
    andrea "Mmmhh... heheh... we should do this again.."
    scene w3_8894 with dissolve
    mc "...yeah?"
    scene w3_8890 with dissolve
    andrea "...uhuh, you can call on me anytime. You don't have a best girl yet, right?"
    scene w3_8891 with dissolve
    mc "...best girl?"
    scene w3_8890 with dissolve
    andrea "Yeah! Y'know, someone you can rely on in a pinch! For fun!"
    scene w3_8891 with dissolve
    mc "I can't say I have anyone like that..."
    scene w3_8893 with dissolve
    andrea "Mmhhh..."
    "She nuzzled my stomach, basking in the warmth, like a dog sitting at her master's feet."

    if not persistent.w3AndreaPublic:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3AndreaPublic = True

    scene w3_8895 with dissolve
    "........."
    scene w3_8896 with fade
    "......"
    scene w3_8897 with dissolve
    mc "You should probably fix your clothes..."
    $ renpy.end_replay()
    scene w3_8898 with dissolve
    andrea "Ahh, in a minute. Who cares about Genine?"
    scene w3_8897 with dissolve
    mc "I believe you did..."
    scene w3_8899 with dissolve
    andrea "Heeeugh.... such a stickler about schedules, yet, ha! I've seen her spreading her legs for Daddy Don on the clock!"
    scene w3_8898 with dissolve
    andrea "I'll just say I'm doing some research for my next part, heheah, hee...♥"
    scene w3_8896 with dissolve
    "On the tail end of a contented murmur, she laughed exuberantly at her own dumb joke."
    scene black with fade
    if mod_var:
        $ mod_var = False
        m_dev "Time to fuck the air head"
        jump w3AndreaQuickie
    show screen textbox2 with dissolve

    if hanaGF == True:
        mc "By the way... I'd prefer if you didn't mention this to Hana..."

    "......"
    "...she did eventually get dressed, and we whittled down the remaining time with idle conversation."
    jump w3DonovanMeet

label w3AndreaQuickie:
    stop ambient
    play music "music/six-days-of-heat-pt2.ogg"
    scene w3_8900 with dissolve
    mc "Oh, fuck...!"
    andrea "Ha, haa... oh, I know {i}that{/i}--"
    scene w3_8901 with dissolve
    "I let my lust overtake my sense, because..."
    andrea "Oh, ohh...?!"
    scene w3_8902 with dissolve
    "In for a penny, {i}in for a pound.{/i}"
    andrea "Haa....!"
    scene w3_8903 with dissolve
    "We were already being adventurous, and while it was true that I wouldn't go {b}four rounds{/b}, I was aiming for a first round knockout."
    play sound "sound effects/spurt.wav"
    scene w3_8904 with hpunch
    andrea "Ah, aheeeeeee!"
    "In one swift motion, I effortlessly hilted myself balls deep inside Andrea."
    mct "(Oh, fuck!)"
    scene andrea_09_a with dissolve
    show andrea_09 with dissolve
    andrea "N-nice--"
    "Go, go, go, {b}GO!{/b}"
    "Turns out, a porn star's cunt was a cunt like any other, which was to say--"
    mc "Oh, fuck. Oh fuck, fuck, {b}fuck...!{/b}"
    "{b}It felt fucking amazing!{/b}"
    andrea "Mmmh, aaahh...!"
    "Neither of us spoke words, we just immediately descended into a rut."
    "In this kind of position, it was me leading the show."
    "My hands seized Andrea's flesh with an iron grip, and every plunge into her quim was intended to discombobulate and knock what little sense the bimbo had out of her head."
    "Yet, she instantly picked up on my rugged tempo. Despite the lack of rhythm or pattern, she moved her hips with razor-thin timing, catching me at the apex of every thrust and pulling me in {i}deep.{/i}"
    scene andrea_09b_a with dissolve
    show andrea_09b with dissolve
    mc "Gh, hhnnn...!"
    "A combination of skill, experience, and instinct."
    andrea "Nh! Nhhh...!"
    "The manifestation of a simple, but important ethos."
    mc "Ghh! Hnn...!"
    "{i}Make the other person happy.{/i}"
    andrea "Nnhh, hhnnn...!"
    "The only discordant element to our dance was our grunts, which tripped over each other like trying to get in the last word."
    mc "Ah, h-haaah!"
    "In the back of my mind, I knew that a glass window and a curtain were all that separated our romp from the editors outside toiling away at stitching together adult videos."
    andrea "Hnng, hnnggg..!"
    "There was a {i}humor{/i} to that which I appreciated."
    mc "Ha, haaa, haha...!"
    "I laughed."
    andrea "Heah, he--"
    "Andrea followed suit, both of us pulled into the mania of the situation."
    "{i}I felt mad{/i}, bordering on delirious."
    "I was getting a taste for this kind of sex, indeed."
    "Quick, rough, without pretense..."
    mc "--!"
    "...no rest, either, just bits maddeningly mashing together in a frenzied daze."
    andrea "Ah, hhaaa, haaa-!"
    scene andrea_09c_a with hpunch
    show andrea_09c with dissolve
    mc "Haaa, haaa...!"
    "I latched my fist around Andrea's beautiful red hair--"
    mct "(Fuck, fuck, fuck...!)"
    "The careening was taking its toll on my hips."
    mct "(Fuck, fuck, fuck, {b}FUCK!{/b})"
    "Every time I collided into the slut, my legs went numb and my ass burned from tightened muscles."
    "Every time my balls slapped against Andrea's thighs, a violent bliss robbed me of reason."
    "It wasn't so much a race anymore but rather a fireball rolling down the road to a charred end."
    "My vision narrowed, and even Andrea disappeared."
    mc "Fwahh, ffwwwwahhhh...!"
    mct "(FUCK, FUCK, FUCK, FUCK, FUCK, {i}fuck.{/i})"
    stop ambient
    stop music
    play sound "sound effects/spurt.wav"
    scene andrea_10_a with flash
    show andrea_10 with dissolve
    play ambient "sound effects/gulp3.mp3"
    andrea "Ehhyyygyeeeeaahhhhh....!"
    "We couldn't make a mess, and so I flooded Andrea's inside without a second thought."
    andrea "Mmmhhh...!"
    "Hot cum pipped through my urethra, and Andrea bucked back into me, driving me deeper, {i}grinding{/i}, extracting every rope she could from me."
    mct "(Ahhh, ffhuuu-!)"
    "I gripped the redhead so hard that my arms hurt."
    andrea "Haa, haaaa... "
    stop ambient
    scene w3_8905 with dissolve
    "........."
    "......"
    "...by the time my sense came back to me, I expected to feel stupid, yet--"
    scene w3_8906 with dissolve
    mc "Heh, I don't know what came over me."
    "I just felt on top of the world, having just fucked a woman I'm sure many men dream and fantasize about..."
    scene w3_8907 with hpunch
    andrea "Heah... you came {i}in{/i}, not {b}over!{/b}"
    "She laughed at her own joke, having taken my load in complete stride."
    play music "music/lobby-time.ogg"
    scene w3_8908 with dissolve
    andrea "...heh, that was fun! If only we had more time..."
    scene w3_8909 with dissolve
    mc "You're a fucking doll..."
    scene w3_8910 with dissolve
    andrea "Mmmhh... heheh... we should do this again.."
    scene w3_8912 with dissolve
    mc "...yeah?"
    scene w3_8910 with dissolve
    andrea "...uhuh, you can call on me anytime. You don't have a best girl yet, right?"
    scene w3_8912 with dissolve
    mc "...best girl?"
    scene w3_8913 with dissolve
    andrea "Yeah! Y'know, someone you can rely on in a pinch! For fun!"
    scene w3_8909 with dissolve
    mc "I can't say I have anyone like that..."
    scene w3_8911 with dissolve
    andrea "Mmhhh..."
    "She nuzzled my chest, basking in the warmth, like a dog resting at her master's side."

    if not persistent.w3AndreaPublic:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3AndreaPublic = True

    scene w3_8914 with dissolve
    "........."
    scene w3_8915 with dissolve
    "......"
    scene w3_8916 with dissolve
    mc "You should probably fix your clothes..."
    $ renpy.end_replay()
    scene w3_8917 with dissolve
    andrea "Ahh, in a minute. Who cares about Genine?"
    scene w3_8916 with dissolve
    mc "I believe you did..."
    scene w3_8917 with dissolve
    andrea "Heeeugh.... such a stickler about schedules, yet, ha! I've seen her spreading her legs for Daddy Don on the clock!"
    andrea "I'll just say I'm doing some research for my next part, heheah, hee...♥"
    scene w3_8915 with dissolve
    "On the tail end of a contented murmur, she laughed exuberantly at her own dumb joke."
    scene black with fade
    show screen textbox2 with dissolve

    if hanaGF == True:
        mc "By the way... I'd prefer if you didn't mention this to Hana..."

    "......"
    "...she did eventually get dressed, and we whittled down the remaining time with idle conversation."
    jump w3DonovanMeet

label w3DonovanMeet:
    scene w3_8918 with fade
    if w3AndreaFoolAround == True:
        "When the time came, Genine led Andrea and me to the small conference room opposite of where we fooled around."
    else:
        "When the time came, Genine led Andrea and me to the small conference room opposite from where we chatted and ran down the clock."

    "Inside, waiting for us, was a middle-aged man whose features were best described as somewhere between slimy and debonair."
    scene w3_8919 with dissolve
    "As we moved in closer, I immediately tried to get a read on the silver fox."
    "He possessed a waning handsomeness, dulled by time, yet still sharp enough to disarm with a smile."
    scene w3_8920 with dissolve
    don "Andrea! Doll!"
    "--and smile he did, as Andrea scrambled into his arms."
    andrea "Daddy Don!"
    "He was well-groomed, yet not enough to feel ostentatious. His long, neat hair had a healthy shine, yet he didn't attempt to cover up the greyness."
    "It gave him a rather {i}wise-lookin{/i} quality..."
    scene w3_8921 with dissolve
    andrea "Hey, hey, hey!"
    "In addition, the open display of affection between the bimbo and her boss was enough to paint an easy-going, laid-back picture of the man."
    andrea "Thanks for taking my call!"
    "Andrea's information about the man seemed reliable."
    scene w3_8922 with dissolve
    don "Aw, I always have time for you, Ann. How's your sister?"
    scene w3_8923 with dissolve
    andrea "7 months sober!"
    "By all accounts, I {i}felt{/i} he was a good man."
    scene w3_8922 with dissolve
    don "That's great to hear!"
    "Yet, despite my overwhelmingly positive impression..."
    stop music
    play sound "sound effects/finger-snap.wav"
    scene w3_8924 with dissolve
    "Something clicked in my head. I felt... {b}uneasy.{/b}"
    andrea "This is [mcf]! Say hello, boss! Uh... both bosses!"
    "There was uncanny familiarity to his face that I couldn't place, and that put me on guard."
    play music "music/hypnosis.ogg"
    scene w3_8925 with dissolve
    don "Hello, [mcf]. I appreciate you coming in to see me on such short notice."
    "{i}Familiar{/i}, pervading dread."
    scene w3_8926 with dissolve
    don "It's nice to meet you. My name is Donovan Gun, {b}director.{/b}"
    "...and that was when it hit me like a bag of bricks. His rugged voice, and the star-quality emphasis he put on his own name..."
    scene w3_8927 with dissolve
    "{i}Donovan Gun.{/i} The company name I didn't recognize, but he was a man known to me."
    "........."
    "......"
    scene w3_8928 with dissolve
    mct "(...)"
    "{i}My stomach flipped.{/i}"
    scene w3_8929 with dissolve
    "Just as Dr. Van Doren alluded to, Morehead Hill's pornography scene was indeed a {i}small{/i} industry. My mind immediately tried to recall the video I'd seen him in, but..."
    hide screen textbox2 with dissolve
    scene w3_8936 with pixellate
    "...to no avail."
    "In the excitement, I was drawing a blank."
    "..............."
    scene w3_8929 with pixellate
    show screen textbox2 with dissolve
    "............"
    "........."
    "......"
    scene w3_8928 with dissolve
    don "...you okay, son?"
    hide screen textbox2 with dissolve

    menu:
        "...don't call me that.":
            scene w3_8930 with dissolve
            show screen textbox2 with dissolve
            mc "I'd appreciate it if you didn't call me that."
            scene w3_8931 with dissolve
            "I was in a tizzy. It was an odd, abrasive response but it was also an honest-to-God gut reaction to that choice word."
            "For a moment, he might have thought it rude... but in a flash--"
            scene w3_8932 with dissolve
            don "Got it! A little too familiar, too fast."
            "He course corrected, as if he was the one making the faux pas."
            scene w3_8933 with dissolve
            mc "Yeah... {size=-15}that's it...{/size}"
            don "Uh, you okay, [mcf]?"
        "Fight past your unease and greet him enthusiastically.":

            scene w3_8934 with dissolve
            show screen textbox2 with dissolve
            mc "I'm a, uh... I'm a {i}fan{/i} of your work."
            scene w3_8935 with dissolve
            don "Oh, yeah?"
            scene w3_8934 with dissolve
            mc "Well, I've seen some of it..."
            "I said it, inwardly hoping to laugh, but I didn't find it that funny. Instead, it just made the sickening feeling worse."


    scene w3_8937 with dissolve
    mct "(Focus, focus, focus on why you're here {b}MORON!{/b} Process this shit later!)"
    stop music
    play sound "sound effects/finger-snap.wav"
    scene w3_8939 with dissolve
    "........."
    "......"
    scene w3_8938 with dissolve
    mc "...I'm sorry to trouble you about all {i}this{/i}, Mr. Gun."
    play music "music/lobby-time.ogg"
    scene w3_8939 with dissolve
    don "{i}Donny{/i}."
    scene w3_8940 with dissolve
    mc "When I asked Andrea if she had seen Isla, I didn't know I was overstepping a... {b}boundary.{/b}"
    scene w3_8941 with dissolve
    don "Oh, no! It's a free country! Plus, you had a good reason, too!"
    scene w3_8942 with dissolve
    don "Love, right? I'm a big fan of it!"
    scene w3_8940 with dissolve
    mc "Uh, huh..."
    mct "(If that's the case, why am I here...?)"
    scene w3_8941 with dissolve
    don "You haven't done anything wrong, {i} I think.{/i}"
    scene w3_8943 with dissolve
    mc "...you aren't certain?"
    scene w3_8944 with dissolve
    "For the first time, the older gentleman looked {i}serious.{/i}"
    "His smile shrank, as if to signify he was moving onto business."
    scene w3_8945 with dissolve
    don "Sit."
    scene w3_8946 with dissolve
    don "And would you give us the room, sweetheart? I'd like to talk to [mcf] man-to-man."
    scene w3_8947 with dissolve
    andrea "You got it! Hehe!"
    scene black with fade
    "......"
    don "...well, you see, my old friend sent Isla to me for \"safekeeping\"; told me there was some trouble with a boyfriend..."
    scene w3_8948 with dissolve
    "I pushed our obvious connection out of my mind, and instead focused on the word {i}safekeeping.{/i} It rang odd."
    scene w3_8949 with dissolve
    mc "...that old friend being one of my bosses, August, right?"
    scene w3_8950 with dissolve
    don "The one and only."
    scene w3_8948 with dissolve
    "{i}August sent Isla off himself a month before Darius vanished...?{/i}"
    scene w3_8951 with dissolve
    don "He was, among many things, a mentor. So... when he asks me to keep an eye on a girl, I take it seriously, even if it's a {i}little brother{/i} asking."
    scene w3_8949 with dissolve
    mc "He'll vouch for me. Did Andrea--"
    scene w3_8950 with dissolve
    don "She did. You're taking up in Isla's boyfriend's old place."
    scene w3_8952 with dissolve
    mc "That's right, but more than just some stuff I found..."
    scene w3_8953 with dissolve
    "Well, without a doubt, Ian and I looking into Darius would make it back to August -- and while I would've liked to avoid that, it is also easily explained..."
    scene w3_8952 with dissolve
    mc "...my best friend was looking for a way to contact Darius. He knew him pretty well, and he's worried about him after he split. He thought that maybe she might have a way, but I had NO idea he had done anything that warranted hiding her from him."
    scene w3_8953 with dissolve
    "--and neither did Dalia, for that matter?"
    scene w3_8954 with dissolve
    "{i}That seemed weird.{/i}"
    mct "(Did she not mention it on purpose...? Like what the fuck, Dalia!)"
    scene w3_8955 with dissolve
    "For a moment, it seemed it was Donovan's turn to take stock of me."
    scene w3_8956 with dissolve
    don "...I don't know the details, exactly. All Auggy said was that they needed to stay separated from each other, before things turned... {i}ugly.{/i}"
    scene w3_8955 with dissolve
    "Was that ugliness he alluded to the old woman's blackmail? Maybe it was unrelated...?"
    scene w3_8957 with dissolve
    don "So, I set her up in the suburbs and gave her a job."
    scene w3_8958 with dissolve
    mc "... performing in porn?"
    scene w3_8959 with dissolve
    don "Nah! She's running our day care!"
    scene w3_8960 with dissolve
    mc "...you pulling my leg?"
    scene w3_8959 with dissolve
    don "Nope! {i}Serious.{/i} Not that I don't pay them enough, but it helps to cut down on a few of our girls' expenses when they're on a shoot."
    scene w3_8961 with dissolve
    "...huh, {i}he really was a good boss.{/i}"
    scene w3_8953 with dissolve
    "Unfortunately, my mind turned away from the pressing issue, and tried to recall any strange babysitters I had as a kid..."
    scene w3_8962 with dissolve
    "........."
    "......"
    mct "(...uh, he must not offered that service back then?)"
    scene w3_8953 with dissolve
    "{b}Stop thinking about that!{/b}"
    scene w3_8952 with dissolve
    mc "Well, I understand if you won't allow me to talk to Isla."
    scene w3_8963 with dissolve
    don "Actually, I've already confirmed that you didn't even know the guy. I just wanted to lay eyes on you."
    scene w3_8964 with dissolve
    don "Whether she'll see you or not is up to her, but I'll let her know someone from the club is looking for her."
    scene w3_8965 with dissolve
    mc "I would {i}greatly{/i} appreciate that."
    scene w3_8964 with dissolve
    don "I wouldn't get my hopes up, she doesn't like even thinking about her old work or the people there."
    scene w3_8948 with dissolve
    "......"
    scene w3_8966 with dissolve
    don "...say, how does someone your age get into that shit show of a place, anyway?"
    scene w3_8949 with dissolve
    mc "Good ol' nepotism. Previously mentioned best friend is one of the owners' nephew."
    scene w3_8950 with dissolve
    don "Charles Kohler?"
    scene w3_8949 with dissolve
    mc "You know him?"
    scene w3_8951 with dissolve
    don "Everyone in the city knows {i}of{/i} him. Never met the man. I was shocked to learn he was part of Auggy's enterprise."
    scene w3_8949 with dissolve
    mc "He advised my physics club, actually."
    mc "Still, you've never been to the club? He's always there. I figured that since you guys have something of an exchange program with the house girls that--"
    scene w3_8950 with dissolve
    don "That's off the books."
    scene w3_8949 with dissolve
    mc "...the entirety of the business is off the books."
    scene w3_8967 with dissolve
    don "Ha, good point! But to answer your question, no, I've never set foot there. It's not really my kind of place, I prefer an... {i}honest{/i} living."
    scene w3_8968 with dissolve
    "While the word honest seemed funny considering he produced smut, I could appreciate he operated out in the open."
    scene w3_8969 with dissolve
    don "There's no way in hell I'd get my family wrapped up in a stressful situation with the law."
    scene w3_8953 with dissolve
    "......"
    scene w3_8952 with dissolve
    mc "...how long have you been doing this, Donny?"
    scene w3_8953 with dissolve
    don "I'm approaching on 25 years."
    scene w3_8970 with dissolve
    mc "...and how could that be? You don't look older than 35."
    scene w3_8971 with dissolve
    don "Ha! Already bustin' my balls?!"
    "As another round of silence ushered us to the end of our meeting, the anxiety I had set aside from meeting a man with ties to my mother's former {i}career{/i} came careening back inside my periphery."
    scene w3_8962 with dissolve
    "Just the other night, the thought of her knowing August had sent me into a panic, but this..."
    "Without realizing it, {i}I liked this guy.{/i} He seemed decent, and I was now well acquainted with the {i}less{/i} decent..."
    scene w3_8953 with dissolve
    "{i}An inexplicable fact that lessened the knot my intestines were in.{/i}"
    mct "(At least I'm not working for the guy...)"
    "........."
    "......"
    scene w3_8954 with dissolve
    "...yet, the more I ruminated on it, the more I didn't like it."
    "My head tried to recall the video, yet--"
    don "You look green. Are you feeling sick?"
    scene w3_8972 with dissolve
    mc "*Ahem* Uh..."
    scene w3_8954 with dissolve
    "{i}Stop thinking about it.{/i}"
    scene w3_8953 with dissolve
    "Why the FUCK do I even need to picture the video? What does that help? What perspective would it add...?"
    scene w3_8973 with dissolve
    mc "Thank you for your time."
    "Yet it gnawed away at my inside."
    don "I'll pass it through Ann when I learn if Isla agrees to see you or not."
    scene w3_8974 with dissolve
    "Stop."
    "Stop. Thinking."
    "Stop. Thinking. About."
    "Stop. Thinking. About. It."
    scene w3_8975 with dissolve
    mc "Yep! It was good to meet you, Donny!"
    don "Ummm..."
    scene w3_8976 with dissolve
    don "Same, [mcf]."
    stop music fadeout 3.0
    scene black with fade
    "..............."
    "..........."
    "......."
    "..."
    "On the way home, against my better sense, I resumed my attempt to recall {i}which{/i} video I knew Donovan from."
    hide screen textbox2 with dissolve
    scene vpt_memory1_a with pixellate
    show vpt_memory1
    "{i}I couldn't{/i}."
    "The impression of Donovan Gun existed within my head, but it was all a blur."
    "That was likely a good sign, right? {i}It wasn't worth remembering.{/i}"
    "But it was precisely my inability to recall it that made me... {i}curious...{/i}"
    "{i}A desire to self-flagellate...{/i}"
    hide screen textbox2 with dissolve

    menu:
        "...okay, seriously, stop thinking about it.":
            stop ambient
            scene black with pixellate
            "Quickly, I wiped the impression from my mind like cleansing paint from a palate."
            "Deep down, despite pretending there was meaning to my recollections, I understood that I was merely exacerbating a hole in my heart."
            "{i}Stop thinking about it.{/i}"
        "That sickness in your stomach {i}is{/i} an old friend.":
            play music "music/leaving-home.ogg"
            "I asked myself, what was even the point, other than further irritation?"
            "I liked to pretend there was meaning to my dreary recollections, but the past was the past, and deep down I understood I was exacerbating a hole in my heart."
            "I understood that, and I knew I should wipe away the image from my mind, yet..."
            play ambient "sound effects/moan2.mp3"
            scene vpt_memory2_a
            show vpt_memory2 with dissolve
            "I. {w}Was.{w} Curious."
            vic "{size=-15}{font=/gui/fonts/MB-Thin_Worms.ttf}B-biiigg-!{/font}{/size}"
            "The irritation I felt was as nostalgic as an old friend."
            don "{size=-15}{font=/gui/fonts/MB-Thin_Worms.ttf}Look at you! I'm not even moving, sweetheart!{/font}{/size}"
            "Other tableaus of depravity hung provocatively in my memory, easily recalled with disgust, but this..."
            vic "{size=-15}{font=/gui/fonts/MB-Thin_Worms.ttf}N, no- I'm just--!{/font}{/size}"
            "{i}I was curious.{/i} What kind expression did she make?"
            "I {b}loathed{/b} myself for asking that question, but it was there, twisting inside of me..."
            "{i}My wish to understand her,{/i} and my inability to do so."
            stop ambient fadeout 3.0
            stop music fadeout 3.0
            scene black with pixellate
            "I thought about it all the way home, and I was no better for it."

    "......"
    "..."
    jump w3RosalindDinnerPrelude

label w3RosalindDinnerPrelude:
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionrosalind06 with blinds
    $ renpy.pause(6, hard=True)
    play sound "sound effects/door-close.wav"
    scene w3_8977 with blinds
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    "I returned, groceries in hand, mind racing."
    "All this Darius stuff, meeting Donovan, even Rosalind's predicament..."
    play music "music/i-love-my-mom.ogg"
    scene w3_8978 with dissolve
    "{i}Those were for later.{/i}"
    "Tonight had a singular focus."
    scene w3_8979 with dissolve
    "{i}Make a nice dinner.{/i}"
    "Life was a series of moments, some good and some unfavorable, but each was an individual island set in time."
    scene w3_8980 with dissolve
    "So, from this one to the next, I took aim for a pleasant departure."
    scene w3_8981 with dissolve
    "For me, AND for the {i}enduring{/i} mother playing my houseguest."
    mct "(.......)"
    scene w3_8982 with pixellate
    vic "...it might be a bit overcooked, but--"
    scene w3_8983 with dissolve
    mc "My favorite!"
    scene w3_8984 with dissolve
    vic "......"
    scene w3_8985 with dissolve
    vic "...you said that about the pasta last week!"
    scene w3_8986 with dissolve
    mc "That was good! This will be good too!"
    scene w3_8987 with dissolve
    vic "...I should {i}really{/i} cook more, shouldn't I? Ah, I'm sorry I--"
    scene w3_8988 with dissolve
    "With fast food and corner stores, with modern life being steps removed from the harvest and slaughter..."
    scene w3_8989 with pixellate
    "I learned early on that you shouldn't take food made with love for granted."
    "It was excessively sentimental, but I wanted tonight's meal to reflect the warm lessons instilled in me. In that way, I'd put a little bit of my wonderful mother back into the world..."
    scene w3_8990 with dissolve
    mct "(I need a beer...)"
    scene black with fade
    play sound "sound effects/can.wav"
    "The words appeared in my head like an apparition."

    if w2ExKathleenAdvice == True:
        scene w3_8991 with w12
        mct "(First time I'd ever thought of them in my life, but..."
        scene w3_8992 with dissolve
        play sound "sound effects/gulp3.mp3"
        "*Gulp, {b}gulp!{/b}*"
        mct "(...a cold beer wasn't so bad on a hot day.)"
        scene w3_8993 with dissolve
        "........."
        "......"
        scene w3_8994 with dissolve
        mct "(...I can't believe that old bitch left Sophia's witch concoction with me as part of her \"homework\"...)"
        "I hadn't given a single fucking thought to it. It's jut been sitting in the back of my fridge."
        mct "(I hope I haven't lost the other shit she gave me.)"
        scene w3_8999 with pixellate
        mct "(...the fuck am I going to do with a whistle?)"
        mc "Hmmm..."
        mct "(Yet, I agreed to it...)"
        scene w3_9000 with fade
        "I had felt particularly malleable that night, and her words {b}seductive...{/b}"
        scene w3_8994 with pixellate
        mct "(Ha! I wonder how much this would fetch from Van Doren's competition?)"
        "Nothing else like it exists in the world... nothing I know of, at least."
        scene w3_8995 with dissolve
        play sound "sound effects/gulp3.mp3"
        "*Gulp, {b}gulp!{/b}"
        "Seems pretty fucking careless to leave it with some dumbass kid."
        mct "(Break into my fucking--)"
        scene w3_8996 with dissolve
        "Don't forget. {i}Pleasant{/i} departures, [mcf]."
        "My mind had started to wander, back to something I still didn't understand."
        "Instead, think of the good things in your life..."
        "The women, the friends, the {b}all expenses paid{/b} medical school."
        mct "(Who cares about that dumbass Darius? {i}Stay in your lane, idiot.{/i})"
        scene w3_8997 with dissolve
        "......"
        "...I suppose part of me found this \"haphazard\" investigation stimulating, while the other half needed to know."
        scene w3_8998 with dissolve
        play sound "sound effects/gulp3.mp3"
        mct "(...not that I would figure anything out.)"
        "{b}*Gulp, gulp, gulp!{/b}*"
        if w3MinaHotelFucked == True:
            play ambient "sound effects/ringing-inbound.wav"
            scene w3_9458 with dissolve
            "............"
            "........."
            "......"
            scene w3_9459 with dissolve
            mct "(...oh, it's me.)"
            play sound "sound effects/phonemenu.wav"
            stop ambient
            stop music
            scene black with fade
            mina "Heeeeeeeeeeey!"
        else:
            jump w3RosalindDinnerStart
    else:

        scene w3_9001 with fade
        mct "(First time I'd ever thought of them in my life, but..."
        scene w3_9002 with dissolve
        "*Gulp, {b}gulp!{/b}*"
        mct "(...a cold beer wasn't so bad on a hot day.)"
        scene w3_9001 with dissolve
        "........."
        "......"
        scene w3_9003 with dissolve
        "...try as I might to leave the day's previous business behind, one thought managed to float to the top."
        "{i}More of a feeling{/i}, really..."
        scene w3_9001 with dissolve
        "......"
        mct "(...what the hell am I doing?! Who cares about that dumbass Darius?!)"
        "Head down, idiot. {b}ALL{/b} expenses paid medical school."
        scene w3_9002 with dissolve
        "*Gulp, {b}gulp!*{/b}"
        "That would be the wise thing, wouldn't it?"
        mct "(Yes, indeed...)"
        scene w3_9001 with dissolve
        "Yet, I suppose part of me found this haphazard \"investigation\" stimulating..."
        mct "(Though, not like I've figured anything out so far...)"
        "{i}And it would be better if I didn't.{/i} If that moron got killed, what the fuck could I do about it?"
        "{i}Nothing.{/i}"
        scene w3_9003 with dissolve
        "......"
        "...the other half needed to know."
        "Pleasant departures, [mcf]. That was the night's itinerary. "
        scene w3_9001 with dissolve
        "Think of the good things in your life."
        scene w3_9002 with dissolve
        mct "(My mother, my friend, the beautiful woman I'm fixing dinner for...)"
        scene w3_9004 with dissolve
        "{b}*Gulp, gulp, gulp!{/b}*"
        if w3MinaHotelFucked == True:
            play ambient "sound effects/ringing-inbound.wav"
            scene w3_9001 with dissolve
            "............"
            "........."
            "......"
            scene w3_9460 with dissolve
            mct "(...oh, it's me.)"
            play sound "sound effects/phonemenu.wav"
            stop ambient
            stop music
            scene black with fade
            mina "Heeeeeeeeeeey!"
        else:
            jump w3RosalindDinnerStart

label w3MinaBeerCall:
    play music "music/ukulele-fun.ogg"
    scene w3_9461 with dissolve
    mc "Sunshine!"
    scene w3_9462 with dissolve
    mina "Sunshine?! You're making fun of me!"
    scene w3_9461 with dissolve
    mc "Just trying it on for size."
    scene w3_9463 with dissolve
    mina "You sound... {i}tired?{/i}"
    scene w3_9464 with dissolve

    if w3FeliciaMinaThreesomeEnd == True:
        mc "Hmm, I wonder the {b}whos{/b} and why of that, {i}kitten.{/i}"
        scene w3_9465 with dissolve
        mina "Oh! Heh, yeah..."
        mina "That waaaas.... {i}yeah.{/i}"
        scene w3_9466 with dissolve
        "I let the memory of our tryst with Felicia simmer in silence while Mina found the words."
        scene w3_9465 with dissolve
        mina "...I've been thinking about that all day."
        scene w3_9466 with dissolve
        mc "Oh? That vivid?"
        scene w3_9467 with dissolve
        mina "Shut up..."
        scene w3_9468 with dissolve
        "........."
        "......"
        scene w3_9472 with dissolve
        "..."
    else:

        mc "{i}Kinda am{/i}, but nothing talking to you won't mend."
        scene w3_9469 with dissolve
        mina "Long day?"
        scene w3_9464 with dissolve
        mc "Been sorting out some... \"extraneous\" matters related to work."
        scene w3_9469 with dissolve
        mina "Aw, poor working stiff."
        scene w3_9464 with dissolve
        mc "We can't all be beautiful."
        scene w3_9470 with dissolve
        mina "Hehe~"
        scene w3_9471 with dissolve
        "........."
        "......"
        scene w3_9472 with dissolve
        "..."

    scene w3_9473 with dissolve
    mc "How are you doing?"
    scene w3_9472 with dissolve
    mina "I'm gooooood, just thought I'd check in..."
    scene w3_9473 with dissolve
    mc "You'll be happy to know all my hands, fingers, and toes are accounted for then."
    scene w3_9472 with dissolve
    mina "Hehe, idiot..."

    if w3FeliciaMinaThreesomeEnd == True:
        scene w3_9474 with dissolve
        mina "It was fun with Felicia, but I hated not getting a chance to talk to you alone."
        mina "The other times we've... uh..."
        if w2MinaLovers == True:
            scene w3_9475 with dissolve
            mc "...made {b}love?{/b}"
            scene w3_9476 with dissolve
            mina "Shut up! I'm just saying {b}I like the what comes after, too!{/b} The talking!"
            scene w3_9477 with dissolve
            mc "I know what you meant. One-on-one time, I missed it too."
        else:

            scene w3_9479 with dissolve
            mina "I like what came afterwards, too."
            scene w3_9478 with dissolve
            mc "I know what you mean. One-on-one time, I missed it too."

        scene w3_9479 with dissolve
        mina "...you did?"
        scene w3_9478 with dissolve
        mc "{b}I did.{/b} You're an ace at cuddling."
        scene w3_9484 with dissolve
        mina "Pah! Ha!"
        scene w3_9481 with dissolve
        "......"
        scene w3_9478 with dissolve
        "..."
    else:
        scene w3_9474 with dissolve
        mina "It's just been a bit since we last talk, yeah?"
        scene w3_9475 with dissolve
        mc "Actually, it's been {i}too long{/i} since our last heart-to-heart."
        scene w3_9480 with dissolve
        mina "Shut up, we've never..."
        scene w3_9481 with dissolve
        mina "........."
        mina "......"
        scene w3_9479 with dissolve
        mina "...I guess that's our go to move."
        scene w3_9478 with dissolve
        mc "Definitely our tempo."

    mc "So, what have you been up to today?"
    scene w3_9482 with dissolve
    mina "Oh, resting at home... painting my toes nails..."
    scene w3_9483 with dissolve
    mc "Send me a picture."
    scene w3_9480 with dissolve
    mina "You just want a photo of my feet!"
    scene w3_9481 with dissolve
    mc "Ha! Not as naive as you look."
    scene w3_9484 with dissolve
    mina "Hehe..."
    scene w3_9485 with dissolve
    "{i}We shared a stupid laugh.{/i}"
    mc "When do you film your {i}Loving Days in Lafayette?{/i}"
    mina "Couple of weeks!"
    "{i}So we shot the shit for a little bit.{/i}"
    scene w3_9486 with dissolve
    mina "...you?"
    scene w3_9487 with dissolve
    mc "Oh, yeah, uh... actually... I'm cooking dinner for a friend who is staying with me."
    scene w3_9488 with dissolve
    mina "Friend? Someone other than Ian?"
    scene w3_9489 with dissolve
    mc "A woman from our work."
    scene w3_9488 with dissolve
    mina "Woman...?"
    scene w3_9489 with dissolve
    mc "Jealous?"
    scene w3_9490 with dissolve
    mina "N-no! I just didn't expect... how long is she staying?"
    scene w3_9491 with dissolve
    mc "Not much longer, I think. It's not my story to tell, but she got saddled with some trouble by her asshole husband and she needed a place to stay a few days while she finds her footing."
    scene w3_9492 with dissolve
    mina "Ah...! That's... that's good of you, [mcf]."
    scene w3_9491 with dissolve
    mc "You're not worried?"
    scene w3_9493 with dissolve
    mina "Pffh, it's..."
    mina "...it must be serious if she only has a co-worker to turn to."
    scene w3_9494 with dissolve
    mc "{b}Loan shark serious.{/b}"
    scene w3_9495 with dissolve
    mina "W-wha?! You're not in any danger, are you?!"
    scene w3_9496 with dissolve
    mc "Unlikely. Just making sure she doesn't get smacked around while things are being settled."
    scene w3_9495 with dissolve
    mina "Holy shit! You should... you should tell me about these things!"
    scene w3_9496 with dissolve
    mc "I just did."
    scene w3_9493 with dissolve
    mina "Yeah..."
    scene w3_9494 with dissolve
    "........."
    "......"
    scene w3_9497 with dissolve
    mina "...so, you gotta make dinner?"
    scene w3_9498 with dissolve
    mc "Shower first."
    scene w3_9497 with dissolve
    mina "Send me a pic..."
    scene w3_9498 with dissolve
    mc "Only if you trade me."
    scene black with fade
    mina "Deal!"
    scene w3_9499 with pixellate
    "{i}She, without a doubt, looked better than I did.{/i}"
    stop music fadeout 3.0
    scene black with pixellate
    "......"
    "..."
    jump w3RosalindDinnerStart


label w3RosalindDinnerStart:
    stop music fadeout 3.0
    scene black with fade
    play sound "sound effects/shower.wav"
    "A shower later, and I was ready to cook."
    stop sound
    scene w3_9005 with fade
    rose "Mmmhh... ah..."
    play music "music/mourning-dove.ogg"
    scene w3_9006 with dissolve
    rose "{size=-10}Smells...{/size}"
    rose "{size=-10}That smells...{/size}"
    scene w3_9007 with dissolve
    rose "...good."
    scene w3_9008 with dissolve
    rose "...you're home."
    scene w3_9009 with dissolve
    mc "Have a good nap?"
    scene w3_9010 with dissolve
    rose "Mmmh... must have. I didn't even hear you come in."
    scene w3_9011 with dissolve
    "The sleepy look on the older woman's face as she blinked the bleariness away was... {i}adorable.{/b}"
    mc "I'm just starting, so you catch some more if you want."
    scene w3_9012 with dissolve
    rose "........."
    scene w3_9014 with dissolve
    rose "......"
    scene w3_9013 with dissolve
    rose "...if you don't mind, I think I would rather watch you cook."
    scene w3_9015 with dissolve
    mc "Be my guest, although it won't be very interesting."
    scene w3_9016 with dissolve
    rose "Well, I've never had a man cook for me before..."
    scene w3_9017 with dissolve
    mc "...{b}never{/b}, never?"
    scene w3_9018 with dissolve
    rose "My husband pretended he couldn't even manage to cook an egg."
    scene w3_9017 with dissolve
    mc "{i}Pretended?{/i}"
    scene w3_9018 with dissolve
    rose "So, I'd baby him. I think there was {b}a lot{/b} of things he pretended he couldn't do or deliberately forgot..."
    scene w3_9019 with dissolve
    mc "And you put up with that? Never called him on it?"
    scene w3_9020 with dissolve
    rose "...ah, I don't know, maybe I liked it?"
    scene w3_9021 with dissolve
    mc "I bet you did a lot of solo-parenting, huh?"
    rose "...Rupert didn't like being the bad guy."
    scene w3_9022 with dissolve
    rose "Which is so funny that I'm forgetting to laugh..."
    mc "That's messed up."
    scene w3_9023 with dissolve
    rose "Yeah... well, obviously it didn't work out for me..."
    scene w3_9024 with dissolve
    mc "......"
    scene w3_9025 with dissolve
    mc "...sorry, I know I'm just saying stuff you already know. It takes for a strong person to raise a kid by themselves."
    scene w3_9026 with dissolve
    mc "You not only got to support another person, but you've got to be strong enough to support yourself."
    scene w3_9027 with dissolve
    mc "......"
    scene w3_9028 with dissolve
    mc "...but as strong and amazing as a person is, no one's perfect, and it can be a strain on the kid when they end up being tagged in to fill in some of the gaps."
    scene w3_9027 with dissolve
    mc "......"
    scene w3_9029 with dissolve
    mc "...ah, I'm rambling."
    scene w3_9030 with dissolve
    rose "........."
    rose "......"
    scene w3_9031 with dissolve
    rose "...so, is it a habit of yours to cook without a shirt?"
    scene w3_9032 with dissolve
    mc "I took a shower after I got in, and you were asleep, so... uh, should I go--"
    rose "N-no! No! You look..."
    scene w3_9033 with dissolve
    rose "*Ahem* {i}Don't.{/i} I don't mind..."
    rose "All you're missing is an apron and you could pass for Mr. May on my calendar."
    scene w3_9034 with dissolve
    "........."
    "......"
    scene w3_9035 with dissolve
    mc "...want me to go pick up an apron?"
    scene w3_9036 with dissolve
    rose "No!"
    "The girlish light in Rosalind's eyes was a nice treat."
    scene w3_9037 with dissolve
    mc "Heh, I don't mind! It's not a problem!"
    rose "{b}Gosh, you're so dumb!{/b}"
    scene w3_9038 with dissolve
    "........."
    "......"
    rose "...you had to fill in the gaps a lot when you were a kid?"
    scene w3_9039 with dissolve
    mc "Not as much as I wish I could've..."
    scene w3_9040 with dissolve
    rose "You wish your mom remarried?"
    scene w3_9041 with dissolve
    mc "That's a complicated question. If I say yes, it sounds like I'm admitting she wasn't enough -- {b}and she was!{/b}"
    scene w3_9042 with dissolve
    mc "She gave me enough love for two people. I just wish someone was there for her like she was for me, but I suppose sometimes you just have to make the best of what life gives you."
    scene w3_9043 with dissolve
    "......"
    scene w3_9042 with dissolve
    mc "...what about you?"
    scene w3_9040 with dissolve
    rose "...would I like to get remarried?"
    scene w3_9041 with dissolve
    mc "Yeah..."
    scene w3_9044 with dissolve
    rose "I haven't even gotten a divorce yet."
    scene w3_9041 with dissolve
    mc "Yeah, but once this is all behind you..."
    scene w3_9045 with dissolve
    "......"
    scene w3_9040 with dissolve
    rose "...I'd like to."
    scene w3_9041 with dissolve
    mc "...get remarried?"
    scene w3_9044 with dissolve
    rose "Or... {i}something{/i} resembling it."
    scene w3_9046 with dissolve
    scene black with dissolve
    m_dev "Hey, my master just wanted to let you know RoseTR is Rose Talk Rapport points and RoseTL is Rose Talk Lubrication points"
    m_dev "Like most points the more the better this will lead to you earning Rose openness points and allow you to invite Rose to stay and live with you"
    m_dev "{m_note} at the end picking the \"Full Deal\" will remove the option to invite her to stay"
    m_dev "Alirght my Master is getting upset at me with all this talk BACK TO THE GAME! Enjoy!"
    scene w3_9046 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "A beautiful woman like her should have no trouble.":
            show screen textbox2 with dissolve
            mc "I don't think a beautiful woman like you will have a problem with that."
            scene w3_9047 with dissolve
            rose "...uh huh."
        "Well, don't {i}settle{/i} again. (RoseTR +1)"(chg=["rosalind_up"]):

            $ w3RTalkRapport += 1
            $ Rosalind_Affection +=1
            show screen textbox2 with dissolve
            mc "Well, whatever you do, don't settle for an asshole like your last husband. You deserve a partner, not a dependent."
            scene w3_9048 with dissolve
            rose "..."

    scene w3_9049 with dissolve
    rose "It's just wishful thinking, anyway. And if I ever got there, I fear Nora is at that... {i}age.{/i}"
    rose "She's a mature girl, but I don't think she'd be receptive to someone new. Not after her dad disappeared on her..."
    scene w3_9050 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Put a hand on her shoulder. It wouldn't hurt to {i}try.{/i}":
            scene w3_9051 with dissolve
            show screen textbox2 with dissolve
            mc "Never know until you try..."
            scene w3_9052 with dissolve
            rose "... 'suppose its something to worry about in the future."
            scene w3_9053 with dissolve
            mc "Hey, that future is a few weeks from now, right?"
            rose "..."
        "She'll just make herself unhappy with that line of thinking. (RoseTR +1)"(chg=["rosalind_up"]):

            $ w3RTalkRapport += 1
            $ Rosalind_Affection +=1
            scene w3_9046 with dissolve
            show screen textbox2 with dissolve
            mc "That kind of thinking is just resigning yourself to loneliness."
            scene w3_9054 with dissolve
            rose "You just said sometimes you've got to make the best of what life gives you..."
            scene w3_9046 with dissolve
            mc "......"
            mc "...you make Nora sound like a great enough kid that she wants you to be happy. You might be surprised."
            scene w3_9055 with dissolve
            rose "Yeah... she's the best."

    scene w3_9056 with dissolve
    "......"
    scene w3_9057 with dissolve
    rose "...we end up talking about this kind of stuff a lot, huh?"
    scene w3_9058 with dissolve
    mc "That we do. I'm like a broken record sometimes."
    mc "So, why don't we throw out all that baggage tonight and put a pin on the parent shit."
    scene w3_9059 with dissolve
    mc "And since you've never had a man cook you a meal, what do you say we treat tonight as two people getting to know each other?"
    scene w3_9060 with dissolve
    rose "Hmmm..."

    if hanaGF == True:
        scene w3_9061 with dissolve
        rose "I don't think Miss Hana would appreciate you suggesting that, [mcf]."

        if roseFlag == True:
            scene w3_9058 with dissolve
            mc "She wouldn't appreciate our little arrangement either, to be honest..."
            scene w3_9063 with dissolve
            rose "That's true..."
            scene w3_9064 with dissolve
            mc "Besides, I'm not propositioning you for sex, Rose, just a night of conversation alongside a nice bottle of wine."
            scene w3_9062 with dissolve
            rose "......"
            scene w3_9063 with dissolve
            rose "...alright, that sounds {i}fun.{/i}"
        else:

            scene w3_9059 with dissolve
            mc "On the contrary, I think she'd appreciate the well meaning behind the suggestion."
            mc "I'm not asking you to have sex with me, Rose, just a night of conversation alongside a nice bottle of wine."
            scene w3_9062 with dissolve
            rose "......"
            scene w3_9063 with dissolve
            rose "...alright, that sounds {i}fun.{/i}"

    elif roseFlag == True:
        scene w3_9057 with dissolve
        rose "...we don't need that pretense, do we? If you want to--"
        scene w3_9058 with dissolve
        mc "I'm not angling for sex, Rose. Just a night of conversation, alongside a nice bottle of wine."
        scene w3_9062 with dissolve
        rose "......"
        scene w3_9063 with dissolve
        rose "...alright, that sounds {i}fun.{/i}"
    else:


        scene w3_9061 with dissolve
        rose "Getting to know each other? That's... {i}silly.{/i}"
        scene w3_9058 with dissolve
        mc "What's silly about breaking open a bottle of wine and having a nice night of conversation?"
        scene w3_9062 with dissolve
        rose "......"
        scene w3_9063 with dissolve
        rose "...I suppose nothing. That doesn't sound too bad, actually... {i}alright{/i}, that sounds fun."

    scene w3_9062 with dissolve
    "As always, she was quick to agree. If she was scoffing inward at the proposal, or was feeling put upon, she wouldn't show it. It was a bitter pill that, no matter what, our positions meant she would always be amenable to my suggestions."
    scene w3_9056 with dissolve
    "{i}It was what it was, though.{/i}"
    hide screen textbox2 with dissolve


    menu:
        "Give her a reaffirming touch. (RoseTR +1)"(chg=["rosalind_up"]):
            $ w3RTalkRapport += 1
            $ Rosalind_Affection +=1
            scene w3_9065 with dissolve
            show screen textbox2 with dissolve
            mc "Awesome."
            scene w3_9066 with dissolve
            rose "..."
        "She's made you a happy man.":

            scene w3_9067 with dissolve
            show screen textbox2 with dissolve
            mc "You've made me a happy man tonight, Rose."
            scene w3_9068 with dissolve
            rose "Oh, pleeeeease."

    scene w3_9069 with dissolve
    rose "...I suppose I should clean up? Maybe put on something nice?"
    mc "Hmmm...?"
    scene w3_9070 with dissolve
    rose "I mean, since {b}you're{/b} making a big deal out of it..."
    scene w3_9071 with dissolve
    mc "...what do you want to do? I don't mind either of us wearing what's comfortable."
    scene w3_9072 with dissolve
    rose "......"
    scene w3_9073 with dissolve
    rose "I... I'd like to wear something nice, for a change..."
    scene w3_9074 with dissolve
    mc "Nice attire for a nice evening, then."

    if roseFlag == True:
        scene w3_9075 with dissolve
        "........."
        "......"
        scene w3_9076 with dissolve
        rose "I'll... go take a shower."
    else:

        scene w3_9077 with dissolve
        rose "I'll go take a shower."

    stop music fadeout 3.0
    scene black with fade
    "In an instant, the kitchen got a whole lot lonelier."
    "......"
    "..."
    scene w3_9078 with fade
    "Our \"conversation\" began."
    "As they do, face to face."
    play music "music/just-stay.ogg"
    scene w3_9079 with dissolve
    rose "...remember this?"
    scene w3_9080 with dissolve
    "She was referring to the dress she wore the night we first met."
    scene w3_9081 with dissolve
    "A meager, frugal, modest thing."
    "{i}Simple{/i}, yet effective in its aims and blunt with its charms."

    if roseSeduceFlag == True:
        "Less showy than the one wielded in her bumbling attempt at seduction."

    if rosalindKilSolution == True:
        "1/3rd the price tag than the thin wisp of fabric strategically employed for our ménage à trois."

    scene w3_9080 with dissolve
    "This kind of straightforward, uncomplicated ensemble suited Rosalind perfectly."
    scene w3_9082 with dissolve
    mc "...I do. You wore it the night we met."
    scene w3_9083 with dissolve
    rose "It's an... {i}old{/i} thing. Older than Nora."
    scene w3_9084 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "You like old things.":
            scene w3_9085 with dissolve
            show screen textbox2 with dissolve
            mc "Lucky for you, I'm partial to old things."
            scene w3_9086 with dissolve
            rose "......"
            scene w3_9087 with dissolve
            mct "(...shit, that sounded a lot smoother in my head.)"
            scene w3_9083 with dissolve
            rose "I..."
            rose "...I like the look of you putting your foot in your mouth."
            scene w3_9085 with dissolve
            mc "You are a kind and generous woman."
        "It must be a favorite of hers. (RoseTR +1)":

            $ w3RTalkRapport += 1
            scene w3_9085 with dissolve
            show screen textbox2 with dissolve
            mc "...a lot of memories made in that dress, eh? A woman's time-worn, reliable battle armor."
            scene w3_9088 with dissolve
            "......"
            scene w3_9089 with dissolve
            rose "...perhaps. Or maybe I just can't let go of old things."
            rose "It's tighter than it used to be."
            scene w3_9090 with dissolve
            mc "Yet, I guarantee you've never looked better in it."
            mct "(Thank God for elastic.)"
            scene w3_9083 with dissolve
            rose "...well, it is something I'm comfortable in. It helped somewhat... I was nervous the night we met."

    scene w3_9091 with dissolve
    mct "(The night we met...)"
    scene w3_9092 with dissolve

    if roseTakeAdvantage == True:
        "...I let loose."
        mct "(How easy it was, huh?)"
        "Even now, after being exposed to much {b}more{/b}, the knowledge I could just reach across the table and have her..."
    else:

        "I instantly spilled my guts to this woman."
        mct "(Which is likely an indictment of my character, rather than hers... still...)"

    mct "(I'm weak to this woman...)"

    scene w3_9093 with dissolve
    "Briefly, I imagined myself 10 years older, and under different circumstances..."
    "Could I be satisfied with domestic minutia?"
    "That my mind would even wander there maybe shone light on an uncovered desire..."
    scene w3_9094 with dissolve
    mc "You looked small that night, all alone in a big bar like that."
    scene w3_9091 with dissolve
    rose "But I wasn't alone, remember?"
    scene w3_9095 with dissolve
    mc "The recollection is better without Warren stinking it up."
    scene w3_9091 with dissolve
    "I was being selfishly selective with my perspective, of course. For Rosalind, our meeting was just another component of an ongoing nightmare."
    scene w3_9096 with dissolve
    rose "That guy gave me the creeps. He just... {b}stared at me.{/b}"
    rose "I was glad when you turned up, for a couple of reasons..."
    scene w3_9097 with dissolve
    mc "What was the other reason?"
    scene w3_9098 with dissolve
    rose "That someone even turned up."
    scene w3_9099 with dissolve
    "......"
    scene w3_9100 with dissolve
    rose "...it smells delicious."
    scene w3_9101 with dissolve
    mc "Should we say grace before we dig in?"
    scene w3_9102 with dissolve
    rose "You joke, but..."
    scene w3_9103 with dissolve
    rose "Rub a dub dub, thanks for the grub!"
    scene w3_9104 with dissolve
    rose "Ah... that would've got me whipped as a child. Rituals are funny. Even after I moved out, food tasted off if I didn't utter {i}something.{/i}"
    rose "It took me months to get over that."
    scene w3_9105 with dissolve
    "Surprisingly, Rosalind took my suggestion that we conversate tonight seriously, sharing a little bit about herself unprompted."
    hide screen textbox2 with dissolve

    menu:
        "Relate your own experience on the subject of dinner rituals. (RoseTR +1)"(chg=["rosalind_up"]):
            $ w3RTalkRapport += 1
            $ Rosalind_Affection +=1
            scene w3_9106 with dissolve
            show screen textbox2 with dissolve
            mc "...I think I relate. It's crazy to think I had to learn to eat a meal without the background noise of a TV."
            scene w3_9107 with dissolve
            mc "It's probably sad and telling that I consider being able to be alone with your own thoughts a skill to be maintained."
            scene w3_9108 with dissolve
            rose "Hey! It {i}is{/i} a struggle. The world is constant stimulation."
            scene w3_9109 with dissolve
            mc "So, I'm guessin' mandatory family dinner growing up?"
            scene w3_9110 with dissolve
            rose "With a side of suffocating non-conversation. I'm guessin' lots of dinners alone?"
            scene w3_9111 with dissolve
            "......"
            scene w3_9112 with dissolve
            mc "...eh, half-and-half? Sometimes, but I ate at Ian's a bunch."
            scene w3_9113 with dissolve
            mc "Which, on the subject of suffocating conversation, I could never get away with \"good\" for \"how did your day go\" either. It was always 1 good thing, 1 bad thing."
            mc "I hated it at the time, but after I moved out, sometimes I found myself enumerating parts of my day to a ham sandwich. So, yeah... I get talking to your food."
            scene w3_9114 with dissolve
            "{b}Nice!{/b} That got a smile from the older woman."
            scene w3_9119 with dissolve
            mc "So... your religious upbringing..."
        "{i}Don't worry,{/i} this isn't grape juice. (RoseTL +1)":


            $ w3RTalkLubrication += 1
            scene w3_9106 with dissolve
            show screen textbox2 with dissolve
            mc "Well, never fear, this isn't sacrament wine we're having."
            scene w3_9115 with dissolve
            "Rosalind watched me carefully pour her a glass of wine."
            scene w3_9116 with dissolve
            rose "Hmmm..."
            scene w3_9117 with dissolve
            "I watched Rosalind smoothly slide the effervescent liquid down her throat with an alluring enthusiasm."
            scene w3_9118 with dissolve
            rose "Good thing I'm not catholic, then."
            mc "Still... your religious upbringing..."
            scene w3_9119 with dissolve

    mc "How's that working out for you?"
    scene w3_9120 with dissolve
    rose "Ah... it's... {i}complicated.{/b}"
    scene w3_9121 with dissolve
    "Rosalind's expression supported her claim. For a moment, her smile diluted into a frown, as if she was weighing something in her mind and didn't like the tally."
    mc "I bet..."
    scene w3_9122 with dissolve
    rose "...do you believe in God?"
    scene w3_9123 with dissolve
    mc "Me...? Uh..."
    hide screen textbox2 with dissolve

    menu:
        "You do not.":
            show screen textbox2 with dissolve
            mc "I'm afraid I don't..."
            scene w3_9124 with dissolve
            rose "That's more and more common, isn't it?"
            scene w3_9125 with dissolve
            "The MILF didn't volunteer her own thoughts on the matter, instead letting a silence grow between us."
        "You'd like to. (RoseTR +1)":

            $ w3RTalkRapport += 1
            show screen textbox2 with dissolve
            mc "Sometimes I think I'd like to."
            scene w3_9122 with dissolve
            rose "...but you don't?"
            scene w3_9123 with dissolve
            mc "I don't know. I just think it'd be nice to think that there's more to life than the box we're in."
            scene w3_9124 with dissolve
            rose "It is a comforting thought."
            scene w3_9126 with dissolve
            mc "I do envy how sure some people are of it."
            scene w3_9127 with dissolve
            rose "Yeah... {i}faith...{/i}"
        "You don't know. (RoseTL +1)":

            $ w3RTalkLubrication += 1
            show screen textbox2 with dissolve
            mc "I usually say \"no\", but if I'm being honest... {i}I don't know.{/i} How could anyone know?"
            scene w3_9127 with dissolve
            rose "I often asked myself the same question..."
            scene w3_9126 with dissolve
            mc "Did you find an answer you're happy with...?"
            scene w3_9125 with dissolve
            rose "..."
            scene w3_9128 with dissolve
            "Rather than answer, she made a point to take a swig of wine."
            scene w3_9129 with dissolve
            "......"
            "..."

    scene w3_9130 with dissolve
    "For me, it wasn't complicated."
    "Growing up, the subject of religion conspicuously never came up."
    scene w3_9131 with dissolve
    "Save for a lone cross that my mother occasionally wore that belonged to my paternal grandmother..."
    mct "(...was my father religious? What about Mom...?)"
    scene w3_9132 with dissolve
    "Until this moment, religion had never been a topic between my mother and I, but suddenly it felt like a glaring omission in my life."
    scene w3_9133 with dissolve
    mct "(...how could I not know?)"
    mct "(There are some things I {i}don't{/i} know about my mother...)"
    scene black with fade
    "Rosalind's words from this morning came back to me."
    hide screen textbox2 with dissolve
    scene vpt_memory3_a with pixellate
    show vpt_memory3
    rose "Nora won't know every aspect of my life, and that's okay."
    "To know that there was something I didn't know about my mother was... {i}comforting?{/i}"
    "Did {b}she{/b} fall out of religion for some reason?"
    "The answer could be innocuous, it could be eye-opening..."
    "And in this moment, I committed myself to never knowing."

    menu:
        "Still, that nagging curiosity...":
            play ambient "sound effects/moan1.mp3"
            scene vpt_memory4_a with dissolve
            show vpt_memory4
            "...hovered within the periphery of my mind."
            vic "{size=-15}{font=/gui/fonts/MB-Thin_Worms.ttf}Ehuahhh...!{/font}{/size}"
            mct "(...should I check later?)"
            vic "{size=-15}{font=/gui/fonts/MB-Thin_Worms.ttf}Ah, ahh-! Hnhhhh...!{/font}{/size}"
            "......"
            "..."
        "Return these images to the recesses of your mind.":


            pass

    stop ambient
    scene w3_9134 with pixellate
    show screen textbox2 with dissolve
    mc "...what about you? do you believe in God?"
    "I decided to be pointed with it, as she had with me."
    scene w3_9135 with dissolve
    rose "........."
    rose "......"

    if w3RTalkRapport >= 4 or w3RTalkRapport >= 3 and w3RTalkLubrication >=1:
        $ w3RTalkReligion = True
        $ w3RTalkOpenness +=1
        $ Rosalind_Affection +=1
        scene w3_9136 with dissolve
        rose "I do believe there's something watching over us. I'm not sure who or what, but..."
        rose "{b}I do.{/b} It's just something I feel..."
        scene w3_9137 with dissolve
        rose "It makes me feel stupid sometimes."
        scene w3_9138 with dissolve
        mc "I don't think it's stupid, Rose."
        scene w3_9139 with dissolve
        rose "..."
    else:

        scene w3_9137 with dissolve
        rose "{i}I don't know.{/i}"
        scene w3_9138 with dissolve
        mc "It's complicated...?"
        scene w3_9140 with dissolve
        rose "Heh, {b}like I said!{/b}"


    scene w3_9141 with dissolve
    rose "Whatever the case, I'm not {i}religious,{/i} that much is for certain. My childhood pretty much took that off the table."
    rose "My first chance I got - college - I bolted."
    scene w3_9142 with dissolve
    mct "(Interesting...)"
    scene w3_9143 with dissolve
    "She really was taking this dumbass suggestion of mine to get to know each other earnestly."
    scene w3_9144 with dissolve
    mc "...was it really that suffocating?"
    scene w3_9145 with dissolve
    rose "As a young woman I thought it was, but... actually, scratch that. Even now, just thinking about never getting out of there.... {b}euuuch.{/b}"
    rose "...were you happy to get a taste of freedom?"
    scene w3_9146 with dissolve
    mc "Going \"off\" to college and living by myself has had its ups and downs, but..."
    scene w3_9147 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "You've missed living with somebody. RoseTR +1)"(chg=["rosalind_up"]):
            $ w3RTalkRapport += 1
            $ Rosalind_Affection +=1
            scene w3_9148 with dissolve
            mc "I kinda miss living with someone."
            scene w3_9147 with dissolve
            rose "Just anyone?"
            scene w3_9149 with dissolve
            mc "...no, not anyone. I had Hana stay a few days with me recently, and it's been pleasant having you here."
            scene w3_9150 with dissolve
            rose "Sounds like you miss having a woman around."
            scene w3_9151 with dissolve
            mc "Perhaps that's it. Actually, tonight... the thought crossed my mind that it wouldn't be so bad to settle down in my future."
            scene w3_9152 with dissolve
            mc "At the very least, it's nice having someone around to appreciate my cooking."
            scene w3_9153 with dissolve
            rose "Mmmhhh..."
            scene w3_9154 with dissolve
            rose "This is good!"
            scene w3_9151 with dissolve
            mc "Thanks for taking the bait."
            scene w3_9150 with dissolve
            rose "Heh, if that's what you enjoy, have you ever considered becoming a chef instead of a doctor?"
            scene w3_9151 with dissolve
            mc "Might be a good backup option if I failed my MCATs..."

            if rosalindKilSolution == True:
                scene w3_9155 with dissolve
                mct "That, or like Ian suggested, we could make porn..."

            scene w3_9150 with dissolve
            rose "I get it, though. Maybe the {i}only{/i} thing I was certain of in life was I wanted to start a family."
        "There are aspects of it you enjoy.":

            scene w3_9148 with dissolve
            show screen textbox2 with dissolve
            mc "There are aspects I enjoy. I like being able to walk around naked for one."
            scene w3_9147 with dissolve
            rose "That's the big perk, is it?"
            scene w3_9149 with dissolve
            mc "There's others! The solitude is nice! And instead of actively seeking quiet, it's the opposite."
            scene w3_9148 with dissolve
            mc "You have to make an effort to see people, and I think that has some value to it."
            scene w3_9157 with dissolve
            rose "That's an interesting way of looking at it, for sure, but I don't think I could stand living alone."
            scene w3_9156 with dissolve
            mc "Yet, you were so gung ho about it when you left for college?"
            scene w3_9158 with dissolve
            rose "I just wanted to get out from underneath {i}that{/i} roof, but I always knew I wanted to start a family."
            scene w3_9150 with dissolve
            rose "Solitude might be nice on paper, but... having someone you love {i}intimately{/i} close by is much, {b}much{/b} preferable for me."


    scene w3_9159 with dissolve
    "It seemed that thought alone was enough to make Rosalind smile."
    scene w3_9160 with dissolve
    rose "*{b}Gulp, gulp, gulp!*{/b}"
    scene w3_9161 with dissolve
    rose "You know..."
    scene w3_9162 with dissolve
    "Rosalind took a moment to consider how to form her thoughts into words."
    scene w3_9163 with dissolve
    rose "When you called about getting me that money, I was a bit drunk. I don't normally--"
    scene w3_9155 with dissolve
    mc "Hey, I'm not judging you!"
    scene w3_9158 with dissolve
    rose "No, really. I don't really drink! I just... want you to know that..."
    scene w3_9155 with dissolve
    "For some reason, that seemed important to her."
    scene w3_9163 with dissolve
    rose "I... uh... {i}I hate drunks.{/i}"
    scene w3_9155 with dissolve
    "Her words were full of remembrance."
    "I didn't know if that related to her husband, or something else in her past, but--"
    scene w3_9164 with dissolve
    mc "...personally, I've never had a taste for this stuff, either."
    "That was a topic I wasn't going to pry into."
    rose "Yeah, but you're still a kid, so that--"
    scene w3_9165 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Cut her off by teasing her. (RoseTR +1)"(chg=["rosalind_up"]):
            $ w3RTalkRapport +=1
            $ Rosalind_Affection +=1
            scene w3_9166 with dissolve
            show screen textbox2 with dissolve
            mc "{b}Oh, am I?!{/b} And what's so kid-like about me, Rose?"
            mc "Were you looking at a kid earlier when you were watching me cook?"
            scene w3_9167 with dissolve
            rose "That--!"
            scene w3_9166 with dissolve
            mc "...hmm, or were you looking at a {b}man?{/b}"
            scene w3_9167 with dissolve
            rose "{b}You're imagining things!{/b}"
            scene w3_9166 with dissolve
            mc "...is that so?"
            scene w3_9168 with dissolve
            "........."
            "......"
            scene w3_9169 with dissolve
            rose "...{size=-10}maybe not so.{/size}"
            scene w3_9171 with dissolve
            mc "What was that? I didn't hear you!"
            scene w3_9170 with dissolve
            rose "{b}--maybe not so!{/b} You're, ah..."
            scene w3_9169 with dissolve
            rose "I mean, I've seen your... uh... and done... uh..."
            scene w3_9170 with dissolve
            rose "*Ahem* I know you're a {b}man{/b}."
            scene w3_9168 with dissolve
            "Her emphasis on the last word sounded quite deliberate, somewhere between apology and enticement."
            scene black with fade
            mc "Thank you for pointing out the obvious."
        "Let her finish, and take a drink. (RoseTL +1)":


            $ w3RTalkLubrication += 1
            scene w3_9172 with dissolve
            show screen textbox2 with dissolve
            rose "--goes without saying!"
            scene w3_9173 with dissolve
            "......"
            scene w3_9174 with dissolve
            mc "...there's times when it's not so bad though, right?"
            scene w3_9175 with dissolve
            rose "Yeah..."
            scene w3_9176 with dissolve
            "She joined me in the gesture."
            scene black with fade
            "......"


    scene w3_9177 with fade
    mc "...by the way, what did you study?"
    "The small talk continued, we finished our meal, and I brought it back to a previous topic."
    scene w3_9178 with dissolve
    mc "You work as an office assistant right now, right? Was it something business-related?"
    scene w3_9179 with dissolve
    rose "Uhh... well, uh..."
    scene w3_9180 with dissolve
    "She had an odd response to a simple question, looking like she didn't know how to answer it."
    scene w3_9179 with dissolve
    rose "That--"
    scene w3_9180 with dissolve
    "Looking like she was trying to cook up a {i}lie.{/i}"

    if w3RTalkRapport >= 6 or w3RTalkLubrication >=3:
        $ w3RTalkOpenness +=1
        $ w3RTalkEducation = True
        $ Rosalind_Affection +=2
        scene w3_9181 with dissolve
        rose "Well, *ahem*..."
        scene w3_9182 with dissolve
        mct "(Curious...)"
        rose "........."
        rose "......"
        scene w3_9181 with dissolve
        rose "...I never really got around to studying anything."
        scene w3_9182 with dissolve
        mc "Are you saying you dropped out?"
        scene w3_9183 with dissolve
        "......"
        scene w3_9184 with dissolve
        rose "...yes."
        scene w3_9183 with dissolve
        mc "Well, that's nothing to be so cagey about. There's nothing wrong with it."
        scene w3_9185 with dissolve
        rose "Ah... well... it's just another thing, isn't it?"
        scene w3_9186 with dissolve
        "I think I know where she was going with this..."
        mc "You dropped out to start a family."
        scene w3_9185 with dissolve
        rose "Yeah... like I said I don't {i}regret{/i} it, but... sometimes..."
        rose "It's just another item on the list of bad decisions I allowed Rupert to talk me into..."
        scene w3_9186 with dissolve
        "........."
        "......"
        scene w3_9187 with dissolve
        rose "...euuch, imagine getting married to the first man you gave yourself to!"
        scene w3_9188 with dissolve
        rose "{i}Fuck{/i} my upbringing!"
        scene w3_9189 with dissolve

        if roseGonzoExperience == True:
            mc "Wait, during your interview, you said you'd had one-night stands--"
            scene w3_9190 with dissolve
            rose "That was a lie for the camera."
            scene w3_9189 with dissolve
            mc "Huh..."
        else:
            mc "Wait, your husband was your--"
            scene w3_9190 with dissolve
            rose "Uh huh. {b}Pathetic{/b}, isn't it?"

        scene w3_9191 with dissolve
        "......"
        scene w3_9192 with dissolve
        mc "...come on, let's take this bottle someplace more comfortable."
    else:

        scene w3_9179 with dissolve
        rose "Y-yeah... {i}Office administration...{/i}"
        scene w3_9191 with dissolve
        "That was definitely a lie..."
        scene w3_9190 with dissolve
        mct "(But whatever the case...)"
        scene w3_9192 with dissolve
        mc "...come on, let's take this bottle someplace more comfortable."

    scene black with fade

    if perk_strongman == True:
        rose "...you want help with that?"
        mc "Naaaaah, I got it."
    else:
        rose "...what are you doing?"
        mc "Come on, give me a hand with this."

    "......"
    "..."
    scene w3_9193 with fade
    mc "I love this time of day."
    scene w3_9194 with dissolve
    rose "It's just a shame there's a city in the way."
    scene w3_9193 with dissolve
    mc "Not big on life in Morehead Hills?"
    scene w3_9195 with dissolve
    rose "Hmmm... I don't hate it. My home city wasn't any better."
    rose "I just think I'd prefer a field of flowers..."
    scene w3_9196 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "There's a flower right here..."(chg=["maid"]):
            scene w3_9197 with dissolve
            show screen textbox2 with dissolve
            mc "...and I think I prefer the lone Rose I have right here to a field of 'em."
            scene w3_9198 with dissolve
            "........."
            "......"
            scene w3_9199 with dissolve
            rose "That sounds lifted from one of my novels..."
            scene w3_9200 with dissolve
            "Wait, did that actually make her... blush?"
            scene w3_9201 with dissolve
            mc "Damn, didn't land. I was trying to make you laugh..."
            scene w3_9202 with dissolve
            rose "Save the comedy for the professionals. And also, that kind of line..."
            scene w3_9201 with dissolve
            mc "...doesn't suit me?"
            scene w3_9202 with dissolve
            rose "...is unnecessary and wasted on me."
            scene w3_9203 with dissolve
            "So... she felt herself beyond cheesy pickup lines she clearly enjoyed, and I was in a place that I didn't need to bother."
            hide screen textbox2 with dissolve

            menu:
                "She has a point...":
                    scene w3_9201 with dissolve
                    show screen textbox2 with dissolve
                    mc "...what were we talking about, again?"
                    scene w3_9202 with dissolve
                    rose "We were..."
                "Fuck it. Double down on the cheese.(RoseTR +1, RoseTL +1)"(chg=["rosalind_up"]):

                    $ w3RTalkRapport += 1
                    $ w3RTalkLubrication += 1
                    $ Rosalind_Affection +=1
                    scene w3_9204 with dissolve
                    show screen textbox2 with dissolve
                    mc "...you think? Yet for me, you're like this wine..."
                    scene w3_9205 with dissolve
                    rose "...?"
                    "I solidified my resolve. {i}This would be cheesier than the last.{/i}"
                    scene w3_9204 with dissolve
                    mc "The more I drink you in, the better I feel."
                    scene w3_9206 with dissolve
                    rose "{i}Ugh...{/i}"
                    scene w3_9207 with dissolve
                    mc "You're redder than a Rose right now."
                    scene w3_9206 with dissolve
                    rose "Because {i}I'm lame!{/i}"
                    scene w3_9208 with dissolve
                    "*Gulp, {b}gulp!{/b}*"
                    scene w3_9199 with dissolve
                    rose "Moving on..."
                    scene w3_9201 with dissolve
                    mc "...yeah, what were we talking about again?"
        "Make the best of it...":

            scene w3_9197 with dissolve
            show screen textbox2 with dissolve
            mc "We just have to make the best of the view we have then..."
            scene w3_9209 with dissolve
            rose "...the company more than makes up for all the asphalt."
            scene w3_9210 with dissolve
            "I didn't think she believed that..."
            scene w3_9201 with dissolve
            mc "Uh huh. What were we talking about again?"


    if w3RTalkEducation == True:
        scene w3_9202 with dissolve
        rose "Before this? The big thing was me dropping out of college..."
        scene w3_9201 with dissolve
        mc "Right, yeah..."
        "That was obviously a sore spot for her, so I refrained from the obvious dumbass platitude. {i}\"We all walk our own path in life\"{/i} would just sound glib considering present circumstances."
        scene w3_9212 with dissolve
        rose "{size=-10}My parents didn't take that well...{/size}"
        scene w3_9201 with dissolve
        mc "...anyway, do you like your current job?"
    else:

        scene w3_9202 with dissolve
        rose "Education."
        scene w3_9201 with dissolve
        mc "Ah, yeah... so... do you like your current job?"
        scene w3_9202 with dissolve
        rose "Uh..."

    "I decided to pivot to a tangentially related topic."
    scene w3_9211 with dissolve
    rose "It's a job, I guess. The only {i}real{/i} one I've ever had."

    if roseGonzoExperience == True:
        scene w3_9197 with dissolve
        mc "I remember you mentioning that..."
        scene w3_9211 with dissolve

    rose "Not that I didn't do odds and ends. Waitressing, and stuff like that."
    scene w3_9214 with dissolve
    rose "Plus, there was some {b}other{/b} stuff..."
    scene w3_9216 with dissolve
    "The way she trailed off made it sound ominous."
    scene w3_9215 with dissolve
    mc "What, you sold your dirty panties to perverts?"
    scene w3_9218 with dissolve
    rose "Pffh! No, I--"
    "Riding the feeling of laughter, she began to explain, but thought better of it all of a sudden."
    scene w3_9217 with dissolve
    rose "*Ahem* ...no, just {i}stuff.{/i}"
    scene w3_9216 with dissolve
    "{i}She quickly moved on.{/i}"
    scene w3_9214 with dissolve
    rose "It's amazing I even got hired... it's a small, family-owned printing company. I help with the front end."
    scene w3_9215 with dissolve
    mc "Why is that amazing?"
    scene w3_9214 with dissolve
    rose "Not that the qualifications were high, {b}but {/b}...I had to {i}fudge{/i} some details on my resume."
    scene w3_9215 with dissolve
    mc "...hey, it's not a life-or-death position."
    scene w3_9214 with dissolve
    rose "Still, I feel awful about it... but what can I say? With Oliver breathing down my neck, I needed the job..."
    scene w3_9215 with dissolve
    mc "I wouldn't feel too bad about it. Again, it's not like you're performing surgery."
    scene w3_9214 with dissolve
    rose "Heh, maybe I should've tried that... {b}it'd pay better.{/b}"
    scene w3_9217 with dissolve
    mc "Is there a career you'd like to have? In a perfect world?"
    scene w3_9219 with dissolve
    rose "Hmm... shockingly... no? I'm a boring woman and I don't have many interests..."
    scene w3_9220 with dissolve
    rose "Something simple, that pays regularly, with undemanding hours... that would've made me happy."
    scene w3_9222 with dissolve
    mc "Work to live, not live to work?"
    scene w3_9223 with dissolve
    rose "Yeah... even as a child, I wanted to be a homemaker..."
    scene w3_9222 with dissolve
    mc "Hey, that's cool. The world needs 'em..."
    scene w3_9219 with dissolve
    rose "The thing is, I don't know if I come by it honestly or just copying what I knew, but my ambition started and ended there."
    scene w3_9221 with dissolve

    if w3RTalkEducation == True:
        mct "(That explains why she married the first guy that came along...)"
    else:
        mct "(That explains why she got married so young, I guess...)"

    scene w3_9222 with dissolve
    mc "Well, shit. What even is an honest desire? It's all picked up somewhere."
    scene w3_9223 with dissolve
    rose "Yeah... I think I just meant that I don't know if I'm happy about {i}that{/i} particular case."
    scene w3_9221 with dissolve
    "......"
    scene w3_9220 with dissolve
    rose "...*sigh* This is starting to feel like a therapy session. What are you trying to pull here by getting me to spill my guts like this?"
    scene w3_9222 with dissolve
    mc "To be fair, I haven't had to try too hard."
    scene w3_9224 with dissolve
    rose "Talk about yourself for a little bit. Make it embarrassing."
    scene w3_9225 with dissolve

    if roseFlag == True:
        mc "{i}Fair.{/i} Our relationship is built on tit-for-tat..."
    else:
        mc "Hmmm, a little tit-for-tat. {i}Fair.{/i}"

    scene w3_9226 with dissolve
    "Put on the spot, I had difficulty recalling something worthwhile."

    if history_firestarter == True:
        "I had shared my greatest childhood malfeasance, my flirtation with pyromania, with the Carnations last week..."

    elif history_voyeur == True:
        "I had shared my greatest childhood malfeasance, {i}my modeling enterprise{/i}, with the Carnations last week..."
    else:

        "I had shared my greatest childhood malfeasance, the charity fraud, with the Carnations last week..."

    "Of course, there were many, many, many lesser incidents I wasn't proud of, but they paled in comparison."
    scene w3_9227 with dissolve
    mc "...want to hear about the great romantic triangle of my senior year?"
    scene w3_9228 with dissolve
    rose "Yes!"
    "I {b}knew{/b} that'd get her."
    scene w3_9227 with dissolve
    mc "Forewarning, I came out looking pretty pathetic..."
    scene w3_9228 with dissolve
    rose "Good! I'm in need of some schadenfreude!"
    scene w3_9229 with dissolve
    mc "Evil woman... Alright, so... it was my senior year of high school, and I had just previously come out of a disappointing relationship with the first girl I ever dated..."
    scene w3_9230 with pixellate
    "So, I begun weaving the tale of Marlow, Ian, and myself. A simple, unimportant event that weighed heavy only for those it concerned."
    "I started with a brief history of my unrequited loves, all minor things, but it painted a picture. I detailed the thrill of the first time I'd ever had my attraction reciprocated, and the subsequent disappointment over how surface-level it all was."
    rose "Heh! Are high school relationships anything, but?"
    scene w3_9231 with w24
    "Then I segued to {i}Marlow.{/i} An ultimately odd girl whose typical teenage foibles were eclipsed by her kindness and ability to disregard all self-doubt and simply {i}throw herself into it.{/i}"
    "I explained to Rosalind how we were friends. {i}Good friends, even.{/i}"
    "I had met her on the first day of Freshman year, and as someone who began to withdraw into his shell in high school, her unrepentant enthusiasm slowly captivated me."
    scene w3_9232 with w22
    "I explained the waxing and waning of my attraction to her over those four years. How I shored up my inaction with excuses like \"it was never meant to be\" or the sanctity of friendship."
    "I detailed some of our ill-timings. Of missed hints, and even the time I deliberately handwaved the idea of us dating out of a misguided commitment to that laughable {i}I'd rather have her as a friend{/i} notion."
    "Unlike her, {i}I couldn't just go for it{/i}, and that is what kept the {i}idea of her{/i} burning through those very long four years."
    scene w3_9233 with w11
    mc "After I broke up with my first girlfriend, it was like a switch was flipped."
    "I told Rosalind of how Marlow had broken up with her boyfriend a month prior, and with dramatic license explained how our mutual unentanglement coincided with our impending graduation and the looming anxiety over the onset of adult life."
    rose "I guess it was now or never?"
    mc "That was {i}my{/i} pitch."
    scene w3_9234 with pixellate
    rose "Where does the love triangle enter in?"
    scene w3_9235 with dissolve
    mc "I'm getting there, but first, do you want to put a face to the name?"
    scene w3_9236 with dissolve
    rose "Do I ever!"
    scene w3_9237 with dissolve
    "It seemed all my little embellishments were adding up to make my uninspiring story land with the repressed romanticist. "
    scene black with fade
    "A quick social media search, and--"
    scene w3_9238 with wipeleft
    rose "She was cute!"
    mc "Probably still is.."
    scene w3_9239 with dissolve
    rose "Okay, so, how does Ian factor in?"
    mc "Ah, well..."
    scene w3_9240 with dissolve
    "I briefly went charted how my friendship with Ian meant that Marlow {i}more or less{/i} became friends with Ian over the years too."
    rose "I think I can see where this is going..."
    "-- and for additional context, I explained how Ian began his change in high school from a timid, all-too-honest tag-along into the first iteration of his current form."
    scene w3_9241 with dissolve
    mc "We'd often do stuff together."
    rose "Did Ian have feelings for her?"
    scene w3_9242 with dissolve
    mc "Not really. {i}I don't think so at least.{/i}"
    "I broke it down. I was infatuated with Marlow, Marlow cared {i}deeply{/i} about me, and Ian..."
    scene w3_9243 with dissolve
    mc "She liked how happy I was around him, and he was admittingly, an attractive dude."
    "Marlow prided herself on being a free spirit, to the point that I sometimes thought she was trying {i}too hard.{/i}"
    mc "So, that now or never I proposed? It ended up biting me in the ass. She wanted a thruple!"
    scene w3_9244 with dissolve
    rose "Huh! And how did that go?!"
    scene w3_9242 with dissolve
    mc "Despite my misgivings, I went along with it. It lasted a week."
    mc "She could tell things had changed with me, and she was the one who called it off completely out of concern for Ian and mine's friendship."
    scene w3_9244 with dissolve
    rose "It's amazing you guys are still friends after that."
    scene w3_9242 with dissolve
    mc "Well, in the end, I'm the only one to blame for going along with something I was uncomfortable with. Marlow was a good person, and Ian is {b}Ian.{/b} It was pretty fucking awkward for a while, though."
    scene w3_9245 with dissolve
    "......"
    scene w3_9246 with dissolve
    mc "...so, how's that for embarrassing and pathetic?"
    scene w3_9247 with dissolve
    rose "......"
    scene w3_9248 with dissolve
    rose "...it's not {i}pathetic.{/i}"
    scene w3_9249 with dissolve
    mc "I'll take one out of two."
    scene w3_9248 with dissolve
    rose "You told it with earnestness and maturity. I love that, and I'm even a little envious."
    scene w3_9249 with dissolve
    mc "Over what?"
    scene w3_9250 with dissolve
    rose "Oh... just... heh, {i}that's so dramatic.{/i} My high school life was boring."
    scene w3_9249 with dissolve
    "......"
    mc "...so, you sold your used panties, huh?"
    scene w3_9251 with dissolve
    rose "No! Stupid!"
    scene w3_9252 with dissolve
    mc "Well, what was it then?! You can't blame me for being curious when you're so dodgy about it!"
    scene w3_9253 with dissolve
    rose "I--"
    rose "Uh..."
    scene w3_9254 with dissolve
    "Again, she paused, but..."

    if w3RTalkRapport >= 7 or w3RTalkLubrication >=4 or w3RTalkRapport >=6 and w3RTalkLubrication >= 2:
        $ w3RTalkOpenness +=1
        $ w3RTalkScamming = True
        $ Rosalind_Affection +=3
        scene w3_9255 with dissolve
        rose "...after Nora was born, my husband ran some phone scams for a time. People..."
        scene w3_9256 with dissolve
        "--but ended up blurting it out."
        scene w3_9263 with dissolve
        rose "...{i}people are more trusting of women."
        scene w3_9257 with dissolve
        "{i}That{/i} was a shock."
        scene w3_9258 with dissolve
        mc "I see... {size=-10}people are more trusting of women...{/size}"

        if kat_polite == True:
            mc "Does Mrs. Pulman know about this?"
        else:
            mc "Does Kathleen know about this?"

        scene w3_9260 with dissolve
        rose "I don't think so? It only went on for a few months and the police never got involved."
        scene w3_9259 with dissolve
        mct "(Yet, I know firsthand how thorough her background checks are...)"
        scene w3_9260 with dissolve
        rose "Just thinking about it makes me sick to my stomach..."
        scene w3_9259 with dissolve
        "For now, I pushed the old woman out of my mind."
        scene w3_9261 with dissolve
        mc "Is that why you stopped?"
        scene w3_9262 with dissolve
        rose "Not really... uh... Rupert moved onto {i}other{/i} things."
        scene w3_9260 with dissolve
        rose "Sometimes I'd get pulled into those things as well..."
        scene w3_9259 with dissolve
        "........."
        "......"
        scene w3_9262 with dissolve
        rose "I deserve how my life has turned out."
        scene w3_9264 with dissolve
        "Rosalind looked genuinely desolate, {i}pained.{/i}"
        mc "Come on... that's the religion talking. It's not like you killed somebody, Rose."
        "......"
        scene w3_9263 with dissolve
        rose "...I didn't just take people's lunch money, [mcf]. A lot of the people we scammed were on a fixed income, {b}get it?{/b}"
        scene w3_9266 with dissolve
        "The vitriol behind her words gave me {b}chills.{/b} The cold look on her face, and the anger seething underneath it..."
        scene w3_9265 with dissolve
        rose "Nice old men and women, willing to give some of the little they had, to those with even less... and what did they get as a reward?"
        scene w3_9266 with dissolve
        "It was an unfathomable look for the soft-spoken woman, and {i}utterly{/i} real. Much more real than any look she had given me before, I realized."
        scene w3_9265 with dissolve
        rose "An eroded trust of people."
        scene w3_9266 with dissolve
        mct "(Ah... maybe the drinking wasn't such a good idea...)"
        scene w3_9265 with dissolve
        rose "I know I'm a piece of shit..."
        scene w3_9264 with dissolve
        "As the silence grew, Rosalind's barely contained fury softened into a slurry of mixed emotion."
        "{i}This was the part where she was feeling stupid for saying too much.{/i} Perhaps even fearful that she had shattered an illusion that worked to her advantage."
        scene w3_9267 with dissolve
        "{b}--and this was the worst part of me.{/b} Rosalind's self-loathing lit a fire inside of me, making me want to reach out and stir the pot, and see where that might lead."
        mct "(...she deserves what she gets?)"
        hide screen textbox2 with dissolve

        menu:
            "Soothe Rosalind.":
                scene w3_9268 with dissolve
                show screen textbox2 with dissolve
                mc "Come here."
                scene w3_9269 with dissolve
                rose "I don't need a hug..."
                scene w3_9270 with dissolve
                mc "I could use one."
                scene w3_9271 with dissolve
                "........."
                "......"
                scene w3_9272 with dissolve
                "...after realizing I wasn't going to budge, Rosalind fell into my chest."
                scene w3_9273 with dissolve
                mc "Thank you."
                scene w3_9274 with dissolve
                "From there, I gave it a few wordless seconds for us to bask in each other's warmth and let a feeling of secureness set in before I shared what was on my mind."
                scene w3_9275 with dissolve
                mc "Would you do me another favor?"
                scene w3_9276 with dissolve
                rose "...*sigh* {i}what?{/i}"
                scene w3_9275 with dissolve
                mc "Put a lid on that kind of thinking."
                scene w3_9277 with dissolve
                rose "You asked..."
                "Her inward bitterness coated her words."
                scene w3_9278 with dissolve
                mc "Just to be sure, you don't have a time machine, do you?"
                scene w3_9277 with dissolve
                rose "W-wha--? {b}Euch.{/b} I know what you're going to say. The past is the--"
                scene w3_9279 with dissolve
                "To make my point, I wholly enveloped the forlorn mother."
                "{i}Nobody's perfect{/i} was too dismissive, too forgiving..."
                scene w3_9280 with dissolve
                mc "...all you can do is try to do better."
                scene w3_9281 with dissolve
                "Imagining saying that to myself allowed me to say that with conviction to the woman in my arms. Platitude as it may be, I relied on the feeling behind my words to connect with Rosalind."
                scene w3_9280 with dissolve
                mc "Recognizing the consequences of your actions doesn't mean you can't move on from them. After all, Nora needs the {b}present{/b} version of her mom, doesn't she?"
                scene w3_9282 with dissolve
                rose "I know that! Of course, I know-- ah... it's just... {i}you asked...{/i}"
                scene w3_9281 with dissolve
                "{i}Same words, less bite.{/i}"
                scene w3_9280 with dissolve
                mc "I know you know that, because it's what you've {i}been{/i} doing all along. I just want to say..."
                scene w3_9283 with dissolve
                mc "...you're doing a good job with it."
                scene w3_9284 with dissolve
                "........."
                "......"
                scene w3_9285 with dissolve
                rose "...can we watch the moon come up?"
                stop music fadeout 3.0
                scene black with fade
                mc "{b}Sure.{/b} I've got nothing else to do tonight..."
                "......"
                "..."
                jump w3RosalindAmore
            "So what? {b}Challenge her.{/b}"(chg=["maid"]):


                stop music
                play sound "sound effects/string-break.wav"
                scene w3_9340 with hpunch
                show screen textbox2 with dissolve
                mc "Oh, shut up!"
                "I went on the offensive."
                scene w3_9341 with dissolve
                rose "Did you just...?"
                "Rather than wallow, I sought to distract Rosalind with an audacious change in tone from our quiet dinner."
                scene w3_9342 with dissolve
                mc "So you were a scamming cunt? {b}Perfect!{/b} All things considered? Probably an asset!"
                scene w3_9343 with dissolve
                rose "You--"
                play music "music/called-upon.ogg"
                scene w3_9344 with dissolve
                mc "What does what {i}you{/i} deserve have to do with anything?"
                mc "{b}Nora{/b} deserves the best mother you can be {b}right here and now{/b}, and shit from 10 years ago only matters as much as it's stuck to your shoe."
                scene w3_9345 with dissolve
                rose "......"
                scene w3_9346 with dissolve
                rose "...I know that! {b}I know that!{/b}"
                scene w3_9347 with dissolve
                "She raised her voice in exasperation."
                scene w3_9346 with dissolve
                rose "You asked!"
                scene w3_9347 with dissolve
                "{i}Good.{/i}"
                scene w3_9348 with dissolve
                mc "I did ask, and {i}you{/i} answered. {b}Why?{/b}"
                scene w3_9349 with dissolve
                rose "What do you mean {i}why{/i}? {b}You asked!{/b}"
                scene w3_9350 with dissolve
                "The switch from Rosalind's typical meek tone to looking at me like I was a fucking idiot was {i}sublime.{/i}"
                scene w3_9351 with dissolve
                mc "Yeah! And you could've lied! Was it a calculated risk?"
                scene w3_9352 with dissolve
                rose "...what?"
                mc "You know, like a ploy to make it feel like we've bonded or--"
                scene w3_9353 with dissolve
                rose "No! Dinner was... {b}I felt like it!{/b} It's nice to talk with someone!"
                rose "{b}Asshole!{/b}"
                scene w3_9354 with dissolve
                mc "........."
                scene w3_9355 with dissolve
                rose "......"
                scene w3_9356 with dissolve
                mc "...I like it when you speak your mind."
                scene w3_9357 with dissolve
                rose "{i}Asshole.{/i}"
                scene w3_9356 with dissolve
                "{i}She was cute right now.{/i}"
                mc "So I did a good job with dinner?"
                scene w3_9358 with dissolve
                rose "Pffhhh, gah, {b}you-{/b}"
                scene w3_9359 with dissolve
                rose "I told you that already."
                scene w3_9360 with dissolve
                mc "Maybe you did, but I've got a bad memory. I did a good job with dinner, didn't I?"
                scene w3_9361 with dissolve
                rose "......"
                scene w3_9362 with dissolve
                rose "...you did an {b}amazing job{/b} with diner. 5 stars."
                scene w3_9361 with dissolve
                mc "Ye~ha! {i}Thank you.{/i}"
                scene w3_9363 with dissolve
                rose "{b}Pah!{/b} You are... you are..."
                rose "*Sigh* {i}Cute.{/i} {b}Christ!{/b}"
                scene w3_9364 with dissolve
                mc "Yeeeeeeah?"
                scene w3_9365 with dissolve
                rose "I don't know, mommy issues. {b}Who knows?{/b}"
                scene w3_9366 with dissolve
                "Her glibness was {i}exquisite.{/i}"
                scene w3_9365 with dissolve
                rose "It's probably part of the {i}ploy{/i} to make you like me."
                scene w3_9366 with dissolve
                hide screen textbox2 with dissolve

                menu w3RosalindSexSplit:
                    "You do like her. (love/caring route)":
                        scene w3_9367 with dissolve
                        mc "Oh, good. Then you can save your breath."
                        mc "{i}I already like you.{/i}"
                        scene w3_9368 with dissolve
                        mc "Thanks for sharing with me about your life."
                        scene w3_9369 with dissolve
                        rose "Y-you -- you're so--"
                        scene w3_9370 with dissolve
                        "........."
                        "......"
                        scene w3_9371 with dissolve
                        rose "Pffh, can we... can we just watch the moon come up? {b}Or something!{/b}"
                        scene w3_9372 with dissolve
                        mc "..you'd like that?"
                        scene w3_9371 with dissolve
                        rose "Y-yeah..."
                        scene black with fade
                        mc "That sounds good to this asshole."
                        jump w3RosalindAmore


                    "{color=#FF1493}[[Full Deal]{/color} Remind Rosalind of your worth." if roseDealFullAcceptance == True:
                        $ w3RosalindEndlessBJWorks = True
                        $ w3RTalkOpenness -=1
                        jump w3RosalindKnowsHerPlace
                    "You can live with not knowing.":

                        scene w3_9373 with dissolve
                        mc "You know... I kinda like not knowing."
                        scene w3_9374 with dissolve
                        rose "{b}God, you're annoying!{/b}"
                        scene w3_9368 with dissolve
                        mc "...wanna watch a movie?"
                        scene w3_9375 with dissolve
                        rose "........."
                        rose "......"
                        scene w3_9376 with dissolve
                        rose "Pffh! Yeah, I kinda do!"
                        scene black with fade
                        $ history_rosalind = "Dinner with Rosalind was followed by a heated moment. But rather than pressing it, we retreated into the safety of a movie."
                        $ unread_rosalind = True
                        play sound "sound effects/notification.wav"
                        show bioupdate with dissolve
                        "And so the night went on."
                        jump w3RosalindMovieInterlude

                    "{color=#696969}[[Full Deal] Remind Rosalind of both your worth.{/color}" if roseDealFullAcceptance == False:
                        jump w3RosalindSexSplit
    else:


        scene w3_9253 with dissolve
        rose "...just stuff to help out with the household income. Odds and {i}ends.{/i}"
        scene w3_9254 with dissolve
        "{i}She wasn't going to tell me.{/i}"
        scene w3_9377 with dissolve
        mc "Okay, okay...."
        mc "A woman is entitled to her secrets."
        scene w3_9378 with dissolve
        rose "......"
        scene w3_9379 with dissolve
        rose "I'll do the dishes?"
        mc "I'll help."
        scene black with fade
        $ history_rosalind = "Rosalind and I shared a nice dinner, but that was about it."
        $ unread_rosalind = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve
        "The night devolved into routine."
        jump w3RosalindDateFailInterlude

label w3RosalindAmore:
    $ w3RosalindVibing = True
    play music "music/campfire.ogg"
    scene w3_9286 with sunshine
    "A dozen minutes passed between Rosalind and I, with just as many words."
    scene w3_9287 with dissolve
    "What was going on in her head? I couldn't say. In that time, she had barely stirred, and her eyes were caught between the skyline beyond and the occasional glance in my direction."
    scene w3_9288 with dissolve
    "Once I thought about breaking the silence with a lazy observation, but a well-timed touch diverted me of that notion."
    scene w3_9289 with dissolve
    "........."
    scene w3_9290 with dissolve
    "......"
    "...in the end, {i}it wasn't a cold silence.{/i} Rosalind appeared comfortable with whatever she was or wasn't contemplating."
    scene w3_9291 with dissolve
    "After a dinner packed with conversation, the absence of it cleansed the palate."
    "Any added words would just upset that equilibrium, so I too basked in evening stillness and the rare excitement of a passing plane."
    scene w3_9292 with dissolve
    "I had learned more about this woman in an hour's time over wine, than I had in the weeks past."
    "Most of it, I figured, was by design. Yet, she also accidentally let slip more than she intended."
    mct "(A lack of life experience and for want of a family...)"

    menu:
        "She was a fool.":
            if w3RTalkEducation == True and w3RTalkReligion == True:
                "...what else would you call a woman who dropped out of college to aid in her husband's schemes?"
            else:
                "...what else could you call her?"

            scene w3_9293 with dissolve
            "The thought was more harsh than my actual feelings toward her."
            "It was hard to {i}feel{/i} ill about Rosalind, not when I had experienced firsthand the warmth she exudes during her daughter's daily camp reports. "
        "Who are you to judge?":

            "...it's not like I'm currently making an honest living."
            mct "(Heh, if I turn state's witness within the next decade, will Ian become my {i}Rupert{/i}?)"
            scene w3_9293 with dissolve
            "Either way, it was hard to think ill of Rosalind having seen the way her face filled with love during her daily phone calls with her daughter. "

    scene w3_9294 with dissolve
    "Even if it wasn't flattering, I had a clearer understanding of this woman and that felt... {i}good.{/i}"
    scene black with fade
    "Eventually the sun left us to brighten the rest of the world."
    scene w3_9295 with fade
    "With the cold concrete beneath our feet, and darkness gripping the four corners of my apartment loft..."
    scene w3_9296 with dissolve
    "It ended up like this."
    "The warmth of the woman in my lap sparing me from a dreary, lonesome scene."
    scene w3_9297 with dissolve
    rose "It's nice..."
    scene w3_9298 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Caress Rosalind's face."(chg=["rosalind_up"]):
            $ Rosalind_Affection +=1
            scene w3_9299 with dissolve
            "My fingers wandered down to the motherly woman's silky auburn hair in agreement."
            "{i}It was nice.{/i}"
            scene w3_9300 with dissolve
            rose "--!"
            "...but the moment I touched her cheek, Rosalind tensed up."
            scene w3_9301 with dissolve
            "Maybe I had miscalculated...?"
            scene w3_9302 with dissolve
            rose "N--"
            "...or maybe I hadn't?"
            scene w3_9303 with dissolve
            rose "I like it..."
            scene w3_9304 with dissolve
            "That was all I needed to hear."
            scene rosa_hd_00_a with dissolve
            show rosa_hd_00
            "So continued our silent agreement, Rosalind's head resting comfortably in my lap as I caressed her beautiful face."
            "Cheek, chin, hair..."
            "A simple act, from which I felt something novel swell in me."
            "{b}Tenderness.{/b}"
            "Uncomplicated, {i}doting{/i} intimacy spurred on by Rosalind's receptive blue eyes."
            "Eyes that asked for more."
            "I wasn't sure how long this went on, but--"

            if roseFlag == True or Rosalind_Affection >= 18:
                scene rosa_hd_00b_a with dissolve
                show rosa_hd_00b
                rose "Mmmhh...♥"
                "In that meager time, pacified, Rosalind let out an absent-minded moan."
                rose "Ah, ha..."
                mct "(Was she...?)"
                "It was subtle and constrained, but her breath quickened and her cheeks dyed an unmistakable color."
                "{i}She was.{/i}"

                menu:
                    "Move your caress lower. (w3RosalindRomanticSex = True)":
                        $ w3RosalindRomanticSex = True
                        "Without hesitation--"
                        scene rosa_hd_01_a with dissolve
                        show rosa_hd_01
                        rose "Ahhh...♥"
                        "As a natural extension of intimacy--"
                        rose "{size=-10}Mmhhh, ah...{/size}"
                        "I continued my caress {i}lower{/i}, cradling Rosalind with care and stroking her lovingly as if she was the dearest thing in the world."
                        rose "{size=-10}Oeuuhh, mmm...{/size}"
                        "And instead of tensing up, whereas she had been relaxed before, Rosalind {i}melted.{/i}"
                        rose "{size=-10}W-wooahh...{/size}"
                        "Her murmurs of contentment dissolved into quiet coos, and all but the smallest sliver of tension left her slight frame."
                        rose "{size=-10}Mmhhh, ah...{/size}"
                        mct "(She's so small...)"
                        rose "{size=-10} Yhhee...{/size}"
                        "Like this, {i}she seemed so frail,{/i} so vulnerable, so exposed..."
                        rose "{size=-10} Ouuhh...{/size}"
                        "Try as she might to hold my gaze, her eyelids grew heavy."
                        rose "{size=-10}Yeeahh, uuhhh...{/size}"
                        "What glints of blue I could spot peeking out diminished in brilliance, sinking into dreamlike bliss."
                        rose "{size=-15}ffhhh, ymmhhh... [mcf]...{/size}"
                        "{i}She was more than beautiful.{/i}"
                        rose "{size=-20}Ehuooh, awehh, whhhooo, hheuuuu, hyuuuh...{/size}"
                        "Her defenseless expression was the picture of serenity."
                        rose "{size=-25}Ehuooh, awehh, whhhooo, hheuuuu, hyuuuh...{/size}"
                        scene w3_9305 with dissolve
                        "And as Rosalind fell deeper into a lull, her {i}purring{/i} too fell to the wayside."
                        rose "..."
                        scene w3_9306 with dissolve
                        "Eventually, far between breaths and the thumping of her heart became my only company."
                        scene w3_9307 with dissolve
                        rose "...?"
                        "Without a word, she asked--"
                        scene black with fade
                        "{i}Why did you stop?{/i}"
                        scene rosa_hd_02_a with dissolve
                        show rosa_hd_02
                        rose "Mmmhhh...♥"
                        "I wanted nothing in between us. {i}Not even a favorite dress.{/i}"
                        rose "{size=-10}Mmhhh, ah...{/size}"
                        "Skin-on-naked-skin, Rosalind's bare chest burned to the touch."
                        rose "{size=-10}Mmhhh, ah...{/size}"
                        "The arousal that colored her face extended down to her breasts, shading each dollop of pale perfection a lovely pink."
                        rose "{size=-15}[mcf]...{/size}"
                        "Grazing my palm over Rosalind's giving flesh, slowly and soothingly, I treated each pass as if I was tending to something precious."
                        rose "{size=-15}Euuuahhh...{/size}"
                        "Conscious of not stirring the MILF from her contended stupor, my fingertips never sank deeper or lingered longer than they needed to."
                        rose "Hnnhhhg..."
                        "{i}As much as I wanted them to.{/i}"
                        "Instead, my gratification lay in observing the motherly woman caught between repose and arousal."
                        rose "{size=-10}Ehuuu...{/size} Aeuuhahh..."
                        "I watched the way she drifted in and out of focus, caught in a waking wet dream."
                        rose "{size=-20}Euuuuhhz, mmmhh...{/size}"
                        scene rosa_hd_03_a with fade
                        show rosa_hd_03
                        rose "Ahh...♥"
                        "{i}This time, she called out with feeling...{/i}"
                        rose "O, o-ohh...♥"
                        "Rather than ebb, now Rosalind flowed."
                        rose "Ah, o-hhhm..."
                        "Her breathing quickened once more."
                        rose "Hnngg, haa...♥"
                        "Her sounds of complacency turned {i}lewd{/i}."
                        rose "Euuahh, heeehhh..."
                        "Her nipples quickly stiffened, forming two perfect points for me to divert my focus to."
                        rose "Ah, huaat...♥"
                        "{i}Not too rough, and never a pinch.{/i}"
                        "Knowing how sensitive her chest was, I kept my restraint. "
                        rose "{b}Mmmh...!{/b}"
                        "I traced my fingers gingerly over her areola, with tips meeting at the peak in a mere embrace."
                        rose "Ah, {size=-10}g-good...{/size}"
                        "As the stimulation persisted, the lights in Rosalind's head dimly switched back on."
                        rose "{size=-10}F-feels good...{/size}"
                        "Tension returned back to her body, and her muscles came back to life."
                        rose "A, aah, aahhh...♥"
                        "And eventually--"
                        scene black with fade
                        play music "music/with-a-rose-in-your-teeth.ogg"
                        rose "MMhh...!"
                        rose "Mmhh, mmhhhaa--"
                        scene rosa_hd_04_a with dissolve
                        show rosa_hd_04
                        rose "{b}Mwwaaaahh...♥{/b}"
                        "Rosalind lost herself in a different way, throwing herself deeper into my grasp."
                        "Somehow or another, we got twisted up like this, the motherly woman clutching my shoulder and suckling at my fingers in pacification."
                        rose "{b}Ahh, mmhhh, Mmhaat...♥{/b}"
                        "And at some point she had lazily ventured a hand down to her twat, taking ownership of the fire that I had maintained at a simmer."
                        rose "Mmhh, hhnnggg..."
                        "What fantasies were playing out in her head, I hadn't a clue."
                        "Was she thinking of me?"
                        "Was she picturing some long-haired hunk plastered on one of her romance novels?"
                        "Was she recounting the pages of those tawdry stories?"
                        rose "Mhhh♥♥♥"
                        "I felt myself grow hard at her casual, absent-minded abandon."
                        rose "..."
                        "My own breath quickened..."
                        rose "Mh, hwwwahh...♥♥♥"
                        "My own need took hold of my faculties."
                        "Sight, sound, sensation..."
                        "Even the smell of Rosalind's shampoo."
                        "All of it formed a singular missive in my head."
                        "{b}To fuck.{/b}"
                        "And it seemed--"
                        scene w3_9308 with dissolve
                        rose "Oh-♥ I, uh--"
                        scene w3_9309 with dissolve
                        rose "*Gulp* Ah, haa..."
                        scene black with fade
                        "She had the same idea."
                        jump w3RosalindAmore2
                    "Keep the moment chaste.":

                        scene w3_9310 with fade
                        mc "...you feelin' alright?"
                        rose "Heh, yeah..."
                        scene w3_9311 with dissolve
                        rose "{i}Full from dinner.{/i}"
                        scene w3_9312 with dissolve
                        mc "Shall we take it easy then? Watch a movie, maybe...?"
                        scene w3_9313 with dissolve
                        rose "........."
                        rose "......"
                        scene w3_9314 with dissolve
                        rose "...that sounds great."
                        scene w3_9315 with dissolve
                        "........."
                        scene w3_9316 with dissolve
                        "......"
                        scene black with fade
                        $ history_rosalind = "Dinner with Rosalind took a cozy turn, but I chose not to push it further."
                        $ unread_rosalind = True
                        play sound "sound effects/notification.wav"
                        show bioupdate with dissolve
                        "...so the night went on."
                        $ renpy.end_replay()
                        jump w3RosalindMovieInterlude
            else:
                scene w3_9320 with dissolve
                rose "That was a lot of food!"
                scene w3_9321 with dissolve
                "The moment passed."
                scene w3_9322 with dissolve
                rose "I feel bloated!"
                scene w3_9323 with dissolve
                mc "...wanna watch a movie?"
                scene w3_9324 with dissolve
                rose "Hmmm. Sounds good to me."
                scene w3_9325 with dissolve
                "........."
                "......"
                scene black with fade
                $ history_rosalind = "Dinner with Rosalind was followed by a movie. How original."
                $ unread_rosalind = True
                play sound "sound effects/notification.wav"
                show bioupdate with dissolve
                "...so the night went on."
                jump w3RosalindMovieInterlude
        "Break the silence and agree.":


            scene w3_9318 with dissolve
            mc "...about as good as a field of flowers?"
            scene w3_9319 with dissolve
            "{i}She smiled.{/i}"
            "And with our silent agreement broken, we returned back to the present."
            scene w3_9317 with dissolve
            rose "I'm fuuuuuuull."
            scene w3_9318 with dissolve
            mc "Want to watch a movie or something...?"
            scene w3_9297 with dissolve
            rose "Sure."
            scene w3_9298 with dissolve
            "......"
            scene black with fade
            $ history_rosalind = "Dinner with Rosalind was followed by a movie. How original."
            $ unread_rosalind = True
            play sound "sound effects/notification.wav"
            show bioupdate with dissolve
            "...so the night went on."
            $ renpy.end_replay()
            jump w3RosalindMovieInterlude

label w3RosalindAmore2:
    scene rosa_hd_05_a with w20
    show rosa_hd_05
    rose "Euugghh--"
    "{i}Rosalind took over.{/i}"
    rose "Ah, haa, haaa--!"
    "In a flash, we had switched positions."
    rose "Hnngg, haaa...♥"
    scene w3_9326 with pixellate
    "Clothes came off."
    scene w3_9327 with pixellate
    mct "(Mr. May, huh...?)"
    "Hands {i}stayed on{/i}..."
    scene rosa_hd_05_a with w20
    show rosa_hd_05
    rose "Ah, haa, haaa...!"
    "And I was {b}caught.{/b}"
    "*Squuuuuek* {b}Shliiick, thwwiip--!{/b}"
    scene rosa_hd_06_a with dissolve
    show rosa_hd_06
    "Caught between couch cushion and Rosalind's ample rear pushing down on me."
    rose "Oh, ooahhhh...!"
    "{i}Initiative was ceded from a look.{/i}"
    scene w3_9328 with pixellate
    "A look of uncertainty, as if asking permission..."
    scene rosa_hd_06_a with pixellate
    show rosa_hd_06
    rose "Mmhm, haaa-!"
    "{i}Rosalind looked best on top.{/i}"
    "From below, I could see her {b}all.{/b}"
    scene rosa_hd_06b_a with dissolve
    show rosa_hd_06b
    "Where we were connected..."
    rose "Ahh, haaa, mmmhh...♥"
    "The way the fat of her hips erotically shifted as she brought them down to bear..."
    rose "Mmmh...! Haaaaht...!"
    "The sight of her abdominal muscles contracting and rhythmically relaxing as she threw her back out."
    rose "Fhh, haaaahhh...!"
    "{i}Her tummy wiggling and alluringly writhing like a belly dancer's.{/i}"
    scene rosa_hd_06c_a with dissolve
    show rosa_hd_06c
    rose "Oh, nnnohhh-♥"
    "And most breathtaking of all, as always--"
    "The bouncing of the MILF's massive tits."
    rose "Ahh, haaaa...! Nnnaah, naaahh...!"
    "--with her beautiful, blushing face peeking out from their prodigious heft."
    rose "Ahh, ooaaahhhh...!"
    scene w3_9329 with pixellate
    "So, when she gave me that look... {b}what the fuck else would I do?{/b}"
    scene rosa_hd_06_a with pixellate
    show rosa_hd_06
    mc "Haah, {b}aaahhhmm...!{/b}"
    "Keeping up our lustful silence, I returned it with an enthusiastic nod."
    rose "Mhaaww, hawwwhh...♥"
    "{b}And here we were.{/b}"
    mct "(Oh, fuck...!)"

    menu:
        "Express in words what you're feeling."(chg=["rosalind_passion_up"]):
            $ Rosalind_Libido +=1
            scene rosa_hd_06c_a with dissolve
            show rosa_hd_06c
            mc "Fuck...!"
            rose "Ahh, haaa...!"
            mc "I love you on top...!"
            scene w3_9330 with dissolve
            rose "Mmmhh♥!"
            "Her response, {i}a wry smile.{/i}"
            scene rosa_hd_06_a with dissolve
            show rosa_hd_06
            rose "{b}Ahhh...!{/b}"
            "Was it my imagination or did her moans get even more lewd?!"
            rose "{b}Mmhh, maaahh, haaa...!{/b}"
            "{i}They were.{/i}"
            mct "(Hot fucking--)"
            scene rosa_hd_07_a with dissolve
            show rosa_hd_07
            rose "{b}Oh, ohhh-♥{/b}"
            "Chasing sexual oblivion, Rosalind threw herself into it."
            rose "Ahh, mmhmhhhhh...♥♥"
            "{i}She picked up the pace,{/i} throwing her head back, and pushing out her chest."
            mct "({i}...did I say I love her on top?{/b})"
        "Keep your trap shut.":

            scene rosa_hd_06b_a with dissolve
            show rosa_hd_06b
            mct "(Fuuuuuck...!)"
            "{i}I tightened my grip on Rosalind's calves.{/i}"
            rose "Mmhh, aahhh...!"
            "I kept my eyes locked squarely on the lusty mother."
            mc "Ahh, ah, aahhh...!"
            "I let my own sounds of abject need combine with hers."
            scene rosa_hd_06_a with dissolve
            show rosa_hd_06
            rose "Ah, o-oaahh, hmhmm...!"
            "{i}That was how I told her how I felt.{/i}"
            rose "Mmhhh...♥"
            mct "(Who needed words--)"
            scene rosa_hd_07_a with dissolve
            show rosa_hd_07
            rose "{b}Oh, ohhh-♥{/b}"
            "Chasing sexual oblivion, Rosalind threw herself into it."
            rose "Ahh, mmhmhhhhh...♥♥"
            "{i}She picked up the pace,{/i} throwing her head back, and pushing out her chest."
            "{b}Yeah.{/b}"
            mct "({i}Who needed words?{/i})"



    "Her lower mouth constricted around my girth, doing all the talking necessary."
    rose "{b}MMmmhhh....!{/b}"
    "In her newfound fervor, {i}sloshing and splashing{/i}, she dirtied my abdomen with viscous desire."
    rose "Ahh, aahh, {b}yeeeahhhhh...!{/b}"
    "Deeper and deeper, she fucked me into the couch, its firm give no match for the lustful mother's unabated restraint."
    "{b}*Squeeewwhk, sqeeeyyhhhk-!*{/b}"
    "The springs cried out for mercy!"
    rose "Y-yes... {b}y-yes...!{/b}"
    "{i}She cried out.{/i}"
    rose "{b}Yes, yes, yes!{/b}"
    "{i}More, more, more.{/i}"
    rose "Ahh, {b}ehhheawaaahhh...!{/b}"
    "I was watching Rosalind lose herself before my very eyes, clinging to a fast-fleeting elation."
    rose "Oh, {b}OHHHH-{/b}"
    "{i}Faster and faster.{/i}"
    rose "Mmhh, haaaaa...♥"
    "{b}Faster and faster and faster.{/b}"
    scene rosa_hd_07b_a with dissolve
    show rosa_hd_07b
    "Each time putting her full weight into bringing her fat ass down onto my cock."
    mc "Mmmh, maahhhh...!"
    "Every bounce off my ball sack sending me deeper into a spine-chilling stupor."
    mc "Mmhmhh, ohh, {b}ohhhh...{/b}"
    "{i}I joined Rosalind in lewd chorus.{/i}"
    mc "{b}S-shit...!{/b}"
    "{i}What had gotten into her?{/i} What had set her off?"
    rose "Ahh, yeaah, fhhuuu-"
    "Whatever it was had transformed her into a carnal goddess."
    rose "Oh, ahhhee, haahhh-♥"
    "{b}What a sight.{/b}"
    rose "Ahh, aahh-! Yeeahh, ahohhhaa...♥"
    "What a--"
    scene w3_9331 with flash
    rose "Ahh, hsaaaaahhhhhh...♥♥♥♥♥♥♥♥♥"
    "What a sight. {i}Rosalind came.{/i}"
    scene w3_9332 with dissolve
    rose "Ahh, ohhh--♥"
    scene w3_9333 with dissolve
    "With a slovenly, slutty cry {i}Rosalind came.{/i}"
    scene w3_9332 with dissolve
    rose "Ahh, aahhh..."
    scene w3_9334 with dissolve
    "{i}Chills.{/i}"
    "The meek woman vanished, and through sex-clouded eyes, what replaced her peered down at me in hunger."
    rose "*Gulp* Ah, haaaa..."
    scene w3_9335 with dissolve
    "A look alone that made me want to shoot a load then and there into her womb."
    rose "Mmmh, hhaaaa...."
    scene w3_9336 with dissolve
    mct "(...she's not out of gas?)"
    "{b}More.{/b}"
    scene rosa_hd_08_a with dissolve
    show rosa_hd_08
    rose "Mmmhhh, mmhhh...!"
    "One didn't need words to communicate."
    rose "Mmmhffh, fffhhh..."
    "Chest-to-chest, moans stifled with a kiss, Rosalind spoke plainly."
    "{i}She wasn't going to be satisfied until she drained my balls.{/i}"
    mct "({b}Fuck!{/b})"
    "This time, I wouldn't be content lying back and playing dildo."
    rose "{b}Mmmhh, mhhh...!{/b}"
    "The moment our lips met, I sprung into action like a rabbit, marshaling lust-fueled strength to my hips."
    rose "Ah, ahhh...!"
    "Thrusting deep, and supporting the ravenous woman's weight with every fuck-hungry plunge, I clung to Rosalind."
    mc "MMhh, hmmgghh...!"
    "Securing my arms around her as if she might vanish otherwise."
    rose "Mhh, ahhh...!"
    "She {i}voiced{/i} a similar affirmation, digging her fingernails into my ribs."
    mct "{b}Ghhh!{/b}"
    "The sharp sensation spurred me on, compelling me to fuck her endlessly."
    play ambient "sound effects/fap2.mp3"
    scene rosa_hd_08b_a with dissolve
    show rosa_hd_08b
    "{i}It was a battle.{/i}"
    "For our pleasure, and for our very breath."
    "Time after time, she met my thrust, wantonly hurling herself down my shaft as much as I was skewering her."
    "The itch in my balls was growing."
    "My head hazy."
    "Less and less was I sure of where I started and ended, as we descended into a blur of insensate thrusts."
    play ambient "sound effects/moan3.wav"
    scene rosa_hd_09_a with dissolve
    show rosa_hd_09
    "I hurled myself toward oblivion."
    rose "Ammhwwwah..."
    "Rougher, and with great affection."
    rose "Mhh, haaa♥"
    "Demonstrating my want and need for this woman."
    rose "Ahh, haaa, heeehh...!"
    "Rosalind accepted the fleeting feeling, going limp in my arms, using her moans to coax me to the inevitable."
    mc "Ahh, ahhh, oh-!"
    "{i}I couldn't escape.{/i}"
    "Not even if I wanted to."
    rose "Ahh, haa, haaa...! [mcf]!"
    "{i}Our skin burning hot, sticky sweat fused us together.{/i}"
    "I {b}WOULD{/b} blow my load inside her."
    rose "Fuck me, fuchhhk me, fhhuuuk-!"
    "That was woven into the fabric of the universe."
    mc "Ahh, eehhhh, heehhhh...!"
    "Do it."
    "{b}Do it. Do it. Do it.{/b}"
    stop music
    stop ambient
    play sound "sound effects/spurt.wav"
    scene w3_9337 with flash
    rose "{b}MMmmmmmmmmmh!{/b}"
    "{i}I did.{/i}"
    rose "Ah, heeuuhah, hmmmahhhh...!"
    play sound "sound effects/spurt.wav"
    scene rosa_hd_10_a with flash
    play ambient "sound effects/gulp3.mp3"
    show rosa_hd_10
    "I squeezed her tight, and she me."
    "I poured myself into Rosalind, as if it was my very last act."
    mc "{b}F-fuck!{/b}"
    "{i}A sodden, sloppy mess.{/i}"
    mc "{b}Ahh, haa, t-take it...!{/b}"
    "That was what we were."
    "........."
    "......"
    stop ambient
    scene black with fade
    if not persistent.w3RosalindRomance:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3RosalindRomance = True
    "..."
    scene w3_9338 with fade
    "We still hadn't really spoken."
    "Nothing really could be said, anyway."
    scene w3_9339 with dissolve
    "Just as it began, I caressed the woman in my arms."
    rose "Mmhhm..."
    scene w3_9338 with dissolve
    "And just as she had previously--"
    rose "That feels good..."
    scene w3_9339 with dissolve
    "That sufficed."
    scene black with fade
    $ history_rosalind = "After dinner, Rosalind and I shared a quiet moment of romance and understanding."
    $ unread_rosalind = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    "Nothing more, and nothing less."
    $ renpy.end_replay()
    jump w3RosalindPostSexInterlude

label w3RosalindKnowsHerPlace:
    play music "music/with-a-rose-in-your-teeth.ogg"
    scene w3_9380 with dissolve
    mc "The thing is, {i}you do like me.{/i}"
    scene w3_9381 with dissolve
    "The moment I touched her--"
    scene w3_9382 with dissolve
    rose "Ahah, you... uh... you {i}sure{/i} about that, [mcf]?"
    scene w3_9383 with dissolve
    "I knew I wasn't {i}completely{/i} off base with my cocky assumption."
    scene w3_9384 with dissolve
    mc "Who's been taking care of you this week, Rose?"
    scene w3_9385 with dissolve
    rose "Pffh, come on..."
    scene w3_9386 with dissolve
    mc "I said {b}who{/b} has been taking care of you?"
    scene w3_9387 with dissolve
    rose "{size=-5}Y-you have...{/size}"
    scene rosa_hd_11_a with dissolve
    show rosa_hd_11
    "Her voice dropped down to a whisper, as if she was admitting to a precarious reality."
    mc "Who got you the money for Oliver?"
    rose "You did..."
    mc "And who {i}then{/i} took care of that asshole?"
    rose "{i}You...{/i}"
    mc "That's right. {b}I did.{/b}"
    "She didn't say anything, but I felt the inimitable rush of {i}authority{/i} suffuse my libido."
    mc "I'm the fuckin man, ain't I?"
    scene w3_9388 with dissolve
    rose "Pffh, {i}asshole.{/i}"
    scene w3_9389 with dissolve
    "She cursed at me again, but the fire was gone. {i}She wasn't disagreeing.{/i}"
    scene w3_9390 with dissolve

    if toughness >22:
        mc "It's nice having someone to rely on who is not a deadbeat, isn't it?"
    else:
        mc "It's nice having someone to rely on, isn't it?"

    scene w3_9391 with dissolve
    "{i}She didn't answer.{/b}"
    scene w3_9392 with dissolve
    mc "Truth is, when you came to my apartment two weeks ago, I didn't have the faintest fucking clue I could do {i}anything{/i} for you. I was a stupid kid out of his depth."
    scene w3_9391 with dissolve
    "Still was, actually, but..."
    scene w3_9392 with dissolve
    mc "Yet, you got me to agree. You knew before {i}I{/i} did that I could help you. You're a smart {b}woman.{/b}"
    scene w3_9391 with dissolve
    "My emphasis was on the last word."
    scene w3_9392 with dissolve
    mc "Even if it's for just a couple of weeks, I think you like feeling like you have a {b}reliable{/b} man in your life."
    scene w3_9393 with dissolve
    "........."
    "......"
    scene w3_9394 with dissolve
    mc "...not gonna deny it? Let the idiot think whatever he wants, eh?"
    scene w3_9395 with dissolve
    rose "You can confirm something for yourself..."
    scene w3_9396 with dissolve
    "The motherly woman opened her legs, extending an invitation."
    scene w3_9397 with dissolve
    rose "Ah--"
    "{i}She was turned on.{/i}"
    scene w3_9398 with dissolve
    rose "...is that {b}honest{/b} enough?"
    scene w3_9399 with dissolve
    "Her words trailed labored breaths."
    scene w3_9400 with dissolve
    rose "{size=-5}{b}No,{/b} I'm not going to deny it...{/size}"
    scene w3_9399 with dissolve
    "Rosalind poured honey into my ears."
    scene w3_9398 with dissolve
    rose "{b}Take charge.{/b}"
    scene w3_9399 with dissolve
    "Emboldened, she now met my gaze."
    scene w3_9398 with dissolve
    rose "Be {i}the{/i} {b}man.{/b}"
    scene w3_9401 with dissolve
    mc "You fuckin--"
    "Scratch that. Not honey, but {b}jet fuel{/b} setting ablaze a masculine fantasy that propelled me forward onto Rosalind as if she was a bitch in heat."
    scene w3_9402 with dissolve
    mc "Ah..."

    if w2RosalindPhoto == True:
        mc "Two weeks ago you were an awkward, bumbling bitch and--"
    else:
        mc "You're getting real good at playin' the slut, Ro--"

    scene w3_9403 with fade
    "Her long legs coiled around me like a snake."
    rose "You're a {b}king{/b}."
    "{i}She lathered it on shamelessly.{/i}"
    scene w3_9404 with dissolve

    if w2RosalindPhoto == True:
        mc "You think I'm that easy, you {b}dumbfuck{/b} whore?"
    else:
        mc "You think I'm that easy?"

    scene w3_9405 with dissolve
    rose "You. Are. A. King. [mcf]."
    scene w3_9406 with dissolve
    "{i}Fuck, I was that easy.{/i} Her ersatz praise stirred my insides."
    scene w3_9404 with dissolve
    mc "Damn straight I am!"
    scene w3_9407 with dissolve
    rose "If I had met a {b}man{/b} like you 12 years ago, things would be different..."
    rose "I mean, the way you rushed to my side the other day..."
    scene w3_9408 with dissolve
    "{i}She was playing me.{/i}"
    scene w3_9409 with dissolve
    rose "You're so strong! ... so {i}reliable...{/i}"
    scene w3_9410 with dissolve
    mc "{i}You fucking know it.{/i}"
    scene rosa_hd_12_a with dissolve
    show rosa_hd_12
    rose "Hands like this could set me straight and keep me out of trouble..."
    "{i}She was fucking playing me.{/i}"
    mc "Ha! You want this dick?"
    rose "Yes! Give it to me!"
    "The motherly woman threw herself into the moment, without an ounce of self-consciousness of how silly she looked."
    rose "Fuck me like a {b}man!{/b}!"
    mc "Shit! Aren't you embarrassed?!"
    rose "A-and why would I be embarrassed?"
    mc "Oh, I don't know. Because you're a 36-year-old woman awkwardly dry-humping me like a hormonal teenager?!"
    rose "Ah, haaa... {b}asshole!{/b} You're the one making me do {i}this.{/i}"
    mc "{b}There she is!{/b} Thing is..."
    "She kept up her fervor, matching her enthusiasm to mine."
    mc "I'm not making you do a {b}goddamn{/b} thing, bitch! This is {b}you!{/b}"
    "I wasn't sure who was getting swept up in whom, but for a moment, Rosalind bowed out of our repartee."
    "She just kept her sex-clouded eyes glued to me, mostly likely idling the seconds trying to gauge how {i}I{/i} wanted her to play this."
    rose "I, ah..."
    scene w3_9411 with dissolve
    "Finally, with a soft and plaintive voice at odds with the atmosphere..."
    scene w3_9412 with dissolve
    rose "I am {i}your{/i} bitch."
    scene w3_9411 with dissolve
    "{b}Bullseye.{/b}"
    "She said it with such conviction that I lost."
    scene w3_9413 with dissolve
    mc "Alright, then..."
    scene w3_9411 with dissolve
    "My own voice dropped down to a whispery cadence in unison with hers."
    scene w3_9413 with dissolve
    mc "I'm the king?"
    scene w3_9412 with dissolve
    rose "You're the fucking {b}king.{/b}"
    scene w3_9413 with dissolve
    mc "You want me to fuck you?"
    scene w3_9412 with dissolve
    rose "How many times do you want to make a woman say it? {b}Yes!{/b}"
    scene w3_9414 with dissolve
    "........."
    "......"
    scene w3_9415 with dissolve
    mc "{b}...well, too bad!{/b}"
    rose "A-ahh...?!"
    scene w3_9416 with dissolve
    mc "Fucking is for {i}peasants!{/i}"
    scene w3_9417 with dissolve
    "She looked at me confused."
    scene w3_9418 with dissolve

    if w2RosalindPhoto == True:
        mc "Know your place, {b}bitch!{/b}"
    else:
        mc "Know your place!"

    "I cackled inward, turning her shameless coaxing around on her."
    scene w3_9417 with dissolve
    rose "........."
    rose "......"
    scene w3_9419 with dissolve
    rose "Pffh! Ha!"
    scene w3_9420 with dissolve
    rose "Y-yes, sir!"
    "The older woman slunk to the floor, {i}amused.{/i}"
    scene w3_9421 with dissolve
    mc "Good. {i}Right{/i} where you belong."
    scene w3_9422 with dissolve
    mc "I don't just mean until I pop, either. My dick better not leave your mouth for ANY reason, got it? Your role tonight is {i}royal{/i} cock warmer."
    rose "I--"
    scene w3_9423 with dissolve
    mc "Don't speak, {b}cock warmer.{/b} Nod if you understand!"
    scene w3_9421 with dissolve
    scene w3_9424 with dissolve
    scene w3_9421 with dissolve
    "She nodded. {i}She understood.{/i}"
    scene w3_9425 with dissolve
    mc "Good girl..."
    "Years, even decades from now, I'd recall this night vividly."
    mc "You have permission to get my dick out."
    scene w3_9426 with dissolve
    "Just thinking about it would be enough to return me to this very moment in time, to live it again, and bring a flush to my face alongside a wistful longing for my youth."
    stop music fadeout 2.0
    scene black with fade
    "{b}Endless Blowjob Works{/b}"
    play music "music/echo-sclavi.ogg"
    scene w3_9427 with fade
    "It began as it should."
    "{i}With the unequivocal worship of my cock.{/i}"
    scene w3_9428 with dissolve
    "A testament to my virility, the caress of Rosalind's delicate fingers and a slavish kiss to my crown was all it took to get me to full mast."
    "From there, she didn't just throw herself into it."
    scene w3_9429 with dissolve
    "Her eyes lingered on my length, the motherly woman making a deliberate show of {i}taking in{/i} my magnificent endowment."
    rose "Heh... all night, huh...?"
    scene w3_9428 with dissolve
    "It wasn't as if this was her first time seeing it, but she {b}wanted{/b} me to read the awe and trepidation on her face."
    "She had taken me before, but {i}hours{/i} sucking on {b}that{/b} bitch breaker?"
    scene w3_9427 with dissolve
    "Was that {b}asshole{/b} serious? Would she even have a jaw after this?"
    scene w3_9428 with dissolve
    "These thoughts, for my delight, she conjured with her eyes."
    scene w3_9430 with dissolve
    mc "Don't just stare at it!"
    "I {b}commanded{/b}, juiced up on the feeling of superiority and cutting to the heart of the matter."
    mc "Lick my fuckin' balls, bitch!"
    play ambient "sound effects/fel4.wav"
    scene rosa_hd_13_a with fade
    show rosa_hd_13
    "In this moment, {i}I didn't care.{/i}"
    "The logistics of her marathon cock sucking? How she would pace herself? {b}Fuck that.{/b}"
    "Her very being existed for my exaltation, and even a second more of my cock going unattended was an affront to {i}me{/i} and her {b}purpose.{/b}"
    "Under my missive, she buried herself in my balls, resting the underside of my shaft across her face as if placing it on an altar."
    "As if to say, {i}look how big you are.{/i}"
    "Your masculinity dwarfs {b}all.{/b}"
    mc "Fuck yeah, it does... a-ah..."
    "For the time being, I was content in letting my cock warmer bask in my glow and do her thing."
    stop ambient
    scene w3_9431 with dissolve
    "From up high, I looked down on the mother's slutty ministrations, watching as she showered my member with admiration."
    scene w3_9432 with dissolve
    "Occasionally, she nuzzled her cheek against it as if it was precious."
    scene w3_9433 with dissolve
    "Other times, she lathered the underside of my shaft with gratitude."
    play ambient "sound effects/fel4.wav"
    scene rosa_hd_14_a with dissolve
    show rosa_hd_14
    "But mainly, she kept to task, lapping at my testicles like a devoted puppy, filling her nostrils with my musk and soaking herself in my ball sweat."
    mc "Ahh... you get the idea!"
    "Over and over, she alternated, cupping each of my royal jewels lovingly in her mouth and giving them both their deserved attention."
    mc "I taste good?"
    rose "Mmmh, mhmhhh...!"
    "She patronized me, moaning into my sack."

    if w2RosalindPhoto == True:
        mc "{b}Let me hear it, you old cow!{/b}"
        scene rosa_hd_13_a with dissolve
        show rosa_hd_13
        rose "Mmhh, mhhh...!"
        mc "That's fucking right, you disgusting cunt! {b}Eat my balls!{/b}"
        "I peppered the older woman with words of abuse, but the devotion did not abate ."
    else:
        mc "Let me hear it!"
        scene rosa_hd_13_a with dissolve
        show rosa_hd_13
        rose "Mmhh, mhhh...!"
        mc "That's right! Enjoy your fucking meal!"
        "I showered the older woman in vulgar encouragement."

    mc "Ah, aahh...♥ That's the fuckin' spot!"
    "How long did she toil away at my ballsack?"
    "{i}I dunno.{/i}"

    if w2RosalindPhoto == True:
        mc "Atta' bitch!!"
    else:
        mc "Atta' girl!"

    "Minutes...? Ten minutes...?"
    stop ambient fadeout 2.0
    scene black with fade
    "Something like that, until I grew numb to that flavor of submission."

    if w2RosalindPhoto == True:
        mc "It's not going to bite your whore ass, Rose."
    else:
        mc "It's not going to bite your ass, Rose."
    play ambient "sound effects/fel5.wav"
    scene rosa_hd_15_a with dissolve
    show rosa_hd_15
    "From there commenced the dick sucking."
    "For a while, I let Rosalind dictate the pace of her devotion, riding the high of my domination."
    "Naturally, Rosalind's approach to fellatio was clumsy, and the promise of a marathon session dulled her enthusiasm."
    "{i}She had to pace herself, after all.{/i}"
    rose "Mmhh, mhhh..."
    "Overall, her approach was tentative. {i}Restrained{/i}."
    "She never took me more than a third of the way, filling her cheeks out nicely with cock but always stopping short of her uvula."
    "To compensate for this lack of depth, she kept a firm hold on the base of my shaft, slightly jerking her wrist in an effort to make sure very little of my prodigious length went unattended."
    "{i}Of course, if this was her plan for the whole night...{/i}"
    mc "How's it taste?"
    rose "Mmmhh, euuahhh..."

    if w2RosalindPhoto == True:
        "The cow was sorely mistaken."
    else:
        "The motherly woman was sorely mistaken."
    stop ambient
    scene w3_9434 with dissolve
    rose "*Chwup, {b}chwwuuup*{/b}"
    scene w3_9435 with dissolve
    "Every so often, she'd free my dick from her mouth, and buy herself rest by showering my rod with kisses."
    scene w3_9434 with dissolve
    rose "{b}Like dick.{/b}"
    scene w3_9436 with dissolve
    "Another tactic in her arsenal, Rosalind would occasionally look up at me."
    rose "......"
    "...letting me know full damn well that her mind was focused {b}solely{/b} on adherence."
    play ambient "sound effects/fel5.wav"
    scene rosa_hd_15_a with dissolve
    show rosa_hd_15
    "It was always one or the other before dutifully jumping back into it with the same muted approach."
    rose "Mmhh, {b}*chwup!*{/b}"
    mc "Come on, you can do better than that, can't you?"
    rose "Mmh, mmhhh..."
    "{i}I wasn't really displeased.{/i}"
    mc "I mean, I'm the man, ain't I?!"
    "All this peacocking had me feeling like an actual king."
    "Her leisurely attention may not have been bringing me close to orgasm, but it kept me on edge."
    "There would be {i}many{/i} orgasms tonight."
    "{i}Too many.{/i}"
    "No need to fucking rush any of 'em."
    "Still, I had to make her think that I was unhappy."

    stop ambient
    scene w3_9437 with dissolve
    mc "Seriously...!"

    if w2RosalindPhoto == True:
        mc "Show some goddamn gratitude, whore."
    else:
        mc "Where's the gratitude?"

    scene w3_9438 with vpunch
    rose "{b}Gh!{/b}"
    stop music fadeout 3.0
    "It was more fun that way."
    scene black with fade
    "{b}Still.{/b} Twenty minutes in, and an orgasm and a half later, she was looking tired and I was growing bored with her monotonous service."
    play music "music/too-cool.ogg"
    scene w3_9439 with circlewipe
    "So I switched gears, turning our marathon into an impromptu adventure, dragging Rosalind all over the damn place."
    mc "My dick better not leave your mouth! Not to look at me, not to kiss it..."
    "Immersed in a game of {i}sucking my dick in every corner of the apartment.{/i}"
    play sound "sound effects/can.wav"
    scene w3_9440 with dissolve
    mc "*Glug, glug, glug* Ah, aaahh....!"
    "Pulling Rosalind to and fro, my insides twisted in sadistic delight as the older woman scrambled to keep up, knees knocking against the concrete floor."
    stop sound
    scene w3_9441 with dissolve
    rose "*Glug, glug, {b}glug!{/b}"
    scene w3_9442 with dissolve
    "Sometimes I'd face fuck her without mercy."
    scene w3_9443 with dissolve
    mc "Gah-! Fuckin--"
    rose "Ghhk, hhkkk-! Euuuueeek...!"
    mc "Choke on it! {b}Choke on it!{/b}"
    scene w3_9444 with dissolve
    rose "{b}*Shhlurrp-!*{/b}"
    "Other times I'd deign to let her rest, like I was granting her a great big favor, playing my role of a sanctimonious cunt of a god."
    scene w3_9445 with dissolve
    "Still, no matter where, no matter how..."
    scene w3_9446 with dissolve
    "I played out my juvenile power fantasy to a T."
    play ambient "sound effects/fel5.wav"
    scene w3_9447 with fade
    "{i}It was good to be {b}king.{/b}{/i}"
    scene w3_9448 with dissolve
    mc "...want a sip?"
    scene w3_9447 with dissolve
    rose "Mmh, euua... *Chwup~*"
    "Rosalind's denial of my generosity came in the form of obedience, the MILF lazily keeping on task while I took a load off."
    scene rosa_hd_16_a with dissolve
    show rosa_hd_16
    rose "Mmhh, {b}*Chwwwhup!*{/b}"
    mc "Well, probably a good idea..."
    rose "Mhh, euuuahh...!"
    mc "...not mixing a stomach of jizz with shitty beer, that is."
    rose "*Cwhhup, fwwhhhup-!*"
    mc "{size=-5}Ha... you perfect cocksucker...{/size}"
    "How long had she been at it?"
    "Caught up in the cock-getting-sucked reverie, I wasn't entirely sure. A couple of hours, maybe?"
    mc "{size=-5}Rose...{/size}"
    "Whatever the case, the sun had gone down, and my head was getting woozy."
    mc "{size=-5}You beautiful fuckin' bitch...{/size}"
    "--not from the beer I was drinking, although that certainly wasn't helping, but from the strain of my body supporting my {i}endless,{/i} {b}massive{/b} hard-on."
    mc "{size=-5}Ah, fuck...{/size}"
    "I muttered to myself like a moron."
    "{i}I may have been overly ambitious...{/i}"
    mc "{size=-5}Ah, fuck, fuck, fuck...{/size}"
    "She may or may not be able to survive four hours, but I didn't factor in my own endurance."
    rose "{b}*Cwhhup, fwhhhup...!*{/b}"
    "What Rosalind lacked in skill, she had made up for in persistence."
    rose "Ghhhupwwh, {b}*Chwwwup!*{/b}"
    "How many times had I cum?"
    stop ambient
    scene w3_9449 with pixellate
    "One."
    play sound "sound effects/spurt.wav"
    scene w3_9450 with flash
    rose "Euuhh...?!"
    "{i}Two.{/i}"
    play sound "sound effects/spurt.wav"
    scene w3_9451 with flash
    rose "Ghkkk!"
    "{b}Three.{/b}"
    play ambient "sound effects/fel5.wav"
    scene rosa_hd_16b_a with pixellate
    show rosa_hd_16b
    "{b}Three times!{/b}"
    "Yeeeeeeeeah..."
    rose "*Chwhhip, fwhhhup...!*"
    "And here Rosalind was working on number 4."

    if w2RosalindPhoto == True:
        mc "What am I going to do with you, slut? You're going to kill me."
    else:
        mc "You're going to kill me..."

    rose "Mmmh, mmhh, *chwwup!*"
    "Even this slow sort of suck, like water dripping on stone, could erode a man's soul."
    rose "Euuh, *Cwhhup*, mhhh...!"
    "Every time her tongue slithered down my glans it was like she was knocking on my spinal cord."
    rose "*CWhhup, fwhhup* Euaaahhh..."
    stop ambient
    scene w3_9452 with dissolve
    rose "...take a break?"
    scene w3_9453 with dissolve
    "She smiled, sensing my distance."
    "Her were eyes tired, but appropriately deferential to the mood."
    scene w3_9452 with dissolve
    rose "I've had to pee for the last hour..."
    scene w3_9454 with dissolve
    "...and before I knew it, I reached out to the older woman, cupping her cheek with affection."
    scene w3_9455 with dissolve
    mc "...I'm going to get rough."
    "{i}Denied.{/i}"
    scene w3_9454 with dissolve
    scene w3_9456 with dissolve
    scene w3_9454 with dissolve
    "{b}Cock warmers don't get to piss.{/b}"
    stop music fadeout 3.0
    play ambient "sound effects/fel2.wav"
    scene black with fade
    rose "Ghhhk, hggghhhk!"
    "This would be the end of it, but I wouldn't let her know that yet."
    rose "{b}Ghhhh, hhhhkk, eehuhuuK!{/b}"
    play music "music/drum-bass.ogg"
    scene rosa_hd_17_a with fade
    show rosa_hd_17
    "All I wanted Rosalind to know was the sensation of my dick hitting the back of her skull."
    mc "Gah! You conniving--!"
    rose "Ghhhk, hhhhkkk!!!"
    "Of my glans digging into her tongue, and of my shaft filling her throat."
    mc "I'm the king, huh?!"
    rose "Hkkkk!"
    "So I pistoned my hips, without restraint, alone in the knowledge that this would be the evening's last hoorah."
    mct "(See me for who I am, Rose!)"
    rose "Hkkkk, hheeuuuuuhhhhh....!"
    mc "What fuckin' good are you?!"

    if w2RosalindPhoto == True:
        mct "(See me for who I am, you fat tittied slut!!)"
    else:
        mct "(See me for who I am, you beautiful bitch!!)"

    "I thrusted and I thrusted, battering the motherly woman's mouth and riding the elation that Rosalind might finally come to understand what an asshole I truly am."
    mct "(Oh, fuck!)"
    scene rosa_hd_17b_a with dissolve
    show rosa_hd_17b
    rose "Ghhhk, {b}hhhhhk-!!!!{/b}"
    "After all, {i}I was a pig.{/i}"
    "I had spun the nice act of making dinner for a house guest into an exploitative romp for my sole gratification."
    rose "Heueuh, hekkhhh, eiuii!"
    "Rosalind had not only accepted the turn of events without complaint, but {i}encouraged it.{/i}"
    mc "God, you're so-!!!"
    "{i}Why did that incense me so?{/i}"
    rose "Hhhhk, hheuuhhk, euhjhkkkk...!!!"
    scene rosa_hd_17_a with dissolve
    show rosa_hd_17
    "It both propelled my hips forward with violent enthusiasm and left something to be desired."
    rose "Ghh, hhnmeueueuk!"
    "I was getting everything I wanted, and sure, that excited me."
    rose "Ehhm hhhkk, hhhkkeeuuu-!"
    "The thing was, while I was happy to be mask off, something else was {i}off.{/i}."
    "When she asked for a break and I denied her, she had {b}nodded.{/i}"
    "{i}Of course.{/i} {b}Okay{/b}"
    rose "Heuuhhk!"
    scene rosa_hd_17b_a with dissolve
    show rosa_hd_17b
    "Instead of a troubled expression I could delight in, her placid expression held a mirror up to my soul."
    rose "Heeuuhhk, heeeuuhkhhkk!"
    "What reflected back wasn't a king, but a boy without agency, swept away."
    mc "Ah, hhmaa, haahhh..."
    "{i}If someone proclaims that you can eat as much as you want, who is to blame if you engorge yourself to the point of sickness?{/i}"
    rose "Ehuuh, hkhkggg!"
    "{i}Consider where you will draw {b}lines.{/b}{/i}"
    rose "Hnngg, euhuhhkk, ehhhkkkeuhh!"
    "{i}If you master yourself, the world becomes a lot simpler -- and makes finally indulging yourself all the more vivid when you do.{/i}"
    mc "Oh--"
    play sound "sound effects/spurt.wav"
    scene rosa_hd_18_a with flash
    play ambient "sound effects/gulp2.wav"
    show rosa_hd_18
    rose "MMhmh, mhmhmhhm!"
    "As I came down this slobbering bitch's throat--"
    with flash
    play sound "sound effects/spurt.wav"
    mc "Drink it down, {b}whore!{/b}"
    "I understood Dr. Chuck better, both his character and his philosophy."
    rose "Mmmh, mhmhmh!"

    if w2RosalindPhoto == True:
        mc "Stupid fucking hole!"
    else:
        mc "A-aah!"

    "My position had simply fallen into my lap, and while enjoyable, there was an imperfect satisfaction in that."
    stop ambient
    scene w3_9457 with dissolve
    if not persistent.w3RosalindKing:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3RosalindKing = True
    "As fucked up and deluded as it sounds, as I glanced down at Rosalind's messed up expression, I had a thought."
    "If I'm going to be an asshole..."
    rose "Geahhh...."
    stop music fadeout 3.0
    scene black with fade
    $ history_rosalind = "I pivoted a nice dinner into a marathon face fucking session with the MILF, who impressively rose to the occasion."
    $ unread_rosalind = True
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    "I should at least become an asshole {i}worthy{/i} of Rosalind's degradation."
    "......"
    "..."
    $ renpy.end_replay()
    jump June19Start


label w3RosalindPostSexInterlude:
    play music "music/mourning-dove.ogg"
    scene w3_9506 with circlewipe
    show screen textbox2 with dissolve
    "The rest of the night was spent in a lazy embrace, Rosalind and I curled up on the couch."
    "At some point, she fetched some reading material and I adopted the role of pillow."
    scene w3_9507 with dissolve
    mc "...boils over in a wave of alabaster cum?"
    scene w3_9508 with dissolve
    rose "Don't read ahead of me!"
    scene w3_9506 with dissolve
    "The mood between us had changed. Rosalind remained her usual gentle self, but the underlying tension was cut."
    scene w3_9509 with dissolve
    "She abandoned all motherly affectation, her bread-and-butter weapon against me, and instead {i}selfishly{/i} took shelter in my shadow."
    scene w3_9510 with dissolve
    rose "...you read much?"
    scene w3_9511 with dissolve
    mc "Mostly textbooks..."
    scene w3_9509 with dissolve
    "Her shape, her warmth, the smell of our exertion... all of it kept the memory of our romp alive."
    scene w3_9512 with dissolve
    "........."
    "......"
    rose "...what's going to become of Oliver?"
    mc "...huh?"
    scene w3_9513 with dissolve
    rose "If I'll be able to go home soon, that means he's gonna be taken care of even sooner..."
    scene w3_9514 with dissolve
    mc "...are you worried about him?"
    scene w3_9515 with dissolve
    "......"
    "...she didn't answer."
    scene w3_9516 with dissolve
    rose "How's he being dealt with, [mcf]? I have a right to know..."

    if w3RosalindViolentSolution == True:
        scene w3_9517 with dissolve
        mc "Let's just say... whatever happens to him, it's something I'd rather not know about."
        scene w3_9518 with dissolve
        rose "...is he going to get hurt?"
        scene w3_9519 with dissolve
        "I gave Rosalind a squeeze in confirmation."
        scene w3_9517 with dissolve
        mc "I don't know to what extent."
        scene w3_9518 with dissolve
        rose "...serves that asshole right -- {i}that's what I want to say.{/i}"
    else:

        scene w3_9520 with dissolve
        mc "The MHPD is going to put him out of business."
        scene w3_9521 with dissolve
        rose "...r-really? That simple?"
        scene w3_9514 with dissolve
        mc "Our friends at the club can move mountains..."
        scene w3_9521 with dissolve
        rose "{b}Wow...{/b}"
        scene w3_9518 with dissolve

    rose "...were you scared when you met him?"
    scene w3_9522 with dissolve
    mc "Why are you asking that?"
    scene w3_9523 with dissolve
    rose "It's not every day a man stands up for me..."
    scene w3_9524 with dissolve
    mc "To answer your question, {b}yes{/b}, but I didn't have a choice."
    scene w3_9523 with dissolve
    rose "...didn't have a choice? That's... you're a college student, he's a hardened criminal."
    scene w3_9524 with dissolve
    mc "The fucker was in your home, Rose. {i}The place you raise your daughter.{/i}"
    scene w3_9525 with dissolve
    "........."
    "......"
    scene w3_9526 with dissolve
    rose "...mmmhh."
    "Her lips tasted even sweeter than earlier."
    scene w3_9527 with dissolve
    mc "What was...?"
    scene w3_9528 with dissolve
    rose "{i}No choice.{/i}"
    scene w3_9529 with dissolve
    mc "Shut up..."
    stop music fadeout 3.0
    scene black with fade
    "That night, she finished her book."
    "......"
    "..."
    jump June19Start

label w3RosalindMovieInterlude:
    scene w3_9530 with circlewipe
    play music "music/mourning-dove.ogg"
    "We watched two, in fact. Reticent to come back to the real world, and comfortable in each other's company."
    "Even more so than the rest of her stay, I think she appreciated the disconnect."
    scene w3_9531 with dissolve
    "After the movies, she shared one final thing that was on her mind."
    "{i}What was going to happen to Oliver?{/i}"
    scene w3_9532 with dissolve

    if w3RosalindViolentSolution == True:
        mc "He's probably going to get his ass kicked. I don't know to what extent."
        scene w3_9533 with dissolve
        rose "...{b}good.{/b}"
    else:

        mc "The cops are going to raid him. Turns out our friends at the club can move mountains."
        scene w3_9534 with dissolve
        rose "{b}Wow...{/b}"

    scene w3_9535 with dissolve
    "I understood her frustration."
    scene w3_9536 with dissolve
    rose "Thanks, [mcf]. For a lot of things..."
    scene w3_9537 with dissolve
    "........."
    "......"
    scene w3_9538 with dissolve
    mc "...no problem."
    stop music fadeout 3.0
    scene black with fade
    "Before bed, Rosalind helped me clean up. A pep in her step, {b}humming.{/b}"
    "......"
    "..."
    jump June19Start


label w3RosalindDateFailInterlude:
    scene w3_9539 with circlewipe
    "We cleaned up."
    scene w3_9530 with dissolve
    "Watched a movie."
    scene w3_9540 with dissolve
    "Went to bed."
    "As I was falling asleep..."
    stop music fadeout 3.0
    scene black with fade
    "I couldn't help but feel I could have somehow gotten {b}more{/b} out of Rosalind..."
    "......"
    "..."
    jump June19Start

label June19Start:
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionhana04 with blinds
    $ renpy.pause(6, hard=True)
    $ date = "june19day"
    scene w3_9541 with blinds
    show screen qmenu with dissolve
    "The next morning, we continued what was safe to call a routine."
    show june19day with squares
    "I was slow to get up, but the smell of bacon proved a strong motivator."
    "I showered, ate, and listened to Rosalind hum yet another one of her old lady songs..."
    play sound "sound effects/door-bell.wav"
    scene w3_9542 with dissolve
    show screen textbox2 with dissolve
    "All until, {b}we had a visitor.{/b}"
    scene black with dissolve
    "Out of politeness, I offered a cup of coffee."
    "{i}I didn't expect the mother fucker to accept.{/i}"
    mc "You know..."
    scene black with dissolve
    play music "music/i-knew-a-guy.ogg"
    scene w3_9543 with dissolve
    mc "...I didn't take you for a milk and sugar kind of guy."
    scene w3_9544 with dissolve
    war "Life's too short to drink nothing but kerosene, kid."
    scene w3_9545 with dissolve
    rose "Uh, here you are... careful, it's--"
    hide screen textbox2 with dissolve
    scene w3_9546 with dissolve
    war "Thanks, slut."
    scene w3_9547 with dissolve
    war "If it doesn't make you feel good, it should at least taste good."
    scene w3_9548 with dissolve
    rose "O-ah... you sure you don't want some eggs or...?"
    war "Just coffee."
    scene w3_9549 with dissolve
    rose "Alright, I'm going to go, uh--"
    war "...what the fuck you staring at?"
    scene w3_9550 with dissolve

    menu:
        "Tell him not to touch Rosalind."(chg=["rosalind_passion_up","warren_down"]):
            $ Rosalind_Libido += 1
            $ Warren_Friendship -= 1
            $ w3WarrenStandOff = True
            scene w3_9551 with dissolve
            "What started as a mere flicker of irritation {b}grew{/b} immensely with his challenge."
            scene w3_9552 with dissolve
            mc "Don't get touchy, huh? Please?"
            scene w3_9551 with dissolve
            "Without thinking, I let fly my animosity."
            scene w3_9553 with dissolve
            war "Ha! Shove that white knight crap."
            "And like I was nothing, as if he wasn't sitting in {i}my home{/i}, he brushed me off."
            scene w3_9554 with dissolve
            war "She's club goods. I could have my hand wrist deep in her snatch if I wanted to."
            scene w3_9555 with dissolve
            war "A little feel doesn't sound too bad now, does it?"
            rose "It's okay, [mcf], I don't--"
            scene w3_9556 with dissolve
            rose "A-ahh..."
            "Contrary to my purpose, I gestured for the older woman to shut her fucking mouth. I didn't care if she'd let it slide..."
            scene w3_9557 with dissolve
            mc "She's {i}my{/i} guest under my hospitality, {b}Warren.{/b}"
            scene w3_9560 with dissolve
            "It was a matter of propriety."
            scene w3_9559 with dissolve
            mc "Are you trying to make me look like a bad host?"

            if w3RosalindEndlessBJWorks == True:
                scene w3_9560 with dissolve
                "A hypocritical sentiment considering what I made her do last night, but {b}fuck it.{/b}. I'd stake this hill."
            elif w3RoseStayLewd == 1:
                scene w3_9560 with dissolve
                "A hypocritical sentiment considering what I made her do a few nights ago, but {b}fuck it.{/b} I'd stake this hill."
            else:
                pass

            scene w3_9558 with dissolve
            war "Tryin' to lose that hand?"
            scene w3_9559 with dissolve
            mc "...and how would you explain that to Dr. Chuck?"
            scene w3_9560 with dissolve
            "It was too early to be this angry, and Warren was too big and scary for me to raise an issue over a meager {i}butt grab{/i}, but I knew the score. He wouldn't do shit to me, not over something like this."
            scene w3_9561 with dissolve
            mc "You're my guest too, by the way. {b}Enjoy the coffee.{/b}"
            "He wasn't {i}that{/i} stupid, and this was a chance to rectify his mistake of thinking me a pushover."
            $ renpy.music.set_volume(.05, 3, channel = "music")
            play sound "sound effects/horror.wav"
            scene w3_9562 with dissolve:
                align (0.5,0.5)
                linear 160 zoom 2.5
                pause 4
            "Still... {i}fuck.{/i}"
            "His cold eyes made me briefly reconsider my hubris, but the adrenaline and machismo kept me rooted in place. {i}The die was cast.{/i}"
            "......"
            $ renpy.music.set_volume(1, 3, channel = "music")
            stop sound
            scene w3_9563 with dissolve
            war "...Alright. Your house, your rules."
            scene w3_9564 with dissolve
            mc "Thank you."
            scene w3_9565 with dissolve
            rose "I'll get you another...?"
            "It might've been my imagination, but the way Rosalind touched me had a {b}charge.{/b}"
            scene w3_9566 with dissolve
            mc "I'll have it with some milk and sugar this time."
            scene w3_9567 with dissolve
            mc "Life's too short."
        "Keep your mouth shut.":


            scene w3_9568 with dissolve
            "...getting angry over his disrespect toward Rose would not only be irrational, but hypocritical."
            scene w3_9569 with dissolve
            mc "Just your handsome face."
            scene w3_9570 with dissolve
            "And while part of me {i}was{/i} irritated that he interrupted my domestic delusion, it's not like he was here for fun. {i}He had a reason.{/i}"
            scene w3_9571 with dissolve
            mc "Sugar and coffee this time, please."
            rose "Oh, uh... s-sure!"
            scene w3_9572 with dissolve
            "Still, the least I could do is give Rosalind a reason to stay busy."
        "You're looking at an ugly son of a bitch."(chg=["warren_up"]):

            $ Warren_Friendship +=1
            scene w3_9573 with dissolve
            mc "An ugly bastard, you prick."
            scene w3_9574 with dissolve
            war "Ha! Don't talk to me like we're friends."
            scene w3_9575 with dissolve
            mc "We're more than that, Warren. You've heard Dr. Chuck's spiel."
            scene w3_9576 with dissolve
            war "Don't give me that family shit."
            mc "At the very least, you're my guest."
            scene w3_9577 with dissolve
            mc "Sugar and coffee this time, please."
            rose "Oh, uh... s-sure!"
            scene w3_9578 with dissolve
            mc "I believe we can all learn something from each other."
            mc "Like, I don't know... I can lighten up and you can chill the fuck out."
            scene w3_9579 with dissolve
            war "Ha! Whatever!"

    scene black with fade
    "We said little for a few minutes."
    scene w3_9580 with fade
    "Warren was not only a man of excruciatingly few words, but was intent on not mixing business and pleasure. Every time I thought we were about to get to the business at hand, he took a sip."
    war "You know, the first time you and I met, she was here too."
    scene w3_9581 with dissolve
    mc "Yeah, that's true...."
    war "Cushy fuckin' job, you landed. Got this bitch clinging to your nuts, huh?"
    scene w3_9582 with dissolve
    mc "It's not like that."
    scene w3_9583 with dissolve
    war "The fuck it isn't."

    if w3WarrenStandOff == True:
        war "With that whole tiff just now?"
    else:
        war "With how you looked at me earlier?"

    if hanaFlag == True:
        war "Then there's you and the boss' daughter..."
    else:
        pass

    scene w3_9584 with dissolve
    mc "What's your point? You jealous?"
    scene w3_9585 with dissolve
    war "Fuck no. Of a witless cunt like you?"
    scene w3_9586 with dissolve
    "......"
    scene w3_9584 with dissolve
    mc "...so, to what do I owe your unexpected visit?"
    scene w3_9587 with dissolve
    war "Ha! Finally got you to ask!"
    scene w3_9588 with dissolve
    war "Bitch here is good to go."
    scene w3_9584 with dissolve
    mc "You came here to tell us that?"
    scene w3_9585 with dissolve
    war "Not something for a phone call."
    scene w3_9589 with dissolve
    "......"
    "........."
    play ambient "sound effects/ringing-inbound.wav"
    scene w3_9590 with dissolve
    mc "...one sec."
    stop ambient
    play sound "sound effects/phonemenu.wav"
    play music "music/take-the-lead.ogg"
    scene w3_9591 with dissolve
    mc "Hey, what's up?"
    hana "I wake you?"
    scene w3_9592 with dissolve
    mc "Nope, actually... I've got Warren here. We're having a cup of coffee."
    scene w3_9593 with dissolve
    hana "What? Like {i}Club{/i} Warren? Drinking coffee? In your apartment?"
    scene w3_9594 with dissolve
    mc "...uh huh, that describes it."
    scene w3_9595 with dissolve
    hana "Well, well, well. {i}Don't want to keep you from that.{/i}"
    hana "I'll be quick then: I've got a show tonight. {i}Come.{/i}"
    scene w3_9596 with dissolve
    mc "You're asking me to--?"
    scene w3_9597 with dissolve
    hana "{b}Come.{/b}"

    if hanaFlag == False:
        hana "You blew me off last time, but we're friends now. No choice."

    scene w3_9598 with dissolve
    "........."
    "......"
    scene w3_9599 with dissolve
    mc "...can I invite the Carnations?"
    scene w3_9597 with dissolve
    hana "The Car--? Uh, yeah, sure..."
    scene w3_9596 with dissolve
    mc "Thanks. I've got this stupid thing I started two weeks ago where I get them together each week before the competition."
    scene w3_9600 with dissolve
    hana "...for real? Shit, you've got middle manager written all over you!"
    scene w3_9601 with dissolve
    mc "...don't I?"
    scene w3_9602 with dissolve
    hana "But yeah, if they want to come sure. The more the merrier. Maybe they can blow off some steam before we pimp 'em out tomorrow."
    scene w3_9601 with dissolve
    mc "{i}Funny.{/i}"
    scene w3_9603 with dissolve
    hana "By the way, I also invited blondie."
    scene w3_9601 with dissolve
    mc "Mina...?"
    scene w3_9600 with dissolve
    hana "Yep. Guess there'll be all sorts of people to see little ol' me blow the roof off the place. Hell, invite Ian, will ya?"
    scene w3_9601 with dissolve
    mc "With Mina there? Probably not a--"
    scene w3_9602 with dissolve
    hana "I ran it by her. I invited Jacob, {i}and you{/i}, so it'll hurt his feelings if we don't. It's a big place, the ex-lovers will have space."
    scene w3_9603 with dissolve
    hana "Besides, it'll be kinda fun to see how they act."
    scene w3_9601 with dissolve

    if hanaFlag == True:
        mc "...you're more sadistic than you get credit for. Same place as last time?"
    else:
        mc "...you're more sadistic than you get credit for. You'll send me the place?"

    scene w3_9603 with dissolve
    hana "Yep. It's settled, then."
    scene w3_9600 with dissolve
    hana "I will let you get back to your illustrious company, then."
    scene w3_9604 with dissolve
    mc "Don't go! He's staring right at--"
    scene w3_9605 with dissolve

    if hanaGF == True:
        hana "See you, boyfriend."
    elif w3HanaDP >= 4:
        hana "See you, lover boy."
    else:
        hana "See ya!"

    play sound "sound effects/phonemenu.wav"
    play music "music/i-knew-a-guy.ogg"
    scene w3_9606 with dissolve
    "........."
    "......"
    scene w3_9607 with dissolve
    war "...as I was saying, it's not the kind of information you relay over a phone."
    scene w3_9608 with dissolve
    mc "...but it's taken care of? For real this time? {b}Last time it wasn't.{/b}"

    if w3RosalindViolentSolution == True:
        scene w3_9609 with dissolve
        war "The {b}fuck{/b} did I just say?"
        scene w3_9610 with dissolve
        "{i}He didn't like that.{/i}"
        scene w3_9611 with dissolve
        war "Keep an eye out for the news."
        scene w3_9612 with dissolve
        mc "...it's gonna make the news?"
        scene w3_9611 with dissolve
        war "Jacob didn't half-ass it, kid."
        scene w3_9613 with dissolve
        "His cold tone did not lie, sending chills down my spine."
        scene w3_9611 with dissolve
        war "The woman has one less thing to worry about."
        scene w3_9613 with dissolve
        "........."
        scene w3_9614 with dissolve
        "......"
        scene w3_9615 with dissolve
        war "...what?"
        scene w3_9616 with dissolve
        rose "Uh... {i}t-thank you.{/i}"
        scene w3_9617 with dissolve
        "........."
        "......"
        scene w3_9615 with dissolve
        war "...I didn't do it for you."
    else:

        scene w3_9618 with dissolve
        war "That's the word from Dr. God himself, passed down from the mount, from his humble servant to your ears."
        scene w3_9619 with dissolve
        war "A bust like that probably wouldn't make the news, but they... {i}resisted.{/i}"
        scene w3_9620 with dissolve
        mc "I see..."
        scene w3_9621 with dissolve
        "{i}What did that mean {b}exactly{/b}?{/i}"
        scene w3_9622 with dissolve
        war "Don't look all white, kid. They're scum, knew the rules, played the game..."
        scene w3_9619 with dissolve
        war "All things considered, a few of 'em eating their 3 squares a day through a straw is getting off easy considering who they pissed off."
        scene w3_9623 with dissolve
        mc "Dr. Chuck, you mean?"
        scene w3_9619 with dissolve
        war "The fucked up thing is they have no idea who they crossed. They just went about their business and, pow! Get smote, poor bastards!"
        scene w3_9622 with dissolve
        war "That's real power for 'ya..."
        scene w3_9624 with dissolve
        rose "...I don't have to worry about him?"
        scene w3_9625 with dissolve
        war "Yeah, you're good, beautiful."


    scene w3_9626 with dissolve
    war "Thanks for the coffee."

    if w2ExEndingKathleen == True:
        scene w3_9627 with dissolve
        war "Oh, one more thing. Mrs. P said she'll drop at 1 PM. Said you probably know what it's about."
        scene w3_9628 with dissolve
        mc "...alone?"
        scene w3_9627 with dissolve
        war "Beats the fuck out of me."
        scene w3_9629 with dissolve
        war "See 'ya, kid."

    scene black with fade
    "And like that, he was gone. {i}He took the cup too.{/i}"
    play music "music/mourning-dove.ogg"
    scene w3_9630 with dissolve
    show screen textbox2 with dissolve
    mc "........."
    rose "......"
    scene w3_9631 with dissolve
    mc "...pleasant start of the day, huh? How are you feeling?"
    scene w3_9632 with dissolve
    rose "I'm..."
    scene w3_9633 with dissolve
    rose "I feel the same."
    scene w3_9634 with dissolve
    mc "You would, wouldn't you... at least you don't feel worse. Olly brought this on himself."
    scene w3_9633 with dissolve
    rose "Is that for me or for you?"
    scene w3_9635 with dissolve
    mc "That..."
    "When she wanted to, Rosalind could cut through the bullshit like a hot knife."
    scene w3_9636 with dissolve
    mc "Who knows. It's a new feeling for both of us."
    scene w3_9637 with dissolve
    "A touch..."
    "A warm, comforting hand..."
    "{i}Don't think about it.{/i}"
    "I'm not sure if that's what she was trying to convey, but that's what I chose to get out of it."
    scene w3_9638 with dissolve
    rose "I'll get out of here as soon as possible."
    scene w3_9639 with dissolve
    "Naturally, she would want that."
    "{i}...did I?{/i}"
    hide screen textbox2 with dissolve

    menu w3RosalindLeaveChoice:
        "{color=#FF1493}[[Openness]{/color} She can stay as long as she wants. (w3RosalindInviteStay = True)" if w3RTalkOpenness ==3:
            $ w3RosalindInviteStay = True
            scene w3_9640 with dissolve
            show screen textbox2 with dissolve
            mc "...you know, I'm not chasing you out."
            scene w3_9641 with dissolve
            rose "I know..."
            scene w3_9640 with dissolve
            mc "If you're not comfortable going home, you can stay as long as you want."
            scene w3_9639 with dissolve
            "......"
            scene w3_9638 with dissolve
            rose "...thanks for the offer, but--"
            scene w3_9642 with dissolve
            mc "Yeah, {b}okay.{/b}"
            "I only hoped my touch was as warm as hers."
        "If she needs anything, {b}call.{/b}":

            scene w3_9640 with dissolve
            show screen textbox2 with dissolve
            mc "I'm a phone call away, Rose. If there's any trouble--"
            scene w3_9638 with dissolve
            rose "Thanks, [mcf]."
            scene w3_9639 with dissolve
            "......"
            "..."

        "{color=#696969}[[Openness] She can stay as long as she wants.{/color}" if w3RTalkOpenness < 3:
            jump w3RosalindLeaveChoice


    scene w3_9645 with dissolve
    mc "Hana's band is playing a show tonight. Be there, alright? {i}Carnation thing.{/i}"
    scene w3_9644 with dissolve
    rose "...you're still insisting on that?"
    scene w3_9643 with dissolve
    mc "{b}I am.{/b}"

    if kat_polite == True:
        "{i}Even after watching them go at it for Mrs. Pulman's punishment game, I was.{/i}"
    else:
        "{i}Even after watching them go at it for Kathleen's punishment game, I was.{/b}"

    if w2ExEndingKathleen == True:
        "Who, speaking of which, will be here this afternoon."

    "{i}I needed to invite Veronica and Felicia.{/i}"
    scene w3_9645 with dissolve
    mc "I think I'm going to go hit the gym. You good holding down the fort?"
    scene w3_9644 with dissolve
    rose "You needn't worry about me, [mcf]."
    scene w3_9643 with dissolve
    mc "Who said I was--"
    stop music fadeout 3.0
    scene black with fade
    "......"
    "..."
    jump w3VeroDannyMeeting

label w3VeroDannyMeeting:
    play ambient "sound effects/gym.wav"
    scene w3_9646 with blinds
    "A bag of gym clothes, and a leisurely walk later, I was at Veronica's money suck-hole of a gym."
    "I could've just called, but I wanted to {i}see{/i} her. She was less likely to wiggle out of my invitation if I insisted face-to-face."
    "Plus, I {b}did{/b} make a commitment to stay fit when I signed up... so, while in Rome..."
    play music "music/training-in-fire.ogg"
    scene w3_9647 with dissolve
    ver "Everything's good, coach. You don't have to worry about me."
    scene w3_9648 with dissolve
    coach "I know, sweetums. You're a strong gal, but I also know how life can pile on..."
    scene w3_9649 with dissolve
    ver "Yet, here you stand healthier than ever. That's inspiration enough to not just lie down and die!"
    scene w3_9650 with dissolve
    coach "...so you don't mind if I go to the wedding, then?"
    scene w3_9651 with dissolve
    ver "No, of course not, Jesus!"
    scene w3_9650 with dissolve
    coach "I just can't help, but feel a little responsible..."
    scene w3_9651 with dissolve
    ver "I insisted!"
    scene w3_9652 with dissolve
    "{i}Lucky me.{/i} There she was."
    ver "...?"
    "Veronica saved me the trouble of looking for her."
    scene w3_9653 with dissolve
    "Only a few people were milling about the gym, but it was more than I'd ever seen in the place."
    "One such miller was a leathery old man, skinny, but with a large frame. Even shrunk with age, I could tell the man used to be an athlete."
    scene w3_9654 with dissolve
    mc "Just the woman I was hoping to see."
    scene w3_9655 with dissolve
    ver "[mcf]..."


    if w3VeroBarDate == True:
        scene w3_9656 with dissolve
        ver "You're here to work out?"
        scene w3_9657 with dissolve
        mc "That, and I wanted to find out if you're free tonight."

        if w3VeronicaSex == True:
            scene w3_9658 with dissolve
            ver "I, uh... ah..."
            ver "Twice in a week is--"
        else:
            scene w3_9655 with dissolve
            ver "I don't know if I can afford twice in a--"
            scene w3_9654 with dissolve
            mc "First of all, I paid last time. Second--"
    else:

        ver "...you're here to work out?"
        scene w3_9654 with dissolve
        mc "And to invite you somewhere."
        scene w3_9659 with dissolve
        ver "You'd have better luck--"

    scene w3_9660 with dissolve
    coach "Who's this, Ronnie? A friend?"
    scene w3_9661 with dissolve
    "........."
    "......"

    if veronicaFriend == True:
        scene w3_9662 with dissolve
        ver "...yeah, he's a friend. Name's [mcf]."
    else:
        scene w3_9663 with dissolve
        ver "He's a member of the gym."
        "{i}Ouch.{/i}"
        scene w3_9664 with dissolve
        mc "The name's [mcf]."

    scene w3_9665 with dissolve
    coach "So I caught that."
    scene w3_9666 with dissolve
    ver "This is my former training coach."
    scene w3_9667 with dissolve

    if VeroFlag == True:
        "Ah, yes. If Samson is to be believed, this was the man who sold the gym to Veronica under Samson's insistence, and pointed her toward an unfavorable leasing company for her equipment..."
        mc "Nice to meet you..."
        "{i}What was he sniffing around for?{/i}"
    else:
        mc "Nice to meet you..."

    scene w3_9668 with dissolve
    ver "It's been a while since we last saw each other. We're playing catch up."
    mc "I see..."
    scene w3_9669 with dissolve
    ver "He had a 6-month ticket to live three years ago!"
    "The man in front of me did look healthy."
    scene w3_9670 with dissolve
    coach "Now I don't know what to do with my time."
    scene w3_9671 with dissolve

    if VeroFlag == True:
        "For someone who offloaded a failing business to a mentee, he seemed to be doing well for himself."
    else:

        "--and more than healthy, he looked like he was doing well for himself."

    mct "(An obnoxious spray tan, brand named watch, expensive shoes...)"
    "He wore his cologne in such quantity that I might suffocate if I got any closer."

    scene w3_9672 with dissolve
    mc "That's wonderful. Congratulations on your health."
    coach "Every day's a gift."

    if VeroFlag == True:
        "Even without what I knew, this man would rub me the wrong way. He didn't seem that different from the men I rubbed elbows with, and {i}that{/i} was the problem."
    else:
        "Something about this man rubbed me the wrong way. He didn't seem that different than the men I know rubbed elbows with, and {i}that{/i} was the problem."

    scene w3_9673 with dissolve
    mc "Well, I'll go get changed, work out, leave you two to your discussions. It was nice meeting you..."
    coach "Danny."
    mc "{b}Danny.{/b}"

    if veronicaFriend == True:
        scene w3_9674 with dissolve
        ver "I'll find you later."
    else:
        scene w3_9675 with dissolve
        ver "I'll find you later."

    scene black with fade
    "...and so, {b}later.{/b}"
    scene w3_9676 with circlewipe
    "After a brief workout--"
    scene w3_9677 with wipeleft
    "Veronica's mentor departed--"
    scene w3_9678 with w24
    "The place thinned out, and--"
    stop music fadeout 3.0
    scene black with fade
    ver "You're inviting me to a {b}rock show?{/b}"
    scene w3_9679 with dissolve
    mc "You, Felicia, and Rosalind."

    if minaGym == True:
        scene w3_9680 with dissolve
        mc "Oh, and Mina's going to be there. Remember her?"
        scene w3_9681 with dissolve
        ver "Of course I remember her. Unlike a certain someone, she's been coming here twice a week."
        scene w3_9682 with dissolve
        mc "Oh, yeah...?"
        scene w3_9683 with dissolve
        ver "Actually, she has an appointment in like 20 minutes. {i}Sweet girl.{/i}"
        mc "I've been busy..."

    scene w3_9684 with dissolve
    ver "And this is mandatory?"
    scene w3_9679 with dissolve
    mc "Better than doing it in the morning, yeah? Besides, it'll be fun."
    stop ambient fadeout 3.0
    scene w3_9685 with dissolve
    ver "......"

    play music "music/brooklyn-nights.ogg"
    if w3VeroBarDate == True:
        scene w3_9686 with dissolve
        ver "It might be. You surprised me last time. You payin'?"
        scene w3_9687 with dissolve
        mc "What am I, your sugar daddy now?"
        scene w3_9688 with dissolve
        ver "You are {i}so{/i} good to me, [mcf]..."
        scene w3_9689 with dissolve
        ver "{i}Daddy.{/i}"
        scene w3_9690 with dissolve
        "Gah, fuck! A woman like Veronica saying--"
        scene w3_9691 with dissolve
        mc "Yeah, I'm paying. Only fair since I'm mandating it. Three drinks though!"
    else:
        scene w3_9686 with dissolve
        ver "...you paying for the drinks?"
        scene w3_9687 with dissolve
        mc "Yeah, sure. If it'll get you to come."
        scene w3_9685 with dissolve
        "......"
        scene w3_9686 with dissolve
        ver "...alright."
        scene w3_9687 with dissolve

    mc "Other than that, how are you doing?"
    scene w3_9692 with dissolve
    ver "I'm... ah..."

    if w3VeroBarDate == True:
        scene w3_9693 with dissolve
        ver "Not much new over the course of a few days, [mcf]."
        ver "Thanks for asking, though..."
        scene w3_9691 with dissolve

    elif veronicaFriend == True:
        scene w3_9693 with dissolve
        ver "Eh, I'm alright. {i}Hanging in there.{/i}"
        ver "Thanks for asking."
        scene w3_9691 with dissolve
    else:

        scene w3_9694 with dissolve
        ver "Eh. {b}I'm good.{/b}"
        scene w3_9687 with dissolve

    mc "Your coach seemed like a nice man."
    scene w3_9686 with dissolve
    ver "...is that the impression you got?"
    scene w3_9687 with dissolve
    mc "No, I actually found him pretty gaudy."
    scene w3_9694 with dissolve
    ver "Yeeeeeeah... {i}I'm{/i} not going to say anything bad about him, but I can see where that might come from."
    scene w3_9695 with dissolve
    ver "But hey, you get sick {i}and{/i} cheat death, that probably realigns your perspective."
    scene w3_9685 with dissolve
    mc "What? He didn't use to murder people's sense of smell?"
    scene w3_9693 with dissolve
    ver "Ha! No! He was a real cheap ass."
    scene w3_9691 with dissolve
    mc "Well, can't take it with you, I guess..."

    if VeroFlag == True:
        scene w3_9696 with dissolve
        "Or whatever he had going with Samson was {i}lucrative.{/i}"
        "Again, part of me felt a pang of guilt and the compulsion of honesty."
        "Veronica had no fucking idea just whose tendrils were sinking her, but telling her anything about it wouldn't be doing her a service."
        scene w3_9697 with dissolve
        mct "(Perhaps {b}afterwards...?{/b})"
        "Or hell, maybe {i}now{/i} would be the best time for her. She could make an informed decision, that was something I wouldn't or couldn't do."
        "Kat wouldn't let her go for one, and if she {b}did{/b} dip, it would be {i}my{/i} failing..."

    scene w3_9679 with dissolve
    mc "No kids to give it to?"
    scene w3_9698 with dissolve
    ver "Three ex-wives with just as many adult kids."
    scene w3_9699 with dissolve
    mc "Damn."
    scene w3_9698 with dissolve
    ver "Red sports car now, too."
    scene w3_9679 with dissolve
    mc "Good to see him?"

    if w3VeroBarDate == True:
        scene w3_9700 with dissolve
        ver "Not especially. He wanted my blessing."
        scene w3_9701 with dissolve
        mc "'bout what?"
        scene w3_9700 with dissolve
        ver "Going to Liliana's wedding."
        scene w3_9701 with dissolve
        mc "Your ex-wife is getting remarried?"
        scene w3_9700 with dissolve
        ver "She moved on pretty damn quickly. Hardly seems fair, when I... {i}haven't.{/i}"
        scene w3_9702 with dissolve
        mc "People move at different speeds, yeah? It doesn't mean she didn't love you."
        scene w3_9700 with dissolve
        ver "I know that, and that's why it fuckin' sucks."
        scene w3_9701 with dissolve
        mc "Sorry for asking."
        scene w3_9703 with dissolve
        ver "It's cool. It's good to admit this shit."
    else:
        scene w3_9700 with dissolve
        ver "I suppose. I felt kinda embarrassed catching up."


    scene w3_9704 with dissolve
    ver "........."
    scene w3_9705 with dissolve
    ver "......"

    if w3VeroBarDate == True:
        scene w3_9706 with dissolve
        ver "...how 'bout you? How are you doing?"
        scene w3_9707 with dissolve
        "I thought about giving her a similarly short answer to match hers, but {i}something{/i} jumped out at me from the mish-mash of the past few days."
        scene w3_9708 with dissolve
        mc "Feelin' kinda weird about my mom {i}thinking{/i} about selling my childhood home."
        scene w3_9709 with dissolve
        "{i}Home.{/i} She seemed like someone who might sympathize."
        scene w3_9710 with dissolve
        ver "You get gutted from that kinda stuff?"
        scene w3_9711 with dissolve
        mc "One, I wouldn't go so far as to say \"gutted.\" And two... {i}why wouldn't I?{/i}"
        scene w3_9710 with dissolve
        ver "I don't know... no offense, just don't seem the type?"
        scene w3_9712 with dissolve
        "......"
        scene w3_9713 with dissolve
        mc "...it's the place I grew up, Veronica."
        scene w3_9714 with dissolve
        ver "........."
        ver "......"
        scene w3_9715 with dissolve
        ver "...want to tell me about it?"
        scene w3_9716 with dissolve
        mc "The house?"
        scene w3_9717 with dissolve
        ver "{b}No,{/b} not the house. The growing up part."
        scene w3_9718 with dissolve
        mc "......"
        scene w3_9719 with dissolve

        if minaGym == True:
            mc "...didn't you say Mina was going to be here in 20 minutes?"
        else:
            mc "How long you got?"

        scene w3_9720 with dissolve
        ver "How long do you plan on gushing?!"
        scene w3_9721 with dissolve
        mc "I dunno. I've got a lot of juices."
        scene w3_9722 with dissolve
        ver "Pssh! Phrasing, you fuck!"
        stop music fadeout 3.0
        scene black with fade
        "{i}So, I talked about my growing.{/i}"
        jump w3FeliciaInvite
    else:

        scene w3_9710 with dissolve
        ver "...so, yeah. I'll be there tonight. I don't have anything going on."
        scene w3_9723 with dissolve
        mc "Great!"
        scene w3_9724 with dissolve
        ver "Fuck you, it isn't! Stop half-assing your workout!"
        mc "Ah... right, r-right..."
        "She was about to take some stuff out on me, huh?"
        stop music fadeout 3.0
        scene black with fade
        "Maybe I should've called. {i}Full-assing it wasn't fun.{/i}"
        jump w3FeliciaInvite


label w3FeliciaInvite:
    play sound "sound effects/ringing-outbound.mp3"
    "With Rosalind and Veronica in the bag, all that was left was Felicia."
    stop sound
    scene w3_9725 with circlewipe
    fel "...that's pretty last minute, stud."
    scene w3_9726 with dissolve
    mc "You can't make it?"
    scene w3_9727 with dissolve
    fel "I know I don't give the impression that I {i}do{/i} anything, but I am the wife of a mayoral candidate, y'know."
    scene w3_9728 with dissolve
    mc "...wait, Elias is running for {b}mayor?!{/b}"
    play music "music/impertinence.ogg"
    scene w3_9729 with dissolve
    fel "*Sigh* He is indeed. {b}Next year.{/b}"
    fel "He told me his plans yesterday."
    scene w3_9730 with dissolve
    mc "And that came as a surprise to you?"
    scene w3_9731 with dissolve
    fel "I thought I knew him well, but he's never even hinted at a desire to hold public office."
    fel "Part of me thinks he's only doing it out of spite over the city council snubbing him, but who the hell knows."
    scene w3_9730 with dissolve
    mc "{b}Holy shit...{/b} and you're still doing what you're doing? If you sit on your hands, you might end up in the governor's mansion one day!"
    scene w3_9732 with dissolve
    fel "......"
    mc "...that thought doesn't change things?"
    scene w3_9733 with dissolve
    fel "{i}He won't win.{/i}"
    scene w3_9734 with dissolve
    mc "And you're sure of that?"
    scene w3_9733 with dissolve
    "Felicia's silence was thick and telling, riddled with uncharacteristic apprehension and uncertainty."
    fel "This ball is already rolling, and even if I could stop it, I'm not sure I want to."
    scene w3_9735 with dissolve
    fel "*Sigh* {i}Mayor's wife...{/i} what does that get me?"
    scene w3_9736 with dissolve
    "{i}More silence.{/i}"
    mc "Sounds like you could use a night out."
    scene w3_9738 with dissolve
    fel "I can't. {i}Wife hat tonight.{/i}"
    fel "Elias is going out of town tomorrow, and wants to stay in. That means I stay in with him."
    scene w3_9739 with dissolve
    mc "Ah, shit, but it kinda defeats the purpose if the three of you aren't there..."
    scene w3_9737 with dissolve
    fel "There's no point in the first place, you know."
    scene w3_9736 with dissolve
    mc "{b}There is!{/b} It's..."
    "Maybe she was right? What was the point in getting them to play nice?"
    scene w3_9739 with dissolve
    "Did I really think these excursions helped with morale?"
    "........."
    "......"
    scene w3_9736 with dissolve
    mc "...so, no go then?"
    scene w3_9735 with dissolve
    fel "Jesus! Don't sound so defeated! I can..."
    scene w3_9740 with dissolve
    fel "After he falls asleep, maybe I can catch you on the tail end. No promises, but..."
    scene w3_9736 with dissolve
    mc "...don't sound so defeated? Thanks, Felicia. You're the best. See you later."
    scene w3_9741 with dissolve
    fel "I said no promises!"
    stop music
    play sound "sound effects/phonemenu.wav"
    scene w3_9742 with dissolve
    "........."
    "......"
    scene w3_9743 with dissolve
    "..Elias Ford running for mayor?"

    if kat_polite == True:
        "As if I didn't already have trepidation over my part in Mrs. Pulman's duplicitous interview scheme."
    else:
        "As if I didn't already have trepidation over my part in Kathleen's duplicitous interview scheme."

    stop music fadeout 3.0
    scene black with fade
    "...wait?! He didn't get the idea to run for mayor from me, did he?!"

    if minaGym == True and minaFlag == True:
        "On my way out--"
        jump w3VeroMinaGymOutro
    elif w3VeroBarDate == True:
        "On my way out--"
        jump w3VeroGymOutro
    else:
        "{i}With nothing else to do, I went home.{/i}"
        "......"
        "..."
        jump w3VickyGraceMingle


label w3VeroMinaGymOutro:

    play music "music/happy-clappy.ogg"
    scene w3_9744 with cmet
    mina "{b}Heeeeeeeeeeeeey!{/b}"
    "{i}I was assaulted.{/i}"
    scene w3_9745 with dissolve
    mina "If you were going to work out today, you should've told me! We could've worked out together."

    if minaBreakOff == True:
        scene w3_9746 with dissolve
        "Despite our premature ending earlier this week, Mina still hugged me like she was seeing a best friend in a long while."
        mct "(...damn it, what a girl.)"

    scene w3_9747 with dissolve
    mc "You could've told {i}me.{/i}"
    scene w3_9748 with dissolve
    mina "Faaaaaaaaaair! Hehe!"

    if w3MinaHotelFucked == True:
        scene w3_9749 with dissolve
        mina "Mmmh, you smell goood..."
        scene w3_9750 with dissolve
        mc "We're in public, you know..."
        scene w3_9751 with dissolve
        mina "Oh, yeeeeeah.... my bad."
        scene w3_9752 with dissolve
        "{i}She didn't stop.{/i}"
        scene w3_9753 with dissolve
        mc "It seems I'll see you at Hana's show tonight?"
        scene w3_9754 with dissolve
        mina "Yep! It's safe to say we're friends now!"
        scene w3_9753 with dissolve
        mc "Like you weren't the moment you met at my birthday party..."
        scene w3_9755 with dissolve
        mina "{i}Friends of friends{/i}, but this will be the second time we hung out outside of when we met."
        scene w3_9756 with dissolve
        mc "What? Uncomfortable with the word as a matter of policy?"
        scene w3_9757 with dissolve
        mina "Maaaaybe, but if you hang out two times outside of anything mandatory, then you can call yourself friends. {i}And like mean it.{/i}"
        scene w3_9756 with dissolve
        mc "I didn't realize it was so complicated."

    elif minaBreakOff == True:
        scene w3_9753 with dissolve
        mc "Hana told me you would be at her show tonight."
        scene w3_9757 with dissolve
        mina "Yep! I guess I'll see you there?"
        scene w3_9759 with dissolve
        "And despite me picking Hana over the whatever nascent {i}whatever-it-was{/i} relationship with Mina, she sounded {i}hopeful{/i} about that."
        scene w3_9756 with dissolve
        mc "You'll see me there."
        scene w3_9758 with dissolve
        mina "Awesome! Awesome! Hehe!"
    else:

        scene w3_9753 with dissolve
        mc "I guess I'll see you at Hana's show tonight?"
        scene w3_9754 with dissolve
        mina "Yep! We're friends now!"
        scene w3_9753 with dissolve
        mc "Pssh, come on... you two were friends the moment you met."
        scene w3_9755 with dissolve
        mina "{i}Friends of friends{/i}, but this will be the second time we hung out outside of when we met."
        scene w3_9756 with dissolve
        mc "What? Uncomfortable with the word as a matter of policy?"
        scene w3_9757 with dissolve
        mina "Maaaaybe, but if you hang out two times outside of anything mandatory, then you can call yourself friends. {i}And like mean it.{/i}"
        scene w3_9756 with dissolve
        mc "I didn't realize it was so complicated."

    scene w3_9759 with dissolve
    "........."
    play music "music/training-in-fire.ogg"
    scene w3_9760 with dissolve
    "......"
    scene w3_9761 with dissolve
    ver "...there you are."
    scene w3_9762 with dissolve
    mina "Sorry for being late, coach!"
    scene w3_9763 with dissolve
    ver "She won't stop calling me that..."
    scene w3_9764 with dissolve
    mina "Hehe! I'm paying you! I'll call you what I want to call you!"
    scene w3_9765 with dissolve
    ver "You can't win against this girl."

    if Mina_BiCurious >= 3 and w3MinaHotelFucked == True:
        scene w3_9766 with dissolve
        "The two momentarily held each other's glance, bringing to mind Mina's burgeoning girl-on-girl proclivity."
        scene w3_9780 with pixellate
        mina "I want to try having sex with a woman."

        if w3FeliciaMinaThreesomeEnd == True:
            "She just got a taste of it the night before, I wonder if she's still eager to explore that..."
        else:
            "I wonder if she's still eager to explore that..."

        scene w3_9766 with pixellate
        "If I wanted, I could use tonight to nudge that along..."
    else:


        pass

    scene w3_9767 with dissolve
    ver "You ready to sweat?!"
    mina "Yes coach!"
    scene w3_9768 with dissolve
    ver "You know, I'm going to work you to the bone if you keep that up."
    scene w3_9769 with dissolve
    mina "O-oh... if you really don't like i--"
    scene w3_9770 with dissolve
    ver "No, no... keep calling me that, {i}sweetums.{/i}"
    scene w3_9771 with dissolve
    mina "Sweet- uh, wha--"

    if w3VeroBarDate == True:
        scene w3_9772 with dissolve
        ver "Oh, [mcf]?"
        scene w3_9773 with dissolve
        mc "Yeah...?"
        scene w3_9772 with dissolve
        ver "I've been thinking. {i}About your mom selling the house.{/i}"
        scene w3_9773 with dissolve
        mc "Really? I was just--"
        scene w3_9774 with dissolve
        ver "She wants to turn a chapter in her life."
        scene w3_9772 with dissolve
        ver "That's a good thing, and it's not something {i}some{/i} of us can do with grace."
        scene w3_9773 with dissolve
        mc "Yeah... I know you're right. I told her I was cool with it. Maybe not convincingly, but--"
        scene w3_9774 with dissolve
        ver "I know... accepting change can be hard."
        scene w3_9775 with dissolve
        mina "When did you two get so close?!"
        scene w3_9776 with dissolve
        mc "Well... she bills herself as a {i}life{/i} coach, remember?"
        scene w3_9777 with dissolve
        mina "I can tell you things?!"
        scene w3_9778 with dissolve
        ver "Uh.. {i}well{/i}..."
        scene w3_9779 with dissolve
        mc "Ha! See you two later!"

    stop music fadeout 3.0
    scene black with fade
    "{i}With nothing else to do, I went home.{/i}"
    "......"
    "..."
    jump w3VickyGraceMingle

label w3VeroGymOutro:
    play music "music/blue-mood.ogg"
    scene w3_9813 with wipeleft
    ver "Good work out today. You should come more often."
    scene w3_9781 with dissolve
    mc "...more often over the next week, you mean. You don't want to see my face after that, right?"

    if w3VeronicaSex == True:
        scene w3_9782 with dissolve
        ver "...{i}maybe.{/i}"
        scene w3_9783 with dissolve
        mc "Maybe? You said I'd just be a shitty reminder."
        scene w3_9784 with dissolve
        ver "Maybe you can keep coming after... I, uh..."
        ver "I could use the membership dues, you know?"
        scene w3_9785 with dissolve
        mc "Ha! Yeah... and I should keep in shape, huh?"
        scene w3_9786 with dissolve
        "What were we doing? Flirting like idiots?"
        "Did Veronica realize how we sounded?"
        scene w3_9787 with dissolve
        "........."
        scene w3_9788 with dissolve
        ver "...I gotta go do stuff."
    else:

        scene w3_9789 with dissolve
        ver "I did say that, yeah..."
        ver "Still, a week's a week..."
        scene w3_9790 with dissolve
        mc "Well, I did make a commitment, huh?"
        scene w3_9791 with dissolve
        "........."
        scene w3_9792 with dissolve
        ver "...I gotta go do stuff."

    scene w3_9793 with dissolve
    mc "Sure, and I got to get home."
    "{i}Rosalind was probably waiting on me.{/i}"
    scene w3_9794 with dissolve
    ver "Hey, [mcf]... about your mom selling the house..."
    scene w3_9795 with dissolve
    mc "Yeah...?"
    scene w3_9796 with dissolve
    ver "It sounds like she just wants to turn a chapter in her life. That's a good thing."
    scene w3_9794 with dissolve
    ver "It's not something {i}some{/i} of us can do with grace."
    scene w3_9795 with dissolve
    mc "I told her I was cool with it, but I don't think I was very convincing."
    scene w3_9794 with dissolve
    ver "Accepting change can be hard..."
    scene w3_9795 with dissolve
    mc "Yeeeeeah..."
    scene w3_9797 with dissolve
    ver "Listen, I've got some things to do, but I'm glad I caught you on the way out."
    scene w3_9798 with dissolve
    mc "You are...?"
    scene w3_9797 with dissolve
    ver "Yeah! I, uh... I probably would've forgotten to mention that to you if I didn't catch you here."
    scene w3_9799 with dissolve
    ver "...why are you looking at me like that?"
    scene w3_9800 with dissolve
    mc "I dunno. I guess it's nice to have someone think about you."
    scene w3_9801 with dissolve
    ver "I'm not, ah... {b}shut up.{/b}"
    scene w3_9802 with dissolve
    ver "Ha... it's not a big deal, like.... {i}we just talked about it.{/i}"
    scene w3_9803 with dissolve
    "She. Looked. Flustered."
    mct "(She's so cute...)"

    if w3VeronicaSex == True:
        "What if I..."
        hide screen textbox2 with dissolve
        menu:
            "Teased her further?"(chg=["veronica_up"]):
                $ Veronica_Affection += 1
                "Something about Veronica's expression made me daring."
                scene w3_9804 with dissolve
                show screen textbox2 with dissolve
                mc "One more thing before I go..."
                ver "W-wha--"
                play music "music/timeless.ogg"
                scene w3_9805 with dissolve
                "*Cwhup!*"
                ver "...?!"
                scene w3_9806 with dissolve
                mc "{b}You're cute.{/b}"
                scene w3_9807 with dissolve
                "........."
                "......"
                scene w3_9808 with dissolve
                ver "Get the fuck out of here..."
                scene w3_9809 with dissolve
                mc "See you tonight, beautiful."
                ver "I said--"
                stop music fadeout 3.0
                scene black with fade
                "With nothing else to do, besides being full of myself, I went home."
                "........."
                "......"
                "..."
            "Welp, time to leave!":

                show screen textbox2 with dissolve
                "I decided to keep my inclination to myself. {i}For the most part.{/i}"
                scene w3_9810 with dissolve
                mc "See you tonight, beautiful."
                ver "Y-you!"
                scene w3_9811 with dissolve
                ver "Yeah, see you..."
                stop music fadeout 3.0
                scene black with fade
                "{i}With nothing else to do, I went home.{/i}"
                "........."
                "......"
                "..."
    else:

        scene w3_9812 with dissolve
        mc "See you tonight."
        ver "Yeah, you too!"
        stop music fadeout 3.0
        scene black with fade
        "{i}With nothing else to do, I went home.{/i}"
        "........."
        "......"
        "..."
        jump w3VickyGraceMingle


label w3VickyGraceMingle:
    play music "music/no1-a-minor-waltz.ogg"
    scene w3_9814 with blinds
    grace "{i}Vicky!{/i} How do you do, dear?"
    scene w3_9815 with dissolve
    vic "It's good to see you, Grace, but..."
    vic "Correct me if I'm wrong, but I don't think you've ever called me that."
    scene w3_9816 with dissolve
    grace "Oh! Is it too familiar?"
    vic "No! Vicky's perfect! I'm just glad to have graduated from {i}[mcf]'s mom!{/i}"
    scene w3_9817 with dissolve
    grace "That's hard to believe! We've had Thanksgiving together!"
    scene w3_9818 with dissolve
    vic "Well, you probably used {b}Victoria{/b} once or {i}twice...{/i}."
    scene w3_9819 with dissolve
    grace "You look good!"
    scene w3_9820 with dissolve
    vic "Not as good as you. You hardly look like you aged - {i}as elegant as ever!{/i}"
    vic "Did you know my son had quite the crush on you?"
    scene w3_9821 with dissolve
    grace "He was a boy going through puberty. I'd have to be deaf, dumb, AND blind not to notice."
    scene w3_9822 with dissolve
    vic "You could've used that to your advantage, you know."
    grace "Advantage for what?"
    scene w3_9823 with dissolve
    vic "{i}Why{/i} you called me here. It's about Ian, right?"
    grace "...he told you I asked for his help?"
    scene w3_9824 with dissolve
    vic "In so many words."
    scene w3_9825 with dissolve
    grace "Then I guess he decided {i}not{/i} to help..."
    scene w3_9824 with dissolve
    vic "Actually, I think [mcf] has been considering it, but you can't force a 21-year-old man to go to school, Grace."
    vic "Not [mcf], and not me..."
    scene w3_9825 with dissolve
    grace "I don't want either of you to force him to do anything... no, just {i}guide{/i} him to the right conclusion."
    scene w3_9824 with dissolve
    vic "Ian's young, and he has all the advantages in the world; he'll be okay, Grace. Bribing his best friend to get him onboard doing what you want risks backfiring {b}spectacularly.{/b}"
    scene w3_9826 with dissolve
    grace "What... what do you suggest I do?"
    scene w3_9827 with dissolve
    vic "You're actually asking me...?"
    scene w3_9826 with dissolve
    grace "You were so good at this sort of stuff."
    scene w3_9828 with dissolve
    "........."
    "......"
    scene w3_9829 with dissolve
    vic "...you really look torn."
    scene w3_9830 with dissolve
    grace "I just want us to find some common ground."
    scene w3_9831 with dissolve
    vic "Let me ask you this first... {i}why{/i} do you want him to work with his father so badly? Because of Francis?"
    scene w3_9832 with dissolve
    grace "Francis is pushing for it yes, but I don't really care about that if I'm being honest. I just want him to find some footing and direction. Like {i}your{/i} son has."
    scene w3_9833 with dissolve
    vic "Oh, [mcf] has it less figured out than it looks."
    scene w3_9832 with dissolve
    grace "When I saw him the other week, I knew instantly. You did a wonderful job with him, Vicky."
    grace "You did a make-shift job with my son as well. We both know--"
    scene w3_9834 with dissolve
    alice "Sorry to interrupt, but do you need anything before I go out, Mrs. Beaufort?"
    scene w3_9835 with dissolve
    grace "We're fine Alice, we've got everything we need."
    scene w3_9836 with dissolve
    vic "Oh! Alice! Hey! Wow!"
    vic "Do you remember--"
    scene w3_9837 with dissolve
    alice "Of course I remember you, Mrs. [mcl]. We arranged quite a few playdates."
    scene w3_9838 with dissolve
    vic "It's still just miss, I'm afraid."
    scene w3_9839 with dissolve
    alice "Ah..."


    if w3AliceOffer == True:
        scene w3_9840 with dissolve
        "........."
        "......"
        scene w3_9841 with dissolve
        alice "...and how is [mcf] do--"
        scene w3_9842 with dissolve
        grace "He's good, Alice. Will you please leave us?"
        scene w3_9843 with dissolve
        alice "Right away Mrs. Beaufort."
    else:
        scene w3_9844 with dissolve
        alice "How is [mcf] do--"
        scene w3_9845 with dissolve
        grace "He's good, Alice. Will you please leave us?"
        scene w3_9846 with dissolve
        alice "Right away Mrs. Beaufort."

    scene w3_9847 with dissolve
    vic "It was nice seeing you!"
    scene w3_9848 with dissolve
    vic "Wow! I can't believe she's still with you. You must be a great employer."
    grace "*Ahem* Where were we?"
    scene w3_9849 with dissolve
    vic "You were in the middle of flattering me to get what you want."
    scene w3_9850 with dissolve
    grace "Now you sound like Ian! I was being sincere! I'm very grateful for the part you've played in my son's life."
    scene w3_9851 with dissolve
    vic "I told [mcf] the same thing yesterday. I'm grateful for how often you opened your home to him."
    scene w3_9852 with dissolve
    "........."
    "......"
    scene w3_9851 with dissolve
    vic "...so, common ground? It's not like I'm a parenting counselor..."
    scene w3_9853 with dissolve
    grace "I'm open to any suggestions."
    scene w3_9855 with dissolve
    vic "Well... in my opinion... you... {i}need to start small.{/i}"
    scene w3_9856 with dissolve
    grace "...?"
    scene w3_9855 with dissolve
    vic "Don't talk down to him, don't order him around, just... just ask him out for lunch once a week."
    scene w3_9854 with dissolve
    vic "Forget about college for awhile, and just focus on... {b}liking{/b} each other."
    scene w3_9856 with dissolve
    grace "*Sigh* Besides women, I don't even know what he likes..."
    scene w3_9857 with dissolve
    vic "Well... he likes horror movies, {i}history{/i}, and there's always his photography. I remember he took some wonderful landscapes in high school. Have you seen them?"
    scene w3_9858 with dissolve
    grace "...I don't remember."
    scene w3_9859 with dissolve
    vic "Really, they were something! In fact, there's nothing wrong with what he does now, is there?"
    vic "Photography is a career! I know he just does it part-time, but maybe you could steer him into pursuing it more earnestly?"
    scene w3_9860 with dissolve
    "......"
    scene w3_9861 with dissolve
    grace "...{b}no{/b}, that's nonsense. It {i}would{/i} be best if he worked with his father."
    scene w3_9862 with dissolve
    vic "...and why is that?"
    scene w3_9863 with dissolve
    grace "{i}Photographer?{/i} With {b}his{/b} lifestyle?"
    scene w3_9862 with dissolve
    vic "I thought you just wanted him to have some direction..."
    scene w3_9864 with dissolve
    grace "By doing something {b}respectable!{/b}"
    scene w3_9865 with dissolve
    grace "*Scoff* He wouldn't be able to support himself without my brother! If it wasn't for him, I'd be able to pull the purse strings shut and he'd get a taste of reality!"
    scene w3_9866 with dissolve
    vic "Your brother..."
    scene w3_9867 with dissolve
    grace "Chuckie, God bless him, you know how he is..."
    scene w3_9868 with dissolve
    vic "I've met him a few times, at school and at--"
    stop music
    scene w3_9869 with dissolve
    grace "He told me."
    scene w3_9870 with dissolve
    vic "He... h-he what?"
    play music "music/doll-dancing.ogg"
    scene w3_9871 with dissolve
    grace "He told me. He tells me {i}everything.{/i}"
    scene w3_9870 with dissolve
    vic "{b}Everything{/b} everything...?"
    scene w3_9872 with dissolve
    grace "I know he can be a bit much, but I assure you he's quite the loving uncle. {i}Too much so.{/i} I hear he's even taken [mcf] under his wing."
    scene w3_9873 with dissolve
    vic "{i}What{/i} do you know?! And how long have you--"
    scene w3_9874 with dissolve
    grace "{b}I know{/b}, and I've known for years."
    scene w3_9873 with dissolve
    vic "And you still invited me to all those--?! To sit across from--"
    scene w3_9874 with dissolve
    grace "Ian would've missed you."
    scene w3_9875 with dissolve
    vic "You... I'm... {b}I'm...!{/b}"
    scene w3_9876 with dissolve
    grace "Relax, I don't give a fuck about any of that. Not about your past, nor the \"messages\" Charles likes to send people who insult him."
    grace "Whatever understanding you have that let you two make awkward Thanksgiving chit-chat over the years is between you two."
    scene w3_9877 with dissolve
    vic "I'm going to go."
    scene w3_9878 with dissolve
    grace "We're not finished."
    vic "I'm leaving!"
    scene w3_9879 with dissolve
    grace "I said we're not finished, {b}whore!{/b}"
    scene w3_9880 with dissolve
    "........."
    "......"
    scene w3_9881 with dissolve
    vic "...give me one good reason I shouldn't slap the {b}SHIT{/b} out of your prissy bitch mouth!"
    scene w3_9882 with dissolve
    grace "Actually, given what I know, I can give you a compelling reason for you to help me with my son."
    scene w3_9883 with dissolve
    vic "You..."
    scene w3_9884 with dissolve
    grace "Sit down. Let's keep this amicable."
    scene w3_9885 with dissolve
    vic "You wouldn't--"
    scene w3_9884 with dissolve
    grace "Sit. {b}Down.{/b}"
    scene black with fade
    "......"
    "..."
    jump w3EmptyLonelyApartmentJump

label w3EmptyLonelyApartmentJump:
    scene w3_9886 with blinds
    "When I got home, Rosalind was gone."
    "She hadn't simply run out, but rather took her stuff - and she didn't forget anything, either."
    "Save for the spare key I lent her that she used to lock up, but I'd be getting that back from her rather than her coming back here."
    mct "(I would've helped her with her stuff...)"
    scene w3_9887 with dissolve
    "........."
    "......"
    "...the place felt as eerily empty as I expected."
    scene w3_9888 with dissolve
    "My mind went back to yesterday. Our dinner, of course, but also..."
    "Donovan."
    "On my computer, just mere feet away, I no doubt had some of his productions."
    scene w3_9889 with dissolve
    "A thought worked itself into my brain. {i}Delete that shit.{/i}"
    "........."
    "......"
    scene w3_9890 with dissolve
    mc "...oh, yeah."
    "Hana wanted me to invite Ian."
    scene w3_9891 with dissolve
    "I wasn't so sure that was a bright idea with Mina there, but I also wasn't so sure it was a bright idea to bring Mina around the Carnations."
    "...but, strangely, I kinda didn't care. For whatever reason, for today in particular, keeping my life untangled felt needlessly exhausting."
    stop music fadeout 3.0
    scene black with fade
    "Ian, sounding excited, naturally accepted. {i}Not a worry in the world.{/i}"

    if w2ExEndingKathleen == True:
        jump w3KatEnlightenmentStart
    else:
        "......"
        "..."
        jump w3RockClubStart

label w3KatEnlightenmentStart:
    play sound "sound effects/door-bell.wav"
    "--and there was the old woman, right on time, duffle bags in tow."
    scene w3_9892 with fade
    "Just her, by her lonesome."
    scene w3_9893 with dissolve
    kat "Hello, [mcf]. Thanks for having me."
    scene w3_9894 with dissolve
    mc "...should I have prepared snacks?"
    scene w3_9893 with dissolve
    kat "It is an unusual visit, isn't it? {b}For both of us.{/b}"
    scene w3_9895 with dissolve
    kat "Are we alone?"
    mc "We {b}ARE{/b}, yeeeeeeah..."
    play sound "sound effects/door-close.wav"
    play music "music/house-on-the-hill.ogg"
    scene w3_9896 with dissolve
    kat "You sound {b}uncertain{/b} about this."
    "After last week's exhibition, it was me who sought her out, looking for insight so I might better navigate my desires. What she offered me was a vague promise that I would be able to act with \"impunity\". Naturally..."
    scene w3_9897 with dissolve
    mc "Can you blame me? When I'm not sure what I've even agreed to here?"
    kat "I like that about you. So... {b}pensive.{/b} The kind of man who'll doubt the good fortune that comes knocking at his door."
    scene w3_9898 with dissolve
    mc "Bad luck often comes disguised as good luck. Ask the Trojans."
    scene w3_9899 with dissolve
    kat "Do I look like a wooden horse to you?"
    scene w3_9900 with dissolve

    if kat_polite == True:
        "Mrs. Pulman, with the experience and wiles of a woman her age, drew my attention to her soft curves."
    else:
        "Kathleen, with the experience and wiles of a woman her age, drew my attention to her soft curves."

    scene w3_9901 with dissolve
    kat "I see you laid out the things I sent you."
    kat "{b}Eager{/b} boy."
    "It wasn't so much her words as it was her tone that brought to mind the unspooling of a spider's webbing."
    scene w3_9902 with dissolve
    mc "Quite the {i}mixed{/i} bag... I'm a bit worried about where that toothbrush has been."
    scene w3_9899 with dissolve
    kat "Have you given any thought to how all those innocuous little items might be {i}utilized{/i} for... {b}fun?{/b}"
    scene w3_9903 with dissolve
    mc "Somewhat, but I'm not even sure what the \"game\" is... honestly, I expected you to turn up with a house girl, now I'm not even--"
    scene w3_9904 with dissolve
    kat "No. No {i}whores.{/i}"

    if w2HarpRainCheck == True:
        kat "Last time I offered, you weren't keen on that. So, this evening, I want you to experience {i}total{/i} freedom with {b}nothing{/b} to weigh down your conscience."
    else:
        kat "Harper came with complications. {i}She's paid.{/i} This evening, I want you to experience {i}total{/i} freedom with {b}nothing{/b} to weigh down your conscience."

    scene w3_9905 with dissolve
    mc "Wait, if it's just us, then that means--"
    scene w3_9906 with dissolve
    kat "Then you understand."
    scene w3_9907 with dissolve
    "Her clarification only amplified my feeling of being ensnared in a trap. After all, there was only one woman who could offer me that and have me fully believe she was doing it out of her own free will."
    scene w3_9908 with dissolve
    mc "...why?"
    scene w3_9909 with dissolve
    kat "A better question is {i}why not?{/i}"
    scene w3_9910 with dissolve
    kat "Any mean, ugly thing you desire to do? I will play your canvas."
    kat "My only stipulation is that all you do, you do {b}earnestly.{/b} Don't second guess {i}anything{/i}, hun."
    scene w3_9909 with dissolve
    kat "I want nothing more than for you to feel an unquestioning acceptance of your {b}beautiful{/b} soul."
    scene w3_9911 with dissolve
    kat "If you'll have an old woman like me."
    scene w3_9912 with dissolve
    "........."
    "......"
    scene w3_9913 with dissolve
    mc "...don't you think writing me a blank check is... I mean... you might be surprised by what I--"
    scene w3_9914 with dissolve
    kat "I can imagine much worse than you, [mcf]."
    scene w3_9912 with dissolve
    "The pertinent question \"why\", which had been ringing in my head like a fire alarm, was drowned out with another as she had said..."
    "{i}Why not.{/i} My wariness over what she stood to get out of this, {i}why she would do this at all{/i}, was dwarfed by a world of possibility."
    scene w3_9915 with dissolve
    "{i}Anything{/i}, she said."
    kat "Can you do that for me? Can you show me [mcf] [mcl]?"
    "Could I really use those to make her old ass {b}regret{/b} goading me into this? {b}I wanted to.{/b}"
    hide screen textbox2 with dissolve
    scene w3_9919 with dissolve
    kat "Will you show me something {b}wonderful?{/b}"
    scene w3_9916 with dissolve
    "I knew this: if I don't put a stop to this now, I {b}would not{/b} be holding back."

    menu:
        "Give the old woman your all. *w3KatSnare = True)"(chg=["kathleen_up5"]):
            $ Kathleen_Affection += 5
            $ w3KatSnare = True
            mc "You're putting a lot of trust in me. I hope you get what you want from this..."
            scene w3_9917 with dissolve
            kat "Oh, hun. You'll do {b}amazing.{/b}"
            scene w3_9916 with dissolve
            mc "How do we get started?"
            scene w3_9918 with dissolve
            kat "One bag is for me, the other is for you..."
            scene w3_9916 with dissolve
            mc "What's in them?"
            scene w3_9919 with dissolve
            kat "Oh, this and that. I'm certain I got your size right..."
            kat "May I use your bathroom?"
            scene w3_9916 with dissolve
            mc "There's one upstairs and one down--"
            scene black with fade
            "My excitement was so thick that I could choke, but what was in the bag surprised me."
            "......"
            "..."
            jump w3KatEnlightenmentContinue
        "This is too much for you. {m_note} this will set all her stats to 0":

            $ Kathleen_Affection = 0
            $ Kathleen_Trust = 0
            $ w3KathleenTestAbort = True
            "If I accepted, would I love the feeling? Would I hate it?"
            mc "...I'm not sure I'm comfortable with this."
            scene w3_9920 with dissolve
            "{i}I didn't want to know.{/i}"
            scene w3_9921 with dissolve
            kat "...no? Are you certain?"
            scene w3_9922 with dissolve
            kat "After I've prepared and put myself out here like this? Are you going to embarrass me, [mcf]?"
            scene w3_9923 with dissolve
            mc "...{b}yes{/b}, I'm certain. I don't think I want to do this."
            scene w3_9924 with dissolve
            "........."
            "......"
            scene w3_9926 with dissolve
            kat "...*sigh* your choice, [mcf]. That tells me {b}everything{/b} I need to know about you."
            scene w3_9925 with dissolve
            mc "Uuuhh. can I... get you something to drink?"
            scene w3_9926 with dissolve
            kat "It's better if I leave."
            scene w3_9925 with dissolve
            mc "Should I walk you--"
            scene black with fade
            "I did not walk her out."
            scene w3_9927 with fade
            "Honestly, part of me felt bad rebuffing her like this. Like she said, she was putting herself out there - even if it was to stoke some sadistic desire for control."
            mct "(Oh, well...)"
            scene black with fade
            "Now to while away the time until Hana's concert."
            "......"
            "..."
            jump w3RockClubStart

label w3KatEnlightenmentContinue:
    if _in_replay:
        play music "music/house-on-the-hill.ogg"
    scene w3_9940 with circlewipe
    "There were, of course, some expected items."
    "Sex toys of various implements, an array of diverse bindings, and other tools of discipline."
    "Items that, besides my disbelief that the boss lady would even allow me to use them on her, {i}matched the scenario.{/i}"
    scene w3_9928 with dissolve
    "Undoubtedly a product of the old woman's penchant for the theatrical, the surprise came from the uniform; a crisp inklike costume that stirred something peculiar in me."
    "An outfit that I knew, if donned, would make me look {b}fucking silly{/b} and there was NO WAY I was wearing it."
    scene w3_9929 with dissolve
    "........."
    "......"
    play ambient "sound effects/high-heel-footsteps.wav"
    "...yet, {i}she was right{i}, it fit {b}perfectly.{/b}"
    scene w3_9930 with dissolve
    kat "You look good."
    scene w3_9931 with dissolve
    mc "Really? 'Cause I feel like I'm wearing a Halloween--"
    stop ambient
    scene w3_9932 with wipeleft
    "{i}Woah.{/i}"
    "No one expects {i}slutty grandma{/i} when they turn around."
    scene w3_9933 with dissolve

    if kat_polite:
        "Mrs. Pulman strode toward me on the heels of a pair of luscious hooker boots, hips poised with killing intent."
    else:
        "Kathleen strode toward me on the heels of a pair of luscious hooker boots, hips poised with killing intent."

    scene w3_9934 with dissolve
    "Black beacons of pleasure, carrying pale white thighs, all capped with a garish pair of purple hot pants."
    scene w3_9935 with dissolve
    kat "I know it seems quaint, but uniforms have a powerful effect on one's psychology. They, for example, can help one feel more {b}authoritative.{/b}"
    scene w3_9936 with dissolve
    "Completing the ensemble was a cheap net and strap that, if put on a street corner at night, would unequivocally tell the world she was for sale."
    scene w3_9937 with dissolve
    kat "Plus, it is fun to play dress up."
    scene w3_9938 with dissolve
    mc "Okay, I kinda get the cop outfit... {b}clothes make the fascist{/b}, but what about you?"
    scene w3_9937 with dissolve
    kat "Your counterpart. {i}Streetwalking trash.{/i}"
    scene w3_9938 with dissolve
    mc "{b}Huh.{/b} After all your speeches about the virtues of being a whore, I bet you play one pretty convincingly..."
    scene w3_9936 with dissolve
    "The hairs on my neck stood up as I tested the waters, treading the very real possibility that {i}whatever I said or did{/i} this evening might hold negative repercussions for our \"working\" relationship."
    scene w3_9939 with dissolve

    if hanaFlag == True:
        kat "You like my hair? I have it on good authority you have a thing for pigtails..."
    else:
        kat "Men love pigtails, right?"

    scene w3_9941 with dissolve

    menu:
        "She looks so {b}fuckable{/b} right now."(chg=["kathleen_up"]):
            $ Kathleen_Affection +=1
            scene w3_9942 with dissolve
            mc "{b}Yeah.{/b} You look so fuckin' {b}nasty{/b} that I love it."
            scene w3_9943 with dissolve
            "To emphasize my point, I enjoyed myself a great big helping of the old woman's soft ass."
            scene w3_9944 with dissolve
            kat "Mmmm..."
            "Especially at her age, Kathleen was a beautiful woman. To witness her elegance diminished by tacky whorish attire... well, {i}it did something for me.{/i}"
            scene w3_9945 with dissolve
            kat "I suspected as much, but I hope it goes without saying... {b}don't{/b} get used to treating me this way."
            scene w3_9946 with dissolve
            mc "...no?"
            scene w3_9945 with dissolve
            kat "You grab my ass outside this evening, {b}we'll have problems...{/b}"
            scene w3_9946 with dissolve
            mc "{b}Counter point:{/b} it would be pretty fun to fuck with the police commissioner's crush on you..."
            scene w3_9947 with dissolve
            kat "Ha! I {i}would{/i} love to see Jim's face, but in that scenario... {b}I'd{/b} be doing the grab ass. Understood?"
            scene w3_9948 with dissolve
            mc "Yes, Ma'am..."
            mct "(But before I forget myself...)"
        "She looks like a clown.":

            scene w3_9949 with dissolve
            mc "A hag dolled up like a whore?"
            "Consequences be damned, I squashed that concern and felt my words sharpen to a point."
            scene w3_9950 with dissolve
            mc "You look like a fucking joke."
            scene w3_9951 with dissolve
            kat "You don't look like you're laughing..."
            scene w3_9952 with dissolve
            kat "I see you're settling into things..."
            scene w3_9953 with dissolve
            mct "(But before I forget myself...)"

    scene w3_9954 with dissolve
    mc "Are you sure this is a good idea?"
    scene w3_9955 with dissolve
    kat "I wouldn't be here if I--"
    play sound "sound effects/spit2.wav"
    scene w3_9956 with dissolve
    "I wanted certainty."
    scene w3_9957 with dissolve
    "The old woman briefly flinched, face contorting in displeasure, before returning to an..."
    scene w3_9958 with dissolve
    "...infuriatingly bemused expression."
    scene w3_9959 with dissolve
    mc "Has anyone ever done that to you before?"
    scene w3_9955 with dissolve
    kat "Once or twice, but... never from {i}this{/i} position."
    scene w3_9959 with dissolve
    mc "How can you stand it? Don't you want to bite back?"
    scene w3_9960 with dissolve
    kat "Maybe, just maybe... I've already got my teeth in you?"
    scene w3_9961 with dissolve
    mc "Yeah...?"
    scene w3_9962 with dissolve
    play sound "sound effects/slap4.wav"
    scene w3_9963 with hpunch
    "{i}One more time.{/i}"
    scene w3_9964 with dissolve
    "It wasn't a hard slap, but it made my point. {i}Are you sure?{/i}"
    "My stomach dipped as I glimpsed a {i}flicker{/i} of disbelief play across the older woman's face."
    scene w3_9965 with dissolve
    "A brief moment where, before rationality kicked in, she regarded me as something to be squashed."
    scene w3_9966 with dissolve
    "Only for a moment though, and then the woman in front of me puffed up with euphoric glee."
    scene w3_9967 with dissolve
    kat "{b}Good.{/b} Don't pussy out on me, [mcf]."
    scene w3_9968 with dissolve
    "All my distaste for this woman, all my hypocritical judgments of her character, they were bleached by the onset of an overwhelming feeling of freedom."
    scene w3_9969 with dissolve
    mc "...thank you."
    scene w3_9967 with dissolve
    kat "You're very welcome, dear."
    scene w3_9968 with dissolve
    "A confusing moment of tenderness welled up in me. Kathleen Pulman, I thought, possessed an unsettling beauty beyond earthly measure."
    scene w3_9970 with dissolve
    "{i}I wanted to crush that feeling.{/i}"
    scene w3_9971 with dissolve
    "You might expect, given the many tools at my disposal, that one would be paralyzed by choice. {b}But I knew.{/b}"
    scene w3_9972 with dissolve
    "And she likely expected clumsy degradation from my fledgling sadist hands, but something about her eyes made me want to prove that wrong."
    scene black with fade
    "I {b}would{/b} prove her wrong."
    stop music fadeout 3.0
    "........."
    "......"
    kat "...we're starting like this?"
    kat "You sure you don't want me to crawl around a little first?"
    play music "music/from-russia-with-love.ogg"
    scene w3_9973 with circlewipe
    mc "This is too precious of a moment to waste on mundane humiliation."
    scene w3_9974 with dissolve
    mc "Sure, you could bark like a dog, but your heart wouldn't be in it. Coming from you, it'd feel patronizing."
    scene w3_9975 with dissolve
    "Despite the oxytocin saturating my blood, I kept an even expression, trying my best to look calm, to speak clearly and confidently, all to sell my next claim."
    scene w3_9974 with dissolve
    mc "I don't know if you were being funny or were genuinely presenting me a challenge when you gave me a suitcase of random crap, but I have what I need to trick you."
    scene w3_9976 with dissolve
    kat "{i}Trick me?{/i}"
    scene w3_9977 with dissolve
    mc "Even if I {i}wanted{/i} to break you, it's not like I would actually be able to do it. You're a real-life person and, this may surprise you, but it's not something I desire even in my purest of fantasies."
    scene w3_9978 with dissolve
    kat "..."
    mc "However, I can sell you on an idea."
    scene w3_9979 with dissolve
    "It felt poetic to hit the old woman with her rambling sort of bullshit for once."
    mc "For an evening, I will make you {b}think{/b} you're going to break. I will make you believe that you can't or don't want to come back from this experience."
    scene w3_9980 with dissolve
    kat "Ha. I'm looking forward to it..."
    scene w3_9978 with dissolve
    mc "You don't believe me?"
    scene w3_9980 with dissolve
    kat "I would be {b}surprised.{/b}"
    scene w3_9978 with dissolve
    mc "That's fair, but you're putting a lot of trust in me here, and I {b}will{/b} live up to that."
    scene w3_9981 with dissolve
    kat "...what are you doing over there?"
    scene w3_9982 with dissolve
    mc "{i}Wouldn't you like to know.{/i}"
    scene w3_9980 with dissolve
    kat "Fine, don't tell me, I'm sure I'm about to find out..."
    scene w3_9979 with dissolve
    mc "By the way, what's your experience with anal? Does Hubby Judge like fucking you up the ass?"
    scene w3_9983 with dissolve
    kat "...we don't have that kind of relationship. I'm not a virgin back there, but it's not like I--"
    scene w3_9984 with dissolve
    mc "{b}Good!{/b} I'm extremely happy to hear that!"
    scene w3_9986 with dissolve
    kat "Pah! You can do anything you want and you want to fuck me in the ass?"
    scene w3_9985 with dissolve
    mc "You sound apprehensive."
    scene w3_9983 with dissolve
    kat "...what do you have in your hand?"
    scene w3_9987 with dissolve
    mc "Sophia's evil juju! Does she know you gave me this?"
    scene w3_9988 with dissolve
    kat "Not a chance... actually, that bitch would be pretty unhappy about it, which is fun in its own way."
    scene w3_9989 with dissolve
    mc "{size=-10}I wonder if she tested this anally...?{/size}"
    scene w3_9990 with dissolve
    kat "Wait, what are you babbling about?"
    scene w3_9989 with dissolve
    mc "I've been thinking! For whatever reason, her sex perfume doesn't affect you. Now, it's possible that the injection form will work on you, but I've got a different delivery method in mind."
    scene w3_9991 with dissolve
    kat "Oh, yeah...? What...?"
    scene w3_9992 with dissolve
    mc "{size=+10}{b}Rectal absorption!{/b}{/size}"
    scene w3_9993 with dissolve
    kat "{b}You're going to drug my ass?!{/b}"
    scene w3_9994 with dissolve
    mc "Why not? Not only will pouring this down your old lady asshole result in the drug circulating through your system faster than the intramuscular route, {i}with less alteration it might even be more potent.{i}"
    scene w3_9995 with dissolve
    kat "Oh, you gotta be fucking kidding me! You--"
    scene w3_9996 with dissolve
    mc "You forgot I'm a med student, didn't you?"
    scene w3_9997 with dissolve
    "........."
    "......"
    scene w3_9998 with dissolve
    kat "*Sigh* ...this will be interesting."
    scene w3_9999 with dissolve
    mc "The idea came to me when I got some on my skin earlier. I mean, what the FUCK is this stuff that even transdermal contact with this {b}insanity{/b} is enough to give you a localized buzz?"
    mc "It's extremely scary to even imagine what this will be used for..."
    scene w3_10000 with dissolve
    kat "I wouldn't think too much about it."
    scene w3_9999 with dissolve
    mc "That sounds like good, applicable advice."
    scene w3_10001 with dissolve
    "She was right. The more I thought about it, the more I realized that Abel Van Doren and his number two were an entirely different breed from the rest of the club's patrons."
    scene w3_10002 with dissolve
    mc "You've got a cute asshole, Mrs. P."
    scene w3_10003 with dissolve
    kat "...{i}real{/i} charming."
    scene w3_10004 with dissolve
    "Her tone said {i}get on with it{/i}, so..."
    scene w3_10005 with dissolve
    "The old woman shuddered at the mere touch of the syringe's barrel meeting her ring."
    kat "Ahh..."
    scene w3_10006 with dissolve
    "She was closed up tight, but with a little finesse.."
    kat "Don't tease--"
    scene w3_10008 with dissolve
    "It was with little fanfare that I pushed the plunger and squirted the barrel's contents up, up, up into the hag's shithole."
    kat "Euuuh...? C-cold...!"
    "A slow, even dispersal that coated and saturated her rectum with the promise of madness."
    scene w3_10007 with dissolve

    if kat_polite == True:
        mc "Nothing about tonight is going to be {b}charming{/b}, Mrs. Pulman."
    else:
        mc "Nothing about tonight is going to be {b}charming{/b}, Kathleen."

    kat "Mmhmh...!"
    mc "Just remember that you're the one who gave me both the gun and instructions here."
    scene w3_10009 with dissolve
    "Her rectal ring twitched, winking flirtatiously, as the concoction pooling in her rectum seized hold of her senses."
    scene w3_10010 with dissolve
    kat "Ah, hnnaa...?! It b-burns...!"
    scene w3_10011 with dissolve

    if kat_polite == True:
        "As with her perfume, the effect was near immediate. Mrs. Pulman's skin turned flush and her face contorted in a strange way."
    else:
        "As with her perfume, the effect was near immediate. Kathleen's skin turned flush and her face contorted in a strange way."

    scene w3_10012 with dissolve
    kat "O-oh... oh, fuck... this is gonna be bad, isn't it?"
    scene w3_10011 with dissolve
    mc "Regretting your decision?"
    scene w3_10012 with dissolve
    kat "Of course not, I want you to g-go... {i}go wild.{/i}"
    scene w3_10011 with dissolve
    mc "You crazy cunt, what the fuck is wrong with you?"
    scene w3_10014 with dissolve
    kat "H-ha..! {b}Ha!{/b}"
    scene w3_10013 with dissolve
    "And, once I felt the plunger meet the flange..."
    scene w3_10015 with dissolve
    mc "All full, now..."
    kat "Ehhuhh, what are you--"
    scene w3_10016 with dissolve
    kat "{b}Ghh!{/b}"
    "With no care or concern for the old woman's comfort, the black egg-shaped plug penetrated and filled the shaking woman's rectum."
    mc "Can't have you go leaking this precious stuff all over my furniture now, can we?"
    scene w3_10017 with dissolve
    mc "There, {i}beautiful.{/b} Now we just have to wait for your body to absorb it all. How you feeling?"
    scene w3_10018 with dissolve
    kat "Don't ask stupid questions, I'm... it's working! My ass is, ahhh..."
    scene w3_10017 with dissolve
    "She trailed off, more concerned with enduring the amplifying heat than indulging my bullshit."
    mc "...on fire? Like you're in great need of a dick?"
    scene w3_10019 with dissolve
    kat "Ahh, hee... what's next? What are you waiting--"
    scene w3_10020 with dissolve
    kat "W-where are you going?"
    mc "Stop asking questions."
    scene black with fade
    "This was just the start of course."
    stop music fadeout 3.0
    scene w3_10021 with fade
    mc "I want you to focus singularly on what you're feeling right now."
    kat "Ah, ahh- heh.. {i}I get it--{/i}"
    scene w3_10022 with dissolve
    kat "Now w-where are you going...?"
    scene ka_01_a with dissolve
    show ka_01
    mc "Stop asking questions!"
    "For the time being, I let her wallow."
    kat "Ah, haae..."
    play ambient "sound effects/tub.wav"
    kat "...i-is that w-water?"
    "{i}It was.{/i} It would come in handy later, but I didn't confirm it, letting Kathleen hear but not comprehend my machinations."
    "After all, imagination beats reality every time."
    kat "Eah, ahhh...! That damn Sophia...♥ Hurry up and get back here!"
    "My answer to her came in the form of my absence."
    mct "(Ha! Sit there and go crazy!)"
    stop ambient fadeout 3.0
    "In the meantime, I kept myself busy."
    play ambient "sound effects/cabinets.wav"
    kat "Mmhh, ehhh...♥"
    "Making sure Kathleen could hear me rustling about, doing {i}stuff.{/i}"
    kat "W-what are you doing...? T-this isn't fun! You're supposed to have fun...♥"
    play ambient "sound effects/ringing-inbound.wav"
    "Stuff that she likely imagined was in support of her pending torment, but was simply buying time for a phone call."
    kat "Eahh... g-get the fuck back over--"
    play sound "sound effects/phonemenu.wav"
    stop ambient
    scene w3_10023 with dissolve
    mc "Hello?"
    scene w3_10024 with dissolve
    "The test ringtone button had never been used for a more devious purpose."
    scene w3_10023 with dissolve
    mc "Ah, shit? Yeah, no problem! Hold tight!"
    scene w3_10025 with dissolve
    mc "Sorry to do this to you, boss, but... uh... my mom got herself into a spot. Locked out of the house and I've got the spare... so just... {b}thirty minutes!{/b} Tops!"
    scene w3_10026 with dissolve
    kat "H-huhh...? Wh-wha, you're lying!"
    scene w3_10027 with dissolve
    mct "(Perfect! The old bitch was looking cooked!)"
    scene ka_01_a with dissolve
    show ka_01
    "Perspiration coated her head to toe, and despite her best efforts to breathe evenly, her chest heaved with arousal."
    "I knew what that demonic compound coursing through her bloodstream felt like from personal experience."
    "I remembered vividly the way it heightened the senses and dulled all thought..."
    kat "It's a nice try, but--"
    scene w3_10028 with dissolve
    mc "Gotta go! Sit tight!"
    scene w3_10029 with dissolve
    kat "H-hold it right there you! Don't think you're just going to leave--"
    scene w3_10028 with dissolve
    "She, of course, kept babbling as I gave myself enough time to get plausibly changed."
    play sound "sound effects/door-openclose.wav"
    scene w3_10030 with dissolve
    scene w3_10028 with dissolve
    "........."
    "......"
    scene ka_01_a with dissolve
    show ka_01
    kat "Ah, {b}fuck.{/b}"
    "For all she knew, she was alone."
    kat "Ahh, o-oh... you fucker..."
    "From what I knew from my own experience with Sophia's drug, it would be pulsing through her system for hours."
    "I had time."
    "{i}Time to wait.{/i}"
    "Time to just watch."
    play music "music/blacksmith.ogg"
    scene w3_10031 with dissolve:
        align (0.5,0.5)
        linear 160 zoom 2.5
        pause 4
    "Time for the old hag to feel alone and too helpless to do anything about her arousal."
    "{i}Unsure of when I'd be coming back.{/i}"
    "I gave it a few minutes."
    "I gave it five minutes, listening to the older woman's groans."
    kat "Uggh.... walked into this one, Kathy... heha... ha..."
    scene w3_10032 with dissolve
    "{i}Ten.{/i}"
    "Enough time for her to feel sufficiently abandoned. Enough for any suspicion that this was just part of our play to be swallowed by unintelligible lust."
    "Once I was satisfied I had her convinced--"
    scene ka_02_a with dissolve
    show ka_02
    kat "Ah, euh...?"
    "I began."
    kat "Ngh...?! W-what?"
    "The ball fell from my palm and struck the concrete with a satisfying {i}plap.{/i}"
    kat "[mcf]...?!"
    "Again and again, {i}steady.{/i} In timed increments."
    "A dull, hollow, endless noise that reverberated off the high ceiling and made it difficult to place."
    "Bounce."
    "Bounce. Bounce."
    "Bounce. Bounce. Bounce."
    scene ka_03_a with dissolve
    show ka_03
    "There was enough distance between us that I hoped she wouldn't figure it out."
    "{i}What was that sound?{/i}"
    "Was she trying to place it right now?"
    kat "...ehh, ah...?!"
    "Bounce."
    scene ka_04_a with dissolve
    show ka_04
    "{i}What was that sound, Kathleen?{/i}"
    "Bounce. Bounce. Bounce."
    "{i}What was that sound, you old cunt?{/i}"
    "The consistent {i}kaplops{/i} were, I hoped, an impediment to staying sane."
    "She had spent the last dozen minutes since I left at odds, no doubt trying to compose herself in the face of her body going mad."
    "Now, whatever she was hearing was bringing her back to reality, a lone physical stimulus rooting her to desperation."
    kat "I k-know you're here!"
    "Back to the fire in her loins, and the abject {i}nothing she can fucking do about it.{/i}"
    scene ka_03_a with dissolve
    show ka_03
    "Minutes passed."
    kat "Ah, haaa...♥ Get the--"

    if kat_polite == True:
        "With just the sound of the ball bouncing and Mrs. Pulman panting like a bitch."
    else:
        "With just the sound of the ball bouncing and Kathleen panting like a bitch."

    kat "G-get the fuck back here, you asshole!"
    "She repeated the familiar plea, not quite talking to herself."
    kat "Get back here! Get back here!"
    "It was more like a spoiled child trying to {i}will{/i} reality, throwing a tantrum, desperately demanding what she wanted. "
    kat "Get back here! Get back here! Get back here!"
    scene ka_02_a with dissolve
    show ka_02
    "{i}No.{/i}"
    "No, no, no, {b}no.{/b}"
    mct "(Go crazy you stupid bitch!)"
    kat "Ah, haa... ahh, oh, {i}Kathy...{/i}"
    "Was she laughing at herself...?"
    kat "F-fuck... ahh... I'll fucking kill you, [mcf]. Ha, haaa..."
    kat "L-leave me here, you s-son of a whore... ahahaa... hahaa...♥"
    "{i}I would remember that comment.{/i}"
    "............"
    "........."
    "......"
    "...{i}many minutes passed.{/i}"
    scene ka_04_a with dissolve
    show ka_04
    kat "Ah, haaa.. you... ha... where's the fucking fun in this?! I w-wanted to s-seee.. .ahh, ahh...♥"
    "So many minutes that I couldn't believe I had stood here for so long, bouncing a {i}goddamn ball.{/i}"
    kat "Fuck, fuck, fuck, fuck, fuck....!"
    "However, in that time, the old woman's unsatisfied whimpers proved a tonic for my aching feet."
    kat "Euuahh, hahhh...♥ Ahh, egett... p-please..."
    "{i}Her plaintive whining had me hard as steel.{/i}"
    scene w3_10033 with dissolve
    "{i}I'm going to destroy you.{/i}"
    "......"
    play sound "sound effects/door-openclose.wav"
    "..."
    scene w3_10034 with dissolve
    mc "Sorry about that. Where were we?"
    scene w3_10035 with dissolve
    kat "Ahh... haha... {b}s-shut up and do something about this!{/b}"
    scene w3_10034 with dissolve
    mc "You're in no position to make demands, boss."
    scene w3_10035 with dissolve
    kat "I--"
    play sound "sound effects/thud-floor.mp3"
    scene w3_10036 with vpunch
    mc "{b}Shut the fuck up!{/b}"
    kat "Ghh, haaa...?!"
    "The moment I got back, I flipped the switch."
    scene ka_05_a with dissolve
    show ka_05
    mc "I could leave you here another six hours if I wanted to! {b}Should I?!{/b}"
    kat "A-ahh...!"
    mc "{b}Should I, you bitch?! You {b}sopping{/b} hag whore?!{/b}"
    "In a fit of mania, I used the outsole of my boot to drive home the disparity in the current situation."
    kat "Ahh, haahhh... haaa...♥"
    mc "I mean, think about your position here!"
    kat "Ahh, haaa....♥ F-fuck...♥"
    mc "I know that's a big ask when all you have on your mind right now is {b}dick{/b}, but I'm the only one who can give it to you in this situation, isn't that right?!"
    mc "So show some {b}fucking{/b} respect, cunt! {b}We get each other here?!{/b}"
    kat "Y-youuu--! Ah, {b}oooOoooooahhwwaaAAAhh...{/b}♥"
    mc "TELL ME WE FUCKING UNDERSTAND EACH OTHER!"
    kat "We d-do! I d-doooooooooo, {b}s-siiiiiiir!{/b}"
    "Hearing Kathleen Pulman utter that submissive word set my body alight with tingles."
    kat "I---"
    scene w3_10037 with dissolve
    kat "Oh, {b}f-fuuuuuck!{/b}"
    "And holy shit! All that waiting had its effect."
    scene w3_10038 with dissolve
    kat "Ehh...!"
    "Left unattended so long under Sophia's chemical spell, just the stimulation of having her pussy rubbed and crushed under my boot was enough to make the old bitch blow."
    mc "Wow! How's that for a sight!"
    scene w3_10039 with dissolve
    kat "Ahh... ahhh..."
    mc "You just came from having your pussy trampled! Ha!"
    scene w3_10040 with dissolve
    mc "Ha, haa...!"
    scene w3_10041 with dissolve
    mc "Ha, haa, haaahahaa! {b}Hahahaha!{/b}"
    mc "Ah, fuck...! {b}You deranged hag!{/b}"
    scene w3_10042 with dissolve
    "........."
    "......"
    scene w3_10043 with dissolve
    mc "..."
    kat "Ahh... d-do... {b}d-do more...{/b}"
    scene w3_10044 with dissolve
    mc "I know, I know..."
    scene w3_10043 with dissolve
    "Flipping a switch once more, I put a few ounces of kindness back in my voice."
    scene w3_10045 with dissolve
    mc "That wasn't enough to satisfy you, was it? {i}Poor baby...{/i}"
    scene w3_10046 with dissolve
    kat "Do... ahh... do... not enough... can't think--"
    scene w3_10047 with dissolve
    kat "A-ah...?!"
    scene w3_10048 with dissolve
    "As she blinked the bleariness from her eyes, adjusting to the sudden bright light, {b}I was the first thing she saw.{/b}"
    mc "It was mean of me to just leave you here. I'm sorry."
    "A smiling face behind a sympathetic voice."
    scene w3_10049 with dissolve
    kat "Ah, ahhh... no you're not..."
    scene w3_10048 with dissolve
    "Kathleen Pulman wasn't stupid, but her mind was scrambled. She herself advocated this kind of approach in her own \"work\", but recognizing the tactic wouldn't be enough to escape the pull."
    scene w3_10050 with dissolve
    mc "{i}Poor thing,{/i} you're drenched in sweat..."
    kat "A-ahh...!"
    scene w3_10051 with dissolve
    "The moment she felt a human touch, she let out an {b}incredible{/b} moan."
    mc "Your pussy is drooling and you're all tied up..."
    scene w3_10050 with dissolve
    kat "Hnng, haaa..."
    scene w3_10052 with dissolve
    mc "*Chwup*"
    scene w3_10053 with dissolve
    mc "I'll take care of you."
    scene w3_10054 with dissolve
    "--but before that, I wanted that same tingle in my bones from earlier."

    menu:
        "Would {i}princess{/i} like that? [mod_chat]":
            $ w3KatPrincessPlay = True
            scene w3_10053 with dissolve
            mc "Would you like that, {b}princess?{/b}"
            scene w3_10055 with dissolve
            kat "Ah, I-I..."
            scene w3_10054 with dissolve
            "It was the perfect moniker for a rich, privileged cunt like herself -- and thrice as degrading given she had 30 years on me."
            scene w3_10055 with dissolve
            kat "I'm going crazy... I n-need to cum..."
            scene w3_10053 with dissolve
            mc "Ask for it nicely, then. Like your parents should've taught you."
            scene w3_10057 with dissolve
            kat "I, heh, h-ha...!"
            scene w3_10056 with dissolve
            "{i}She chuckled.{/i}"
            scene w3_10057 with dissolve
            kat "P-please... make me cum, daddy."
            scene w3_10056 with dissolve
            "She chuckled, but she said it simply, recognizing the truth I had highlighted in my fit of control. {i}She needed release, and I was the one to give it to her.{/i}"
            scene w3_10053 with dissolve
            mc "Good girl, that's my princess."
            scene w3_10058 with dissolve
            "Yet, despite my doting tone, things were about to get rough."
        "A slut like her only needs to ask.":

            scene w3_10053 with dissolve
            mc "You only need to ask, Mrs. P. Not demand, but {b}ask.{/b}"
            scene w3_10055 with dissolve
            kat "I... I need release. [mcf], w-would you... {i}please{/i} help me out? L-lend a hand...?"
            scene w3_10053 with dissolve
            mc "Keep it to sir or Mr. [mcl], I don't care which..."
            scene w3_10055 with dissolve
            kat "Mr. [mcl]! H-help me out, sir!"
            scene w3_10054 with dissolve
            "She got the picture, and I got that tingle."
            scene w3_10053 with dissolve
            mc "You're a smart cookie, Mrs. P."
            scene w3_10058 with dissolve
            "{i}Things were about to get rough."

    scene w3_10059 with dissolve
    "......"
    scene w3_10060 with dissolve
    kat "...!"
    scene w3_10061 with dissolve
    mc "...by the way, what were you thinking when you brought this thing? ...you a size queen?"
    scene w3_10062 with dissolve
    kat "Ah, haa... ah... well... I can take about 3/4ths on a good night. Thought you might want to try fitting the {b}whole thing.{/b}"
    scene w3_10063 with dissolve
    mc "Three fourth... that's in your pussy, right?"
    scene w3_10064 with dissolve
    kat "W-wait, you're not-! That's not going to fit!"
    scene w3_10063 with dissolve

    if w3KatPrincessPlay == True:
        mc "Don't worry, princess. We're gonna turn you into an anal queen."
    else:

        mc "We'll take it one inch at a time. You're gonna cum from your asshole, Mrs. P -- ALL NIGHT. Doesn't that sound like fun?"

    scene w3_10064 with dissolve
    kat "J-just... d-don't go too crazy... I..."
    "She sounded so deliciously {i}small.{/i}"

    scene black with fade
    if w3KatPrincessPlay == True:
        mc "I think you'll surprise both of us, beautiful."
    else:
        mc "I think you'll surprise both of us, you old hag."

    "..."
    scene w3_10065 with fade
    mc "I think you're ready..."
    "I had spent an additional 10 minutes generously applying lube and first getting her accustomed to a smaller toy, but by now both of us were sick from the anticipation of it all."
    scene w3_10066 with dissolve
    kat "Ah, hey... *Gulp* {size=-10}easy does it...{/size}"
    scene w3_10067 with dissolve
    "The old woman for obvious reasons, and me..."
    scene w3_10068 with dissolve
    mc "Hmmmm, are you telling me what to do again?"
    "From my overwhelming sadistic desire."
    scene w3_10069 with dissolve

    if w3KatPrincessPlay == True:
        kat "Ah... n-no..."
    else:
        kat "Ah... n-no, sir."

    scene w3_10068 with dissolve
    mc "You sure? Because if you need help with that, I could shove this {b}mother fucker{/b} down the opposite end of your shithole."
    scene w3_10070 with dissolve
    kat "Ah, haa... no..."
    scene w3_10071 with dissolve
    "Even through a trepidatious smile, there was a glint of satisfaction behind her eyes. As if everything was going according to her plan."
    scene w3_10070 with dissolve
    kat "{size=-10}Just a request...{/size}"
    scene w3_10071 with dissolve
    mct "(Ha! Let's see if you can keep that arrogance with a 12 inch horse dildo shoved up your shitter!)"
    scene w3_10072 with dissolve
    kat "Oh, o-oh...!"
    "Circling her o-ring, reality began to set in. Despite her bravado, {i}she was nervous.{/i}"
    scene w3_10073 with dissolve
    mc "What's the biggest thing you've ever fit back here?"
    scene w3_10074 with dissolve
    kat "Haa... I wonder... uh... heh..."
    kat "There was this one Dominican cabana boy... ha... haha, I would normally say \"hung like a horse\", but considering what's in front of me..."
    kat "I don't want to give you the wrong impress--"
    scene w3_10075 with hpunch
    kat "Oh-!!"
    "With just a little push and the right amount of distraction, the horse dildo's flare pried past the muscular ring of her rectum."
    scene w3_10076 with dissolve
    mc "So far, so good. That's the {b}thickest{/b} part."
    kat "The width isn't going to be the issue! I--"
    scene w3_10077 with dissolve
    mc "No it fucking isn't."
    "With a flick of the wrist, mere centimeters became an inch, but that was still the easy part. Unless I wanted this to turn into manslaughter, I would have to take it slow and with care..."
    scene w3_10078 with dissolve
    kat "O-, hhngg...!"
    mc "Remember what I said at the start of this? When I told you I'd trick you into thinking you're going to break? Well..."
    scene w3_10079 with dissolve
    kat "O-oh, auuahhh...♥"
    scene w3_10080 with dissolve
    mc "I hadn't considered this part, really. You might {b}actually{/b} break."
    scene w3_10081 with dissolve
    kat "Hnhh, ouahh..."
    scene w3_10080 with dissolve
    "{i}Half an inch."

    if w3KatPrincessPlay == True:
        mc "So far so good, princess."
    else:
        mc "So far so good, slut."

    scene w3_10082 with dissolve
    kat "--!"
    "{i}An inch this time.{/i}"
    mc "Yeah, just suck down air..."
    scene w3_10083 with dissolve
    "We had a long journey ahead of us, but inch by half inch, Kathleen's expression was a slurry of discomfort {i}and{/i} pleasure."
    "Another inch, and--"
    scene w3_10084 with dissolve
    "--and this was the first speed bump. The toy no longer wanted to go in with ease. It was now deeper than the past implements, and the curve wasn't making things easier."
    mc "Relax your sphincter."
    kat "F-fuck you! I would if I could!"
    scene w3_10085 with dissolve
    kat "Hg, hhaa!"
    scene w3_10086 with dissolve
    "...so I gave it time, and with the {b}most{/b} minor of force - we're talking micrometer by micrometer - slowly coaxed it deeper down the hag's quivering asshole."
    scene w3_10087 with dissolve
    kat "Oh, God, God, God, God...! Unnng..."
    "Second by second, turned into a minute."
    scene w3_10088 with dissolve
    "{i}Two.{/i}"
    "The time it took for her rectum to expand and reshape to accommodate the invader."
    scene w3_10089 with dissolve
    kat "Oh, G-god...♥"
    scene w3_10080 with dissolve
    mc "It's a bit too early to be thinking about him. {b}You're not gonna die.{/b}"
    "Yeah, slow and steady, until--"
    play sound "sound effects/spurt.wav"
    scene w3_10090 with hpunch
    kat "Gh-♥ H-heeuhh...?!"
    "--until I felt a pop as she relaxed and surprisingly {b}gushed{/b}, the head of the horse dildo pressing roughly into the soft tissue of her rectum and placing pressure on her womb."
    scene w3_10091 with dissolve
    kat "Ghhah, haaa..."
    mc "Look! We're halfway there!"
    kat "Ah, haahh...! I..."
    scene w3_10092 with dissolve
    mc "Isn't that exciting? There's just as much to come!"
    kat "Ah, hwwww--"
    scene w3_10093 with dissolve
    "{i}A quarter of an inch.{/i} I didn't want to push my luck."
    "Another inch and another roadblock, defeated all the same, with time and controlled persistence."
    scene w3_10089 with dissolve
    kat "Gahh, haaa...!"
    mc "It's a funny fucking tactic, this--"
    scene w3_10094 with dissolve
    kat "Gahh, hhaaaa..."
    "{i}Another half an inch.{/i}"
    mc "-- you giving up control to feel like you're {i}in control.{/i} Not that I mind..."
    scene w3_10095 with dissolve
    kat "Ah, haeehhh-!"
    mc "If this is what it feels like getting played by you, I'm all--"
    scene w3_10096 with hpunch
    kat "Gahh, haaaghh, heuuh...!"
    "With one final, firm push--"
    scene w3_10097 with dissolve
    mc "I'm all in! In both senses!"
    scene w3_10098 with dissolve
    kat "Ahh, ahh, eiauhh-"
    "At some point during the last half of our excursion, what little sense the sex drug left her was pushed out of the old woman's head to make room for a fake horse cock."
    scene w3_10099 with dissolve
    kat "Ghh...♥"
    scene w3_10100 with dissolve
    kat "Ah, ghwwah, hahhii...♥"

    if w3KatPrincessPlay == True:
        mc "There you go, princess! Good girl!"
    else:
        mc "There you go! There you go you fuckin' cunt!"

    "Brimming with bile, I put my weight down on the older woman's worthless womb, imprinting the horse dildo on her insides."
    play sound "sound effects/thud-floor.mp3"
    scene w3_10101 with hpunch
    kat "Gh, eeuuhh, heehhh--"
    mc "How do you like this shit, cunt? Am I living up to your expectations?"
    kat "Ghh, ahhh-♥"
    play sound "sound effects/spurt.wav"
    scene w3_10102 with vpunch
    kat "Ah, a--ahhwaaahhhhh...♥ {b}F-hhuch...!!{/b}"

    if w3KatPrincessPlay == True:
        mc "Ha! There ya go, princess! Bravo! Bravo!"
    else:
        mc "Ha! Nasty slut!!"

    scene w3_10103 with dissolve
    kat "Ghh, hehhh, wwa-awwahh..."
    mc "Babbling hag..."
    scene w3_10104 with dissolve
    kat "Gh- ahheeh..."
    mc "Quiet down and taste your own asshole for a little bit."
    scene w3_10105 with dissolve
    "Blissed out, she didn't protest."
    scene w3_10106 with dissolve
    "I took a moment and admired my work, and a terrible feeling gripped my being."
    scene w3_10107 with hpunch
    kat "Gahh, heehhh..."
    scene w3_10106 with dissolve
    "{i}A feeling of happiness.{/i}"
    mc "You should be proud. I didn't think it'd actually fit."

    if w3KatPrincessPlay == True:
        mc "You take cock with the best of 'em, princess. I doubt Felicia even has the anal fortitude to pull off a feat like this."
    else:
        mc "You take cock with the best of 'em, Mrs. P. I doubt Felicia even has the anal fortitude to pull off a feat like this."

    scene w3_10107 with dissolve
    kat "Euughh, gnhng..."
    scene w3_10106 with dissolve
    mc "You don't understand a fucking word I'm saying, do you?"
    "What I prepared in advance would snap her out of that haze, but first..."

    menu:
        "Commemorate the moment with a photo. ( w3KatPhoto = True)":
            $ w3KatPhoto = True
            scene w3_10108 with dissolve
            "It was only natural to mark success with a picture."
            "......"
            scene w3_10109 with dissolve
            if w3KatPrincessPlay == True:
                mc "Smile, princess."
            else:
                mc "Smile, cunt."

            play sound "sound effects/camera-phone-shutter.wav"
            with flash
            "She looked too messed up to care."
            scene w3_10108 with dissolve
            mc "Ha! Something to jerk off to later!"
        "She probably doesn't want any photos taken...":

            "Considering Darius' nebulous fate, let's not get too carried away taking compromising photos..."

    scene w3_10107 with dissolve
    kat "Gha, haa..."
    scene w3_10110 with dissolve
    mc "I've got something that'll wake you up!"
    scene w3_10111 with dissolve
    mct "(Now, for the main course...)"
    kat "G-gahh, heee-?!"
    "{i}It came out a lot easier than it went in.{/i}"
    play sound "sound effects/handcuffs.wav"
    mc "C'mon, look alive! {b}Move, move, move!{/b}"
    play ambient "sound effects/run-wood.wav"
    "............."
    "........."
    "......"
    play sound "sound effects/door-close.wav"
    "..."
    stop ambient
    play sound "sound effects/water-splash2.wav"
    mc "Seriously, I just don't comprehend it--"
    scene w3_10112 with fade
    kat "Ghh, hhk- pleeaahh--"
    "The old woman offered nothing in the way of resistance as I plunged her head into the tub."
    play sound "sound effects/water-splash3.wav"
    scene w3_10113 with dissolve
    mc "Is it just that you're so bored? So rich? So {b}old{/b} that something broke in your head and you need to do shit like this to get off?"
    kat "Ghhugg, gkhkhhk, gghhlugg...!"

    if w2HarpRainCheck == True:
        "This was my slice of irony. Just as she had offered Harper up to me..."
    else:
        "This was my slice of irony. Just as she had given Harper to me..."

    play sound "sound effects/water-splash3.wav"
    scene w3_10114 with dissolve
    mc "Or do you just have a pathological need to stir shit up? Bad childhood? A lack of control in your married life?"
    kat "Ghh, hhkk, mmhhuaahh-"
    scene w3_10115 with dissolve
    mc "Ah, shit. I'm getting too excited here..."
    "With the old woman submerged, my words were only rhetorical."
    play sound "sound effects/water-splash2.wav"
    scene w3_10116 with dissolve
    kat "Ghh, ahha, h-haa..."
    scene w3_10117 with dissolve
    mc "Now, where was I? Oh, yeah..."
    scene w3_10120 with dissolve
    "I didn't really know much about Kathleen Pulman, but I could take some stabs in the dark. {i}See if I draw blood.{/i}"
    scene w3_10117 with dissolve
    mc "That must be it! The reason you do {i}any of this.{/b}"
    mc "You haven't accomplished anything in life, have you? Not on your own merit."
    scene w3_10118 with dissolve
    kat "Ah, hahhh--"
    scene w3_10120 with dissolve
    "My hot breath on her cool, wet neck elicited a shudder."
    scene w3_10117 with dissolve
    mc "Just a middle-aged woman, over the hill... the wife of an elected official, playing with money your father made... running a charity made by your sister."
    mc "You. Are. {b}Nothing.{/b}"
    scene w3_10118 with dissolve
    kat "Ah, haa..."
    scene w3_10119 with dissolve
    kat "G-give me some credit... I'm n-not that cli--"

    if w3KatPrincessPlay == True:
        mc "Face it! You're fucking nothing, princess. Your sister {b}was{/b} better than you."
    else:
        mc "Face it! You're fucking nothing, {b}bitch.{/b} Your sister {b}was{/b} better than you."

    scene w3_10121 with dissolve
    kat "S-shut u-up and just--"
    play sound "sound effects/f-grunt1.wav"
    scene w3_10122 with vpunch
    kat "G-gahhh...! Y-you're i-in..."
    "After the horse dildo hollowed out her colon, slipping into this bitch's backdoor was seamless."
    scene ka_07_a with dissolve
    show ka_07
    kat "Ghh, haa-- a-ahh...! F-finally! G-good...!"
    mc "Hell, you're less than nothing! With all this shit you do at your charity and the club, you {b}detract{/b} from the world."
    "I had denied my need to fuck long enough. I immediately fell into a rut, bucking my hips with little regard or compassion."
    kat "Gmmh, hhaa- haa...!"
    "And if Kat's mewling was any evidence, she was in long need of an actual dicking too. The \"foreplay\" hadn't been enough to satiate her, but neither would this in all likelihood given her drug-soaked asshole."
    kat "Mmmh, mmhhh--!"

    if kat_polite == True:
        "The moment Mrs. Pulman's face delved back into the water, balls bouncing off her twat, I felt high."
    else:
        "The moment Kathleen's face delved back into the water, balls bouncing off her twat, I felt high."

    mc "That's right! You haven't accomplished shit in your life, have you?"
    "Over and over, I thrust wildly, careening in and out of the old woman's stretched bowels with an unsettling enthusiasm."
    scene ka_06_a with dissolve
    show ka_06
    mc "Everything you do at the club is just you pathetically staving off that reality!"
    "Similarly, words indiscriminately blasted out of my mouth like a shotgun, looking for slaughter."
    mc "Fuck, you're sad and pathetic!"
    "My only preoccupation here and now was wounding Kathleen's pride."
    kat "Ghhh, haehhhh--! Ghh, hhhk-!"
    "To implant my words in her malleable, lust-possessed mind and make her believe them."
    mc "Hedonism isn't--"
    "After all, the diatribe I was spewing was likely off the mark, but {i}even if a fraction of it landed...{/i}"
    scene ka_09_a with dissolve
    show ka_09
    mc "Hedonism isn't an accomplishment, you fucking bitch! No one respects you for it!"
    "If even a fraction of it landed, the prideful woman's already addled mental state would be in tatters.."
    kat "Ghh, hhhhkkk-!"
    "Not that she was getting even half of what I was saying..."
    scene ka_08_a with dissolve
    show ka_08
    mc "You're hearing me right? You catching any of this you {b}dumb shit hag?!{/b}"
    kat "Gh, hhmmm, ghhuuugg-!"
    mc "Ah, f-fuck..."
    "That happy feeling from earlier came back to me, {i}proving it was never that out of reach.{/i} I only needed to surrender to the opportunities that presented themselves."
    mc "And why the fuck would they?! I mean, {b}Christ{/b}, you're goddamn stupid!"
    "If I was in my right mind, I would stay my tongue."
    mc "Seriously?! What the fuck do you add to anything?!"
    kat "Ghh, haa-!"

    if kat_polite == True:
        "If Mrs. Pulman was in her right mind, my balls would be in a vice."
    else:
        "If Kathleen was in her right mind, my balls would be in a vice."

    scene ka_09_a with dissolve
    show ka_09
    mc "You're fucking nothing! August knows the business! Dr. Chuck's got the money!"
    "...but thankfully, both of us were {i}lost{/i} in the moment."
    mc "You add nothing!"
    "Lost {b}and{/b} paradoxically free."
    mc "But the patrons don't respect you just because you're a woman, right?"
    scene ka_08_a with dissolve
    show ka_08
    mc "That is what you think it comes down to, yeah? You don't have a dick?!"
    "So I let fly even more half-assed assumptions, even more half-formed nonsense..."
    mc "If only you were born a man, am I right?!"
    kat "Ghh, hhehhh--"
    mc "I bet you tell yourself you don't need anyone's respect, huh!"
    kat "Ghhm, mmhhh-! GHh, a-ahh!! Glgghhugg!"
    mc "Huh, you {b}fucking{/b} cunt?! All that matters is that you have {b}fun{/b}, right?! That's what you tell yourself?!"
    kat "Ghmm, mmhhh-!"

    if w3KatPrincessPlay == True:
        mc "Huh, princess?! Is that what you tell yourself? You nothing-ass-bitch!"
    else:
        mc "That what you fucking tell yourself? You nothing-ass-bitch!"

    kat "Ahh, hahhhh--"
    scene ka_07_a with dissolve
    show ka_07
    "Christ almighty, {b}this was cathartic!{/b}"
    mc "Aaaaah, {b}shit! Answer me you pig! {b}Answer me!{/b}"
    kat "Ghh, haeehhh...!"
    "If Kathleen Pulman was nothing, {i}I was even less,{/i} but that self-loathing gave my words feeling and released the gunk caked on the deepest parts of my soul."
    mc "You trashy fucking pig-hag-{b}bitch{/b}!"
    "It pushed me to give her what she wanted."
    scene ka_09_a with dissolve
    show ka_09
    mc "It eats you up! How dare those dumbasses not respect you?!"
    "No, {i}to give her what I wanted.{/i}"
    mc "Huh?! What do they got that you don't, huh?!"
    "After all, if I'm going to let this unwanted redheaded stepchild out in the sun, it might as well run free."
    mc "What do they have that you don't?! Well, news flash! Everything!"
    scene ka_06_a with dissolve
    show ka_06
    "This was me."
    kat "Ghhk, mhmhmhh-! Ahhh-!"
    "{i}This was me.{/i}"
    mc "They built businesses! They influence policy! Politics!"
    kat "Amhhh, h--hhhaa--"
    mc "Did you build a global pharmaceutical company?! You fucking pioneer some rocket tech?!"
    kat "Gh, yeee-♥"
    mc "Have you done ANYTHING that the world truly knows about?!"
    "{b}This was me.{/b}"
    scene ka_09_a with dissolve
    show ka_09
    kat "Hkhh,hkkhh, hhggguu-!"
    mc "No! All you do is call sad, needy women {b}whores{/b} and parade them about!"
    "Feelings that my rational mind rejected and put to the side; {i}it was all me.{/i}"
    kat "Ghh, hhhh--k--"
    scene ka_07_a with dissolve
    show ka_07
    mc "Your prissy fat ass doesn't {b}deserve{/b} respect and you GODDAMN know it."
    kat "Ghh, hkhh--"
    "My discontent, my unease, my disappointments and hatreds..."
    mc "The only thing your old ass deserves is the dick that's wedged up!"
    kat "Ghh, hhaahhh--"
    scene ka_08_a with dissolve
    show ka_08
    "Everything that the house of cards that was [mcf] was built on..."
    mc "You like getting fucked you fucking cunt?!"
    kat "Ghh, hweehhh--"
    "It all coalesced with the thrusting of my hips and the hatred I was letting out. I was weightless, {b}unshackled{/b}, relieved."
    play sound "sound effects/water-splash2.wav"
    scene w3_10123 with dissolve
    if w3KatPrincessPlay == True:
        mc "Answer me! Who's your fucking daddy?!"
        scene w3_10124 with dissolve
        kat "Ghh, h-a-hhhh--"
        scene w3_10123 with dissolve
        mc "Whos' your fucking daddy, princess?!"
        scene w3_10124 with dissolve
        kat "P-poppop, ahh-- y-you!"
    else:
        mc "Say yes, sir!"
        scene w3_10124 with dissolve
        kat "Eyyhhesshh--"
        scene w3_10123 with dissolve
        mc "Yes sir I'm a worthless old-ass pig!"
        scene w3_10124 with dissolve
        kat "Ghh, ahhehhh--"

    play sound "sound effects/water-splash.wav"
    scene w3_10125 with flash
    mc "Oh, {b}shut the fuck up, you shit-sucking moron!{/b}"
    "I held the old woman's head underwater."
    scene ka_10_a with dissolve
    show ka_10
    kat "Ghh, hhguuhhhk--"
    "I held her {b}firm.{/b}"
    mc "Seriously... philanthropist? Loving wife? {b}Show woman?{/b}"
    "{i}I held her firm and squeezed out everything in me.{/i}"
    mc "Think about it! Your actual fucking reality!"
    kat "Ghh, hhaahhh--"
    mc "You're speared on some 22-year old's cock, babbling, not hearing a fucking word I'm saying as you struggle to breathe!"
    kat "Ghh, khhhhkk, hgghluhhhg-! Ahghh--"
    mc "Like really?! Who the fuck are you?!"
    kat "Ghh, hehhh-"
    mc "You're fucking nothing!"
    "I was spiraling toward climax. How could I not?"
    mc "{b}NOTHING!{/b}"
    "Holding the older woman's head beneath the surface, feeling her body buck back with panic... {i}this was the most turned on I had been in my entire life.{/i}"
    kat "Ghh, hhggkk--"

    if w2HarpRainCheck == True:
        "Nothing could compare."
    else:
        "The scene that played out with Harper couldn't even compare."

    kat "Ghhh, hlhllluuhhhh--"
    mc "What?! You need to breathe? That's funny! Realizing now that you're just a frail old woman? That I can do {i}anything{/i} I want?"
    kat "Ghh, heuuuhhh--"
    mc "{b}You need air?!{/b}"
    kat "Ghh, wmmmh, mhmhhh-♥"
    mc "T-too fuckin' bad! A-although... you d-don't need to hold your breath much longer... {b}ah, shit.{/b}"
    kat "Mmhh, mhmhhh"
    mc "J-just fuckin' hold on... a-about to f-fill your guts... a-ahh... y-you.."
    kat "Mmhh, whmemmhfdh?!"
    mc "You c-can breathe when you're packed full of my--"
    stop music
    play sound "sound effects/spurt.wav"
    scene w3_10126 with flash
    "{i}Everything hit me all at once.{/i}"
    mc "Gahh, hhh--"
    play sound "sound effects/spurt.wav"
    with flash
    "As I poured my seed into Kathleen Pulman's bowels, hand locked on the back of her head, no stone was out of place. There was {b}harmony.{/b}"
    play sound "sound effects/spurt.wav"
    scene w3_10127 with flash
    kat "Ghh, hsdhhgh- Mmhmhh- mhmh, mhmh--"
    "This was the freedom promised, a once scary and terrible thing that had lost its bite."
    mc "Ahh, hahhh-!"

    if kat_polite == True:
        "Pressing deeply into Mrs. Pulman soft ass, I nurtured that precious feeling, knowing that it would slip away once the last bit of jism escaped my urethra."
    else:
        "Pressing deeply into Kathleen's soft ass, I nurtured that precious feeling, knowing that it would slip away once the last bit of jism escaped my urethra."

    play sound "sound effects/water-splash2.wav"
    play sound2 "sound effects/f-cough1.wav"
    scene w3_10128 with dissolve
    "......"
    scene w3_10129 with dissolve
    "..."
    play sound "sound effects/thud-heavy.wav"
    scene w3_10130 with vpunch
    "What immediately followed my invincibility was intense vulnerability."
    mc "Ah, haahhh... s-shit..."
    scene w3_10131 with dissolve
    "I had exposed myself to another person, {b}fully.{/b}"
    kat "Ah, haa, haaaa...."
    "--and not just anyone, but this incomprehensible witch of a woman."
    scene w3_10132 with dissolve
    kat "Ha, hahh, *cough* holy... ahh..."
    mc "Oh, I'm so fucked up..."
    scene black with fade
    "That feeling of freedom disappeared into blackness."
    play music "music/house-on-the-hill.ogg"
    scene w3_10133 with fade
    "...or so I thought, but next I knew, I found myself embraced."
    "The adrenaline dump hit me hard. I didn't want to move, I didn't want to utter a word, or anything that might otherwise confirm that I was indeed the outlet for that hateful outpour."
    kat "Haa, hahaaa..."
    scene w3_10134 with dissolve

    if kat_polite == True:
        "For some time, likely in an effort to collect herself, Mrs. Pulman didn't say a thing."
    else:
        "For some time, likely in an effort to collect herself, Kathleen didn't say a thing."

    kat "Ha, haa..."
    "...but her silence had an added effect. There was no room for rejection in between ragged breaths."

    "......"
    "..."
    scene black with fade
    mc "Ha... This floor fucking sucks..."
    kat "{b}Stop.{/b}"
    "As I made my way to my knees, a warm hand prevented my retreat."
    scene w3_10135 with fade
    "Though she struggled, {i}she got up first.{/i}"
    kat "Don't run..."
    scene w3_10136 with dissolve
    "The meaning of that act wasn't lost on me."
    scene w3_10137 with dissolve
    kat "Ah, haa...!"
    scene w3_10138 with dissolve
    "In real time, I watched the pieces of Kathleen Pulman pull themselves back together."
    if not persistent.w3KathleenTest:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3KathleenTest = True
    mc "...how are you okay?"
    scene w3_10139 with dissolve
    "{i}She clearly wasn't.{/i} Her legs shook, but she still willed herself erect. Both an admiration and a new fear of this woman's sheer willpower took hold in me."
    scene w3_10140 with dissolve
    kat "Heh, I'm {b}not{/b} okay. {b}I feel crazy.{/b} The aphrodisiac will be in my system for another hour... traces of the effect will linger all day..."
    scene w3_10141 with dissolve
    "She loomed over me as if I hadn't just battered her drug-laden ass while dunking her into a tub of water. {b}Like what the actual fuck.{/b}"
    scene w3_10140 with dissolve
    kat "...but that's not important right now. {b}How are you feeling?{/b}"
    scene w3_10141 with dissolve
    "Through ruined makeup and tear-stained eyes, she looked genuinely interested. Without thinking, {b}I answered honestly.{/b}"
    scene w3_10142 with dissolve
    mc "Like I'm not even myself..."
    scene w3_10143 with dissolve
    kat " H-ha... you sure? I think that was the most {i}you{/i} that I've ever seen. It was beautiful."
    scene w3_10142 with dissolve
    mc "...fuck off. What's so great about it?"
    scene w3_10144 with dissolve
    kat "It came from you, done with a... thoughtfulness and intensity {i}that's you.{/i}"
    "I didn't have anything to say to that. My instinct was to reject her, but..."
    scene w3_10146 with dissolve
    kat "Shame is an invention that hobbles us."
    scene w3_10145 with dissolve
    "She cradled me warmly, in a way I didn't think possible from her, and the vulnerability vanished."
    scene w3_10146 with dissolve
    kat "H-ha... the m-most insidious thing is that we inflict it on ourselves. It's born out of the fear of being... *scoff* {i}devalued{/i}... in the eyes of others..."
    scene w3_10145 with dissolve
    "With labored breath, she spoke in a way that suggested that wasn't a good thing; part of me thought it bullshit. Worrying about how the people you care about think of you was only natural, but I didn't refute her."
    $ renpy.end_replay()
    scene w3_10146 with dissolve
    kat "Shame only has the power you allow it, [mcf]."
    scene w3_10145 with dissolve
    "That much I agreed with... {i}I think.{/i} She was very persuasive right now."
    scene w3_10146 with dissolve
    kat "Was anything you did or felt tonight a bad thing?"
    scene w3_10147 with dissolve
    mc "{size=-10}Yes...{/size}"
    scene w3_10145 with dissolve
    "My affirmation was a whisper, like I didn't quite believe it myself."
    scene w3_10146 with dissolve
    kat "Why? Who got harmed?"
    scene w3_10147 with dissolve
    mc "I don't think it wise to nurture that kind of anger..."
    scene w3_10146 with dissolve
    kat "It's better to sit on it, then? I--"
    scene w3_10148 with dissolve
    kat "I..."
    scene w3_10149 with dissolve
    mc "Are you okay?"
    kat "Heh, ahh-ahh..."
    scene w3_10150 with dissolve
    "Again, even though she looked like she might faint, she willed herself to stand and mustered the composure to speak clearly."
    scene w3_10151 with dissolve
    kat "Can I let you in on a secret? You don't need to build a pharmaceutical empire to be an emperor."
    scene w3_10152 with dissolve
    mc "Ah, shit... you remember that part..."
    scene w3_10151 with dissolve
    kat "Any man or woman who understands and accepts themselves is sovereign. That is something men like Abel Van Doren have made the world forget."
    scene w3_10153 with dissolve
    kat "*Chwup* You impressed me... stand up."
    scene w3_10154 with dissolve
    "I hesitated. My own legs felt weak all of a sudden."
    scene w3_10155 with dissolve
    kat "Stand up! The floor doesn't suit you."
    scene w3_10156 with dissolve
    mc "..."
    scene w3_10157 with dissolve
    kat "If you don't believe me, I'll help."
    "God help me, why did those words fill me with an irrational sense of camaraderie?"
    scene w3_10158 with dissolve
    "It was absurd, but a simple change in level? I felt different all of a sudden."
    scene w3_10159 with dissolve
    kat "Good. Stand tall."
    scene w3_10160 with dissolve
    mc "Uh... did... did you get what you wanted out of this?"
    scene w3_10159 with dissolve
    kat "Yes, aha... ah... it was quite... {i}dramatic.{/i}"
    scene w3_10160 with dissolve
    mc "I see..."
    scene w3_10169 with pixellate
    kat "To my boyfriend and his bruised hand... to the frat boy who was now half-consciously pulling teeth out of his nose... {b}things were a big deal to them{/b}."
    "I recalled the old woman's words during our last heart-to-heart."
    kat "Their anger and angst, it turned out, was contagious. Watching them had me feel things I would otherwise only see in stories."
    scene w3_10161 with pixellate
    mc "I'm glad to be of use so {i}vicariously{/i}..."
    scene w3_10162 with dissolve
    kat "Do you really mean that, [mcf]?"
    scene w3_10161 with dissolve
    "She had accepted me for who I was, so..."
    mc "Fair is fair, right?"
    scene w3_10163 with dissolve
    kat "[mcf]! I..."
    scene w3_10164 with dissolve
    kat "Let's both have some fun tomorrow."
    scene w3_10165 with dissolve
    "She meant the exhibition, of course."
    scene w3_10166 with dissolve
    kat "Two more for this year and I think I'm going to treat them like they might just be my last. Now, uh..."
    scene w3_10167 with dissolve

    if kat_polite == True:
        "Mrs. Pulman gave me a lot to think about, but what she ultimately left me with defied thought."
    else:
        "Kathleen gave me a lot to think about, but what she ultimately left me with defied thought."

    kat "Help me to the kitchen."
    scene w3_10168 with dissolve
    "A call to will. An either you do or don't, are or aren't sort of feeling..."
    stop music fadeout 3.0
    scene black with fade
    "I carried it with me all the way to Hana's rock show."
    "......"
    "..."
    jump w3RockClubStart

label w3RockClubStart:
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionthegirls01 with blinds
    $ renpy.pause(6, hard=True)
    $ date = "june19night"
    play music "music/heavy-trailer-1.ogg"
    scene w3_10170 with blinds
    show screen qmenu with dissolve
    bar "What can I get you?"
    scene w3_10171 with dissolve
    show june19night with squares
    mina "I'm here to see... {i}Eros...?{/i} Massacre? Is, uh... Hana around?"
    scene w3_10170 with dissolve
    bar "You're not some kind of crazy stalker-fan type, are you?"
    scene w3_10172 with dissolve
    mina "What, uhh.... n-no?!"
    scene w3_10173 with dissolve
    bar "Why don't you sound sure of that?"
    scene w3_10174 with dissolve
    mina "I'm not! I'm her... I'm her... {i}friend.{/i}"
    scene w3_10175 with dissolve
    bar "Anyway, the band's in the back, getting ready. They go on in ten. Can I get you anything?"
    mina "Hmm, I don't know, what's--"
    scene w3_10176 with dissolve
    man "Whatever she wants, Eve."
    mina "Oh, uh..."
    scene w3_10177 with dissolve
    rfb "I'm {i}Pete.{/i}"
    scene w3_10178 with dissolve
    mina "Mina..."
    scene w3_10177 with dissolve
    rfb "I clocked you as soon as you walked in, Mina."
    scene w3_10179 with dissolve
    mina "Heh, I'm that out of place?"
    scene w3_10180 with dissolve
    rfb "Because you're beautiful."
    scene w3_10181 with dissolve
    mina "Oh, ummm.... really?"
    scene w3_10180 with dissolve
    rfb "I find it hard to believe that's news to you."

    if w3MinaHotelFucked == True:
        scene w3_10182 with dissolve
        mina "It's just I'm not used to being approached."
        scene w3_10180 with dissolve
        rfb "Makes sense. A girl like you gotta have a boyfriend."
        scene w3_10182 with dissolve
        mina "No... well, not exactly... it's... {i}complicated.{i}"
        scene w3_10183 with dissolve
        rfb "Got it. Lotta that around. I just broke up with mine a month ago."
        rfb "You wake up one day and you don't recognize the person you love anymore. {i}Nasty{/i} business..."
        rfb "So, can I buy you a drink?"
        scene w3_10184 with dissolve
        mina "Thanks! It's too early in the night for me, though."
        scene w3_10185 with dissolve
        rfb "I respect that. Mind if we talk?"
        mina "Sure... I don't mind the company."
        scene w3_10186 with dissolve
        mina "Just don't think I'm ignoring you. Lemme tell my friend I'm here."
        scene rewind1AZ
        stop music
        show rewind1
        rfb "Coo--"
    else:

        scene w3_10187 with dissolve
        mina "Oh, {i}thanks.{/i}"
        mina "It's just I'm not used to being approached."
        scene w3_10188 with dissolve
        rfb "Makes sense. A girl like you gotta have a boyfriend."
        scene w3_10189 with dissolve
        mina "No, I'm... I'm {b}single.{/b}"
        scene w3_10190 with dissolve
        rfb "Everyone here just let out a sigh of relief!"
        mina "Shut up!"
        scene w3_10191 with dissolve
        rfb "So, can I buy you a drink?"
        scene w3_10192 with dissolve
        mina "......."
        scene w3_10193 with dissolve
        mina "...sure, why not?"
        rfb "{i}Why not.{/i} That is what I like to hear."
        scene w3_10186 with dissolve
        mina "Lemme tell my friend I'm here..."
        scene rewind1AZ
        stop music
        show rewind2
        rfb "Coo--"

    scene black
    mc "Oh, look. There's Mina."
    kil "Great..."
    play music "music/heavy-trailer-1.ogg"
    scene w3_10194 with dissolve
    mc "What's with that reaction? You knew she was coming."

    if w3KatSnare == True:
        "Ian and I got here quite early. It beat sitting just navel-gazing about plugging a hag."
    else:
        "Ian and I got here quite early. It beat just sitting around in an empty apartment."

    scene w3_10195 with dissolve
    kil "It's just awkward, man! She wasn't even pissed-pissed at me. {i}Just disappointed and sad.{/i}"
    scene w3_10196 with dissolve
    mc "Should've thought of {i}this{/i} before you introduced her to me and Hana."
    scene w3_10197 with dissolve
    kil "Can't believe she even wanted to come..."
    scene w3_10198 with dissolve
    mc "Why? Did you expect her to be in mourning for a month or...?"
    scene w3_10199 with dissolve
    kil "I mean, she knows I'm here, right?"
    scene w3_10198 with dissolve
    mc "As I understand it, yes. Hana cleared it. Guess Mina's cool with it."
    scene w3_10195 with dissolve
    kil "Hana's fuckin' stupid and Mina's just being polite. If she turns her head and sees us yammering here it's gonna ruin her night."
    scene w3_10196 with dissolve
    mc "...and that thought bothers you?"
    scene w3_10200 with dissolve
    mc "......"
    scene w3_10201 with dissolve
    mc "...why'd you come, then?"
    scene w3_10202 with dissolve
    kil "{i}Beats me.{/i}"
    scene w3_10203 with dissolve
    mc "Well, looks like you don't have to worry about her being {i}too{/i} hung up..."
    scene w3_10204 with dissolve
    kil "What makes you say that?"
    scene w3_10205 with dissolve
    mc "Blood is in the water."
    scene w3_10206 with dissolve
    kil "...why do you always put shit in a gay way?"
    kil "That guy doesn't have a fuckin' chance."
    scene w3_10207 with dissolve
    mc "You sure about that? He's pretty handsome."
    scene w3_10208 with dissolve
    kil "{i}That{/i} skinny fucker?"
    scene w3_10209 with dissolve
    mc "Since when are you the jealous type?"
    scene w3_10210 with dissolve
    kil "I'm not jealous!"

    if w3MinaHotelFucked == True:
        scene w3_10211 with dissolve
        mc "Sure, you're not..."
    else:
        scene w3_10207 with dissolve
        mc "You sure? Because look. She's touching her hair..."

    scene w3_10212 with dissolve
    kil "I'm just stating an objective fact. Mina wouldn't go for a dude like that."
    scene w3_10211 with dissolve
    mc "Well, maybe you soured her on the preppy look, huh? You know how Felicia is... her rebound advice probably involves screwing half the town."
    scene w3_10213 with dissolve
    kil "{i}Whatever.{/i} She's entitled to some fun."
    scene w3_10214 with dissolve
    mc "Yeah? So would you mind if I took a stab at her? For some fun?"
    scene w3_10215 with dissolve
    kil "Dude, just stop. You're embarrassing yourself."
    mc "{i}How so?{/i}"

    if w3MinaHotelFucked == True:
        scene w3_10216 with dissolve
        "For whatever reason, I pushed the conversation in {i}that{/i} direction."
        scene w3_10217 with dissolve
        kil "You'd think she'd bite? {i}With you?{/i} Even without you being my best friend..."
        scene w3_10216 with dissolve
        "Did I want to tell him the truth? That we were fooling around? Or was this a {i}gloating{/i} feeling?"
    else:
        scene w3_10217 with dissolve
        kil "You'd think she'd bite? {i}With you?{/i} Even without you being my best friend..."

    scene w3_10218 with dissolve
    mc "...{i}I'm not her type?{/i}"
    scene w3_10216 with dissolve
    "......"
    scene w3_10219 with dissolve
    kil "...nah, dude. I didn't say that. You're a handsome fucking killer!"
    mc "Uh huh..."

    if w3MinaHotelFucked == True:
        scene w3_10220 with dissolve
        mct "(You've got no idea, fuckface...)"

    scene w3_10221 with dissolve
    kil "And if you two did hook up, it'd just be to get back at me, anyway."
    scene w3_10220 with dissolve

    menu:
        "You could live with that."(chg=["killian_down"]):
            $ Killian_Bromance -=1
            scene w3_10214 with dissolve
            mc "I could live with that..."
            scene w3_10208 with dissolve
            kil "...you serious?"
            scene w3_10211 with dissolve
            mc "I'm just busting your balls."
        "Mina's not that kind of girl.":
            scene w3_10209 with dissolve
            mc "I don't think Mina's that kind of girl."
            scene w3_10210 with dissolve
            kil "You're too trusting of women, dude."
            scene w3_10214 with dissolve
            mc "And you think too highly of your lasting effect on women."

    scene w3_10220 with dissolve
    "........."
    "......"
    scene w3_10221 with dissolve
    kil "...you should go say hello. I'll hang back here."
    scene w3_10209 with dissolve
    mc "You want me to gum up that guy, don't you?"
    scene w3_10217 with dissolve
    kil "Nah. It's just she'll be mad if she realizes you've waited so long to hug her."
    scene w3_10218 with dissolve
    mc "Riiiiight..."
    scene black with fade
    "Ian had a weird energy tonight."

    if w3MinaHotelFucked == True:
        scene w3_10222 with dissolve
        rfb "...if you want a place to start, I could recommend some bands."
        mina "Oh, that'd be neat! It'd give me something to talk about with--"
        scene w3_10223 with dissolve
        mina "[mcf]!"
        scene w3_10224 with dissolve
        "As usual, the blonde {i}pounced.{/i}"
        mc "Hey!"
        scene w3_10225 with dissolve
        mc "Sorry to interrupt."
        mina "Oh, you're not! This is Pete, he was teaching me a little about the kind of music Hana plays."
        scene w3_10226 with dissolve
        rfb "A friend?"
        mina "{i}Good{/i} friends."
        scene w3_10227 with dissolve
        rfb "'sup?"
        mc "Hey! I'm [mcf]."
        scene w3_10228 with dissolve
        mina "Pete is also in a band. You're on the radio, right?"
        scene w3_10229 with dissolve
        rfb "It's not that big of a deal. Just a couple of alternative stations nationally."
        mc "That sounds like a big deal to me."
    else:
        scene w3_10230 with dissolve
        rfb "...oh! You could be in one of our music videos."
        mina "Oh, really...? Hehe, I've never considered acting in a music video before, aren't they usually a bit...?"
        scene w3_10231 with dissolve
        rfb "It's a dying art; it's not all twerking."
        mina "Hehe, what are--"
        scene w3_10232 with dissolve
        mina "[mcf]!"
        scene w3_10233 with dissolve
        "As usual, the blonde {i}pounced.{/i}"
        mc "Hey!"
        scene w3_10234 with dissolve
        mc "Sorry to interrupt. I just wanted to say hi real quick."
        mina "Heh, don't apologize for something like that!"
        scene w3_10235 with dissolve
        rfb "'sup?"
        mc "Hey! I'm [mcf]."
        rfb "{i}Pete.{/i}"
        scene w3_10236 with dissolve
        mina "[mcf]'s a {b}friend.{/b}"
        mc "Nice to meet you."
        scene w3_10228 with dissolve
        mina "Pete was just telling me about his band! They sounded like a pretty big deal."
        scene w3_10229 with dissolve
        rfb "Oh, not really... we just get some play regionally."
        mc "Sounds cool!"

    scene w3_10237 with dissolve
    rfb "Ha! Yeah! It's pretty cool."
    scene w3_10238 with dissolve
    mc "So, you're a fan of Eros Massacre?"
    scene w3_10239 with dissolve
    rfb "They're good! I like how {i}eclectic{/i} they are..."
    scene w3_10238 with dissolve
    mc "Do you know Hana?"
    scene w3_10240 with dissolve
    rfb "Oh, yeah. I know the whole band. It's a small scene."

    if minaBreakOff == True:
        scene w3_10241 with dissolve
        mina "Oh! [mcf] is dating Hana!"
        scene w3_10242 with dissolve
        rfb "Man, {b}good luck{/b} with that."
        scene w3_10243 with dissolve
        mc "What's that supposed to mean?"
        rfb "Ah, I didn't mean... just... eh, she's kinda intense, isn't she?"
        scene w3_10244 with dissolve
        mc "{i}In the best way.{/i}"
        rfb "I bet you have the claw marks down your back to prove that, huh?"
        "{i}I didn't like this fucker.{/i}"
    else:

        scene w3_10241 with dissolve
        mina "{b}Oh! Awesome!{/b}"
        scene w3_10240 with dissolve
        rfb "You a fan?"
        scene w3_10238 with dissolve
        mc "Friend of Hana, actually."
        scene w3_10242 with dissolve
        rfb "Right on, right on..."

    scene w3_10245 with dissolve
    rfb "So, how do {b}you two{/b} know each other?"
    scene w3_10246 with dissolve
    mina "Uh, ha, that's..."

    if w3MinaHotelFucked == True:
        scene w3_10247 with dissolve
        rfb "Complicated?"
        scene w3_10238 with dissolve
        mc "Not really. We met through a friend recently."
    else:
        scene w3_10238 with dissolve
        mc "We met through a friend recently."

    scene w3_10240 with dissolve
    rfb "Really? I figured you two went way back. You have that kind of vibe."
    scene w3_10248 with dissolve
    mc "That's her talent."
    scene w3_10249 with dissolve
    "......"
    "...Pete was playing it cool, checking the temperature, running his calculations behind a smile. And just as an awkward silence began to set--"
    scene w3_10250 with dissolve
    rfb "Well, I've got a friend I should go talk to."
    "He came out ahead of it."
    scene w3_10251 with dissolve
    rfb "Message me sometime, Mina. We could be friends too."

    if w3MinaHotelFucked == True:
        mina "Oh, oh yeah, um.... it was nice meeting you!"
    else:
        mina "{b}Sure!{/b} Thanks for the drink!"

    scene w3_10252 with dissolve
    "........."
    scene w3_10253 with dissolve
    "......"
    scene w3_10254 with dissolve
    mc "...so, he gave you his number, did he? He works fast."
    scene w3_10255 with dissolve
    mina "We just exchanged Instagrams."
    scene w3_10254 with dissolve
    mc "Oh... I don't have one of those."
    scene w3_10256 with dissolve
    mina "Heh! You're old!"
    scene w3_10257 with dissolve
    mc "Shut up."
    scene w3_10258 with dissolve
    mina "I don't like it either, but it promotes my acting and modeling, soooo..."
    scene w3_10254 with dissolve
    mc "So are you going to \"message\" him? He left the ball in your court on purpose."

    if w3MinaHotelFucked == True:
        scene w3_10259 with dissolve
        mina "Ah, I don't know... he kinda reminds me of a certain someone, and... well... wouldn't you be mad?"
        scene w3_10260 with dissolve
        "I paused to consider that question. The correct answer was no - {i}and I wouldn't{/i}, but the feeling in my gut wasn't so straightforward."
        scene w3_10261 with dissolve
        mc "Why? I don't have any right to be. It's not like you're my woman..."
        scene w3_10262 with dissolve
        mina "Yeeeahh, that's true..."
        scene w3_10263 with dissolve
        "At best, I was Mina's rebound. At worst, I was a rebound with the loaded potential of getting back at her shitty ex."

        if hanaGF == True:
            "To top it all off, I wasn't in a position to want more from her. I {i}had{/i} promised Hana monogamy..."
            mct "(Which is goin' great, you prick...)"

        "Yet..."

        scene w3_10264 with dissolve
        menu:
            "I felt greedy. (w3MinaJealous = True)":
                $ w3MinaJealous = True
                "It was only natural to want a woman like Mina to yourself."
            "You are okay with that.":
                "...we had the perfect arrangement already. All upside, no down."

        scene w3_10255 with dissolve
        mina "...do you think I should?"
        scene w3_10264 with dissolve
        mc "Message him...? If you want to."

        if w3MinaJealous == True:
            "I hated saying that, but I was annoyingly committed to saying the \"intellectually honest\" thing..."

        mc "It could be a good experience, getting to know more people... that's what your goal is, right?"
        scene w3_10259 with dissolve
        mina "I'm just saying I'd get it if you didn't want me to... I wouldn't be upset about it..."
        scene w3_10261 with dissolve
        mc "God, you're such a sweetheart."
        scene w3_10265 with dissolve
        mina "Hehe..."

        if w3MinaJealous == True:
            scene w3_10260 with dissolve
            "Putting a lid on my greed, I didn't answer her. If I told her not to, she probably wouldn't, but to what end? Did I want Mina as {i}my{/i} girlfriend?"

            if hanaGF == True:
                "Was I stupid?"
            else:
                "Perhaps that was a relevant question..."

        scene w3_10255 with dissolve
        mina "...are you here {i}alone?{/i}"
        scene w3_10266 with dissolve
        mc "No, I came here with--"
    else:

        scene w3_10258 with dissolve
        mina "I might... I don't have a reason not to."
        scene w3_10257 with dissolve
        mc "Meeting some new people might do you some good."
        scene w3_10255 with dissolve
        mina "...are you here {i}alone?{/i}"
        scene w3_10266 with dissolve
        mc "No, I came here with--"


    scene w3_10267 with dissolve
    "Ian had vanished."
    mc "He's somewhere... are you good with that? I don't think it was such a good idea for Hana to--"
    mina "I'll manage, [mcf]."
    scene w3_10268 with dissolve
    mc "Are you sure? It's been like what? A week?"
    mina "I'm choosing to focus on the positive people in my life and I just want to see Hana perform. That's gonna be cool!"
    scene w3_10269 with dissolve
    mc "That's an admirable perspective."
    mina "Heh, we'll see how that goes... do you mind me sticking to you for a little bit? Next to Ian, you're the only person I know until Hana appears..."
    scene w3_10270 with dissolve
    mc "Not at all. Stick away."

    if w3MinaHotelFucked == True:
        scene w3_10271 with dissolve
        mina "...but not {i}too{/i} close, right? Not with Ian and all..."
        mc "I haven't told him, no."
        scene w3_10272 with dissolve
        mina "You probably shouldn't, either..."
        scene w3_10273 with dissolve
        mc "If you asked me yesterday, I would have said there was a chance he could be okay about it, but... {i}eh.{/i} I think he's anxious about seeing you tonight."
        scene w3_10272 with dissolve
        mina "Yeah, {i}right.{/i}"
        scene w3_10273 with dissolve
        mc "No, really..."
    else:
        scene w3_10271 with dissolve
        mc "Besides, I don't think Ian will be sniffing around."
        mina "...why not?"
        scene w3_10273 with dissolve
        mc "Would you believe me if I said he was anxious about seeing you tonight?"
        scene w3_10272 with dissolve
        mina "No, I wouldn't."
        scene w3_10273 with dissolve
        mc "Seriously. I'm getting a similar shy vibe as when were kids, but unfortunately for him, he can't hide behind my mother's skirt."

    stop music fadeout 3.0
    scene w3_10274 with dissolve
    mina "......"
    mina "...whatever."

    play music "music/running-it-down.ogg"
    if minaGym == True:
        scene w3_10275 with dissolve
        ver "Hey, guys!"
        mina "Oh...? {b}Veronica!{/b} Why are you here?!"
        scene w3_10277 with dissolve
        ver "Am I not allowed to be?"
        scene w3_10278 with dissolve
        mina "No! I'm just surprised to see you!"
        scene w3_10279 with dissolve
        mc "I invited her. The more to see Hana the merrier, right?"
        scene w3_10280 with dissolve
        mina "........."
        mina "......"
        scene w3_10281 with dissolve
        ver "...something on my face?"
        scene w3_10282 with dissolve
        mina "I..."
        scene w3_10280 with dissolve
        "Wearing the expression of a puppy dog in need, Mina looked like she wanted to say something."
        scene w3_10282 with dissolve
        mina "Can I give you a hug, coach?"
        scene w3_10283 with dissolve
        "Veronica, amused. just opened her arms invitingly."
        scene w3_10284 with dissolve
        mina "Heh~"
        scene w3_10285 with dissolve
        "Without a second thought, Mina fell into the Amazon's embrace like she was jumping into a big pile of leaves."
        scene w3_10284 with dissolve
        mina "I didn't know if it'd be appropriate."
        scene w3_10286 with dissolve
        ver "We're not at the gym. Hug away, cutie."
        scene w3_10285 with dissolve
        "And so she did, relishing the large woman's all-comprehensive embrace."
        scene w3_10287 with dissolve
        "As they broke, Mina's potency proved too much for even Veronica to bear. She smiled wide, without restraint."
        scene w3_10288 with dissolve
        mina "I love your outfit!"
        scene w3_10289 with dissolve
        ver "Thanks! You look scrumptious yourself."
    else:
        scene w3_10276 with dissolve
        ver "Hey, [mcf]. Who's the beautiful woman?"
        mc "Veronica, hey! This is Mina."
        scene w3_10290 with dissolve
        mina "Ooooh! A friend?"
        mc "This is my trainer at the gym. I invited her here tonight. The more seeing Hana rock out the better, eh?"
        scene w3_10291 with dissolve
        mina "Ah, good idea! I should've invited some people!"
        scene w3_10292 with dissolve
        mina "It's great to meet you, Veronica!"
        scene w3_10293 with dissolve
        ver "Likewise, cutie."
        scene w3_10294 with dissolve
        mina "I like your outfit!"
        scene w3_10295 with dissolve
        ver "Thanks. You..."
        "......"
        scene w3_10296 with dissolve
        ver "...you look scrumptious yourself."

    scene w3_10297 with dissolve
    mc "Why do you always sound like a perverted old man, Veronica?"
    scene w3_10298 with dissolve
    mina "What?! No, she doesn't!"
    "Oh, sweet, naive Mina..."
    scene w3_10299 with dissolve
    ver "Hey, maybe later you could give me tips on how to accessorize... I'm not good at that sort of thing. Grew up a tomboy, as you can probably guess."
    scene w3_10300 with dissolve
    mina "I wouldn't guess! You look so freaking cool! Like one of a kind, but {b}I'd love to talk fashion.{/b}"
    scene w3_10299 with dissolve
    ver "Awesome!"
    scene w3_10301 with dissolve
    mc "See, Veronica? Not such a bad idea coming out, was it?"
    scene w3_10302 with dissolve
    ver "Well... this isn't really my type of bar, but a change of pace isn't so bad. I'm going to go get a beer."
    scene w3_10299 with dissolve
    ver "I'll hit you up about those tips later. Sound good?"
    scene w3_10300 with dissolve
    mina "Hehe, sounds good!"
    scene w3_10303 with dissolve
    "........."
    scene w3_10304 with dissolve
    "......"
    m_dev "Hey, my Master just wanted to let you know, you should probably save here. There is many \"routes\" ahead and you WILL need to do several playthroughs to see them all."
    m_dev "{m_note}If you push for Mina x Veronica you will NOT get the Mina x Hana kiss scene, nor will you get it if you're on Hana's GF route."
    m_dev "Enough talk back to the game!"
    if minaGym == True:
        jump w3RockShowVeroMinaGymTalk
    else:
        jump w3RockShowVeroMinaTalk

label w3RockShowVeroMinaGymTalk:
    scene w3_10305 with dissolve
    mc "...you two seem to get along well."
    scene w3_10306 with dissolve
    mina "She's super cool!"
    mina "I'm surprised you invited her. I didn't know you guys were friends like that."
    scene w3_10307 with dissolve

    if w3VeroBarDate == True:
        mc "We've hung out outside of the gym a couple of times."
        scene w3_10308 with dissolve
        mina "Wow! You're more social than you let on."
    else:
        mc "It was just a spur-of-the-moment thing."

    scene w3_10309 with dissolve
    mina "Well, whatever the case, I'm glad she's here! Now I have three people here I know {i}and{/i} like."
    scene w3_10310 with dissolve
    mc "Maybe {i}four.{/i} Felicia might stop by, but she couldn't make any promises."
    scene w3_10311 with dissolve
    mina "Yeah... she told me her husband is running for mayor. She's going to be busy playing her part, she said... which is really fricken' crazy."
    scene w3_10312 with dissolve
    mc "She didn't sound happy about that."
    scene w3_10311 with dissolve
    mina "{i}She's not.{/i} I don't think Felicia wants the spotlight on her like that."
    scene w3_10312 with dissolve
    mc "It sounded like Elias' plans came out of the blue. Felicia was surprised."
    scene w3_10311 with dissolve
    mina "It's bothering her. She says Elias isn't spontaneous, so she thinks he either didn't tell her his plans on purpose or something's changed."
    scene w3_10313 with dissolve
    mc "I imagine she's not too thrilled about either of those being the case..."
    scene w3_10314 with dissolve
    mc "Hey, look..."
    scene w3_10315 with dissolve
    mc "It kinda looks like she's flirting with the bartender."
    mina "She's so cool..."
    mc "You think?"
    scene w3_10316 with dissolve
    mina "I'm a little envious. She's so forward with what she wants..."
    mc "And you're one of the things she wants, you know. Or haven't you noticed?"

    if Mina_BiCurious >= 3 and w3MinaHotelFucked == True:
        mina "So you've said, but she's probably just like that with everybody."
    else:
        mina "She's probably just like that with everybody."

    scene w3_10317 with dissolve
    mc "Every hot girl, maybe."
    scene w3_10318 with dissolve
    "......"

    if Mina_BiCurious >= 3:
        scene w3_10319 with dissolve
        mina "...you think she would really? Like with me, I mean...?"
        scene w3_10320 with dissolve
        mc "Why not?"
        scene w3_10321 with dissolve
        mina "Look at her... she's a world-class athlete... she owns her own business... and..."
        scene w3_10320 with dissolve
        mc "And?"
        scene w3_10322 with dissolve
        mina "And I'm just a kid?"
        scene w3_10317 with dissolve
        mc "Ha! I'm not sure where the disconnect is. Older, accomplished people gravitate toward young and beautiful ones."
        scene w3_10322 with dissolve
        mina "Maybe for creepy old men, but not--"
        scene w3_10317 with dissolve
        mc "Not a tall, beautiful, super cool woman you admire?"
        scene w3_10323 with dissolve
        mina "......"
        scene w3_10324 with dissolve
        mina "...heh, it {i}is{/i} flattering."
        scene w3_10323 with dissolve
        menu:
            "{color=#FF1493}[[Lesbian Push]{/color} ...{i}just{/i} flattering?":
                $ w3VeronicaMinaLezPush = True
                scene w3_10325 with dissolve
                mc "You're blushing. Is it {i}only{/i} flattering?"
                scene w3_10323 with dissolve
                "Mina didn't answer."

                if w3FeliciaMinaThreesomeEnd == True:
                    scene w3_10325 with dissolve
                    mc "...maybe doing it with Felicia whet your appetite??"
                    scene w3_10326 with dissolve
                    mina "You just want to do it with two women again..."
                    scene w3_10327 with dissolve
                    "Perhaps, in time, but tonight..."
                    mc "Nothing to do with me. {i}You{/i} should flirt with her. I'll root from the sidelines."
                    scene w3_10328 with dissolve
                    mina "W-what? You want me to approach her alone?!"
                    scene w3_10320 with dissolve
                    "Something about Mina awkwardly trying to flirt with the carnivorous lesbian {i}did something to me.{/i}"
                    mc "Why not? You said you were envious of how she goes for what she wants. {b}You want her{/b}, don't you?"
                    scene w3_10318 with dissolve
                    "--so, I encouraged her as such."
                elif w3MinaHotelFucked == True:
                    scene w3_10325 with dissolve
                    mc "...you're curious about it. It's on your list."
                    scene w3_10324 with dissolve
                    mina "It is..."
                    scene w3_10323 with dissolve
                    mc "You should flirt with her."
                    scene w3_10322 with dissolve
                    mina "What about you?"
                    scene w3_10317 with dissolve
                    "In time, perhaps the three of us might tangle, but tonight..."
                    mc "I'll root from the sidelines."
                    scene w3_10328 with dissolve
                    mina "W-what? You want me to approach her alone?!"
                    scene w3_10320 with dissolve
                    "Something about Mina awkwardly trying to flirt with the carnivorous lesbian {i}did something to me.{/i}"
                    mc "Why not? You said you were envious of how she goes for what she wants. {b}You want her{/b}, don't you?"
                    scene w3_10318 with dissolve
                    "--so, I encouraged her as such."
                elif minaBreakOff == True:
                    scene w3_10325 with dissolve
                    mc "...you still doing your list?"
                    scene w3_10322 with dissolve
                    mina "I hadn't thought about it. Without you to help me..."
                    scene w3_10320 with dissolve
                    "We may have ended our arrangement prematurely thanks to Hana, but..."
                    mc "I may not be able to help you personally anymore, but... I can encourage you. {b}You should flirt with her.{/b}"
                    scene w3_10321 with dissolve
                    mina "I don't think I could..."
                    scene w3_10320 with dissolve
                    mc "Why not? You said you were envious of how she goes for what she wants. {b}You want her{/b}, don't you?"
                    scene w3_10318 with dissolve
                else:
                    scene w3_10325 with dissolve
                    mc "...you're curious, aren't you? I can tell."
                    scene w3_10323 with dissolve
                    "We weren't that close for me to be prodding her like this, but I felt like encouraging my {i}single{/i} friend."
                    scene w3_10324 with dissolve
                    mina "Well, I mean... I've wondered sometimes..."
                    scene w3_10323 with dissolve
                    mc "You're a single woman. You seem to be interested, she's {i}clearly{/i} interested. You should try flirting a little."
                    scene w3_10321 with dissolve
                    mina "I don't know, [mcf]..."
                    scene w3_10320 with dissolve
                    mc "Why not? You said you were envious of how she goes for what she wants. {b}You want her{/b}, don't you?"
                    scene w3_10318 with dissolve

                "......"
                "...she was actually thinking about it."
                scene w3_10332 with dissolve
                hana "Heeeeeeey!"
                jump w3RockShowHanaGreeting
            "...switch the topic to Hana.":

                scene w3_10317 with dissolve
                mc "Do you know when Hana's gonna go on?"
                scene w3_10329 with dissolve
                mina "Bartender said 10 minutes five minutes ago."
                scene w3_10317 with dissolve
                mc "...guess she's getting ready."
                scene w3_10329 with dissolve
                mina "I texted her, she said she'd come out in a sec."
                scene w3_10317 with dissolve
                mc "Awesome."
                scene w3_10330 with dissolve
                "We waited around a bit, and--"
                scene w3_10332 with dissolve
                "Speak of the devil."
                hana "Heeeeeeey!"
                jump w3RockShowHanaGreeting
    else:
        scene w3_10329 with dissolve
        mina "It's kinda flattering."
        scene w3_10317 with dissolve
        mc "Just flattering, huh? Well, do you know when Hana's gonna go on?"
        scene w3_10329 with dissolve
        mina "Bartender said 10 minutes five minutes ago."
        scene w3_10317 with dissolve
        mc "...guess she's getting ready."
        scene w3_10329 with dissolve
        mina "I texted her, she said she'd come out in a sec."
        scene w3_10330 with dissolve
        mc "Awesome."
        "We waited around a bit, and--"
        scene w3_10332 with dissolve
        "Speak of the devil."
        hana "Heeeeeeey!"
        jump w3RockShowHanaGreeting


label w3RockShowVeroMinaTalk:
    scene w3_10305 with dissolve
    mc "...you two seemed to hit it off quick."
    scene w3_10306 with dissolve
    mina "Oh, my god! She's {i}so{/i} tall! If I had a best friend like that, I could get out of the sun whenever I wanted."
    scene w3_10307 with dissolve
    mc "You have a beautiful way of looking at things, Mina. Never change."
    scene w3_10331 with dissolve
    mina "Shut {b}uuuuuuup!{/b}"
    scene w3_10310 with dissolve
    mc "By the way, she was flirting with you."
    scene w3_10308 with dissolve
    mina "Really? She's gay?"
    scene w3_10310 with dissolve
    mc "Yep."
    scene w3_10309 with dissolve
    mina "Huh! {b}Cool!{/b} It'll be nice having someone to get to know tonight. Apart from you, Hana will be busy..."
    scene w3_10310 with dissolve
    mc "Speaking of. Felicia might stop by, but she couldn't make any promises."
    scene w3_10311 with dissolve
    mina "Yeah... she told me her husband is running for mayor. She's going to be busy playing her part, she said... which is really fricken' crazy."
    scene w3_10312 with dissolve
    mc "She didn't sound happy about that."
    scene w3_10311 with dissolve
    mina "{i}She's not.{/i} I don't think Felicia wants the spotlight on her like that."
    scene w3_10312 with dissolve
    mc "It sounded like Elias' plans came out of the blue. Felicia was surprised."
    scene w3_10311 with dissolve
    mina "It's bothering her. She says Elias isn't spontaneous, so she thinks he either didn't tell her his plans on purpose or something's changed."
    scene w3_10312 with dissolve
    mc "I imagine she's not too thrilled about either of those being the case..."
    scene w3_10313 with dissolve
    "........."
    scene w3_10318 with dissolve
    "......"
    scene w3_10317 with dissolve
    mc "...when do you think Hana is going on?"
    scene w3_10329 with dissolve
    mina "Bartender said 10 minutes five minutes ago."
    scene w3_10317 with dissolve
    mc "...guess she's getting ready."
    scene w3_10329 with dissolve
    mina "I texted her, she said she'd come out in a sec."
    scene w3_10330 with dissolve
    mc "Awesome."
    "We waited around a bit, and--"
    scene w3_10332 with dissolve
    "Speak of the devil."
    hana "Heeeeeeey!"
    jump w3RockShowHanaGreeting

label w3RockShowHanaGreeting:
    scene w3_10333 with dissolve
    mina "{b}Haaaaanaaaaaa!{/b}"
    scene w3_10334 with dissolve
    "It was the most audacious hug yet."
    hana "Ha.. ah-ah-? D-down dog--"
    "{i}Hana was not prepared.{/i}"
    scene w3_10335 with dissolve
    mina "Hehe, no! Thanks for inviting me tonight!"
    hana "I should be the one thanking you for coming since you're probably not into this kind of music, but--"
    mina "Yeah, yeah, yeah... it's going to be the coolest thing I've seen all week. Don't get shy on us~ hehe~"
    scene w3_10336 with dissolve
    mina "Besides I'm picking up a few things. Did you know {i}Pussy Tommy's{/i} influence was the {b}Anal Cats?{/b}"
    scene w3_10337 with dissolve
    hana "Uh, no I didn't... you didn't have to do research for this."
    scene w3_10338 with dissolve
    mc "She didn't. Some rocker boy gave her a primer while flirting with her."
    scene w3_10339 with dissolve
    hana "Oh, God! I know the fucking type."
    scene w3_10340 with dissolve
    mc "Well, that specific type knows you, too. Pete--"
    scene w3_10341 with dissolve
    hana "{i}Him?{/i} {b}Trolley Problem{/b} Pete?"
    mina "I think that's what he said his band--"
    scene w3_10342 with dissolve
    hana "Hahahah, ah...!"
    mina "What's so funny?!"
    scene w3_10343 with dissolve
    hana "Nothing. What did you think of him?"
    scene w3_10344 with dissolve

    if w3MinaHotelFucked == True:
        mina "Ummm, he seemed nice-ish? Until [mcf] scared him off..."
    else:
        mina "...I guess, he seemed nice? He left when [mcf] showed up..."

    hana "...did he?"
    "Hana shot me a smile."
    scene w3_10345 with dissolve
    mina "Why were you laughing?"
    scene w3_10346 with dissolve
    hana "Well..."
    "......"
    scene w3_10347 with dissolve
    hana "...eh, water under our lead singer's bridge, but nothing you need to be warned about."

    if w3MinaJealous == True:
        "Again, I felt a hypocritical pang in my stomach."

    scene w3_10345 with dissolve
    mina "Water under the bridge? Don't be mysterious! Why did you laugh?!"
    scene w3_10348 with dissolve
    hana "It's a long {i}and{/i} embarrassing story. Ask me later when I'm not about to go on stage."
    hana "Plus, I don't want to dissuade you on anything. He's a successful and interesting guy; you could do worse with your time."
    scene w3_10349 with dissolve
    mina "I'm not sure if I'm interested in the first place..."
    hana "I don't blame you for that..."
    "......"
    scene w3_10350 with dissolve
    hana "...Ian here?"
    scene w3_10351 with dissolve
    mc "He's somewhere. We came together."
    scene w3_10352 with dissolve
    hana "...nothing wrong with taking a break from men, but don't let one asshole control what you do either. Go with your gut, eh?"
    scene w3_10353 with dissolve
    mina "A break from men, huh..."

    if Mina_BiCurious >= 3 and minaBreakOff == True or Mina_BiCurious >= 3 and w3MinaHotelFucked == True or w3VeronicaMinaLezPush == True:
        "Little did Hana know, {i}that had a whole other meaning for Mina.{/i}"

    if hanaGF == True:
        jump w3RockShowHanaGFGreeting
    elif w3HanaDP >= 4:
        jump w3RockShowHanaFBGreeting
    else:
        jump w3RockShowHanaFriendGreeting

label w3RockShowHanaGFGreeting:
    scene w3_10354 with dissolve
    hana "And you..."
    mc "Me...?"
    "Hana got closer, wearing an unusually bashful expression."
    scene w3_10355 with dissolve
    "She was showing her cute side, waiting and hoping for an acknowledgment from her boyfriend."

    if w3MinaTransparent == False and w3MinaHotelFucked == True:
        "I would have kissed her then and there, but..."
        scene w3_10356 with dissolve
        mc "What Mina said earlier. Thanks for inviting me."
        "Mina had no knowledge about Hana being my {i}girlfriend.{/i}"
        scene w3_10357 with dissolve
        hana "...?"
        scene w3_10358 with dissolve
        hana "You know it..."
        scene w3_10356 with dissolve
        mc "You go on soon?"
    else:

        scene w3_10359 with dissolve
        mc "Chwup*"
        scene w3_10360 with dissolve
        mc "You look even more beautiful than the first time I saw you standing here. No after-work visits this time, eh?"
        hana "What are they going to do? Fire me?"

        if minaBreakOff == True:
            scene w3_10361 with dissolve
            mina "Aaaah, you two are such a cute couple!"
        elif w3MinaHotelFucked == True:
            scene w3_10362 with dissolve
            mina "..."
        else:
            scene w3_10363 with dissolve
            mina "Oooh, I didn't know you two..."

        "Suddenly I remembered Mina and thought better about joking about the club, even in a vague way."
        scene w3_10364 with dissolve
        mc "You go on soon?"

    scene w3_10365 with dissolve
    hana "Yep. Actually, I need to get back to the band... next time you see me I'll be on stage."
    scene w3_10364 with dissolve
    mc "I'm looking forward to it."
    scene w3_10366 with dissolve
    "She just smiled back, as if sitting on top of the world."
    scene w3_10367 with dissolve
    hana "By the way, Mina..."
    mina "Hmmm?"
    hana "{i}You look hot tonight.{/i} Fuck your ex-boyfriend."

    if Mina_BiCurious >= 3:
        scene w3_10368 with dissolve
        mina "Aaaah, um... {i}thanks...{/i} I wanted to look good for your show."
        scene black with fade
        "......"
        "..."
    else:
        scene w3_10369 with dissolve
        mina "Thanks!"
        scene black with fade
        "......"
        "..."
    jump w3RockShowRosalindCantGetIn

label w3RockShowHanaFBGreeting:
    scene w3_10370 with dissolve
    hana "Thanks for coming too, [mcf] - even though you probably thought we were awful last week."
    scene w3_10371 with dissolve
    mc "Well... what are {i}friends{/i} for, eh?"
    scene w3_10372 with dissolve
    hana "They're for saying \"no, you were amazing\" when they see a friend fishing for a compliment."
    scene w3_10371 with dissolve
    mc "Can I try again?"
    scene w3_10373 with dissolve
    hana "Sure - thanks for coming, even though you probably thought we were awful last week."
    scene w3_10374 with dissolve
    mc "{i}What are friends for again?{/i}"
    scene w3_10375 with dissolve
    hana "Pssh! Unfunny fuck!"
    scene w3_10376 with dissolve
    "We shared a friendly, yet intimately brief smile."
    scene w3_10371 with dissolve
    mc "You go on soon?"
    scene w3_10372 with dissolve
    hana "Yep. Actually, I need to get back to the band... next time you see me I'll be on stage."
    scene w3_10371 with dissolve
    mc "I'm looking forward to it."
    scene w3_10373 with dissolve
    hana "Uh huh... sure you are..."
    scene w3_10366 with dissolve
    "And a brief moment of awkward sexual tension later..."
    scene w3_10367 with dissolve
    hana "By the way, Mina?"
    mina "Hmmm?"
    hana "{i}You look hot tonight.{/i} Fuck your ex-boyfriend."

    if Mina_BiCurious >= 3:
        scene w3_10368 with dissolve
        mina "Aaaah, um... {i}thanks...{/i} I wanted to look good for your show."
        scene black with fade
        "......"
        "..."
    else:
        scene w3_10369 with dissolve
        mina "Thanks!"
        scene black with fade
        "......"
        "..."
    jump w3RockShowRosalindCantGetIn


label w3RockShowHanaFriendGreeting:
    scene w3_10377 with dissolve
    hana "Thanks for coming too, [mcf]."
    mc "What are friends for?"
    scene w3_10378 with dissolve
    hana "Yeah... fyi, you didn't have to get dressed up."
    mc "...what, do I look out of place?"
    hana "Abso-fucking-lutely you square, {i}and{/i} it looks like your work attire."
    scene w3_10379 with dissolve
    mina "Oh, Ian's uncle's--"
    mc "Fuck you, I look {i}great.{/i}"
    "Suddenly I remembered Mina, and even if it was a vague mention, I steered the conversation away from the club."
    scene w3_10380 with dissolve
    mc "Don't I, Mina?"
    mina "Oh, yeah! I think you look handsome!"
    scene w3_10381 with dissolve
    hana "That's the equivalent of your mom telling you that."
    mc "Remember that when you ask for my opinion about tonight's show."
    scene w3_10376 with dissolve
    "Hana and I briefly smiled at each other and our mutual ribbing."
    scene w3_10371 with dissolve
    mc "So... you go on soon?"
    scene w3_10372 with dissolve
    hana "Yep. Actually, I need to get back to the band... next time you see me I'll be on stage."
    scene w3_10371 with dissolve
    mc "I'm looking forward to it."
    scene w3_10373 with dissolve
    hana "Uh huh..."
    scene w3_10366 with dissolve
    "And a brief moment of sexual tension later..."
    scene w3_10367 with dissolve
    hana "By the way, Mina..."
    mina "Hmmm?"
    hana "{i}You look hot tonight.{/i} Fuck your ex-boyfriend."

    if Mina_BiCurious >= 3:
        scene w3_10368 with dissolve
        mina "Aaaah, um... {i}thanks...{/i} I wanted to look good for your show."
        scene black with fade
        "......"
        "..."
    else:
        scene w3_10369 with dissolve
        mina "Thanks!"
        scene black with fade
        "......"
        "..."
    jump w3RockShowRosalindCantGetIn



label w3RockShowRosalindCantGetIn:
    scene w3_10382 with dissolve
    mina "She's great, isn't she...?"
    mc "One of a kind."
    play ambient "sound effects/ringing-inbound.wav"
    stop music fadeout 3.0
    scene w3_10383 with dissolve
    "*Ring, ring*"
    mc "One sec."
    stop ambient
    play sound "sound effects/phonemenu.wav"
    scene w3_10384 with dissolve
    mc "Uh huh? Yeah...? {i}Really{/i}"
    "..."
    mc "You don't say? Why won't they-- don't leave, I'll be right there."
    play sound "sound effects/phonemenu.wav"
    scene w3_10385 with dissolve
    mina "Who was that?"
    mc "Another friend I invited tonight."
    play music "music/positioned.ogg"
    scene w3_10386 with dissolve
    mina "How many people did you invite?"
    scene w3_10387 with dissolve
    mc "Veronica, Felicia, and a co-worker."

    if w3MinaHotelFucked == True:
        scene w3_10386 with dissolve
        mina "The one that's staying with you?"
        scene w3_10387 with dissolve
        mc "She left today, but she's all alone, so..."
        scene w3_10388 with dissolve
        mc "...what's with that look?"
        scene w3_10389 with dissolve
        mina "Nothing..."
    else:
        scene w3_10390 with dissolve
        mina "Oh, cool! More people to meet!"

    scene w3_10387 with dissolve
    mc "I need to go help her get in."
    scene w3_10391 with dissolve
    mina "Can I come with? I'd go chat with Veronica, but..."
    scene w3_10392 with dissolve
    mc "I don't think I've met anyone else with more game than her..."
    mina "It's astounding..."
    scene w3_10393 with dissolve
    "......"
    scene w3_10394 with dissolve
    mc "...anyway, yeah, come with me. You can help me solve the problem."
    mina "What do you--"
    scene black with fade
    "........."
    "......"
    scene w3_10395 with dissolve
    rose "I look like someone's mom?! He said they were at capacity!"
    "As it were, the bouncer wouldn't let Rosalind in."
    mina "The nerve of that guy!"
    "Luckily--"
    scene w3_10396 with pixellate
    mina "Whatever! We can go to that bar down the street."
    bouncer "Hey, hold on! You're her friend?"
    mina "That's right..."
    "Luckily Mina {i}was{/i} the kind of face they'd want brightening up the walls."
    scene w3_10397 with pixellate
    rose "Greasy idiot!"
    mina "Yeah! Jerk!"
    "The two quickly found a burgeoning camaraderie."
    scene w3_10398 with dissolve
    "........."
    "......"
    scene w3_10399 with dissolve
    mc "...how you doin' Rose?"
    scene w3_10400 with dissolve
    rose "Thanks for your help, although... I also wouldn't be here {i}at all{/i} if I didn't have to."
    scene w3_10401 with dissolve
    mina "...what do you mean by that? Why do you have--"
    scene w3_10402 with dissolve
    mc "...have you been drinking? Did you pre-game this?!"
    rose "So what?! You know how expensive drinks are in a place like this?!"
    "{i}Huh.{/i}"
    scene w3_10403 with dissolve
    mc "I'm not judging you; just surprised is all. Was also surprised that you didn't say goodbye earl--"
    scene w3_10404 with dissolve
    rose "I was making it easy on you, okay?! Getting out of your hair, not making a big pro--"
    mc "I would've helped you--"
    scene w3_10405 with dissolve
    rose "I took care of everything just--"
    scene w3_10406 with dissolve
    mina "You guys are {b}really{/b} good friends!"
    scene w3_10407 with dissolve
    mc "Huh? What makes you say that?"
    scene w3_10408 with dissolve
    rose "By the way... who is this, [mcf]?"
    mc "{i}Mina.{/i}"
    scene w3_10409 with dissolve
    rose "......"
    scene w3_10410 with dissolve
    rose "...thanks for your help earlier."
    scene w3_10411 with dissolve
    mina "No problem! I don't know what that guy was on about. {i}You're gorgeous!{/i}"
    scene w3_10412 with dissolve
    rose "Oh, uh... {i}thanks.{/i}"
    play music "music/finland.ogg"
    scene w3_10413 with dissolve
    jacob "[mcf!]! My man!"
    scene w3_10414 with dissolve
    mc "Jacob, and..."
    mc "Mr. Byrnes!"

    if hanaFlag == True:
        "No surprise. He was here last time."

    scene w3_10415 with dissolve
    mina "Huh? How many people do you know? Am... {size=-10}am I the loser between us?{/size}"
    scene w3_10416 with dissolve
    aug "It seems my daughter has a lot of support tonight."
    scene w3_10417 with dissolve
    mina "You're--"
    mina "Oh! You're Hana's Dad?! Wow!"
    scene w3_10418 with dissolve
    aug "And who is this beautiful young woman?"
    mc "A friend of mine {i}and{/i} Hana's."
    aug "How do you do, dear?"
    scene w3_10419 with dissolve
    rose "They let {i}you{/i} in?!"
    aug "...and why wouldn't they."
    scene w3_10420 with dissolve
    "......"
    scene w3_10421 with dissolve
    rose "...maybe the drinks aren't {i}that{/i} expensive."
    scene w3_10422 with dissolve
    "And like that, Rosalind moved deeper into the club."
    scene w3_10423 with dissolve
    aug "I'd love to learn more about you, Mina."
    "{i}I didn't like the sound of that...{/i}"
    mina "Oh, sure!"
    scene w3_10424 with dissolve
    "They had come up so suddenly, it was just now dawning on me that Mina was being introduced to a dangerous gangster."
    "...{i}good fuckin' job [mcf] and Hana.{/i} What friends!"
    scene black with fade
    "......"

    if ianIntrospect == True:
        jump w3RockShowIanTalkOption
    else:
        jump w3RockShowBarTalkInterlude

label w3RockShowIanTalkOption:
    scene w3_10425 with fade
    "On the way back in, I scanned for Ian."
    scene w3_10426 with dissolve
    "There he was, by himself... {i}looking lonely.{/i}"
    "........."
    "......"

    menu:
        "...go talk to him."(chg=["killian_up"]):
            $ Killian_Bromance += 1
            $ w3RockShowIanTalk = True
            "He {i}is{/i} my longest friend - and I know that expression."
            "Bereft of bravado, no distractions, unhappy..."
            scene w3_10427 with dissolve
            mc "*Sigh* I'll be right back."
            mina "Where are you-- {b}oh, okay.{/b}"
            "Mina thankfully realized without me saying it."
            mina "He looks kinda sad, doesn't he? I've never... eh, go play the child of divorce. I'm fine."
            stop music fadeout 3.0
            scene black with fade
            mc "Thanks. Find you later."
            jump w3RockShowIanIntrospectiveTalk
        "...go to the bar with the group.":

            scene w3_10427 with dissolve
            "...whatever the case, as much as I {i}hated{/i} that expression of his... I didn't want to leave Mina alone in the company of August."
            stop music fadeout 3.0
            scene black with fade
            "..."
            jump w3RockShowAugustMinaTalk

label w3RockShowBarTalkInterlude:
    scene w3_10425 with fade
    "On the way back in, I scanned for Ian."
    scene w3_10428 with dissolve
    "There he was: occupying his time just fine. Flirting with {i}two{/i} women."
    mct "(Ha... you prick. {i}Have fun.{/i})"
    stop music fadeout 3.0
    scene black with fade
    "..."
    jump w3RockShowAugustMinaTalk


label w3RockShowIanIntrospectiveTalk:
    play music "music/outreach.ogg"
    scene w3_10429 with dissolve
    mc "...hey, buddy. How are you doing?"
    scene w3_10430 with dissolve
    kil "Aaaaaw, {b}shit{/b}, don't use your stepdad voice! Fuck you! I'm not--"
    scene w3_10429 with dissolve
    mc "You're not sitting around like a sad sack in a club full of people?"
    scene w3_10430 with dissolve
    kil "Can't a guy just vibe? Just for a few minutes?"
    scene w3_10431 with dissolve
    mc "I'll vibe with you."
    scene w3_10432 with dissolve
    "........."
    scene w3_10433 with dissolve
    "......"
    scene w3_10434 with dissolve
    kil "...how's Mina?"
    scene w3_10435 with dissolve
    mc "Meeting {i}everyone.{/i}"
    scene w3_10434 with dissolve
    kil "I saw you two walk in with August and Jacob... kinda fuckin' wild."
    scene w3_10436 with dissolve
    mc "He's just Hana's dad. That's what I'm telling myself."
    kil "Yeah, of course he is... {i}he's Hana's dad{/i}, not our pimp boss that I've seen perfectly carve an apple in ten seconds."
    mc "He's not that tonight, no..."
    scene w3_10432 with dissolve
    "......"
    "..."
    scene w3_10437 with dissolve
    mck "Pffh, ha!"
    "We shared a laugh over the situation."
    scene w3_10438 with dissolve
    mc "Ah, heh... seriously, why you sitting here doing nothing? There's plenty of chicks to hit on. Have you seen the bartender?"
    scene w3_10439 with dissolve
    kil "She's alright."
    scene w3_10438 with dissolve
    mc "Fuck you dude, she's a smoke show."
    scene w3_10439 with dissolve

    if w3HanaDP >= 4:
        kil "Got a thing for tats, eh? Makes sense."
    else:
        kil "Got a thing for tats, eh?"

    scene w3_10440 with dissolve
    mc "You haven't answered my question."
    scene w3_10441 with dissolve
    kil "You don't have to hit on chicks or drink to have fun."
    scene w3_10440 with dissolve
    mc "Yeah, that's my fucking line to you, dude. {i}You{/i} are out of character."
    scene w3_10442 with dissolve
    "......"
    scene w3_10443 with dissolve
    kil "Just not feelin' it is all."
    scene w3_10440 with dissolve
    mc "Not since Mina walked in?"
    scene w3_10441 with dissolve
    kil "Pretty much."
    scene w3_10433 with dissolve
    "I was surprised he admitted it."
    scene w3_10435 with dissolve
    mc "...remember that homework I gave you?"
    scene w3_10434 with dissolve
    kil "You'll have to refresh my memory..."
    scene w3_10452 with pixellate
    mc "All I'm asking you to do is to introspect when things are out of place in your headspace - and Mina is a good place to start."
    scene w3_10453 with dissolve
    kil "...because it will make me a better person?"
    scene w3_10454 with dissolve
    mc "I'm suggesting that figuring out what dissatisfied you about how things ended with her will help you determine if it's worth the effort to alter or mask your behavior."
    scene w3_10447 with pixellate
    kil "Oh, that?"
    scene w3_10446 with dissolve
    mc "What's the deal with you and Mina, really?"
    "He didn't answer, but {i}considered.{/i}"
    "He considered for a dozen seconds, half a minute... {i}the silence was uncanny.{/i}"
    scene w3_10444 with dissolve
    kil "I'm hung up on a particular thought... I'm pathetic."
    scene w3_10445 with dissolve
    mc "...that's your conclusion? That doesn't sound like you."
    scene w3_10444 with dissolve
    kil "I don't give anyone a reason to respect me, do I?"
    scene w3_10445 with dissolve
    mc "Whose respect do you want that you don't have?"
    scene w3_10447 with dissolve
    kil "I don't know, and maybe that is even worse. There's you and Vicky, but who else do I have in my life whose respect matters?"
    scene w3_10446 with dissolve
    mc "...your uncle?"
    scene w3_10447 with dissolve
    kil "Sure, and... {i}Mina.{/i} The most earnest girl I've met. Most people are just... {i}I don't know.{/i}"
    scene w3_10455 with pixellate
    kil "Sometimes it felt like she was a mirror, right? Whenever I fucked up or made her jealous, it was like seeing what other people saw when they looked at me."
    kil "For the first time, instead of testing other people's limits, I was seeing what I could get away with with myself. Whenever she looked hurt, {i}I felt it{/i}."
    scene w3_10448 with pixellate
    mc "You don't like your reflection."
    kil "Huh? What?"
    mc "Your Mina mirror metaphor."
    scene w3_10443 with dissolve
    kil "{i}Oh...{/i} no shit. I'm not going to pretend otherwise."
    scene w3_10442 with dissolve
    "........."
    "......"
    scene w3_10441 with dissolve
    kil "...I want to apologize to her. You think that's stupid?"
    scene w3_10440 with dissolve
    mc "No, I don't, but..."
    scene w3_10441 with dissolve
    kil "It is up to her if she wants to hear it. That's what Vicky taught us about apologies, right?"
    scene w3_10434 with dissolve
    kil "It takes two people. An apology you force on somebody is just self-centered."
    scene w3_10435 with dissolve
    mc "You want me to ask her to talk to you?"
    scene w3_10441 with dissolve
    kil "Would you...?"
    scene w3_10432 with dissolve

    menu:
        "You will. (w3IanMinaTalk = True)":
            $ w3IanMinaTalk = True
            scene w3_10438 with dissolve
            mc "Of course I will."
            scene w3_10439 with dissolve
            kil "...thanks, dude."
        "No promises.":
            scene w3_10440 with dissolve
            mc "I won't make any promises. The wound is still fresh, you know?"
            scene w3_10443 with dissolve
            kil "*Sigh* Yeah, okay..."
            scene w3_10449 with dissolve
            mc "If the mood is right, I'll bring it up."
            scene w3_10443 with dissolve
            kil "That's all I can ask."

    scene w3_10450 with dissolve
    mc "Can I get you anything at the bar?"
    kil "Nah, I want to stay sober tonight."
    scene w3_10451 with dissolve
    mc "Sure, but go meet some people or something. Don't just sit around."
    kil "You got it, amigo."
    scene black with fade
    "So he wants to apologize, eh? For the shit he set on fire {i}on purpose?{/i}"
    jump w3RockShowStarting


label w3RockShowAugustMinaTalk:
    play music "music/knockout.ogg"
    scene w3_10456 with dissolve
    aug "So, Mina, how long have you known my daughter?"
    scene w3_10457 with dissolve
    mina "Not too long, we met at [mcf]'s birthday party a couple weeks ago."
    scene w3_10458 with dissolve
    aug "That short of time?"
    scene w3_10459 with dissolve
    mina "Why do you sound surprised?"
    scene w3_10456 with dissolve
    aug "She spoke of you fondly last night."
    scene w3_10460 with dissolve
    mina "She did?!"
    aug "She did indeed. My daughter is a smart girl; she doesn't have many friends."
    scene w3_10461 with dissolve
    aug "She takes after her old man like that."
    "August {i}relished{/i} the chance to speak about his daughter, conveying a degree of familiarity that I wasn't so sure was there."
    scene w3_10462 with dissolve
    mina "Me too!"
    "His smile, however, was genuine. I'd never seen him {i}beam{/i} like that."
    scene w3_10463 with dissolve
    aug "You too, what?"
    mina "That I, uh... I'm fond of Hana too, heh..."
    scene w3_10464 with dissolve
    aug "Aren't you precious?"
    mina "Hehe~"
    scene w3_10465 with dissolve
    aug "Get me a drink, [mcf]."
    "It didn't read as a question..."
    scene w3_10466 with dissolve
    aug "You want anything, dear?"
    mina "I'm good!"
    mc "Alright..."
    scene black with fade
    "...a couple of people in front of me later--"

    if hanaFlag == True:
        scene w3_10467 with fade
        bar "What can I get-- ah, I remember you."
        scene w3_10468 with dissolve
        mc "You do? You've got to see a million faces."
        scene w3_10469 with dissolve
        bar "You stand out, to put it nicely."
        scene w3_10470 with dissolve
        mc "Do I...?"
        scene w3_10469 with dissolve
        bar "What, that a surprise?"
        scene w3_10471 with dissolve
        "......"
        scene w3_10468 with dissolve
        mc "...yeah, I know I fuckin' do."
        scene w3_10472 with dissolve
        bar "What can I get you?"
    else:
        scene w3_10472 with fade
        bar "What can I get you?"

    scene w3_10473 with dissolve
    "........."
    "......"
    "...ah, shit."
    scene w3_10474 with dissolve
    mc "Hey, what do you--"
    scene w3_10475 with dissolve
    mc "......"
    scene w3_10473 with dissolve
    mc "...my boss didn't tell me what he wanted."
    scene w3_10472 with dissolve
    bar "Point him out to me, and I'll tell you a safe bet."
    scene w3_10468 with dissolve
    mc "Bullshit."
    scene w3_10476 with dissolve
    bar "You don't believe me? Are you belittling the experience of a bartender?"
    scene w3_10477 with dissolve
    mc "...alright. Your guess {i}is{/i} better."
    bar "Damn straight it is."
    scene w3_10478 with dissolve
    mc "Over there. The guy in the--"
    bar "You're with Mr. Byrnes?"
    scene w3_10479 with dissolve
    mc "...uh, you know him?"
    bar "{i}You{/i} know him? He's {i}your{/i} boss?"
    scene w3_10480 with dissolve
    "The bartender looked at me cautiously."
    scene w3_10481 with dissolve
    bar "No guessing needed. Regal Scotch Whiskey, coming up."
    mc "Thanks..."
    scene w3_10482 with dissolve
    "........."
    "......"
    scene w3_10483 with dissolve
    mc "...hey! Since when are you two friendly?"
    scene w3_10484 with dissolve
    jacob "I'm everybody's friend!"
    scene w3_10485 with dissolve
    bar "Here 'ya go... Mister...?"
    scene w3_10486 with dissolve
    mc "[mcf]. Just [mcf]."
    scene w3_10487 with dissolve
    bar "Sorry about gettin' stiff on 'ya. I'm just surprised; I usually have a pretty good read, but you don't look like you work for--"
    scene w3_10488 with dissolve
    mc "No, I do not. It's probably not what you are imagining though."
    scene w3_10489 with dissolve
    bar "You Mr. Byrnes gardener?"
    scene w3_10488 with dissolve
    mc "Nope. Guess again."
    scene w3_10489 with dissolve
    bar "Chef? chauffeur?"
    scene w3_10488 with dissolve
    mc "No and no. I'm just the guy fetching drinks."
    scene w3_10490 with dissolve
    bar "Ha! Right!"
    scene w3_10491 with dissolve
    bar "...you like lookin' out of place? That your thing?"
    scene w3_10492 with dissolve
    mc "Uh..."
    scene w3_10491 with dissolve
    bar "Cute."
    scene w3_10493 with dissolve
    "......"
    scene w3_10494 with dissolve
    bar "...I'm guessing you probably shouldn't keep Mr. Byrnes waiting?"
    scene w3_10495 with dissolve
    mc "What do I owe--"
    scene w3_10496 with dissolve
    bar "It's on the house, {i}of course.{/i}"
    scene w3_10495 with dissolve
    mc "{b}Of course{/b}, yeah..."
    scene black with fade
    "..."
    jump w3RockShowStarting



label w3RockShowStarting:
    if w3RockShowIanTalk:
        scene w3_10497 with fade
        "I quickly rejoined the pair, who had found a corner away from the crowd."
        aug "[mcf]! Sit down. Mina was just telling me she's an actress!"
        scene w3_10498 with dissolve
        "So I joined them. The opportunity to convince Mina to talk to Ian, if I even wanted to, wasn't now."
        mc "You two are chatty."
    else:
        scene w3_10499 with dissolve
        aug "Oh, [mcf]! Thanks! Sit down!"
        scene w3_10498 with dissolve
        mc "No problem... {i}you two are chatty.{/i}"

    scene w3_10500 with dissolve
    mina "Hana's dad is really nice!"
    scene w3_10501 with dissolve
    aug "Ha! Don't tell her that! Besides, it is only when I want to be..."
    scene w3_10502 with dissolve
    mina "Hehe, anyway, only an aspiring actress. Modeling is mostly what pays the bills..."
    scene w3_10503 with dissolve
    aug "You know, I used to make movies!"
    "{b}--!{/b}"
    mina "Really?!"
    mct "(What the fuck old--)"
    scene w3_10504 with dissolve
    aug "Lots of 'em, actually, I--"
    mc "Hey when was Hana--"
    scene w3_10505 with dissolve
    aug "Nothing you would have seen. Corporate videos, and the occasional {i}art{/i} film."
    scene w3_10506 with dissolve
    mina "I guess creativity runs in the family?"
    aug "Ha ha, I suppose it does!"
    scene w3_10507 with dissolve
    "He looked at me, {i}knowing.{/i} Amused."
    scene w3_10508 with dissolve
    aug "How are you, [mcf]? I never asked. Looking forward to the weekend?"
    scene w3_10509 with dissolve
    mc "Ha, uh... to be honest, every day has been feeling like a Saturday recently."
    scene w3_10510 with dissolve
    aug "Not a bad problem to have."
    play sound "sound effects/rock-crowd-start.wav"
    scene w3_10511 with dissolve
    aug "Oh, look--"
    aug "The show is about to start. It feels good not needing to hide in the corner anymore..."
    scene w3_10512 with dissolve
    aug "By the way, the upstairs room is yours."
    mc "What do you--"
    scene w3_10513 with dissolve
    aug "You and your friends are free to use it."
    mc "Thanks..."
    scene w3_10514 with dissolve
    aug "Come on! Let's get close to the action! {b}Bahaha!{/b}"
    mina "Yeah!"
    "August's enthusiasm for his daughter's performance was a {i}match{/i} for Mina's."
    scene black with fade
    mina "Let's scream our butts off!"
    play ambient "sound effects/rock-crowd-stage-loop.wav"
    jump w3RockShowStart

label w3RockShowStart:
    "The music began with little fanfare. Just..."
    play music "music/pure-energy-9.ogg"
    scene w3_10515 with snake
    jer "Fuck you very much for having us again!"

    if hanaFlag == True:
        "Jerrica swaggered out with the same nonchalance as before, jumping straight into it."
    else:
        "The girl I had met earlier belted out a non-introduction, taking pride in it."

    scene w3_10516 with snake2
    pause
    scene w3_10517 with snakes
    pause
    scene w3_10518 with goslow
    pause
    scene w3_10519 with w4
    pause
    scene w3_10516 with snake2
    pause
    scene w3_10520 with irisout
    pause
    scene w3_10520 with vpunch
    pause
    scene w3_10520 with vpunch
    pause
    scene w3_10520 with vpunch
    pause
    scene w3_10518 with w19
    pause
    scene w3_10518 with vpunch
    pause
    scene w3_10518 with vpunch
    pause
    scene w3_10518 with vpunch
    pause
    scene w3_10516 with vpunch
    pause
    scene w3_10516 with vpunch
    pause
    scene w3_10519 with vpunch
    pause
    scene w3_10519 with vpunch
    pause
    scene w3_10521 with vpunch
    stop music fadeout 4.0
    play sound "sound effects/applause-small.wav"
    "........."
    "......"
    jer "...okay, next one, you pricks!"
    scene black with fade
    "Without missing a beat the band launched into another song and--"
    play ambient "sound effects/rock-crowd-floor-ambience.wav"
    play music "music/positioned.ogg"
    scene w3_10522 with fade
    mina "{b}Wooooooah!{/b} I've never seen live music before like {i}this.{/i} This is *SO* awesome!"
    scene w3_10523 with dissolve
    "My blonde companion was enamored by the cacophony blasting us, meanwhile I..."
    scene w3_10524 with dissolve
    mc "Yeah, it is {i}pretty{/i} cool..."
    scene w3_10523 with dissolve

    if hanaFlag == True:
        "...still wasn't quite used to the discordant pangs and howls."
    else:
        "...hadn't yet made sense of the discordant pangs and howls."
        scene w3_10524 with dissolve
        mc "Pretty, {b}pretty{/b} cool...}"
        scene w3_10523 with dissolve
        "Did this even qualify as music? Everyone here seemed to think so..."

    scene w3_10522 with dissolve
    mina "Hana's got so much energy!"
    scene w3_10525 with dissolve
    "That was something I could agree with. The goth girl looked radiant on stage, happy and at ease amongst her friends."
    scene w3_10526 with dissolve

    if hanaGF == True:
        mc "Hehe, doesn't she?"
    else:
        mc "She's really something, huh?"

    scene w3_10527 with dissolve
    mina "{size=-5}I'm so glad I was invited...{/i}"
    "More a personal affirmation than a statement, Mina spoke in a soft voice, inaudible over the growl of the bass guitar save for the pattern of her lips."
    scene w3_10528 with dissolve
    mc "...you liking the music so far?"
    mina "I am! It's so different!"

    if w3RockShowIanTalk == True:
        "The genuinely happy look on her face had me envying her openness for life. I thought back on Ian's request; {i}this wasn't the time.{/i}"
    else:
        "The genuinely happy look on her face had me envying her openness for life."

    scene w3_10529 with dissolve
    mc "We better get back to cheering then."
    mina "Haha! {i}{b}Fuck{/b}{/i} yeah!"
    scene black with fade
    mc "Oh no, the bad influence is setting in."
    "{i}Eros Massacre{/i} played on."

    if w3VeronicaMinaLezPush == True:
        jump w3RockShowBeginTheFlirt
    else:
        stop ambient fadeout 3.0
        jump w3RockShowBathroomBreak

label w3RockShowBeginTheFlirt:

    scene w3_10530 with fade
    ver "Hey, cute thing."
    mc "You talkin' to me, right?"
    ver "Who else would I be talking to?"
    mina "Pffh!"
    scene w3_10531 with dissolve
    ver "You two are chummy."

    if w3VeroBarDate == True:
        scene w3_10532 with dissolve
        "Sufficiently plied with alcohol, Veronica found her way back to us around the fourth song."
        scene w3_10533 with dissolve
        ver "She's been in your shadow all night."
    else:
        scene w3_10532 with dissolve
        "Sufficiently plied with alcohol, Veronica found her way back to us around the fourth song. I knew as much because.."
        scene w3_10533 with dissolve
        ver "She's been in your shadow all night."
        scene w3_10532 with dissolve
        "...she wouldn't touch me like this otherwise."

    scene w3_10534 with dissolve
    mina "...you, uh... you've been looking?"
    scene w3_10535 with dissolve
    "Just as I was, Mina also remembered our conversation from earlier, asking a painfully transparent question."
    scene w3_10536 with dissolve
    ver "I..."
    "And caught off guard by the blonde's openness, Veronica momentarily faltered."
    ver "I happen to turn my head every now and then..."
    scene w3_10537 with dissolve
    "Despite her egregious flirting at the gym, she likely wrote Mina off as an improbability. This was my chance to give the gals a little push."
    scene w3_10538 with dissolve
    mc "Good thing you're here."
    scene w3_10539 with dissolve
    ver "Why's that?"
    scene w3_10540 with dissolve
    mc "She doesn't know too many people here, and I bet..."
    mina "...eh?"
    mc "I think she's been getting bored of my company."
    scene w3_10541 with dissolve
    mina "I'm not, I'm--"
    mc "Not happy to see Veronica?"
    mina "I am, but don't put words in my--"
    scene w3_10542 with dissolve
    mc "I need to go to the bathroom."
    "Playing mama bird, I pushed Mina out of the proverbial nest with a conspiratorial wink."
    mina "Ah..."
    scene w3_10543 with dissolve
    "Its possible it won't go anywhere, but Sink or swim, it was in her hands."
    "Or, more likely, {i}Veronica's{/i}. Something about throwing this sweet young thing to that wolf turned me the fuck on."
    scene w3_10544 with dissolve
    ver "What's with that look, [mcf]?"
    scene w3_10545 with dissolve
    mc "Uh, this is the face I make when I'm about to piss myself?"
    scene w3_10544 with dissolve
    ver "Go to the bathroom!"
    stop music fadeout 3.0
    stop ambient fadeout 3.0
    scene black with fade
    "I left the two alone."
    jump w3RockShowBathroomBreak


label w3RockShowBathroomBreak:
    if w3VeronicaMinaLezPush == True:
        "I had used it as an excuse, but I really did have to piss."

    play music "music/outreach.ogg"
    if w3RockShowIanTalk == True:
        scene w3_10546 with dissolve
        "Coming out of the restroom, I was mobbed by a familiar face."
        kil "...did you ask her?"
        scene w3_10548 with dissolve
        "To my partial surprise, the first thing out of Ian's mouth was about Mina."
        scene w3_10551 with dissolve
        mc "Not yet."
        scene w3_10548 with dissolve

        if w3IanMinaTalk == False:
            "And I didn't really plan to, if I was being honest..."
        else:
            "I had promised, but..."

        scene w3_10552 with dissolve
        mc "She's having a good time. I'm not keen on killing the mood."
        scene w3_10553 with dissolve
        kil "...yeah. Uh... maybe it's too soon?"
        scene w3_10554 with dissolve
        mc "We'll just have to see if the chance comes up, eh? Or are you getting cold feet?"
        scene w3_10555 with dissolve
        mc "Ha! Where the fuck is my friend?"
        scene w3_10556 with dissolve
        kil "..."

    elif ianIntrospect == True and w3RockShowIanTalk == False:
        scene w3_10547 with dissolve
        "Coming out of the restroom, I was mobbed by a familiar face."
        mc "...hey, man. What were you doing just sitting around earlier? Don't tell me no one here tickles your pickle."
        mc "You seen the bartender?!"
        scene w3_10549 with dissolve
        kil "Ah, you know... you don't have to pick up chicks to have a good time. I'm just vibing."
        scene w3_10552 with dissolve
        mc "You don't? Who are you and what did you do to Killian Beaufort?"
        scene w3_10557 with dissolve
        kil "Ha, fuck you, dude! I actually..."
    else:
        scene w3_10547 with dissolve
        "Coming out of the restroom, I was mobbed by a familiar face."
        mc "...any luck out there? I saw you talking to a couple of chicks."
        scene w3_10550 with dissolve
        kil "Eh, they weren't buying my bullshit."
        scene w3_10551 with dissolve
        mc "Love the self-awareness."
        scene w3_10557 with dissolve
        kil "Ha, fuck you, dude! I actually..."

    scene w3_10558 with dissolve
    kil "Oh shit! I just remembered something. Have you talked to your mom?"
    scene w3_10559 with dissolve
    mc "...no. Why do you ask?"
    scene w3_10560 with dissolve
    kil "Alice said she saw her today at the summer home."
    scene w3_10561 with dissolve
    mc "Yeah, she told me about that yesterday. They were having lunch."
    scene w3_10560 with dissolve
    kil "That's pretty fuckin' weird, isn't it?"
    scene w3_10561 with dissolve
    mc "I dunno. Maybe your mom seeing me last week got her all nostalgic?"
    scene w3_10562 with dissolve
    kil "Fat fucking chance."
    scene w3_10563 with dissolve
    mc "...yeah, {b}fat fuckin' chance.{/b}"

    if w3IanDealReveal == True:
        "I {i}had{/i} told Ian about the deal she offered me, and I had a suspicion it was related to that, but I wasn't going to haphazardly lob that into his lap. No sense in pissing him off without confirmation."
    else:
        "She and I had some shared suspicions, but... I never told Ian about the deal. Maybe I should, but I wasn't about to now, in the middle of a rock club. {i}No way.{/i}"

    scene w3_10565 with dissolve
    mc "I haven't talked to her today, but I'll ask her how it went later and give you a call."
    scene w3_10564 with dissolve
    kil "Sure, but... here's the thing... Alice said when she came back from forgetting something that Vicky was pale as a ghost."
    scene w3_10565 with dissolve
    mc "Mom's a pale woman..."
    scene w3_10562 with dissolve
    kil "{i}She looked unhappy.{/i}"
    scene w3_10561 with dissolve
    "An irrational feeling took hold of me."
    mc "...is that how she put it exactly? {i}Unhappy?{/i}"
    scene w3_10560 with dissolve
    kil "She used more words."
    scene w3_10561 with dissolve
    "......"
    scene w3_10564 with dissolve
    kil "Ah... you know how my mom is. Vicky may be good at putting up with people's shit, but Mom is an armor-cracking, certified bitch. She probably--"
    scene w3_10565 with dissolve
    mc "No point in speculating, Ian. I'll talk to her."
    scene w3_10566 with dissolve
    kil "And don't forget to tell me how it goes you, prick."
    scene w3_10567 with dissolve
    "......"
    scene w3_10568 with dissolve
    kil "...so, what are you going to do in the meantime? Back to Mina?"

    if w3HanaFriendEncourage == True:
        scene w3_10569 with dissolve
        mc "Probably get a drink and watch Hana, or-- {i}Oh!{/i}"
        scene w3_10570 with dissolve
        mc "Hey!"
        cyn "...?"
        mc "The music therapist!"
        scene w3_10571 with dissolve
        cyn "Ah! Hana's boyfriend, uh--"
        scene w3_10572 with dissolve
        mc "[mcf]."
        scene w3_10573 with dissolve
        cyn "I was going to say that!"
        scene w3_10572 with dissolve
        mc "Enjoying the show?"
        scene w3_10574 with dissolve
        cyn "Fuck no. This noise makes my ears bleed."
        scene w3_10575 with dissolve
        mc "Then why--"
        scene w3_10576 with dissolve
        cyn "{i}Hana asked.{/i}"
        cyn "I was surprised she got back in touch..."
        scene w3_10577 with dissolve
        "I smiled inwardly at Hana taking my suggestion."
        scene w3_10571 with dissolve
        cyn "...it was nice seeing you. I'd talk more, but my boyfriend is enduring it alone out there."
        scene w3_10572 with dissolve
        mc "Ha! I won't tell Hana you said any of that."
        scene w3_10578 with dissolve
        cyn "*Scoff* Please do. Bitch thinks she's all that."
        "If she wanted that to sound mean, with a smile on her face, she failed."
        scene w3_10579 with fade
        kil "...I didn't know sun-dried tomatoes could speak."
        mc "Pffh! So, what about you?"
        scene w3_10568 with dissolve
        kil "Me what?"
        scene w3_10581 with dissolve
        mc "What are you going to do? Skulk about?"
    else:

        scene w3_10580 with dissolve
        "Probably get a drink and watch Hana."
        scene w3_10581 with dissolve
        mc "What about you? You going to skulk about?"

    scene w3_10582 with dissolve
    kil "I'll probably hang out with Jacob. Turn this into a boys' night, attract some chicks for him."
    kil "{i}Dude's lost without me.{/i}"
    scene w3_10581 with dissolve
    mc "Haha, yeah. {i}Right.{/i}"
    scene w3_10568 with dissolve
    kil "You're welcome to join us."
    scene w3_10581 with dissolve
    mc "I'll think about it."
    stop music fadeout 3.0
    scene black with fade
    "...but first, a beer."
    play music "music/positioned.ogg"
    if w3VeronicaMinaLezPush == True:
        jump w3RockShowMinaVeronicaLift
    else:
        play ambient "sound effects/rock-crowd-floor-ambience.wav"
        jump w3RockShowEdwinWhatDo


label w3RockShowMinaVeronicaLift:
    play ambient "sound effects/rock-crowd-floor-ambience.wav"
    mina "...w-woaah! E-easy does-"
    ver "Relax, relaaaaax, you're in good hands."
    mina "No, no, your hands-- {b}o-oh!{/b}"
    scene w3_10583 with wipeleft
    mina "Hahaha, I'm the queen of the world!"
    ver "See? I told you I could do it no problem!"
    scene w3_10584 with dissolve
    mina "I didn't doubt you, it's just, d-don't drop me!"
    ver "Afraid of heights?"
    mina "Kiiiiiiinda."
    scene w3_10585 with hpunch
    mina "W-woah, w-woahh-!"
    ver "I 'spose we better work on that."
    scene w3_10586 with dissolve
    mina "Not funny!"
    ver "Wave hi to the band! You have the best view in the house!"
    scene w3_10587 with dissolve
    mina "Oh, yeeeeah, Haaaaaaaana! Hey! {b}Woooooo!{/b}"
    scene w3_10588 with dissolve
    mina "--?!"
    scene w3_10589 with dissolve
    mina "--! --!"
    scene w3_10590 with dissolve
    mina "She saw me! She saw me!"
    ver "Haha, you get easily excited!"
    scene w3_10591 with dissolve
    mina "You good down there?"
    ver "Of course I am! I could do this all day! Cheer your fuckin' head off, cutie!"
    scene w3_10592 with dissolve
    mina "Yeeeeah! Woooooooooah!"
    ver "With more feeling!"
    mina "{b}HAAAAAAAAAAAANAAAAAAAAAAAAAAAA!{/b}"
    scene black with fade
    mina "Wooooooooooooooooooooooooooooooooooooooooooohhh--"
    jump w3RockShowEdwinWhatDo


label w3RockShowEdwinWhatDo:
    scene black with fade
    m_dev "Recommended to make another save here to try different paths"
    if w3VeronicaMinaLezPush == True:
        scene w3_10593 with dissolve
        mina "Wooooooooooooooooooooooooooooooooooooooooooohhh--"
        "An unmistakable cry pierced the room."
        mct "(She's having fun...)"
        scene w3_10594 with dissolve
        "......"
        "...where did that leave me?"
        "I had committed to giving them some space, that meant I had some free time on my hands..."
        scene w3_10595 with dissolve
        "With a quick glance about the room, I sized up my options."
        scene w3_10596 with dissolve
        "Rosalind was looking positively bored. No surprise there; I dragged her to this, and Felicia hadn't even turned up. All-in-all a pointless exercise in will..."
        "I could go keep her company..."
        scene w3_10597 with dissolve

        menu:
            "Rosalind {i}does{/i} look lonely. (Rose path)":
                $ w3RockShowRosaPath = True
                jump w3RockShowRosaBored
            "Think of something else to do. (option for other girls path)":
                pass

        mct "(Eh, she's probably sick of me by this point.)"

        if feliciaFlag == True:
            scene w3_11023 with dissolve
            "Thinking of Felicia, she did say she'd try to make it. Should I give her a call?"

            menu:
                "Give Felicia a ring. (Felicia path)":
                    $ w3RockShowFeliciaPath = True
                    jump w3RockShowFeliciaCall
                "Keep scanning the room. (option to lead to others paths)":
                    pass

            scene w3_11024 with dissolve
            "Nah. She said she was staying in with Elias. If she's gonna be here, she'll be here. Calling her would just be an annoyance."

        "Next I scanned for Ian. He said he and Jacob..."
        scene w3_10598 with dissolve
        "There they are, just the two of 'em. Should I go add another sausage into the mix?"

        menu:
            "...naaaaaah. Find something else to do. (option to lead to others paths)":
                pass
            "Bro it up. (Killians path":
                $ w3RockShowBroPath = True
                jump w3RockShowBroTime

        "Welp, with Mina and Veronica occupied, that leaves..."

        scene w3_10600 with dissolve
        if hanaGF == True:
            "I can just go cheer my ass off for my girlfriend. I mean come on, what else am I here for?"
        else:
            "I can just go cheer my ass off for Hana. It's why I'm here, after all."

        if w3RockShowIanTalk == False and hanaGF == False:
            scene w3_10601 with dissolve
            mct "(Although...)"

            menu:
                "{color=#FF1493}[[Flirt]{/color} Chat up the bartender. (Bartender Path)":
                    $ w3RockShowBartenderPath = True
                    jump w3RockShowBartenderDive
                "Cheer for Hana. (Hana path)":
                    $ w3RockShowHanaPath = True
                    jump w3RockShowHanaCheer
        else:
            $ w3RockShowHanaPath = True
            jump w3RockShowHanaCheer
    else:

        scene w3_10594 with dissolve
        mct "(Hmmm...)"
        "No idea how long Hana will be playing for."
        scene w3_10595 with dissolve
        "With a quick glance about the room, I sized up my options on how to spend my time."
        scene w3_10596 with dissolve
        "Rosalind was looking positively bored. No surprise there; I dragged her to this, and Felicia hadn't even turned up. All-in-all a pointless exercise in will..."
        "I could go keep her company..."
        scene w3_10597 with dissolve

        menu:
            "Rosalind {i}does{/i} look lonely. (Rose path)":
                $ w3RockShowRosaPath = True
                jump w3RockShowRosaBored
            "Think of something else to do. (option for other girls path)":
                pass

        mct "(Eh, she's probably sick of me by this point.)"
        "Wonder what the other Carnation is doing, she's..."
        scene w3_10602 with dissolve
        "{i}Dancing.{/i}"

        if w3VeronicaSex == True:
            "I could go join her. I was a pretty good dance partner, wasn't I?"

            menu:
                "Go hang out with Veronica. (Veronica path)":
                    $ w3RockShowVeronicaPath = True
                    jump w3RockShowVeroHang
                "Find something else to do. (option to lead to others paths)":
                    "I'll leave her to that."
        else:
            "I'll let her have some fun without me."


        scene w3_11023 with dissolve
        if feliciaFlag == True:
            scene w3_11023 with dissolve
            "Thinking of Felicia, she did say she'd try to make it. Should I give her a call?"

            menu:
                "Give Felicia a ring. (Felicia Path)":
                    $ w3RockShowFeliciaPath = True
                    jump w3RockShowFeliciaCall
                "Keep scanning the room (option to lead to others paths)":
                    pass

            scene w3_11024 with dissolve
            "Nah. She said she was staying with Elias. If she's gonna be here, she'll be here. Calling her would just be an annoyance."

        "Next I scanned for Ian. He said he and Jacob..."
        scene w3_10599 with dissolve
        "There they are, just the two of 'em. Should I go add another sausage into the mix?"

        menu:
            "...naaaaaah. Find something else to do. (option to lead to others paths)":
                pass
            "Bro it up. (Killians path":
                $ w3RockShowBroPath = True
                jump w3RockShowBroTime

        "Eh. I've seen enough of that fuck."
        scene w3_10603 with dissolve
        if hanaGF == True:
            "Honestly, I should probably just go back to Mina and cheer for my girlfriend. It's why I'm here in the first place."
        else:
            "Honestly, I should probably just go back to Mina and cheer for Hana. It's why I'm here in the first place."

        if w3RockShowIanTalk == False and hanaGF == False:
            scene w3_10601 with dissolve
            mct "(Although...)"

            menu:
                "{color=#FF1493}[[Flirt]{/color} Chat up the bartender. (bartender path)":
                    $ w3RockShowBartenderPath = True
                    jump w3RockShowBartenderDive
                "Rejoin Mina. (Hana and Mina Path)":
                    $ w3RockShowMinaHanaPath = True
                    jump w3RockShowMinaHanaCheer
        else:
            $ w3RockShowMinaHanaPath = True
            jump w3RockShowMinaHanaCheer


label w3RockShowRosaBored:
    scene black with fade
    "..."
    scene w3_10604 with wipeleft
    mc "...I take it this isn't your kind of scene."
    scene w3_10605 with dissolve
    rose "You'd be surprised."
    scene w3_10604 with dissolve
    mc "...uh, would I?"
    scene w3_10606 with dissolve
    rose "{b}No{/b}, you wouldn't be! And that doesn't make me old, okay?"
    scene w3_10607 with dissolve
    mc "Sorry for dragging you out."
    scene w3_10608 with dissolve
    rose "I noticed Felicia isn't here. Your dumbass comradery building didn't last very long."
    scene w3_10609 with dissolve
    mc "She said she'd try to make it."
    scene w3_10608 with dissolve
    rose "I don't really care if she does. We aren't friends."
    scene w3_10609 with dissolve
    mc "No, I suppose you're not..."
    scene w3_10610 with dissolve
    "......"
    scene w3_10611 with dissolve
    rose "...sorry about leaving unannounced. I really was just getting out of your hair. I appreciate--"
    scene w3_10612 with dissolve
    mc "Ah, it's been all said. Besides, I left you alone. Were you happy to get home?"
    scene w3_10611 with dissolve
    rose "The house was as empty as I left it."

    if w3RosalindInviteStay == True:
        scene w3_10604 with dissolve
        mc "The offer to stay with me as long as you want still stands."
        scene w3_10611 with dissolve
        rose "I know it does."
        scene w3_10610 with dissolve
        "She left it at that."
    else:
        scene w3_10610 with dissolve
        "......"

    scene w3_10609 with dissolve
    mc "...so, how many of those have you had?"
    scene w3_10608 with dissolve
    rose "Shut up! I don't want a lecture."
    scene w3_10607 with dissolve
    mc "I'm just asking."
    scene w3_10608 with dissolve
    rose "Just the one."
    scene w3_10609 with dissolve
    mc "Not counting what you drank before you got here--"
    scene w3_10605 with dissolve
    rose "Shut up!"
    scene w3_10604 with dissolve
    mc "...can I buy you another one?"
    scene w3_10613 with dissolve
    "......"
    scene w3_10614 with dissolve
    rose "Please do! They're too expensive! I mean, how is this place so grungy with these prices?!"
    scene w3_10615 with dissolve
    mc "Come. Let's go to the bar."
    scene black with fade
    "This was one way to build morale."
    scene w3_10616 with fade
    mc "Cheers!"
    rose "Heh, this is twice in just as many nights that you and I are drinking like this."
    scene w3_10617 with dissolve
    rose "*Glug, glug, glug~*"
    scene w3_10618 with dissolve
    rose "Ah. That's good."
    scene w3_10619 with dissolve
    rose "*Glug, glug~*"
    scene w3_10620 with dissolve
    rose "That. {i}Is.{/i} Good. Pwwwwahh!"
    scene w3_10621 with dissolve
    mc "Impressive..."
    scene w3_10622 with dissolve
    mc "I wouldn't advise it, but drink as much as you want."
    rose "Oh, yeah...?"
    scene w3_10623 with dissolve
    rose "Yoink! Must be nice."
    mc "What is?"
    scene w3_10624 with dissolve
    rose "Saying shit like that."
    scene w3_10625 with dissolve
    mc "You complainin'?"
    scene w3_10624 with dissolve
    rose "Noooooooooooooo, {b}sir.{/b}"
    scene w3_10626 with dissolve
    "I watched her again devour the bottle, this time taking it halfway."
    scene w3_10627 with dissolve
    rose "Ugh, my head. Okay, there's diminishing returns on the taste. Watered-down beer is still watered-down beer."
    scene w3_10628 with dissolve
    bar "Hey!"
    scene w3_10629 with dissolve
    rose "What?!"
    scene w3_10628 with dissolve
    bar "Fair! But say that shit away from the bar!"
    scene w3_10629 with dissolve
    rose "Bah! It's a free country!"
    scene w3_10630 with dissolve
    rose "........."
    bar "......"
    scene w3_10631 with dissolve
    rose "...she's letting loose."
    if w3VeronicaMinaLezPush == True:
        scene w3_10632 with dissolve
        "{i}She was referring to her competitor.{/i}"
        "Veronica was jumping and banging her head, and Mina tentatively followed her example."
        "I leered at the pair for a moment, watching Mina as she gradually grew more comfortable with the rhythm."
        "{i}Better than I would.{/i} Not to this music."
        scene w3_10633 with dissolve
        "After waiting a bit, and allowing Mina's shyness to naturally melt away, Veronica put her hands around the ball of energy's waist and ground her dance partner's tempo to a crawl."
    else:
        scene w3_10634 with dissolve
        "{i}She was referring to her competitor.{/i}"
        "Veronica was right where I last saw her, jumping and banging her head like she belonged."
        "The people around her bumped into her, but the large woman didn't mind. She made her own space, following the discordant rhythm far better than I ever could."

    scene w3_10635 with dissolve
    mc "...seems that way. Want to join her?"
    rose "{i}No.{/i} For all I know..."
    scene w3_10636 with dissolve
    rose "We'll be back-to-back tomorrow night, guzzling down cum and spitting in each other's face."
    "Drunk Rosalind was proving to be a couple of things. One: extremely blunt and colorful, and two..."
    scene w3_10637 with dissolve
    mc "I didn't figure. Music aside..."
    "With the kerfuffle at the door in mind, I aimed low."
    mc "You don't look like you like to dance."
    scene w3_10638 with dissolve
    rose "I like to dance just fine, thank you very much! In fact, I love to!"
    scene w3_10639 with dissolve
    mc "...oh, you do?"
    "And two, drunk Rosalind proved easily provoked."
    scene w3_10640 with dissolve
    rose "Before I got married, I used to go out dancing every week in college! And even a little bit after that!"
    scene w3_10641 with dissolve
    mc "{i}Really?{/i} That's surprising."
    "I mustered every bit of {i}smug{/i} into that claim."
    scene w3_10642 with dissolve
    rose "You don't believe me?!"
    scene w3_10643 with dissolve
    mc "No, uh... I... {i}I believe you.{/i}"
    scene w3_10644 with dissolve
    rose "Arrr! Buy me a beer!"
    mc "Okay, but finish that one first--"

    if w3VeronicaMinaLezPush == True:
        jump w3RockShowVeroMinaGetPersonal
    else:
        jump w3RockShowRosalindDance

label w3RockShowBroTime:
    scene black with fade
    "..."
    scene w3_10645 with wipeleft
    mc "Whaddup boys?"

    if w3HanaDP >= 4:
        scene w3_10646 with dissolve
        jacob "Not cheerin' for your girl?"
        scene w3_10645 with dissolve
        mc "Thought I'd take a load off."
        scene w3_10647 with dissolve
        jacob "Then sit down, my man!"
    else:

        scene w3_10647 with dissolve
        jacob "Oh, you know: listening to this asshole. Sit down!"

    scene w3_10648 with dissolve
    mc "Don't mind if I do."
    scene w3_10649 with dissolve
    mc "How's life treatin' you, Jacob?"
    scene w3_10650 with dissolve
    jacob "Can't complain."

    if w3RosalindViolentSolution == True:
        scene w3_10649 with dissolve
        mc "I heard you took \"care\" of that loan shark."
        scene w3_10651 with dissolve
        jacob "What are you {i}talking{/i} about?"
        mc "...right, yeah, sorry."

    scene w3_10649 with dissolve
    mc "How's Emma?"
    scene w3_10650 with dissolve
    jacob "She's alright. Good of you to ask."
    scene w3_10649 with dissolve
    mc "She working?"
    scene w3_10650 with dissolve
    jacob "Uh huh."
    scene w3_10649 with dissolve
    mc "Shame. You two could've had a date."
    scene w3_10652 with dissolve
    jacob "We're not like {i}that.{/i}"
    scene w3_10653 with dissolve
    mc "No?"
    scene w3_10652 with dissolve
    jacob "Better to keep that sort of thing inside the club's walls."
    scene w3_10654 with dissolve
    kil "She's his work wife."
    mc "Ha ha, really?"
    scene w3_10650 with dissolve
    jacob "She likes to bring me a sausage and egg biscuit every morning!"
    scene w3_10649 with dissolve
    mc "Lucky you, but you really don't want to hang out with her outside the club?"
    scene w3_10650 with dissolve
    jacob "Never bring work home."
    scene w3_10649 with dissolve
    mc "You live at the club, though?"
    scene w3_10652 with dissolve
    jacob "She doesn't. She's got her own shit out there. Best not to confound that."
    scene w3_10655 with dissolve
    kil "Sounds like a fuckin' excuse to me. You're just afraid to make that jump."
    scene w3_10656 with dissolve
    jacob "What the hell do you know about that, Casanova?"
    mc "Yeah, {i}Mr. Careful-Around-The-Whores.{/i}"
    scene w3_10657 with dissolve
    kil "You, {b}yeah.{/b} Jacob's got more sense than you!"
    kil "You find something good in this world, you should go at it 110 percent."
    scene w3_10650 with dissolve
    jacob "What the fuck is this guy saying? He had an epiphany?"
    scene w3_10658 with dissolve
    mc "See that blonde over there?"

    if w3VeronicaMinaLezPush == True:
        scene w3_10632 with dissolve
        jacob "The one dancing with Veronica?"
        mc "She dumped his ass for cheating."
        "While I pointed Mina out to Jacob, I peered at the pair for a moment."
        jacob "No shit, that's Mina, huh?"
        "Veronica was jumping and banging her head, and Mina tentatively followed her example, gradually growing more comfortable with the rhythm."
        jacob "Ha! Good for her!"
        scene w3_10633 with dissolve
        "After waiting a bit, and allowing Mina's shyness to naturally melt away, Veronica put her hands around the ball of energy's waist and ground her dance partner's tempo to a crawl."
        kil "Eh? What the fuck is Red doing? They know each other...?"
        "{i}I ignored his question{/i}."
    else:
        scene w3_10603 with dissolve
        jacob "That ten out of 10?"
        mc "She dumped his ass for cheating."
        jacob "No shit, that's Mina, huh?"
        "......"

    scene w3_10659 with dissolve
    jacob "I always thought it was crazy you had a serious girlfriend."
    kil "I'm not talking about it. {b}None{/b} of us are monogamy material."
    scene w3_10660 with dissolve
    jacob "Ha! Here, here!"
    "I didn't care enough to agree or disagree with the sentiment, I just raised my beer."
    scene w3_10661 with dissolve
    harp "Oh, there you guys are."
    scene w3_10662 with dissolve

    if hanaFlag == True:
        "Like last time, Harper was here."

    jacob "Harper! Nico!"
    scene w3_10663 with dissolve
    nico "Hey, uh--"
    jacob "Jacob."
    nico "Right, yeah..."
    scene w3_10664 with dissolve
    mc "Is the whole house going to drop by?"
    harp "Nah, just the two of us; I told Nico about the show and she said she knew somebody that worked here. Wanted to tag along."
    scene w3_10665 with dissolve
    nico "That and I'm in need of a night out -- ah, {i}there's my friend.{/i}"
    scene w3_10666 with dissolve
    nico "See you guys around."
    scene w3_10667 with dissolve
    jacob "Standoffish gal, isn't she?"
    harp "Been through a lot before she landed at the club."
    scene w3_10668 with dissolve
    jacob "Shit, girl. Don't tell me you workin' her too?"
    scene w3_10669 with dissolve
    harp "Wouldn't you like to know?"
    scene w3_10670 with dissolve
    jacob "Pff, that's a no! Not fresh-faced enough, and your charm is only good for so much."
    harp "Hey, fuck you, Jacob!"
    jacob "Anytime you wish, baby!"
    scene w3_10671 with dissolve
    harp "Get me a drink?"
    scene w3_10672 with dissolve
    mc "Me? I just sat down."
    "{i}And since when was she comfortable around me?{/i}"
    scene w3_10671 with dissolve
    harp "Cooome on? I want to go cheer on Hana, and I don't want to ask those two assholes for one."
    scene w3_10673 with dissolve
    mc "...alright, fine."

    if w2HarpRainCheck == True:
        harp "Thanks! Just {i}another{/i} thing I'll owe you for, huh?"
        stop music fadeout 3.0
        scene black with fade
        harp "FYI, cash out any time you'd like"
    else:
        harp "Don't worry. I'll pay you back."
        stop music fadeout 3.0
        scene black with fade
        harp "Unlike some whores, I'm good for it."

    if w3VeronicaMinaLezPush == True:
        jump w3RockShowVeroMinaGetPersonal
    else:
        jump w3RockShowNicoBartender


label w3RockShowHanaCheer:
    scene black with fade
    "Leaving Mina to Veronica's devices, I pointed my compass to the stage, pushing my way to the front row."

    scene w3_10674 with cmet
    if hanaGF == True:
        "I would put my all into screaming for my girlfriend."
    elif w3HanaDP >= 4:
        "I would put my all into screaming for my lover."
    else:
        "I would put my all into screaming for my friend."

    "There was no hope she'd hear me over the clamor of her drum set, but I nevertheless shouted, hooted, and hollered."
    scene w3_10675 with dissolve
    "I stretched my body out as far as I could: standing tall, thrashing, and otherwise moving my bones to the bombastic beats and muddied tones of {i}Eros Massacre.{/i}"
    "Not my tune, but it was easy enough to trick myself. I mean, how fuckin' cool was it that Hana was on stage?"
    scene w3_10674 with dissolve
    mc "Wooooooo! Yeeeeeah! {b}Woooyyeeeeah!{/b}"
    scene w3_10632 with dissolve
    "A quick glance showed Mina doing the same, albeit with a bit more distraction."
    "Veronica was jumping and banging her head, and Mina tentatively followed her example."
    "I leered at the pair for a moment, watching Mina as she gradually grew more comfortable letting go."
    scene w3_10633 with dissolve
    "After waiting a bit, and allowing Mina's shyness to naturally melt away, Veronica put her hands around the ball of energy's waist and ground her dance partner's tempo to a crawl."
    mct "(That's going well...)"

    if hanaFlag == True:
        scene w3_10676 with dissolve
        jer "Heeeeeeey!"
        scene w3_10677 with dissolve
        "Back in my neck of the crowd, {i}I got noticed.{/i}"
        scene w3_10676 with dissolve
        jer "It's fuckin' [mcf]!"
        scene w3_10677 with dissolve
        mc "Yep! That's me!"
        "I doubt she heard me, but she paid close attention to my expression."

        scene w3_10678 with dissolve
        if w3HanaDP >= 4:
            jer "Haha, that's our drummer's boy toy, everyone!"
        else:
            jer "Look at you! Cheering like you're our number one fan!"

        scene w3_10679 with dissolve
        crowd "Haawwwhhooo!"
        scene w3_10678 with dissolve
        jer "Get the fuck up here!"
        scene w3_10679 with dissolve
        mc "Huh?! I don't--"
        scene w3_10678 with dissolve
        jer "Come on, you pussy!"
        scene w3_10680 with dissolve
        crowd "Yeeeahhh! Get-- there!"
        "Jerrica redirected the crowd's attention on me, a reality that would perhaps make the old me blanche but--"
        mc "Ah, fuck it! Help me up!"
        stop music fadeout 3.0
        scene black with fade
        "The old me hadn't fucked on stage yet. {b}Fake it until you make it, mother fucker!{/b}"
    else:

        scene w3_10675 with dissolve
        "Well, then, all that was left for me to do was scream my lungs out."
        scene w3_10674 with dissolve
        mc "Let's fucking {b}GOOOOOOOOOOOOOOOOOOOOO--!{/b}"

    jump w3RockShowVeroMinaGetPersonal


label w3RockShowBartenderDive:
    scene w3_10681 with dissolve
    mc "Hey, lemme ask you something."
    scene w3_10682 with dissolve
    "A whim hit me, and before I knew it, I followed it with a surprising level of confidence."
    scene w3_10681 with dissolve
    mc "How many people have flirted with you tonight?"
    scene w3_10683 with dissolve
    bar "Oh? I don't know. That's like asking me how many drinks have I poured."
    scene w3_10684 with dissolve
    "She was beautiful, of course, but I was used to beautiful women and part of me wanted to learn more about August."
    scene w3_10685 with dissolve
    mc "I guess if we wanted a concrete answer, you'd have to count your tips."
    scene w3_10686 with dissolve
    bar "Ha! Everyone here is a cheap skate!"
    scene w3_10685 with dissolve
    mc "Probably because you charge $7 for a bottle of beer."
    scene w3_10687 with dissolve
    bar "I don't charge it. I just fetch it out of the fridge or work the tap."
    scene w3_10688 with dissolve
    mc "How'd she do?"

    if w3VeronicaMinaLezPush == True:
        scene w3_10632 with dissolve
        "I pointed to Veronica."
        bar "Who? The redhead dancing with the blonde? {i}And what?{/i}"
        mc "She was flirting with you earlier. How convinced were you?"
        bar "Three out of ten."
        mc "That low?"
        scene w3_10633 with dissolve
        bar "That's pretty high since I don't bat for women. Not unless--"
        mc "Unless...?"
    else:
        scene w3_10634 with dissolve
        "I pointed to Veronica."
        bar "Who? The dancing redhead? {i}And what?{/i}"
        mc "She was flirting with you earlier. How convinced were you?"
        bar "Three out of ten."
        mc "That low?"
        scene w3_10695 with dissolve
        bar "That's pretty high since I don't bat for women. Not unless--"
        scene w3_10690 with dissolve
        mc "Unless...?"

    scene w3_10689 with dissolve
    bar "Unless nothing."
    scene w3_10690 with dissolve
    mc "I'm [mcf]."
    scene w3_10691 with dissolve
    bart "Eve."
    scene w3_10692 with dissolve
    mc "How'd he do?"
    scene w3_10693 with dissolve
    eve "Tall, dark, and handsome? About a seven."
    mc "Wow!"
    eve "Pretty high, honestly. Considering flirting is how I make my tips."
    scene w3_10690 with dissolve
    mc "{i}Interesting.{/i} And what did he do to earn that seven?"
    scene w3_10691 with dissolve
    eve "He didn't try to flirt with me at all."
    scene w3_10694 with dissolve
    mc "That doesn't make any sense."
    scene w3_10695 with dissolve
    eve "...doesn't it?"
    scene w3_10690 with dissolve
    mc "And how am I doing?"
    scene w3_10691 with dissolve
    eve "Flirting with me?"
    scene w3_10690 with dissolve
    mc "Yeah."
    scene w3_10695 with dissolve
    eve "Heh, {i}cute.{/i} Why don't you tell me..."
    scene w3_10696 with dissolve
    "I gave the bartender a casual look up and down."
    scene w3_10697 with dissolve
    mc "Decent enough for you not to notice you've got a customer."
    scene w3_10698 with dissolve
    eve "O-oh, sorry! What can I get--"
    scene black with fade
    "......"
    "..."
    scene w3_10699 with fade
    "Once everyone was plied with liquor, she returned to me."
    scene w3_10700 with dissolve
    eve "Alright. I'll give you a 7.5."
    scene w3_10701 with dissolve
    mc "Oh, gee, better than the guy who didn't try? That's good to know."
    scene w3_10700 with dissolve
    eve "I have a thing for younger guys..."
    scene w3_10702 with dissolve
    "Well, that partially satisfied my curiosity. My connection with August wasn't making her shy, which meant she must not necessarily fear {i}that{/i} type."
    mc "Interesting..."


    if w3VeronicaMinaLezPush == True:
        scene black with fade
        "..."
        jump w3RockShowVeroMinaGetPersonal
    else:
        scene black with fade
        "..."
        jump w3RockShowBartenderDivePart2


label w3RockShowVeroMinaGetPersonal:
    play music "music/young-squire.ogg"
    scene w3_10703 with wipeleft
    mina "Ah, hey, Veronica? Ah.. haa...! Can we...?"
    ver "Want to go someplace and sit? Chat a little?"
    mina "You read my mind. I think... I think we've cheered our butts off to make Hana happy!"
    scene w3_10704 with dissolve
    ver "She's pretty lucky to have you in her cheer section..."
    mina "Eheh~"

    if w3RockShowHanaPath == True:
        scene w3_10705 with dissolve
        mina "O-oh! Look!"
        scene w3_10706 with dissolve
        mina "[mcf]'s on stage!"
        ver "He's a pretty considerate friend?"
        mina "What do you mean?"
        scene w3_10704 with dissolve
        ver "He made room for you to give me those fashion tips, yeah?"
        mina "Hehe, ah... you have no idea..."
    else:
        ver "I believe you had some fashion tips for me?"
    scene black with fade
    "......"
    scene w3_10707 with fade
    ver "...good for you for trying to get out of your comfort zone. I didn't date until my 20s."
    scene w3_10708 with dissolve
    mina "I find that hard to believe!"
    scene w3_10707 with dissolve
    ver "My dad was strict, and I put all my time and energy into sports, so--"
    scene w3_10709 with dissolve
    mina "Wait, you were a virgin until your--"
    scene w3_10710 with dissolve
    ver "Oh, god no. I just mean I didn't \"properly\" date. Still, I bet you're more advanced than I was at your age even with your all-girls schooling."
    scene w3_10711 with dissolve
    mina "Uh, from that perspective... there is one thing that there was plenty of but I never tried."
    scene w3_10712 with dissolve
    ver "What's that...?"
    scene w3_10711 with dissolve
    mina "With no boys, a lot of girls made do with playing girlfriend-girlfriend."
    scene w3_10712 with dissolve
    ver "You curious about that?"
    scene w3_10711 with dissolve

    if w3FeliciaMinaThreesomeEnd == True:
        mina "...kinda a lot?"
    else:
        mina "A little..."

    scene w3_10713 with dissolve
    ver "Hmmm... let me ask you something: when you look at Hana, what do you feel?"
    scene w3_10714 with dissolve
    mina "Happiness! And hope that we can become better friends!"
    scene w3_10713 with dissolve
    ver "Ha, that's sweet, but I mean... what does it compare to when you look at a hot guy? {i}Physically.{/i}"
    scene w3_10714 with dissolve
    mina "{b}Oh!{/b} Um... it's different?"
    mina "With a hot guy, it's like an instant thing."
    scene w3_10713 with dissolve
    ver "{i}An attraction.{/i}"
    scene w3_10714 with dissolve
    mina "Yeah... but with a beautiful woman, it's more like admiration? Like \"thinking\" about girls doesn't turn me on... but like..."
    scene w3_10715 with dissolve
    mina "Hana's just so cool that I want to be near her and maybe even see other sides to her..."
    scene w3_10716 with dissolve
    ver "They call that a girl crush."
    scene w3_10717 with dissolve
    mina "N-no... it's not like {i}that.{/i}"
    scene w3_10718 with dissolve
    ver "Is it not? That's kinda how it is with me, but reversed with men."
    ver "I wouldn't say I'm attracted to the platonic idea of them, but... get the right mood, the right vibe, {i}the right person{/i}... it can take care of an itch."
    scene w3_10719 with dissolve
    mina "......"
    scene w3_10720 with dissolve
    ver "...say, what do you feel when you look at me?"
    scene w3_10721 with dissolve
    mina "...d-don't ask me that!"
    scene w3_10722 with dissolve
    ver "{i}Tell me.{/i}"
    scene w3_10723 with dissolve
    mina "...ah, you're like something out of a comic book. Big and strong and beautiful..."
    scene w3_10724 with dissolve
    ver "Heh, you like my muscles?"
    scene w3_10725 with dissolve
    mina "Plus, you seem so {i}wise...{/i}"
    scene w3_10726 with dissolve
    ver "Oh, I'm not {i}that{/i} wise."
    mina "That's what a wise woman would say!"
    scene w3_10727 with dissolve
    ver "...{b}shit{/b} you're cute, Mina. I just want to eat you up."
    scene w3_10728 with dissolve
    mina "...why don't you?"
    scene w3_10729 with dissolve
    ver "Ha! That's bold."
    mina "I don't know why I said that, it's just what they say in--"
    scene w3_10730 with dissolve
    ver "If I was five years younger, you're the kind of girl I'd give my left tit to make my wife."
    scene w3_10731 with dissolve
    "........."
    "......"
    scene w3_10732 with dissolve
    ver "...ah, I'm just teasing--"
    scene w3_10733 with dissolve
    ver "--!"
    scene rs_vm_01_a with dissolve
    show rs_vm_01
    "............"
    "........."
    if not persistent.w3VeroMinaKiss:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3VeroMinaKiss = True
    "......"
    scene w3_10734 with dissolve
    mina "...another intrusive thought won. Hehe~"
    scene w3_10735 with dissolve
    ver "I like the way you think..."
    $ renpy.end_replay()

    if w3RockShowRosaPath == True:
        scene w3_10736 with dissolve
        gawk "Wooooah! Fuck yeah?"
        ver "...huh?"
        scene w3_10737 with dissolve
        ver "Holy shit! Why is that old bitch dancing on the bar?!"
        mina "Wait, I know that--"
        jump w3RockShowRosalindDance
    elif w3RockShowHanaPath == True and hanaFlag == True or w3RockShowMinaHanaPath and w3MinaRockShowKiss == False:
        scene w3_10738 with dissolve
        mina "Oh my god! Look at him!"
        jump w3RockShowMCJam
    else:
        scene w3_10734 with dissolve
        mina "L-let's make it twice as nice..."

        if w3RockShowBroPath == True:
            jump w3RockShowNicoBartender
        elif w3RockShowFeliciaPath == True:
            stop ambient fadeout 3.0
            scene black with fade
            play music "music/wanderlust.ogg"
            "..."
            jump w3RockShowFeliciaGreeting
        elif w3RockShowBartenderPath == True:
            jump w3RockShowBartenderDivePart2
        else:
            scene black with fade
            "..."
            jump w3RockShowMCNotSoJam

label w3RockShowRosalindDance:
    $ renpy.music.play("music/young-squire.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    scene rs_rosadance_a with fade
    show rs_rosadance
    mc "I believe you! You can get down from there!"
    "{i}I didn't need a Carnation with a cracked skull on my hands.{/i}"
    rose "Eh?! You wanted me to dance, didn't you?!"
    "Somehow, in my ploy to get Rosalind to go dance with Veronica, I had coaxed out Rosalind's inner Drunk-Aunt persona."
    "Now she was throwing caution to the wind, swaying her hips to and 'fro, and captivating a growing audience."
    gawk "Wooooah! Fuck yeah?"
    rose "Ha! Everyone's looking!"
    nico "Mommy's wild."
    mc "...aren't you embarrassed?!"
    rose "Not really! Not compared to last week! Or the week before!"
    rose "{i}Or what I'll be doing tomorrow!{/i}"
    "Even in a drunken stupor, or especially because of it, Rosalind wasn't a bad dancer."
    nico "Haha, yeah! Take it off!"
    "Of course, her figure was such that any amount of movement was enough to cut an eye-pleasing performance. The forthcoming whistling and cat-calling attested to that."
    mc "Don't encourage her, Nico!"
    scene w3_10739 with dissolve
    mc "Um... sorry about the commotion. "
    scene w3_10740 with dissolve
    bar "People have done worse on this bar."
    scene w3_10741 with dissolve
    mc "What about your liability insurance?"
    scene w3_10742 with dissolve
    bar "Haha! What's that? I--"
    scene w3_10743 with dissolve
    rose "W-woah?!"
    scene w3_10744 with dissolve
    nico "Oh, shi--"
    "My body moved on its own, bringing us onto a collision course and--"

    if perk_strongman == True:
        scene w3_10745 with dissolve
        "150 pounds of dead weight came crashing down on me, and to my own surprise, I held steady."
        rose "A-ahh...? W-ow, [mcf]! Haha, good catch!"
        nico "No shit..."
    else:
        scene w3_10746 with dissolve
        "150 pounds of dead weight came crashing down on me, bringing us to the floor.."
        play sound "sound effects/thud-floor.mp3"
        scene w3_10747 with vpunch
        mc "Ooof!"
        gawk "Haha!"
        bar "O-oh! Are you--"

    scene black with fade
    rose "...why'd you let me do that, [mcf]?!"
    mc "Yeah... {i}my{/i} fault you went \"Coyote Ugly\"..."
    "..."
    scene w3_10748 with dissolve
    rose "W-wooo! Haha...! Head woozy!"
    mc "You good...?"
    scene w3_10749 with dissolve
    "........."
    "......"
    scene w3_10750 with dissolve
    rose "...no. I'm a mess."
    scene w3_10751 with dissolve
    mc "Hey, don't say that. That was... {i}fun?{/i}"
    scene w3_10750 with dissolve
    rose "What good does fun do me?"

    if w3VeronicaMinaLezPush == True:
        scene w3_10752 with dissolve
        ver "What the fuuuuuuck?"
        rose "Oh, {i}God{/i}, it's you."
        scene w3_10753 with dissolve
        ver "Ha, that was {i}something!{/i}, Rosie."
        scene w3_10754 with dissolve
        mina "You two know each other...?"
        scene w3_10755 with dissolve
        mc "Oh, uh... they go to our gym. Lots of people do."
        scene w3_10756 with dissolve
        ver "You should get up there and show her how it's done?"
        mina "I don't--"
        ver "Come on, come on, I'll join you!"
        scene w3_10757 with dissolve
        bar "O-okay, two is a bit much to--"
        "What had I started?"
        scene w3_10758 with dissolve
        bar "You're too tall to--"
        nico "No, no, let her!"
        rose "Oh, God. I don't feel so good. I'm gonna puke--"
    else:

        scene w3_10759 with dissolve
        ver "Bahaha, what? I didn't have that on my bingo card."
        rose "Oh, {i}God{/i}, it's you."
        ver "That's right, it's me!"
        "First Veronica and..."
        scene w3_10760 with dissolve
        "And even Mina was drawn to the site of the commotion."
        mina "Pff, what's going on over here? You two know each other?"
        scene w3_10761 with dissolve
        mc "Oh, uh... they go to the same gym. Lots of people do."
        scene w3_10762 with dissolve
        ver "You know Rosie?"
        mina "We met tonight..."
        ver "That looked fun?"
        scene w3_10763 with dissolve
        mina "Wait, you're not--"
        ver "Why not?"
        rose "Oh, God. I don't feel so good. I'm gonna puke--"

    scene black with fade
    rose "Bleeeeeech~!"
    ver "Oh, shit hold on, I'll take her to the--"
    "......"
    "..."

    if w3VeronicaMinaLezPush == True:
        scene w3_10764 with fade
        mc "Ah, well... well... well... it's us again."
        scene w3_10765 with dissolve
        "Veronica, to Rosalind's chagrin, ushered her to the bathroom to help her refresh."
        scene w3_10766 with dissolve
        mina "So it is... you sure know a lot of people, [mcf]."
        scene w3_10764 with dissolve
        mc "You don't know the half of it, actually. You seemed to be getting on with Veronica."
        scene w3_10767 with dissolve
        mina "Haha, yeah... we uh... *ahem* I kissed her."
        scene w3_10768 with dissolve
        mc "{i}You{/i} took the lead?"
        scene w3_10767 with dissolve
        mina "It's more like I met her 51 percent of the way."
        scene w3_10768 with dissolve
        mc "Oh! You {i}lady killer!{/i}"
        scene w3_10769 with dissolve
        "It was then it occurred to me that I had an even better chance to play wingman. Mr. Byrnes told me the VIP room was ours, but..."

        menu:
            "Suggest Mina and Veronica get away from the crowd. (Mina + Veronica path":
                scene w3_10770 with dissolve
                mc "See that room up there? Hana's dad rented that out."
                mc "I think it'd be a good, {i}quiet{/i} place to talk to get to know Veronica better.."
                scene w3_10771 with dissolve
                mina "Ah... uh..."
                scene w3_10772 with dissolve
                mc "Keep that initiative going, Mina. You're into her, aren't you?"
                scene w3_10773 with dissolve
                "......"
                scene w3_10774 with dissolve
                mina "...y-yeah."
                scene w3_10775 with dissolve
                mc "Then fly, baby bird. The world is yours."
                scene w3_10767 with dissolve
                mina "...pah, *sigh* you're SO dorky!"
                scene w3_10776 with dissolve
                mc "Here she comes..."
                stop music fadeout 3.0
                scene black with fade
                "{i}It took next to no convincing.{/i}"
                "......"
                "..."
                jump w3RockShowVeroMinaVIP
            "...on second thought, Rosalind might like to sit down somewhere away from the noise. (Rose path)":

                "The two were getting on just fine already."
                scene w3_10764 with dissolve
                mc "Keep at it, huh?"
                scene w3_10765 with dissolve
                "Veronica was occupied, but I was the entire reason Rosalind was here. Prioritizing her comfort made the most sense to me."
                scene w3_10764 with dissolve
                mc "Maybe you'll score by the end of the night."
                scene w3_10767 with dissolve
                mina "Ha, yeah... uh.."
                scene w3_10769 with dissolve
                "{i}She was picturing it.{/i}"
                scene w3_10776 with dissolve
                mc "Here she comes..."
                stop music fadeout 3.0
                scene black with fade
                mc "Hey, Rose, let's go to the--"
                "..."
                jump w3RockShowRosaVIP
    else:
        jump w3RockShowRosaVIP


label w3RockShowNicoBartender:
    $ renpy.music.play("music/young-squire.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    scene w3_10777 with fade
    nico "Yeah, like what the fuck is up with that?"
    bar "Pffh, you know how stupid she is."
    scene w3_10778 with dissolve
    nico "I'd say, and then she--"
    scene w3_10779 with dissolve
    nico "...what do you want?"
    scene w3_10780 with dissolve
    mct "(The bartender is who Nico knew, huh...?)"
    scene w3_10781 with dissolve
    mc "Huh? Do you think I'm following you?"
    bar "This is a bar, Letty!"
    scene w3_10782 with dissolve
    nico "I know that! It's just--"

    if w3RockShowIanTalk == False:
        scene w3_10783 with dissolve
        bar "Wait?! You're with the Irish now?!"
        scene w3_10782 with dissolve
        nico "Not exactly, but... it {i}is{/i} true that I've exchanged employers..."
        scene w3_10783 with dissolve
        bar "Huh..."
        scene w3_10784 with dissolve
        nico "I'm tied to a *ahem* hush-hush arrangement..."
        bar "Oh..."
    else:
        scene w3_10785 with dissolve
        bar "Do you two know each other?"
        scene w3_10782 with dissolve
        nico "Sort of."
        scene w3_10786 with dissolve
        "Out of caution, I didn't say anything."
        scene w3_10782 with dissolve
        nico "You see... I'm under new management."
        scene w3_10787 with dissolve
        bar "You mean...?"
        scene w3_10788 with dissolve
        "I followed the bartender's eyes to August."
        bar "The Irish?"
        scene w3_10784 with dissolve
        nico "Not exactly, but it's hush-hush. I can't talk about it."
        bar "Oh..."

    scene w3_10789 with dissolve
    bar "{b}I see.{/b}"
    scene w3_10790 with dissolve
    mc "Anyway, can I get a beer?"
    scene w3_10791 with dissolve
    mc "...Harper's putting me to work."
    scene w3_10792 with dissolve
    nico "...ah, jumped to a conclusion. My bad."
    scene w3_10793 with dissolve
    mc "It's okay. I like how prickly you are. {i}Like a rose.{/i}"
    scene w3_10794 with dissolve
    nico "Oh, god-- *ahem* and--"
    "A rude sound escaped Nicolette's lithe body."
    scene w3_10795 with dissolve
    nico "That was a physical response. The groaning, I mean. Don't blame me--"
    mc "Ha! I brought it on myself with that one."
    nico "*Ahem* So as long as you understand..."
    scene w3_10796 with dissolve
    mc "You don't have much free time, do you?"
    scene w3_10797 with dissolve
    nico "That... no, not lately, no..."
    scene w3_10796 with dissolve
    mc "How do you two know each other?"
    scene w3_10797 with dissolve
    nico "We go aways back..."
    scene w3_10798 with dissolve
    bar "That's the nondescript way of putting it."
    scene w3_10799 with dissolve
    mc "And it's a good enough one for me. Sorry about interrupting your chat."
    scene w3_10800 with dissolve
    bar "Again, it's a bar. Sorry about giving you a weird look."

    if w3RockShowIanTalk == True:
        scene w3_10801 with dissolve
        mc "You know August?"
        scene w3_10802 with dissolve
        bar "It's a small city."
        scene w3_10801 with dissolve
        mc "Huh, I see..."
        scene w3_10802 with dissolve
        bar "You an \"associate\" of his?"
        scene w3_10801 with dissolve
        mc "I know what you're thinking. I'm too handsome to look the part."
        scene w3_10803 with dissolve
        bar "Wow! You're a mind reader!"
        scene w3_10804 with dissolve
        bar "What am I thinking now?"
        scene w3_10805 with dissolve
        mc "Go away and let me catch up with my friend."
        scene w3_10806 with dissolve
        bar "I don't mind you sticking around."
    else:


        scene w3_10801 with dissolve
        mc "Don't be. Whatever you imagined, true or not, I deserve a weird look or two."
        scene w3_10807 with dissolve
        bar "...don't we all? You're in good company."
        scene w3_10808 with dissolve
        nico "Speak for yourself. I'm normal as shit."
        scene w3_10809 with dissolve
        "........."
        "......"
        scene w3_10810 with dissolve
        bar "...couldn't keep a straight face for more than a few seconds after that, could you?"
        scene w3_10811 with dissolve
        nico "I tried."
        scene w3_10812 with dissolve
        mc "I'll get out of your hair."
        bar "You don't have to..."

    scene w3_10813 with dissolve
    nico "You flirty ho..."
    scene w3_10814 with dissolve
    mc "This isn't mine, remember?"
    scene w3_10815 with dissolve
    nico "Why are you playing that whore's gopher?"
    scene w3_10816 with dissolve
    mc "I like to make nice. You should try it sometime."
    scene w3_10817 with dissolve
    "I paused, waiting for a scoff that never came."
    mc "See ya."

    if w3VeronicaMinaLezPush == True:
        scene w3_10818 with fade
        "A quick search of the room confirmed what I wanted to see. Mina and Veronica were getting more than a {i}little{/i} friendly."
        "Suddenly, I remembered August said the VIP room was ours."
        scene black with fade
        "..."
        scene w3_10819 with fade
        "They might make better use of it than me."
        scene w3_10820 with dissolve
        mina "Oh, uhmmmm..."
        mc "Just thought you two might like to talk someplace with less noise."
        scene w3_10821 with dissolve
        ver "That was a {b}fantastic{/b} idea."
        scene w3_10822 with dissolve
        mc "I thought you might be amenable to it."
        scene w3_10823 with dissolve
        mina "Heh... we did never get to those fashion tips..."
        scene black with fade
        "With that taken care of, and one beer delivered, I found my way back to the boys."
        jump w3RockShowVeroMinaVIP
    else:
        scene w3_10824 with fade
        mct "(There she is...)"
        mina "[mcf]! You left me alone!"
        scene w3_10825 with dissolve
        mc "Aha, my bad."
        scene w3_10826 with dissolve
        mc "...want a beer?"
        scene w3_10827 with dissolve
        mina "...yeah! Give me that!"
        stop music fadeout 3.0
        scene black with fade
        "Sorry Harper, I tried."
        "........."
        "......"
        "..."
        jump w3RockShowMusicDone

label w3RockShowBartenderDivePart2:
    scene w3_10828 with fade
    "We talked pleasantly for a few minutes."
    scene w3_10829 with dissolve
    eve "What kind of wheels do you have?"
    scene w3_10830 with dissolve
    mc "We live in the city."
    scene w3_10829 with dissolve
    eve "You don't have a car?"
    scene w3_10830 with dissolve
    mc "Of course I do, but we live in the city, I--"
    scene w3_10831 with dissolve
    nico "Heeeeeey, how--"
    "...thankfully, a familiar voice and face drew both our attentions."
    nico "Ah... you're here, huh?"
    scene w3_10832 with dissolve
    "Saved by the Nico."
    scene w3_10833 with dissolve
    eve "Letty! Wait, you two know each other...?"
    nico "Something like that, I--"
    scene w3_10834 with dissolve
    eve "Don't tell me! You're holed up with the Irish, now?"
    nico "I am... {b}not.{/b}"
    eve "No...?"
    scene w3_10835 with dissolve
    nico "I {i}am{/i} under new management, though. You're not wrong about that... {i}the hush-hush kind.{/i}"
    scene w3_10836 with dissolve
    mc "This is surprising. How do you two know each other?"
    eve "Nicolette is an old roomie from my stint as a cam girl."
    scene w3_10837 with dissolve
    nico "Those were the days..."
    mc "Your cam girl days, huh? I'll have to look that up."
    scene w3_10838 with dissolve
    eve "If you like jerking it to 240p, go ahead."
    scene w3_10839 with dissolve
    nico "And you two are...?"
    mc "Not remotely acquainted. She's been fending off my advances."
    scene w3_10840 with dissolve
    "......"
    scene w3_10841 with dissolve
    eve "...not the Irish, but it {i}is{/i} August Byrnes, Letty?"
    scene w3_10842 with dissolve
    nico "I--"
    scene w3_10843 with dissolve
    mc "She saw who I walked in with."
    scene w3_10842 with dissolve
    nico "I can't give any details--"
    scene w3_10841 with dissolve
    eve "Hush-hush. That worries me..."
    scene w3_10844 with dissolve
    nico "Don't! I'm good and I'm here to party!"
    scene w3_10845 with dissolve
    eve "That I can help with."
    scene w3_10846 with dissolve
    eve "Hey playboy, would you mind--?"
    mc "Already giving you some space to catch up."
    eve "Not so fast."
    scene w3_10847 with dissolve
    mc "Oh...?"
    scene w3_10848 with dissolve
    eve "I was going to ask you to run the bar."
    scene w3_10847 with dissolve
    mc "I don't know how to--"
    scene w3_10848 with dissolve
    eve "If someone asks for a beer give them a beer."
    scene w3_10847 with dissolve
    mc "Okay..."
    scene w3_10848 with dissolve
    eve "If someone asks for a cocktail, give them a beer too."
    scene w3_10847 with dissolve
    mc "I think I can handle that..."
    scene black with fade
    "Somehow, for some reason, it ended up like--"
    scene w3_10849 with fade
    woman "Can I get a-?"
    scene w3_10850 with fade
    man "You're out of mixer or...?"
    scene w3_10851 with fade
    man "Can you put this in a glass--"
    scene black with fade
    "Again, and again, until--"

    if w3VeronicaMinaLezPush == True:
        scene w3_10852 with fade
        ver "What are you doing back there, [mcf]...?"
        scene w3_10853 with dissolve
        mc "Being a student doesn't pay the bills."
        scene w3_10854 with dissolve
        ver "I sympathize..."
        mina "What?! He's joking, what are you doing--"
        scene w3_10855 with dissolve
        mc "You two got pretty close while I was away, huh?"
        scene w3_10856 with dissolve
        mina "H-how can you tell?"
        scene w3_10857 with dissolve
        mc "Let's just say it's a deduction born from my well-honed detective skills..."
        mc "By the way, if you two want to get away from the noise, Hana's dad booked the VIP room."
        mina "Why would we--"
        scene w3_10858 with dissolve
        ver "You can't think of any reason?"
        scene w3_10857 with dissolve
        mina "O-oh... uh... yeah, you never got those fashion tips..."
        scene w3_10859 with dissolve
        mina "What about you? Are you really {i}working?{/i}"
        scene w3_10860 with dissolve
        mc "Don't mind me, I'm having fun."
        scene w3_10861 with dissolve
        mina "Oh, then, uh... one Strawberry--"
        scene w3_10862 with dissolve
        mc "You'll get a beer and you'll like it!"
        scene black with fade
        "......"
        "...his wasn't a bad seat to watch Hana play, or to peak into the VIP--"
        jump w3RockShowVeroMinaVIP
    else:
        scene w3_10863 with fade
        kil "...what the fuck you doin' back there, bro?"
        scene w3_10864 with dissolve
        mc "I was flirting with the bartender."
        scene w3_10865 with dissolve
        jacob "You're kidding..."
        kil "Haha, you fucking simp!"
        scene w3_10866 with dissolve
        eve "He's doing a bang-up job! Thanks [mcf]!"
        scene w3_10867 with dissolve
        mc "And for your information Jacob, I rated higher."
        jacob "Huh? What are you talking about?"
        scene black with fade
        "...and, to be honest, this wasn't a bad seat to watch Hana play."
        jump w3RockShowBartenderPaysOff



label w3RockShowMinaHanaCheer:
    "So that's what I did."
    scene w3_10868 with dissolve
    "Me and Mina, cheering for {i}our{/i} girl, the strands of the Carnation Club unknowingly tethering themselves to the actress."
    mina "Waaah, haa! {b}Yeeeeah!{/b}"
    mct "(She's surrounded, and she doesn't even know...)"

    if w3MinaHotelFucked == True:
        scene w3_10869 with dissolve
        "That didn't matter, though. Hana had found a friend in Mina, and so had I for that matter, as questionable and complicated as it weas."
    else:
        scene w3_10870 with dissolve
        "That didn't matter, though. Hana had found a friend in Mina, and so had I for that matter."

    mc "Woooh, yeeeeah! {b}Wooooaaaaah!{/b}"
    "I joined the boisterous blonde's chorus until my throat felt sore."
    mina "Haha, yeah! Woooooo!"
    scene w3_10871 with dissolve
    "Adding to my earlier rumination was another familiar face."
    mc "Oh, hey!"

    if hanaFlag == True:
        harp "Yeah! Hey!"
    else:
        harp "Good! You came this time!"

    scene w3_10872 with dissolve
    "My mind immediately searched for an explanation of who Harper could be, before Mina had even--"
    mina "Wow! Cool tattoos!"
    harp "Thanks! I like your..."
    scene w3_10873 with dissolve
    harp "Damn! That outfit is killer!"
    mina "O-oh...! Haha, thanks!"
    scene w3_10874 with dissolve
    mc "Mina! This is Harper!"
    mina "Huh?!"
    mc "I said this is Harper!"
    scene w3_10875 with dissolve
    mina "Yeah! That's my name!"
    scene w3_10876 with dissolve
    mc "No! {i}Her{/i} name is Harper! She's a mutual friend of Hana and I!"
    scene w3_10877 with dissolve
    mina "Ooooooh! Hey! We share a name! My last name is--"
    "Harper just looked at Mina with an expression somewhere between confusion and a smile."
    scene w3_10878 with dissolve
    harp "Mina Harper? Like Dracula?"
    mina "No! That's Harker! I'm--"
    scene w3_10879 with dissolve
    "{i}The music was making it impossible to talk.{/i}"
    scene w3_10880 with dissolve
    harp "Is she in the business? I--"
    scene w3_10881 with dissolve
    mc "Let's go get a drink!"
    mina "Oh, uh--"
    scene w3_10882 with dissolve
    mc "See you around, Harp!"
    scene black with fade
    mina "Ha! Uh... You know--"
    scene w3_10883 with wipeleft
    mina "Another interesting person to add to the list! Do you know half the people in here?"
    scene w3_10884 with dissolve
    mc "You know them too now, and besides, she's more Hana's--"
    scene w3_10885 with dissolve
    nico "Oh, hey, it's you. {i}Middle manager guy.{/i}"
    scene w3_10886 with dissolve
    "........."
    "......"
    mct "(...ah, fuck.)"
    scene w3_10887 with dissolve
    mc "So, Mina, this is--"
    stop music fadeout 3.0
    scene black with fade
    "Did she actually invite the whole club?!"
    "......"
    "..."
    play ambient "sound effects/rock-crowd-floor-ambience-muffled.wav"
    play music "music/young-squire.ogg"
    scene w3_10888 with circlewipe
    mina "Haha! Shut up!"
    mc "No, but would you? To get a role, I mean?"
    mina "No! What the hell, [mcf]?!"
    mc "It's just a hypothetical!"
    scene w3_10889 with dissolve
    mina "Who the {b}fuck{/b} do you think I am?"
    scene w3_10890 with dissolve
    "........."
    "......"
    scene w3_10891 with dissolve
    mina "...aha, I'm already buzzed by the second beer."
    mc "Lightweight."
    scene w3_10892 with dissolve
    mina "Ah, haaa....! Hehehe...!"
    scene w3_10893 with dissolve
    mina "I'm glad we could find someplace quiet for a few minutes. I'm enjoying the music, but... ah, I think I'll bring earplugs next time. Save myself from tinnitus..."
    scene w3_10894 with dissolve
    mc "You've got Hana's dad to thank for that. He rented this out."
    scene w3_10895 with dissolve
    mina "Hehe, it's so nice that he's here supporting her! I wish my own dad wasn't so far away..."
    scene w3_10894 with dissolve
    mc "They have a pretty rough relationship, actually..."
    scene w3_10896 with dissolve
    mina "Oh... he's been looking at her with so much love tonight. I figured..."
    scene w3_10897 with dissolve
    mina "......"
    scene w3_10898 with dissolve
    mina "...heh, what's with that purple suit, anyway? Pretty weird!"
    scene w3_10899 with dissolve
    mc "I think he makes it work!"
    mina "You do not!"
    mc "...okay, I think he dresses like a comic book clown."
    scene w3_10900 with dissolve
    mina "Pahaha! But it's cute! In an old man way!"
    mc "Weird or cute, make up your mind!"
    scene w3_10901 with dissolve
    mina "...hmm, so, is he rich?"
    scene w3_10902 with dissolve
    mc "Hana's dad?"
    scene w3_10901 with dissolve
    mina "I've been around rich girls all my life. I don't get that impression from Hana."
    scene w3_10902 with dissolve
    "I hesitated to ask, but..."
    mc "...and what kind of impression do you get from Mr. Byrnes?"
    scene w3_10903 with dissolve
    "I was curious to see the sort of read Mina had on a surface-level meeting with a man like August."
    scene w3_10904 with dissolve
    mina "Hehe, didn't I just say it? Weird?"
    scene w3_10903 with dissolve
    mc "...{i}just{/i} weird?"
    scene w3_10904 with dissolve
    mina "...he skipped in front of the line and Jacob doesn't look like his {i}friend.{/i}"
    scene w3_10902 with dissolve
    mc "Huh..."
    scene w3_10905 with dissolve
    mina "He dresses and smells... uh..."
    scene w3_10906 with dissolve
    mc "...tacky?"
    scene w3_10905 with dissolve
    mina "I don't know how to put it, but you also had a weird vibe when he popped up."
    scene w3_10903 with dissolve
    mc "...he owns a stake in Uncle Chuck's lounge. That vibe you're getting is probably because he's also my boss."
    scene w3_10904 with dissolve
    mina "Haha, that makes sense, then!"
    scene w3_10907 with dissolve

    if hanaFlag == True:
        mc "...to get back to your question, I believe she was raised by her mom. August has money, but she--"
        scene w3_10908 with dissolve
        mina "--she told me the other day her mom's sick?"
        scene w3_10909 with dissolve
        mc "She is. "
    else:

        mc "...to get back to your question, she was raised by her mom. August has money, but she--"
        scene w3_10908 with dissolve
        mina "--she told me the other day her mom's sick?"
        scene w3_10909 with dissolve
        mc "I've heard as much through the grapevine..."

    scene w3_10910 with dissolve
    "......"
    scene w3_10911 with dissolve
    mina "...good to know about her dad, though. I should be careful what I say to Hana if he comes up."
    scene w3_10909 with dissolve
    mc "You know as well as I do she isn't going to care if you say he seems nice. Plus, she did invite him..."
    scene w3_10910 with dissolve
    "......"
    scene w3_10912 with dissolve
    mina "...hehe, I wish she was here right now. I want to talk to her."
    scene w3_10913 with dissolve
    mc "You have the sweetest look on your face."
    scene w3_10914 with dissolve
    mina "What?! I don't!"
    scene w3_10915 with dissolve
    mc "...don't believe me?"
    scene w3_10916 with dissolve
    mc "Hold that expression--"
    mina "I don't need a picture!"
    scene w3_10917 with dissolve
    mc "Haha, alright, alright... don't be self-conscious."
    scene w3_10918 with dissolve
    mc "There'll be time to talk to Hana after the show."

    if Mina_BiCurious >= 3:
        scene w3_10919 with dissolve
        mina "..."
        scene w3_10920 with dissolve
        mc "You've got that look again."
        scene w3_10921 with dissolve
        mina "Take a picture."
        scene black with fade
        mc "...haha, alright."
    else:
        scene w3_10922 with dissolve
        mina "..."
        scene w3_10923 with dissolve
        mc "You've got that look again."
        scene w3_10924 with dissolve
        mina "Take a picture."
        scene black with fade
        mc "...haha, alright."

    play sound "sound effects/camera-phone-shutter.wav"
    "*Click!*"
    scene w3_10925 with fade
    mina "Ah, shoot... I do look happy."
    scene w3_10926 with dissolve
    mc "You couldn't tell by the way you were feeling?"
    scene w3_10927 with dissolve
    mina "It's just I tried really hard not to be an open book that time!"
    scene w3_10926 with dissolve
    mc "You're hopeless in that regard, Mina."
    scene w3_10927 with dissolve
    mina "That doesn't bode well for me as an actress!"
    scene w3_10928 with dissolve
    mc "Bah! You'll do {i}just{/i} fine."
    mina "Hehe... ah..."
    scene w3_10929 with dissolve
    mc "You can turn it on when you really want to."

label w3RockShowMinaKiss:

    if _in_replay:
        play ambient "sound effects/rock-crowd-floor-ambience-muffled.wav"
        play music "music/young-squire.ogg"

    if w3MinaHotelFucked == True:
        scene w3_10930 with dissolve
        "........."
        "......"
        scene w3_10931 with dissolve
        mina "...this kinda feels like a date."
        scene w3_10932 with dissolve
        mc "Being out and about plus alone like this?"
        scene w3_10933 with dissolve
        mina "We haven't really been on one... {i}not properly...{/i} have we?"
        scene w3_10934 with dissolve
        mc "What about the arcade?"
        scene w3_10935 with dissolve
        mina "My brother was there! That doesn't count..."
        scene w3_10934 with dissolve
        mc "...no, {b}that doesn't count.{/b} By the way, how's he doing?"
        scene w3_10935 with dissolve
        mina "{b}Good.{/b} He asked about you."
        scene w3_10934 with dissolve
        mc "What did he say?"
        scene w3_10935 with dissolve
        mina "He asked if you were treating me well. {b}Again.{/b} I told him it wasn't like that."
        scene w3_10934 with dissolve
        mc "...did he believe you?"
        scene w3_10936 with dissolve
        mina "He said, \"yeah, sure\" sarcastically."
        scene w3_10937 with dissolve
        "Mina and I stared at each other, leaving more than that unsaid."
        scene w3_10938 with dissolve
        mina "...what kind of look do I have on my face now?"
        scene w3_10939 with dissolve
        mc "...a drunk one."
        scene w3_10940 with dissolve
        mina "Pffffh! Wanna know what you look like?"
        scene w3_10939 with dissolve
        mc "A nerdy, nondescript, early 20s white dude?"
        scene w3_10938 with dissolve
        mina "You look like you want to kiss me."
        scene w3_10941 with dissolve
        "Every once in awhile, Mina spoke with a confidence and boldness fitting of her appearance."
        mc "Now that you mention it, I--"
        scene w3_10942 with dissolve
        "She shook her head in the negative."
        mc "...no?"
        scene w3_10943 with dissolve
        mina "We should get back down there. I feel bad about not cheering for Hana."
        scene w3_10944 with dissolve
        "Mina's perfume filled my nostrils, and her lips looked extra plump and wet..."
        scene w3_10945 with dissolve
        mc "But it would only take a second..."
        scene w3_10946 with dissolve
        mina "And she's probably missing us by the second!"
        scene w3_10944 with dissolve
        "With desire in her eye, she feigned concern in her voice."
        mct "(She'll do just fine as an actress...)"
        scene w3_10945 with dissolve
        mc "We {i}could{/i} cheer for her up here..."
        scene w3_10947 with dissolve
        mina "Was that your plan for getting me alone, [mcf]? Away from {b}everyone{/b} else?"
        "I gave her a look that said {i}of course not! I'm a gentleman!{/i}"
        scene w3_10945 with dissolve
        mc "You said it yourself. It's been nice getting away from the crowd for a minute."
        scene w3_10943 with dissolve
        mina "The noise, {b}not the crowd...{/b}"
        scene w3_10944 with dissolve
        "It was difficult to resist making a move right then and there. Mina was so close, her skin so flawless and exposed..."
        "{b}I wanted to kiss her,{/b} a desire she wittingly planted with the way she positioned herself."
        scene w3_10948 with dissolve
        mc "You're right. Hana's missing her finest cheerleader."
        mc "We {i}should{/i} get back down there."
        scene w3_10949 with dissolve
        mina "Mmmmhmm..."
        scene w3_10950 with dissolve
        "For a moment, the pretense was dropped. Clear as day, there was something Mina left unexpressed."
        scene w3_10948 with dissolve
        mc "Let's go."
        scene black with fade
        "As we made our way back downstairs, I wondered what that was."
        "Side by side, that urge from earlier did not abate."
        play ambient "sound effects/rock-crowd-stage-loop.wav"
        scene w3_10951 with wipeleft
        "...but had I missed the chance?"
        "Down here, in the crowd, {i}possibly.{/i}"
        mct "(It would be too risky with Ian arou--)"
        "{i}And then it hit me.{/i} Was that it?"
        scene w3_10952 with dissolve
        "The noise, {i}not the crowd...{/i}"
        "Was that what she wanted?"

        if w3MinaJealous == True:
            "I thought of that earlier, rationally irrational feeling. The distaste I felt at the thought of Mina giving that tool hitting on her the time of day."
            "{i}There was an impulse{/i} and--"

            menu:
                "Fuck it! (w3MinaRockShowKiss = True)"(chg=["mina_up3"]):
                    $ Mina_Affection +=3
                    $ w3MinaRockShowKiss = True
                    scene w3_10953 with dissolve
                    mc "Hey, Mina?"
                    mina "Yeah--"
                    stop ambient
                    play music "music/for-time-to-disappear.ogg"
                    scene rs_minakiss_a with dissolve
                    show rs_minakiss
                    "Ian {i}might{/i} see. There was a chance."
                    mina "Mmmhh....?!"

                    if hanaGF == True:
                        "Hana or August, {i}probably not.{/i}"
                        "Either way it was a silly risk to take."
                    else:
                        "{i}There was a risk.{/i}"

                    mina "Mmmh, hhmmm...!"
                    "I hope she was aware of that."
                    mina "Mmmh, mhhh...♥"
                    "This was me staking a claim, showing Mina that I could read her like a book."
                    "........."
                    scene w3_10954 with dissolve
                    "......"
                    play ambient "sound effects/rock-crowd-stage-loop.wav" fadein 3.0
                    scene w3_10955 with dissolve
                    mina "...eheh, what was that for?"
                    scene w3_10956 with dissolve
                    mc "Don't call that douche musician."
                    scene w3_10957 with dissolve
                    mina "Uh, ahah... I hadn't planned on it..."
                    scene w3_10956 with dissolve
                    mc "Good girl."
                    scene w3_10957 with dissolve
                    $ history_mina = "In an impulsive moment, I kissed Mina for all the world to see and asked her not to see another guy. She seemed pleased with my declaration."
                    $ unread_mina = True
                    play sound "sound effects/notification.wav"
                    show bioupdate with dissolve
                    mina "Ah, [mcf]..."
                    $ renpy.end_replay()
                    if not persistent.w3RockshowMinaKiss:
                        play sound "sound effects/notification.wav"
                        show memoryunlock with dissolve
                        $ renpy.pause(3, hard=True)
                        $ persistent.w3RockshowMinaKiss = True

                    menu:
                        "Now, lets cheer for Hana. (Hana + Mina path":
                            scene w3_10956 with dissolve
                            mc "What you say we get closer to the band? Let Hana know we're {i}really{/i} here."
                            scene w3_10959 with dissolve
                            mina "I... heh... I love that idea..."
                            scene w3_10956 with dissolve
                            mc "We'll call this our first date."
                            scene w3_10958 with dissolve
                            mina "O-ohh..."
                            scene w3_10959 with dissolve
                            mina "O-okay, sounds good..."
                            scene black with fade
                            "..."
                            scene w3_10962 with dissolve
                            "So that's what we did. We jumped and shouted, making sure we were seen and heard."

                            if hanaFlag == True:
                                "Hana had our full support, and I--"
                                mc "Woooah, yeeeeeah!"
                                scene w3_10676 with dissolve
                                jer "Hey! It's fuckin' [mcf]!"
                                scene w3_10677 with dissolve
                                mc "Huh?! Me?!"
                                "I doubt she heard me, but she paid close attention to my expression."
                                scene w3_10678 with dissolve
                                jer "Haha, that's our drummer's boy toy, everyone!"

                                if w3MinaTransparent == True:
                                    scene w3_10963 with dissolve
                                    mina "Haha, toy?! Pffh--"
                                else:
                                    $ w3RockShowMinaTransparent = True
                                    scene w3_10964 with dissolve
                                    mina "...?"

                                scene w3_10678 with dissolve
                                jer "Get the fuck up here!"
                                scene w3_10679 with dissolve
                                mc "Huh?! I don't--"
                                scene w3_10678 with dissolve
                                jer "Come on, you pussy!"
                                scene w3_10965 with dissolve
                                crowd "Yeeeahhh! Get-- there!"
                                mina "Yeah, get up there, [mcf]!"
                                mc "Ah, fuck it! Help me up!"
                                jump w3RockShowMCJam
                            else:
                                stop music fadeout 3.0
                                scene black with fade
                                "........."
                                "......"
                                "..."
                                jump w3RockShowMusicDone
                        "Take Mina to the bar. (Mina path":

                            $ w3RockShowMinaBarEnding = True
                            scene w3_10956 with dissolve
                            mc "I know you want to cheer for Hana, but... let's go get some more drinks and talk."
                            scene w3_10957 with dissolve
                            mina "B-but--"
                            scene w3_10956 with dissolve
                            mc "We'll call this our first date."
                            scene w3_10958 with dissolve
                            mina "I, ahh--"
                            scene w3_10959 with dissolve
                            mina "{i}Okay.{/i}"
                            stop music fadeout 3.0
                            scene black with fade
                            "........."
                            "......"
                            "..."
                            jump w3RockShowMusicDone
                "Caution, [mcf]. Caution.":


                    scene w3_10960 with dissolve
                    "Rationality won out."
                    if hanaGF == True:
                        "Not only would Ian witnessing us kissing make a few aspects of my life messy, but there was also Hana and August..."
                    else:
                        "Ian seeing would make a few aspects of my life more messy."

                    "Sorry, Mina, but thankfully you all you gave me was an insanely vague hint..."
                    scene w3_10961 with dissolve
                    mc "Woooah, hhaaaa!"
                    "Instead, I just joined Mina in her chorus."
                    mc "Come on! Let's get to the front of the crowd!"
                    mina "Haha, okay!"
                    scene w3_10962 with dissolve
                    "So that's what we did. We jumped and shouted, making sure we were seen and heard."
                    $ renpy.end_replay()


                    if hanaFlag == True:
                        "Hana had our full support, and I--"
                        mc "Woooah, yeeeeeah!"
                        scene w3_10676 with dissolve
                        jer "Hey! It's fuckin' [mcf]!"
                        scene w3_10677 with dissolve
                        mc "Huh?! Me?!"
                        "I doubt she heard me, but she paid close attention to my expression."
                        scene w3_10678 with dissolve
                        jer "Haha, that's our drummer's boy toy, everyone!"

                        if w3MinaTransparent == True:
                            scene w3_10963 with dissolve
                            mina "Haha, toy?! Pffh--"
                        else:
                            $ w3RockShowMinaTransparent = True
                            scene w3_10964 with dissolve
                            mina "...?"

                        scene w3_10678 with dissolve
                        jer "Get the fuck up here!"
                        scene w3_10679 with dissolve
                        mc "Huh?! I don't--"
                        scene w3_10678 with dissolve
                        jer "Come on, you pussy!"
                        scene w3_10965 with dissolve
                        crowd "Yeeeahhh! Get-- there!"
                        mina "Yeah, get up there, [mcf]!"
                        mc "Ah, fuck it! Help me up!"
                        jump w3RockShowMCJam
                    else:
                        stop music fadeout 3.0
                        scene black with fade
                        "........."
                        "......"
                        "..."
                        jump w3RockShowMusicDone
        else:


            scene w3_10960 with dissolve
            "I considered kissing her, certain that was what she wanted, but I quickly reeled back in that possibility."
            "Ian seeing that would be highly problematic."

            if hanaGF == True:
                "Hana or August... {i}disastrous.{/i}"

            "Sorry, Mina, but thankfully all you gave me was an insanely vague hint..."
            scene w3_10961 with dissolve
            mc "Woooah, hhaaaa!"
            "Instead, I just joined Mina in her chorus."
            mc "Come on! Let's get to the front of the crowd!"
            mina "Haha, okay!"
            scene w3_10962 with dissolve
            "So that's what we did. We jumped and shouted, making sure we were seen and heard."

            if hanaFlag == True:
                "Hana had our full support, and I--"
                mc "Woooah, yeeeeeah!"
                scene w3_10676 with dissolve
                jer "Hey! It's fuckin' [mcf]!"
                scene w3_10677 with dissolve
                mc "Huh?! Me?!"
                "I doubt she heard me, but she paid close attention to my expression."
                scene w3_10678 with dissolve
                jer "Haha, that's our drummer's boy toy, everyone!"

                if w3MinaTransparent == True:
                    scene w3_10963 with dissolve
                    mina "Haha, toy?! Pffh--"
                else:
                    $ w3RockShowMinaTransparent = True
                    scene w3_10964 with dissolve
                    mina "...?"

                scene w3_10678 with dissolve
                jer "Get the fuck up here!"
                scene w3_10679 with dissolve
                mc "Huh?! I don't--"
                scene w3_10678 with dissolve
                jer "Come on, you pussy!"
                scene w3_10965 with dissolve
                crowd "Yeeeahhh! Get-- there!"
                mina "Yeah, get up there, [mcf]!"
                mc "Ah, fuck it! Help me up!"
                jump w3RockShowMCJam
            else:
                stop music fadeout 3.0
                scene black with fade
                "........."
                "......"
                "..."
                jump w3RockShowMusicDone
    else:

        scene w3_10895 with dissolve
        mina "Haha, yeah I can! Anyway, I feel bad about not cheering for Hana. Want to go back down there?"
        scene w3_10894 with dissolve
        mc "You know it. Hana's missing her biggest cheerleaders."
        scene black with fade
        "So. That's what we did, making our way to the front of the crowd."
        scene w3_10962 with fade
        mina "Wooooah!"
        "We jumped and shouted, making sure we were seen and heard."

        if hanaFlag == True:
            mc "{b}Rhhoooououuuuhh!{/b}"
            "Hana had our full support, and I--"
            mc "Woooah, yeeeeeah!"
            scene w3_10676 with dissolve
            jer "Hey! It's fuckin' [mcf]!"
            scene w3_10677 with dissolve
            mc "Huh?! Me?!"
            "I doubt she heard me, but she paid close attention to my expression."
            scene w3_10678 with dissolve
            jer "Haha, that's our drummer's boy toy, everyone!"

            if w3MinaTransparent == True:
                scene w3_10963 with dissolve
                mina "Haha, toy?! Pffh--"
            else:
                scene w3_10964 with dissolve
                mina "...?"

            scene w3_10678 with dissolve
            jer "Get the fuck up here!"
            scene w3_10679 with dissolve
            mc "Huh?! I don't--"
            scene w3_10678 with dissolve
            jer "Come on, you pussy!"
            scene w3_10965 with dissolve
            crowd "Yeeeahhh! Get-- there!"
            mina "Yeah, get up there, [mcf]!"
            mc "Ah, fuck it! Help me up!"
            jump w3RockShowMCJam
        else:
            mc "{b}Let's fucking gooooooooo!{/b}"
            stop music fadeout 3.0
            scene black with fade
            "........."
            "......"
            "..."
            jump w3RockShowMusicDone

label w3RockShowMCJam:
    $ w3RockShowJammed = True
    play music "music/higher-octane.ogg"
    scene w3_10966 with wipeleft
    "The feeling was electric."
    "Face to face with the crowd, under the haze of the stage lights, I couldn't make out a single person."
    "Instead, staring me down, was a single gesticulating entity. A sea of fists, cresting and falling, breaking against the sound of the music."
    "Freezing up here would be akin to drowning, but thankfully..."
    scene w3_10967 with dissolve
    mc "Woooooooooaahwwwaaah!"
    "I wasn't alone."
    hana "Woohhooo! Haha, {b}whooo!{/b}"
    scene w3_10968 with dissolve
    "The cracking of Hana's drums replaced the thoughts in my head, excising the hesitation from my body."
    "Action, sound, I had to do {i}anything{/i} to show that I'm alive."
    mc "Yeeeeah! Wooooo!"
    "Quickly, I lost myself in the noise at my back."
    scene w3_10969 with dissolve
    jer "Wooahh, like a BIIIIITCH leeeeft outttt-- in the rraaaaaiinn!"
    "Jerrica howled like a tortured animal, adding to {i}what ever the fuck this song was.{/i}"
    scene w3_10970 with dissolve
    mc "BIIIIIITCH~ RAAAAAAAAAAIN~!"
    "{i}I joined her, straining my vocal cords like a fucking moron.{/i}"
    scene w3_10971 with dissolve
    jer "Got a set of pipes, eh?!"
    scene w3_10972 with dissolve
    mc "I don't know the lyrics!"
    jer "Haha, me neither, man!"
    scene w3_10973 with dissolve
    mc "What?!"
    jer "Sing something from the heart!"
    mc "Uh..."
    scene w3_10974 with dissolve
    "Goddamn it, [mcf]! Warrior spirit! The best thing to do when put on the spot is not think about how put on the spot you are!"
    scene w3_10975 with dissolve
    jer "Come on! Like a bitch left out in the rain! I--"

    menu:
        "...pain.":
            scene w3_10976 with dissolve
            mc "...I'm soaked to my bone, cold, {b}in pain!{/b}"
            scene w3_10977 with dissolve
            "Somewhere, locked away deep in me, I found some leftover teenager and pelted out the {i}obvious{/i} connection."
            jer "Yeeeah! Bone white, cold night-!"
            "{i}I don't know what the fuck she's on about though.{/i}"
        "...remain.":
            scene w3_10976 with dissolve
            mc "...less, and less, and less of me remaaaaaaains!"
            scene w3_10977 with dissolve
            "I went for the gusto, my out-of-tune singing perfectly at home on this stage."
            jer "Aha! Less, and less- and-"
        "...rogaine.":
            scene w3_10976 with dissolve
            mc "I really could use some ~rogaine!"
            scene w3_10978 with dissolve
            jer "Pffh, huh?! Ahaha--"
            hana "Haha, spider's future!"
            spid "Shut up!"

    scene w3_10979 with dissolve
    "The song carried on. Sensing an opening, I briefly considered getting offstage, but as I willed my muscles to that end--."
    scene w3_10980 with dissolve
    jer "Oh, you're not going anywhere, dork!"
    "...Jerrica kept me in the spotlight."
    mc "Dork...? Fu--"
    scene w3_10981 with dissolve
    jer "Go ahead!"
    scene w3_10982 with dissolve
    mc "{b}...fuck you!{/b}"
    scene w3_10983 with dissolve
    "{i}The crowd loved that.{/i}"
    jer "Pahahaha!"
    scene w3_10984 with dissolve
    mc "Oh...?"
    scene w3_10985 with dissolve
    "There was Felicia, looking like a million bucks as usual, {i}smirking.{/i}"
    mct "(She {b}did{/b} make it!)"
    "It was difficult to make out at a distance, but I'm pretty sure she's mouthing..."
    stop music fadeout 3.0
    scene w3_10986 with dissolve
    fel "What."
    scene w3_10987 with dissolve
    fel "The."
    scene w3_10988 with dissolve
    fel "Fuck?!"
    play music "sound effects/bass-riff.wav"
    scene w3_10989 with dissolve
    "Back on stage, Spider was in the middle of what he imagined to be a solo."
    scene w3_10990 with dissolve
    mc "Did Hana put you up to this!"
    scene w3_10991 with dissolve
    jer "Nope! I just saw you and thought \"why the fuck not?\" Pretty punk of me, huh?! Haha!"

    if w3HanaDP >= 4:
        $ w3RockShowHanaKiss = True
        scene w3_10990 with dissolve
        mc "I think saying that disqualifies--"
        scene w3_10992 with dissolve
        jer "Heads up!"
        mc "Huh?!"
        scene w3_10993 with dissolve
        jer "I said heads up! Wrecking ball com--!"
        scene w3_10994 with dissolve
        mc "--?!"
        scene rs_hanakiss_a with dissolve
        show rs_hanakiss
        hana "Mmmhh..."
        "Hana put a lot of faith in my upper body strength and balance."
        hana "Aah, aahh...♥"
        "This situation, whatever it was, had Hana {b}revved{/b} up and raring to go."
        hana "Mmmh, mmmm!"
        "Whether it was me being on stage with her, the feeling of having an audience, or something else... Hana laid claim to me in front of everyone."

        if w3MinaHotelFucked == True and w3VeronicaMinaLezPush == False:
            $ hanaMinaFlag = True
            scene w3_10995 with dissolve:
                align (0.5,0.5)
                linear 160 zoom 2.5
                pause 4
            "........."
            "......"
            "...{i}everyone.{/i}"
            scene rs_hanakiss_a with dissolve
            show rs_hanakiss
            hana "Mmhh...."

            if w3MinaTransparent == False:
                mct "(I miiiight have some explaining to do with Mina...)"

        jer "Haha, yeah!"
        "Spider's solo felt like it went on forever, and as crappy as it was, I had to admit..."

        if hanaGF == True:
            "{i}Pretty nice having live music playing out your kiss with your hot goth GF."
        else:
            "{i}Pretty nice having live music playing out your kiss with your hot goth lover."


        scene w3_10996 with dissolve
        if not persistent.w3HanaRSKiss:
            play sound "sound effects/notification.wav"
            show memoryunlock with dissolve
            $ renpy.pause(3, hard=True)
            $ persistent.w3HanaRSKiss = True

        hana "...ever consider being a singer?"
        scene w3_10997 with dissolve
        jer "Excuse me?! You're not replacing me, bi--"
        $ renpy.end_replay()


        if w3VeronicaMinaLezPush == True:
            jump w3RockShowVeroMinaYeet
        else:
            stop music fadeout 3.0
            scene black with fade
            "This was my chance not to wear out my welcome."
            "........."
            "......"
            "..."
            jump w3RockShowMusicDone
    else:
        scene w3_10990 with dissolve
        mc "I think saying that disqualifies you!"
        scene w3_10998 with dissolve
        jer "Oh...?! What do you know?! Get the fuck off my stage!"
        scene black with fade
        mc "Haha, with pleasure--"

        if w3VeronicaMinaLezPush == True:
            "I waved goodbye to Hana."
            "........."
            "......"
            "..."
            jump w3RockShowVeroMinaYeet
        else:
            stop music fadeout 3.0
            scene black with fade
            "I waved goodbye to Hana."
            "........."
            "......"
            "..."
            jump w3RockShowMusicDone


label w3RockShowVeroMinaYeet:
    play ambient "sound effects/rock-crowd-stage-loop.wav"
    play music "music/young-squire.ogg"
    scene w3_10999 with circlewipe
    if w3RockShowJammed == True:
        ver "Ha! He can {i}not{/i} sing!"
        scene w3_11000 with dissolve
        mina "..."
    else:
        ver "You know, I kinda get what you see in her.."
        scene w3_11000 with dissolve
        mina "..."
    scene w3_11001 with dissolve
    ver "You alright...?"
    scene w3_11002 with dissolve
    mina "H-hey... this might sound crazy, but... let's go upstairs."
    scene w3_11001 with dissolve
    ver "Oh? Sure, but--"
    scene w3_11002 with dissolve
    mina "My ex keeps looking at me."
    scene w3_11003 with dissolve
    ver "...things end messy?"
    scene w3_11004 with dissolve
    mina "Uh huh..."
    scene w3_11005 with dissolve
    ver "He's still looking."
    scene w3_11004 with dissolve
    mina "I know..."
    scene w3_11006 with dissolve
    ver "Ah... I think I know what you're getting at..."
    ver "Take me by the hand and lead the way."
    scene w3_11007 with dissolve
    mina "M-me...?"
    ver "Lest you forget... you initiated this."
    mina "O-oh... I did... heh."
    scene w3_11008 with dissolve
    ver "I don't mind a girlie taking charge... especially one as cute as you."
    scene w3_11009 with dissolve
    mina "I--"
    scene w3_11010 with dissolve
    mina "You're pretty damn lucky, you know."
    ver "I'm counting my blessings..."
    stop music fadeout 3.0
    scene black with fade
    ver "He's still looking."
    mina "{b}Good.{/b}"
    "..."
    jump w3RockShowVeroMinaVIP

label w3RockShowMCNotSoJam:
    scene w3_11011 with fade
    mc "Oh, hey! When did you get here!"
    harp "Not too long ago! I see you came this time!"
    mc "Yeah! I couldn't turn down Hana twice!"
    scene w3_11012 with dissolve
    harp "Especially not when she's your boss!"
    scene w3_11013 with dissolve
    mc "That's what I said, but Hana hates that joke!"
    scene w3_11014 with dissolve
    harp "I--"
    rfb "Hey I like your tat--"
    scene w3_11015 with dissolve
    harp "Don't butt into conversations."
    scene w3_11016 with dissolve
    rfb "Aha, I didn't mean to be rude, I was just waiting--"
    scene w3_11015 with dissolve
    harp "Yet you still are. Walk away."
    scene w3_11017 with dissolve
    "He looked at me, looking for a rope."
    mc "Sorry, Pete. She's not very nice is she?"
    scene w3_11018 with dissolve
    rfb "Bah, whatever."
    scene w3_11019 with dissolve
    mc "Damn. You shut him down."
    scene w3_11020 with dissolve
    harp "Like I have time for a fuck boy like him."
    scene w3_11019 with dissolve
    mc "Haha, I like it!"
    scene w3_11021 with dissolve
    harp "Get me a drink?"
    scene w3_11022 with dissolve
    mc "Sure, why not?"
    scene black with fade
    "One can only scream so much."
    jump w3RockShowVeroMinaYeet

label w3RockShowFeliciaCall:
    scene w3_11024 with dissolve
    mc "Hmm, why not?"
    "It bugged me that only two of my three Carnations were here."
    scene black with fade
    play ambient "sound effects/ringing-inbound.wav"
    "Gotta find someplace relatively quiet..."
    scene w3_11025 with fade
    "It rang until I thought it was going to go to voicemail and then--"
    play sound "sound effects/phonemenu.wav"
    stop ambient
    scene w3_11026 with dissolve
    fel "[mcf], [mcf], [mcf]... you want me there that bad huh?"
    scene w3_11027 with dissolve
    mc "Of course I do, Felicia. Anywhere you go is instantly improved by your presence."
    scene w3_11026 with dissolve
    fel "That came out so smoothly that it's a little frightening."
    scene w3_11027 with dissolve
    mc "Sorry to bother you. Is Elias around?"
    scene w3_11026 with dissolve
    fel "Putting it like that makes it sound like we're affair partners."
    scene w3_11033 with dissolve
    mc "Like you said, maybe I just want you here that bad."
    scene w3_11032 with dissolve
    fel "Well, you'll be happy to know I'm on my way. I put Elias to {i}bed.{/i}"
    scene w3_11029 with dissolve
    mc "He's asleep?"
    scene w3_11028 with dissolve
    fel "Uh huh. Out like a baby."

    menu:
        "Ask how she managed that.":
            scene w3_11029 with dissolve
            mc "...{b}tuckered{/b} him out, did you? How did you manage that?"
            scene w3_11030 with pixellate
            fel "Oh, I just performed my {i}wifely duties.{/i}"
            mc "Sounds romantic."
            fel "Those are his words, not mine."
            mc "How can you stand it? Don't you hate his guts?"
            fel "I guess work is work."
            mc "I suppose he's going to miss you during his trip out of town tomorrow."
            scene w3_11028 with pixellate
            fel "Unlikely. No shortage of skanks in Tokyo, but he likes to pull on my leash from time to time."
            scene w3_11029 with dissolve
            mc "That's where he's going?"
        "...you have a pretty good idea and don't need to know more..":

            scene w3_11033 with dissolve
            mc "Lets leave it at that."
            scene w3_11032 with dissolve
            fel "Smart boy."
            scene w3_11029 with dissolve
            mc "So he wanted you to stay in? Sounds like he's going to miss you during his trip."
            scene w3_11028 with dissolve
            fel "Unlikely. No shortage of skanks in Tokyo, but he likes to pull my leash from time to time."
            scene w3_11029 with dissolve
            mc "That's where he's going?"

    scene w3_11028 with dissolve
    fel "So he says. Anyway, I'll be at this... uh... \"Asp Hole\" - nice name by the way - in ten if traffic keeps up."
    scene w3_11029 with dissolve
    mc "Good. I'll come out and meet you."
    scene w3_11028 with dissolve
    fel "You don't have to do that."
    scene w3_11033 with dissolve
    mc "No, but I'm going to pass up the chance of walking into this shit hole with the most beautiful artist in the city."
    scene w3_11032 with dissolve

    if w3FeliciaSoloEnd == True or w3FeliciaMinaThreesomeEnd == True:
        fel "Ah... [mcf]..."
    else:
        fel "Yet we ended it as just friends the other night..."
        scene w3_11028 with dissolve
        mc "I don't need sex to value you as a person, Felicia."
        scene w3_11029 with dissolve
        "..."
        scene w3_11028 with dissolve
        mc "...you there?"
        scene w3_11032 with dissolve


    fel "I'm going to miss this kind of thing."
    scene w3_11033 with dissolve
    mc "Oh...? What makes you say that?"
    scene w3_11032 with dissolve
    fel "I won't be able to be spotted entering seedy rock clubs with young men once he's on the campaign trail."
    scene w3_11033 with dissolve
    mc "Oh..."
    scene w3_11032 with dissolve
    fel "I'll see you soon."
    play sound "sound effects/phonemenu.wav"
    "*Click*"
    if w3VeronicaMinaLezPush == True:
        scene w3_11034 with dissolve
        mc "..."
        play ambient "sound effects/rock-crowd-stage-loop.wav"
        scene w3_10632 with dissolve
        "{i}On the way out, I checked up on my project: {i}Mina and Veronica.{/i}"
        "Things were going good. Veronica was jumping and banging her head, and Mina tentatively followed her example."
        "I peered at the pair for a moment, watching Mina as she gradually grew more comfortable with the rhythm."
        "{i}Better than I would.{/i} Not to this music."
        scene w3_10633 with dissolve
        "After waiting a bit, and allowing Mina's shyness to naturally melt away, Veronica put her hands around the ball of energy's waist and ground her dance partner's tempo to a crawl."
        "{b}Good.{/b}"
        scene black with fade
        "..."
        jump w3RockShowVeroMinaGetPersonal
    else:
        stop music
        scene w3_11034 with dissolve
        mc "......"
        play music "music/wanderlust.ogg"
        scene black with fade
        "..."
        jump w3RockShowFeliciaGreeting

label w3RockShowFeliciaGreeting:
    if _in_replay:
        play music "music/wanderlust.ogg"
    scene w3_11035 with blinds
    mc "There you are. Love that dress."
    fel "Guess we're both overdressed for this shithole."
    mc "...am I?"
    scene w3_11036 with dissolve
    fel "Seems I did it on purpose though. Funny though."
    scene w3_11037 with dissolve
    mc "What is?"
    scene w3_11036 with dissolve
    fel "Our first date you were {i}underdressed{/i}."
    scene w3_11038 with dissolve
    mc "Good to see you, Felicia. {i}Missed you.{/i}"
    scene w3_11036 with dissolve
    fel "It's just been a couple of days, [mcf]."
    scene w3_11037 with dissolve
    mc "Oh? You didn't miss me then?"

    if w3FeliciaSoloEnd == True or w3FeliciaMinaThreesomeEnd == True:
        scene w3_11039 with dissolve
        fel "I'm not saying I didn't."
        scene w3_11040 with dissolve
        mc "You're cute."
        fel "Mmmh..."
        scene w3_11041 with dissolve
        mc "I'm happy you're here."
    else:
        scene w3_11036 with dissolve
        fel "Hmm, should I? I don't know..."
        scene w3_11038 with dissolve
        mc "I don't know about you, but I'm happy {i}you're{/i} here."

    scene w3_11036 with dissolve
    fel "Carnation \"bonding\" time is--"
    scene w3_11037 with dissolve
    mc "Yes, yes, I know. {i}Pointless{/i}. I don't care about that."

    if w3FeliciaSoloEnd == True:
        scene w3_11043 with dissolve
        fel "What--"
        scene w3_11048 with dissolve
        fel "What are you doing?"
        scene w3_11049 with dissolve
        mc "I won't get a chance to kiss you in there. Not in front of the other Carnations, and the thought of seeing you without even a kiss..."
        scene w3_11050 with dissolve
        fel "Oh..."
        scene rs_feliciakiss_a with dissolve
        show rs_feliciakiss
        "Felicia's lips met mine, seemingly mollified by my reasoning."
        fel "Mmmhh..."
        "It may have just been a line, but after our night out, I'd be lying to myself if I said I didn't feel anything romantic for this woman..."
        mct "(Bah, I wish we could do more than just kiss...)"
        "........."
        "......"
        scene w3_11051 with dissolve
        fel "...I didn't {i}not{/i} miss that."
        scene w3_11052 with dissolve
        mc "Ready to go in?"
        scene w3_11051 with dissolve
        fel "Uh... how about I smoke another cig or two? Enjoy it just being us before it's not."
        scene w3_11052 with dissolve
        mc "I {i}love{/i} that idea."
        scene black with fade
        if not persistent.w3FeliciaRSKiss:
            play sound "sound effects/notification.wav"
            show memoryunlock with dissolve
            $ renpy.pause(3, hard=True)
            $ persistent.w3FeliciaRSKiss = True
        "It turned out to be three cigarettes."
        $ renpy.end_replay()
        if w3VeronicaMinaLezPush == True:
            jump w3RockShowVeroMinaYeet
        else:
            stop music fadeout 3.0
            "........."
            "......"
            "..."
            jump w3RockShowMusicDone
    else:
        scene w3_11036 with dissolve
        fel "What do you care about?"
        scene w3_11038 with dissolve
        mc "Having a nice night out. You excited for tomorrow?"
        scene w3_11044 with dissolve
        fel "Strangely... {i}no.{/i}"
        scene w3_11045 with dissolve
        mc "It's not all fun and games anymore?"
        scene w3_11044 with dissolve
        fel "The preview for hell week didn't help, plus... this Elias stuff has complicated my plans."
        scene w3_11046 with dissolve
        "........."
        scene w3_11047 with dissolve
        "......"
        scene w3_11036 with dissolve
        fel "...I'm going to smoke another cigarette. Wanna hang around and enjoy being alone for a bit before we're not?"
        scene w3_11037 with dissolve
        mc "I'd love to."
        scene black with fade
        "Just like the other night, we hung out for a bit, {b}as friends.{/b}"

        if w3VeronicaMinaLezPush == True:
            jump w3RockShowVeroMinaYeet
        else:
            jump w3RockShowMusicDone

label w3RockShowRosaVIP:
    play ambient "sound effects/rock-crowd-floor-ambience-muffled.wav"
    play music "music/outreach.ogg"
    scene w3_11053 with wipeleft
    rose "...wwwwwwhy are you so nice to meeee?"
    scene w3_11054 with dissolve
    "...{i}Jesus{/i}, how much did she actually drink before coming here?"
    scene w3_11053 with dissolve
    rose "S-seriously... n-no one's that, a-ahh..."
    scene w3_11053 with dissolve

    if w3RosalindEndlessBJWorks == True:
        mct "(She thinks I've been nice...? {b}That's sad.{/b})"
        "...did she forget I used her as a cum receptacle last night?"

    scene w3_11055 with dissolve
    mc "What have I done that's so nice, Rose?"
    scene w3_11056 with dissolve
    rose "You held my hair when I--"
    scene w3_11055 with dissolve
    mc "That was Veronica."
    scene w3_11057 with dissolve
    rose "Veronica?! No!"
    scene w3_11058 with dissolve
    mc "...'fraid so."
    scene w3_11059 with dissolve
    rose "Ah is this that com-cahm-comodorie you wanted?"
    scene w3_11060 with dissolve
    mct "(I should see about getting her home...)"
    "Rosalind vacantly stared off into {b}nothing{/b} as this night added another picture to the photo album of the many different faces of Rosalind Carter."
    scene w3_11061 with dissolve
    rose "Veronica... I feel bad for her..."
    scene w3_11062 with dissolve
    mc "I thought you thought the other two Carnations had bullshit reasons..."
    scene w3_11061 with dissolve
    rose "Euuauh... everyone's problems are important to themselves..."
    scene w3_11060 with dissolve
    "........."
    "......"
    scene w3_11063 with dissolve
    rose "...Felicia's still a fucking whore though! I don't get her..."
    scene w3_11064 with dissolve
    mc "Big appetite and a lot of wants."
    scene w3_11065 with dissolve
    rose "More like she's got a big hole! And, uh... I'm not talking about her cunt! Haha!"
    scene w3_11055 with dissolve
    mc "...you think?"
    scene w3_11066 with dissolve
    rose "She's trying to convince herself of something."
    scene w3_11055 with dissolve
    mc "You see right through her, huh?"
    scene w3_11067 with dissolve
    rose "Hey! Are you and her...?"
    scene w3_11068 with dissolve
    mc "Are we...?"
    scene w3_11067 with dissolve
    rose "Hmm....? You know! {b}Fucking!{/b}"
    scene w3_11068 with dissolve
    mc "No, why would you--"
    scene w3_11069 with dissolve

    if roseFlag == True:
        rose "I mean, I did it. Veronica... {i}she wouldn't{/i}, but that floozy would!"
    else:
        rose "I mean, I tried it. Veronica... {i}she wouldn't{/i}, but that floozy would!"

    if feliciaFlag == True:
        mct "(...damn her intuition, but it's not like I can admit it.)"

    scene w3_11068 with dissolve
    mc "She probably thinks she doesn't need an advantage."
    scene w3_11070 with dissolve
    rose "{b}Hmmmmmmhhhhhh...!{/b}"
    scene w3_11081 with dissolve
    mc "Honest, Rose."
    scene w3_11070 with dissolve
    "........."
    "......"
    scene w3_11065 with dissolve
    rose "...like I care, haha! How was my dancing?"
    scene w3_11071 with dissolve
    mc "It was... {b}bold.{/b}"
    scene w3_11063 with dissolve
    rose "Good! Let that be a lesson to you! Don't look down on Rosie!"
    scene w3_11064 with dissolve
    mc "Oh, you can be sure I'll never make that mistake again."
    scene w3_11056 with dissolve
    rose "...hey, would you get me a drink?"
    scene w3_11055 with dissolve
    mc "You've had enough, Rose."
    scene w3_11059 with dissolve
    rose "Some water, [mcf]... I need to hydreh-- hydrate if I'm going to be at my best tomorrow."
    scene w3_11055 with dissolve
    mc "Okay..."
    scene w3_11072 with dissolve
    mc "Be back in a jiffy."

    if w3RosalindRomanticSex == True:
        scene w3_11073 with dissolve
        rose "W-wait..."
        scene w3_11074 with dissolve
        "She looked at me and smiled, with a glint in her eye not dissimilar to last night."
        scene w3_11075 with dissolve
        rose "Thank you for your concern. About my drinking, I, uh... {i}yeah...{/i} and..."
        scene rs_rosakiss_a with dissolve
        show rs_rosakiss
        "And she kissed me."
        "Her breath smelled {i}awful{/i}, but I didn't care."
        "When you're so starved for affection, even just common decency can mean a lot."
        "........."
        "......"
        scene w3_11076 with dissolve
        rose "...and uh, {i}I don't know.{/i} I can't think. Hopefully I won't remember that tomorrow."
        scene w3_11077 with dissolve
        "......"
        scene w3_11078 with dissolve
        rose "...ggghh... I'm starting to feel sick!"
        mc "What?! Don't-- then sit down!"
        scene w3_11079 with dissolve
        rose "Y-yes, sir! Mr [mcl], sir! Ahah!"
        stop music fadeout 3.0
        scene black with fade
        "........."
        "......"
        if not persistent.w3RosaVIPKiss:
            play sound "sound effects/notification.wav"
            show memoryunlock with dissolve
            $ renpy.pause(3, hard=True)
            $ persistent.w3RosaVIPKiss = True

        "..."
        $ renpy.end_replay()
    else:

        scene w3_11080 with dissolve
        rose "...I'll just rest my eyes in the meantime."
        stop music fadeout 3
        scene black with fade
        "And that was how I rode out Hana's set, nursing an inebriated Rosalind."
        "........."
        "......"
        "..."
    jump w3RockShowMusicDone


label w3RockShowVeroHang:
    scene w3_11082 with fade
    mc "Dancing alone? No luck tonight?"
    scene w3_11083 with dissolve
    ver "I'm 0 for 2. At first the bartender seemed into me, but then I realized she's just working for tips..."
    scene w3_11084 with dissolve
    mc "I'm a little hurt I wasn't your first choice."
    scene w3_11085 with dissolve
    ver "You think you'd ever be my first, second, or third choice?"
    scene w3_11086 with dissolve
    mc "Why shouldn't I be? Remember the other night?"
    scene w3_11151 with pixellate
    mc "The way you had your legs wrapped around me, nails digging into my back? Do you remember?"
    ver "Uh... I..."
    scene w3_11152 with pixellate
    mc "Or are you so quick to forget how I had you folded? Pressed against the couch? Pissing yourself on Ian's leather?"
    scene w3_11087 with pixellate
    ver "Aaah... sneaky fuck, whispering in my ear like that..."
    scene w3_11088 with dissolve
    mc "I'm just sayin'... you won't get that kind of \"firm hand\" from the women you try it with."
    scene w3_11089 with dissolve
    ver "I seem to remember having your legs over your shoulders..."
    scene w3_11090 with dissolve
    mc "...and wasn't that fun?"
    scene w3_11089 with dissolve
    ver "...{i}it was.{/i}"
    scene w3_11091 with dissolve
    mc "So, fuck that bartender, you should've stuck with me."
    scene w3_11092 with dissolve
    ver "Maybe I would've, but you had a bubbly blonde clinging to you."
    scene w3_11091 with dissolve
    mc "I don't know..."
    scene w3_11093 with dissolve
    "......"
    scene w3_11094 with dissolve
    ver "...let's go get a drink."
    scene w3_11095 with dissolve
    mc "Sure, anything you want."
    scene w3_11096 with dissolve
    ver "It's not for me. I've given myself a three-drink limit. No way I'm getting wasted before tomorrow night."
    scene w3_11095 with dissolve
    mc "Then who's the drink for?"
    scene w3_11094 with dissolve
    ver "It's so that you can flirt with the bartender."
    scene w3_11095 with dissolve
    mc "...and why would I want to do that when I have you right here?"
    scene w3_11094 with dissolve
    ver "Because if you get her number, I'll be impressed."
    scene w3_11093 with dissolve
    "I wasn't entirely convinced I'd be able to manage that, but it was also true that the nature of our relationship meant I never got to demonstrate my \"prowess\" to Veronica..."
    scene w3_11095 with dissolve
    mc "...and if I don't?"
    scene w3_11093 with dissolve
    "The thought of testing myself, going out on a limb and proving my desirability to the amazon..."
    scene w3_11094 with dissolve
    ver "{i}You{/i} strike out."
    scene w3_11095 with dissolve
    mc "Alright. Stick close to me."
    stop music fadeout 3.0
    scene black with fade
    "{i}This should be fun.{/i}"
    play music "music/finland.ogg"
    scene w3_11097 with wipeleft
    bar "What can I get you?"
    scene w3_11098 with dissolve
    mc "I'll take a beer and your number."
    scene w3_11099 with dissolve
    bar "Sorry. That's not on the menu."
    scene w3_11100 with dissolve
    mc "No...? Not even for a young, handsome guy like me?"
    scene w3_11101 with dissolve
    bar "{i}Especially{/i} for a young guy like you."
    scene w3_11102 with dissolve

    if w3RockShowIanTalk == False:
        mc "Damn. Is it because of Mr. Byrnes?"
    else:
        mc "What's so especially about me?"

    scene w3_11101 with dissolve
    bar "You resemble my type."
    scene w3_11103 with dissolve
    "...{i}shit{/i}, I'm starting out with a bigger advantage than I could hope for."
    scene w3_11102 with dissolve
    mc "...how does that make any sense?"
    scene w3_11104 with dissolve
    bar "Well, it never seems to end great, no matter how cute and well-dressed you are. Younger guys... {i}are just too clingy.{/i} Still want that beer?"
    scene w3_11105 with dissolve
    mc "Absolutely. It'll give me more time to convince you."
    scene w3_11106 with dissolve
    bar "Haha, sure."
    scene w3_11107 with dissolve
    mc "The name's [mcf], by the way."
    scene w3_11108 with dissolve
    bar "...okay, I can at least give you mine: I'm Eve."
    scene w3_11109 with dissolve
    mc "Very pretty name, {b}Eve.{/b} And that's Veronica over there."
    scene w3_11110 with dissolve
    mc "Did she introduce herself?"
    scene w3_11111 with dissolve
    eve "No. Are you going to ask me to feel your muscles too?"
    scene w3_11110 with dissolve
    mc "Oh, I doubt I'd compare."
    scene w3_11112 with dissolve
    mc "Come~"
    scene w3_11113 with dissolve
    "Veronica looks unsure over this unexpected direction, but she joined me at the bar."
    scene w3_11114 with dissolve
    mc "Did you know she's an Olympic silver medalist?"
    scene w3_11115 with dissolve
    eve "...really?"
    ver "I don't like to--"
    scene w3_11116 with dissolve
    mc "I can't believe you didn't open with that."
    "{i}She still looked confused at me putting her in the middle of this.{/i}"
    scene w3_11117 with dissolve
    eve "What is this? Some kind of game?"
    scene w3_11118 with dissolve
    mc "No game. Just a young guy trying his best to get a stunningly beautiful bartender's number."
    mc "I'm not the clingy type, but {i}we{/i} do like to have fun."
    scene w3_11119 with dissolve
    eve "That's a new one..."
    scene w3_11120 with dissolve
    eve "With the way you were aggressively hitting on me, I pegged you as 100 percent gay, {i}Veronica.{/i}"
    scene w3_11121 with dissolve
    mc "I'm an uncommon exception."
    ver "You--!"
    scene w3_11122 with dissolve
    mc "Aw, come on. Tell her about one of my good qualities."
    ver "Like you have any!"
    scene w3_11123 with dissolve
    eve "Aw, I'd like to hear one!"
    scene w3_11124 with dissolve
    "......"
    scene w3_11125 with dissolve
    ver "...lean in, I'll whisper it to you. Don't want this asshole getting a big head."
    scene w3_11126 with dissolve
    "I watched Veronica pour unknown words into the barkeep's head."
    "At first, she was dubious, but then--"
    scene w3_11127 with dissolve
    eve "...oh? No shit?"
    ver "I... uh... I can vouch for that first hand."
    scene w3_11128 with dissolve
    mc "So, come on, give me your number and I'll let you get back to work."
    scene w3_11129 with dissolve
    "......"
    scene w3_11130 with dissolve
    eve "...pfff, alright! You're cute, and this song and dance you two have has me interested."
    scene w3_11131 with dissolve
    eve "...and an Olympian, huh?"
    mc "Got a napkin?"
    scene black with fade
    "..."
    scene w3_11132 with fade
    mc "Ha! Can't believe that worked! What did you even tell her?"
    ver "You know that doesn't count, right?"
    scene w3_11133 with dissolve
    mc "And why doesn't it?"
    ver "You used me to seal the deal!"
    scene w3_11134 with dissolve
    mc "Oh? And I {i}didn't{/i} win you over last Tuesday?"
    ver "I'm not a trophy!"
    scene w3_11135 with dissolve
    mc "You're looking at it the wrong way, baby."
    scene w3_11136 with dissolve
    "I was, without a doubt, full of myself right now."
    scene w3_11137 with dissolve
    mc "{i}We{/i} won her over. I caught her interest and {b}you{/b} gave her the little push she needed."
    mc "She recognized how great you are, and--"
    scene w3_11138 with dissolve
    ver "...you tricked her into making her think you're worth a shit."
    scene w3_11139 with dissolve
    mc "Don't be a sore loser."

label w3RockShowVeroVIP:

    play music "music/ocean-view.ogg"
    scene rs_verokiss_a with fade
    show rs_verokiss
    "Before I realized it, I was not only swept up in my own fantasy, but Veronica's as well."
    ver "Mmmh~"
    "The big woman overwhelmed me, pulling me into her embrace, and coddled me like a lover."
    "A bit of fun, a bit of distraction, {i}whatever{/i} before tomorrow. An unknown quantity held in her strapping arms."
    "The soft way she kissed me at odds with her iron-clad grip."
    "For a moment, the world stopped."
    "........."
    "......"
    scene w3_11140 with dissolve
    ver "...that {i}was{/i} fun."
    scene w3_11141 with dissolve
    mc "We make a good team, don't we?"
    scene w3_11140 with dissolve
    ver "By the way, I think that assist entitles me to her number too."
    scene w3_11141 with dissolve
    mc "Oh? But its in my pocket, Veronica. If you really want it though, there is something you can do to earn it."
    scene w3_11140 with dissolve
    ver "Oh, this ought to be good..."
    scene black with fade
    "........."
    if not persistent.w3VeroVIPKiss:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3VeroVIPKiss = True
    "......"
    scene w3_11142 with fade
    ver "...come on. This--"
    scene w3_11143 with dissolve
    mc "Isn't it nice? You smell good."
    scene w3_11142 with dissolve
    ver "Yeah, but--"
    scene w3_11144 with dissolve
    mc "I just want to chill for a bit. Just you and me. It's not a big ask, is it?"
    scene w3_11145 with dissolve
    ver "Hmm..."
    scene w3_11146 with dissolve
    mc "Don't pout!"
    scene w3_11147 with dissolve
    ver "...fuckin' idiot."
    scene w3_11148 with dissolve
    "........."
    "......"
    scene w3_11149 with dissolve
    mc "...you really going to call the bartender?"
    scene w3_11150 with dissolve
    ver "Eh. Don't ruin the moment, [mcf]. I don't want it anymore."
    scene w3_11149 with dissolve
    mc "...sorry."
    stop music fadeout 3.0
    scene black with fade
    "........."
    "......"
    "..."
    $ renpy.end_replay()
    jump w3RockShowMusicDone


label w3RockShowVeroMinaVIP:
    $ w3RockShowVeroMinaMadeOutExtra = True
    play music "music/for-time-to-disappear.ogg"
    play ambient "sound effects/rock-crowd-floor-ambience-muffled.wav"

    if w3RockShowHanaPath == True:
        scene w3_11153 with wipeleft
        mina "Heh, now... so, where were we?"
        scene w3_11154 with dissolve
        ver "You were sucking my face."
        scene w3_11155 with dissolve
        mina "Ah, right..."
        scene w3_11156 with dissolve
        ver "Aw, where did your confidence go?"
        scene w3_11157 with dissolve
        mina "Ah... I just... {i}realized{/i} we're pretty alone..."
        scene w3_11158 with dissolve
        ver "I've got to say, using me like a {b}prop{/b} to make some boy squirm..."
        mina "W-what, no, I--"
        scene w3_11159 with dissolve
        ver "{i}That's fun.{/i}"
        mina "Oh... well... {b}good.{/b}."
    else:


        scene w3_11160 with wipeleft
        ver "Nice place. If I didn't know better, I'd say [mcf] is helping us."
        mina "Haha, oh... you, uh... you think?"
        scene w3_11161 with dissolve
        ver "What's with that look, hmm?"
        scene w3_11155 with dissolve
        mina "Ah, well... nothing, it's just... *ahem* he did encourage me to..."
        mina "It doesn't matter. {b}*Ahem*{/b} Here we are..."
        scene w3_11162 with dissolve
        "........."
        "......"
        scene w3_11163 with dissolve
        ver "...thinking about good things?"
        scene w3_11157 with dissolve
        mina "About our kiss and... uh... how we're... {i}alone.{/i}"
        scene w3_11164 with dissolve
        ver "...mmh, oh! Is that what you and [mcf] cooked up? I've become easy prey for some big bad she-wolf?"
        mina "N-no...! I just went with what he suggested, but--"
        scene w3_11165 with dissolve
        mina "Wait, she-wolf? Ha! Me?!"
        scene w3_11166 with dissolve
        ver "You like the sound of that, Mama?"
        mina "A-ahh..."

    scene w3_11167 with dissolve
    ver "{i}I{/i} liked the way you marched me up the stairs."
    scene w3_11168 with dissolve
    mina "...what way was that?"
    scene w3_11167 with dissolve
    ver "Like a woman who knows and takes what she wants."
    scene w3_11169 with dissolve
    mina "Haha! Yeah, right!"
    scene w3_11170 with dissolve
    ver "And why is that so funny?"
    scene w3_11171 with dissolve
    mina "Because that's not me at all. I usually just follow the flow..."
    scene w3_11172 with dissolve
    ver "Usually doesn't have to be always... {i}you kissed me{/i}, after all."
    scene w3_11173 with dissolve
    mina "I did. I have this thing I'm working on right now... I'm trying to be... {b}more.{/b}"
    scene w3_11174 with dissolve
    ver "To be young and in the process of discovering yourself. How exciting."
    scene w3_11175 with dissolve
    mina "It is... it is {i}exciting.{/i}"
    scene w3_11176 with dissolve
    "........."
    scene w3_11177 with dissolve
    "......"
    scene w3_11178 with dissolve
    mina "...I love your freckles."
    scene w3_11179 with dissolve
    ver "Thank you. They used to be the least favorite thing about me. I thought they were ugly..."
    scene w3_11180 with dissolve
    mina "Why?! They're so... {i}striking.{/i} What changed?"
    scene w3_11179 with dissolve
    ver "I... my ex loved them. She used to draw invisible things on my body. You know... by connecting them..."
    scene w3_11181 with dissolve
    mina "Mmmh..."
    scene w3_11182 with dissolve
    ver "Oh, uh... FYI, I'm the type of gal who is constantly going \"that reminds me of my...\", so sorry if that puts you--"
    scene w3_11183 with dissolve
    mina "...it's s'okay. Why would that put me off?"
    scene w3_11184 with dissolve
    mina "*Cwhup*"
    scene w3_11185 with dissolve
    mina "It's so dainty! It doesn't fit your appearance at all..."
    scene w3_11186 with dissolve
    ver "{i}That's{/i} what you're thinking about?!"
    scene w3_11187 with dissolve
    mina "I'm serious! I love it."
    scene w3_11186 with dissolve
    ver "So, let me get this straight: you like my muscles and my height..."
    scene w3_11187 with dissolve
    mina "Mmhhhmm, that makes you hot..."
    scene w3_11186 with dissolve
    ver "...but you also like my freckles and my {i}dainty{/i} nose?"
    scene w3_11187 with dissolve
    mina "Those... those make you {b}cute.{/b}"
    scene w3_11188 with dissolve
    ver "Ah, okay... thanks for explaining..."
    scene w3_11189 with dissolve
    "......"
    scene w3_11190 with dissolve
    "...."
    scene w3_11191 with dissolve
    mina "Hey! It's hard to touch your face when you're up in the clouds..."
    scene w3_11192 with dissolve
    ver "Oh, I can help you reach them."
    scene w3_11193 with dissolve
    mina "Mmmhh..."
    scene w3_11194 with dissolve
    pause
    scene w3_11195 with dissolve
    pause
    scene rslez_01 with fade
    $ renpy.pause(3, hard=True)
    pause
    scene w3_11203 with dissolve
    mina "*Gulp* Ahh... more of that..."
    scene w3_11204 with dissolve
    pause
    scene w3_11205 with dissolve
    pause
    scene rslez_02 with fade
    pause
    scene w3_11196 with dissolve
    mina "H-hey, I--!"
    scene w3_11197 with dissolve
    mina "I... I want to..."
    scene w3_11198 with dissolve
    mina " {b}Sit back.{/b}"
    scene w3_11199 with dissolve
    ver "I like that tone..."
    scene w3_11200 with dissolve
    ver "Ear! -do my ear--"
    scene rslez_03_a with fade
    show rslez_03
    mina "Mmmh, *Chwup, chwwwup-!"
    ver "T-there it is! That's the spot!"
    mina "Ah~ mmwwah~"
    ver "Thwwhat...! If you keep dhoing thwwwhat..."
    mina "Mmhh, hmhmm *giggle* mhaaah... your ears are small and cute... ah..."
    ver "Y-yeah...?"
    mina "Ah, mwwwah~"
    ver "Mmmh, ahhh..."
    mina "Hehe~ just like your nose~"
    scene rslez_04_a with dissolve
    show rslez_04
    ver "Ghh, hhaaa!"
    pause
    scene w3_11201 with dissolve
    mina "Wow... you look..."
    scene w3_11202 with dissolve
    mina "{b}Wow.{/b}"
    stop music fadeout 3.0
    scene black with fade
    "........."
    if not persistent.w3VeroMinaLez:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3VeroMinaLez = True
    "......"
    "..."
    $ renpy.end_replay()
    if w3RockShowBartenderPath == True:
        stop ambient fadeout 3.0
        jump w3RockShowBartenderPaysOff
    else:
        jump w3RockShowMusicDone

label w3RockShowMusicDone:

    play ambient "sound effects/rock-crowd-stage-loop.wav"
    scene w3_11206 with circlewipe
    jer "Thank you all! That was us! We'll be selling CDs and shit!"
    spid "No, we won't! Because I forgot the merch at home!"
    jer "Okay! Our bassist will be turning tricks in the men's room! Don't miss out!"
    stop ambient
    play music "music/heavy-trailer-1.ogg"
    scene w3_11207 with cmet
    "After a second encore, which followed the first which no one asked for, most people flocked to the bar."
    jump w3RockShowCarnationMeeting

label w3RockShowCarnationMeeting:
    if w3RockShowVeroMinaMadeOutExtra == True:
        scene w3_11208 with dissolve
        jacob "Dope as usual, Hana."
        "...the rest gathered around the band."
        hana "Haha, thanks!"
        scene w3_11209 with dissolve
        "Mina eventually joined them too, faintly blushing and nervously fixing her clothes."
    else:

        scene w3_11210 with dissolve
        mina "That. Was...! Wow!"
        "...the rest gathered around the band."
        jacob "Dope as usual, Hana."
        hana "Haha, thanks!"


    if w3RockShowFeliciaPath == True:
        scene w3_11211 with dissolve
        "But, with Felicia by my side, I had another destination."
        scene w3_11212 with dissolve
        mc "We should find Veronica and Rose."
        scene w3_11213 with dissolve
        fel "Good idea. Just what I need: a chat with my gal pals before Kathleen has us tear out each other's throats ."
        scene w3_11212 with dissolve
        mc "...dial back on the sarcasm. You came, Felicia."
        scene w3_11213 with dissolve
        fel "That I did."

    elif w3RockShowJammed == True:
        scene w3_11214 with dissolve
        "But, with Felicia here, I had another destination."
        mc "Hey! I saw you from the stage!"
        scene w3_11215 with dissolve
        fel "I noticed! What the fuck was that about?"
        scene w3_11216 with dissolve
        mc "My debut performance! Let's find Veronica and Rose!"
        scene w3_11217 with dissolve
        fel "Good idea. Just what I need: a chat with my gal pals before Kathleen has us tear out each other's throats ."
        scene w3_11216 with dissolve
        mc "...dial back on the sarcasm. You came, Felicia."
        scene w3_11215 with dissolve
        fel "That I did."
    else:
        scene w3_11214 with dissolve
        "But..."
        mc "Hey! You fucking made it!"
        "Spotting Felicia, I had another destination."
        scene w3_11215 with dissolve
        fel "Ha! I found a way to slip away from Elias!"
        scene w3_11216 with dissolve
        mc "Great! Then we should find Veronica and Rose!"
        scene w3_11217 with dissolve
        fel "Oh, good idea. Just what I need: a chat with my gal pals before Kathleen has us tear out each other's throats ."
        scene w3_11216 with dissolve
        mc "...dial back on the sarcasm. You came, Felicia."
        scene w3_11215 with dissolve
        fel "That I did."

    scene black with fade
    "..."
    scene w3_11218 with circlewipe
    ver "...she's not wrong."
    scene w3_11219 with dissolve
    mc "Of course she isn't! And I've spent the entire night acknowledging how silly getting you three together is, but you bitches don't have a choice."
    scene w3_11220 with dissolve
    mc "So kumbaya, my Lord."
    scene w3_11221 with dissolve
    "........."
    "......"
    scene w3_11222 with dissolve
    rose "...was that a joke?"
    scene w3_11223 with dissolve
    fel "I don't think so. It wasn't funny?"
    scene w3_11224 with dissolve
    ver "That was pretty lame, [mcf]."
    scene w3_11225 with dissolve
    mc "See... I {i}can{/i} get you girls to agree on something."

    if w3RockShowVeroMinaMadeOutExtra == True:
        scene w3_11226 with dissolve
        fel "By the way, you look happy."
        scene w3_11227 with dissolve
        ver "It's been a good night."
        mct "(I bet it has...)"
        scene w3_11228 with dissolve
        fel "That one doesn't look so hot."
    else:
        scene w3_11228 with dissolve
        fel "You don't look so hot, Rose."

    scene w3_11229 with dissolve
    rose "I'm doing my best okay?!"
    mc "Uh, she's a little drunk..."
    scene w3_11230 with dissolve
    ver "What about you? Take off those glasses! You look stupid!"
    "Yep. Off to a {b}great{/b} start."
    fel "I will if you lose the cunt--"
    scene w3_11231 with dissolve
    mc "Gah! Will you cool it?!"
    rosefelvero "Hmhm...?!"
    scene w3_11232 with dissolve
    mc "Uh, you heard me!"
    "......"
    scene w3_11233 with dissolve
    fel "...if anything, this is good practice for tomorrow."
    scene w3_11234 with dissolve
    ver "Ha! Yeah! We'll put on an even better show tomorrow."
    scene w3_11235 with dissolve
    rose "Oh! So that's your plan...! Get us together so we'll fight! You're inshiid- a, a snake in the grass, Mr. [mcl]!"
    scene w3_11236 with dissolve
    "......"
    scene w3_11237 with dissolve
    mc "*sigh* Tomorrow's going to be rough... just know I'm rooting for you girls."
    scene w3_11238 with dissolve
    ver "But like last time, you don't have any idea what that old bitch is going to have us do?"
    scene w3_11237 with dissolve
    mc "No, {b}I don't.{/b}"
    scene w3_11238 with dissolve


    if w3KathleenFeliciaReveal == True:
        mct "(Well, I did glean a little bit of something about what Kathleen had in store for Felicia, but...)"
        "Mrs. Pulman told me to keep my lips sealed."

        menu:
            "Unzip 'em. ( w3PaintingReveal = True)":
                $ w3PaintingReveal = True
                scene w3_11239 with dissolve
                mc "Actually, I have it on good authority the old woman is getting personal with it."
                scene w3_11240 with dissolve
                ver "{b}Explain.{/b}"
                scene w3_11241 with dissolve
                mc "Uh, well... she bought one of Denise's paintings the other night, Felicia."
                scene w3_11242 with dissolve
                "......"
                scene w3_11243 with dissolve
                fel "...did she? Ha! I'm glad Denise got paid for it."
                scene w3_11244 with dissolve
                mc "...that doesn't bother you? Surprise?"
                scene w3_11243 with dissolve
                fel "I figured she was up to something when I ran into Eric and that dumb bitch teacher."
                scene w3_11245 with dissolve
                rose "...what are you guys talking about?"
                mc "Nothing. All you need to understand is you should probably expect some surprises tomorrow."
                scene w3_11246 with dissolve
                ver "Oh, yeah, {b}great.{/b} Helpful."
                scene w3_11247 with dissolve
                fel "{i}You{/i} didn't tell Kathleen about the art exhibition in the first place, right [mcf]?"
                scene w3_11248 with dissolve
                mc "...you think I would?"
                scene w3_11249 with dissolve
                fel "I don't know... people can surprise you..."
                mct "(That kinda hurts...)"
                scene w3_11250 with dissolve
                mc "Of course I fucking didn't."
                scene w3_11251 with dissolve
                ver "Uh... what's with this energy?"
                scene w3_11253 with dissolve
                mc "I learned {b}later{/b} what she was doing, and I'm telling you now so you won't be surprised."
                scene w3_11252 with dissolve
                "......"
                scene w3_11253 with dissolve
                mc "...but do {i}try{/i} to act surprised tomorrow, okay? She'll expect it."
                scene w3_11252 with dissolve
                ver "Hey! Why does she get an unfair advantage?!"
                scene w3_11237 with dissolve
                mc "...don't let animosity prevail tomorrow. All I'm asking."
            "Keep it that way.":
                scene w3_11237 with dissolve
                mc "I ask that you try not to let animosity prevail tomorrow."


    scene w3_11254 with dissolve
    ver "If hating this rich bitch will help me win, then no can do."
    scene w3_11255 with dissolve
    rose "...I agree."
    scene w3_11256 with dissolve
    fel "Hey, you got us to reach a consensus."
    scene w3_11257 with dissolve
    mc "Ah... and that's that, huh?"
    scene w3_11256 with dissolve
    fel "Hopefully, because I should say hello to Mina."
    play music "music/hotshot.ogg"
    scene w3_11258 with dissolve
    "........."
    "......"
    scene w3_11259 with dissolve
    kil "...yo! What are you guys doing up here and whydoesitinvolvewearingclothes?"
    scene w3_11260 with dissolve
    "With perfect timing, there popped up my friend, demolishing the tension."
    scene w3_11261 with dissolve
    mc "Uh... just touching base before tomorrow's show."
    scene w3_11262 with dissolve
    kil "...judging by everyone's expression, I can see it's going well."
    scene w3_11263 with dissolve
    fel "Uh huh, and I drove out here for this."
    scene w3_11264 with dissolve
    kil "Ha! Darius never bothered with this kind of shit, y'know?"
    scene w3_11265 with dissolve
    mc "Yeeeeeah..."
    scene w3_11266 with dissolve
    kil "...?"
    "For a flash, Ian briefly dropped the swagger, and took stock."
    scene w3_11267 with dissolve
    kil "*Sigh* Damn, dude. Alright... I knoooooow that look. Killian to the rescue."
    scene w3_11268 with dissolve
    kil "What you girls need is to cut loose."
    scene w3_11269 with dissolve
    ver "Actually, what I don't need is some fuckboy--"
    scene w3_11270 with dissolve
    kil "Oh, shut the fuck up! I'll be back in a jiffy!"
    scene w3_11271 with dissolve
    ver "........."
    ver "......"
    stop music fadeout 3.0
    scene black with fade
    ver "...{b}that's fair.{/b}"
    play music "music/outreach.ogg"
    scene w3_11272 with wipeleft
    hana "Where'd Spider run off to?"
    scene w3_11273 with dissolve
    jer "He had to put money in the meter."
    scene w3_11272 with dissolve
    hana "...isn't it free parking after 7?"
    scene w3_11274 with dissolve
    jer "...ha! {b}Dumbass!{/b}"
    hana "Oh, shut up! You didn't know it either!"
    scene w3_11275 with dissolve
    jer "You can never be too careful. No one wants their house towed!"
    scene w3_11276 with dissolve
    mina "...you live in a car?"
    scene w3_11277 with dissolve
    jer "Van! And it's a pretty {b}swanky{/b} van!"
    scene w3_11276 with dissolve
    mina "Is that like one of those YouTube things?"
    scene w3_11278 with dissolve
    jer "Uh... {i}no.{/i}"
    jer "Where did you find this one, Han?"
    scene w3_11279 with dissolve
    hana "Speed dating - and I'm thinking about replacing you, Jer. To answer your next question."
    hana "Trade up for a newer model."
    scene w3_11280 with dissolve
    mina "...I'm Mina."
    jer "She already told me. In fact, I know ALL about you."
    scene w3_11281 with dissolve
    mina "...r-really?"
    jer "Hana tells me {i}everything.{/i}"
    scene w3_11282 with dissolve
    hana "Can the territorial shit. She'll think you're serious."
    jer "I'm not...?"
    scene w3_11283 with dissolve
    hana "She's very protective of me."
    jer "Pffh, I just don't trust anyone who'd befriend her is all."
    scene w3_11284 with dissolve
    mina "...you two are hilarious. If the music thing doesn't work out, you could take {i}this{/i} on the road."
    scene w3_11285 with dissolve
    jer "It's gonna work out!"

    if w3RockShowJammed == True:
        scene w3_11286 with dissolve
        hana "Wonder where [mcf] got... by the way what fucking possessed you to pull him up on the stage?"
        jer "I dunno. Whim? I thought I would embarrass him, he'd say no, and you'd realize how much of a bitch he is."

        if w3MinaRockShowKiss == True:
            scene w3_11287 with dissolve
            jer "That backfired, {i}with a kiss.{/i}"
            mina "..."
            scene w3_11288 with dissolve
            hana "What's with you tonight? You were over the moon I met someone."
            jer "Aw, fuck, I don't know. I'm just kidding, you know? Mostly. Woke up on the wrong side of the air mattress."
            hana "Oh, I actually wanted to mention something about that... we should look into getting a place together."
            jer "What about your mom?"
            hana "That's part of it. I'm thinking about moving her into a bigger place..."
            jer "Since when can you afford something like that?"
            hana "I, uh... Dad's being a bit more generous."
            jer "Fuck that! Don't take that creep's money."
            hana "You don't get it, Jer. You don't... you don't live with it. Fuck pride."
            "......"
            scene w3_11289 with dissolve
            hana "...hey! Something the matter, Mina?"
            scene w3_11290 with dissolve
            mina "Uh... haha, no!"
            scene w3_11291 with dissolve
            hana "You sure...?"
            scene w3_11290 with dissolve
            mina "Yeah! I'm having a great time. I just... I just need to go to the little girls' room."
            scene w3_11292 with dissolve
            hana "We'll come with."
            scene w3_11293 with dissolve
            mina "N-no, you don't have to--"
            scene w3_11292 with dissolve
            hana "Come on! That's what girls do, right? Go to the bathroom together? I want to try it on for size."
            scene w3_11294 with dissolve
            mina "...okay. Hehe, sure."
            jer "Why am I included in this?"
        else:
            scene w3_11295 with dissolve
            mina "Really? That wasn't very nice..."
            scene w3_11296 with dissolve
            jer "Hey! He didn't complain."
            scene w3_11297 with dissolve
            hana "Shit. What's with you today? You're not normally so catty."
            scene w3_11298 with dissolve
            jer "Aw, fuck, I don't know. I'm just kidding, you know? Mostly. Work up on the wrong side of the air mattress."
            scene w3_11299 with dissolve
            hana "Oh, I actually wanted to mention something about that... we should look into getting a place together."
            scene w3_11300 with dissolve
            jer "What about your mom?"
            scene w3_11299 with dissolve
            hana "That's part of it. I'm thinking about moving her into a bigger place..."
            scene w3_11300 with dissolve
            jer "Since when can you afford something like that?"
            scene w3_11301 with dissolve
            hana "I, uh... Dad's being a bit more generous."
            scene w3_11302 with dissolve
            jer "Fuck that! Don't take that creep's money!"
            scene w3_11301 with dissolve
            hana "You don't get it, Jer. You don't... you don't live with it. Fuck pride."
            scene w3_11303 with dissolve
            jer "I can't argue against that."
            scene w3_11304 with dissolve
            hana "Ah, you probably have no idea what we're talking about. Sorry."
            scene w3_11305 with dissolve
            mina "Hehe, that's alright! I didn't want to interrupt. Sounded like you were having a moment..."
            scene w3_11304 with dissolve
            hana "Yeah, but let's include you in on some of that. I'm hoping you two will get to know each other better..."
    else:

        scene w3_11299 with dissolve
        hana "Speaking of vans... I actually wanted to mention something about that... I think we should look into getting a place together."
        scene w3_11300 with dissolve
        jer "What about your mom?"
        scene w3_11299 with dissolve
        hana "That's part of it. I'm thinking about moving her into a bigger place..."
        scene w3_11300 with dissolve
        jer "Since when can you afford something like that?"
        scene w3_11301 with dissolve
        hana "I, uh... Dad's being a bit more generous."
        scene w3_11302 with dissolve
        jer "Fuck that! Don't take that creep's money!"
        scene w3_11301 with dissolve
        hana "You don't get it, Jer. You don't... you don't live with it. Fuck pride."
        scene w3_11303 with dissolve
        jer "I can't argue against that."
        scene w3_11304 with dissolve
        hana "Ah, you probably have no idea what we're talking about. Sorry."
        scene w3_11305 with dissolve
        mina "Hehe, that's alright! I didn't want to interrupt. Sounded like you were having a moment..."
        scene w3_11304 with dissolve
        hana "Yeah, but lets include you in on some of that. I'm hoping you two will get to know each other better..."

    stop music fadeout 3.0
    scene black with fade
    rose "Hey! Puff, puff, pass!"
    play music "music/jah-jah-bangs.ogg"
    scene w3_11306 with w12
    kil "You look like you've done this before."
    rose "Mmmh-"
    scene w3_11307 with dissolve
    rose "A-aaahh~"
    scene w3_11308 with dissolve
    ver "Once is enough, I--"
    scene w3_11309 with dissolve
    rose "For such a big woman, you're a lightweight."
    scene w3_11310 with dissolve
    ver "...give me that."
    scene w3_11311 with dissolve
    "When Ian returned with some pot, I was equally dubious as the girls... but here we were."
    kil "Haha, now {i}this{/i} is morale building."
    scene w3_11312 with dissolve
    mc "Where'd you get the weed?"
    kil "August has bad knees."
    mc "...really?"
    scene w3_11313 with dissolve
    kil "I doubt it, I've seen some spry shit out of him, but who cares? He's like an old man giving out candy. Just have to ask."
    mc "I'll keep that in mind in case of an emergency..."
    scene w3_11314 with dissolve
    mc "...thanks."
    scene w3_11315 with dissolve
    fel "Ugh, the smell's going to get into my clothes..."
    scene w3_11316 with dissolve
    kil "Would you prefer if I procured you some coke, Princess?"
    scene w3_11315 with dissolve
    fel "{b}No{/b}, I should've worn sweatpants is all."
    scene w3_11317 with dissolve
    fel "Besides... are you 50? Cocaine's not in vogue anymore. It's all pills."
    fel "Pills to keep you thin, pills to keep the party going, and pills..."
    scene w3_11318 with dissolve
    "Felicia inhaled deeply."
    scene w3_11319 with dissolve
    fel "Ah, aaah~ and pills to keep you complacent."
    scene w3_11320 with dissolve
    rose "Thanks for the empty insight, Dr. Shhhhhllut."
    ver "Pfffh, haaa-"
    scene w3_11321 with dissolve
    mc "...she was already kinda drunk when she got here."
    fel "Lovely."
    scene w3_11322 with dissolve
    rose "My turn! Give it here!"
    kil "I know how a circle w--"
    scene w3_11323 with dissolve
    "And so we rotated, taking a hit, and passing it down the line."
    "This went on for a handful of minutes, with all of us gradually loosening up."
    scene w3_11324 with dissolve
    "Veronica and Rosalind got chatty."
    rose "You're not so bad..."
    ver "No... like, ah... I don't know..."
    scene w3_11325 with dissolve
    "While the remaining of us..."
    kil "Hana's my coworker! It's nice to be invited!"
    scene w3_11326 with dissolve
    fel "Awww, it's nice to be invited~ooooh, {b}you should've said no!{/b}"
    scene w3_11325 with dissolve
    kil "Why do I need to say no?!"
    scene w3_11328 with dissolve
    fel "It's just common decency after you fucked around and found out."
    scene w3_11327 with dissolve
    kil "I've been staying clear of her! Don't get on a high horse Felicia, not when you and I are {i}both{/i} at the club."
    scene w3_11328 with dissolve
    fel "You got caught, dude."
    scene w3_11327 with dissolve
    kil "Oh, and it would've been okay if I got away with it?"
    scene w3_11328 with dissolve
    fel "Look, it's not like I can judge you for cheating, but we play different games with different players."
    scene w3_11329 with dissolve
    mc "Jesus Christ, shut the fuck up. You guys are making me anxious."
    scene w3_11330 with dissolve
    "......"
    scene w3_11331 with dissolve
    fel "...sorry."
    scene w3_11332 with dissolve
    kil "Haha! I remember that time you got so high, laid down because you thought you were having a heart attack, and repeated--"
    scene w3_11333 with dissolve
    mc "--I'm not going to be okay. I blame the frappuccino."
    scene w3_11334 with dissolve
    fel "*Sigh* I don't know what I'm even going on about. I'm just a hypocritical bitch..."
    kil "Ah, no... you kinda do have a point..."
    scene w3_11335 with dissolve
    fel "...{i}whatever.{/i} Live your life. It's not like I personally mind you being here."
    kil "...that so?"
    fel "Well..."
    scene w3_11336 with dissolve
    rose "...then I started thinking, the demiurge is real!"
    ver "The what...?"
    scene w3_11337 with dissolve
    rose "The demiurge! But, I don't know... is he really evil? There are a lot of good things in this world, and... are we any different? We're both soul-trapped--"
    ver "What the fuck are you talking about Rose?"
    scene w3_11338 with dissolve
    fel "...the mood certainly changed since you've returned."
    mc "Better than the bickering, that's for sure."
    rose "Oh, no... I think I'm crossfaded."
    ver "How do you know what that means? I don't know what that means."
    scene w3_11339 with dissolve
    hana "There you are, and you're having a party without me! Tsk, tsk! What the fuck?"

    scene w3_11340 with dissolve
    if w3FeliciaMinaThreesomeEnd == True:
        fel "Oh, hey, Kitten!"
    else:
        fel "Oh, hey, sweetheart!"

    scene w3_11341 with dissolve
    mina "Uh, hey, Felicia..."
    "The older blonde and I briefly looked at each other, Mina's lack of enthusiasm being glaringly obvious."
    scene w3_11342 with dissolve
    mina "Haha! Glad you made it! [mcf] told me you had Elias to deal with."
    "Which made sense... as Ian and Mina were not only face to face for the first time tonight, but on the edge of being packed in like sardines in the overcrowded room."
    fel "I'll tell you about it later."
    scene w3_11343 with dissolve
    "The ex-lovers weren't so much looking at each other as they were engaged in a series of scattered glances."
    "The uncharacteristic blip wasn't lost on Hana - after all, she was the one who invited both of them..."
    scene w3_11344 with dissolve
    hana "It's crowded up here. Want to--"
    scene w3_11345 with dissolve
    kil "There's room opening up. I was about to split and find Jacob."
    hana "...yeah? Last I saw he was wandering off somewhere..."
    kil "I'll find him."
    scene w3_11346 with dissolve
    "......"
    scene w3_11347 with dissolve
    kil "...excuse me."
    "And with a conflicted smile, only dragging the moment out a little, my friend slipped past the two twin-tailed compatriots in a bid to play it {b}cool.{/b}"
    scene w3_11348 with dissolve
    hana "So, hot boxing high above the plebs, huh?"
    "Hana spared no focus for that brief stint of awkwardness, instead mercifully moving on as if it never even happened. Yet, without Ian, {i}I{/i} was acutely aware of one fact..."
    scene w3_11349 with dissolve
    hana "Man, you all are a weird bunch at a glance."

    if minaCheat == True and w3HanaDP >=4 == True or w3MinaHotelFucked == True and w3HanaDP >=4 == True:
        "I was now alone with {b}five{/b} women, all of whom I had some form of weird relationship with. "
    else:
        "I was now alone with {b}five{/b} women, most of whom I had some form of weird relationship with."

    scene w3_11350 with dissolve
    mc "...it's going to get even weirder. Sit down and join us."
    scene black with fade
    "If Mina plopping down next to ALL the Carnations gave Hana any pause, she didn't show it."
    scene w3_11351 with fade
    mina "You don't have to sit on the floor, there's room to--"
    scene w3_11352 with dissolve
    hana "And miss my chance to be between your legs?"
    scene w3_11353 with dissolve
    ver "Pah! {b}Gaaaaaay!{/b}"


    if w3VeronicaMinaLezPush == True:
        scene w3_11354 with dissolve
        hana "Oh, and feel free to stroke my hair~ I've always wanted to try something like this."
        "...as Hana prattled, Mina and Veronica shared a look that I was inadvertently and knowingly complicit in."

        if w3RockShowVeroMinaMadeOutExtra == True:
            "They must've gotten close during their time alone up here."
        else:
            "They must've gotten close while Rosalind and I spent time up here."
    else:

        scene w3_11355 with dissolve
        hana "Oh, and feel free to stroke my hair~ I've always wanted to try this position."

    scene w3_11356 with dissolve
    mc "I feel bad for Jerrica. You're acting like you've never had a girlfriend before!"
    hana "Jerrica's {b}Jerrica!{/b} She might choke me out if I gave up my back!"
    scene w3_11351 with dissolve
    mina "Uh... you're joking, right?"
    scene w3_11352 with dissolve
    hana "Half joking... although, I'm usually the one cuddling her. She's more sensitive than she looks. Don't tell her I said that."
    scene w3_11357 with dissolve
    mina "Oh, no, I'm..."
    hana "...don't partake?"
    scene w3_11358 with dissolve
    "......"
    scene w3_11359 with dissolve
    mina "...oh, what the heck. There's no cops around."
    scene w3_11360 with dissolve
    fel "That's the spirit."
    scene w3_11361 with dissolve
    mina "By the way, you came up here to smoke with [mcf] before you even said hi to me?!"
    scene w3_11362 with dissolve
    fel "Sorry, sweet thing. He {i}scooped{/i} me up first."
    scene w3_11363 with dissolve
    rose "...have we met?"
    scene w3_11364 with dissolve
    "......"
    mina "...{b}yes.{/b}"
    scene w3_11365 with dissolve
    "......"
    scene w3_11366 with dissolve
    rose "...I know that. I was just testing you. You're--"
    scene w3_11367 with dissolve
    mina "{i}Mina{/i} - and you're Rosalind, [mcf]'s coworker."
    scene w3_11368 with dissolve
    ver "Co-worker? Ha!"
    scene w3_11369 with dissolve
    "Hana and I both shot Veronica a mean look."
    scene w3_11370 with dissolve
    mina "...huh? Is she not...?"
    scene w3_11371 with dissolve
    hana "She is. She waits table at the club."
    scene w3_11372 with dissolve
    ver "Sorry. I don't know why I laughed... it must've been the pot. I don't even know where [mcf], Hana, or Rosie works."
    scene w3_11373 with dissolve
    "Veronica, clearly not knowing the lies that had been spun to the younger blonde, quickly picked up on our deception."
    scene w3_11374 with dissolve
    mina "...but, you know Felicia?"
    scene w3_11375 with dissolve
    ver "Uh, I've known her tonight..."
    scene w3_11376 with dissolve
    "......"
    scene w3_11377 with dissolve
    mina "...this {i}is{/i} a weird bunch."
    scene w3_11378 with dissolve
    rose "...so you gonna hit that thing or just hog it to yourself?"
    scene w3_11379 with dissolve
    mina "Oh, uh-- {b}right!{/b}"
    scene w3_11380 with dissolve
    "The blonde frantically puffed her cheeks up like a hamster and filled her lungs with smoke."
    "...{i}even that was cute.{/i}"
    scene w3_11381 with dissolve
    mina "Pwwah, aah-! *Cough*"
    scene w3_11382 with dissolve
    mina "*Cough* Ouhaha-- y-your turn!"
    scene w3_11383 with dissolve
    rose "Ha! She handled that better than you!"
    scene w3_11384 with dissolve
    ver "...you're a gremlin."
    "...whatever this vibe is, at least they're not bickering. {i}Thanks, Ian.{/i}"
    "{i}Sorry you can't be here.{/i}"

    if w3RockShowIanTalk == True:
        scene w3_11385 with dissolve
        "He did ask me to tell Mina he wanted to talk..."
        scene w3_11386 with dissolve

        if w3IanMinaTalk == True:
            "I'll find the chance."
        else:
            "...should I find the chance?"
            menu:
                "Why not? (w3IanMinaTalk = True)":
                    $ w3IanMinaTalk = True
                    scene w3_11385 with dissolve
                    "If I find the right chance, sure. I owe Ian as much."
                "Stay out of it.":
                    if w3MinaHotelFucked == True:
                        "I shouldn't rock the boat. I've got a good thing going with Mina."
                    else:
                        "...I'm not going to rock the boat."


    scene w3_11387 with dissolve
    mina "Oh, by the way! You two haven't been introduced yet, right?"

    if hanaGF == True and w3MinaHotelFucked == True:
        "...then again, I'm not sure if I even want to be here. So far so good, but Hana was my girlfriend and Mina...."
    elif hanaMinaFlag == True:
        "...then again, Hana and Mina are getting chummy and I'm banging both of them."
    else:
        pass

    scene w3_11388 with dissolve
    fel "...no, but Mina's talked about you."

    if hanaGF == True and w3MinaHotelFucked == True:
        "...is my side piece, I guess."
    elif hanaMinaFlag == True:
        mct "(The future is wide open and a man can dream...)"
    else:
        pass

    scene w3_11389 with dissolve
    mina "Felicia's a good friend of mine. I've done some work with her husband's modeling agency."
    scene w3_11390 with dissolve
    hana "Uh... cool to meet 'ya, Felicia."
    fel "You... likewise. Nice drumming up there. I caught the end of it."
    hana "...{i}thanks.{/i} It's a hobby."
    scene w3_11391 with dissolve
    fel "...what do you do for a living? From the sound of it, you work with [mcf] and Rose?"
    "I wasn't sure if Felicia was just acting natural or having a go, but Hana answered convincingly."
    scene w3_11392 with dissolve
    hana "Yep! I bartend."
    scene w3_11391 with dissolve
    fel "Oh, cool! I've done a little bit of that."
    scene w3_11393 with dissolve
    mc "...uh huh, and now everyone knows each other. The world gets smaller."
    "Poor Mina. I nudged us beyond this charade."
    scene w3_11394 with dissolve
    rose "How far do you think you could throw me?"
    scene w3_11395 with dissolve
    ver "...uh, farther than you could throw me?"
    scene w3_11396 with dissolve
    rose "...don't underestimate a mom. We can lift cars!"

    if w3MinaHotelFucked == True:
        scene w3_11397 with dissolve
        mina "Oh! You have a kid! That must be... [mcf] told me you were staying with him, cause of uh... {i}issues.{/i} Does that mean...?"
        scene w3_11398 with dissolve
        mc "She's at camp."
        rose "What?! She knows about me?!"

    scene w3_11397 with dissolve
    mina "...I've always wondered something. Ian's uncle's \"lounge\"... it's not a strip club, right?"
    scene w3_11399 with dissolve
    rose "Is she saying I look like a stripper?"
    scene w3_11400 with dissolve
    fel "Take it as a compliment. You look young for a single mother."
    rose "I--"
    scene w3_11401 with dissolve
    mc "No. It's more like a... social {i}lodge{/i}. You know, old guys, robes, rituals, blah blah blah."
    scene w3_11402 with dissolve
    mina "That makes it sound even weirder."
    "Hana and I briefly shared a look, acknowledging that we had been playing with fire."
    scene w3_11403 with dissolve
    hana "You have no idea. Old fucks roleplaying."
    scene w3_11404 with dissolve
    mc "What makes you think that...?"
    hana "Yeah, you think {i}I'm{/i} a stripper?"
    scene w3_11405 with dissolve
    mina "No! Those... those need bartenders too!"
    mina "You... you could be if you wanted to, though! Not saying you don't have the body for it!"
    scene w3_11406 with dissolve
    rose "Pffh! It's not a strip club! It's a brothel!"
    scene w3_11407 with dissolve
    "......"
    "...\"crossfaded\" Rosalind {i}was{/i} a gremlin."
    scene w3_11408 with dissolve
    mina "Haha, yeah, {b}right!{/b}"
    rose "She doesn't believe me..."
    ver "There, there..."
    scene w3_11409 with dissolve
    mina "Blah! I was just curious! With [mcf] and Hana, there's been a lot of people in my life who work there and I don't even know where it is."
    scene w3_11410 with dissolve
    hana "Trust me, there's nothing interesting about the place, but... eh, I could send you some pictures of what it looks like if you're so curious!"
    mina "Oh... that's not necessary..."
    scene w3_11411 with dissolve
    "Hana and I shared yet another glance, this time I could tell she was displeased at having to lie to her new friend."
    scene w3_11412 with dissolve
    hana "Hey! What about a tour!"
    scene w3_11413 with dissolve

    if hanaFlag == True:
        mc "That... that didn't go over so hot with Jerrica and Spider."
        hana "I had less pull then."
    else:
        mct "(...she's bluffing, {i}right?{/i})"

    scene w3_11414 with dissolve
    mina "No, no, no... that's not necessary either."
    hana "Then..."
    scene w3_11415 with dissolve
    hana "...then you'll just always have to wonder."
    scene w3_11416 with dissolve
    hana "{i}Maybe it is a brothel.{/i}"
    scene w3_11417 with dissolve
    "......"
    scene w3_11418 with dissolve
    mina "...I almost believed you."
    scene w3_11419 with dissolve
    hana "Hey! Dance with me!"
    scene w3_11420 with dissolve
    "So that was how Hana dodged the question, chest-to-chest with the younger blonde."
    "The rest of us sat back, laughing and having a good time."
    scene black with fade
    "........."
    "......"
    scene w3_11421 with circlewipe
    ver "...what the hell do you think you're doing?"
    scene w3_11422 with dissolve
    rose "Wrestling!"
    scene w3_11421 with dissolve
    ver "This isn't the kind of tumbling I like to do with women."
    scene w3_11422 with dissolve
    rose "Oh, I know all about that!"
    stop music fadeout 3.0
    scene w3_11423 with wipeleft
    "...we gave the tumbling gals some room."
    mina "...holy shit. When she said she wanted to wrestle, I thought she was kidding."
    mc "Haha, so did Veronica, it seems."

    play music "music/smooth-and-cool.ogg"
    if w3VeronicaMinaLezPush == True:
        jump w3RSMinaEndingTalkLezVersion
    elif w3IanMinaTalk == True:
        jump w3RSMinaEndingTalkIanVersion
    else:
        jump w3RSMinaEndingTalk

label w3RSMinaEndingTalkLezVersion:
    scene w3_11424 with dissolve
    "......"
    scene w3_11425 with dissolve
    mc "Speaking of which, how did that go?"
    scene w3_11426 with dissolve
    mina "...I don't know what got into me."
    scene w3_11427 with dissolve
    mc "Ho'oh! Must've been something."

    if w3RockShowVeroMinaMadeOutExtra == True:
        scene w3_11428 with dissolve
        "Mina leaned in, sharing with me the details."

        scene rslez_05_a with pixellate
        show rslez_05
        "........."
        "......"
        scene w3_11427 with pixellate
        mc "...you let it get that far?"
        scene w3_11429 with dissolve
        mina "Mmhmm."
        "She looked... {i}proud?{/i}"
    else:
        scene w3_11426 with dissolve
        mina "We kissed a little bit, had a nice talk..."
        mina "It was... {i}exciting.{/i}"

    scene w3_11430 with dissolve
    mc "You going to explore that more?"
    scene w3_11426 with dissolve
    mina "I don't know..."
    scene w3_11430 with dissolve
    mc "You want to. I can tell."
    scene w3_11429 with dissolve
    "..."

    if w3MinaHotelFucked == True and w3VeroBarDate == True:
        scene w3_11431 with dissolve
        "I shared my own desire with the blushing blonde."
        scene w3_11432 with dissolve
        mina "...you think she'd be up for that?"
        scene w3_11433 with dissolve
        mc "I think she wouldn't turn down the chance to take it further with you, even if I was there..."
        scene w3_11432 with dissolve
        mina "I should've known you had something like that in mind when you encouraged me to flirt with her."
        scene w3_11433 with dissolve
        mc "I'll leave the ball in your court. Set something up with her if you want."
    else:
        scene w3_11434 with dissolve
        mc "Good job tonight."
        mina "Shush! That's a weird way to put it!"

    scene w3_11435 with cmet
    ver "...okay, you asked for it!"
    rose "B'wwahh?!"

    if w3IanMinaTalk == True:
        scene w3_11436 with dissolve
        mc "...by the way, Ian wants to talk to you."
        scene w3_11437 with dissolve
        mina "...he could've approached me all night."
        scene w3_11438 with dissolve
        mc "...he's ashamed."
        scene w3_11437 with dissolve
        mina "Good, and I have no desire to speak to him."
        scene w3_11438 with dissolve
        mc "Alright, well... I did what he asked. You don't owe him anything."
        scene w3_11439 with dissolve
        "......"
        scene w3_11440 with dissolve
        mina "...what did he want to talk about?"
        scene w3_11441 with dissolve
        mc "He wants to apologize."
        scene w3_11440 with dissolve
        mina "He just wants to screw with my head."
        scene w3_11441 with dissolve
        mc "I... {i}I don't think so.{/i}"
        scene w3_11437 with dissolve
        mina "...this oughta be good."
        scene w3_11438 with dissolve
        mc "You'll talk to him...?"
        scene w3_11437 with dissolve
        mina "Why not? Afraid I'll go running back into his arms?"
        scene w3_11438 with dissolve
        mc "I wouldn't insult you like that."

        if w3MinaHotelFucked == True:
            scene w3_11442 with dissolve
            mc "...besides, {b}I'm better.{/b}"
            mina "...you sound just like him."
        else:
            mc "You've got self-respect."
            scene w3_11443 with dissolve
            mina "Thanks, [mcf]."
    else:


        scene w3_11436 with dissolve
        mc "...things are heating up. I think Rosalind might need a little help."
        scene w3_11444 with dissolve
        mina "Haha, {i}I'll tag myself in.{/i}"


    scene w3_11445 with dissolve
    mc "...hm?"
    scene w3_11446 with dissolve
    mina "Is something the matter?"
    scene w3_11447 with dissolve
    mc "Just a couple missed calls."
    scene w3_11445 with dissolve
    mct "(Mom left a voice mail.)"
    scene w3_11448 with dissolve
    mc "...do you mind if I--?"
    mina "Go ahead."
    mc "Thanks."
    scene black with fade
    "..."
    jump w3RockShowVickyCall


label w3RSMinaEndingTalkIanVersion:
    scene w3_11449 with dissolve
    mina "...tonight's been fun."
    scene w3_11450 with dissolve
    mc "I'm glad."
    scene w3_11451 with dissolve
    mina "Haha, things are looking up for Mina!"

    if w3MinaHotelFucked == True:
        scene w3_11450 with dissolve
        mc "Exactly. You've got me for one."

        if w3RockShowMinaBarEnding == True:
            scene w3_11449 with dissolve
            mina "Hmm... our first date..."
            scene w3_11452 with dissolve
            "Mina got lost in thought."
            scene w3_11453 with dissolve
            mina "...don't get too serious about me."
            scene w3_11452 with dissolve
            "She looked hopeful to the contrary."
            scene w3_11453 with dissolve
            mina "Let's take it one day at a time..."
            scene w3_11454 with dissolve
            mc "Whatever you say."

        elif hanaMinaFlag == True:
            scene w3_11455 with dissolve
            "......"
            scene w3_11456 with dissolve
            mina "...for now."
            scene w3_11457 with dissolve
            mc "What's with that look?"
            scene w3_11458 with dissolve
            mina "You and Hana looked good tonight. On stage, I mean... {i}kissing...{/i}"

            if w3MinaTransparent == True:
                scene w3_11457 with dissolve
                mc "...I told you about her and I, right?"

                if w3MinaRockShowKiss == True:
                    scene w3_11456 with dissolve
                    mina "You did... but you also asked me not to call that guy."
                    scene w3_11457 with dissolve
                    mc "...I admit the hypocrisy."
                    scene w3_11456 with dissolve
                    mina "...heh, I get it. Hana's great."
                    scene w3_11459 with dissolve
                    mc "Don't compare."
                    scene w3_11458 with dissolve
                    mina "...how can I not?"
                else:
                    scene w3_11458 with dissolve
                    mina "You did. I'm just more aware of the little triangle we've got going after tonight..."
            else:

                scene w3_11457 with dissolve
                mc "You and I are keeping it casual, aren't we? After my birthday, it just sort of--"
                if w3MinaRockShowKiss == True:
                    scene w3_11458 with dissolve
                    mina "Absolutely. {i}Casual.{/i}. It's just... you also asked me not to call that guy."
                    scene w3_11459 with dissolve
                    mc "...I can see the hypocrisy."
                    scene w3_11458 with dissolve
                    mina "*Sigh* ...Hana's great, isn't she?"
                    scene w3_11459 with dissolve
                    mc "Don't compare."
                    scene w3_11458 with dissolve
                    mina "...how can I not?"
                else:
                    scene w3_11456 with dissolve
                    mina "I'm not mad. Just..."

            scene w3_11457 with dissolve
            mc "You're worried it's going to end messy."
            scene w3_11456 with dissolve
            mina "Kinda. I do like you both. Hana as a friend and you as a.... {i}point is{/i}, we're only human. Realistically speaking {i}someone{/i} will get unhappy..."
            scene w3_11459 with dissolve
            mc "What are you saying?"
            scene w3_11458 with dissolve
            mina "Just something to think about I guess..."

            if w3FeliciaMinaThreesomeEnd == True:
                scene w3_11459 with dissolve
                mc "You didn't have this issue with Felicia."
                scene w3_11458 with dissolve
                mina "Felicia is Felicia."

            scene w3_11455 with dissolve
            "........."
            "......"
            scene w3_11456 with dissolve
            mina "...s-sorry, I don't mean to be a downer."
            scene w3_11457 with dissolve
            mc "No. You're right. It's something to bear in mind."

            if hanaGF == True:
                scene w3_11455 with dissolve
                mct "(That and she doesn't know Hana is my girlfriend girlfriend...)"
        else:
            scene w3_11451 with dissolve
            mina "...heheh, and here's hoping for more to come!"
            scene w3_11450 with dissolve
            mc "I'm not going anywhere."
    else:

        scene w3_11450 with dissolve
        mc "Neither of us should complain, should we?"
        scene w3_11451 with dissolve
        mina "Haha, that doesn't stop anyone!"

    scene w3_11435 with cmet
    ver "...okay, you asked for it!"
    rose "B'wwahh?!"
    scene w3_11436 with dissolve
    mc "...by the way, Ian wants to talk to you."
    "This was as good of a time as any to bring this up."
    scene w3_11437 with dissolve
    mina "...he could've approached me all night."
    scene w3_11438 with dissolve
    mc "He's ashamed, I think."
    scene w3_11437 with dissolve
    mina "Good, but I have no desire to speak to him."
    scene w3_11438 with dissolve
    mc "Alright, well... I did what he asked. Told you about it. You don't owe him anything, Mina."
    scene w3_11439 with dissolve
    "......"
    scene w3_11440 with dissolve
    mina "...what did he want to talk about?"
    scene w3_11441 with dissolve
    mc "He wants to apologize."
    scene w3_11440 with dissolve
    mina "He just wants to screw with my head."
    scene w3_11441 with dissolve
    mc "I... {i}I don't think so.{/i} I think he means it."
    scene w3_11440 with dissolve
    mina "You'd be the one able to tell..."
    scene w3_11441 with dissolve
    mc "{b}I would.{/b}"
    scene w3_11437 with dissolve
    mina "...this oughta be good."
    scene w3_11438 with dissolve
    mc "You'll talk to him...?"
    scene w3_11437 with dissolve
    mina "Why not? Afraid I'll go running back into his arms?"
    scene w3_11438 with dissolve
    mc "I wouldn't insult you like that."

    if w3MinaHotelFucked == True:
        scene w3_11442 with dissolve
        mc "...besides, {b}I'm better.{/b}"
        mina "...pffh, you're more like Ian than you think."
    else:
        mc "You've got self-respect."
        scene w3_11443 with dissolve
        mina "Thanks, [mcf]."

    scene w3_11445 with dissolve
    mc "...hm?"
    scene w3_11446 with dissolve
    mina "Is something the matter?"
    scene w3_11447 with dissolve
    mc "Just a couple missed calls."
    scene w3_11445 with dissolve
    mct "(Mom left a voice mail.)"
    scene w3_11448 with dissolve
    mc "...do you mind if I--?"
    mina "Go ahead."
    mc "Thanks."
    scene black with fade
    "..."
    jump w3RockShowVickyCall


label w3RSMinaEndingTalk:
    scene w3_11449 with dissolve
    mina "...tonight's been fun. Like I couldn't imagine."
    scene w3_11450 with dissolve
    mc "I'm glad."
    scene w3_11451 with dissolve
    mina "Haha, things are looking up for Mina!"

    if w3MinaHotelFucked == True:
        scene w3_11450 with dissolve
        mc "Exactly. You've got me for one."

        if w3RockShowMinaBarEnding == True:
            scene w3_11449 with dissolve
            mina "Hmm... our first date..."
            scene w3_11452 with dissolve
            "Mina got lost in thought."
            scene w3_11453 with dissolve
            mina "...don't get too serious about me."
            scene w3_11452 with dissolve
            "She looked hopeful to the contrary."
            scene w3_11453 with dissolve
            mina "Let's take it one day at a time..."
            scene w3_11454 with dissolve
            mc "Whatever you say."

        elif hanaMinaFlag == True:
            scene w3_11455 with dissolve
            "......"
            scene w3_11456 with dissolve
            mina "...for now."
            scene w3_11457 with dissolve
            mc "What's with that look?"
            scene w3_11458 with dissolve
            mina "You and Hana looked good tonight. On stage, I mean... {i}kissing...{/i}"

            if w3MinaTransparent == True:
                scene w3_11457 with dissolve
                mc "...I told you about her and I, right?"

                if w3MinaRockShowKiss == True:
                    scene w3_11456 with dissolve
                    mina "You did... but you also asked me not to call that guy."
                    scene w3_11457 with dissolve
                    mc "...I admit the hypocrisy."
                    scene w3_11457 with dissolve
                    mina "...heh, I get it. Hana's great."
                    scene w3_11459 with dissolve
                    mc "Don't compare."
                    scene w3_11458 with dissolve
                    mina "...how can I not?"
                else:
                    scene w3_11456 with dissolve
                    mina "You did. I'm just more aware of the little triangle we've got going after tonight..."
            else:

                scene w3_11457 with dissolve
                mc "You and I are keeping it casual, aren't we? After my birthday, it just sort of--"
                if w3MinaRockShowKiss == True:
                    scene w3_11458 with dissolve
                    mina "Absolutely. {i}Casual.{/i}. It's just... you also asked me not to call that guy."
                    scene w3_11459 with dissolve
                    mc "...I can see the hypocrisy."
                    scene w3_11456 with dissolve
                    mina "*Sigh* ...Hana's great, isn't she?"
                    scene w3_11459 with dissolve
                    mc "Don't compare."
                    scene w3_11458 with dissolve
                    mina "...how can I not?"
                else:
                    scene w3_11456 with dissolve
                    mina "I'm not mad. Just..."

            scene w3_11457 with dissolve
            mc "You're worried it's going to end messy."
            scene w3_11456 with dissolve
            mina "Kinda. I do like you both, Hana as a friend and you as a.... {i}point is{/i}, we're only human. Realistically speaking {i}someone{/i} will get unhappy..."
            scene w3_11457 with dissolve
            mc "What are you saying?"
            scene w3_11458 with dissolve
            mina "Just something to think about I guess..."

            if w3FeliciaMinaThreesomeEnd == True:
                scene w3_11459 with dissolve
                mc "You didn't have this issue with Felicia."
                scene w3_11458 with dissolve
                mina "Felicia is Felicia."

            scene w3_11455 with dissolve
            "........."
            "......"
            scene w3_11456 with dissolve
            mina "...s-sorry, I don't mean to be a downer."
            scene w3_11457 with dissolve
            mc "No. You're right. It's something to bear in mind."

            if hanaGF == True:
                scene w3_11455 with dissolve
                mct "(That and she doesn't know Hana is my girlfriend...)"
        else:
            scene w3_11449 with dissolve
            mina "...heheh, and here's hoping for more to come!"
            scene w3_11450 with dissolve
            mc "I'm not going anywhere."
    else:

        scene w3_11450 with dissolve
        mc "Neither of us should complain, should we?"
        scene w3_11451 with dissolve
        mina "Haha, that doesn't stop anyone!"


    scene w3_11435 with cmet
    ver "...okay, you asked for it!"
    rose "B'wwahh?!"
    scene w3_11436 with dissolve
    mc "...things are heating up. I think Rosalind might need a little help."
    scene w3_11444 with dissolve
    mina "Haha, {i}I'll tag myself in.{/i}"
    scene w3_11445 with dissolve
    mc "...hm?"
    scene w3_11446 with dissolve
    mina "Is something the matter?"
    scene w3_11447 with dissolve
    mc "Just a couple missed calls."
    scene w3_11445 with dissolve
    mct "(Mom left a voice mail.)"
    scene w3_11448 with dissolve
    mc "...do you mind if I--?"
    mina "Go ahead."
    mc "Thanks."
    scene black with fade
    "..."
    jump w3RockShowVickyCall



label w3RockShowVickyCall:
    scene w3_11460 with fade
    "The voicemail didn't alleviate my concern."
    vic "Hey, uh... ah... you're out having fun. Uh, be safe! L-love you."
    scene w3_11461 with dissolve
    "I knew from her tone and the way fumbled her words that something was amiss."
    scene w3_11462 with dissolve
    play ambient "sound effects/ringing-outbound.mp3"
    "So I called."
    scene w3_11463 with dissolve
    "........."
    "......"
    play sound "sound effects/phonemenu.wav"
    stop ambient
    vic "...heeeeeey!"
    scene w3_11464 with dissolve
    mc "Hey, I got your voice mail. That was weird."
    scene w3_11463 with dissolve
    vic "Haaa... what are you up to, son?"
    scene w3_11464 with dissolve
    mc "I'm out at a rock club in the city with Ian!"
    scene w3_11463 with dissolve
    vic "Ian! Ian, Ian, Ian! Haaa, hnnngg."
    scene w3_11465 with dissolve
    mc "Are you drunk...?"
    scene w3_11466 with dissolve
    vic "It's Friday night!"
    "That was unusual. My mom was a social drinker, I'd rarely, {i}very rarely{/i}, seen her drink alone."
    vic "Ian... haaa... he should probably know too."
    scene w3_11465 with dissolve
    mc "What should he know?"
    scene w3_11466 with dissolve
    vic "I, eeeeey... I've got something to tell you. Something... b-big..."
    scene w3_11464 with dissolve
    mc "You already told me you're thinking about selling the house."
    scene w3_11463 with dissolve
    vic "Bigger than that..."
    scene w3_11467 with dissolve
    "{i}Oh.{/i}"
    "Fucking {b}oh.{/b}"
    vic "I don't know, I don't know... just forget I called!"
    "My stomach dropped."
    scene w3_11468 with dissolve
    mc "That's not how that works, Mom. You know that."
    scene w3_11469 with dissolve
    vic "I know... that's how your head works. Can't put the lid back on the bottle."
    vic "Maybe I was counting on that... like getting a little push off the diving board."
    scene w3_11468 with dissolve
    mc "What's wrong? Tell me."
    scene w3_11469 with dissolve
    vic "I can't think straight right now. The wine isn't helping."
    scene w3_11468 with dissolve
    mc "Then stop drinking."
    scene w3_11469 with dissolve
    vic "Mmh, don't want to."
    "........."
    "......"
    vic "...hey, sweetie. Could you and Ian come over?"
    scene black with fade
    "That was all she had to say."

    if w3IanMinaTalk == True:
        scene w3_11470 with dissolve
        "I found Ian alongside Mina, no doubt interrupting whatever it was he had to say to his jilted lover."
        scene w3_11471 with dissolve
        kil "What's up?"
        scene w3_11472 with dissolve
        mc "We need to go to Mom's."
        scene w3_11473 with dissolve
        "........."
        "......"
        scene w3_11474 with dissolve
        kil "...okay."
        scene w3_11475 with dissolve
        "He knew my tone and recognized that I wasn't asking."
        scene w3_11476 with dissolve
        mina "Is everything okay?"
        mc "Sorry to interrupt."
        scene w3_11477 with dissolve
        mina "...?"
        kil "We'll continue this talk some other time?"
        mina "...sure."
        "Mina looked confused, but that wasn't my problem."
        stop music fadeout 3.0
        scene black with fade
        "I bid a quick goodbye to the lot, and off we went."
        "......"
        "..."
        jump w3VickyTruth
    else:
        scene w3_11478 with dissolve
        "I found Ian at the bar, thankfully not drinking a drop."
        scene w3_11479 with dissolve
        kil "What's up?"
        scene w3_11480 with dissolve
        mc "We need to go to Mom's."
        scene w3_11481 with dissolve
        "........."
        "......"
        scene w3_11482 with dissolve
        kil "...okay."
        "He knew my tone and recognized that I wasn't asking."
        stop music fadeout 3.0
        scene black with fade
        "I bid a quick goodbye to the lot, and off we went."
        "......"
        "..."
        jump w3VickyTruth


label w3VickyTruth:
    play ambient "sound effects/car-loop.wav"
    scene rs_iancar_a with blinds
    show rs_iancar
    "Ian saved his questions for the car ride, but I didn't have any answers."
    "I simply explained the odd tone and my mother's request."
    "Naturally, my head was spinning as fast as the tires that carried us to the suburbs."
    mct "(...something big she had to tell me?)"
    "My mind, as I'm sure Ian's did, went to what Alice had told him earlier."
    mct "(Pale as a ghost...)"
    "I didn't like this."
    "I didn't like this one bit."
    stop ambient fadeout 2.0
    scene black with fade
    play sound "sound effects/door-openclose.wav"
    "When I got there, I let myself in."
    mc "Mom....?"
    play music "music/st-francis.ogg"
    scene w3_11483 with blinds
    vic "Ah... I was hoping I dreamed our conversation."
    "What I found was a disheveled version of my mother, eyelashes stained with tears."
    scene w3_11484 with dissolve
    mc "No... wasn't... it wasn't a dream..."
    mc "You asked for us to come over."
    scene w3_11485 with dissolve
    "........."
    "......"
    scene w3_11486 with dissolve
    kil "...coffee! I'll get coffee."
    "It was at times like this that I loved that man. He was full of genuine concern, yet he pushed forward to give me the space to do what I needed to do."
    scene w3_11487 with dissolve
    mc "Ha! So what's all this about?"
    scene w3_11488 with dissolve
    "I was nervous, so I forced a laugh, hoping I might will the shoe not to drop. She was trying to hide it, but it had been a long time since I had seen her so fraught."
    scene w3_11489 with dissolve
    vic "F-first of all, I'm not dying, so... let's keep things in perspective."
    scene w3_11490 with dissolve
    mc "That's a hell of a preface, Mom..."
    scene w3_11491 with dissolve
    "........."
    "......"
    scene w3_11492 with dissolve
    mc "...what's wrong?"
    scene w3_11493 with dissolve
    "...she winced?"
    "My touch bothered her?"
    scene w3_11494 with dissolve
    vic "O-oh!"
    scene w3_11495 with dissolve
    "She immediately picked up on my reaction."
    scene w3_11496 with dissolve
    vic "I... it's not... if I say..."
    scene w3_11497 with dissolve
    mc "I love you Mom. Take your time."
    scene w3_11496 with dissolve
    vic "It's just if I say what's on my mind, you might not ever want to touch me again."
    scene w3_11497 with dissolve
    mc "Don't be stupid, what are you--"
    scene w3_11498 with dissolve
    "........."
    "......"
    scene w3_11499 with dissolve
    "...oh, fuck."
    "......"
    scene w3_11500 with dissolve
    vic "I've got some stuff... I... I'm not proud of it, but also I'm not-- I mean..."
    scene w3_11499 with dissolve
    "Oh fuck, oh fuck, oh fuck, OH FUCK...!"
    scene w3_11500 with dissolve
    vic "I've got something to tell you that's gonna make you think less of me. P-probably even disgust you, but--"
    scene w3_11501 with dissolve
    mc "{b}No.{/b}"
    scene w3_11502 with dissolve
    "Just... {i}no.{/i}"
    "What the fuck? What the fuck? WHAT THE FUCK?"
    "WHY. {b}NOW?!{/b} What compelled--"
    scene w3_11503 with dissolve
    "Shut the fuck up brain. No time for that, I needed--"
    scene w3_11504 with dissolve
    mc "First of all: there is NOTHING you could do that will EVER make me love you one ounce less."
    scene w3_11505 with dissolve
    "Whatever brought this on did not matter right now. I needed to make sure she understood that simple truth."
    scene w3_11504 with dissolve
    mc "I'd never, and I mean NEVER, look at you with anything other than the same affection and love you have gifted me."
    scene w3_11506 with dissolve
    vic "You say that, but--"
    scene w3_11507 with dissolve
    mc "There's no fucking {b}buts!{/b} You could drive a school bus of orphans off a cliff and you'd still be my mother."
    scene w3_11508 with dissolve
    vic "I-- that's easy to say..."
    scene w3_11507 with dissolve
    mc "...did you ever stop loving me when I made life difficult for you?"
    scene w3_11508 with dissolve
    vic "That's different..."
    scene w3_11507 with dissolve
    mc "No it isn't, and whatever it is you want to say..."
    "I never wanted to hear these words from her lips, but if I were to, this wasn't the time."
    scene w3_11509 with dissolve
    mc "...t-tell me when you're sober."
    scene w3_11510 with dissolve
    "My voice cracked."
    scene w3_11511 with dissolve
    vic "I... I don't think I can do that..."
    scene w3_11512 with dissolve
    mc "Think about it. If it's so important... {i}you have to.{/i}"
    mc "Have a good night's rest, and if you still have something to get off your chest under the light of day, I'll listen. {b}Without{/b} judgement."
    scene w3_11511 with dissolve
    vic "[mcf]..."
    scene w3_11512 with dissolve
    mc "...but, and I can't emphasize this enough, {b}you don't need to.{/b} We're all entitled to our pasts."
    scene w3_11513 with dissolve
    vic "...w-what?! Y-you know! Y-you know already, don't you...?"
    "A spark of realization washed the drunkenness from her eyes."
    scene w3_11514 with dissolve
    "One that I hoped she'd forget in the morning."
    scene w3_11515 with dissolve
    mc "Just working off context clues. All I actually know is that I love you."
    scene w3_11514 with dissolve
    "........."
    "......"
    scene w3_11516 with dissolve
    "...if she didn't believe it, she nevertheless accepted that."
    scene w3_11517 with dissolve
    vic "I didn't... I didn't do a bad job..."
    vic "I, I, I..."
    scene w3_11518 with dissolve
    mc "{b}I love you.{/b}"
    scene w3_11519 with dissolve
    "........."
    "......"
    scene w3_11520 with dissolve
    kil "...?"
    scene w3_11521 with dissolve
    "Whatever fucking prompted this, there was {b}another{/b} thing I had to make sure she understood."
    scene w3_11522 with dissolve
    "The love she put out in the world wasn't just reflected in me."
    mc "...dude, why are you crying?"
    scene w3_11523 with dissolve
    kil "I don't know! Just seemed like the mood? I'm confused as hell!"
    scene w3_11522 with dissolve
    vic "...I love you boys."
    "........."
    "......"
    scene w3_11523 with dissolve
    kil "...huh... uh... {i}I love you too.{/i}"
    stop music fadeout 3.0
    scene black with fade
    "...no coffee was had. She willingly went to bed, apologizing for wasting our time."
    "What the fuck, what the fuck, {b}whatthefuckwhatthefuckwhatthefuckwhatthefuckwhatthefuckwhatthefuckwhatthefuck--{/b}"
    play ambient "sound effects/cricket2.wav"
    scene w3_11525 with dissolve
    "Ian hit me with a stern look that stopped my thoughts cold."
    scene w3_11526 with dissolve
    kil "Dude, what was that about?!"
    scene w3_11527 with dissolve
    mc "Uh... don't know."
    scene w3_11528 with dissolve
    kil "Bullshit! What was that about?!"
    kil "You wouldn't leave Vicky alone if you didn't have an inkling! Why the fuck was Vicky crying?!"
    scene w3_11529 with dissolve
    "Ah, shit."
    "{b}Shitshitshitshitshitshitshitshitshitshitshitshitshitshit.{/b}"
    scene w3_11530 with dissolve
    "I--"

    menu:
        "Lie. Lie. Lie your fucking ass off.":
            "I knew what I had to do and it didn't involve Ian."
            scene w3_11531 with dissolve
            mc "...she's selling the house and she's being really sentimental about it."
            scene w3_11532 with dissolve
            "For one, he couldn't handle this information."
            scene w3_11533 with dissolve
            kil "...w-what?"
            scene w3_11534 with dissolve
            mc "She's thinking about selling the house."
            scene w3_11533 with dissolve
            kil "Oh... that's it?"
            scene w3_11534 with dissolve
            mc "That's.. {b}it.{/b}"
            scene w3_11532 with dissolve
            "Second, whatever scared my Mom into potentially confessing, it had to do with Ian's mother. I was sure of that."
            "Looping him into that would be a nightmare."
            scene w3_11535 with dissolve
            mc "...kinda stupid, huh? I didn't realize she was that sentimental."
            scene w3_11536 with dissolve
            kil "Yeah, that surprises me too. I mean, dude, the look on her face tonight that was--"
            scene w3_11537 with dissolve
            "........."
            "......"
            "...he didn't one hundred percent buy it, but I think he was grateful for the simple answer."
            scene w3_11536 with dissolve
            kil "Okay."
            scene w3_11538 with dissolve
            mc "*Sigh* Let's go home. We've got a big night tomorrow."
            kil "That we do..."
            stop ambient fadeout 3.0
            scene black with fade
            "Lie upon lie."
        "Trust him with the truth. (ianVickyTruth = True)"(chg=["killian_up5"]):

            $ Killian_Bromance +=5
            $ ianVickyTruth = True
            play music "music/leaving-home.ogg"
            "My instinct told me to lie, to guard my dear mother's secret, but I didn't want to. All I wanted to do was get to the bottom of this and he could help."
            scene w3_11539 with dissolve
            mc "It's better if you don't know."
            scene w3_11540 with dissolve
            "Still, I cautioned him."
            scene w3_11541 with dissolve
            kil "{b}Fuck you.{/b} Don't keep me in the dark."
            scene w3_11539 with dissolve
            mc "You can't unring this bell."
            scene w3_11541 with dissolve
            kil "I don't care, {b}I don't fucking care!{/b} I've never seen her like that!"
            scene w3_11540 with dissolve
            "I warned him twice for good measure."
            scene w3_11539 with dissolve
            mc "...you really want--"
            scene w3_11542 with dissolve
            kil "{b}Fucking tell me!{/b}"
            scene w3_11543 with dissolve
            mc "You tell me. She had lunch with your mother today and she came back like {i}that.{/i}"
            scene w3_11544 with dissolve
            kil "W-what, I don't know, what could she have possibly--"
            scene w3_11543 with dissolve
            mc "I don't know, but before I convinced her not to, she was about to tell me she did porn when we were growing up."
            scene w3_11545 with dissolve
            kil "...? W-what...? Vicky did-"
            scene w3_11546 with dissolve
            mc "She did."
            scene w3_11545 with dissolve
            kil "No... that ain't funny."
            scene w3_11546 with dissolve
            mc "Look at my face, Ian. If {b}anyone{/b} knows when I'm not joking..."
            scene w3_11547 with dissolve
            kil "No, you {b}are{/b} joking. She's not that kind of..."
            scene w3_11548 with dissolve
            "He got a look."
            mc "Don't--"
            scene w3_11549 with hpunch
            mc "{b}NO!{/b}"
            scene w3_11550 with dissolve
            "He got a {b}rotten fucking look!{/b}"
            scene w3_11549 with dissolve
            mc "Don't. Make. That. Face!"
            scene w3_11551 with dissolve
            "I understood fully just how shocked he must be, but--"
            scene w3_11552 with dissolve
            mc "{b}Please!{/b} I'm begging you!"
            mc "Please...!"
            stop music fadeout 5.0
            scene w3_11554 with dissolve
            "I asked my best friend for that selfish mercy."
            scene w3_11552 with dissolve
            mc "She's the woman she's always been."
            scene w3_11553 with dissolve
            kil "Yeah, b-but..."
            scene w3_11555 with dissolve
            "If either of us tried to speak, I didn't hear."
            "Ian looked to me for understanding, and what I gave him was my unfiltered soul."
            "I pleaded to him with my eyes to reach the same conclusion I had years and years ago."
            "An unfair request given that I had a much longer time to reach that point, but I {i}needed{/i} him there."
            "If we shared a single thing in common, it was a love for that woman."
            "Please, Ian. {b}Confirm that.{/b}"
            "........."
            "......"
            scene w3_11556 with dissolve
            kil "I mean, o-of course she's the same Vicky as yesterday! I'm not gonna think less...! Fuck, no I'm not!"
            scene w3_11557 with dissolve
            "........."
            "......"
            scene w3_11558 with dissolve
            mc "...thank you, {b}brother.{/b}"
            scene w3_11559 with dissolve
            mc "Thank you."
            scene w3_11560 with dissolve
            kil "...fuck you! You've got to give me more here, dude!"
            mc "Haha, there's... there's not a lot to it..."
            scene w3_11561 with dissolve
            "...but I slowly explained the {i}how{/i} and {i}when{/i} I knew."
            "The {i}why{/i} needed no explanation. After all, it was a simple truth. She had sex on camera, for money. For thrill?"
            "We didn't go into that."
            scene w3_11562 with dissolve
            kil "Shit, dude. You sat on it that long?"
            scene w3_11563 with dissolve
            mc "I'm... I'm not going to pretend like it doesn't bother me."
            scene w3_11564 with dissolve
            "......"
            scene w3_11565 with dissolve
            kil "...I mean, we work at a brothel."
            scene w3_11566 with dissolve
            mc "We do. {b}Yeah{/b}. Ha!"
            scene w3_11564 with dissolve
            "......"
            scene w3_11562 with dissolve
            kil "...so, what the fuck happened between Vicky and Mom?"
            scene w3_11563 with dissolve
            mc "I don't know! We--"
            scene w3_11562 with dissolve
            kil "We should ask Vicky directly."
            "He suggested something surprisingly straightforward."
            scene w3_11563 with dissolve
            mc "She doesn't know we know."
            scene w3_11562 with dissolve
            kil "...she's going to tell you."
            scene w3_11563 with dissolve
            mc "...you think so? I'm hoping she doesn't."
            scene w3_11565 with dissolve
            kil "She'll have even more courage in the morning."
            scene w3_11567 with dissolve
            mc "..."
            scene w3_11568 with dissolve
            kil "...you know, a lot of things make sense now. About her life."

            if ianIntrospect == True:
                scene w3_11569 with dissolve
                kil "I'm glad I know."
                mc "...yeah?"
                kil "I think so..."
            else:
                scene w3_11570 with dissolve
                kil "God I wish I didn't know."
                mc "Told you so."
                kil "I'll take this to my grave..."

            stop ambient fadeout 3.0
            scene black with fade
            "We went home."
            "......"
            "..."

    if hanaMinaFlag == True:
        jump w3RockShowHanaMinaParkingLot
    else:
        jump june19End

label w3RockShowHanaMinaParkingLot:
    play sound "sound effects/motorcycle-ride.wav"
    scene w3_11571 with circlewipe
    mina "Seriously, I can call an Uber..."
    hana "I'll save you the cash and drive you home."
    play music "music/modern-situations.ogg"
    scene w3_11572 with dissolve
    mina "What about your bike?"
    scene w3_11573 with dissolve
    hana "Jerrica will pick me up after they finish taking Rosalind home."
    scene w3_11574 with dissolve
    mina "...sorry to impose."
    scene w3_11575 with dissolve
    hana "You're apologizing with a smile."
    scene w3_11576 with dissolve
    mina "I'm happy... thanks for being a friend."
    scene w3_11577 with dissolve
    hana "No problem."
    scene w3_11578 with dissolve
    "........."
    "......"
    scene w3_11579 with dissolve
    mina "...so, you and [mcf] are close."
    scene w3_11580 with dissolve
    hana "We are... we kinda clicked on his birthday..."
    scene w3_11581 with dissolve
    mina "Heh, I know..."
    scene w3_11582 with dissolve
    hana "...you heard us fooling around, didn't you?"
    scene w3_11581 with dissolve
    mina "Maaaaaaybe."
    scene w3_11580 with dissolve
    "......"
    scene w3_11579 with dissolve
    mina "...you really like him?"

    if hanaGF == True:
        scene w3_11580 with dissolve
        hana "I do. It's been a long time since I've had a boyfriend."
        scene w3_11583 with dissolve
        mina "...b-boyfriend?"
        scene w3_11584 with dissolve
        hana "Yeah, we're dating. You didn't know?"
        scene w3_11585 with dissolve
        mina "I, uh... I thought it was a casual thing."
        scene w3_11586 with dissolve
        hana "Me too, but he insisted. He was pretty sweet about it."
        scene w3_11587 with dissolve
        mina "I... uh..."
        hana "What's wrong...?"
        stop music fadeout 3.0
        mina "I, I..."
        scene w3_11588 with dissolve
        mina "My stomach."
        scene w3_11589 with dissolve
        hana "...we should get you home then."
        scene w3_11588 with dissolve
        mina "T-thanks..."
        scene w3_11590 with dissolve
        "........."
        "......"
        scene w3_11591 with dissolve
        mina "...how long have you two been dating?"
        scene w3_11590 with dissolve
        hana "Not long, about--"
        jump june19End
    else:
        scene w3_11592 with dissolve
        hana "...there's something about him I can't place - in a good way."
        scene w3_11593 with dissolve
        mina "I know what you mean..."
        "......"
        scene w3_11594 with dissolve
        hana "...{b}oh.{/b}"
        scene w3_11595 with dissolve
        mina "I don't hold a candle to you."
        scene w3_11596 with dissolve
        hana "The fuck you don't. Like you don't out-punch me."
        scene w3_11597 with dissolve
        "......"
        scene w3_11598 with dissolve
        hana "...got to suck, though. With him being Ian's friend and all, you can't make a move."
        scene w3_11599 with dissolve
        "........."
        "......"
        scene w3_11600 with dissolve
        hana "...{b}oh!{/b}"
        mina "I don't want you to feel jealous! It just sort of happened, what with the shit with Ian and--"
        scene w3_11601 with dissolve
        hana "...no shit?"
        scene w3_11602 with dissolve
        "........."
        "......"
        scene w3_11603 with dissolve
        hana "...well, It's not like we're dating. And... {i}a woman like you...{/i}"
        scene w3_11604 with dissolve
        hana "It makes all the sense in the world why he would, but... why are you telling me this?"
        scene w3_11605 with dissolve
        mina "Because I... I... I don't know?"
        scene w3_11604 with dissolve
        hana "You want to avoid a mess. I get it."
        scene w3_11605 with dissolve
        mina "No, it's..."
        scene w3_11606 with dissolve
        mina "I'm jealous."
        scene w3_11607 with dissolve
        hana "Jealous...? Uh... [mcf] and I, we... there's enough there that I'm not willing to give that up so you can feel better. Sorry."
        scene w3_11608 with dissolve
        mina "N-no! I wouldn't want you to, it's just... {i}I don't know...{/i}"

        if Mina_BiCurious >= 3:
            $ w3RockShowMinaHanaKiss = True
            mina "...do you want me to back off?"
            scene w3_11609 with dissolve
            hana "Like I said... we're not dating, and... I... I like you enough not to ask you to do that."
            scene w3_11610 with dissolve
            mina "Oh! I'm happy to hear that...!"
            scene w3_11611 with dissolve
            "........."
            "......"
            scene w3_11612 with dissolve
            hana "...what are you doing?"
            scene w3_11613 with dissolve
            mina "To be honest, when I saw you two kiss on stage, it put a mean thought in my head..."
            scene w3_11614 with dissolve
            hana "Mina, hey... what are you doing...?"
            scene w3_11613 with dissolve
            mina "L-listen! While I've got the courage to do this...!"
            scene w3_11615 with dissolve
            "......"
            scene w3_11616 with dissolve
            mina "When I saw you two kiss, I wasn't sure who I was jealous of. Of you kissing [mcf], or [mcf] kissing you. Isn't that odd?"
            scene w3_11615 with dissolve
            "........."
            scene w3_11617 with dissolve
            mina "It's just, you're both so... {b}tremendous.{/b} You looked perfect for each other, and... I got to thinking..."
            scene w3_11618 with dissolve
            "........."
            "......"
            scene w3_11617 with dissolve
            mina "I don't know whose shoes I'd rather fill..."
            scene w3_11619 with dissolve
            hana "Hey, Mina, I don't--"
            scene w3_11620 with dissolve
            mina "I admire you. You're the {b}coolest{/b}, Hana."
            stop music fadeout 3.0
            scene w3_11619 with dissolve
            hana "No, I'm... {i}I'm not.{/i} You barely know me... I..."
            play music "music/inner-light.ogg"
            scene rs_hm01_a with dissolve
            show rs_hm01
            pause
            scene w3_11621 with dissolve
            hana "...d-don't read into that. I just went with the flow."
            scene w3_11622 with dissolve
            mina "Good... you can teach me. I need to learn to do that better..."
            scene rs_hm02_a with dissolve
            show rs_hm02
            pause
            play music "music/modern-situations.ogg" fadein 3.0
            scene rs_hm03_a with dissolve
            show rs_hm03
            hana "I'd say you're already pretty goood at it..."
            mina "So... I like [mcf]... {b}you{/b} like [mcf]..."
            mina "Haha, m-maybe... I'm just thinking... since all three of us like each other..."
            hana "Mina... {i}that{/i} isn't going to make things less complicated..."
            mina "I'm not saying we should date, just... we could leave it all out in the open? We're all... {b}friends{/b}."
            mina "Neither of us should feel like we're taking a backseat. Neither of us has to feel {b}less.{/b} Plus, I bet it would make [mcf] happy..."
            scene w3_11623 with dissolve
            hana "Ha! No shit that dog would be!"
            scene w3_11624 with dissolve
            hana "...bah, give me your keys. Let's go."
            scene w3_11625 with dissolve
            "........."
            "......"
            scene w3_11626 with dissolve
            hana "S-seriously! I'm...! It's not like I'm a prude either! Some of what you're saying makes sense, but the last time I was with a chick, I just felt like a cheap whore after! And not in a good way!"
            scene w3_11627 with dissolve
            hana "So, let's go home, okay...? We can... we can talk about this later when you're less tipsy."
            scene w3_11628 with dissolve
            "......"
            scene w3_11629 with dissolve
            mina "I can't believe I just did that."
            scene w3_11630 with dissolve
            hana "Bullshit. You're used to getting what you want."
            scene w3_11631 with dissolve
            mina "Haha, NOT untrue, so..."
            scene w3_11632 with dissolve
            hana "No more kissing tonight."
            scene w3_11633 with dissolve
            mina "...have I told you how cool you are?"
            scene w3_11632 with dissolve
            hana "*Sigh* Let's get your prissy ass home."
            scene w3_11645 with dissolve
            "..."
            stop music fadeout 3.0
            scene black with fade
            "......"
            if not persistent.w3HanaMinaLez:
                play sound "sound effects/notification.wav"
                show memoryunlock with dissolve
                $ renpy.pause(3, hard=True)
                $ persistent.w3HanaMinaLez = True
            "..."
            $ renpy.end_replay()
            jump june19End
        else:

            mina "...do you want me to back off?"
            scene w3_11607 with dissolve
            hana "Like I said... we're not dating."
            scene w3_11606 with dissolve
            mina "I know from personal experience that doesn't mean feelings aren't involved."
            scene w3_11607 with dissolve
            hana "...yeah, but it is what is. It might not end pretty, but..."
            scene w3_11634 with dissolve
            hana "...shit, I want to get to know you better. I don't want to budge on a thing."
            scene w3_11635 with dissolve
            hana "We have so much in common, including our taste in men apparently."
            scene w3_11636 with dissolve
            mina "...if that's true, does that mean you think Ian's hot?"
            scene w3_11637 with dissolve
            hana "Fuck no! I mean, as far as looks go, I guess--"
            scene w3_11638 with dissolve
            hana "*Sigh* Let's get you home."
            stop music fadeout 3.0
            scene black with fade
            mina "...alright."
            "......"
            "..."
            jump june19End

label june19End:
    play music "music/leaving-home.ogg"
    "When I got home, I felt like shit."
    "What spooked my mother into confessing after all these years?"
    "That question was eating me up inside."
    "I didn't want to think, because if I thought..."
    scene vpt_memory3_a with pixellate
    show vpt_memory3
    "I wouldn't move past this."
    mct "(Seriously...)"
    scene w3_11639 with pixellate
    mct "(Don't think...)"
    "Go to bed, [mcf]."
    scene w3_11641 with dissolve
    mct "(It's on there somewhere...)"
    "In a folder, where one simple click would indulge the nagging desire that plagued me since meeting Donovan yesterday."
    mct "(I {i}could{/i} watch it...)"
    scene w3_11640 with dissolve
    "...but after tonight, how could I?"
    scene w3_11691 with pixellate
    "The sheer desperation on my mother's face."
    "If she knew what I've {i}seen.{/i}"
    scene w3_11640 with pixellate
    "Disgust at me, disgust at herself..."
    scene w3_11642 with dissolve
    "It would be irreparable."
    "............"
    "........."
    "......"
    scene w3_11639 with dissolve

    menu:
        "...delete the videos of your mother.":
            $ vickyVideoDeletus = True
            scene w3_11643 with dissolve
            "This fixation had to end."
            scene w3_11644 with dissolve
            mct "(Did you see her fucking tears, [mcf]?! You fucking prick?!)"
            "I did what I should've done years ago."
            stop music fadeout 3.0
            scene black with fade
            mct "(Now... {b}empty the trash can.{/b})"
            "........."
            "......."
            "..."
            jump w3DreamingOfDad
        "...search for the casting video with Donovan.":


            "Of course, she would never know."
            scene w3_11643 with dissolve
            "As much as it shouldn't, these awful files represented something to me."
            scene w3_11644 with dissolve
            "Deleting them would be letting go of something {i}comforting.{/i}"
            scene black with fade
            "I found it."
            don "That a girl. Bounce that beautiful ass of yours!"
            play ambient "sound effects/moan2.mp3"
            scene vpt_04_a with pixellate
            show vpt_04
            vic "A-ah, ahhh-"
            don "Look at you! I'm barely even moving, sweetheart!"
            vic "Ah, Daauuhh...♥"
            "{b}I found it.{/b}"
            jump w3VickySmutPart4


label w3RockShowBartenderPaysOff:
    play music "music/positioned.ogg"
    scene w3_11647 with wiperight
    eve "Hey, handsome. Thanks for manning the station."
    scene w3_11648 with dissolve
    mc "So that's what it feels like to be objectified in the workplace."
    scene w3_11647 with dissolve
    eve "It's fun, right?"
    scene w3_11649 with dissolve
    "Eve let her hand linger on my ass before brushing the length of her index finger down my crack."
    mct "({i}Holy shit.{/i})"
    "Somehow I proved charming enough to draw the hot bartender's amorous advance."
    scene w3_11650 with dissolve
    mc "Mmmhm, {i}fun{/i} is a word for it."
    scene w3_11649 with dissolve
    "{b}Me.{/b} I did that. And while the circumstances that got me here weren't entirely without connection to the club, I..."
    scene w3_11651 with dissolve
    "I felt empowered."
    scene w3_11652 with dissolve
    nico "Uggh, please, {b}don't.{/b} He's sort of my boss."
    scene w3_11653 with dissolve
    eve "Then I'm doing you a favor by putting in a good word, little Nico."
    scene w3_11652 with dissolve
    nico "Uh huh, sure you are, bitch."
    scene w3_11654 with dissolve
    eve "{i}Unfortunately{/i}, I've got to get home straight after closing..."
    scene w3_11655 with dissolve
    mc "That's an awful thing to say after tickling my scrotum."
    scene w3_11656 with dissolve
    eve "...isn't it?"
    scene w3_11655 with dissolve
    mc "You're evil."
    scene w3_11656 with dissolve
    eve "I take my fun where I can get it..."
    scene w3_11657 with dissolve


    menu:
        "So do you. (w3RockShowBartenderFingerFuck = True)":
            $ w3RockShowBartenderFingerFuck = True
            scene w3_11658 with dissolve
            mc "Interesting choice of words."
            scene w3_11659 with dissolve
            "An insane thought crossed my mind."
            scene w3_11658 with dissolve
            mc "...not much foot traffic when the band's playing, is there?"
            scene w3_11660 with dissolve
            eve "My boss would kill me if I snuck off somewhere..."
            scene w3_11661 with dissolve
            mc "Who said anything about abandoning your station?"
            scene w3_11662 with dissolve
            mc "Man, Your ass looks killer in these jeans."
            scene w3_11663 with dissolve
            eve "Uh... what do you think you're doing down there?!"
            scene w3_11664 with dissolve
            mc "Admiring your fashion sense."
            scene w3_11665 with dissolve
            mc "*Cwhup~*"
            eve "Ah, ha... {b}umm...{/b} this is an even worse idea..."
            scene w3_11666 with dissolve
            "Perhaps, but after her cam girl admission, I had her pegged as a freak."
            scene w3_11667 with dissolve
            mc "Chirp up if anyone's coming, {i}Little{/i} Nico."
            scene w3_11668 with dissolve
            nico "Hey! Don't mix me up into--"
            scene rs_bar01_a with dissolve
            show rs_bar01
            eve "Euahh...!"
            "...so, gently, I began to knead the bartender's ass."
            "No game plan. I wasn't sure where this was going or how far I could take it, but I followed the bartender's body language, because inlaid with her yelp of surprise was..."
            eve "*Gulp...* Mmmh..."
            "...was a passive wait-and-see-where-this-was-going. The bartender merely kept her eyes forward, searching for approaching customers."
            eve "*Sigh* K-keep your head low..."
            "And now, Nico was silent, with not a complaint over me groping her friend."
            eve "...surely, you've gotten a good look by now?"
            mc "I hope you got a discount on these things..."
            eve "I did... they were on sale for two hundred dollars..."
            "I would never get fashion, but..."
            scene w3_11669 with dissolve
            mc "Lean forward."
            "...{b}I got this ass.{/b}"
            scene w3_11670 with dissolve
            eve "..."
            scene w3_11671 with dissolve
            nico "...mmmh, where's your punk spirit, E?"
            scene w3_11672 with dissolve
            "......"
            scene w3_11673 with dissolve
            eve "...weren't you opposed to this?"
            scene w3_11674 with dissolve
            "She shrugged dispassionately, refuting the notion."
            nico "Kinda reminds me of the old days."
            scene rs_bar02_a with dissolve
            show rs_bar02
            "I ventured further."
            eve "W-wha... ah..."
            mc "Try to look business as usual."
            eve "F-fine...! Just keep your head down!"
            "Ha! She {i}was{/i} a freak!"
            scene w3_11675 with dissolve
            eve "...and you're actually going to watch?"
            scene w3_11677 with dissolve
            nico "Boss said keep a lookout."
            scene w3_11676 with dissolve
            "I couldn't see Nicolette from this position, but I didn't need to. She traded her usual dry, acerbic tone for an amused one."
            scene rs_bar03_a with dissolve
            show rs_bar03
            eve "Ah, aahhh..."
            "Inconspicuously, I filled Eve's cunt, in search of that sweet spot."
            eve "Mmh... what the fuck, man--"
            jer "Wooahh, like a BIIIIITCH leeeeft outttt-- in the rraaaaaiinn!"
            "Thankfully, both her subtle moans and the tell-tale sounds of my index finger dipping in and out of her honeypot were drowned out by {i}Eros Massacre's{/i} playing."
            eve "This... escalated... ah..."
            "If her not putting a stop to this wasn't enough, the hot bartender's cunt readily latching onto my finger confirmed it."
            "If she was down to see this to a finish, then so was I!"
            eve "Ah, aahh..."
            "Time was an issue, of course. At any moment, some dumbass rocker boy might stroll up to the bar in need of a shitty beer."
            mc "All good up there?"
            eve "Mmm, hhhhh--"
            scene w3_11679 with dissolve
            nico "All good!"
            scene w3_11678 with dissolve
            "Her whore friend was no longer just amused, but enthralled."
            scene w3_11681 with dissolve
            nico "Haha, look me in the eye, E."
            scene w3_11680 with dissolve
            eve "Haa, c-come on... you're--"
            scene rs_bar04_a with dissolve
            show rs_bar04
            "She might just be enjoying this more than me."
            eve "Mmmpffh, mppfhh-"
            "It hadn't even been a minute, but her reaction was intense. She did her best to muffle her moans."
            nico "O-oh! Someone's"
            eve "....?!"
            "Her sex snagged my finger out of fear!"
            eve "Aah, hooh--"
            nico "Oh, sorry! False alarm!"
            eve "Ah, ahh-- y-you-!"
            "{i}That got her juices flowing.{/i}"
            mct "(Nico, Nico, Nico...)"
            mct "(I should get to know her better. {i}She's fun.{/i})"

            if toughness >= 20:
                mct "(Mmmh, if only I could take this tattooed slut right now...)"
            else:
                mct "(Mmmh, if only I could take this tattooed beauty right now...)"

            scene rs_bar05_a with pixellate
            show rs_bar05
            eve "Mmh, hhhma... {b}y-you bitch!{/b}"
            mct "(Fucking a bartender at the bar...)"
            nico "Too easy! You're the one looking forward, E."

            if w3HanaDP >= 4:
                mct "(Might be something to try with Hana one of these days...)"
            else:
                mct "(There's a new fantasy: free use, while serving drinks...)"

            mct "(Shit...)"
            eve "{b}Ah, haaa-!{/b}"
            play ambient "sound effects/rock-crowd-floor-ambience.wav"
            stop music fadeout 3.0
            scene rs_bar06_a with pixellate
            show rs_bar06
            mct "(...I'll never be able to have simple sex after the club, will I?)"
            eve "Gh, hhaaa..."
            "That was {b}fast.{/b} A short, drowned-out squeal and the bartender was oozing sex into the palm of my hand."
            eve "{b}H-haa, aahh...!{/b}"
            "Nico for her part..."
            scene w3_11682 with dissolve
            "...kept silent and played with her hair."
            scene w3_11683 with dissolve
            mc "Enjoying the show?"
            scene w3_11684 with dissolve
            nico "...not really."
            scene w3_11682 with dissolve
            "{b}Liar.{/b}"
            eve "Haa, haaaa..."
            play music "music/heavy-trailer-1.ogg"
            scene w3_11685 with dissolve
            jer "Thank you all! That was us! We'll be selling CDs and shit!"
            spid "No, we won't! Because I forgot the merch at home!"
            nico "...okay, {i}wasn't so bad.{/i} Hotter than what's being put on tomorrow."
            jer "Okay! Our bassist will be turning tricks in the men's room! Don't miss out!"
            scene w3_11686 with dissolve
            mc "See you there...?"
            nico "Like I got a choice."
            eve "Oh, shit... here comes the rush... t-take your finger--"
            stop ambient fadeout 3.0
            scene black with fade
            "And thus, I made out like a thief into the night."
            "......"
            if not persistent.w3BartenderFun:
                play sound "sound effects/notification.wav"
                show memoryunlock with dissolve
                $ renpy.pause(3, hard=True)
                $ persistent.w3BartenderFun = True
            "..."
            $ renpy.end_replay()
        "What you're thinking is crazy.":

            "...finger fuck a bartender publicly? What's gotten into me? {i}Shit.{/i}"
            scene w3_11655 with dissolve
            mc "I should get your number."
            scene w3_11656 with dissolve
            eve "If you want to see me again, I work weekends."
            scene w3_11655 with dissolve
            mc "So that's how it is?"
            scene w3_11654 with dissolve
            eve "I'm worth hoofing it over."
            scene w3_11687 with dissolve
            nico "Ugh. Neither of you can flirt worth a shit."
            scene w3_11667 with dissolve
            mc "Shut up, {b}Little{/b} Nico."
            $ renpy.end_replay()
            scene w3_11688 with dissolve
            "......"
            "..."
            "I enjoyed watching Nico's various scowls as we chatted a bit until--"
            play music "music/heavy-trailer-1.ogg"
            scene w3_11206 with dissolve
            jer "Thank you all! That was us! We'll be selling CDs and shit!"
            "The music was over."
            spid "No, we won't! Because I forgot the merch at home!"
            jer "Okay! Our bassist will be turning tricks in the men's room! Don't miss out!"
            scene w3_11689 with dissolve
            eve "Here comes the rush..."
            scene w3_11690 with dissolve
            mc "I'll get out of the way..."
            stop music fadeout 3.0
            scene black with fade
            "And as she anticipated, with the band finished, most people flocked to the bar."
            "......"
            "..."

    jump w3RockShowCarnationMeeting
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
