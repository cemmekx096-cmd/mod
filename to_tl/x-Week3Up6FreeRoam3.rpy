



screen w3ExNavMenuStage3:

    imagemap:
        idle "gui/screens/imagemaps/w3ExNavMenu3_idle.png"
        hover "gui/screens/imagemaps/w3ExNavMenu3_hover.png"
        ground "gui/screens/imagemaps/w3ExNavMenu3_ground.png"

        if w3ExAugustTalk == False:
            hotspot (249,240,460,280) action [Play("menu_click","sound effects/door-open.wav"), Jump("w3ExAOStage3")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        elif w3ExAugustStage3Repeat == False:
            hotspot (249,240,460,280) action [Play("menu_click","sound effects/door-open.wav"), Jump("w3ExAugustCuriosity")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]


        hotspot (739,244,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w3ExBarStage3")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]

        if w3ExKOStage3Empty == False:
            hotspot (1217,245,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w3ExKOGothMommies")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]

        hotspot (260,535,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w3ExSaunaStage3End")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        hotspot (737,525,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w3ExHallwayStage3")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        if w3ExHDROPen == True:
            hotspot (1208,529,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w3ExHDRStage3")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        if w3ExKatHallwaySeen == True:
            hotspot (497,802,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w3ExVRStage3")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        if w3ExKOStage3Seen == True:
            hotspot (1000,792,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w3ExVIPFeliciaFinally")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        hotspot (10, 22, 180, 180) action [ Play ("menu_click","sound effects/click2.wav") ], Rollback() hovered [ Play ("hover_load", "sound effects/click.wav")]

label w3ExNavMenuStage3:
    call screen w3ExNavMenuStage3 with pixellate




screen w3ExAO3:

    imagemap:
        imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage3")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        idle "gui/screens/imagemaps/w3ExAO3_idle.png"
        hover "gui/screens/imagemaps/w3ExAO3_hover.png"
        ground "gui/screens/imagemaps/w3ExAO3_ground.png"
        hotspot (1245,351,1500,1500) action Jump("w3ExAO3Chat")

label w3ExAOStage3:
    show black
    $ renpy.music.play("music/as-i-figure.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w3ExAO3 with pixellate

label w3ExAO3Chat:
    $ w3ExAugustTalk = True
    if w3ExHallwayLucyGone == False:
        $ w3ExHallwayLucyGone = True

    scene w3_13126 with dissolve
    mc "...you wanted to talk?"
    scene w3_13127 with dissolve
    aug "Ah, uh... *ahem*{b}yeah.{/b}"
    scene w3_13128 with dissolve
    mc "You alright, boss...?"
    "The old man seemed caught off guard. The door was open, so I didn't knock..."
    scene w3_13129 with dissolve
    aug " That... that was sooner than I thought. Where's Elias?"
    scene w3_13130 with dissolve
    mc "Having a heart-to-heart with Dr. Chuck."
    scene w3_13131 with dissolve
    aug "Ha! Of course he is... that old codger will take {i}any{/i} chance to run his mouth."
    scene w3_13132 with dissolve
    aug "So, mmmh--"
    aug "What do you make of our newest patron?"
    scene w3_13133 with dissolve
    mc "...why are you asking me?"
    play sound "sound effects/kiss2.wav"
    scene w3_13134 with dissolve
    aug "Don't answer a question with a question. I {b}hate{/b} that."
    stop sound
    scene w3_13135 with dissolve
    mc "Oh, uh, well..."
    scene w3_13136 with dissolve

    menu:
        "Elias has surprised you.":
            scene w3_13137 with dissolve
            mc "Honestly...? He's more earnest than I expected."
            scene w3_13138 with dissolve
            aug "{i}Earnest{/i}...?"
            scene w3_13137 with dissolve
            mc "Yeah, like... transparent? He just comes out and says what he thinks and feels. He told me about his dad, for some reason."
            scene w3_13138 with dissolve
            aug "I see..."
        "He reminds you of any other patron in this place.":

            scene w3_13137 with dissolve
            mc "I don't know... it seems like he's buying his way into an election, right? Guess he has as much integrity as any bastard in this place."
            scene w3_13139 with dissolve
            aug "Don't talk about our members like that!"
            scene w3_13140 with dissolve
            mc "You asked..."

    scene w3_13137 with dissolve
    mc "Can I ask why you're asking now?"
    scene w3_13141 with dissolve
    aug "Ah... that's..."
    aug "It's kinda fucked up his wife's here."
    scene w3_13142 with dissolve
    "He looked like he wanted to say more, but he left it at that."
    scene w3_13143 with dissolve
    mc "Yeeeeeeep."
    scene w3_13141 with dissolve
    aug "If someone did that to me, I'd kill them. I'll never understand what runs through their heads."
    scene w3_13142 with dissolve
    mc "...whose heads?"
    scene w3_13143 with dissolve
    "Despite the old man's earlier ass kissing and bribery, the look on his face suggested he wasn't enthused with the situation."
    scene w3_13144 with dissolve
    aug "A, aah...!"
    scene w3_13145 with dissolve
    mc "You sure you're okay? You look flushed."
    scene w3_13146 with dissolve
    aug "Close the door on your way out."
    scene w3_13145 with dissolve
    mc "Alright..."
    scene w3_13147 with dissolve
    "It seems he was done with me."
    scene black with fade
    mct "(That was weird.)"
    jump w3ExNavMenuStage3

label w3ExAugustCuriosity:
    $ w3ExAugustStage3Repeat = True
    scene w3_13148 with dissolve
    mc "Oh...?"
    mct "(Was that Dalia?)"
    scene w3_13149 with dissolve
    "At any rate, I don't have any reason to drop back in on the old gangster."
    jump w3ExNavMenuStage3



screen w3ExBarStage3:

    if w3ExBar3AllisonLeft == False:

        imagemap:
            imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage3")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            idle "gui/screens/imagemaps/w3ExBar3_idle.png"
            hover "gui/screens/imagemaps/w3ExBar3_hover.png"
            ground "gui/screens/imagemaps/w3ExBar3_ground.png"
            hotspot (7,239,250,250) action Jump("w3ExBar3Kimber")
            hotspot (234,205,300,750) action Jump("w3ExBar3Allison")
            hotspot (1414,213,1500,1500) action Jump("w3ExBar3Sophia")


    else:
        imagemap:
            imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage3")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            idle "gui/screens/imagemaps/w3ExBar3Gone_idle.png"
            hover "gui/screens/imagemaps/w3ExBar3Gone_hover.png"
            ground "gui/screens/imagemaps/w3ExBar3Gone_ground.png"
            hotspot (7,239,1500,1500) action Jump("w3ExBar3Kimber")
            hotspot (1414,213,1500,1500) action Jump("w3ExBar3Sophia")


label w3ExBarStage3:
    show black
    $ renpy.music.play("music/jazz-apricot.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w3ExBarStage3 with pixellate


label w3ExBar3Allison:
    $ w3ExBar3AllisonLeft = True
    if w3ExHallwayLucyGone == False:
        $ w3ExHallwayLucyGone = True


    scene w3_13150 with dissolve
    allison "*Sigh* You must enjoy bothering me, Bukowski."
    scene w3_13151 with dissolve
    "Her look said it all. {b}Go{/b} away."
    scene w3_13152 with dissolve

    if w3ExAllisonPutInPlace == True:
        mc "Like flies enjoy bothering shit. You're going to call me that, too?"
    else:
        mc "You're going to call me that, too?"

    scene w3_13153 with dissolve
    "Needless to say, I was undeterred."
    scene w3_13154 with dissolve
    allison "I've probably heard your real name, but I don't remember it."
    mc "It's--"
    scene w3_13155 with dissolve
    allison "And I don't care to."
    scene w3_13156 with dissolve
    mc "Don't be like that. After all, we're both here for the same reason tonight: to give one man the illusion of companionship. Since we're both on stand-by, why not pass the time with some pleasant conversation?"
    scene w3_13157 with dissolve
    allison "That's what you call sniffing around me like a horny mutt?"
    scene w3_13158 with dissolve
    mc "If I'm truly bothering you, I'll leave."
    scene w3_13159 with dissolve
    "......"

    if Allison_Interest <= 3:
        scene w3_13160 with dissolve
        allison "...listen, it's nothing personal. I'd just like to have some moments to myself before it's game time again. Do you mind?"
        scene w3_13161 with dissolve
        "For a moment, she lost her edge. Instead, it felt like she was asking for a sliver of genuine understanding."
        scene w3_13162 with dissolve
        mc "...let it be known, [mcf] [mcl] can take a hint."
        scene w3_13163 with dissolve
        allison "Thanks. {b}[mcf]{/b}. I was going to go freshen up anyway. This drink {b}sucks.{/b}"
        scene black with fade

        if w3ExBar3SophiaRepeat == False:
            "Oh, well. I could always bother Sophia if I want to figure out that earlier weirdness."
            mct "(No shortage of blondes tonight.)"
        else:
            "Oh, well. I can find something else to do with my time."
    else:

        scene w3_13164 with dissolve
        allison "...{b}no{/b}, stay. You're at least better noise than the sighing bartender."
        scene w3_13165 with dissolve
        "I almost said \"that's a low {i}bar{/i} to clear\", but I didn't want her to rescind her permission."
        scene w3_13166 with dissolve
        allison "Just don't pretend you're making \"pleasant\" conversation because you find me interesting. I hate that."
        scene w3_13168 with dissolve
        mc "You have a movie coming out this summer. You're more interesting than me, Miss Smith."
        scene w3_13167 with dissolve
        allison "Just because that is true doesn't invalidate what I asked. That's the {b}one{/b} thing I like about this place, it's honest."
        scene w3_13168 with dissolve
        mc "How so?"
        scene w3_13166 with dissolve
        allison "There's no need for insinuation or double speak about creative pow-wows, nor do you have to lie to scumbags to avoid shattering their delusions."
        allison "Here, it's all on the table."
        scene w3_13169 with dissolve
        allison "{b}You want to fuck me.{/b}"
        scene w3_13170 with dissolve
        "She wasn't wrong per se, but..."
        scene w3_13171 with dissolve
        mc "Want and actually would are separate things."
        scene w3_13172 with dissolve
        allison "Don't make me laugh. You would jump at the chance."
        scene w3_13170 with dissolve

        menu w3ExAllisonFlirtMenu:
            "{color=#FF1493}[[HanaGF]{/color} You have a girlfriend." if hanaGF == True:
                $ Allison_Interest += 1
                $ w3ExAllisonHaveGF = True
                scene w3_13171 with dissolve

                if w3ExAOAllisonSeen == True:
                    mc "That \"scowling\" bartender's my girlfriend."
                else:
                    mc "That woman who was talking to August is my girlfriend."

                scene w3_13172 with dissolve
                allison "So, what?"
                scene w3_13171 with dissolve
                mc "Have you seen her? Why would I mess that up for... {i}you{/i}?"
                scene w3_13173 with dissolve
                allison "Why-- What does she have that I--"
                scene w3_13174 with dissolve
                allison "{b}Big talk.{/b}"
                scene w3_13175 with dissolve
                mc "Oh, man. You actually can't conceive of a world where a man {i}wouldn't{/i}?"
                scene w3_13174 with dissolve
                allison "It doesn't matter, because we will never find out."
                scene w3_13176 with dissolve
                "........."
                "......"
                scene w3_13177 with dissolve
                mc "...so, what's your favorite movie that you've been in? Leading or otherwise."
                scene w3_13178 with dissolve
                allison "You actually want to talk after bitch mode?"
                scene w3_13179 with dissolve
                mc "You're an interesting woman."
                scene w3_13180 with dissolve
                allison "{b}Fuck{/b}, that's... {i}fine.{/i} I don't know if I have a--"
                "And so we made pleasant conversation, while Allison finished her drink, before excusing herself to \"get her game face\" on. Whatever that meant."
                scene black with fade
                "...probably something going up her nose or ingested into her body. {i}Just a guess.{/i}"
            "Jesus Christ, she needs to calm her tits.\n {mod_green}Allison Interest +2":

                $ Allison_Interest += 2
                scene w3_13171 with dissolve
                mc "That's sad. You can't conceive of a world where a man {i}wouldn't{/i}, can you?"
                scene w3_13172 with dissolve
                allison "Sad?! Don't--"
                scene beyblade with dissolve
                stop music
                show allibar_spin
                play sound "sound effects/music-stop.wav"
                mc "Reset!"
                allison "{i}Eeewah?!{/i} What the--"
                play music "music/dont-fret.ogg"
                scene w3_13181 with dissolve
                "I don't know what died up her beautiful ass, but it had to be removed."
                scene w3_13182 with dissolve
                allison "What the hell was that?"
                scene w3_13183 with dissolve
                mc "The mood was way too intense for {b}no{/b} reason."
                scene w3_13182 with dissolve
                allison "...so you spun me around?"
                scene w3_13184 with dissolve
                mc "Yep. Give me your hand."
                scene w3_13185 with dissolve
                "........."
                "......"
                scene w3_13186 with dissolve
                allison " ...alright."
                scene w3_13187 with dissolve
                mc "What made you want to become an actress?"
                scene w3_13188 with dissolve
                allison "Are you serious?"
                scene w3_13187 with dissolve
                mc "I'm curious!"
                scene w3_13189 with dissolve
                allison "Ah, what do you think? Lotsa girls want to be famous."
                scene w3_13190 with dissolve
                mc "Sure, but it's never just one reason. There's easier ways to be famous nowadays, and movies are a dying art form. So, why acting?"
                scene w3_13191 with dissolve
                allison "......"
                scene w3_13192 with dissolve
                allison "...it's fun."
                scene w3_13193 with dissolve
                mc "That's a great reason."
                scene w3_13194 with dissolve
                allison "I don't think you should touch me, [mcf]."
                scene w3_13195 with dissolve
                mc "You {b}do{/b} know my name."
                scene w3_13196 with dissolve
                allison "Won't you get in trouble?"
                mc "...I wouldn't even call this a touch. Besides, I've done worse to Elias."
                scene w3_13197 with dissolve
                allison "What does that mean?"
                scene w3_13198 with dissolve
                mc "That you'll have to wait and see about that. So, how good is {i}Storms of Andromeda?{/i}"
                scene w3_13199 with dissolve
                allison "Pfft, I haven't seen it, but it fuckin' sucks."
                scene w3_13200 with dissolve
                mc "Yeah, I've seen the trailer."
                scene w3_13201 with dissolve
                "So, we had that pleasant conversation I hoped for, and Allison seemed a whole lot nicer during it. Eventually, though, she wanted to go \"freshen\" up."
                "Which left me with one thought..."
                scene black with fade
                "I was good at {i}this.{/i}"
            "Whatever the case, you are each on the job.":

                scene w3_13171 with dissolve
                mc "I might, but we'll never know. You're Elias' date tonight."
                scene w3_13202 with dissolve
                allison "That I am..."
                scene w3_13203 with dissolve
                mc "Stranger things have happened, though. What's your favorite movie that you've been in? Leading or otherwise."
                scene w3_13178 with dissolve
                allison "You're not a reporter. Don't ask questions like that."
                scene w3_13179 with dissolve
                mc "What? I genuinely want to know."
                scene w3_13180 with dissolve
                allison "I don't have a--"
                "Somehow, before she realized it, I had tricked the movie star into that \"pleasant conversation\" I had touted. Eventually, though, all too soon, she excused herself to \"get her game face\" on. Whatever that meant."
                scene black with fade
                "...probably something going up her nose or ingested into her body. {i}Just a guess.{/i}"

            "{color=#696969}[[HanaGF] Girlfriends are perfect for a time like this.{/color}" if hanaGF == False:
                jump w3ExAllisonFlirtMenu

    jump w3ExBarStage3


label w3ExBar3Sophia:

    if w3ExBar3SophiaRepeat == False:
        $ w3ExBar3SophiaRepeat = True
        if w3ExHallwayLucyGone == False:
            $ w3ExHallwayLucyGone = True

        scene w3_13245 with fade
        "Off in the corner was Sophia and her spectacular behind."
        "Oh, and some old dudes too, but that hardly registered."
        "Part of me wanted to go over there, the other part didn't."
        "........."
        "......"
        scene black with fade
        "The more curious part of me won out. What was that shit about in the hallway?"
        scene w3_13204 with dissolve
        mc "Do you mind if I borrow your aid a moment, Dr. Van Doren?"
        abel "Oh...?"
        scene w3_13205 with dissolve
        abel "Go. I'll be fine."
        scene w3_13206 with dissolve
        sophia "What is it?"
        mc "I want to talk."
        scene black with fade
        "..."
        scene w3_13207 with dissolve
        mc "What kind of game are you playing?"
        scene w3_13208 with dissolve
        sophia "You're referring to my visit this morning?"
        scene w3_13207 with dissolve
        mc "Then you do remember?"
        scene w3_13209 with dissolve
        sophia "...{b}yes.{/b} I extended you the offer of a favor."
        scene w3_13210 with dissolve
        mc "You don't sound so sure..."
        scene w3_13209 with dissolve
        sophia "I've been up for thirty-six hours, I thought... I lost track of the day. That's all."
        scene w3_13210 with dissolve
        mc "You mentioned the exhibition when you--"
        scene w3_13211 with dissolve
        sophia "Why are you so pushy about this?! I'm not perfect! Can't I have a hiccup every now and then?!"
        scene w3_13212 with dissolve
        mc "Ah--"
        scene w3_13213 with dissolve
        mc "Yeah, of course. Sorry."
        scene w3_13214 with dissolve
        "Shit. I didn't expect Sophia to get so... {i}emotive.{/i}"
        "......"
        scene w3_13215 with dissolve
        sophia "...I apologize. I did not mean to show my anger. I do not... {i}like to.{/i}"
        scene w3_13216 with dissolve

        menu:
            "You liked it.\n {mod_green}Sophia Rapport +1":
                $ sophiaRapport += 1
                scene w3_13217 with dissolve
                mc "I kinda liked it."
                scene w3_13218 with dissolve
                sophia "You did...? What manner of deviancy is that?"
                scene w3_13217 with dissolve
                mc "It's not a {i}deviancy{/i}... it's just, you're usually so straight-faced, y'know? It's nice to see a bit of life in your beautiful face."
                scene w3_13219 with dissolve
                sophia "...you are a deviant. You grabbed my hand."
                scene w3_13220 with dissolve
                mc "Are you fucking with me?"
                scene w3_13221 with dissolve
                "........."
                "......"
                scene w3_13222 with dissolve
                sophia "{b}...yes.{/i}"
                scene w3_13223 with dissolve
                mc "Dr. Van Doren was right. You are funny."
                scene w3_13222 with dissolve
                sophia "I told you."
            "It did surprise you, yes.":


                scene w3_13217 with dissolve
                mc "I was a little shocked. You're usually... {b}cold.{/b}"
                scene w3_13218 with dissolve
                sophia "I'm human, Mr. [mcl]."
                scene w3_13217 with dissolve
                mc "Yeah, of course, what else would you be?"
                scene w3_13224 with dissolve
                "........."
                "......"
                "...fuck, this is awkward. {b}Let's go for broke.{/b}"


        scene w3_13226 with dissolve
        mc "Can I ask you something?"
        scene w3_13227 with dissolve
        sophia "I don't know, can you?"
        scene w3_13225 with dissolve
        "I had to admit, while Sophia wasn't wearing her perfume like she had promised... my eyes were still drawn to her charms."
        scene w3_13228 with dissolve
        mc "Do you... {i}enjoy{/i} that part of your job?"
        scene w3_13227 with dissolve
        sophia "I do not know what you mean. What part?"
        scene w3_13226 with dissolve
        mc "Wearing outfits like that and... {b}fucking{/b} who Dr. Van Doren tells you to."
        scene w3_13229 with dissolve
        sophia "Enjoy...?"
        scene w3_13230 with dissolve
        "She looked like she had never considered that question before."
        scene w3_13227 with dissolve
        sophia "As much as I enjoy turning off a catalytic burner. It's just a step in a long process."
        scene w3_13231 with dissolve
        sophia "...that confuses you?"
        scene w3_13232 with dissolve
        mc "It's not normal. You're so smart, yet--"
        scene w3_13233 with dissolve
        sophia "There are many things in this world that is difficult to wrap one's head around, each different depending on the person."
        sophia "You did not have my upbringing."
        scene w3_13234 with dissolve
        mc "...? What don't you get?"
        scene w3_13233 with dissolve
        sophia "Body language, for one. "
        scene w3_13234 with dissolve
        mc "That's a funny thing to say when you have your hand on my chest."
        scene w3_13233 with dissolve
        sophia "I didn't say I did not learn it. It's just inefficient for communicating."
        scene w3_13234 with dissolve
        mc "That's not true. Sometimes it's the only way to convey what is otherwise impolite or difficult to say."
        scene w3_13235 with dissolve

        menu:
            "Look at her tits.\n {mod_green}Sophia Rapport +1":
                $ sophiaRapport += 1
                scene w3_13236 with dissolve
                "I let my eyes wander below, daring and bold."
                scene w3_13237 with dissolve
                sophia "Why is that difficult to convey?"
                scene w3_13238 with dissolve
                mc "Maybe not in a place like this, but... you really do fascinate me, Sophia. Like a horror movie."
                scene w3_13237 with dissolve
                sophia "Interesting... I'll remember that."
                scene w3_13238 with dissolve
                mc "What for?"
                scene w3_13237 with dissolve
                sophia "It could be useful if I need to kill you."
                scene w3_13239 with dissolve
                mc "Uh--"
                sophia "Yes, that was a joke."
                mc "I knew that..."
                scene w3_13240 with dissolve
                "As she drew away, her hand trailed down and lingered, while her eyes flittered up..."
                scene w3_13241 with dissolve
                sophia "You're quite firm."
                scene w3_13240 with dissolve
                "It was for a moment, but it felt deadly precise for someone who proclaimed to find body language difficult."
                scene w3_13242 with dissolve
                sophia "Will that be all, Mr. [mcl]?"
                scene w3_13243 with dissolve
                mc "See you around, {b}Soph.{/b}"
            "Take her hand off you.":

                if sophiaRapport >= 2:
                    $ sophiaRapport -= 2
                elif sophiaRapport = 1:
                    $ sophiaRapport  = 0
                else:
                    pass

                "I did not trust her."
                scene w3_13244 with dissolve
                sophia "Ah... I understand. I also do not like being touched without purpose."
                mc "Yeah..."
                scene w3_13242 with dissolve
                sophia "Will that be all, Mr. [mcl]? Or do you have more questions for me?"
                scene w3_13243 with dissolve
                mc "No, Miss Lundgren. I was just... you looked very confused earlier. I was concerned."
                scene w3_13242 with dissolve
                sophia "I appreciate."
                scene w3_13243 with dissolve
                mc "I'll let you get back to Dr. Van Doren."

        scene black with fade
        "..."
    else:
        $ randint = renpy.random.randint(1, 2)
        scene w3_13245 with fade
        if randint == 1:
            if sophiaRapport >= 3:
                "I still don't know what to make of that woman, but she intrigues me..."
            else:
                "I do not know what to make of that woman..."
        elif randint == 2:
            mct "Before I go, one last look at that ass..."

    jump w3ExBarStage3


label w3ExBar3Kimber:
    scene w3_13246 with fade
    if w3ExBar3KimberRepeat == False:
        $ w3ExBar3KimberRepeat = True
        if w3ExHallwayLucyGone == False:
            $ w3ExHallwayLucyGone = True

        mct "(...looks like Harper switched places with Kimber.)"
    else:
        mct "(She doesn't have the most inviting demanor of the girls, but I suppose there's some appeal in...)"

    jump w3ExBarStage3



label w3ExKOGothMommies:
    stop music fadeout 4.0
    $ w3ExKOStage3Empty = True
    $ w3ExKOStage3Seen = True

    if w3ExHallwayLucyGone == False:
        $ w3ExHallwayLucyGone = True

    scene w3_13247 with fade
    hana "{i}Of course{/i} I look great, but why do I {b}need{/b} to? Isn't this the opposite of getting them to take me seriously?"
    "As I was passing by Kat's office, I heard something \"interesting\" through the cracked door."

    menu:
        "Listen in."(chg=["hana_anger_down"]):
            $ Hana_Anger -= 1
            $ w3ExHanaKatTalk = True
            play music "music/Moonlight-Sonata.ogg" fadein 3.0
            kat "Mmmh, they will~ {b}never{/b} take you seriously. You're too young and too much of a woman, {b}BUT{/b} that can work in your favor."
            scene w3_13248 with dissolve
            "Quickly, before Hana could wrench herself from her clutches, Kathleen whirled behind her with a song in her step and evil in her eyes."
            kat "Your large, perky breasts~"
            scene w3_13249 with dissolve
            hana "Uh... where do you think you're touching--"
            scene w3_13250 with dissolve
            kat "Your {b}enviable{/b} slender waist..."
            scene w3_13251 with dissolve
            kat "Not to mention these hips, pert ass, and luscious thighs..."
            scene w3_13252 with dissolve
            hana "I know what I'm working with! I don't need the rundown!"
            scene w3_13253 with dissolve
            kat "We could {b}all{/b} use a reminder."
            scene w3_13254 with dissolve
            kat "You're beautiful. You look like perfection itself."
            scene w3_13255 with dissolve
            kat "If you know how amazing you look, then why are you blushing?"
            scene w3_13256 with dissolve
            hana "...b-bitch, cause you're up in my business?!"
            scene w3_13255 with dissolve
            kat "You may not like me, but you can learn something from me. You're young and can thrive in ways that I can't."
            kat "{i}Our{/i} clientele are men who can have anything they want in the world, but they can't have {b}you{/b}. There's a power in that, so don't let them forget it."
            scene w3_13257 with dissolve
            hana "I don't give a fuck about holding power over those assholes!"
            scene w3_13258 with dissolve
            kat "No...? Yet you, a bright woman, are here. {b}Reluctance{/b} is beneath you."
            scene w3_13259 with dissolve
            hana "Stop talking to me like we're friends..."
            scene w3_13260 with dissolve
            kat "No, but we're {b}colleagues.{/b} Are you still planning on selling?"
            scene w3_13261 with dissolve
            hana "Should I wait until I'm retirement age or until we all get arrested?"
            scene w3_13260 with dissolve
            kat "You're quite right, it's all about timing. Which, for the time being, I hear you're already dealing with petty squabbles... how is that going?"
            scene w3_13262 with dissolve
            hana "It's been... {i}frustrating.{/i}"
            scene w3_13263 with dissolve
            kat "I can imagine. I'm glad that isn't my side of the business."
            scene w3_13264 with dissolve
            kat "But it's not all bad, is it?"
            scene w3_13265 with dissolve
            hana "Uh... I guess I like working with Dalia and... {i}I don't know{/i}... it's nice to be focused on something."
            scene w3_13264 with dissolve
            kat "There's no shame in that. We all need purpose, and your \"situation\" with your poor mother is suffocating, isn't it?"
            scene w3_13266 with dissolve
            kat "...oh? You're not biting my head off?"
            scene w3_13267 with dissolve
            hana "If I did that, your blood is probably toxic... "
            scene w3_13268 with dissolve
            kat "So, do you {i}really{/i} hate the outfit?"
            scene w3_13269 with dissolve
            "........."
            scene w3_13270 with dissolve
            "......"
            scene w3_13271 with dissolve
            hana "...no, I look amazing."
            scene w3_13272 with dissolve
            kat "{b}Yes{/b}, you do..."
            scene w3_13273 with dissolve
            hana "Wearing it feels nice..."
            scene w3_13274 with dissolve
            "........."
            scene w3_13275 with dissolve
            "......."
            scene w3_13276 with dissolve
            hana "... I hate to say it, but you're gorgeous too."
            scene w3_13277 with dissolve
            kat "Oh, oh...?"
            scene w3_13278 with dissolve
            hana "A-ah, I mean... you said it yourself. We could all use the reminder. You have good taste."
            hana "Like seriously?! Do you bathe in the blood of virgins or something?!"
            scene w3_13279 with dissolve
            mct "(Huh...)"
            "The two of 'em were speaking on far more amicably than I could ever dream."
            "Whatever the case, it was long past the time for eavesdropping."
            play sound "sound effects/door-knock.wav"
            scene w3_13280 with dissolve
            kat "I--"
            scene w3_13281 with dissolve
            mc "Oh, hey. What are you two up to?"

            if w3KatSnare == True:
                "I should interject, lest the old woman worms herself even deeper into Hana's brain like she's doing to me."
            else:
                "I should interject, lest the old woman worms herself even deeper into Hana's brain."

            scene w3_13282 with dissolve
            kat "[mcf]!"
            "The old woman practically floated over to me, a rare unabashed smile beautifying her stern features."
            scene w3_13293 with dissolve
            kat "Where's Elias?"
            scene w3_13294 with dissolve
            "And with her, the faint scent of something insidious."
            scene w3_13292 with dissolve
            mc "He's having a one-on-one with Chuck."
        "Announce your presence.":


            play music "music/Moonlight-Sonata.ogg" fadein 3.0
            play sound "sound effects/door-knock.wav"
            scene w3_13283 with dissolve
            mc "Oh, hey. Am I interrupting anything?"
            scene w3_13284 with dissolve
            kat "[mcf]! I was just convincing Hana of the allure of her beauty. She looks great, doesn't she?"
            scene w3_13285 with dissolve


            menu:
                "Kathleen is right.":
                    pass
                "Kathleen isn't wrong.":
                    pass
                "Yes, you agree with her assessment.":
                    pass
                "Seriously, there is no other option.":
                    pass

            scene w3_13286 with dissolve
            $ Hana_Affection +=1
            if hanaGF == True:
                mc "She's the most beautiful woman in this building, but in that dress..."
                mc "{b}Holy shit!{/b}"
            elif w3HanaDP >= 4:
                mc "Yeah, {b}holy shit...{/b}"
            else:
                mc "She'd look good even in a burlap sack."

            scene w3_13287 with dissolve
            kat "See dear? Don't you like it?"
            hana "Well... ah..."
            scene w3_13288 with dissolve
            hana "*Sigh* I do feel like I could conquer the world..."
            scene w3_13289 with dissolve
            kat "Then you like it! Hardly any shame in admitting that you like to look your best. We're going to look {i}killer{/i} next to each other tonight."
            hana "A-ah, w-what? What am I, your Barbie?! P-pah, I--"
            scene w3_13290 with dissolve
            hana "You have good taste... I'll give you that."
            "Hana was fast to concede to the old woman, but this was one of those rare cases that could not be disputed. {i}She looked like a million bucks.{/i}"
            scene w3_13291 with dissolve
            kat "By the way, where's Elias?"
            "The old woman practically floated over to me, a rare, unabashed smile beautifying her stern features. Her excitement for tonight must've been unbound."
            scene w3_13292 with dissolve
            mc "He's having a one-on-one with Chuck."
            scene w3_13294 with dissolve
            "And with her, the faint scent of something insidious."

    scene w3_13295 with dissolve
    kat "Hmm, interesting..."
    "It was different than usual though, more... {b}subtle{/b}."
    scene w3_13296 with dissolve
    mc "So, uh... he's been on board with all of {i}this{/i}?"
    kat "Of course. Elias wouldn't be here if Chucky didn't desire it so."
    scene w3_13297 with dissolve
    "...too subtle, too faint, too different. Was it just regular perfume? If it was, my eyes were nevertheless drawn to both the full-figured goddess and devil in front of me."
    scene w3_13292 with dissolve
    mc "What are the Carnations up to? I haven't seen them."
    scene w3_13294 with dissolve
    "...although, who wouldn't be?"
    scene w3_13293 with dissolve
    kat "Felicia should be waiting in the VIP room, for her husband's welcome. The other two are stashed away for safekeeping."
    scene w3_13298 with dissolve
    mc "Ah..."
    "The closer Kathleen got, the more aware of {b}both{/b} of them I became."

    if hanaGF == True:
        scene w3_13299 with dissolve
        kat "By the way, you two are dating, yes?"
        mc "How did you--"
        kat "I can tell."
        scene w3_13300 with dissolve
        hana "{b}Yes.{/b} We're dating..."
        "Hana stepped up, looking bold."
        scene w3_13301 with dissolve
        kat "Ha! Our first \"Carnation Club Couple\", how lovely..."
        scene w3_13302 with dissolve
        kat "Enjoy tonight, {b}together.{/b}"
        scene w3_13301 with dissolve
        kat "I'm both jealous and rooting for you..."
        scene w3_13303 with dissolve
        mc "Uh, right..."
        scene w3_13304 with dissolve
        kat "Anyway, I need to go check on some things... I'll leave you two love birds alone."
        kat "Still, do tend to Elias once Chucky is finished with him."
        mc "Will do..."
        scene black with fade
        "The scene was subtle, but it still lingered between us."
    else:
        scene w3_13305 with dissolve
        kat "Anyway, I need to go check on some things..."
        scene w3_13306 with dissolve
        "As she passed, she brushed up against me like a cat. Not helping my paranoia..."
        mc "Sure..."
        "Still, this was {b}nowhere{/b} near as intense as my other inoculations."
        scene w3_13307 with dissolve
        kat "Don't forget to tend to Elias once Chucky is finished with him."
        mc "Will do..."
        scene black with fade
        "While subtle, the scent still lingered in the air."

    "..."
    scene w3_13308 with fade
    hana "So... uh... playing lackey still going well? You need to get back to that?"
    scene w3_13309 with dissolve

    if w3HanaDP >= 4:
        "She looked at me, a faint color to her cheeks and some hope in her eye that I'd hang around."
        "If I did, it'd probably eat up all my time before I needed to get back to Elias."


    menu w3ExHanaSplit:
        "{color=#FF1493}[[Bumped Uglies]{/color} Spend your remaining time with Hana." if w3HanaDP >= 4:
            $ w3ExHanaPhotoshoot = True
            scene w3_13310 with dissolve
            mc "You know..."
            scene w3_13311 with dissolve
            "...how could I say no to those eyes?"
            scene w3_13310 with dissolve
            mc "I've got some time to kill, what do you say to taking some photos?"
            scene w3_13312 with dissolve
            hana "Photos, what like...?"
            scene w3_13313 with dissolve

            if hanaGF == True:
                mc "Yeah... you're so fuckin' beautiful right now, babe. I'd like a memento..."
            else:
                mc "Yeah... you look so fuckin' beautiful right now. I'd like a memento..."

            "It was an errant, mischievous thought that I immediately voiced."
            scene w3_13314 with dissolve
            hana "Ha, you...! What? [mcf]... since when are you a photographer?"
            scene w3_13315 with dissolve
            mc "I'm not, but... looking at you makes it seem like an appealing hobby. How 'bout it?"
            scene w3_13316 with dissolve
            hana "Hmm..."
            scene w3_13314 with dissolve
            hana "You're not going to show them to Ian, are you?"
            scene w3_13315 with dissolve
            mc "No! Of course not! They'll be for my eyes only!"
            scene w3_13316 with dissolve
            hana "Hmm..."
            scene w3_13317 with dissolve
            "The way Hana's eyes refocused on me after a brief silence foretold something {b}good.{/b}"
            scene w3_13318 with dissolve
            hana "You going to jerk off to it?"
            scene w3_13317 with dissolve
            mc "That depends... you want me to?"
            scene w3_13318 with dissolve
            hana "{b}Yes.{/b}"
            hana "Where are we going?"
            scene w3_13317 with dissolve
            mc "Oh, I've got the perfect place."
            stop music
            jump w3ExHanaPhotoShoot
        "The devil's work is never done...":

            scene w3_13319 with dissolve
            mc "Yeah, that would probably be for the best..."

            if w3HanaDP >= 4:
                scene w3_13320 with dissolve
                hana "Oh..."
                "She looked disappointed, but she didn't push it."

                if w3HanaMomMeet == True:
                    scene w3_13321 with dissolve
                    mc "Don't pout. We still have our \"rendezvous\" later."
                    scene w3_13322 with dissolve
                    hana "Huh, you mean...? {b}Oh, yeah!{/b}"
                    "The promise we made this morning."
                    scene w3_13321 with dissolve
                    mc "Aw, don't tell me you already forgot. How could you forget?"
                    scene w3_13322 with dissolve
                    hana "Oh, I don't know... maybe because you made it while you were finger blasting me!"
                    scene w3_13323 with dissolve
                    "........."
                    "......"
                    scene w3_13324 with dissolve
                    hana "...come here, you."
                else:

                    scene w3_13310 with dissolve
                    mc "Duty calls. We'll find the time later."
                    scene w3_13312 with dissolve
                    hana "You promise?"
                    scene w3_13313 with dissolve
                    mc "Uh, huh..."
                    scene w3_13324 with dissolve
                    hana "Come here, you..."

                scene black with fade
                "We spent a few minutes embracing, before parting ways. I still had more to explore."
                "I could even check in with Felicia if I wanted."
            else:

                mc "What about you?"
                scene w3_13325 with dissolve
                hana "I should... I don't know. Make sure Kimber isn't slacking off?"
                scene w3_13326 with dissolve
                mc "Just make sure there's a witness around when you do."
                hana "Pff, I can take that bitch."
                scene black with fade
                "With that, we parted ways. I still had more to explore. I could check in with Felicia if I wanted."

        "{color=#696969}[[Bumped Uglies] Spend your remaining time with Hana.{/color}" if w3HanaDP <=3:
            jump w3ExHanaSplit


    jump w3ExHallwayStage3

label w3ExHanaPhotoShoot:
    scene w3_13327 with pixellate
    hana "[mcf]..."
    play music "music/knockout.ogg" fadein 3.0
    scene w3_13328 with dissolve
    hana "You want to lock me up?"
    scene w3_13329 with dissolve
    mc "For safe keeping, beautiful."
    scene w3_13330 with dissolve
    hana "Ah... frisky fuck."
    scene w3_13329 with dissolve
    mc "Me? You're practically tapping your foot in excitement."
    scene w3_13330 with dissolve
    hana "Mmmh...♥"
    scene w3_13329 with dissolve
    mc "You look great in this light..."
    scene w3_13331 with dissolve
    hana "Where do you want me, Mr. Photographer?"
    scene w3_13332 with dissolve
    mc "Ohoho... I get to direct you?"
    scene w3_13331 with dissolve
    hana "Uuuuu-{b}huh{/b}. {i}Should{/i} be fun."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w3_13333 with dissolve
    mc "So, what should--"
    scene w3_13334 with dissolve
    hana "I wasn't ready!"
    mc "Just wanted a candid one. Now, how about you sit on that table over there?"
    scene w3_13335 with dissolve
    hana "That's it? You just want me to... {i}sit{/i}?"
    scene w3_13336 with dissolve
    mc "More like \"lord over an invisible slave\", that kind of vibe, but yeah... {b}sit{/b}"
    scene w3_13337 with dissolve
    hana "Pfft, {i}weirdo{/i}."
    scene w3_13338 with dissolve
    mc "Oh, don't fret. You'll be bent every which way if you'll let me. That's a promise."
    scene black with fade
    mc "Say, if I didn't know any better..."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w3_13339 with fade
    mc "I'd say this is turning you on."
    mc "You're as red as the walls."
    scene w3_13340 with dissolve
    hana "It {i}is{/i} a strange feeling."
    scene w3_13339 with dissolve
    mc "You say that, but you've done a concert topless..."
    scene w3_13340 with dissolve
    hana "Yet, I'm more aware of both my body and your eyes right now than I've ever been..."
    scene w3_13339 with dissolve

    if w3HanaBrothelRP == True:
        mc "Spread your legs for the camera, slut."
    else:
        mc "Spread your legs for the camera, beautiful."

    scene w3_13341 with dissolve
    hana "Mmmhehehe, aaaaallll~right..."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w3_13342 with dissolve
    mc "Jesus, Hana... your skin is so... {b}goddamn.{/b}"
    scene w3_13341 with dissolve
    hana "What next?"
    scene w3_13342 with dissolve
    "Under the glow of the fluorescent light, with milky white tracts of skin cut up deliciously by black lace..."
    scene w3_13343 with dissolve
    mc "I... let's see what you look like against those bars..."
    scene w3_13344 with dissolve
    "She looked otherworldly, like an apparition. So much so that I felt the need to capture her before she could vanish."
    scene w3_13345 with dissolve
    "She did as I asked, a seductive sway to her hips, as she sauntered over to the cage."
    scene w3_13346 with dissolve
    "There she immediately sprang into action, gripping the cage like a prisoner, and sticking out her ass for the camera."
    mc "Ah, ~Hanaaaaa..."
    "She couldn't see me, so I put my all into intonating my satisfaction for the would-be jailbird."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w3_13347 with dissolve
    mc "Fuckin' A..."
    "From head-to-toe, her back was almost completely black, save for the lily white ass peaking out from the darkness like a tantalizing treat."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w3_13348 with dissolve
    "I wanted to stretch and devour it here and now, but--"

    scene w3_13349 with dissolve
    if hanaGF == True:
        hana "You're looking devious, boyfriend..."
    else:
        hana "You're looking quite dirty, [mcf]."

    scene w3_13350 with dissolve
    mc "I believe it... if only you could..."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w3_13351 with dissolve
    mc "...could feel what's going on with my insides."
    scene w3_13352 with dissolve
    "The expression on her lips was downright devilish, riding high on top of the world and taking ownership of my soul."
    scene w3_13353 with dissolve
    hana "I have a pretty good idea..."
    scene w3_13352 with dissolve
    "Complete, utter confidence in her own sexual appeal."
    scene w3_13354 with dissolve
    hana "Not going to tuck that into your waistband?"
    scene w3_13352 with dissolve
    mc "Just giving you something to be proud about..."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w3_13355 with dissolve
    mc "*Gulp* Ah..."
    "{i}Beautiful.{/b}"
    scene w3_13356 with dissolve
    mc "Let's get inside."
    hana "Mmhehe, {b}'kaaaaay.{/b}"
    scene black with fade
    mc "Just a few more..."
    scene w3_13357 with fade
    hana "Bed's pretty comfortable... care to join me?"
    scene w3_13358 with dissolve
    mc "{b}Pose.{/b}"
    scene w3_13359 with dissolve
    hana "Mmmh... {b}yes{/b}, sir..."
    scene w3_13360 with dissolve
    hana "I don't know what it is..."
    scene w3_13361 with dissolve
    "Hana splayed herself out beautifully, accentuating her hips and staring daringly into the camera."
    scene w3_13362 with dissolve
    hana "I'm so horny right now. Almost like I'm ovulating."
    scene w3_13361 with dissolve
    mc "...are you?"
    scene w3_13362 with dissolve
    hana "Nuh uh, just feels like it... {b}fuck{/b}, I'm burnin' up."
    scene w3_13361 with dissolve
    mc "Ah... *ahem* there's..."
    "And {b}that{/b} was a look that made me want to impregnate her on the spot."
    mc "There's one more thing I want to photograph."
    scene w3_13360 with dissolve
    hana "Is this the part where I start taking off my clothes?"
    stop music fadeout 3.0
    scene black with fade
    mc "Stand up..."
    hana "Alright, now--"
    play sound "sound effects/camera-phone-shutter.wav"
    scene w3_13363 with fade
    play music "music/with-a-rose-in-your-teeth.ogg" fadein 3.0
    pause
    scene w3_13364 with dissolve
    hana "...huh? What are you photographing?"
    scene w3_13365 with dissolve

    if hanaGF == True:
        mc "Your face. I want a photo of you for my phone."
    else:
        mc "Your face."

    scene w3_13366 with dissolve
    mc "It can't be said enough. You're so goddamn beautiful. You're so... {b}pretty.{/b}"
    scene w3_13367 with dissolve
    hana "It's the makeup, idiot..."
    scene w3_13368 with dissolve
    mc "It's only accentuating your natural beauty, Hana. Smile for me."
    scene w3_13369 with dissolve
    hana "..."
    "Even with the situation standing, she hesitated, looking {i}bashful{/i} of all things."
    scene w3_13370 with dissolve
    hana "...okay."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w3_13371 with dissolve
    hana "{i}You dirty ass perv.{/i}"
    mct "(God, she truly was stunning.)"
    scene w3_13372 with dissolve
    "As I moved forward under a spell, the hunger must've been plain as day on my face, because--"
    "Hana herself held her breath in anticipation."
    scene w3_13373 with dissolve
    hana "Taking photos not enough anymore, Mister?"
    scene w3_13372 with dissolve
    "........."
    "......"
    scene w3_13374 with dissolve
    hana "...damn it, {b}dooooo~{/b} something!"
    scene hanabdr_01_a with dissolve
    show hanabdr_01
    hana "A-ahh-"
    mc "*Cwhup* Every... *Chwup* part *Chwup* o-of you~ *Chwup* is... *Chwup {i}perfect.{/i}"
    hana "Y-yeah, I get the idea... you don't... you don't need to keep saying that."
    mc "Need... has... {b}nothing{/b} to do with it. I'll say it until you get sick of it."
    hana "Ah, haa-♥"
    mc "I'm... *Chup* the luckiest... *Chwup~* dirty ass perv... *Chup* In. The. World."
    hana "W-what's... what's so great about me? {i}Seriously?{/i}"
    "Hana, so normally full of confidence, sounded doubtful."
    hana "I'm obnoxious... I..."
    "Maybe it was a normal, healthy person's response to unconditional praise, but..."
    hana "I don't have anything more than a high school education... I--"
    scene hanabdr_02_a with dissolve
    show hanabdr_02
    mc "{b}Alluring.{/b}"
    "I wanted to leave no room for doubt."
    mc "Exquisite."
    hana "Ah..."
    mc "Angelic."
    hana "Euuh... {b}stupid...{/b}"
    mc "Gorgeous."
    hana "D-dumb...!"
    mc "Lovely."
    hana "Horny bastard..."
    mc "Bewitching."
    hana "M-monkey b-brain...!"
    mc "Ravishing."
    hana "You're, aahh..."
    mc "Cute."
    hana "Ah, okay..."
    mc "Stunning."
    hana "M-maybe you're right..."
    mc "{b}Splendiferous!{/b}"
    hana "A-aah...♥"
    scene w3_13375 with dissolve
    hana "Pfft, splendiferous?! That--!"
    scene w3_13376 with dissolve
    hana "Mmmhhmmhmh?!"
    "She was all those things. {i}No discussion.{/i}"
    scene hanabdr_03_a with dissolve
    show hanabdr_03
    hana "Euuaahh...[mcf]... Iwwhmm..."
    "The headstrong Hana went slack in my arms, surrendering herself to a deep kiss."
    hana "-♥♥♥"
    scene w3_13377 with dissolve
    hana "A-ah... *gulp*..."
    "Limp and heavy, but I held onto her like precious china."
    scene w3_13378 with dissolve
    hana "Alright... I'm... *sigh* {i}splendiferous{/i}. Happy?"
    scene w3_13377 with dissolve
    scene w3_13379 with dissolve
    scene w3_13377 with dissolve
    "I was."
    scene w3_13380 with dissolve
    "........."
    scene w3_13381 with dissolve
    "......"
    scene w3_13382 with dissolve
    "...her face said it all, eyes locked on me. There was something good coming my way."
    scene w3_13383 with dissolve

    if w3HanaBrothelRP == True:
        hana "Welcome back to the Carnation Club, sir. How can I serve you?"
        scene w3_13384 with dissolve
        mc "What are you... {b}ah.{/b}"
        "Like last time, when she sucked my dick in the bar."
        scene w3_13385 with dissolve
        mc "You impressed me last time, girl."
        scene w3_13386 with dissolve
        hana "If I may be so forward... I would like to try something else."
        scene w3_13387 with dissolve
        hana "...may I?"
    else:
        hana "*Gulp* I... I'd like to try something."
        scene w3_13387 with dissolve
        hana "...you game?"

    scene w3_13388 with dissolve
    "Holy fuck. If you could bottle that look, Sophia's aphrodisiac would be out of business."
    scene black with fade
    play sound "sound effects/zipper.wav"
    "Without waiting for an answer..."
    scene w3_13389 with fade
    "...Hana freed the beast and rested it atop a bounty of porcelain titflesh."
    "The grotesque sight of my cock, in the wake of Hana's femininity, filled me with a throbbing potency."
    scene w3_13390 with dissolve
    hana "Use 'em..."
    play sound "sound effects/spit2.wav"
    scene w3_13391 with dissolve
    mc "--?!"
    scene w3_13392 with dissolve
    mct "({b}Holy!{/b})"
    scene w3_13393 with dissolve
    hana "Look me in the eye while you use my tits. That same look earlier when you said I was--"
    scene w3_13394 with dissolve
    mc "{b}Angelic.{/b}"
    hana "Y-yes...♥ That! Something about the way you were looking at me just--!"
    scene hanabdr_04_a with dissolve
    show hanabdr_04
    hana "{size=-10}Yes...♥♥♥{/size}"
    "This pure, witch of a woman--"
    mc "You're lovely...!"
    "She had me completely, without escape, soul trapped inside pools of incandescent amber."
    mc "You're..."
    "Not another word parted her full, dark lips, yet I moved my hips in accordance with Hana's unsung voice, trying in vain to recall all the synonyms I had just used to imperfectly describe her divinity."
    mc "...{i}s-stunning.{/i}"
    "The red staining her pale cheeks told a similar tale. Whatever she had cast on me had enthralled her the same."
    mc "Gorgeous..."
    "She just wholly surrendered her chest to me, looking up at me through lust-heavy eyes, head churning with bridled elation."
    mc "Eh-exquisite..."
    "Over and over, my dick slowly pushed its way through Hana's cleavage, lubricated by her own spit and meeting resistance from the taut lace prescribed by Mrs. Pulman."
    mc "Ah, aahh..."
    "And as uneven of a trek it was, awkwardly humping away at her chest with little support, {b}I did not mind.{/b}"
    mc "R-ravishing..."
    "Hana's visage alone was propelling me toward orgasm."
    $ renpy.music.set_volume(0.2, 3, channel = "music")
    play ambient "sound effects/heartbeart.wav"
    scene hanabdr_05_a with dissolve
    show hanabdr_05
    mc "Uh.. ah..."
    pause
    mct "(Ah, fuck... what were the other words?)"
    pause
    "Instead of thoughts, my head was filled with the thrumming of a heartbeat."
    pause
    "Mine, hers, or both... I didn't know."
    pause
    mct "(Seriously, what was I saying...?)"
    pause
    "No. There was a word."
    scene hanabdr_04_a with dissolve
    show hanabdr_04
    $ renpy.music.set_volume(1, 3, channel = "music")
    stop music fadeout 10.0
    stop ambient fadeout 10.0
    mc "N-none..."
    "A single word."
    mc "N-none of those words fit you. You're... y-you're... {size=-10}In--{/size}"
    "One perfect word that fit the feeling swelling inside of me."
    mc "Ah... In, in...!"
    "{i}What was it?{/i} In--"
    scene w3_13395 with dissolve
    mc "{size=+10}INEFFABLE!{/b}"
    scene w3_13396 with dissolve
    "That was it. {i}Ineffable.{/b}"
    scene w3_13395 with dissolve
    mc "Your beauty is too great to be put into words."
    scene w3_13396 with dissolve
    "{i}That was it.{/i}"
    scene w3_13397 with dissolve
    hana "[mcf]... f-fuck...!"
    play music "music/your-big-rock-concert.ogg"
    scene w3_13398 with dissolve
    hana "Harder!"
    scene w3_13399 with dissolve
    mc "H-heah?!"
    "A vice-like squeeze ground my thrusting to a near halt as Hana reclaimed ownership of her tits."
    scene w3_13400 with dissolve
    hana "Fuck my tits until you {b}ruin{/b} my beautiful face!"
    scene w3_13399 with dissolve
    mct "({b}F-fuck...!{/b})"
    scene hanabdr_06_a with dissolve
    show hanabdr_06
    "{i}Hana understood me.{/i}"
    "Even within the throes of her own passion, she was surgical with her words."
    "Over and over, my dick barreled through Hana's cleavage, lubrication and paltry resistance be damned."
    mc "A-ah..."
    "Over and over, I pistoned my hips in search of an explosive end; groans of the lowest order leaking from my throat."
    "{b}*Squick, ssqqqhh...!*{/b}"
    hana "Heeh, aahh...♥"
    "{i}No more praise.{/i}"
    mc "A-ah, mmhh, H-ana...!"
    "She didn't need it anymore. The witless devotion she was creaming herself over was instead written on my thrusting cock."
    "{b}*Squick, ssqqqhh...!*{/b}"
    "Instead, my words of reverence and worship were replaced by the sounds of flesh-on-flesh and the duet of our ragged breaths."
    mc "Uaah...♥♥ It feels--"
    "Every time I sawed close, her hot breath seared my glans."
    mc "F-fuck...!"
    "All the while, neither of us could look away. Our eyes remained locked, tangled in lusty free fall."
    mc "Oh, ohhh..."
    "There was no escape. Hana would meet oblivion with me head-on."
    mc "Gaawaah..."
    hana "Ah, haaa...♥ Go ahead..."
    "{i}Fuck.{/i} She knew...!"
    scene w3_13401 with dissolve
    hana "G-go ahead-- inwhhereee~♥"
    "She knew I was cumming even before I--"
    scene hanabdr_07_a with fade
    show hanabdr_07
    play sound "sound effects/spurt.wav"
    with flash
    mc "A-aaah....!"
    "Without hesitation, I shot my wad straight into Hana's eager mouth."
    play sound "sound effects/spurt.wav"
    with flash
    "Rope after rope painted her pretty pink tongue and splashed the back of her throat, but the succubus between my legs didn't flinch."
    "{i}She demanded it,{/i} eyes turned perpetually upward in lusty exhuberance."
    mc "H-holy shit...! {size=-10}Oh, whaa...{/size}"
    stop music fadeout 10.0
    scene w3_13402 with dissolve
    "........."
    scene w3_13403 with dissolve
    "......"
    scene w3_13404 with dissolve
    hana "...aaaaaww~"
    "She insisted. {i}Admire your work, you dumb bastard.{/i}"
    scene w3_13405 with dissolve
    mc "Ah... ha..."
    "Beautiful."
    "Beautiful. Beautiful."
    "Beautiful. Beautiful. Beautiful."
    scene w3_13406 with dissolve
    mc "{b}Good girl.{/b}"
    play sound "sound effects/gulp-short.wav"
    scene w3_13407 with dissolve
    hana "*Gulp* Aahh..."
    scene w3_13408 with dissolve
    "She swallowed at my direction."
    "Beautiful."
    if not persistent.w3HanaPaizuri:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3HanaPaizuri = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    scene black with fade
    hana "...[mcf]?"
    scene w3_13409 with fade
    hana "...was it good for you?"
    scene w3_13410 with dissolve
    mc "I think that's my line."
    scene w3_13411 with dissolve
    hana "Hehehe..."
    scene w3_13410 with dissolve
    mc "I was the only one who got--"
    scene w3_13409 with dissolve
    hana "Don't fuckin' keep score idiot."

    if w3HanaMomMeet == True:
        hana "Besides, technically, we're one-on-one today. Tie breaker to be determined later..."
    else:
        hana "This was fun."

    scene w3_13412 with dissolve
    "........."
    "......"
    scene w3_13413 with dissolve
    mc "...I die? This heaven?"
    scene w3_13414 with dissolve
    hana "If it was, you wouldn't be leaving me to babysit some rich loser."
    scene w3_13415 with dissolve
    mc "Uh... shit. He's probably done by now."
    scene w3_13414 with dissolve
    hana "If he is, he can wait another five or ten minutes, can't he?"
    scene w3_13412 with dissolve
    "........."
    "......"
    scene w3_13413 with dissolve
    mc "...shit, what's another 20 minutes? My boss needed me."
    scene w3_13416 with dissolve
    hana "........."
    scene black with fade
    $ renpy.end_replay()

    "......"
    "..."
    jump w3ExStage3Donezo



label w3ExSaunaStage3End:
    scene w3_13417 with dissolve
    if w3ExHallwayLucyGone == False:
        $ w3ExHallwayLucyGone = True

    "Elias and Dr. Chuck will probably be a while..."
    mct "(Let's find something to do...)"
    jump w3ExNavMenuStage3




screen w3ExHallwayStage3:

    imagemap:
        imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage3")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]

        if w3ExHallwayLucyGone == False:
            idle "gui/screens/imagemaps/w3ExHallway3Lucy_idle.png"
            hover "gui/screens/imagemaps/w3ExHallway3Lucy_hover.png"
            ground "gui/screens/imagemaps/w3ExHallway3Lucy_ground.png"
            hotspot (97,426,1500,1500) action Jump("w3ExHallwayLucyGlimpse")

        elif w3ExKOStage3Empty == False or w3ExKatHallwaySeen == True:
            idle "gui/screens/imagemaps/w3ExHallway3_empty.png"
            hover "gui/screens/imagemaps/w3ExHallway3_empty.png"
            ground "gui/screens/imagemaps/w3ExHallway3_empty.png"
        else:
            idle "gui/screens/imagemaps/w3ExHallway3_idle.png"
            hover "gui/screens/imagemaps/w3ExHallway3_hover.png"
            ground "gui/screens/imagemaps/w3ExHallway3_ground.png"
            hotspot (759,429,1500,1500) action Jump("w3ExHallwayKatBother")


label w3ExHallwayStage3:
    show black
    $ renpy.music.play("music/cello-suite-No-1-G-Major-Prelude.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w3ExHallwayStage3 with pixellate

label w3ExHallwayKatBother:
    if _in_replay:
        play music "music/cello-suite-No-1-G-Major-Prelude.ogg"
    scene w3_13418 with dissolve

    if kat_polite == True:
        "As I left Hana, I caught sight of Mrs. Pulman. She hadn't gotten very far."
    else:
        "As I left Hana, I caught sight of Kathleen. She hadn't gotten very far."

    "Looks like our Chief of Police has her cornered, and either his personal infatuation or the perfume had him... {i}handsy.{/i}"
    scene w3_13419 with dissolve
    jim "Haha, we'll need a top-up in the VIP room."
    scene w3_13420 with dissolve
    kat "Uh, huh... I'll see to it that you're well equipped..."

    if w3KatSnare == False:
        scene w3_13421 with dissolve
        kat "...but where do you think you're touching, tubby?"
        jim "Ah, I love that lip! If only we were thirty years younger! We'd make each other {i}miserable{/i}."
        scene w3_13422 with dissolve
        kat "If you were thirty years younger, you'd--"
        mct "(Welp, I'll leave her to it...)"
        "After all, it's {i}her{/i} job to handle him."
        scene black with fade
        $ w3ExKatHallwaySeen = True
        "I waited for everyone to clear out before moving on."
        jump w3ExHallwayStage3
    else:

        scene w3_9945 with dissolve
        kat "You grab my ass outside this evening, {b}we'll have problems...{/b}"
        scene w3_9946 with dissolve
        mc "{b}Counter point:{/b} it would be pretty fun to fuck with the police commissioner's crush on you..."
        scene w3_9947 with dissolve
        kat "Ha! I {i}would{/i} love to see Jim's face, but in that scenario... {b}I'd{/b} be doing the grab ass. Understood?"
        scene w3_13420 with dissolve
        mct "(...that's a bad idea.)"
        "A bad, bad idea."
        mct "(Plus, if I go over there, who knows what I might get wrapped up in. It could eat up the rest of my free time.)"

        menu:
            "Grab a tiger by the tail.":
                mct "(...fuck, let's mess with her.)"
                scene black with fade
                kat "...but where do you think you're touching, tubby?"
                jump w3ExHallwayKatFlirt
            "Go do something else.(w3ExKatHallwaySeen = True)":
                $ w3ExKatHallwaySeen = True
                "No."
                scene w3_13421 with dissolve
                kat "...but where do you think you're touching, tubby?"
                jim "Ah, I love that lip! If only we were thirty years younger! We'd make each other {i}miserable{/i}."
                "No. No. No, no."
                scene w3_13422 with dissolve
                kat "If you were thirty years younger, you'd--"
                "Bad idea."
                scene black with fade
                "I waited for everyone to clear out before moving on."
                $ renpy.end_replay()
                jump w3ExHallwayStage3

        jump w3ExNavMenuStage3

label w3ExHallwayKatFlirt:
    $ w3ExKatFlirt = True
    scene w3_13421 with dissolve
    jim "Ah, I love that lip! If only we were thirty years younger! We'd make each other {i}miserable{/i}."
    scene w3_13423 with dissolve
    kat "If you were thirty years younger, you'd be a poor patrolman not even worth a whore's time..."
    scene w3_13424 with dissolve
    kat "[mcf]!"
    mc "...is there anything I can do?"
    scene w3_13425 with dissolve
    "I ignored the feeling of danger as I placed a light touch on the small of Kathleen's back. A gesture a dirty old man in front of me might not pay any mind, but she would."
    scene w3_13426 with dissolve
    jim "I was just telling Kathy that she needed more hands around here!"
    scene w3_13427 with dissolve
    "It was spur of the moment, but as my hands traveled down her back, I couldn't help but feel {i}something{/i} at the memory of having gone balls deep in the club matriarch's ass."
    scene w3_13428 with dissolve
    "The elation of letting loose, as well as the bitch's paradoxical blend of tender acceptance and fucking with me. It was all fresh in my mind."
    "I had seen a side of her that the patrons never will. Suddenly, she didn't seem so scary."
    kat "We have enough help. August likes to say..."
    scene w3_13429 with dissolve
    "It made me feel all the more daring."
    scene w3_13430 with dissolve
    "She shot me a look that alone felt like it could kill me, a {i}what the fuck are you doing{/i}, but I placed my palm on her ass nonetheless."
    scene w3_13431 with dissolve
    kat "*Ahem* He says less is more when it comes to {i}business.{/i}"
    scene w3_13432 with dissolve


    if kat_polite == True:
        "Mrs. Pulman, to her credit, adapted quickly by removing every ounce of anger from her voice."
    else:
        "Kathleen, to her credit, adapted quickly by removing every ounce of anger from her voice."

    "This was the same impervious witch that stood over me in triumph after taking everything I had yesterday. A fact that made me feel petty and want to--"
    scene kat_x3_s1_a with dissolve
    show kat_x3_s1
    "{i}Win.{/i}"
    mc "Well, here's a pair of {i}hands{/i}. What can I do for you, Mr. O'Doherty?"
    jim "Is everything okay, Kathy?"
    "From this angle, Jim couldn't tell what I was doing, but was puzzled reading the old woman's odd expression."
    jim "You look like you need to take a shit..."
    kat "I'm... {i}fine.{/i} Jim needs more Viagra in the VIP room."
    jim "Huh?! I was talking about the usual platter of stuff! Why would you think--"
    kat "Oh, I just assumed... I mean, I've seen you pop 'em by the handful."
    "Even with my fingers digging deep into the flesh of her fat ass, the devilish woman didn't miss an opportunity to belittle the man in front of her."
    jim "I was just making sure we aren't dry for Elias' {i}pre-welcome{/i} welcome in the velvet room! I hear he has an {i}itchy{/i} nose."
    mc "What's going on in the velvet room?"
    jim "Lots of fun! You'll be there!"
    mc "I will?"
    scene w3_13433 with dissolve
    kat "You... {i}will.{/i}"
    scene w3_13434 with dissolve
    "Oh, no. It was just there for a flash, but the edge in her voice was razor sharp and vicious."
    scene w3_13435 with dissolve
    kat "Go to the bar and get one of the girls to drop off some ketamine and coke."
    kat "After that, I need to talk to you in my office. {b}Don't dally.{/b}"
    scene w3_13436 with dissolve
    mc "Uh... {i}yes{/i} Ma'am..."
    stop music fadeout 3.0
    scene black with fade
    "Shit."
    "Shit. shit. shit."
    "Like a misbehaving child on pins and needles waiting for their father to get home, the walk to the bar and the office gave me {b}plenty{/b} of time to think about what I had done."
    "........."
    "......"
    "..."
    play music "music/hypnosis.ogg"
    scene w3_13437 with fade
    kat "What the fuck do you think you were doing?!"
    "The moment I opened the door, she was on me. Angry. {b}Livid.{/b}"
    scene w3_13438 with dissolve
    kat "I'm not some fucking whore you can grope as you please!"
    "This was... {b}new.{/b} Uncalculated and honest. In a way that I had never seen from the collected woman."
    scene w3_13439 with dissolve
    kat "I told you {i}specifically{/i} not to do {b}that.{/b}"
    "I had screwed up, grown too comfortable and deluded myself into thinking she might find the whole thing a playful injoke."
    scene w3_13440 with dissolve
    kat "I told you {b}NOT{/b}--"
    "{i}Why in God's name would I ever think that?{/i}"
    scene w3_13441 with dissolve
    kat "Did I give you the impression that you didn't need to respect me? God, men are so fucking predictable."
    mct "(Well, fuck...)"
    scene w3_13442 with dissolve
    kat "You give them a taste and they think they own the cow!"
    "There were probably no words that would appease her, so the only conciliation would be just to stand here and take it on the chin."
    scene w3_13443 with dissolve
    kat "Am I a joke to you, [mcf]? What would you have done if--"
    "So I stood, half-hearing, watching the old woman flap her gums and poke my chest."
    "Waiting for her to finish, but she just kept on and on and {i}a funny thing happened.{/i}"
    scene w3_13444 with dissolve
    kat "You're lucky--"
    scene w3_13445 with dissolve
    "With flight not being the option, I was starting to feel indignant."
    scene w3_13446 with dissolve
    kat "That I-"
    "What was she on about?"
    "She pokes and prods me for her satisfaction, makes insinuations about my mother, and she's blowing up over an innocuous touch? This was stupid."
    scene w3_13447 with dissolve
    kat "And furthermore--"
    scene w3_13448 with dissolve
    scene w3_13449 with hpunch
    mc "Shut the {b}FUCK{/b} up! Get out of my face!"
    scene w3_13450 with dissolve
    kat "You-- {b}did you just--?!{/b}"
    mct "(Oh, fuck oh fuck oh fuck. What am I doing?! I--)"
    scene w3_13451 with dissolve
    mc "Jesus Christ, are you listening to yourself?"
    "Oh, welp. {i}Guess I'll double the fuck down.{/i}"
    scene w3_13452 with dissolve
    kat "It's a matter of respect!"
    mc "{b}Respect?!{/b} You pimp out desperate women out of a charity!"
    scene w3_13453 with dissolve
    mc "Just {i}yesterday{/i} you were encouraging me to do what I want to do, and guess what? That's exactly what I did, you stupid bitch!"
    mc "I saw your fine ass and wanted to grab it!"
    scene w3_13454 with dissolve
    kat "That comes with the caveat of what you can afford to get away with, you {b}dumb bastard!{/b}"
    scene w3_13455 with dissolve
    mc "Oho! {i}And{/i} what did touching Kathleen Pulman's posterior cost me, exactly? Am I going to end up like Darius?"
    scene w3_13454 with dissolve
    kat "Oh, don't give me idea--"
    scene w3_13455 with dissolve
    mc "Whatever it costs, {b}it was worth it.{/b}"
    scene w3_13456 with dissolve
    kat "You...!"
    scene w3_13457 with dissolve
    "For a blood-curdling second, I felt a very real possibility that she might plunge a letter opener deep into my chest."
    mc "What are you--"
    play ambient "sound effects/kissing3.wav"
    play music "music/addict.ogg"
    scene kat_x3_s2_a with dissolve
    show kat_x3_s2
    "Instead, she did something even more terrifying."
    "I {b}kissed{/b} Kathleen Pulman, an act that somehow felt more transgressive than what came before."

    if w2KatSex == True:
        "More than when we fucked."
    if w3KatPromoFinish == True:
        "More than when I nutted down her spasming throat."

    "More than when I buried every inch of my cock deep in her ass."
    "This was unexpected."
    "{i}This{/i} was unholy."
    "Forget grabbing the tiger by the tail, I was traipsing right into the maneater's jaw."
    kat "Mmhh..."
    "Scariest most to admit..."
    "{i}It felt good.{/i}"
    "Her lips were sweet like black licorice and her touch felt like a bed of nails."
    "She didn't melt into my arms like a warm lover, but instead lulled me into a hypothermic stupor."
    stop ambient
    play sound "sound effects/munch.wav"
    scene w3_13458 with flash
    mc "--?!"
    "Then a salty sting."
    scene w3_13459 with dissolve
    mc "--?!"
    "{i}Then{/i} the warm taste of copper."
    scene w3_13460 with dissolve
    pause
    scene w3_13461 with dissolve
    pause
    play sound "sound effects/thud-heavy.wav"
    scene w3_13462 with vpunch
    "Before I knew it, the tables were literally turned."
    scene kat_x3_s3_a with dissolve
    show kat_x3_s3
    "Kathleen climbed atop me like I was to be sacrificed."
    "{i}I didn't breathe.{/i}"
    "I physically couldn't."
    "She was just an old woman. It would be so easy to regain control, to shift my weight or to push her off..."
    scene kat_x3_s4_a with dissolve
    show kat_x3_s4
    "I didn't."
    "I couldn't."
    "And I wouldn't."
    "{i}Fuck, I'm turned on.{/i}"
    pause
    "...was this the end of [mcf] [mcl]?"
    scene w3_13463 with dissolve
    kat "That was... {i}unexpected.{/i}"
    scene w3_13464 with dissolve
    "A wry smile released me from Mrs. Pulman's hold and brought me back to my senses. I wasn't in a spider's web, but merely flat on my back upside the cold marble of the old woman's desk."
    scene w3_13463 with dissolve
    kat "Unexpected, {b}BUT{/b}..."
    scene w3_13465 with dissolve
    kat "Interesting."
    scene w3_13466 with dissolve
    "I'm not sure if I preferred the electrifying illusion or the pathetic reality..."
    scene w3_13467 with dissolve
    kat "Get up."
    scene w3_13466 with dissolve
    "I looked at her dubiously. The implications of what we just did... I mean..."
    scene w3_13467 with dissolve
    kat "I'm not going to bite you... {i}again.{/i}"
    scene w3_13468 with dissolve
    "{i}What the fuck?!{/i}"
    scene w3_13469 with dissolve
    "Judging by her words, she didn't know either, but with age comes poise."
    scene w3_13470 with dissolve
    "Meanwhile, the look on my face must have said it all."
    scene w3_13471 with dissolve
    kat "To think... {i}you had the balls{/i} to force yourself on me."
    scene w3_13472 with dissolve
    mc "Forced...? {b}You bitch.{/b} Who kissed who here?!"
    scene w3_13473 with dissolve
    kat "That..."
    "An actual, legitimate question when it all happened so fast..."
    scene w3_13474 with dissolve
    kat "Me?! Tell me, who groped who in the hallway and began this whole thing?! You--"
    stop music fadeout 7.0
    scene w3_13475 with dissolve
    "........."
    "......"
    scene w3_13476 with dissolve
    kat "...how disappointing. You won't even take ownership of your own impulses."
    scene w3_13477 with dissolve
    "The rejection on the old woman's face hit me like a bag of bricks."
    mct "(Disappointing...?)"
    scene w3_13476 with dissolve
    kat "*Sigh* I shouldn't have gotten my hopes up."
    scene w3_13477 with dissolve
    mct "(I was disappointing...?)"
    "Why did I suddenly, outside of her being my boss, care about her opinion? Did I just want to prove her wrong?"
    "My mind went back to yesterday. That elusive feeling of freedom and unconditional acceptance."
    scene w3_13478 with dissolve
    "It was turning its back on me."
    scene w3_13479 with dissolve
    kat "Don't mistake my passing curiosity as anything else. You grab me again in public, and I won't be so forgiving. Is that understood?"
    scene w3_13478 with dissolve
    "Why did that make me feel so bleak?"
    scene w3_13479 with dissolve
    kat "I'll take your silence as a yes."
    scene w3_13480 with dissolve
    mct "(Just let her walk away, [mcf]...)"
    scene w3_13481 with dissolve
    "Let her walk away and put yourself back neatly in a well-worn box."
    scene black with fade
    "........."
    "......"

    if Kathleen_Affection >= 15:
        $ katAffair = True
        play music "music/doll-dancing.ogg"
        kat "...what do you think you're doing?"
        scene w3_13482 with dissolve
        mc "You didn't say anything about grabbing you in private."
        kat "I..."
        scene w3_13483 with dissolve
        kat "{b}There{/b} he is. The ~lion from earlier."
        scene w3_13484 with dissolve
        "Something about the seductive lilt in her voice, the way she teased out the word {b}lion{/b}, sent shivers down my spine."
        "She had a way of making me believe it."
        scene w3_13485 with dissolve
        kat "If we're going to explore this, we have to set some ground rules..."
        mc "Rules...?"
        scene w3_13486 with dissolve
        kat "A-aah...?!"
        scene w3_13487 with dissolve
        mc "{b}Fuck that.{/b} There's only one."
        scene w3_13486 with dissolve
        kat "...w-{b}what?{/b}"
        scene w3_13487 with dissolve
        mc "We only do what we're willing to meet the consequences for."
        scene w3_13486 with dissolve
        kat "That's not carte blanche to treat me like a whore--"
        scene kat_x3_s5_a with dissolve
        show kat_x3_s5
        kat "--{b}a-ah!{/b}"
        mc "You're a beautiful woman, Kathleen. Who..."
        kat "C-call me Kat..."
        mc "You're a beautiful woman, Kat. Why would I treat you less than you deserve?"
        kat "H-ha...! {i}Deserve?{/i} Such a malleable...!"
        mc "Right? It's a word {b}full{/b} of possibilities."
        kat "A-ahh...♥ You have no idea what you're stepping into..."
        mc "That's what makes it thrilling. You'll have to teach me."
        "She seemed fond of that word yesterday."
        kat "A-ahh... I was {b}right{/b} about you. You've got a killer's instinct."
        kat "You just know what to say and what buttons to push..."
        mc "Make up your mind, first you were disappointed in me."
        scene w3_13488 with dissolve
        kat "Oh! You actually believed that?"
        "She was right about one thing."
        scene w3_13489 with dissolve
        "I had no idea what I was stepping into. "
        scene w3_13490 with dissolve
        kat "I told you yesterday... I'll accept who you are. I just want to see the whole picture."
        scene w3_13491 with dissolve
        "Not what it meant for my longevity at the club, nor what this growing feeling of emancipation would spell for who I wanted to be."
        scene w3_13492 with dissolve
        kat "Mmmh, you don't know how badly I want to {b}fuck{/b} right now, but sadly--"
        scene w3_13493 with dissolve
        mc "We don't have the time."
        scene w3_13492 with dissolve
        kat "Not for anything that would satisfy me."
        scene w3_13494 with dissolve
        kat "*Cwhup~*"
        scene w3_13495 with dissolve
        kat "I guess we'll see where this goes. Should be fun."
        scene w3_13496 with dissolve
        mc "Yeah..."
        scene black with fade
        mct "(Who I wanted to be?)"
        $ renpy.end_replay()

        if not persistent.w3KatFlirt:
            play sound "sound effects/notification.wav"
            show memoryunlock with dissolve
            $ renpy.pause(3, hard=True)
            $ persistent.w3KatFlirt = True
            hide memoryunlock with dissolve
            $ renpy.pause(0.5, hard=True)
            "...how could I know without exploring that?"
            "{i}Should be fun.{/i}"
    else:

        "..."
        scene w3_13480 with dissolve
        "She was right. {i}I can't even take ownership of your own impulses.{/i}"
        scene w3_13481 with dissolve
        "Thankfully it sounded like she was willing to sweep my insanity under the rug and pretend like it didn't happen."
        scene w3_13497 with dissolve
        mct "(Yes, this is for the best...)"
        "If I did what I really wanted to do, to stop her and prove her wrong, there's no telling what it would spell for both my longevity at the club and for who I wanted to be."
        scene black with fade
        "........."
        "......"
        "..."

    jump w3ExStage3Donezo


label w3ExHallwayLucyGlimpse:
    $ w3ExHallwayLucyGone = True
    scene w3_13501 with fade
    "As I passed by, I caught sight of Lucy ducking into the house girl dressing room."

    if w3ExIsaakPromise == True:
        "I did promise Isaak that I'd point her in his direction..."
    else:
        mct "(Isaak's been looking for her...)"

    scene w3_13502 with dissolve
    "Plus, even Harper asked me to make sure she doesn't shirk her duties..."


    menu:
        "Go talk with her now.\n(w3ExHDROPen = True, w3ExLucyNow = True)":
            $ w3ExHDROPen = True
            $ w3ExLucyNow = True
            scene w3_13503 with dissolve
            mc "*Sigh* I guess it {i}is{/i} part of my responsibilities."
            scene black with fade
            mct "(I'll go say hello.)"
            jump w3ExHDRStage3
        "Give the lady some time alone.\n(w3ExHDROPen = True)":

            $ w3ExHDROPen = True
            scene w3_13503 with dissolve
            "She's probably collecting herself after Shelby chased her off. I'll give her some time to breathe."
            "Maybe I'll swing by later, maaaaaybe I won't..."
            jump w3ExHallwayStage3
        "You'd rather not.":

            scene w3_13504 with dissolve
            mct "(Eh... whose to say I saw her.)"
            "She's probably collecting herself after Shelby chased her off."
            "Her avoiding Isaak or his dissatisfaction, {i}whatever.{/i} That's between them."
            jump w3ExHallwayStage3




screen w3ExHDRStage3:

    imagemap:
        if w3ExLucyNow == False:
            imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage3")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        idle "gui/screens/imagemaps/w3ExHDR3_idle.png"
        hover "gui/screens/imagemaps/w3ExHDR3_hover.png"
        ground "gui/screens/imagemaps/w3ExHDR3_ground.png"
        hotspot (690,456,250,250) action Jump("w3ExHDRLucy")

label w3ExHDRStage3:
    show black
    $ renpy.music.play("music/air-on-g.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w3ExHDRStage3 with pixellate

label w3ExHDRLucy:
    scene w3_13505 with dissolve
    if w3ExLucyNow == True:
        mct "(...huh? I saw her come in here. Where...)"
    else:
        mct "(Hmm...)"
        mct "(Has see already left...? Where...)"

    scene w3_13506 with dissolve
    mc "({b}Aha!{/b})"
    scene w3_13507 with dissolve
    mc "I spy with my little eye, something that is..."

    menu:
        "Beautiful.":
            scene w3_13508 with dissolve
            mc "The most beautiful raven hair I have ever--"
        "Naughty.":
            scene w3_13509 with dissolve
            if toughness >= 22:
                mc "A whore neglecting her--."
            else:
                mc "A woman neglecting her--"

    scene w3_13510 with dissolve
    lucy "{b}Oh, eohh--?!{/b}"
    lucy "...it's you!"
    scene w3_13511 with dissolve
    mc "Sorry to startle you. Senator Shelby sure is prickly, huh?"
    scene w3_13512 with dissolve
    "........."
    "......"
    scene w3_13513 with dissolve
    lucy "...I can't believe I voted for that prick! {b}Twice!{/b}"
    scene w3_13514 with dissolve
    "........."
    "......"
    scene w3_13515 with dissolve
    lucy "Pfft--"
    "She and I both appreciated the absurdity in that."
    scene w3_13516 with dissolve
    mc "Haha, yeah... tonight has kinda ruined my sense of civic duty. Our future mayor's here."
    lucy "Yeah, wow... that hadn't escaped my notice."
    scene w3_13517 with dissolve
    mc "You doing alright? Don't let Shelby--"
    scene w3_13518 with dissolve
    lucy "No, no... it's... *sigh* I'm glad he did. All the girls have stories about him."
    scene w3_13519 with dissolve
    mc "I've heard, and you got saddled with him?"
    scene w3_13520 with dissolve
    lucy "Saddled? No... I... more like first-come, first-served. I wanted to make sure I had someone, and Senator Shelby was the first person I saw..."
    scene w3_13518 with dissolve
    lucy "Anyone is better than--"
    scene w3_13521 with dissolve
    lucy "And oh {b}God!{/b} Now Harp's covering him and I'm hiding in here!"
    scene w3_13522 with dissolve
    "Evidently, even in a setting like this, Lucy possessed a strong sense of responsibility."
    mc "We can both call it a \"breather\" if you'd like... hiding is--"
    scene w3_13521 with dissolve
    lucy "...is EXACTLY what I'm doing. I was hoping no one would find me."
    scene w3_13523 with dissolve
    "......"
    mc "...what are you hiding from?"
    scene w3_13520 with dissolve
    lucy "I don't know! Everything out there...? My husband? My son?"
    scene w3_13518 with dissolve
    lucy "{b}My own stupid ass?!{/b}"
    scene w3_13524 with dissolve
    lucy "I just want to crawl into a ball..."
    mc "That sounds... {i}tough.{/i}"
    scene w3_13525 with dissolve
    lucy "Why am I...? Yeah, {b}I know.{/b} I'm having a moment. You don't care."
    scene w3_13526 with dissolve
    "........."
    "......"
    scene w3_13527 with dissolve
    mc "...uh, you're a bit neurotic, aren't you?"
    scene w3_13528 with dissolve
    lucy "{b}Clearly!{/b}"
    scene w3_13529 with dissolve
    "Lucy was obviously overwhelmed tonight. I had come here for a reason, to yet again play whore wrangler, but the thought of herding her in this emotional state into Isaak's hands..."

    menu:
        "Spend some time with the teacher trying to get her battle-ready.\n(w3LucyEdwinTime = True)":
            $ w3LucyEdwinTime = True
            scene w3_13530 with dissolve
            mc "Well, me too."
            scene w3_13531 with dissolve
            "It felt both cruel and like bad business."
            mct "(It would be irresponsible sending her into a customer's hands in that state, right...?)"
            scene w3_13532 with dissolve
            mc "Sit down. I'll run up to the bar."
            scene w3_13533 with dissolve
            lucy "What are you...?"
            mct "(Yeah...)"
            scene w3_13534 with dissolve
            mc "What? You want me to tell Mrs. Pulman?"
            "{i}Bad business.{/i}"
            scene w3_13535 with dissolve
            lucy "Oh o-okay!"
            stop music fadeout 3.0
            scene black with fade
            "I was being prudent by having a drink with the half-naked, big-breasted school teacher."
            "..."
            jump w3ExLucyEdwin
        "Let her hide.\n(w3LucyAvoided = True, w3ExHDROPen = False)":

            $ w3LucyAvoided = True
            $ w3ExHDROPen = False
            scene w3_13536 with dissolve
            mc "Alright then. Take as much time as you'd like."
            scene w3_13537 with dissolve
            lucy "You aren't going to tell Mrs. Pulman?"
            scene w3_13538 with dissolve
            mc "My job is the Carnations, and you lost that job."
            scene w3_13539 with dissolve
            lucy "Yeah..."
            "{i}What could've been.{/i}"
            scene w3_13534 with dissolve
            mc "I should say Harper did want me to remind you {i}why{/i} you're here."
            scene w3_13540 with dissolve
            lucy "Like I've forgotten..."
            scene w3_13541 with dissolve
            mc "Alright then, I've done my part."
            lucy "You really aren't going to--"
            mc "{b}Nope!{/b} Bye!"
            scene black with fade
            "That was that. She had only herself to blame for being here, but that didn't mean I couldn't cut her some slack."
            jump w3ExHallwayStage3
        "Stand on business.\n(w3LucySent = True, w3ExHDROPen = False)":

            $ w3LucySent = True
            $ w3ExHDROPen = False
            scene w3_13542 with dissolve
            "I pushed out any nagging feeling of sympathy."
            scene w3_13543 with dissolve
            mc "By the way... Mr. Miller has requested your time."
            scene w3_13544 with dissolve
            "........."
            "......"
            scene w3_13545 with dissolve
            lucy "...okay."
            scene w3_13546 with dissolve
            mct "(...Jesus Christ.)"
            "She looks like she was just given six months to live."
            scene w3_13547 with dissolve
            mc "Is he really that bad? Compared to some of the other patrons, he's relatively harmless, isn't he?"
            scene w3_13548 with dissolve
            lucy "HARMLESS...?! He...!"
            lucy "I don't know what to call a feeling of ick so bad that you'd rather die! I tried to ignore it last week, but..."
            scene w3_13549 with dissolve
            lucy "Ugh!"
            scene w3_13550 with dissolve
            mc "You've swallowed more bitter pills these past few weeks, surely..."
            scene w3_13551 with dissolve
            lucy "It's stupid, I know. You're telling me to fuck him, right?"
            scene w3_13552 with dissolve
            "{i}Sudden, cold acceptance.{/i} Truly an indecipherable woman."
            scene w3_13553 with dissolve
            mc "I'm relaying his request. I can't make you do anything."
            mc "Although, I think Harper wanted me to remind you of {b}why{/b} you're doing this. Sunk cost or whatever..."
            scene w3_13551 with dissolve
            lucy "She knows best..."
            scene w3_13553 with dissolve
            mc "No, she's not stupid, is she?"
            scene w3_13551 with dissolve
            lucy "Can I at least have a moment...?"
            scene w3_13553 with dissolve
            mc "Sure. As long as you think best."
            scene w3_13554 with dissolve
            mc "See you around."
            scene w3_13555 with dissolve
            "{i}Whatever.{/i} I was done with this."
            "She signed up to play whore. {i}Do your job, bitch.{/i}"
            scene black with fade
            "......"
            "..."
            jump w3ExHallwayStage3


label w3ExLucyEdwin:
    play music "music/select.ogg"
    scene w3_13556 with fade
    lucy "How did you know I liked this?"
    scene w3_13557 with dissolve
    mc "I know {i}everything{/i} about you."
    scene w3_13558 with dissolve
    lucy "R-really...?"
    scene w3_13557 with dissolve
    mc "No. I saw you drink it at the bar a few weeks ago."
    scene w3_13558 with dissolve
    lucy "Oh... {i}yeah.{/i}"
    scene w3_13559 with dissolve
    "........."
    "......"
    scene w3_13560 with dissolve
    lucy "...wow, you're a freak."
    scene w3_13561 with dissolve
    mc "I know, but my memory is the least of it."
    scene w3_13562 with dissolve
    lucy "P'aah, my husband can't even remember the brand of tea I drink at the store."
    "She trailed off, looking like she was running some calculations in her head."
    scene w3_13563 with dissolve
    lucy "And don't even get me started on my dumbass son - {i}never{/i} remembers a single thing you tell him."
    scene w3_13564 with dissolve
    mc "Teenagers have lots of things to worry about."
    lucy "Like video games?"
    scene w3_13565 with dissolve
    mc "Becoming a full-formed person can be daunting."
    "And the more she calculated..."
    scene w3_13566 with dissolve
    lucy "{b}Bullshit.{/b} He doesn't have a single critical thought running through his head, just screams and curses at his shooting game friends on the internet."
    "...the more faults she found in her life."
    scene w3_13567 with dissolve
    lucy "He's spoiled rotten! My fault, of course... but what's wrong with wanting the best for your kid?! {size=-5}Ungrateful little shit...{/size}"
    scene w3_13563 with dissolve
    lucy "Just yesterday, Benny yelled at me for interrupting his video games. After all I've been doing for him! All I'm {b}currently{/b} doing for him!"
    scene w3_13567 with dissolve
    lucy "Like, I know you can't pause multi-player! I just don't give a crap!"
    scene w3_13568 with dissolve
    "Part of me was inclined to just shut up and let her vent, as watching the school teacher gesticulate wildly was downright entertaining."
    "The entitlement she was spewing wasn't anything new. I was familiar with the brand, but watching her ample flesh jiggle more and more as she got heated made for an {i}appreciable{/i} distinction from the mothers of the students I used to tutor."
    scene w3_13569 with dissolve
    mc "You've got something backwards..."
    scene w3_13570 with dissolve
    lucy "What?!"
    scene w3_13571 with dissolve
    mc "Don't lay {i}this{/i} choice at his feet. Does he even want to get into St. Ives?"
    scene w3_13572 with dissolve
    lucy "No! No..."
    scene w3_13573 with dissolve
    lucy "...he doesn't. *Sigh* What's the point?"
    scene w3_13574 with dissolve
    lucy "He'll get into St. Ives and just be... {i}mediocre.{/i} He isn't going to start magically applying himself, I know that..."
    lucy "All I'm doing here is just..."
    scene w3_13575 with dissolve
    "........."
    "......"
    scene w3_13576 with dissolve
    mc "...it sounds like you want to quit."
    scene w3_13577 with dissolve
    "For some time, she merely looked at me, an inscrutable expression plastered on her face."
    "{i}For a second{/i}, she looked like she was coming to terms with something."
    scene w3_13578 with dissolve
    lucy "I don't."
    scene w3_13579 with dissolve
    mc "...no?"
    scene w3_13578 with dissolve
    lucy "No. I've lived and felt more in the past few weeks than I have in ten years."

    if w3LucyGrope == True:
        stop music fadeout 5.0
        scene w3_13580 with dissolve
        lucy "You were right the other night, at the art show... {b}ha...{/b}, Goddamnit you were right."
        lucy "I'm enjoying some parts of this... playing arm candy during dinner dates, getting my brains fucked out by a rich CEO, and..."
        scene w3_13581 with dissolve
        lucy "*Gulp* Getting manhandled publicly by a kid."
        if w3LucySupergrope == True:
            scene w3_13600 with pixellate
        else:
            scene w3_13599 with pixellate
        mc "...ah, is that right?"
        lucy "Y-yeah..."
        play music "music/six-days-of-heat-pt2.ogg"
        scene w3_13582 with pixellate
        "That look she served me was a provocation, but she made no move of her own."
        "She just sat there in anticipation, waiting for {i}something{/i} to help her digest the hard truth she had swallowed."
        scene w3_13581 with dissolve
        lucy "I just wish I wasn't me, that the other parts weren't there to interfere with enjoying this..."
        scene w3_13582 with dissolve
        "{i}Finish what you started.{/i}"
        scene w3_13583 with dissolve
        mc "...{i}this?{/i}"
        scene w3_13584 with dissolve
        lucy "Y-yes..."
        scene w3_13585 with dissolve
        mc "Stand up."
        lucy "A-aaah...♥"
        scene black with fade
        "I was loving this job right about now."
        jump w3ExLucyFuck
    elif w3LucyArtKiss == True:
        stop music fadeout 5.0
        scene w3_13579 with dissolve
        mc "...when did you realize that?"
        scene w3_13578 with dissolve
        lucy "Just now, while blabbing my guts out to a dumb college kid."
        scene w3_13577 with dissolve
        mct "(That {i}is{/i} talent, it seems...)"
        scene w3_13580 with dissolve
        lucy "Never in my life have I been someone's arm candy at an art show. And boring Lucy would never dream of fucking a rich CEO, or..."
        scene w3_13581 with dissolve
        lucy "...spontaneously {b}kiss{/b} a man as young as my nephew."
        scene w3_13601 with pixellate
        mc "...ah, is that right?"
        lucy "Y-yeah..."
        play music "music/six-days-of-heat-pt2.ogg"
        scene w3_13582 with pixellate
        "That look she served me was a provocation, but she made no move of her own."
        "She just sat there in anticipation, waiting for {i}something{/i} to help her digest the hard truth she had swallowed."
        scene w3_13581 with dissolve
        lucy "I just wish I wasn't me, that the other parts weren't there to interfere with enjoying this..."
        scene w3_13582 with dissolve
        "{i}She was looking for reassurance,{/i} that she was free to be as dirty as she could be."
        "{i}I sympathized.{/i}"

        menu:
            "{mod_green}Make a move.":
                scene w3_13583 with dissolve
                mc "...what do you want to do, Mrs. Long?"
                scene w3_13586 with dissolve
                lucy "C-can I?"
                mc "If you don't, {b} I will.{/b}"
                scene w3_13587 with dissolve
                lucy "--!"
                scene black with fade
                "With her blushing like a young woman, how could I deny her?"
                jump w3ExLucyFuck
            "She's got a job to do.":

                $ w3ExHDROPen = False
                jump w3ExLucyNoFuck
    else:
        $ w3ExHDROPen = False
        scene w3_13579 with dissolve
        mc "...when did you realize that?"
        scene w3_13578 with dissolve
        lucy "Just now, while blabbing my guts out to a dumb college kid."
        scene w3_13588 with dissolve
        mct "(That {i}is{/i} talent, it seems...)"
        scene w3_13580 with dissolve
        lucy "Never in my life have I been someone's arm candy at an art show or getting my brains screwed out by a rich CEO, yet here I sit..."
        scene w3_13589 with dissolve
        mc "Huh..."
        scene w3_13588 with dissolve
        "Lucy sat there quietly for a moment, digesting a hard truth about herself."
        scene w3_13580 with dissolve
        lucy "I just wish I wasn't me, that the other parts weren't there to interfere with... {i}enjoying{/i} this."
        scene w3_13588 with dissolve
        mc "That's..."
        "{i}Okay...{/i}"
        jump w3ExLucyNoFuck


label w3ExLucyFuck:

    if _in_replay:
        play music "music/six-days-of-heat-pt2.ogg"
        show transitionlucy01 with cmet
        show screen textbox2 with dissolve
        "Did you kiss Lucy during Felicia's art exhibition?"
        hide screen textbox2 with dissolve

        menu:
            "Yes.":
                $ w3LucyArtKiss = True
            "No.":
                pass
        scene black with fade

    $ w3ExLucyFuck = True
    "..."
    play sound "sound effects/thud-floor.mp3"
    with hpunch
    lucy "Gwwahh--"
    play ambient "sound effects/kissing3.wav"
    scene lucyex3_01_a with circlewipe
    show lucyex3_01
    "After a bit of a scramble, I had the school teacher pinned against the lockers, tongue down her throat in an exploratory bid for control."
    lucy "Mmmh, mmhhh- ♥"
    "--and Lucy was all too happy to let me lead, moaning through lip and teeth."
    lucy "Ah- ahhh..."
    "Tonight I'd go all the way."
    "I had wanted to do as much since Lucy first faced off against Veronica all those weeks ago, but there it was just a nascent urge."
    "The kind that would creep into any man's mind from seeing a beautiful woman debauched."
    lucy "MMmhh, mwwahh-♥"
    "Now it was a concrete reality slack in my grip, breathing heavy and hopeful, surrendering herself to me."
    lucy "Yaaee... mmhhh..."
    "Faces that I would probably never know, of her husband and son, materialized in my mind."
    lucy "Ao- ahhh..."
    "This woman, a wife and mother, is betraying all sense of fidelity and maternal instinct in lieu of a fleeting thrill."
    stop ambient
    scene w3_13590 with dissolve
    if w3LucyArtKiss == True:
        mc "This is what you want?!"
    else:
        mc "This is what you want, you little whore?!"

    scene w3_13591 with dissolve
    "An ugly, regrettable impulse that was turning {b}both{/b} of us on."
    scene w3_13592 with dissolve
    lucy "Ah, yeea, {b}y-yes!{/b}"
    scene w3_13593 with dissolve
    lucy "{b}Yes!{/b}"
    scene w3_13594 with dissolve
    lucy "Do what you--"
    scene black with fade
    scene lucyex3_02_a with dissolve
    show lucyex3_02
    "--what I wanted?"
    "*Chwup~*"
    "{b}Okay.{/b}"
    "Ever since the art show, I wanted a taste. Because {i}hot damn did she look impeccable that night.{/i}"
    lucy "Nyeeah, neee... a-ah..."
    "{b}TONIGHT TOO{/b}, what with breasts framed and hips flared by lustrous black leather."
    lucy "Ah, y-you......"
    "Lucy was a delicacy and I would make sure she {b}fully{/b} understood that."
    lucy "Y-uoii... you're g-good at that..."
    "I would help fade all the parts of herself that she wished away."
    lucy "Fu-fuhhh..."
    "The school teacher's eyes were already glassed over, mind ensnared by the promise of escape from her dreary daily life."
    $ renpy.music.set_volume(0.1, 1, channel = "music")
    scene black with fade
    play ambient "sound effects/kissing1.mp3"
    pause
    $ renpy.music.set_volume(1, 1, channel = "music")
    scene lucyex3_03_a with fade
    show lucyex3_03
    lucy "O-ohhh... {size=-5}ooohww~{/size}"
    "*Cwhup, fwhhp-*"
    lucy "{size=-10}Eeuaahh...{/size}"
    "A minute passed before even a lonely thought passed between my ears, all for me to discover my lips now fervently locked around the school teacher's teat."
    lucy "Eeeahh, aahh...♥"
    "Lewd sups filled the room, the sound of pale flesh being marred red by gluttonous suction."
    lucy "{size=-15}Ahh, aahh- aahh...{/size}"
    "All highlighted by the little soft notes of pleasure escaping Lucy's lips."
    lucy "{size=-10}Ah, mmhhh...{/size}"
    $ renpy.music.set_volume(0.1, 1, channel = "music")
    scene black with fade
    play ambient "sound effects/kissing3.wav"
    pause
    $ renpy.music.set_volume(1, 1, channel = "music")
    scene lucyex3_04_a with dissolve
    show lucyex3_04
    lucy "{size=+10}Ahh, wwahhh-♥{/size}"
    "Just a few moments more and that softness became {b}shrill.{/b}"
    "I bit down, {b}hard.{/b}"
    lucy "{size=+10}Euuah, o-oahh,{/size}"
    "{i}Vacuum tight{/i}, like my life depended on the bounty of the milfy woman's tits."
    lucy "{size=-5}Eeehh...{/size} {size=-10}Eeuaahh...{/size}"
    "Through the friction and spittle, I felt them chaff, but I didn't relent."
    lucy "{size=+10}Mmh, that feehhhhhsss...{/size}"
    "{i}How could I?{/i}"

    if w3LucyArtKiss == True:
        "Lucy was coming in and out, riding a tidal wave of pleasure."
    else:
        "The bitch was coming in and out, riding a tidal wave of pleasure."

    lucy "Ah, aahh.... yeaeeahhh...♥"
    "I sucked and sucked and sucked, until she was there."
    lucy "Ah, aah, {b}w-waaaa...!{/b}"
    "Well, {i}almost there,{/i} on the edge of gratification."
    lucy "C-calm down, t-they're n-nohht... going--"
    "--but I wouldn't let her reach it. {b}Not yet.{/i}"
    "Just as she had ceded the initiative over to me, so became my prerogative to--"
    stop ambient
    stop music
    scene w3_13595 with dissolve
    "Stop."
    play music "music/with-a-rose-in-your-teeth.ogg" fadein 5.0
    lucy "A-ahh...? Ahh...?"
    scene lucyex3_05_a with dissolve
    show lucyex3_05
    "We held each other's gaze for a moment, neither of us breaking the trance."
    pause
    mct "(She was beautiful...)"
    scene w3_13596 with dissolve
    lucy "H-hey..."
    "{i}Classical{/i} even."
    scene w3_13597 with dissolve
    "*Chwup*"
    lucy "O-ooohh... That's embarrassing..."
    scene w3_13598 with dissolve
    mc "I know."
    scene lucyex3_06_a with dissolve
    show lucyex3_06
    "Start and stop."
    lucy "Eh... ha-hahaaa..."
    "And start again."
    "*Cwhup, fwhhhp~!*"
    "Warming up the engines, lavishing the school teacher with my intentions."
    "I licked and licked and licked, the taste of perspiration locked behind the chemical flavor of deodorant."
    "{i}It made my head spin.{/i}"
    mct "(Ah, aah--)"
    pause
    $ renpy.music.set_volume(0.1, 1, channel = "music")
    scene black with fade
    play ambient "sound effects/kissing2.mp3"
    pause
    $ renpy.music.set_volume(1, 1, channel = "music")
    scene lucyex3_07_a with dissolve
    show lucyex3_07
    lucy "Fwwhhe..."
    "And lastly, {i}back where we started{/i}, except this time..."
    lucy "MMh, hmhmhh...!!!"
    "{i}She put a lot more of herself into it,{/i} kissing me back."
    lucy "Mmmh, *Shhlrrrp*, eaahh..."
    "Tongue coiling with mine."
    lucy " Ffh-hmmhh, *Shhlrprp...!*"
    "Nails digging into my shoulder, as she became weightless in my arms."
    "We kissed and kissed and kissed."
    pause
    stop ambient
    scene w3_13602 with dissolve
    "Free, we each caught our breath."
    scene w3_13603 with dissolve
    "............"
    "........."
    "......"
    scene w3_13604 with dissolve
    mc "...are you really this dirty of a woman?"
    scene w3_13605 with dissolve
    lucy "I've been asking myself that. I must be, or else I'm having a mental break..."
    scene w3_13604 with dissolve
    mc "Let's see about that. {b}Grab{/b} my cock."
    scene w3_13605 with dissolve
    lucy "Ah..."
    scene w3_13606 with dissolve
    lucy "Oh, ho.. s-sure..."
    scene w3_13607 with dissolve
    "For a second, I swam in the school teacher's chocolate brown eyes, enjoying the added tension of her lily white hands fumbling with my manhood straining to break free of my monkey suit."
    scene w3_13608 with dissolve
    "She didn't return my gaze, not directly, but the growing blush on her cheeks said enough."

    menu:
        "Ask what she thinks.":
            scene w3_13609 with dissolve
            mc "Well... what do you think?"
            scene w3_13610 with dissolve
            lucy "It's big..."
            scene w3_13609 with dissolve
            mc "That it?"
            scene w3_13611 with dissolve
            "........."
            "......"
            scene w3_13612 with dissolve
            lucy "...I just wonder if you know how to use it."
        "Be a little mean: ask about her husband, because it {b}REALLY{/b} turns you on.":
            $ w3ExLucyCheatingPlay = True
            scene w3_13609 with dissolve
            mc "Is it bigger than your husband's?"
            "She may have wanted to forget the \"Lucy\" parts of her life, but I didn't. {i}It was more thrilling if she remembered.{/i}"
            scene w3_13613 with dissolve
            lucy "Don't bring him into this..."
            scene w3_13609 with dissolve
            mc "I'll take that as a--"


    scene w3_13614 with dissolve
    mc "What are you...?"
    "Taking me by the collar, she pulled me forward like a dog..."
    scene w3_13615 with dissolve
    "...and put her back against the wall."
    scene w3_13616 with dissolve
    lucy "You've got the young part, but are you... {i}strong?{/i}"
    play sound "sound effects/zipper.wav"
    scene w3_13617 with dissolve
    "*Ziiiip*"
    mc "Ah..."
    scene w3_13618 with dissolve
    "She issued a challenge with hope in her eyes."

    if perk_strongman == True:
        mc "Don't you fucking doubt it."
    else:
        mc "We're about to find out..."

    scene black with fade
    "..."

    if perk_strongman == True:
        "I didn't want to disappoint."
    else:
        "It took a bit of strain, but I didn't want to disappoint."

    scene lucyex3_08_a with dissolve
    show lucyex3_08
    lucy "O-oh, f-fuck...!"
    "Held against the lockers, Lucy's face said it all."
    "{i}Okay, fine.{/i} {b}You're young AND strong.{/b}"
    mct "(Damn fucking straight I am.)"
    "--or so all the oxytocin swimming in my blood told me, as the rush of pinning a St. Ives educator aloft on my dick hit me in {b}spades.{/b}"

    if perk_strongman == True:
        mc "{i}Told{/i} you, I can move weight like {b}you{/b} no problem."
    else:
        mc "Ha, you don't weigh much!"

    lucy "Mmmh... oh, f-fuck...!"
    "{i}She liked that.{/i}"
    mc "So you've said..."

    "She couldn't look at me straight, but she {b}loved{/b} the feeling of being moved."
    lucy "Fuck, fuck, fuck...! O-okay...!"
    "The way she accepted the full brunt of my length was proof of that."
    "From this position, thrusting up at this angle, every push inside gouged the underside of her vulva."
    lucy "Ahh, hhmmm-♥"
    "She was in no way a virgin, and despite the thrill of being held, it wasn't an ideal position for either of our pleasures."
    scene lucyex3_09_a with dissolve
    show lucyex3_09
    lucy "Hnnhhh..."
    "I'd change that, though. {i}I'd make it hotter.{/i}"
    mc "Hey, look at me."
    lucy "Hhhh, fhh...!"
    "She didn't hear me, lost in the ebb and flow of getting dicked."
    lucy "Ewhh... wwahh...♥"
    "--and while watching her {b}endure{/b} had its appeal..."
    mc "Lucy! Look at me!"
    lucy "Mmhh...?"
    scene w3_13619 with dissolve
    lucy "..w-wha...?"
    "I wanted to remind her of something."
    scene w3_13620 with dissolve
    "That there was more than just the pounding she was taking down there."
    lucy "Mmmhh, mmhhh...!"
    scene w3_13621 with dissolve
    "That there was two of us of here, that she was more than a mere hole, and that I {b}demanded{/b} her attention."
    scene w3_13622 with dissolve

    if toughness >= 22:
        mc "Look at me when I fuck you, slut!"
    else:
        mc "Look at me when I fuck you!"
    lucy "--!"
    scene lucyex3_10_a with dissolve
    show lucyex3_10
    "{i}That's better.{/i}"
    lucy "Why... w-why..."
    "I pushed in deeper, no less impeded by the position, but spurred on by our eye contact."
    lucy "T-that was so hot...!"

    if w3ExLucyCheatingPlay == True:
        mc "Does your husband ever fuck you like this?!"
        "Caught up in the ugly thrill, I brought the dirty talk closer to home."
        lucy "I, I-- nuh--"
        "She {i}almost{/i} answered, but the decent parts of her recoiled from the truth."
        lucy "M-my... my husband has a bad back..."
        mc "Does he ever screw you like he owns you? Does he ever fuck you like a whore?"
        lucy "He w-would n-never, he's--"
        mc "A good man?!"
        lucy "A-aaaah...♥ Y-yes!"
        "I was gliding in and out of Lucy's cunt effortlessly by this point."
        mc "He's a good man and you're here bouncing on my dick! Where does he think you are?"
        mc "What do you tell him when you whore yourself out to the club?!"
        lucy "M-my, sister's-♥♥"
        mct "(Poor fucker...)"
        scene lucyex3_11_a with dissolve
        show lucyex3_11
        lucy "T-that's enough... stop bringing him up!"
        mc "Bullshit, you love cheating on your husband! You're wrapped around my dick!"
        "I should feel bad, but I've made my choice here. {i}As did she.{/i}"
        lucy "S-shut up!"
        "She had told me she wanted to forget her life outside of right now, but I wouldn't let her."
        mc "Admit it, you damn bitch!"
        lucy "O-oh, fuck...!"
        "{i}She liked that.{/i}"
        mc "You're a cheating whore! Don't run away from it!"
        lucy "A-ah...! F-fuck...♥"
        scene lucyex3_12_a with dissolve
        show lucyex3_12
        mc "What's his name?! What's your husband's name?!"
        lucy "ROhh... R-robert...!"
        mc "Robert Long, huh?"
        lucy "Ahhyye...♥"
        mc "You love him?!"
        lucy "Y-yhhes! Of c-courseehh!"
        mc "And how long have you been married?!"
        lucy "F-fifteen years!"
        mc "Fifteen years....? {b}Wow!{/b}"
        lucy "Eeahh, eeahhh...♥♥♥"
        mc "Well, next time you look Bob in the eyes..."
        lucy "Eahh, n-no...♥"
        mc "Your husband of FIFTEEN years...!"
        lucy "Oh, fuck, fuck, fuck...♥♥♥"
        mc "The father of your child...!"
        lucy "...♥♥♥♥♥♥"
        mc "You're going to remember something..."
        scene lucyex3_14_a with dissolve
        show lucyex3_14
        lucy "--guuashhhluuuaahhht!"
        "Putting my back into it, I flattened the busty school teacher out, driving myself to the hilt over and over."
        mc "Remember!"
        lucy "♥♥♥"
        mc "{size=+10}My!{/size}"
        lucy "♥♥♥♥♥♥"
        mc "{size=+15}FACE!{/size}"
        lucy "♥♥♥♥♥♥♥♥♥"
        "{i}She came.{/i}"
        mc "Remember!"
        mc "{size=+10}My!{/size}"
        lucy "♥♥♥♥♥♥"
        mc "{size=+15}VOICE!{/size}"
        lucy "♥♥♥♥♥♥♥♥♥"
        "{i}She came again.{/i}"
        mc "Remember!"
        mc "{size=+10}This!{/size}"
        lucy "♥♥♥♥♥♥"
        mc "{size=+15}DICK!{/size}"
        lucy "♥♥♥♥♥♥♥♥♥"
        "Over and over she came, as her organized mind, alongside fifteen years of marriage, was trampled on."
        lucy "Eueaahh.... R-robert...♥♥♥"
        "If Lucy was discovering something about herself while babbling her cuck husband's name, so was I."
        lucy "Roohnnn..."
        "An overwhelming sense of superiority under the spell of a kink I didn't know I possessed."
        lucy "Bho, bbbobb...!"
        mc "Remember!"
        lucy "♥♥♥"
        mc "{size=+10}My!{/size}"
        lucy "♥♥♥♥♥♥"
        mc "{size=+15}Load!{/size}"
        lucy "♥♥♥♥♥♥♥♥♥"
        mc "{size=+20}Inside!{/size}"
        lucy "♥♥♥♥♥♥♥♥♥♥♥♥"
        mc "{size=+25}You!{/size}"
        lucy "♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥"
        mc "{size=+30}BITCH!{/size}"
        stop music
        play sound "sound effects/spurt.wav"
        play ambient "sound effects/gulp2.wav"
        scene lucyex3_15_a with flash
        show lucyex3_15
        lucy "♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥"
        "........."
        "......"
    else:
        $ Lulu = True
        mc "How long has it been since you've been kissed like that?"
        lucy "Ah, haaa... uh..."
        mc "You don't have to answer..."
        lucy "Oh, fuck..."
        mc "I see it in your eyes..."
        "Oh, fuck, fuck, fuck...!"
        mc "You wouldn't be here otherwise, Luce."
        lucy "Ahh....♥"
        mc "...would you prefer I call you something else?"
        "It might've seemed a strange question, but she said herself she wanted to forget {i}Lucy Long{/i}, {b}teacher.{/b}"
        lucy "Ah, wha...?"
        mc "Who do you want to be right now, beautiful?"
        lucy "Nnyyeah...♥ It's stupid...♥"
        mc "No, it's not. You can be anyone right now, and no one has to know..."
        scene lucyex3_13_a with dissolve
        show lucyex3_13
        "She thought about it."
        "She thought about it perhaps {i}too{/i} earnestly for a woman riding a dick."
        lucy "Call me... {i}Lulu.{/i}"
        mc "Lulu...?"
        mc "Very cute..."
        mc "Alright, {b}Lulu...{/b}"
        "Maybe it was something an old boyfriend called her..."
        scene lucyex3_12_a with dissolve
        show lucyex3_12
        lucy "Ah, aahh...♥"
        "Maybe it was someone she wanted to be."
        mc "That's just between us then... I'll be the only one who calls you that."
        "Maybe it was just different."
        lucy "Y...y-eah...?"
        "She {b}liked{/b} the thought of that."
        lucy "W-what... what should I call you?"
        mct "(Me...?)"
        "I didn't want to be anyone else right now, but fair is fair..."
        mc "...well, okay. Does Lulu need a daddy?"
        lucy "Ah, that--"
        "She thought about it, again too earnestly for someone taking a cock."
        lucy "Heheh... a-alright... you can be {b}Daddy.{/b}"
        mc "...not going to roll your eyes?"
        lucy "W-why would I...? That...?"
        mc "It's what...?"
        lucy "{b}It's hot!{/b}"
        mc "Goddamn it Lulu..."
        lucy "Hehe... did I do something wrong, Daddy?"
        mc "{b}Fuck no!{/b} You're..."
        "Why the hell were there so many beautiful women around me? {i}And why couldn't I have them all?{/i}"
        mc "...{b}perfect.{/b}"
        lucy "Ah, hhmmm, yes...♥"
        mc "Daddy's {b}perfect{/b} slut..."
        lucy "Y-yes! Yes, Fuck me Dadd--!"
        scene lucyex3_14_a with dissolve
        show lucyex3_14
        lucy "eEeA{b}Aayyyhee!!!{/b}"
        "Spurred on, I flattened Lulu out, driving myself to the hilt over and over in a mad dash to supplant the name {i}Lucy{/i} from her memory."
        lucy "Ah, hheeehh...♥♥♥ D-daddy...!"
        mc "F-fuck...! {b}Lulu...!{/b}"
        "Sometimes I cursed my passions and inclinations, but in a moment like this, I was fortunate to be so simple."
        lucy "Gyeeah, heeee...♥♥♥♥♥♥"
        "Lucy was weighed down by many things: her family, her pride, regrets unseen..."
        lucy "Your dick... y-your dhiii--"
        "...but me? I was an easily corralled {b}beast{/b}."
        mc "Get f-fucked! {b}Get fucked!{/b}"
        "A {b}bull{/b}, seeing red from a five-letter word and induced into a rut from a bit of aggrandizing."
        lucy "♥♥♥"
        mc "C-come for Daddy!"
        lucy "♥♥♥♥♥♥♥♥♥"
        "I barked my command, but she was ahead of me, having already gone slack from the rough treatment."
        mc "You hear me, slut?! Come...!"
        lucy "♥♥♥"
        mc "{size=+10}For...!{/size}"
        lucy "♥♥♥♥♥♥"
        mc "{size=+15}Daddy...!{/size}"
        lucy "♥♥♥♥♥♥♥♥♥"
        mc "Come!"
        lucy "♥♥♥"
        mc "{size=+10}For!{/size}"
        lucy "♥♥♥♥♥♥"
        mc "{size=+15}Daddy!{/size}"
        lucy "♥♥♥♥♥♥♥♥♥"
        mc "{size=+20}{b}BITCH!{/b}{/size}"
        lucy "♥♥♥♥♥♥♥♥♥♥♥♥"
        "Again and again she came, cunt seizing and letting go of my cock like it was malfunctioning."
        mc "Come!"
        lucy "♥♥♥"
        mc "{size=+10}For!{/size}"
        lucy "♥♥♥♥♥♥"
        mc "{size=+15}Daddy!{/size}"
        lucy "♥♥♥♥♥♥♥♥♥"
        mc "{size=+20}{b}LULU!{/b}{/size}"
        lucy "♥♥♥♥♥♥♥♥♥♥♥♥"
        stop music
        play sound "sound effects/spurt.wav"
        play ambient "sound effects/gulp2.wav"
        scene lucyex3_15_a with dissolve
        show lucyex3_15
        "And then, {i}I joined her{/i}."
        lucy "♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥"
        "Dumping my inane vanity inside her."
        mc "Ah, f-fuck...!"
        "Filling Lulu to the brim with Daddy's seed."
        mc "Ah-- ahh--"

    stop ambient
    scene w3_13623 with dissolve
    mct "(Shit...!)"
    scene black with fade
    play sound "sound effects/thud-floor.mp3"
    "My arms went weak and--"
    scene lucyex3_16_a with dissolve
    show lucyex3_16
    "--and gravity did its thing."
    "........."
    "......"
    play music "music/select.ogg"
    "...There was a perverse thrill watching Lucy slide down to the floor, mind pureed into a finely fucked mush."
    lucy "Ahh... {size=-10}huh...{/size}"
    "Whereas not 20 seconds ago her face was contorted from depravity, now there was nothing..."
    "Just unfocused eyes and my handiwork oozing out of her well-fucked cunt."
    mc "Look at me."
    lucy "..."
    if Lulu == True:
        mc "{b}Look{/b} at me, Lulu."
    else:
        mc "{b}Look{/b} at me."

    scene w3_13624 with dissolve
    lucy "...?"
    "The woman looking into my eyes served as a reflection."
    "{i}It wasn't just me swept up in this place.{/i}"
    mc "Heh... that got a bit intense... let me help you up..."
    scene black with fade
    $ renpy.end_replay()

    if not persistent.w3LucyFuck:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3LucyFuck = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)


    "After that, we just returned to what little was left of our drinks."
    "Neither of us said much, and Lucy didn't look too happy."
    scene w3_13625 with fade
    "...and why would she?"
    "A bit of pleasure doesn't alter reality."
    scene w3_13626 with dissolve
    mc "You can't do this for the rest of your life."
    scene w3_13627 with dissolve
    lucy "I know..."
    scene w3_13625 with dissolve
    "........."
    scene w3_13628 with dissolve
    "......"
    scene w3_13629 with dissolve
    lucy "...but I'm overdue for a \"rebellious phase.\" I never got one when I was a teen. Too busy studying."
    scene w3_13630 with dissolve
    mc "...{b}huh.{/b}"
    scene w3_13631 with dissolve
    lucy "What?"
    scene w3_13632 with dissolve
    mc "You never think of women going through midlife crisis."
    scene w3_13631 with dissolve
    lucy "That's because we do it quietly. No shiny red car."
    scene w3_13632 with dissolve
    mc "Heh, yeah..."
    scene w3_13633 with dissolve
    "........."
    scene w3_13634 with dissolve
    "......"
    scene w3_13635 with dissolve
    mc "...by the way, Mr. Miller has requested your time, but I'm sure you could figure out an excuse to avoid him."
    scene w3_13636 with dissolve
    mc "I know you don't like him..."
    scene w3_13637 with dissolve
    "........."
    scene w3_13638 with dissolve
    "......"
    scene w3_13639 with dissolve
    lucy "...no, I'll go. I can't avoid him."
    scene w3_13638 with dissolve
    mc "Really?"
    scene w3_13639 with dissolve
    lucy "Yeah... I was sick all day thinking about that man, but... ha. This has helped me feel strangely okay with it right now."
    scene w3_13638 with dissolve
    mc "You don't have to do anything you don't want to do."
    scene w3_13640 with dissolve
    lucy "I know."
    scene black with fade
    "And that was that. I did my job AND got laid."
    "I didn't know how to feel about that."
    "........."
    "......"
    "..."
    jump w3ExStage3Donezo


label w3ExLucyNoFuck:
    scene w3_13647 with dissolve
    mc "I hate to do this to you, but I should tell you Isaak has been looking for you."
    lucy "I know. He's been telling me at school all the time..."
    mc "If you don't {i}hate{/i} working here, why are you even ducking him?"
    scene w3_13648 with dissolve
    lucy "Because he gives me the ick!"
    scene w3_13649 with dissolve
    mc "Well, that makes sense..."
    scene w3_13648 with dissolve
    lucy "A state senator is one thing, but him? Euch..."
    scene w3_13650 with dissolve
    mc "I get where you're coming from, but you've swallowed more bitter pills these past few weeks. Surely?"
    scene w3_13651 with dissolve
    lucy "It's stupid, I know. You're telling me to go fuck him, right?"
    scene w3_13652 with dissolve
    "Sudden, cold acceptance from the indecipherable woman."
    scene w3_13653 with dissolve
    mc "I'm relaying his request. I can't make you do anything."
    mc "Although, I think Harper wanted me to remind you of {b}why{/b} you're doing this. Sunk cost or whatever..."
    scene w3_13654 with dissolve
    lucy "She knows best..."
    scene w3_13655 with dissolve
    mc "No, she's not stupid, is she?"
    scene w3_13654 with dissolve
    lucy "Unlike me..."
    scene w3_13656 with dissolve
    "........."
    scene w3_13657 with dissolve
    "......"
    scene w3_13658 with dissolve
    lucy "...can I at least have a moment?"
    scene w3_13659 with dissolve
    mc "Yeah, sure of course."
    scene w3_13658 with dissolve
    lucy "Thanks for getting me the drink. Sadly, it was sweet that you remembered..."
    scene w3_13659 with dissolve
    mc "Are you good?"

    scene w3_13660 with dissolve
    lucy "...yeah. Just need to prepare myself."
    scene w3_13661 with dissolve
    mc "Take as long as you want..."
    scene black with fade
    "I didn't feel too good about having to do that, but ultimately the ball was in her court."
    "Her reasons were her own."
    "......"
    "..."
    jump w3ExHallwayStage3




screen w3ExVRStage3:

    imagemap:
        imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w3ExNavMenuStage3")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
        idle "gui/screens/imagemaps/w3ExVR3_idle.png"
        hover "gui/screens/imagemaps/w3ExVR3_hover.png"
        ground "gui/screens/imagemaps/w3ExVR3_ground.png"
        hotspot (0,580,250,250) action Jump("w3ExVRDrugs")
        hotspot (511,289,500,500) action Jump("w3ExVRWrestling")
        hotspot (981,157,500,500) action Jump("w3ExVRMilitaryMan")
        hotspot (1268,265,500,500) action Jump("w3ExVRackrub")


label w3ExVRStage3:
    show black
    $ renpy.music.play("music/sneaky-snitch.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w3ExVRStage3 with pixellate


label w3ExVRWrestling:

    if w3ExVRFirst == False:
        $ w3ExVRFirst = True
        $ w3ExVRFirst = True
        scene w3_13641 with dissolve
        "Looks like they're getting set up in here for something... {i}fun.{/i}"
    if w3ExVRWrestlingRepeat == False:
        scene w3_13642 with dissolve
        $ w3ExVRWrestlingRepeat = True
        "............"
        "........."
        "......"
        mct "(...uh, okay.)"
    else:
        $ randint = renpy.random.randint(1, 2)
        if randint == 1:
            scene w3_13646 with dissolve
            "My money is on Harper...?"
        else:
            scene w3_13642 with dissolve
            "To be honest... I {i}can{/i} see the appeal of this..."

    jump w3ExVRStage3

label w3ExVRackrub:
    if w3ExVRFirst == False:
        $ w3ExVRFirst = True

        scene w3_13641 with dissolve
        "Looks like they're getting set up in here for something... {i}fun.{/i}"

    scene w3_13643 with dissolve
    "He got changed quick..."

    jump w3ExVRStage3


label w3ExVRDrugs:

    if w3ExVRFirst == False:
        $ w3ExVRFirst = True
        scene w3_13641 with dissolve
        "Looks like they're getting set up in here for something... {i}fun.{/i}"
    $ randint = renpy.random.randint(1, 2)
    scene w3_13644 with dissolve
    if randint == 1:
        "Behold, an assortment of goodies."
    else:
        mct "Cocaine and Viagra... {i}not a great mixture...{/i}"

    jump w3ExVRStage3

label w3ExVRMilitaryMan:
    if w3ExVRFirst == False:
        $ w3ExVRFirst = True
        scene w3_13641 with dissolve
        "Looks like they're getting set up in here for something... {i}fun.{/i}"

    scene w3_13645 with dissolve
    if w3ExVRMMRepeat == False:
        $ w3ExVRMMRepeat = True
        "Seems all of Elias' new friends are here."
    else:
        mct "(He {i}certainly{/i} has an aura...)"

    jump w3ExVRStage3





label w3ExVIPFeliciaFinally:
    play music "music/Moonlight-Sonata.ogg"
    scene w3_13662 with pixellate
    "When I poked my head in, I found Felicia {i}almost{/i} by her lonesome."
    "Our resident gorilla was off to the side, looking tough for no one in particular."
    "On second thought, maybe it was best if I didn't come in... did I really want to look Felicia in the eyes right now?"

    menu:
        "Yes.":
            $ w3ExFeliciaTalk = True
            "Perhaps coming here was a mistake, but..."
            scene w3_13663 with dissolve
            mc "...yo!"
        "Back out before you get her attention.":
            $ w3ExEndSkip = True
            "Felicia's got a strong intuition. Why trust my poker face when I didn't have to...?"
            scene black with fade
            "So I simply gave Warren a nod, like I was checking in, and backed out."
            mct "(Let's just wait for Elias.)"
            "........."
            "......"
            "..."
            jump w3ExStage3Donezo

    fel "Oh...! {i}Finally!{/i} [mcf]!"
    "She lit up as soon as we locked eyes, casting a shadow on my refusal to turn back."
    scene w3_13664 with dissolve
    fel "I'm glad you're here, I have been boooooooored."
    scene w3_13665 with dissolve
    "...but that was why I am here. "
    scene w3_13666 with dissolve
    mc "I can't believe Warren is not enough company for you."
    scene w3_13667 with dissolve
    fel "He's... *ahem* Yeah, he's... he's a \"friendly\" guy."
    scene w3_13668 with dissolve
    war "I've been a gentleman. Will I see her smile at all over the remaining week?"
    fel "Uh huh..."
    scene w3_13669 with dissolve
    "I wanted to see her face {i}before{/i} her life got completely uprooted."
    scene w3_13670 with dissolve
    fel "I don't know where the other two are."
    scene w3_13671 with dissolve
    mc "Ah, uh... Rosalind and Veronica? I believe they're getting prepared for the night."
    scene w3_13670 with dissolve
    fel "...and why aren't I?"
    scene w3_13671 with dissolve
    mc "You... {i}are?{/i}"
    scene w3_13670 with dissolve
    fel "Was that a question?"
    scene w3_13672 with dissolve
    mc "Is something the matter? You don't look like your usual speckless self."
    scene w3_13673 with dissolve
    fel "I don't know... it's odd."
    scene w3_13674 with dissolve
    mc "What is?"
    scene w3_13673 with dissolve
    fel "I feel... {i}anxious?{/i}"
    scene w3_13674 with dissolve
    mc "Was {i}that{/i} a question?"
    scene w3_13675 with dissolve
    fel "Being dressed like {b}this{/b} and dumped alone in {i}here{/i}... it feels weird."
    scene w3_13676 with dissolve
    war "I told you, you're right where you need to be. The party's moving here later."
    scene w3_13677 with dissolve
    "Warren finally chimed in, making sure to dangle the narrative right in front of me."
    scene w3_13678 with dissolve
    war "You'll get all the attention a rich slut like you craves."
    scene w3_13679 with dissolve
    "Felicia glanced at me dubiously from the corner of her eyes, looking for confirmation of Warren's words."
    mct "(Ah, fuck...)"
    scene w3_13680 with dissolve
    mc "Yep, you're right where you need to be."
    scene w3_13681 with dissolve
    "I swung at Warren's lob. Technically, that was {i}not{/i} a lie."
    scene w3_13682 with dissolve
    fel "Heh... it's the sitting around, I guess. Calm before the storm."
    scene w3_13683 with dissolve
    "........."
    "......"
    scene w3_13684 with dissolve
    fel "...what's with the screen? Kathy throwing a movie night?"
    scene w3_13685 with dissolve
    mc "Your guess is as good as mine."
    fel "I have a feeling that's not true."
    "......"
    "...I should change topics."
    mc "Hey! If you were stuck on a desert island, what movie would you pick?"
    scene w3_13686 with dissolve
    fel "Small talk? {i}Really?{/i}"
    scene w3_13687 with dissolve
    mc "You were {b}just{/b} complaining about being bored."
    scene w3_13688 with dissolve
    "......"
    scene w3_13689 with dissolve
    fel "...I don't know. I don't like movies."
    scene w3_13690 with dissolve
    mc "{i}Youdon'tlikemovies?!{/i}"
    scene w3_13691 with dissolve
    fel "The only ones I ever see are the premieres Elias drags me to."
    scene w3_13690 with dissolve
    mc "That... that..."
    scene w3_13692 with dissolve
    war "Singing in the Rain."
    mc "What...?"
    scene w3_13693 with dissolve
    war "Desert island. Singing in the Rain, that's my pick."
    scene w3_13694 with dissolve
    "........."
    "......"
    scene w3_13695 with dissolve
    mc "With Gene Ke-- ...you--"
    scene w3_13696 with dissolve
    mc "There's a lot to unpack there, but even he watches movies!"
    scene w3_13697 with dissolve
    mc "I {i}suddenly{/i} want to show you so many things..."

    if feliciaFlag == True:
        scene w3_13698 with dissolve
        fel "*Sigh* Ah, you're cute... nerdy, but cute."
    else:
        scene w3_13699 with dissolve
        fel "Settle down, nerd. I'm sure you'll make some girl very bored someday."

    scene w3_13700 with dissolve
    "........."
    scene w3_13701 with dissolve
    "......"
    scene w3_13702 with dissolve
    fel "I guess you're checking up on me, Mr. Handler-Stud?"
    scene w3_13703 with dissolve
    mc "I hadn't seen you today."

    if w3FeliciaRomanceFocus == True or w3FeliciaLoseControl == True:
        scene w3_13704 with dissolve
        fel "Charmer..."
        scene w3_13705 with dissolve
        fel "Hey, uh... it's not an in-and-out thing, I hope?"
        scene w3_13706 with dissolve
        mc "Why, what's up?"
        scene w3_13705 with dissolve
        fel "I... would you mind hanging around longer?"
    else:
        scene w3_13705 with dissolve
        fel "If that's the case... would you... would you mind hanging around longer?"

    scene w3_13706 with dissolve
    mc "Uh..."
    scene w3_13707 with dissolve
    "For once, Felicia looked guileless."
    "She had no idea what was in store, but you didn't need a keen intuition for even a woman like her to feel trepidation over this week's theme."
    scene w3_13708 with dissolve
    mc "Yeah, I've got time."
    "It was my choice to come in here. I wouldn't say no."
    scene w3_13709 with dissolve
    mc "We're going over there. That okay with the boss, big guy?"
    scene w3_13710 with dissolve
    war "Knock yourself out. She just can't leave the room."
    scene w3_13711 with dissolve
    mc "Noted..."
    scene black with fade
    "{b}Funny.{/b} {i}Looks like this was where I was going to be until I had to retrieve her husband.{/i}"
    "..."
    scene w3_13712 with fade
    "Once we sat down, neither of us knew what to say. Whatever anxiety I had, incidentally dispelled from Felicia by coming in, was brought back with Warren's painting of her as a prisoner."
    "And naturally, thanks to the silence, I thought about Elias and the Sword of Damocles getting closer and closer to chopping off her pretty head."
    scene w3_13713 with dissolve
    mc "What are you going to do if you don't win?"
    scene w3_13714 with dissolve
    "That wouldn't help the bad feeling she had, but I had to ask."
    scene w3_13715 with dissolve
    mc "I mean, are you going to spend the rest of your life playing wife?"

    if w1ExGame2WinnerFel == False and w2ExWinnerFelicia == False:
        scene w3_13716 with dissolve
        "After all, she was already down two weeks..."

    scene w3_13717 with dissolve
    fel "I'll win."
    scene w3_13718 with dissolve
    mc "...but if you don't? Your husband might be the city's next mayor."
    scene w3_13716 with dissolve
    "{i}That{/i} thought gave me a naive comfort. Maybe Elias couldn't easily throw her away amid political scrutiny. "
    scene w3_13717 with dissolve
    fel "If I don't, I'll have to recalculate..."
    scene w3_13716 with dissolve
    "......"
    scene w3_13719 with dissolve
    mc "...what's your prenup like?"
    scene w3_13720 with dissolve
    fel "...what?"
    scene w3_13721 with dissolve
    mc "Enlighten me on rich people mating rituals, Felicia."
    scene w3_13722 with dissolve
    fel "There's barely any room to kick or scream."
    scene w3_13721 with dissolve
    mc "Figures..."
    scene w3_13723 with dissolve
    "Hell... even if she won, she was sunk, wasn't she? I saw it firsthand that the club members are ostensibly on Elias' side."
    scene w3_13724 with dissolve
    fel "What's with the pointed questions?"
    scene w3_13725 with dissolve
    mc "I... {i}worry{/i} about you."
    scene w3_13726 with dissolve
    fel "What?! {i}I'll be fine.{/i}"
    scene w3_13725 with dissolve
    mc "That..."
    scene w3_13723 with dissolve
    "{i}I wished to believe.{/i}"
    scene w3_13727 with dissolve
    mc "Of course you will be."
    scene w3_13728 with dissolve
    fel "You're being weird and it's not helping, [mcf]."
    mc "Sorry..."

    if w3FeliciaRomanceFocus == True or w3FeliciaLoseControl == True:
        scene w3_13729 with dissolve
        mc "...does this help?"
        fel "{i}Does what help--{/i}"
        scene w3_13730 with dissolve
        mc "Me, holding your hand."
        scene w3_13731 with dissolve
        fel "No, because I'm not a child."
        scene w3_13732 with dissolve
        mc "Oh, my b--"
        fel "I didn't say let go!"
        scene w3_13733 with dissolve
        "........."
        "......"
        scene w3_13734 with dissolve
        fel "...what happened to your hand?"
        scene w3_13735 with dissolve
        mc "Punched a wall."
        scene w3_13736 with dissolve
        fel "Really? {i}You?{/i}"
        scene w3_13737 with dissolve
        fel "Did it involve a woman?"
        scene w3_13738 with dissolve
        mc "Uh... technically. {i}Yes.{/i}"
        scene w3_13739 with dissolve
        fel "That...!"
        scene w3_13740 with dissolve
        fel "Pah! How passionate!"
        scene w3_13741 with dissolve
        "It was slight, but I happily labeled Felicia's expression as a pout."
        scene w3_13742 with dissolve
        mc "Not like that. Someone... {i}deeply{/i} disrespected my mother."
        scene w3_13743 with dissolve
        fel "Then why a wall? Why not punch the person?"
        scene w3_13744 with dissolve
        mc "Because the person in question is Ian's mother."
        scene w3_13745 with dissolve
        fel "{b}Huh.{/b} Sounds messy."
        scene w3_13746 with dissolve
        mc "You've got no idea."
        scene w3_13745 with dissolve
        fel "You know, you can put a surprising amount of quarters in a luxury handbag. Want me to beat the shit out of her?"
        scene w3_13746 with dissolve
        mc "Appreciate the offer, but you've got other things to worry about this week."
        scene w3_13739 with dissolve
        fel "Don't say I didn't offer. I've got your back."
        scene w3_13747 with dissolve
        mc "Heh, thanks, Felicia..."
        scene w3_13748 with dissolve
        "........."
        "......"
        scene fel_w3vip_01_a with dissolve
        show fel_w3vip_01
        fel "...ah, that's nice."
        mc "Yes, you are..."
        fel "Did you forget where we are, stud?"
        mc "Yes. It's very easy too. You have that effect."
        fel "You don't have to lay it on so thick. I was just bored..."
        mc "Have to? No. {b}Want{/b} to. I'm very selfish."
        fel "Mmmh..."
        mc "There are two dozen people in the building tonight, and look at us. We found a bit of quiet."
        fel "Damn it..."
        mc "What...?"
        fel "I'm too old to swoon."
        mc "No, you're not..."
        scene w3_13749 with dissolve
        mc "*Cwhup*"
        fel "A-ah...♥ I..."
        scene fel_w3vip_02_a with dissolve
        show fel_w3vip_02
        fel "Now you've done it. I wish we were somewhere {i}else{/i} right now."
        mc "Like where?"
        fel "Someplace where it's just you and me."
        mc "You've gotta keep your head in the game, Felicia."
        fel "Not helping, [mcf]..."
        "........."
        "......"
        scene w3_13750 with dissolve
        "Frankly, I wished the same as her. The look on her face later..."
        mct "(Fuck...)"
        scene w3_13751 with dissolve
        "The apprehension nipping at my heels intensified. After tonight, would she even want to see me?"
        "{i}I liked seeing Felicia.{/i} I could admit that."
        "........."
        "......"
        scene w3_13752 with dissolve
        mct "(...{b}fuck.{/b})"
        scene w3_13753 with dissolve
        "Telling her wouldn't make a difference. {i}I needed to believe that{/i}."
        scene w3_13754 with dissolve
        fel "You know... I've never been comfortable with the idea of myself growing old."
        scene w3_13755 with dissolve
        mc "Where's that coming from?"
        scene w3_13756 with dissolve
        fel "Your line of questioning. What will I do if I lose? How do I see myself?"
        scene w3_13757 with dissolve
        fel "I haven't even had a five-year plan that was more than just {i}get rich.{/i}"
        fel "Ten years...? Twenty...? {b}That scares me.{/b} I mean, what am I going to do when I get wrinkles?"
        scene w3_13758 with dissolve
        "........."
        "......"
        scene w3_13759 with dissolve
        fel "...that's why people find others to grow old with, huh?"
        scene w3_13760 with dissolve
        mc "I think it ends up that way because of some other stuff, but... {i}yeah?{/i}"
        scene w3_13761 with dissolve
        fel "Growing old with someone..."
        scene w3_13762 with dissolve
        "........."
        "......"
        scene w3_13763 with dissolve
        fel "What a delusional fantasy."
        scene w3_13764 with dissolve
        mc "Felicia..."
        "That look was like a knife in my heart."
        mc "I don't think it's any more absurd than a hick from a small town marrying into American royalty. You just have to want it."
        scene w3_13765 with dissolve
        fel "{i}Sounds boring...{/i}"
        scene w3_13766 with dissolve
        "............"
        "........."
        scene w3_13767 with dissolve
        "......"




        scene w3_14437 with dissolve
        fel "What's with that look, [mcf]?"
        scene w3_13767 with dissolve

        menu:
            "Risk it. Give her a heads up about what's coming in so few words.(w3ExFelForewarnedSortOf = True)"(chg=["felicia_passion_up"]):
                $ w3ExFelForewarnedSortOf = True
                $ Felicia_Confidence += 3
                mc "I..."
                scene w3_13768 with dissolve
                fel "We've been over this. Don't... not out of the blue..."
                scene w3_13769 with dissolve
                "{i}I had to be careful.{/i}"
                scene w3_13770 with dissolve
                mc "Tonight's gonna be bad, Felicia. {b}Real bad.{/b}"
                scene w3_13771 with dissolve
                fel "What are you--"
                scene w3_13770 with dissolve
                mc "Don't say anything. {b}Just listen.{/b}"

                scene w3_14438 with dissolve
                "I made sure Warren wasn't watching."
                scene w3_14439 with dissolve
                mc "I can't tell you what it is, Mrs. Pulman would know if I did, just..."

                scene w3_14440 with dissolve
                mc "No matter what that rickety bitch has in store, you'll come out the other side, alright? I believe in you."
                scene w3_14441 with dissolve
                fel "Okay, I'm more than just a littled worried now, [mcf]--"

                scene w3_14442 with dissolve
                fel "--!"

                scene w3_14443 with dissolve
                war "*Scoff* Ha..."

                scene w3_14444 with dissolve
                war "Fucking kid..."

                scene w3_14445 with dissolve
                mc "You're bigger than the box you put yourself in."
                scene w3_14446 with dissolve
                "Felicia stared at me uncertain, but she read my expression carefully."

                scene w3_14447 with dissolve
                mc "Hell, you're {b}bursting{/b} out of it -- and that's why you're here, because you need a change."
                "I was hinting at something I shouldn't and she took that seriously."
                scene w3_14448 with dissolve
                mc "Just try to keep that word in mind. {b}Change.{/b}"

                mc "Win or lose, consider throwing out that goddamn box."

                scene w3_14449 with dissolve
                fel "I... *scoff* you going to support me?"
                scene w3_14447 with dissolve
                mc "You know damn well you can support yourself. Now, push me off you, This looks too--"

                scene w3_14450 with dissolve
                fel "Save it for the exhibition!"
                "{i}She got the idea.{/i}"

                scene w3_14451 with dissolve
                fel "Seriously! What? You want to fuck here?"

                scene w3_14452 with dissolve
                fel "First that Gorilla puts his hands on me, now--"
                scene black with fade
                "Before I excused myself in embarassment, having been rebuked, I could see the gears inside Felicia's head turning, as she tried to figure."
                "There was no hedging her bets anymore, what she desired would be lobbed in her lap and I could only hope she could see it that way once my half-assed warning made sense."
                "........."
                "......"
                "..."
                jump w3ExStage3Donezo
            "Don't be stupid. Just leave.":


                "{b}No. {/b}Nonononono, bad idea.{/b}"
                scene w3_13768 with dissolve
                fel "We've been over this. Don't... not out of the blue..."
                scene w3_13769 with dissolve
                mc "*Chwup~*"
                scene w3_13770 with dissolve
                mc "It would {i}never{/i} be boring waking up next to you."
                scene w3_13771 with dissolve
                fel "...fuck off."
                scene w3_13772 with dissolve
                mc "I've got to go."
                fel "Why?"
                scene w3_13773 with dissolve
                mc "I need to go take care of business."
                scene w3_13774 with dissolve
                fel "Thanks for sitting with me..."
                scene w3_13775 with dissolve
                "Her eyes said don't go."
                scene w3_13776 with dissolve
                mc "*Chwup* No..."
                "I {b}had to go{/b}."
                scene w3_13773 with dissolve
                mc "No problem."
                scene w3_13775 with dissolve
                "If I didn't, I'd blab."
                "I'd blab {b}everything.{/b}"
                scene black with fade
                "{i}Coming here was a mistake.{/i}"
                "........."
                "......"
                "..."
                jump w3ExStage3Donezo
    else:

        scene w3_13777 with dissolve
        mc "I like your outfit."
        "If she wanted a distraction, I could do that. That was my job."
        scene w3_13778 with dissolve
        fel "Of course you do. I look like a confused cross-fetish stripper."
        scene w3_13779 with dissolve
        mc "Too tacky for Felicia Ford?"
        scene w3_13780 with dissolve
        fel "No, it's just the underside of my tits are chaffing!"
        scene w3_13781 with dissolve
        mc "Ha! Yeah...!"
        fel "Seriously! I mean, where's the fucking baby powder!"
        mc "The old woman is a sadist, remember?"
        scene w3_13782 with dissolve
        "........."
        "......"
        scene w3_13783 with dissolve
        fel "...anyway, I've got no idea about all that stuff you were asking me about. It's kinda hard picturing myself in ten years."
        scene w3_13784 with dissolve
        fel "Wife for the rest of my life? I'll be replaced by then. {b}God,{/b} I can't imagine being sixty. I might have to walk into the sea."
        scene w3_13785 with dissolve

        menu:
            "Crack a joke.":
                mc "You'll have to join a monastery. That's the only answer."
                scene w3_13786 with dissolve
                fel "{i}Obviously.{/i}"
                scene w3_13785 with dissolve
                mc "That or ask Mrs. Pulman for the phone number of her crossroad demon."
                scene w3_13784 with dissolve
                fel "Oh, that's a good idea. What am I even using my soul for?"
            "Flatter her."(chg=["felicia_passion_up"]):

                $ Felicia_Confidence += 1
                mc "You'll be sixty years old and still gorgeous, Felicia."
                scene w3_13786 with dissolve
                fel "Yeah, but I won't be {i}as{/i} gorgeous."
                scene w3_13785 with dissolve
                mc "Nah, you'll be the same dynamo, just more wise and more scary."
                scene w3_13783 with dissolve
                fel "Yeah, right..."

        scene w3_13787 with dissolve
        "So we chatted, with me doing my duty of keeping Felicia's mind preoccupied."
        "There was a point where I wanted to blab to her about Elias, but I didn't. {i}I couldn't.{/i}"
        mct "(Not like it would help...)"
        scene w3_13788 with dissolve
        "Thankfully, Warren eventually saved me from my better self."
        scene w3_13789 with dissolve
        war "The fuck? What are you two making goo-goo eyes for?"
        scene w3_13790 with dissolve
        mc "You need something, Warren?"
        scene w3_13789 with dissolve
        war "Yeah, this slut needs to get in place."
        scene w3_13791 with dissolve
        mc "......"
        scene w3_13792 with dissolve
        fel "...it's okay. Duty calls."
        scene w3_13793 with dissolve
        mc "Yeah, you're right. I've got to go see... *ahem* {i}someone.{/i}"
        scene w3_13794 with dissolve
        fel "Thanks for keeping me from being bored, stud."
        scene w3_13795 with dissolve
        mc "No problem, Felicia. You know I love your company."
        scene black with fade
        "......"
        "...and now, {i}let's go schmooze her husband again.{/i}"
        jump w3ExStage3Donezo


label w3ExStage3Donezo:
    play music "music/future-rennaisance.ogg"
    scene w3_13796 with circlewipe
    chuck "I'm glad we had this talk..."
    scene w3_13797 with dissolve
    elias "Yeah, uh... it was {b}wow.{/b}"
    scene w3_13798 with dissolve
    chuck "Right on time, lad."
    scene w3_13799 with dissolve
    mc "You guys finished?"
    scene w3_13800 with dissolve
    chuck "We are!"
    scene w3_13801 with dissolve
    play sound "sound effects/slap2.wav"
    scene w3_13802 with vpunch
    elias "--!"
    scene w3_13803 with dissolve
    chuck "I've learned everything I needed to know about Eli here."
    scene w3_13804 with dissolve
    mc "Fast friends, huh?"
    scene w3_13805 with dissolve
    "......"
    scene w3_13806 with dissolve
    elias "...{b}yep.{/b} We have a... {i}perfect{/i} understanding of each other."
    scene w3_13807 with dissolve
    chuck "You're looking at a remarkable man, [mcf]."
    mc "Uh... don't I know it."
    scene w3_13808 with dissolve
    chuck "You two have a lot in common, actually."
    scene w3_13809 with dissolve
    mc "Do... {i}do we?{/i}"
    scene w3_13810 with dissolve
    chuck "I think you'd find that true. You both lost your father before their time."
    scene w3_13811 with dissolve
    elias "R-really?"
    scene w3_13812 with dissolve
    chuck "If you need... {b}anything{/b}..."
    scene w3_13813 with dissolve
    chuck "Please, don't hesitate to come to me. Nothing is insurmountable."
    chuck "Welcome to the club."
    scene w3_13814 with dissolve
    "........."
    "......"
    scene w3_13815 with dissolve
    chuck "Anyway! This old man has taken up too much of your time! Tonight is about fun!"
    chuck "I'm told some of your new friends are waiting for you..."
    scene w3_13816 with dissolve
    elias "Right... {i}fun.{/i}"
    scene w3_13817 with dissolve
    chuck "Take good care of him, lad."
    scene w3_13818 with dissolve
    "I nodded."
    scene w3_13817 with dissolve
    chuck "Good."
    scene w3_13819 with dissolve
    "........."
    scene w3_13820 with dissolve
    "......"
    scene w3_13821 with dissolve
    mc "Uh, you feeling sick? You look pale, Mr. Ford."
    elias "I'm..."
    scene w3_13822 with dissolve
    "........."
    "......"
    scene w3_13823 with dissolve
    elias "...*ahem* I'm fine, Bukowski. Let's find that fun. I could use it."
    scene black with fade
    "........."
    "......"
    jump w3ExOrgyStart

label w3ExOrgyStart:
    scene w3_13824 with circlewipe
    "...I had never been downwind of so many duplicitous smiles."
    "The moment we entered the velvet room, Elias' would-be cadre was on us like a pack of lions, teeth bared in a grotesque imitation of hospitality and friendship."
    jim "Finally! Elias!"
    scene w3_13825 with dissolve
    dal "It's good to see you again so soon, Mr. Ford."
    scene w3_13826 with dissolve
    elias "Ah... ha... {i}Hi, Dalia{/i}."
    "I had to give Dalia credit. The sensuous way she commanded attention, even opposed to the movie star in Elias' arm, was almost supernatural."
    scene w3_13827 with dissolve
    elias "...Abel! You too?"
    scene w3_13828 with dissolve
    "...but even with Dalia's wiles, to the PR man's credit, he already had full stock of the room."
    scene w3_13829 with dissolve
    "{i}I had yet to even notice them.{/i}"
    scene w3_13828 with dissolve
    elias "...oho, and what do we have here? What's going on?"
    scene w3_13830 with dissolve
    shel "The breaking of bread."
    scene w3_13831 with dissolve
    elias "Ha! What else?"
    scene w3_13832 with dissolve
    dal "Should I find you a girl, Mr. [mcl]? My apologies, but I didn't account for you."
    scene w3_13833 with dissolve
    mc "...what's that?"
    scene w3_13832 with dissolve
    dal "You're the odd man out. Four house girls, four patrons..."
    scene w3_13834 with dissolve
    mct "(Ah...)"
    mct "(I'm guessing she's not counting Abel, Sophia, or Allison amongst that total...)"
    scene w3_13833 with dissolve
    mc "I'll make do, Dal. Focus on making our VIP happy."
    scene w3_13835 with dissolve
    dal "It needs not be said."
    scene w3_13836 with dissolve

    menu:
        "Send her off with an ass slap.":
            scene w3_13837 with dissolve
            play sound "sound effects/slap2.wav"
            scene w3_13838 with hpunch
            dal "Oh!"
            "She was right. {i}There were better ways to send her off.{/i}"
            "I was perhaps too comfortable with this."
        "Refrain.":
            scene w3_13840 with dissolve
            pass

    scene w3_13839 with dissolve
    shel "For Christ's sake, someone get this man a drink! And turn some music on!"
    dal "Right away!"
    scene black with fade
    "Time to play fly on the wall--"
    play music "music/running-it-down.ogg"
    scene w3_13841 with w20
    elias "Stop playing wallflower, Bukowski! Get the hell over here!"
    mc "I'm not--"
    elias "I'm not letting you get rid of me that easily!"
    scene w3_13842 with dissolve
    jim "Yeah, get over there, kid!"
    scene black with fade
    mc "Ah, ha... you guys know how to--"
    scene w3_13843 with cmet
    mct "(...make a guy feel included.)"
    mc "I told you I'd make do..."
    shel "Now where was I?"
    scene w3_13844 with dissolve
    jim "Toasting to new friendships, blah blah blah. Let's drink!"
    "{i}Neither age nor status took the frat out of the boy.{/i}"
    scene w3_13845 with dissolve
    jiji "Drink!"
    whores "Drink, drink, drink!"
    mc "Should I just..."
    scene w3_13846 with dissolve
    mc "{b}Mmmh...?!{/b}"
    dal "Get in there!"
    shel "To friendship!"
    jimjiji "To friendship!"
    mcelias "Thmhmmfreeehship!"
    scene black with fade

    if hanaGF == True:
        "{i}Sorry, Hana.{/i} I--"
    else:
        "Okay, at first I thought this was stupid, but maybe all alcohol should be served like--"

    scene ex3vr_01_a with w20
    show ex3vr_01
    jiji "She served her up like dinner!"
    elias "{i}Her?{/i} Really?"
    jiji "Should've seen her! I want to hire her!"
    shel "Sandbaging bitch! I've seen her fight before, and never once did she use jujitsu!"
    jiji "Always happy to take your cash, Senator."
    scene w3_13847 with dissolve
    dal "You don't seem very comfortable, Mr. [mcl]. Is there anything I can do to help you relax?"
    scene w3_13848 with dissolve
    mc "I'm fine, Dalia... uh, how long did it take you to get used to rubbing elbows with..."
    scene w3_13849 with dissolve
    "I let my wandering eyes finish the sentence."
    scene w3_13850 with dissolve
    dal "I've done this work, in {b}some{/b} form, for oh... fifteen years now? {i}I'm still not comfortable.{/i}"
    scene w3_13848 with dissolve
    mc "I find that hard to believe when you're so good at commanding a room."
    scene w3_13851 with dissolve
    "Although, then again, that would explain why I always get the sense she's on edge..."
    scene w3_13852 with dissolve
    mc "Fifteen years, though? How have you lasted?"
    scene w3_13847 with dissolve
    dal "By not getting comfortable."
    scene w3_13853 with dissolve
    cass "Mr. Ford..."
    elias "Hmmm?"
    scene w3_13854 with dissolve
    cass "Courtesy of Dr. Van Doren and Miss Lundgren."
    scene w3_13855 with dissolve
    elias "Well, then... It'd be rude of me not to."
    scene w3_13856 with dissolve
    jim "Just him?"
    scene w3_13857 with dissolve
    sophia "There's enough to go around."
    "........."
    "......"
    scene black with fade
    "...there was no way in hell I'd take anything that woman--"
    scene w3_13858 with w20
    jim "Come on, don't be a pussy! We're all having fun here."
    scene w3_13859 with dissolve
    "Dalia looked at me curiously, but I shook my head {b}no.{/b}"
    "{i}She didn't seem surprised.{/b}"
    scene w3_13860 with dissolve
    elias "Ho, h-holy shit! What is this?!"
    sophia "My personal take on methylenedioxymethamphetamine."
    scene w3_13861 with dissolve
    scene w3_13862 with dissolve
    scene w3_13863 with dissolve
    scene w3_13861 with dissolve
    "This time, I shook my head {b}adamantly{/b} no."
    scene w3_13864 with dissolve
    dal "Understood, Mr. [mcl]. Leave it to me, I'll help you play along."
    scene w3_13865 with dissolve
    mc "What do you...?"
    scene w3_13866 with dissolve
    dal "Do you trust me?"
    scene w3_13867 with dissolve
    mc "Right now? Strangely enough, yeah--"
    scene ex3vr_02_a with dissolve
    show ex3vr_02
    mc "Mmm--"
    "Dalia pried my mouth open with a kiss, but that was that."
    "No ecstasy found its way into my mouth."
    "Instead she used my tongue to push the party drug down {b}her{/b} throat."
    "Damn it, Dalia. {b}Beautiful{/b} woman. I owed her."
    scene w3_13868 with dissolve
    elias "Hey, Bukowski!"
    mc "Uh, y-yeah...? A-aha..."
    scene w3_13869 with dissolve
    elias "It just occurred to me that I have no idea what you do. One would presume there's more to you than the club."
    scene w3_13870 with dissolve
    mc "Right... uh--"
    elias "Tell me something. I'd like to know you better."
    scene w3_13871 with dissolve
    mc "I'm studying to be a doctor."
    elias "A doctor?!"
    scene w3_13872 with dissolve
    mc "Well, hopefully... I still have to take the MCATS."
    scene w3_13873 with dissolve
    elias "There's no hope, Bukowski! You'll nail it! You're beautiful!"
    scene w3_13874 with dissolve
    mc "I think the ecstasy is kicking in, sir."
    scene w3_13875 with dissolve
    elias "Haha, no it hasn't! It normally takes like twenty minutes!"
    "That may be so, but--"
    scene ex3vr_03_a with dissolve
    show ex3vr_03
    "Given the unconscious and needy way Dalia was grinding her ass into me, I'd say the drug had worked its way to Dalia's nervous system and serotonin was now flooding her brain."
    "Whatever the chemist's \"personal take\" was, it was fast acting."
    dal "Bukowski...? As in the poet?"
    mc "Long story, but yep, that's me. You read a lot, Dal?"
    dal "Are you surprised?"

    menu:
        "A little.":
            mc "Honestly? A little, he's not exactly Emerson."
        "Not at all.":
            mc "Not at all. You're as smart as you are beautiful!"
            dal "I've heard every line, Mr. [mcl]."
            mc "Not from me, though..."

    dal "The job comes with a surprising amount of downtime, plus it gives me and Jacob something to talk about."
    mc "The Carnation {b}Book{/b}club, eh?"
    scene w3_13876 with dissolve
    dal "Pfft, y-yeah, ah... {i}fuck{/i}, you're {b}hard{/b}. Sorry, I didn't even realize I was-"
    mc "It's alright. You {b}are{/b} helping me look like I belong."
    scene w3_13877 with dissolve
    dal "I think you already look the--"
    scene w3_13878 with dissolve
    jim "Bah! Don't we have some malt somewhere?"
    scene w3_13879 with dissolve
    shel "Why would you want to drink--"
    scene w3_13878 with dissolve
    jim "It's affordable AND nostalgic!"
    scene w3_13880 with dissolve
    shel "Jesus Christ, you filthy fucking--"
    scene w3_13881 with dissolve
    mc "You should find our police chief his cheap liquor."
    dal "Are you sure?"
    scene w3_13882 with dissolve
    mc "Go."
    scene black with fade

    if hanaGF == True:
        "If this got back to Hana, I could probably explain it as part of my duties, but--"
    else:
        "I missed her as soon as she got up, but--"

    scene w3_13883 with circlewipe
    "Watching others' sobriety fall away when you're clean as a whistle was uncanny, but that was doubly so when the men in question were the city's luminaries."
    "It was {i}interesting{/i}, to say the least."
    jim "Oh man, oh man, oh man...! I can still picture the white of that fucker's eyes."
    scene w3_13884 with dissolve
    "For some, it just intensified their worst impulses."
    elias "That's uh... great. You should see a therapist."
    scene w3_13885 with dissolve
    jim "You ever shoot somebody, soldier boy?"
    scene w3_13886 with dissolve
    jiji "It's nothing to be proud of, fatso!"
    scene w3_13887 with dissolve
    "For others, it surprisingly stimulated a rare scrap of empathy."
    scene w3_13886 with dissolve
    jiji "It's nothing to joke about either!"
    scene w3_13888 with dissolve
    abel "Yet, you've made a fortune off of it."
    scene w3_13889 with dissolve
    jiji "It was like carrion downwind of a rotting corpse. I'm not responsible for the politics that started that war, but..."
    scene w3_13888 with dissolve
    abel "...but what, Mr. Jameson?"
    scene w3_13890 with dissolve
    jiji "Ha, it does leave a bitter taste! Bahahaha!"
    scene w3_13891 with dissolve
    mc "What's so funny?"
    scene w3_13892 with dissolve
    jiji "Ah, just... they got what they paid for, didn't they? Someone to underbid on a contract, pour gasoline on the flames, embarrass the country globally, and--"
    scene w3_13893 with dissolve
    abel "...{b}distract.{/b}"
    scene w3_13894 with dissolve
    jiji "{b}That{/b} is worth a paycheck, yes."
    scene w3_13895 with dissolve
    jiji "Distract, distract, distract!"
    scene w3_13896 with dissolve
    mc "...you alright?"
    jiji "God, I want to do something, go for a run or..."
    scene w3_13897 with dissolve
    harp "Ah, ahh...♥"
    jiji "...{b}break{/b} something! Fuck something!"
    scene w3_13898 with dissolve
    elias "Bukowski!"
    scene w3_13899 with dissolve
    elias "God, my heart is pounding! Like I'm going to die!"
    scene w3_13900 with dissolve
    mc "You'll be alright, it's just the..."
    scene w3_13901 with dissolve
    sophia "Tachycardia. It's to be expected."
    scene w3_13902 with dissolve
    elias "I've taken Molly, it's never been like this!"
    mc "Would you like to lie--"
    scene w3_13903 with dissolve
    elias "Fuck no! I want... I want to..."
    "First, his eyes flittered to Allison, like he wanted to fuck."
    scene w3_13904 with dissolve
    "Then he shifted his attention to me, {b}like he wanted to fuck.{/b}"
    mc "Uh..."
    scene w3_13905 with dissolve
    elias "You have no idea, Bukowski. I'm so jealous of you!"
    scene w3_13906 with dissolve
    mc "Me? What do I have to be jealous? You're rich, have a beautiful wife, you're going to be mayor and--"
    scene w3_13907 with dissolve
    elias "Doctor! That's tangible! TANGIBLE!"
    scene w3_13906 with dissolve
    mc "I--"
    scene w3_13907 with dissolve
    elias "Don't care, shut up, let's get you a drink! I just tasted malt liquor for the first time in my life, have you ever had that stuff?!"
    scene w3_13906 with dissolve
    mc "I {i}am{/i} a college student..."
    scene w3_13907 with dissolve
    elias "If I tasted it, I won't let you be the only one to get away from Jim's disgusting tastes. Plus, I've got some stuff I want to ask you about!"
    scene w3_13906 with dissolve
    mc "What about--"
    scene w3_13908 with circlewipe
    elias "It's not a bad idea, is it? Eh? {b}Eeeeeh?{/b}"
    "For everything else, it amplified in the other patrons, in Elias' case, the drug made him many things."
    scene w3_13909 with dissolve
    mc "No, no... charity-- I, I... I think that kind of foundation is a good idea, dude."
    "For one, more generous."
    scene w3_13910 with dissolve
    elias "Yeah, {i}yeah?{/i} You {b}think?!{/b} Everyone's gonna call it self-serving."
    mc "Who cares what people say? Just, maybe, uh... dial down the pompous spin? Stop calling it stewardship."
    elias "I--"
    scene w3_13911 with w20
    elias "--of every heart in gray! The army line you'll ever find--"
    "It also made him more {b}gregarious.{/b}"
    scene w3_13912 with dissolve
    mc "A t-terror in the fray?"
    "He gave me no time to remember the lyrics!"
    scene w3_13913 with dissolve
    elias "And when the team is fighting--"
    mc "Wow, you can actually sing, huh?"
    jiji "Rah! Rah! Rah! Boom!"
    scene w3_13914 with dissolve
    elias "Military school choir, Bukowski! Such a butcher's arrangement of words!"
    scene w3_13915 with dissolve
    "Soon enough, I found myself actually having fun."
    scene w3_13916 with dissolve
    mc "Hey, Dal."
    scene w3_13917 with dissolve
    elias "Seems she missed you! Want to swap with me?"
    mc "What do you...?"
    elias "Dance with Allison! Don't you want to? I mean, she's a future A-lister! Pretty fuckin' cool, yeah?"

    if Allison_Interest > Elias_Friendship:
        scene w3_13918 with dissolve
        "Before I could even answer, the Carnation Queen took the initiative."
        allison "You heard Elias, dance with me! Or don't you want to?"
        mc "Of course--"
    else:
        scene w3_13919 with dissolve
        allison "What? Are you getting bored of me?"
        elias "No, Darling. It's just... we're all friends here."
        scene w3_13920 with dissolve
        allison "Mmmh, of course, let's dance--"

    scene ex3vr_04_a with circlewipe
    show ex3vr_04
    "And not only did I start to get into it, but I began to forget whose company I was keeping."
    "It didn't matter."
    "Not with the cheap alcohol oxidizing in my blood."
    "Not with my grubby fingers holding tight on a movie star's shapely hips."
    "Hell, I even began to forget that Elias wasn't really my friend and that he was soon in for a hazing of a lifetime."

    if Allison_Interest > Elias_Friendship:
        scene ex3vr_05_a with dissolve
        show ex3vr_05
        mc "I'll be damned, you're getting into it!"
        allison "So what if I am?!"
        allison "I hate to admit it, but you {i}are{/i} the only one here not old enough to be my dad or sugar daddy."
        mc "Good enough reason for me!"
        scene w3_13921 with dissolve
        elias "I could use a top up."
        scene w3_13922 with dissolve
        mc "What does that mean?"
        scene w3_13921 with dissolve
        elias "Have you ever tried coke?"
        scene w3_13922 with dissolve
        mc "It's not really my--"
    else:

        scene w3_13923 with fade
        elias "Hey, beautiful. Miss me?"
        allison "Of course I did."
        scene w3_13924 with dissolve
        elias "Shit, I think I could use a top up. You down, Bukowski?"
        scene w3_13925 with dissolve
        mc "Down for what?"
        scene w3_13924 with dissolve
        elias "Have you ever tried coke?"
        scene w3_13925 with dissolve
        mc "It's not really my--"

    play sound "sound effects/snort3.wav"
    scene w3_13926 with w20
    elias "*Snoooooorrttyhhttt--*"
    scene w3_13927 with dissolve
    "........."
    "......"
    scene w3_13928 with dissolve
    elias "Mmmh, {i}fuck!{/b}"
    scene w3_13929 with dissolve
    "Elias looked at me with a big dumb smile on his face, dilated pupils turned upward like a puppy dog."
    "The encroaching smirk on his lips read... {i}well?{/i}"
    scene w3_13930 with dissolve
    mc "Thanks, but--"
    scene w3_13931 with dissolve
    jim "Pussy! You a cop or sumtin'?!"
    scene w3_13932 with dissolve
    mc "It's more I'm not a fan of hypertension, psychosis, hyperthermia, or--"
    scene w3_13933 with dissolve
    play sound "sound effects/slap4.wav"
    scene w3_13934 with vpunch
    jim "P-U-S-S-Y!"
    mct "(You, fucking--!)"
    scene w3_13935 with dissolve
    elias "What are you? In high school?"
    elias "If he doesn't want to do it, he doesn't have to do it! You balding, sweaty fuck!"
    scene w3_13936 with dissolve
    jim "Eh? I touch a nerve? I'm just breaking balls!"
    scene w3_13937 with dissolve

    menu:
        "Ah, fucking do it!(w3ExDidDrugs = True) \n Sophia Rapport -2":
            $ w3ExDidDrugs = True
            $ sophiaRapport -= 2
            scene w3_13938 with dissolve
            "I didn't think too much about it."
            "I did it, just to say I had."
            scene w3_13939 with dissolve
            mc "--!"
            "Just to say I had. I mean, how many people get to snort drugs off a movie star's ass?"
            "Just to shut that annoying pig up."
            play sound "sound effects/snort2.wav"
            scene w3_13940 with dissolve
            "{i}Just to play ball.{/i} Just to do my job."
            "It was just a short high, anyway."
            "The excuses piled up in my head as the fine powder coated my septum."
            play sound "sound effects/whoosh.wav"
            scene w3_13941 with dissolve
            mc "A-aah...!"
            "My nose went numb."
            mc "Jesus Christ, that's--"
            scene w3_13942 with dissolve
            "{b}Head rush.{/b}"
            mc "*Ahem* W-woah."
            mct "(Fuck me, shit...)"
            scene w3_13943 with dissolve
            mc "And that's all I'm doing!"
            play sound "sound effects/thud-floor.mp3"
            scene w3_13944 with vpunch
            jim "W-wha..? Did you just {i}shove{/i} me, you little--"
            scene w3_13945 with dissolve
            mc "Just breaking balls, comb over."
            "{i}Why the hell did I do that?{/i}"
            elias "Pfft, comb over!"
            "It just seemed like a good idea."
            scene w3_13944 with dissolve
            jim "{b}Shut up!{/b} That's a toddler's insult!"
            scene w3_13953 with dissolve
            mc "Fuck, I missed this feeling."
            scene w3_13954 with dissolve
            elias "Haha, what? You've never done this before!"
            scene w3_13955 with dissolve
            mc "I didn't mean the cocaine! I meant putting a bully on his ass!"
            scene w3_13956 with dissolve
            jim "Fuck you, I'm being nice!"
            scene w3_13955 with dissolve
            mc "Shit, I feel like going for a walk."
            scene w3_13957 with dissolve
            dal "I've got a better idea."
            mc "Shit is it hot in here? Or is it just you?"
            scene w3_13958 with dissolve
            dal "How about a show, boys?"
            scene w3_13959 with dissolve
            elias "A show? Oh, I like that look in your eyes!"
            scene w3_13958 with dissolve
            dal "Can I borrow Allison?"
            scene w3_13960 with dissolve
            allison "Yes, please! Can I get up?"
            scene w3_13961 with dissolve
            elias "Sounds like you're needed, Sweetie."
            scene w3_13960 with dissolve
            mct "(Fuck...)"
            "I was already getting hard."
            "Intellectually, I understood why people did drugs, but feeling it first hand..."
            "Some things {i}are{/i} better experienced."
        "Firmly decline.":

            scene w3_13946 with dissolve
            mc "No, thanks."
            "There was no value in saying I had tried an addictive substance, even if it was just once."
            "Even if it was off the pert mound of a movie star's ass."
            scene w3_13947 with dissolve
            jim "Move aside then! More for me."
            scene w3_13948 with dissolve
            mc "Hey, thanks for sticking up for me."
            play sound "sound effects/snort1.wav"
            scene w3_13949 with dissolve
            elias "No problem. He reminds me of a bully I hated."
            mc "That's surprising. It's hard to imagine you being bullied."
            scene w3_13950 with dissolve
            elias "A long time ago, hardly worth mentioning."
            scene w3_13951 with dissolve
            mc "Yet you mentioned it."
            scene w3_13950 with dissolve
            elias "We're getting to know each other, aren't we?"
            scene w3_13951 with dissolve
            mc "Yeah..."
            scene w3_13952 with dissolve
            "{i}We are.{/i}"
            scene w3_13962 with dissolve
            elias "Hey, Dalia! What's happening, beautiful?!"
            dal "Oh, I was just thinking it's time for a show. A little something to soften your landing."
            dal "May I borrow Allison?"
            scene w3_13963 with dissolve
            allison "Yes, please! Can I get up?"
            scene w3_13964 with dissolve
            dal "Just so we're clear, I can't promise to return her spotless."
            allison "Uh--"
            scene w3_13965 with dissolve
            elias "Yes, you may! Sounds like you're needed, Sweetie!"
            "It seems the fun was just getting started."

    stop music fadeout 3.0
    scene black with fade
    "The night could only go in one direction, couldn't it?"
    play music "music/organic.ogg"
    scene w3_13966 with curtains
    "The rules were simple: three-minute, alternating rounds."
    scene w3_13967 with dissolve
    allison "O-okay... I wasn't expecting to..."
    scene w3_13968 with dissolve
    "{i}Harper vs. Allison.{/i}"
    scene w3_13969 with dissolve
    allison "{i}Compete{/i} again..."
    scene w3_13968 with dissolve
    "The first woman to dissolve into a certifiable fuck puddle was the loser."
    scene w3_13970 with dissolve
    shel "This wasn't exactly what I had in mind when I suggested--"
    scene w3_13971 with dissolve
    jim "No one fucking wants to watch yet another wrestling match, you freak."
    scene w3_13972 with dissolve
    "{i}Harper started.{/i}"
    scene w3_13973 with pixellate
    harp "Ha! I'm not gonna need that!"
    scene w3_13974 with dissolve
    allison "Alright, then you go first. Experience before beauty."
    scene w3_13975 with dissolve
    harp "{i}Oh...{/i} {b}THIS{/b} is going to be fun."
    scene ex3vr_06_a with pixellate
    show ex3vr_06
    "...and now Harper was taking a sensual approach."
    harp "We've got to make it look good..."
    allison "Ha, haa... I {i}know.{/i}"
    harp "Not that it's hard..."
    harp "Sometimes I {b}love{/b} my job..."
    allison "O-oh, stop...♥"
    "As the game got going, Allison's typically raspy voice shifted to a vocal fry."
    allison "You, uh... you actually think that will work? You should've accepted the toy..."
    harp "I don't need no fuckin' toy."
    allison "Nggh, women don't do it for me..."
    harp "You don't need to like women to like what {i}{b}I{/b}{/i} am doing to you."
    allison "B-bullshit..."
    harp "Mmmh, I'm {i}very{/i} confident when it comes to girlies like you, Princess. You'll see..."
    scene ex3vr_07_a with dissolve
    show ex3vr_07
    harp "Ah...♥"
    "Harper's attack was still slow and measured, but it covered the bases."
    harp "*Chwup* Admit it..."
    allison "N-nothing to admit..."
    "She started at the top, doting Allison's perfect porcelain skin with kisses-"
    harp "For an actress *chwup*... you're a terribble *chwup*... {b}LIAR.{/b}"
    "--breathing and heavy into the blonde's ears as she enacted her other ministrations."
    allison "Mmmmh...♥"
    "Down below, the working girl used her knee like a third hand, parting the movie star's legs and teasing her breasts in tandem."
    harp "At least your body is honest..."
    "A three-pronged attack, applying the {i}perfect{/i} amount of tease to get the passive blonde going."
    harp "Did you just shudder...?"
    "Harper was in no rush, paying no mind to the three-minute time limit before Allison got her turn."
    harp "Do that again for me, Princess..."
    "She was confident, and why wouldn't she be? Allison had beaten other amateurs, but {b}SHE{/b} was a pro."
    allison "Ahh, ahh--"
    scene w3_13976 with dissolve
    elias "You know, Bukowski... taking a step back. It's kinda weird."
    scene w3_13977 with dissolve
    mc "What is..?"
    scene w3_13976 with dissolve
    elias "Bunch of ugly bastards sitting in a drum circle and watching two girls go at it."
    scene w3_13977 with dissolve
    mc "You..."
    "{i}Shit.{/i} It wasn't even weird to me anymore."
    scene w3_13978 with dissolve
    mc "You get used to it. That feeling goes away."
    scene w3_13979 with dissolve
    cass "That's cause that's just the appetizer."
    cass "You're forgetting one important detail, Mr. Ford."
    scene w3_13980 with dissolve
    elias "What's that, sweetheart?"
    scene w3_13981 with dissolve
    cass "There's more than just those two."
    scene w3_13982 with dissolve
    "To make her point, the house girl submissively bolted between Senator Shelby's legs."
    scene w3_13983 with dissolve
    elias "Oh, I wasn't complaining."
    scene ex3vr_08_a with dissolve
    show ex3vr_08
    "To further her point, she began slavishly sucking the old man's dick, but our in-flight entertainment paid it no heed."
    "Harper was focused on what she was doing, having given up Allison's back in favor of a frontal assault."
    "She worked her target with a skilled hand, a woman after my own heart, plumbing the movie star's sex and sucking hardily on a pale teat."
    allison "{size=-5}Hmmpf...{/size}"
    "...but, like the champion she was, Allison wasn't sitting on her hands."
    mct "(Smooth...)"
    "No, the movie star was already priming Harper for her own turn, tweaking and teasing subtly what she could get her fingers on."
    "It was against the rules, but no one seemed to notice or mind, least of all Harper, whose enthusiastic sucking said all that needed to be said."
    "{i}She was very clearly keen on the idea of working over a silver-screen beauty.{/i}"
    mct "(Not that I could blame her...)"

    if w3ExDidDrugs == True:
        "It was all too easy imagining myself switching places with the brunette, fingering her holes and sucking on her tits."
    else:
        "My mind raced with violent images of taking Harper's place, of violently finger blasting the blonde into a quivering mess, lips locked--"
        mct "(Fuck, is it hot in here?!)"

    allison "You s-should've went with the t-toy..."
    "The blonde's voice broke with a squeak, stammering both unnecessarily and unconvincingly."
    allison "Bah, p-pah... I'm feeling n-nothing...♥"
    "{b}Too{/b} unnecessary and unconvincingly, in the sense she would have been better served saying nothing at all."
    "Instead, she used just the right amount of inflection to stimulate a predator response from her attacker. {i}Egging her on.{i}"
    allison "{size=-10}Ammh, mmhh...{/size}"
    "{b}Yes.{/b} The way she muffled her cries, bit her tongue, held back...."
    allison "{size=+5}A-aaah...♥{/size}"
    "What she strategically let slip out."
    allison "F-feeling, n-noth..."
    "All fuel for the fire burning in Harper."
    scene ex3vr_09_a with dissolve
    show ex3vr_09
    shel "Fuck, what good are your muscles?! What good are {b}you?{/b}"
    "No, not just Harper, but the reticent display was causing the perverts waiting in the wing to bare their teeth as well."
    cass "Ghh, hhhkk--"
    "It seemed the senator wasn't paying attention anymore, which was understandable given the violent way he was fucking Cassandra's throat."
    shel "Dumb whore! You must like me pissing down your throat! That has to be it!"
    cass "HHkk, hhhkk-"
    shel "Why else would you continually disappoint me?"
    jim "Ha! Joe is still mad about losing."
    cass "Ghhhk, hnnnk, {b}geuuuhhhk...!{/b}"
    elias "Jesus Christ, I guess that's what running unopposed for 18 years will do to a man."
    cass "Ghh, gghhkhk, {b}HGGGGGKKKGHK!{/b}"

    if w3ExDidDrugs == True:
        "The sight was repulsive, but it {b}mademesofuckinghard!{/b} I couldn't help but imagine living as I pleased."
        "Hanging with movie stars, doing drugs off their asses, and fucking bitches like they're nothing..."
    else:
        "I was caught between repulsion and enticement; one couldn't help but imagine living as one pleased."
        "Hanging with movie stars and fucking all day, every day..."

    elias "Oh, fuck... Allison, {b}baby...{/b}, you're so hot!"
    scene w3_13984 with dissolve
    "When my attention returned to my charge, Dalia was getting Elias primmed for fun of his own."
    scene w3_13985 with dissolve
    "Next to join the fun was Elias, with Dalia working him like the pro she was."
    jim "Seems Elias has a type, eh?"
    scene w3_13986 with dissolve
    elias "What's that supposed to mean?"
    scene w3_13987 with dissolve
    jim "If I remember correctly, your wife is blonde."
    scene w3_13988 with dissolve
    elias "Uh, I suppose, yeah..."
    scene w3_13989 with dissolve
    shel "Really? I've never met your wife."
    elias "Bukowski here has. He actually interviewed the both of us, pretending to be a journalist. Can you believe it?"
    scene w3_13990 with dissolve
    jim "Haha, no! I can't even imagine it!"
    "Jim relished the irony of this moment, the skirting of the line, {i}the giving me a goddamn heart attack{/i} by teasing the truth. To the extent that--"
    scene w3_13991 with dissolve
    jim "Ah, fuck, come here...!"
    scene w3_13992 with dissolve
    "{i}I'm pretty sure it got all the crooked fucks going.{/i}"
    serena "No need to be rough-- y-you only have to ask!"
    scene w3_13993 with dissolve
    jim "Eheheh... sorry! I guess I could use some calming energy!"
    scene black with fade
    "Even before the three minutes were up, Harper yielded the floor."
    scene ex3vr_10_a with fade
    show ex3vr_10
    harp "F-fuck, alright... your turn now, no need to rush though... I'll make this last a few rounds."
    "...but Allison didn't go on the offensive; instead, she let Harper guide her to her knees."
    allison "Ah, aaahhaa...♥"
    "The look on Allison's face was pure sex, mind addled while bathing in the heat radiating from Harper's cunt."
    jiji "Oh! She's confident."
    jim "A-aah... or the tattooed slut doesn't care who wins and is just horny."
    shel "Take this seriously! Don't you lose me another ten large!"
    harp "You've got nothing to worry about, Mr. Shelby. I'm A LOT more experienced in this area."
    "...was she intentionally underestimating Allison to make this more exciting? Or did she genuinely believe in her prowess?"
    harp "I bet more than not she just lies there whenever a producer wants a go at her."
    "I was actually excited to find out and see last year's exhibition winner in action."
    harp "Lick it, slut."
    allison "E, aahh... y-you want me to eat you out?"
    harp "What did I say?"
    allison "Mmhhh..."
    harp "Time's ticking."
    scene w3_13994 with dissolve
    allison "I... *Chwup*"
    scene w3_13995 with dissolve
    harp "That's it, baby..."
    scene w3_13996 with dissolve
    allison "*Chwup* In your--"
    stop music
    play sound "sound effects/ironside.wav"
    scene w3_13997 with dissolve
    allison "In your wildest dreams bitch."
    scene w3_13998 with dissolve:
        align (0.5,0.5)
        linear 160 zoom 2.5
        pause 4
    pause
    "The shift was {i}chilling.{/i} All the scrambled brain huffing, the bedroom eyes... it vanished."
    "--and in its place was a look of sheer defiance, in direct challenge."
    scene w3_13999 with dissolve
    harp "Uh, what--"
    scene w3_14000 with dissolve
    "{i}She sprang into action.{/i}"
    play music "music/addict.ogg"
    scene w3_14001 with dissolve
    "The look on Harper's face was palatable."
    scene w3_14002 with dissolve
    allison "No way in hell am I going to put MY lips on some random whore's pussy."
    scene w3_14003 with dissolve
    "{i}This{/i} was going to be good."
    scene w3_14004 with dissolve
    harp "Ahh, ha-haaa... come on, that's not very sporting."
    play sound "sound effects/vib-start.wav"
    allison "Tough shit, bitch!"
    scene w3_14005 with dissolve
    harp "Ah, heeeaaahhh--"
    "........."
    scene w3_14004 with dissolve
    "......"
    scene w3_14006 with dissolve
    dal "A, aaaahhh...!"
    scene ex3vr_11_a with dissolve
    show ex3vr_11
    "Everything was running its due course."
    dal "Mmmh, look at me, Mr. Ford."
    "While I wasn't looking, Dalia had climbed atop our special guest and was now riding him for all his worth."
    elias "I, I... eheh... don't be offended, dear, there's a lot to pay attention to!"
    harp "Eeeuuaahghhhjh-?!!"
    elias "Holy! Wow, Ally is kinda scary, huh, Bukowski?!"
    mc "Uh huh..."
    "And it wasn't just him..."
    scene ex3vr_12_a with dissolve
    show ex3vr_12
    "The city police chief's stubby cock was proudly engorged between Serena's fingers as she kissed the disgusting pig like she loved him."
    jim "*Chwwuip, cwqwhhuhpp-!*"
    mct "(How the hell do they do this job without puking?)"
    "A man like Elias I can actually understand, but {b}fuck.{/b}"
    harp "Eeuuauaah--?! Eeaaaah..! S-slow down, you're going to ruin the f--f-funnnn...!"
    scene ex3vr_13_a with dissolve
    show ex3vr_13
    "Before I knew it, save for the old soldier and myself, the scene had quickly devolved into an orgy."
    "The house girls were good, dragging everyone into the fray as if it was as natural as breathing."
    "...and for these men, it was, wasn't it? This was their life. {i}This was my life.{/i} Sort of."
    "That very thought made the hair on my neck stand up."
    "Decadent. Depraved. Unfettered pleasure."
    "Suddenly I felt... {i}unattended.{/i} Like I didn't know what to do with my hands."
    scene w3_14007 with dissolve
    sophia "It's surreal being the odd man out, is it not?"
    scene w3_14008 with dissolve
    mc "I suppose."
    scene w3_14007 with dissolve
    sophia "They're animals. It's like we're in a zoo."
    scene w3_14008 with dissolve
    mc "You had a hand in it."
    scene w3_14009 with dissolve
    sophia "Even without a push, they would throw aside their dignity just the same. Just as they do every week, month, and year, both in and outside this building."
    scene w3_14008 with dissolve
    mc "Everyone pisses and shits."
    scene w3_14010 with dissolve

    if sophiaRapport >= 3:
        sophia "That is sophistry, [mcf]. And I think you know it."
        scene ex3vr_14_a with dissolve
        show ex3vr_14
        elias "A-aah, f-fuck...! Fuck, fuck, fuck...!"
        sophia "Nobody is perfect, yes..."
        elias "Your pussy is on another level, Dal!"
        sophia "And as you say... everyone shits, but..."
    else:
        sophia "That is disingenuous sophistry, Mr. [mcl]. And you know it."
        scene ex3vr_14_a with dissolve
        show ex3vr_14
        elias "A-aah, f-fuck...! Fuck, fuck, fuck...!"
        sophia "Nobody is perfect, yes..."
        elias "Your pussy is on another level, Dal!"
        sophia "And as you say, everyone {i}defecates{/i}, but..."

    play ambient "sound effects/vib-ongoing.wav"
    scene ex3vr_15_a with wipeleft
    show ex3vr_15
    allison "I thought you were a pro!"
    sophia "It doesn't mean we have to swim in it."
    "Her words mirrored my own thoughts and feelings, but coming from her, {i}I wanted to disagree.{/i}"

    if sophiaRapport >= 3:
        mc "Seems like you bring out the contrarian in me, Sophia."
        "As Harper was being dismantled before our very eyes, Sophia put a hand on my shoulder."
        allison "...but all it takes is a little toy, huh?!"
        sophia "Miss Smith fast-tracked her career by beating a bunch of other sad women."
        "It was a paradoxically light, soothing touch."
    else:

        mc "True enough. You bring out the contrarian in me, {i}Miss Lundgren.{/i}"
        "As Harper was being dismantled before our very eyes, Sophia continued."
        allison "...but all it takes is a little toy, huh?!"
        sophia "Miss Smith fast-tracked her career by beating a bunch of other sad women."

    harp "Eeuaahh, aaahhh-♥"
    sophia "And, as talented as she no doubt is in this area of... {i}expertise{/i}, she won because it was more advantageous to have a famous actress in the club's debt than a debt-ridden husk."
    allison "I know I'm hot, but--"
    sophia "It's a success earned not through ability or hard work, but through the willingness to denigrate oneself. A career playing pretend built on dishonesty."
    sophia "It'd be hilarious if I didn't sympathize at some level."
    harp "Euuaahh, eeeghhhhhh--♥"
    "Harper shook and convulsed violently as an orgasm suddenly racked her body."
    sophia "It's difficult to ascertain what is and isn't real in all this nonsense."
    mc "Maybe, it's like acting. Harper's mixing lies with truth."
    sophia "*Sigh* That {i}is{/i} the state of the world."

    $ renpy.end_replay()

    if not persistent.w3OrgyStart:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3OrgyStart = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)

    stop ambient
    if sophiaRapport >= 3:
        scene w3_14011 with wiperight
        sophia "You're painfully alone right now, [mcf]."
        scene w3_14012 with dissolve
        sophia "That's why I came over here. I saw it on your face."
        scene w3_14013 with dissolve
        mc "...you were just decrying all this as nonsense."
        scene w3_14019 with dissolve
        "She simply shrugged, as if to say {i}so what.{/i}"
        scene w3_14014 with dissolve
        sophia "It would be accurate to say I'm experiencing a feeling of... {i}cognitive dissonance{/i} right now."
        scene w3_14015 with dissolve
        "Contrary to her words, the eyes staring back at me weren't cold, and certainly neither was her touch..."
        scene w3_14016 with dissolve
        mc "Ah, that does feel nice..."
        scene w3_14017 with dissolve
        "I mean, she {i}was{/i} scritchin' my head like a puppy dog."
        scene w3_14018 with dissolve
        sophia "Sorry..."
        mc "...about what?"
        scene w3_14020 with dissolve
        sophia "I..."
        sophia "I was left alone to my own devices and wanted to... {i}talk{/i}."
        sophia "I'll let you watch the \"show\" in peace."
        scene w3_14021 with dissolve
        "........."
        "....."
        scene w3_14022 with dissolve
        "....{b}fuck.{/b}"
        menu:
            "Go after her.":
                scene w3_14023 with dissolve
                "Sometimes people do stupid things, like walk into the mouth of a volcano."
                scene black with fade
                "This was one of those times."
                jump w3ExSophiaOrgy
            "Let her leave.":

                scene w3_14024 with dissolve
                mct "(Fuck that.)"
                "I don't want that mess."
                scene black with fade
                "Sophia left, likely following after wherever Abel went."
                jump w3ExOrgyContinue
    else:
        scene w3_14008 with dissolve
        mc "You're chatty today. Where's your boss?"
        scene w3_14007 with dissolve
        sophia "He got bored, and I suppose so did I."
        scene w3_14025 with dissolve
        sophia "Thank you for the momentary distraction, Mr. [mcl]."
        mc "Where are you going?"
        scene w3_14026 with dissolve
        sophia "I've got a chess match."
        scene w3_14027 with dissolve
        mc "Ah... alright..."
        scene w3_14028 with dissolve
        "Her cold demeanor cracked, revealing a look of trepidation."
        scene w3_14029 with dissolve
        sophia "Goodbye."
        scene w3_14030 with dissolve
        mc "Yeah..."
        scene black with fade
        "{i}Have fun with that.{/i}"
        jump w3ExOrgyContinue


label w3ExSophiaOrgy:
    if _in_replay:
        play music "music/addict.ogg"

    scene w3_14031 with dissolve
    sophia "...yes?"
    mc "Don't feign innocence, you psychotic bitch. Where do you think you're going?"
    scene w3_14032 with dissolve
    sophia "I--"
    "--couldn't even blame the perfume for what I did next."
    sophia "I've... I have to go play a game of chess."
    scene w3_14033 with dissolve
    mc "You don't {b}HAVE{/b} to do anything. I thought you wanted to talk?"
    sophia "I was just--"
    scene ex3vr_16_a with dissolve
    show ex3vr_16
    mc "*Chwup*~ ...what? You were just *Chwup~* what?"
    sophia "A-ah, aah...?"
    "The moment my lips met her cheek, she seemed confused."
    sophia "H-having a bit of fun before--"
    "Maybe that was owed to the surprising gesture or just the intimate nature of the act."
    mc "...{b}don't{/b} play chess. How 'bout that...?"
    sophia "Ah... Dr. Kohler will be... {i}unhappy.{/i}"
    mc "Is that a problem? Isn't that a fun outcome?"
    sophia "I--"
    scene ex3vr_17_a with dissolve
    show ex3vr_17
    sophia "Mmmhh..."
    "It was easy to forget that Sophia was not only a genius, but maybe even a once-in-a-generation scientific mind."
    "Yet here I was, tongue down that luminary's throat, with a great big helping of her plump ass within my grip."
    "At the end of the day, Sophia Lundgren was a woman, and I could handle that."
    sophia "Eehh, maaa..."
    "No matter how smart she was, I could tease and coax her into feeling something."
    sophia "Nhaaa, ne--♥"
    "The clumsy way she returned my kiss was cute."
    "{i}She wasn't very good at it{/i}, but that somehow made her even more enticing."
    "Like she had spent too much time with her head in the book and never learned how to properly french kiss."
    "{i}Like I could show her something.{/i}"
    scene ex3vr_18_a with dissolve
    show ex3vr_18
    sophia "W-wh..."
    mc "{b}*Chgwwup, fwwhhup--!*{/b}"
    "She let me do as I please, ensnaring her tongue as a rush of lightheadedness overtook my senses."
    mc "*Swehhuuup, scheeewwwh--!*"
    "Sex was all around us, a dozen bodies careening toward oblivion, but my head became an island of its own."
    "The world was but a pair of lips, a slippery tongue, viscous strands of spittle."
    "Its history was written in the way Sophia's eye fluttered and its future foretold by the forceful way I pressed my cock into her groin."
    "Sophia had looked down on the Carnation Club, but its spell had both of us enchanted."
    "Just another pair of animals, looking to satisfy an urge."
    pause
    "........."
    scene w3_14034 with dissolve
    "......"
    scene w3_14035 with dissolve
    sophia "...ah, haaa, *gulp*, okay."
    scene w3_14036 with dissolve
    sophia "After some consideration, I believe this to be a plausible excuse."
    scene w3_14037 with dissolve
    mc "I thought you might..."
    scene w3_14038 with dissolve
    harp "Eeuauahh-! Wwwaahhh--"
    scene w3_14039 with dissolve
    harp "Aahhh, eeehhhh...♥♥♥♥♥♥♥"
    "A shrill cry momentarily drew my attention."
    scene w3_14040 with dissolve
    harp "Fu, ffhhhu... h-hhaa..."
    "There was still plenty of time left and Harper was still standing."
    play sound "sound effects/zipper.wav"
    sophia "A-aahh--"
    scene ex3vr_19_a with dissolve
    show ex3vr_19
    sophia "O-okay..."
    "{i}The fever continued unabated.{/i}"
    "Freeing myself, my cock naturally found its place in between the scientist's thighs."
    "Sophia immediately understood, not saying a word, but gripping me firmly and squeezing her thighs together for my selfish pleasure."
    mc "'atta girl, {b}Sophie.{/b}"
    sophia "{b}Hnnggn...!{/b}"
    "With that accord struck, I slowly began to saw, using the genius blonde like a toy."
    "I hugged her close, flat against my chest, arduously pushing my way through stiffening muscle."
    sophia "{size=-5}Ah, haa, mmhhh...{/size}"
    "She moaned quietly, in a low whisper. Not for the benefit of the room, but for me alone."
    "For {b}my{/b} gratification."
    sophia "Hnnn, I... I have a clear answer to my question..."
    mc "...?"
    scene w3_14041 with pixellate
    sophia "My stomach or my thighs?"
    scene ex3vr_20_a with pixellate
    show ex3vr_20
    mc "H-heh..."
    pause
    mc "A, ah...!"
    "Sophia followed along with the sway of my body, playing the perfect outlet for my lust."
    "She squeezed her thighs tightest at the apex of my thrust, using her whole undercarriage to embrace my full length."
    mc "Jesus, that feeeeeeeells--"
    "Thigh, pussy lips, and cheeks - working in tandem, clinging to me in a bid to get me to pop. Timing it in just a way that, no matter how slow or fast I went, she eased up half a second too late."
    mc "{b}F-fuck!{/b}"
    "The feeling of my bare dick caught between Sophia's burning pussy and the cool touch of her leather panties sent a chill through my body."
    "Wait... {i}was I sure she wasn't...?"
    "Lust and I were well acquainted these past few weeks, but this felt way too good for what it was."
    mc "You're way too good at this! What is--"
    scene ex3vr_21_a with dissolve
    show ex3vr_21
    sophia "...my secret? Mmmh, I know what you're thinking."
    sophia "Maybe she IS wearing perfume."
    "That strange thought crossed my mind, coinciding with images of pushing the genius woman down and fucking her raw."
    mc "Ah, heeah....! W-well...?!"
    sophia "Well, it's true that you have no idea how long a microdose takes to work its way into your system."
    mc "Wah, aah..."
    sophia "Nor do you have a frame of reference for how effective the drugs can be at those levels."
    mc "I have an--"
    sophia "No, you don't. Even I don't fully comprehend it. It scares me, actually."
    "Despite what she was saying, her eyes glassed over, brimming with elation. The implications had her turned on."
    sophia "To know I've given birth to something that will irrecoverably alter the course of human history."
    mc "B-bullshit... an aphrodisiac? It's not the a-atomic bomb...!"
    "She was fucking nuts. {i}I knew that.{/i}"
    sophia "You think that's the extent of it?"
    "{i}I knew that,{/i} but I was still thrusting."
    mc "F-fuck! Are you or aren't you--?"
    sophia "No, [mcf]. This is all me and my training. {b}No drug.{/b}"
    sophia "Tonight I'm a woman of my word, and I know how to use every part of my body to give pleasure. Do you know what will feel even better?"
    mc "I--"
    scene ex3vr_22_a with dissolve
    show ex3vr_22
    mc "When did I...?"
    "...{i}when did I start fucking her pussy?{/i}"
    sophia "Ah, aahh...♥ {b}This{/b} is fun!"
    "My brain didn't even register I was balls deep in the seductress until after the fact."
    mc "Ghhahh...?!"
    "{i}She wasn't lying about her talent.{/i}"
    mc "D-don't squeeze your stomach so hard..."
    "Every time I went balls deep, Sophia tightened her core."
    sophia "Then you better fuck me until I can't~"
    mct "(...was this the same woman from earlier?)"
    "The bad jokes, the stilted conversation, all disappeared behind crazed eyes."
    mc "Eh, hnngg...!"
    "She was barely even moving, and it felt like she was the one fucking me."
    scene w3_14042 with dissolve
    sophia "Looks like it's over."
    mc "H-huh...? You--"
    scene ex3vr_23_a with dissolve
    show ex3vr_23
    "Despite my dick's best efforts, she somehow had the wherewithal to refer to Allison and Harper."
    jiji "Ah, h-ha... mmmh..."
    "Allison won, but it's not that anyone really cared by this point."
    jiji "Oh, o-oh...!"
    "The true odd man out was now racing toward his own gratification."
    allison "Enjoyed the show, old man?"
    jiji "Very much so..."
    allison "Mmh, I'm done with this slut. You want her?"
    scene w3_14043 with dissolve
    harp "Euah, hee... ah..."
    jiji "Hehe, don't mind if I do."
    scene w3_14044 with dissolve
    sophia "Ah, {b}fuckfuckfuck-!{/b}"
    scene ex3vr_24_a with dissolve
    show ex3vr_24
    "I still had a lot of work to do if Sophia was taking note of the room."
    "I wasn't sure if I hoisted her or if she climbed me, but by now she was moving her hips instead of fighting against the grain."
    sophia "{b}Yesyesyesyes!{/b}"
    pause
    sophia "O-oh, {b}{size=+10}haAAAAh...♥♥♥♥♥{/size}{/b}"
    "Either way, she clung to me sweetly, head on my shoulder and hot breath staining my shirt."
    mc "D-damn it...!"
    pause
    "My thighs burned and my head felt woozy."
    mc "Ah, haaa...!"
    "There was a very real fear that I might topple over and crack my head open all over the velvet room, but--"
    sophia "{b}Yhhnnn, aaahhh--!{/b}"
    "I thrusted. And thrusted."
    mct "(...her training?)"
    "For some reason, the funny thing she said earlier only now registered in my receding consciousness."
    mc "H-heh, f-fuck..."
    "{i}Whatever.{/i}"
    "I kept thrusting."
    "I had been enamored by hanging with a movie star, but going balls deep in a world-class chemist..."
    stop music
    play sound "sound effects/spurt.wav"
    scene ex3vr_25_a with dissolve
    show ex3vr_25
    mc "H-haaat--!"
    "...who fucking knew, huh?"
    "I unloaded everything I had without a second thought."
    sophia "H-hehe... ah..."
    scene w3_14045 with dissolve
    sophia "Thank you, [mcf]..."
    scene w3_14046 with dissolve
    mc "F-for what...?!"
    scene w3_14045 with dissolve
    sophia "I don't often play hooky."
    scene w3_14046 with dissolve
    mc "O-oh..."
    scene w3_14045 with dissolve
    sophia "*Sigh* I hate that old man."
    scene w3_14046 with dissolve
    mc "Who? Dr. Kohler?"
    scene w3_14047 with dissolve
    sophia "Both of them..."
    scene w3_14049 with dissolve
    mc "Oh..."
    scene w3_14047 with dissolve
    sophia "{b}All of them...{/b}"
    scene w3_14048 with dissolve
    "I didn't ask for clarification. I didn't need it."
    scene w3_14049 with dissolve
    mc "That's fair."
    scene w3_14050 with dissolve
    sophia "H-heh..."
    scene w3_14051 with dissolve
    mc "I'm going to put you down now, okay?"
    scene w3_14050 with dissolve
    sophia "Okay."
    scene black with fade
    $ renpy.end_replay()
    "..."
    play music "music/smooth-and-cool.ogg"
    scene w3_14143 with fade
    sophia "Good job. That was adequate."
    scene w3_14144 with dissolve
    mc "...adequate?"
    scene w3_14143 with dissolve
    sophia "One should give credit where credit is due."
    scene w3_14145 with dissolve
    "........."
    "......"
    scene w3_14146 with dissolve
    mc "...{b}ha!{/b} You fucking weirdo! Where did the succubus from earlier go?"
    scene w3_14147 with dissolve
    sophia "Uh... *ahem* She..."
    sophia "She only comes out when she needs to."
    scene w3_14148 with dissolve
    mc "What does that mean?"
    scene w3_14145 with dissolve
    "........."
    "......"
    scene w3_14149 with dissolve
    shel "Ah, that's--"
    scene w3_14150 with dissolve
    sophia "...have you read any good books lately?"
    shel "Hahaha, {b}y-yes!{/b}"
    mc "That was the worst way I've ever seen someone dodge a question."
    scene w3_14151 with dissolve
    mc "...and what did you mean by training? You mentioned it was why you were so good at--"
    scene w3_14152 with dissolve
    sophia "Huh, I said that? I don't know... maybe it was just some dirty talk? I'm weird, remember?"
    scene w3_14153 with dissolve
    "........."
    scene w3_14154 with dissolve
    "......"
    scene w3_14153 with dissolve
    "...I sure as shit hope the look I was giving her was {i}scrutinizing.{/i}"
    scene w3_14155 with dissolve
    jim "Aaaaaah, hhh-!"
    mc "{b}Fine{/b}, but if you're going to keep secrets, don't drop hints."
    jim "Ha, haaa..."
    scene w3_14156 with dissolve
    mc "It annoys the piss out of me."
    scene w3_14157 with dissolve
    sophia "Noted."
    scene w3_14158 with dissolve
    sophia "...have you given any thought about Dr. Van Doren's suggestion that you go into research?"
    scene w3_14159 with dissolve
    mc "What? Would you give me a job?"
    scene w3_14158 with dissolve
    sophia "{b}Yes.{/b}"
    scene w3_14159 with dissolve
    mc "No fuckin' way I'd be remotely qualified."
    scene w3_14160 with dissolve
    sophia "You could clean my beakers for me."
    scene w3_14161 with dissolve
    mc "You're getting better at joking."
    sophia "But I'm not--"
    scene w3_14162 with dissolve
    elias "Oh, sweet Jesus, Mother of--"
    "Naturally, the double assault made quick work of my charge -- not that I could blame him."
    "I mean {i}shit{/i}. Dalia and Allison? Must be nice to be a nepo baby billionaire."
    scene w3_14163 with dissolve
    mc "Be honest. Did Dr. Van Doren tell you to sleep with me?"
    scene w3_14164 with dissolve
    sophia "He did, yes, but tonight has nothing to do with Abel's war with Dr. Kohler. It might not even get back to him."
    scene w3_14165 with dissolve
    mc "...{i}war?{/i}"
    "That was a dramatic way to describe their pissing match."
    scene w3_14166 with dissolve
    sophia "...war? Did I say that? They're friends, of course."
    scene w3_14167 with dissolve
    mc "I hate talking to you."
    scene w3_14168 with dissolve
    harp "Ihh, hh---"
    scene ex3vr_42_a with dissolve
    show ex3vr_42
    pause
    play sound "sound effects/spurt.wav"
    scene w3_14140 with flash
    jiji "Yeeeesaaaaahhhhh!"
    "Last to wrap up the orgy was the old {b}old{/b} man."
    sophia "Wow. Listen to him yell. See? {b}Zoo.{/b}"
    scene w3_14169 with dissolve
    mc "I never disputed that."
    scene w3_14170 with dissolve
    "..."
    scene w3_14171 with dissolve
    sophia "I should go."
    scene w3_14172 with dissolve
    mc "Uh huh..."
    scene w3_14170 with dissolve
    "It was getting close to time to take Elias to the VIP room."
    scene w3_14173 with dissolve
    elias "Hey! What the fuck are you doing over there, Bukowski?! Come join us!"
    scene w3_14174 with dissolve
    sophia "If the world were merely seductive, that would be easy. If it were merely challenging, that would be no problem."
    sophia "But I arise in the morning torn between a desire to improve the world and a desire to enjoy the world. This makes it hard to plan the day."
    scene w3_14175 with dissolve
    sophia "{b}Goodbye{/b}, [mcf]."
    scene w3_14176 with dissolve
    mc "*Ahem* I believe Mrs. Pulman is waiting for us in the VIP room, gentlemen - for your official welcome, Mr. Ford."
    scene w3_14177 with dissolve
    elias "How many welcomes do I need?!"
    "{i}It was time.{/i}"
    "Elias would finally see his wife's true face."
    stop music fadeout 3.0
    scene black with fade
    if not persistent.w3OrgySophia:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3OrgySophia = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    mct "*Sigh* (Let's rock...)"
    jump w3LetsAllGoToTheVIPRoom

label w3ExOrgyContinue:
    scene w3_14052 with fade
    harp "F, fhhhuuu-♥"
    mct "(Jesus Christ, she's working her over...)"
    scene w3_14053 with dissolve
    jiji "Who do you got?"
    scene w3_14054 with dissolve
    mc "I didn't bet."
    scene w3_14055 with dissolve
    jiji "That's not what I asked."
    scene w3_14054 with dissolve
    mc "If you would've asked me ten minutes ago, I would have said Harper."
    scene w3_14055 with dissolve
    jiji "You didn't see Allison last year. She was a goddamn demon."
    scene w3_14054 with dissolve
    mc "What makes you say that?"
    scene w3_14056 with dissolve
    jiji "It was--"
    scene w3_14039 with dissolve
    harp "Aahhh, eeehhhh...♥♥♥♥♥♥♥"
    "A shrill cry stopped the old man's train of thought."
    jiji "Plus, Harper's got no incentive to win."
    scene w3_14040 with dissolve
    harp "Fu, ffhhhu... h-hhaa..."
    mc "What about losing people's money? She'd want to avoid that, right?"
    scene w3_14057 with dissolve
    allison "How do you like that, you dumb slut?"
    play sound "sound effects/thud-floor.mp3"
    scene w3_14058 with cmet
    harp "Ahahaaa..."
    jiji "I don't think she cares about Shelby losing a little face."
    scene w3_14059 with dissolve
    harp "I can still stand... it ain't over."
    scene w3_14060 with dissolve
    allison "Yes, it is. You just don't know it yet."
    play sound "sound effects/thud-floor.mp3"
    scene w3_14061 with vpunch
    harp "Eah--?!"
    allison "Hold still, {b}bitch.{/b}"
    scene ex3vr_26_a with dissolve
    show ex3vr_26
    harp "Eaahhhh...♥♥♥"
    jiji "What were we talking about?"
    mc "You called Allison a demon."
    jiji "Ah, right. She gave an unprecedented performance, you see."
    harp "Eeahh, {b}gghh, weeaahh...!{/b}"
    jiji "Kathy kept the real reason for her competing between them, and let her run wild with her own made-up backstory."
    jiji "Had the other two Carnations thinking she had a sick kid brother. Came with tears and used it to throw off their game."
    mc "...seriously, for real? How did the patrons feel when they learned the truth?"
    allison "Just give up!"
    harp "HHaat, ghnnnaahttt...♥"
    jiji "I personally {b}loved{/b} it, but I come here to get a taste of war."
    mc "...and you got that from a fake sob story?"
    jiji "All warfare is based on deception. When you are near, you must make the enemy believe that you are far away, vice versa, and so on and so on."
    jiji "And what I saw last year was a woman who was willing to do what it took to win. It warms an old heart."
    scene w3_14056 with dissolve
    jiji "A good reminder that conflict {b}is{/b} conflict."
    scene w3_14054 with dissolve
    mc "I'm going to regret asking this, but... {i}what?{/i}"
    scene w3_14055 with dissolve
    jiji "That conflict is conflict. If that woman was born under a name with prestige and had the right education..."
    scene w3_14054 with dissolve
    mc "She'd fit right in?"
    scene w3_14062 with dissolve
    harp "Ah, auoohh, {b}ahhhoooooooooooo!{/b}"
    jiji "Excuse me."
    scene black with fade
    mc "Yeah, sure--"
    scene ex3vr_23_a with dissolve
    show ex3vr_23
    allison "Enjoying the show old man?"
    jiji "Can't you tell?"
    harp "Ah, he-hehehh... w-wahh... I can..."
    allison "No, you're not. You're fucking done."
    harp "Ha, heaa... ooohhhkaa, heheh..."
    allison "Want her? I'm done with this slut."
    scene w3_14043 with dissolve
    harp "Euah, hee... ah..."
    jiji "Hehe, don't mind if I do."
    scene black with fade
    allison "Oh, hoh... you're a sprightly--"
    scene ex3vr_27_a with dissolve
    show ex3vr_27
    "I had to agree with Allison. Despite his age..."
    harp "{size=-10}Aaah, aahhh...♥{/size}"
    "He handled Harper's dead weight like she was nothing."
    jiji "Daddy's got you, nice and slow..."
    harp "{size=-10}Wwwaah, waaahhh...{/size}"
    "In no time at all, he had the insensate whore folded in half and speared on his cock, thrusting deep with a steady rhythm."
    pause
    mct "(Shit, he's not even breathing hard...)"

    if Allison_Interest > Elias_Friendship:
        scene w3_14063 with dissolve
        "Feeling a hole being burned into me, my attention turned to its source."
        scene w3_14064 with dissolve
        mc "What are you looking at?"
        scene w3_14065 with dissolve
        "I suppose, like me, she now didn't have anything to do."
        scene w3_14066 with dissolve
        mc "Good job."
        scene w3_14067 with dissolve
        allison "I hate your smirking face, you know that?"
        scene w3_14064 with dissolve
        mc "...{b}and?{/b}"
        scene w3_14068 with dissolve
        allison "..."
        scene ex3vr_28_a with dissolve
        show ex3vr_28
        pause
        scene ex3vr_29_a with dissolve
        show ex3vr_29
        "A quick glance over at Elias and then back to me was the answer to my question. She was too proud to come over to me."
        mct "(Well, it is looking like an orgy, but...)"

        menu:
            "She was Elias' date\n Elias Friendship +2":
                $ Elias_Friendship += 2
                "I just shrugged and shook my head."
                scene w3_14069 with dissolve
                mc "I'm sure Dalia will scoot right over."
                "Part of me felt stupid, but..."
                scene w3_14070 with dissolve
                allison "Hmmpfh!"
                "...there was a thrill in denying a demanding movie star."
                scene black with fade
                jump w3ExOrgyContinueAgain
            "{mod_green}...but nothing. Go over there.":

                "I don't think Elias will mind."
                stop music fadeout 3.0
                scene black with fade
                "We ARE all friends here, right?"
                jump w3ExOrgyAllison
    else:

        scene w3_14071 with dissolve
        allison "{size=-5}Fuckin' bitch... who do you...{/size}"
        "With nothing to do, Allison's attention returned to her date."
        scene ex3vr_28_a with dissolve
        show ex3vr_28
        pause
        scene w3_14072 with dissolve
        allison "Mmmh, Elias..."
        scene w3_14073 with dissolve
        allison "You like the show?"
        scene w3_14074 with dissolve
        "And now it's just me again..."
        scene w3_14075 with dissolve
        elias "Haha, I loved it!"
        jump w3ExOrgyContinueAgain

label w3ExOrgyAllison:
    play music "music/rockville.ogg"
    scene w3_14076 with dissolve
    mc "I can't see my face, am I still smirking?"
    scene w3_14077 with dissolve
    mc "Where are you going?"
    scene w3_14078 with dissolve
    "She didn't say anything, only glared."
    mct "(Fuck that's a turn on...)"
    scene w3_14079 with dissolve
    "If I'm not mistaken..."
    scene w3_14080 with dissolve
    mc "*Chwup~"
    allison "..."
    scene w3_14081 with dissolve
    mc "*Chhhhwup~*"
    "{i}That was an invitation.{/i}"
    scene ex3vr_30_a with dissolve
    show ex3vr_30
    "It was just that easy, huh?"
    "I had been peacocking all night, but the reality of having the silver screen beauty in my grasp hit me like a ton of bricks."
    "Just a little over a month ago, I was in that dingy apartment, but now...!"
    shel "Look who's joining the fun!"
    "Here I am, pawing and licking a movie star in full view of the city's elite...."
    jim "Shit, I didn't know she was up for grabs."
    mct "(What a fucking rush!)"
    "{i}I felt bulletproof.{/i}"
    scene w3_14082 with dissolve
    allison "Ha, ha... you have any idea how lucky you are?"
    scene w3_14083 with dissolve
    mc "Lucky...?"
    scene w3_14084 with dissolve

    menu:
        "Drop the act. She's right.(w3AllisonHonest = True)":
            $ w3AllisonHonest = True
            scene w3_14099 with dissolve
            mc "No disagreement here."
            scene w3_14098 with dissolve
            allison "What? Where did the prick from earlier go?"
            scene w3_14099 with dissolve
            mc "Why bother when I've already got you where I want you, huh?"
            scene w3_14100 with dissolve
            allison "God, that somehow pisses me off even more."
            scene w3_14101 with dissolve
            allison "I suppose I was right ear--"
            scene ex3vr_31_a with dissolve
            show ex3vr_31
            "Of course she was right. What red-blooded male wouldn't fuck her?"
            allison "Mmmh, mmaaa...!"
            "The difference though was that I had made it happen."
        "{mod_green}Play up your prowess.":

            scene w3_14083 with dissolve
            mc "I'm far better than any of these old men."
            scene w3_14085 with dissolve
            allison "There's more to--"
            scene ex3vr_31_a with dissolve
            show ex3vr_31
            jim "Fuck you, [mcf]!"
            allison "Mmmh, mmaaa...!"
            "Why not continue the full-of-myself routine?"
            elias "Haha! You get fucked, fatty!"


    pause
    scene w3_14087 with dissolve
    allison "You...! Ha... *gulp*"
    "She looked at me full of... {i}something good.{/i}"
    scene w3_14088 with dissolve
    elias "Hey, Ally, why don't you come over here? Bukowski can come to!"
    scene w3_14089 with dissolve
    allison "...you've your hands full, don't you Eli?"
    elias "Aw come on, the more the merrier!"
    scene ex3vr_32_a with dissolve
    show ex3vr_32
    "I paid no heed to Elias' request and apparently neither did Allison. That probably wasn't intelligent on either of our parts, but..."
    jiji "Haha! Sounds like she's jealous you abandoned her!"
    "He had a harsher reality to face tonight than just me fucking his whore."
    elias "Oh, is that what this is about? You were preoccupied!"


    if feliciaSex == True:
        "I mean, I've also had my dick inside his wife..."
    else:
        "I mean, I've also had my dick in his wife's mouth..."

    allison "O, o-oh... mmmhh...!"
    jim "Seems like she's preoccupied now too!"
    "I had been fretting about that revelation, but in the moment... {b}fuck{/b}."
    allison "Ahh, s-shit...♥"
    jim "Haha, listen to her moan! This fucking bitch!"
    "{i}It made me hard.{/i}"
    allison "S-shut {size=-5}uuaaaaphh...{/size}"
    "{b}God, I love blondes.{/b}"
    elias "Bah! Have it your way, sweetheart!"
    "God I love this bastard's women!"
    elias "Bah, whatever! Get her, Bukowski! Teach her a lesson!"
    play sound "sound effects/zipper.wav"
    scene black with fade
    "Don't mind if I do."
    scene w3_14090 with fade
    allison "{size=-5}Holy--{/size}"
    elias "Holy shit, Bukowski!"
    scene w3_14091 with dissolve

    if w3AllisonHonest == True:
        mc "How 'bout you make me feel even luckier?"
        scene w3_14102 with dissolve
        allison "You think I'm just going to suck your dick because you asked me to?"
        scene w3_14103 with dissolve
        mc "I'm hoping you will."
        scene w3_14092 with dissolve
        "For a moment, I thought she might let her pride win out, but thankfully the lust in her eyes prevailed."
    else:
        mc "I don't need to tell you what comes next, right?"
        scene w3_14102 with dissolve
        allison "You think I'm just going to suck your dick because you told me to?"
        scene w3_14103 with dissolve
        mc "We both know the answer to that."
        scene w3_14092 with dissolve
        "For a moment, I had the Carnation Queen stupefied. She stared at me, watching me trample on her pride, but her dignity was betrayed by the lust in her eyes."


    scene w3_14093 with dissolve
    allison "Damn it..."

    scene w3_14094 with dissolve
    if w3AllisonHonest == True:
        mc "Come on, give it a taste..."
    else:
        mc "Go on. Get it ready for me to fuck you."

    scene w3_14095 with dissolve
    allison "Y-you..."
    scene w3_14096 with dissolve
    allison "Be careful what you wish for, because I'm going to wipe that smirk off your face. You're not going to last past two minutes."
    scene w3_14097 with dissolve
    mc "Sounds like a challenge."
    scene w3_14104 with dissolve
    allison "Doesn't it? Bah, maybe I really am in my element here..."
    scene w3_14105 with dissolve
    mc "Two minutes then?"
    scene w3_14104 with dissolve
    allison "Agreed. If you win, you get to fuck me."
    scene w3_14105 with dissolve
    mc "And if I lose?"
    scene w3_14104 with dissolve
    allison "I don't know. Maybe I'll get one of those old men to satisfy me?"
    scene w3_14106 with dissolve
    "(Not a fucking chance...)"
    scene w3_14107 with dissolve
    allison "*Chwup~*"
    "She started slow. A kiss here."
    scene w3_14108 with dissolve
    "A lick there."
    "Super simple stuff, all focusing on the head."
    scene ex3vr_33_a with dissolve
    show ex3vr_33
    mc "A-ahh...!"
    "But soon she launched straight into it."
    allison "*Shhlrup~* *Cggwwhhup!*"
    pause
    mc "O-okay...! Ha...!"
    "What she was hitting me with wasn't the flashy kind of blowjob you see in porn, but it WAS efficient."
    mct "(I can take this for two minutes, right?)"
    "{b}No{/b}, while she didn't take it deep in her throat, she focused on my most sensitive parts."
    "One hand worked my balls, timing her massage with her ministrations up top; well-lotioned fingers giving the family jewels a squeeze every time her tongue kissed my slit."
    mc "Haa, {b}haa...!{/b}"
    "Top and bottom, stimulating me from both ends of my cock."
    allison "*Chwup, {b}fhwwwup~!{/b}*"
    mct "(Y-yeah, heh, no problem...)"
    "Meanwhile, her other hand gripped close enough to my glans to glide over the frenulum, picking up the slack in that area whenever her mouth left it wet and cold."
    "It was the total, complete control of a dick. Simple looking at first, but deceptively complicated in its mechanical precision."
    "The kind of whorish display you might see from a working girl looking to get to her next trick as quickly as possible, yet it was from a rising starlet."
    pause
    mc "Ah...♥"
    "{b}Shit!{/b} She was actually going for the kill. Where was the fun in that?!"
    mct "Ah, {b}fuuuuuhk!{/b}"
    "What's more, I had let slip that I was getting close."
    scene ex3vr_34_a with dissolve
    show ex3vr_34
    allison "Mmmh, come for me. Why fight it? You know you want to."
    "She put on her most sultry tone while jerking my cock."
    allison "Think of how good it'll feel..."
    mct "(D-damn it...!)"
    "{i}I was about to pop.{/i}"
    allison "Mmh, I'll drink every last drop, Mr. [mcl]..."
    mct "(Fuck, fuck, fuck...! How long has it been?)"
    allison "Just imagine, anytime you see me read a line... you can think back to how you blew a load in my slutty mouth~"
    allison "Doesn't that sound--"
    scene w3_14109 with dissolve
    mc "{b}T-time's up...!"
    "To be honest, I wasn't sure if it was {i}exactly{/i} two minutes, but I suspected neither did Allison--"
    scene w3_14110 with dissolve
    allison "Ghhk-?!"
    scene w3_14111 with dissolve
    mc "Should've given yourself {i}at least{/i} three minutes..."
    "--but to stop myself from cumming, I jammed my cock straight down the actress's gullet."
    scene w3_14112 with dissolve
    mc "You underestimate me if you think something like that would do me in... heh..."
    scene w3_14113 with dissolve
    mct "({size=+10}{b}Fuck{/b}{/size}, that was close!)"
    allison "Hhhk-!"
    scene w3_14114 with dissolve
    jim "Haha, holy shit! Listen to those beautiful noises!"
    shel "Give it to that stuck-up bitch!"
    scene w3_14113 with dissolve

    menu:
        "Ignore them. Recover. {b}Enjoy the moment.{/b}(w3ExAllisonTender = True)":
            $ w3ExAllisonTender = True
            scene ex3vr_35_a with dissolve
            show ex3vr_35
            "...but this?"
            mc "Ah..."
            "{i}This was nice.{/i}"
            pause
            "The feeling of being lodged in the blonde's throat was so pleasurable that I momentarily forgot where I was."
            mc "H-hold it there, baby, please."
            "The starlet sputtered against the base of my cock, her throat trying to reject me, but she did as I requested."
            allison "Ghhk--"
            "I was surprised to discover our Carnation Queen had a gag reflex, but she obviously saw no need to rid herself of it."
            allison "{b}--aaahk!{/b}"
            "After all, the {i}ability{/i} to choke on a dick wasn't entirely useless."
            pause
            scene w3_14115 with dissolve
            mct "(Oh, yeah...!)"
            scene w3_14116 with dissolve
            allison "A-hah...! *Cough* Ah...!"
            scene w3_14117 with dissolve
            "To my surprise, she didn't seem upset, but rather a mix of pleased with herself and {b}wanting{/b} to fuck. Like she had gotten both outcomes of our game."
            scene w3_14118 with dissolve
            allison "Aha... fair's fair, you asshole. What are you just standing there for?"
            scene w3_14119 with dissolve
            allison "Let's see where all the bravado comes from!"
            "In one breath, she spoke to the men around us. In another, just to me..."
            scene w3_14120 with dissolve
            allison "*Whisper* You know I wanted to do this the {i}moment{/i} I laid eyes on you, right?"
            mc "Wait, for real--"
            scene black with fade
            mc "--!"
        "Put on a show.":

            "That gave me an idea..."
            scene w3_14121 with dissolve
            mc "It sounds like the boys want to see what I can do."
            scene w3_14113 with dissolve
            "...and after waiting a few ticks to make sure the urge to climax had subsided, I barked my command."
            scene w3_14112 with dissolve
            mc "Hands down."
            scene w3_14113 with dissolve
            "She got the picture, and like the crowned slut she was, {i}she complied.{/i}"
            scene ex3vr_36_a with dissolve
            show ex3vr_36
            "It was easy pushing in and out of the starlet's mouth."
            mc "A-ah...!"
            "She sputtered and gagged, but she did not fight it."
            mc "F-fucking hell..."
            "For the cold demeanor, for her high opinion of herself, for all that she may or may not believe she's entitled to--"
            allison "Ghhhk, ghhhhk!"
            "{i}She was letting some twenty-two-year dumbass fuck her throat.{/i}"
            pause
            mc "Ahaha...!"
            "{b}I'll remember this for a goddamn lifetime.{/b}"
            allison "yyyyHhhk, heeehh--!"
            jim "'atta boy, give it to that cunt!"
            elias "J-jesus Christ! Bitch this, cunt that! S- a-aah...! Have some fuckin' respect! Don't you have a mother?!"
            "Strangely, the comments from the peanut gallery only emboldened me."
            jim "Bah! You're a weird man, Elias."
            "I guess the performative thrill had grown on me since all those weeks ago."
            allison "Yyyhhm, hhhkhk...!"
            pause
            scene w3_14122 with dissolve
            scene w3_14123 with dissolve
            allison "Hhhhhk, eeahhh... *cough* Ahh..."
            mc "I can see how you won."
            scene w3_14124 with dissolve
            allison "*Cough* Heek, you... you haven't seen {i}anything.{/i} What's the matter? Why'd you stop?"
            allison "You... aha... weren't about to come {b}again{/b}, were you? Disappointingly quick... *ahem*."
            scene w3_14125 with dissolve
            mc "Let's call it a no contest and have some fun."
            scene w3_14126 with dissolve
            allison "Heh, you're shameless..."
            "Okay, yeah, {i}so she noticed...{/i}"
            scene w3_14127 with dissolve
            mc "It comes with the territory, right?"
            scene w3_14128 with dissolve
            shel "What are you two standing around blathering for?"
            jim "Yeah! Keep it going!"
            scene w3_14129 with dissolve
            allison "Goddamn it, I {i}really{/i} hate you."
            scene w3_14128 with dissolve
            "She looked at me with curiosity in her eyes."
            scene black with fade
            mc "No, you don't."

    scene w3_14130 with fade
    allison "This is why Kathy keeps you around, huh? Your stupidly huge cock?"
    scene w3_14131 with dissolve
    mc "Ah, haa... what? Was Darius not packing?"
    scene w3_14132 with dissolve
    allison "Mmmh, what do you want me to say?"
    scene w3_14133 with dissolve
    allison "That it's not even close? That I can't say?"
    allison "What will get you to fuck me harder, [mcf]?"
    scene w3_14134 with dissolve

    menu:
        "That you're the best...?":
            mc "I don't mind being the best."
            scene w3_14133 with dissolve
            allison "I think he might've been bigger."
        "You like competition.":

            mc "I can be a little competitive..."
            scene w3_14133 with dissolve
            allison "He wasn't even close."

    scene w3_14134 with dissolve
    mc "Ha, you--"
    scene ex3vr_37_a with dissolve
    show ex3vr_37
    allison "Eeeah, ahh...♥"
    "We didn't waste time getting to it. It was an orgy after all."
    allison "B-bingo!"
    "{i}This was fun.{/i}"
    mc "Ha! You bitch!"
    "When I zigged, she zagged."
    allison "Mmmh, hhmmm~ hehe~"
    "Allison Smith was both so easy to read and impenetrable all at once."
    "Again, for all her protesting, she was into this."
    "No, like Felicia, {i}she was made for it.{/i}"
    allison "Mmmh, hmmm, mhhhhh~"

    if w3ExAllisonTender == True:
        "Gliding in and out of the movie star was effortless."
        mc "You're a voracious woman, Allison."
        allison "I just know what I want. E-even if all that little peacocking you did worked against that~"
        mc "Don't you think it's a little late to play coy after admitting I've won you over?"
        allison "Mmmh, it's {i}I{/i} who got you."
        mc "Tomato, tom--"
    else:

        "Gliding in and out of the movie star was as effortless as it had been with her throat."
        mc "You're a voracious woman, Allison."
        allison "Ahaa, heeh... for fuck's sake, don't use five-dollar words when you have your dick in somebody."
        allison "Besides, h-how can you be so confident? I could be putting it on..."
        mc "No amount of acting would account for the way you're clinging to my--"

    scene ex3vr_38_a with dissolve
    show ex3vr_38
    mc "A-ahh...?!"
    "It had only been a minute, yet..."
    mc "Damn it, this is first rate...!"
    allison "A-ahhe...♥ I know, but don't get ahead of yourself."
    allison "You've got to~ Fuck. Me. Happy."
    "I was trying, but the urge to cum, which I had only quelled a few minutes earlier, returned."
    "I tried to alter my angle of attack, yet the movie star refused."
    "Every time I retreated, she used her legs to pull me back in and keep me on pace."
    mct "(Shit...!)"
    "It seemed, unconscious on her part or otherwise, cumming quickly was an inevitability with the Carnation Queen."
    "My only choice was to buck forward, fucking Allison hard, {i}exactly{/i} how she wanted it."
    scene ex3vr_39_a with dissolve
    show ex3vr_39
    pause
    scene ex3vr_37_a with dissolve
    show ex3vr_37
    "{i}Like hell it was.{/i}"
    mc "H-hey, give me your hands..."
    allison "A-aaahh...♥ It's okay, you don't have to fight it..."
    "She read my mind, but there was no way in hell I wasn't going to try and hold back."
    "I had been too full of myself earlier to let things end so pitifully."
    scene w3_14135 with dissolve
    allison "Mmmh...?!"
    "{i}A kiss to open up the blonde's defenses.{/i}"
    scene w3_14136 with dissolve

    if w3ExAllisonTender == True:
        mc "Just work with me, eh?"
    else:
        mc "Don't fight me, slut."

    scene w3_14137 with dissolve
    allison "Hmmm...♥ This isn't--"

    scene ex3vr_40_a with dissolve
    show ex3vr_40
    "If I relaxed, it was over, so I grabbed ahold of the blonde and tightened every muscle in my pelvic floor."
    mc "Not everything is a competition..."
    shel "The fuck it isn't!"
    "I timed up my breathing with my rhythm, exhaling a deep breath on every fourth thrust."
    mc "S-shut up, old man!"
    "Hell, I thought about baseball, grandmas, and {b}Warren.{/b}"
    jiji "Ha! {b}Bahaha!{/b}"
    "{i}Anything{/i} to hold back the tide as I thrust relentlessly into the starlet."
    allison "{i}Heh...♥{/i}"
    "Allison didn't cry out from the rough transition, no, but her wavering, amused smirk showed my size getting to her."
    scene ex3vr_41_a with dissolve
    show ex3vr_41
    pause
    scene ex3vr_40_a with dissolve
    show ex3vr_40
    shel "Ah, o-ohh--"
    "{i}One-by-one{/i} they started to fall."
    play sound "sound effects/spurt.wav"
    scene w3_14138 with cmet
    shel "{b}Fuuuuuuuuuuuuuuuuuuuuuuuck--!{/b}"
    "I heard the senator groan as he, I imagined, dumped his load down his musclebound cockleeve's throat."
    shel "That's right...!"
    scene ex3vr_40_a with dissolve
    show ex3vr_40
    shel "Drink it down!"
    mct "(A-ah... fuck...!)"
    "Picturing her sorry state wasn't helping things, but I kept thrusting."
    "And thrusting."
    "{b}And thrusting.{/b}"
    "{i}And thrusting.{/i}"
    "Anything short of that would be a failure."
    jim "That--"
    play sound "sound effects/spurt.wav"
    scene w3_14139 with cmet
    jim "Gaaaah, g-good, Lord!"
    "I could easily picture his grubby, sweaty face contorted in ecstasy..."
    jim "You're my new favorite, s-shit...!"
    scene ex3vr_40_a with dissolve
    show ex3vr_40
    "{b}That helped things.{/b}"
    allison "A-aaah...!"
    mct "(Yes!)"
    allison "Ah, haha... {size=-10}f-fuck me...{/size}"
    "Allison was catching up to me as we both spiraled to the bottom of the abyss."
    "{i}Hold in there, [mcf].{/i}"
    harp "Ehhe.. hehhhh..."
    scene ex3vr_42_a with dissolve
    show ex3vr_42
    "Out of my peripheral, I caught the old soldier's work."
    "{i}Fucking Harper good.{/i}"
    harp "Eehahh, haaoo....? Ahhaa...."
    "He was still in there."
    jiji "{size=-10}Mmmh, Keep coming, doll.{/size}"
    mct "({b}Hang in there{/b}, don't lose to that war criminal.)"
    pause
    play sound "sound effects/spurt.wav"
    scene w3_14140 with flash
    jiji "Yeeeesaaaaahhhhh!"
    "{i}A warrior's scream.{/i}"
    mct "(S-seriously?)"
    scene w3_14141 with dissolve
    harp "Aii...? Huh--"
    play sound "sound effects/thud-floor.mp3"
    scene w3_14142 with vpunch
    harp "{b}Ehiihh?!{/b}"
    scene ex3vr_41_a with dissolve
    show ex3vr_41
    "That just left me and my charge."
    pause
    allison "Ah, haaa...♥♥♥"
    "Only Elias and I remained, but to my relief, now Allison didn't even bother to cover her moans."
    allison "F-fuck me, you f-fucking-- that's the--"
    scene ex3vr_43_a with dissolve
    show ex3vr_43
    mct "There it was!"
    "I had found the starlet's G-spot. She was on the ropes, and while I wasn't sure I'd last much longer..."
    allison "Ah, {b}hh---aaa...!{/b}"
    "I figured I'd take my shot at dragging Allison down with me into the churning abyss."
    allison "{b}Nnnhh, haaa...!{/b}"
    "So... I swapped my attack to quick, shallow thrusts; rabbit humping at the pixel-perfect spot to make her squeal."
    pause
    scene ex3vr_44_a with dissolve
    show ex3vr_44
    mct "(Fuck...!)"
    "Unlike with Harper, this wasn't acting."
    allison "...!"
    "Allison was scrambled, and the dumb look on her face was bringing me to climax."
    allison "Oh, {b}hh--!{/b}"
    "I watched with rapt attention as the movie star's conscious thought grew tenuous. The more I sawed at her insides, the more she looked like she was about to snap."
    scene ex3vr_43_a with dissolve
    show ex3vr_43
    pause
    scene w3_14178 with dissolve
    elias "Fuck yeah! Give it to her good, Bukowski!"
    "For a brief moment, I looked over and locked eyes with Elias."
    scene w3_14179 with dissolve
    "He looked uncivil, and maybe even a little mad."
    "Was he cross at me fucking his date? Or was it just simply the expression of a rutting animal, and I was right there with him?"
    play sound "sound effects/spurt.wav"
    scene w3_14180 with flash
    elias "A-aaah, aahh....!"
    "{i}He came.{/i} That left just me."
    scene w3_14181 with dissolve
    mc "You watching, Eli?!"
    elias "{b}S-show me...!"
    allison "O-oh, ohh, {b}o-oooh...!{/b}"
    scene ex3vr_43_a with dissolve
    show ex3vr_43
    pause
    play sound "sound effects/spurt.wav"
    scene ex3vr_45_a with flash
    show ex3vr_45
    allison "{b}Ghhhhht--!{/b}"
    "The movie star plummeted to her death."
    mc "Gh, {b}hahahaaa...!{/b}"
    "And I with her, in an act of mutually assured destruction."
    allison "{b}Y-yyehhh...!{/b}"
    "In a pit of old men, of flabby flesh meeting toned perfection, I felt nothing short of beautiful."
    "And as I piped out strands of white into my movie-star-cum-dump, a thought that had been in my periphery the whole night was the last to burn out."
    "I love the Carnation Club."
    "{i}I love the Carnation Club.{/i}"
    "{b}I love the Carnation Club.{/b}"
    stop music fadeout 3.0
    scene black with fade
    $ renpy.end_replay()

    if not persistent.w3OrgyAllison:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w3OrgyAllison = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    "........."
    "......"
    "..."
    play music "music/Moonlight-Sonata.ogg"
    scene w3_14182 with fade
    elias "I was happy to share, Bukowski. You should've come over..."
    scene w3_14183 with dissolve
    mc "Sorry, Mr. Ford. I got swept up in the moment..."
    scene w3_14184 with dissolve
    "........."
    "......"
    scene w3_14185 with dissolve
    elias "...that's alright. We're friends. This place is great."
    scene w3_14186 with dissolve
    mct "(Friends? Ha. No, we're not...)"
    scene w3_14187 with dissolve
    dal "It's time."
    scene w3_14188 with dissolve
    "{i}Fuck.{/i}"
    scene w3_14189 with dissolve
    "........."
    "......"
    scene w3_14190 with dissolve
    mc "I believe Mrs. Pulman is waiting for us in the VIP room, gentlemen - for your official welcome, Mr. Ford."
    scene w3_14191 with dissolve
    mct "(Time to learn what your wife has been up to...)"
    scene w3_14192 with dissolve
    elias "How many welcomes do I need?"
    scene w3_14193 with dissolve
    jim "Kathy's saved the best for last, I'm sure. She's the best."
    stop music fadeout 3.0
    scene black with fade
    "So, that's what we did. A bunch of naked old men and whores, moving through the building without a care in the world."
    "Only I was apprehensive."
    "........."
    "......"
    "..."
    jump w3LetsAllGoToTheVIPRoom

label w3ExOrgyContinueAgain:
    "So, I sat on the sidelines, watching the devolution of man."
    scene w3_14194 with dissolve
    "Allison joined Dalia at her rightful place on Elias' cock."
    "I think she was feeling a little bit jealous."
    scene w3_14150 with dissolve
    shel "Ahh--"
    "The senator blew his load down Cassandra's throat."
    shel "Y-yes...!"
    "He seemed fond of doing that..."
    scene w3_14155 with dissolve
    jim "Gahh, oh, {b}momma...!{/b}"
    "Next was our chief of police."
    "He looked pathetic from here."
    scene w3_14140 with flash
    jiji "Yeeeesaaaaahhhhh!"
    "The war criminal cried out next."
    mct "(S-seriously?)"
    scene w3_14141 with dissolve
    harp "Aii...? Huh--"
    scene w3_14142 with dissolve
    harp "{b}Ehiihh?!{/b}"
    "Okay, with him I was actually a little impressed."

    if w3ExDidDrugs == True:
        scene w3_14195 with dissolve
        mct "(Ah, fuck...)"
        "The high from the coke was wearing thin, but there were still some lingering effects. {i}Although...{/i}"
        "Maybe it was just all the sex and naked flesh that was fueling my raging boner right now."
    else:
        scene w3_14075 with dissolve
        "It was a surreal feeling being hands off, adrift in a sea of flesh and fucking."
        "If I wanted, I could grab a house girl, but..."
        "I just sat and watched."

    scene w3_14196 with dissolve
    shel "You a fairy or something?"
    scene w3_14197 with dissolve
    mc "You've seen me on stage, Mr. Shelby."
    mct "({i}Don't{/i} think about the old man cock dangling a mere foot away..."
    scene w3_14198 with dissolve
    shel "As far as initiations go, I'll say Elias has it pretty good."
    scene w3_14199 with dissolve
    dal "Eeeuaah, Eli~"
    shel "He's got the head whore and last year's winner doting over him. That's more than I got."
    allison "Haa, {b}haaaa...!{/b}"
    mc "...did Mrs. Pulman haze you too?"
    scene w3_14200 with dissolve
    shel "Worse. I was here for the club's opening. That night was Charles' doing. What a goddamn massacre that was."
    shel "Let me tell you, what Charles has on some of us? This retard is getting off light."
    scene w3_14201 with dissolve
    mct "(So that's how he really feels...)"
    scene w3_14202 with dissolve
    mc "They had a long chat earlier, actually... a private one."
    scene w3_14203 with dissolve
    shel "{b}Jesus.{/b}"
    mc "What...?"
    scene w3_14204 with dissolve
    shel "I just got chills. {i}Bad memory.{/i}"
    mct "(Who the fuck even is--)"
    scene w3_14162 with dissolve
    elias "Aaaaaah, yees! Sweeet-!"
    "Naturally, Elias soon followed everyone else."
    "A respectable showing, considering the double attention."
    scene w3_14205 with dissolve
    mct "(--Dr. Chuck?)"
    scene w3_14206 with dissolve
    shel "Hehe, the fun's just starting."
    scene w3_14207 with dissolve
    mc "Actually, I wouldn't start something you wouldn't want to stop. It's almost time."
    scene w3_14208 with dissolve
    shel "For what?"
    scene w3_14207 with dissolve
    mc "Elias' big welcome."
    scene w3_14208 with dissolve
    shel "My statement stands then."
    scene w3_14209 with dissolve
    "So I did my duty and rounded up Elias, corralling him out of the Velvet Room."
    "He was in a pretty fucking good mood."
    stop music fadeout 3.0
    scene black with fade
    "{b}For now.{/b}"
    "........."
    "......"
    "..."
    jump w3LetsAllGoToTheVIPRoom

label w3LetsAllGoToTheVIPRoom:
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionfelicia07 with blinds
    $ renpy.pause(6, hard=True)
    $ date = "june20night"
    play music "music/doll-dancing.ogg"
    show screen qmenu with dissolve
    scene w3_14210 with blinds
    elias "One room to the next, Jesus Christ, this place is needlessly confusing."
    kat "Welcome, Gentlemen."
    jim "Kathy!"
    scene w3_14211 with dissolve
    "........."
    scene w3_14212 with dissolve
    "......"
    scene w3_14213 with dissolve
    "...I held my breath, but when we got here, Felicia was nowhere to be seen."
    "In her place was this painting."
    scene w3_14214 with dissolve

    if w3PaintingReveal == True:
        mct "(So this was the one...)"
        "I had seen this at Denise's art show."
    elif feliciaFlag == True:
        "...wasn't this from Felicia's art show?"
        "{i}Shit.{/i} So that was what Eric Waylon was doing there."
    else:
        pass

    "........."
    "......"
    mct "...how prophetic."
    scene w3_14215 with dissolve
    kil "The fuck is this painting doing here?"
    scene w3_14216 with dissolve
    mc "Hey, dude."
    kil "'sup."
    scene w3_14217 with dissolve
    kil "So, this is going to be interesting!"
    mc "Uh, huh..."
    scene w3_14218 with dissolve
    kat "This is your place, Elias. Best seat in the house."
    elias "Where's everyone else going to sit?"
    scene w3_14219 with dissolve
    chuck "Oh, we'll be right behind you."

    if w3DuoVickyVisit == True:
        scene w3_14220 with dissolve
        mc "You had something you wanted to talk about?"
        scene w3_14221 with dissolve
        "The moment I brought it up, Ian had the same pensive look from earlier."
        "It didn't take a fucking emotional genius to realize what it was about."
        scene w3_14222 with dissolve
        mc "Mom's still the woman who took us out for ice cream, dude."
        scene w3_14221 with dissolve
        "........."
        scene w3_14223 with dissolve
        "......"
        scene w3_14224 with dissolve
        kil "...I'm going to hurt that bitch."
        mc "What are you--"
        scene w3_14225 with dissolve
        hana "No hello?"
        mct "(...what the fuck was that expression?)"

        if hanaGF == True:
            scene w3_14226 with dissolve
            mc "Hello."
            scene w3_14227 with dissolve
            "*Chwup*"
            scene w3_14228 with dissolve
            hana "Hey."
            scene w3_14229 with dissolve
            "For a flash, Ian's eyes scared me."
            scene w3_14230 with dissolve
            mc "Uh, sorry. Can you give me a second? I need to talk to Ian alone."
            scene w3_14231 with dissolve
            hana "Uh, sure..."
            scene w3_14232 with dissolve
            "*Chwup*"
            scene w3_14233 with dissolve
            mc "Hallway, dude."
            scene black with fade
            "..."
        else:
            scene w3_14234 with dissolve
            mc "Hey..."
            "For a flash, Ian's eyes scared me."
            scene w3_14235 with dissolve
            hana "What are you two talking about?"
            scene w3_14234 with dissolve
            mc "That's a good question. Uh, sorry. Can you give us a second? I need to talk to Ian alone."
            scene w3_14236 with dissolve
            hana "Not the best place for that."
            mc "I know..."
            scene w3_14237 with dissolve
            mc "Hallway, dude."
            scene black with fade
            "..."

        play music "music/myst-on-the-moor.ogg"
        scene w3_14238 with fade
        mc "You're thinking something bad. I can tell."
        scene w3_14239 with dissolve
        kil "And stupid."
        scene w3_14238 with dissolve
        mc "Then stop."
        scene w3_14239 with dissolve
        kil "{b}No.{/b}"
        scene w3_14240 with dissolve
        "........."
        scene w3_14241 with dissolve
        "......"
        scene w3_14242 with dissolve
        mc "...what is it then?"
        scene w3_14243 with dissolve
        "......"
        mct "(...second thoughts?)"
        "That \"bitch\" he was referring to was obviously--"
        scene w3_14244 with dissolve
        kil "What would you say to fucking my mom?"
        scene w3_14245 with dissolve
        mc "W-wha--?"
        scene w3_14246 with dissolve
        "{b}Oh God.{/b}"
        "{i}He was serious.{/i}"
        scene w3_14247 with dissolve
        kil "Ha! Oh fuck, I just came out and said it! And somehow, {b}goddamnit{/b}, it didn't make me change my mind."
        kil "I really thought it would... shit. So how 'bout it?"
        scene w3_14248 with dissolve
        mc "What the fuck are you talking about?!"
        scene w3_14249 with dissolve
        "........."
        scene w3_14250 with dissolve
        "......"
        scene w3_14251 with dissolve
        kil "I wonder... how far will she go, [mcf]? To get me to go to college?"
        kil "It's all I can think about."
        scene w3_14250 with dissolve
        "...had he ever looked so despondent."
        scene w3_14251 with dissolve
        kil "Wouldn't it be funny? Getting her to film a little video for you after she tried to use Vicky's past to--"
        scene w3_14252 with dissolve
        mc "{i}Bro.{/i}"
        mc "You're not thinking straight."
        scene w3_14253 with dissolve
        kil "No shit! It's not every day you find out the woman you love the most in the world is a whore--"
        scene w3_14254 with dissolve
        mc "Fuck you!"
        scene w3_14255 with dissolve
        kil "You-! It's not... what the fuck is wrong with my mom, [mcf]?"
        kil "She's never loved me. You all tell me she does, but she doesn't. I can tell--"
        scene w3_14256 with dissolve
        kil "--!"
        scene w3_14257 with dissolve
        "........."
        "......"
        scene w3_14258 with dissolve
        kil "...wouldn't it be funny? No, wouldn't it be poetic? Getting her to film a little video for you?"
        scene w3_14259 with dissolve
        mct "(...Jesus, why did I tell him?)"
        "A small part of me felt guilty, but all I had done was tell him the truth, hadn't I?"
        scene w3_14260 with dissolve
        "It was Grace who had done the damage. First to Ian, then my mom, and also me..."
        scene w3_14261 with dissolve
        mc "I get where you're coming from, I do..."
        scene w3_14260 with dissolve
        "The more I thought about it, it's not like I didn't understand the impulse to get even, but--"
        scene w3_14261 with dissolve
        mc "It's not like she'd even agree to that."
        scene w3_14260 with dissolve
        kil "...she's a woman, isn't she?"
        scene w3_14262 with dissolve
        "A vitriolic feeling so sickening that I wanted to puke came over me. {i}I knew exactly what he meant.{/i}"
        "There was no exception there. Part of me wanted to punch him in the fucking for the insinuation, but more than that..."
        scene w3_14263 with pixellate
        mc "Why do you just sit there and let them bully you?"
        scene w3_14264 with dissolve
        kil "Anything I do will just make it worse..."
        scene w3_14263 with dissolve
        mc "You can't know that if you haven't tried."
        scene w3_14264 with dissolve
        kil "You should go away. They'll move on to you, too, if they see you talking to me."
        scene w3_14265 with dissolve
        "........."
        scene w3_14266 with dissolve
        "......"
        scene w3_14267 with dissolve
        mc "...fuck 'em. I hope they do."
        scene w3_14268 with dissolve
        kil "Don't--"
        mc "Don't what?"
        kil "Don't curse! You'll get in trouble."
        scene w3_14269 with dissolve
        mc "Fuck, fuckity, fuck!"
        "Yes, I wanted to be angry at Ian, but..."
        kil "S-stop! You're going to get me in trouble--"
        scene w3_14270 with pixellate
        "...if I hadn't spoken to him then, none of this would have happened."
        scene w3_14271 with dissolve
        kil "I've got to burn some fuckin' bridges, man. No matter what, that much is clear. I've gotta... I've got to cut ties with that woman."
        scene w3_14270 with dissolve
        "There'd be no \"Vicky\" for his mom to twist the knife with and my lonely ass might've never made a friend."
        scene w3_14271 with dissolve
        kil "She's not going to let me go quietly. Who knows how she might lash out? I need--"
        scene w3_14272 with dissolve
        mc "{b}Leverage.{/b}"
        scene w3_14270 with dissolve
        "Leverage for when she cuts him off financially, leverage for when she finds out that my mom undercut her plans by simply telling the truth."
        scene w3_14271 with dissolve
        kil "Exactly..."
        scene w3_14260 with dissolve
        "Everything from that moment led up to this. From us getting detention together to us now standing face-to-face in the Carnation club."
        "For better and worse, we were on this path together, inextricably linked."
        "I wanted to take responsibility."

        menu:
            "Like old times, I wanted to get revenge.(graceRevenge = True)":
                $ graceRevenge = True
                scene w3_14273 with dissolve
                mc "I doubt she'd agree to it."
                "{i}What the hell was I saying?"
                scene w3_14274 with dissolve
                kil "It's fucked up, but that's what I'm dying to know."
                scene w3_14273 with dissolve
                mc "It's a stupid plan, Ian. Have you forgotten about your uncle?"
                scene w3_14275 with dissolve
                kil "What would she tell him? That she agreed to spread her legs so I'd go to college? I don't think he'd give a fuck."
                kil "Besides, she would never. She has her pride."
                scene w3_14270 with dissolve
                "........."
                "......"
                scene w3_14271 with dissolve
                kil "...I know that look. You're actually considering it."
                scene w3_14270 with dissolve
                "Once I got past the absurdity of his request, I saw the logic. Of Ian having leverage, of the thrill of getting back at the cunt, and--"
                scene w3_14272 with dissolve
                mc "It's a bad idea."
                scene w3_14276 with dissolve
                "...doing something stupid, like old times."
                scene w3_14277 with dissolve
                kil "That's not a no..."
                scene w3_14278 with w20:
                    align (0.5,0.5)
                    linear 160 zoom 2.5
                    pause 4
                "No, it wasn't."
                "No, it fucking wasn't."
                "No, it goddamn fucking wasn't."
                scene w3_14279 with pixellate
                mc "..."
                play sound "sound effects/door-open.wav"
                scene w3_14280 with dissolve
                kat "What the hell are you two doing out here? We're about to begin. Take your places."
                scene w3_14281 with dissolve
                mck "Yes, Ma'am."
                scene w3_14282 with dissolve
                kat "Wha... bah, I don't know what's with you two, and I don't care. {b}This is going to be fun!{/b}"
                play sound "sound effects/door-close.wav"
                scene w3_14283 with dissolve
                kil "We'll talk more about this later."
                scene w3_14284 with dissolve
                mc "Yeah..."
                scene w3_14285 with dissolve
                "The smiling face looking at me wasn't the friend I knew."
                "I knew in my heart that nothing good would come of this, but I wasn't sure rejecting the idea would leave Ian in any better of a headspace."
                stop music fadeout 3.0
                scene black with fade
                "{i}Might as well swing for the fences.{/i}"
                "......"
                "..."
                jump w3ExTheBigReveal
            "I wanted to set Ian straight.(badIdeaBro = True)":

                $ badIdeaBro = True
                scene w3_14286 with dissolve
                mc "I get she's done a fucking number on you, but this dumbass plan will just make you even more--"
                scene w3_14277 with dissolve
                kil "...more what?!"
                scene w3_14287 with dissolve
                mc "{b}Fucked{/b} in the head."
                scene w3_14288 with dissolve
                kil "{i}I'm{/i} fucked in the head?! Who cares?! She's dead to me! What about you-"
                scene w3_14289 with dissolve
                mc "{b}Listen{/b} to yourself and think about what you're asking. {i}Really{/i} think about it."
                mc "There's no satisfaction at the end of it!"
                scene w3_14276 with dissolve
                "........."
                "......"
                scene w3_14277 with dissolve
                kil "...I'll never be satisfied."
                scene w3_14290 with dissolve
                kil "...and I'm okay with that. Do you remember that Fourth of July you and Vicky stayed at the lake house?"
                scene w3_14291 with dissolve
                mc "Of course, I do. Both our moms had an aneurysm when you shot a Roman candle at me."
                scene w3_14290 with dissolve
                kil "It was perfect."
                kil "Like a movie, I used to lie in bed at night and replay that weekend in my head."
                kil "Lately though... I think I'm forgetting some of the details. I don't feel the... {b}warmth{/b} anymore."
                scene w3_14292 with dissolve
                kil "Do you think a memory could last a lifetime?"
                scene w3_14293 with dissolve
                "........."
                "......"
                scene w3_14294 with dissolve
                play music "music/hotshot.ogg"
                scene w3_14295 with vpunch
                mc "Don't be so fuckin' dramatic, Moron!"
                scene w3_14296 with dissolve
                kil "Eh?!"
                scene w3_14298 with dissolve
                mc "You don't have to feed on scraps of happiness for the rest of your life. Make some fucking new memories!"
                scene w3_14297 with dissolve
                "It was harsh, and maybe a little bit hypocritical for me to dole out life advice, but I latched onto a feeling. "
                scene w3_14298 with dissolve
                mc "Start by getting a girlfriend whose head you don't fuck with! I love you man, but there are other people out there who are capable of loving you for who you are, too."
                mc "You {i}just{/i} have to go for it."
                scene w3_14299 with dissolve
                mc "And hell, while you're at it, maybe actually think about what you want to do with your life. Like what would you like to try?"
                scene w3_14300 with dissolve
                mc "I'm guessing {i}this{/i} has been getting stale, right? Then reorient! Don't wallow!"
                mc "You had better grades than me in middle school without even trying! Fuck your bitch mother, but maybe you {b}should{/b} think about it!"
                scene w3_14301 with dissolve
                mc "Stop being lazy! Do the lifting!"
                scene w3_14302 with dissolve
                kil "Dude, what the fuck! Why--"
                play sound "sound effects/door-open.wav"
                scene w3_14280 with dissolve
                kat "What the hell are you two doing out here? We're about to begin. Take your places."
                scene w3_14303 with dissolve
                kil "Can you give us a moment?! We're having a--"
                scene w3_14304 with dissolve
                kil "Ah... *ahem* Uh... {i}oops.{/i} Heh."
                scene w3_14305 with dissolve
                kat "...remembered who you're talking to? {b}Good.{/b} Get inside."
                play sound "sound effects/door-close.wav"
                scene w3_14306 with dissolve
                mc "Uh, we'll talk about this later?"
                scene w3_14307 with dissolve
                kil "And get hit with more dad advice? Fuck off!"
                scene w3_14306 with dissolve
                mc "Am I wrong?"
                scene w3_14307 with dissolve
                kil "...no, but you didn't have to pile it on."
                scene w3_14306 with dissolve
                mc "But maybe I did?"
                scene w3_14308 with dissolve
                kil "*Sigh* We'll talk later. Just forget I asked you to--"
                stop music fadeout 3.0
                scene black with fade
                kil "I can't believe I actually--"
                "......"
                "..."
                jump w3ExTheBigReveal
    else:


        scene w3_14309 with dissolve
        kil "This could get messy, {i}Bukowski.{/i}"
        scene w3_14310 with dissolve
        kil "I've got your back."
        scene w3_14311 with dissolve
        hana "No hello?"

        if hanaGF == True:
            scene w3_14312 with dissolve
            mc "*Chwup*"
            scene w3_14313 with dissolve
            mc "Hello."
            scene w3_14314 with dissolve
            kil "Oh! Can I get a kiss too?"
            hana "Which one of us are you asking?"
        else:
            scene w3_14315 with dissolve
            mck "Hello."
            scene w3_14316 with dissolve
            hana "Funny."

        scene w3_14317 with dissolve
        hana "What are you two talking about?"
        kil "Elephant in the room."
        hana "Ah..."
        scene w3_14318 with dissolve
        mc "Surprised you're here, actually."
        hana "The old man said all hands on deck. It wouldn't do for an owner to snub our newest member's big welcome."
        scene w3_14319 with dissolve
        "........."
        "......"
        scene w3_14320 with dissolve
        "...the three of us collectively sighed."
        scene w3_14321 with dissolve
        kil "I'm going to get a drink..."
        scene w3_14322 with dissolve
        kat "We'll be starting soon. You've got a place backstage."
        hana "Have fun..."
        stop music fadeout 3.0
        scene black with fade
        "This was about when the nerves kicked in."
        jump w3ExTheBigReveal

label w3ExTheBigReveal:
    play music "music/unsafe-roads.ogg"
    scene w3_14323 with curtains
    pause
    scene w3_14324 with dissolve
    pause
    scene w3_14325 with dissolve
    "............"
    "........."
    "......"
    scene w3_14326 with dissolve
    elias "...I don't see anything."
    scene w3_14327 with dissolve
    kat "You don't? Are you sure?"
    scene w3_14328 with dissolve
    elias "...?"
    scene w3_14326 with dissolve
    elias "...is this a joke? I don't see anything."
    scene w3_14329 with dissolve
    kat "What do you want more than anything in the world? Nothing less than the world itself?"
    scene w3_14330 with dissolve
    elias "Ha, that'd be a good start. Are you saying the world is my stage?"
    scene w3_14329 with dissolve
    kat "{b}No.{/b} God, no! My point is a lot more painful."
    scene w3_14331 with dissolve
    elias "I'm confused..."
    scene w3_14332 with dissolve
    kat "I'm sorry I sold you on a lie. I told you the club could satisfy your every whim, but... we can't give you what you really want."
    kat "And even if we could raise the dead, there's no way we can get your daddy to love you, can we?"
    scene w3_14333 with dissolve
    elias "What the fuck are you--?!"
    scene w3_14334 with dissolve
    kat "I don't know what Charles told you in private, but don't believe him."
    kat "Fraternity? Playing your part? {b}No.{/b}"
    scene w3_14335 with dissolve
    kat "Every person in this room, myself included, is but a {b}light{/b} in the darkness trying to drown out their neighbor."
    scene w3_14336 with dissolve
    chuck "Oh, Kathy, I love your beautiful mind!"
    scene w3_14337 with dissolve
    kat "I sympathize with you, my sweet Elias. To live in the shadows is a {b}maddening{/b} thing, doubly so when it's cast by a husk, but what you see in front of you could be a light of your own."
    scene w3_14338 with dissolve
    elias "I.. I... eh...? I still don't..."
    scene w3_14339 with dissolve
    kat "That is my gift to you, for a man who has it all. It's dim, but it might just disperse the gloom you're living under."
    scene w3_14340 with dissolve
    chuck "Ehehe...! {b}Fuck!{/b} This is gonna be--"
    kat "You haven't met our short-lived flowers, have you?"
    elias "I h-haven't had the pleasure, no..."
    scene w3_14341 with dissolve
    kat "The ones cultivated this year are simply superb. Allow me to introduce them."
    scene w3_14342 with dissolve
    kat "Warren!"
    "............"
    "........."
    "......"
    scene w3_14343 with dissolve
    play sound "sound effects/thud-floor.mp3"
    scene w3_14344 with vpunch
    "--!"
    scene w3_14345 with dissolve
    mc "You-- Mother fucker, don't--"
    scene w3_14346 with dissolve
    kil "Not the time, dude--"
    scene w3_14347 with dissolve
    kat "First, we have Rosalind."
    kat "Except for her tits, a man like you would find her rather plain, I would think."
    elias "I like what I see!"
    scene w3_14348 with dissolve
    kat "Mmmh, 'fraid she's not blonde under here."
    kat "Dauntless Rosie is here to clear up a debt, although..."
    scene w3_14349 with dissolve
    kat "I guess that problem has been taken care of in a sense."
    rose "Wh, w-where-?"
    scene w3_14350 with dissolve

    if w3RosalindViolentSolution == True:
        kat "The club owns her ass after August had her creditor thrown off an overpass."
    else:
        kat "The club owns her ass after Chucky juiced the wheels of justice."

    scene w3_14351 with dissolve
    jiji "Really?"
    kat "Oops, we really should have a newsletter, shouldn't we?"
    scene w3_14352 with dissolve
    kat "Quite a compelling bit of drama, actually. Your good friend Bukowski has been an ardent supporter of {b}Mrs.{/b} Carter, staring down dragons on her behalf."
    scene w3_14353 with dissolve
    kat "She's good like that. Greet the man of honor, slut."
    scene w3_14354 with dissolve
    rose "H-hello...?"
    scene w3_14355 with dissolve
    kat "Next, we have Veronica! {b}Get out here, Ian!{/b}"
    scene w3_14356 with dissolve
    kil "Come on, come... ah, you can't hear me. Fuck it!"
    scene w3_14357 with dissolve
    kat "Ohoho, I knew all that moving work would come in handy."
    scene w3_14358 with dissolve
    kil "Yeah, yeah... *sigh*"
    scene w3_14359 with dissolve
    kat "Veronica fancies herself a proprietress, but she's more of a bull in a china shop. Not a fucking clue what she's doing."
    kat "To be honest, I doubt she's to your tastes either."
    scene w3_14360 with dissolve
    elias "I'm not really into muscles--"
    scene w3_14361 with dissolve
    elias "Huh. She's got a cute face."
    scene w3_14362 with dissolve
    ver "Eh, haa... {i}great.{/i}"
    scene w3_14363 with dissolve
    kat "Our valkyrie is actually an Olympian. You ever fuck a silver medalist, Elias?"
    elias "I can't say I have."
    scene w3_14364 with dissolve
    kat "Mmmh, that {i}could{/i} be arranged, but I think you'll find our last Carnation to be juuuuuust right."
    scene w3_14365 with dissolve
    chuck "Except Goldilocks is the one being eaten!"
    scene w3_14366 with dissolve
    kat "[mcf]! Bring out Carnation Number Three!"
    scene w3_14367 with dissolve
    "....................."
    ".................."
    scene w3_14368 with dissolve
    "..............."
    "........."
    "......"
    scene w3_14369 with dissolve
    kat "...get the fuck out here!"
    scene w3_14370 with dissolve
    if w3ExFelForewarnedSortOf == True:
        "Not only did I have a front row seat to the betrayal, I was the hand delivering it."
    else:
        mct "(It's all about to make sense, Felicia...)"
    scene w3_14371 with dissolve
    "Meanwhile. Felicia followed me easily, letting me guide her."
    scene w3_14372 with dissolve
    jim "Wow! What a body!"
    scene w3_14373 with dissolve
    elias "Yeah, I like the... those tan lines are..."
    scene w3_14374 with dissolve
    "For a second I thought the jig was up, but."
    scene w3_14375 with dissolve
    elias "...are {b}perfect.{/b} I'll give you that: you've got a pretty good read on me, Kathleen."
    scene w3_14376 with dissolve
    elias "Hey, Bukowski!"
    mc "Ah... yeah, long time no see..."
    scene w3_14377 with dissolve
    "Felicia, to the old woman's credit, couldn't hear a fucking thing with the mask on."
    "At some point I needed to pull it off, I just needed to wait for the cue..."
    scene w3_14378 with dissolve
    elias "So, what does this one want?"
    scene w3_14379 with dissolve
    kat "{b}That{/b} is the million dollar question. She's come here seeking to {b}join{/b} our clientele."
    scene w3_14380 with dissolve
    elias "Her?"
    scene w3_14381 with dissolve
    kat "Uh huh! Believe it or not, this Carnation is quite affluent - and her appetites? She'd actually fit right in."
    scene w3_14383 with dissolve
    chuck "I've taken quite the shine to her!"
    "...? I had never seen Kathleen and Dr. Chuck look as alike as I had in this moment. Both were smiling ear-to-ear, geeked out on the tension, giddy for the shoe to drop."
    scene w3_14382 with dissolve
    kat "Yes... she's very... {b}willful.{/b}"
    scene w3_14383 with dissolve
    elias "Huh! Would I know her?"
    scene w3_14384 with dissolve
    kat "Hahaha! You've seen her, but I don't think you {b}know{/b} her."
    scene w3_14385 with dissolve
    elias "Alright. Can we stop the pronoun game now? Who the hell is it?"
    "With those words I felt an itching in my stomach..."
    scene w3_14384 with dissolve
    kat "You really want to know? You can't take it back."
    scene w3_14385 with dissolve
    "...that quickly grew into a sickness."
    scene w3_14386 with dissolve
    elias "Cut the rhetorical bullshit!"
    scene w3_14387 with dissolve
    "Elias wasn't stupid, he had picked up on the irregularity and undoubtedly keyed into Mrs. Pulman's malicious aura."
    scene w3_14388 with dissolve
    elias "I'm here, aren't I?"
    scene w3_14389 with dissolve
    elias "A-ah, h-huh?"
    kat "[mcf], would you do the honors? Drum roll! Tell Elias what he's won!"
    scene w3_14390 with dissolve
    mct "(Shit... why do I care?)"

    if Elias_Friendship >= 4:
        "Did part of me actually kinda like Elias? Was it Felicia?"
    else:
        "Was it Felicia?"

    scene w3_14391 with dissolve
    "Did I just fear having a target put on my back for my complicity?"
    scene w3_14392 with dissolve
    "............"
    "........."
    "......"
    play music "music/no-turning-back.mp3"
    scene w3_14393 with dissolve
    "...when I returned, I was outside myself, looking in."
    scene w3_14394 with dissolve
    "{i}All was calm.{/i} I had no bearing on the wind, did I?"
    mc "I don't bear any ill feelings toward you, Elias."
    scene w3_14395 with dissolve
    elias "What are you talking about, Bukowski?"
    mc "May I present to you the third and final Carnation..."
    scene w3_14396 with dissolve
    elias "What the, I... just--"
    scene w3_14397 with dissolve
    elias "W-wait...! {b}No...!{/b}"
    scene dundundun with dissolve
    show felex3_reveal
    elias "F-felicia?!"
    "He had guessed it before the mask had even come off."
    kat "That's right! Felicia {i}Barnes{/i}-Ford. Your lovely wife!"
    scene w3_14398 with dissolve
    fel "Ehh...?! {b}E-el...?!{/b}"
    "For once, Felicia was bereft of {b}all{/b} that made her {i}her.{/i}."
    fel "I, h-huh- Elias?! "
    scene w3_14399 with dissolve
    "There was nothing but pure terror in Felicia's voice."
    fel "N-no! No, no, no, no!"
    kat "Welcome to our first-ever Club Power couple!"
    scene w3_14400 with dissolve
    elias "What the fuck is the meaning of that? I, I...! F-felicia... I'm, a-ah..."
    scene w3_14401 with dissolve
    elias "What, I'm... we're both members? Is that it? Both of us?"
    scene w3_14402 with dissolve
    kat "Not quite; she's competing for the chance."
    scene w3_14403 with dissolve
    elias "Jesus Christ, this... B-bukowski..."
    scene w3_14404 with dissolve
    kat "That's right. Your interview had more than one hidden purpose. Take a bow, [mcf]."
    fel "No.."
    mc "Felish--"
    scene w3_14405 with dissolve
    fel "Nonononono..."
    kat "[mcf]! Take. A. Bow!"

    menu:
        "Do as ordered.":
            scene w3_14406 with dissolve
            "...fuck."
            "{i}Why did I listen?!{/i}"
        "Fuck that, check on Felicia.":

            scene w3_14407 with dissolve
            mc "Felicia, I--"
            fel "Shut the fuck up! Shut the fuck up!"
            scene w3_14408 with dissolve
            if w3ExFelForewarnedSortOf == True:
                fel "So, that's, that' what..."
            else:
                fel "I don't want to h-hear it..."

            scene w3_14407 with dissolve
            mc "Breathe! Breathe!"


    if w1ExGame2LoserFel == True:
        scene w3_14409 with dissolve
        kat "For the last three weeks, your wife has been part of our games."
    else:
        scene w3_14410 with dissolve
        kat "For the last three weeks, your wife has been part of our games."

    scene w3_14411 with dissolve
    kat "You should be proud of her. She's really shone, but I'm sure you are well acquainted with her talents and personality."
    elias "I..."
    scene w3_14412 with dissolve
    fel "Elias, I can ex--"
    scene w3_14413 with dissolve
    elias "Shut the fuck up! You kept this from me?!"
    elias "Is this all a lie? A trick?!"
    scene w3_14414 with dissolve
    kat "Not at all. I'm looking at the city's next mayor, and what I'm sure will be a stepping stone to--"
    scene w3_14415 with dissolve
    chuck "...maybe our fine state's governor?"
    scene w3_14416 with dissolve
    hana "Jesus Christ, Dad..."
    scene w3_14417 with dissolve
    aug "Yeah, I fucking know kid."
    scene w3_14418 with dissolve
    fel "I'm fucked, it's over..."
    scene w3_14419 with dissolve
    kat "Don't be too mad. In a sense, you can thank your wife for your present windfall."
    scene w3_14420 with dissolve
    chuck "We had an eye on you, but the timing was too good to pass up."
    scene w3_14421 with dissolve
    fel "E-even if I..."
    scene w3_14422 with dissolve
    kat "Everything has led up to this. From--"
    scene w3_14423 with dissolve
    fel "Don't touch me!"
    scene w3_14424 with dissolve
    chuck "From your father's murder--"
    scene w3_14425 with dissolve
    kat "To your failure of a first marriage and your choice of a second wife--"
    scene w3_14426 with dissolve
    chuck "You chose a good woman, I might add."
    scene w3_14427 with dissolve
    kat "Rejoice, Elias. You're home. Just remember--"
    scene w3_14428 with dissolve
    chuck "Corvus oculum corvi non eruit."
    scene w3_14429 with dissolve
    kat "A crow will not pull out the eye of another crow."
    scene w3_14430 with dissolve
    chuck "All this to say, with this, you're {b}officially{/b} a member of our club."
    scene w3_14431 with dissolve
    kat "Before we begin our games, do you have anything to say to your wife?"
    scene w3_14432 with dissolve
    ".................."
    "..............."
    "........."
    "......"
    scene w3_14433 with dissolve
    elias "You {b}better{/b} win, Felicia."
    scene w3_14434 with dissolve
    play sound "sound effects/thud-floor.mp3"
    scene w3_14435 with vpunch
    fel "--!"
    kil "Oh, shit!"
    mc "She's passed out--"
    scene w3_14436 with dissolve
    kat "Fabulous! Wonderful! Ah, yes, yes, yes!"
    ver "B-blondie!"
    kat "Now, without further ado... {b}let the games begin!{/b}"
    pause
    scene black with fade
    "And with that, {i}hell week's exhibition had officially started."
    stop music
    play sound "sound effects/sting-mumbaieffect.wav"
    hide screen qmenu with dissolve
    call screen thanksforplaying
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
