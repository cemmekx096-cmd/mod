label w2MinaRevealContinued:
    "..."
    play music "music/sneaky-snitch.ogg"
    scene w2_3505 with dissolve
    "Mina let the question hang in the air with a pregnant pause, pulling the whole room into a communal silence."
    scene w2_3506 with dissolve
    fel "A... video, hun?"
    scene w2_3505 with dissolve
    "Until finally, Felicia saw fit to break it."
    scene w2_3506 with dissolve
    fel "I don't think..."
    scene w2_3507 with dissolve
    "Mina looked into Felicia's eyes with a funny, almost investigative look."
    scene w2_3508 with dissolve
    mina "Ha!"
    scene w2_3509 with dissolve
    mina "You should see the look on your faces."
    scene w2_3510 with dissolve
    mina "I'm... kidding. Just..."
    mina "...kidding."
    scene w2_3511 with dissolve
    mina "I mean, could you imagine it?"
    "The expression on her face revealed the gears grinding in her cute little head."
    scene w2_3512 with dissolve
    mina "You? ...me?"
    scene w2_3513 with dissolve
    mina "...and [mcf]?"
    scene w2_3514 with fade
    mina "Nope!"
    scene w2_3515 with dissolve
    mina "File that alongside the growing list of bad impulses today."
    mina "Right next to sending Ian's mother the videotape of him boinking his nanny."
    scene w2_3516 with dissolve
    mina "So... fucking..."
    scene w2_3517 with vpunch
    mina "GROSS!"
    scene w2_3518 with dissolve
    fel "Don't try and understand it, sweetie. You're hotter than either of those skanks in the video, but men are... fickle."
    mc "Fickle is a very kind and generous way of describing Ian."
    scene w2_3519 with dissolve
    mc "Heh..."
    $ renpy.music.set_volume(.3, 3, channel = "music")
    "{b}This{/b} was very, {i}very{/i} much not a situation I was suited for."
    "How did I get pulled into this?"
    scene w2_3520 with dissolve

    if Killian_Bromance <= 15:
        "That was an easy question to answer. It was very much like the Carnation Club; a byproduct of being within that asshole's orbit."
    else:
        "That was an easy question to answer. It was very much like the Carnation Club; a byproduct of being within my friend's orbit."

    "How should I deal with it?"
    scene w2_3521 with dissolve
    "I'd seen it in movies. The words of consolation and the usual platitudes..."

    if perk_strongman == True:
        "I didn't quite know what to say or how to say it."

        if minaFlag == True:
            "Mina was a nice person who I went out of my way to befriend."
        else:
            "Even if it wasn't my job, I am presently here."
    else:

        "I knew the things I should say, but I was apprehensive of how empty it would sound coming from my lips."

        if minaFlag == True:
            "Mina was a nice person who I went out of my way to befriend."
        else:
            "Even if it wasn't my job, I am presently here."

    "I knew from experience..."
    scene w2_3522 with pixellate
    "Words don't always suffice."
    "There are simply situations that logic is unable to mend."
    scene w2_3523 with pixellate
    mct "(Well, she said it herself.)"
    scene w2_3524 with dissolve
    "She doesn't need a babysitter."
    scene w2_3525 with dissolve
    mc "What are you two talking about?"
    mina "Just... stupid stuff."
    fel "Don't say that."
    scene w2_3526 with dissolve
    fel "Our girl's got a kernel of an idea just awaiting a kettle."
    scene w2_3527 with dissolve
    mina "Oh gosh, I was just talking out of my tushie."
    scene w2_3528 with dissolve
    fel "No need to be rash, but what you were saying made sense."
    fel "You're young and in your prime after all."
    scene w2_3529 with dissolve
    mina "I don't know, Felicia..."
    scene w2_3530 with dissolve
    fel "It was your idea. Mull it over."
    fel "Tell [mcf] about it later if you want."
    scene w2_3531 with dissolve
    "I waited to be filled in, but neither of the women deigned to explain."
    scene w2_3532 with dissolve
    mina "I know how Elias is. You should go and get prepared for your thing."
    scene w2_3533 with dissolve
    fel "I really don't want to, you know that?"
    scene w2_3532 with dissolve
    mina "Yeah, yeah, I know about your arrangement with that crackpot."
    mina "I appreciate you picking up the phone this morning."
    scene w2_3533 with dissolve
    fel "Well, you don't usually call that early..."
    scene w2_3534 with dissolve
    mina "Thanks for coming, Felicia."
    fel "No problem, hun. I'll be back later tonight, after my thing."
    mina "I'm not a kid, I'll be alright."
    scene w2_3535 with dissolve
    fel "...really?"
    mina "...no, I actually love that. Please do."
    scene w2_3536 with dissolve
    fel "Count on it then, you geek."
    scene w2_3537 with dissolve
    fel "Don't make a move on poor little Mina while she's down in the dumps, okay?"
    scene w2_3538 with dissolve
    mina "Pffft...!"
    "Felicia's little crack had its intended effect, dragging a delightful snort from the blonde."
    scene w2_3539 with dissolve
    mc "Come on, what do you take me for?"
    scene w2_3540 with dissolve
    fel "Are you really asking that?"
    mina "Heh. Yeah, what do you take [mcf] for, Felicia?"
    scene w2_3541 with dissolve
    fel "I take you for a man in the lone company of a young and beautiful woman."
    scene w2_3542 with dissolve
    fel "Then again, I guess she is single now. So no harm in trying, right?"
    scene w2_3543 with dissolve
    mina "Heh... shut up, Felicia."
    scene w2_3544 with dissolve
    fel "You'll get there."
    scene w2_3545 with dissolve
    fel "I'm going to leave now, before the instinct to take your cute ass on a shopping spree wins out over my wifely duty."
    scene w2_3546 with dissolve
    mina "Jeez, just get out of here, slut!"
    stop music fadeout 3.
    scene black with fade
    mina "You have stuff to do."
    fel "Okay, okay..."
    scene w2_3547 with fade
    "After another five minutes of yammering, Felicia finally departed and left the two of us alone in the middle of Mina's obnoxiously pink apartment."
    mina "Jeez, it's always one more thing with her."
    mc "Not the type to make a quick exit, huh?"
    mina "Yeah... I like that about Felicia."
    scene w2_3548 with dissolve
    mina "..."
    scene w2_3549 with dissolve
    mina "You don't have to stay if you don't want to. Felicia calling you wasn't my idea."
    scene w2_3550 with dissolve
    mina "I mean... you're kind of between a rock and a hard place."
    mina "Bros before hos, right?"
    scene w2_3551 with dissolve
    "She punctuated her little joke with an awkward chuckle that was more nervous energy than good humor."
    mc "Ah..."
    scene w2_3552 with dissolve

    if minaFlag == True:
        hide screen textbox2 with dissolve

        menu w2MinaTalk:
            "Attempt to gently assuage her concerns.":
                play music "music/soft-feeling.ogg"
                show screen textbox2 with dissolve
                mc "Yeah, I know... it's kind of weird, right? Considering how we're connected, but..."
                scene w2_3553 with dissolve
                "Mina transfixed me with an anxious, lonely look."
                "A look that told me all I needed to know about how she was feeling and what she hoped I would say."
                mc "It doesn't have to be like that."
                scene w2_3554 with dissolve
                mina "No...?"
                scene w2_3553 with dissolve
                mc "Of course not."
                mc "Bros before hos? Taking your social cues from how much two words rhyme is a dumbass thing to do."
                scene w2_3555 with dissolve
                mina "Aha... yeah... but I mean..."
                mina "We don't know each other all that well. I would understand."
                scene w2_3556 with dissolve
                mc "I would like to get to know you better."
                scene w2_3557 with dissolve
                "I tried my best to sound as matter-of-fact about it as I could."
                scene w2_3558 with dissolve
                mina "That simple?"
                scene w2_3557 with dissolve
                mc "It doesn't have to be so complicated. I mean, I'm already here."
                mc "Let's just hang out, easy peasy."
                mina "..."
                scene w2_3559 with dissolve
                mina "{b}Yeah{/b}, simple is good."
                scene w2_3560 with dissolve
                "......"
                scene w2_3561 with dissolve
                "..."
                scene w2_3562 with dissolve
                mina "Thanks, [mcf]."
                scene w2_3563 with dissolve
                mina "You can find friends in the funniest places."
                mina "I don't have many of those anymore."
                scene w2_3564 with dissolve
                hide screen textbox2 with dissolve

                menu:
                    "Hug her tighter.":
                        scene w2_3565 with dissolve
                        "I returned Mina's embrace. It only made sense."
                        mc "Heh. You get a lot of hugs growing up? Or not enough?"
                        scene w2_3568 with dissolve
                        mina "My dad."
                        scene w2_3567 with dissolve
                        mc "Oh yeah...?"
                        scene w2_3568 with dissolve
                        mina "Uhuh, he was real big on physical affection."
                        mina "He had the biggest arms."
                        scene w2_3566 with dissolve
                        "She trailed off in a dreamy, contented way..."
                        scene w2_3568 with dissolve
                        mina "I guess I get that from him, among other things..."
                        scene w2_3567 with dissolve
                        mc "What else?"
                        scene w2_3569 with dissolve
                        mina "Ah, well..."
                        mina "My hair, as you already know, and..."
                        scene w2_3570 with dissolve
                        mina "I definitely don't get my figure from my mom's side."
                        scene w2_3571 with dissolve
                        mina "Heh..."
                        mina "I know it's my fault, but stop looking, okay?"
                        scene w2_3572 with dissolve
                        mc "...sorry."
                        scene w2_3558 with dissolve
                        mina "So did you want a drink or something?"
                        scene w2_3557 with dissolve
                        mc "You don't have to play host right now. Let's do something fun."
                        mc "Are you feeling up to that?"
                        scene w2_3555 with dissolve
                        mina "I mean, put on the spot like that..."
                        scene w2_3573 with dissolve
                        "..."
                        scene w2_3574 with dissolve
                        mina "Okay, I got an idea..."
                    "Pat her head.":


                        $ w2MinaPat = True
                        show screen textbox2 with dissolve
                        "For an inexplicable reason, a particular urge came over me."
                        scene w2_3575 with dissolve
                        "...one whose origin might've lain somewhere earlier this week."
                        mc "No problem."
                        scene minalr_pat1_a with dissolve
                        show minalr_pat1
                        "With measured intensity to make sure I wasn't half-assing it, I placed my hand atop Mina's head and gave it a comforting pat."
                        "Her eyes only briefly conveyed confusion, before her expression slipped into one of warm acceptance."
                        mina "Eheh..."
                        "My fingers dug into the soft, flaxen bed of her hair; gently scratching the skin of her scalp."
                        mina "Hey... I'm not a dog..."
                        "Despite her words, she sounded relatively pacified by the touch."
                        scene minalr_pat2_a with dissolve
                        show minalr_pat2
                        mc "I know."
                        mina "....oooh, hey! That feels really nice."
                        "With added vigor, I attacked the side of her head, grazing my closely cut nails around the periphery of her ear, working the tips into the glossy golden depths."
                        mina "A-and oddly comforting, too."
                        mina "Simple... is good..."
                        "She murmured a snippet of our previous conversation as if it was a reassuring mantra."
                        mina "Simple is good."
                        scene w2_3576 with dissolve
                        mc "So, what do you want to do?"
                        mc "Would you like to bitch or would you prefer to get your mind off things?"
                        scene w2_3577 with dissolve
                        mina "I'll go with option two, please."
                        scene w2_3556 with dissolve
                        mc "You got anything you want to do? Anything fun?"
                        scene w2_3555 with dissolve
                        mina "Weeeeell..."
                        scene w2_3573 with dissolve
                        "..."
                        scene w2_3574 with dissolve
                        mina "Okay, I got an idea..."
            "Call her a moron.":


                play music "music/inner-light.ogg"
                scene w2_3578 with dissolve
                show screen textbox2 with dissolve
                mc "Don't be an idiot, moron."
                scene w2_3579 with dissolve
                mina "...h-huh?"
                scene w2_3578 with dissolve
                mc "I'm telling you not to say moronic things."
                "I opted to put it as emphatically as I possibly could, in an attempt to leave little room for doubt."
                mc "I'm here, standing in your garish apartment, aren't I? That should refute that dumb saying."
                scene w2_3581 with dissolve
                mina "..."
                scene w2_3580 with dissolve
                "She looked at me blankly, before..."
                mc "I. Want. To. Be--"
                scene w2_3582 with vpunch
                mina "Bwaaaaah!"
                "With surprising speed, Miss Congeniality almost knocked me off my feet."
                mina "I AM a big fuuucking moron!"
                mc "Uh... I didn't mean that..."
                scene w2_3583 with dissolve
                mina "I knew, deep down, it would always come to this, so why the hell am I feeling so bitter about it?"
                mina "I don't get it! I really, {b}really{/b} don't get it!"
                mina "I'm like my fucking MOOOOOOOOOM!"
                scene w2_3584 with dissolve
                "With surprising strength, the tearful blonde squeezed me tighter and tighter."
                mina "Now I'm crying into the shoulder of his friend of all people!"
                hide screen textbox2 with dissolve

                menu:
                    "Don't say anything, hold her tighter, and comfort her.":
                        scene minalr_cry_a with dissolve
                        show minalr_cry
                        show screen textbox2 with dissolve
                        "Instead of speaking, I turned the previously one-sided clinch into an embrace."
                        "Mina accepted the gesture, running her hands up my back and digging her nose deep into my chest."
                        mina "*Sniff... sniff...!*"
                        "A faint dampness spread across the center of my shirt, warmed by Mina's hot and muggy breath."
                        "The odd thought crossed my mind that Mina was very easy to hold, like a big stuffed animal."
                        "And even though it was physically impossible, as if being pulled by some invisible force, it felt like she was sinking deeper and deeper into me."
                        "There was something to be said for the comfort of dumb physical warmth."
                        "Yeah, just like I learned from my mom..."
                        "Words don't always suffice."
                        scene w2_3585 with dissolve
                        mina "Moron? Geez...!"
                        mina "You don't pull your punches, do you?"
                        mc "I meant that in a friendly, endearing way... like, \"Hey, you big moron!\"..."
                        scene w2_3586 with dissolve
                        scene w2_3587 with dissolve
                        scene w2_3588 with dissolve
                        mina "I mean I took it that way, but still...!"
                        scene w2_3589 with dissolve
                        mina "Heh. How does that song go?"
                        mina "Only fools fall in love?"
                        mc "I don't think I know that one."
                        scene w2_3590 with dissolve
                        mina "It's old..."
                        mina "My grandparents are old... so..."
                        scene w2_3591 with dissolve
                        mc "I see the connection."
                        scene w2_3592 with dissolve
                        mc "So, what do you want to do?"
                        mc "Would you like to let it out some more or do you want to get your mind off things?"
                        scene w2_3590 with dissolve
                        mina "Hmm... my problems will be here later. I don't see why we can't try and have some fun."
                        scene w2_3591 with dissolve
                        mc "You got anything you want to do?"
                        scene w2_3601 with dissolve
                        mina "Weeeeell..."
                        mina "There is something..."
                    "Break the hug and reassure her.":


                        scene w2_3593 with dissolve
                        show screen textbox2 with dissolve
                        mc "Hey, aforementioned {b}moron{/b}..."
                        scene w2_3594 with dissolve
                        mina "..."
                        "Mina's eyes looked up into mine, resembling reflective pools of water muddied with confusion."
                        scene w2_3593 with dissolve
                        mc "Crying into the shoulder of {i}your{/i} friend."
                        mc "...am I mistaken?"
                        scene w2_3594 with dissolve
                        "She just looked at me dumbly for a time, mouth slightly ajar, unsure of how to respond..."
                        "Maybe this route wasn't such a..."
                        scene w2_3595 with hpunch
                        mina "No! You're not mistaken!"
                        mina "I'm just... you know..."
                        scene w2_3596 with dissolve
                        mc "I know."
                        mc "Me? I'm always second-guessing and doubting people's motives. I can't turn it off."
                        scene w2_3597 with dissolve
                        mina "Really?"
                        scene w2_3599 with dissolve
                        mc "Yeah..."
                        scene w2_3598 with dissolve
                        mct "(You see in other people what you know of yourself, after all.)"
                        "...but I didn't say that much."
                        scene w2_3599 with dissolve
                        mc "So even without experiencing what you're going through, I understand the nagging feeling of uncertainty."
                        scene w2_3600 with dissolve
                        mc "So, you should get your mind off things."
                        scene w2_3589 with dissolve
                        mina "How do you propose I do that?"
                        mc "I don't know. Do you have something fun we can do here?"
                        scene w2_3601 with dissolve
                        mina "Well..."
                        mina "I can think of something."
    else:


        "Quite frankly, I'm only standing here because Felicia asked me to and Felicia is currently my job."
        "I turned her offer down to hang out weeks ago partially because I didn't want to be in the middle of Ian's \"love\" life."
        "Yet, I'm here, so..."
        mc "That's just a dumb saying. What kind of person would I be if I just let you stew here by your lonesome?"
        mc "Unless you want me to go...?"
        scene w2_3554 with dissolve
        mina "No, I said earlier I was cool with it... I was just giving you an out."
        scene w2_3555 with dissolve
        mina "This IS the first time we've spent one-on-one..."
        scene w2_3602 with dissolve
        mc "How considerate of you."
        scene w2_3603 with dissolve
        mina "Don't tease!"
        scene w2_3604 with dissolve
        mc "Relax, I'm here, aren't I? Let's do something fun to take your mind off Ian."
        scene w2_3605 with dissolve
        mc "What do you usually do for fun?"
        mina "Honestly, that's a hard question when you're put on the spot..."
        scene w2_3606 with dissolve
        mc "No, it's not. Go with your gut."
        scene w2_3607 with dissolve
        mina "Hmmm, okay! I do have something we can do..."


    scene black with fade
    stop music fadeout 3.0
    mina "Just don't complain when you get your ass kicked by a chick."
    "After a few seconds of rummaging in a drawer..."
    "Oh?"
    scene w2_3608 with fade
    mc "I didn't know you liked those kinds of games."
    "Mina held in her hand a copy of a fighting game. To be precise, it was a copy of {b}Royal Melee{/b}."
    scene w2_3609 with dissolve
    mina "Who doesn't like whacking someone with a sword?"
    scene w2_3608 with dissolve
    mc "You have a point. That one is pretty old though, isn't it?"
    scene w2_3610 with dissolve
    mina "So what? It's still as fun now as it was four years ago."
    scene w2_3611 with dissolve
    mina "You play a lot of games?"
    scene w2_3612 with dissolve
    mc "Used to..."
    scene w2_3613 with dissolve
    "How long has it been? It had been..."
    scene w2_3614 with dissolve
    mc "Not since my freshman year of high school. Me and--"
    scene w2_3615 with dissolve
    "I caught myself."
    scene w2_3614 with dissolve
    mc "I used to play them a lot growing up."
    scene w2_3613 with dissolve
    "It was probably best not to bring Ian up right now."
    scene w2_3616 with dissolve
    mina "What? You \"put your childish things away\" or something?"
    scene w2_3617 with dissolve
    mc "..."
    scene w2_3618 with dissolve
    mina "Oh my gosh! Really?"
    mc "...yes?"
    scene w2_3619 with dissolve
    mina "Pft, hahaha! That was just a guess!"
    mc "What's so funny?"
    mina "Nothing I guess, it's just... ah!"
    scene w2_3620 with dissolve
    mina "That's just such a childish mentality. Although, it fits you..."
    "That felt awfully accusatory and closer to the truth than I cared to admit."
    scene w2_3621 with dissolve
    mc "Yeah... probably could've crafted a diamond from inside my body with how much of a tight-ass I was back then."
    mina "From all the stories, I never had you pegged like that."
    mc "I've been known to be a wet blanket..."
    scene w2_3622 with dissolve
    mina "I never would've guessed."
    scene w2_3623 with dissolve
    mina "Here you go."
    scene w2_3624 with dissolve
    mina "......"
    "Mina, I was sure, was going through the motions."
    scene w2_3625 with dissolve
    play sound "sound effects/operating-system-sting.mp3"
    mc "..."
    scene w2_3626 with dissolve
    "I hoped I could help her genuinely have some fun."
    stop sound
    play music "music/training-in-fire.ogg"
    scene w2_3627 with pixellate
    fga "Select your character!"
    scene w2_3628 with dissolve
    "It didn't take long to go from the boot menu to the character select screen, where Mina instantly locked in her character."
    mc "I've never played this before. Who's good?"
    "..."
    $ renpy.music.set_volume(.3, 0, channel = "music")
    scene w2_3629 with pixellate
    "...she must not have heard me."
    $ renpy.music.set_volume(1, 1, channel = "music")
    hide screen textbox2 with dissolve
    scene w2_3630 with pixellate
    mc "I'll go with this guy. He looks cool."
    play sound "sound effects/thud-heavy.wav"
    scene w2_3631 with CropMove(0.25)
    with hpunch
    "Shit."
    mct "(Well, I don't know the buttons...)"
    play sound "sound effects/thud-heavy.wav"
    scene w2_3632 with cmet
    with vpunch
    mc "That was a cool combo. Maybe I'll try that guy."
    play sound "sound effects/thud-heavy.wav"
    scene w2_3633 with circlewipe2
    with hpunch
    mc "Ah... you made it look easy..."
    play sound "sound effects/big-explosion.mp3"
    scene w2_3634 with rush
    with hpunch
    "I managed to take a single round by randomly mashing, but..."
    play sound "sound effects/thud-heavy.wav"
    scene w2_3635 with wipedownfast
    with vpunch
    "She quickly adapted and took the match."
    $ renpy.music.set_volume(.3, 2, channel = "music")
    scene w2_3636 with pixellate
    mc "You must play a lot."
    scene w2_3637 with dissolve
    mina "Oh, yeah... maybe an hour a night."
    scene w2_3636 with dissolve
    mc "That's not as much as I..."
    scene w2_3638 with dissolve
    mina "For the last four years."
    scene w2_3639 with dissolve
    "Despite my best efforts to joke around with her, Mina had mostly delivered my ass reaming with a dejected look on her face."
    mct "(It was stupid to think something like this would take her mind off her problems, huh?)"
    scene w2_3640 with dissolve
    mina "..."
    scene w2_3641 with dissolve
    mina "Heh, he... hey, I warned you that you were about to get your ass kicked."
    scene w2_3642 with dissolve
    "A smile and a laugh that resembled any other I've seen her wear."
    scene w2_3641 with dissolve
    mina "Hehehe..."
    scene w2_3642 with dissolve
    "This time, I had the context to know it was utterly fake."
    "She was making an effort to entertain {i}me{/i}."
    scene w2_3643 with dissolve
    mc "You don't have to force yourself if you're not feeling it."
    scene w2_3644 with dissolve
    mina "...? I don't know what you mean, [mcf]."
    scene w2_3643 with dissolve
    mc "You don't notice it?"
    scene w2_3641 with dissolve
    mina "Let's play a few more games."
    $ renpy.music.set_volume(1, 1, channel = "music")
    scene w2_3645 with pixellate
    play sound "sound effects/metal-crash.mp3"
    with vpunch
    "It was utterly hopeless. Without fail, no matter how hard I tried..."
    scene w2_3646 with flash
    play sound "sound effects/thunder-crack.mp3"
    with hpunch
    "The end result was always the same."
    scene w2_3647 with dissolve
    fga "Player 1 Wins!"
    scene w2_3648 with dissolve
    pd "What did you expect? I'm the world's strongest hero!"
    stop music fadeout 2.0
    scene black with fade
    "......"
    "..."
    scene w2_3649 with circlewipe
    play music "music/inner-light.ogg"
    "After an hour or so, Mina and I went back to her room to enjoy a cup of coffee."
    "The conversation wasn't particularly lively, but she continued to make an effort."
    "The whole thing felt backward. I should be the one going out on a limb here. To that end..."
    hide screen textbox2 with dissolve

    menu:
        "Tease her about your losing streak.":

            scene w2_3650 with dissolve
            show screen textbox2 with dissolve
            mc "You couldn't let me win a single game, you bully?"
            scene w2_3651 with dissolve
            mina "It would've been pretty obvious if I threw one, right? Would you really have preferred that?"
            scene w2_3650 with dissolve
            mc "It'd make it worse if I knew, but I'm not very smart, I probably wouldn't have noticed."
            scene w2_3652 with dissolve
            mina "Heh..."
            mina "That reminds me of the time I played with Ian."
            scene w2_3653 with dissolve
            mc "Shit, sorry."
            "I reflexively apologized for inadvertently bringing the subject around to him."
            scene w2_3654 with dissolve
            mina "Why are you saying sorry? I was the one who picked the game."
            mina "You don't have to walk on eggshells. In fact, I'd prefer it if you didn't."
            scene w2_3650 with dissolve
            mc "Understood."
            scene w2_3655 with dissolve
            mc "...what reminded you?"
            scene w2_3656 with dissolve
            mina "Your complete and utter destruction."
            scene w2_3657 with dissolve
            mc "Oh, that?"
            scene w2_3658 with dissolve
            mc "You can be surprisingly sadistic."
            scene w2_3660 with dissolve
            mina "The second time Ian had ever stayed overnight at my place, we played a bunch of matches."
            scene w2_3661 with dissolve
            mina "I thought it would be a harmless way of earning some points with him. I know some guys like girls who play video games."
            scene w2_3662 with dissolve
            mc "Oh..."
            $ renpy.music.set_volume(.3, 3, channel = "music")
            scene w2_3667 with pixellate
            "I recalled playing games with Ian as a kid."
            scene w2_3668 with dissolve
            play sound "sound effects/thud-floor.mp3"
            scene w2_3669 with vpunch
            "He was the very picture of timid, but he didn't like losing at things he felt he was good at."
            scene w2_3670 with dissolve
            kil "Ah, this damn thing is broken!"
            $ renpy.music.set_volume(1, 1, channel = "music")
            scene w2_3657 with pixellate
            mc "I think I can see where this is going."
            scene w2_3671 with dissolve
            mina "Yeah, I could tell he was getting frustrated, so I lost on purpose."
            scene w2_3663 with dissolve
            mina "I could tell he knew. He didn't say anything, but he slowly got more and more upset about that as the matches went on."
            mina "I knew I made a mistake when he insisted we keep playing."
            scene w2_3664 with dissolve
            mc "You really shouldn't have to worry about his fragile ego. In my experience, he gets over it."
            scene w2_3663 with dissolve
            mina "No, I shouldn't, but I liked him."
            scene w2_3665 with dissolve
            mina "A week later, he wanted to play again and I learned my lesson. He didn't take a single round."
            scene w2_3666 with dissolve
            mina "We never played together again after that. A couple of months later, he admitted to me he practiced every night up to that point."
            scene w2_3672 with dissolve
            mina "We had a laugh about it."
            scene w2_3673 with dissolve
            "Mina smiled bittersweetly."
            scene w2_3674 with dissolve
            mina "I liked that memory, but now it feels a little stupid."
            scene w2_3675 with dissolve
            mc "Losing your shit over a video game doesn't seem like a good early impression to make in a fledgling romance."
            scene w2_3674 with dissolve
            mina "I mean it was childish, but also human."
            scene w2_3676 with dissolve
            mina "Very human and very authentic. Which I thought was a nice change of pace from my usual life up to that point."
            scene w2_3677 with dissolve
            "Very bittersweetly."
            scene w2_3678 with dissolve
            mc "We could've... played or done something else."
            scene w2_3679 with dissolve
            mina "Don't be silly. I'm not going to let a guy ruin something I've enjoyed for years."
            mina "I just brought that story up because I thought it was amusing."
            scene w2_3680 with dissolve
            mina "All in all, you're a more gracious {b}loser{/b}."
            scene w2_3681 with dissolve
            "She made a particular emphasis on the last part."
            mc "Thank you?"
            scene w2_3680 with dissolve
            mina "You are perfectly welcome, [mcf]."
            scene w2_3678 with dissolve
            mc "Oh, by the way!"

        "Ask her about her work." if w2MinaWorkQ == False:
            $ w2MinaWorkQ = True

            scene w2_3650 with dissolve
            show screen textbox2 with dissolve
            mc "How's work going?"
            if minaFlag == True:
                mc "Anything new with your TV gig?"
                scene w2_3652 with dissolve
                mina "Eh, not really. Just waiting on actually filming it."
            else:
                mc "I think you mentioned you got a role on TV?"
                scene w2_3651 with dissolve
                mina "Oh, yeah. I haven't actually filmed it yet though."

            scene w2_3650 with dissolve
            mc "You nervous about it?"
            scene w2_3652 with dissolve
            mina "Not yet. I'll be positively mortified the day of, but right now I'm feeling good about it."
            mina "Hopefully, it'll be like all the other times I've acted on stage."
            scene w2_3655 with dissolve
            mc "What do you mean?"
            scene w2_3660 with dissolve
            mina "Nervous to the point of puking leading up to it, but completely fine once you get in character."
            scene w2_3662 with dissolve
            mc "Does it really work like that?"
            scene w2_3661 with dissolve
            mina "In my experience. I don't know how to describe it. It's like entering a trance?"
            mina "It's like by the time the spotlight is on you, it's no longer in my hands."
            scene w2_3660 with dissolve

            if minaFlag == True:
                mina "It'll be all up to Elizabeth at that point."
            else:
                mina "It's all up to the character I'm playing."

            scene w2_3662 with dissolve
            mc "Like you're possessed?"
            scene w2_3682 with dissolve
            mina "No, of course not."
            scene w2_3683 with dissolve
            mina "...but also yes?"
            mina "I think athletes call it the zone."
            scene w2_3684 with dissolve
            mc "Oh! That actually came up in a psychology course I took as an elective. {b}Flow{/b}."
            mc "It's a mental state when you're fully immersed in a task. You're completely energized and focused."
            mc "You become so completely absorbed that it screws with your sense of time."
            scene w2_3685 with dissolve
            mina "Heh, that sounds just like it."
            scene w2_3663 with dissolve
            mina "It's modeling that currently helps pay the bills, though."
            scene w2_3664 with dissolve
            mc "Have you done any recently?"
            scene w2_3663 with dissolve
            mina "As a matter of fact, yes. Just yesterday."
            scene w2_3666 with dissolve
            mina "Some camping magazine. It wasn't very exciting; a lot of baggy clothes and hiking gear."
            mina "Not the most flattering of work or career-making, but that level of job is steady work... actually, I met Ian on a job like that."
            scene w2_3664 with dissolve
            mc "...oh yeah?"
            "I hadn't intended to go down this direction, but if she wanted to talk about Ian, I couldn't stop her."
            mc "Not every job is glamorous for photographers either I guess. Someone's got to take family portraits at the department store."
            scene w2_3686 with dissolve
            mina "That asshole likes to think he's better than that, but I've worked with real photographers. Let me tell you, they have a whole different energy and approach."
            scene w2_3687 with dissolve
            mc "I wouldn't know anything about it."
            "This week aside, I mean. I got no clue what makes a good photograph when it doesn't involve bare-ass nudity."
            scene w2_3688 with dissolve
            mina "Oh, yeah. He's good enough to get the occasional job, but he's so painfully mediocre. It's all spray and pray with him and uncreative shots."
            scene w2_3689 with dissolve
            mc "I guess you'd know a lot about it working as a model?"
            scene w2_3690 with dissolve
            mina "I take an interest. Knowing the other side of the camera helps when you're in front of it."
            scene w2_3686 with dissolve
            mina "...and he's kinda garbage!"
            scene w2_3689 with dissolve
            mc "I see..."
            scene w2_3691 with dissolve
            mina "Ah, I don't know why I'm bad-mouthing him to you..."
            scene w2_3692 with dissolve
            mc "You're pissed off and you have the right to be."
            scene w2_3691 with dissolve
            mina "Yeah, but I doubt you want to hear about it."
            scene w2_3692 with dissolve

            if minaFlag == True:
                mc "It's okay to vent. I don't mind."
                scene w2_3693 with dissolve
                mc "I promise none of this talk about his shoddy photography and inflated ego will get back to him."
            else:
                mc "It's a little awkward, but you're not telling me anything I don't know."
                scene w2_3693 with dissolve
                mc "Feel free to vent if you want, I don't mind."

            scene w2_3694 with dissolve
            mina "Ha, I shouldn't get started or I won't stop."
            scene w2_3695 with dissolve
            mina "I really, really won't stop."
            scene w2_3684 with dissolve
            mc "Oh, by the way!"


    scene w2_3696 with dissolve
    mc "...you know, I think you made quite the impression on Hana the other night."
    scene w2_3685 with dissolve
    "I decided to nudge the conversation away in a more positive direction."
    mina "Oh? Did I? What makes you say that?"
    scene w2_3684 with dissolve
    mc "She was the one who drove me over here. Maybe it was more like insisted?"
    mc "Either way, she was worried. She said you were really cool."
    scene w2_3685 with dissolve
    mina "Aw..."
    scene w2_3697 with dissolve
    mina "Tell her I feel the same."
    mina "To be honest, I felt like a dork next to her."
    scene w2_3698 with dissolve
    mc "Don't be absurd."
    scene w2_3697 with dissolve
    mina "It's not absurd, it's just I've lived a pretty sheltered life and she... hasn't."
    scene w2_3699 with dissolve
    mc "That's sheltered to you?"
    "I gestured toward the half-naked magazine cover adorning her wall."
    scene w2_3700 with dissolve
    mina "In a certain way... yes?"

    if minaFlag == True:
        mina "I went to an all-girls school, remember?"
        if w2MinaJulietQ == True:
            scene w2_3655 with dissolve
            mc "I remember you played Juliet, even though you wanted to play Mercutio."
            scene w2_3656 with dissolve
            mina "Ha! Good job remembering something from three days ago!"
            scene w2_3686 with dissolve
            mina "Fucking Ian, he never remembered jack, except when I was mad at him..."
            scene w2_3701 with dissolve
            mina "Then he remembered the smallest, sweetest, most meaningful things..."
            scene w2_3657 with dissolve
            mc "You were saying you're sheltered?"
            scene w2_3671 with dissolve
            "Another nudge."
            mina "Right yeah..."
            mina "For one, I went to an all-girls school where the student body was watched over like hawks. For two, at home, my mother..."
        else:
            scene w2_3666 with dissolve
            mina "They watched over us like hawks. There was also my mother..."
            scene w2_3664 with dissolve
            mc "What about her?"
    else:

        scene w2_3663 with dissolve
        mina "I don't know. Forget it."
        scene w2_3664 with dissolve
        mc "No, I'm genuinely curious."
        scene w2_3666 with dissolve
        mina "Well, for one I went to an all-girls school. They watched over us like hawks. There's was also my mother..."
        scene w2_3664 with dissolve
        mc "What about her?"

    scene w2_3674 with dissolve
    mina "She was traditional for a woman who's been divorced three times. A lot of rules and I was never one to break them..."
    mina "You always hear about people going crazy when they finally get let off the leash of their strict parents, but that never occurred to me."
    scene w2_3675 with dissolve
    mc "You're an adult now and you live on your own, though."
    scene w2_3679 with dissolve
    mina "Don't get me wrong, I'm definitely a lot more experimental. I try my best to have new experiences, but there's always a nagging voice in the back of my head stopping me from doing anything too crazy."
    scene w2_3678 with dissolve
    mc "What's your idea of {i}too{/b} crazy?"
    scene w2_3702 with dissolve
    mina "Come on, don't ask me that. You're just setting me up to be made fun of."
    scene w2_3703 with dissolve
    mc "Put some faith in me that I'm not."
    scene w2_3704 with dissolve
    mina "..."

    if minaFlag == True:
        scene w2_3705 with dissolve
        mina "Maybe I'll tell you later."
        scene w2_3704 with dissolve
        mc "Why later? Why not now?"
        scene w2_3706 with dissolve
        mina "I've got to think about it."
        scene w2_3678 with dissolve
        "An odd answer, but no point in pushing it."
        scene w2_3679 with dissolve
        mina "Anyway..."
    else:


        scene w2_3706 with dissolve
        mina "Ah, the usual stuff... sex and drugs..."
        mina "Sky diving."
        scene w2_3678 with dissolve
        mc "Oh, yeah! The usual stuff. Throwing yourself out of a plane!"
        scene w2_3707 with dissolve
        mina "Hey, you said you wouldn't make fun of me!"
        mc "Sorry, I didn't mean to. I guess that might qualify as too crazy."
        scene w2_3706 with dissolve
        mina "Uh, huh. Yeah... so, anyway..."


    scene w2_3678 with dissolve
    "Mina deliberately directed the conversation elsewhere."
    mc "Yeah, anyway..."
    hide screen textbox2 with dissolve

    menu:
        "Relay your own experiences on the subject.":

            show screen textbox2 with dissolve
            mc "I had pretty loose reins growing up. That's probably the main reason I never wanted to party or experiment."
            mc "It's push and pull when it comes to parents and their children I guess."
            scene w2_3708 with dissolve
            mina "The stories I've heard make that a little hard to believe."
            mc "I guess I just got it out of my system before I became old enough to be interested in that stuff."
            scene w2_3709 with dissolve
            mina "About that... I'm a little curious."

            if history_firestarter == True:
                mina "Did you really burn down your neighbor's shed?"
                mc "I did."
                mina "...{b}why?{/b}"

                if trait_inquisitive == True:
                    scene w2_3710 with pixellate
                    mc "I... just wanted to see it burn."
                    mina "That's it? Just for that reason?"
                    mc "It wasn't very smart."
                    mc "I wanted to see what would happen and I had... very poor impulse control."
                    scene w2_3713 with dissolve
                    mina "That should've been obvious, even to a kid."
                    scene w2_3714 with dissolve
                    mc "Sure, it'd burn to the ground if no one did anything, but I wanted to see how."
                    mc "How fast it'd spread, what part would weaken and collapse fist. How hot it'd be standing near it..."
                    scene w2_3713 with dissolve
                    mina "Well, was it fun?"
                elif trait_tireless == True:
                    scene w2_3712 with pixellate
                    mc "I was... bored one night."
                    mina "That's it? Just for that reason?"
                    mc "It wasn't very smart."
                    mc "I had nothing to do and poor impulse control."
                    scene w2_3715 with dissolve
                    mina "That's so... {b}wow{/b}!"
                    "Mina looked truly confounded by the trifling reason."
                    scene w2_3713 with dissolve
                    mina "Well... what did it feel like? Was it fun at least?"
                else:
                    scene w2_3711 with pixellate
                    mc "I... had anger problems and the guy was kind of a dick to my mom."
                    mina "You did it for revenge?"
                    mc "There wasn't that much thought behind it. It would probably be more accurate to say I did it for my own gratification."
                    mina "Well, I guess at least he wasn't very nice."
                    mc "In retrospect, he actually wasn't even that big of a dick."
                    scene w2_3716 with dissolve
                    mina "Pft, for real?"
                    mc "Yeah..."
                    mc "I wasn't very smart and had poor impulse control."
                    scene w2_3717 with dissolve
                    mina "Huh..."
                    "She looked at me with an unasked question on her lips."
                    scene w2_3714 with dissolve
                    mc "What?"
                    scene w2_3713 with dissolve
                    mina "I just wanted to know... what did it feel like? Was it fun?"

                scene w2_3714 with dissolve
                mc "No, I fucked up big time."
                scene w2_3715 with dissolve
                mina "I didn't ask if it was worth it. I asked if it was exhilarating at the time?"
                "The spark of curiosity was evident on her face, causing me to genuinely weigh my answer before giving it."
                scene w2_3718 with dissolve
                mc "...yeah, at the time, it was very exciting."
                mc "The hairs on my arms were standing on end. My whole body was jittery."
                mc "The warmth of it was comforting and the fire made for a very pretty sight in the winter night."
                scene w2_3719 with dissolve
                mc "...shit, that makes me sound like a psycho, huh?"
                scene w2_3720 with dissolve
                mina "A liiiittle bit, but I get it."
                scene w2_3719 with dissolve
                mc "I find that hard to believe."
                scene w2_3721 with dissolve
                mina "I think everyone wants to see things crumble sometimes."
                mina "It's like when you're driving and you think {i}if I turned my wheel only just a little bit, all those people on the sidewalk would just disappear{i}..."
                scene w2_3722 with dissolve
                mc "There's a term for that. Call of the void."
                scene w2_3723 with dissolve
                mina "Of course you'd know that."
                scene w2_3724 with dissolve
                mc "What's that supposed to mean?"
                scene w2_3731 with dissolve
                mina "Oh, nothing!"
                scene w2_3725 with dissolve
                mina "{size=-10}Weirdo...{/size=-10}"
                scene w2_3724 with dissolve
                "Mina cutely mumbled under her breath, which made the tongue-in-cheek insult oddly endearing."

            elif history_voyeur == True:
                mina "Did you really take creep shots of all the moms in your neighborhood?"
                mc "It wasn't ALL the moms, but... yeah, I did."
                mina "...{b}why?{/b} Because of puberty?"

                if trait_inquisitive == True:
                    scene w2_3726 with pixellate
                    mc "That was a large part of it."
                    mc "It wasn't very smart. I shared them around. Naturally, it would end up catching back up to me and I knew that."
                    mina "What drove you to do it then?"
                    mc "I guess I was just curious to see what everyone's beloved mother looked like underneath their clothes."
                    scene w2_3715 with dissolve
                    mina "Jeez!"

                elif trait_tireless == True:
                    scene w2_3726 with pixellate
                    mc "That was part of it, but I was also bored and wanted pocket change."
                    mina "Oh, yeah! You sold them, right?"
                    mc "I blame the influence of our consumer-driven culture."
                    mina "Right... very funny!"
                    mc "It wasn't very smart. I shared them around. Naturally, it would end up catching back up to me and I knew that."
                    scene w2_3713 with dissolve
                    mina "If you knew you'd eventually get caught, why'd you do it then?"
                    scene w2_3714 with dissolve
                    mc "I guess I was just excited to see what everyone's beloved mother looked like underneath their clothes."
                    scene w2_3715 with dissolve
                    mina "Jeez!"
                else:
                    scene w2_3726 with pixellate
                    mc "That was part of it, but I mainly wanted to get back at them for snubbing my mom one too many times."
                    mina "What, really? You did it for revenge?"
                    mc "I guess. Despite all the work it took to get the photos, the idea itself was pretty impulsive."
                    mc "I wasn't a very smart kid; I shared them around. Naturally, it would end up catching back up to me and I knew that."
                    scene w2_3713 with dissolve
                    mina "If you knew it was dumb, why do it?"
                    scene w2_3714 with dissolve
                    mc "I guess I just wanted to see what those stuck-up bitches looked like under their clothes and humiliate them while doing it."
                    scene w2_3715 with dissolve
                    mina "Jeez!"

                scene w2_3727 with dissolve
                mina "...what did they look like?"
                scene w2_3728 with dissolve
                mc "I mean..."
                mc "That's a weird thing to ask. You want me to describe them one by one?"
                scene w2_3727 with dissolve
                mina "Of course not, I..."
                scene w2_3729 with dissolve
                mc "They looked like you'd expect a naked, older woman to look. They all had their hands, fingers, and toes."
                mc "Some were fitter and prettier than others and some were more on the flabby side, but each of them was beautiful in their own way."
                scene w2_3715 with dissolve
                mina "Was it fun spying on them?"
                scene w2_3720 with dissolve
                "The spark of curiosity was evident on her face, causing me to genuinely weigh my answer before giving it."
                scene w2_3719 with dissolve
                mc "...yeah, it was--"
                scene w2_3720 with dissolve
                mina "Exciting? Exhilarating?"
                scene w2_3718 with dissolve
                mc "All of the above and more."
                mc "I discovered for myself that there's an odd, misplaced sense of power to voyeurism."
                scene w2_3720 with dissolve
                mina "Explain."
                scene w2_3730 with dissolve
                mc "You have an advantage for one. To see, without being seen - like God looking down on the world."
                mc "That's being hugely melodramatic, but you get the point right?"
                scene w2_3720 with dissolve
                mina "Yeah, I can... imagine..."
                scene w2_3719 with dissolve
                mc "This all probably makes me sound like a psycho."
                scene w2_3731 with dissolve
                mina "Maybe a liiiiitle, but I get it."
                scene w2_3732 with dissolve
                mc "You do? Did you want to see what all the neighborhood DILFs were packing in their jean shorts?"
                scene w2_3731 with dissolve
                mina "No... I'm a curious gal is all."
                scene w2_3725 with dissolve
                mina "{size=-10}...but also some of them.{/size=-10}"
                scene w2_3724 with dissolve
                "Mina cutely mumbled under her breath an odd and endearing admission."
            else:

                mina "Did you really steal money from your school?"
                mc "No... I stole money from people under the pretense it was going to the school."
                mina "Why? Did you need the money?"
                scene w2_3719 with dissolve
                mc "Well, my mom wasn't rich, but... no. It wasn't plain greed either."
                scene w2_3720 with dissolve
                mina "Why did you do it then?"
                scene w2_3730 with dissolve
                mc "Well..."
                scene w2_3733 with pixellate

                if trait_inquisitive == True:
                    mc "I wanted to see if I could get away with it."
                    mina "That's it?"
                elif trait_tireless == True:
                    mc "I got bored and wanted to see if I could do it and get away with it."
                    mina "That's it? You stole people's money because you got bored?"
                    mc "Yeah, it was really shitty. I want to chalk it up to being a kid, but my actions are my own."
                else:
                    mc "It's hard to explain. I was an angry kid and I acted out a lot."
                    mina "You stole people's money because you were angry?"
                    mc "It sounds really stupid, I know, but I don't mean it as a justification. That's just the place my actions came from."

                mc "You always see heists in movies, I guess I wanted to see if I could do my own and get away with it."
                mc "Turns out... no, I couldn't. I wasn't as smart as I thought I was."
                scene w2_3715 with dissolve
                mina "Heh, a heist?"
                mina "I got to admit that does make it sound fun."
                scene w2_3716 with dissolve
                mc "It's a preeeetty grandiose term for fraudulently selling chocolate bars."
                mina "Pfft, yeah, but to a kid, I could see it looking like that."
                scene w2_3731 with dissolve
                mina "Was stealing fun?"
                scene w2_3732 with dissolve
                mc "No, I fucked up big time."
                scene w2_3731 with dissolve
                mina "I didn't ask if it was worth it. I asked if it was exhilarating at the time?"
                scene w2_3732 with dissolve
                "The spark of curiosity was evident on her face, causing me to genuinely weigh my answer before giving it."
                scene w2_3730 with dissolve
                mc "Scheming was exciting. Executing it was all butterflies, but the rush that came after a sale..."
                scene w2_3718 with dissolve
                mc "Yeah, I guess it was fun breaking bad."
                scene w2_3713 with dissolve
                mina "I see..."
                scene w2_3724 with dissolve
                mc "Why? You want to rob a bank? You'd have to be the getaway driver on account that I have neither a car nor license."
                scene w2_3716 with dissolve
                mina "Heh. I don't think I'd make a good one either. My car's too recognizable."
                mc "Let's come back to the idea later once our wheels situation has changed then."
                mina "It's a promise."

            scene w2_3734 with dissolve
            mina "So you and I can partially blame how we turned out on our mothers?"
            mc "I think that goes for a lot of people, even if they don't like to admit it."
            scene w2_3735 with dissolve
            mina "Some people love, love, LOVE pointing their fingers there; Ian, for example."
            mina "He loves blaming his parents for him turning out a complete and giant douchebag."
            mc "That's a complica--"
            scene w2_3736 with dissolve
            mina "It's not complicated. He's just a fucking brat."
            mina "He acts like not seeing his parents as much as other kids excuses him for doing whatever the hell he pleases. Like they're the reason he half-asses everything and can't take anything seriously."
            scene w2_3737 with dissolve
            "A rare glimpse of Mina tossing out her friendly persona and baring her teeth."
            scene w2_3736 with dissolve
            mina "I'd be more sympathetic if he wasn't so damn whiny about it."
            scene w2_3738 with dissolve
            mc "Tell me how you really feel."
            scene w2_3739 with dissolve
            mina "Ah - s-shoot. I must sound like a bitch."
            scene w2_3740 with dissolve
            mc "You sound like someone who just got cheated on."
            scene w2_3739 with dissolve
            mina "I'm just angry. Don't listen to me."
            scene w2_3740 with dissolve
            mc "That's bound to happen when you keep it all in. You've been pretty reserved today, all things considered."
            scene w2_3741 with dissolve
            mina "Yeah, but you don't want to hear it."

        "Switch topics and ask about work." if w2MinaWorkQ == False:

            show screen textbox2 with dissolve
            mc "How's work going?"
            scene w2_3679 with dissolve
            mina "Work...?"
            scene w2_3708 with dissolve
            mina "What about it?"
            if minaFlag == True:
                mc "Anything new with your TV gig?"
                mina "Eh, not really. Just waiting on actually filming it."
            else:
                mc "I think you mentioned you got a role on TV?"
                mina "Oh, yeah. I haven't actually filmed it yet though."

            mc "You nervous about it?"
            mina "Hmm..."
            scene w2_3743 with dissolve
            mina "Not yet. I'll be positively mortified the day of, but right now I'm feeling good about it."
            mina "Hopefully, it'll be like all the times I've acted on stage."
            scene w2_3744 with dissolve
            mc "What do you mean?"
            scene w2_3743 with dissolve
            mina "Nervous to the point of puking leading up to it, but completely fine once you get in character."
            scene w2_3744 with dissolve
            mc "Does it really work like that?"
            scene w2_3731 with dissolve
            mina "In my experience. I don't know how to describe it. It's like entering a trance?"
            mina "It's like by the time the spotlight is on you, it's no longer in my hands."
            scene w2_3723 with dissolve

            if minaFlag == True:
                mina "It'll be all up to Elizabeth at that point."
            else:
                mina "It's all up to the character I'm playing."

            scene w2_3724 with dissolve
            mc "Like you're possessed?"
            scene w2_3725 with dissolve
            mina "No, of course not."
            scene w2_3745 with dissolve
            mina "...but also yes?"
            mina "I think athletes call it the zone."
            scene w2_3746 with dissolve
            mc "Oh! That actually came up in a psychology course I took as an elective. {b}Flow{/b}."
            mc "It's a mental state when you're fully immersed in a task. You're completely energized and focused."
            scene w2_3730 with dissolve
            mc "You become so completely absorbed that it screws with your sense of time."
            scene w2_3713 with dissolve
            mina "Heh, that sounds just like it."
            mina "It's modeling that currently helps pay the bills, though."
            scene w2_3714 with dissolve
            mc "Have you done any jobs recently?"
            scene w2_3747 with dissolve
            mina "As a matter of fact, yes. Just yesterday."
            mina "Some camping magazine. It wasn't very exciting; a lot of baggy clothes and hiking gear."
            mina "Not the most flattering of work or career-making, but that level of job is steady work... actually, I met Ian on a job like that."
            scene w2_3714 with dissolve
            mc "...oh yeah?"
            "Naturally, the conversation yet again turned to Ian."
            scene w2_3747 with dissolve
            mc "Not every job is glamorous for photographers either I guess. Someone's got to take family portraits at the department store."
            scene w2_3748 with dissolve
            mina "That asshole likes to think he's better than that, but I've worked with real photographers. Let me tell you, they have a whole different energy and approach."
            mc "I couldn't tell you the difference between a bad and a good one."
            "This week aside, I mean. I got no clue what makes a good photograph when it doesn't involve nudity."
            scene w2_3749 with dissolve
            mina "Oh, you definitely could. I think everyone knows what a bad or an outstanding photo looks like."
            mina "It's harder to tell the difference between a mediocre one and a pretty good one, which is where that prick lies."
            mina "Oh, yeah. He's good enough to get the occasional job, but he's so unremarkable. It's all spray and pray with him and uncreative shots."
            mc "I guess you'd know a lot about it working as a model?"
            scene w2_3736 with dissolve
            mina "I take an interest. Knowing the other side of the camera helps when you're in front of it."
            scene w2_3742 with dissolve
            mc "I see..."
            scene w2_3739 with dissolve
            mina "Ah, I don't know why I'm bad-mouthing him to you..."
            scene w2_3740 with dissolve
            mc "Duh, you're pissed off. You have the right to be."
            scene w2_3741 with dissolve
            mina "Yeah, but you don't want to hear it."
        "Move the conversation back to the subject of school.":


            show screen textbox2 with dissolve
            mc "Did you like going to a girl's boarding school?"
            "I decided to pick up a recent conversational marker."
            scene w2_3708 with dissolve
            mina "Eh."
            mina "There was good and bad. In terms of living and learning, I think few things in life are truly without an upside."
            mc "That is..."
            mc "That is true, I think. You've got a positive way of looking at things."
            scene w2_3743 with dissolve
            mina "Well, I try to be optimistic. It can be hard sometimes, but \"a girl should never frown\", after all."
            scene w2_3744 with dissolve
            mc "What kind of backward thinking is that?"
            scene w2_3750 with dissolve
            mina "Just something that was drilled into my head growing up."
            scene w2_3753 with dissolve
            "...that's fucked."
            scene w2_3752 with dissolve
            mc "...so was school more good or bad?"
            scene w2_3750 with dissolve
            mina "It's hard to say. It's not like I've tallied it up."
            scene w2_3751 with dissolve
            mina "It did help shape me to become the person standing here; not that I love everything about myself, but I don't hate who I am either."
            scene w2_3752 with dissolve
            mc "That is a {b}painfully{/b} lukewarm appraisal of your past."
            scene w2_3750 with dissolve
            mina "It's a fair one. Everyone's got something they want to change about themselves."
            scene w2_3752 with dissolve
            mc "That's... also true."
            scene w2_3751 with dissolve
            mina "What would you change about yourself, [mcf]?"
            scene w2_3753 with dissolve
            "The answer to that question wasn't something I needed to arrive at. It was something I'd long since been at an impasse with."
            scene w2_3752 with dissolve
            mc "I'd like to be more... {i}normal{/i}."
            scene w2_3754 with dissolve
            mina "Define normal."
            scene w2_3755 with dissolve
            mc "I know. Not being \"normal\" is the source of everyone's societal woe, isn't it?"
            scene w2_3756 with dissolve
            mina "..."
            scene w2_3757 with dissolve
            mina "What's abnormal about you?"
            scene w2_3719 with dissolve
            mc "My thoughts and feelings aren't always polite."
            scene w2_3720 with dissolve
            "That was as tactful as I could put it."
            scene w2_3730 with dissolve
            mc "Sometimes I feel a pull to do stuff that isn't... acceptable."
            scene w2_3725 with dissolve
            mina "Who's being lukewarm now? You can just admit sometimes you want to punch somebody."
            scene w2_3731 with dissolve
            mina "I get that angry too. Sometimes there's not even a good reason either."
            scene w2_3732 with dissolve
            mc "You're half-right. Sometimes I do want to punch some annoying asshole in the face, but it's not always out of anger."
            scene w2_3745 with dissolve
            mina "Is it similar to when you're standing someplace high and you think to yourself \"I could just jump\"? Or when..."
            scene w2_3758 with dissolve
            mina "...or when some overly familiar jerk who can't take a hint is so preoccupied with talking that you just think \"I could mash his face into the table before he even knows what I'm doing\"...?"
            scene w2_3759 with dissolve
            mc "Uh..."
            scene w2_3760 with dissolve
            mina "Y-you'd never do it of course, but the thought crosses your mind..."
            mc "It's not quite that either."
            scene w2_3761 with dissolve
            mina "Okay then, just tell me before I expose myself any further by guessing."
            mc "Well, I'm..."
            "I was finding it difficult to come up with an exit strategy from this line of conversation."
            scene w2_3762 with dissolve
            mina "Oooooh! I got it! It's fun?"
            mina "If it's not anger or morbid curiosity, it's gotta be because it's exciting, right?"
            scene w2_3732 with dissolve
            mc "That's a pretty good way of putting it."
            scene w2_3731 with dissolve
            mina "That's not so bad. People like boxing and MMA, right?"
            mina "Is that why you and Ian got into a lot of fights?"
            scene w2_3732 with dissolve
            mc "It wasn't the reason, but it did help me to better know myself."
            "I wasn't really talking about fighting specifically, but it was better this way."
            scene w2_3764 with dissolve
            mina "*sigh* I kind of wish I could've seen what he was like as a kid."
            scene w2_3765 with dissolve
            mina "Might help me understand what goes through that jerkass' rotten brain. He uses his childhood as a crutch, to excuse all his laziness and failures."
            mina "He blames all of his damn problems on his parents and being picked on, but I've got to be honest..."
            scene w2_3736 with dissolve
            mina "He just comes off as a whiny, entitled baby most of the time."
            scene w2_3737 with dissolve
            "Her usual gleeful and cheery pretense was nowhere to be found. Instead, it had an understandably genuine ire to it."
            scene w2_3763 with dissolve
            mc "Ian... well..."
            scene w2_3737 with dissolve
            "To me, Ian was like a poor person that won the lottery; mentally unequipped to do anything but go broke and squander the fortune that landed in their lap."
            "In my friend's case, he was an unpopular kid at heart who found recognition once he hit his growth spurt. All his personal hang-ups lurked beneath the surface, rotting and poisoning the good things in his life like Mina."
            scene w2_3742 with dissolve
            mc "You know him better than I do in some regards. We've never really talked to each other about feelings."
            scene w2_3739 with dissolve
            mina "Crap, I probably just came off as a complete bitch."
            scene w2_3740 with dissolve
            mc "No, it's... COMPLETELY understandable."
            mc "You're pissed off and have the right to be."
            scene w2_3741 with dissolve
            mina "Yeah, but you don't really want to hear it."


    scene w2_3742 with dissolve
    "Actually..."
    hide screen textbox2 with dissolve

    menu:
        "Tell her it's cool for her to vent.":
            $ w2MinaFlagVent = True
            show screen textbox2 with dissolve
            scene w2_3766 with dissolve
            mc "I don't mind you venting. I bet you have a lot of shit to unpack."
            scene w2_3769 with dissolve
            mina "It feels... weird."
            scene w2_3768 with dissolve
            mc "Are you worried about anything you say getting back to him?"
            scene w2_3769 with dissolve
            mina "Of course not. After what he did, like I give a crap about his feelings."
            scene w2_3767 with dissolve
            "Honestly, Mina hadn't even appropriately reacted tonight, let alone overreacted."
            mct "(She's a very odd person...)"
            scene w2_3768 with dissolve
            mc "So {b}yes{/b}, I do want to hear it."
        "Don't focus on the negativity. Try to take her mind off things."(chg=["maid"]):


            show screen textbox2 with dissolve
            scene w2_3766 with dissolve
            mc "I don't mind you venting. That'd be completely normal."
            scene w2_3767 with dissolve
            "Honestly, Mina hadn't even appropriately reacted tonight, let alone overreacted."
            mct "(She's a very odd person...)"
            scene w2_3768 with dissolve
            mc "...but I feel like I should help take your mind off things instead."

    if minaFlag == True:
        jump w2MinaRevealFlag
    else:
        jump w2MinaRevealNotFlag


label w2MinaRevealFlag:

    scene w2_3769 with dissolve
    mina "That so? Alright..."

    if w2MinaFlagVent == True:
        mina "If you really want to help me let off steam..."
    else:
        mina "If you want to distract me..."

    scene w2_3770 with dissolve
    "With weighted shoulders, Mina flopped down onto her bed like a dropped sack of potatoes."
    stop music
    play sound "sound effects/thud-floor.mp3"
    scene w2_3771 with vpunch
    mina "How are you at giving massages? My body's so tense I feel like I might explode."
    scene w2_3772 with dissolve
    mc "Pick your poison: foot, shoulder, or back?"
    scene w2_3773 with dissolve
    mina "So I get to choose? Lucky me."
    play music "music/anacaptainslogue.ogg"
    scene w2_3774 with dissolve
    "Mina extended her leg, weakly raising it into the air and proffering her foot for attention."
    mina "Okay... how are you at giving {b}foot{/b} massages?"
    scene w2_3775 with dissolve
    mc "Inexperienced, but willing to learn."
    scene w2_3776 with dissolve
    "Without delay, I made my way over to the bed and took ahold of the weary-looking blonde's feet."
    mina "Oooh~ your hands are so warm."
    scene w2_3777 with dissolve
    mc "That's because your feet are like ice."
    "Like the rest of her, the skin on the bottom of her feet was shockingly soft. I had always thought the word \"delicate\" was an odd way to describe a person's extremities, but the adjective fit Mina's feet down to a tee."
    "They were small and pale to the point of looking anemic, free of blemish and ending in five dainty points polished in an eye-catching shade of red."
    scene w2_3778 with dissolve
    mina "You're not a foot fetishist, right?"
    scene w2_3777 with dissolve
    mc "This was your idea."
    scene w2_3779 with dissolve
    mina "Yeah, but you could've just got lucky."
    scene minafeet1_a with dissolve
    show minafeet1
    mc "How's this?"
    "With the ball of my thumb, I began to gently knead the arch of her foot."
    mina "It kinda tickles."
    mc "Sorry, I don't know how to make it not-"
    mina "No, it's a pleasant kind of ticklish."
    "The smile on her lips was slight, but warm and reaffirming."
    scene minafeet2_a with dissolve
    show minafeet2
    "With a bit more confidence, I gradually made full use of my hands, working the length of my thumb up her sole and into the ball of her foot."
    mina "That's nice..."
    "...but as the massage progressed, without a topic of conversation, so did the gaps of silence."
    "Mina looked relatively relaxed, but the lull in conversation made me aware of the innate intimacy of the shared act."

    if w2MinaFlagVent == True:
        mc "I was serious. I really don't care if you want to vent."
        mina "I know, but I think I got my cursing done earlier with Felicia..."
        mc "Ah, yeah..."
    else:

        "I wracked my brain for a topic of conversation, but everything seemed so frivolous. Earlier, I had wanted to make her laugh, but..."
        "How the heck do you make someone laugh on purpose?"
        mc "(...fuck if I know.)"

    "The awkwardness persisted."
    mct "(Might as well put all my focus on the task at hand...)"
    scene minafeet3_a with dissolve
    show minafeet3
    "If a conversation wasn't fruitful, I would give the best damn amateur foot massage a twenty-two year old hopeful medical student could give to his disloyal best friend's spurned lover."
    mina "You're doing a good job, [mcf]. You have a very pleasant touch."
    mc "You sound surprised."
    mina "A little."
    mc "Ha! Me too!"
    "My attention was mostly preoccupied with applying the right amount of pressure. Not too gentle, but not too rough either. For some reason, I had it in my head that a good massage needed to be firm."
    "With that in mind, I put most of my focus on working the metatarsals of her foot, using my thumb to drive out tension from her flexor muscles."
    mc "I'm surprised you're enjoying it to be honest. You look like someone who gets a lot of massages."
    scene w2_3782 with dissolve
    mina "That's a nice way of calling me spoiled and soft."
    scene w2_3780 with dissolve
    mc "Oh, you could tell?"
    scene w2_3781 with dissolve
    mina "Of course. Saying one thing and meaning something else is an essential skill in my little bubble."
    scene w2_3780 with dissolve
    mc "Was I being presumptuous?"
    scene w2_3782 with dissolve
    mina "Yes... but it annoys me you're not wrong. My aunt owns a chain of massage places."
    mina "I get a free one every week."
    scene w2_3780 with dissolve
    mc "That's a lot of massages. So this is like me trying to impress a Michelin star chef?"
    scene w2_3781 with dissolve
    mina "Oooh, are you trying to impress me? Was Felicia right to warn you off?"
    scene w2_3787 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Tell her you simply like doing a good job.":
            scene w2_3788 with dissolve
            show screen textbox2 with dissolve
            mc "I try to do a good job with everything I do."
            scene w2_3787 with dissolve
            mina "Well, don't worry about it. You're doing fine."
            scene w2_3786 with dissolve
            mina "I'm easily satisfied, otherwise I wouldn't be so damn complacent, would I?"
            scene w2_3785 with dissolve
            "Mina's expression took a sharp turn."
            scene w2_3786 with dissolve
            mina "S-sorry, you didn't say anything wrong."
            mina "I'm just mad at myself. My head is making all sorts of dumb connections right now."
            scene w2_3785 with dissolve
            mc "I understand."
            scene minafeet3_a with dissolve
            show minafeet3
            mc "Just turn your brain off and enjoy."
        "Tease her.":
            scene w2_3788 with dissolve
            show screen textbox2 with dissolve
            mc "Maybe she has a good instinct for these things."
            scene w2_3787 with dissolve
            "With a straight face, I let drop an ambiguous answer and waited for Mina to draw her own wild conclusion."
            scene w2_3783 with dissolve
            mina "......"
            mina "..."
            scene w2_3784 with dissolve
            "Instead of getting flustered, she just weakly smiled and left it at that."
            scene minafeet3_a with dissolve
            show minafeet3
            "Thus the brief conversation receded once more into shared contemplation."

    "For the next while, Mina shut her eyes and let her mind drift elsewhere."
    "All that occupied my ears was the hum of Mina's apartment and the soft, comforted coos of a woman being massaged."
    mct "(Fuck, Ian really did her dirty...)"

    if Killian_Bromance >= 20:
        "I like the guy, but..."

    mct "(What an absolute moron. I guess he and Mina are through?)"
    mct "(Should I try and give him a heads-up about what Mina found?)"
    mct "(Would that be fair to Mina?)"
    mct "(Then again, why should I even involve myself any further than I have to?)"
    "All sorts of thoughts percolated inside my head, but no answer filtered through..."
    "Eventually, one extra sound was added to the mix: the soft, muffled sound of Mina sleeping."
    scene w2_3789 with dissolve
    mina "Efewee~"
    "It was a pleasant sound."
    scene w2_3790 with dissolve
    mc "Hmm..."
    scene black with fade
    "A quick search yielded a blanket."
    scene w2_3791 with dissolve
    mct "(There. That completes the picture.)"
    "More so than her usual manufactured presentation, she looked positively beautiful when at ease like this."
    "Which meant something, considering that usual self was extremely cute to begin with."
    scene black with fade
    stop music fadeout 3.0
    mct "(Boy, did I feel completely useless today.)"
    "Still, I remained."
    scene w2_3792 with circlewipe
    "It didn't feel right leaving while she was asleep and I didn't want to wake her up. Plus, I had time to kill until I had to be at Felicia's."
    "So I spent my idle time the best way my generation knows how..."
    "Browsing the web and texting."
    "I didn't explicitly fill Hana in on the details, but considering she gave me a ride, I felt obliged to let her know everything was fine."
    scene w2_3793 with dissolve
    hide screen textbox2 with dissolve
    call phone_start_hana from _call_phone_start_hana
    call phone_after_menu from _call_phone_after_menu_16
    call message_start ("[mcf]", "Thanks again for the ride.") from _call_message_start_23
    call message ("Hana", "Is Blondie okay???") from _call_message_68
    call reply_message ("Yes. It's about what you'd expect. She fell asleep, so I'm just going to hang out here for a while.") from _call_reply_message_23
    call message ("Hana", "Are you two that close?") from _call_message_69
    call reply_message ("Not exactly, but a mutual friend pulled me into this.") from _call_reply_message_24
    call message ("Hana", "Well, I'm glad you're there.") from _call_message_70
    call reply_message ("Did she really make that big of an impression on you?") from _call_reply_message_25
    call message ("Hana", "Yeah, it's weird. I've never met anyone like her.") from _call_message_71
    call reply_message ("What do you mean by that?") from _call_reply_message_26
    call message ("Hana", "I don't know how to put it.") from _call_message_72
    call message ("Hana", "Disarming?") from _call_message_73
    call reply_message ("I know what you mean.") from _call_reply_message_27
    call message ("Hana", "What time will you be back tonight? Should I try and cook something?") from _call_message_74
    call phone_end_hana from _call_phone_end_hana
    scene w2_3792 with dissolve
    show screen textbox2 with dissolve
    "The smell of burnt food filled my nostrils as I remembered what happened the last time Hana tried to cook something."
    play music "music/ukulele-fun.ogg"
    scene w2_3794 with dissolve
    "No... need... I'm... likely... having..."
    scene w2_3795 with dissolve
    "...dinner... out... tonight."
    scene w2_3796 with dissolve
    mina "*Yawn*"
    "I'll... tell... you... about... it... later..."
    scene w2_3797 with dissolve
    "It's... really... REALLY... stupid. I'd... rather..."
    scene w2_3798 with hpunch
    mina "Boo."
    mc "-geh!"
    scene w2_3799 with dissolve
    mina "Didn't mean to startle you."
    scene w2_3800 with dissolve
    mc "You said \"boo\"..."
    scene w2_3801 with dissolve
    mc "Did you have a good nap?"
    scene w2_3802 with dissolve
    mina "Hmm... very good. Can't believe I was out for two hours."
    mina "I was a little surprised you are still here. You could've slipped out."
    scene w2_3801 with dissolve
    mc "I could've, but..."

    if w2MinaFlagVent == True:
        mc "I baked you some cookies."
        mc "Hope you don't mind, I found some cookie dough and--"
    else:
        $ Mina_Affection += 1
        mc "Then I wouldn't have been able to tell you this joke."
        scene w2_3803 with dissolve
        mina "You stuck around to tell me a joke?"
        scene w2_3804 with dissolve
        mc "You want to hear it?"
        scene w2_3803 with dissolve
        mina "Okay..."
        scene w2_3805 with dissolve
        "Mina looked at me dubiously, but nonetheless humored me."
        scene w2_3804 with dissolve
        mc "Why was the baby strawberry late for school?"
        scene w2_3803 with dissolve
        mina "...why?"
        scene w2_3806 with dissolve
        mc "Because her parents were stuck in a... JAM."
        scene w2_3807 with dissolve
        "Nothing. Absolutely nothing. Not even half a smile from the Princess of Cheer."
        scene w2_3808 with dissolve
        mc "Uh... that didn't land huh?"
        "I could read it in her eyes that she was politely abstaining from groaning."
        mc "I got to be honest. I may have spent the better part of an hour looking up jokes."
        scene w2_3803 with dissolve
        mina "You... looked it up...?"
        scene w2_3804 with dissolve
        mc "I really wanted to make you laugh."
        scene w2_3805 with dissolve
        mina "......"
        scene w2_3809 with dissolve
        mina "..."
        scene w2_3810 with dissolve
        mina "Ha...! Ah...! For real?"
        mina "That was the best you found?"
        scene w2_3811 with dissolve
        mc "I thought it was a pretty good one!"
        mina "Oh, yeah... no. No."
        mina "Bless your heart, no."
        scene minamcpat_a with dissolve
        show minamcpat
        mina "But... uh... I'll give you a gold star for effort."
        "She patted my head like one would do to comfort a child."
        if w2MinaPat == True:
            "The shoe was on the other foot."
            "... and it did feel pretty nice."
        else:
            "It felt... pretty nice."

        mina "The better part of an hour?"
        mc "I thought you might go for a lame joke like that--"

    scene w2_3812 with hpunch
    mina "Thanks, [mcf]."
    mina "I was feeling like shit that the only person I had for support besides Felicia was someone I barely know, but..."
    mina "...it was really shitty and rude of me to ignore your efforts. I'm sorry."
    scene w2_3813 with dissolve
    mc "...uh, s'okay."
    "-was all I could say with my head pressed into the blonde's shockingly tight stomach."
    scene w2_3814 with dissolve
    mc "What about your mom or brother?"
    scene w2_3815 with dissolve
    mina "Too embarrassed to let them know how much of a doormat I am."
    scene w2_3816 with dissolve
    mc "I don't think you're a doormat. I think you're in a relationship for the first time in your life."
    mc "One of life's learning curves, I'm sure."
    scene w2_3818 with dissolve
    mina "No, it's more than that."
    stop music fadeout 2.0
    mina "I'm just..."
    scene w2_3817 with dissolve
    "Mina paused, formulating her words."
    scene w2_3818 with dissolve
    play music "music/future-rennaisance.ogg"
    mina "I just don't know who I am."
    scene w2_3819 with dissolve
    mina "Sometimes I don't even feel like a human being. Isn't that fucking weird?"
    scene w2_3820 with dissolve
    mc "Not knowing what you want is normal. You're nineteen."
    scene w2_3818 with dissolve
    mina "I'm only me, so I don't know how other people feel, but..."
    scene w2_3817 with dissolve
    "She didn't finish her sentence."
    scene w2_3821 with dissolve
    "Something about the way she looked at me felt especially jarring."
    scene w2_3823 with dissolve
    mina "I'm going to ask a question, okay? It's a question you won't be able to give me an answer I'm happy with, but it'd make me feel better to say it out loud."
    scene w2_3822 with dissolve
    "It wasn't the joyless expression on her face, but her profoundly vacant eyes."
    scene w2_3824 with dissolve
    mina "This isn't about you wanting to be a doctor or me wanting to be an actress, it's..."
    scene w2_3823 with dissolve
    mina "Do you ever doubt the way you feel about things?"
    scene w2_3822 with dissolve
    mc "Sometimes."
    scene w2_3823 with dissolve
    mina "Only sometimes...?"
    scene w2_3822 with dissolve
    mc "Maybe. Give me an example."
    scene w2_3823 with dissolve
    mina "Like say... you see something sad happen to another person and your gut response is sympathy. I think a lot of people conclude then and there that they're an empathetic person."
    scene w2_3824 with dissolve
    mina "...but what if your gut response, the very first thing you think and feel, feels off to you? Doesn't feel like you at all?"
    scene w2_3823 with dissolve
    mina "Like the things you're feeling aren't anything more than what's been drilled into you?"
    scene w2_3825 with dissolve
    mc "Mina..."
    scene w2_3826 with dissolve
    "I didn't know how to answer her, but at this moment, I felt in her a kind of kindred spirit."
    scene w2_3827 with dissolve
    mina "Sometimes, I feel like a big question mark."
    mina "That's why this thing with Ian is so... I just don't know what to make of it."
    scene w2_3828 with dissolve
    mina "I feel anger, but the part that comes after that feels like I'm watching it happen to another person."
    scene w2_3829 with dissolve
    mc "Mina I..."
    mc "I know how you feel."
    "I was as authentic as I could possibly be."
    mina "Do you really...?"
    scene w2_3830 with dissolve
    mina "I fucking hate it, [mcf]."
    mina "I just want to feel the world is right-side-up, but I just don't understand how to."
    scene w2_3831 with dissolve
    mc "The more you experience and learn about yourself, the more you can be sure."
    mc "That's the only way to know if what you feel is just what's expected of you or who you genuinely are as a person."
    mc "That or get a shrink."
    scene w2_3832 with dissolve
    mina "Ha... yeah..."
    mina "Experience... I think so too. About that..."
    scene w2_3833 with dissolve
    mina "I want your help with gaining some experience."
    scene w2_3834 with dissolve
    mc "Well, if it's something I can do, I'll do it."
    scene w2_3833 with dissolve
    mina "You should hear what it is first, before you make a promise like that."
    scene w2_3835 with dissolve
    mc "Damn, that's uh... mysterious. Okay then... what is it?"
    scene w2_3836 with dissolve
    mina "Mmmm..."
    scene w2_3837 with dissolve
    mina "...oh God, this is a stupid idea."
    scene w2_3838 with dissolve
    mc "Just say it."
    scene w2_3839 with dissolve
    mina "I've got a list of things I want to do. Stuff that I've been either too embarrassed, too afraid, or just otherwise can't do by myself."
    scene w2_3840 with dissolve
    mc "Like a bucket list?"
    scene w2_3839 with dissolve
    mina "Sort of, but most of it is..."
    scene w2_3841 with dissolve
    "Her body language was skittish, but her eyes were appraising like a hawk, vetting my response and looking to see if she needed to course-correct her approach. Undoubtedly without even realizing it."
    "She didn't know just how dangerous of a woman she was."
    scene w2_3842 with dissolve
    mina "You still coming to the arcade tomorrow?"
    scene w2_3843 with dissolve
    mc "Oh, yeah... to be honest, I forgot all about that, but... I'm still free."
    scene w2_3844 with dissolve
    mc "Maybe I can get revenge for today's slaughter."
    scene w2_3845 with dissolve
    mina "If you want, afterward... you can help me with one of the items on the list."
    mina "I promise it's nothing sketchy, it's just better to surprise you than put it into words. At least initially..."
    scene w2_3846 with dissolve
    "I don't really do surprises, but I suppose there was no harm in humoring the vulnerable blonde. The only thing I was obligated to do tomorrow was hand in the pictures of the Carnations."
    mc "Well, I've already promised to hang out with you, so..."
    scene w2_3847 with dissolve
    mina "It's not like I'm taking you to climb a mountain or--"
    mc "...no biggie in dropping by your place afterward."
    scene w2_3849 with dissolve
    mina "G-good!"
    mina "Sorry for..."
    scene w2_3850 with dissolve
    mina "Sorry to ask a lot. I feel really stupid right now."
    scene w2_3851 with dissolve
    mc "Relax. I've done nothing."
    scene w2_3852 with dissolve
    "In tandem with my reassurance, Mina firmly pressed her cheek against my breast and warmly nuzzled my chest."
    "Lots of hugs today..."
    mct "(Not so bad.)"
    scene w2_3853 with dissolve
    "This hug lingered a tad longer than I expected, with the cuddly blonde accidentally shifting her weight ever so slightly in a way that made me acutely aware of her softest bits."
    scene w2_3854 with dissolve
    mina "So... you have someplace to be?"
    "No sooner had we parted, did she pose that question."
    scene w2_3855 with dissolve
    mc "You want me out of here?"
    scene w2_3856 with dissolve
    mina "Kiiiinda. I've got to run out and take care of some stuff, but I need to get ready first."
    scene w2_3857 with dissolve
    "That worked for me. I still had to get ready for my date with Felicia."
    scene w2_3856 with dissolve
    mina "You can tell Felicia your babysitting mission was a success."
    scene w2_3855 with dissolve
    mc "How about you tell her? God knows how she might take that coming from me."
    scene w2_3858 with dissolve
    mina "Hehe. Thanks for being here, [mcf]."
    scene black with fade
    mina "Truly."
    stop music fadeout 3.0
    "......"
    "..."
    "Shit. I never asked Mrs. Pulman what the dress code was..."
    jump w2FeliciaStart

label w2MinaRevealNotFlag:

    stop music fadeout 3.0
    if w2MinaFlagVent == True:
        scene w2_3769 with dissolve
        mina "Thanks, [mcf]. I'll keep that in mind, but..."
        scene w2_3770 with dissolve
        "With an exasperated sigh, Mina flopped down onto the bed like a deflated balloon..."
        scene w2_3771 with dissolve
        mina "I think I just want to take a nap."
    else:
        scene w2_3769 with dissolve
        mina "I don't think that's very likely. Not today at least."
        scene w2_3770 with dissolve
        "With an exasperated sigh, Mina flopped down onto the bed like a deflated balloon..."
        scene w2_3771 with dissolve
        mina "Today... right now..."
        mina "All I want to do is sleep."

    scene w2_3859 with dissolve
    mina "I found that USB drive early last night, so... didn't sleep much..."
    scene w2_3862 with dissolve
    mc "No one would."
    scene w2_3861 with dissolve
    "Stating the obvious when there's nothing else to say - name a better combo."
    mina "Ahaah..."
    scene w2_3860 with dissolve
    mina "You can leave, [mcf]."
    scene w2_3862 with dissolve
    mc "Are you sure?"
    scene w2_3860 with dissolve
    mina "Can I be honest?"
    "She didn't wait for what I would obviously affirm."
    mina "I appreciate you being here. I like you..."
    mina "...but seeing you at this particular moment reminds me of Ian. It makes me feel angry."
    mina "I hate feeling that way, since it's not your fault and you're being awesome, it's just--"
    scene w2_3863 with dissolve
    mc "Say no more."
    mc "It's raw. I completely understand."
    mc "Being a friend means knowing when to back off."
    scene w2_3860 with dissolve
    mina "Thanks for understanding, [mcf]..."
    mina "Thanks so..."
    scene w2_3861 with dissolve
    "Facedown on her bed, her words were interrupted by a choked-out, muffled sob."
    mina "Thanks so much."
    scene black with fade
    "At this moment, regardless of how I felt about my friend on a normal day, I loathed him."
    "After insisting she call me if she needed anything, which I knew she wouldn't, I left the apartment and finally felt like I could breathe again."
    "......"
    "..."

label w2FeliciaStart:
    $ w2FelShootPoints +=2
    play sound "sound effects/door-open.wav"
    scene w2_3864 with blinds
    "I went home to blindly prepare."

    if minaFlag == True:
        $ history_mina = "Mina discovered an extremely damning video of Ian, pulling me into the drama. I promised to vaguely help with something after going to the arcade with her tomorrow."
        $ unread_mina = True
    else:
        $ history_mina = "Mina discovered an extremely damning video of Ian, pulling me into the drama. Thankfully, I extricated myself from the situation."
        $ unread_mina = True

    play sound "sound effects/notification.wav"
    show bioupdate with dissolve

    if kat_polite == True:
        "Mrs. Pulman didn't answer my call, so what to wear to an \"interview\" with a wealthy transportation magnate whose wife I was there to secretly take lewd photos of, was left entirely to my inexperienced discretion."
    else:
        "Kathleen didn't answer my call, so what to wear to an \"interview\" with a wealthy transportation magnate whose wife I was there to secretly take lewd photos of, was left entirely to my inexperienced discretion."

    scene w2_3865 with dissolve
    "If I were to be forthright with my feelings, while my trepidation hadn't weakened, now that I was this close to zero hour..."
    "I was feeling excited."
    play music "music/the-loner.ogg"
    scene w2_3866 with fade
    mc "You're a real piece of shit, [mcf]."
    scene w2_3867 with dissolve
    "That was what I thought, but I didn't feel guilty about it."
    "I desperately wanted to feel conscience-stricken, like I imagined a normal person would feel."
    "The self-awareness brought me a small measure of comfort, but I was also cognizant that it made me fully culpable in my actions."
    scene w2_3868 with dissolve
    hana "Usually, when people give themselves a pep talk in a mirror, it's a little less insulting."
    mc "You heard that?"
    scene w2_3869 with dissolve
    hana "I was in the kitchen. I guess the sound in the bathroom carries well."
    mc "That's good to know for the future."
    scene w2_3870 with dissolve

    if minaFlag == True:
        hana "You made it sound in your text like you wouldn't be home until tonight."
        mc "I needed to get dressed."
        hana "Must be a fancy dinner."
        scene w2_3871 with dissolve
        mc "It's for work."
    else:

        hana "What's with the clothes?"
        mc "I have someplace to be tonight. Work-related."

    scene w2_3872 with dissolve
    hana "Aha! The self-deprecation makes sense now."
    scene w2_3878 with dissolve
    "Hana was the only person in the world who could appreciate my feelings, given our similar positions."

    if w2HanaSex == True:
        scene w2_3874 with dissolve
        hana "You look... good."
        scene w2_3875 with dissolve
        "I don't think she meant to, but Hana gave me a rather provocative look."
        mc "You've seen me dressed up before."
        scene w2_3873 with dissolve
        hana "That {i}costume{/i} you wear doesn't count."
    else:

        scene w2_3873 with dissolve
        hana "You look good."
        scene w2_3871 with dissolve
        mc "Eh? Is it any different than what you see me in at work?"
        scene w2_3873 with dissolve
        hana "Yes. {b}Very{/b} different."

    hana "Do you ever think a waiter looks good in his clothes?"
    scene w2_3871 with dissolve
    mc "I tend not to have an opinion on a man's appearance."
    scene w2_3876 with dissolve
    hana "Well, trust me on this."
    scene w2_3871 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Tell her she looks good at work.":

            show screen textbox2 with dissolve

            if w2HanaSex == True:
                mc "You look hot at work."
                scene w2_3877 with dissolve
                hana "That's because I am hot."
                scene w2_3878 with dissolve
                "The implication being that I'm..."
                mc "Ouch. That's hurtful."
                scene w2_3873 with dissolve
                hana "Do you want to know what the actual difference is?"
            else:

                mc "You look good at work."
                scene w2_3879 with dissolve
                hana "Gee, I wonder what the difference is?"

            scene w2_3871 with dissolve
            mc "The lingerie?"
            scene w2_3876 with dissolve
            hana "No shit. Wear some heels, fishnets, and a garter belt next time and I might feel differently too."
            scene w2_3881 with dissolve
            mc "...you really think I look good?"

            if w2HanaSex == True:
                scene w2_3882 with dissolve
                hana "You look... {b}handsome{/b} right now."
                scene w2_3883 with dissolve
                hana "Don't let it go to your head."
                scene w2_3881 with dissolve
                mc "Too late."
            else:

                scene w2_3883 with dissolve
                hana "Don't get a big head about it."
                scene w2_3881 with dissolve
                mc "Too late."
        "You thought women loved a man in uniform.":




            show screen textbox2 with dissolve
            mc "I always heard women liked men in uniforms."
            scene w2_3873 with dissolve
            hana "Every gal likes a good sailor or fireman. Those are the good ones."
            scene w2_3871 with dissolve
            mc "What are the bad ones?"
            scene w2_3879 with dissolve
            hana "Uh... a prison jumpsuit? Although I'm sure there are people into that..."
            scene w2_3878 with dissolve
            mc "Fair enough."
            scene w2_3880 with dissolve
            hana "Oh yeah, and for me, {b}no cops{/b}. Blech."
            scene w2_3871 with dissolve
            mc "Too bad. I always wanted to try that roleplay."
            scene w2_3872 with dissolve
            hana "Well, maybe you can talk one of the house girls into that. It'd be an easy night for them."
            scene w2_3878 with dissolve
            mc "Are you encouraging me to employ the services of a prostitute?"
            scene w2_3884 with dissolve
            hana "It's the most likely way you're getting laid, right?"
            scene w2_3885 with dissolve
            mc "Hey, fuck off."

            if w2HanaSex == True:
                mc "You seemed interested enough the other night."



    scene w2_3886 with dissolve
    hana "Ha!"
    scene w2_3887 with dissolve
    "..."
    hana "So, you've been unusually busy with work this week."
    scene w2_3888 with dissolve
    mc "I wouldn't know, this is my first summer."
    scene w2_3887 with dissolve
    hana "Not like I knew Darius all that well, but as far I know, most of his duties were kept to the weekend."
    scene w2_3888 with dissolve
    mc "Maybe the old woman is feeling extra creative this season?"
    scene w2_3889 with dissolve
    hana "Yeah, maybe... what is she having you do tonight?"
    scene w2_3890 with dissolve
    hana "I know you keep saying we shouldn't talk about it, and you're probably right, but I want to know."
    scene w2_3891 with dissolve
    mc "Worried about the kind of person you're rooming with??"

    if w2HanaSex == True:
        scene w2_3892 with dissolve
        hana "No, it's just..."
        hana "I'm just concerned my new friend might be forced to do something fucked up."
    else:
        scene w2_3889 with dissolve
        hana "No, it's just..."
        hana "I like you and I'm just concerned you might be doing something you don't want to do."

    scene w2_3893 with dissolve
    mc "I'm meeting with Felicia's husband to interview him."
    scene w2_3895 with dissolve
    hana "You're meeting with one of the Carnation's husbands?! For-fuckin'-real?"
    scene w2_3896 with dissolve

    if kat_polite == True:
        mc "It's all some stupid ruse Mrs. Pulman cooked up to make her photoshoot spicier."
    else:
        mc "It's all some stupid ruse Kathleen cooked up to make her photoshoot spicier."

    scene w2_3897 with dissolve
    hana "So let me get this straight... you're meeting with her husband and you're going to... take lewd photos of her?"
    scene w2_3896 with dissolve
    mc "Secretly take lewd photos of her, yes."
    scene w2_3897 with dissolve
    hana "That's... that's so..."
    scene w2_3898 with dissolve
    hana "Baaah, that's so messed up!"
    scene w2_3899 with dissolve
    mc "You've seen worse at the club, surely."
    scene w2_3898 with dissolve
    hana "That doesn't make it any less fucked. That poor man."
    scene w2_3897 with dissolve
    hana "You're really just going to do it because she said to?"
    scene w2_3896 with dissolve
    mc "It's my job."
    scene w2_3900 with dissolve
    hana "Where are we, Nuremberg?"
    scene w2_3901 with dissolve
    mc "Not even remotely the same."
    scene w2_3902 with dissolve
    hana "Yeah, but come on... it doesn't give you any pause? Shitting on a man's marriage vows in his own house?"
    scene w2_3903 with dissolve
    mc "I've wrestled with it over the last few days, but if I'm going to do it, fretting about it would be unhelpful."
    mc "Besides, Felicia's the one who volunteered for the club and I'm pretty sure her husband is also unfaithful..."
    scene w2_3904 with dissolve
    hana "Wrong is wrong is wrong, [mcf]."
    scene w2_3905 with dissolve
    mc "Why the hell are you getting so hung up on this? There's a lot more going on at the club other than infidelity."
    mc "You're going to own a part of it."
    scene w2_3906 with dissolve
    hana "It's just..."
    scene w2_3907 with dissolve
    hana "I don't fucking know. You're right, but it still pisses me off."
    hana "I just want you to be pissed off about it too, I guess."
    hana "Am I going to become as nonchalant about this as you?"
    scene w2_3908 with dissolve
    mc "I don't know...?"
    scene w2_3909 with dissolve
    hana "Neither do I..."
    scene w2_3910 with dissolve
    hana "Bah! I'm going to go kick the sidewalk or something."
    hana "Don't have too much fun tonight, you pig."
    scene w2_3911 with dissolve
    mct "(Did we just have a fight...?)"
    "It was over way too quick to even make sense of it, but I could understand how she felt."
    play sound "sound effects/door-openclose.wav"
    stop music fadeout 3.0
    "Wrong is wrong is wrong."
    scene black with fade
    "So, I went to go do some wrong."
    "......"
    "..."
    play sound "sound effects/elevator-bell.wav"
    play music "music/air-on-g.ogg"
    scene w2_3912 with blinds
    "Elias Ford lived atop a gilded tower, in a penthouse whose only public access was an express elevator."
    fel "Welc-"
    scene w2_3913 with wipeleft
    "The man himself, with beautiful wife in tow, was there to greet me personally. For a lowly (fake) journalist, I was expecting a maid."
    fel "W-welcome to our..."
    "Finding the couple in their bathing suits was a surprise, but naturally I was far less shocked than the dumbstricken bombshell that stood next to him."
    scene w2_3914 with dissolve
    el "...what's the matter with you?"

    if kat_polite == True:
        "Just as Mrs. Pulman had anticipated, Felicia's look was priceless. Her mouth opened and closed like a fish choking on air."
    else:
        "Just as Kathleen had anticipated, Felicia's look was priceless. Her mouth opened and closed like a fish choking on air."

    scene w2_3915 with dissolve
    el "Welcome to our home, Charles."
    "Charles Bukowski -- that was the name I was working under, as per the information that the old woman had texted me days before."
    scene w2_3916 with dissolve
    mc "Call me Chuck."
    "I took it the alias was her idea of a joke, considering the philandering nature of the evening."
    scene w2_3917 with dissolve
    el "I hope you'll forgive my attire. We were just enjoying a leisurely soak by the pool and lost track of time."
    scene w2_3916 with dissolve
    mc "That's alright. No need for things to be so stiff. In fact, it's better if you're comfortable."
    "There were two reasons that made me feel abundantly certain Elias' excuse was a total fabrication."
    mc "Comfort makes people more honest, in my experience."
    "The primary red flag was Felicia's haste earlier in preparation for today. The second reason relied on my intuition. I just had a feeling that..."
    scene w2_3918 with dissolve
    "{b}This{/b} wasn't a man who would lose track of time, let alone do so while lounging by a pool."
    scene w2_3919 with dissolve
    el "Trick of the trade, eh?"
    scene w2_3920 with dissolve
    fel "Yes, {b}welcome{/b}. We're so very glad to have you."
    scene w2_3921 with dissolve
    el "The lights finally turned on, huh? That's not like you."
    scene w2_3922 with dissolve
    el "This is my wife, Felicia. She's the light of my life and a wonderful mother to my children."
    scene w2_3918 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Shake Elias' hand.":
            scene w2_3923 with dissolve
            show screen textbox2 with dissolve
            mc "It's nice to meet you, Mr. Ford."
            "While holding out my hand, I recalled my twelfth grade English teacher Mrs. Sullivan and the way she impressed upon the class the importance of a strong handshake."
            "That had always stayed with me, but for some reason, that lesson was at the forefront of my mind right now."
            scene w2_3924 with dissolve
            el "Likewise."
            "I was certain it wasn't because I was hungry to make a good first impression on the man. The thought didn't even cross my mind when I met Abel Van Doren, someone I actually respected."
            scene w2_3925 with dissolve
            "It was something more..."
            scene w2_3926 with dissolve
            "Illogical and adversarial."
            scene w2_3927 with dissolve

            if feliciaFlag == True:
                "The lurid and adulterous nature of my mission had me feeling territorial in the face of the man I was two-timing."
            else:
                "Even if my interest in Felicia didn't go beyond the walls of the club, the lurid and adulterous nature of my mission had me feeling territorial in the face of the man who I was two-timing."

            scene w2_3928 with dissolve
            mc "And you..."
            hide screen textbox2 with dissolve

            menu:
                "Shake Felicia's hand.":
                    scene w2_3929 with dissolve
                    show screen textbox2 with dissolve
                    mc "It's nice to meet you as well, Mrs. Ford."
                    scene w2_3930 with dissolve
                    fel "It's my pleasure, Mr. Bukowski."
                "Kiss Felicia on the cheek.":


                    scene w2_3931 with dissolve
                    show screen textbox2 with dissolve
                    mc "It's nice to meet you as well, Felicia."
                    fel "O-oh?"
                    scene w2_3932 with dissolve
                    "Despite having recovered from the shock of my visit like a tried and true professional, she still winced when my lips met her soft cheeks."
                    fel "It's my pleasure, {i}Chuck{/i}."
        "Make a point of greeting Felicia first."(chg=["felicia_up"]):

            $ Felicia_Affection += 1
            show screen textbox2 with dissolve
            "For some reason, his reaction to Felicia's social misstep rubbed me the wrong way."
            scene w2_3933 with dissolve
            mc "It's nice to meet you, Mrs. Ford."
            scene w2_3934 with dissolve
            el "..."
            scene w2_3935 with dissolve
            fel "...it's my pleasure, Mr. Bukowski."
            scene w2_3936 with dissolve
            "As juvenile as it was, I made it a point to greet my beleaguered ward first and foremost."
            hide screen textbox2 with dissolve

            menu:
                "Pull her into a hug.":
                    scene w2_3938 with dissolve
                    show screen textbox2 with dissolve
                    mc "Sorry, I'm a hugger."
                    scene w2_3939 with dissolve
                    fel "...that's okay. The world is... full of... all types."
                    scene w2_3938 with dissolve
                    mc "That's a lovely swimsuit. Probably costs half of what I make in a year."
                    scene w2_3940 with dissolve
                    mc "And you..."
                "Keep it cordial.":

                    scene w2_3937 with dissolve
                    show screen textbox2 with dissolve
                    mc "You look very charming tonight."
                    scene w2_3940 with dissolve
                    mc "And you..."

            mc "I've been looking forward to meeting you."
            scene w2_3941 with dissolve
            el "Likewise, Chuck."

    scene w2_3942 with dissolve
    mc "You have a really lovely home."
    fel "That's kind of you to say so."
    scene w2_3943 with dissolve
    el "I believe in living modestly, to keep the essentials close."
    mc "M-mod--"
    "I felt a vein in my forehead twitch and I choked back a scoff at Elias' flagrant abuse of the word {i}modest{/i}."
    mc "That's... an admirable approach to building a home."
    scene w2_3944 with dissolve
    el "Isn't it? I always hated how big my grandfather's estate was. Vastness can be suffocating."
    el "A small home though, now that's the mark of a steward and preserver of the important things in life."
    scene w2_3945 with dissolve
    mc "Ah... minimalism, right?"
    scene w2_3946 with dissolve
    mct "(You call this small, you out-of-touch fuck?)"
    el "Oh God, no. I know how that would sound on paper."
    el "Just compared to how I grew up."
    scene w2_3947 with dissolve
    mc "If you don't mind, I'd like to get a picture of you and your wife together."
    scene w2_3948 with dissolve
    el "Be my guest."
    scene w2_3949 with dissolve
    el "Felicia?"
    scene w2_3950 with dissolve
    mc "I'll be taking more throughout the night. We only need a few for the write-up, but it pays to be thorough."
    scene w2_3951 with dissolve
    el "I understand that well. Fastidiousness is another key component of stewardship."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_3952 with flash
    "*Click*"
    mct "(There he goes with that steward crap again...)"
    scene w2_3953 with dissolve
    mc "You're a wise man, Mr. Ford."
    scene w2_3954 with dissolve
    el "Please, allow me to extend to you the same courtesy you offered me. Call me {i}Elias{/i}."
    scene w2_3955 with dissolve
    mc "How should we do this, Elias?"
    scene w2_3956 with dissolve
    el "The interview? We'll conduct the interview in my office, but first I'd like to sit down and have a chat. There's sparse information about your work as a journalist on the net."
    scene w2_3957 with dissolve
    "Oh, I {b}bet{/}."

    if kat_polite == True:
        "Seems my assigned alias was more than just Mrs. Pulman's sense of irony. It also obscured."
    else:
        "Seems my assigned alias was more than just Kathleen's sense of irony. It also obscured."

    scene w2_3958 with dissolve
    el "I'd like to get to know you better."
    scene black with fade
    mc "If that's what you want, we're on your time."
    scene w2_3959 with fade
    el "You seem young to be writing an article like this, you must be talented."
    "A \"fluff piece on a celebrity businessman?\", I almost asked, but didn't due to the self-important implication that a talented writer is what he {i}deserves{/i}."
    mc "More than young, what I feel like is {b}overdressed{/b}."
    el "Oh, don't worry about that. I'll change shortly into something more appropriate."
    $ renpy.music.set_volume(.1, 0, channel = "sound")
    play sound "sound effects/water-splash3.wav"
    scene w2_3960 with dissolve
    el "You'll be the one writing the article?"
    mc "I'll transcribe our conversation and editorialize it, yes."
    "That was a lie. I was assured it was going to be ghost-written."
    el "Editorialization can be good and bad."
    stop sound
    $ renpy.music.set_volume(1, 0, channel = "sound")
    scene w2_3961 with dissolve
    mc "Don't worry, our paper doesn't do hit pieces. You're sure of that or else you wouldn't have agreed to meet me."
    el "Don't get me wrong, I have the most profound respect for the institution of journalism. It's a noble and needed profession for a truly free society. Accountability..."
    scene w2_3962 with dissolve
    mc "...is the mark of good stewardship?"
    scene w2_3963 with dissolve
    el "That's right."
    scene w2_3964 with dissolve
    el "Accountability is integral to the self-governance of one's goals and self."
    scene w2_3965 with dissolve
    "While Elias fed me his self-important bullshit, Felicia did what I imagined Elias expected of her. {i}Shut up and look pretty{/i}."
    "She was posed in just a way that her bombastic body would draw our eyeline back even from its periphery."
    el "Anyway... journalism. I respect the job itself, the problem I have is with journalists."
    scene w2_3966 with dissolve
    el "Most are bloodsuckers using that noble profession as a shroud to drum up sensation or advance their own agenda. Years and years ago, they accused my great grandfather's legacy of being built on blood and exploitation."
    el "Which, let's be honest... that was simply the way progress was built back then. They conveniently forget the railroad helped to modernize this nation, he built infrastructure and supply lines, enabled the common person to travel far and wide and manifest destiny."
    el "How do a few \"labor disputes\" really measure up to that when seen through the long lens of history?"
    scene w2_3967 with dissolve
    mct "(Holy crap, this wackadoo is lucky I'm not an actual fucking journalist.)"
    mc "It doesn't, of course."
    scene w2_3968 with dissolve
    el "All this is to say, I respect the journalists in your paper's employ. It's a bastion of truth standing stalwart against the tyranny of the masses."
    scene w2_3969 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Crack a joke.":
            scene w2_3970 with dissolve
            show screen textbox2 with dissolve
            mc "You want a good write-up, huh?"
            scene w2_3971 with dissolve
            el "Thanks, I would love one!"
            el "Ha!"
            "The asshole shamelessly laughed in the face of what was meant to be an accusation."
        "Let his insincerity pass.":

            scene w2_3972 with dissolve
            show screen textbox2 with dissolve
            mc "Well, we do our best..."

    scene w2_3973 with dissolve
    "As the man droned on and on, I focused less on his words and more on Felicia."
    "One reason was her beauty. Even in this gilded tower, she shined brighter than anything else and drew my attention like a moth to the flame."
    scene w2_3974 with dissolve
    "The more pressing reason though... I had yet to find a chance to begin {i}our shoot{i}."
    "I had come here with a plan, one that would ensure I would be able to get what the old woman needed even under Elias' scrutiny, but I needed to find alone time with the blonde to enact it."
    scene w2_3975 with dissolve
    el "--don't you agree?"
    scene w2_3976 with dissolve
    mc "Oh... yeah, of course."
    scene w2_3977 with dissolve
    el "My wife... she's beautiful, isn't she?"
    scene w2_3978 with dissolve
    "Elias knew where my attention had landed, but he didn't seem plussed about it."
    scene w2_3979 with dissolve
    fel "Oh, honey. He's here to talk about you. Not me."
    scene w2_3980 with dissolve
    mc "Behind every great man is an even greater woman they say."
    scene w2_3981 with dissolve
    el "That's right. Felicia is a solid woman."
    el "I couldn't have chosen a better one after my previous wife passed."
    scene w2_3982 with dissolve
    el "I love her dearly. She's an incredibly shrewd woman."
    scene w2_3983 with dissolve
    "Solid woman, chosen, shrewd... he didn't even realize it."
    "To a man like him, I think he genuinely believed his words were ones of affection."
    scene w2_3982 with dissolve
    el "Most of my friends are divorced, having carelessly picked the wrong partner."
    scene w2_3981 with dissolve
    el "Felicia... she's right as rain."
    scene w2_3984 with dissolve
    fel "I'm just a small part of something greater."
    scene w2_3985 with dissolve
    el "Why don't you play that part by getting Chuck and me something to drink."
    scene w2_3986 with dissolve
    fel "Anything, dear."
    scene w2_3987 with dissolve
    el "You'll excuse me while I go freshen up and make a call?"
    el "Felicia will entertain you. I won't be long."
    scene w2_3990 with dissolve
    mc "That would be perfect."
    scene w2_3988 with dissolve
    el "Would it?"
    scene w2_3990 with dissolve
    mc "I... welcome a break to stretch my legs and speak with your lovely wife."
    stop music fadeout 3.0
    scene w2_3991 with dissolve
    el "Make yourself at home."
    scene black with fade
    "With that, he left Felicia and me alone."
    scene w2_3992 with fade
    mc "Well..."
    play music "music/bellissimo.ogg"
    scene w2_3993 with dissolve
    fel "{b}Well{/b}...!"
    scene w2_3994 with dissolve
    "I knew what was coming."
    scene w2_3995 with dissolve
    "Felicia gave me a killer look and stormed over."
    mc "Bit of a sur--"
    scene w2_3996 with hpunch
    fel "Bit of a surprise? Is that what you were about to say?!"
    scene w2_3997 with dissolve
    fel "I think I know what's going on here, but you couldn't have given me a heads-up?! A little forewarning when we saw each other this morning?!"
    fel "I about jumped out of my tan when I saw you come out of the elevator!"
    scene w2_3998 with dissolve

    if kat_polite == True:
        mc "Mrs. Pulman insisted it remain a surprise. She thought you might have an issue with the arrangement."
    else:
        mc "Kathleen insisted it remain a surprise. She thought you might have an issue with the arrangement."

    scene w2_3999 with dissolve
    fel "This is that mission she talked about on Monday. The photoshoot, is it?"
    scene w2_4000 with dissolve
    mc "Correct."
    scene w2_4001 with dissolve
    fel "You know my husband is expecting an actual article, right? He's the type to dig when things don't go to his expectations."
    scene w2_4002 with dissolve
    fel "And honestly, I suspect the club isn't that well kept of a secret considering I know about it!"
    scene w2_4003 with dissolve
    mc "Relax, he'll get his fluff piece."
    mc "I'm supposed to take notes and pass them on to a writer at the paper. The plan is absurd, yes, but the bases are covered."
    scene w2_4004 with dissolve
    fel "That right...? Ah, holy shit..."
    fel "This whole dog and pony show for some peep shots?"
    scene w2_4005 with dissolve
    fel "That woman really doesn't do simple, does she? What a cre~a~tive {b}cunt{/b}."
    scene w2_4000 with dissolve
    mc "I'm honestly glad you picked up on things so quickly, it saves me from explaining the situation."
    scene w2_4003 with dissolve
    mc "I don't expect we have much time to align our goals before Elias gets back."
    scene w2_4002 with dissolve
    fel "Align {i}our{/i} goals? You mean go along with this?"
    scene w2_4006 with dissolve
    fel "Yeeeeah, I don't think so stud. I'm just going to have to take an L in this game."
    fel "This is way, waaay, waaaay too fuckin' risky. I'll just have to overperform this Saturday."
    scene w2_4007 with dissolve
    "Ah, shit."
    "It's not like I didn't understand where she was coming from. This whole scenario crossed the line, but she had no one else to blame."
    "She was the one who put her foot over the line to begin with, volunteering for the old woman's game. I liked her, but I genuinely felt little sympathy for her."

    if kat_polite == True:
        "Veronica did what she wanted, but at least the photos were dirty as hell. Even if Mrs. Pulman notices the conspicuous lack of people teeming around the gym, I reckon she'll be satisfied with the end result."
    else:
        "Veronica did what she wanted, but at least the photos were dirty as hell. Even if Kathleen notices the conspicuous lack of people teeming around the gym, I reckon she'll be satisfied with the end result."

    "That wouldn't really fly in this situation. It was one thing for Felicia to jeopardize her seemingly frivolous prize, but her failure to perform will reflect on me. This is my job, after all."
    scene w2_4008 with dissolve
    mc "Listen, I considered your situation before coming here..."
    scene w2_4009 with dissolve
    "From my pocket, I withdrew quite the familiar egg-shaped toy."
    mc "...and came up with a safe plan. If we just combine that with a few other--"
    scene w2_4010 with dissolve
    fel "Don't just hold that in your hand! *Whisper* What if Elias came waltzing out of his office just now?"
    scene w2_4011 with dissolve
    fel "I can explain a lot of things convincingly enough for him to pretend to believe them, but the journalist he's expecting to stroke his ego offering a sex toy to his wife ain't one of them."
    scene w2_4012 with dissolve
    fel "Christ, do you know how ridiculous this whole situation already is, even if you were really who you are pretending to be?"
    scene w2_4013 with dissolve
    fel "Someone made one joke at a charity roast one time, a year ago, about how much of a tight-ass he is and now he's all..."
    scene w2_4014 with dissolve
    fel "*Whisper* ...laissez-fucking-faire for this interview!"
    scene w2_4015 with dissolve
    fel "*Whisper* He's never even been in the fucking pool! Not once since we bought this place!"
    scene w2_4016 with dissolve
    fel "*Whisper* How the fuck does he manage a talent agency?"
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_4017 with dissolve
    "*Click*"
    fel "H-huh?"
    "Her exasperation made for a cute photo and I didn't miss the chance."
    scene w2_4018 with dissolve
    fel "Oh, you fu--."
    scene w2_4019 with dissolve
    "In her excited state, her southern inflection reared its charming head."
    hide screen textbox2 with dissolve


    menu:
        "Call her cute"(chg=["felicia_down"]):
            $ Felicia_Affection -= 1
            show screen textbox2 with dissolve
            mc "You sounded cute there."
            scene w2_4018 with dissolve
            fel "And your nonchalance is annoying as shit, [mcf]."
            scene w2_4020 with dissolve
            "Both of us flinched at how loud and clear my name rang out, causing us to crane our necks in the direction of Elias' office, until we finally breathed a sigh of relief."
            scene w2_4021 with dissolve
            fel "Ahaaa..."
            fel "I've done this for so long, I should know how to keep that junk in. Your glibness aside, none of this is really your fault."
            scene w2_4022 with dissolve
            fel "Almost none of it."
            scene w2_4023 with dissolve
            fel "It's just a bunch of crap that's been piling up since last year..."
            scene w2_4024 with dissolve
            mc "Last year?"
            scene w2_4023 with dissolve
            fel "No time to get into it."
            scene w2_4024 with dissolve
            mc "You're not wrong. We {b}don't{/b} have time."
            scene w2_4025 with dissolve
            mc "You should insert what's in your hand, so we can complete the shoot."
        "Tell her to take a breath":


            show screen textbox2 with dissolve
            scene w2_4026 with dissolve
            mc "Slow down a minute and reset. Think about where we are."
            scene w2_4027 with dissolve
            fel "......"
            scene w2_4028 with dissolve
            "If blinking had a sound, Felicia would be screeching at me right now."
            scene w2_4029 with dissolve
            fel "..."
            scene w2_4030 with dissolve
            fel "Shit. I'm feelin' a little basic for getting excited like that."
            scene w2_4029 with dissolve
            mc "It's understandable."
            scene w2_4021 with dissolve
            fel "No, it's not. Not for me."
            fel "It's just a lot of little things compounding on one another, but I should be more composed."
            scene w2_4023 with dissolve
            fel "This ain't my first rodeo."
            scene w2_4024 with dissolve
            mc "Little things?"
            scene w2_4023 with dissolve
            fel "Oh, hun. Even if we were alone and had all night, I wouldn't even know where to start."
            scene w2_4025 with dissolve
            mc "You could start by inserting what's in your hand, so we can complete the shoot."


    scene w2_4031 with dissolve
    fel "Do you honestly think I've changed my stance in the last minute?"
    scene w2_4032 with dissolve
    mc "I was hoping..."
    scene w2_4033 with dissolve
    fel "......"
    scene w2_4034 with dissolve
    fel "..."
    scene w2_4035 with dissolve
    fel "...does this have a bearing on who wins?"
    scene w2_4036 with dissolve
    mc "She said the best shoot gets an advantage."
    scene w2_4035 with dissolve
    fel "That's vague... as much as I would love to stick it to--"
    scene w2_4037 with dissolve
    el "Felicia?"
    scene w2_4038 with dissolve:
        subpixel True
        yalign 1.0
        xalign 0.6
        linear 6 yalign 0.1
    "..."
    scene w2_4039 with dissolve
    el "I thought I said to fix Charles a drink, what the hell are you dawdling for?"
    el "I swear you've been spacing out more and more lately. Is something the matter?"
    scene w2_4040 with dissolve
    fel "Nothing, we were just talking about... art. You know how I get about that."
    scene w2_4041 with dissolve
    el "Your little {i}distractions{/i} are good and fine, but you can pour a drink while you flap your gums."
    el "It used to be your old \"job\", remember?"
    scene w2_4042 with dissolve
    mc "It's no big deal, Elias. I'm not--"
    scene w2_4043 with dissolve
    el "Nonsense. You're a guest in my home and you've gone far too long without a drink in your hand."
    scene w2_4042 with dissolve
    "He left no room to argue. As ridiculous as he sounded earlier, full of hot air and flattery, this demanding demeanor fit him like a glove."
    scene w2_4044 with dissolve
    el "I'll be another twenty minutes, so make yourself at home."
    scene w2_4045 with dissolve
    "I counted my blessings over the allotted time. Hopefully, inside of that window, I could take some pictures and convince Felicia to play along with my plan."
    scene w2_4046 with dissolve
    mc "Where were we?"
    scene w2_4047 with dissolve
    mc "Remember, you want jo--"
    fel "Tsk...! I'll play along."
    fel "On second thought, this will be {b}fun{/b}."
    scene w2_4048 with dissolve
    mc "...really? Just like that?"
    mc "What changed your mind?"
    scene w2_4049 with dissolve
    fel "I remembered why I wanted to do this in the first place."
    scene w2_4050 with dissolve
    "Naturally, I was curious as to what that was, but this wasn't the time nor the place. We were on a clock."
    scene w2_4048 with dissolve
    mc "No time to waste. Put the vibrator inside you and I'll explain what the plan is."
    scene w2_4049 with dissolve
    fel "It's not organic chemistry, [mcf]."
    scene w2_4051 with dissolve
    fel "You're going to use this baby to get me juiced up and my thighs quaking while you take photos of Elias and me for \"your paper\"."
    scene w2_4048 with dissolve
    mc "Hey, I put a lot of thought into coming up with an idea that wouldn't risk us getting caught."
    scene w2_4049 with dissolve
    fel "Don't pat yourself on the back too hard, stud. It's a plan straight out of a porno..."
    scene w2_4048 with dissolve
    mc "I thought your perverted side would appreciate it."
    scene w2_4052 with dissolve
    fel "Aw, don't frown. I didn't say it was a {b}bad{/b} idea..."
    fel "Art imitates life, right?"
    scene w2_4053 with dissolve
    fel "There's only one hiccup to your plan..."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_4054 with dissolve
    "*Click*"
    mc "Do tell."
    scene w2_4053 with dissolve
    fel "You brought a horse and buggy when you should've brought a race car."
    scene w2_4052 with dissolve
    fel "Do you think this alone will do anything more than tickle a gal like me? Well, wouldn't be the first time I had to fake it..."
    scene w2_4048 with dissolve

    if kat_polite == True:
        mc "Mrs. Pulman isn't your husband. She'll know the difference."
    else:
        mc "Kat isn't your husband. She'll know the difference."

    scene w2_4055 with dissolve
    mc "Besides, I didn't say I brought only one, did I?"
    scene w2_4056 with dissolve
    mc "There's more where that came from. Four total, to be exact."
    fel "Four...? That's..."
    scene w2_4057 with dissolve
    fel "You trying to make my cooch sound like a maraca?"
    scene w2_4058 with dissolve
    mc "{b}Trust me{/b}. Elias won't notice. Not only can I control the intensity with my phone, but that windbag will be busy talking about himself."
    scene w2_4059 with dissolve
    mc "What was that history taking a long view shit?"
    scene w2_4060 with dissolve
    fel "I still don't know about this..."
    scene w2_4061 with dissolve
    "Seeing Felicia look unsure for once was a tasty treat, one that might've been fun to explore in any other situation."
    mc "Where did your courage suddenly go? I thought you had your reasons."
    scene w2_4062 with dissolve
    fel "..."
    scene w2_4063 with dissolve
    fel "..ah, fuck it. In for a penny, in for a pound."
    scene w2_4064 with dissolve
    fel "Should I do it or do you want to lend me a hand, stud?"
    scene w2_4065 with dissolve
    mc "I'll get a photo of you doing the first two and then I'll get some close-ups of me doing it myself."
    mc "Be mindful of the camera and make it look good."
    stop music fadeout 3.0
    scene black with fade
    fel "{b}That{/b} I won't have a problem with."

label w2FeliciaStuffed:

    if _in_replay:
        show transitionfelicia05 with cmet
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

    scene w2_4066 with fade
    "Not afforded the luxury of taking it nice and easy, Felicia set to task on stuffing her pussy to the brim with the tiny pink devices."
    scene w2_4067 with dissolve
    fel "Ready?"
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_4068 with dissolve
    "*Click*"
    "I nodded and let the sound of the camera's shutter act as my confirmation."
    scene w2_4069 with dissolve
    fel "Don't worry about up there."
    fel "When he says he'll be twenty minutes, it'll be twenty minutes. He's annoying like that..."
    play music "music/ode-to-joy.ogg"
    scene w2_4070 with dissolve
    fel "Still, there's always the chance..."
    "On that nerve-wracked note, Felicia brought the toy down to her lower opening, pressing the miniature gadget against the tender flesh of her labia."
    fel "Here I go."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_4071 with dissolve
    "*Click*"
    scene w2_4072 with dissolve
    "In one quick thrust the toy egg disappeared, gripped tightly by her inner folds and swallowed whole."
    scene w2_4073 with dissolve

    if minaGym == True:
        "I was reminded of Veronica's little educational lecture on the virtues of Kegel exercises."

    fel "Here's the next..."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_4071 with dissolve
    "*Click*"
    scene w2_4072 with dissolve
    "The second egg was gulped down by her lower mouth just as easily as the first."
    scene w2_4074 with dissolve
    fel "It's weird. I'm already feeling full."
    fel "I know I can take more than this..."
    scene w2_4075 with dissolve
    mc "For the remaining pair, go place your palms flat on the edge of the sofa."
    scene w2_4076 with dissolve
    "Felicia cast another fretful glance up toward the door that separated us from discovery. If caught, there would be absolutely no wiggle room for explainations."
    scene w2_4077 with dissolve
    "What would happen afterward? No clue, but in no way would it be good."

    if toughness >=23:
        "It was a thought that, in theory, should've unsettled me."
        scene w2_4078 with dissolve
        mct "(In theory...)"
    else:
        "For the first time since I stepped through the doors, I truly felt the weight of getting swept up in that old woman's whims all in the name of greed."
        scene w2_4079 with dissolve
        "It didn't stop me."

    scene w2_4081 with dissolve
    fel "It's only been a few minutes."
    scene w2_4080 with dissolve
    "Felicia most likely said that to reassure herself, but my reassurance was found somewhere among the hills of tanned flesh that was Felicia's shapely ass."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_4082 with dissolve
    "*Click*"
    scene w2_4083 with dissolve
    mc "Yeah... no worries."
    "We may have had no time to waste, but there was still time."
    scene w2_4084 with dissolve

    if toughness <= 21:
        mc "Ready?"
        scene w2_4085 with dissolve
        fel "Just hurry up."
        scene w2_4084 with dissolve
        mc "Alright, here's number three..."
    else:
        mc "Here I go."

    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_4086 with dissolve
    "*Click*"
    scene w2_4087 with dissolve
    "Just the same as with the other two toys, the third one glided its way inside the tight passage with relative ease until I felt the sensation of plastic clacking against plastic."
    scene w2_4088 with dissolve
    fel "That's... damn, I know I can do more than this, why am I so freakin' stuffed?"
    scene w2_4089 with dissolve
    "The reason for that was obvious; she wasn't aroused."
    scene w2_4088 with dissolve
    fel "Three is all you're going to comfortably get up there, stud."
    scene w2_4089 with dissolve
    "She was right and this was enough. There was no need to push it, other than..."
    "My own personal satisfaction."
    "If she was more turned on, the fourth wouldn't be a problem..."
    hide screen textbox2 with dissolve

    menu w2FeliciaRecall:
        "This isn't the time for that: three will suffice.":
            show screen textbox2 with dissolve
            mct "(Nah. Three will be enough to make her sufficiently squirm.)"
            scene w2_4128 with dissolve
            mc "Three is enough."
            scene w2_4120 with dissolve
            fel "Okay then, I guess..."
            scene w2_4125 with dissolve
            fel "I guess all that's left is to wait for Elias to come back."
            scene w2_4123 with dissolve
            mc "Don't worry."
            "I would do enough of that for both of us."
            mc "In for a penny, in for a pound."
            $ renpy.end_replay()


        "{color=#FF1493}[[Felicia Date]{/color} This is exactly the time to push it: turn her on with story time."(chg=["FeliciaShootPoints_up"]) if feliciaFlag == True:
            $ w2FeliciaPacked = True
            $ w2FelShootPoints += 1
            scene w2_4090 with dissolve
            show screen textbox2 with dissolve
            mc "There's just one more remaining. Go for the gusto?"
            scene w2_4091 with dissolve
            fel "Go for the fuckin' gusto? Why don't you stick it up your ass first and then we can {i}go for the gusto{/i}?"
            scene w2_4092 with dissolve
            "I guess she didn't think it was a good idea."
            scene w2_4093 with dissolve
            play sound "sound effects/slap3.wav"
            scene w2_4094 with hpunch
            "*Slap!*"
            fel "Ghe-!?"
            "The impact of my hand meeting the flesh of Felicia's ass produced a much more potent {b}crack{/b} than expected, reaching all the way to the four corners of the penthouse's high ceiling."
            scene w2_4095 with dissolve
            "It was loud enough that the distinctly sharp sound might've carried all the way up to the ears of Felicia's husband, but it also served its intended purpose."
            scene w2_4096 with dissolve
            fel "What the he--"
            scene w2_4095 with dissolve
            "To focus the blonde's attention on me and segue into the fantasy I was to describe."
            scene w2_4097 with dissolve
            mc "You and I are not alone."
            "A familiar fantasy of the capricious blonde's own making."
            scene w2_4098 with dissolve
            fel "H-huh?"
            scene w2_4099 with dissolve
            mc "You and I, {b}we're not alone{/b}. Remember?"
            mc "We're on stage, with many familiar faces looking at us."
            "I did my best to recall the fantasy she herself weaved that night in the park."
            scene w2_4100 with pixellate
            mc "People of import. People you read about or hear on the news.... businessmen, community leaders..."
            mc "Men of ostensibly good moral fiber."
            scene w2_4102 with pixellate
            fel "Oh..."
            "The connection finally took hold in Felicia's mind."
            scene w2_4103 with dissolve
            fel "This isn't the time for--"
            scene w2_4101 with pixellate
            mc "Tonight though, that facade has been dropped."
            mc "They've been unmasked of their civility and good manners. What they are tonight are... {b}customers{/b}."
            scene w2_4104 with dissolve
            mc "Men who are here to shower you with attention and watch you squirm."
            mc "That's what you like, don't you? Being the center of it all?"
            scene w2_4107 with pixellate
            fel "...yes."
            scene w2_4108 with dissolve
            fel "I... love it."
            scene felh_rub1_a with dissolve
            show felh_rub1
            "Her words matched what her body was telling me. It wasn't much, but the very tips of my fingers felt the bent-over bombshell begin to ooze."
            fel "N-no fair... using my imagination against me like this..."
            "Her words were intonated with a plaintive, puppy-like whine totally unlike the confident woman I knew."
            mc "No fair? Fairness is everyone getting what they need, silly."
            scene w2_4109 with dissolve
            fel "G-guheeoh...?"
            mc "It's not my fault what you need is so filthy."
            scene w2_4110 with dissolve
            "Flipping things around on her was getting me excited, but..."
            scene w2_4111 with dissolve
            mct "(I needed to remain mindful)."
            mc "Of course, need and want are two separate things."
            scene w2_4104 with pixellate
            mc "The woman I'm seeing ain't the prim and proper picture-perfect wife of Elias Ford, is it?"
            mc "What do I see, Felicia?"
            scene w2_4105 with dissolve
            fel "...a cock hungry bitch begging for release."
            mc "Bingo! All I see is a bitch ready for the taking, who wants her pussy split open by a fat cock."
            scene felh_rub2_a with dissolve
            show felh_rub2
            mc "But I'm not going to give you what you want. An unfaithful wife like you doesn't deserve that."
            mc "Instead, you'll get what you need: an ass fucking."
            fel "C'mon- this is-Ah~ g-getting~ nngh..!"
            scene felh_rub3_a with dissolve
            show felh_rub3
            fel "Mmmhhh-?!"
            mc "You got to be quieter than that, Felicia."
            fel "M-mmh..!"
            scene w2_4106 with pixellate
            mc "That's right, what you need..."
            mc "I'll rail your ass over and over again, plunging every inch of my cock straight into your guts."
            scene felh_rub3_a with dissolve
            show felh_rub3
            fel "Mmuuh...!"
            mc "Every thrust fucking more and more sense out of you until you're reduced to a babbling slab of meat."
            "I colored my words to match the vivacity of Felicia's own telling."
            scene w2_4112 with dissolve
            mc "Every hit sends your ass quaking..."
            play sound "sound effects/slap2.wav"
            scene w2_4113 with vpunch
            "*Smack!*"
            scene felh_rub3_a with dissolve
            show felh_rub3
            mc "Every hit causes your bowels to tighten and spasm around my girth."
            fel "Mumaah...!"
            mct "(This is fun, but I'm getting too carried away here.)"
            "Felicia was sufficiently aroused for the fourth toy; my hand was smattered in her feminine juices."
            mc "You'll lose all sense of time..."
            fel "Ghmmyshuit!"
            mc "The only marking of its passage will be a growing amount of jizz filling your belly."
            mc "More and more will pack your bowels until..."
            scene w2_4114 with dissolve
            fel "W-wha... h-huh...?"
            "The abrupt stop confused the lust-dazed blonde."
            scene w2_4115 with dissolve
            fel "I can't believe I let myself get so..."
            scene w2_4116 with dissolve
            "*Squelch*"
            scene w2_4117 with dissolve
            "In her stupor, all it took was one quick motion and Felicia's pussy gleefully gobbled up the egg-shaped toy."
            play sound "sound effects/camera-phone-shutter.wav"
            scene w2_4118 with dissolve
            "*Click*"
            mc "There..."
            scene w2_4119 with dissolve
            "*Pat, pat*"
            mc "We both knew you could do four."
            scene w2_4120 with dissolve
            fel "Huh...? Oh yeah..."
            scene w2_4121 with dissolve
            "A few more blinks had Felicia better oriented."
            scene w2_4122 with dissolve
            fel "THAT was what this was all about..."
            scene w2_4123 with dissolve
            mc "The vaginal canal expands like an accordion when aroused. Isn't the human body magical?"
            scene w2_4124 with dissolve
            fel "Oh look, a man thinking he needs to explain how a woman's body works to a..."
            scene w2_4125 with dissolve
            fel "Ah, shit."
            fel "No harm, no foul."
            scene w2_4126 with dissolve
            fel "That was.... wild, stud. Wild, but fun."
            fel "Who knew you had it in you?"
            $ renpy.end_replay()
            scene w2_4127 with dissolve
            "Without missing a beat, Felicia had reckoned with the abrupt attack and taken it with patented nonchalance."


        "{color=#696969}[[Felicia Date]{/color} This is exactly the time to push it: turn her on with story time." if feliciaFlag == False:
            jump w2FeliciaRecall


    if not persistent.w2FeliciaEggStuff:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w2FeliciaEggStuff = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)

    scene w2_4129 with dissolve
    mc "How do you feel?"
    fel "...how do I feel?"

    scene w2_4130 with dissolve
    if w2FeliciaPacked == True:
        fel "Not too bad surprisingly. It's a little odd, but nothing I can't handle."
        mc "I'm glad to hear that."
    else:
        fel "Like I'm walking around with a roll of quarters stuffed up my twat."
        mc "You'll manage."

    scene w2_4131 with dissolve
    mc "Now, how about that drink? Oh, and just in case, put some music on. It'll mask the buzz of the motors."
    stop music fadeout 3.0
    scene black with fade
    fel "Damn it... I'm trusting you here, [mcf]."

label w2FeliciaConvoTease:
    if _in_replay:
        show screen textbox2 with dissolve
    scene w2_4132 with fade
    "Just like Felicia predicted, Elias returned twenty minutes on the dot in an eerie display of punctuality."
    el "I apologize for the interruption, but there's been an extraordinary dispute at the agency that I've needed to closely monitor for the past few days."
    "Naturally, she took her place next to her husband, quim stuffed full of sex toys and an uneasy smile on her face as she waited for the figurative shoe to drop."
    mc "That's quite alright, I'm here at your leisure. It must be quite serious if you need to be involved, though."
    play music "music/impertinence.ogg"
    scene w2_4134 with dissolve
    "She was entirely at my mercy. At any moment, I could activate the toy eggs with my phone."
    scene w2_4133 with dissolve
    el "Serious? Not yet, but... I've learned that, in the talent industry, no problem is too small. The pettiest squabble can suddenly explode into an insurmountable quagmire when a star's ego is involved."
    scene w2_4134 with dissolve
    "No matter my complicated feelings, that knowledge alone was a tasty erotic delight."
    scene w2_4135 with dissolve
    fel "It's night and day from Elias' previous work."
    scene w2_4136 with dissolve
    el "Oh, you're quite right about that, honey. Logistics may be in my blood, but cultivating talent is my calling."
    el "Every client is a one-and-only product, each offering their own unique set of problems. It's just simply more... {i}intellectually{/i} stimulating."
    scene w2_4137 with dissolve
    mc "Can you give me an example?"
    scene w2_4138 with dissolve
    el "Hmm, well--"
    mc "Oh! Wait a sec, I should record our conversation for my notes."
    play sound "sound effects/phonemenu.wav"
    scene w2_4139 with dissolve
    "*Beep*"
    "Cloaked with the subterfuge of journalistic intent, I turned Felicia's vibrators on and set them on low."
    $ renpy.music.set_volume(.3, 0, channel = "sound")
    play sound "sound effects/vib-start.wav"
    scene w2_4140 with dissolve
    "Her reaction was immediate, her face contorted in surprise and her thighs defensively clamped shut in a futile attempt to abate the sudden sensation."
    el "You're good! I wasn't intending to get started on this yet, but you've got me on my favorite subject already."
    scene w2_4141 with dissolve
    mct "(Yourself?)"
    "That wasn't hard, asshole."
    scene w2_4142 with dissolve
    el "Felicia..."
    fel "Uh.. huh?"
    scene w2_4143 with dissolve
    el "Go and grab us a couple of beers."
    fel "S-sure thing, hun."
    scene w2_4144 with dissolve
    el "Are you... feeling alright?"
    "Felicia fell under the squirrely man's analytic gaze, but quickly recovered her senses and played it off."
    scene w2_4145 with dissolve
    fel "I am, but thanks for your concern, husband."
    scene w2_4146 with dissolve
    "A peck on the forehead and a reassuring smile to mask the mild stimulation she was enduring."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_4147 with dissolve
    "*Click*"
    scene w2_4148 with dissolve
    "The sound of the camera's shutter focused the couple's attention on me."
    mc "Sorry, probably won't use it for the article, but... cute moment. Couldn't resist."
    scene w2_4149 with dissolve
    el "That's quite alright, take as many photos as you need."
    play sound "sound effects/slap1.wav"
    scene w2_4150 with vpunch
    el "Now, about those beers."
    fel "Right on it!"
    scene w2_4151 with dissolve
    "With an energetic step, Felicia sashayed off toward the bar."
    el "Now, you asked me about the unique problems that come with working with models and actresses, right?"
    mc "I did. You called it intellectually stimulating."
    scene w2_4152 with dissolve
    el "Well, let's take this week's kerfuffle as our example."
    el "Our firm has an unexpected rising star. She's not particularly talented, but she's exceptionally beautiful and has captured the public's interest after a breakout role in a beloved series."
    scene w2_4153 with dissolve
    el "More often than not in this business, success is a fragile and capricious thing. It ignites quickly like a pan fire, but is just as easily squandered if you don't correctly anticipate what's needed to sustain and grow it."
    scene w2_4154 with dissolve
    el "Great so far, but this is where the friction begins..."
    scene w2_4155 with dissolve
    "Once Felicia reappeared from beneath the bar, I could tell that even on the lowest intensity, the vibrators were doing their job in stimulating the wifely blonde."
    scene w2_4156 with dissolve
    el "Her agent is a young man, yet to cut his teeth but astute and brimming with potential. A prospective loyal and long-term asset if given the right challenges to grow."
    "She was hunched over from titillation and her face flush. A mere walk to the bar really did a number on her."
    scene w2_4157 with dissolve
    el "You see, a good agent can be worth more than a star..."
    mct "(Hmm...)"
    "Not only that, but Felicia left her phone on the bar earlier."
    mct "(If I'm quick about it, I could...)"
    hide screen textbox2 with dissolve

    menu:
        "Use it to have her secretly expose herself for a photo."(chg=["FeliciaShootPoints_up2"]):
            $ w2FelShootPoints +=2
            show screen textbox2 with dissolve
            "If I'm quick about it, I could send her a message."
            "Not letting the chance to directly communicate with her pass, I picked up my phone and shot Felicia a text while her husband enumerated on the virtues of a good talent agent."
            scene w2_4158 with dissolve
            "Bzzt... bzzzt...!"
            scene w2_4159 with dissolve
            el "The problem is she's..."
            scene w2_4160 with dissolve
            el "...been carrying on about how insulting it is having a newbie represent her."
            scene w2_4161 with dissolve
            mc "Has he done a poor job?"
            scene w2_4162 with dissolve
            "Felicia could have simply ignored my request, but instead with next to no hesitation..."
            el "Not in the least. I have full confidence in the boy's ability as an agent."
            scene w2_4163 with dissolve

            if kat_polite == True:
                "She struck while the iron was hot, seizing the opportunity to fulfill Mrs. Pulman's expectations while Elias was utterly distracted by his own yammering."
            else:
                "She struck while the iron was hot, seizing the opportunity to fulfill Kathleen's expectations while Elias was utterly distracted by his own yammering."

            mc "Oh, hold that!"
            scene w2_4164 with dissolve
            mc "You're looking quite dapper."
            el "Really?"
            "The fact that not fifteen feet behind him, this powerful man's wife was exposing herself to me had me feeling like a conqueror even though I logically knew my charms and merits as a man had nothing to do with it."
            play sound "sound effects/camera-phone-shutter.wav"
            scene w2_4165 with dissolve
            "*Click*"
            mc "Oh, yeah. Ring-a-ding-ding, right?"
            play sound "sound effects/camera-phone-shutter.wav"
            scene w2_4166 with dissolve
            "*Click*"
            "Elias smiled at the overly generous comparison, unbeknownst to him that his wife's naked fat tits had him looking less like The Rat Pack and more like a complete fool."
            "{b}This{/b} was the kind of shit the old woman was looking for from tonight."
            play sound "sound effects/camera-phone-shutter.wav"
            scene w2_4167 with dissolve
            "*Click*"
            "The club's patrons would salivate at the chance to feel superior to someone who is ostensibly one of their peers."
            scene w2_4168 with dissolve
            mc "I apologize for stopping you mid-convo like that, but sometimes inspiration strikes."
            el "You have your job to do, I understand."
            mct "(You very much don't...)"
            scene w2_4169 with dissolve
            mc "You were saying you had full confidence in the agent representing your diva."
            el "Ah, that's right..."
        "Forget about it. Just snag a photo of Felicia flustered.":



            scene w2_4170 with dissolve
            show screen textbox2 with dissolve
            el "The problem is she's been carrying on about how insulting it is to have a newbie represent her."
            mc "Has he done a poor job?"
            "I weighed the value of directly instructing the stimulated blonde with the riskiness of what I was thinking and, at least for now, ultimately let caution win out."
            play sound "sound effects/camera-phone-shutter.wav"
            scene w2_4171 with dissolve
            "*Click*"
            scene w2_4172 with dissolve
            el "Not in the least. I have full confidence in the boy's ability as an agent."
            scene w2_4171 with dissolve
            "Plus, there's a less overt option. For example, the toys tickling her insides are only on the lowest setting..."

    scene w2_4173 with dissolve
    el "Most firms would probably balk at the idea of pairing an unproven agent with a star talent, but that's one of our competitive edges at EBF Talent."
    el "Good help is hard to come by and our most important resource isn't our models or actresses; those are a dime a dozen."
    scene w2_4174 with dissolve
    el "We believe -- thanks, hun -- ... we believe our most fundamental resources are the men and women that facilitate our talent's success."
    mc "That makes sense. Can't have one without the other."
    scene w2_4175 with dissolve
    el "Precisely, and what better way of cultivating both other than linking the success of a young agent with that of a young star?"
    scene w2_4176 with dissolve
    mc "It's also about loyalty, right?"
    scene w2_4177 with dissolve
    el "{b}Very{/b} perceptive, Charles! For our agents, we give our fledgling employees a chance to flourish far sooner than they would at any other agency. That leads to loyalty on their part."
    scene w2_4178 with dissolve
    fel "Here you are, Mr. Bukowski."
    scene w2_4179 with dissolve
    "Having done a commendable job of adjusting to the pink toys' endlessly vibrating assault, Felicia stood in front of me with a beer outstretched and looking relatively normal."
    scene w2_4180 with dissolve
    mc "Thank you, Mrs. Ford."
    scene w2_4181 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Keep her on her toes: set the toys to medium intensity.":
            scene w2_4182 with dissolve
            show screen textbox2 with dissolve
            el "For our talent.... loyalty to their agent is tantamount to loyalty to my firm."
            mc "If you consider that your competitive edge..."
            play sound "sound effects/phonemenu.wav"
            scene w2_4183 with dissolve
            "*Beep*"
            mc "...isn't that easily imitated?"
            $ renpy.music.set_volume(.4, 0, channel = "sound")
            play sound "sound effects/vib-start.wav"
            scene w2_4184 with dissolve
            "Felicia was stopped in her tracks, but she commendably endured with nary a peep."
            el "Now, now... I said it's one of them. We don't just sign any talentless hack with any two-bit agent."
            scene w2_4185 with dissolve
            "As expected, Elias didn't even notice Felicia catching her breath. He was too wrapped up in talking about himself."
            el "It's a strategy that only works if it's employed by a world-class firm, staffed by people with a keen eye for the 'X' factor and a brand image that attracts the cream of the crop."
            scene w2_4186 with dissolve
            fel "...!"
            mc "Ah, so the real secret sauce is to be good at your job?"
            el "You said it! We're not selling fried chicken here!"
            scene w2_4187 with dissolve
            mc "So what do you do when one of your clients wants a more experienced representative?"
            scene w2_4188 with dissolve
            el "All I do is monitor the situation, do you know why?"
            play sound "sound effects/camera-phone-shutter.wav"
            scene w2_4189 with dissolve
            "*Click*"
            if kat_polite == True:
                "While she was still looking uneasy, I made sure to snap a picture. I wasn't sure how much of the story would be conveyed in a static sequence of images, but I trusted Mrs. Pulman would provide ample context to her audience."
            else:
                "While she was still looking uneasy, I made sure to snap a picture. I wasn't sure how much of the story would be conveyed in a static sequence of images, but I trusted Kathleen would provide ample context to her audience."

            mc "I could hazard a guess."
            scene w2_4190 with dissolve
            el "I would love to hear it."
        "Give her a shock: set the toys to high intensity."(chg=["felicia_down", "FeliciaShootPoints_up"]):

            $ w2FeliciaHigh = True
            $ w2FelShootPoints +=1
            $ Felicia_Affection -=1
            scene w2_4182 with dissolve
            show screen textbox2 with dissolve
            el "For our talent.... loyalty to their agent is tantamount to loyalty to my firm."
            mc "If you consider that your competitive edge..."
            play sound "sound effects/phonemenu.wav"
            scene w2_4191 with dissolve
            "*Beep*"
            scene w2_4192 with dissolve
            fel "G-guh..?!"
            "Felicia, to her credit, stifled her surprise as best she could, but it still sounded like she was sucking down air."
            $ renpy.music.set_volume(.6, 0, channel = "sound")
            play sound "sound effects/vib-start.wav"
            scene w2_4193 with dissolve
            "Elias, just as I expected, was so wrapped up in talking about himself that he didn't notice his wife's abrupt distress."
            mc "...isn't that easily imitated?"
            "How a man so seemingly anal-retentive didn't notice something right next to him might boggle the mind, but I understood it. His meticulousness only extended to things he considered worth the energy."
            scene w2_4194 with dissolve
            el "Now, now... I said it's one of them. We don't just sign any talentless hack with any two-bit agent."
            el "It's a strategy that only works if it's employed by a world-class firm, staffed with people with a keen eye for the 'X' factor and a brand image that attracts the cream of the crop."
            "That is how men like him pull ahead."
            scene w2_4195 with dissolve
            mc "Ah, so the real secret sauce is to be good at your job?"
            el "You said it! We're not selling fried chicken here!"
            scene w2_4196 with dissolve
            "My focus wasn't nearly as honed as his. It took one hundred percent of my willpower to channel my attention on Elias and not the bikini-clad blonde squirming nearby."
            scene w2_4187 with dissolve
            mc "So what do you do when one of your clients wants a more experienced representative?"
            scene w2_4197 with dissolve
            fel "Mmmh..!"
            el "All I do is monitor, do you know why?"
            play sound "sound effects/phonemenu.wav"
            scene w2_4198 with dissolve
            "*Click*"
            mc "I could hazard a guess."
            "Wary of knocking her off her feet, I set the intensity down to medium."
            scene w2_4199 with dissolve
            fel "...!"
            play sound "sound effects/camera-phone-shutter.wav"
            scene w2_4189 with dissolve
            "*Click*"
            if kat_polite == True:
                "While she was still reeling from the shock, I made sure to snap a picture. I wasn't sure how much of the story would be conveyed in a static sequence of images, but I trusted Mrs. Pulman would provide ample context to her audience."
            else:
                "While she was still reeling from the shock, I made sure to snap a picture. I wasn't sure how much of the story would be conveyed in a static sequence of images, but I trusted Kathleen would provide ample context to her audience."

            scene w2_4190 with dissolve
            el "I would love to hear it."

    $ renpy.music.set_volume(1, 0, channel = "sound")
    scene w2_4189 with dissolve
    "Elias looked at me intently, waiting to make an appraisal of my answer."
    "I didn't give a shit what he thought of me, but I was moderately curious if I had the mindset to rub elbows with a man like him. I carefully considered it, before answering..."
    hide screen textbox2 with dissolve

    menu:
        "He has more important things to do.":
            show screen textbox2 with dissolve
            mc "You have more important things to do?"
            scene w2_4200 with dissolve
            el "I already told you, the smallest issues have a tendency to snowball out of control. Therefore, problems are rarely beneath me."
            scene w2_4201 with dissolve
            mc "Then why?"
            scene w2_4200 with dissolve
            el "Well, simply put... the problem warrants my attention, but the solutions are beneath me."
            scene w2_4201 with dissolve
            mc "...that's what your employees are for."
            scene w2_4202 with dissolve
            el "Exactly. The agency would not be nearly as prosperous if it relied solely on my limited problem solving skills."
            scene w2_4203 with dissolve
            fel "A good boss knows how to delegate."
            scene w2_4204 with dissolve
            fel "That's why you're the..."
            scene w2_4205 with dissolve
            fel "...!"
            scene w2_4204 with dissolve
            fel "...man in charge, hun."
        "Smoothing things out with his client is the young agent's job.":


            show screen textbox2 with dissolve
            show screen textbox2 with dissolve
            mc "Is it because it's her agent's job to endear himself to her and solve the problem?"
            mc "If he can't do that, he shouldn't even work for you."
            scene w2_4202 with dissolve
            el "That's precisely one of the underlying reasons, yes. You have a good head on you."
            el "I have complete faith in the men and women I hire, but that said I'm not infallible. If I've misjudged her agent's abilities... well, that's why I keep an eye on it."
            scene w2_4203 with dissolve
            fel "Trust, but verify..."
            scene w2_4204 with dissolve
            fel "That's why you're the..."
            scene w2_4205 with dissolve
            fel "...!"
            scene w2_4204 with dissolve
            fel "...man in charge, hun."
        "Giving the talent what she wants will cause bigger headaches down the line."(chg=["tough_up","felicia_down"]):


            $ Felicia_Affection -=1
            $ toughness += 1
            show screen textbox2 with dissolve

            if trait_governor == True or toughness >= 22:
                mc "You can't expect to control the talent if you easily give into their whims."
            else:
                mc "You can't work together smoothly if you just immediately acquiesce to such a large demand."

            mc "Instantly giving a diva what she wants, even if it's valid, will just further empower her to push back in the future."
            scene w2_4207 with dissolve
            el "That's right! It's always best to let things simmer for a while and see how it plays out."
            el "If her demand is invalid, my man will convince her he's the right person to represent her. If he can't do that..."
            scene w2_4206 with dissolve
            mc "Let her sweat a little and get her to be thankful you sided with her."
            scene w2_4202 with dissolve
            el "{b}Very{/b} good. That's exactly right."
            el "Managing people isn't all that different from accounting for problems in a supply chain."
            scene w2_4203 with dissolve
            fel "You..."
            scene w2_4205 with dissolve
            fel "...!"
            scene w2_4204 with dissolve
            fel "...need to know your points of failure and plan accordingly."
            scene w2_4208 with dissolve
            el "That's... right. Have you said that before?"
            scene w2_4209 with dissolve
            fel "We've been married for eight years, I'm bound to have absorbed some of your {i}wisdom{/i}. Plus..."
            fel "It's common sense to always have a backup plan."

    scene w2_4210 with dissolve
    "Felicia speaking up and placing herself in the conversation supplied me with an idea."
    scene w2_4211 with dissolve
    mc "How did you two meet?"
    scene w2_4212 with dissolve
    el "Oh, you don't want to hear about that. Felicia and I love each other very much, but our story isn't anything special."
    el "Wouldn't you rather hear about my conservation work or city initiatives?"
    scene w2_4213 with dissolve
    mc "Absolutely, but I'm also here to learn more about the man who has it all, and I do mean {b}all{b}, Elias."
    mc "Trust me, our {i}subscribers{/i} would be {b}delighted{/b} to \"read\" about your romantic life -- not in a gossip mag sort of way mind you, just... it's reaffirming to know that someone with your level of success can also have an enviable marriage."
    scene w2_4214 with dissolve
    el "Hmm, very well. I suppose a few questions on the subject wouldn't hurt before we move onto other topics I'd like to discuss."
    "The mission was about taking photos, but..."
    scene w2_4215 with dissolve
    el "Now, what was it that you asked? How did Felicia and I meet?"
    scene w2_4216 with dissolve

    if kat_polite == True:
        "Mrs. Pulman would no doubt listen and maybe even make use of this recording. Plus, I would like to know more about Felicia."
    else:
        "Kathleen would no doubt listen and maybe even make use of this recording. Plus, I would like to know more about Felicia."
    hide screen textbox2 with dissolve

    menu:
        "Let Elias answer the question.":

            scene w2_4217 with dissolve
            show screen textbox2 with dissolve
            mc "That's right. Where did you find such a lovely woman as your wife?"
            mc "I know you didn't meet in line while getting coffee."
            scene w2_4218 with dissolve
            el "Not coffee no, but... {i}wine{i}."
            scene w2_4219 with dissolve
            el "I first laid eyes on Felicia at the grand opening of a mutual acquaintance's winery."
            scene w2_4220 with dissolve
            fel "Hmpfh. {size=-10}Right...{/size=-10}"
            scene w2_4219 with dissolve
            el "She was there with someone, but--"

            if w2FeliciaPacked == True:
                scene w2_4221 with dissolve
                fel "T-that {b}someone{/b}... wasn't anything serious... just a friend."
                scene w2_4222 with dissolve
                "Given the circumstances, with her cunt packed full of four endlessly jostling sex toys, Felicia did an admirable job supporting her husband's story as he no doubt expected."
            else:
                scene w2_4223 with dissolve
                fel "That {i}someone{/i}... wasn't anything serious, mind you. It was a... friend..."
                scene w2_4224 with dissolve
                "Given the circumstances, with three vibrators incessantly going to town on her lady parts, Felicia did an admirable job supporting her husband's story as he no doubt expected."

            scene w2_4225 with dissolve
            el "She was there with someone, but as soon as I saw her I knew..."
            scene w2_4226 with dissolve
            "Elias paused for a moment, pretending to dig deep and mine the words from within a dramatic pause while his wife beside him coped the best she could with the building pleasure."
            scene w2_4227 with dissolve
            el "It had only been a year since my previous wife passed, but I knew I wanted to take my chance. There was just something..."
            scene w2_4228 with dissolve
            el "Something...?"
            scene w2_4229 with dissolve
            fel "--!"
            play sound "sound effects/camera-phone-shutter.wav"
            scene w2_4230 with flash
            "*Click*"
            "Another fabricated pause provided the right cover to snap another photo of Felicia's wretched expression."
            scene w2_4231 with dissolve
            "Meanwhile, he just smiled at me, thinking he allowed me to capture a vulnerable moment of his."
            scene w2_4232 with dissolve
            el "There was just something captivating about her."

            if w2FeliciaHigh == True:
                scene w2_4233 with dissolve
                fel "Ge--!"
            else:
                scene w2_4234 with dissolve
                fel "{size=-10}...mh!{/size=-10}"

            el "She worked the courtyard flawlessly, juggling conversations while moving from group to group."
            scene w2_4235 with dissolve
            el "Thankfully, she approached me and I somehow conned her into a date."
        "Pivot to Felicia."(chg=["felicia_up"]):

            $ Felicia_Affection +=1
            scene w2_4237 with dissolve
            show screen textbox2 with dissolve
            mc "I'd like to ask Mrs. Ford that, if you don't mind."
            fel "..e-eh...?"
            "Felicia was caught off guard by the conversational hot potato."
            scene w2_4238 with dissolve
            el "Her...? Well..."
            scene w2_4239 with dissolve
            el "Of course I don't mind. She'll tell it better than I."
            scene w2_4240 with dissolve
            mc "I know you two didn't meet while waiting in line for coffee. So where did you first cross paths?"
            scene w2_4241 with dissolve
            fel "No, no coffee... I first met Elias at a..."
            scene w2_4242 with dissolve
            fel "We met at a brewery."
            scene w2_4243 with dissolve
            fel "It was the grand opening of a mutual acquaintance's brewery. I was there with..."
            scene w2_4222 with dissolve
            "...!"
            "For the briefest of a second, the words were momentarily stricken from her throat by a jolt of pleasure."
            scene w2_4221 with dissolve
            fel "...someone."
            scene w2_4224 with dissolve
            el "I remember the disheartening feeling when I thought you were there with another man."
            "Elias leapt at the chance to add to the conversation."
            scene w2_4223 with dissolve
            fel "Lucky for you it was only a friend..."
            scene w2_4225 with dissolve
            fel "--!"
            el "Lucky indeed."
            scene w2_4244 with dissolve
            mc "Did you know who he was when you first met?"
            scene w2_4245 with dissolve
            fel "At first glance, but I pretended I didn't. I took my time in approaching him."
            scene w2_4244 with dissolve
            mc "You were interested in him from the start?"
            scene w2_4245 with dissolve
            fel "Naturally."

            if w2FeliciaPacked == True:
                scene w2_4246 with dissolve
                el "Ha, but she took her sweet-ass time getting to me!"
                "While Elias elbowed his way into answering the question, Felicia's face made all sorts of wonderful expressions as she endured the sensation of four vibrators ceaselessly tormenting her cunt."
            else:
                scene w2_4247 with dissolve
                el "Ha, but she took her sweet-ass time getting to me!"
                "While Elias elbowed his way into answering the question, Felicia's expression contorted in apprehension as she endured the sensation of three vibrators going to town on her cunt."

            scene w2_4248 with dissolve
            el "I thought about approaching her myself, but I always got pulled in another direction."
            el "Luckily, by the end of the night..."
            scene w2_4249 with dissolve
            fel "...!"

            "The look on Felicia's face told me what I needed to do."
            play sound "sound effects/camera-phone-shutter.wav"
            scene w2_4250 with dissolve
            "*Click*"


            if w2FeliciaHigh == True:
                scene w2_4251 with dissolve
                fel "Ge--!"
            else:
                scene w2_4252 with dissolve
                fel "{size=-10}...hm!{/size=-10}"

            scene w2_4235 with dissolve
            el "...we had hit it off and I managed to con her into a date."


    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_4236 with dissolve
    "*Click*"
    mc "Where was your first date?"
    el "We flew out to..."
    scene w2_4253 with dissolve
    "*Beep, beep*"
    el "I flew her out to Paris and..."
    scene w2_4254 with dissolve
    el "Hmm..."
    el "We spent a whole week going to art galleries and seeing other sights."
    scene w2_4255 with dissolve
    mc "That's quite the first date..."
    el "I was trying painfully hard to impress her."
    scene w2_4256 with dissolve
    fel "It worked, as you... can... tell."
    scene w2_4257 with dissolve
    el "Listen, I'm sorry to have to do this, but we'll need to wrap this up over the next thirty minutes or so."
    mc "I understand. Your time is extremely valuable."
    scene w2_4258 with dissolve
    el "Yeah... something like that. I'm going to go make a quick call."
    el "Felicia will show you up to my office in five minutes and then I'll go over all the things I want you to write about."
    "He spoke like it was entirely his decision alone."
    mc "I have no objections to that."
    scene w2_4259 with dissolve
    el "...what's wrong with you? You look tired."
    scene w2_4260 with dissolve
    fel "Ah... it's... the humidity, hun."
    scene w2_4261 with dissolve
    el "Eh? It's not that bad?"
    scene w2_4262 with dissolve
    el "Now..."
    stop music fadeout 3.0
    scene black with fade
    el "If you'll excuse me, I need to go contact that agent we spoke of. It looks like he's managed to smooth things out."
    scene w2_4263 with fade
    "Once more, Felicia and I were temporarily alone."
    scene w2_4264 with dissolve
    "Giving a repeat performance from earlier, she jolted from her seat and stormed up to me."
    "In her wake, she left a glistening puddle of femspunk caked onto her seat."
    scene w2_4265 with dissolve
    mc "That went pretty--"
    scene w2_4266 with dissolve
    fel "Give me that!"
    "Swiping my phone from my hand, she..."
    play sound "sound effects/phonemenu.wav"
    scene w2_4267 with dissolve
    "*Beep*"
    "...relieved herself from the continual pulsated assault on her quim."
    scene w2_4268 with dissolve
    fel "Fuck me, this was fun!!"

    if feliciaFlag == True and Felicia_Affection >= 16:
        play music "music/romantic-motivation.ogg"
        scene w2_4269 with dissolve
        "{i}Fun{i}."
        scene w2_4270 with dissolve
        "That was the word she used."
        scene w2_4271 with dissolve
        mc "Are you about to..."
        scene felh_kiss_a with dissolve
        show felh_kiss
        mc "...mh?!"
        "Not terrifying. Not {i}shameful{/i}, but {b}fun{/b}."
        "So enflamed by her secretive performance, she pulled me into a kiss of unabashed passion the likes I had never experienced."
        "I was suddenly on the back foot, wilting from the unexpected intensity and fervor of Felicia's abrupt amorous advance."
        "If I had allowed myself to get swept up inside the old woman's game of dominance and control, Felicia had wrested that feeling from my lizard brain with a lone kiss."
        "There was platonic kissing, kissing for love, and then there was..."
        scene w2_4272 with dissolve
        "Kissing to fuck."
        scene w2_4273 with dissolve
        fel "What the hell is wrong with me?"
        scene w2_4272 with dissolve
        "She kissed me like she wanted to fuck."
        scene w2_4274 with dissolve
        mc "What the hell is wrong with us, the old woman, or the patrons at the club?"


    scene w2_4275 with dissolve
    fel "That was... new. I'm glad as shit I signed up for this."
    scene w2_4276 with dissolve
    "She said something shocking and entirely in character at the same time."
    scene w2_4275 with dissolve
    fel "Fuck you, dickhead."

    if feliciaFlag == True and Felicia_Affection >= 16:
        "There was more than hedonistic glee in her words. There was an animosity for the man she was spitting poison at."
    else:
        "Instead of exasperation toward me, she directed it elsewhere with a mixture of excitement and animosity to her voice."


    scene w2_4277 with dissolve
    fel "I've lived thirty-four years and I'm still finding new ways to tickle myself. Isn't life grand?"
    scene w2_4278 with dissolve
    mc "I..."
    stop music fadeout 3.0
    scene w2_4279 with dissolve
    "That was when it hit me. In the face of Felicia's exuberance, I was forced to reconcile the absurdity of this situation, and all the anxiety I pushed aside to be able to excel closed in on itself like the Red Sea."
    mc "H-holy shit..."
    "It wasn't the immorality of the evening that had suddenly encumbered me, but something far more simple."
    scene w2_4280 with dissolve
    "Fear."
    $ renpy.end_replay()
    fel "Are you okay, stud?"
    scene w2_4281 with dissolve
    "The panic, delayed as it was, had finally set in."
    mc "Yeah, I just... need a sec for my brain to catch up with what just happened."
    scene w2_4282 with dissolve
    fel "Seriously? You were acting so cool that I was taking it a little personally."
    scene w2_4283 with dissolve
    "I had never viewed my personal detachment as a plus. In my mind, it was something I had to work around if I wanted to fit in."
    scene w2_4284 with dissolve
    mc "Ha, yeah... I'd never seen you so worried."
    "...but that detachment had never been stretched this thin - toying with a woman while she sat next to her unaware husband, all under the guise of being someone I wasn't was far and away the most egregious thing I had ever done."
    scene w2_4285 with dissolve
    fel "Well... take a breath. It's alright."
    "The fact this wasn't lost on me and was currently weighing me down on my chest like a ton of bricks, made me... {b}happy{/b}."
    fel "...and now you're smiling?"
    scene w2_4286 with dissolve
    "Stupid and unabashedly happy."
    mc "It's just..."
    mc "I may just be more screwed in the head than you are."
    scene w2_4287 with dissolve
    fel "Hmpfh..."
    scene w2_4288 with dissolve
    fel "I doubt it, but let's not turn it into a competition."
    scene w2_4289 with dissolve
    fel "I'll get you a drink of water to help settle your nerves and then I'll lead you up so you can play some make-believe with Elias."
    scene w2_4288 with dissolve
    fel "The evening ain't quite over, is it stud?"

    if not persistent.w2FeliciaConvoTease:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w2FeliciaConvoTease = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)

    scene black with fade
    "She wasn't wrong."
    "......"
    "..."
    play sound "sound effects/door-openclose.wav"
    scene w2_4290 with fade
    play music "music/air-on-g.ogg"
    "As soon as I entered Elias' office, the man was there to greet me, standing waiting like a sentry."
    scene w2_4291 with dissolve
    el "It occurs to me I haven't thanked you for your interest in doing a profile on me."
    scene w2_4292 with dissolve
    mc "That's a two-way street, Elias. You're doing me the favor here."
    scene w2_4293 with dissolve
    mc "To be honest, my boss isn't too impressed with me lately. This exclusive should get him off my back."
    "I shocked myself with how easily I added to the deception without even flinching."
    scene w2_4294 with dissolve
    mc "These are your kids?"
    scene w2_4295 with dissolve
    el "They are. I gave my late wife a daughter and she blessed me with a son."
    el "They're at our summer home at the moment."
    scene w2_4296 with dissolve
    mc "Too bad. I would've liked to meet them."
    "As if."
    "I've tutored a dozen rich brats like them."
    el "If not for St. Ives, they would spend more than their summers there. The city is no place to raise children, in my opinion."
    scene w2_4297 with dissolve
    mc "Is that why you're pushing for the city to allocate more space for public parks?"
    scene w2_4298 with dissolve
    el "It could use it, don't you agree? All the concrete and steel is suffocating."
    el "It's one of the many things I'd like to change about Morehead Hills."
    scene w2_4297 with dissolve
    mc "Sounds like you should run for mayor."
    scene w2_4299 with dissolve
    el "..."
    "He smiled and I could see him weigh his answer in his head."
    scene w2_4300 with dissolve
    el "If there exists a need."
    el "For now, I prefer to let other people fight for and spend their political capital."
    scene w2_4301 with dissolve
    el "Take a seat, Charles."
    scene w2_4302 with dissolve
    mc "Who's that in the portrait behind you?"
    scene w2_4303 with dissolve
    el "My father. He was a great man, charged with the unenviable task of modernizing under the weight of a dying industry's carcass."
    el "It didn't survive of course, but our name did."
    scene w2_4304 with dissolve
    mc "He kept it relevant with his philanthropy, right?"
    "...and guided the Ford family fortune's precipitous decline with a series of bad investments."
    el "Good deeds outlast men."
    scene w2_4305 with dissolve
    "The Ford family is still \"rich\" of course, by mine and most people's standards, but it's a paltry sum in comparison to what it was."
    scene w2_4306 with dissolve
    mc "Well, then... let's talk about your own philanthropic interests, Elias."
    scene black with fade
    "And so we did."
    scene w2_4307 with fade
    "For ten minutes, he talked my ear off about things that I nor anyone else in Morehead Hills gave a shit about."
    scene w2_4308 with dissolve
    "He talked about his three initiatives and what he hoped they would accomplish for the city."
    scene w2_4309 with dissolve
    "Some of them weren't bad per se, in fact all of them would be beneficial, but they all glossed over real issues in a bid to prop up a yuppie idea of living wholesomely."
    scene w2_4310 with dissolve
    "*Beep, beep*"
    scene w2_4311 with dissolve
    "A message temporarily pulled me away from the man's vain droning, not that his self-aggrandizing allowed him to notice my lapse in attention."

label w2FeliciaBathroomJill:

    if _in_replay:
        play music "music/air-on-g.ogg"

    scene w2_4312 with dissolve
    if _in_replay:
        show screen textbox2 with dissolve
    "It was from Felicia."
    mct "(This...)"
    scene w2_4313 with dissolve
    mct "(What is this woman planning?)"
    "As uncertain as I was, I did as she bid me and accepted the call out of perverse curiosity."
    play sound "sound effects/phonemenu.wav"
    scene w2_4314 with dissolve
    "*Beep*"
    scene w2_4315 with dissolve
    "What I found..."
    scene w2_4316 with dissolve
    "Must've put a remarkably stupid look on my face."
    el "Is something the matter, Charles?"
    scene w2_4317 with dissolve
    mc "Oh, no. Everything is... good. I was just making a note on something."
    scene w2_4318 with dissolve
    mc "Continue on, please."
    scene w2_4319 with dissolve
    el "Where was I?"
    scene w2_4320 with dissolve
    mc "Stewardship."
    scene w2_4321 with dissolve
    "He was going on and on once more about proper stewardship. It was practically pathological!"
    scene w2_4322 with dissolve
    el "Right, I believe in..."
    scene w2_4323 with dissolve
    "Meanwhile, Felicia patiently waited for Elias to move on, wearing nothing but a smile."
    scene w2_4324 with dissolve
    "At least, I was assuming she was smiling. I couldn't say entirely for sure considering where my focus was..."
    scene w2_4325 with dissolve
    "She moved in and did something to the screen."

    if felPN == "Daddy":
        scene w2_4326 with dissolve
        mct "(Good lord...)"
    else:
        scene w2_4327 with dissolve
        mct "(Good lord...)"

    "Felicia's vivaciousness still managed to surprise me."
    "She remained fired up from earlier and she wasn't letting it go."
    scene w2_4325 with dissolve
    "Not letting it go {b}in the least{/b}."
    scene w2_4328 with dissolve
    feltxt "Turn it on, pleeeeease?"
    "I had just had a minor panic attack over this very thing, yet part of me still wanted to abide by her wishes..."
    scene w2_4329 with dissolve
    "She knew how to put on a damn good pleading act."
    "Meanwhile, her husband was still carrying on, none the wiser that his wife was bared fully nude on the screen in front of me."

    if kat_polite == True:
        "It was my decision. This wasn't part of the photoshoot. There was no advantage for Felicia here or any esteem for me to gain with Mrs. Pulman."
    else:
        "It was my decision. This wasn't part of the photoshoot. There was no advantage for Felicia here or any esteem for me to gain with Kathleen."

    "Pushing this button would be purely an affirmation of my own desires..."
    hide screen textbox2 with dissolve

    menu:
        "Continue and see where this goes."(chg=["felicia_up"]):
            $ w2FeliciaExtra = True
            $ Felicia_Affection += 1
            scene w2_4330 with dissolve
            mctxt "Convince me."
            scene w2_4331 with dissolve
            "My reply was answered by one hell of a salacious, sexed-up grin and the mouthing of the word..."
            "{b}O-k-a-y.{/b}"
            scene w2_4332 with dissolve
            "As Felicia moved away from the camera, I did my best to maintain the illusion of giving my full attention to the slutty woman's husband."
            scene felh_tubrub1_a with dissolve
            "If I had failed in that task, I didn't know. Elias spoke undaunted with the assurance his words were being recorded, with me adding some filler \"I see\"s and \"Tell me more\"s whenever he stopped and took a much needed breath."
            scene felh_tubrub1_a with dissolve
            show felh_tubrub1
            "As Elias continued, so did Felicia and her provocations."
            "Her talent as an exhibitionist was on full display; she knew how to please the viewer's eyes while setting a proper, agonizing pace."
            "Far enough back from the camera to give me a good view, she placed one hand on the gold-plated faucet to balance herself while the other spread her intimate place wide open."
            "She didn't use her fingers to penetrate her already overstuffed cunt, instead, she simply rubbed."
            "Slowly at first, she gingerly ran her fingertips over her labia, teasing and prodding with methodical intent."
            scene w2_4333 with dissolve
            mc "That's odd. Why wouldn't the city council agree to that?"
            scene w2_4334 with dissolve
            el "That's a good question and one that I don't have the foggiest--"
            play sound "sound effects/phonemenu.wav"
            scene w2_4335 with dissolve
            "*Beep*"
            $ renpy.music.set_volume(.1, 0, channel = "sound")
            play sound "sound effects/vib-start.wav"
            "From the small screen of my phone, Felicia's reaction was hard to read, but the way her body suddenly jerked confirmed one thing."
            scene w2_4336 with dissolve
            "The remote control did indeed reach as far as where Felicia presently stood, butt naked and jilling herself off."
            "Which meant, although I had set it on the lower side... I could just as easily..."
            $ renpy.music.set_volume(1, 0, channel = "sound")
            play sound "sound effects/phonemenu.wav"
            "*Beep*"
            $ renpy.music.set_volume(.4, 0, channel = "sound")
            play sound "sound effects/vib-start.wav"
            scene w2_4337 with dissolve
            "Bring it up to half power, if I so pleased."
            scene felh_tubrub2_a with dissolve
            show felh_tubrub2
            "Felicia's hand didn't cease, rather it was spurred on by the abrupt increase in intensity, her fingertips working her swollen lips with greater fervor."
            fel "...!"
            "I could visibly make out the parting of the wanton blonde's lips, but was left to guess what kind of saccharine sounds were reaching her own ears."
            "Was she cursing? Was she trying to keep it down? Was she moaning with abandon?"
            "Not knowing was charming, my brain drawing its own conclusions as I recalled her earlier animosity."
            fel "{i}Fuck you, dickhead{/i}."
            "Was that it?"
            $ renpy.music.set_volume(1, 0, channel = "sound")
            "Was she focusing on the endless thrum of her husband's voice as she got herself off?"
            "Whatever had clicked with her earlier, she was now running with it."
            scene felh_tubrub3_a with dissolve
            show felh_tubrub3
            fel "...!"
            fel "......!"
            "As she picked up speed, I could tell she was losing herself. The pleasure on her face was as clear as day even through the viewport of a small screen."
            "Her fingers were battering her clit now, catching and rolling the little bean with each feverish pass."
            "In no time at all, she had worked herself near orgasm, but she never took her eyes off the direction of her phone."
            "However distant we were, with however many walls between us, she looked at the phone like she was looking directly at me. Even virtually..."
            "She knew how to make a man feel wanted."
            scene w2_4338 with dissolve
            fel "...!"
            scene w2_4339 with dissolve
            fel "...! ...!"
            mct "(She's there!)"

            menu:
                "Crank it to max."(chg=["felicia_up"]):
                    $ Felicia_Affection += 1
                    "A devious idea hit me and I reacted instantly, scrambling to switch over to the vibrators' controller and then back to the video call so I didn't miss a thing."
                    play sound "sound effects/vib-start.wav"
                    scene w2_4340 with vpunch
                    "My brain filled in the cacophonous wails."
                    fel "--!!!!!!!!!!!!!!!!!!!!!!!!!!"
                    scene w2_4341 with vpunch
                    "In no way was she expecting 100 percent power, especially not at the height of her climax."
                    "The result was glaringly obvious. Her face contorted in a delightful mix of bottomless pleasure and abject surprise."
                    scene w2_4342 with dissolve
                    "She hadn't just hit her peak..."
                    scene w2_4343 with vpunch
                    fel "--!!!!!!!!!!!"
                    "She had blown past it."
                    mct "(Shit! Good thing she's in the tub...!)"
                    scene w2_4344 with dissolve
                    fel "...! ...! ----!!!!!!!"
                    play sound "sound effects/water-splash2.wav"
                    scene w2_4345 with dissolve
                    "Fuck..."
                    "The wind utterly knocked out of her by her own orgasm, Felicia's legs gave out and she collapsed into the tub with what I can only guess was an impressive splash."
                    scene w2_4346 with dissolve
                    mct "(That didn't kill her did it?)"
                    scene w2_4347 with dissolve
                    "......"
                    "..."
                    scene w2_4348 with dissolve
                    "I waited..."
                    scene w2_4349 with dissolve
                    "I breathed a sigh of relief that she hadn't cracked her head open on the side of the tub."
                    scene w2_4350 with dissolve
                    "That might've been a first in the history of involuntary manslaughter..."
                    scene w2_4351 with dissolve
                    play sound "sound effects/phonemenu.wav"
                    "*Beep*"
                    scene w2_4352 with dissolve
                    "..."
                "No surprises. Let her finish.":

                    fel "--!"
                    "I was content to watch her bring herself to orgasm by her own hand, albeit with some considerable assistance from the old woman's toys."
                    scene w2_4340 with dissolve
                    "The pleasure twisted Felicia's beautiful face into something wholly obscene."
                    "Honestly, this was a more fitting appearance for the shameless woman..."
                    scene w2_4353 with dissolve
                    "Her eyes went from half-lidded to cross, mouth pried ajar in bliss."
                    scene w2_4354 with dissolve
                    fel "..."
                    "It was over almost as quick as it hit her."
                    scene w2_4355 with dissolve
                    "Her eyes refocused on the camera and she looked..."
                    "{b}Hungry still{/b}."
                    scene w2_4356 with dissolve
                    "......"
                    scene w2_4351 with dissolve
                    "..."
                    scene w2_4352 with dissolve
                    "{i}Call ended{/i}."


            scene w2_4357 with dissolve
            show screen textbox2 with dissolve
            el "...so, all three of my proposals tie into that very idea of Stewardship."
            "At the end of it, Elias Ford was none the wiser that my attention was divided between his circuitous points and his wife debasing herself in the bathroom."
            scene w2_4358 with dissolve
            "He just smiled at me with a shit-eating grin."
            $ renpy.end_replay()
            "...but we weren't finished. Not yet"
            scene black with fade
            if not persistent.w2FeliciaBathroomJill:
                play sound "sound effects/notification.wav"
                show memoryunlock with dissolve
                $ renpy.pause(3, hard=True)
                $ persistent.w2FeliciaBathroomJill = True
                hide memoryunlock with dissolve
                $ renpy.pause(0.5, hard=True)
            "We ate up the rest of the time talking about subjects that I found even less interesting: his personal life, his upbringing, and so on."
        "Finish the interview without any distractions."(chg=["felicia_down3"]):


            $ Felicia_Affection -= 3
            scene w2_4330 with dissolve

            mctxt "This is outside the scope of our task."
            scene w2_4359 with dissolve

            if w2FeliciaPacked == True:
                feltxt "Don't act like a robot all of a sudden when I know you had fun spanking my ass and whispering all that dirty crap into my ear."
            else:
                feltxt "Don't act like a robot all of a sudden. I know you had fun earlier."
            scene w2_4360 with dissolve
            hide screen textbox2 with dissolve

            menu:
                "Tell her she's welcome to take care of herself and then hang up."(chg=["felicia_down"]):
                    $ Felicia_Affection -= 1
                    show screen textbox2 with dissolve
                    mctxt "If you can't control yourself, you're welcome to jill off in the bathroom without an audience."
                    scene w2_4361 with dissolve
                    fel "...!"
                "Tell her the shoot isn't over and then hang up.":

                    show screen textbox2 with dissolve
                    mctxt "The shoot isn't necessarily over. Be patient."
                    scene w2_4362 with dissolve
                    fel "..."

            scene w2_4351 with dissolve
            "*Beep*"
            scene w2_4352 with dissolve
            "That was that."
            "I tried my best not to think of the lovely sight I had just missed out on."
            $ renpy.end_replay()
            scene w2_4363 with dissolve
            el "...that's why it's important to offer parents a safe place for children to gather and socialize."
            scene w2_4358 with dissolve
            "The rest of the interview was uneventful. Elias finished explaining his politics and then we moved onto more personal aspects."
            "Subjects like his upbringing, his father's suicide, and so on. What made him the man he was."
            "This was the meat and potatoes of the guise the old woman had me working under. In one way, it was a nice reprieve..."
            scene black with fade
            "In another, when compared to earlier, it was painfully dull."

    scene w2_4364 with fade
    el "I'm sorry to have to cut things short. Felicia made preparations for the three of us to eat, but..."
    scene w2_4365 with dissolve
    mc "I completely understand."
    scene w2_4366 with dissolve
    play sound "sound effects/door-openclose.wav"
    "--and just like before, a half-hour was just that. Punctual down to the minute."
    "I found his internal clock enviable."
    scene w2_4367 with dissolve
    fel "You should get going, hun. You shouldn't keep Theo waiting."
    "Also on time, down to the minute, was Felicia."
    scene w2_4368 with dissolve

    if w2FeliciaExtra == True:
        "She entered the room the picture-perfect model of wifely radiance, without a trace of the debauched woman who was just howling and creaming herself on camera."
    else:
        "She entered the room as serene as a graven image, far and removed from the wanton hunger on display not fifteen minutes ago."

    scene w2_4369 with dissolve
    fel "I'll keep Charles duly entertained and then send him on his way. It's not polite to usher a guest out the door, after all."
    scene w2_4370 with dissolve
    el "My wife is right. It would be poor manners to allow you to leave with an empty stomach."
    el "Hors d'oeuvres for three can just as easily be hors d'oeuvres for two."
    scene w2_4371 with dissolve
    mc "I'll gladly accept your hospitality."
    scene w2_4372 with dissolve
    "Saves me the trouble of coming back after he leaves and finishing the shoot."
    scene w2_4373 with dissolve
    el "I'll leave you in my wife's lovely hands then."
    scene w2_4372 with dissolve
    "For a couple of seconds that dragged on and on, the pair locked eyes and shared a silent moment of mutual understanding."
    scene w2_4374 with dissolve
    "A look that carried unspoken expectations and instructions."

    if kat_polite == True:
        "Not even when she was licking Mrs. Pulman's heel did she look so small."
    else:
        "Not even when she was licking Kathleen's heel did she look so small."

    scene w2_4375 with dissolve
    fel "I'll walk you out?"
    scene w2_4376 with dissolve
    el "No need for you to bother, dear."
    scene w2_4377 with dissolve
    el "Charles..."
    el "I look forward to reading your write-up."
    scene w2_4378 with dissolve
    "For one last time, he proffered his hand, drawing a curtain on the old lady's asinine farce."
    scene black with fade
    stop music fadeout 3.0
    el "...and I appreciate the good word."
    play sound "sound effects/elevator-bell.wav"
    scene w2_4379 with dissolve
    mc "He's gone..."
    "As Felicia and I watched the elevator doors close, I breathed a great sigh of relief."
    scene w2_4380 with dissolve
    fel "That's right. He's gone..."

    if w2FeliciaExtra == True:
        play music "music/sneaky-snitch.ogg"
        scene w2_4381 with dissolve
        "Now that we were alone, I could finally take a good look at what Felicia had changed into following the aftermath of our lecherous call."
        scene w2_4382 with dissolve
        fel "It's just you, me, and the... {i}camera{/i}, all alone in this great big, {b}empty{/b} penthouse..."
        scene w2_4383 with dissolve
        "Adorned on her shapely body was a form-fitting lace dress dyed a beautifully striking amber that paired perfectly with Felicia's tan skin and golden tresses."
        scene w2_4384 with dissolve
        mc "The fire still burning after that... {i}show{/i}?"
        scene w2_4385 with dissolve
        fel "Whoever said \"a light that burns twice as bright burns half as long\", hadn't met this hoe. I've got a big..."
        scene w2_4386 with dissolve
        fel "...appetite."
        scene w2_4387 with dissolve
        "Felicia was a cat in heat."
        "Despite having let slip earlier that there was potentially more to her participation at the club beyond her sexual fulfillment, this was..."
        scene w2_4388 with dissolve
        fel "We ain't finished yet, are we?"
        "This was Felicia at her most base."
        scene w2_4389 with dissolve
        mc "More photos won't hurt your chances of winning..."
        mc "Let the camera get a look at you in that dress."
    else:

        play music"music/sneaky-snitch.ogg"
        scene w2_4390 with dissolve
        fel "...and now it's just you and me, [mcf]."
        scene w2_4391 with dissolve
        "Now that we were alone, I could finally take a good look at what Felicia had slipped into during the interim."
        scene w2_4393 with dissolve
        "Adorned on her shapely body was a form-fitting lace dress dyed a beautifully striking amber that paired perfectly with Felicia's tan skin and golden tresses."
        scene w2_4392 with dissolve
        fel "You think the boss lady got what she wanted out of this?"
        scene w2_4394 with dissolve
        mc "Who knows what that woman actually expected from this charade..."
        scene w2_4395 with dissolve
        "..."
        "......"
        scene w2_4394 with dissolve
        mc "I'd say we got some pretty good material, though."
        scene w2_4396 with dissolve
        fel "Hell yeah, we did. That was..."
        scene w2_4397 with dissolve
        fel "That's right, you little...!"
        scene w2_4398 with dissolve
        fel "It's fucking rude to hang up on a girl like that. It killed my mood; made me feel {i}real{/i} stupid."
        scene w2_4399 with dissolve
        mct "(Mood...?)"
        "She had already let slip there was more to her participation beyond her sexual gratification."
        scene w2_4400 with dissolve
        mc "That wasn't part of the shoot, plus your husband was looking me dead in the eye at the time. The toys were one thing, but..."
        scene w2_4401 with dissolve
        "She cut me short with a sad look and a long, well-manicured finger."
        scene w2_4402 with dissolve
        fel "Yeah, it's {b}fucked{/b} and {i}incredibly{/i} stupid on my part, but that's..."
        scene w2_4403 with dissolve
        fel "That's the point."
        fel "We ain't finished yet, are we?"
        scene w2_4404 with dissolve
        mc "Depends. Do you want to have a better shoot than Veronica and Rosalind?"
        scene w2_4403 with dissolve
        fel "Yes."
        "The brusque answer and serious look didn't fit the wifely blonde, but there you had it..."
        scene w2_4404 with dissolve
        mc "Let the camera get a look at you in that dress then."


    scene w2_4405 with dissolve
    fel "Oh? You like it?"
    scene w2_4406 with dissolve
    fel "This dress cost five grand. Ain't that fucking stupid?"
    mc "There's no denying though..."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_4407 with flash
    "*Click*"
    mc "It looks stunning on you."
    scene w2_4408 with dissolve
    fel "It does."
    fel "Thank you, [mcf]."
    scene w2_4409 with dissolve
    mc "Give me a spin. I want to see the back."
    scene w2_4408 with dissolve

    if felPN == "Sir":
        fel "Yes, {b}sir{/b}..."

    elif felPN == "Daddy":
        fel "If that is what {b}Daddy{/b} wants..."
    else:
        fel "Anything for you, {b}stud{/b}..."

    scene w2_4409 with dissolve
    "The intonation she used left the hair on the back of my neck standing, each and every syllable its own separate seduction."
    scene w2_4410 with dissolve
    "In stark contrast to the sophisticated front, the rear of her dress was cut tantalizingly short, offering a delectable peek at her toned back and tan lines."
    mct "(If I had money...)"
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_4411 with dissolve
    "*Click"
    mct "(I'd be stupid enough to fall for this.)"
    scene w2_4412 with dissolve
    fel "Just how far did Big Red and Rosie go with their shoots?"
    scene w2_4414 with dissolve
    mc "You'd find it difficult to believe."
    scene w2_4413 with dissolve
    fel "Try me."
    scene w2_4414 with dissolve
    mc "Rosalind got down on the floor and titfucked me in a dirty park bathroom and Veronica pretended to be a dog."
    scene w2_4415 with dissolve
    fel "...holy cow, those bitches ARE playing to win."
    scene w2_4416 with dissolve
    mc "No shit."
    mct "(You're the one whose life isn't on the line here...)"
    scene w2_4417 with dissolve
    fel "Hmmm..."
    scene w2_4418 with dissolve
    fel "Stay here for a minute. I'll call to come in"
    stop music fadeout 3.0
    scene w2_4419 with dissolve
    "Like that, Felicia suddenly disappeared back into her husband's office."
    scene w2_4420 with dissolve
    "......"
    "..."
    mct "(Nice view...)"
    mct "(Knowing how much a place like this costs would probably make me sick...)"
    scene w2_4421 with dissolve
    fel "Okay ...ready! Come on in, stud."
    scene black with fade
    mct "(What is she thinking?)"

label w2FeliciaSex:

    play sound "sound effects/door-openclose.wav"
    scene w2_4422 with fade
    play music "music/cello-suite-No-1-G-Major-Prelude.ogg"
    if _in_replay:
        show screen textbox2 with dissolve
    "Oh..."
    scene w2_4423 with dissolve
    fel "Who needs stupid gimmicks when you look like I do?"
    scene w2_4422 with dissolve
    "THAT is what she's thinking."
    "Splayed out on her husband's desk, wearing naught but an expensive-looking strapless bra and a pair of extravagant lace panties, Felicia welcomed me with open legs."
    scene w2_4424 with dissolve
    mc "I would agree with you if this was purely based on sex appeal..."
    scene w2_4425 with dissolve
    fel "Please... this is about humiliating my husband more than it is about demeaning me. That's what she's selling those old farts."
    scene w2_4426 with dissolve
    fel "What's more demonstrative of that than doing {i}this{/i} in his very office?"
    scene w2_4427 with dissolve
    mc "...and you're okay with that?"
    scene w2_4426 with dissolve
    fel "If I'm getting what I want out of the deal, the old lady and her customers should get theirs."
    scene w2_4427 with dissolve
    mc "What ARE you getting out of this? What's the upside of joining the club?"
    mct "(I mean... isn't she afraid of her husband discovering any of this?)"

    if feliciaFlag == True:
        "In her own way, she worked hard for this life. This was a risk, no matter how casual she was about it, and Felicia was an extraordinarily intelligent and self-reflective woman."
        "I could say that for certain after the night we shared dinner."
    else:
        "In her own way, she worked hard for this life. This was a risk no matter how casual she was about it, and Felicia was an intelligent woman."
        "I was certain of that."

    scene w2_4428 with dissolve
    fel "Upside? Ah, who knows...? I'm just a dumb country slut."
    fel "I haven't given it that much thought."
    scene w2_4429 with dissolve
    "I didn't believe her, not in the least. The way she strategically belittled herself when it suited her and the way she downplayed her worth... it pissed me off."
    scene w2_4430 with dissolve
    "It pissed me off, but it gave me an idea..."
    hide screen textbox2 with dissolve

    menu:
        "Challenge her."(chg=["felicia_up", "felicia_passion_up"]):
            $ Felicia_Confidence += 1
            $ Felicia_Affection += 1

            scene w2_4431 with dissolve
            show screen textbox2 with dissolve
            mc "You really think I buy that, Felicia? Considering where you started in life and where we presently stand?"
            mc "You didn't just luck your way into a penthouse apartment."
            scene w2_4432 with dissolve
            fel "Get the fuck off this horse, will ya? You're here to take photos, not psychoanalyze my motivations."
            fel "What do you care, anyway?"
            scene w2_4433 with dissolve
            mc "Intelligence shouldn't be minimized."
            scene w2_4434 with dissolve
            fel "Oh, God! You're such a kid!"
            scene w2_4435 with dissolve
            fel "Intellect can be wielded like a battleaxe or used as a knife to be stuck in the back."
            scene w2_4436 with dissolve
            mc "This isn't an RPG..."
            scene w2_4437 with dissolve
            fel "Intelligence shouldn't be minimized? That's ego."
            scene w2_4438 with dissolve
            fel "Let me ask you this, if you had to pick, do you think most men want brains or a tittering bimbo?"
            scene w2_4439 with dissolve
            mc "Most people would say brains."
            scene w2_4440 with dissolve
            fel "That's the operative word, [mcf]. {b}Say{/b}."
            fel "...and that's true to an extent, but there's a fine balance to walk. Men like Elias want a woman intelligent enough to show off and know how to comport themselves, but dumb enough that it won't threaten their masculinity."
            scene w2_4439 with dissolve
            "We were getting far off the topic of what motivated her, but the way her face lit up when she tried to school what she saw as naivety..."
            play sound "sound effects/camera-phone-shutter.wav"
            scene w2_4441 with flash
            "*Click*"
            "She was glowing right now; her eyes fiercely intelligent and her expression deeply sure of herself. If the camera only captured a quarter of that, this would be gold."
            scene w2_4439 with dissolve
            mc "No offense, but if that's really true, then your husband is a moron with some major blind spots."
            mc "Come to think of it... is that why you specifically picked him or was he really just the best you could pull?"
            scene w2_4443 with dissolve
            fel "Don't act like you know--"
            play sound "sound effects/camera-phone-shutter.wav"
            scene w2_4444 with dissolve
            "*Click*"
            mc "Take off your top you \"tittering\" bimbo."
            scene w2_4445 with dissolve
            fel "You..."
            scene w2_4442 with dissolve
            "Felicia wore a look of surprise on her face that tailed into a smirk."
            scene w2_4448 with dissolve
            fel "You're playing me?"
            scene w2_4442 with dissolve
            mc "See? You catch on quick!"
            hide screen textbox2 with dissolve
            scene w2_4446 with dissolve
            mc "I do {i}need{/i} to see your tits, but I also mean what I said."
            scene w2_4447 with dissolve
            mc "You could do a lot better than someone who needs to be the smartest man in the room."
            scene w2_4449 with dissolve
            fel "What? You got ten million dollars in your back pocket?"
            play sound "sound effects/camera-phone-shutter.wav"
            scene w2_4450 with dissolve
            "*Click*"
            mc "That isn't a line."
            scene w2_4451 with dissolve
            fel "The fuck it isn't, coming from a twenty-one year old."
            scene w2_4452 with dissolve
            mc "Twenty-two. Now, turn around and stick out your ass."
            scene w2_4453 with dissolve
            fel "Oh, I'm sorry. That year makes all the difference, does it?"
            scene w2_4454 with dissolve
            fel "All those brain cells you killed with alcohol the previous year must've made space for newer and better ones?"
            scene w2_4455 with dissolve
            mc "Not how the brain works -- kick one of your legs back and make a pose."
            play sound "sound effects/camera-phone-shutter.wav"
            scene w2_4456 with dissolve
            "*Click*"
            scene w2_4457 with dissolve
            fel "What would I know about the human brain? I'm just a communications major that sucked dicks to get here."
            scene w2_4458 with fade
            fel "What's the point of this conversation again?"
            scene w2_4459 with dissolve
            mc "I want you to admit you're full of crap and that you believe you're the most intelligent person in the room."
            play sound "sound effects/camera-phone-shutter.wav"
            "*Click*"
            mc "I also want you to take off your panties."
            scene w2_4460 with dissolve
            fel "Something that simple and then we can move onto focusing on how damned turned on I am right now?"
            scene w2_4461 with dissolve
            fel "Fine..."
            scene w2_4462 with dissolve
            fel "I don't really think I'm stupid, but I'm not going to budge on the country or slut part."
            fel "Those latter two are just objective facts."
            play sound "sound effects/camera-phone-shutter.wav"
            scene w2_4463 with dissolve
            "*Click*"
            scene w2_4464 with dissolve
            mc "I'll take it."
            scene w2_4465 with dissolve
            mc "I'm not knocking how you climbed here by the way. I just think you could've been successful at anything you set your mind to. It irks me that you put the most attractive thing about you away in a box for convenience."
            stop music fadeout 3.0
            scene w2_4466 with dissolve
            "I said something. Something really, {b}really{/b} lame..."
            scene w2_4467 with dissolve
            fel "[mcf], stop saying cliched nonsense."
            scene w2_4468 with dissolve
            "To my surprise, she didn't laugh."
            scene w2_4467 with dissolve
            fel "Please?"
            scene w2_4469 with dissolve
            "Instead of scoffing, she responded with a painfully pleading expression that made me think I had inadvertently said something offensive."
            scene w2_4470 with dissolve
            fel "Saying such a sweet thing offhandedly..."

            if feliciaFlag == True:
                scene w2_4471 with dissolve
                fel "Really makes a gal wish you had ten million dollars in your back pocket."
                scene w2_4472 with dissolve
                "Try as I might, I couldn't make eye contact with the sultry blonde."
                scene w2_4473 with dissolve
                fel "You're kinda fucking annoying, but also..."
                scene w2_4472 with dissolve
                "The look she was giving me... if this was her trying to move onto something more fun, this was far beyond Rosalind's bumbling attempt at seduction."
                scene w2_4474 with dissolve
                fel "Thanks."
                scene w2_4472 with dissolve
                "If the look was genuine..."
                "Well, genuine or not, I had to resist throwing her down on this desk right now and having my way with her."
                mct "(Wait... why shouldn't I?)"

                menu:
                    "Grab Felicia."(chg=["maid"]):
                        $ w2FeliciaImpressed = True
                        scene w2_4504 with dissolve
                        scene w2_4505 with dissolve
                        "After all..."
                        scene w2_4506 with dissolve
                        fel "Oh, my... you look like you want to--"
                        play music "music/bellissimo.ogg"
                        scene felh_grope_a with dissolve
                        show felh_grope
                        fel "O-oh!"
                        "She's shown herself to be more than willing, so why not just drop the pretense?"
                        "I buried my face in Felicia's neckline, dotting her beautiful skin with a myriad of little kisses while my hands dumbly fumbled to grasp every part of her body within reach."
                        fel "Mmmh! You..."
                        fel "You, uh... dropped the camera, stud. Isn't this part of the shoot?"
                        scene w2_4507 with dissolve
                        mc "Not in the least."
                        scene w2_4508 with dissolve
                        fel "Ha... okay, then."
                        scene w2_4509 with dissolve
                        "Felicia's gentle smile pulled me back in. She had never looked so... soft."
                        scene w2_4510 with dissolve
                        fel "A-ah, bold and c-clumsy...! I..."
                        scene w2_4512 with dissolve
                        fel "...{b}love{/b} that."
                        scene w2_4511 with dissolve
                        "She dangerously wielded the same smoldering look as earlier, gone unabated in the wake of our adulterous bar side chat."
                        scene w2_4512 with dissolve
                        fel "I want it, [mcf]. I want..."
                        scene w2_4513 with dissolve
                        fel "{b}You{/b}."
                        scene w2_4511 with dissolve
                        hide screen textbox2 with dissolve

                        if w2FeliciaPacked == True:

                            menu:
                                "Live out her fantasy."(chg=["felicia_up2"]):
                                    $ edwinAnal = True
                                    $ Felicia_Affection +=2
                                    scene w2_4514 with dissolve
                                    show screen textbox2 with dissolve
                                    mc "You and I are not alone."
                                    scene w2_4515 with dissolve
                                    fel "Oh...?"
                                    "A familiar fantasy of the capricious blonde's own making."
                                    scene w2_4516 with dissolve
                                    fel "{b}Oh{/b}."
                                    "She caught on quick."
                                    scene w2_4517 with dissolve
                                    fel "Have you ever...?"
                                    scene w2_4518 with dissolve
                                    mc "No, never."
                                    scene w2_4519 with dissolve
                                    "She zeroed in on a thought I had lingering in the back of my mind."
                                    scene w2_4520 with dissolve
                                    fel "So, I'll have the pleasure of being your first then..."
                                    scene w2_4519 with dissolve
                                    "Felicia smiled at the revelation that I'd never had anal sex with a woman."
                                    scene w2_4521 with dissolve
                                    "In a show of odd affection, the blonde gave me a kiss on the cheek."
                                    fel "You and I aren't alone... and I'm..."
                                    hide screen textbox2 with dissolve
                                    scene w2_4522 with dissolve
                                    "Felicia did an abrupt about-face and bent over the desk, sticking her ass in the air and offering full unfettered access."
                                    scene w2_4523 with dissolve
                                    fel "I'm just a cock hungry bitch begging for release, right?"
                                    scene w2_4522 with dissolve
                                    mc "Wait a sec... hold that pose..."
                                    scene w2_4523 with dissolve
                                    fel "[mcf]... I'm waaaaiting--"
                                    play sound "sound effects/camera-phone-shutter.wav"
                                    scene w2_4524 with flash
                                    "*Click*"
                                    fel "Killing two birds with one stone?"
                                    mc "No..."
                                    stop music fadeout 3.0
                                    scene black with fade
                                    mc "We do still have a job to do, but that one is for my own collection."
                                    jump w2FeliciaDoggystyle
                                "Enjoy the best view in the house.":


                                    scene w2_4514 with dissolve
                                    show screen textbox2 with dissolve
                                    mc "Lie back and show me where you want it then."
                                    scene w2_4513 with dissolve
                                    fel "Why do men like to make women beg when they want it just as much?"
                                    scene w2_4525 with dissolve
                                    fel "Better question, though... why do I enjoy telling them what they want to hear?"
                                    fel "You want me to spell it out for you stud?"
                                    hide screen textbox2 with dissolve
                                    scene w2_4526 with dissolve
                                    "I nodded, never taking my eyes off the sprawled-out blonde."
                                    scene w2_4527 with dissolve
                                    fel "I want it..."
                                    scene w2_4528 with dissolve
                                    fel "Here."
                                    fel "I want it in my pussy. I want you to ram your fat cock up my--"
                                    play sound "sound effects/camera-phone-shutter.wav"
                                    scene w2_4529 with flash
                                    "*Click"
                                    fel "You like that thing, don't you?"
                                    scene black with fade
                                    "I did."
                                    jump w2FeliciaMissionary
                        else:


                            scene w2_4514 with dissolve
                            show screen textbox2 with dissolve
                            mc "Lie back and show me where you want it then?"
                            scene w2_4513 with dissolve
                            fel "Why do men like to make women beg when they want it just as much?"
                            scene w2_4525 with dissolve
                            fel "Better question, though... why do I enjoy telling them what they want to hear."
                            fel "You want me to spell it out for you stud?"
                            scene w2_4526 with dissolve
                            "I nodded, never taking my eyes off the sprawled-out blonde."
                            scene w2_4527 with dissolve
                            fel "I want it..."
                            scene w2_4528 with dissolve
                            fel "Here."
                            fel "I want it in my pussy. I want you to ram you fat cock up my--"
                            play sound "sound effects/camera-phone-shutter.wav"
                            scene w2_4529 with flash
                            "*Click"
                            fel "You like that thing, don't you?"
                            scene black with fade
                            "I did."
                            jump w2FeliciaMissionary
                    "Get some distance.":

                        scene w2_4530 with dissolve
                        show screen textbox2 with dissolve
                        mc "No need. That's not me flattering you."
                        mc "You just... perplex the shit out of me."
                        scene w2_4531 with dissolve
                        "I truly did wonder if, should it be within the realm of human comprehension, if I would ever understand what made Felicia Ford tick."
                        scene w2_4532 with dissolve
                        fel "That's also flattering in its own way, stud."
                        scene w2_4533 with dissolve
                        mc "You would take it that way."
                        scene black with fade
                        fel "Well... Elias will be gone for a few hours, but we should get back to why we're here..."
                        $ renpy.end_replay()
                        jump w2FeliciaSoloFinish
            else:


                scene w2_4475 with dissolve
                fel "Makes me wish you had ten million dollars in your back pocket."
                scene w2_4476 with dissolve
                mc "Heh, I wouldn't be standing here if I did..."
                scene w2_4477 with dissolve
                fel "Let's finish the shoot, stud."
                jump w2FeliciaSoloFinish
        "Degrade her."(chg=["tough_up2","felicia_down"]):

            $ w2FeliciaDegrade = True
            $ toughness += 2
            $ Felicia_Affection -=1
            stop music fadeout 3.0
            show screen textbox2 with dissolve
            scene w2_4478 with dissolve
            mc "Just a dumb slut, huh?"
            scene w2_4479 with dissolve
            fel "What else would you call a woman sitting on her husband's desk, gleefully spreading her legs to be photographed?"
            scene w2_4478 with dissolve
            mc "Well, you're right about the last part at least. You are a... {b}slut{/b}."
            $ renpy.music.set_volume(.3, 0, channel = "music")
            play music "music/hypnosis.ogg"
            scene w2_4480 with dissolve
            mc "A low-down, conniving, duplicitous {b}slut{/b} that sold it not only to the highest bidder, but gives it up for free for fun."
            scene w2_4481 with dissolve
            fel "I didn't go that far, dickhead."
            scene w2_4482 with dissolve
            mc "I don't mean it as a bad thing.... photos of a member of the illustrious Ford family showing her true colors as a trashy whore... {b}that{/b} is what will bring our customers' old, shriveled dicks back from the dead."
            scene w2_4483 with dissolve
            $ renpy.music.set_volume(.1, 3, channel = "music")
            "I laid it on thick, not so much for the mood of the shoot but because I enjoyed it. Because just now, it was hitting me, this woman had access to money I could only dream about."
            "What she would consider pocket change..."
            scene w2_4484 with pixellate
            vic "Sorry, I know it's sudden, but Trina asked me to cover her shift at the bar. Her son broke his arm."
            scene w2_4485 with dissolve
            vic "There's money for pizza on the kitchen table. Don't eat all of it! Save some for your lunch tomorrow!"
            scene w2_4486 with dissolve
            vic "Bye! Love you!"
            $ renpy.music.set_volume(1, 0, channel = "music")
            scene w2_4487 with pixellate
            "It was then I felt spiteful bile rise out of my core and permeate my being. Before I was just angry about her pretending to be stupid, but now I felt a momentary antipathy toward the bitch."
            scene w2_4488 with pixellate
            fel "Hmpfh..."
            scene w2_4429 with dissolve
            "She was treading the same path, but for fun?!"
            scene w2_4488 with dissolve
            fel "You have an interesting look in your eyes, stud. You look like you reeeeeally hate me right now..."
            scene w2_4429 with dissolve
            "There are parts of Felicia I really like. She is unpretentious and unflinchingly honest with herself."

            if feliciaFlag == True:
                "She was vibrant and good-natured. She pulled herself out of the muck to attain a life I could never dream of."
            else:
                "She pulled herself out of the muck to attain a life I could never dream of."

            scene w2_4428 with dissolve
            fel "I know that look. You want to get mean with me, don't you? Well, I get it. It's for the shoot, right? Not because you're a pervert or anything..."
            fel "If you want me to jump, just..."
            scene w2_4427 with dissolve
            "She had won. She had carved out the life she wanted."
            "Yet here sat her pretty ass, playing a game I didn't understand. I mean shit, even just the dress she had on earlier..."
            scene w2_4426 with dissolve
            fel "...just say jump."
            scene w2_4427 with dissolve
            "Their \"value\" would have made my mother and me comfortable for months."
            mc "Oh, you bitch... {b}take them off{/b}."
            scene w2_4425 with dissolve
            fel "My bra or my--"
            scene w2_4489 with dissolve
            mc "Both of them. It's like putting makeup on a dog; a cumdump like you wearing clothes at all is a joke, let alone a set that costs so much money..."
            mc "You look fucking ridiculous, so stand up and get rid of them."
            scene w2_4490 with dissolve
            "If she was going to pretend to be a dumb country slut, for the purpose of this shoot, I'd do her the courtesy of treating her like one."
            scene w2_4491 with dissolve
            "True to what she said, smile on her face, Felicia jumped."
            scene w2_4492 with dissolve
            "First, the top."
            scene w2_4493 with dissolve
            "Then, the bottom."
            scene w2_4494 with dissolve
            "Until she stood in front of me, legs held straight, wearing nothing but a pair of heels."
            fel "Huh... that's a new, {i}interesting{/i} feeling as well..."
            play sound "sound effects/camera-phone-shutter.wav"
            scene w2_4495 with flash
            "*Click*"
            mc "What is?"
            scene w2_4496 with dissolve
            fel "A man your age talking down to me like that. It feels..."
            scene w2_4497 with dissolve
            fel "Honestly, I kind of hate it, but do feel free to explore."
            fel "For this month at least, I'm just a piece of meat and the old woman made you my {b}butcher{/b}."
            fel "It might be the only time you'll get your hands on an A5 slab of ass like this..."
            scene w2_4498 with dissolve

            if kat_polite == True:
                "Those were bold words for a self-proclaimed slut, but I saw firsthand her hesitation when Mrs. Pulman had her kneel. The flash of pride may have been momentary, but it was there."
            else:
                "Those were bold words for a self-proclaimed slut, but I saw firsthand her hesitation when Kathleen had her kneel. The flash of pride may have been momentary, but it was there."

            "This woman pretended to be shameless, but she had also clawed her way to becoming the wife of a wealthy man. Try as she might to downplay it, she lived daily as a woman of her station."

            scene w2_4499 with dissolve
            if w1ExGame2LoserFel == True:
                fel "Treat me as contemptuously as your heart desires, but let's beat Rosie and Red, shall we? I have to make up for my poor showing from last week."
            else:
                fel "Treat me as contemptuously as your heart desires, but let's beat Rosie and Red, shall we?"

            scene w2_4500 with dissolve
            "What the hell kind of fucked-up metaphor is that?"
            scene w2_4501 with dissolve
            mct "(Of course she'd pick a prime cut even when she's degrading herself!)"
            scene w2_4502 with dissolve
            fel "What's so funny?"
            scene w2_4503 with dissolve
            mc "Nothing it's just..."
            "Once again, I felt disgust well in me and venom pool in the back of my throat."
            scene w2_4534 with pixellate
            "She was choosing {b}this{/b}, for {i}fun?{/i}"
            "From the comfort of her multi-million dollar penthouse?"
            hide screen textbox2 with dissolve

            menu:
                "Explore your contemptuous feelings."(chg=["tough_up2"]):
                    $ feliciaAnger = True
                    $ toughness += 2
                    scene w2_4535 with pixellate
                    show screen textbox2 with dissolve
                    mc "It's just I'm realizing what a joke this is."
                    scene w2_4536 with dissolve
                    fel "I'm glad I can amuse."
                    scene w2_4537 with dissolve
                    "Felicia chose to take my words in good humor, ignoring the blatant agitation in my voice."
                    mc "We have a shoot to continue."
                    mc "Put your hands behind your back, stand up straight, and stick your tits out like you're trying to land a husband again."
                "Shove your feelings down where they belong":

                    scene w2_4535 with pixellate
                    show screen textbox2 with dissolve
                    "I swallowed my feelings. My history had nothing to do with the woman in front of me or whatever her reasons for standing here."
                    mc "It's just I think we should drop the weirdly cannibalistic metaphor and move on with the shoot."
                    scene w2_4537 with dissolve
                    mc "Put your hands behind your back, stand up straight, and point your chest out."

            scene w2FeliciaInterviewBounce with dissolve
            "Felicia sprung up with the pep of a soldier at ten-hut, quickly clasping her arms behind her back and sending her pert breasts quaking."
            scene w2_4546 with dissolve
            if felPN == "Sir":
                fel "Yes, {b}sir{/b}!"
            elif felPN == "Daddy":
                fel "Anything for {b}Daddy{/b}."
            else:
                fel "Anything you ask, stud."

            play sound "sound effects/camera-phone-shutter.wav"
            scene w2_4547 with dissolve
            "*Click*"
            "Her blush, barely noticeable on the canvas of her tanned cheeks, still persisted."
            scene w2_4548 with dissolve

            if feliciaAnger == True:
                mc "Don't look at me, you stupid cunt. Look straight ahead."
            else:
                mc "Look straight ahead."

            scene w2_4549 with dissolve
            "Again, she followed the simple orders without complaint. It was a nice change of pace from working with Veronica."
            scene w2_4550 with dissolve
            fel "O-oh!"
            "The attentive blonde jerked as soon as my cool hands touched the burning hot flesh of her breasts."
            play sound "sound effects/camera-phone-shutter.wav"
            scene w2_4551 with dissolve
            "*Click*"
            mc "A5 beef, eh...?"
            scene w2_4552 with dissolve

            if feliciaAnger == True:
                mc "Sure, but in that analogy, you're still just a piece of meat. Don't get full of yourself, bitch."
            else:
                mc "Sure, but in that analogy, you're still just a piece of meat. Don't be proud of it."

            scene w2_4553 with dissolve
            "She kept looking straight ahead, never breaking character. The only answer came in the form of a bemused smile."
            scene w2_4554 with dissolve
            mc "Don't smile. Stick out your tongue."
            scene w2_4555 with dissolve
            fel "Bleeh~!"
            play sound "sound effects/camera-phone-shutter.wav"
            scene w2_4556 with dissolve
            "*Click*"
            "Another stupid photo to add to the pile."
            scene w2_4549 with dissolve
            "Her eyes remained forward. I had her complete attention, but for some reason... I felt like I was under {i}her{/i} spell."
            scene w2_4557 with dissolve

            if felPN == "Sir":
                fel "What else would you have me do, sir?"
            elif felPN == "Daddy":
                fel "What else, Daddy?"
            else:
                fel "What else would please you, Mr. [mcl]?"

            scene w2_4549 with dissolve
            "Honestly, her obliging demeanor felt routine and artificial."
            "The photos were good in their own way, but they could be better..."
            hide screen textbox2 with dissolve

            if feliciaFlag == True:
                menu:
                    "Live out her fantasy."(chg=["maid"]):

                        $ w2FeliciaImpressed = True
                        $ edwinAnal = True

                        if w2FeliciaPacked == True:
                            show screen textbox2 with dissolve
                            "My mind wandered earlier back into the evening and I was flooded with a vivid recollection of Felicia mewling and squirming while under the spell of her own carnal making."
                            "I could use that again, except this time..."
                            "It'd be more simulatory."
                            scene w2_4558 with dissolve
                            mc "You know... we have an audience."
                            scene w2_4559 with dissolve
                            "Felicia wordlessly waited for me to explain, a puzzled look on her face."
                            scene w2_4560 with dissolve
                            mc "You and I are not alone."
                            scene w2_4561 with dissolve
                            "Despite my direction, she remained committed."
                            scene w2_4560 with dissolve
                            mc "You may look."
                            scene w2_4562 with dissolve
                            fel "Hm...? Oh!"
                            scene w2_4304 with dissolve
                            "We were quickly on the same page."
                            scene w2_4564 with dissolve

                            if feliciaAnger == True:
                                mc "Bend over your husband's desk and stick your ass out."
                                mc "Your father-in-law is going to have a front-row seat to see what a cock-hungry bitch you are."
                            else:
                                mc "Bend over the desk and present yourself."
                        else:


                            show screen textbox2 with dissolve
                            "A thought hit me and I recalled the events of the night we shared in the park, when Felicia weaved her sensuous tale of being fucked in the ass."
                            scene w2_4558 with dissolve
                            mc "We have... something of an audience, y'know..."
                            scene w2_4559 with dissolve
                            "Felicia looked confused, but she didn't say anything. She just waited for me to explain."
                            scene w2_4560 with dissolve
                            mc "You and I are not alone."
                            scene w2_4561 with dissolve
                            "Despite my direction, she kept her eyes on some imaginary point beyond me."
                            scene w2_4560 with dissolve
                            mc "You have my permission to look."
                            scene w2_4562 with dissolve
                            fel "Hmmm...? It's just a painting."
                            scene w2_4304 with dissolve
                            mc "No. It's your father-in-law, but not a single soul in this room is what they seem."
                            "I did my best to recollect Felicia's own words from that night."
                            mc "I'm not a student, he's a customer, and you're..."
                            scene w2_4563 with dissolve
                            fel "Oh! ...really?"
                            scene w2_4564 with dissolve
                            mc "Let's try it."

                            if feliciaAnger == True:
                                mc "Bend over your husband's desk and stick your ass out."
                                mc "Your father-in-law is going to have a front-row seat to see what a cock-hungry bitch you are."
                            else:
                                mc "Bend over the desk and present yourself."

                        hide screen textbox2 with dissolve
                        scene w2_4523 with dissolve
                        fel "Tell me... you ever take a woman's ass before, stud?"
                        play sound "sound effects/camera-phone-shutter.wav"
                        scene w2_4524 with flash
                        "*Click*"
                        mc "You'll be the first. Does that make you happy?"
                        scene w2_4523 with dissolve
                        fel "Honestly? Happy as a pig in muck."
                        fel "It's hot knowing I'll be your first."
                        fel "...but is a \"cumdump\" like me good enough for you?"
                        stop music fadeout 2.0
                        scene black with fade
                        "I didn't answer. Instead, I simply approached from behind."
                        jump w2FeliciaDoggystyle
                    "Creatively end the shoot without touching her.":

                        jump w2FeliciaSoloFinishDegrade
            else:
                jump w2FeliciaSoloFinishDegrade


label w2FeliciaDoggystyle:

    hide screen textbox2 with dissolve
    play music "music/devious-little-smile.ogg"
    scene w2_4565 with cmet
    "Felicia and I were just mere inches apart now, but I wasn't in any rush. I wanted to savor every individual note of this moment."
    "To burn the dubious feeling of having another man's wife face down and ass up on his very desk, offering the shapely prize for the taking, in my mind."
    scene w2_4566 with dissolve
    fel "You're being terribly quiet back there. Don't keep me waiting."
    scene w2_4567 with dissolve
    "Especially when I considered that the man I was cuckolding had enough power and means to make me disappear without a trace..."
    scene w2_4566 with dissolve
    fel "You're not nervous, are you? It's a hole just like its neighbor, you just have to take a lil' more care... especially if you're planning on going in dry."
    scene w2_4567 with dissolve
    mc "I don't think either of us would enjoy that."
    scene w2_4568 with dissolve
    fel "Should I go get a bottle of lube from my stash then? I've got expensive ones that feel {b}amazing{/b}."
    scene w2_4567 with dissolve
    mc "No need to kill the mood like that when you're..."
    scene w2_4569 with dissolve
    fel "A-ah...!"
    mc "...flooding down here."
    "The bent-over blonde shuddered while my fingertips lightly brushed against her labia."
    scene w2_4570 with dissolve
    mc "You've been creaming yourself all evening. There's more than enough lube right here."
    scene w2_4571 with dissolve
    fel "Mmmgh...! Help yourself to all you want, just... don't.... dawdle."
    scene felh_predog1_a with dissolve
    show felh_predog1

    if felPN == "Sir":
        fel "I'm hurtin' for a cock right now, sir"
    elif felPN == "Daddy":
        fel "I'm hurtin' for a cock right now, Daddy."
    else:
        fel "I'm hurtin' for a cock right now, stud."

    "Felicia bucked back in her teasing, rubbing her pucker against my crown. I wanted to plunge it in then and there, but I mustered my self-restraint."
    "I wanted her to get me ready."
    mc "You do it."
    mc "If you want it in your ass, get it ready with your cunt."
    scene w2_4572 with dissolve
    fel "My..."
    scene felh_predog2_a with hpunch
    mc "Oh-!"
    fel "...pleasure!"
    "Without hesitation, Felicia used the edge of the table to push herself back and spear herself on my cock right down to the base."
    scene felh_predog2_a with dissolve
    show felh_predog2
    "Her insides welcomed me like an old friend. She was so turned on that it gobbled up my full length in an instant."
    fel "Mmm...!"
    "She didn't just stop at insertion though..."
    "She continued to buck her hips and shake her ass, repeatedly impaling herself on my cock and filling the room with the skin-slapping sound of copulation."
    mc "Ah...!"
    mct "(Shit...!)"
    mct "(That's...!)"
    scene w2_4573 with dissolve
    "It took a surprising amount of strength to hold her in place."
    mc "N-not so fast...!"
    "The way she was moving felt way too damn good and I wasn't going to risk popping off so soon."
    mct "(Besides...)"
    scene w2_4574 with dissolve
    mc "I can't let you do what you want."
    scene w2_4575 with dissolve
    "I recounted the words of her own making, the very ones she used in the park."
    mc "That'll be \"too much satisfaction for a despicable slut like you\"."
    scene w2_4576 with dissolve
    fel "Ah... fuck, you're right..."
    fel "How... \"despicable\" of me..."
    stop music
    play sound "sound effects/mouth-pop.wav"
    scene w2_4577 with vpunch
    "*Plop*"
    scene w2_4578 with dissolve
    "Just as easily as it went in, it came out. Shined and lubricated with Felicia's juices, primed and ready to go in her ass."
    "But first..."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_4579 with flash
    "*Click*"

    if kat_polite == True:
        "One quick picture for Mrs. Pulman, replete with the view of Felicia's fat ass and the portrait of her father-in-law. {b}This{/b} was the money shot."
    else:
        "One quick picture for Kathleen, replete with the view of Felicia's fat ass and the portrait of her father-in-law. {b}This{/b} was the money shot."

    mc "You and I are not alone..."
    scene w2_4580 with dissolve
    "I said the familiar words once more and drew Felicia's eyes to the portrait of the man in front of her."
    scene w2_4581 with dissolve
    fel "No, we're not..."
    mc "Now..."

    if w2FeliciaDegrade == True:
        mc "Ready, whore?"
    else:
        mc "You ready, Felicia?"
    play music "music/thunder.ogg"
    scene w2_4582 with dissolve
    fel "...are you?"
    scene w2_4583 with dissolve
    "I was."

    if w2FeliciaDegrade == True:
        "Let's fuck this bitch in the ass!"

    scene w2_4584 with dissolve
    "With care, I positioned my cock at the mouth of her anus and slowly pushed the tip past the border."
    "I wanted to relish my first time penetrating a woman anally."

    if w2FeliciaDegrade == True:
        scene w2_4587 with dissolve
        fel "Ah...!"
    else:
        scene w2_4585 with dissolve
        mc "You okay?"
        scene w2_4586 with dissolve
        fel "Thanks [mcf], but I'm not a delicate flower. You can push in more."
        scene w2_4587 with dissolve
        fel "Mmh...!"

    "I wasn't sure of what to make of the act. The sensation was... {i}different{/i}."
    "It was somewhat tighter than a vagina, but it didn't grip my shaft the same way. It was also... smooth and lacking texture."
    scene w2_4588 with dissolve
    fel "Ha...! Ha...!"
    "It was different, but it was nevertheless immensely pleasurable."
    scene w2_4589 with dissolve
    "Her insides were warm and the deeper I went in her ass, so grew my feeling of conquest. A feeling that built until..."
    scene w2_4590 with dissolve
    fel "Fuck..! Yes...!"
    mc "Ngg...!"
    "A sudden jolt from her upper body had the soft tissue of Felicia's guts tighten and spasm around my cock."
    scene w2_4591 with dissolve
    fel "Ah... ha... ha... fuck, that thing is big! It feels like my first fucking time!"
    fel "H-how... how does it feel, [mcf]?"
    scene w2_4592 with dissolve

    menu:
        "Be honest: it feels good.":
            mc "It's different, but I... like it. It feels good."
            mc "{b}You{/b} feel good."
            scene w2_4593 with dissolve
            fel "How am I getting even more turned on in this situation?"
            fel "You really know what to say to a slut."

        "Taunt her."(chg=["felicia_down"]) if feliciaAnger == True:
            $ Felicia_Affection -=1
            mc "Feels like I'm balls deep in the ass of a rich pig."
            scene w2_4591 with dissolve
            fel "You know... you sound like Kat right now."
            fel "You want me to oink like she did?"
            scene w2_4592 with dissolve
            mc "Let's not go that far."
            "...yet."
            scene w2_4593 with dissolve

        "Tease her." if feliciaAnger == False:
            mc "Feels like I'm balls deep in your ass and you're loving it."
            scene w2_4593 with dissolve
            fel "Well, you're going to love the next part too..."


    if felPN == "Daddy":
        fel "Don't keep me waiting. Go ahead and move, Daddy."
    else:
        fel "Don't keep me waiting. Go ahead and move."

    scene felh_dog1_a with dissolve
    show felh_dog1
    "Despite her words, it was the carnivorous butt slut herself who made the first move, freeing my cock from the confines of her ass and then immediately skewering her guts of her own volition."
    "With a grip on her sides, I thrust to match her sudden movement."
    "Slowly at first, as the way Felicia clenched her sphincter made prying myself from her dick-devouring black hole an arduous task."
    fel "Mmmh...! Oh, fh-fhuck me!"
    "Working in tandem, Felicia would wrest herself about halfway off my dick, before I would use my leverage to pull her back in with ass-quaking force."
    scene felh_dog2_a with dissolve
    show felh_dog2
    "I was {b}fucking{/b} Felicia's ass."
    fel "Ngh, it's been too long...!"
    "Felicia howled without restraint, secure in the knowledge it was just me and her alone, standing eighteen stories above the world below."
    fel "It's been too, {i}too{/i} long!"
    mc "Too long since you've had a dick in your ass?"
    scene felh_dog1_a with dissolve
    show felh_dog1
    fel "Y-yes! B-been too long since I've felt sooooo full!"
    "Felicia's bawdy words hit my ears like steam to an engine's piston, spurring me on to give it to the blonde harder and faster."
    "It had become easier to move in the meantime, every thrust smearing beads of pre-cum along the wall of her guts."
    fel "I l-lo-loove this!"
    "Her insides were gradually loosening and conforming to the outline of my cock, making it easier to move still."
    fel "Oh, fuck me...! This is...!"
    fel "I love {i}your{/i} dick. Fuck me, it's..."
    fel "This...a-ah!"
    scene felh_dog2_a with dissolve
    show felh_dog2
    "Every time I would slam home and her ass greedily swallowed every inch of my dick, her words would catch in her throat."
    fel "Ah...! Oh fuck, [mcf]."
    fel "This is the best...!"

    if feliciaAnger == True:
        "In no time at all, the despicable cunt was acting true to her colors. Her indecipherable motive disgusted me, but the way she carried on got my dick so very, very hard."
    else:
        "There was something about her sexual exuberance, the ecstatic way she spoke, that made me shudder. The way she could carry on without shame made my dick so very, very hard."

    fel "This is the absolute best!"
    scene felh_dog3_a with dissolve
    show felh_dog3
    "...and she wasn't far off from being right. At this moment, I loved how dirty Felicia could be."
    "Fwhap... thwap... chwlap...!"
    "Every time she was yanked backwards, her firm but pleasantly plump ass collided with my nuts and sent a radiating wave of pleasure through my body."
    "Fwhap... thwap... chwlap... khap...!"
    "It caused me to dig my fingertips deeper into Felicia's side and grip tighter, it caused me to thrust harder, and it put me ever-so slightly off tempo in our rutting dance."
    "At the present, there wasn't any place I'd rather be than balls deep in a gorgeous, extraordinarily libidinous, lewd and shameless trophy wife."
    "Like the [mcf] from Felicia's fantasy, everything about my daily life felt so insignificant and quaint in the face of the building pleasure."
    scene w2_4619 with pixellate
    fel "You're no longer a student right now. All that studying, that stressful daily grind to establish yourself as a respectable adult, that's out the window."
    fel "All you know right now is what's in front of you... a drooling cunt and ripe, fuckable asshole completely at your mercy."
    scene felh_dog4_a with pixellate
    show felh_dog4
    mct "(Fuckable asshole is right!)"
    "My head was completely full of the woman in front of me."
    fel "Ohoohoo... oh, fuck me, don't stop! Bastard!"
    "My ears were filled with her explicative-laden moans."
    "My sensation of touch - the ground beneath my feet and the cool air on my skin - were dead in the face of the overwrought excitement of rutting the blonde's ass. I was beginning to feel like I was floating."
    "Felicia's natural scent, marred by expensive perfume, hit the nerves of my nostrils and flooded my brain with pornographic images of bluster and violence."
    "All my eyes took in was the sight of Felicia's bouncing. The way her ass trembled with every down thrust, the way her ponytail danced about with an uneven rhythm, and the way her back arched with every surge of gut-wrenching pleasure."
    scene w2_4620 with dissolve
    fel "My point is, it isn't unnatural to lean into your desires..."
    "--This was the butt-fucked blonde's philosophy in action."
    scene felh_dog3_a with dissolve
    show felh_dog3

    if w2FeliciaDegrade:
        "At this moment, I was utterly consumed by this slut."
    else:
        "At this moment, I was swallowed whole and consumed by this woman."

    mc "Ah, shit... You...!"

    menu:
        "Play up the fantasy elements":
            scene felh_dog4_a with dissolve
            show felh_dog4
            mc "How does it feel?!"
            "A key component of Felicia's fantasy was having an audience to give her debasement added meaning."
            fel "G-good...!"
            "This may have not been the club stage, and we may be alone, but this office did have something I could work with to fan the flames of lust..."
            mc "How does it feel--"
            fel "Good! It feels--"
            mc "How does it feel to be fucked in the ass in front of your father-in-law?"
            scene w2_4594 with dissolve
            fel "O-oh...? Eh... it fe--"

            if feliciaAnger == True:
                scene w2_4595 with vpunch
                fel "Heug-!"
                mc "Wow, and here I thought pigs couldn't look up!"
                scene w2_4596 with dissolve
                fel "C-careful! I don't mind a little hair tugging, but I've g-got a sensitive scalp..."
                scene w2_4597 with dissolve
                "With a strong yank, I directed Felicia's eyes back at the portrait in front of her."
                mc "Don't look at me! Look at him!"
            elif w2FeliciaDegrade == True:
                scene w2_4595 with vpunch
                fel "Ungh-!"
                scene w2_4597 with dissolve
                "With a firm grip, I directed Felicia's eyes back at the portrait in front of her."
                mc "Don't look at me, slut! Look at him!"
            else:
                scene w2_4595 with vpunch
                fel "O-oh!"
                scene w2_4597 with dissolve
                "With a gentle tug on her ponytail, I redirected Felicia's gaze to the man in the portrait in front of her."
                mc "Don't look at me... look at him!"


            scene felh_dog2_a with dissolve
            show felh_dog2
            mc "You wanted an audience, right? That's part of your fucked-up little fantasy!"
            fel "Y-yes!"
            mc "Well, you've got one. The man is looking his daughter-in-law in the eyes right now as she gets railed in the ass!"
            fel "Ack-! Ah...!"
            scene felh_dog3_a with dissolve
            show felh_dog3
            "The dirty talk seemed to be working. The degrading words caused her ass to tug and clamp down on my dick."
            fel "H-he is!"
            mc "That's right, ah--!"
            "The feeling of tightness was overwhelming. Waves of pleasure colored my brain."
            mc "You really are shameless!"
            scene felh_dog4_a with dissolve
            show felh_dog4
            "Her ring hole practically formed a hermetic seal around my shaft.... her ass was quite literally sucking me in!"
            fel "Y-yes!"
            mc "Just a cock-hungry bitch!"
            fel "Yes!"
            mc "Drooling..."
            fel "Y-yhesh!"
            mc "...and babbling..."
            fel "Yes!"
            mc "For release!"
            scene felh_dog3_a with vpunch
            show felh_dog3
            fel "{b}{size=+20}YES!{/size=+20}{/b}"
            "How's this for being dragged into the muck? She fantasized about everyone being sucked into the madness. "
            fel "Yes, yes, yes, yes...!"
            "Felicia wanted the whole world to be as depraved as she. Somewhere within the fog of my sex-induced fugue state, I wondered..."
            mct "(Was it lonely?)"
            "A bizarre thought to have when you're plugging someone's ass with dick meat."
            fel "H-harder [mcf]... please!"
            mc "You want it harder...?"
            scene felh_dog4_a with dissolve
            show felh_dog4
            "By this point our pace was already testicle-bruising...!"
            fel "P-please!"
            mct "(The desperation in her voice...)"
            "I suppose I could still put my back into it. Careful what you wish for!"
            play sound "sound effects/thud-floor.mp3"
            scene felh_dog5_a with vpunch
            show felh_dog5

            if w2FeliciaDegrade == True:
                "Eat mahogany, slut!"
            else:
                "Down!"

            fel "Ye-!"
            "With a shove, I put my body weight on Felicia's shoulders and had her face down on the desk with the plan of using the superior position to fuck her senseless."
            fel "Ack...! Heug...! Y-you're... hitting new spots of me!"
            "With reckless disregard for my hips, I put everything I had into plowing the gold digger's ass."

            if feliciaAnger == True:
                "In short, I fucked her like I hated her -- which wasn't a difficult thing to conceptualize when I considered her place of privilege in the world."
                mc "Mmmgh...! You rich bitch!"
                scene felh_dog6_a with dissolve
                show felh_dog6
                "I thought of the scrimping and saving my mom did and the sacrifices she made... and it was easy to fuck Felicia like she asked."
                mc "You wealthy cunt! Does nothing satisfy you?"
                fel "A-aaah! Wha- heug!"
                "My hands thoughtlessly dug into Felicia's flawless, sun-kissed skin."
                mc "Is this how you \"earned\" all of this? Is this all you're good for?"
                fel "Ngh-! Hueg-! Heug-!"
                mc "Did you let Elias fuck your ass like this until he lost all sense and married a whore?"
                mc "Is this all you're good for, you fucking rich pig? Getting skewered on dick?"
                fel "Ah, f-fhuck...! Itz fheelz ghood! So...!"
                mc "Fuck you, fuck you, fuck you!"
            else:

                "In short, I fucked her like I was running out of time on this earth."
                mc "Ah...! This is what you want?"
                scene felh_dog6_a with dissolve
                show felh_dog6
                fel "Yes! This is... {b}perfect{/}!"
                mc "Does this make you happy?"
                fel "Yes! I'm happy!"
                "I held Felicia firmly in place as I hammered home. By this point, with Felicia growing tired and pinned underneath my weight, I was doing all the work."
                fel "Ah-! Hueg-! Heug-!"

                if felPN == "Daddy":
                    fel "Keep fucking my ass, Daddy!"
                else:
                    fel "Keep fucking my ass, stud!"

                "Felicia, to her credit, stayed sensate. She used her voice to feed my ego and led me to the conclusion she desired."
                mc "S-shut up, I'm trying to concentrate! What do you think I'm d-doing?!"

            scene felh_dog5_a with dissolve
            show felh_dog5
            "She had me giving my all. Thrusting away with mad abandon. She had me huffing and puffing, unable to catch my breath."
            "Soon, I was beginning to lose focus. Felicia and the table had merged in a haze of sex."


            if w2KatSex == True:
                if kat_polite == True:
                    "My back ached horrendously and I was assailed by a feeling of déjà vu, when Mrs. Pulman and I fucked to near oblivion."
                else:
                    "My back ached horrendously and I was assailed by a feeling of déjà vu, when Kat and I fucked to near oblivion."

                "--but the animal need boiling over in my nuts was far greater."
            else:

                "My back ached horrendously, but the animal need boiling over in my nuts was far greater."

            mc "Ah...! Ha...!"
            mc "Haaa...!"
            stop music
            play sound "sound effects/spurt.wav"
            scene w2_4598 with flash
            fel ".....yaaaaaaah!"
            mc "Ng! Shiiiit!"
            "Only one thing pulled me from my fuck-induced tunnel vision: the sudden release of sexual tension."
            play sound "sound effects/spurt.wav"
            scene w2_4599 with flash
            mc "--!"
            "For both of us."
            "The abrupt cock-choking compression around my dick was too much and sent me over the edge myself."
            "Before I had even realized I was cumming, I had already begun flooding Felicia's bowels."
            play sound "sound effects/spurt.wav"
            scene w2_4600 with flash
            fel "OoooooOoooooh, ghod! Tssh...!"
            "Her backdoor didn't let up. Felicia was as tense and taut as a piano string and her ass simply wouldn't let go."
            "Like dropping a bowling ball on a tube of toothpaste, it milked and milked my cock, pushing every milliliter of semen out of my urethra with ball-rending velocity."
            mc "Ah...!"
            play sound "sound effects/thud-floor.mp3"
            scene w2_4601 with vpunch
            fel "Fhuck...!"
            mc "S-shit..."
            "In a stupor, we both let out some last minute curses as I collapsed atop the well-fucked blonde."
            fel "Ha... ha..."

            if feliciaAnger == True:
                fel "That got pretty fucking intense there at the end but..."
            else:
                fel "I'm not going to be able to walk straight for a whole year, shithead."

            fel "That was something else. Thanks, [mcf]."
            scene black with fade
            if not persistent.w2FeliciaSex:
                play sound "sound effects/notification.wav"
                show memoryunlock with dissolve
                $ renpy.pause(3, hard=True)
                $ persistent.w2FeliciaSex = True
                hide memoryunlock with dissolve
                $ renpy.pause(0.5, hard=True)
            mc "Myhplheasure... Eye thwink..."
            $ renpy.end_replay()
            jump w2FeliciaMissionEnd
        "Stoke the fire a different way. Own her.":

            "This wasn't enough."
            "She had given me her ass, but it still wasn't enough. I wanted more."
            scene w2_4602 with hpunch
            "I wanted her close."
            fel "E-eh...?"
            scene felh_sdog1_a with dissolve
            show felh_sdog1
            "I wanted her body pressed into mine as I fucked her deep."
            fel "Gh...fewaah...?"

            if perk_strongman == True:
                "As she wasn't expecting it, forcing the blonde suddenly to her feet took some strength, but it wasn't anything I couldn't manage."
            else:
                "Forcing Felicia suddenly to her feet almost knocked me off mine, but after a bit of teeter-tottering, I managed to safely lock my knees and support the half-sensate blonde in my arms."

            fel "Holy...! That was...!"
            fel "I don't mind a little hair tugging you know, but a little warning next time would be nice. I've got a sensitive scalp..."
            mc "Ha, n-noted..."
            mct "(The casual way she spoke as I was balls deep in her ass... this woman!)"
            "After a dozen or so seconds of mismatched thrusting owed to the abrupt transition, we finally settled in on the right rhythm."
            scene w2_4603 with dissolve
            fel "Mmmh... we could've just done it like this in the first place if that's what you wanted..."
            "Felicia relaxed her upper body, content to be cradled in my arms."
            scene felh_sdog3_a with dissolve
            show felh_sdog3
            mc "I was starting to get a little cold and I wanted to get my hand on these."
            fel "Mmmn~oh!"
            fel "Greedy boy... my ass wasn't enough for you?"
            "As she spoke, the scent of fruity shampoo filled my nostrils."
            mc "I don't want to hear about greed from you of all people."
            fel "Ha... f-fhuuuuck... well, this is also nice in its own way."
            "One hand on her breast, my other rested comfortably on her toned midriff, ever so often catching the faintest trace of my dick as I slow pistoned deep into her guts."
            "I wanted her as close as she humanly could be."
            fel "Ha... ya...! {b}Really{/b} nice..."
            "The pace had slowed, but it was nonetheless ball-churning. Instead of the rapid, shallow, and desperate thrusts of a pair of animals, this was methodical. This was savoring every second."
            "I would slowly and teasingly retreat from Felicia's warm embrace, only to find myself hilted back in Felicia's ass with a powerful thrust."
            scene felh_sdog2_a with dissolve
            show felh_sdog2
            "With Felicia's back pressed into me and the evening sun filtering in through the skyrise's windows, I felt at ease for the first time this evening."
            "The immorality of this ceased to be a prodding question and instead everything was just... warm."

            if felPN == "Daddy":
                fel "Mmha... ah... Daddy... you're fucking me so good right now."
            else:
                fel "Mmha... ah... you're fucking me so good, stud."

            fel "It's like my ass belongs to you..."
            mc "Heug-!"
            "As if to underline her words, Felicia tightened her butthole and brought the pace down even slower and to a new level of pleasure."
            fel "Would you like that? To own my ass?"
            mc "I'd use it every day if I could..."
            fel "Well, what if I said you were the only man I gave my ass to for the rest of my life?"
            mc "I'd say you're just bullshittin' me."
            fel "Mmmh, maybe I am... but why do you think I want this so bad? It's been a while since anyone's used this hole."
            fel "I've... missed it, very much."
            scene felh_sdog1_a with dissolve
            show felh_sdog1
            "She said such an obscene thing in the cutest voice imaginable."
            fel "If you wanted, and if you keep fucking me like this, you could be the only one. {b}You could own this ass{/b}."
            "Even if I knew it was just ear service, she said it so convincingly."
            mc "C'mon now... the rest of your life?"
            fel "Ha..! Okay, how about for as long as we don't get tired of each oth- ohhmuhh!"
            "With added vigor, I pushed past the tight hold her asshole had on my cock and resumed fucking it long and hard in earnest."

            menu:
                "Play along.":
                    "If she wanted to pretend, we could pretend."
                    scene w2_4604 with dissolve
                    mc "Don't you think that... in a situation like this..."
                    "I brought my mouth to her head and poured the words directly into her ear."
                    mc "...Fucking you in your husband's office..."
                    scene w2_4605 with dissolve
                    fel "Mmmh..."
                    mc "That I already own your cheap ass?"
                    scene felh_sdog2_a with dissolve
                    show felh_sdog2
                    fel "Heug-!"
                    "As if to underline my own words, I drove every single inch of my dick as deep as it would go into her ass."
                    mc "Who owns this ass?"
                    fel "You do!"
                    mc "You? Who's you?"
                    mc "Tell me {b}who{/b} owns this ass, you bitch!"
                    fel "[mcf]...!"
                    fel "[mcf] owns this ass..."
                    scene felh_sdog3_a with dissolve
                    show felh_sdog3
                    mc "That's right! Your ass is mine, Felicia Ford!"
                    mc "It's mine whenever I want. If I'm bored, horny, or just pissed off... I can fill it full of cum as I see fit."
                    fel "Ooo-oh! Yes! Fill it!"
                    mc "Who owns this ass?"

                    if felPN == "Sir":
                        fel "Sir owns this ass...!"
                    elif felPN == "Daddy":
                        fel "Daddy owns this ass...!"
                    else:
                        fel "[mcf] owns this ass...!"

                    "Bullshit, but it sounded like honey to my lust-cooked brain."
                "Enjoy even more of her.":


                    scene w2_4604 with dissolve
                    mc "I don't think anyone has ever owned a single hair on your head, Felicia."
                    scene w2_4606 with dissolve
                    "Having told her my honest thoughts, I buried myself in her neckline, where I went to work planting kiss after kiss in search of an erogenous zone."
                    fel "Mmhh... idiot!"
                    "The way her body shuddered as the tip of my teeth grazed her delicate skin told me I had found it."
                    scene w2_4607 with dissolve
                    fel "J-just fuck me as if you own it, then."
                    "That I could do."
                    scene felh_sdog2_a with dissolve
                    show felh_sdog2
                    fel "Heug-!"
                    "As if to dramatically mark that very intent, I drove my dick as deep as it would go into the blonde's ass."
                    fel "G-good!"
                    mc "You like it?"
                    fel "I do... I love it."
                    mc "Then I have a request of my own to make: {b}look at me{/b}."
                    fel "H-huh? Okay..."
                    scene w2_4608 with dissolve
                    mc "Look me in the eye."
                    fel "That's what I'm--"
                    scene w2_4609 with dissolve
                    "With Felicia right where I wanted her, I did the one thing she probably didn't expect."
                    fel "Mmm...!"
                    "I kissed her."
                    "At first, she didn't return it, but every thrust into her ass broke down more and more of her defenses until..."
                    scene w2_4610 with dissolve
                    "She surrendered her mouth entirely to me."
                    fel "Mmmh...!"
                    scene w2_4611 with dissolve
                    fel "[mcf]... don't... that's not..."
                    scene felh_sdog3_a with dissolve
                    show felh_sdog3
                    "She didn't finish her thought."
                    fel "Ah, screw it..."

            "By now, the inner walls of her anus were slathered in my pre-cum, making the tunnel extraordinarily slick and easy to fuck."
            "To compensate for the decrease in tension, I slowed back down to the previously more deliberate pace."
            "Long, hard strokes. That was what I was going to use to make Felicia cream herself."
            scene w2_4612 with dissolve
            fel "Ack... ha... [mcf]..."
            scene w2_4613 with dissolve
            fel "My legs are turning to..."
            fel "Ah... I'm going weak in the..."
            scene w2_4614 with dissolve
            mc "It's fine, I've got you..."
            mc "Just relax and I'll make you feel good."
            scene w2_4615 with dissolve
            fel "Ha... {b}okay{/b}."
            scene felh_sdog4_a with dissolve
            show felh_sdog4
            fel "Hold on tight..."
            mc "{b}I've got you{/b}, Felicia."
            "The blonde let herself go limp under my reassurance, arms flopping to her sides and head coming to a rest on my shoulder."
            "The added dead weight made it more difficult to thrust, but it was manageable as long as I kept my legs firmly planted."
            fel "Ah... ha...! [mcf]..."
            "The way she now angled her hips added a new dimension to the ass-reaming. The head of my cock scraped along her rectum's wall in a more protracted curve."
            fel "[mcf]...!"
            "Every thrust digging into the sensitive nerves lining her anus and wrenching a lovely cry from Felicia's lips."
            fel "Mhaa.. ah~♥"
            "She was {b}purring{/b}."
            mc "{b}Felicia{/b}, you...!"

            if feliciaAnger == True:
                "Funny how it works..."
                "In lieu of the overwhelming pleasure, my disgust from earlier felt a distant memory."

            fel "I-ah, I..."
            "At this moment she was putty in my hands. Who she was or why she was doing this didn't matter."
            "We were just two people sharing in intimacy -- or as close as you can get in these utterly depraved circumstances."
            fel "Life is just... ah...♥"
            fel "Life is just an absurd game... in the face of this...♥"
            "In no way did I agree with her, but at this moment she was right."
            "Nothing. Else. Mattered."
            "All that mattered right now was plowing Felicia's ass until we collapsed into a heap on the floor, bodies aching and exhausted."
            "Nothing. Else. Mattered."
            "All that mattered right now was busting my load in the hedonistic blonde's ass and freeing myself from the beastly need."
            "Nothing. Else. Mattered."
            mc "Ah...!"
            "Five minutes after that... everything would matter."
            fel "Ha... yaa... heug...!"
            "Life would feel cold and deathly serious. People would become unknowable again. But right now..."
            "Nothing. Else. Mattered."
            mc "Felicia...!"
            "In reducing ourselves to the most simple and basest level, Felicia and I understood each other."
            fel "I k-know...♥"
            fel "Don't... ha... stop... ha... until you fill me... up~♥"
            fel "Until you...♥ ...pack my ass with...♥ ...your jizz~♥!"
            fel "Shoot it deep in my ass~♥ So I won't ever forget..♥!"
            scene felh_sdog5_a with dissolve
            show felh_sdog5
            mc "Arrrg...!"
            "My climax was precipitated by her bewitching words."
            "She pulled me into fucking her fiercely."

            if w2KatSex == True:
                if kat_polite == True:
                    "My back ached horrendously and I was assailed by a feeling of déjà vu, when Mrs. Pulman and I fucked to near oblivion."
                else:
                    "My back ached horrendously and I was assailed by a feeling of déjà vu, when Kat and I fucked to near oblivion."

                "--but the animal need boiling over in my nuts was far greater."
            else:

                "My back ached horrendously, but the animal need boiling over in my nuts was far greater."

            mc "Ah...! Ha...!"
            "Felicia felt heavier and heavier all of a sudden. The grip I had on her arms grew more precarious from the sweat of our exertion."
            mc "Haaa...!"
            "The feeling of electricity ran through my body and that inevitable nut-busting conclusion was nigh."
            mc "Here it comes...!"
            stop music
            play sound "sound effects/spurt.wav"
            scene w2_4616 with flash
            fel ".....yaaaaaaah!"
            "Felicia's ass went suddenly as tense and taut as a piano string."
            "It milked and milked my cock, squeezing every drop of semen out of my urethra with ball-rending velocity."
            play sound "sound effects/spurt.wav"
            scene w2_4617 with flash
            mc "--!"
            "If she wanted it deep, she got it deep."
            fel "OoooooOoooooh, ghod! Tssh...!"
            "My semen would line her bowels for days to come."
            mc "Ah...!"
            play sound "sound effects/thud-floor.mp3"
            scene w2_4618 with vpunch
            mc "Ack-!"
            fel "Heug...?"
            "And like that, I was ushered back through the doors to the cold and deadly serious reality, albeit with a well-fucked blonde on top of me."
            scene w2_4621 with dissolve
            fel "Ha... ha..."
            fel "Don't...♥ Forget it...♥!"
            scene w2_4622 with dissolve
            mc "Forget... what...?"
            scene w2_4621 with dissolve
            fel "I was the first... woman... you fucked in the ass...♥"
            scene w2_4623 with dissolve
            mc "Pftaha-! You gotta be--!"
            mc "I don't think that's a big deal for guys!"
            scene black with fade
            if not persistent.w2FeliciaSex:
                play sound "sound effects/notification.wav"
                show memoryunlock with dissolve
                $ renpy.pause(3, hard=True)
                $ persistent.w2FeliciaSex = True
                hide memoryunlock with dissolve
                $ renpy.pause(0.5, hard=True)
            "Well, maybe not so cold and serious..."
            $ renpy.end_replay()
            jump w2FeliciaMissionEnd


label w2FeliciaMissionary:

    scene w2_4624 with dissolve
    fel "You enjoy taking pictures of women?"
    scene w2_4625 with dissolve
    mc "That's..."
    mc "...well, don't want to step on Ian's thing."
    scene w2_4626 with dissolve
    fel "Oh, shit, that's right. I've been so caught up in this that..."
    fel "How is that kid doing?"
    scene w2_4627 with dissolve

    if minaFlag == True:
        mc "When I left her, she seemed... surprisingly okay. Determined, maybe?"
    else:
        mc "About as well as you can expect, I guess."

    scene w2_4628 with dissolve
    mc "We... should talk about it later though, when I'm not busy committing identity fraud and you're not butt-ass naked."
    scene w2_4629 with dissolve
    fel "Hmm... good point."
    scene w2_4630 with dissolve
    fel "Where were we? Oh, that's right..."
    scene w2_4631 with dissolve
    "Felicia took my hand and brought it up to her mouth, planting a gentle kiss on the underside of my wrist."
    mc "What are you doing?"
    scene w2_4632 with dissolve
    "Felicia's eyes honed in on the camera in my hand and gave a directing nod."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_4633 with dissolve
    "*Click*"
    "She delivered a loving look to the camera's lens."
    scene w2_4634 with dissolve
    fel "Why don't I... play the dutiful wife for the rest of the shoot?"
    scene w2_4635 with dissolve
    "Felicia followed up on her idea by sliding a finger into her mouth and giving it an affectionate taste."
    scene w2_4636 with dissolve

    if w2HanaSex == True:
        mct "(That's twice in one week...)"
    else:
        "Her mouth teased the tip of my finger as if she was simulating fellatio."

    "All the while, she kept her eyes turned toward me with a lustful gleam, waiting for..."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_4637 with dissolve
    "*Click*"
    scene w2_4638 with dissolve
    fel "A little make-believe can be fun, y'know..."
    scene w2_4639 with dissolve
    "To make her point, she used her long and shapely legs to pull me closer and hold me in place."
    scene w2_4640 with dissolve
    fel "Get a taste of the good life."
    fel "Perform your husbandly duties, [mcf]."
    scene w2_4641 with dissolve
    mc "Don't you... live this \"roleplay\" every day of your life?"
    scene w2_4642 with dissolve
    fel "This is about getting {b}you{/b} into an agreeable mindset, stud. Not me."
    fel "I just want to fuck and have the best shoot, in that order."
    scene w2_4643 with dissolve
    "I had no real interest in calling Felicia \"honey\" but it did get me thinking..."
    scene w2_4644 with dissolve
    "If I had all this material wealth and a beautiful wife like Felicia, would I be content? Would I be happy? Would I give up on the idea of being decent?"
    "Whenever I imagined the prosperous future I was working toward, it was always..."
    scene w2_4645 with pixellate
    "Practicing medicine while living someplace warm and tropical with Mom, where she could enjoy the climate and a life of carefree leisure."
    "In contrast to that vision, this..."
    stop music fadeout 3.0
    scene w2_4644 with pixellate
    "{b}All of this{/b}... just seemed gaudy."
    scene w2_4646 with dissolve
    "Being wrapped in Felicia's legs, however, did have its undeniable charms though."
    scene w2_4647 with dissolve
    fel "You're smiling?"
    scene w2_4646 with dissolve
    "I had thought of something really nice, but I wasn't going to share that with her. Instead..."
    play sound "sound effects//zipper.wav"
    scene black with fade
    mc "Alright then. Let's fuck."
    scene w2_4648 with fade
    fel "Is that for me, {i}hun{/i}?"
    scene w2_4649 with dissolve
    "Despite how often I see her like this, her body still had the capacity to stun lock me."
    scene w2_4650 with dissolve
    fel "Hurry up, pretty please?"
    scene w2_4649 with dissolve
    "When she wanted to be, the cocksure woman could sound so painfully pathetic and wistful."
    scene w2_4651 with dissolve
    "She was right; there's no need to stop and smell the roses. In this position, the whole ride was going to be a scenic view."
    "I might as well..."
    play music "music/thunder.ogg"
    scene w2_4652 with dissolve
    fel "Mmmh..."
    "Hurry up."
    scene felh_mis1_a with dissolve
    show felh_mis1
    "Felicia's body accepted me readily, my dick snugly slipping into her lower mouth with pleasurable ease."

    "After allowing myself to soak for a moment in Felicia's warm embrace, and giving her a nod signaling my intent, I launched into fucking the waiting wife with vim and vigor."
    fel "Ooooh, ah...!"

    if feliciaSex == True and prAfterParty == False:
        "For the second time ever, I was balls deep in Felicia's cunt."
    else:
        "For the first time ever, I was getting a taste of Felicia's cunt."

    fel "That's right, stud. Fuck me... long... and hard, just like that~♥."
    "Felicia demanded of me what didn't need to be said, in a clear and rapturous voice."
    fel "Mmmh...hmm...mh...♥"
    "Cooing and purring in a sing-song way, like a kitten eagerly lapping up milk."
    fel "Ah...♥ Ha...♥ {b}Fuck{/b}, you guys talked for SO. DAMN. LONG."
    "Felicia and I quickly settled ourselves into an agreeable rhythm, matching our movements and pushing and pulling each other's bodies in the bid for pleasure."
    fel "You have any idea, how tortuous it was to wait?"
    "All the while, Felicia comfortably leaned back and braced herself on her husband's desk."
    mc "I have an... idea."
    "Felicia's frivolous video call was the damning evidence of that need, after all."
    scene felh_mis3_a with dissolve
    show felh_mis3
    fel "Mmmh...hmm...mh...♥"

    if w2FeliciaExtra == True:
        fel "I know~♥ Did my lil' show get you rock hard while you tried to keep your composure with your stupid questions?"
        fel "Were you able to maintain eye contact?"
        fel "Did you enjoy pushing the buttons?"
        mc "Yes... no... yes."
        fel "Mmmh...hmm...mh...♥ Why was that so fun, [mcf]?"
        fel "Ah--♥ J-just the thought of earlier... the t-toys and s-sitting next to...!"
        fel "Sometimes I even surprise myself.... It was way past okay and I was {i}terrified{/i}, but... ah-♥"
    else:

        fel "Mmmh...♥ Why was that so fun, [mcf]?"
        fel "Sometimes I even surprise myself.... It was way past okay and I was {i}terrified{/i}, but... ah-♥"
        fel "Did you enjoy pushing the button?"
        fel "Ah--♥ J-just the thought of earlier... the t-toys and s-sitting next to...!"

    fel "Take responsibility and fuck me until I'm sick of it~♥"
    scene felh_mis2_a with dissolve
    show felh_mis2
    "As she worked through the perverted recollection, the grip she had on little [mcf] would tug and tighten in an erotic ebb and flow."
    "The toying from earlier had done the trick. Felicia was raring to go, her insides greedily sucking me and already attempting to coax out a load from my balls."
    mc "Nng, that's...!"
    "If it wasn't for how soaked she was, I might have never pried myself from her twat's full dick massage."
    mc "D-damn, you're wet..."
    fel "Hmpfh...♥ Feeling good?"
    scene felh_mis3_a with dissolve
    show felh_mis3
    "She asked a question she already knew the answer to."
    mc "Yeah... it feels amazing."
    fel "{b}You{/b} feel amazing, stud!"
    "The lusty blonde kept her eyes directed my way, front and center."
    "My eyes on the other hand didn't quite know what to focus on."
    "Do I look at her breasts, which hypnotically bounced with every thrust?"
    "Do I drift my gaze down to her toned midriff, whose dancer-like undulation threatened the inevitable conclusion of an early climax?"
    "Do I return back up to Felicia's face, whose fiery gaze wavered and flickered with every pang of pleasure?"
    mc "F-fuck..."
    scene felh_mis1_a with dissolve
    show felh_mis1
    "I considered the question again."

    if felPN == "Daddy":
        fel "Mmmh...hmm...mh...♥ Fuck this pussy like you own it, Daddy."
    else:
        fel "Mmmh...hmm...mh...♥ Fuck this pussy like you own it, [mcf]."

    mc "...!"
    "If I had all this material wealth and a beautiful wife like Felicia, would I be content? Would I be happy? Would I give up on the idea of being decent?"
    "My original feelings remained, but the fantasy in front of me felt more agreeable when viewed alongside the mitigating circumstance of dicking down the beautiful blonde."
    mc "Y-you... {b}really{b} know how to make a guy feel wanted."
    "With her diction alone, this woman could lead me by the dick."
    fel "Ah~ha... call it a... job qualification. Ha...♥ Ah...♥"
    "Still..."
    fel "Not that I ain't sincere when I say... {b}I love your dick♥{/b}."
    mc "You-!"
    scene felh_mis2_a with dissolve
    show felh_mis2
    fel "Mhh..! Oh...!?"
    "While I enjoyed the dirty talk..."
    "I did take the fact she could still express complex thoughts as a personal challenge."
    fel "What's gotten into you? Ah...♥ You look... haaa... determined~♥"
    mc "You're talking too much."
    scene w2_4653 with dissolve
    fel "Mmmh...?!"
    "Lunging forward, I stole Felicia's lips. At first, she was surprised."
    scene w2_4654 with dissolve
    "...but every time my cock hammered into her cunt, more and more of her mouth pried open."
    fel "Aghh...! Fwh....♥"
    scene felh_mis2_a with dissolve
    show felh_mis2
    fel "Ha... ha....♥"
    "Fwhip.. schluwp...!"
    fel "Message received...♥"
    "Fwhip.. schluwp... schluppp...!"
    scene felh_mis1_a with dissolve
    show felh_mis1
    "For what felt like an eternity, we shared in a fuck-induced comfortable silence, the only thing reaching our ears was the creak of her husband's desk and the slick squelching of frantic copulation."
    fel "Ha... ah, ha...!"
    "Nothing hindered our rut."
    "I simply enjoyed the position of power, of Felicia's legs splayed open, offering unfettered access to the deepest parts of her."
    "Over and over I slammed home and Felicia gave as good as she got, rushing to meet me at the apex of every thrust."
    fel "Ah, s-shit... my arms are feeling a bit..."
    mct "(It's not enough!)"
    scene w2_4654 with dissolve
    fel "Mmmh...♥"
    "Again, I attacked the blonde's lips."
    "This time she expected it and accepted it without hesitation."
    scene w2_4655 with dissolve
    mct "(It's not enough!)"
    "I could feel myself losing composure as violent need took hold of my faculties."
    scene w2_4654 with dissolve
    "The drive to own and ruin her, to do whatever it took in the delirious rush to push hot cum out of my urethra and paint Felicia in my color."
    scene w2_4656 with dissolve
    fel "Ah...!"
    "There was my chance."
    scene w2_4657 with dissolve
    "Felicia fell backwards onto the desktop and I saw the opportunity to seize control..."
    "Or so I thought."
    scene w2_4658 with dissolve
    mc "--?!"
    "No sooner than she had hit the mahogany surface, did the blonde wrap her long and shapely legs around my waist and pull me along for the ride."
    scene felh_mis4_a with dissolve
    show felh_mis4
    fel "Mmmh...♥"
    fel "Easier on the elbows~"
    "Despite the abrupt change in position, neither of us missed a beat."
    mc "Ngh... ha...! Felicia...!"
    fel "Ha...♥ Mhaaa...♥ [mcf]!"
    scene felh_mis5_a with dissolve
    show felh_mis5
    fel "[mcf]...♥"
    "If I had all this material wealth and a beautiful wife like Felicia, would I be content? Would I be happy? Would I give up on the idea of being decent?"
    "At this moment, the thought was yes. At the very least, I'd fuck her every day."
    "I'd fuck her even after I got sick of it."
    mc "Ah...!"
    scene felh_mis4_a with dissolve
    show felh_mis4
    "It was the sort of haphazard, lust-induced thought that would disappear as quickly as the post-nut clarity hit me, but at this moment this was all there was in the world."
    "We were just two people sharing in intimacy -- or as close as you can get in these utterly depraved circumstances."
    "Nothing else mattered, except plowing Felicia's cunt until we collapsed from exhaustion."
    fel "Mmh...♥ "
    fel "Ah... [mcf]...♥"
    fel "[mcf]...? H-hey...?"
    "It took me a minute to register that she was calling out my name in the form of a question."
    mc "Ah, y-yeah? What is it?"
    scene w2_4659 with dissolve
    fel "Ha... k-kiss me again, stud."
    mc "I tho-"
    scene w2_4660 with dissolve
    mc "...?!"
    "Felicia initiated our embrace this time, wrapping her arms around me and attacking my mouth with urgency."
    fel "Mmmh...♥"
    "Her tongue took the lead in the dance, overpowering and lulling mine into submission."
    scene w2_4661 with dissolve
    fel "Ha...♥ Something about this position, I guess..."
    scene felh_mis6_a with dissolve
    show felh_mis6
    fel "Haaaaaaaaaaaaaaaaaaaaaa!?"
    "That last admission was the kick I needed to finally put me over the edge and into overdrive."
    "I bucked faster, the head of my dick forcefully scraping the inside of Felicia's vagina and eliciting louder and more discordant cries from the blonde's throat."
    fel "Ha...! Ha...! Oh, God. Oh, yes-♥"
    "Everything felt muggy. My shirt was drenched in sweat."
    mc "Ha...! Ngh, ah...!"
    "My glasses fogged up something fierce, which suited me just fine, because by this point I wasn't even really seeing Felicia anymore. All my brain power went to keeping my hips pistoning past the point of exertion."
    "Then suddenly..."
    scene w2_4662 with flash
    fel "Oh, oooh aaaaah...♥♥♥"
    "In an instant, all sexual tension in the humping blonde reached its peak."
    "She clamped down hard on my shaft and her eyes clouded over, rolling to the back of her head."
    scene felh_mis6_a with dissolve
    show felh_mis6
    fel "Ha...♥ K-keep going, don't stop fucking me!"
    "Despite her release, she still bid me on."
    mc "Ha...! But I..."
    "I was nearing the end of my rope as well."
    mc "Ha...! S-shit, I'm getting close. Should I-?"
    fel "N-no!"
    "Her legs gripped me tighter, refusing me escape, and giving me no choice."
    fel "C-cum inside me. It's safe...♥"
    fel "Let me have every last drop from your balls...♥"
    "It was a request I was in a position to fulfill and fill I did."
    stop music
    play sound "sound effects/spurt.wav"
    scene w2_4663 with flash
    fel "Ahh...♥"
    "The moment my seed ejected from my urethra and flooded the blonde's womb, Felicia used all four of her limbs to pull me even deeper inside her, clinging to me with a breath-taking tightness."
    fel "Ahh... ah...♥ That's right...♥"
    "In my befuddled state, I gave her everything I had."
    play sound "sound effects/spurt.wav"
    scene w2_4664 with flash
    fel "Oh...?! F-fhuck...!"
    "And as if she wasn't satisfied with that, her inner walls coaxed out even more cum when a second orgasm rocked her body."
    fel "Ah... yesh...♥ Very... ah... ha...♥"
    play sound "sound effects/thud-floor.mp3"
    scene w2_4665 with vpunch
    mc "Ah... ha... ha..."
    "Felicia rubbed my back tenderly."
    fel "Ha... ha...♥ That was..."
    fel "Nice, [mcf]. That scratched the itch."
    "Her touch was warm and comforting."
    fel "Ha..."
    "So comforting that it threatened to lull me asleep."
    "..."
    scene w2_4666 with dissolve
    mc "Ah... crap."
    fel "What?"
    $ renpy.end_replay()
    scene black with fade
    if not persistent.w2FeliciaSex:
        play sound "sound effects/notification.wav"
        show memoryunlock with dissolve
        $ renpy.pause(3, hard=True)
        $ persistent.w2FeliciaSex = True
        hide memoryunlock with dissolve
        $ renpy.pause(0.5, hard=True)
    mc "We should've taken some pictures."
    fel "Pft...!"
    "She simply laughed at the dumb realization."
    jump w2FeliciaMissionEnd




label w2FeliciaSoloFinish:

    "Over the next half hour, for the rest of the shoot, we had carte blanche of the penthouse."
    play sound "sound effects/camera-phone-shutter.wav"
    hide screen textbox2 with dissolve
    scene w2_4667 with cmet
    "So we gave the club's patrons a little room-by-room tour, courtesy of the woman of the house."
    scene w2_4668 with blinds
    "It was a more tasteful shoot than when directly compared to the other two, but I hoped the woman and the location would carry the day."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_4674 with dissolve
    mc "It's too bad that video call wasn't recorded..."
    scene w2_4675 with dissolve
    fel "Don't you want me to do something besides... pose? Something more fun maybe?"
    mc "No, we'll leave the viewer wanting more."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_4669 with blinds
    mct "(Ha... nice view...)"
    scene w2_4676 with blinds
    "It all culminated in a final series of photos of her jilling off on her husband's desk."
    "Indeed, the sordidness of the scenario... that was key."
    fel "Mmmhh..."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_4677 with dissolve
    fel "--geh!"
    scene w2_4678 with dissolve
    mc "I think that's a wrap. I'm starting to feel a little thirsty."
    scene black with fade
    mc "How 'bout you?"
    jump w2FeliciaMissionEnd



label w2FeliciaSoloFinishDegrade:
    stop music fadeout 3.0
    hide textbox2 with dissolve
    "Over the next half hour, I had carte blanche of both Felicia and the penthouse."
    "The theme was {i}house tour{/i}."
    $ renpy.end_replay()
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_4670 with blinds
    "Some of it was really fucking silly."
    scene w2_4671 with dissolve
    "Some made me painfully erect."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_4672 with blinds
    fel "H-hey... don't!"
    "Some managed to dredge up a look of genuine surprise."
    play sound "sound effects/camera-phone-shutter.wav"
    scene w2_4676 with dissolve
    "It all culminated into a final series of photos of her jilling off on her husband's desk."
    "Indeed, the sordidness of the scenario... that was key."
    fel "Mmmhh..."
    scene w2_4677 with dissolve
    fel "--geh!"
    scene w2_4678 with dissolve
    mc "I think that's a wrap. I'm starting to feel a little thirsty."
    scene black with fade
    mc "How 'bout you?"
    scene black with fade
    jump w2FeliciaMissionEnd


label w2FeliciaMissionEnd:

    "......"
    "..."
    play music "music/jazz-piano-bar.ogg"
    scene w2_4679 with blinds
    show screen textbox2 with dissolve
    mc "Ha..."
    scene w2_4680 with dissolve
    "Before making the trek back home, I took a moment to clear my mind and calm my nerves."
    "A topside view, in a luxury penthouse apartment, did seem better for that task than a subway train."
    scene w2_4707 with dissolve

    if w2FeliciaImpressed == True:
        "After we had screwed, I took photos of the aftermath. {i}That{/i} was the purpose of the evening, right?"
    else:
        "After the shoot, we took a rest downstairs and enjoyed the view of the city."

    if w2FeliciaImpressed == True:

        if edwinAnal == True:
            "I got some choice shots of her ass leaking my cum and making a mess of Elias' office. Hell, we even..."
        else:
            "I got some choice shots of her cunt leaking my cum and making a mess of Elias' office. Hell, we even..."

        scene w2_4673 with pixellate
        "Padded the shoot with Felicia playing the housewife."
        "That was... \"fun\", to say the least. I'd bank on those perverted assholes loving that."
        scene w2_4681 with pixellate
        fel "What are you thinking about?"
    else:
        scene w2_4681 with dissolve
        fel "What are you thinking about?"

    scene w2_4682 with dissolve
    "Felicia pulled me away from my thoughts and back to her idle company."
    scene w2_4683 with dissolve
    mc "Hmmm, well... truthfully, I'm thinking about something that will annoy the piss out of you."
    scene w2_4684 with dissolve
    fel "Oh? Should I try and guess what it is? Nah..."
    fel "Just spit it out and let me be the judge of that."
    scene w2_4685 with dissolve
    mc "Okay, then. What made you change your mind earlier?"
    scene w2_4686 with dissolve
    fel "You're going to have to be more specific, stud."
    scene w2_4687 with dissolve
    mc "I mean, what convinced you to go along with the toy plan? You were against it, until you suddenly... weren't."
    scene w2_4688 with dissolve
    "She had come around to it after Elias' patronizing interruption."
    scene w2_4689 with dissolve
    fel "Why are you so curious about that?"
    scene w2_4688 with dissolve
    mc "How could I not be? You had a pretty dumbass reason for whoring yourself out, but then you dropped an interesting line."
    scene w2_4690 with dissolve
    fel "Not mincing your words, are you?"
    scene w2_4689 with dissolve
    fel "So, what did I say?"
    scene w2_4688 with dissolve
    mc "Something like... \"I remembered why I wanted to do this in the first place,\" I believe."
    scene w2_4689 with dissolve
    fel "Ah, yeah. That would raise some questions..."
    scene w2_4691 with dissolve
    fel "I don't even remember saying that, but I guess I'll chalk it up to the stress and being in the moment."
    scene w2_4692 with dissolve
    mc "So, why {i}do{/i} you want to become a member of that place?"
    scene w2_4693 with dissolve
    fel "Hmm~ ah..."
    scene w2_4694 with dissolve
    fel "You can't just let it end at this all being for funsies? Because while it partly is, the precise reason isn't any more sympathetic."
    scene w2_4695 with dissolve
    "So there was something deeper than she originally let on."
    scene w2_4696 with dissolve
    mc "I can't force it out of you, but I would like to know."
    scene w2_4694 with dissolve
    fel "You could ask your boss. Pretty sure she read me like a book."
    fel "What with the oh so many pointed questions about my past and what my plans were should I win. Bitch really knows how to beat around the bush."
    scene w2_4696 with dissolve
    mc "There wasn't anything like that in your file."
    scene w2_4695 with dissolve
    "I think she wants me to figure this stuff out on my own, but I didn't say as much to Felicia."
    scene w2_4697 with dissolve
    fel "Hmmm... ah, fine. You've met him, so you'll get it."
    fel "However, if you want to know..."
    scene w2_4698 with dissolve
    "*Glug, glug, glug...!"
    scene w2_4699 with dissolve
    fel "Let's go for a ride. "
    scene w2_4700 with dissolve
    mc "Where to?"
    scene w2_4701 with dissolve
    fel "My favorite place in the city, although we're not going to stay. I'm going to crash at Mina's tonight, but I want to grab some \"recreational\" fun first."
    scene w2_4702 with dissolve
    mc "It's not a club, right? I don't want to go to a club."
    scene w2_4703 with dissolve
    fel "Nah, farthest thing from that actually."
    fel "It's a bit of a drive, but if you ride with me and help me stave off the boredom, I'll answer your question. Sound fair?"
    scene w2_4704 with dissolve
    mc "Hmmm..."

    if feliciaFlag == True:
        "I didn't really feel like a long car ride, but at least it would be in Felicia's company. Plus, I really did want to know her real reason for doing all of this."
    else:
        "Truthfully, I didn't really feel like a long car ride, but knowing what motivated Felicia would help with my job of everyone finishing out the month. Out of all the Carnations, she was the most likely to just walk away on a whim."
        "Plus, I was curious..."

    scene w2_4705 with dissolve
    mc "Alright. Sure, it's a deal."
    scene w2_4706 with dissolve
    fel "Great! Oh, and uh..."
    stop music fadeout 3.0
    scene black with fade
    fel "If we get pulled over on the way back, you're holding."
    mc "Holding what?"
    "......"
    "..."
    jump w2FeliciaGarden


label w2FeliciaGarden:
    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionfelicia05 with blinds
    $ renpy.pause(6, hard=True)
    scene w2_4708 with cmet
    $ date = "june11night"
    show june11night with squares
    play sound "sound effects/car-beep.wav"
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    "Felicia drove fast. Uncomfortably fast."
    "Even so, even with only light traffic, it was a forty-five minute drive."
    play ambient "sound effects/city-night.wav"
    scene w2_4709 with dissolve
    "Eventually, we arrived at a building on the outskirts of the city, in a yuppie-like bougie neighborhood."
    scene black with fade
    mc "Do we have to take the stairs the rest of the way?"
    "I half expected to find a whole other sex club at the top of this place."
    scene w2_4710 with dissolve
    "Instead, on the other side of the door, was a rooftop garden."
    mc "{b}This{/b} is your favorite place in the city?"
    "I mean it was nice - very nice even - but for a woman who lived in a penthouse, it seemed relatively banal."
    scene w2_4711 with dissolve
    fel "Yep, you could call it my... ah, secret hideout?"
    fel "No one, but a few people know about it. Just the man who lends it to me, yours truly, our bubbly friend, and now... {b}you{/b}."
    scene w2_4712 with dissolve
    "The rooftop was wellfurnished. There was an easel with canvas standing proudly near some stairs, plus a variety of tables and comfortable looking seating."
    mc "Lucky me."
    scene w2_4713 with dissolve
    mc "So, secret hideout, huh? Like a supervillain?"
    scene w2_4714 with dissolve
    fel "Nah, it's just a place to get away. I just come up here when I want to think. Or when I don't want to think. Or..."
    scene w2_4715 with dissolve
    mc "Or when you want to paint?"
    scene w2_4716 with dissolve
    fel "I don't like to call it that."
    fel "I don't do anything as inspired as \"paint\". I just kill time."
    mc "Really? It's not finished, but even I can tell it's good."
    scene w2_4717 with dissolve
    fel "Thank you for saying as much, [mcf]."
    scene w2_4718 with dissolve
    "Her tone told me she didn't believe my words."
    scene w2_4719 with dissolve
    mc "You don't agree?"
    scene w2_4720 with dissolve
    fel "I'm just saying painting isn't about a work being pleasing to the eye."
    scene w2_4719 with dissolve
    mc "...at the risk of sounding like a rube, {i}isn't it?{/i}"
    scene w2_4721 with dissolve
    fel "Ah... well, not for me."
    scene w2_4722 with dissolve
    "She chose not to elaborate beyond a weak smile."
    scene w2_4721 with dissolve
    fel "Well, since you upheld your side of the bargain, I guess it's only fair I answer your question now."
    fel "Ask away."
    scene w2_4723 with dissolve
    mc "Well, then? You already know what I was curious about."
    stop ambient fadeout 3.0
    scene w2_4724 with dissolve
    fel "Let's sit down and get comfortable first."
    scene black with fade
    mc "Alright..."
    play music "music/Moonlight-Sonata.ogg"
    scene w2_4725 with dissolve
    fel "So, yeah... it's not a complicated answer, but..."
    scene w2_4726 with dissolve
    fel "Shit, how should I put this? I... uh..."
    scene w2_4727 with dissolve
    "Felicia looked at me like I could help with her loss of words."
    scene w2_4728 with dissolve
    fel "I asked to become a member because...I'm treading water and it feels like I'm getting awfully fuckin' stagnant."
    "She found the words."
    scene w2_4729 with dissolve
    mc "So you're... {i}bored{/i}? That's it?"
    "That answer was no different than her saying she was doing this for fun."
    scene w2_4730 with dissolve
    fel "No! it's not because I'm bored, it's because... ah...!"
    fel "To put it simply, the club represents an open possibility."
    scene w2_4731 with dissolve
    "I sort of understood what she meant, because I was profiting off my position, but I didn't understand how that was true for her."
    mc "What possibility?"
    scene w2_4732 with dissolve
    fel "To {b}advance{/b}."
    fel "You see, no surprise, but I've always thought of life as a ladder. Not exactly a novel way of looking at things, but when climbing, you should always focus on moving to the rung in front of you."
    scene w2_4731 with dissolve
    mc "Sure, okay. Breaking your goals down into actionable steps is fundamental to achieving them, right?"
    scene w2_4734 with dissolve
    fel "Right. That's just common sense."
    scene w2_4733 with dissolve
    fel "So, the starting rung on the ladder was being born poor, in a small nowhere town with backwards people who conflated their ignorance as simple, honest living."
    scene w2_4731 with dissolve
    "Her voice oozed contempt when talking about where she came from. It was the most vitriolic I'd ever heard the seemingly carefree blonde sound."
    mc "Was it really that bad?"
    scene w2_4736 with dissolve
    fel "I won't tell you there wasn't anything redeeming about the town of Wheatley, but what good there was was a silver lining on a big, fat storm cloud."
    scene w2_4734 with dissolve
    fel "Luckily though, through complete fucking luck of the draw, I was born pretty."
    scene w2_4737 with dissolve
    mc "Not just pretty, but smart."
    "-- a dangerous combination."

    if w1FelGonzo == True:
        mc "I remember you said you got out of there as soon as you could."
    else:
        mc "I imagine you got out of there as quick as you could?"

    scene w2_4732 with dissolve
    fel "Ah, yeah... you see I noticed at way too young of an age the way men would look at me, and of course, a whole lotta life had to be packed into my adolescence before I had the courage and wherewithal to effectively wield it, but when I did..."
    fel "I got myself a bus ticket out of town and took it all the way to the city, where I had an online \"friend\" that was willing to foot my rent while I worked to get accepted into college."
    scene w2_4731 with dissolve
    mc "Sounds more like a sucker than a friend."
    scene w2_4733 with dissolve
    fel "Well, I wouldn't be here without that sucker. I prefer to think of him in fonder terms."
    scene w2_4731 with dissolve
    "She sounded genuinely grateful."
    scene w2_4735 with dissolve
    fel "Anyway, there began my climb - in case you forgot the hackneyed metaphor that started this conversation, all the way to become the woman in front of you."
    scene w2_4732 with dissolve
    fel "To what I considered my absolute peak."
    scene w2_4731 with dissolve
    mc "How does this tie into the club being an opportunity for you?"
    scene w2_4732 with dissolve
    fel "The key thing here is I {b}considered{/b} it to be my peak. Given the extent of my resources and the clock on my natural commodities, I had decided that's where I'd stop and find contentment."
    scene w2_4731 with dissolve
    mc "The \"clock on your natural commodities\"? Jesus Christ, that's a cold take."

    if w2FeliciaDegrade == True:
        scene w2_4736 with dissolve
        fel "Well, the sky's blue and I'm a gold-digging whore. You seemed pretty eager to agree with that earlier."
        scene w2_4731 with dissolve
        mc "That was different, I was a bit..."
        "Horny."
    else:
        scene w2_4736 with dissolve
        fel "Well, the sky's blue and I'm a gold-digging whore. Do you really want to rehash our earlier conversation?"
        scene w2_4731 with dissolve
        mc "No, I guess not."


    if feliciaFlag == True:
        scene w2_4738 with dissolve
        fel "So, all this to answer your question with one of my very own..."
        scene w2_4739 with dissolve
        "Felicia looked at me, with an unfashionably sad glint in her eye."
        scene w2_4740 with dissolve
        fel "...why the hell couldn't I have been happy with where I landed, [mcf]? I should've wanted for nothing."
        fel "Why did that damn school have to close?"
        scene w2_4741 with dissolve
        mc "School?"
        scene w2_4742 with dissolve
        fel "Kennedale Children's Academy for the Arts..."
        scene w2_4743 with dissolve
        "Felicia twitched and gritted her teeth. The name conjured ill feelings for the blonde."
        scene w2_4744 with dissolve
        fel "That fuck head! It wasn't that much money... not for him... it would've been a drop in the bucket... it... it...!"
        scene w2_4745 with dissolve
        fel "I pleaded with Elias to save it. I did something I promised myself I'd never do after leaving home: I {b}begged{/b} for something. I laid myself bare to the prick."
        fel "I explained to him how important that school was to me, how the woman who ran it impacted my life, and what it would mean for future boys and girls who didn't have much..."
        scene w2_4746 with dissolve
        mc "Hold up..."
        scene w2_4747 with dissolve
        "She was getting on a tangent and I wasn't exactly clear on the subject she was ranting about."
        scene w2_4745 with dissolve
        fel "I put myself genuinely out there and he didn't give a good goddamn! The \"PR of saving a community arts academy in a shitty town\" simply wasn't worth it!"
        scene w2_4748 with dissolve
        fel "I mean... fuck, {b}HE{/b} doesn't get to call it shitty. I do! Just me!"
        scene w2_4745 with dissolve
        fel "He fucking grew up in a goddamn palace!"
        scene w2_4747 with dissolve
        "More pieces fell into place and Felicia's motivation revealed itself."
        scene w2_4746 with dissolve
        mc "So this is about an art school you went to as a kid closing down...?"
        scene w2_4749 with dissolve
        fel "Y-yes... it was funded by an old trust. Kids could go there for free."
        fel "I could crack open a thesaurus and put it a million different ways, but I'll never be able to articulate just how much that place truly meant to a poor little girl whose mother could only afford colored pencils for her 8th birthday."
        scene w2_4750 with dissolve
        mc "Sounds like you did just that for your husband."
        scene w2_4749 with dissolve
        fel "Yeah... I wouldn't let it go. Eventually, he told me in no uncertain terms to get over it and behave myself."
        scene w2_4751 with dissolve
        fel "It wasn't that much money..."
        scene w2_4752 with dissolve
        fel "I had no illusion of the nature of our relationship, but I foolishly thought that after some time, he might have the smallest amount of respect for me."
        scene w2_4752 with dissolve
        fel "I'm... a fuckin' moron."
        scene w2_4754 with dissolve
        mc "You have pull with other wealthy people, right? Couldn't you have..."
        scene w2_4755 with dissolve
        fel "Truthfully? I was afraid."
        scene w2_4731 with dissolve
        mc "Of your husband?"
        scene w2_4756 with dissolve
        fel "Yeah, I could've done more, but I \"knew my place\". I let the most precious thing of my life disappear because I was afraid of upsetting the status quo."
        scene w2_4736 with dissolve
        fel "If the school suddenly found funding by one of our acquaintances, he would've known I disobeyed him and didn't drop it. At the time, I was afraid to jeopardize my standing."
        scene w2_4731 with dissolve
        mc "When was this?"
        scene w2_4732 with dissolve
        fel "A year and a half ago."
        scene w2_4733 with dissolve
        fel "I tried to get over it, but over time I've just gotten more angry about it..."
        scene w2_4731 with dissolve
        mc "So if the academy is already closed, is working at the club your way of getting revenge then?"
        scene w2_4757 with dissolve
        fel "Revenge...?"
        "She looked at me like I was stupid."
        scene w2_4733 with dissolve
        fel "Any incidental hit to Elias' reputation is a big, big, BIG upside, but..."
        scene w2_4736 with dissolve
        fel "I'm not taking such a big risk because I'm having a temper tantrum. I'm doing it because I've realized the extent of my reach. For once there was something beyond creature comforts that I actually wanted and it wasn't within my power to protect."
        scene w2_4732 with dissolve
        fel "You asked me what I meant by the club representing an opportunity for me? Well, I want to build connections independent of my husband."
        fel "I want to have options. I want to use the club to make my own money."
        scene w2_4731 with dissolve
        mct "(So, that's it...)"
        mc "How do you plan on doing that?"
        scene w2_4758 with dissolve
        fel "One rung at a time, [mcf]. Life is a ladder."
        scene w2_4731 with dissolve
        "To be honest, that seemed no less stupid to me than doing it for kicks, but her admission about the school..."
        mc "Thanks for telling me, Felicia."
        scene w2_4737 with dissolve
        "It wasn't like her to lose control of her emotions. It clearly meant something to her."
        scene w2_4759 with dissolve
        fel "Yeah... well, you twisted my arm and dragged it out of me. I don't know why I went into all the detail, but..."
        fel "Guess I just felt like it..."
        scene w2_4760 with dissolve
        fel "..."
    else:

        scene w2_4757 with dissolve
        fel "To cut to the chase - you've met my husband - I'm no longer content."
        scene w2_4735 with dissolve
        fel "I want some connections of my own, independent of Elias. I want to have options."
        fel "Get to know some people and maybe make some money of my own."
        scene w2_4731 with dissolve
        mc "How do you plan on doing that?"
        scene w2_4758 with dissolve
        fel "One rung at a time, [mcf]."
        scene w2_4737 with dissolve
        "That... didn't seem any better to me than her just doing it for kicks."


    scene w2_4729 with dissolve
    mc "So that's the reason you're enduring all this..."
    scene w2_4761 with dissolve
    fel "Oh, c'mon... enduring?"
    fel "That place ain't so bad. I get to spread my wings and have a little fun doing it."
    fel "There's no downside."
    scene w2_4762 with dissolve
    mc "Ha...! Oh, man."
    "If Felicia was any less crazy, I'd be disappointed."
    mc "I'm actually... relieved to hear that."
    scene w2_4763 with dissolve
    fel "Well, now that you know... you must think I'm stupid, right?"
    fel "That I should just be content and happy with where I am? That I'm being greedy?"
    scene w2_4764 with dissolve
    mct "(Hmm...)"
    "Honestly, I didn't know what Felicia expected to gain from rubbing elbows with the club's patrons and I think she didn't quite know either."
    "That place is a viper pit and she was more likely to be bit than to find advantage, but if a woman could do it, it'd be someone like her, right?"
    hide screen textbox2 with dissolve

    menu:
        "She IS being dumb":
            scene w2_4765 with dissolve
            show screen textbox2 with dissolve
            mc "Yeah, since you've asked, it's really fucking stupid Felicia."
            scene w2_4766 with dissolve
            mc "Wanting more is fine, but you've got to know when to stop. I mean, one of the men there last week was the COO of Hoarfrost Risk Management."
            scene w2_4765 with dissolve
            mc "Those guys have done some fucked-up shit in the name of \"security\". You'd think it wise to get on that guy's good side?"
            scene w2_4768 with dissolve
            fel "That's... expected and I agree with you, but..."
            scene w2_4767 with dissolve
            fel "Isn't part of your job to get on that man's good side as well?"
            scene w2_4765 with dissolve
            mc "There's a difference. My job is to basically just stand around."
            scene w2_4767 with dissolve
            fel "So your concern is practical rather than moral?"
            scene w2_4769 with dissolve
            mc "Ah, fuck I don't know."
            scene w2_4767 with dissolve
            fel "Reality bends over strong wills. It belongs to the fearless."
            scene w2_4768 with dissolve
            fel "What good is all my comfort when I can't protect the one thing I really want to protect?"
            scene w2_4766 with dissolve
            mc "...you and Veronica are a lot alike it seems."
            scene w2_4764 with dissolve
            "They both could've just walked away, the only difference is the scale of their ambition."
            scene w2_4770 with dissolve
            fel "Ha! Don't insult me. That bitch is too stupid to match wits with this dumb country slut."
            scene w2_4765 with dissolve
            mc "The bravado doesn't help your case."
        "Caution her, but you believe she can do it"(chg=["felicia_passion_up"]):

            $ Felicia_Confidence += 1
            scene w2_4765 with dissolve
            show screen textbox2 with dissolve
            mc "Since you asked, I do think it's dumb."
            scene w2_4768 with dissolve
            fel "That's... expected and I agree with you, but..."
            scene w2_4765 with dissolve
            mc "I think you can do it though. You're the type of person who knows how to leave an impression. If you somehow win..."
            scene w2_4766 with dissolve
            mc "Well, I just hope it doesn't bite you in the ass. There are some bad people at the club."
            scene w2_4765 with dissolve
            mc "One of the men there last week was the COO of Hoarfrost Risk Management. You're older than me, you should remember them making the news."
            scene w2_4767 with dissolve
            fel "Yeah, and your dear Dr. Chuck built and sold missiles to them. You should also be cautious with who you associate with as well, you know."
            scene w2_4769 with dissolve
            mc "Huh.. I mean..."
            "She wasn't wrong, and she wasn't telling me anything I didn't know, but..."
            "To me, Dr. Chuck was just a guy who liked applied physics and pioneered some rocket tech - all of which had legitimate purpose. Was it his fault if someone misused them?"
            scene w2_4765 with dissolve
            mc "You've done your research."
            scene w2_4767 with dissolve
            fel "I knew a lot of the men in that building that night, and the ones I didn't, I now know."
            scene w2_4766 with dissolve
            mc "Yeah, your plan is dumb, but as I said, if any woman can rub elbows with those fucks, it's you."
            scene w2_4765 with dissolve

            if feliciaAnger == True:
                mc "Good luck, Felicia. Just don't expect any pity."
            else:
                mc "Good luck, Felicia."

    stop music fadeout 3.0
    scene w2_4771 with dissolve
    fel "Now that you know, let's not talk about this ever again."
    scene w2_4772 with dissolve
    fel "Until the month is up, I'm just going to focus on having fun. That's how I'm going to win."
    scene w2_4773 with dissolve
    mc "What's in there?"
    fel "Why we came in the first place, remember?"
    scene w2_4774 with dissolve
    fel "Our mutual friend is getting blitzed tonight."
    hide screen textbox2 with dissolve
    scene black with fade
    "......"
    "..."
    if feliciaFlag == True and w2FeliciaImpressed == True:
        jump w2feliciaFlag
    else:
        $ feliciaFlag = False
        jump w2June11End



label w2feliciaFlag:
    play sound "sound effects/car.wav"
    play music "music/wanderlust.ogg"
    scene w2_4775 with w9
    fel "Hey, [mcf]..."
    mc "Yeah?"
    fel "I just wanted to say... I had fun earlier. Lots of fun."
    "We had traversed the roads leading back to my apartment in peace, until Felicia broke the silence and shared what was on her mind."
    scene w2_4776 with dissolve
    fel "So much so that it got me thinking... you and I are compatible in a {b}very{/b} particular way."
    scene w2_4777 with dissolve
    mc "Do you mean what we did after your husband left?"
    scene w2_4778 with dissolve
    fel "Uh huh. It's called chemistry. For someone as perverted as I am, finding even one person who can meet me halfway in my appetite is uncommon."
    fel "...and you blew past halfway. To put it bluntly, you and I were fucking on the same wavelength tonight."
    mc "If you say so..."
    "I am, it turned out, a horny bastard. I wasn't about to wax poetic about putting pole to hole."
    scene w2_4779 with dissolve
    fel "Don't look at me like that. I really mean it."

    if edwinAnal == True:
        fel "Anyone can screw, but you read me like a book and satisfied a desire of mine. You really surprised the hell out of me."
        scene w2_4780 with dissolve
        mc "What are you talking about?"
        fel "You remembered the details of what I whispered in your ear last week. You used my fantasy against me."
        scene w2_4781 with dissolve
        mc "C'mon, I just did what I wanted."
        scene w2_4782 with dissolve
        fel "Exactly, and you made things more fun for me. That's my definition of compatible."
    else:
        fel "Anyone can screw, but intuition is another matter. There's a momentum to a good fuck and you know when to slow down or plunge ahead."
        fel "With a little practice, you could make something of yourself."
        scene w2_4780 with dissolve
        mc "What are you talking about?"
        fel "I'm just saying, both of us ended up satisfied right? You came buckets and the way I milked you made no secret of how I felt about it."
        scene w2_4781 with dissolve
        mc "A-hem..."
        "For some reason, the ease with which she colorfully described our coupling caught me off guard."
        mc "I... just did what felt good."
        scene w2_4782 with dissolve
        fel "Exactly, that's called intuition and that's what makes us compatible."

    scene w2_4783 with dissolve
    fel "By the way, how old are you again?"
    mc "Twenty-two."
    mc "Why do you ask?"
    fel "Twenty-two... old enough to have a taste for life, but not yet set in your appetite. Easy to mold, like a block of clay..."
    scene w2_4784 with dissolve
    fel "The perfect age... "
    scene w2_4785 with dissolve
    mc "That in no way, shape, or form answered my question."
    scene w2_4784 with dissolve
    fel "Relax, I'm getting there."
    fel "You see, normally these kinds of arrangements aren't done so upfront, but I would like to propose something, stud."
    scene w2_4786 with dissolve
    "She waited for me before she continued."
    scene w2_4785 with dissolve
    mc "I'm listening..."
    scene w2_4784 with dissolve
    fel "There's an art exhibition next Wednesday at a friend's gallery."
    fel "A young artist I know will have one of her paintings on display there that night and I'd like some friendly company."
    scene w2_4787 with dissolve
    mc "That was a lot of buildup to ask me to an art gallery."
    fel "I'm not finished, [mcf]. Before that, I'd like to take you out and buy you some clothes, share a nice meal, and ultimately..."
    fel "I want you to satisfy me as you did tonight."
    scene w2_4786 with dissolve
    "With her cards on the table, Felicia's eyes returned to the road. Yet despite how cool she was playing it, her impatience was readily visible in the glances she stole while awaiting my answer."
    scene w2_4785 with dissolve
    mc "So let me get this straight... you want to make a date so we can screw again?"
    scene w2_4784 with dissolve
    fel "Pssh, as I said, {b}Anyone can screw{/b}. What I want is to confirm our suitability and find out if we're as simpatico as I think we are."
    fel "If I'm happy, this could be a repeat thing. I'll pay you for your time."
    scene w2_4786 with dissolve
    mc "........."
    mc "......"
    mc "Hhuuuuuuuh?"
    scene w2_4787 with dissolve
    mc "You'll pay me... like a...? Like a...?"
    fel "Like a sugar mama."
    fel "Might be fun to put the shoe on the other foot for once."
    scene w2_4788 with dissolve
    mc "Pfft~ha! Oh my God, you're fucking serious? Me?"
    mc "Haaaaa! Me?!"
    scene w2_4789 with dissolve
    fel "Oh, yeah I'm serious and why not? You're young, got a big dick, and I've got the money."
    scene w2_4790 with dissolve
    mc "No offense, but you could pull some buff, big-dicked, and absurdly handsome college student with that offer."
    scene w2_4791 with dissolve
    fel "And they most likely would be a boring lay. Believe it or not, being a sugar baby isn't solely about being attractive."
    scene w2_4790 with dissolve
    mc "That your professional pride talking?"
    scene w2_4789 with dissolve
    fel "What I'm saying is, don't undervalue yourself. We have an established rapport."
    fel "You're in a unique position where you know my past, as well as both of my present selves. Those being Felicia Ford and the horny bitch presently making you this amazing offer."
    scene w2_4792 with dissolve
    mc "Amazing, huh..."
    "It sounded crazy, but Felicia was absurdity personified."
    scene w2_4793 with dissolve
    fel "Think about it: we could have some fun and you can profit. Isn't that a dream come true?"
    scene w2_4787 with dissolve
    mc "What do you mean you'll pay me?"
    fel "You're not familiar with the concept of commerce? Aren't med students supposed to be smart?"
    scene w2_4785 with dissolve
    mc "Just explain it to me like I'm not."
    scene w2_4793 with dissolve
    fel "It's a simple arrangement. I'll give you an allowance and exceeding that, if you ever need anything, you can come to me and we'll figure it out."
    scene w2_4786 with dissolve
    mc "Huh..."

    if felPN == "Daddy":
        scene w2_4784 with dissolve
        fel "And don't worry, I can still call you Daddy if you want."

    scene w2_4794 with dissolve
    "Naturally, as a man, I was considering it. Getting paid to do something that I not only want to do, but am currently more or less already doing would be..."
    "Like she said, a dream. However, the proposition was weird."
    mc "I don't get it. We've already done it without you paying me. You don't think I wouldn't do it for free?"
    scene w2_4795 with dissolve
    fel "There's only a couple weeks left in the competition. If I lose, who knows if I'll ever see you again?"
    scene w2_4796 with dissolve
    fel "If I win... well, it wouldn't be bad to have one of the employees in my pocket, now would it?"
    "She grinned wickedly, ear-to-ear."
    scene w2_4797 with dissolve
    fel "Let me be clear though, I'll have certain expectations of you. You won't ever have to do anything you don't want, but that also means the relationship might not work."
    scene w2_4785 with dissolve
    mc "That's assuming I pass your lil' interview next week?"
    scene w2_4786 with dissolve

    if id_greed == True:
        "How absurd indeed. Deep down, I felt like I should say no."
        "The club paid me extraordinarily well, but then again, not well enough that I didn't have a need for money..."
    else:
        "How absurd indeed. I should say no, what with my college being taken care of and the club already paying me a tidy sum. I didn't want for money, yet..."

    "Another thought crossed my mind: $3,100."
    "That was what Rosalind needed to get her loan shark off her back. Not just that sum either, I should probably assume she won't be able to pay the next two weeks either, which would tack on another two grand to the sum."

    if kat_polite == True:
        "I was going to bring the topic up tomorrow with Mrs. Pulman or maybe Dr. Chuck or August, but..."
    else:
        "I was going to bring the topic up tomorrow with Kathleen or maybe Dr. Chuck or August, but..."

    "Assuming she'd even advance me that sum, taking care of it by dicking down a bombshell would be a more enjoyable approach."
    "Then again, I could just make some money for myself or decline and try to solve Rosalind's problem through the proper channels."

    scene w2_4784 with dissolve
    fel "What do you say? Go with me next week and we'll take it from there?"
    scene w2_4786 with dissolve

    menu:
        "Sure, go on Felicia's date next week.":
            $ feliciaSugarBaby = True
            scene w2_4785 with dissolve
            mc "Sure, why the hell not?"
            scene w2_4798 with dissolve
            fel "Yeah? For real?"
            scene w2_4799 with dissolve
            "It might have been my imagination, but Felicia sounded surprisingly giddy."
            scene w2_4800 with dissolve
            mc "Yeah, let's have some fun. I don't have anything to do Wednesday, and even if it doesn't work out, an evening with you wouldn't be so bad."
            scene w2_4798 with dissolve
            fel "[mcf]... you're not already trying to charm me, are you?"
            scene w2_4785 with dissolve
            mc "Oh no, isn't that how it goes in this type of relationship? Never knowing what's real and what's not?"
            scene w2_4787 with dissolve
            fel "I'll look forward to Wednesday then."
            fel "Just don't flake out, it's an important night for me."
            mc "How so?"
            scene w2_4784 with dissolve
            fel "I... I've had enough of your questions for one day, so I'll tell you about it then."
            play sound "sound effects/notification.wav"
            $ Felicia_Relations = "Potential Sugar Mama"
            show relationfel with dissolve
            "The rest of the way to my apartment continued in a weird flux of trying to find things to say - which was understandable, as having gotten what she wanted, it wasn't like we had much else in common besides sex and the club."
            "It made me wonder why she even wanted to wine and dine me next Wednesday, when we could just skip to the good part..."
        "Bring up Rosalind.":


            $ feliciaSugarBaby = True
            $ rosalindFelSolution = True
            $ rosalindSolution = True
            scene w2_4801 with dissolve
            mc "I know you called it a trial run, but could you advance me some money beforehand?"
            scene w2_4802 with dissolve
            fel "Oh? How much are we talking about?"
            scene w2_4801 with dissolve
            mc "Five thousand dollars."
            scene w2_4802 with dissolve
            fel "That's a good chunk of money for a single evening - not to mention, specific. What do you need it for?"
            scene w2_4801 with dissolve
            mc "Do I have to tell you?"
            scene w2_4802 with dissolve
            fel "Yes, even if you lie."
            scene w2_4803 with dissolve
            mc "Hmm... it's for Rosalind."
            scene w2_4804 with dissolve
            fel "Rosie? You want to give money to that pair of cow tits?"
            scene w2_4803 with dissolve
            mc "She's in debt with a loan shark and he's putting pressure on her. It might affect her performance this month, so it's my job to get it sorted out."
            scene w2_4802 with dissolve
            fel "Sounds like a Kat issue."
            scene w2_4801 with dissolve
            mc "Maybe, but I'm asking you first since you brought up your ridiculous offer. If you don't want to help the competition I understand, we can forget you ever brought this--"
            scene w2_4805 with dissolve
            fel "Text me your bank account number later and you'll have it."
            mc "R-really?"
            "I was actually surprised."
            scene w2_4806 with dissolve
            fel "If that's what it takes to get you to go with me this Wednesday."
            fel "Plus, I don't want to win by throwing a nice woman like Rosie under the bus."
            mct "(...under the bus is exactly where she's going should you win, Felicia.)"
            scene w2_4787 with dissolve
            fel "You'll go with me then?"
            scene w2_4785 with dissolve
            mc "I'll keep my Wednesday open just for you."
            scene w2_4784 with dissolve
            fel "You better, it's an important night for me..."
            scene w2_4785 with dissolve
            mc "How so?"
            scene w2_4784 with dissolve
            fel "I... I've had enough of your questions for one day, so I'll tell you about it then."
            scene w2_4814 with dissolve
            "The rest of the way to my apartment continued in a weird flux of trying to find things to say - which was understandable, as having gotten what she wanted, it wasn't like we had much else in common besides sex and the club."
            play sound "sound effects/notification.wav"
            $ Felicia_Relations = "Potential Sugar Mama"
            show relationfel with dissolve
            "It made me wonder why she even wanted to wine and dine me next Wednesday, when we could just skip to the good part..."
        "Go with her, but tell her you don't want money."(chg=["felicia_passion_up"]):

            $ Felicia_Confidence += 1

            scene w2_4801 with dissolve
            if toughness >= 20:
                mc "I'll go with you, but I don't want your fucking money. Why the hell would you even propose that?"
            else:
                mc "I'll go with you Felicia, but I don't want your money."

            scene w2_4807 with dissolve
            fel "You will...?"
            scene w2_4808 with dissolve
            mc "Believe it or not, despite how crazy you are or maybe even because of it, I like spending time with you - so let's not overcomplicate things."
            mc "...or maybe is that how you simplify things? Do you like me so much that you're afraid I'd say no?"
            "I said it teasingly, but there was a half-baked suspicion in there."
            scene w2_4809 with dissolve
            fel "I... ah-"
            fel "..."
            fel "I like what {i}we{/i} did earlier and find the idea of turning a loser like you into my personal cock-on-demand hot. That's it."
            scene w2_4783 with dissolve
            "The gobsmacked expression on Felicia's face told me I hit the mark. Her offer was predicated on the control and reassurance money buys."
            mc "No, I think you like me and you want a guarantee that I'll say yes. It's very flattering, but your company is payment enough for me."
            fel "Don't be obnoxious."
            "I had to admit, I was letting the idiotic proposal go to my head and who could blame me?"
            scene w2_4810 with dissolve
            fel "Bah. If you're going to do it anyway, why turn the money down? That's just... stupid."
            scene w2_4811 with dissolve
            mc "Maybe, but that's not how I want to do things."
            mc "You talked about chemistry, so let's not ruin it with money, alright?"
            scene w2_4812 with dissolve
            fel "......"
            scene w2_4813 with dissolve
            fel "..."
            scene w2_4793 with dissolve
            fel "Okay, dummy! Just don't cancel on me, okay? It's kinda an important night."
            scene w2_4785 with dissolve
            mc "How so?"
            scene w2_4784 with dissolve
            fel "I... I've had enough of your questions for one day, so I'll tell you about it then."
            scene w2_4814 with dissolve
            "The rest of the way to my apartment continued in a weird flux of trying to find things to say - which was understandable, as having gotten what she wanted, it wasn't like we had much else in common besides sex and the club."
            "It made me wonder why she even wanted to wine and dine me next Wednesday, when we could just skip to the good part..."
        "No, you're not interested."(chg=["felicia_down4"]):


            $ feliciaFlag = False
            $ w2FeliciaAbort = True
            $ Felicia_Affection -= 4
            scene w2_4785 with dissolve
            mc "I like you Felicia, but it's probably best if we limit the time we spend together to Mina or whenever the old lady deigns it."
            mc "Your husband's family may not really be tabloid-worthy anymore, but us spending an exorbitant amount of time together would just be inviting trouble."
            scene w2_4815 with dissolve
            fel "...hmm. You don't really have to worry about, Elias. He has his own affairs and it goes unsaid that I like to play. We have... a practical arrangement."
            fel "I'm not checked up on."
            scene w2_4816 with dissolve
            mc "Even still..."
            scene w2_4815 with dissolve
            fel "Seriously, I mean... ah..."
            scene w2_4817 with dissolve
            fel "I understand. You're probably right, anyway."
            fel "Who knows what the next two and a half weeks have in store? I should focus all my attention on becoming a member, but it would've been nice... for that night to..."
            fel "Yeah, no... I understand."
            scene w2_4814 with dissolve
            "The rest of the way to my apartment continued in a heavy silence. I tried making some idle conversation, and while Felicia tried to make a nominal effort, I knew my rejection had killed the mood."
            "I guess she wasn't used to not getting what she wanted..."

    stop music fadeout 3.0
    scene black with fade
    "......"
    "..."
    scene w2_4818 with dissolve
    fel "This it?"
    mc "Yeah, we're here. Thanks for the ride."

    if w2FeliciaImpressed == True:
        fel "Thanks for the... {i}interesting{/i} evening, stud."
    else:
        fel "It was an unusual evening, to say the least..."

    scene w2_4819 with dissolve
    mc "Yeah, it was... uh, I guess I'll open the door now and go."
    mc "Take care of Mina tonight. Show her a good time and help her take her mind off that video, will you?"
    scene w2_4820 with dissolve
    fel "That you don't have to worry about. I may not be so good at the romantic shit, but when it comes to having fun, our little ray of sunshine is in good hands."
    scene w2_4821 with dissolve
    mc "I guess I'll see you Saturday. Don't forget we're meeting at the diner beforehand, just like last week."
    scene w2_4822 with dissolve
    fel "Yep, see ya Saturday. Who knows what the old woman has cooked up. I get goosebumps just imagining it..."
    scene w2_4823 with dissolve
    mc "Okay, actually going now..."

    if feliciaFlag == True:
        scene w2_4824 with dissolve
        fel "[mcf]?"
        mc "Yeah?"
        scene w2_4825 with dissolve
        "*Chup*"
        scene w2_4826 with dissolve
        fel "I'm looking forward to Wednesday."


    scene black with fade
    play sound "sound effects/car-door-close.wav"
    mc "Drive safe."
    "......"
    "..."


label w2June11End:
    play ambient "sound effects/teeth-brush.wav"
    scene w2_4827 with blinds
    show screen textbox2 with dissolve
    mc "Hmm... mmm... mmggg"
    stop ambient
    scene w2_4828 with dissolve

    if feliciaFlag == True and feliciaSugarBaby == False:
        $ history_felicia = "Felicia ridiculously proposed we enter into a sugar baby relationship. I declined, but agreed to go with her to an art gallery next Wednesday."
        $ unread_felicia = True

    if feliciaFlag == True and feliciaSugarBaby == True and rosalindFelSolution == True:
        $ history_felicia = "Felicia proposed a sugar baby relationship on a trial basis. That sounded like a good deal to me, so I used it as an opportunity to momentarily alleviate Rosalind's loan shark problem. I agreed to go with her to an art gallery next Wednesday."
        $ unread_felicia = True

    if feliciaFlag == True and  feliciaSugarBaby == True and rosalindFelSolution == False:
        $ history_felicia = "Felicia proposed a sugar baby relationship on a trial basis. It was an odd offer, but it sounded like a good deal to me. I agreed to go with her to an art gallery next Wednesday."
        $ unread_felicia = True

    if feliciaFlag == False and w2FeliciaAbort == True:
        $ history_felicia = "Felicia proposed a sugar baby relationship on a trial basis. Not wanting to have anything to do with the married woman outside of work, I declined.."
        $ unread_felicia = True



    play sound "sound effects/notification.wav"
    show bioupdate with dissolve
    "*Ptweh!"
    hana "Hey."
    scene w2_4829 with dissolve
    mc "Oh, hey. We gotta stop meeting like this."
    mc "Did you eat yet? I made some gumbo for dinner and there's plenty left."
    play music "music/modern-situations.ogg"
    scene w2_4830 with dissolve
    hana "I ate with my mom."
    scene w2_4831 with dissolve
    mc "Oh? You guys make up?"
    scene w2_4830 with dissolve
    hana "Yeah, it was more me than her that needed the space. I'll be getting out of your hair tomorrow."
    scene w2_4831 with dissolve
    mc "Well, anytime you need some space again, even without a big dramatic blowup, my doors are open. I've enjoyed having you here."
    scene w2_4832 with dissolve
    hana "Really? You don't mind?"
    scene w2_4831 with dissolve
    mc "Of course, you ARE my new boss after all."
    scene w2_4833 with dissolve
    hana "Christ, will you stop with that already?"
    scene w2_4834 with dissolve
    mc "Aye aye, ma'am."
    scene w2_4835 with dissolve
    hana "Actually, speaking of work... I'm sorry about giving you a hard time earlier."
    hana "You're doing me a favor and what do you get? Some bitch nagging you."
    scene w2_4836 with dissolve
    mc "C'mon, I forgot all about it in the first place, but all you did was say your piece."
    mc "Don't apologize for that. We're friends."
    scene w2_4837 with dissolve
    hana "Ha... not counting Harper or Jacob since they're old as shit, would you believe you're the first \"friend\" I've made since working there? Even outside of the club, it's..."
    hana "That was the last time I had a boyfriend too."
    scene w2_4838 with dissolve
    mc "I get it, but that must suck."
    scene w2_4839 with dissolve
    hana "Not really, I've got my mom, Jerrica, and Spider..."
    scene w2_4838 with dissolve
    mc "If you have to hide a part of your life from them, you can have all the company in the world and it can still feel a little lonely."
    scene w2_4839 with dissolve
    hana "You know that first hand?"
    scene w2_4840 with dissolve
    mc "Not really, more just speaking out of my ass."
    hana "Heh...!"
    mc "So you've all but shut down your social life then?"
    scene w2_4841 with dissolve
    hana "I can't get away from my band or my mom, but how could I start a new relationship with someone and hide where I go on the weekends?"
    hana "I don't like having to hide part of my life from the people I know."
    scene w2_4842 with dissolve
    mc "I hadn't thought about that. It's not hard to keep from my mom since we don't live together, but romance..."

    if kat_polite == True:
        mc "If I did find a girlfriend, with the things Mrs. Pulman has me do, I wouldn't be faithful to her. I'd be no better than Ian."
    else:
        mc "If I did find a girlfriend, with the things Kathleen has me do, I wouldn't be faithful to her. I'd be no better than Ian."

    scene w2_4843 with dissolve
    mc "So I guess that's off the table for me as well."
    scene w2_4844 with dissolve
    mct "(Well, I didn't have any romantic aspirations while I was studying in the first place, so I guess that's not a big deal.)"
    hana "Hmm..."

    if w2HanaSex == True and w2HanaHump == True:
        scene w2_4845 with dissolve
        hana "At least we can be honest with each other."
        mc "Yeah, no need for secrets when we work at the same place."
        scene w2_4844 with dissolve
        hana "..."
        scene w2_4846 with dissolve
        hana "...hey, [mcf]?"
        scene w2_4847 with dissolve
        "Hana suddenly looked concerned."
        mc "Yeah?"
        scene w2_4846 with dissolve
        hana "Actually, if I'm to be honest, about this morning... when we almost..."
        scene w2_4847 with dissolve
        mc "Don't worry about it."
        mc "We can pick that back up some other time, {b}only if you want to{/b}."
        scene w2_4848 with dissolve
        hana "It's just... I didn't want you to think I was using you."
        scene w2_4849 with dissolve
        mc "Using me? Why would I think that?"
        scene w2_4848 with dissolve
        hana "Why? I bitch and moan to you, I take my sexual frustration out by dry humping the shit out of you, and then on top of it all, I'm freeloading in your home..."
        hana "You seriously don't see me taking advantage of you?"
        scene w2_4849 with dissolve
        mc "Nope and quite frankly, I would've been offended if we had sex for that dumbass reason."
        scene w2_4846 with dissolve
        hana "Ah--"
        scene w2_4850 with dissolve
        hana "It's not like I don't want to..."
        scene w2_4851 with dissolve
        mc "I get it. It's about work."
        "Despite the sexual tension, the thing that connected us was also a huge wall for Hana."
        scene w2_4848 with dissolve
        hana "Yeah..."
        scene w2_4849 with dissolve
        mc "Remember what I said. You can crash here any time you want - just... stop overthinking things, you fucking nerd."
        mc "It doesn't fit your image."
        scene w2_4852 with dissolve
        hana "..."
        scene w2_4853 with dissolve
        hana "Thanks, [mcf]."


    elif w2HanaSex == True:
        scene w2_4854 with dissolve
        hana "We do have each other as an option."
        mc "I guess you're right. No need for secrets if we work at the same bloodsucking sex club."
        scene w2_4852 with dissolve
        mc "Although, if I'm not mistaken, you were on the fence about me."
        scene w2_4850 with dissolve
        hana "Hey, I like you, it's just..."
        scene w2_4851 with dissolve
        mc "I get it. It's about work."
        "Despite the sexual tension, the thing that connected us was also a huge wall for Hana."
        scene w2_4848 with dissolve
        hana "Yeah..."
        scene w2_4849 with dissolve
        mc "Remember what I said. You can crash here any time you want."
        scene w2_4853 with dissolve
        hana "Thanks, [mcf]."
    else:


        scene w2_4854 with dissolve
        hana "Push comes to shove, if we still have the same job over the next few years, we do have an option..."
        mc "Oh, you'd settle for moi?"
        hana "At least we wouldn't have secrets."
        scene w2_4855 with dissolve
        mc "Okay then, deal."
        hana "No need for a blood pact. A handshake will do."
        mc "Ha, deal!"


    scene w2_4856 with dissolve
    mc "Now, Hana... not to be a rude host, but I'm tired as balls and you're on my bed."
    hana "O-oh!"
    scene w2_4857 with dissolve
    hana "I should get to bed too. I've got to get up early."
    mc "You have plans?"
    scene w2_4858 with dissolve
    hana "The old bitch wants to see me."
    scene w2_4859 with dissolve
    mc "Twice in one week?"
    scene w2_4858 with dissolve
    hana "I let my dad know my intentions today. It's no doubt about that."
    scene w2_4859 with dissolve

    if kat_polite == True:
        mc "I'll go in with you. I've got some photos to turn in to Mrs. Pulman."
    else:
        mc "I'll go in with you. I've got some photos to turn in to Kathleen."

    if rosalindFelSolution == False:
        mc "Plus, there's an issue with Rosalind I need to talk to her about."

    scene w2_4858 with dissolve
    hana "You need to get your license, you parasite."
    scene w2_4860 with dissolve
    mc "Ha... you figured me out, huh?"
    stop music fadeout 3.0
    hide screen textbox2 with dissolve
    scene black with fade
    "Bedtime."
    "......"
    "..."
    play music "music/doll-dancing.ogg"
    scene w2_4861 with w20
    "For some reason, while trying to get to sleep, Ian was on my mind."
    "It started with me taking account of the day and Mina's troubles, but it grew from there."
    "I thought about how his mother asked me to do the impossible and get him to start taking things seriously and go back to college."
    scene w2_4862 with pixellate
    "I thought about the man he was now, with his good looks and uncle's riches giving him near-unfettered access to life's pleasures."
    scene w2_4863 with dissolve
    "I thought about the timid kid who would spend entire weekends at my house."
    scene w2_4861 with pixellate
    "As unrestrained as he was, he was my friend and deep down I knew I didn't have the moral ground to look down on him."
    "Should I give him a heads up about Mina?"

    menu:
        "Give Ian a call."(chg=["killian_up3"]):
            $ killianHeadsUp = True
            $ Killian_Bromance += 3
            scene w2_4864 with dissolve
            "It wasn't like it would help him come up with an excuse, but it might spare him from being blindsided..."
            play sound "sound effects/ringing-outbound.mp3"
            scene black with fade
            "*Ring, ring*"
            show screen textbox2 with dissolve
            scene w2_4866 with dissolve
            "As to not disturb Hana, I made the call from the bathroom..."
            stop sound
            "*Click*"
            scene w2_4867 with radio
            kil "Hey doc, what's up?"
            scene w2_4868 with dissolve
            "As ever, Killian picked up on the second ring."
            mc "You dumbass, you want to know what you did?"
            scene w2_4869 with dissolve
            kil "That's a pretty open-ended question..."
            scene w2_4870 with dissolve
            mc "Something so careless that I wonder if you did it on purpose."
            scene w2_4871 with dissolve
            kil "Just spit it out, asshole."
            scene w2_4870 with dissolve
            mc "I'll take being a plain ol' asshole over being a reeking, fecal-spewing one. Mina found that thumb drive of yours with one of your trophies on it!"
            scene w2_4872 with dissolve
            kil "Oh, she did...? Which one?"
            mc "Which one...? Which one?!"
            mc "You're just leaving multiple sex tapes lying around to be found?"
            "Ian's reaction to the news of his duplicity being uncovered was disproportionally cool and nonplussed."
            scene w2_4873 with dissolve
            kil "Did Mina tell you she found it?"
            mc "She told Felicia, who then dragged me into it."
            kil "Hmm..."
            mc "Just hmmm? That's it?"
            scene w2_4874 with dissolve
            kil "Well, I always wondered what would be the last straw with her. I've given her enough reasons and she sure as shit put up with a hell of a lot."
            scene w2_4875 with dissolve
            "It was a small relief that he was cognizant of that fact, but it raised several other unpleasant questions."
            scene w2_4874 with dissolve
            kil "For a girl as nice and pretty as her, {b}way{/b} more than she should've. It was almost like a game of how much can I get away with."
            scene w2_4875 with dissolve
            mc "You didn't do it on purpose, did you?"
            scene w2_4876 with dissolve
            kil "Are you asking me did I leave that USB drive on my coffee table hoping that her curiosity would get the better of her and she'd take it home and snoop?"
            scene w2_4875 with dissolve
            mc "Did you?"
            scene w2_4874 with dissolve
            kil "No, I did not. I'm just a dumbass, honest."

            if w2MinaIanCover == True:
                scene w2_4874 with dissolve
                kil "You saw how bad I am at hiding things. You even had to cover for me last week when I snuck in that slut from the club."
                scene w2_4875 with dissolve

            mc "You're not a dumbass, Ian. You just..."
            scene w2_4876 with dissolve
            kil "I'm getting mixed signals here."
            scene w2_4875 with dissolve
            mc "You just don't care."
            scene w2_4874 with dissolve
            kil "Isn't that worse?"
            scene w2_4875 with dissolve
            "We shared in an awkward pause, with me not knowing how to answer with the obvious {b}yes{/b}."
            scene w2_4879 with dissolve
            kil "*Sigh* Ten months..."
            kil "That's more than three times longer than any other relationship of mine. Hell, those others probably don't even fit the definition."
            scene w2_4878 with dissolve
            "As he reminisced, he almost sounded sad."
            mc "She hasn't broken up with you yet."
            scene w2_4877 with dissolve
            kil "No, she hasn't. It's weird that she hasn't blown up at me, right?"
            scene w2_4878 with dissolve
            mc "{b}Very{/b}."

            if minaFlag == True:
                mc "Just so you know, as a heads up, I'm hanging out with her tomorrow."
                kil "..."
                mc "You're cool with that, I hope?"
                scene w2_4879 with dissolve
                kil "It's not like I have any right not to be. Put in a good word for me?"
                scene w2_4878 with dissolve
                mc "Sorry, you made your own bed."
                scene w2_4877 with dissolve
                kil "*Sigh* Seriously, why the hell hasn't she blown up at me yet?"
                scene w2_4878 with dissolve

            mc "I think she's still processing it. You kinda took a big shit in her lap, you know."
            mc "Alice AND another woman... that's a great big dick slap in the face. That's the sort of thing that tanks your view on relationships for the rest of your life."
            scene w2_4880 with dissolve
            kil "Alright, alright jeez... I don't..."
            kil "I don't want to think about that."
            scene w2_4878 with dissolve
            mc "You mean the consequences of your actions?"
            scene w2_4881 with dissolve
            kil "You're having fun rubbing it in, aren't you dickhead?"
            scene w2_4875 with dissolve
            mc "A little, but I'm also curious. Do you feel... {b}bad{/b}?"
            scene w2_4877 with dissolve
            kil "I, uh... I don't know. Uncle Chuck has always told me not to feel bad for doing what I want."
            scene w2_4874 with dissolve
            kil "He says enjoying yourself is all that matters in life. Everything else is radio interference."
            scene w2_4882 with dissolve
            mc "..."
            "For as much of an influence Dr. Chuck has had on my life, Ian was much more significant. In no uncertain terms, he was closer to his uncle than he was to his own father."
            scene w2_4873 with dissolve
            mc "I see... well, I was just calling to give you a heads up."
            kil "I appreciate it, but now it's going to feel like I'm waiting for the knife to drop in slow motion."
            scene w2_4872 with dissolve

            if minaFlag == True:
                kil "Do me a favor..."
                mc "What is it?"
                kil "Whatever you're doing, make sure she has fun tomorrow."
                mc "She ain't going to forget, dude."
                kil "No, I just want her to..."
            else:
                kil "I'd almost prefer not to know."
                mc "Well, consider it penance for your misdeeds."
                kil "Ah, you fucker...!"

            mc "I'm going to go now."
            scene w2_4883 with dissolve
            kil "..."
            scene w2_4884 with dissolve
            kil "Aight, sleep tight doc."
            scene w2_4883 with dissolve
            mc "Bye."
            stop music
            play sound "sound effects/phonemenu.wav"
            "*Click*"
            scene w2_4885 with dissolve
            kil "......"
            scene w2_4886 with dissolve
            kil "..."
            scene w2_4887 with dissolve
            alice "I'm off, but there's some ice tea in the fridge. I made it just how you like it."
            scene w2_4888 with dissolve
            kil "...thanks, Alice."
            scene w2_4889 with dissolve
            alice "Are you feeling alright? You look a little pale."
            kil "Don't go."
            scene w2_4890 with dissolve
            alice "Don't be spoiled."
            scene w2_4891 with dissolve
            alice "It's late and you know I can't stay, Ian."
            scene w2_4892 with dissolve
            kil "You never had it in you to say no to me either..."
            scene w2_4893 with dissolve
            alice "..."
            stop music fadeout 3.0
            scene black with fade
            alice "*sigh* You want a grilled cheese?"
            "......"
            "..."
            jump june12start
        "Don't stick your nose in it.":


            stop music fadeout 3.0
            scene w2_4865 with dissolve
            "No. He made his own bed. It's not my place to rob Mina of the chance of confronting him."
            scene black with fade
            "Putting my friend out of my mind, I turned my thoughts to other things and slowly drifted off to sleep."
            "......"
            "..."
            jump june12start



label june12start:

    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionthegirls01 with blinds
    $ renpy.pause(6, hard=True)
    $ date = "june12day"
    scene w2_4894 with blinds
    show june12day with squares
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    hana "Oh, great..."
    "Hana's exasperated hiss as soon as we breached the central hall was, as far as I could tell, owed to one obvious thing."
    play music "music/i-knew-a-guy.ogg"
    scene w2_4895 with dissolve
    "A slew of scary-looking men were crowding the entrance hall."
    hana "It's not the end of the month. Why are they here?"
    mc "Do I even want to know who \"they\" are?"
    hana "They're.... the old man's \"business\" partners."
    scene w2_4896 with dissolve
    mc "In the club?"
    scene w2_4897 with dissolve
    hana "No. His {i}other{/i} interests."
    scene w2_4896 with dissolve
    mc "Oh."
    scene w2_4898 with dissolve
    "That was all I needed to hear to know that these men were criminals. Preferably, we'd just move past them and go about our business, but that option..."
    scene w2_4899 with dissolve
    aug "Aha, kids! Good morning!"
    "...was plucked off the table for us with a hearty hello."
    hana "*Sigh* Let's go..."
    scene w2_4900 with dissolve
    "As we got closer, one person in the group stood out like a single rose in a field of weeds - a woman with a worn and dejected expression."
    scene w2_4901 with dissolve
    aug "You two get here at the same time?"
    scene w2_4902 with dissolve
    hana "No. We arrived together."
    hana "I've been shacking up at [mcf]'s place for the past five nights."
    "It was as if she was deliberately inviting a misunderstanding..."
    scene w2_4903 with dissolve
    aug "..."
    "Ah, crap..."
    scene w2_4904 with dissolve
    aug "Baha! Good! I had hoped Charles bringing the boy in would get you out of your shell."
    scene w2_4905 with dissolve
    lm "Who's this?"
    scene w2_4906 with dissolve
    aug "Wait, have I really never introduced you to my daughter?"
    hana "I've purposefully avoided meeting you--"
    scene w2_4905 with dissolve
    lm "Your daughter? I didn't know you had a..."
    scene w2_4907 with dissolve
    lm "Ah, now I remember! Brandy's kid! What was that, twenty years ago?"
    hana "Tsk...!"
    "I could tell Hana was about to blow a gasket."
    scene w2_4908 with dissolve
    mc "Mrs. Pulman wanted to see us, we should--."
    scene w2_4909 with dissolve
    lm "That hag can wait, kid."
    lm "I haven't been properly introduced to August's daughter yet."
    scene w2_4910 with dissolve
    aug "Ah, where are my manners? This is Hana!"
    lm "Nice to meet you, Hana. You can call me Otto."
    otto "Your father and I used to work together before he went his own way. I knew your mother as well."
    aug "She was a fun woman, wasn't she? Why--"
    scene w2_4911 with dissolve
    hana "I have no interest in knowing a scumbag like you."
    hana "Let's go, [mcf]."
    stop music
    scene w2_4912 with dissolve
    yg "Watch your mouth, bitch!"
    yg "You--"
    scene w2_4913 with dissolve
    otto "What did you just say?"
    yg "She needs to--!"
    play music "music/hypnosis.ogg"
    scene w2_4914 with dissolve
    otto "What did you just say?"
    yg "I'm s-sorry!"
    otto "Open your mouth."
    scene w2_4915 with dissolve
    "To my astonishment, the man immediately complied."
    otto "Hold out your tongue."
    yg "I'm...!"
    scene w2_4916 with dissolve
    "The man wavered but quickly showed his obedience just as before."
    hana "W-wait a minute!"
    scene w2_4917 with dissolve
    yg "Ng-!"
    aug "Cut him a break, will ya?"
    scene w2_4918 with dissolve
    otto "Even if you ask me to, there's the principle of it. He insulted your daughter."
    scene w2_4917 with dissolve
    aug "I'm ancient history, Otto. {b}You and I{/b} are ancient history."
    scene w2_4919 with dissolve
    otto "..."
    scene w2_4920 with dissolve
    aug "Besides, Hana can be rude and impetuous, just like her mother."
    scene w2_4921 with dissolve
    hana "H-hey, it's nice to meet you as well."
    scene w2_4922 with dissolve
    otto "*Sigh* Go wait outside."
    stop music fadeout 3.0
    scene w2_4923 with fade
    "The man quickly did as he was bid, without any further word. I guess he didn't want to tempt fate."
    aug "See? No need to overreact. All's well that ends well."
    scene w2_4924 with dissolve
    otto "I didn't mean to upset you Hana, but it's just your father is an old friend of mine."
    mct "(An old friend who you didn't even know had a daughter...)"
    otto "Now, don't let me keep you from that rich cunt."
    hana "..."
    scene w2_4925 with dissolve
    hana "C'mon..."
    scene w2_4926 with dissolve
    aug "[mcf]... one thing..."
    aug "Could you see me at the bar after you finish your business with Kathy?"
    mc "Yeah, sure..."
    scene black with fade
    mct "(Please, for all that is good, don't let it be about Hana \"shacking up\" with me...)"
    scene w2_4927 with dissolve
    hana "Holy shit, my heart about jumped out of my chest."
    hana "How are you not freaking out?"
    scene w2_4928 with dissolve
    mc "It happened so fast I guess. I didn't know what to think."
    scene w2_4929 with dissolve
    hana "That REALLY didn't startle you?"
    scene w2_4930 with dissolve
    mc "Who do you think that girl was?"
    scene w2_4931 with dissolve
    hana "The miserable-looking woman dressed like a hooker?"
    scene w2_4930 with dissolve
    mc "Right. Dumb question."

    if kat_polite == True:
        mc "I thought Mrs. Pulman handled that stuff."
    else:
        mc "I thought Kathleen handled that stuff."

    scene w2_4931 with dissolve
    hana "Usually, but not always. Even Ian's perverted uncle has brought in a girl or two since I've been here."
    scene w2_4932 with dissolve
    mc "Huh..."
    mct "(Kathleen had her charity and August was an ex-gangster, but I couldn't fathom Dr. Chuck knowing how to find women who would be willing to work here.)"
    mc "We should go in."
    play sound "sound effects/door-knock.wav"
    scene black with fade
    "*Knock, knock*"
    play sound "sound effects/door-open.wav"
    scene w2_4933 with wipeleft
    mc "Oh! Sorry, are you in the middle of something?"
    kat "Not at all. Abel and I were just killing time while he waits on one of Charles' indulgences."
    abel "How do you do, [mcf]?"
    mc "I'm good, thank you for asking Dr. Van Doren."
    abel "And Miss... do you prefer Miss Rhodes or Miss Byrnes?"
    scene w2_4934 with dissolve
    hana "I'd prefer it if you didn't--"
    scene w2_4935 with dissolve
    hana "..."
    scene w2_4936 with dissolve
    hana "Just Hana is fine."
    scene w2_4937 with dissolve
    kat "You have the photos, [mcf]?"
    scene w2_4938 with dissolve
    mc "Both the raws and the curated picks, plus the notes I took from the interview for you to pass along."
    scene w2_4939 with dissolve
    kat "How lovely. I've been looking forward to seeing how you approached the assignment."
    kat "I hope you appreciate the latitude of freedom you were given on this."
    scene w2_4940 with dissolve
    mc "It was a lot of new experiences, to say the least..."
    scene w2_4941 with dissolve
    kat "Did you have any trouble with the girls?"
    scene w2_4942 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Everything went smooth.":
            show screen textbox2 with dissolve
            mc "Nothing worth mentioning and nothing I couldn't handle."
            scene w2_4943 with dissolve
            kat "Well, then... if you say so and the photos prove to be quality, then I shall be VERY pleased with your performance."
            scene w2_4944 with dissolve
            kat "Very pleased indeed..."
            scene w2_4945 with dissolve
            mc "You won't be disappointed."
        "Tell her Veronica insisted on closing down the gym."(chg=["kathleen_trust_up2","VeronicaShootPoints_down2"]):

            $ w2VeronicaExposed = True
            $ Kathleen_Trust += 2
            $ w2VeroShootPoints -= 2
            show screen textbox2 with dissolve
            mc "Veronica wouldn't do the shoot unless she temporarily shut down the gym. I didn't have a problem with that."
            scene w2_4946 with dissolve
            kat "You didn't? ...but closing it down sucks a lot of the fun out of the whole scenario."
            scene w2_4942 with dissolve
            mc "It was a compromise. You'll be pleased with the shoot regardless."
            scene w2_4946 with dissolve
            kat "You're confident of that?"
            scene w2_4942 with dissolve
            mc "Absolutely sure of it."
            mc "It's uh..."
            mc "You'll see."

    scene w2_4943 with dissolve
    kat "Once I finish speaking with Hana here about her enhanced role in the club, I'll review them."
    scene w2_4946 with dissolve
    kat "Stick around and come back to see me in say... thirty minutes?"
    scene w2_4942 with dissolve

    if minaFlag == True:
        "I had plans with Mina today, but that was in the evening."
    else:
        "I didn't have anything else to do today."
    mc "Sure, that won't be a problem."

    if rosalindSolution == False:
        "Plus, I needed to speak with her about Rosalind's debt."
    mc "I'll be around the building then."
    scene w2_4947 with dissolve
    "With that, I moved to extricate myself from the conversation."
    mc "You made your choice, so keep your head up, okay?"
    scene black with fade
    hana "Thanks, [mcf]."
    "Now, where to? August did ask to speak to me, but I could poke around first."
    jump w2TIHallway





screen w2TINavMenu:
    if w2TINavUnlock == False:
        imagemap:
            idle "gui/screens/imagemaps/w2TINavMenu1_idle.png"
            hover "gui/screens/imagemaps/w2TINavMenu1_hover.png"
            ground "gui/screens/imagemaps/w2TINavMenu1_ground.png"

            hotspot (736,56,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2TIBar")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            if w2TINavUnlock == False:
                hotspot (311,367,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2TISecurityRoomAB")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            else:
                hotspot (311,367,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2TISecurityRoom")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            hotspot (777,367,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2TIHallway")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            hotspot (1237,367,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2TIKatOffice")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            hotspot (10, 22, 180, 180) action [Play("menu_click","sound effects/page-turn.wav"), Return()] hovered [ Play ("hover_extra", "sound effects/click.wav") ]

    else:
        imagemap:
            idle "gui/screens/imagemaps/w2TINavMenu2_idle.png"
            hover "gui/screens/imagemaps/w2TINavMenu2_hover.png"
            ground "gui/screens/imagemaps/w2TINavMenu2_ground.png"

            hotspot (736,56,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2TIBar")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            hotspot (311,367,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2TISecurityRoom")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            hotspot (777,367,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2TIHallway")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            hotspot (1237,367,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2TIKatOffice")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            hotspot (311,668,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2TIDressingRoom")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            hotspot (777,668,460,250) action [Play("menu_click","sound effects/door-open.wav"), Jump("w2TIVIPLounge")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]
            hotspot (10, 22, 180, 180) action [Play("menu_click","sound effects/page-turn.wav"), Return()] hovered [ Play ("hover_extra", "sound effects/click.wav") ]

label w2TINavMenu:
    call screen w2TINavMenu with pixellate

screen w2TIHallway:

    imagemap:

        imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w2TINavMenu")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]

        idle "gui/screens/imagemaps/w2TIHallway_idle.png"
        hover "gui/screens/imagemaps/w2TIHallway_hover.png"
        ground "gui/screens/imagemaps/w2TIHallway_ground.png"

        if w2TITimeBlock == "A":
            hotspot (1400,407,600,600) action Jump("w2TIWarrenDaliaA")
        if w2TITimeBlock == "C" and w2TIHarperCSeen == False:
            hotspot (864,436,500,500) action Jump("w2TIHarperC")



label w2TIHallway:
    show black
    $ renpy.music.play("music/i-knew-a-guy.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w2TIHallway with fade


screen w2TIBar:

    imagemap:

        imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w2TINavMenu")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]

        ground "gui/screens/imagemaps/w2TIBar_ground.png"

        if w2TITimeBlock == "A":
            hover "gui/screens/imagemaps/w2TIBar_hoverA.png"
            idle "gui/screens/imagemaps/w2TIBar_idleA.png"

            hotspot (155, 245,600,600) action Jump("w2TIAugustAB")
            hotspot (702, 242,500,500) action Jump("w2TINicoletteA")


        if w2TITimeBlock == "B" and w2TIDaliaNicoFirst == False and w2TIDaliaNicoSecond == False:
            hover "gui/screens/imagemaps/w2TIBar_hoverA.png"
            idle "gui/screens/imagemaps/w2TIBar_idleA.png"

            if w2TIAugustLeft == False:
                hotspot (155, 245,600,600) action Jump("w2TIAugustAB")
            hotspot (1312, 225,500,500) action Jump("w2TIDaliaNicoB")


        if w2TITimeBlock == "B" and w2TIDaliaNicoFirst == True and w2TIDaliaNicoSecond == False:
            hover "gui/screens/imagemaps/w2TIBar_hoverB1.png"
            idle "gui/screens/imagemaps/w2TIBar_idleB1.png"

            if w2TIAugustLeft == False:
                hotspot (155, 245,600,600) action Jump("w2TIAugustAB")
            hotspot (1312, 225,500,500) action Jump("w2TIDaliaNicoB")

        if w2TITimeBlock == "B" and w2TIDaliaNicoFirst == True and w2TIDaliaNicoSecond == True:
            hover "gui/screens/imagemaps/w2TIBar_hoverB2.png"
            idle "gui/screens/imagemaps/w2TIBar_idleB2.png"

            if w2TIAugustLeft == False:
                hotspot (155, 245,600,600) action Jump("w2TIAugustAB")
            if w2TIDaliaNicoLeft == False:
                hotspot (1312, 225,500,500) action Jump("w2TIDaliaNicoB")






label w2TIBar:
    show black
    $ renpy.music.play("music/jazz-apricot.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w2TIBar with fade


screen w2TISecurityRoom:

    imagemap:

        imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w2TINavMenu")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]

        idle "gui/screens/imagemaps/w2TISecurityRoom_ground.png"
        hover "gui/screens/imagemaps/w2TISecurityRoom_ground.png"
        ground "gui/screens/imagemaps/w2TISecurityRoom_ground.png"


label w2TISecurityRoom:

    show black
    $ renpy.music.play("music/sneaky-snitch.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w2TISecurityRoom with fade



label w2TIKatOffice:

    show black
    if kat_polite == True:
        "It's still too early to meet with Mrs. Pulman. I should come back later."
    else:
        "It's still too early to meet with Kathleen. I should come back later."
    $ renpy.music.play("music/jazz-apricot.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w2TIHallway with fade

screen w2TIDressingRoom:

    imagemap:

        imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w2TINavMenu")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]

        if w2DressingRoomFinished == False:
            idle "gui/screens/imagemaps/w2TIDressingRoom_idle.png"
            hover "gui/screens/imagemaps/w2TIDressingRoom_hover.png"
            ground "gui/screens/imagemaps/w2TIDressingRoom_ground.png"
            hotspot (598, 200,800,800) action Jump("w2TIDressingRoomAB")
        else:
            idle "gui/screens/imagemaps/w2TIDressingRoom2_ground.png"
            hover "gui/screens/imagemaps/w2TIDressingRoom2_ground.png"
            ground "gui/screens/imagemaps/w2TIDressingRoom2_ground.png"


label w2TIDressingRoom:

    show black
    $ renpy.music.play("music/as-i-figure.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w2TIDressingRoom with fade

screen w2TIVIPLounge:

    imagemap:

        imagebutton auto "gui/screens/imagebuttons/travel_%s.png" action [Play("menu_click","sound effects/page-turn.wav"), Jump("w2TINavMenu")] hovered [ Play ("hover_extra", "sound effects/click.wav") ]

        if w2TITimeBlock == "A":
            idle "gui/screens/imagemaps/w2TIVIPLounge_ground.png"
            hover "gui/screens/imagemaps/w2TIVIPLounge_ground.png"
            ground "gui/screens/imagemaps/w2TIVIPLounge_ground.png"

        if w2TITimeBlock == "B":
            idle "gui/screens/imagemaps/w2TIVIPLounge_idle.png"
            hover "gui/screens/imagemaps/w2TIVIPLounge_hover.png"
            ground "gui/screens/imagemaps/w2TIVIPLounge_ground.png"
            hotspot (752, 393,250,250) action Jump("w2TINurse")

        if w2TITimeBlock == "C":
            idle "gui/screens/imagemaps/w2TIVIPLounge_idle.png"
            hover "gui/screens/imagemaps/w2TIVIPLounge_hover.png"
            ground "gui/screens/imagemaps/w2TIVIPLounge_ground.png"
            hotspot (752, 393,600,300) action Jump("w2TIChessGame")
            hotspot (312, 624,600,600) action Jump("w2TIAbel")


label w2TIVIPLounge:

    show black
    $ renpy.music.play("music/jazz-piano-bar.ogg", loop=True, fadeout=1.0, fadein=1.0, if_changed=True)
    call screen w2TIVIPLounge with fade


label w2TIWarrenDaliaA:

    if w2TIWarrenDaliaRepeat == False:
        $ w2TIWarrenDaliaRepeat = True
        scene w2_4948 with dissolve
        "I spotted an unusual pair, made even more peculiar by the animated conversation they appeared to be having."
        scene w2_4949 with dissolve
        dal "...all I'm asking is that you have more consideration for the girls. {b}Please{/b}."
        scene w2_4950 with dissolve
        war "I don't know what the fuck you're talking about, Dal."
        scene w2_4951 with dissolve
        dal "You...! I don't care about the free service you coax out of the girls, but the moment it starts to hurt their earnings is when you and I have a problem."
        scene w2_4952 with dissolve
        war "...is that so?"
        scene w2_4953 with dissolve
        dal "{b}That's so{/b}. Emma couldn't work for a whole day after the state you left her in."
        scene w2_4954 with dissolve
        war "I guess my dick's just that good, but I fail to see how that's my problem."
        scene w2_4955 with dissolve
        dal "..."
        scene w2_4956 with dissolve
        dal "Don't forget you're just dumb muscle. We may just be whores, but you're just as much an easily replaceable commodity."
        scene w2_4957 with dissolve
        war "Is that a threat, Dal?"
        scene w2_4956 with dissolve
        dal "No, just a heads up. Mrs. Pulman may find your brutality amusing, but this is a business and August treats it as one."
        scene w2_4955 with dissolve
        war "......"
        dal "..."
    else:

        scene w2_4958 with dissolve
        war "Sheesh, shesh, alright. You sure can be scary when you want."
        war "I'll ask about their schedules first next time."

    jump w2TIHallway


label w2TIHarperC:
    $ w2TIHarperCSeen = True
    scene w2_4959 with dissolve
    mc "Heading home?"
    scene w2_4960 with dissolve
    harp "Yeah, my Friday morning regular canceled, which means my mom gets a break from watching my kid."
    scene w2_4959 with dissolve
    mc "Win-win."
    scene w2_4960 with dissolve
    harp "Why do you ask?"

    if w2HarpRainCheck == True:
        $ harperOption = True
        scene w2_4961 with dissolve
        harp "You want that... {b}rain check{/b} from your birthday?"
        scene w2_4962 with dissolve
        mc "Ah..."

        if kat_polite == True:
            "She was talking about the night I turned down Mrs. Pulman's sadistic gift."
        else:
            "She was talking about the night I turned down Kathleen's sadistic gift."

        scene w2_4963 with dissolve
        mc "No, just saying hello, I guess."
        scene w2_4961 with dissolve
        harp "Well, anytime you want to go, give me a call."
        scene w2_4963 with dissolve

        if toughness >= 20:
            mc "I might do that sometime."
            scene w2_4961 with dissolve
            harp "Sure, we could even pretend it's still your birthday if you want."
        else:
            mc "I wouldn't want to take advantage."
            scene w2_4961 with dissolve
            harp "Don't worry, you wouldn't be the first."

        scene w2_4964 with dissolve
        harp "See you around!"
    else:
        scene w2_4959 with dissolve
        mc "Just saying hello, I guess."
        scene w2_4964 with dissolve
        harp "Well, then. Hello and goodbye, Mr. [mcl]."

    mc "Take care."
    jump w2TIHallway



label w2TINicoletteA:

    if w2TINicoletteRepeat == False:
        $ w2TINicoletteRepeat = True
        scene w2_4965 with dissolve
        mc "You're new, right? I'm [mcf]."
        scene w2_4966 with dissolve
        woman "..."
        scene w2_4967 with dissolve
        woman "Hello, [mcf]..."
        scene w2_4965 with dissolve
        mc "What's your name?"
        scene w2_4968 with dissolve
        nico "Nicolette."
        scene w2_4965 with dissolve
        mc "You're a new house girl, Nicolette?"
        scene w2_4968 with dissolve
        nico "That's what they tell me."
        scene w2_4965 with dissolve
        mc "They? Those men you were with?"
        scene w2_4968 with dissolve
        nico "I don't really feel like playing twenty questions, hun."
        scene w2_4966 with dissolve
        "She looked very sad. The other girls here had a certain resolve or otherwise just hid it well, but I could tell..."
        scene w2_4969 with dissolve
        nico "Who are you exactly, [mcf]?"
        "She was on edge."
        scene w2_4970 with dissolve
        mc "I help with things around here."
        scene w2_4969 with dissolve
        nico "Does that mean you tell me what to do, Mr. Helper?"
        scene w2_4970 with dissolve
        mc "No."
        scene w2_4967 with dissolve
        nico "Then you wouldn't mind letting me sit here in peace for a bit, would ya? Please."
        scene w2_4971 with dissolve
        mc "Right, yeah... sorry to bother you."
    else:
        scene w2_4972 with dissolve
        "I should leave Nicolette alone for the time being. She's dealing with some shit."
    jump w2TIBar


label w2TIAugustAB:

    if w2TIAugustRepeat == False:
        if w2TITimeBlock == "A":
            $ w2TITimeBlock = "B"
        else:
            $ w2TITimeBlock = "C"

        $ w2TIAugustLeft = True

        scene w2_4973 with dissolve
        mc "You wanted to see me, boss?"
        aug "Sit down and take a load off, kid."


        if w2TITimeBlock == "B":

            if w2TINicoletteRepeat == True:
                scene w2_4976 with dissolve
                aug "I see you met Nico."
                scene w2_4975 with dissolve
                mc "We spoke briefly."
                mc "She seems... really nervous."
            else:
                scene w2_4975 with dissolve
                mc "Who's that?"
                scene w2_4976 with dissolve
                aug "The new girl, Nicolette."
                scene w2_4975 with dissolve
                mc "She seems... really nervous."

            scene w2_4980 with dissolve
            aug "Naturally. It's a tough gig. It can take a little while to get acclimated."
            aug "Especially for a \"special interest\" like her."
            scene w2_4979 with dissolve
            mc "What does that mean?"
            scene w2_4981 with dissolve
            aug "It means... she's got a colorful future ahead."
            scene w2_4979 with dissolve
            "That in no way provided a clearer picture, but I took it that ambiguity was for Nicolette's benefit, given she was within earshot."
            mc "I see..."

        if w2TITimeBlock == "C":
            scene w2_4974 with dissolve
            mc "What's going on there?"

            if w2TINicoletteRepeat == False:
                scene w2_4977 with dissolve
                aug "Dalia's just getting a sense of what's what with the new girl."
                mc "Who is the new girl?"
                aug "Her name's Nicolette. Beautiful isn't she?"
                mc "Every woman here is."
                aug "That they are."

            if w2TINicoletteRepeat == True and w2TIDaliaNicoFirst == False and w2TIDaliaNicoSecond == False:
                scene w2_4978 with dissolve
                aug "Dalia's just getting a sense of what's what with the new girl."
                mc "She came with your friends?"
                aug "Uh huh. Call it a consignment of sorts. She's here to make money fast."
            if w2TINicoletteRepeat == True and w2TIDaliaNicoFirst == True and w2TIDaliaNicoSecond == False:
                scene w2_5010 with dissolve
                aug "Dalia's just getting a sense of what's what with the new girl."
                mc "She came with your friends?"
                aug "Uh huh. Call it a consignment of sorts. She's here to make money fast."
            if w2TINicoletteRepeat == True and w2TIDaliaNicoFirst == True and w2TIDaliaNicoSecond == True:
                scene w2_5017 with dissolve
                mc "She came with your friends?"
                aug "Uh huh. Call it a consignment of sorts. She's here to make money fast."
            scene w2_4979 with dissolve
            mc "Against her will?"
            scene w2_4981 with dissolve
            aug "It's more of a... gray area."
            scene w2_4979 with dissolve
            "I didn't really like how that sounded."


        scene w2_4980 with dissolve
        aug "So, you've been on the payroll for about a month now."
        scene w2_4979 with dissolve
        "August saw fit for a change of topics."
        mc "A whole month already, huh..."
        "Such a short time, but so much has been packed into it."
        scene w2_4980 with dissolve
        aug "Enjoying your time here?"
        scene w2_4979 with dissolve
        hide screen textbox2 with dissolve

        menu:
            "Yes. Very much so.":
                show screen textbox2 with dissolve
                mc "How could I not be?"
                scene w2_4981 with dissolve
                aug "Heh. The day we met, you were so adamant about not wanting anything to do with this place. Quite the change of tune."
                scene w2_4979 with dissolve
                mc "I'm a man after all. This is a persuasive environment."
                scene w2_4980 with dissolve
                aug "That. It. Is."
            "You try to think of it as work."(chg=["august_up"]):

                $ August_Friendship +=1
                show screen textbox2 with dissolve
                mc "I try to think of it as work, although that can be a little difficult given my duties. You know what I mean?"
                scene w2_4980 with dissolve
                aug "I certainly do. Mixing business with pleasure is inevitable with this work, but it's like taking a shit at work. Necessary and enjoyable, but you're doing it on company time."
                scene w2_4979 with dissolve
                mc "That's a gross way of putting it."
                scene w2_4982 with dissolve
                aug "I'm glad you're being mindful of the difference."
                scene w2_4980 with dissolve

        aug "On the topic of enjoying your time..."
        aug "You and my daughter seem to be close."
        scene w2_4979 with dissolve
        mc "...is that why you wanted to speak?"
        scene w2_4981 with dissolve
        aug "Relax, it's not a problem. Just an observation."
        aug "I haven't earned the right to have a say in my daughter's life."
        scene w2_4979 with dissolve
        mc "Yet she's working here with some pretty big strings attached, isn't she?"
        scene w2_4985 with dissolve
        aug "...you're getting pretty fuckin' cheeky, kid."
        scene w2_4984 with dissolve
        mc "You're the one who brought up the subject, all I'm doing is being honest."
        scene w2_4986 with dissolve
        aug "Maha! You've got some balls, [mcf]! You're right!"
        scene w2_4985 with dissolve
        aug "I'm not a good man to begin with and helping her mother was an act of a desperate father. One that I regret, but would do again and again if I had to."
        scene w2_4983 with dissolve
        mc "Maybe I'll understand one day."
        scene w2_4981 with dissolve
        aug "I'm just glad she seems to be coming around. I was shocked when she accepted her share of the business out of the blue, but now I understand I have Kathy to thank for appealing to her pragmatic side."
        scene w2_4980 with dissolve
        aug "Still, it's a start."
        scene w2_4983 with dissolve
        mc "Do you make a habit of spilling your guts to college students?"
        scene w2_4986 with dissolve
        aug "Baha, no! No, I don't, but I wanted to speak with you honestly today and get a better sense of who you are."
        scene w2_4983 with dissolve
        mc "Why?"
        scene w2_4982 with dissolve
        aug "You and my daughter seem to be close."
        scene w2_4983 with dissolve
        mc "It's more like--"

        if w2TITimeBlock == "B":
            scene w2_4987 with dissolve
            "Having finished her dressing down of Warren, the click of Dalia's heels signaled her approach toward the bar."
            scene w2_4988 with dissolve
            dal "I'm Dalia. I'm here to help you, but I'm not your friend."
            dal "You'll go through me for anything you need."
            scene w2_4989 with dissolve
            nico "It's gonna be like that, huh?"
            scene w2_4990 with dissolve
            dal "Let's go over there. I want to get a look at you."
            scene w2_4991 with dissolve
            mc "Ah, where were we?"


        if w2TITimeBlock == "C":
            scene w2_4992 with dissolve
            nico "Wait, what about my clothes? L-let me get dressed first!"
            dal "You don't need them. Just follow me, dear."
            scene w2_4993 with dissolve
            nico "..."
            scene w2_4994 with dissolve
            nico "Ack, whatever...!"
            scene w2_4995 with dissolve
            mc "Is she fucking with her?"
            scene w2_4996 with dissolve
            aug "Dalia? No, she's not the type."
            aug "I'd be surprised if she derived any fun from our business."
            scene w2_4995 with dissolve
            mc "...huh. So where were we?"


        scene w2_4998 with dissolve
        aug "I was about to pour us each a glass of the finest single malt you'll ever taste."
        scene w2_4997 with dissolve
        mc "...sure, please do."
        scene w2_4998 with dissolve
        aug "Like you ever had a choice in the matter."
        scene black with fade
        "All the while, we carried on a seemingly inconsequential conversation."
        "It was nothing resembling personal, but he spoke candidly about sports and other mundane matters. Considering the scene from earlier, the banality of our conversation felt uncanny. "
        scene w2_4999 with fade
        aug "Thanks for indulging me, [mcf]."
        mc "Boss says \"drink\" you drink."
        aug "That. You. Do."

        if rosalindSolution == False:
            scene w2_5000 with dissolve
            mct "(Hmm...)"
            "While I was planning to raise the issue with the old woman, since we're being so friendly, I could ask August about alleviating Rosalind's problem with the loan shark."
            "It's as much in his interest as it is hers, so to speak."
            hide screen textbox2 with dissolve

            menu:
                "Tell him about the problem.":
                    scene w2_5001 with dissolve
                    show screen textbox2 with dissolve
                    mc "One of the Carnations needs some cash or else she might not be able to perform."
                    "I decided to be AS direct as possible."
                    mc "I figured I should bring it up to you, boss."
                    scene w2_5002 with dissolve
                    aug "Oh, yeah? Well..."

                    if August_Friendship >= 6:
                        $ rosalindSolution = True
                        $ rosalindAugSolution = True
                        scene w2_5004 with dissolve
                        aug "Normally I'd let Kathy take care of that side of things, but tell me about it."
                        scene w2_5001 with dissolve
                        mc "Rosalind's got a loan shark hassling her. She needs to pay back her interest or else it sounds like he's gonna lean more heavily on her."
                        mc "She needs about five tho--"
                        scene w2_5003 with dissolve
                        aug "Say no more. Do you have the name of the outfit?"
                        scene w2_5001 with dissolve
                        mc "Just Oliver."
                        scene w2_5002 with dissolve
                        aug "It might take a few days to find \"Just Oliver\", but she'll be square for the next few weeks."
                        scene w2_5003 with dissolve
                        aug "Let Rosalind know she doesn't have anything to worry about."
                        scene w2_5001 with dissolve
                        mc "You're going to pay?"
                        scene w2_5005 with dissolve
                        aug "No, not at all. I'm just going to politely ask whoever it is for some professional courtesy."
                        scene w2_5001 with dissolve
                        mc "You sure he'll agree to that?"
                        scene w2_5005 with dissolve
                        aug "I'm {b}very{/b} sure."
                        "I didn't care to ask anything further, I just knew the issue would be taken care of."
                        scene w2_5001 with dissolve
                        mc "Thanks, Mr. Byrnes."
                        scene w2_5004 with dissolve
                        aug "We're in this ugly business together, right?"
                        scene black with fade
                        "Right. We're in this together."
                        "After a few more minutes of talking, August left for other business."
                    else:

                        scene w2_5003 with dissolve
                        aug "I prefer to let Kathy take care of that side of things. The exhibition is her pride and joy."
                        scene w2_5002 with dissolve
                        aug "I don't want to hear it from her if I step on her toes."
                        scene w2_5001 with dissolve
                        mc "Yeah, I figured that might be the case. Just thought I'd ask."
                        scene w2_5005 with dissolve
                        aug "She'll get whoever's problem taken care of, one way or another. She won't let anything impede her fun."
                        scene black with fade
                        "After a few more minutes of talking, August left for other business."
                "You'd rather get someone else's help.":



                    show screen textbox2 with dissolve

                    if w2TITimeBlock == "C":
                        "Nah. I'll bring it up to Mrs. Pulman."
                    else:
                        "Nah. I'll bring it up to either Mrs. Pulman or Dr. Chuck."

                    scene w2_5002 with dissolve
                    aug "Would you like another glass?"
                    scene w2_5001 with dissolve
                    mc "No. It's too early for that."
                    scene black with fade
                    "After a few more minutes of talking, August left for other business."
        else:


            scene black with fade
            "After a few more minutes of talking, August left for other business."

        jump w2TIBar


label w2TIDaliaNicoB:

    if w2TIDaliaNicoFirst == False and w2TIDaliaNicoSecond == False:
        $ w2TIDaliaNicoFirst = True
        scene w2_5006 with dissolve
        nico "Right here? Right now? In the middle of the bar?"
        scene w2_5007 with dissolve
        dal "It's not like it's a public space."
        scene w2_5008 with dissolve

        if w2TIAugustLeft == True:
            dal "Plus, the only person here besides me is..."
        else:
            dal "Plus, there's just Mr. Byrnes and..."

        scene w2_5009 with dissolve
        dal "Mr. [mcl], anyway. You don't have a problem with getting undressed in front of strangers, right?"
        "I gave Dalia a friendly wave back."
        scene w2_5006 with dissolve
        nico "No, of course not."
        scene w2_5007 with dissolve
        dal "Then hop to it. I need to give you the rundown of the place since you'll be diving into the deep end soon."
        jump w2TIBar

    if w2TIDaliaNicoFirst == True and w2TIDaliaNicoSecond == False:
        $ w2TIDaliaNicoSecond = True
        scene w2_5010 with dissolve
        dal "Good body. Ass could be a little fatter, but you've got a great pair of breasts."
        dal "The tattoo will make you popular with a few of our clients."
        scene w2_5011 with dissolve
        dal "Mr. Garcia in particular will take a shine to you if I present you right. Harp will be happy to share that burden."
        nico "Alright..."
        scene w2_5012 with dissolve
        dal "Open your mouth."
        scene w2_5013 with dissolve
        "With a sigh to belabor the humiliation, Nicolette did as the head girl asked."
        dal "Good, you've got nice teeth. Mr. Bianchi is particular about that."
        dal "Won't touch a girl without a set of pearly whites."
        scene w2_5014 with dissolve
        dal "He'll like this too."
        nico "Don't they all?"
        dal "Oh, hun... men ARE men, but the men you'll be serving are more... particular than what you may be used to."
        scene w2_5015 with dissolve
        dal "Which brings me to my next question: you said you wanted to expedite your time here?"
        nico "The quicker, the better."
        scene w2_5016 with dissolve
        dal "Do you know what that means?"
        scene w2_5017 with dissolve
        nico "The man with the goatee explained it to me already."
        scene w2_5016 with dissolve
        dal "Personally, I think you should take it slow, but if that's what you want..."
        dal "I'll have some questions."
        jump w2TIBar

    if w2TIDaliaNicoFirst == True and w2TIDaliaNicoSecond == True:
        if w2TIAugustLeft == True:
            $ w2TIDaliaNicoLeft = True
            scene w2_5018 with dissolve
            "Dalia and Nicolette talked for a while, before the older woman began walking off."
            scene w2_5019 with dissolve
            nico "Wait, what about my clothes? L-let me get dressed first!"
            dal "You don't need them. Just follow me, dear."
            scene w2_5020 with dissolve
            nico "..."
            scene w2_5021 with dissolve
            nico "Ack, whatever...!"
        else:
            scene w2_5018 with dissolve
            "Dalia and Nicolette are still talking. I shouldn't just stand around gawking at them for any longer."
        jump w2TIBar



label w2TISecurityRoomAB:
    $ w2TINavUnlock = True
    stop music fadeout 3.0
    scene black with fade
    "I have no clue where Dr. Chuck is, but if I want to find him, that could be easily remedied."
    play sound "sound effects/door-knock.wav"
    "*Knock, knock*"
    mc "Anyone there?"
    mct "(I saw Warren in the central area, so I doubt anyone's...)"
    play sound "sound effects/door-open.wav"
    play music "music/sneaky-snitch.ogg"
    scene w2_5022 with dissolve
    mct "(Aha, it's not locked!)"
    scene w2_5023 with fade
    "The quickest way to find anyone within this labyrinth of rooms would be to check the camera feeds."
    "I was certain it was okay for me to be in here alone, but I still couldn't escape the nagging feeling that I was snooping."
    scene w2_5024 with dissolve
    mct "(The best view in the house, huh?)"
    mct "(Now, let us see...)"
    scene w2_5025 with pixellate
    "Slowly, I began making my way through the feed, one empty bedroom at a time."
    scene w2_5029 with dissolve
    mct "(Of course, if he's somewhere that doesn't have a security camera, this will just be a waste of time...)"

    if w2TITimeBlock == "A":
        if w2TIWarrenDaliaRepeat == True:
            scene w2_5027 with dissolve
            "It seems Dalia and Warren are where I left them."
            mct "(Looks like they've calmed down some, at least.)"
        else:
            scene w2_5028 with dissolve
            "Dalia and Warren are still where I last saw them, in the middle of an enthusiastic conversation."
            "His patience looks like it's wearing thin."

        scene w2_5026 with dissolve
        mct "(Nothing here...)"
        scene w2_5030 with dissolve
        "Looks like it's just Hana and the old woman left in her office now."
        mct "(Meaning there's no referee to get between them...)"
        scene w2_5031 with dissolve
        mct "(There's Jacob, enjoying a soak all alone.)"
        "Do he and Warren ever go home? It's like they're both always here..."
        scene w2_5032 with dissolve
        mct "(No Chuck in the lounge either...)"
        scene w2_5033 with dissolve
        mc "Ah! There he is!"
        mct "(And Ian too!)"
        "...wait."
        mct "(What the hell are those two doing?)"
        "A woman was spread out on all fours between them, ass raised in the air as the two casually conversed. What's more, this bizarre sight was taking place in the middle of the..."
        scene w2_5024 with dissolve
        "Well, if I want to check in and kill time with Dr. Chuck, I guess the women's dressing room is the destination."
        mct "(Plus, I kind of want to go see what's up.)"
        scene black with fade
        mct "(Nothing should really surprise me anymore, but it did pique my curiosity.)"


    if w2TITimeBlock == "B":
        scene w2_5034 with dissolve
        "Looks like Warren wandered off after finishing his argument with Dalia."
        scene w2_5026 with dissolve
        mct "(This room is also empty...)"
        scene w2_5035 with dissolve
        "Nothing outside of Kat's office either, of course."
        scene w2_5036 with dissolve
        mc "Huh..."
        "The first sign of life I found was of Jacob, soaking in the sauna, comfortably availing himself to a house girl's lap."
        "Even from the camera's distance, the sight seemed uncharacteristically tender and sweet for this building's walls, with the woman's hand gently rubbing the muscular man's bald head."
        mct "(I wonder if he or Warren ever go home?)"
        scene w2_5037 with dissolve
        mct "(Is that Van Doren's nurse? What's she doing alone in the lounge?)"
        "There she was, with what appeared to be a chessboard set up on the table in front of her, absent her charge. It was the first time I'd ever seen her leave his side."
        scene w2_5038 with dissolve
        mc "There, finally! And Ian too!"
        "...wait."
        mct "(What the hell are those two doing?)"
        "A woman was spread out on all fours between them, ass hiked in the air as the two casually conversed. What's more, this bizarre sight was in the middle of the..."
        scene w2_5024 with dissolve
        "Well, if I want to check in and kill time with Dr. Chuck, I guess the women's dressing room is the destination."
        mct "(Plus, I kind of want to go see what's up.)"
        "I just want to check one more thing..."
        scene w2_5056 with dissolve
        "I quickly rotated through the rest of the feeds, in search of Dr. Van Doren."
        scene w2_5039 with dissolve
        "I found him, alongside Warren, in a cold spartan part of the building I had never laid eyes on."
        scene w2_5040 with dissolve
        "The two seemed to be calmly exchanging words."
        scene w2_5041 with dissolve
        mct "(I wish I could make out what they are saying...)"
        scene w2_5042 with dissolve
        "Eventually, the two moved into another room, escaping the camera's frame and try as I might..."
        scene w2_5029 with dissolve
        "It seemed wherever they had gone, was outside the eye of the building's security system."
        scene w2_5024 with dissolve
        mct "(Hmm...)"
        "Not every corner of the building being watched wasn't all that a big surprise, but what were they doing in there?"
        mc "Odd..."
        scene black with fade
        "Pushing what I saw to the back of my mind, I left the security room."

        if w2TIAugustRepeat == True:
            "I still had to visit August and I could drop in on Dr. Chuck while I was at it. I had time to kill."
        else:
            mct "(Let's go see what Dr. Chuck is up to.)"

    jump w2TIHallway



label w2TIDressingRoomAB:

    if w2TITimeBlock == "A":
        $ w2TITimeBlock = "B"
    else:
        $ w2TITimeBlock = "C"
    $ w2DressingRoomFinished = True

    "Save for a quick glance and friendly wave from Dr. Chuck, my entrance into the room went unnoticed, its occupants' attention captured by the game being played at the center of the room."
    scene w2_5044 with dissolve
    mc "What's, uh... what's going on here, fellas?"
    scene w2_5043 with dissolve
    kil "......"
    kil "..."
    scene w2_5045 with dissolve
    chuck "How do you do, lad?"
    scene w2_5046 with dissolve
    mc "I'm good, Dr. Chuck. What are you two doing in here?"
    "With everyone acting so casual right now, lest I look like a bumpkin, I didn't draw direct attention to the woman being used as a game board."
    chuck "Just Ian and myself's weekly game of Go. I don't have an office in the building, so we usually just play in here."
    scene w2_5047 with dissolve
    chuck "Best view in the building, am I right?"
    scene w2_5048 with dissolve
    mc "You've certainly got some lovely company, yes."
    scene w2_5049 with dissolve
    "As absurd as this situation was, I couldn't argue against the erotic appeal. The woman between them was beautiful and remained as still as a statue, her generously proportioned ass hiked high in the air for the men's convenience."
    "Even if it was a disgusting display of power, the everyday casualness in which they objectified this woman tickled something deep and depraved in me."
    scene w2_5050 with dissolve
    chuck "Do you know how to play?"
    scene w2_5049 with dissolve
    mc "Not at all, I'm afraid."
    scene w2_5051 with dissolve
    chuck "It's a lovely game. The oldest board game still played today actually, going back more than two thousand years."
    chuck "I taught Ian when he was very young, but it's only in the last few years that we've started playing regularly."
    scene w2_5052 with dissolve
    kil "Your go--"
    scene w2_5053 with dissolve
    chuck "Would you like to learn? I'm always looking for more people to play with."
    scene w2_5054 with dissolve
    kil "..."
    mc "No thank you, I believe you've got a perfectly satisfactory punching bag right there."
    scene w2_5055 with dissolve
    kil "You can say that again. I've never won once against this old bastard, yet he won't let me quit."
    scene w2_5057 with dissolve
    chuck "You can quit once you're no longer able to improve. Even if it takes twenty years, if you continue to get better and if you can just beat me once, then our time playing will have been worth it."
    scene w2_5058 with dissolve
    kil "For you, maybe..."
    scene w2_5059 with dissolve
    chuck "Did you need anything, lad?"
    scene w2_5060 with dissolve

    if kat_polite == True:
        mc "No, I'm just killing time waiting for Mrs. Pulman to finish with Hana."
    else:
        mc "No, I'm just killing time waiting for Kathleen to finish with Hana."

    scene w2_5061 with dissolve
    kil "Eh? They usually avoid each other like the plague. What does Kat want with her?"
    chuck "Worming her way into the young lass' life, I reckon. She IS going to own a part of this place very soon."
    kil "Wait, {b}what{/b}?!"
    scene w2_5062 with dissolve
    chuck "That was August's intention since she first started working here, it just took her this long to come around to the idea."
    kil "Oh, that's just fuckin' great. She's going to be extra annoying now."
    chuck "You should play nice with her, Killian."
    kil "Maybe I would if you gave me part of this place too."
    scene w2_5063 with dissolve
    chuck "Hmmpfh, one day. You haven't earned it yet lad."
    scene w2_5064 with dissolve
    mc "You already have the run of this place. What would even change?"
    kil "It'd just be nice..."
    scene w2_5065 with dissolve
    chuck "Chin up and enjoy yourself, lad. You're young. You should just concern yourself with enjoying life."
    chuck "God knows what I would've given to be able to enjoy all of this before my body got old and tired, but at least my charming nephew can reap the benefits of my fortune in my stead."
    scene w2_5066 with dissolve
    kil "You move better than I do, you spritely fuck!"
    scene w2_5065 with dissolve
    chuck "Not just you, but [mcf] too. Med school will be hell and you have a big future ahead of you, so suck as much pleasure out of this place as you can."
    scene w2_5067 with dissolve
    chuck "Most importantly though, make some fine memories {b}together{/b}."
    scene w2_5068 with dissolve
    mct "(Fine memories on the back of others' hardships, he means.)"
    chuck "It's your move, by the way."
    kil "Why bother? The outcome of the game was already decided before we even sat down."
    kil "Just like everything else..."
    scene black with fade
    "The game continued on, but I had known Ian long enough to know something was bothering him and festering beneath the surface."
    "Eventually, even though I had no idea how the game worked, it appeared Chuck beat Ian quite handily."
    scene w2_5069 with fade
    chuck "Ah... for want of a younger set of knees. Money really can't buy everything."
    scene w2_5070 with dissolve
    chuck "Thanks for sitting in, lad. Seeing you two together always makes me nostalgic for the time I spent at my sister's."
    mc "No problem. It was... enlightening."
    chuck "To think, he used to never want birthday parties!"

    if rosalindSolution == False:
        scene w2_5071 with dissolve
        mct "(Hmm...)"
        "Before I leave I could ask Chuck about alleviating Rosalind's problem with the loan shark."
        "Out of all the owners, we have the best rapport and it IS his business after all."
        hide screen textbox2 with dissolve

        menu:
            "Tell him about Rosalind's problem.":
                $ w2KillianRoseOffer = True
                show screen textbox2 with dissolve
                mc "Can I bring up some business with you?"
                scene w2_5072 with dissolve
                chuck "How odd, what is it?"
                scene w2_5071 with dissolve
                mc "One of the Carnations, Rosalind, requires some money or else it'll risk her--"
                scene w2_5074 with dissolve
                chuck "I'll stop you right there, lad. Bring it up with Kathy."
                chuck "The exhibition is her baby and I prefer to be hands-off with this place as much as possible."
                scene w2_5071 with dissolve
                "It was a flat refusal."
                mc "Right... I understand."
                scene w2_5073 with dissolve
                chuck "I wouldn't concern yourself too much about it. That woman has never let any of her playthings go."
                scene w2_5072 with dissolve
                chuck "Anyway, if you'll excuse me, nature calls."



            "Just wait and bring it up to Mrs. Pulman." if w2TIAugustRepeat == False:
                show screen textbox2 with dissolve
                "Nah, I'll just wait and broach the subject with the old woman as I planned."
                scene w2_5072 with dissolve
                chuck "Anyway, if you'll excuse me, nature calls."

            "Just wait and bring it up to someone else." if w2TIAugustRepeat == True:
                show screen textbox2 with dissolve
                "Hah, I'll just wait and broach the subject with either the old woman or August."
                scene w2_5072 with dissolve
                chuck "Anyway, if you'll excuse me, nature calls."

        scene w2_5075 with fade
        kil "So Hana's getting a piece of this pie..."
        scene w2_5076 with dissolve
        mc "You jealous?"
        scene w2_5077 with dissolve
        kil "Abso-fucking-lutely. She has nothing but hate for this place. I mean it's not like I deserve it any more than her, but like... {i}fuck{/i}."
        kil "It still irks me."
        scene w2_5078 with dissolve
        mc "...you ever think about what you're going to do with your life? Like when you're forty, do you think you'll still be taking pictures?"
        scene w2_5079 with dissolve
        kil "Fuck if I know. My dad is always on my back about working with him, but that's the one thing I definitely don't want to do."
        scene w2_5078 with dissolve
        mc "..."

        if w2KillianRoseOffer == True:
            scene w2_5080 with dissolve
            kil "Hey, speaking of Uncle's suggestion of making memories..."
            mc "Yeah?"
            "Ian looked like he had something to say, but didn't know how to say it."
            scene w2_5081 with dissolve
            kil "Let me help Rosalind with her problem."
            scene w2_5083 with dissolve
            mc "You don't know how much it is."
            scene w2_5081 with dissolve
            kil "Well?"
            scene w2_5083 with dissolve
            mc "About five thousand or so."
            scene w2_5082 with dissolve
            kil "I can comfortably do five thousand."
            scene w2_5083 with dissolve

            if kat_polite == True:
                mc "I'm sure Mrs. Pulman will take care of it."
            else:
                mc "I'm sure Kathleen will take care of it."

            scene w2_5084 with dissolve
            kil "Eh, I didn't work for any of my money. It all comes from my family, one way or another."
            scene w2_5083 with dissolve
            mc "Your self-awareness is commendable, you infuriating bastard."
            scene w2_5080 with dissolve
            kil "The reason I want to do it is... well..."
            scene w2_5082 with dissolve
            kil "Do you think she'll let us spit roast her if I gave her the money?"
            scene w2_5083 with dissolve
            mc "W-what?"
            scene w2_5081 with dissolve
            kil "I want you and me to double team her."
            scene w2_5083 with dissolve
            mc "You'll give her money if she sleeps with you?"
            scene w2_5085 with dissolve
            kil "If she sleeps with {b}us{/b}."
            scene w2_5083 with dissolve
            mc "Why the both of us?"
            scene w2_5082 with dissolve
            kil "I dunno. It's always been a dream of mine to lay some pipe with my bro."
            scene w2_5083 with dissolve
            mc "That's... pretty fucking weird."
            scene w2_5084 with dissolve

            if w1ExVeroPissedOn == True:
                kil "Don't give me weird. I watched you piss on a chick's face last week!"
            else:
                kil "Don't give me weird, you sadistic prick. I watched you fuck in front of a crowd of men just last week."

            scene w2_5085 with dissolve
            kil "Don't you think it would be fun to ruin that fat-tittied slut together? Maybe even high five as the guitar riff kicks in?"
            scene w2_5083 with dissolve
            mc "Are you fucking serious? You'll give Rosalind five thousand dollars to sleep with us?"
            scene w2_5081 with dissolve
            kil "Extremely goddamn serious."
            scene w2_5083 with dissolve
            mc "......"
            mc "..."
            hide screen textbox2 with dissolve

            menu:
                "Okay, you'll bring it up to Rosalind."(chg=["killian_up2"]):
                    $ Killian_Bromance +=2
                    $ rosalindKilSolution = True
                    $ rosalindSolution = True
                    show screen textbox2 with dissolve
                    mc "Why not?"
                    scene w2_5086 with dissolve
                    "It wasn't like I was opposed to banging Rosalind and this would solve her immediate problems. The exhibition itself was a whole other ballgame, but she would be able to breathe for a few weeks."
                    scene w2_5087 with dissolve
                    kil "Really? You're not going to get holier-than-thou about it? Really, really?"
                    scene w2_5086 with dissolve
                    mc "Yeah. If she agrees to it, why not?"
                    scene w2_5088 with dissolve
                    kil "Haha! Fuckin' awesome!"
                    mc "It's up to her."
                    kil "She'll say yes!"
                    "It was true. She will. She probably would've done it even with just the sliver of hope of it helping her exhibition standing."
                    scene w2_5089 with dissolve
                    mc "It's strange how happy you are about this..."
                    kil "It's strange that you're not, quite frankly."
                    scene w2_5090 with dissolve
                    mc "......"
                    kil "..."
                    scene w2_5091 with dissolve
                    mc "Pft-"
                    "It was so absurd and Ian was so genuinely happy that I couldn't help but share in a laugh."
                    mc "Alright, fine. I'll bring it up with her."
                    scene black with fade
                    "We talked for a few more minutes and parted ways, Ian with a spring in his step."
                    jump w2TIHallway
                "That's too much for you."(chg=["killian_down2"]):

                    $ Killian_Bromance -=2
                    show screen textbox2 with dissolve
                    mc "I don't think so. She's already being taken advantage of, let's not layer it on."
                    if roseFlag == True:
                        "The hypocrisy of my own words wasn't lost on me."
                    scene w2_5093 with dissolve
                    kil "She won't have a problem with it you know. She'd probably even be relieved it was so simple."
                    scene w2_5092 with dissolve
                    "He wasn't wrong. She probably would've done it even with just the sliver of hope of it helping her exhibition standing."
                    "That's how desperate she was."
                    mc "Still, I don't think I want to do that."
                    scene w2_5095 with dissolve
                    kil "..."
                    scene w2_5094 with dissolve
                    kil "Whatever, it was just an offer."
                    scene w2_5095 with dissolve
                    "He looked completely defeated."
                    scene w2_5096 with dissolve
                    kil "Still, maybe one day, in a different set of circumstances?"
                    "Now he looked hopeful, like a child looking for his parents to buy him a toy."
                    scene black with fade
                    mc "You're so fucking weird."
                    "We talked for a few minutes before parting ways."
                    jump w2TIHallway
        else:
            mc "Well, you'll figure it out. You have the luxury of taking the time to find something that makes you happy."
            "Ian and I talked for a few minutes, talking about this and that and nothing, before finally parting ways."
            scene black with fade
            "......"
            "..."
            jump w2TIHallway
    else:
        jump w2TIHallway


label w2TINurse:

    if w2TINurseRepeat == False:
        $ w2TINurseRepeat = True
        scene w2_5097 with dissolve
        mc "Hello."
        scene w2_5098 with dissolve
        nurse "Hello, Mr. [mcl]."
        scene w2_5099 with dissolve
        mc "You don't have to call me that."
        scene w2_5098 with dissolve
        nurse "I don't have to call you [mcf] either."
        scene w2_5099 with dissolve
        mc "What are you doing here?"
        scene w2_5100 with dissolve
        nurse "Waiting to play a game of chess, as you can see."
        scene w2_5101 with dissolve
        mc "Ah... \"one of Dr. Chuck's indulgences\" you mean."
        scene w2_5102 with dissolve
        nurse "Yes, he wanted to have a game with me."
        scene w2_5101 with dissolve
        mc "Are you good at chess?"
        scene w2_5102 with dissolve
        nurse "Not particularly. It's only a passing hobby."
        scene w2_5101 with dissolve
        mc "I see... sorry for all the questions. I don't mean to interrogate you, but it's just we've never spoken and I was surprised to find you here sitting all alone..."
        scene w2_5102 with dissolve
        nurse "No need to explain yourself, Mr. [mcl]."
        sophia "To answer what you want to ask, my name is Sophia."
        scene w2_5101 with dissolve
        mc "I like that. That's a pretty name."
        scene w2_5103 with dissolve
        sophia "..."
        mc "Well, you already know who I am, so I can just say..."
        scene w2_5104 with dissolve
        mc "Nice to meet you."
        scene w2_5105 with dissolve
        mc "Oh, sorry. You don't have to get up."
        sophia "No..."
        scene w2_5106 with dissolve
        sophia "It was rude of me to remain sitting."
        scene w2_5107 with dissolve
        "The moment we got close, I got a whiff of something alarming."
        "It was faint, but the perfume she wore bore the same scent as Mrs. Pulman's and had a similarly..."
        scene w2_5108 with dissolve
        mc "Ah-heh...!"
        "A similarly arousing effect."
        scene w2_5109 with dissolve
        mc "That's a... \"nice\" perfume you're wearing. Where did you get it?"
        scene w2_5110 with dissolve
        sophia "{b}Perfumery{/b} is another passing hobby of mine."
        scene w2_5109 with dissolve
        mc "You're telling me you made it yourself?"
        scene w2_5110 with dissolve
        sophia "That's correct."
        scene w2_5108 with dissolve
        "{b}She{/b} created that devilish aroma? Isn't she a nurse?"
        scene w2_5109 with dissolve
        mc "That's... impressive."
        scene w2_5111 with dissolve
        sophia "It's only an interest of mine."
        scene w2_5112 with dissolve
        mct "(Who is this woman?)"
        scene w2_5109 with dissolve
        mc "Do you have any other talents to speak of?"
        scene w2_5113 with dissolve
        sophia "Well..."
        "Her gaze went below my neck, past my waistline, and stopped at the subtle outline of the half-chub in my pants."
        scene w2_5111 with dissolve
        sophia "There is one other thing, but it must ONLY be done at Dr. Van Doren's discretion."
        scene w2_5108 with dissolve
        "Her implication immediately raised many questions about the man and I could tell she had a handle on my unscrupulous thoughts by the way her eyes drank me in."
        scene w2_5109 with dissolve
        mc "I guess Abel Van Doren likes to surround himself with women of talent."
        scene w2_5111 with dissolve
        sophia "I glow but faintly next to a man of his stature."
        scene w2_5109 with dissolve
        mc "That's..."
        scene w2_5108 with dissolve
        "As the aphrodisiac worked its insidious magic and took a stronger hold of my body, I knew it was time to cut our conversation short."
        scene w2_5109 with dissolve
        mc "I'm glad we got introduced."
        scene black with fade
        sophia "Likewise, Mr. [mcl]."
        jump w2TIVIPLounge
    else:

        scene w2_5114 with dissolve
        "I've already introduced myself to Abel Van Doren's nurse. It'd be dangerous to get close to her again, lest I want this half-chub in my pants to graduate to a raging, reason-consuming hardon."
        jump w2TIVIPLounge

label w2TIChessGame:

    if w2TIChessGameRepeat == False:
        $ w2TIChessGameRepeat = True

        if w2TINurseRepeat == True:
            scene w2_5115 with dissolve
            sophia "You may play white, sir."
            scene w2_5116 with dissolve
            chuck "Ohohoh, you cheeky lass! Don't think I won't take any advantage I can get."
            chuck "Don't forget the terms of our bet."
            scene w2_5117 with dissolve
            sophia "None of this is necessary for {i}that{/i}, sir."
            scene w2_5118 with dissolve
            chuck "Quite frankly, if I can't beat you, I don't want it."
            scene w2_5117 with dissolve
            sophia "I'm afraid you won't get it then, sir."
            scene w2_5116 with dissolve
            chuck "Oh, time will tell."
            jump w2TIVIPLounge
        else:

            scene w2_5115 with dissolve
            nurse "You may play white, sir."
            scene w2_5116 with dissolve
            chuck "Ohohoh, you cheeky lass! Don't think I won't take any advantage I can get."
            chuck "Don't forget the terms of our bet."
            scene w2_5117 with dissolve
            nurse "None of this is necessary for {i}that{/i}, sir."
            scene w2_5118 with dissolve
            chuck "Quite frankly, if I can't beat you, I don't want it."
            scene w2_5117 with dissolve
            nurse "I'm afraid you won't get it then, sir."
            scene w2_5116 with dissolve
            chuck "Oh, time will tell."
            jump w2TIVIPLounge
    else:

        scene w2_5119 with dissolve
        "No telling how long the game will go on."
        jump w2TIVIPLounge

label w2TIAbel:
    scene w2_5120 with dissolve
    abel "Your Dr. Kohler is an interesting man."
    scene w2_5121 with dissolve
    mc "How so?"
    scene w2_5122 with dissolve
    abel "For the past two months, he's requested to play against my aide."
    scene w2_5123 with dissolve
    abel "For the past two months, he has been hopelessly defeated. One wonders what the point of this exercise is, when the gap in their ability is so insurmountable."
    scene w2_5124 with dissolve
    abel "Men our age don't have the time for games."
    scene w2_5125 with dissolve
    mc "Yet, you're here watching a game?"
    scene w2_5124 with dissolve
    abel "Well, the man {b}is{/b} a hospitable host. I should be an equally gracious guest."
    scene w2_5125 with dissolve
    "All the while we spoke, Abel kept his steely gaze on the subject of his words, as if he was trying to unravel the man with his eyes."
    mc "Do you continue to enjoy your time at the club then, Dr. Van Doren?"
    scene w2_5124 with dissolve
    abel "I do. It's truly a playground."
    abel "The results of my time here will be illuminating."
    scene w2_5125 with dissolve
    mc "..."
    scene w2_5126 with dissolve

    if w2TINurseRepeat == True:
        "Over the next ten or so minutes, we sat in silent observation of Dr. Chuck and Sophia's game."
    else:
        "Over the next ten or so minutes, we sat in silent observation of Dr. Chuck and the nurse's game. The fairer of which's name I came to learn was Sophia."

    scene w2_5127 with dissolve
    chuck "Ah... how frustrating!"
    chuck "You got me. I resign."
    sophia "Thank you for the game, Dr. Kohler."
    chuck "The pleasure is all mine, Miss."
    scene w2_5128 with dissolve
    abel "You held out longer than last week, Charles."
    chuck "Not long enough..."
    sophia "Would you like to play again, Dr. Kohler?"
    chuck "Would you mind me taking up some more of your precious assistant's time, Abel?"
    abel "I've told you to consider her yours."
    scene w2_5129 with dissolve
    chuck "Then I would very much like to play again."
    sophia "You may play white, sir."
    chuck "Aha...! This woman...!"
    stop music fadeout 3.0
    scene black with fade
    "Two more games saw Chuck suffer the same result: defeat. I had come to learn that this was his thirty-first straight loss."
    "Still, he remained undeterred and another game was set up for tomorrow night."
    play music "music/devious-little-smile.ogg"
    scene w2_5130 with dissolve
    chuck "Ha! Did you enjoy watching me lose, lad?"
    scene w2_5131 with dissolve
    mc "For you to be so determined, Dr. Van Doren's nurse must be quite good."
    scene w2_5132 with dissolve
    chuck "Nurse? Dr. Lundgren is posed to take over Abel's responsibilities as research lead at Vanderbilt once he dies."
    scene w2_5131 with dissolve
    mc "Shit, I just assumed..."
    scene w2_5132 with dissolve
    chuck "I can see why you might think that... looking after his health is also part of what she does for that tight ass."
    scene w2_5130 with dissolve
    chuck "One day though, I'll beat her. Losing just makes the victory all that much sweeter."
    scene w2_5133 with dissolve
    chuck "And when I do..."
    scene w2_5134 with dissolve
    "He may not have finished his thought, but at this moment, Dr. Chuck didn't look like the jovial man I thought I knew."
    "His lips curled up with lascivious intent, his good-natured expression replaced by something more unsettling."
    stop music fadeout 3.0
    scene black with fade
    chuck "Come, lad. Let's get out of here."
    play sound "sound effects/notification.wav"
    $ met_sophia = True
    show bioadd with dissolve
    $ renpy.pause(3, hard=True)
    "......"
    "..."
    jump w2TIKathleen

label w2TIKathleen:
    play music "music/cold-sober.ogg"
    scene w2_5135 with circlewipe
    kat "Excellent timing. Hana and I just concluded our discussion."
    mc "I was gone for almost fifty minutes. What did the two of you possibly talk about for that long?"
    "A quick glance at the old woman told me her face was intact and she still had all her fingers."
    scene w2_5136 with dissolve
    kat "Oh, this and that. Needless to say, we talked about her future involvement in the club and what shape that may take, as well as what could practically be changed around her for the better."
    scene w2_5137 with dissolve
    mc "I'm interested in what those suggestions might be."
    scene w2_5136 with dissolve
    kat "If Hana wants to that's fine, but the details are not mine to divulge. It was a private conversation."
    scene w2_5138 with dissolve
    kat "I will say she found the photos you took \"interesting\"..."
    scene w2_5137 with dissolve
    mc "She... saw those?"
    scene w2_5139 with dissolve
    "The thought of Hana seeing the debauchery I helped orchestrate filled me with an implacable sense of frustration bordering on shame."
    scene w2_5140 with dissolve
    kat "I couldn't wait to do my initial review. I had spent all week anticipating the juicy morsels you would hand deliver me."
    scene w2_5136 with dissolve
    kat "And since she was here, I took it as an opportunity to evaluate her eye for the erotic."
    scene w2_5137 with dissolve
    mc "What did she think of them?"
    scene w2_5136 with dissolve
    kat "As you might expect, she didn't have much to add."
    scene w2_5137 with dissolve
    mc "Is that so?"
    scene w2_5140 with dissolve
    kat "Don't worry. I only showed her a select few. For example, I spared her from seeing you parade that large whore around like a dog."
    kat "That was... well, that made my whole damn morning [mcf]."
    scene w2_5137 with dissolve
    mc "That was Veronica's idea. Her collar too."
    scene w2_5141 with dissolve
    kat "Was it now? She surprises me!"
    scene w2_5142 with dissolve
    mc "She's determined to save her business. She wants to win. That desperation is what you count on, right?"
    scene w2_5141 with dissolve
    kat "True, but to hear she {b}volunteered{/b} to crawl around like a bitch... what a delight."
    scene w2_5142 with dissolve
    mc "So you are pleased with what I brought you then?"
    scene w2_5143 with dissolve
    kat "Very pleased. It wasn't perfect, but you lived up to the task colorfully."
    scene w2_5144 with dissolve
    kat "Felicia wasn't as flustered as I hoped, but the shoot itself was impeccable. She's such an expressive woman, she carried the earlier portion entirely with her clothes on."
    scene w2_5142 with dissolve
    mc "Good. I was worried that might not have translated well through just simple photos. We should've done it on video."
    scene w2_5143 with dissolve
    kat "You think? I find there's something particularly sordid about a photo myself, but I will keep that in mind for the future."
    scene w2_5145 with dissolve
    kat "After all, you should always match the right tool with the artist."
    scene w2_5142 with dissolve
    mc "How did you find Rosalind's shoot?"
    "I, to my own surprise, found myself asking questions as if I genuinely wanted an honest appraisal of my work."
    scene w2_5144 with dissolve
    kat "Rose went according to expectations, which is to say it turned out well. Out of all the Carnations, she was textbook in her actions."
    scene w2_5141 with dissolve
    kat "Really... that woman's got such sad eyes and that combination of meek and desperate... ah, I {b}love{/b} it."
    scene w2_5142 with dissolve
    "Do what you enjoy and you'll never work a day in your life, eh?"
    mc "Do you know who's going to win then?"
    scene w2_5143 with dissolve
    kat "Not yet. I have my own favorite, but it all depends on how our patrons feel. I'll send them out this evening and we'll know by tomorrow night."
    scene w2_5145 with dissolve
    kat "Before we finish, tell me: who did you have the most fun with? Which bitch did you enjoy watching squirm the most?"
    scene w2_5147 with dissolve
    hide screen textbox2 with dissolve

    menu:
        "Rosalind."(chg=["RoseShootPoints_up"]):
            $ w2RoseShootPoints +=1
            show screen textbox2 with dissolve
            "We were being so candid, the answer came easily from my mouth, unfiltered and entirely truthful."
            scene w2_5148 with dissolve
            mc "Rosalind."
            scene w2_5147 with dissolve
            kat "Mrs. Carter. I thought so. Doe-eyed and vulnerable, {b}motherly{/b}. It must be fun for a man with your peculiarities to stomp all over that."
            scene w2_5149 with dissolve
            mc "What is that supposed to mean?"
            scene w2_5147 with dissolve
            kat "Nothing. Just the musings of an old woman."
        "Veronica."(chg=["kathleen_up","VeronicaShootPoints_up"]):

            $ w2VeroShootPoints +=1
            $ Kathleen_Affection +=1
            show screen textbox2 with dissolve
            "We were being so candid, the answer came easily from my mouth, unfiltered and entirely truthful."
            scene w2_5148 with dissolve
            mc "Veronica."
            scene w2_5147 with dissolve
            kat "Miss Lynch. Not much in the looks department, but it is exciting to put a heel to the back of that prideful cunt's neck and grind her face into the dirt."
            kat "Am I right?"
            scene w2_5149 with dissolve
            mc "I enjoy working with her. That's it."
            scene w2_5147 with dissolve
            kat "Hmpfh. Alright."
        "Felicia."(chg=["FeliciaShootPoints_up"]):


            $ w2FelShootPoints += 1
            show screen textbox2 with dissolve
            "We were being so candid, the answer came easily from my mouth, unfiltered and entirely truthful."
            scene w2_5148 with dissolve
            mc "Felicia."
            scene w2_5147 with dissolve
            kat "Mrs. Ford, yes. She's got quite the magnetic pull."
            kat "Personally, the way she rises to the occasion makes breaking her in less fun, but I understand that appeal."
            scene w2_5148 with dissolve
            mc "She's easy to work with."
            scene w2_5147 with dissolve
            kat "I bet she is..."

    scene w2_5137 with dissolve
    mc "Why do you ask?"
    scene w2_5136 with dissolve
    kat "I'll take your opinion into account when factoring in who wins this challenge. Could matter if things are close and I need to tip the scales in one girl's direction."

    if rosalindSolution == False:
        kat "I believe that's all I had to say. Do you have anything to add?"
        scene w2_5137 with dissolve
        mc "Actually, I do. It's about Rosalind and could present a problem with her participation for the remaining weeks."
        scene w2_5150 with dissolve
        kat "Sounds serious. Speak."
        scene w2_5151 with dissolve
        mc "Her loan shark is putting the screws to her. Threatening her."
        mc "She has less than a week to pay back what she owes in interest before he acts on his threats."
        scene w2_5152 with dissolve
        kat "I see... well, this isn't the first time a Carnations' circumstances have threatened the prosperity of my show."
        kat "I'll give her whatever money she needs, but even should she win, that will be a separate account."
        scene w2_5153 with dissolve
        mc "Meaning?"
        scene w2_5155 with dissolve
        kat "Meaning her fat ass will work here after the exhibition is over until she pays back what is due."
        scene w2_5153 with dissolve
        mc "That's..."
        hide screen textbox2 with dissolve

        menu w2TIKatRoseSolution:
            "{color=#FF1493}[[Social Butterfly/Chameleon]{/color} Suggest the situation would be a good rallying moment."(chg=["kathleen_trust_up"]) if perk_socialButterfly == True or perk_socialChameleon == True:
                $ Kathleen_Trust += 1
                $ rosalindSolution = True
                $ rosalindKatSolutionFree = True

                show screen textbox2 with dissolve
                mc "I think you should do it at cost."
                scene w2_5158 with dissolve
                kat "Why? The amount of money may be a pittance, but it's a good chance to ensnare that cow and squeeze a little more out of her."
                scene w2_5149 with dissolve
                mc "Hear me out, alright? You remove this burden off Rosalind's shoulders, no strings attached, you'll invigorate her in the coming weeks."
                scene w2_5159 with dissolve
                mc "She'll shine more brightly on the stage, knowing that the only thing she has to focus on over the next two weeks is the exhibition itself."
                scene w2_5147 with dissolve
                kat "Maybe. Do you think that's the case with her?"
                scene w2_5149 with dissolve
                mc "I mean, I'm new at this and nothing's guaranteed, but my primary job responsibility is to keep the Carnations motivated."
                scene w2_5159 with dissolve
                mc "I think fostering some goodwill between the club and the Carnations will be beneficial. Plus, on the opposite side of things, adding another chain around her neck will just weigh her down."
                scene w2_5148 with dissolve
                mc "Having more debt looming over her regardless of the contest's outcome will just demotivate her. Her performance on stage will suffer."
                scene w2_5156 with dissolve
                kat "Hmm..."
                mc "Quite frankly, it's in the club's best interest if she's unfettered by everything else besides putting on the best show."
                scene w2_5154 with dissolve
                kat "And what if Veronica sees the handout and gets jealous?"
                scene w2_5156 with dissolve
                mc "You explain to her that it's extenuating circumstances. She's a reasonable woman."
                mc "She's not the type of person to be embittered just because Rose's unfortunate circumstances were made better."
                scene w2_5158 with dissolve
                kat "Are you basing this on what you know of the woman or are you just giving her the benefit of the doubt?"
                scene w2_5157 with dissolve
                kat "..."
                scene w2_5145 with dissolve
                kat "Alright, we'll do it your way. I'll unconditionally give her the money she needs."
            "As a favor, ask her to do it for free.":


                show screen textbox2 with dissolve
                mc "I think you should do it for free."
                scene w2_5158 with dissolve
                kat "On what basis? The amount of money may be a pittance, but it's a good chance to ensnare that cow and squeeze a little more out of her."
                scene w2_5156 with dissolve
                mc "It just doesn't sit right with me, piling atop her misery like this."
                scene w2_5158 with dissolve
                kat "This place doesn't run on happy feelings, [mcf]."
                scene w2_5156 with dissolve
                mc "The exhibition does run on our performers' well-being."
                scene w2_5157 with dissolve
                kat "Hmmm..."
                mc "At the very least, can we do it my way, as a favor? I did a good job this week didn't I?"

                if w2KatSex == True or Kathleen_Affection >= 20:
                    $ rosalindSolution = True
                    $ rosalindKatSolutionFree = True
                    scene w2_5145 with dissolve
                    kat "Alright. We'll do it your way since I like you. I'll unconditionally give that cow the money she needs."
                    kat "Remember it and don't ever call me an unreasonable woman."
                else:
                    $ rosalindSolution = True
                    $ rosalindKatSolution = True
                    scene w2_5146 with dissolve
                    kat "No. We don't give handouts around here and there's a certain way things should be done."
                    scene w2_5143 with dissolve
                    kat "Tell Rosalind her loan shark problem will be taken care of in the immediate future, but she'll be on the hook to me for a more manageable sum after the exhibition."
                    scene w2_5142 with dissolve
                    "Well, I tried. It's out of my hands."
                    mct "(...maybe I should've fostered a better working relationship with the woman.)"
            "You guess Rose has no other choice in the matter.":

                $ rosalindSolution = True
                $ rosalindKatSolution = True
                show screen textbox2 with dissolve
                mc "Well, it's something I guess."
                scene w2_5144 with dissolve
                kat "Good. Tell Rosalind her loan shark problem will be taken care of in the immediate future, but she'll be on the hook to me for a more manageable sum after the exhibition."

            "{color=#696969}[[Social Butterfly/Chameleon] Suggest the situation would be a good rallying moment. {/color}." if perk_socialButterfly == False and perk_socialChameleon == False:
                jump w2TIKatRoseSolution

        scene w2_5137 with dissolve
        mc "Thank you, Mrs. Pulman. That was the only other thing I had to report."
    else:


        scene w2_5160 with dissolve
        mc "Then do you need me for anything else? Can I go?"
        kat "If you have nothing else to report then, {b}yes{/b}. You may."

    scene w2_5161 with dissolve
    kat "Oh, [mcf]..."
    mc "..."
    scene w2_5162 with dissolve
    stop music fadeout 3.0
    kat "Good work, by the way. Having you around to do the stuff I can't do is proving worthwhile indeed."
    scene black with fade

    if rosalindFelSolution == True:
        "Having wrapped up my business at the club, a thought crossed my mind regarding something I probably should've done last night."
        scene w2_5163 with circlewipe
        "I should notify Rosalind that, thanks to Felicia's help, she can breathe easier for the time being. {b}Only{/b} just a little though..."
    else:
        "Having wrapped up my business at the club, I wanted to notify Rosalind that she can breathe easier for the time being."
        scene w2_5163 with circlewipe
        "If only just a little bit..."

    play sound "sound effects/ringing-outbound.mp3"
    "*Ring, ring.*"
    stop sound
    rose "Hello?"
    scene w2_5164 with dissolve
    mc "I hope I'm not calling at an inconvenient time."
    play music "music/a-lost-map-of-a-heaven.ogg"
    scene w2_5165 with dissolve
    rose "A bad time? *Scoff* What do you want?"
    scene w2_5166 with dissolve
    "Rosalind's tone was unusually frosty and vacant."
    mc "Is everything okay?"
    scene w2_5165 with dissolve
    rose "Oh, just swell..."
    scene w2_5167 with dissolve
    mc "Has that asshole bottom feeder been harassing you?"
    scene w2_5168 with dissolve
    rose "Of course he has, but even if he wasn't..."
    scene w2_5165 with dissolve
    rose "*Sigh* It's not like my life wouldn't be in the shitter anyway..."
    scene w2_5167 with dissolve
    mc "You don't have anyone to talk about your problems with, do you? It must be tough."
    scene w2_5165 with dissolve
    rose "Not really. What good would talking do?"
    scene w2_5166 with dissolve
    mc "Talking helps."
    scene w2_5168 with dissolve
    rose "The only thing that would help is $23,000 or my husband's balls in a jar."
    scene w2_5166 with dissolve
    mc "...sorry."
    "Platitudes would obviously be distasteful to a woman with her circumstances."
    scene w2_5170 with dissolve
    rose "Forget I said anything. I'm fine."
    rose "What do you need, Mr. [mcl]?"
    scene w2_5169 with dissolve
    mc "I'll cut to the chase. I found some money for you to pay off the interest you owe, as well as keep you square for the remaining weeks of the exhibition."
    scene w2_5171 with dissolve
    rose "...y-you did?"

    if rosalindFelSolution == True:
        scene w2_5172 with dissolve
        mc "I did. No strings attached, either."
        scene w2_5173 with dissolve
        "--for Rosalind, at least. Naturally, I'm leaving out the details of her sugar mama proposition."
        scene w2_5172 with dissolve
        mc "Felicia is going to wire me the money and I'm going to transfer it to you."
        scene w2_5173 with dissolve
        rose "Felicia...? Why would she...?"
        scene w2_5174 with dissolve
        mc "Who can say why the crazy woman does anything, but in this case, I think she just wanted to be a friend. You guys may be competing, but you're in this together."
        scene w2_5176 with dissolve
        mc "I bet it was my speech last week that made an impression on her."
        scene w2_5177 with dissolve
        "I said it with a cocky inflection as a joke."
        scene w2_5178 with dissolve
        rose "Heh, I doubt that... {b}a lot{/b}."
        scene w2_5179 with dissolve
        mc "So you'll take it, right? Of course?"
        scene w2_5180 with dissolve
        rose "I feel weird about it, but I'm not in any position to refuse."
        scene w2_5181 with dissolve
        mc "Don't worry. It really is an unconditional sum. Felicia is... very wealthy."
        scene w2_5182 with dissolve
        rose "I still don't understand why she would... ah..."
        scene w2_5173 with dissolve
        rose "Will you thank her for me?"
        scene w2_5174 with dissolve
        mc "Eh? Find the right moment and do it yourself."
        mc "Don't forget we're meeting at the diner tomorrow."
        scene w2_5183 with dissolve
        rose "You're really serious about this team-building nonsense, huh?"
        mc "It helps me feel like I'm doing a real fucking job. For some reason, that's important to me."
        scene w2_5184 with dissolve
        rose "Heh...! Then I'll thank her in person."
        mc "I know this is a tough ask, but take all the time you can to get in a good headspace for tomorrow."
        scene w2_5185 with dissolve
        mc "Do something you enjoy or treat yourself or... whatever. Everything must feel joyless right now, but you should try."
        rose "Thanks, [mcf]. I'll try."
        "To my relief, her words weren't as vacant as earlier."
        $ history_rosalind = "I called Rosalind and she seemed unusually down, but perked back up when she learned that her loan shark problems have been temporarily alleviated thanks to my arrangement with Felicia."
        $ unread_rosalind = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve
        mc "I'll see you tomorrow, Rose. Take care."

    if rosalindAugSolution == True or rosalindKatSolutionFree:
        scene w2_5172 with dissolve
        mc "I did. No strings attached, either."
        scene w2_5173 with dissolve
        rose "I don't have to do anything or pay it back?"
        scene w2_5176 with dissolve
        mc "Nope. Not a thing."
        mc "It's in the club's best interest not to allow anything to interfere with your performance. You can't imagine the kind of money the exhibition brings in and you're one of the stars."
        mc "Don't forget I have your back, Rose."
        scene w2_5177 with dissolve
        "I mean it's not like I had figures or anything, but it seemed like a good guess."
        scene w2_5178 with dissolve
        rose "That's... Ha...! That's a relief."
        scene w2_5179 with dissolve
        mc "Honestly, I don't know why I'm acting so cool considering I'm not the one footing the bill, but..."
        scene w2_5180 with dissolve
        rose "Thank you, [mcf]."
        scene w2_5181 with dissolve
        "She cut me off, her words less vacant than before."
        scene w2_5180 with dissolve
        rose "I know you said you would help, but I just... I expected it to cost me."
        scene w2_5176 with dissolve
        mc "I know it's not a cure for what ails you, but take it one day at a time and get yourself in a good headspace for tomorrow."
        mc "Do something you enjoy or treat yourself or... whatever. Everything must feel joyless right now, but you should try."
        scene w2_5183 with dissolve
        rose "I'll try my best."
        scene w2_5184 with dissolve
        rose "I didn't mean what I said earlier, about my life being in the shitter."
        scene w2_5185 with dissolve
        mc "I know. I'll see you at the diner tomorrow, just like last week."
        $ history_rosalind = "I called Rosalind and she seemed unusually down, but perked back up when she learned that her loan shark problems have been temporarily alleviated."
        $ unread_rosalind = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve
        mc "Take care, Rose."


    if rosalindKilSolution == True:
        scene w2_5174 with dissolve
        mc "Well potentially. Killian said he'd pay it, on the condition that you entertain us one evening."
        scene w2_5175 with dissolve
        "No point in beating around the bush..."
        scene w2_5174 with dissolve
        mc "More specifically, he wants me, you, and him to have a threesome."
        scene w2_5186 with dissolve
        rose "...are you serious?"
        scene w2_5187 with dissolve
        mc "I know you feel like you don't have a choice, but you can say no and I can take this to Mrs. Pul-"
        scene w2_5188 with dissolve
        rose "All that money, just for {b}that{/b}? Ha...!"
        scene w2_5178 with dissolve
        rose "Why the heck would I say no? That's just a drop in the bucket after everything I've already done and am going to do by the end of this month."
        scene w2_5179 with dissolve
        mc "I... figured you might see it that way."
        scene w2_5180 with dissolve
        rose "If the club paid for it, I'd likely have to pay it back, right?"
        scene w2_5181 with dissolve
        mc "Possibly."
        scene w2_5178 with dissolve
        rose "No, this way is for the best. Having some fun and making some money feels a lot better than the current gamble I'm taking with this game."
        scene w2_5179 with dissolve
        "I expected her to be pragmatic, but I didn't expect this level of enthusiasm."
        mc "I'll let him know then."
        scene w2_5176 with dissolve
        mc "I know it's not a cure for what ails you, but take it one day at a time and get yourself in a good headspace for tomorrow."
        mc "Do something you enjoy or treat yourself or... whatever. Everything must feel joyless right now, but you should try."
        scene w2_5183 with dissolve
        rose "I'll try my best."
        scene w2_5184 with dissolve
        rose "I didn't mean what I said earlier, about my life being in the shitter."
        scene w2_5185 with dissolve
        mc "I know. I'll see you at the diner tomorrow, just like last week."
        $ history_rosalind = "I called Rosalind and she seemed unusually down, but perked back up when she learned that her loan shark problems have been temporarily alleviated thanks to the unusual (and weird) arrangement made with Ian."
        $ unread_rosalind = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve
        mc "Take care, Rose."


    if rosalindKatSolution == True:
        scene w2_5174 with dissolve
        mc "I did, but whether you win or lose, the club is going to want you to pay it back after the exhibition is over."
        scene w2_5175 with dissolve
        rose "...heh, figures."
        scene w2_5167 with dissolve
        mc "I know it's not ideal, but..."
        scene w2_5168 with dissolve
        rose "Nothing in life is free."
        scene w2_5166 with dissolve
        mc "So, you'll take the money?"
        scene w2_5165 with dissolve
        rose "Of course. If I win, it's a small sum compared to what I currently owe. If I lose, well just pile more dirt on me, I'm already buried."
        scene w2_5166 with dissolve
        "Her dark pragmatism got under my skin and made me wish I found a way to get her the money with no strings attached."
        mc "I'll let Mrs. Pulman know then."
        scene w2_5172 with dissolve
        mc "I know it's not a cure for what ails you, but take it one day at a time and get yourself in a good headspace for tomorrow."
        mc "Do something you enjoy or treat yourself or... whatever. Everything must feel joyless right now, but you should try."
        scene w2_5183 with dissolve
        rose "I'll... try my best."
        scene w2_5184 with dissolve
        rose "I didn't mean what I said earlier, about my life being in the shitter."
        scene w2_5185 with dissolve
        "Her voice wasn't quite as vacant as previously before."
        mc "I know. I'll see you at the diner tomorrow, just like last week."
        $ history_rosalind = "I delivered the news to Rosalind. Her loans shark woes have been temporarily alleviated, at the steep cost of owing the club money as well."
        $ unread_rosalind = True
        play sound "sound effects/notification.wav"
        show bioupdate with dissolve
        mc "Take care, Rose."

    stop music
    play sound "sound effects/phonemenu.wav"
    scene w2_5189 with dissolve
    "*Click*"
    mct "(Good. Glad that's taken care of...)"
    scene w2_5190 with dissolve
    hana "There you are. I got sick of twiddling my thumbs at the bar waiting for you."
    mc "Why were you waiting for me?"
    hana "I'm your ride, remember? I wasn't just gonna ditch you."
    scene w2_5191 with dissolve
    mc "Ah, yeah. Right. You're the best, Hana."
    scene w2_5192 with dissolve
    hana "Ain't I?"
    scene w2_5191 with dissolve
    mc "Now, take me home, driver."
    scene w2_5193 with dissolve

    if minaFlag == True:
        mct "(I think I'll get a nap in before meeting Mina and her brother at the arcade.)"
        scene black with fade
        hana "Fucker...!"
        "......"
        "..."
        jump w2MinaArcade
    else:
        mct "(I'm feeling like a nap.)"
        scene black with fade
        hana "Fucker...!"
        "......"
        "..."
        jump w2June12End

label w2MinaArcade:

    hide screen textbox2 with dissolve
    hide screen qmenu with dissolve
    play sound "sound effects/sting-bluesy-vibes.wav"
    scene transitionmina02 with blinds
    $ renpy.pause(6, hard=True)
    $ date = "june12day"
    play ambient "sound effects/city-night.wav"
    scene w2_5194 with fade
    show screen textbox2 with dissolve
    show screen qmenu with dissolve
    "Despite having absolutely nothing to do between getting home and meeting up with Mina, I still somehow managed to be late."
    "Our meeting spot was an old arcade in the city, one that had been there for as long as I could remember and had changed hands many times over the years. It was the kind of place whose floor and walls took you to a whole other era."
    mc "Ah...!"
    scene w2_5195 with dissolve
    mc "Sorry I'm late, I hope you didn't... hmm, where's your sister?"
    scene w2_5196 with dissolve
    sora "Not here yet..."
    scene w2_5197 with dissolve
    "His voice came out in a wispish tone that was hard to make out against the hum of the city."
    scene w2_5198 with dissolve
    mc "Ah, no biggie. Want to go in and play some games or do you want to wait out here together?"
    scene w2_5196 with dissolve
    sora "You can go in if you want... I'll stay out here..."
    scene w2_5197 with dissolve
    mct "(Right, the kid's shy...)"
    scene w2_5199 with dissolve
    mc "I'll wait with you then."
    sora "Suit yourself..."
    scene w2_5200 with dissolve
    "......"
    scene w2_5201 with dissolve
    "..."
    scene w2_5202 with dissolve
    sora "So... how do you know my sister?"
    scene w2_5203 with dissolve
    mc "I met her through Killian. You know him?"
    "I recalled Mina mentioning that Ian hadn't met her mother, so I could only guess what her brother might know."
    scene w2_5202 with dissolve
    sora "Yeah, I've met him two or three times... and I've heard about him a whole lot more..."
    scene w2_5203 with dissolve
    mc "You and Mina are pretty close, huh?"
    "That much was clearly obvious to me already, but I wanted to start building a rapport with the boy if the three of us were going to be spending a couple of hours together."
    scene w2_5204 with dissolve
    sora "I guess... I mean, she's my sister..."
    scene w2_5203 with dissolve
    mc "I don't know what that's like. Only child here."
    scene w2_5204 with dissolve
    sora "It's... I mean..."
    scene w2_5200 with dissolve
    "Looks like I was losing him again."
    scene w2_5205 with dissolve
    mc "It's got its ups and downs?"
    scene w2_5206 with dissolve
    sora "Yeah, she couldn't wait to leave home last-- oh, there..."
    mc "...?"
    play music "music/ukulele-fun.ogg"
    scene w2_5207 with vpunch
    "It was sudden. {b}All too sudden{/b}."
    "An ambush. A sneak attack. A {i}stealth glomp{/i}."
    "Like prey caught unaware by a stalking lioness, I was {b}had{/b}."
    scene w2_5208 with dissolve
    mc "Hey..."
    scene w2_5209 with dissolve
    "Using her superior position, Mina pressed her chest firmly into my back and enveloped me in an all-consuming hug."
    scene w2_5210 with dissolve
    mina "Hey~!"
    scene w2_5209 with dissolve
    mct "(No bra...)"
    "The tight hold she had on me told me as much. I could feel semi-stiff buds of her breasts through the fabric of both of our shirts."
    scene w2_5210 with dissolve
    mina "Sorry I'm late. I mistimed my wash and didn't know what to wear, hehe."
    scene w2_5211 with dissolve
    mina "C'mere you!"
    sora "You don't have to- it's embarrass-"
    scene w2_5212 with dissolve
    "His protests were stifled by the power of Mina's hug."
    mina "Hey, dorkus!"
    mct "(A terrifying foe...)"
    sora "Hey, sis..."
    scene w2_5213 with dissolve
    mina "What are you guys doing just standing outside?"
    sora "Waiting for you."
    scene w2_5214 with dissolve
    mina "Eh? Why didn't you go inside? Is it that you can't have fun without little' ol' meeeee?"
    "Mina's over-exuberance was in stark contrast to yesterday's revelation. She wore it well, but it still felt..."
    mct "(Fake.)"
    scene w2_5215 with dissolve
    sora "Yesh, tone it down. People are going to think you're weird."
    mina "I'm excited to spend some time with my little brother!"
    sora "...don't forget [mcf]."
    scene w2_5216 with dissolve
    mina "Uh huh..."
    scene w2_5217 with dissolve
    mina "{b}And{/b} [mcf] too."
    scene w2_5216 with dissolve
    mct "(What's with that expression...?)"
    stop ambient fadeout 3.0
    stop music fadeout 3.0
    scene black with fade
    mc "Come on, let's go inside."
    scene w2_5218 with fade
    "The inside of the arcade smelled as stale as the decor was abundantly gaudy."
    "Numerous game machines dotted the walls and filled the floor space, far outnumbering players and giving us the pick of the place."
    play music "music/dog-park.ogg"
    scene w2_5219 with dissolve
    mc "So... you doing okay?"
    scene w2_5220 with dissolve
    mina "Yep! Just peachy!"
    scene w2_5221 with dissolve
    "Mina let her gaze linger on me, holding the awkward pose."
    "The way she wrinkled her shoulders and shifted her weight seemed to purposefully invite my eyeline down into the expansive valley of her chest."
    mc "Well... let's just focus on having fun today."
    "I wanted to caution her about overdoing it, but I feared popping her enthusiasm like an overinflated balloon."
    scene w2_5222 with dissolve
    mina "What should we play first~?"
    scene w2_5223 with dissolve
    mc "I'm just here for the company. You pick."
    scene w2_5224 with dissolve
    mina "Everything it is then, hehe!"
    "With a titter and a skip, Mina forged ahead and I soon followed."
    scene w2_5225 with wipeleft
    "......"
    "..."
    scene w2_5226 with hpunch
    mina "Ha! Got you!"
    sora "Stop being so loud..."
    scene w2_5227 with wiperight
    "......"
    "..."
    scene w2_5228 with dissolve
    mct "(Damn...)"
    "Utter defeat."
    scene w2_5229 with dissolve
    mina "Heh...!"
    "It started off rocky, but naturally, Mina was the lynchpin in the whole afternoon. Her enthusiasm was inescapably infectious."
    scene w2_5230 with fade
    "It quickly melted away my feeling of being a third wheel and thawed the awkward atmosphere between her brother and myself."
    sora "Oh! Uh, I don't really know any of those movies..."
    scene w2_5231 with dissolve
    mc "You {b}seriously{/b} haven't seen Samurai Cop?"
    mina "No, neither of us have seen your nerdy movies!"
    mc "Next time we hang out we've got to..."
    scene w2_5232 with dissolve
    mina "Ah, shoot! My last ball!"
    "The pair of them had a natural rhythm befitting siblings, but Mina did her utmost to draw me into the conversation and humor."
    scene w2_5233 with fade
    "What had been something I was doing simply because someone asked me to had become genuine fun."
    mina "You sure you want a rematch? There's all these other games."
    mc "C'mon, give me a shot."
    mina "Well..."
    scene w2_5234 with dissolve
    mina "Okay, but you've got to make it fun for me."
    mc "Are you proposing a bet?"
    mina "I mean, I've got to make it interesting for myself. Beating someone as sucky as you is SO boring."
    scene w2_5235 with dissolve
    mc "You...!"
    "The way she leaned into me and tugged at my arm made it a difficult proposition to refuse."
    mc "Fine. What are the terms?"
    scene w2_5236 with dissolve
    mina "Hm... good question. If I win, you give me a piggyback to my car."
    mc "What are you, a child?"
    scene w2_5237 with dissolve
    mina "Shut it. That's what I want."
    mina "If you win... let's just call it a tee-bee-dee eye-oh-you?"
    scene w2_5238 with dissolve
    mc "A favor?"
    mina "Yeah, a {b}favor{/b}. Open ended."
    scene w2_5239 with dissolve
    mina "Don't bother putting too much thought into it. You're not going to win."
    scene w2_5240 with dissolve
    "I could tell Mina delighted in showing her teeth."
    scene w2_5241 with dissolve
    mc "Alright. Bet."
    scene w2_5242 with dissolve
    "Why not? For the most likely outcome. A piggyback wasn't such a big deal."
    scene w2_5243 with dissolve
    mina "Hehe... bet!"
    mina "However, first..."
    scene w2_5244 with dissolve
    mina "UDB is finally free! Thought those hogs would never get off of it!"
    scene w2_5245 with dissolve
    "Setting our bet aside for later, Mina headed toward the vacant center piece of this dingy arcade, leaving Sora and I alone."
    scene w2_5246 with dissolve
    mct "(Hmm... I could...)"
    "Beating Mina at her own game would prove improbable. I only managed to take a single round yesterday. "
    scene w2_5247 with dissolve
    "The only chance I would have of winning the bet would be..."
    hide screen textbox2 with dissolve

    menu:
        "Enlist Sora's help in distracting Mina during your bet.":
            $ w2MinaDistract = True
            scene w2_5271 with dissolve
            show screen textbox2 with dissolve
            mc "Hey, kid. How'd you like to help me take your sister down a peg?"
            scene w2_5272 with dissolve
            sora "Are you talking about winning that stupid bet you just made?"
            scene w2_5273 with dissolve
            mc "Yeah, that one. I don't have a snowball's chance in hell of winning."
            scene w2_5272 with dissolve
            sora "Then why did you agree to it?"
            scene w2_5274 with dissolve
            mc "Because... where there's a will there's a Sora?"
            scene w2_5272 with dissolve
            sora "You sure it wasn't because she was all over you?"
            scene w2_5275 with dissolve
            mc "What? She's just the touchy-feely type."
            scene w2_5276 with dissolve
            sora "Not really. She's being weird today."
            scene w2_5277 with dissolve
            "He noticed that too."
            scene w2_5276 with dissolve
            sora "What's in it for me and what do you want me to do?"
            scene w2_5278 with dissolve
            mc "Just distract her somehow when we play and I'll give you twenty bucks and the potential of stopping your sister's tyranny."
            scene w2_5279 with dissolve
            sora "Well... it would be fun to see her face if she loses."
            sora "I've never beaten her either."
            scene w2_5280 with dissolve
            mc "It's a deal."
            "I don't think Mina would mind too much. She did want us to get to know each other and what better way to do that than a conspiracy?"
        "Play fair.":


            show screen textbox2 with dissolve
            "Nah. What's the point of winning if you don't play fair?"
            scene w2_5280 with dissolve
            mc "Want to join your sis on the dance pad?"

    scene w2_5604 with dissolve
    sora "You any good at UDB?"
    mc "No, I was... more into shooters as a kid."
    sora "Me too..."
    scene w2_5605 with dissolve
    sora "Ah..."
    scene w2_5606 with dissolve
    sora "Hey, pick Belariel if my sister picks Phaendar."
    scene w2_5607 with dissolve
    mc "Belariel?"
    scene w2_5608 with dissolve
    sora "She's the big tidd- ...she's the large succubus lady. Her main doesn't fare well against ranged pokes."
    sora "It won't be an automatic win, but you'll get some free damage in that way."
    scene w2_5609 with dissolve
    mc "Noted. Thanks for the advice, teacher."
    scene w2_5610 with dissolve
    sora "No problem."
    scene w2_5611 with dissolve
    sora "Let's trade picking the song this time!"
    stop music fadeout 3.0
    scene black with fade
    "......"
    "..."
    play music "music/higher-octane.ogg"
    scene w2_5612 with dissolve
    mct "(--!)"
    mct "(I took the first round...?)"
    "It was close, but a lot of unpredictable mashing coupled with Sora's advice let me eke out a round."
    mct "(That or...)"
    scene w2_5613 with dissolve
    mina "Don't get cocky, that was a fluke."
    scene w2_5614 with dissolve
    mct "(...did she sandbag?)"
    "I got my answer in the second round."
    $ renpy.music.set_volume(.3, 0, channel = "music")
    hide screen textbox2 with dissolve
    play sound "sound effects/big-explosion.mp3"
    scene w2_5679 with w19
    pause
    play sound "sound effects/metal-drop.wav"
    scene w2_5684 with hpunch
    pause
    play sound "sound effects/big-explosion.mp3"
    scene w2_5679 with vpunch
    pause
    play sound "sound effects/thud-heavy.wav"
    scene w2_5687 with hpunch
    pause
    play sound "sound effects/thud-heavy.wav"
    scene w2_5685 with vpunch
    pause
    play sound "sound effects/thud-heavy.wav"
    scene w2_5686 with hpunch
    show r3ov10 with dissolve
    show screen textbox2 with dissolve
    "She quickly adapted to my braindead strategy of spamming fireballs, nearly landing a perfect on me in a demoralizing defeat."
    scene w2_5615 with dissolve
    mina "Heh, heh~ toooold you~"

    if w2MinaDistract == True:
        scene w2_5616 with dissolve
        "In either round, nary a peep from Sora in distracting Mina."
        mct "(I'm going to want my money back, punk...)"
        scene w2_5617 with dissolve
        sora "Heh..."

    scene w2_5618 with dissolve
    mc "Guess it comes down to the wire?"
    scene w2_5619 with dissolve
    mina "Ohohoho, does it look that way to you?"
    scene w2_5678 with pixellate
    show r3ov1 with dissolve
    "Round 3... Start!"
    hide screen textbox2 with dissolve

    menu:
        "Keep your distance and exploit your ranged attacks.":
            $ w2FightBranch = 1
            "I should open by playing my advantage, keeping Mina at a distance and getting a life lead with some chip damage."
            play sound "sound effects/big-explosion.mp3"
            scene w2_5679 with hpunch
            "*Pfweeh!*"
            "Mina, who was slow on the draw, failed to bridge the gap between us and got stuck blocking my incoming fireballs."
            play sound "sound effects/big-explosion.mp3"
            with hpunch
            "*Pfweeh!* *Pfweeh!*"
            "She used the time between inputs to gradually advance, but each time she blocked she took a sliver of damage."
            play sound "sound effects/big-explosion.mp3"
            with hpunch
            "*Pfweeh!* *Pfweeh!* *Pfweeh!*"
            scene w2_5614 with pixellate
            mct "(It may not amount to much, but every little bit of damage counts!)"
            "I was ahead in health, but now she had me cornered..."
            mina "You really just going stand there like that?"
        "Rush in and use a command grab to take her by surprise.":

            "Just like I did in round 1 and round 2, she'll no doubt expect me to spam fireballs. Instead..."
            play sound "sound effects/grab-chime.wav"
            scene w2_5688 with vpunch
            mct "(I'll take her by surprise!)"
            mct "(Yes, I...)"
            play sound "sound effects/punch.wav"
            scene w2_5687 with hpunch
            "--Shit!"
            play sound "sound effects/thud-heavy.wav"
            scene w2_5685 with vpunch
            "I had successfully made my grab, but my options up close were limited and I made myself vulnerable to Mina's counterattack."
            scene w2_5614 with pixellate
            "Now she had me cornered..."
            scene w2_5613 with dissolve
            mina "Ha, now...!"

    play sound "sound effects/metal-crash.mp3"
    scene w2_5679 with pixellate
    "Through dumb luck, I mashed my way out of the mix-up, pushing her back, and avoided her pressuring me."
    play sound "sound effects/big-explosion.mp3"
    scene w2_5681 with hpunch

    if w2FightBranch == 1:
        show r3ov2 with dissolve
    else:
        show r3ov3 with dissolve

    "However, unsure of my options, I dumbly began lobbing more fireballs. Naturally, she blocked, but this time Mina's character spent some meter and shifted into a strange stance."
    "Strangely, the blow also charged her meter, but I was only slightly behind in that aspect. Maybe I could top off my meter with this spam and hit my special while she's focused on blocking..."


    menu:
        "Keep charging!":
            mct "(Yeah, if we both played that game, I'll come out ahead...)"
            play sound "sound effects/big-explosion.mp3"
            with hpunch
            "...or so I thought."
            play sound "sound effects/thunder-crack.mp3"
            scene w2_5683 with hpunch
            "To my shock, my second fireball completely filled her meter and she instantly spent it on a devastating counter."
            play sound "sound effects/thud-heavy.wav"
            scene w2_5685 with vpunch
            "Spending what was left of her meter to dash forward, she then put me in the same soul-crushing combo she finished me off with in round 2."
            play sound "sound effects/thud-heavy.wav"
            stop music fadeout 3.0
            scene w2_5686 with hpunch
            show r3ov4 with dissolve
            mc "Shit, it's..."
            scene w2_5620 with dissolve
            mina "Ha!"
            mct "(It's over.)"
            scene w2_5621 with dissolve
            play music "music/ukulele-fun.ogg"
            mina "Good game!"
            scene w2_5622 with dissolve
            mc "Yeah, it was..."
            "I had made a critical mistake, and it was frustrating, but I had no hope in the first place."
            scene w2_5623 with dissolve
            mc "Well, you win. Hop on?"
            mina "Not right now. You're going to carry me to my car remember?"
            sora "{size=-10}Why would you even ask for...{/size=-10}"
            scene w2_5624 with dissolve
            mc "What do you want to play next then?"
            sora "{size=-10}Yeesh, you're so blatant...{/size=-10}"
            mc "Best two out of three?"
            mina "You two can play if you want."
            jump w2ArcadeSora
        "Rush her down and grab her!":

            play sound "sound effects/grab-chime.wav"
            scene w2_5688 with wipeleft
            "Now's the time to dash forward, grab her, and force her into a mix-up. Mina's far better than me, so the only way I can win is by getting her to guess wrong."
            play sound "sound effects/metal-crash.mp3"
            scene w2_5679 with hpunch
            "It was a dangerous game. I was surprisingly coming out ahead in our exchanges, but I didn't know any combos to capitalize on a successful blow, while Mina did."
            play sound "sound effects/big-explosion.mp3"
            with hpunch
            "There was always the threat that I'd overextend with some slow move and Mina would use that as an opening to put me in that same devastating combo she used to finish me in round 2."
            play sound "sound effects/big-explosion.mp3"
            scene w2_5681 with hpunch

            if w2FightBranch == 1:
                show r3ov5 with dissolve
            else:
                show r3ov6 with dissolve

            mct "(Nice, my meter is fully charged... I can...)"
            "Mina abruptly spent her meter, partially expending it and entering into a strange stance that charged herself with every blow I landed."

    "This feels like a critical moment."


    menu:
        "Stop attacking and block what is coming.":
            "I got to block what's coming...!"
            play sound "sound effects/thunder-crack.mp3"
            scene w2_5683 with hpunch
            "--it was unblockable. She instantly hit some big, flashy attack that hit half the screen."
            play sound "sound effects/thud-heavy.wav"
            scene w2_5685 with vpunch
            "Spending what was left of her meter to dash forward, she then put me in that tried and true combo I had already seen."
            play sound "sound effects/thud-heavy.wav"
            scene w2_5686 with hpunch
            show r3ov8 with dissolve
            stop music fadeout 3.0
            mc "Shit, it's..."
            scene w2_5620 with dissolve
            show screen textbox2 with dissolve
            mina "Ha!"
            mct "(It's over.)"
            play music "music/ukulele-fun.ogg"
            scene w2_5621 with dissolve
            mina "Good game!"
            scene w2_5622 with dissolve
            mc "Yeah, it was..."
            "I had made a critical mistake, and it was frustrating, but I had no hope in the first place."
            scene w2_5623 with dissolve
            mc "Well, you win. Hop on?"
            mina "Not right now. You're going to carry me to my car remember?"
            sora "{size=-10}Why would you even ask for...{/size=-10}"
            scene w2_5624 with dissolve
            mc "What do you want to play next then?"
            sora "{size=-10}Yeesh, you're so blatant...{/size=-10}"
            mc "Best two out of three?"
            mina "You two can play if you want."
            jump w2ArcadeSora
        "Mash that special button and pray!":

            "Whatever. I'm charged and it's likely she hasn't noticed it yet."
            "Once she does, and she's looking out for it, it will become useless since I don't know any setups to safely deploy it. Catching her unaware in this moment is exactly..."
            play sound "sound effects/thunder-crack.mp3"
            scene w2_5682 with hpunch
            with flash
            "I didn't even know the range on the thing, but it worked!"
            "Mina reflexively blocked, but to no avail. The blast filled the entire screen and did HUGE damage."

    "That may have eaten most of her health bar, but it was not yet over. A few more hits were all I needed, but the only way I would successfully land those would be by getting in her face and making her guess again."
    "She was waaaaay better than me, but with a lot of luck, I might just win..."
    scene w2_5625 with pixellate
    mct "(... wait, why do I even care this much about winning?)"
    "I'm more childish than I give myself credit for."

    if w2MinaDistract == True:
        $ w2MinaBetWin = True
        scene w2_5626 with dissolve
        sora "Hey, Mina... did you hear Mom is talking to Richard again?"
        scene w2_5627 with dissolve
        mina "W-wait, what?! Are things not going well with-"
        scene w2_5678 with pixellate
        "That little snot waited for the critical moment!"
        play sound "sound effects/grab-chime.wav"
        scene w2_5688 with vpunch
        "For a second, Mina's attention was fully focused on her brother, which condensed needing a lot of luck into something more likely."
        play sound "sound effects/big-explosion.mp3"
        scene w2_5680 with hpunch
        show r3ov7 with dissolve
        "...just a little bit of luck."
        stop music fadeout 3.0
        scene w2_5628 with pixellate
        mina "E-h, s-shoot!"
        mct "(I won!)"
        sora "Oh yeah, it was just some stuff about alimony though."
        sora "It's not what you're thinking!"
        scene w2_5629 with dissolve
        mina "......"
        mina "..."
        scene w2_5630 with dissolve
        mina "Heh..."
        play music "music/ukulele-fun.ogg"
        scene w2_5631 with dissolve
        mina "Good game, [mcf]!"
        mina "Hehe, you got me!"
        mc "It was just dumb luck."
        scene w2_5632 with dissolve
        mina "Yeah... \"dumb\" luck, huh?"
        mina "Well, you win the bet. What would you ask of me?"
        scene w2_5633 with dissolve
        mina "Could I interest you in a shoulder massage?"
        "That was tempting, especially with the funny look on her face."
        scene w2_5634 with dissolve
        mc "There's no expiration date on our deal."
        scene w2_5633 with dissolve
        mina "Yeah, no rush."
        jump w2ArcadeSora
    else:

        play sound "sound effects/thud-heavy.wav"
        scene w2_5685 with pixellate
        "Damn."
        stop music fadeout 3.0
        scene w2_5686 with hpunch
        show r3ov9 with dissolve
        play sound "sound effects/punch.wav"
        "Well, I made her guess and she read me like a book. I was lucky to get this far, but there's no advantage like experience."
        scene w2_5620 with pixellate
        mina "Ha!"
        play music "music/ukulele-fun.ogg"
        scene w2_5621 with dissolve
        mina "Good game!"
        scene w2_5622 with dissolve
        mc "Yeah, it was..."
        "I had come so close to winning, and it was frustrating, but the match was really fun."
        "I had never used my brain that much when playing a fighting game."
        scene w2_5623 with dissolve
        mc "Well, you win. Hop on?"
        mina "Not right now. You're going to carry me to my car remember?"
        sora "{size=-10}Why would you ask for...{/size=-10}"
        scene w2_5624 with dissolve
        mc "What do you want to play next then?"
        sora "{size=-10}Yeesh, you're so blatant...{/size=-10}"
        mc "Best two out of three?"
        mina "You two can play if you want."
        jump w2ArcadeSora


label w2ArcadeSora:

    scene w2_5635 with dissolve
    show screen textbox2 with dissolve
    mina "I need to use the little girls' room."
    "With her standard pep, she turned and bounded toward the restrooms, leaving Sora and I alone."
    scene w2_5636 with dissolve
    mc "...so you want to play?"
    scene w2_5637 with dissolve
    sora "Eh, not really. I'm kind of sick of that game."
    scene w2_5638 with dissolve
    sora "Like really, {b}really{/b} sick of it."
    scene w2_5639 with dissolve
    "......"
    "..."
    scene w2_5640 with dissolve
    mc "...that black eye cleared up nicely."
    sora "Y-yeah, it wasn't so bad."
    scene w2_5641 with dissolve
    mc "You get a lot of those?"
    sora "No... it was the first time actually. I got too..."
    scene w2_5642 with dissolve
    sora "...ah, nothing. The UBD machine is still free, let's..."
    scene w2_5643 with dissolve
    mc "Too what?"
    scene w2_5644 with dissolve
    sora "..."
    scene w2_5645 with dissolve
    mc "Sorry."
    sora "It's okay. Did my sister put you up to this?"
    scene w2_5646 with dissolve
    mc "Not at all. I'm just being nosy."
    scene w2_5647 with dissolve
    sora "...there's this asshole I know from school. It's not a big deal, but he likes to run his mouth."
    scene w2_5646 with dissolve
    mc "It's a pretty big deal if he hit you."
    scene w2_5648 with dissolve
    sora "Everyone just ignores him and it's usually fine, I just got too angry the other day."
    scene w2_5646 with dissolve
    mc "Classes are out for summer, aren't they?"
    scene w2_5647 with dissolve
    sora "We take the same prep course during the summer."
    scene w2_5646 with dissolve
    mc "You take your education that seriously to give up your summers like that?"
    scene w2_5648 with dissolve
    sora "Mom does, although she never gave a crap how Mina did in school..."
    scene w2_5646 with dissolve
    mc "That kinda fits the picture that Mina painted of your Mom."
    scene w2_5649 with dissolve
    sora "Are... you two close like that?"
    scene w2_5650 with dissolve
    mc "Eh, your sister is just an open person I guess."
    scene w2_5651 with dissolve
    sora "She's actually not at all."
    scene w2_5652 with dissolve
    mc "..."
    scene w2_5653 with dissolve
    mc "Anyway, sorry for prying."
    scene w2_5654 with dissolve
    sora "It's okay. You're cool."
    scene w2_5653 with dissolve
    mc "In my experience, adults usually don't take kids' problems very seriously until it becomes a problem for them."
    scene w2_5654 with dissolve
    "I decided not to beat around the bush with my thoughts."
    sora "I'd rather just not draw attention to it."
    "I don't even know what advice I was dumbly offering just now. What might help in one circumstance, could just escalate and make another worse."
    "People only cared when one of Ian's bullies got their head split open - that's when the teachers began checking up on him and making sure there were no more problems."
    mct "(Which is in no way good advice.)"
    scene w2_5653 with dissolve
    mc "I know it can be hard to, but if ignoring him works like you say it does, just go back to doing that."
    scene w2_5655 with dissolve
    mc "If he assaults you again..."
    scene w2_5656 with dissolve
    mc "{b}You{/b} need to openly take it seriously before anyone else will."
    scene w2_5657 with dissolve
    sora "Sure, alright. Can we play something now?"
    mc "Sure, let's just go back to getting my ass handed to me by a teenager."
    mc "Just pick a machine."
    stop music fadeout 3.0
    scene black with fade
    if w2MinaDistract == True and w2MinaBetWin == False:
        mct "(Oh, and give me my twenty bucks back you dweeb!)"
    "......"
    "..."
    play ambient "sound effects/city-night.wav"
    scene w2_5658 with circlewipe
    mina "You guys seemed kinda chummy after I got back. What did you two talk about?"
    mc "Nothing really. He just told me some embarrassing stories from your past."
    scene w2_5659 with dissolve
    mina "Oh, he did, did he?"
    scene w2_5660 with dissolve
    mina "Well, it's probably nothing compared to what Ian has told me about you."
    scene w2_5661 with dissolve
    mc "You KEEP saying that, but... what stories has he told you, exactly?"
    scene w2_5662 with dissolve
    mina "Oh... just about {b}everything{/b} I reckon."
    scene w2_5663 with dissolve
    mina "Hehe~ no, for real. Thanks for coming today."
    mina "Sora needs to get used to socializing with someone other than Mom, me, and his two nerdy friends."
    scene w2_5664 with dissolve
    mc "It's been years since I've been to an arcade."
    scene w2_5665 with dissolve
    mina "Well, what do you want to do next?"
    "Mina moved closer and gave me a playful poke with her elbow."
    scene w2_5666 with dissolve
    mc "You had something you wanted me to help you with, right?"
    scene w2_5667 with dissolve
    mina "Uh huh. So... want to head to my place?"
    scene w2_5668 with dissolve
    "Awfully closer still."

    if w2MinaBetWin == False:
        $ Mina_Affection += 1
        scene w2_5670 with dissolve
        mc "Hop on."
        mina "Eh?"
        mc "You don't think I forgot about our bet, do you?"
        scene w2_5671 with dissolve
        mina "Not going to be embarrassed lugging me down the street?"
        mc "Hurry up. You gonna get on or not?"
        scene w2_5677 with dissolve
        mina "Well, then..."
        mina "Excuse me."
        scene w2_5672 with fade
        "She was as light and soft as expected."
        scene w2_5673 with dissolve
        mina "You smell nice."
        scene w2_5674 with dissolve
        "It was weird, but in a way, this felt more intimate than anything we had done during her rehearsal."
        "The way her limbs hugged my body was oddly... carnal."
        scene w2_5675 with dissolve
        mc "Where are you parked?"
        scene w2_5676 with dissolve
        mina "That way, driver."
    else:
        scene w2_5669 with dissolve
        mc "Where are you parked?"

    stop ambient fadeout 3.0
    scene black with fade
    "......"
    "..."

label w2MinaBucketList:

    play sound "sound effects/door-open.wav"
    scene w2_5248 with circlewipe
    "The way up to Mina's apartment was quiet. The blonde seemed anxiously preoccupied with something, but she kept close to me, stealing furtive glances and leading me by the arm to our destination."
    scene w2_5249 with dissolve
    mina "B'waaah...!"
    mina "Home, sweet home!"
    mina "The outside world can be so freakin' exhausting."
    "Despite her relieved outburst, she looked no less weary."
    scene w2_5250 with dissolve
    mc "You're either more introverted than you let on or you overdid it today by pretending everything is chipper."
    play music "music/devious-little-smile.ogg"
    scene w2_5251 with dissolve
    mina "Hehe... guilty on both counts, officer."
    scene w2_5252 with dissolve
    mina "Putting on a face can be oh so tiring, but..."
    scene w2_5253 with dissolve
    "She moved so close that I could feel the heat of her breath as she presented herself to me."
    scene w2_5254 with dissolve
    mina "I'm glad you're here right now."
    scene w2_5253 with dissolve
    "Something was arresting about her vast green eyes..."
    scene w2_5255 with dissolve
    mc "We're friends, Mina. Please, for the love of God, stop bringing up how appreciative you are."
    scene w2_5256 with dissolve
    mina "Hmm..."
    scene w2_5257 with dissolve
    mina "Nah. I don't think I will."
    scene w2_5258 with dissolve
    mina "Would you like a glass of water?"
    mc "No, thank you."
    scene w2_5259 with dissolve
    mc "You know, I've been pretty curious about what you need help with."
    scene w2_5260 with dissolve
    mc "Did you actually make a list?"
    scene w2_5261 with dissolve
    mina "Uh huh. Handwritten no less, on a piece of paper. Pretty dorky, huh?"
    scene w2_5260 with dissolve
    mc "Can I see it?"
    scene w2_5261 with dissolve
    mina "Ah, well..."
    scene w2_5262 with dissolve
    "*Glug, glug, glug.*"
    scene w2_5263 with dissolve
    "*Glug, glug, glug... glug, glug, glug.*"
    scene w2_5264 with dissolve
    mina "F'wah...! Later, I promise!"
    scene w2_5265 with dissolve
    mina "{size=-10}If item number one is a success...{/size=-10}"
    scene w2_5266 with dissolve
    mc "What was that?"
    scene w2_5267 with dissolve
    mina "Nothing. Just talking to myself like a complete weirdo!"
    scene w2_5268 with dissolve
    mc "I do that myself sometimes."
    scene w2_5269 with dissolve
    mina "...what about food?"
    mc "Stop playing the good host and sit down."
    scene w2_5270 with dissolve
    mina "Ah... okay."
    mina "Let's... talk then."
    scene w2_5281 with fade
    "Mina popped a squat closer than she needed, but I wasn't going to complain. She smelled nice and the warmth of her body was a pleasant contrast to the air-conditioned apartment."
    scene w2_5282 with dissolve
    mina "Yeah... so... talk..."
    scene w2_5283 with dissolve
    mc "What would you like to talk about?"
    scene w2_5284 with dissolve
    mina "Mmmh..."
    "She looked like she had something to say, but hesitated to say it."
    scene w2_5285 with dissolve
    mina "How 'bout them Yankees?"
    scene w2_5286 with dissolve
    mc "I don't know football."
    scene w2_5287 with dissolve
    mina "Pfft...! Ha! Me either, but I know more than you!"
    hide screen textbox2 with dissolve

    menu:
        "Bully her head in turn.":
            scene w2_5288 with dissolve
            mc "Just full of giggles, aren't you?"
            "I put some force into my palm and used the tips of my fingers to dig in, shake, and ruffle the tresses of the blonde's hair."
            scene w2_5289 with dissolve
            mina "'Ey... ha..! Stop, stop, stop! You're messing up my hair! Pft..."
            "I didn't stop."
            scene w2_5290 with dissolve
            mina "Fwhaha-ha! They're a baseball team, idiot!"
            scene w2_5288 with dissolve
            mc "Okay, fine! I don't know baseball either."
        "Ask what's so funny.":

            scene w2_5286 with dissolve
            mc "What's so funny?"
            scene w2_5285 with dissolve
            mina "They're a baseball team."
            scene w2_5286 with dissolve
            "Oh."
            scene w2_5287 with dissolve
            mina "Fwahaha-ha!"
            mc "Okay, fine! I don't know baseball either."

    scene w2_5291 with dissolve
    show screen textbox2 with dissolve
    "Once Mina's contagious tittering died down, and I was no longer fighting back my own, the atmosphere suddenly got a whole lot more comfortable."
    scene w2_5292 with dissolve
    mina "[mcf]..."
    "She looked at me with a purpose, pulling my attention undertow with those same beguiling green eyes as earlier."
    scene w2_5293 with dissolve
    mc "Yeah, Mina...?"
    scene w2_5292 with dissolve
    mina "Am I really not enough? Would you..."
    mina "Would you date a woman like me?"
    scene w2_5294 with dissolve
    mc "Stop there. Anyone should be so lucky."
    "The hurt in her voice left me with no hesitation, lest she doubted my answer."
    scene w2_5295 with dissolve
    mina "I'm not asking anyone. I'm asking [mcf]."
    scene w2_5296 with dissolve
    mc "Mina... you're warm, vibrant, and thoughtful. The thought you put into my birthday gift alone is evidence of that last trait."
    scene w2_5297 with dissolve
    mc "On top of that, you're open, generous, and you know how to make people feel included - and not to dance around it, but you're drop-dead gorgeous."
    scene w2_5298 with dissolve
    mc "Why the hell would you even doubt that? I should be so lucky under another circumstance."
    scene w2_5299 with dissolve
    "It was a bit heavy-handed, but I wanted to put her unease to rest. There wasn't anything wrong with her after all. It was my friend who was dysfunctional."
    scene w2_5300 with dissolve
    mina "You could've just said yes, dummy."
    hide screen textbox2 with dissolve
    scene w2_5301 with dissolve
    mc "Hey Mina, you're a bit..."
    "The distance between the two of us had shrunk and now Mina's lips were perilously perched underneath mine, glossed over with lip balm and inviting me to cross the line."
    scene w2_5302 with dissolve
    "All day she had been sending me flagrant signals so clear that you could guide an airplane safely down with them, but that was all it was. Signals."
    "Now, our bodies overlapping and with her leering up at me longingly, she was daring me to make a move."

    menu:
        "Cross the line."(chg=["mina_killian_down3","mina_up4"]):
            $ minaCheat = True
            $ Mina_Affection += 4
            $ Mina_KLove -= 3
            scene minalr_kiss_a with dissolve
            show minalr_kiss
            mina "Mmmm...!"
            "As our lips met, all the tension in the blonde's body evaporated. She wasn't surprised by the kiss."
            "This {b}was{/b} the result that she expected."
            mina "Fwha~"
            "It wasn't like me to be so impulsive and maybe I was ultimately no different than Ian, but this was my choice. "
            "The choice to yield to what those expansive green eyes dredged out of me."
            mct "(Still, if my friend ever found out...)"
            "Well, I doubt I'd get fired, but would it hurt him?"

            if killianHeadsUp == True:
                mct "(He DID ask for me to do him a favor and make sure she had fun today...)"
            else:
                "To be honest, I'm not even sure if that crazy bastard gives a fuck, but it remained a potential risk."

            $ renpy.music.set_volume(.05, 0, channel = "ambient")
            play ambient "sound effects/ringing-inbound.wav"
            "*Ring, ring*"
            "Ack! Stop thinking and just enjoy..."
            "*Ring, ring.*"
            scene w2_5303 with dissolve
            mina "H-huh? Oh, C-crap!"
            stop music fadeout 3.0
            scene w2_5304 with dissolve
            mina "I forgot! That's my brother calling to see if I got in alright!"
            mina "Be right back."
            scene w2_5305 with dissolve
            mc "......"
            mc "..."
            mct "(You've got to be fucking kidding me...)"
            "The moment our lips parted, that resolve went out the window and I started to feel weird about what I had just done."
            stop ambient
            scene w2_5306 with dissolve
            $ renpy.music.set_volume(1, 0, channel = "ambient")
            mina "Hey! Yeah, yeah...!"
            mina "No, I got in alright!"
            scene w2_5307 with dissolve
            mina "I told you [mcf] was coming back to my place. You didn't have to--"
            mina "I'm the big sister, y'know?"
            scene black with fade
            mct "(Oh, come on...)"
            jump w2MinaMindBlown
        "Even if they're bound to break up, that's still Ian's girlfriend."(chg=["mina_down4"]):

            $ Mina_Affection -=4
            stop music fadeout 3.0
            scene w2_5503 with dissolve
            mc "It's getting a little stuffy in here."
            scene w2_5504 with dissolve
            mina "..."
            scene w2_5505 with dissolve
            mina "O-oh... s-sorry."
            jump w2MinaLetDown

label w2MinaMindBlown:

    scene w2_5308 with wipeleft
    mina "What? No, he's not my new boyfr-- well, I don't think...ah!"
    mina "Listen, I'm home, okay? I'm going to hang up now, but thanks for checking up on me little brother!"
    scene w2_5309 with dissolve
    mina "Bye bye!"
    scene w2_5310 with dissolve
    mc "......"
    scene w2_5311 with dissolve
    mina "..."
    scene w2_5312 with dissolve
    mc "It's nice he's so protective of you."
    mina "Heh, I know, right...?"
    "Bereft of touch, the sexual tension that burned just moments before was now replaced by an empty awkwardness."
    scene w2_5313 with dissolve
    mc "Kinda... kinda poor timing though..."
    mina "Y-yeah..."
    scene w2_5314 with dissolve
    mina "Not so great with the timing..."
    mc "Oh yeah, what did you need help---"
    scene w2_5315 with dissolve
    mina "Aaah! My back's a bit sore."
    "She made a big, exaggerated movement in support of her claim."
    scene w2_5316 with dissolve
    mc "...really?"
    scene w2_5317 with dissolve
    mina "Yeah, all that dancing at the arcade I guess..."
    scene w2_5318 with dissolve
    mina "These things are killer and sometimes not in a good way..."
    scene w2_5319 with dissolve
    mc "I imagine they must be pretty heavy..."
    scene w2_5320 with dissolve
    mina "You have no idea... say... "
    scene w2_5321 with dissolve
    mina "D-do you want to feel how heavy they are?"
    scene w2_5322 with dissolve
    mct "(...ah!)"
    "She was getting things back on track in the wake of our interruption. It may have been an extremely dorky way of going about it, but somehow it felt perfect for the blonde in front of me."
    scene w2_5323 with dissolve
    mc "Yeah..."
    scene w2_5324 with dissolve
    "I waved Mina closer as my lecherous eyes fell on the bountiful mounds crammed in the wonderfully-too-small pink fabric of her blouse."
    mc "I guess I am pretty curious..."
    scene w2_5325 with dissolve
    "As the distance between us shrunk, so did the time for awkward reflection. Once more, Mina became my only focus."
    mct "(The abrupt change in décor wasn't without its perks...)"
    scene w2_5326 with dissolve
    "The light streaming in from the windows did make Mina all the more lovely."
    scene w2_5327 with dissolve
    mina "Ha..."
    "The anxious look on her face as I kept her waiting was a pleasure of its own."
    scene w2_5328 with dissolve
    "......"
    "...."
    scene w2_5329 with dissolve
    mina "What are you-"
    play music "music/ob1.ogg"
    scene minata_1_a with dissolve
    show minata_1
    mina "O-oh!"
    "Satisfied I had embarrassed the woman long enough, I gently cupped Mina's breasts from the side and easily filled my hands with her bust."
    "The jutting pair had incredible heft that fought tooth and nail against gravity, with a suppleness owed to age that simply couldn't be matched by the other older women in my life."
    mct "(Fuck, they look amazing in that shirt...)"
    "Pressing the pair together made for exquisite eye candy."
    mc "Are my hands cold?"
    "Her chest felt like it was on fire."
    mina "N-no, you're fine..."
    mc "I'm glad then."
    scene minata_2_a with dissolve
    show minata_2
    "The cut of Mina's blouse proved no match for even a minor assault. Even just gently working her breasts easily freed one of her puffy, rosy areolas from its bounds."
    "However, I don't think she noticed her exposure as..."
    mina "{b}Ha...!{/b}"
    "She seemed preoccupied with what was going on in her pretty head."
    "Light touches alone were extricating small whimpers of enjoyment from the blushing blonde."
    "Every exploratory caress caused her to fidget and hum."
    mina "Heut...!"
    mct "(Damn, she's responding better than Rosalind did during the exhibition...)"
    mina "Hat... ha..."
    scene w2_5330 with dissolve
    mc "Hm..."
    mina "S-so, yeah... what did you think? P-pretty uh... heavy, right?"
    mct "(Is her chest {i}really{/i} that sensitive?)"
    mina "[mcf]? S-say some--"
    scene minata_3_a with dissolve
    show minata_3
    "I would discern the truth."
    mina "H-hey w-wait...! W-what are you... ha...!"
    "My perverted curiosity had to know: was Mina truly as big of a simpering tit whore as Rose?"
    mina "Heut! T-tongue...!"
    "I set myself to task on a two-pronged attack."
    mina "This is... t-too... ah!"
    scene minata_4_a with dissolve
    show minata_4
    "With one hand, I roughly groped at her ass while rolling her nipple with my tongue."
    mina "I just said t-toooouch! This is t-towwwhoooo..!"
    "With the other, I teased and prodded the border of her areolas betwixt the edges of my fingers."
    "The semi-stiff buds had now turned to stone, causing the puffy towers to stand erect against the lashing of my tongue."
    mina "H-heut.. hat...!"
    "Engorged with blood as they were made them all the more sensitive, drawing even more soft moans from Mina's throat."
    scene minata_5_a with dissolve
    show minata_5
    "I continued on like this for minutes, prodding and licking at Mina's mammaries to my heart's content. For Mina's part, she submissively stood there, her body slowly tensing up like a coil."
    "Still... this wasn't enough."
    mina "Heut...! [mcf]..."
    "I wanted to see what an even stronger reaction would look like from the prim and proper actress."
    mina "Ssh-slow down..."
    "I wanted to cast her cute demeanor into the dirt and..."
    mina "M-my ch-chest is--"
    scene minata_6_a with dissolve
    show minata_6
    mina "E-eh...?!"
    mct "(See what kind of lewd expressions that adorable face of hers could make!)"
    "*Chwup...! Chwup...*"
    "The cheery blonde may have anticipated the kiss, but now she was utterly confounded."
    "*Fwhup, chwhuup!*"
    "Mina had been so forward earlier, but now she was on the back foot, bewildered by pleasure."
    mina "Ha...! H-heut...!"
    "{b}That{/b} confusion tasted like manna from heaven. Her baffled, pleasured cries fueled me to push on as I latched onto her left breast like a starving newborn."
    mina "Efwwwhe...!"
    "The way her chest heaved with arousal made forming a seal around the raised peaks a sporadic dance of push and pull."
    mina "A-ha..."
    "Every time she'd sharply breathe in, her nipple would flee the embrace of my mouth and I would give chase."
    mina "Ha..."
    "Every time she breathed out, the enflamed nub would smash against the bed of my tongue."
    mina "Heaut... haat-!"
    mct "(Fuck do I love tits!)"
    scene minata_7_a with dissolve
    show minata_7
    "*Chwup...! Chwup... fwhup!*"
    "Again, I toiled away for minute upon minute, savoring every inarticulate squeak and incomprehensible muttering."
    mina "Haat...♥ Heut...♥"
    "Where other women might have grown bored of the infantile attention by this point, the feeling of Mina's body going taut as the excitement built told me she was still on board."
    mina "Ha...♥"
    "Still, like before..."
    mina "Haat...♥"
    "Her sounds and bodily reactions were becoming routine and predictable."
    mina "Heaut... haat-♥"
    "It was time for another deviation in my attack."
    scene minata_8_a with dissolve
    show minata_8
    mina "Nngh-! Eh...♥ Euh?"
    "Switching targets, I moved my mouth over to her right breast and went {b}fucking ham on it{/b}."
    "*Chwup...! Fwhup...! Thwup...!*"
    "My own excitement was building. My cock painfully strained the denim of my jeans, a fact that was becoming increasingly hard to ignore."
    mina "Heut...! Ha...♥ Eaauh...♥"
    "Mina's servile complacency as her whorish moans bounced around her obnoxiously cute room set my mind awash in expletive-laden thoughts."
    mct "(Ah, fuck...! Shit!)"
    "My head swarmed with things I'd like to express to the babbling bitch if only my mouth wasn't otherwise occupied."
    mct "(Bitch!)"
    "Disparaging words that I wouldn't truly mean, but nevertheless wormed their way into my feeble, sex-addled, sadistic brain."
    scene minata_9_a with dissolve
    show minata_9
    mina "Fggg- oh, wwha-? Ehk...♥♥♥"
    "*Chwup...! Fwhup...! Thwup...!*"
    scene w2_5331 with pixellate
    "Soon the words were replaced with abstract vulgar images."
    scene w2_5332 with dissolve
    "Pornographic, depraved, decadent desires..."
    scene minata_9_a with pixellate
    show minata_9
    mina "Ha~♥♥♥ Haat...♥♥♥"
    "I wondered if she'd be disgusted with me if she knew, that given a chance in a void, the dirty things I'd love to do to her beautiful body."
    "That'd be the end of it I suspect."
    mina "Ha~♥♥♥ Haat...♥♥♥"
    "She wouldn't want to see me again if she knew the ugly images that lurked in the recesses of my mind, waiting patiently for my faculties to dull and my appetite to grow."
    "No, it wasn't the time for those kinds of thoughts. Mina was putting herself in my hands."
    mina "[mcf]...! Ffh- ah♥ Euuh-♥ Wa-wh-♥"
    "Until now, all of my partners had vastly more experience than I had. Now the shoe was on the other foot."
    "It was up to me to take care and reward the faith and trust she was putting in me."
    mina "Fr- for, rh-♥ Eal-?♥"
    "It was my duty to make it an experience she would enjoy. And to that end..."
    mina "Ayerm...♥ Bhhhh-b, Ohout♥ Twhooo♥ W-what...?"
    "Like a coil needing to be sprung, it was time to release her from the mounting tension. One last dramatic note to push her over the zenith by..."
    scene w2_5333 with dissolve
    mina "♥♥♥Niiiiiiiiiiiiiiii-♥~"
    "Suctioning as hard as I could and pulling myself off Mina's right breast with an exquisite..."
    play sound "sound effects/mouth-pop.wav"
    scene w2_5334 with dissolve
    "*POP!*"
    mina "Eyee...♥♥♥♥♥♥♥"
    scene w2_5335 with dissolve
    "...until all that potential force came to an equilibrium."
    mina "Haat, ha...!"
    mina "Ha..."
    scene w2_5336 with dissolve
    mina "Ha... ha..."
    mina "What the heck... t-that was... never..."
    scene w2_5337 with dissolve
    mc "Mina..."
    mina "Y-yeah...?"
    scene w2_5338 with dissolve
    "Chwup...!"
    scene w2_5339 with dissolve
    mc "I'm..."
    scene w2_5340 with dissolve
    mc "I'm going to continue."
    mina "That's...!"
    scene w2_5341 with dissolve
    "She nodded."
    scene w2_5342 with dissolve
    mina "Okay... just give me a second to catch my breath--"
    scene w2_5343 with dissolve
    mina "Mmmh...!"
    "Give her a second? As if. There was something about Mina that made me want to bully her."
    scene minarubdub1_a with dissolve
    show minarubdub1
    "Cutting her off with a kiss, I began rubbing the flustered actress' nether region through the thin denim fabric of her jeans."
    "Mina freely offered up her mouth without restraint, allowing my tongue access to probe it to my satisfaction."
    mina "Mmm..."
    "Our tongues snaked around each other, clumsily coiling and unwinding. The lack of shared rhythm was novel in its own way, like two young lovers desperately fumbling around in the dark."
    "Covered as it was, her sex radiated a clammy heat that warmed the palm of my hand. The more I pressed, the damper the material got."
    "Naturally, my efforts were dulled by the denim, but I wasn't going to rush things."
    "I would take my time, just as I had done with her chest. I would have Mina's eyes cloud over with want before I unwrapped the prize."
    "*Chwup, fwhup...!*"
    "The kiss carried on for another minute or so, until a heady feeling came over me and the inside of my skull felt like it was filled with hot air."
    mina "Mh...♥"
    "Mina's own head must have been similarly vacant, as the bumbling movements of her tongue had laxed and it was I now leading our dance."
    scene w2_5344 with dissolve
    mina "Fhwaaa~ ha, h-haaaa...♥"
    scene w2_5345 with dissolve
    mina "D-dang it, it was hard to breathe..."
    scene w2_5346 with dissolve
    mc "Breathing is the only thing you have to worry about right now. Leave everything else to me."
    scene minarubdub2_a with dissolve
    show minarubdub2
    mina "Atta-♥"
    "Mina's body worked with me, hips giving a cute little wiggle that followed the path of my rubbing."
    mina "Mh, ha...♥ Y-you're getting full of yourself..."
    "How could I not? Mina was out of my league. Hell, every woman in my life right now was out of my league, but Mina especially as..."
    mina "Haeut-"
    "She wasn't part of the club. Something about that felt refreshing."
    mina "Ha, haat-!"
    "Maybe she was just doing this to get back at Ian, but I felt certain that at this moment she was entirely present with me."
    scene minarubdub3_a with dissolve
    show minarubdub3
    mina "Tsk~ haat, ha...♥ C-come on, [mcf]..."
    mc "Come on what?"
    mina "D-don't..."
    mc "Don't what?"
    mina "Ne-no, no... don't you want to..."
    mina "D-don't y-you, ha...! D-don't you w-want to t-ouch me... {b}directly{/b}."
    mc "Touch what directly?"
    mina "Y-you know... haat!"
    scene w2_5347 with dissolve
    "Stopping what I was doing, I stood up and came face to face with the blonde."
    scene w2_5348 with dissolve
    mc "What do you want me to touch, Mina?"
    scene w2_5349 with dissolve
    mina "My... {b}pussy{/b}."
    scene w2_5350 with dissolve
    mina "I want you to directly touch my pussy."
    stop music fadeout 3.0
    scene w2_5351 with dissolve
    mc "I'll do you one better."
    scene black with fade
    mina "H-hey, oh! Don't sho--"
    mc "I told you, all you've got to worry about is breathing."
    scene w2_5352 with dissolve
    mina "Yeah, but it's embarrassing..."
    scene w2_5353 with dissolve
    mc "Should I not then? We can stop right now if it's too much for you."
    scene w2_5352 with dissolve
    mina "W-what... I-I, didn't say that..."
    scene w2_5353 with dissolve
    mc "Good. Because you've got a very pretty pussy and I'd like a taste."
    scene w2_5354 with dissolve
    mina "Shut up!"
    mina "J-just shut up and lick, idiot."
    play music "music/thunder.ogg"
    scene minacunni1_a with dissolve
    show minacunni1
    mina "*Schlick...!* Ah...!"
    "This reprieve was the last she would get. If she wasn't a blathering mess by the end of this, it would be my failure."
    "With that mission in mind, I set to task."
    mina "T-this...!"
    "First I tasted her outer folds, tracing my way up to the lovely pleasure bean that was already poking its head out of its hood."
    "I worked my way around the perimeter of her clitoris, teasing and prodding its outer limits while never quite directly touching the fleshy nub."
    "I hadn't even taken the plunge into her depths yet and my mouth was already full of the taste of sexual arousal."
    mina "Ha, haat...!"
    "Thick, slimy vaginal discharge generously coated my upper lip and I knew I would soon be drowning in it."
    "Having my fill of her outer parts, I then moved onto the next course: her suffocatingly clingy inner depths."
    scene minacunni2_a with dissolve
    show minacunni2
    "*Schlick..! Schlick...!*"
    "Slow and steadily I lapped at her insides, firmly dragging my tongue along the floor of her vagina."
    "The muscular tube did its best to cling to the foreign invader, but couldn't quite grab ahold of the slippery appendage."
    "In effect, the result was almost like a pleasant massage for my tongue."
    mina "Haeut, haa~ ha..."
    "Unable to directly ask her if it was good, I had to rely on Mina's involuntary reactions to guide my attack."
    "My focus was on the little things, like the way her thighs would momentarily squeeze together or the way her heels would dig into the back of my leg."
    "There was an intimacy in learning the peculiarities of Mina's body."
    mina "D-dang, ha...! Y-you're p-prehtty g-good at this..."
    "To be honest, it was more her than me."
    "Mina, it turned out, had quite the lewd body and talent for receiving pleasure. From her chest to her quim, even just a light effort wrenched a response from the wriggling beauty."
    mina "Ahhy...♥"
    scene minacunni3_a with dissolve
    show minacunni3
    "*Schlick..! Schlick...!*"
    mina "MMmh...♥ Haat...♥"
    "*Schlick..! Schlick...! Schlick!*"
    mina "Ack, t-tingly...! It's h-happening... s-seriously?"
    mina "It's h-happening again so soon...♥"
    mct "(Ha...!)"
    "As I strained my tongue by extending it as far as it could physically go, it seemed Mina was perched on the edge of sensual release."
    "Not that I needed her words to figure that out. No, her thighs firmly gripping my head were all the intimation I needed."
    mina "Ha...! Heeah...♥ Euht... ahht... euttss....♥"
    mina "Ehim, ggg-oiring, ttwo...♥"
    scene w2_5355 with flash
    mina "FRICK...!!!!!!!!!!"
    "Like a locomotive hurling down the tracks and piping hot steam, Mina loudly announced to the world her sexual peak."
    mina "Eeeh... yeah....♥♥♥♥"
    scene w2_5356 with flash
    mct "(Ack...!)"
    "While I had preciously survived the trap of Veronica's massive thighs, that didn't mean the way Mina locked her legs around my neck felt any less precarious in the moment."
    mc "*Cough... cough...!*"
    $ renpy.music.set_volume(.1, 3, channel = "music")
    play sound "sound effects/thud-floor.mp3"
    scene w2_5357 with vpunch
    "*Thud!*"
    mina "Ah... ack... euphg..."
    scene w2_5358 with dissolve
    mina "Ha... ha... w-ha... everything is so... s-soft and h-hazy... holy cow..."
    mina "Ha... Ha..."
    scene w2_5359 with dissolve
    mina "Ha... is it..."
    scene w2_5360 with dissolve
    mina "It's... y-your turn now, right? I should... make yhouuu fheel good t-tooo~♥"
    "Mina, in a delirious daze, moved her hand to my crotch as if on instinct."
    scene w2_5361 with dissolve
    mina "Ayeee... t-take it out... my f-fhingers are s-still..."
    scene w2_5362 with dissolve
    mc "No."
    "Not yet at least."
    mc "I'm not done yet."
    "At this moment, I wanted to focus on her pleasure. Twice wasn't enough."
    "I wasn't just satisfied turning her legs to jelly. I would carve the memory of me in her body."
    scene w2_5363 with dissolve
    mina "Ey... but I've already..."
    "I had a feeling that with Ian she wasn't used to being the focus of attention."
    scene w2_5364 with dissolve
    mc "Shirt. Off."
    "With a snap of my fingers, I made my demand."
    mct "(When did I become so bold?)"
    "Well, I guess it's true. Give a man an inch and he'll take a mile."
    scene w2_5365 with dissolve
    mina "Eyy... eh?"
    scene w2_5364 with dissolve
    mc "Take your shirt off."
    scene w2_5366 with dissolve
    mina "......"
    mina "..."
    "I watched the gears turn in her muddied orgasm-wracked brain until she finally parsed my directive."
    scene w2_5367 with dissolve
    mina "Oh, 'k-kay...!"
    scene w2_5368 with dissolve
    "Like a newly birthed fawn, Mina got up on shaky feet and reached for her shirt."
    scene w2_5369 with fade
    mc "Damn..."
    "Taken in unobstructed and up close, Mina's breasts were in a tier of their own."
    scene w2_5370 with dissolve
    mc "Turn around."
    scene w2_5369 with dissolve
    scene w2_5371 with dissolve
    scene w2_5369 with dissolve
    mina "..."
    scene w2_5372 with dissolve
    "With a simple nod, Mina once again did as I asked."
    scene w2_5373 with dissolve
    mc "Good girl..."
    scene w2_5374 with dissolve
    "*Fwup...!"
    scene w2_5375 with dissolve
    "*Fwup..., chup...!*"
    scene w2_5376 with dissolve
    "Slowly, I planted kisses along the curvature of the model's back."
    scene w2_5377 with dissolve
    mct "(Fuckin' beautiful...)"
    "It wasn't like I hadn't been appreciating it thus far, but being face to face with that slice of bubbly perfection was a new perspective altogether."
    mct "(Just a little...)"
    scene w2_5378 with dissolve
    play sound "sound effects/slap3.wav"
    scene w2_5379 with vpunch
    "*Smack*"
    mina "Yiii-"
    scene w2_5380 with dissolve
    "The tentative smack yielded a cutesy minuscule yip, more appropriate for a small poodle than a grown woman."
    "It took a mindful effort not to try and reproduce that sound, as the sadistic side of me envisioned repeatedly walloping her ass to indulge in every adorably sweet cry."
    scene w2_5381 with dissolve
    mc "Hmm..."
    scene w2_5382 with dissolve
    mina "Ooo-h!"
    $ renpy.music.set_volume(1, 3, channel = "music")
    scene minacunni4_a with dissolve
    show minacunni4
    "My tongue found its way back to Mina's genitals."
    mina "Eeeh... a-again...? L-like this?"
    mc "(Again. Like this.)"
    "*Schlick..! Schlick...! Schlick!*"
    mina "Haat...! This position is..."
    "In this new position, my tongue was able to reach an even deeper part of the blonde's sex."
    mina "Hhhyaaatt...♥ S-top, y-you're staring at my butthooole...!"
    mct "(Ah, you...!)"
    "I wondered... did she know that saying such ridiculously lewd things so cutely would just spur me on even more?"
    mina "Aee, I don't know if I can hold this p-position...!"
    "Mina, yet reeling from her previous orgasm, was already on shaky legs. The moment my tongue parted her lips made her uprightness even more tenuous."
    scene minacunni5_a with dissolve
    show minacunni5
    "To make sure she didn't fall and bust her face open, I steadied the blonde's posture by scooping up handfuls of her fat tits. Not an unpleasant way of playing a counter-balance..."
    mina "Ah...!"
    "*Schlick..! Schlick...!*"
    "Contrary to her concern about her butthole, Mina aided me in my goal by pushing her toned buttocks deep in my face and wearing me like a hat."
    mina "Haaa...!"
    "The shake and clap of Mina's callipygian ass was a powerful motivator, accelerating my tongue fucking and sporadically making me forget to even breathe."
    "*Schlick..! Schlick...! Schlick!*"
    mina "Gyeeeh... gyyy...♥"
    "Bent over as she was, gave me an entirely new dimension of intrusion."
    mina "Eyy... dhat's myy..."
    "Every so often, I'd withdraw my tongue from Mina's insides and work it around the rim of her asshole - never going so far as to penetrate it, but enough to make the blonde aware of my attentions despite her half-lidded stupor."
    mina "Ay, it's d-dirty...!"
    "*Schlick..! Schlick...!*"
    mina "Ha, haaat... Ha, haa... E-ym, I'm d-dirty!"
    "*Schlick..! Schlick...! Schlick!*"
    mina "Haeut...♥ Maasss...♥"
    "Two minutes of gorging myself on Mina's delectable cunt was all it took to once more bring her pleasure to a head."
    "*Schlick..! Schlick...!*"
    mina "Gyeeeh... gyyy...♥ I'm g-goinna f-fhall...?!"
    "*Schlick..! Schlick...! Schlick!*"
    mc "Mmmghottoyuu...!"
    "Mina's legs were comically clacking together by this point, threatening to give out and topple her over. Fortunately, my hold on her quivering body remained strong."
    mct "(...I hope, at least.)"
    mina "Gyy... eeh... ayeee...♥ T-thoughts... c-can't...♥"
    mina "T-thinkh...♥ I'm...♥ Eyy..."
    scene w2_5383 with flash
    with flash
    mina "Fffwwwhhgwwwww....♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥"
    "That was the fastest yet. I can't--"
    $ renpy.music.set_volume(.1, 3, channel = "music")
    scene w2_5384 with dissolve
    mct "(Oh, shit...!)"
    play sound "sound effects/thud-floor.mp3"
    scene w2_5385 with vpunch
    "*Thud*"
    "With a distinct thump, Mina crumpled into a pile of tongue-fucked blonde."
    mina "Heehh.... ooowuch... ha... ha..."
    scene w2_5386 with dissolve
    "The sight of the well-composed actress panting on the floor like a bitch was of such satisfaction that it felt like I had already fucked."
    mina "I can't... I can't... ha...♥"
    mct "(Hmm...)"
    scene w2_5387 with dissolve
    mina "Haat...♥ Whah...♥ Arr...♥"
    mina "...?"
    scene w2_5388 with dissolve
    mina "Ehhh..."
    "Once more."
    scene black with fade
    "*Schlick...!*"
    mina "Eh~oooh..."
    $ renpy.music.set_volume(1, 3, channel = "music")
    scene minacunni6_a with dissolve
    show minacunni6
    "*Schlick..! Schlick...!*"
    "At this junction, Mina was more or less where I had hoped to go from the start of this fun."
    mina "Eh... w-what? Mh-mercy..."
    "*Schlick..! Schlick...! Schlick!*"
    mina "Eyee... can't fheel myyy lehgs...!"
    "She had enjoyed back-to-back-to-back orgasms and all that was left of the warm and cheery blonde was the quivering mess crumpled face down on the bed, ass limply raised in obedience."
    mina "Haat... eeyhh...♥"
    scene minacunni8_a with dissolve
    show minacunni8
    mina "Eyts... ah...♥ Down't you wanna c-cum...?"
    "She was right. I was so turned on that even rubbing myself against the fabric of my jeans threatened to make a mess."
    mina "You... can... t-thake... your... dihk... ouut...!"
    "*Schlick..! Schlick...!*"
    "Even half-sensate, the caring blonde was thinking about her partner's enjoyment."
    "*Schlick..! Schlick...! Schlick!*"
    mina "..haaat, ng...♥"

    if Killian_Bromance >=18:
        "As much as I love Ian, I couldn't help but think \"what a fucking dumbass\" for the umpteenth time for letting a girl like Mina slip through his fingers."
    else:
        mct "(Ian's such a fucking dumbass for letting a girl like Mina slip through his fingers.)"

    "*Schlick..! Schlick...!*"
    mina "Gah... ng, ha...♥"
    scene minacunni7_a with dissolve
    show minacunni7
    "By now, Mina's pussy was positively swollen from the repeated sexual stimulation, flush and fat from the past fifteen minutes of unending service."
    "*Schlick..! Schlick...! Schlick!*"
    "Her lips parted effortlessly with every lap of my tongue and the roof of her vagina had expanded to eagerly accommodate the intrusion of a dick."
    mina "Ehha...♥"
    "Every flick of her overwrought nub caused Mina to jerk and squeak like an untied balloon."
    mina "Gyee...♥"
    "Worn out as she was, I still had to consciously steady her lower half to keep myself on track."
    scene minacunni8_a with dissolve
    show minacunni8
    "*Schlick..! Schlick...!*"
    mct "(That's right...)"
    "*Schlick..! Schlick...! Schlick!*"
    scene minacunni6_a with dissolve
    show minacunni6
    "She said she felt like a big question mark."
    mina "Ah...! Ah...!"
    "She said that it felt like she was watching something else live her life."
    scene minacunni7_a with dissolve
    show minacunni7
    mina "Gy...♥ Hat...!"
    mct "(Well, set aside your troubles, Mina. Just for half an hour.)"
    mina "Ha, hat...! Ah, y-you m-meanie...!"
    mct "(Forget about them.)"
    "*Schlick..! Schlick...!*"
    mina "Y-you're tryin' to k-kill me...!"
    "*Schlick..! Schlick...! Schlick!*"
    scene minacunni6_a with dissolve
    show minacunni6
    "Another few minutes of licking and my jaw was fucking sore and my tongue ached."
    mina "Ng... ~ha... ha~"
    "Mina had become less vocal, her explicit moans replaced by a near-persistent pleasured hum emanating from her tired vocal cords."
    mct "(Ah, maybe going for four orgasms was being too greedy?)"
    "She was still feeling pleasure, but dulled by it as she was, there was no tension."
    scene minacunni8_a with dissolve
    show minacunni8
    mina "{size=-10}Haa~ mh...♥ So...{/size=-10}"
    mina "So, so... ah... [mcf]... It f-feels different... like... ah~"
    mct "(Or at least it felt like there was no tension...)"
    scene minacunni9_a with dissolve
    show minacunni9
    "Guided by her admission, I set aside my own fatigue and reset my efforts."
    "*Schlick..! Schlick...!*"
    "I retraced every part of Mina I had already grown confidently familiar with and plumbed her depths with the desperation of a man whose tongue would soon fall off."
    "*Schlick..! Schlick...! Schlick!*"
    mina "{size=-10}Ha... hat....{/size=-10}"
    mct "(C'mon! Cum for me!)"
    "*Schlick..! Schlick...!*"

    if toughness >= 24:
        mct "(One last time for me you dirty cunt!)"
    else:
        mct "(One last time!)"

    "*Schlick..! Schlick...! Schlick!*"
    mina "O-oh... ah...! Heut...!"
    mct "(Cum your damn brains out!)"
    mina "Eyyeehh....♥"
    stop music
    play sound "sound effects/record-scratch.wav"
    scene w2_5389 with flash
    with flash
    mina "--!"
    "It was to the point and with a whimper, but by no means weak."
    mina "Aaaah... eh... ohh... h,hha...!"
    "Mina's body tensed up and shook, her dangling feet kicked, and her face glazed over in dumb pleasure."
    scene w2_5390 with fade
    "Pulling back, I admired my work."
    "Her thighs quivered and her cunt was a mess with saliva and girl juices."
    mina "Hattta, haaat..."
    "Her beautiful demeanor was demolished. Her mouth dumbly hung open with tongue perched on her lips, spit pooling on the bedsheets that cushioned her dead weight."
    mina "Ha... ha..."
    "The blonde hair she was so proud of matted to her forehead from sweat."
    scene w2_5391 with dissolve
    mina "Oh, no.. m-move away..."
    mc "Huh--"
    $ renpy.music.set_volume(.1, 0, channel = "sound")
    play sound "sound effects/urine-ground.wav"
    scene w2_5392 with dissolve
    mina "Ah...!"
    "With a cute cry, a stream of girl-lube-diluted clear urine trickled from Mina's urethral opening."
    mina "Haaat... haat...♥"
    mct "(Holy shit.)"
    "It lasted only for a brief window, but yep, she definitely..."
    stop sound
    $ renpy.music.set_volume(1, 0, channel = "sound")
    scene w2_5393 with dissolve
    mina "Oh, no...!"
    scene w2_5394 with dissolve
    mina "Eyee... c-can't believe Eyve... I c-couldn't... c-control... it was just... oh, no..."
    mina "I've ruined it... haven't I? Eyhee, ha... killed the mood."
    scene w2_5395 with dissolve
    mina "S-stupid. So, so stupid..."
    mina "You must think I'm disgusting..."
    scene w2_5396 with dissolve
    mc "Disgusting...? Are you kidding?"
    "It felt so good that she peed herself? That's prime fodder for my dumb fucking ego!"
    mc "Let me show you how \"disgusted\" I am..."
    scene black with fade
    play sound "sound effects/zipper.wav"
    "*Ziiiip*"
    scene w2_5397 with fade
    mc "Does this read \"disgusted\" to you?"
    mina "A-ah... w-woah..."
    "Exposing my swollen cock to the air was a pleasure in and of itself. It had strained so long to get out that it was dyed scarlet and throbbing for something warm and wet to take its frustration out on."
    scene w2_5398 with dissolve
    mc "No, I'm so fucking turned on right now and it's all due to you."
    "In a situation like this, it would take a lot more than a little pee to turn me off a girl like Mina."
    scene w2_5399 with dissolve
    mina "Ha... y-yeah..."
    scene w2_5398 with dissolve
    "Make that a fuck ton more with the look she was presently giving me."
    scene w2_5399 with dissolve
    mina "{size=-10}Because of me...{/size=-10}"
    "......"
    "..."
    scene w2_5400 with dissolve
    mina "Um..."
    play sound "sound effects/thud-floor.mp3"
    scene w2_5401 with vpunch
    mina "Ah...!"
    "She tried to move forward, but stumbled."
    scene w2_5402 with dissolve
    mina "C'mere... I'll, ha..."
    mina "I'll take care of you..."
    play music "music/ob1.ogg"
    scene w2_5403 with dissolve
    "I honestly doubted what good she'd be in this state, but I positioned myself above her."
    "The sight of my ugly dick so close to Mina's beautiful face had my stomach sickeningly turn over with desire."
    scene w2_5404 with dissolve
    mina "Haat...!"
    "To my horny satisfaction, the blonde didn't just reach out and grab my pole, instead she bunched her nose and gave it a cute and nut-bustingly lewd whiff."
    scene w2_5405 with dissolve
    mina "{size=-10}Because of me... h-huh...{/size=-10}"
    scene w2_5406 with dissolve
    "Mina adorably looking up at me with her big green eyes filled me with a singular, all-consuming desire..."

    menu:
        "(Bully) Encourage her to get an even better whiff.":
            "The desire to bully."
            mc "How do I smell?"
            scene w2_5407 with dissolve
            mina "Um..."
            "The correct answer would be \"not good\". It was a summer day, and with travel, it had been about five or so hours since my last shower..."
            "The more precise and colorful answer would be \"like sweaty balls\", but yet Mina looked conflicted."
            scene w2_5408 with dissolve
            mina "I... {b}like{/b} it."
            scene w2_5407 with dissolve
            mc "...for real?"
            scene w2_5408 with dissolve
            mina "Y-yeah... it smells... {b}manly{/b}."
            scene w2_5407 with dissolve
            "Honestly, I couldn't decide if she was just being indulgent or if odors were truly a sexual trigger of hers. The lewd expression on her face did make it look like she was being genuine, however..."
            scene w2_5409 with dissolve
            mc "Give it another whiff then."
            mina "Uh...?"
            scene minasniff_a with dissolve
            show minasniff
            mina "--Oooh, oh!"
            mc "{b}Smell it!{/b}"
            "With a gentle, but firm grip on her hair... I guided her face on an impact course with my dick."
            mina "Umpfh...! Umpfh...!"
            mct "(That's right, smell my balls bitch!)"
            mc "Drink it all in!"
            scene w2_5410 with dissolve
            mina "Ummh, fwaah...♥"
            mct "(Holy crap, she wasn't just pillow talking.)"
            "The dumb look on her face radiated sex."
            scene w2_5411 with dissolve
            mina "Haat...♥"
            scene w2_5412 with dissolve
            mc "You really surprise the hell out of me."
            scene w2_5411 with dissolve
            mina "Ah... I s-should..."
        "(Affection) Maximum pats.":

            scene w2_5413 with dissolve
            "The desire to place my hand on her flaxen-colored scalp and pat the bitch for all I'm worth."
            mc "You're so damn cute, you know that?"
            scene w2_5414 with dissolve
            mina "...h-huh? I mean, yeah... I kinda... I count on that in my daily life..."
            scene w2_5415 with dissolve
            mc "No. I mean {b}really{/b} damn cute. Maybe the cutest."
            scene w2_5417 with dissolve
            "This girl confused the hell out of me, but an amalgamation of those emotions resulted in one thing: an outpouring of affection in this moment."
            scene w2_5416 with dissolve
            mina "Eheh..."
            scene w2_5417 with dissolve
            "An earnest smile peeked out from behind her sexily exhausted expression. That was a strong point of hers."
            "The way she reacted to compliments was the best."
            scene w2_5418 with dissolve
            mina "Eheh... stop being weird. You've got your dick in my face!"
            mina "Speaking of which..."

    scene w2_5419 with dissolve
    mina "I'm... going to touch it now?"
    "If she had just done so, that would've been that. The fact that she posed the question, left some room..."
    "Some room to get creative. A half-tired blowjob had its appeal, but in a situation where I was so blindingly horny, I would rather..."
    scene w2_5420 with dissolve
    mc "Actually... do you mind if I take the lead?"
    scene w2_5421 with dissolve
    mina "Uh, umm..."
    mina "What do you have in mind?"
    scene black with fade
    mc "I'll show you."
    mina "H-hey, oh, --oh?"
    scene w2_5422 with fade
    "With some forceful guidance, I laid Mina back against the bed and was now sitting on her chest with my cock wedged between her ginormous milkers."
    scene w2_5423 with dissolve
    mina "You want to use my..."
    scene w2_5424 with dissolve
    mc "Yup."
    scene w2_5425 with dissolve
    mina "O-okay, if that's what you want..."
    mina "It makes me feel bad that you're doing all the work though..."
    scene w2_5426 with dissolve
    "The damnable thing about Mina was she really meant what she just said. She had a genuine look of concern on her face, like she was worried about coming off as self-centered."
    scene w2_5427 with dissolve
    mc "Mina..."
    mc "Don't worry about it. I'm the one being selfish right now, not you."
    scene w2_5428 with dissolve
    "She told me to carry on with a simple nod."
    scene minapai_1_a with dissolve
    show minapai1
    "A tentative thrust marked the beginning of our tit fuck, as I roughly bore my way through her cleavage to get a feel for the mechanics of the act."
    "Unlubricated as I was, pushing through her tit flesh was a somewhat grueling task - one that might've been remedied by a little spit if I wasn't wary of the crudeness of the act."
    "Instead, I decided to use a more natural lubrication process. With how turned on I was, it wouldn't be long before my precum would ooze from the tip of my dick and coat both itself and the blonde's cleavage with a beautiful shine."
    mina "Ha...♥ My heart is pounding right now..."
    "For Mina's part in this dance, she looked upward at me and peered into my head as if trying to read my thoughts, eyes clouded with a yet still growing lust."
    mina "Y-you feel it?"
    "Unsure of what to do, she awkwardly posed a silly question."
    mct "(I mean, yeah... what else can she do in this situation to feel involved?)"
    "That line of inquiry gave me an idea. Just because I was going to rut her tits end-to-end didn't mean we couldn't connect on a mental level."
    mc "Hey, Mina..."
    mina "S-sorry, I bet you want me to shut up, right? Ian says I talk too much--"
    mc "Just the opposite. I want you to... ah..."
    mc "Ah... ha, I want you to focus on me right now and tell me what you see."
    mina "Um... I mean, you're..."
    "As we spoke, the rough ride through Mina's valley became more manageable, the muggy heat from dick-on-titflesh creating a bed of perspiration for my cock to glide with."
    mc "Be expressive. Have fun with it."
    mina "I... you're..."
    scene w2_5429 with dissolve
    mina "You're fucking my chest right now..."
    scene w2_5430 with dissolve
    mc "You can be more colorful than that. I mean, I bet I have a pretty dumb look on my face right now."
    scene w2_5431 with dissolve
    mina "Ah..."
    scene w2_5432 with dissolve
    mina "Your cock is..."
    scene w2_5433 with dissolve
    mina "Your cock is fucking my breasts like it's a pussy!"
    scene minapai_2_a with dissolve
    show minapai2
    mct "(Ha!)"
    "I had no idea why it was so satisfying for a woman to state the obvious during sex, but hearing lewd words in Mina's girly voice certainly did something for me."
    mina "Your fat dick is snug between my tits and you... you look like an animal right now!"
    mc "I'm like this {b}because of you{/b}, Mina."
    mina "...and the smell! Your dick smells so.. so... {b}musky{/b}! {b}Manly!{/b}"
    mc "You like the smell of dick, you dirty bitch?"
    mina "Ha... haat! I do! I've fantasized about it..."
    mina "I've fantasized about a lot of things... so many dirty things..."
    "Mina's thought turned inward as her face beamed a gloriously lewd expression to my eyeballs."
    mina "Ah, how I want to do {b}everything{/b}..."
    mc "Tell me about it. {b}In detail{/b}."
    "What came next was an outpouring of sexual fantasies the likes I'd never imagined from the bubbly actress."
    mina "I... want to know what it feels like to be tied up and fucked without mercy..."
    mc "Yeah, what else?"
    mina "I want to know what it feels like to tie someone else up and fuck {b}them{/b} senseless."
    mc "Both of those are, -ah! P-pretty easy to do, you know..."
    mina "I want to have sex outdoors, where anyone can see...! I want to be treated and loved like a puppy dog!"
    mina "I want men to worship my feet...! And I also want to be used like dirt...!"
    "Mina, caught up with her own soul-searching, continued with a shocking number of fantasies."
    mina "I want to have a threesome...! I want to be {b}overwhelmed with sex{/b}! To live and breathe it, to not be able to get the burly smell of dick and cum out of my hair!"
    mc "Ha...!"
    mct "(That's, uh... {b}wow!{/b})"
    "--she wasn't finished."

    if Mina_BiCurious >= 2:
        mina "I want to have sex with a woman! I want to have my cunt eaten out by someone getting smashed from behind!"

    mina "I want to choke on a dick until I'm red in the face and can't breathe!"
    mina "I want to have my hair pulled and my face slapped, I want to dance naked for my lover, and eat off his naked body...!"
    "By this point, I wasn't even in the equation. She was looking past me, lost in her own little world. That was, until..."
    mina "Most importantly, I want someone I can trust! To do those things with!"
    scene minapai_3_a with dissolve
    show minapai3
    mc "Ack... M-mina...!"
    mina "That's right! I'm dirty! I'm a filthy, fucking dirty bitch and... ha...! ...and your dick is like this because of me!"
    mina "It's big... grotesque... veiny... it's so hot between my breasts..."
    mina "Keep fucking my tits until you explode, you lucky nerd! Give me all that gooey cock-juice!"
    "Mina looked at me with confidence unbound, with a fierce expression bereft of her usual people-pleasing pretenses."
    "Did I finally, {i}truly{/i} get a glimpse of what was inside her head?"
    mc "Ah...! Y-yes, ma'am!"
    "*Sclick, schlick...!*"
    "The urge to bust my nut was all-consuming. I had practically blue-balled myself earlier and now my ball sack was cooking up what might just be the biggest load of my life."
    "With great urgency and need, I rutted the carnivorous succubus' rack, staring down at the same set of bottomless green eyes that started all of this."
    mc "Ha... hnng...!"
    "*Sllick, fwhick, fwhick...!*"
    "Those unfathomably unending green pools of lust...!"
    mc "Ah, fuck...!"
    "I might just drown in them!"

    menu:
        "Make a mess!":
            $ w2MinaMess = True
            "She said she wanted to be unable to get the smell of dick and jizz out of her hair? Well, careful what you ask for!"
            stop music
            play sound "sound effects/spurt.wav"
            scene w2_5434 with flash
            mc "--!"
            "I came."
            mc "G'aaah-!"
            play sound "sound effects/spurt.wav"
            scene w2_5435 with flash
            "I came... So. Damn. Hard."
            "Rope after rope pushed itself out of my urethra with leg-bucking intensity, splashing down on the devilish blonde's chin with what I could've sworn was an audible {b}smack{/b}."
            mc "Ah, ha... ha! F~uuu~uuck me!"
            play sound "sound effects/spurt.wav"
            scene w2_5436 with flash
            "By the time I came to my senses and I had regained focus, the sight before me was a magnificently rancid and beautiful one."
            scene w2_5437 with dissolve
            mina "Ghyuuu, ew...!"
            scene w2_5436 with dissolve
            "Globs and chunks of cum caked the adorable blonde's face, turning her cute visage into something wholly unrecognizable."
            scene w2_5437 with dissolve
            mina "Thwhooick...!"
            scene w2_5436 with dissolve
            "So thick that it impeded even her ability to speak..."
            mct "(Why do I feel so damn proud right now?)"
            scene w2_5437 with dissolve
            mina "Haalp! Cheeen, ghettt aye hand?"
            scene w2_5438 with dissolve
            mc "Ah, s-shit...! Don't try and open your eyes, I'll...!"
            scene black with fade
            stop music fadeout 3.0
            if not persistent.w2MinaMindBlown:
                play sound "sound effects/notification.wav"
                show memoryunlock with dissolve
                $ renpy.pause(3, hard=True)
                $ persistent.w2MinaMindBlown = True
                hide memoryunlock with dissolve
                $ renpy.pause(0.5, hard=True)
            "......"
            "..."
            $ renpy.end_replay()
            jump w2MinaAftercare
        "Roughly feed it to her!":

            "Somewhere in her unending landscape of fantasies, she said she wanted to be treated rough... well, that idea suited me just fine as I felt my impending release draw near."
            scene w2_5439 with dissolve
            mina "H-huh...?"
            mc "Open your mouth!"
            mina "Uh..."
            scene w2_5440 with dissolve
            mina "Oh!"
            mc "Stick out your fucking tongue!"
            mina "Y-yes, d-Daddy!"
            scene w2_5441 with dissolve
            mina "Ah...!"
            mct "(Daddy?)"
            "Mina did as I asked, sluttily rolling her cute pink tongue out of her mouth and exposing her throat to me."
            scene w2_5442 with dissolve
            mc "Ah..."
            "A few seconds of jerking while looking down at Mina's stupid face was all I needed to get me there."
            mc "Open wide, pervert!"
            scene w2_5443 with dissolve
            mina "G-guh?!"
            mc "That \"gooey cock-juice\" is going straight down your beautiful throat!"
            play sound "sound effects/spurt.wav"
            scene w2_5444 with flash
            mc "--Nggh!"
            "For a split second, as rope after rope of jizz was pushed through my urethra, my sight and hearing turned off."
            "All I could feel was Mina's hands digging into my thighs and the panicked sputtering and flickering of her tongue as the biggest load of my life was directly deposited into her stomach."
            play sound "sound effects/spurt.wav"
            scene w2_5445 with flash
            mina "*Cough!* *Cough*!"
            "Mina herself did her best to adjust and accept my selfish desire, but her throat wasn't as welcoming to the sudden invasion."
            mc "Ah, suck it all down, you dirty bitch!"
            play sound "sound effects/spurt.wav"
            scene w2_5446 with flash
            mina "*Cough!* *Cough!"
            mct "(You want to be treated like dirt? Like a dog?)"
            "I'd happily oblige!"
            scene w2_5447 with dissolve
            mina "*Cough!* *Cough!"
            mc "Don't spill a drop, you perverted cunt!"
            "With one last push, I wedged my dick as deep as it would go into the back of her tight throat and let it milk me to my very last drop. The way it gripped my shaft was pure bliss!"
            mc "Ah..."
            scene w2_5448 with dissolve
            "Spent, my hand unconsciously found its way to Mina's crown and gave it a well-deserved pat."
            mc "Ah... good girl."
            scene w2_5449 with dissolve
            mc "That was... wow."
            mina "Eyeh..."
            mc "Thank you, Mina."
            scene black with fade
            stop music fadeout 3.0
            if not persistent.w2MinaMindBlown:
                play sound "sound effects/notification.wav"
                show memoryunlock with dissolve
                $ renpy.pause(3, hard=True)
                $ persistent.w2MinaMindBlown = True
                hide memoryunlock with dissolve
                $ renpy.pause(0.5, hard=True)
            "......"
            "..."
            $ renpy.end_replay()
            jump w2MinaAftercare

label w2MinaAftercare:

    play music "music/inner-light.ogg"
    scene w2_5450 with wet
    "Everything had happened so quickly, but in the time that followed, I didn't contemplate the implications of what we had done."
    scene w2_5451 with dissolve
    "Instead, I concerned myself with the worn-out woman in front of me. I carried the wobbly blonde to the bathroom and helped her clean the dried semen off her face."
    "As of yet, Mina hadn't said much, but..."
    scene w2_5452 with dissolve
    mina "...it's funny."
    scene w2_5451 with dissolve
    "I continued to wash her hair and patiently waited for her to explain."
    scene w2_5452 with dissolve
    mina "Haat... you're so gentle and caring right now, but ten minutes ago... you..."
    scene w2_5453 with dissolve
    "*Chomp!*"
    scene w2_5454 with dissolve
    mina "You ate me up. Ha...!"
    "I didn't know what to say, so Mina filled my empty response with a nervous giggle."
    scene w2_5455 with dissolve
    mina "Truthfully, I had hoped something would happen between us today, but I didn't expect you to be so... {b}aggressive{/b}."
    "She would be right under normal circumstances, but I suppose my experience in the last few weeks had emboldened me."
    scene w2_5456 with dissolve
    mc "Well, what man could resist a line so smooth like..."
    mc "{i}W-want to feel how heavy they are?{/i}"
    scene w2_5457 with dissolve
    mina "Heeeey! Don't make fun of me, jerk!"
    scene w2_5458 with dissolve
    mc "Sorry. I meant to say {i}what man wouldn't seize the chance to be with a woman like you?{/i}"
    mc "I'm quite the \"lucky nerd\", aren't I?"
    scene w2_5459 with dissolve
    mina "Ah...! I didn't mean that, that was just the heat of the moment..."
    scene w2_5460 with dissolve
    mc "It's okay, I'm just teasing you."
    mct "(It's also true as fuck.)"
    scene w2_5461 with dissolve

    if w2MinaMess == True:
        mina "Mmmh...! No teasing for at least a day after you rudely jizz on my face, okay?!"
    else:
        mina "Mmmh...! No teasing for at least a day after you rudely shove your dick down my throat, okay?!"

    mc "That a standing rule?"
    scene w2_5462 with dissolve
    mina "Y-yes...?"
    scene w2_5463 with dissolve
    "*Smooch!*"
    mc "I'm sorry."
    scene w2_5464 with dissolve
    mina "Ah, well..."
    mina "I don't {b}actually{/b} mind."
    mc "Good. I wasn't {i}actually{/i} sorry."
    mina "Hehe~! Ah..."
    scene w2_5465 with dissolve
    mc "So..."
    mina "Hmmm?"
    mc "What was the deal with that list, by the way? Was that all made up?"
    mc "If not, do you still need help with... {i}whatever{/i}?"
    scene w2_5466 with dissolve
    mina "No, it's real... pen to paper real..."
    scene w2_5467 with dissolve
    mina "{b}Well{/b}..."
    mina "Ah, you see..."
    "I idled away my time waiting for her to find the right words to explain, content to just enjoy the softness of her curves and the warmth of her body pressed into mine."
    scene w2_5466 with dissolve
    mina "We've actually just checked line item numero uno off the list."
    scene w2_5465 with dissolve
    mc "We did? That was easy."
    scene w2_5467 with dissolve
    mina "Yeah.. you know all that crap I was spewing when I was turned on? All those... {b}fantasies{/b}?"
    scene w2_5468 with dissolve
    mc "It turns out you've got quite the array of interests, huh?"
    mina "S-shut it! Those were all... true. It's a... bedroom bucket list of sorts."
    mc "...hmm, no shit?"
    scene w2_5467 with dissolve
    mina "...y-yeah."
    scene w2_5465 with dissolve
    mc "So the first one was...?"
    scene w2_5466 with dissolve
    mina "I wanted to know what it felt like to be unfaithful."
    scene w2_5467 with dissolve
    mina "I mean, what the hell is so great about it?!"
    scene w2_5468 with dissolve
    mc "Did you find your answer?"
    mina "No... even if I haven't broken up with Ian yet, I guess it's not really the same, is it?"
    "As far as I'm concerned, Mina was guiltless. Me on the other hand..."
    scene w2_5469 with dissolve
    mina "*Sigh* Honestly..."
    mina "I just enjoyed... {b}what we did{/b}, for what it was. I've, uh... mmmh..."
    scene w2_5470 with dissolve
    "Mina awkwardly spun around, kicking up bath water and bringing me face-to-tit."
    mina "I don't think it occurred to me just how lonely I've felt until right now."
    mc "Mina..."
    scene w2_5471 with dissolve
    mina "Listen, [mcf]. I'm not going to ask you to be my boyfriend, but how about something like... my lover?"
    scene w2_5472 with dissolve
    mina "God, that sounds like something from a hundred years ago, doesn't it? I can't believe I just said that!"
    mina "I m-mean, we don't have to put a label on it, but... I still have a lot of things left on my list I want to do and I'd like to do them with someone I trust, so--"

    menu:
        "Accept with a kiss.":
            $ w2MinaLovers = True
            scene w2_5473 with dissolve
            mina "Mmmh..."
            "A kiss should be a strong enough yes."
            scene w2_5474 with dissolve
            $ Mina_Relations = "Casual lovers"
            show relationmina with dissolve
            play sound "sound effects/notification.wav"
            mc "I'll introduce you to my mom as \"my lover\" then?"
            mina "E-eyh...?! I didn't mean..."
            scene w2_5475 with dissolve
            "*Chwup...!*"
            "Lovers... for some reason, the word didn't sound so bad. Almost felt like a fantasy."
            scene w2_5474 with dissolve
            mina "Ha..."
        "You'll happily help with her list.":

            scene w2_5476 with dissolve
            mc "Okay."
            scene w2_5477 with dissolve
            mina "Okay...?"
            scene w2_5478 with dissolve
            scene w2_5474 with dissolve
            $ Mina_Relations = "Fuck buddies"
            show relationmina with dissolve
            mc "Uh huh. Let's live out your fantasies, together."
            scene w2_5479 with dissolve
            "No labels seemed like a hell of a good deal to me."


    scene w2_5481 with dissolve
    mc "That stuff about feeling like a robot, though... do you really think you'll get to know yourself better by screwing around?"
    mc "I don't think you'll get what you're hoping for out of all of this."
    scene w2_5482 with dissolve
    mina "I think I might, but if I don't..."
    scene w2_5483 with dissolve
    mina "Well, you and I will have had some fun, right?"
    scene w2_5481 with dissolve
    mc "Fun..."
    scene w2_5480 with dissolve
    "My mind recounted just some of Mina's lewd fantasies. The ones that she CHOSE to share, with any number of untold possibilities left unsaid."
    "Lewd, numerous, and utterly depraved fantasies..."
    scene w2_5481 with dissolve
    mc "Yeah, there isn't anything wrong with that."
    scene w2_5480 with dissolve
    "There was only the issue of Ian..."
    "I couldn't anticipate how he might react if he found out that I was fooling around with Mina. Not that he had a leg to stand on morally speaking, but..."
    "I wouldn't put it past him to act like a kid who had his toy taken away from him."

    menu:
        "Stipulate that she should break up with Ian as soon as possible.":
            $ w2MinaPush = True

            scene w2_5478 with dissolve
            mc "You're planning on ending things with Ian, right?"
            scene w2_5479 with dissolve
            "Ian's goodwill toward me being what it was, should he find out, I could see him being fine with it if Mina and I \"just happened\" after they broke up."
            scene w2_5484 with dissolve
            mct "(It's generally in bad taste to get involved with a friend's ex, but bro code be damned, it's not like he loves Mina.)"
            scene w2_5472 with dissolve
            mina "Ah, yeah..."
            scene w2_5484 with dissolve
            "In the event he actually gives a shit, I could leverage our history together. I could make him okay with it."
            mct "(Maybe.)"
            scene w2_5472 with dissolve
            mina "I really should get that over with, shouldn't I?"
            scene w2_5485 with dissolve
            mc "You {b}need{/b} to."
            scene w2_5472 with dissolve
            mina "I will..."
            scene w2_5486 with dissolve
            mc "Before we do this again?"
            scene w2_5487 with dissolve
            "She smiled and nodded."
            scene w2_5488 with dissolve
            mina "Yeah. Like ripping a band-aid off."
            scene w2_5478 with dissolve
            mc "I don't think he's going to fight you over it."
            scene w2_5488 with dissolve
            mina "Oh, that's for certain. He's not going to give a crap."
            mina "I'm just afraid of how pissed off that's going to make me or..."
            scene w2_5489 with dissolve
            "The blonde slinked down and came to a rest on my chest."
            mina "...how much it might hurt to glimpse how little someone you thought cared about you never, truly did."
            scene w2_5490 with dissolve
            mc "It'll be alright."
            scene w2_5491 with dissolve
            "It was easy to forget that Mina was only nineteen and this was her first relationship. Despite her womanly appearance, in a lot of ways, she was still a young girl at heart."
            mina "Thanks, [mcf]."
            scene w2_5492 with dissolve
            mc "New standing rule."
            mina "Hmmm...?"

            if w2MinaMess == True:
                mc "For at least a day, you don't have to say thank you after I blow a load on your cute face, alright? "
            else:
                mc "For at least a day, you don't have to say thank you after I rudely shove my dick down your throat, alright?"

            scene w2_5493 with dissolve
            mina "J-jeez, don't be so lewd!"
            scene w2_5494 with dissolve
            mc "Oh, come on. Who are you trying to fool?"
            scene w2_5495 with dissolve
            "......"
            scene w2_5496 with dissolve
            mina "Ah..."
            scene w2_5497 with dissolve
            mina "Mmmh..."
            "Mina pulled me into a tender, affectionate kiss that I happily returned."
            scene w2_5498 with dissolve
            mina "I guess I don't get to pretend I'm so innocent anymore, huh?"
            scene w2_5499 with dissolve
        "Let her handle things at her own pace.":



            "Well, that ship has already sailed. Mina and I did what we did and I wouldn't change that even if I could."
            scene w2_5478 with dissolve
            mc "Let's do that. Let's have some fun together."
            scene w2_5479 with dissolve
            "I enjoyed having her in my arms and I refuse to give that up out of fear of that jerk getting his feelings hurt."
            scene w2_5478 with dissolve
            mc "I only have one question though."
            scene w2_5488 with dissolve
            mina "Yeah...?"
            scene w2_5478 with dissolve
            mc "Next time... should I worship your feet or should I treat you like a dog?"
            scene w2_5500 with dissolve
            mina "Those were just some examples! They're not all like that!"
            scene w2_5501 with dissolve
            mc "Hah!"
            "The thought of Mina writing all those dirty things down, by hand and in detail, was a profoundly funny image to me."
            mina "What the heck is so funny?"
            scene w2_5502 with dissolve
            mc "Nothing, just..."


    "Come what may, I was glad to have met you, Mina."
    scene black with fade
    stop music fadeout 3.0
    "Should it even just be for a brief length of time, and for a most nebulous reason, the thought of being with her soothed me on the inside."
    "......"
    "..."
    jump w2June12End

label w2MinaLetDown:

    play music "music/inner-light.ogg"
    scene w2_5506 with dissolve
    show screen textbox2 with dissolve
    mina "Ah, crap..."
    "I felt bad about rejecting her, on multiple levels, but..."
    scene w2_5507 with dissolve
    mc "I don't think that'll help sort out your feelings."
    scene w2_5508 with dissolve
    mina "..."
    scene w2_5509 with dissolve
    mina "Am I not attractive?"
    scene w2_5510 with dissolve
    mc "Seriously? you're a model, idiot. You have your face plastered on a giant magazine cover hanging in your room."
    scene w2_5509 with dissolve
    mina "No, I just mean... am I not attractive... {i}sexually{/i}? Why else would Ian cheat on me?"
    mina "I was so sure you'd... I mean, it's not like all the touching when you helped me during rehearsal was innocent, y'know?"
    scene w2_5511 with dissolve
    mc "I ignored {b}a lot{/b} of instincts right then."
    scene w2_5512 with dissolve
    mina "Then why?"
    scene w2_5513 with dissolve
    mc "It's kinda weird being so candid about this..."
    scene w2_5514 with dissolve
    mina "You're the one who made it that way."
    scene w2_5513 with dissolve
    mc "Fair enough. It's just that..."
    $ renpy.music.set_volume(.05, 0, channel = "ambient")
    play ambient "sound effects/ringing-inbound.wav"
    "*Ring, ring*"
    "The faint sound of a cell phone could be heard from behind Mina's bedroom door."
    scene w2_5515 with dissolve
    mc "Are you going to get that?"
    scene w2_5516 with dissolve
    mina "It's just my brother making sure I got in safe. I'll call him back in a minute."
    mina "Finish what you were saying. It's just what?"
    stop ambient fadeout 3.0
    scene w2_5517 with dissolve
    "It's just..."
    hide screen textbox2 with dissolve

    menu:
        "She's your friend and it would be a mistake."(chg=["mina_up"]):
            $ Mina_Affection +=1
            show screen textbox2 with dissolve
            mc "You're my friend."
            scene w2_5518 with dissolve
            mina "Yeah, so...?"
            scene w2_5517 with dissolve
            mc "So I like that and prefer it to being a fucking rebound or revenge lay, okay?"
            scene w2_5518 with dissolve
            mina "You misunderstand, it's.... because I trust you and n-not... it has nothing to do with getting..."
            scene w2_5519 with dissolve
            $ renpy.music.set_volume(1, 0, channel = "ambient")
            mina "It has nothing to do with getting even, seriously..."
            mina "Ah... that's not very freakin' convincing, but it's true."
            scene w2_5520 with dissolve
            "Mina looked pretty fucking genuine right now and my mind went back to our conversation from yesterday, about her feeling like a robot and wanting to get some experience."
            "That's when things clicked into place in no certain terms."
            mc "Sorry, I shouldn't have assumed. Still..."
            scene w2_5521 with dissolve
            "I gave her back an obnoxiously friendly slap."
            mc "That's a short road, if you know what I mean."
            scene w2_5520 with dissolve
            "Seriously. I'm no better than Ian and not just because we hold the same job. In some ways, I might even be worse."
            mc "I'd prefer something more substantial."
            scene w2_5522 with dissolve
            mina "Ha...!"
            scene w2_5523 with dissolve
            mina "You're \"friend zoning\" me?"
            scene w2_5524 with dissolve
            mc "Yeah, kinda."
            mc "Feels pretty good, to be honest."
            scene w2_5525 with dissolve
            mina "Jerk...!"
            scene w2_5529 with dissolve
            "I didn't want things to be weird, but that was a tall order..."
        "Despite his many flaws, Ian is your bro"(chg=["killian_up"]):

            $ Killian_Bromance += 1
            show screen textbox2 with dissolve
            mc "Not that he doesn't have it coming, but Ian's been my friend for over a decade."
            scene w2_5519 with dissolve
            mina "Oh..."
            scene w2_5520 with dissolve
            mc "I don't have many of those to begin with and none for nearly that long."
            scene w2_5522 with dissolve
            mina "I'm sorry. I'm awful, aren't I?"
            mina "I shouldn't have tried to put you in this position..."
            $ renpy.music.set_volume(1, 0, channel = "ambient")
            scene w2_5521 with dissolve
            mc "Oh, come on. Don't be. It's a big boost for my ego."
            "Frustratingly enough, I suspected that I only had the willpower to turn her down thanks to being knee-deep in sex because of the club."
            scene w2_5519 with dissolve
            mina "I feel so stupid, though..."
            scene w2_5520 with dissolve
            mc "You feel stupid, how do you think I feel? Turning down a beautiful woman because of THAT asshole?"
            scene w2_5529 with dissolve
            mc "I'll take it to my death bed."
            scene w2_5526 with dissolve
            mina "Ha...! You really are stupid, just not in the way you think."
            scene w2_5529 with dissolve
            "I was pleased to see she could laugh in this situation."
            scene w2_5518 with dissolve
            mina "Hmm... I don't know what I was thinking here, I just... I don't have a lot of experience with men."
            scene w2_5519 with dissolve
            mina "Guess I was... trying to fast-track some or something..."
            scene w2_5520 with dissolve
            mc "I'm going to be frank. You don't really need a point of comparison to know you should break up with someone who treats you like trash."
            scene w2_5526 with dissolve
            mina "Heh. So you're turning me down because of Ian and now you're telling me to also break up with him?"
            scene w2_5527 with dissolve
            mc "Two completely unrelated things, numbskull."
            scene w2_5528 with dissolve
            mina "Hmpfh...!"
            mina "You have no idea how frustrating you are."
            mc "Eh, I have an inkling."
            "I am patting her head like she's a kid."
            scene w2_5529 with dissolve
            mc "So..."
            "I didn't want things to be weird, but that was a tall order..."

    mct "(What to do...?)"
    "The only comfort I can offer I guess."
    scene w2_5530 with dissolve
    mc "Go get changed into something comfortable. That's an order."
    mina "Huh, why...?"
    scene w2_5531 with dissolve
    mc "I'm going to cook us some dinner and then we're going to watch a movie. Something dumb and loud, just like you like, right?"
    scene w2_5532 with dissolve
    "......"
    "..."
    scene w2_5533 with dissolve
    mina "You think I want to have dinner with a man that rejected me?"
    scene w2_5534 with dissolve
    mc "Well, I was hoping..."
    mina "Jeez..."
    scene w2_5535 with dissolve
    mina "You have NO idea how frustrating you are."
    mina "...but it's kinda refreshing, to be honest. Fine."
    stop music fadeout 3.0
    scene black with fade
    mina "Let's pretend I'm not a dunce - super comfy it is."
    scene w2_5536 with blinds
    "So I set to task, feeling a little dumb, but also like I wasn't just some dumb animal."
    mct "(Okay, maybe REALLY dumb...)"
    scene w2_5537 with circlewipe
    mina "This... is good?"
    mc "Why is everyone always surprised about that?"
    "Still, I liked Mina and a night like this felt cozy and comfortable. I had no regrets turning her down."
    scene w2_5538 with ccirclewipe
    mina "I know I told you I like stupid action movies, but this..."
    scene w2_5540 with dissolve
    mina "Never mind, this is flippin' great!"
    "Friends."
    scene w2_5539 with dissolve
    play sound "sound effects/big-explosion.mp3"
    "I don't have very many of those."
    scene black with fade
    "......"
    "..."


label w2June12End:
    play sound "sound effects/door-open.wav"
    scene w2_5541 with blinds
    $ date = "june12night"
    show june12night with squares
    mct "(Damn, what a week...)"

    if minaFlag == True and minaCheat == True and  w2MinaPush == True:
        $ history_mina = "The sexual tension between us came to a head, resulting in Mina and I having a bit of fun. Afterward, I encouraged her to break up with Ian and she told me about a sordid list of things she'd like to try in the bedroom."
        $ unread_mina = True

    if minaFlag == True and minaCheat == True and  w2MinaPush == False:
        $ history_mina = "The sexual tension between us came to a head, resulting in Mina and I having a bit of fun. Come whatever happens between her and Ian, Mina did tell me about a sordid list of things she'd like to try in the bedroom..."
        $ unread_mina = True

    if minaFlag == True and minaCheat == False and  w2MinaPush == False:
        $ history_mina = "In the wake of Ian's brazen infidelity, Mina looked to me for physical comfort and I could offer none. Still, I hope that we'll remain friends and I'll continue to see her."
        $ unread_mina = True

    hide june12night with dissolve
    play sound "sound effects/notification.wav"
    show bioupdate with dissolve


    "I got home to an empty, lifeless apartment. With her toothbrush gone, it seemed Hana did indeed go back to her mom's."

    play sound "sound effects/door-open.wav"
    scene w2_5542 with dissolve
    "*Sigh*"
    mct "(It's good that they made up, but why do I feel so glum?)"
    scene w2_5543 with dissolve
    "...maybe it would be nice to live with somebody?"
    mct "(...like a roommate?)"
    play music "music/ill-remember-you.ogg"
    scene w2_5544 with dissolve
    mct "(Yeah, no!)"
    "I shouldn't conflate how nice it was having a hot girl live with me for a few days with someone constantly invading my privacy."
    scene w2_5545 with dissolve
    mct "(Having someone around most of the time would be annoying.)"
    "...right?"
    scene w2_5546 with dissolve
    "......"
    "..."
    scene w2_5547 with dissolve
    mct "(What about a girlfriend...?)"
    "Someone to have and hold? Someone to share how my day went that isn't my mother."
    mct "(What am I thinking? Sex is falling from the sky now!)"
    scene w2_5545 with dissolve
    "...{b}Impossible{/b}."

    if minaFlag == True:

        if minaCheat == True:
            "The thought is only in my head because of how cozy it felt to be with Mina."
        else:
            "The thought is probably only in my head because Mina put it there..."

    "My job makes it impossible to be monogamous."

    mct "(Besides, do I really want that kind of relationship?)"
    "One where I lie and cheat?"
    scene w2_5547 with dissolve
    "I wish I remembered what my mom and dad were like together. She speaks so lovingly and fondly of him, in contrast with the sparse other examples of a \"normal relationship\" I can think of."
    mct "(I'd love to have that as a template, but...)"
    "I can't help but wonder if death doesn't color your memories of a person."
    scene w2_5548 with dissolve
    mct "(Why am I thinking about all this useless crap...? It's because...)"
    "Rosalind, Veronica, Felicia, Hana, and Mina... it was annoying, but interacting with them has shone a spotlight on something I lacked."
    "*Sigh*"
    mct "(Was I happy before this, living in a small and insular world? Am I happy now?)"
    mc "Bleugh..."
    "Pointless questions posed from the prerogative of someone in a comfortable enough situation to idly stare a hole in their own navel all day."
    scene w2_5549 with dissolve
    mc "Hmm..."
    "......"
    scene w2_5550 with dissolve
    "..."
    "Should I... call someone?"
    hide screen textbox2 with dissolve
    scene w2_5549 with dissolve
    $ mod_var = False
    menu:
        "[mod_option] Call all":
            $ mod_var = True
            jump mod_w2June12call_1
        "Call Hana.":

            label mod_w2June12call_1:
            scene w2_5551 with dissolve
            show screen textbox2 with dissolve
            "Friends do call each other to talk."
            mct "(...I think.)"
            scene black with fade
            play sound "sound effects/ringing-outbound.mp3"
            "*Ring, ring*"
            stop sound
            scene w2_5552 with fade
            hana "*click* What's up?"
            scene w2_5553 with dissolve
            mc "I'm uh... just calling to talk I guess. You're back at your mom's, right?"
            scene w2_5552 with dissolve
            hana "Awww, you miss me?"
            scene w2_5554 with dissolve
            woman "Is that a boy?"
            scene w2_5555 with dissolve
            mc "A little. I got used to having you walk around half-naked, I guess."
            scene w2_5554 with dissolve
            woman "Oh, is that where you've been? You should bring him--"
            scene w2_5556 with dissolve
            hana "Shush! I'm on the phone!"
            scene w2_5557 with dissolve
            hana "Anyway, that's kind of fuckin' weird, right?"
            scene w2_5558 with dissolve
            mc "What do you mean? Friends call each other right?"
            scene w2_5557 with dissolve
            hana "No. No, they don't."
            scene w2_5559 with dissolve
            hana "You don't have any friends, do you? People don't call each other. They {b}text{/b}."
            scene w2_5558 with dissolve
            mc "So, I should hang up then...?"
            scene w2_5560 with dissolve
            hana "N-no, I didn't say that. I'm not doing anything."
            scene w2_5561 with dissolve
            hana "Let's talk. How are you?"
            scene w2_5562 with dissolve
            mc "Feeling a little antsy about the exhibition tomorrow - less than I did last week, but I still don't know what the hell is going to happen."
            scene w2_5564 with dissolve
            mc "Bet I'm going to have to get my dick out in front of some old men again."
            scene w2_5563 with dissolve
            hana "Ha! Yeah, me too. The old woman had the idea that I should sit in on tomorrow's show. Thinks it's a good start in showing August that I have an interest in the business."
            scene w2_5562 with dissolve
            mc "Just by watching?"
            scene w2_5563 with dissolve
            hana "Well, uh... she wants me to judge."
            scene w2_5564 with dissolve
            mc "...are you okay with that?"
            scene w2_5563 with dissolve
            hana "Let's move off this topic."
            scene w2_5562 with dissolve
            mc "What do you want to talk about?"
            scene w2_5563 with dissolve
            hana "It occurs to me I know nothing about your musical taste."
            scene w2_5562 with dissolve
            mc "I like a bit of everything."
            scene w2_5563 with dissolve
            hana "Ugh! That is the worst answer!"
            hana "Do you know Pitfall of My Own Miserable Making?"
            scene w2_5562 with dissolve
            mc "No..."
            scene w2_5563 with dissolve
            hana "What about Him's Debaucherous Debacle?"
            scene w2_5564 with dissolve
            mc "...are these bands?"
            scene w2_5586 with dissolve
            hana "Oh, man! I've got some shit you need to listen to!"
            "Like this, Hana and I talked for an hour. I knew not a single band of hers and she shared none of my limited interests, but it was... nice."
            scene w2_5565 with fade
            "It was very nice."
            "Eventually though, the drowsiness prevailed."
            hana "Night, [mcf]."
            stop music fadeout 3.0
            scene w2_5566 with dissolve
            mc "Good night..."
            scene w2_5567 with dissolve
            "....."
            if mod_var:
                "Next call"
                if minaFlag and minaCheat:
                    jump mod_w2June12call_2
                else:
                    jump mod_w2June12call_3
            scene w2_5568 with dissolve
            "...sleep took hold, bringing me into tomorrow."
            scene black with fade
            "To a day that made the first week's exhibition look like light fun."

        "Call Mina." if minaFlag == True and minaCheat == True:
            label mod_w2June12call_2:
            scene w2_5551 with dissolve
            show screen textbox2 with dissolve
            "I just saw her, but..."
            mct "(Giving a girl a call is normal, right?)"
            scene black with fade
            "There's no point in overthinking this. I should do what I want."
            play sound "sound effects/ringing-outbound.mp3"
            "*Ring, ring*"
            stop sound
            scene w2_5569 with dissolve
            mina "H-hey...!"
            scene w2_5570 with dissolve
            mc "Bad time?"
            scene w2_5571 with dissolve
            mina "Uh, n-no... I was just..."
            scene w2_5572 with dissolve
            mina "I was just winding down before bed."
            scene w2_5573 with dissolve
            mc "I see..."
            scene w2_5574 with dissolve
            mina "What's on your mind?"
            scene w2_5573 with dissolve
            mc "I got home to an empty apartment and felt like calling someone."
            scene w2_5574 with dissolve
            mina "Heh, that so?"
            scene w2_5562 with dissolve
            mc "I've never called someone on the phone before just to talk, but I thought... you and I are..."
            scene w2_5563 with dissolve
            mina "Never? That's so weird! I talk all the time to Felicia."
            scene w2_5562 with dissolve
            mc "Just her?"
            scene w2_5563 with dissolve
            mina "Eh, well, I'm not so good with having \"girl friends\" if you know what I mean..."
            "I had no clue."
            scene w2_5564 with dissolve
            mc "I find that surprising. You're so friendly."
            scene w2_5563 with dissolve
            mina "It can come off as fake..."
            "Okay, I had a clue."
            mina "So, anyway. Let's chat! Tell me about your studies!"
            scene w2_5562 with dissolve
            mc "That stuff is boring."
            scene w2_5586 with dissolve
            mina "I want to know!"
            "It felt like she truly did."
            scene w2_5585 with dissolve
            mc "Well, okay..."
            "Mina and I talked until we were both about asleep. We talked about all sorts of things - about my first love, about doctors and medicine, and even on how to string a bow."
            scene w2_5565 with dissolve
            "It was a quick hour."
            "Eventually though, the drowsiness prevailed."
            stop music fadeout 3.0
            scene w2_5566 with dissolve
            mc "Good night, Mina."
            scene w2_5565 with dissolve
            mina "Ha... good night [mcf]."
            scene w2_5567 with dissolve
            if mod_var:
                "Next call"
                jump mod_w2June12call_3
            "....."
            scene w2_5568 with dissolve
            "...sleep took hold, bringing me into tomorrow."
            scene black with fade
            "To a day that made the first week's exhibition look like light fun."
        "Call Mom.":

            label mod_w2June12call_3:
            scene w2_5551 with dissolve
            show screen textbox2 with dissolve
            "I haven't talked to my mom in a few days..."
            scene black with fade
            mct "(I should really give her a call.)"
            play sound "sound effects/ringing-outbound.mp3"
            "*Ring, ring...*"
            stop sound
            scene w2_5575 with dissolve
            vic "My favorite son! What do I owe the pleasure?"
            scene w2_5576 with dissolve
            vic "Don't you have anything better to do on a Friday night than call your mom?"
            scene w2_5577 with dissolve
            mc "Ouch. That hurts coming from you of all people. How's your social book looking?"
            scene w2_5578 with dissolve
            vic "Full. I'm spending a hot and heavy night with a ruggedly handsome good book."
            scene w2_5577 with dissolve
            mc "Don't say things in that kind of voice..."
            scene w2_5576 with dissolve
            vic "Ha! How are you, [mcf]? How's Hana?"
            scene w2_5577 with dissolve
            mc "We're not dating."
            scene w2_5575 with dissolve
            vic "I didn't say that did I? I just asked how that lovely, way-out-of-your-league girl was doing."
            scene w2_5576 with dissolve
            vic "I'm definitely not saying you should strike while the iron's hot..."
            scene w2_5564 with dissolve
            mc "Good thing I took everything literally or I might be getting conflicting signals here."
            scene w2_5563 with dissolve
            vic "Sorry. Am I being too pushy?"
            scene w2_5562 with dissolve
            mc "Nah, I mean... you're right that I'm at home on a summer's Friday night."
            scene w2_5563 with dissolve
            "Obviously not going to mention how active my afternoons have been every single day this week."
            vic "I just don't want your 20s to be all work, work, work. I was with your father when I was your age."
            scene w2_5562 with dissolve
            mc "How did you and dad meet?"
            scene w2_5563 with dissolve
            vic "You've heard that story."
            scene w2_5562 with dissolve
            mc "I know. I'd like to hear it again though."
            scene w2_5563 with dissolve
            vic "Hmpfh, alright..."
            "So she told me the story and more, replete with other tales of how sweet my father could be and how big his dreams were."
            "The subject was bittersweet, but my mother's stories were the only connection I had with my father."
            stop music fadeout 3.0
            "Eventually though..."
            scene w2_5565 with dissolve
            vic "Good night, hun. Sleep tight."
            scene w2_5567 with dissolve
            if mod_var:
                $ mod_var = False
                "Next call"
                jump mod_w2June12call_4
            "....."
            scene w2_5568 with dissolve
            "...sleep took hold, bringing me into tomorrow."
            scene black with fade
            "To a day that made the first week's exhibition look like light fun."
        "Call Ian.":

            label mod_w2June12call_4:
            stop music fadeout 3.0
            scene w2_5551 with dissolve
            show screen textbox2 with dissolve
            "It's not like my contact list is bursting with options..."
            play sound "sound effects/ringing-outbound.mp3"
            scene black with fade
            "*Ring, ring...*"
            stop sound
            scene w2_5579 with dissolve
            play music "music/hotshot.ogg"
            kil "[mcf]!"

            if killianHeadsUp == True:
                kil "I can't believe you're calling me twice in twenty-four hours. What's up?"
            else:
                kil "It's weird for you to call me out of the blue. What's up?"

            scene w2_5580 with dissolve
            mc "I dunno. Just kinda wanted to talk to somebody and you're like my only friend, sadly."
            scene w2_5581 with dissolve
            kil "Shit, {b}really{/b}? Are you feeling okay?"
            scene w2_5582 with dissolve
            mc "What's that supposed to mean?"
            scene w2_5581 with dissolve
            kil "Don't make me look like I'm the one being the jerk, you're the unsociable cunt between the two of us."
            kil "You didn't get any bad news today, did you? You've never called me to just quote unquote talk."
            scene w2_5582 with dissolve
            mc "Oh, fuck off. This was a mistake, I'm hanging--"
            scene w2_5583 with dissolve
            kil "Wait, wait, wait...! What do you want to talk about?"
            scene w2_5580 with dissolve
            mc "Nothing in particular. I guess I'm just bored."
            scene w2_5579 with dissolve
            kil "Want to come over and play some games then?"
            scene w2_5580 with dissolve
            mc "Sorry. Too tired."
            scene w2_5563 with dissolve
            kil "Alright, conversation it is!"

            if killianHeadsUp == True and minaFlag == True:
                kil "So... how did things go with you and Mina today?"

                if minaCheat == True:
                    scene w2_5584 with dissolve
                    mct "(Uh... shit.)"
                    "Don't say fucking your soon-to-be ex-girlfriend. {b}Don't say fucking your soon-to-be ex-girlfriend."
                    scene w2_5564 with dissolve
                    mc "We went..."

                scene w2_5562 with dissolve
                mc "We went to the arcade with her brother. He said you two have met?"
                scene w2_5563 with dissolve
                kil "Yeah, that dork? He's a bit..."
                scene w2_5564 with dissolve
                mc "Like you as a kid?"
                scene w2_5563 with dissolve
                kil "Yeah, exactly. It kinda pisses me off to look at him."
                scene w2_5585 with dissolve
                mc "That is refreshingly, yet painfully honest."
                scene w2_5563 with dissolve
                kil "Did Mina seem in high spirits?"

                if minaCheat == True:
                    scene w2_5584 with dissolve
                    mct "(Uh... double shit.)"
                    "Don't say {i}does cumming her brains out qualify as high spirits?{/i}"

                scene w2_5564 with dissolve
                mc "As high as you can expect I guess."
                scene w2_5563 with dissolve
                kil "*Sigh* Ah, shit..."
                scene w2_5562 with dissolve
                mc "Let's not talk about this anymore."
                scene w2_5563 with dissolve
                kil "Good idea..."

            scene w2_5564 with dissolve
            mc "Did you see that new preview for Dying Dogma 4?"
            scene w2_5563 with dissolve
            kil "Those games haven't been any good since the first one, dude."
            scene w2_5585 with dissolve
            mc "Yeah, but... keep hope alive. The first one was so good!"
            scene w2_5586 with dissolve
            kil "Ha! Keep hoping!"
            "We talked for an hour, of nothing substantial and across many frivolous topics."
            "That sort of inanity was actually nice. Junk food conversation can be just what a person needs from time to time."
            stop music fadeout 3.0
            scene w2_5565 with dissolve
            "Eventually though, drowsiness prevailed."
            kil "Night, dude. See you tomorrow."
            scene w2_5566 with dissolve
            mc "Yeah, see you tomorrow..."
            scene w2_5567 with dissolve
            "....."
            scene w2_5568 with dissolve
            "...and sleep took hold, bringing me into tomorrow."
            scene black with fade
            "To a day that made the first week's exhibition look like light fun."

    play music "music/leaving-home.ogg"
    scene w2_5587 with snake
    "......"
    "..."
    scene w2_5588 with dissolve
    sophia "It's been seven days and there's been no notable change in tolerance levels."
    scene w2_5589 with dissolve
    abel "No adjustment required, {b}at all{/b}?"
    scene w2_5588 with dissolve
    sophia "None, sir."
    scene w2_5590 with dissolve
    kat "That's good news?"
    scene w2_5591 with dissolve
    abel "Very. The terribly diminishing effect was our biggest hurdle."
    scene w2_5590 with dissolve
    kat "I'm glad you're happy."
    scene w2_5592 with dissolve
    abel "You've been very accommodating Kathleen, but I think your choice of locale is rather brazen. Do the other two really not mind your... hospitality?"
    scene w2_5593 with dissolve
    kat "Charles... well, that pervert likes to watch and if you know where someone is looking..."
    scene w2_5594 with dissolve
    kat "You can easily slip things by their blind spots."
    scene w2_5592 with dissolve
    abel "And what about the gangster?"
    scene w2_5593 with dissolve
    kat "Eventually, he'll get curious and come looking, but for now the club is being paid."
    scene w2_5595 with dissolve
    kat "Once he does discover what's going on underneath his nose, he'll no doubt raise a {b}major{/b} issue with it."
    scene w2_5596 with dissolve
    abel "Then are you sure it's wise to conduct the tests here?"
    scene w2_5597 with dissolve
    kat "I insist on it. {b}Here is perfect{/b}. It's easier to capsize a ship when you have a wave to break it against."
    kat "Don't tell me {i}the{/i} Abel Van Doren is concerned?"
    scene w2_5598 with dissolve
    abel "Not at all. I'm untouchable. You, however..."
    scene w2_5599 with dissolve
    kat "Don't worry about me. As it is, this place is too mundane and boring."
    scene w2_5600 with dissolve
    kat "I'll stake my life on making it more... enriching."
    scene w2_5601 with dissolve
    woman "{size=-10}Gyuhh... Eyll be guud... j-jjuust...{/size=-10}"
    scene w2_5602 with dissolve
    abel "Hmmfph. Very well then."
    scene w2_5603 with dissolve
    abel "It disgusts me, but shortsighted bitches like you have their use."
    scene black with fade
    stop music fadeout 3.0
    kat "Happy to be of use, sir."
    "......"
    "..."
    jump June13Start
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
